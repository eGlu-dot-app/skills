#!/usr/bin/env python3
"""Candidate checker for translated UI strings.

Finds patterns worth a human look: placeholder and tag mismatches, missing ICU
plural categories, locale punctuation and spacing (checked per rendered plural
or select branch), branches that end differently, Simplified/Traditional mixing,
terms listed in avoid-terms.csv, possibly untranslated strings, length limits,
source strings with a count but no plural, Korean register (default 합니다체),
and (optionally) dashes and emojis.

Every finding is a candidate. Confirm it in context before calling it an error.

Usage:
  python3 lint_strings.py --table strings.csv                 (locale column in the file)
  python3 lint_strings.py --table strings.csv --locale fr-FR  (one locale for all rows)
  python3 lint_strings.py --source en.json --target de.json --locale de-DE
  python3 lint_strings.py --table strings.tsv --length-unit width --no-dashes --no-emoji --format json

Table input: CSV or TSV with columns key, source, target, and optionally
locale and max_length (one row per key per locale). JSON input: flat or nested
objects; nested keys are joined with dots. Python 3.8+, standard library only.
"""

import argparse
import csv
import json
import os
import re
import sys
import unicodedata
from collections import Counter

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_AVOID = os.path.join(SCRIPT_DIR, "..", "references", "avoid-terms.csv")

# CLDR cardinal plural categories (CLDR 48 data, checked with ICU 78.3).
PLURAL_CATEGORIES = {
    "en": {"one", "other"},
    "fr": {"one", "many", "other"},
    "de": {"one", "other"},
    "es": {"one", "many", "other"},
    "ko": {"other"},
    "ja": {"other"},
    "zh": {"other"},
}
MANY_EXAMPLE = {"fr": "1 000 000 de ...", "es-ES": "1.000.000 de ...", "es": "1,000,000 de ... (es-419) or 1.000.000 de ... (es-ES)"}

# Common UI characters that exist only in one script. Candidate list, not exhaustive.
SIMP_TRAD_PAIRS = (
    "们們 这這 个個 为為 说說 时時 发發 动動 设設 关關 开開 门門 问問 题題 应應 该該 删刪 "
    "复復 导導 录錄 账帳 号號 户戶 网網 络絡 软軟 视視 频頻 数數 据據 链鏈 务務 报報 错錯 "
    "误誤 页頁 载載 认認 证證 选選 择擇 项項 编編 辑輯 预預 览覽 输輸 显顯 隐隱 储儲 档檔 "
    "码碼 线線 级級 体體 资資 讯訊 节節 点點 击擊 图圖 标標 签簽 无無 权權 请請 间間 闭閉 "
    "联聯 订訂 阅閱 续續 费費 试試 败敗 过過 购購 买買 单單 进進 么麼 从從 将將 对對 与與 "
    "当當 实實 现現 还還 换換 让讓 气氣 万萬 亿億 广廣 历歷 归歸 尽盡 样樣 机機 构構 优優 "
    "欢歡 贴貼 销銷 结結 统統 计計 质質 键鍵 盘盤 绝絕 转轉 际際 类類"
)
SIMPLIFIED_ONLY = {p[0] for p in SIMP_TRAD_PAIRS.split()}
TRADITIONAL_ONLY = {p[1] for p in SIMP_TRAD_PAIRS.split()}

PH = "\u0000"  # marker for a placeholder in rendered text
EMOJI_RE = re.compile("[\U0001F000-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF️]")
DASH_RE = re.compile("[‒–—―]")
URL_RE = re.compile(r"(https?://|www\.)\S+")
PRINTF_RE = re.compile(r"%(\d+\$)?[-+ #0]*\d*(\.\d+)?[sdifgeEu@]|%@|%\([A-Za-z_]\w*\)[sd]")
DOUBLE_BRACE_RE = re.compile(r"\{\{\s*([A-Za-z_][\w.]*)\s*\}\}")
TEMPLATE_RE = re.compile(r"\$\{\s*([A-Za-z_][\w.]*)\s*\}")
TAG_RE = re.compile(r"<\s*(/?)\s*([A-Za-z][\w-]*)[^>]*?(/?)>")
TERMINAL_PUNCT = set(".?!:;…。？！：；")
MAX_VARIANTS = 64


