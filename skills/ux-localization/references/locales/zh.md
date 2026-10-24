# zh-Hans-CN and zh-Hant-TW: Chinese (mainland China, Taiwan)

Based on the CJK UX Localization Reference v0.2 (2026-10-24), translated into English and extended. All examples are `proposed`.

## Contents

1. Scope and register
2. Language characteristics and UX implications
3. Typography and punctuation
4. Common mistakes, mainland (ZHCN-01 to ZHCN-11)
5. Common mistakes, Taiwan (ZHTW-01 to ZHTW-11)
6. Worked examples

## 1. Scope and register

- zh-Hans-CN: Standard Chinese UI for mainland China, Simplified characters.
- zh-Hant-TW: Standard Chinese UI for Taiwan, Traditional characters.
- Hong Kong, Macau and Singapore are out of scope. Do not apply Taiwan terms to Hong Kong just because both use Traditional characters.
- Address: 你 or 您 is a product decision. The examples use 你 for CN and 您 for TW as editorial choices, not as a rule of either market. Do not switch address forms within a product, and do not invent a relationship by changing honorifics between user and admin messages without a reason.
- Region, script and politeness are three separate settings. Taiwan does not imply 您 in every sentence.

## 2. Language characteristics and UX implications

- **Script conversion is not localization.** Converting Simplified to Traditional character by character leaves mainland vocabulary in a Taiwan UI (文件夾 instead of 資料夾, 軟件 instead of 軟體). Choose the term per market. The term table is in `pairs.md`, section zh-CN and zh-TW.
- **Politeness works differently from Korean and Japanese.** There are no verb endings for politeness. Politeness comes from 你/您, 请/請 and sentence construction.
- **No spaces between words** in Chinese text. Spaces around Latin letters and numbers are a product typography rule; decide it per product and apply it consistently.
- **Aspect and state markers.** Use 已 (done), 正在 (in progress), 尚未 (not yet) deliberately. Do not add 已 or 了 to every past-tense English sentence.
- **Measure words.** Use the right measure word for the object: 3 个文件 / 3 個檔案. Do not use 条 for every count (ZHCN-08).
- **Articles and plural** have no visible marker. Do not invent markers for them, but do not drop quantity and scope words either: 部分, 全部, 仅/僅, 至少, 最多 are meaning-checked items.
- **Short verbs can be ambiguous.** Add the object when the verb alone could mean several things: 取消订阅 / 取消訂閱.
- **Buttons are short; sentences state cause, result and next action clearly.** Do not add success guarantees or politeness the source does not have.
- **Glyphs differ by region.** The same code point may need a different glyph shape, and punctuation sits in a different position in mainland and Taiwan fonts. Tag content with the right language and use regional fonts. [S3] [S4]

## 3. Typography and punctuation

- Use full-width Chinese punctuation in Chinese sentences: ，。？！：；、. Keep ASCII symbols inside code, URLs and email addresses (ZHCN-05).
- Quotation marks: mainland text normally uses “ ”; Taiwan text normally uses 「」 and 『』 (ZHTW-10). [S3]
- No final 。 on buttons, menu items, titles or standalone labels.
- Ellipsis in Chinese is ……(two ellipsis characters) in running text; loading indicators follow the product style.

## 4. Common mistakes, mainland (zh-Hans-CN)

| ID | Type | Avoid | Prefer | Rule |
|---|---|---|---|---|
| ZHCN-01 | Term | 登陆 for account sign-in | 登录 | Fix the authentication term for the product. |
| ZHCN-02 | Regional term | 檔案 / 儲存 in account UI | 文件 / 保存 | Use the mainland glossary. |
| ZHCN-03 | Translationese | 你的文件已经被成功地保存了。 | 文件已保存。 | For general success notices, drop the pronoun and passive structure. |
| ZHCN-04 | Meaning | Cancel button → 删除 | 取消 | Stopping an operation is not deleting an object. |
| ZHCN-05 | Punctuation | 保存失败,请重试. | 保存失败，请重试。 | Chinese punctuation in sentences. Check that retry is really possible. |
| ZHCN-06 | State | Not saved yet → 无法保存 | 尚未保存 | "Not yet" is not "cannot". |
| ZHCN-07 | Meaning | Lack of permission → 不支持 | 没有权限, or the specific access instruction | Permission problems are not missing features. |
| ZHCN-08 | Context | 条 for every count | Choose the measure word per object (个文件, 条消息, 位成员) | |
| ZHCN-09 | Translationese | 文件被删除了。 | 文件已删除。 | 被 copies the English passive; it also tends to sound adverse. Use it only when the agent matters. |
| ZHCN-10 | Translationese | 正在进行文件的上传 | 正在上传文件 | 进行 + verb nominalization copies "perform the upload of". |
| ZHCN-11 | Consistency | 你 and 您 in the same product surface | One address form per product | |

