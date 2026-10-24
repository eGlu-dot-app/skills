# Universal rules

Rules that apply to every target locale. Locale files add language-specific rules; `pairs.md` adds direction-specific ones.

## Contents

1. Principles
2. Cross-language mistakes (ALL-01 to ALL-19)
3. Message patterns that preserve state and result
4. Destructive actions and undo
5. AI actions
6. Placeholders, variables and protected values
7. Plurals and counts
8. Text input and IME
9. Accessibility text
10. Layout and length
11. Review severity
12. What a checker can find vs what needs a person
13. Data model for a product glossary

## 1. Principles

- Translate the concept and the product behavior, not the English words.
- English is the comparison language, not the sentence template. Do not force English structure on any target.
- Repetition of one term is correct in UI text. Synonym variety reads as different features.
- Use the term users already know from their platform before a literal translation (ALL-19). A literal translation of an established term reads as a different feature.
- Add nothing the source and the product do not support. Drop nothing that changes scope, conditions, or warnings.
- Language rules and product style settings are different things. Record which one you applied.
  - Language rule examples: French space before `?`, Spanish `¿`, Korean particle choice, German noun capitalization.
  - Product setting examples: register (vous/tu, Sie/du, 해요체/합니다체), sentence case, Oxford comma, ellipsis on loading states, no em or en dashes, no emojis.
  - Using 존댓말 does not by itself mean 해요체; 합니다체 is also 존댓말. The same applies to other registers: decide the product default and keep it within each message type.

## 2. Cross-language mistakes

Formerly `CJK-01` to `CJK-10` in the CJK reference v0.2; they apply to every locale.

| ID | Category | Avoid | Do |
|---|---|---|---|
| ALL-01 | Meaning | Translating "Pending" as "processing" everywhere | Check which: waiting to run, waiting for review, waiting for payment |
| ALL-02 | Meaning | Translating "Available" as "usable" everywhere | Separate remaining storage, bookable time slots, feature availability |
| ALL-03 | Meaning | Translating "Disabled" as "unavailable" everywhere | Separate turned off by the user, blocked by permission, temporarily down |
| ALL-04 | Meaning | Adding "Check your internet connection" when no cause is known | State only the known error and the actions that actually work |
| ALL-05 | Meaning | Translating destructive confirmations as Yes / No | Name the action on the confirm button (Delete) and pair it with Cancel |
| ALL-06 | Meaning | Translating "Subscription canceled" as "Refund complete" | Show subscription state and refund state separately |
| ALL-07 | Meaning | Rendering must, can, may with the same strength | Decide obligation, ability, permission or likelihood, then keep its strength |
| ALL-08 | Meaning | Dropping only, except, at least, up to | Keep ranges, exceptions, minimums and maximums |
| ALL-09 | Style | Cutting the object or scope to make a label short | Read the button with its surrounding text; cut only what is redundant there |
| ALL-10 | Accessibility | Translating the visible label but leaving the accessible name in English | Translate accessible names; the visible label text must be contained in the accessible name [S7] |
| ALL-11 | Data | Building sentences by concatenating fragments ("Delete" + " " + item + "?") | One string per full message, with named placeholders the translator can move |
| ALL-12 | Data | Reusing one key for two meanings because the English is identical | Separate keys when the concept or UI position differs |
| ALL-13 | Meaning | Collapsing do not / cannot / not yet / failed to | Keep "did not", "is not able to", "has not yet", and "tried and failed" distinct |
| ALL-14 | Meaning | Turning a suggestion or estimate into a statement of fact | Keep hedges ("may", "about", "suggested") at the same strength |
| ALL-15 | Style | Copying English Title Case into languages that do not use it | Follow target casing; only en-US style guides commonly use title case, and that is a product choice |
| ALL-16 | Meaning | Translating an empty state as an error, or one "nothing here" message for every empty case | Separate keys: empty list, no search results, no access, failed to load |
| ALL-17 | Tone | Copying every English exclamation mark and hype word ("Upgrade now!", "Awesome!") | Keep exclamation marks and intensity only where the target product voice uses them, and never add them. Promotional tone is a product setting per locale |
| ALL-18 | Meaning | Silently "fixing" or silently copying a defect in the source (unconfirmed cause, missing plural, concatenation) | Translate faithfully, fix structure where the target grammar needs it, and report the defect under Source issues |
| ALL-19 | Term | Literal translation of a UI word that already has an established platform term (ko 책갈피 for Bookmarks, zh-Hant-TW 幫助 for Help, fr "Tab" for a browser tab) | Use the term users already see in their browser and OS: the glossary cell, checked against Chrome, Android and Firefox (`evidence` column). If a term is not in the glossary, look it up in `platform-evidence.csv` or in current products before inventing one |

## 3. Message patterns that preserve state and result

Proposed English sources and the state each one carries. Locale files give the translations.