class Finding:
    def __init__(self, locale, key, severity, rule, message, target=""):
        self.locale, self.key, self.severity, self.rule = locale, key, severity, rule
        self.message, self.target = message, target

    def as_dict(self):
        return {"locale": self.locale, "key": self.key, "severity": self.severity,
                "rule": self.rule, "message": self.message, "target": self.target}


# ---------------------------------------------------------------- ICU parsing

class ICUError(Exception):
    pass


class ICU:
    """Small ICU MessageFormat reader: argument inventory, plural/select blocks,
    and rendered variants (one per branch, placeholders replaced by a marker)."""

    def __init__(self, text):
        self.t = text
        self.n = len(text)
        self.args = Counter()
        self.blocks = []

    # -- shared helpers
    def _quoted(self, i):
        """ICU apostrophe rules. Returns (literal_text, next_index)."""
        t, n = self.t, self.n
        if i + 1 < n and t[i + 1] == "'":
            return "'", i + 2
        if i + 1 < n and t[i + 1] in "{}#|":
            j = t.find("'", i + 1)
            if j == -1:
                return t[i + 1:], n
            return t[i + 1:j], j + 1
        return "'", i + 1

    def _read_until(self, i, stops):
        j = i
        while j < self.n and self.t[j] not in stops:
            j += 1
        if j >= self.n:
            raise ICUError("unclosed '{'")
        return self.t[i:j].strip(), j

    def _skip_balanced(self, i):
        depth = 1
        while i < self.n:
            if self.t[i] == "{":
                depth += 1
            elif self.t[i] == "}":
                depth -= 1
                if depth == 0:
                    return i + 1
            i += 1
        raise ICUError("unclosed '{'")

    # -- rendering parser (also fills args and blocks)
    def render(self):
        alts, i = self._message(0, 0, False)
        if i < self.n:
            raise ICUError("unexpected '}'")
        return alts

    def _message(self, i, depth, in_plural):
        t, n = self.t, self.n
        alts, buf = [""], []

        def flush():
            nonlocal alts, buf
            if buf:
                s = "".join(buf)
                alts = [a + s for a in alts]
                buf = []

        while i < n:
            c = t[i]
            if c == "'":
                lit, i = self._quoted(i)
                buf.append(lit)
            elif c == "{":
                flush()
                sub, i = self._argument(i + 1, depth, in_plural)
                alts = [a + s for a in alts for s in sub][:MAX_VARIANTS]
            elif c == "}":
                if depth == 0:
                    raise ICUError("unexpected '}'")
                flush()
                return alts, i + 1
            elif c == "#" and in_plural:
                buf.append("1")
                i += 1
            else:
                buf.append(c)
                i += 1
        if depth > 0:
            raise ICUError("unclosed '{'")
        flush()
        return alts, i

    def _argument(self, i, depth, in_plural):
        t = self.t
        name, j = self._read_until(i, ",}")
        if not re.fullmatch(r"[A-Za-z_][\w.]*|\d+", name or ""):
            end = self._skip_balanced(i)
            return ["{" + t[i:end]], end
        self.args[name] += 1
        if t[j] == "}":
            return [PH], j + 1
        typ, j = self._read_until(j + 1, ",}")
        if typ not in ("plural", "selectordinal", "select"):
            return [PH], (self._skip_balanced(j) if t[j] == "," else j + 1)
        if t[j] == "}":
            raise ICUError(f"{typ} without options")
        j += 1
        cats, texts, alts = [], [], []
        while True:
            while j < self.n and t[j].isspace():
                j += 1
            if j >= self.n:
                raise ICUError("unclosed plural/select")
            if t[j] == "}":
                self.blocks.append({"arg": name, "type": typ, "categories": cats, "texts": texts})
                return alts[:MAX_VARIANTS], j + 1
            sel, j = self._read_until(j, "{}")
            if t[j] == "}":
                raise ICUError(f"selector '{sel}' without a branch")
            sel = re.sub(r"^offset:\s*\d+\s*", "", sel).strip()
            start = j + 1
            sub, j = self._message(start, depth + 1, in_plural or typ != "select")
            cats.append(sel)
            texts.append(t[start:j - 1])
            alts.extend(sub)