## 5. Common mistakes, Taiwan (zh-Hant-TW)

| ID | Type | Avoid | Prefer | Rule |
|---|---|---|---|---|
| ZHTW-01 | Regional term | 软件 converted to 軟件 | 軟體 | Taiwan glossary choice. Do not mark 軟件 wrong for every Traditional market. |
| ZHTW-02 | Regional term | 文件夹 converted to 文件夾 | 資料夾 | Taiwan folder label. |
| ZHTW-03 | Regional term | 登錄 for the sign-in label | 登入 | 登錄 is fine in other contexts (registering a record). |
| ZHTW-04 | Regional term | 导出 converted to 導出 | 匯出 | Term choice, not just character conversion. |
| ZHTW-05 | Translationese | 您的檔案已經被成功地儲存了。 | 檔案已儲存。 | Shorten general success notices. Do not remove 您 where the message needs it. |
| ZHTW-06 | Meaning | Undo, Restore and Reset all → 還原 | 復原 / 還原檔案 / 重設 | Separate the actions and name the object. This split is an editorial proposal, not a single universal norm. |
| ZHTW-07 | Consistency | 链接 and 連結 for the same link action | 連結 | Taiwan glossary choice. |
| ZHTW-08 | Consistency | 請 on every CTA (請儲存, 請刪除) | 儲存, 刪除 | Buttons stay bare. Keep 請 in sentences where it fits. |
| ZHTW-09 | Regional term | Mainland vocabulary left after conversion (信息, 视频→視頻, 默认→默認, 网络→網絡) | 訊息 or 資訊, 影片, 預設, 網路 | Run the term table in `pairs.md`. |
| ZHTW-10 | Punctuation | “保存” style quotes | 「儲存」 | Taiwan quotation marks. |
| ZHTW-11 | Script mixing | Simplified characters left in Traditional text (设定, 档案) | 設定, 檔案 | The checker flags candidates; names, quotes and brands may mix on purpose. |

## 6. Worked examples

| Meaning | EN | zh-Hans-CN | zh-Hant-TW |
|---|---|---|---|
| In progress | Saving changes. | 正在保存更改。 | 正在儲存變更。 |
| Done | Changes saved. | 更改已保存。 | 變更已儲存。 |
| Failed | Couldn't save changes. | 无法保存更改。 | 無法儲存變更。 |
| No permission | You don't have permission to edit this file. | 你没有编辑此文件的权限。 | 您沒有編輯此檔案的權限。 |
| Not created yet | No projects yet. | 暂无项目。 | 尚無專案。 |
| Missing input | Enter a project name. | 请输入项目名称。 | 請輸入專案名稱。 |
| No results | No results found. | 未找到搜索结果。 | 找不到搜尋結果。 |
| Confirmation | Delete this file? | 要删除此文件吗？ | 要刪除此檔案嗎？ |

- The "Failed" examples fit a failure message after an attempt. Do not share the key with a settings message saying saving is not available.

| Scenario | Locale | Title | Body | Primary | Secondary |
|---|---|---|---|---|---|
| Trash, restorable | zh-Hans-CN | 要将文件移至回收站吗？ | 你可以从回收站恢复文件。 | 移至回收站 | 取消 |
| Trash, restorable | zh-Hant-TW | 要將檔案移至垃圾桶嗎？ | 您可以從垃圾桶還原檔案。 | 移至垃圾桶 | 取消 |
| Permanent | zh-Hans-CN | 要永久删除文件吗？ | 删除后无法恢复。 | 永久删除 | 取消 |
| Permanent | zh-Hant-TW | 要永久刪除檔案嗎？ | 刪除後無法還原。 | 永久刪除 | 取消 |

Chinese has one plural category. Counts use measure words: 3 个文件 / 3 個檔案.