| State | EN source | What must survive translation |
|---|---|---|
| In progress | Saving changes. | Not finished yet |
| Done | Changes saved. | Finished successfully |
| Failed | Couldn't save changes. | Attempted and failed |
| No permission | You don't have permission to edit this file. | Blocked by permission, not by a fault |
| Not created yet | No projects yet. | Empty, normal, not an error |
| Missing input | Enter a project name. | A field needs a value |
| No results | No results found. | The search ran and matched nothing |
| Confirmation | Delete this file? | Asks before acting; adds no permanence claim |

- An empty state is not an error. Keep empty list, no search results, no permission and load failure as separate keys.
- Partial success is not total failure. If some items succeeded, say how many succeeded and failed, and what can be retried, only if the product provides those numbers.
- Error messages name the object and the problem. Give a fix only when one is known and available. [S8]
- A "save failed" message for a failure event is not the same string as "saving is not available here" on a settings screen.

## 4. Destructive actions and undo

Write copy for the behavior the product actually has. Two example scenarios:

**A. Moved to trash, can be restored (confirmed)**
- Title: Move file to trash?
- Body: You can restore it from the trash.
- Primary: Move to trash
- Secondary: Cancel

**B. Permanently deleted, cannot be recovered (confirmed)**
- Title: Permanently delete file?
- Body: Deleted files can't be recovered.
- Primary: Delete permanently
- Secondary: Cancel

**C. Deleted with a short undo window (toast)**
- Message key: `toast.file_deleted` → "{fileName} deleted." (or "moved to trash." if that is what happened)
- Action key: `toast.file_deleted.action` → "Undo"
- Accessible name of the action: "Undo delete {fileName}" or equivalent, so it contains the visible "Undo" and names the object (ALL-10)
- Split the message and the inline action into separate keys. Never translate "{fileName} deleted. Undo" as one string (ALL-11).
- The message must match the behavior: "deleted" vs "moved to trash".
- Keep the undo window long enough to read and act on the translated text, which may be longer than English; how long is a product decision.
- fr-FR: "Annuler" is the standard Undo label; if a Cancel button can be visible at the same time, use "Annuler la suppression".
- de-DE: "Rückgängig machen" may not fit a toast; "Rückgängig" is a common short form.

Do not mix the scenarios. If the source only says "Delete" and the behavior is unknown, do not add "permanently" or "can be restored". Flag it under Needs product check.

## 5. AI actions

| Action | Meaning to keep |
|---|---|
| Stop generating | When it stops, and whether partial output is kept |
| Regenerate | Replaces the current result, or adds another candidate |
| Apply changes | Preview vs actual change to the document |
| Discard changes | Unapplied suggestion vs unsaved real edits |
| Revert / Undo | Scope: last action, selected change, or the whole session |
| Suggestion or estimate | Never phrased as a confirmed fact or completed work |

## 6. Placeholders, variables and protected values

- Keep placeholder names and counts exactly: `{count}`, `{fileName}`, `{date}`, `%1$s`, `%@`, `{{name}}`, HTML or XML tags.
- Placeholders may move to any position the grammar needs. Placeholder names are never translated.
- Decide first whether these are translatable: amounts, URLs, email addresses, code, IDs, real user names, product and feature names.
- Keep displayed product names and translatable feature names in separate lists.
- Grammatical agreement around a variable breaks easily:
  - Korean particles depend on the last syllable of the inserted word (을/를, 이/가, 은/는, 으로/로). Use complete per-message translations or a tested particle helper; do not apply batchim rules to English names and numbers by guesswork. Alternative layout: `삭제한 파일: {fileName}` when the information structure allows it.
  - French elision and gender: "le fichier de {name}" fails for names starting with a vowel ("d'Anna"); past participles agree with gender and number. Use ICU `select` for gender, or rephrase so the variable is not governed by an article.
  - German case and gender: "{object} wurde gelöscht" needs "Die Datei", "Der Ordner", "Das Projekt". Use one string per object type or `select`.
  - Spanish gender: "{item} eliminado" vs "eliminada". Same fix.
- Do not apply the same spacing around variables in every CJK language. Spacing between CJK and Latin text is a product typography rule; decide it per locale.
- Length limits: confirm whether they count characters, grapheme clusters, display width or bytes. Never assume a translation fits.

## 7. Plurals and counts

- Use ICU plural (or the platform equivalent) and provide every category the target locale uses, including `many` for French and Spanish even when the count is unlikely to reach millions. It costs one line and removes the question. Category lists per locale are in `formats.md`.
- If the source has a count next to a plural noun without a plural block ("{days} days"), the source is defective for count = 1. Add the plural block the target grammar needs and report the source defect (see SKILL.md, Source issues).
- English has `one` and `other`. French and Spanish add `many` (used for exact large round numbers such as 1,000,000). German has `one` and `other`. Korean, Japanese and Chinese have only `other`. [S6] [S18]
- A single category does not mean the language has no plural meaning; it means the number does not change the word form. Do not split CJK strings into one/other copies for no grammatical reason.
- French uses the singular for 0 and 1 ("0 fichier", "1 fichier"). English, German and Spanish use the plural for 0.
- A separate zero message (`=0`) is a product decision for a different empty-state UX, not a grammar requirement.
- Counters: Chinese and Japanese need the right measure word or counter for the object (3 个文件 / 3 個檔案 / ファイル3件). Korean uses counters too (파일 3개).
- Keep exact counts and compact counts (1.2K) apart. Billing amounts and limits need a decision on rounding and abbreviation.