def pre_mask(text):
    """Replace non-ICU placeholders and tags before ICU parsing."""
    inv = Counter()
    for m in DOUBLE_BRACE_RE.finditer(text):
        inv["{{" + m.group(1) + "}}"] += 1
    text = DOUBLE_BRACE_RE.sub(PH, text)
    for m in TEMPLATE_RE.finditer(text):
        inv["${" + m.group(1) + "}"] += 1
    text = TEMPLATE_RE.sub(PH, text)
    for m in PRINTF_RE.finditer(text):
        inv["printf:" + m.group(0)] += 1
    text = PRINTF_RE.sub(PH, text)
    for m in TAG_RE.finditer(text):
        inv["<" + m.group(1) + m.group(2).lower() + m.group(3) + ">"] += 1
    text = TAG_RE.sub("", text)
    return text, inv


def analyze(text):
    """Return (placeholder inventory, plural blocks, rendered variants, icu_error)."""
    masked, inv = pre_mask(text)
    icu = ICU(masked)
    try:
        variants = icu.render()
        err = None
        for a in icu.args:
            inv["{" + a + "}"] += 1  # presence only: branches repeat args legitimately
    except ICUError as e:
        err = str(e)
        variants = [masked]
        for m in re.finditer(r"\{\s*([A-Za-z_][\w.]*)\s*[,}]", masked):
            inv["{" + m.group(1) + "}"] += 1
    return inv, icu.blocks, variants, err


# ---------------------------------------------------------------- helpers

def lang_of(locale):
    return locale.split("-")[0].lower()


def locale_matches(rule_locale, locale):
    rule_locale, locale = rule_locale.lower(), locale.lower()
    return locale == rule_locale or locale.startswith(rule_locale + "-")


def measure(text, unit):
    text = unicodedata.normalize("NFC", text.replace(PH, ""))
    if unit == "bytes":
        return len(text.encode("utf-8"))
    if unit == "chars":
        return len(text)
    count = 0
    for c in text:
        if unicodedata.combining(c) or c in "‍️︎":
            continue
        if unit == "width":
            count += 2 if unicodedata.east_asian_width(c) in ("W", "F") else 1
        else:
            count += 1
    return count


def terminal(s):
    s = s.replace(PH, "").rstrip()
    return s[-1] if s and s[-1] in TERMINAL_PUNCT else ""


def load_table(path, locale_default):
    delim = "\t" if path.lower().endswith((".tsv", ".tab")) else ","
    rows = []
    with open(path, newline="", encoding="utf-8-sig") as f:
        for i, r in enumerate(csv.DictReader(f, delimiter=delim), start=2):
            r = {(k or "").strip().lower(): (v if v is not None else "") for k, v in r.items()}
            if "source" not in r or "target" not in r:
                sys.exit("Table needs columns: key, source, target (optional: locale, max_length)")
            ml = (r.get("max_length") or "").strip()
            rows.append({
                "key": r.get("key") or f"row{i}",
                "source": r["source"],
                "target": r["target"],
                "locale": (r.get("locale") or locale_default or "").strip(),
                "max_length": int(ml) if ml.isdigit() else None,
            })
    return rows


def flatten(obj, prefix=""):
    out = {}
    if isinstance(obj, dict):
        for k, v in obj.items():
            out.update(flatten(v, f"{prefix}.{k}" if prefix else str(k)))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            out.update(flatten(v, f"{prefix}[{i}]"))
    elif isinstance(obj, str):
        out[prefix] = obj
    return out


