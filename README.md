# eGlu skills

[![skills.sh](https://skills.sh/b/eGlu-browser/skills)](https://skills.sh/eGlu-browser/skills)

Agent skills for Claude Code, Claude.ai and other agents that read `SKILL.md`.

| Skill | What it does |
|---|---|
| [ux-localization](skills/ux-localization/SKILL.md) | Translates and reviews UX writing (buttons, errors, toasts, dialogs, onboarding, AI copy) across en-US, en-GB, fr-FR, de-DE, es-ES, es-419, ko-KR, ja-JP, zh-Hans-CN and zh-Hant-TW |

## Install

With the [skills CLI](https://github.com/vercel-labs/skills) (Node.js 22.20 or later):

```bash
npx skills add eGlu-browser/skills --skill ux-localization
```

Add `-g` to install for all projects, or `-a claude-code` to pick the agent.

Manual install for Claude Code: copy `skills/ux-localization` into `~/.claude/skills/` (all projects) or `.claude/skills/` (one project).

## ux-localization

- **Workflow:** collect context, map strings to concepts, translate whole messages by meaning, check, and deliver a table with notes, a "Needs product check" list and a "Source issues" list
- **Glossary:** 198 concepts in 10 locales, each checked against the shipped translations of Chrome, Android and Firefox (`references/glossary.csv`, `references/platform-evidence.csv`)
- **Per-language guidance:** characteristics, typography, common mistakes and worked examples (`references/locales/`)
- **Direction-specific mistakes:** for example EN to KO translationese, KO to EN 확인 → "Confirm", zh-CN to zh-TW vocabulary, false friends across Korean, Japanese and Chinese (`references/pairs.md`)
- **Checker:** `scripts/lint_strings.py` finds candidate problems in CSV, TSV or JSON string files: placeholders, ICU plural categories, locale punctuation, Simplified and Traditional mixing, register, literal translations, length

```bash
python3 skills/ux-localization/scripts/lint_strings.py --table strings.csv --locale fr-FR
```

### Defaults

- Korean sentences use 합니다체 (requests as -해 주십시오). Change the default in `references/locales/ko-KR.md` and run the checker with `--ko-register haeyo` if your product uses 해요체.
- All terms and examples are marked `proposed`. They have not been reviewed by native speakers. A product's own glossary and style guide take priority.

## Sources and attribution

Sources for typography, formats, accessibility and legal labels are listed in `skills/ux-localization/references/sources.md`.

`platform-evidence.csv` quotes short UI terms, with counts, from:

- Chromium, BSD-3-Clause, https://github.com/chromium/chromium
- Android Open Source Project, Apache-2.0, https://github.com/aosp-mirror
- Mozilla Firefox and firefox-l10n, MPL-2.0, https://github.com/mozilla-firefox/firefox and https://github.com/mozilla-l10n/firefox-l10n

These products' terms are used as evidence of current usage. The glossary does not copy their translation catalogs.

## License

MIT. See [LICENSE](LICENSE). Quoted platform terms in `platform-evidence.csv` remain under their original licenses listed above.
