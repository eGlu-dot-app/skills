# ja-JP: Japanese (Japan)

Based on the CJK UX Localization Reference v0.2 (2026-10-24), translated into English and extended. All examples are `proposed`.

## Contents

1. Scope and register
2. Language characteristics and UX implications
3. Typography and punctuation
4. Common mistakes (JA-01 to JA-17)
5. Worked examples

## 1. Scope and register

- Proposed default: です・ます for guidance, feedback, errors and confirmations.
- Buttons and menus: short action names, usually kanji nouns or katakana loanwords (保存, 削除, キャンセル), or short verb forms where natural (元に戻す, やり直す). No sentence endings on buttons.
- Use polite form without piling up honorifics. A request does not need extended keigo (JA-12).
- Do not mix です・ます and だ・である inside one type of text. Short menu labels are a separate category (JA-10).

## 2. Language characteristics and UX implications

- **Three scripts.** Kanji, hiragana and katakana are used together. Do not turn every English product term into katakana, and do not replace every established katakana term with a kanji compound.
- **Particles and sentence endings** decide the meaning of the whole sentence. Translate whole messages; do not assemble English-order noun chains.
- **No spaces between words** in normal Japanese text. Latin text, code and product names need a product rule for surrounding spaces.
- **Line-breaking rules (kinsoku).** Some punctuation may not start or end a line. Check rendered text; do not rely on character counts. [S2]
- **Ability, permission and obligation are distinct.** できます (can), してもよい (may), する必要があります (must) are not interchangeable.
- **Shared kanji is not shared meaning.** Words shared with Korean or Chinese can differ in meaning (see `pairs.md`, CJK shared characters).
- **Do not compress everything into kanji nouns.** Guidance text needs the relation between action and object; a string of kanji compounds is hard to read.
- **Katakana spelling variants** (フォルダ/フォルダー, ユーザ/ユーザー, サーバ/サーバー) are allowed variants. Pick one per product and record it; do not call the other one wrong.
- **Buttons vs sentences.** Check buttons for unneeded sentence endings separately from body text.
- **Counters.** Choose a counter per object and screen type and keep it (ファイル3件, 3個, 3つ; JA-09).

## 3. Typography and punctuation

- Sentence end: 。(full-width ideographic full stop). Comma: 、. Do not use ASCII `.` or `,` in Japanese sentences (JA-06). Code and URLs keep ASCII.
- Question and exclamation in sentences: full-width ？ and ！ are common. Question marks are often omitted after ますか in formal text; in UI confirmations, ？ is widely used. Choose a product rule.
- Quote UI labels and terms with 「」: 「保存」を選択してください。
- Use half-width for Latin letters and digits; do not use half-width katakana. Full-width Latin letters and digits are uncommon in UI text. [Convention; confirm against the product style guide.]
- No final 。 on buttons, menu items, titles or standalone labels.

## 4. Common mistakes

JA-01 to JA-11 come from the CJK reference v0.2. JA-12 to JA-17 are added. Error types to check, not frequency findings.

| ID | Type | Avoid | Prefer | Rule |
|---|---|---|---|---|
| JA-01 | Register | あなたのファイルを保存してください。 | ファイルを保存してください。 | Drop あなたの unless ownership needs emphasis. |
| JA-02 | Button style | 保存してください on a button | 保存 | Sentences are polite; buttons are short action names. |
| JA-03 | Style | ファイルの保存を行います。 | ファイルを保存します。 | Cut unnecessary nominalization with を行う. |
| JA-04 | Consistency | ログイン and サインイン in the same feature | Pick one from the product glossary | Neither is wrong; mixing is. |
| JA-05 | Meaning | Undo → キャンセル | 元に戻す | Undo reverses a completed action; キャンセル stops an operation. |
| JA-06 | Punctuation | ファイルを保存しました. | ファイルを保存しました。 | Japanese sentence-final mark. Leave code and URLs unchanged. |
| JA-07 | State | Not saved yet → 保存できません | まだ保存していません。 | "Not yet done" is not "cannot". |
| JA-08 | Style | 同期を実施しております。 | 同期中です。 | Proposed for a general status message. Formal style is not automatically an error. |
| JA-09 | Context | Random mix of 数, 個, 件 for the same file count | Fix one counter per object and screen. Example: ファイル3件 | |
| JA-10 | Consistency | です・ます and だ・である in the same description | Fix the style per text type | Short menu labels are allowed to differ. |
| JA-11 | Meaning | Always swapping 課金 and 請求 | Separate charge incurred, invoice issued, payment completed | Translate the actual billing event. |
| JA-12 | Register | ご確認させていただきます / ご利用になられます | 確認します / ご利用になれます | Avoid stacked honorifics (二重敬語) and overuse of させていただく in UI. |
| JA-13 | Punctuation | Copying every English "!" (保存しました！) | 保存しました。 | English exclamation marks in UI rarely carry over. Keep only where the product voice wants it. |
| JA-14 | Quotation | "保存"をクリック | 「保存」をクリック | Quote UI labels with 「」. |
| JA-15 | Width | ｶﾀｶﾅ (half-width katakana), ＡＢＣ１２３ (full-width Latin) | カタカナ, ABC123 | Convention for UI text; confirm with the style guide. |
| JA-16 | Loanword choice | コンファーム, ディスカード, リバート | 確認, 破棄, 元に戻す | Do not transliterate when an established Japanese UI term exists. Keep established loanwords (ワークスペース, プロンプト). |
| JA-17 | Meaning | 削除 for both Delete and Remove from list with no object | リストから削除 / ファイルを削除 | Japanese uses 削除 for both; name the target and scope. |

## 5. Worked examples

| Meaning | EN | JA |
|---|---|---|
| In progress | Saving changes. | 変更を保存しています。 |
| Done | Changes saved. | 変更を保存しました。 |
| Failed | Couldn't save changes. | 変更を保存できませんでした。 |
| No permission | You don't have permission to edit this file. | このファイルを編集する権限がありません。 |
| Not created yet | No projects yet. | プロジェクトはまだありません。 |
| Missing input | Enter a project name. | プロジェクト名を入力してください。 |
| No results | No results found. | 検索結果がありません。 |
| Confirmation | Delete this file? | このファイルを削除しますか？ |

| Scenario | Title | Body | Primary | Secondary |
|---|---|---|---|---|
| Trash, restorable | ファイルをゴミ箱に移動しますか？ | ゴミ箱から復元できます。 | ゴミ箱に移動 | キャンセル |
| Permanent | ファイルを完全に削除しますか？ | 削除したファイルは復元できません。 | 完全に削除 | キャンセル |

Japanese has one plural category. Counts use counters, not plural forms.