def load_json_pair(src_path, tgt_path, locale):
    with open(src_path, encoding="utf-8") as f:
        src = flatten(json.load(f))
    with open(tgt_path, encoding="utf-8") as f:
        tgt = flatten(json.load(f))
    return [{"key": k, "source": src.get(k), "target": tgt.get(k), "locale": locale, "max_length": None}
            for k in sorted(set(src) | set(tgt))]


def load_avoid(path):
    rules = []
    if not path or not os.path.exists(path):
        return rules
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            try:
                rules.append({**r, "rx": re.compile(r["regex"])})
            except re.error as e:
                print(f"warning: bad regex in avoid list ({r['regex']}): {e}", file=sys.stderr)
    return rules


# ---------------------------------------------------------------- punctuation per rendered text

def punct_findings(prose, lang, loc):
    out = set()
    prose = URL_RE.sub(lambda m: PH * len(m.group(0)), prose)
    if lang == "fr":
        for i, ch in enumerate(prose):
            prev = prose[i - 1] if i > 0 else ""
            nxt = prose[i + 1] if i + 1 < len(prose) else ""
            if ch in ";!?:":
                if ch == ":" and prev.isdigit() and nxt.isdigit():
                    continue
                if prev in (PH, "") or prev in ";!?":
                    continue
                if prev == " ":
                    out.add(("warn", "FR-02", f"Regular space before '{ch}' can wrap. Use U+202F (; ! ?) or U+00A0 (:)."))
                elif prev not in (" ", " "):
                    out.add(("warn", "FR-02", f"No space before '{ch}'. European French uses a no-break space."))
            elif ch == "«" and nxt not in (" ", " "):
                out.add(("warn", "FR-12", "Opening « should be followed by a no-break space."))
            elif ch == "»" and prev not in (" ", " "):
                out.add(("warn", "FR-12", "Closing » should follow a no-break space."))
        if '"' in prose:
            out.add(("info", "FR-12", "Straight double quotes; French text normally uses « »."))
    elif lang == "de":
        if '"' in prose or re.search("“[^”“]*”", prose):
            out.add(("info", "DE-12", "English-style quotes; German uses „…“."))
    elif lang == "es":
        for close, open_ in (("?", "¿"), ("!", "¡")):
            if prose.count(close) > prose.count(open_):
                out.add(("warn", "ES-01", f"'{close}' without a matching opening '{open_}'."))
            elif prose.count(open_) > prose.count(close):
                out.add(("warn", "ES-01", f"'{open_}' without a closing '{close}'."))
    elif lang in ("ja", "zh"):
        m = re.search(r"[぀-ヿ㐀-鿿]([,.;:?!]|\.\.\.)", prose)
        if m:
            sev = "info" if (lang == "ja" and m.group(1) in "?!") else "warn"
            rule = "JA-06" if lang == "ja" else "ZHCN-05"
            out.add((sev, rule, f"ASCII '{m.group(1)}' after CJK text; use full-width punctuation in sentences."))
    return out


# ---------------------------------------------------------------- checks per row