## 8. Text input and IME

An input method editor (IME) composes characters or converts phonetic input into characters. Composition is a separate state from committed text; the W3C UI Events spec defines composition events for it. [S9]

These are implementation checks, not translation fixes. Flag them as implementation issues:

- Pressing Enter to confirm Hangul composition or Japanese/Chinese conversion must not also submit the form.
- Do not show a format error or truncate text while it is still being composed.
- Validate and search on committed text, not on intermediate composition text.
- Do not forbid CJK characters in name or address fields without a real reason. If some characters or formats are not supported, say which and why.
- Decide full-width and half-width normalization per field. Never normalize user names, passwords or codes silently.
- Accented Latin input (é, ß, ñ) also needs testing in names, search and sorting; do not strip diacritics in stored values.

## 9. Accessibility text

- Review visible labels, accessible names, tooltips, error text and alt text together.
- The accessible name contains the visible label text. Example: visible "Delete", accessible name "Delete file". [S7]
- Describe the action, not the icon shape ("Delete file", not "Trash can icon").
- Link text states the destination or purpose; avoid "Click here".
- Do not identify errors by color alone. Name the field and the problem in text. [S8]
- After translating visible and screen reader text separately, check they still describe the same action.
- Set the correct language tag on content (`lang="zh-Hant-TW"`, `lang="ja"`) so screen readers pronounce it and fonts render the regional glyphs. [S4] [S10]

## 10. Layout and length

- German and French strings are often noticeably longer than English; Spanish too. Test real translations in the real component width; do not rely on a fixed expansion percentage.
- CJK strings are often shorter in characters but each glyph is wider. Count display width, not characters.
- German compounds create long unbreakable words. Allow hyphenation (`hyphens: auto` with the correct `lang`) or a soft hyphen in fixed components.
- Japanese and Chinese need line-break rules for punctuation (kinsoku): some marks may not start or end a line. Check rendered output. [S2] [S3]
- Korean uses spaces between words; Japanese and Chinese body text does not. Do not apply Korean spacing rules to Japanese or Chinese. [S1] [S5]
- One Unicode Han character can need a different glyph shape in each region. Use the correct language tag and a regional font. [S4]
- Do not apply one line length, font or character limit to all CJK languages because they are "CJK".
- Truncation and ellipsis decisions use the translated text, the real width and the real font.

## 11. Review severity

| Level | Examples | Handling |
|---|---|---|
| Meaning error | Delete vs remove confusion; permission scope changed; billing timing changed | Must fix before approval |
| Data error | Missing variable; amount changed; broken URL; wrong plural category | Must fix before approval |
| Language error | Wrong particle, wrong character, broken grammar, missing accent | Fix with context |
| Consistency | Several terms for one concept; register mixed | Compare against approved glossary and style |
| Style suggestion | Shorter toast; unnecessary possessive | Decide by product tone and screen context |
| Implementation | Submit during IME composition; truncation; missing accessible name | Log as a design or engineering issue |

Score accuracy, naturalness, consistency and fit separately. One combined score hides meaning errors.

## 12. What a checker can find vs what needs a person

| Candidate for automatic checks | Needs a person |
|---|---|
| Placeholder names and counts kept | Whether a particle or article fits the inserted value |
| Protected strings unchanged | Which brand and feature names are translated |
| Approved "avoid" terms present | Exceptions where the same word has a different meaning |
| Mixed Simplified and Traditional characters | Intentional mixing in names, quotes, brands |
| Punctuation and spacing patterns | Exceptions in code, URLs, times |
| Length over a defined limit | Real line breaks, truncation, readability |
| Numbers and currency values kept | Counters, ranges, billing cycles |
| Accessible names missing | How it sounds in a screen reader |

A finding from a checker is a candidate. Confirm it in context before calling it an error.

## 13. Data model for a product glossary

Use these fields when the user wants to turn this baseline into their own glossary or TMS import.

Term entry:
- `concept_id`: meaning-based ID, not an English word
- `definition`: actual product behavior
- `ui_context`: button, menu, title, body, error, status, and so on
- `locales`: preferred term per locale
- `allowed_variants`: allowed alternatives and their contexts
- `avoid_in_context`: terms to avoid in a specific context
- `examples`: full messages per locale
- `provenance`: written in-house or imported
- `source_url`, `source_revision`, `source_license`: for imported entries
- `review_status`: proposed, linguistically_reviewed, product_verified, approved
- `reviewer`, `reviewed_at`

Mistake rule:
- `rule_id` (for example KO-03), `locale`, `category` (grammar, meaning, term, style, regional, layout), `severity`, `trigger_context`, `before`, `after`, `exceptions`, `rationale`, `review_status`

Before importing terms from another product's translations, check source, version and license, and keep the imported wording separate from your own recommendation. When an approved translation already exists, compare against it first, but do not keep a meaning error or an outdated behavior description just because it was approved.
