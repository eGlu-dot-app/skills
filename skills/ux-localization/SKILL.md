---
name: ux-localization
description: Translate, localize, adapt, or review UX writing (buttons, menus, labels, errors, toasts, empty states, dialogs, onboarding, paywalls, notifications, in-product AI copy) between English (en-US, en-GB), French (fr-FR), German (de-DE), Spanish (es-ES, es-419), Korean (ko-KR), Japanese (ja-JP), Simplified Chinese (zh-Hans-CN) and Traditional Chinese (zh-Hant-TW). Use this skill whenever the user asks to translate or localize app or web copy, string files (JSON, XLIFF, .strings, ICU messages), Figma text or a UI glossary; to check a translation for translationese (번역투), inconsistent terms, register or regional mistakes; or to convert en-US copy to en-GB, es-ES to es-419, or zh-CN to zh-TW, even if the user never says "localization".
---

# UX localization

Translate interface text so that each locale says the same thing about the same product behavior, in the form a native product writer would use. The job is meaning and behavior first, then natural language, then consistency, then fit on screen. A fluent string that changes what a button does is a failure; a slightly stiff string that is accurate is a fixable style issue.

Everything bundled here (terms, examples, defaults) is a **proposed** editorial baseline, not an approved product glossary and not native-reviewed. Say so when you deliver, and let an existing product glossary or style guide override it.

## Supported locales

| Tag | Language and market | Reference file | Proposed default address |
|---|---|---|---|
| en-US | English, United States | `references/locales/en.md` | "you", contractions allowed |
| en-GB | English, United Kingdom | `references/locales/en.md` | same as en-US; spelling and vocabulary differ |
| fr-FR | French, France | `references/locales/fr-FR.md` | vous |
| de-DE | German, Germany | `references/locales/de-DE.md` | Sie (du only when the brand uses it) |
| es-ES | Spanish, Spain | `references/locales/es.md` | tú (usted for formal or regulated contexts) |
| es-419 | Spanish, Latin America | `references/locales/es.md` | tú (usted for formal or regulated contexts) |
| ko-KR | Korean, South Korea | `references/locales/ko-KR.md` | 합니다체 for sentences; requests as -해 주십시오 (set as the default) |
| ja-JP | Japanese, Japan | `references/locales/ja-JP.md` | です・ます for sentences |
| zh-Hans-CN | Simplified Chinese, mainland China | `references/locales/zh.md` | 你 or 您, decided per product |
| zh-Hant-TW | Traditional Chinese, Taiwan | `references/locales/zh.md` | 你 or 您, decided per product |

The register defaults are proposals, except Korean 합니다체, which is a chosen default. If the product already has a register, use it and say so in the notes. Never mix registers inside one product surface.

Out of scope for now: fr-CA, fr-CH, de-AT, de-CH, es-US, zh-HK, zh-MO, zh-SG, en-AU and other markets. Do not apply a neighboring locale's rules to them automatically (Taiwan terms are not Hong Kong terms; France spacing is not Quebec spacing). If asked for one, say it is outside the reviewed scope and mark the output accordingly. Use `en-GB`, not `en-UK`: the region subtag for the United Kingdom is GB.

## Workflow

### 1. Collect context

What you need for each string or batch:

- Target locale and market
- Where the text appears (button, menu, title, body, toast, error, status, placeholder, tooltip, accessible name, notification)
- What actually happens: the object, the current state, and the result of the action
- Length limits and what they count (characters, display width, bytes)
- Placeholders, markup, brand and product names, values that must not change
- Existing product glossary, style guide, register, and casing rules

Do not interrogate the user for every string. Proceed with what you can determine, and ask only when a missing fact would change the meaning: deletion scope or permanence, who has permission, when billing happens, who can see something, who must act. When working unattended, take the most likely reading, say which reading you took, and flag the string.

### 2. Normalize the source into concepts

- Map each string to a concept in `references/glossary.csv` (search it by English term or concept ID; do not load the whole file into your reply).
- Prefer the established platform term over a literal translation (ALL-19). Glossary cells were checked against Chrome, Android and Firefox; the `evidence` column says how well each one matches. For a word not in the glossary, search `references/platform-evidence.csv` by English label before writing your own term, and say in the notes when a term has no platform evidence.
- English source text often varies words for one concept ("remove", "delete", "erase" for the same action). Resolve the variation to one concept and one target term. Do not reproduce the variation in the target.
- One English word can hold several concepts ("Cancel" an operation, a subscription, an order; "Apply" settings vs "apply" for a job; "Free" as no cost vs available). Split them. `references/pairs.md` has a table of high-risk English words.
- If the same English string means two things in two places, it needs two keys.
- If a string contains an inline action ("{fileName} deleted. Undo"), split the message and the action into separate keys.
- Check the source itself. If it states a cause the product cannot confirm, lacks a plural ("{days} days"), or is built by concatenation, translate faithfully, fix the structure where the target grammar requires it, and list the defect under **Source issues** (ALL-18).

### 3. Load only the references you need

| Need | Read |
|---|---|
| Term for a concept, allowed variants and short forms (`variants` column), platform evidence (`evidence` column), context limits | `references/glossary.csv`, then `references/glossary-notes.md` section named in the `notes` column |
| A UI word not in the glossary | `references/platform-evidence.csv` (search the English label) |
| Rules that apply to every language (state, scope, variables, plurals, accessibility, IME, review levels) | `references/universal-rules.md` |
| Grammar, register, typography and common mistakes of the target | `references/locales/<file>.md` |
| Mistakes specific to the translation direction (for example EN to KO, KO to EN, zh-CN to zh-TW) | the matching section of `references/pairs.md` |
| Numbers, dates, times, currency, lists, plural categories | `references/formats.md` |
| Where a claim comes from | `references/sources.md` |

