# en-US and en-GB: English (United States, United Kingdom)

English is usually the source language. This file covers English as a **target** (translating from Korean, Japanese, Chinese, French, German or Spanish into English) and **en-US to en-GB adaptation**. All examples are `proposed`.

## Contents

1. Scope and register
2. Language characteristics and UX implications
3. Typography and punctuation
4. Common mistakes when writing English UI from another language (EN-01 to EN-16)
5. en-GB adaptation and its mistakes (ENGB-01 to ENGB-08)
6. Worked examples

## 1. Scope and register

- Address the user as "you". Refer to the product as "we" only if the brand voice does.
- Contractions (can't, don't, couldn't) are common in en-US and en-GB product UI. Whether to use them is a product style setting.
- Casing: sentence case vs title case for buttons, menus and titles differs between platform guidelines and products. It is a product setting, not an English grammar rule. Apply one rule consistently.
- Tag British English as `en-GB`, not `en-UK`: ISO 3166-1 assigns GB to the United Kingdom, and BCP 47 region subtags follow it. (S10 shows en-GB as an example.)

## 2. Language characteristics and UX implications

- **Articles are required.** "Enter project name" reads as a truncated label; in a sentence write "Enter a project name". Labels and buttons can drop articles ("Project name", "Delete file").
- **Countable and uncountable nouns.** information, feedback, advice, software, equipment, content (in the sense of material) have no plural "-s" (EN-01).
- **Phrasal verb vs noun.** Verb forms are two words; noun or adjective forms are one word: log in / login, sign up / signup, set up / setup, back up / backup, check out / checkout, sign in / sign-in page.
- **Verb first on buttons.** Buttons start with the action ("Delete file", "Save changes"). Avoid "OK" when a specific verb fits.
- **Active voice for errors and results, when the actor is useful.** "We couldn't save your changes" or "Couldn't save changes" rather than "Your changes could not be saved successfully".
- **Plain words.** Prefer "use" to "utilize", "start" to "initiate", "help" to "assistance". Avoid internal jargon unless users know it.
- **Second person, not "the user".** "You can edit this file", not "The user can edit this file".
- **Polysemy is high.** The same English word often carries several concepts. When English is the target, choose words that name exactly one concept, and keep one word per concept.

## 3. Typography and punctuation

- Period on full sentences in body text; no period on buttons, menu items, titles or standalone labels. Toast punctuation is a product rule; keep it consistent.
- Quotation marks: en-US convention uses double quotes; en-GB publishing often uses single quotes first. This is a style setting.
- Ellipsis: one character (…) or three periods, by product style. Use it in menu items that open a further dialog only if the platform convention does.
- Serial (Oxford) comma: en-US style guides commonly use it; en-GB style guides often omit it. CLDR list data differs the same way (see `formats.md`). Decide per product.
- Dashes: whether to use em or en dashes is a style setting. If the product or person bans them, restructure the sentence rather than substituting another character.

## 4. Common mistakes when writing English UI from another language

| ID | Type | Avoid | Prefer | Rule |
|---|---|---|---|---|
| EN-01 | Grammar | informations, feedbacks, advices, softwares, equipments | information, feedback, advice, software, equipment | Uncountable nouns. |
| EN-02 | Grammar | Enter name of project. | Enter a project name. | Articles in sentences. |
| EN-03 | Style | Please Save / Please click OK | Save / OK | "Please" does not belong on buttons, and is rarely needed in short instructions. |
| EN-04 | Meaning | Confirm or Check for every 확인 / 確認 / 确认 / 確定 | Name the action: Save, Delete, Got it, Review, Verify, OK | The source word covers OK, confirm, check, verify, review. Pick by what happens. |
| EN-05 | Style | Registration is completed. / Success! | Account created. / You're signed up. | Say what happened. |
| EN-06 | Translationese | Your file has been successfully saved. | File saved. | Cut "successfully" and stacked passive in success messages. |
| EN-07 | Meaning | Do you want to delete? | Delete this file? | Name the object. |
| EN-08 | Grammar | Login to continue / Setup your account | Log in to continue / Set up your account | Verb vs noun forms. |
| EN-09 | Translationese | The corresponding function is not available. | Export isn't available. | "corresponding", "relevant", "said" come from 해당 / 該当 / 该. Name the thing. |
| EN-10 | Meaning | Upload fail | Couldn't upload {fileName}. | Name the object and use a full verb form. |
| EN-11 | Style | Proceed with deletion | Delete | 진행하다 / 進める / 进行 do not need a verb in English. |
| EN-12 | Register | The user can change settings here. | You can change settings here. | Second person. |
| EN-13 | Term | My page, SNS, hand phone, PC version | Account or Profile, social media, phone, desktop | Words formed in Korean or Japanese from English elements that English speakers do not use this way. |
| EN-14 | Term | Inquiry / Inquire | Contact us / Get help / Ask a question | 문의 / お問い合わせ are usually "contact" actions in UI. |
| EN-15 | Consistency | Title Case on some buttons, sentence case on others | One casing rule | Product setting. |
| EN-16 | Meaning | Fighting! / Cheer up! | Good luck. or remove | Exhortations rarely carry over. Keep the function (encouragement) only if the product voice wants it. |

## 5. en-GB adaptation

en-US and en-GB share grammar. Adaptation changes spelling, some vocabulary and some formats. Change only displayed text; never change code identifiers, API names, CSS properties or brand names ("color" in code stays).

### Spelling (proposed en-GB column uses -ise; see glossary-notes `en-gb-spelling`)

| en-US | en-GB | Note |
|---|---|---|
| color, behavior, favorite | colour, behaviour, favourite | |
| center | centre | |
| organization, customize, analyze | organisation, customise, analyse | Oxford spelling keeps -ize but still uses analyse |
| canceled, labeled, traveled, modeling | cancelled, labelled, travelled, modelling | |
| license (noun and verb) | licence (noun), license (verb) | |
| practice (noun and verb) | practice (noun), practise (verb) | |
| catalog | catalogue | |
| enrollment, fulfill | enrolment, fulfil | |
| gray | grey | |
| program (software) | program (software) | programme only for TV, events, initiatives |
| dialog (UI element) | dialog (UI element), often kept | dialogue for conversation |
| defense | defence | |

### Vocabulary

| Concept | en-US | en-GB |
|---|---|---|
| Deleted-items container | Trash | Bin |
| Postal code field | ZIP code | Postcode |
| Mobile phone | cell phone, mobile phone | mobile, mobile phone |
| Time off | vacation | holiday |
| Sales tax | sales tax | VAT (a different tax system; check the actual tax) |
| Bill at a restaurant | check | bill |
| Apartment | apartment | flat |
| State or region field | State | County (optional in UK addresses) |

### Mistakes

| ID | Avoid | Prefer | Rule |
|---|---|---|---|
| ENGB-01 | programme for software | program | Software keeps "program". |
| ENGB-02 | Changing spelling inside code, variables, API names, brand names | Change only displayed text | |
| ENGB-03 | Mixing -ize and -ise in one product | One rule | Product setting. |
| ENGB-04 | licence used as a verb | license (verb), licence (noun) | |
| ENGB-05 | US vocabulary left: Trash, ZIP code, cell phone | Bin, Postcode, mobile | |
| ENGB-06 | MM/DD dates in en-GB strings | Locale formatter, or "24 October 2026" | |
| ENGB-07 | 12-hour times assumed | 24-hour times are common in UK UI; use the formatter | CLDR en-GB short time is 14:30. [S18] |
| ENGB-08 | Assuming VAT equals sales tax | Use the real tax rule | Tax wording is product and legal content, not spelling. |

## 6. Worked examples

| Meaning | en-US | en-GB |
|---|---|---|
| In progress | Saving changes. | Saving changes. |
| Done | Changes saved. | Changes saved. |
| Failed | Couldn't save changes. | Couldn't save changes. |
| No permission | You don't have permission to edit this file. | You don't have permission to edit this file. |
| Not created yet | No projects yet. | No projects yet. |
| Missing input | Enter a project name. | Enter a project name. |
| No results | No results found. | No results found. |
| Confirmation | Delete this file? | Delete this file? |
| Trash title | Move file to Trash? | Move file to the bin? |
| Trash body | You can restore it from Trash. | You can restore it from the bin. |
| Canceled status | Subscription canceled | Subscription cancelled |

Whether "Trash" or "Bin" is capitalized as a named place is a product style setting.