def check_row(row, avoid_rules, opts):
    key, src, tgt, loc = row["key"], row["source"], row["target"], row["locale"]
    out = []

    def add(sev, rule, msg):
        out.append(Finding(loc, key, sev, rule, msg, tgt or ""))

    if not loc:
        add("error", "SETUP", "No target locale. Pass --locale or add a locale column.")
        return out
    lang = lang_of(loc)

    if src is None:
        add("warn", "DATA", "Key exists in target but not in source.")
        src = ""
    if tgt is None or tgt.strip() == "":
        add("error", "DATA", "Missing or empty translation.")
        return out

    s_inv, s_blocks, s_vars, s_err = analyze(src)
    t_inv, t_blocks, t_vars, t_err = analyze(tgt)

    # placeholders and ICU syntax
    if t_err:
        add("error", "ICU", f"Target ICU syntax problem: {t_err}.")
    if s_err:
        add("info", "ICU", f"Source ICU syntax problem: {s_err} (placeholder check used a fallback).")
    missing, extra = s_inv - t_inv, t_inv - s_inv
    if missing:
        add("error", "ALL-11", "Placeholder or tag missing in target: " + ", ".join(sorted(missing)))
    if extra:
        add("error", "ALL-11", "Placeholder or tag not in source: " + ", ".join(sorted(extra)))

    # plural categories and branch consistency
    required = PLURAL_CATEGORIES.get(lang)
    for b in t_blocks:
        cats = {c for c in b["categories"] if not c.startswith("=")}
        if "other" not in b["categories"]:
            add("error", "PLURAL", f"'{b['arg']}' {b['type']} has no 'other' branch.")
        if b["type"] == "plural" and required:
            miss, unused = required - cats, cats - required
            if miss:
                ex = MANY_EXAMPLE.get(loc, MANY_EXAMPLE.get(lang, ""))
                note = f" ('many' is selected for exact millions: {ex})" if "many" in miss and ex else ""
                add("warn", "PLURAL", f"'{b['arg']}' plural lacks {sorted(miss)} for {loc}{note}.")
            if unused:
                add("info", "PLURAL", f"'{b['arg']}' plural has categories {loc} never selects: {sorted(unused)}.")
        ends = {terminal(x) for x in b["texts"]}
        if len(b["texts"]) > 1 and len(ends) > 1:
            add("info", "BRANCH", f"'{b['arg']}' branches end with different punctuation: {sorted(ends)}.")

    # source-side plural defect (count placeholder followed by an English plural noun, no plural block)
    if src and not s_blocks and lang_of(opts.source_locale) == "en":
        m = re.search(r"\{\s*([A-Za-z_]\w*)\s*\}\s+[a-z]+s\b", src)
        if m:
            add("info", "ALL-18", f"Source uses '{{{m.group(1)}}}' with a plural noun but no plural block; "
                                  "wrong for 1. Report under Source issues.")

    # punctuation per rendered branch
    seen = set()
    for v in t_vars:
        for f in punct_findings(v, lang, loc):
            if f not in seen:
                seen.add(f)
                add(*f)

    # Korean register (product setting; default 합니다체)
    if lang == "ko" and opts.ko_register != "off":
        if opts.ko_register == "hamnida":
            rx, msg = re.compile(r"[\uac00-\ud7a3]요(?=[.?!]|\s*$)"), "해요체 ending in a 합니다체 product (KO-27). Use -ㅂ니다/-습니다, -하시겠습니까, -해 주십시오."
        else:
            rx, msg = re.compile(r"(니다|니까|십시오)(?=[.?!]|\s*$)"), "합니다체 ending in a 해요체 product (KO-27)."
        if any(rx.search(v) for v in t_vars):
            add("warn", "KO-27", msg)

    # Chinese script mixing
    if lang == "zh":
        is_trad = "hant" in loc.lower() or loc.lower().endswith(("-tw", "-hk", "-mo"))
        bad = sorted({c for c in tgt if c in (SIMPLIFIED_ONLY if is_trad else TRADITIONAL_ONLY)})
        if bad:
            add("warn", "ZHTW-11" if is_trad else "ZHCN-02",
                f"{'Simplified' if is_trad else 'Traditional'} characters in {loc} text: {''.join(bad)} "
                "(names, quotes and brands may mix on purpose).")

    # avoid terms
    for r in avoid_rules:
        if locale_matches(r["locale"], loc):
            m = r["rx"].search(tgt)
            if m:
                add(r["severity"], r["rule_id"], f"'{m.group(0)}': {r['note']}. Prefer: {r['prefer']}.")

    # untranslated
    if lang != "en" and src and tgt.strip() == src.strip():
        s = src.strip()
        multi = re.search(r"[A-Za-z]{3,}.*\s.*[A-Za-z]{3,}", s)
        single = re.fullmatch(r"[A-Z]?[a-z]{2,}", s)
        if multi or single:
            add("info", "DATA", "Target equals source. Untranslated, or a name that stays in English?")

    # whitespace
    if src and (src[:1].isspace() != tgt[:1].isspace() or src[-1:].isspace() != tgt[-1:].isspace()):
        add("info", "DATA", "Leading or trailing whitespace differs from source.")
    if "  " in tgt:
        add("info", "STYLE", "Double space.")

    # length, measured on rendered branches ('#' as 1, placeholders not counted)
    t_len = max(measure(v, opts.length_unit) for v in t_vars)
    if row.get("max_length") and t_len > row["max_length"]:
        add("warn", "LENGTH", f"{t_len} {opts.length_unit} in the longest rendered branch; limit is "
                              f"{row['max_length']} (placeholders not counted; confirm what the limit counts).")
    if opts.max_ratio and src:
        s_len = max(measure(v, opts.length_unit) for v in s_vars) or 1
        if t_len > opts.max_ratio * s_len:
            add("info", "LENGTH", f"Target is {t_len / s_len:.1f}x the source length; check the component width.")

    # product style settings
    if opts.no_dashes and DASH_RE.search(tgt):
        add("warn", "STYLE-DASH", "Em or en dash present (product setting). Restructure the sentence.")
    if opts.no_emoji and EMOJI_RE.search(tgt):
        add("warn", "STYLE-EMOJI", "Emoji present (product setting).")
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--table", help="CSV/TSV with key, source, target [, locale, max_length]")
    ap.add_argument("--source", help="Source JSON file")
    ap.add_argument("--target", help="Target JSON file")
    ap.add_argument("--locale", help="Target locale for all rows, e.g. fr-FR, zh-Hant-TW")
    ap.add_argument("--source-locale", default="en-US", help="Source locale (default en-US)")
    ap.add_argument("--glossary-avoid", default=DEFAULT_AVOID, help="avoid-terms.csv path ('' to disable)")
    ap.add_argument("--length-unit", choices=["chars", "graphemes", "width", "bytes"], default="graphemes",
                    help="How max_length is counted (width: East Asian wide characters count 2)")
    ap.add_argument("--max-ratio", type=float, default=None, help="Flag targets longer than N x source")
    ap.add_argument("--ko-register", choices=["hamnida", "haeyo", "off"], default="hamnida",
                    help="Korean register to enforce (product setting; default hamnida = 합니다체)")
    ap.add_argument("--no-dashes", action="store_true", help="Flag em and en dashes (product setting)")
    ap.add_argument("--no-emoji", action="store_true", help="Flag emojis (product setting)")
    ap.add_argument("--min-severity", choices=["info", "warn", "error"], default="info")
    ap.add_argument("--format", choices=["text", "json"], default="text")
    opts = ap.parse_args()

    if opts.table:
        rows = load_table(opts.table, opts.locale)
    elif opts.source and opts.target:
        if not opts.locale:
            sys.exit("--locale is required with --source/--target")
        rows = load_json_pair(opts.source, opts.target, opts.locale)
    else:
        ap.error("Use --table, or --source with --target")

    avoid = load_avoid(opts.glossary_avoid)
    rank = {"info": 0, "warn": 1, "error": 2}
    findings = [f for row in rows for f in check_row(row, avoid, opts)
                if rank[f.severity] >= rank[opts.min_severity]]

    if opts.format == "json":
        print(json.dumps([f.as_dict() for f in findings], ensure_ascii=False, indent=2))
    else:
        for f in findings:
            print(f"[{f.locale}:{f.key}] {f.severity.upper():5} {f.rule}: {f.message}")
            print(f"    target: {f.target}")
        c = Counter(f.severity for f in findings)
        print(f"\n{len(rows)} strings checked: {c.get('error', 0)} error, {c.get('warn', 0)} warn, "
              f"{c.get('info', 0)} info. Findings are candidates; confirm in context.")
    sys.exit(1 if any(f.severity == "error" for f in findings) else 0)


if __name__ == "__main__":
    main()