### 4. Translate whole messages by meaning

- Write the complete message the target language needs; do not assemble fragments in English word order.
- Preserve state and result: in progress, done, failed, not yet done, not possible, partially done.
- Preserve modality and scope: must, can, may, only, except, at least, up to, all, some.
- Preserve the actor: the user, an admin, the owner, the system.
- Do not add what the source does not say: causes, recovery steps, permanence, refunds, guarantees, apologies, extra politeness.
- Do not drop what the source does say to make the string shorter.
- Buttons name the action ("Delete", not "Yes"). Confirmation dialogs pair a specific action with Cancel.
- Keep one term per concept across the product. Repetition is correct in UI text; synonyms read as different features.
- Keep placeholders and markup intact. Reorder them freely; never translate placeholder names.
- Use ICU `plural` and `select` (or the platform equivalent) instead of string concatenation, with the plural categories the target locale needs (`references/formats.md`).

### 5. Label where each rule comes from

Every choice you note comes from one of three places. Label it in the notes:

- **Language rule**: French spacing before `?`, Spanish `¿`, Korean particles, German noun capitals.
- **Product setting**: register, sentence case, Oxford comma, exclamation marks, no em or en dashes, no emojis. These belong to the product or the person you work for.
- **Legal requirement**: statutory button labels such as BGB § 312k and § 312j in Germany, or the EU order-button rule (`glossary-notes.md`, billing). Legal labels are not shortened or reworded by translation; a shorter version goes to legal as a question.

Never present a product setting or a legal requirement as a grammar rule, or the reverse.

### 6. Check

Run the checker on every batch of more than a few strings. If the strings were pasted into the conversation, write them to a CSV first.

- CSV or TSV columns: `key, source, target`, plus optional `locale` (needed when one file holds several locales) and `max_length`. One row per key per locale.
- JSON: pass `--source` and `--target` files (nested keys are joined with dots) and one `--locale`.
- Run with the path to the script; the avoid list is found automatically.

```bash
python3 <skill-dir>/scripts/lint_strings.py --table strings.csv
python3 <skill-dir>/scripts/lint_strings.py --table strings.csv --locale fr-FR --length-unit width
python3 <skill-dir>/scripts/lint_strings.py --source en.json --target de.json --locale de-DE --no-dashes --no-emoji
```

It finds candidates: placeholder and tag mismatches, missing plural categories, punctuation and spacing per rendered plural branch, branches that end differently, Simplified and Traditional mixing, terms in `avoid-terms.csv`, possibly untranslated strings, length over `max_length` (per rendered branch; `--length-unit chars|graphemes|width|bytes`), source strings with a count but no plural, and optional dash and emoji checks. Treat findings as candidates to confirm in context, not as verdicts.

Then review by hand against `universal-rules.md` and the locale file. Read each string as the user would see it on the screen, next to its button or title.

### 7. Deliver

For a batch, use this table. Add the Locale column when the batch has more than one target locale, and sort by key, then locale, so one key's translations sit together.

| Key | Locale | Source | Target | Notes | Status |
|---|---|---|---|---|---|

- Notes: assumptions, rule IDs applied (for example `KO-05`, `ALL-08`, `ENDE-04`), and whether a choice is a language rule, product setting or legal requirement.
- Status: `proposed` for everything you write. Only a reviewer moves it forward (see below).
- Short versions: if a length limit forces one, add a row with the key suffix `#short` (`button.cancel_sub#short`), and say in Notes what the short version loses. A short version may not drop scope, conditions, warnings or legal wording.
- New keys you had to create (for example a split-off toast action) are marked "new key" in Notes.

After the table, add these lists (omit a list when it is empty):

- **Needs product check**: strings whose meaning depends on behavior you could not confirm (deletion permanence, billing timing, permissions, who sees what, what a length limit counts), plus legal questions.
- **Source issues**: defects in the source text (ALL-18), with a suggested fix for the source.
- **Checker findings left open**: candidates you judged acceptable, with one line each on why.

For a single string, give the target and at most one line of note.

For a review of an existing translation, report by severity: meaning errors, data errors (placeholders, numbers, links), language errors, consistency, style suggestions, implementation issues. See the severity table in `universal-rules.md`.

## Review status

`proposed` → `linguistically_reviewed` → `product_verified` → `approved`

A string that a native linguist reviewed is not yet verified against product behavior. Never mark your own output beyond `proposed`.

## Bundled files

- `references/glossary.csv`: 198 concepts across all 10 locales, with concept IDs, UI context, definitions, variants, short forms and platform evidence
- `references/platform-evidence.csv`: how Chrome, Android and Firefox translate each concept's English label, per locale, with counts
- `references/glossary-notes.md`: context limits, variants, collisions and legal anchors per concept
- `references/avoid-terms.csv`: machine-readable "avoid in this locale" list used by the checker
- `references/universal-rules.md`: cross-language rules, message patterns, accessibility, IME, review levels
- `references/formats.md`: number, date, time, currency, list and plural behavior per locale (generated from ICU 78.3 / CLDR 48)
- `references/locales/*.md`: per-language characteristics, typography, common mistakes, worked examples
- `references/pairs.md`: direction-specific mistakes and false friends
- `references/sources.md`: sources, what each one supports, and the change log
- `scripts/lint_strings.py`: candidate checker (Python 3 standard library only)
