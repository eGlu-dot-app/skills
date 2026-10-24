# ko-KR: Korean (South Korea)

Based on the CJK UX Localization Reference v0.2 (2026-10-24), translated into English and extended. All examples are `proposed`.

## Contents

1. Scope and register
2. Language characteristics and UX implications
3. Typography and punctuation
4. Common mistakes (KO-01 to KO-27)
5. Worked examples

## 1. Scope and register

- Market: South Korea. North Korean usage is out of scope.
- **Default register: 합니다체 (formal polite, -ㅂ니다 / -습니다).** This is the product setting chosen for this skill (2026-10-24). If a product's own style guide uses 해요체, follow the product and say so in the notes.

| Sentence type | Default form | Example |
|---|---|---|
| Statement, result, status | -ㅂ니다 / -습니다 | 변경 사항을 저장했습니다. |
| In progress | -고 있습니다, 또는 명사 + 중입니다 | 변경 사항을 저장하고 있습니다. / 동기화 중입니다. |
| Confirmation question to the user | -하시겠습니까? | 이 파일을 삭제하시겠습니까? |
| Request or instruction | -해 주십시오 | 프로젝트 이름을 입력해 주십시오. |
| Negative fact | -지 않습니다 / -ㄹ 수 없습니다 / -지 못했습니다 | 저장할 수 없습니다. |

- Requests: "-해 주십시오" is the default. "-하십시오" alone reads as a command; use it only where the product wants a direct instruction. Many Korean products pair 합니다체 statements with "-해 주세요" requests; that mix is an allowed variant only when the product's style guide chooses it. Record it as a product setting.
- -시- honors the user when the user is the subject (삭제하시겠습니까, 입력하신 이메일). Never attach -시- to files, payments or system states (KO-03).
- Buttons and menus: short action names or noun phrases (저장, 설정, 목록에서 제거). No sentence endings, no final period on standalone labels. The register applies to sentences, not to labels.
- Never 반말 or slang in product UI unless the brand explicitly uses it.
- Do not mix 합니다체 and 해요체 within one product surface (KO-27). Terms of service and legal text already use 합니다체; system logs may use other forms by product rule.
- Product style settings seen in this project (not Korean grammar): 합니다체 default, no em or en dashes, no emojis.

## 2. Language characteristics and UX implications

- **Particles and endings carry roles and attitude.** Do not assemble translated fragments in English word order. Translate the whole message.
- **Subjects and possessors can be omitted** when context makes them clear. Keep them when the responsible party matters (user, admin, system), for example who must approve, or who can see a shared item.
- **Two kinds of honorifics.** Politeness toward the reader (the register: 합니다체 here) is separate from honoring the sentence subject (-시-). Do not honor files, payments or system states (KO-03).
- **Negation types differ.** Keep "did not" (안 함), "could not / cannot" (못함, 할 수 없음), "not yet" (아직 안 함) and "failed" (실패) distinct (KO-05).
- **Many-to-one and one-to-many verbs.** Several English words can map to one Korean verb, and one English word can need different Korean words: remove → 제거, 삭제, 해제 by context.
- **Spacing (띄어쓰기).** Particles and endings attach to the word; words, dependent nouns (수, 것, 중 in some uses) and auxiliary constructions need checking (KO-06).
- **No letter case in Hangul.** English title case does not apply. Keep the original casing of brands and acronyms.
- **Long noun modifiers** (English-style stacked modifiers) become hard to read. Split condition and action. Proposed: 관리자가 승인한 멤버만 접근할 수 있습니다.
- **The possessive 의 is not the default for English 's or "of".** Project settings → 프로젝트 설정. Keep 의 only when ownership or disambiguation needs it.
- **Variables and particles.** Particle choice depends on the final syllable of the inserted word. See `universal-rules.md` section 6. When a sentence would need a particle after an unknown name, consider a label layout: 삭제한 파일: {fileName}.
- **One term per concept.** Repeating the same noun is natural in Korean. Do not replace a term with a synonym, a demonstrative (해당, 본, 이것) or the English form of the same term within a product.
- **합니다체 length.** 합니다체 endings are longer than 해요체 endings. Keep toasts short by cutting words, not by switching register.
- **UX writing:** state the result and the next action the user can take, briefly. Do not add a cause or recovery step that the source does not give.

## 3. Typography and punctuation

- Sentence-final period on full sentences in body text and toasts; none on buttons, menu items, titles and standalone labels.
- Question mark for questions (삭제하시겠습니까?).
- Avoid East Asian full-width punctuation (。、) in Korean text; Korean uses Western punctuation (checker rule KO-PUNCT).
- Spaces between Hangul and Latin text or numbers follow normal word spacing; units attached to numbers follow 한글 맞춤법 (3개, 10자). Decide a product rule for spaces around variables.
- Quotation: Korean UI normally uses straight or curly double quotes; follow the product style.

## 4. Common mistakes

KO-01 to KO-14 come from the CJK reference v0.2, with examples converted to 합니다체. KO-15 to KO-26 cover translationese (번역투) and term variation. KO-27 covers register mixing. These are error types to check, not frequency findings.

| ID | Type | Avoid | Prefer | Rule |
|---|---|---|---|---|
| KO-01 | Register | 당신의 프로젝트를 저장하세요. | 프로젝트를 저장해 주십시오. | Drop the pronoun when the owner is clear. Keep ownership when contrasting with someone else's project. |
| KO-02 | Style | 귀하의 파일이 성공적으로 저장되었습니다. | 파일을 저장했습니다. | Example for a short success toast: drop 귀하 and 성공적으로. Do not ban 귀하 in formal documents. |
| KO-03 | Honorific target | 파일이 저장되셨습니다. | 파일이 저장되었습니다. | Do not honor objects or system states. |
| KO-04 | Style, brevity | 프로젝트의 생성을 진행합니다. | 프로젝트를 만듭니다. | Cut nominalization and "proceed" phrasing. If it is really in progress, keep the state: 프로젝트를 만드는 중입니다. |
| KO-05 | Meaning | Cannot save → 저장하지 않았습니다 | 저장할 수 없습니다. | Separate inability, permission or condition limits from simply not doing it. Past failure: 저장하지 못했습니다. |
| KO-06 | Spacing | 저장 할 수 없습니다. | 저장할 수 없습니다. | Distinguish conjugation from dependent nouns. |
| KO-07 | Variable and particle | Inserting 폴더 into 파일을 삭제했습니다 to get 폴더을 | 폴더를 삭제했습니다. | Translate full messages per object, or use a tested particle helper. Do not guess batchim for English names and numbers. |
| KO-08 | Meaning | No results → 아무것도 없습니다 | 검색 결과가 없습니다. | Keep what is missing. No access, no file and no connection are different messages. |
| KO-09 | Over-correction | Converting every passive to active | 연결이 끊겼습니다. | Keep state-centered passives that read naturally. Only fix unnecessary stacked passives. |
| KO-10 | UI style | 저장하기. / 설정. | 저장 / 설정 | Label rule for this baseline. Do not mechanically remove natural forms such as 만들기. |
| KO-11 | Style | 설정의 변경의 적용 | 설정 변경 사항 적용 | Chained 의. The actual button can be just 적용 when the meaning is clear. |
| KO-12 | Style | 동기화가 진행되어지고 있습니다. | 동기화 중입니다. | Remove stacked passive and "proceed". |
| KO-13 | Meaning | Treating 10자 이내 and 10자 미만 as the same | 최대 10자를 허용하면 10자 이내 | Confirm the boundary value first. 이내 includes 10; 미만 excludes it. |
| KO-14 | Style | 가능합니다 with no object | 편집할 수 있습니다. | Name the possible action. |
| KO-15 | Translationese | 보안에 있어서 중요한 설정입니다. | 보안에 중요한 설정입니다. | ~에 있어서 copies "in terms of". Restructure. |
| KO-16 | Translationese | 설정을 통해 알림을 끌 수 있습니다. | 설정에서 알림을 끌 수 있습니다. | ~를 통해 copies "through/via". Use the particle that states the real relation (에서, 로, 해서). |
| KO-17 | Translationese | 이 파일은 3개의 버전을 가지고 있습니다. | 이 파일에는 버전이 3개 있습니다. | 가지고 있다 copies "have". Also prefer noun + count (버전 3개) over "3개의 버전". |
| KO-18 | Translationese | 파일을 내보내는 것이 가능합니다. | 파일을 내보낼 수 있습니다. | ~하는 것이 가능하다 copies "it is possible to". |
| KO-19 | Translationese | 선택한 파일들을 삭제하시겠습니까? | 선택한 파일을 삭제하시겠습니까? | -들 copies English plural. Use it only when plurality would otherwise be unclear. |
| KO-20 | Translationese | 성공적으로 업로드되었습니다. | 업로드했습니다. | "successfully" adds nothing to a success message. |
| KO-21 | Term variation | Same action labeled 삭제 on one screen, 제거 on another, 지우기 in a toast | One term per concept from the glossary | English source often varies verbs for style. Map to the concept and repeat the Korean term. If they really are different actions (delete vs remove from list), keep them different on purpose. |
| KO-22 | Literal figurative words | 첫 프로젝트를 착지시키십시오 (land), 이 기능이 빛나는 순간 (shine), 경쟁에서 이기십시오 (win) | 첫 프로젝트를 완성해 보십시오 / 이 기능이 특히 유용한 경우 | Do not carry English metaphors or polysemous words over literally. State the literal meaning. |
| KO-23 | Term variation | IME and 입력기, headless and 헤드리스 in the same product | Pick one form | Do not mix the Korean and English forms of one term. |
| KO-24 | Vague reference | 해당 기능을 사용할 수 없습니다. | 내보내기 기능을 사용할 수 없습니다. | 해당, 본, 이것 hide the object. Name it when the screen does not make it obvious. |
| KO-25 | Meaning | 확인 as the confirm button of a destructive dialog | 삭제 / 취소 | Name the action. 확인 is acceptable for an acknowledge-only dialog. |
| KO-26 | Loanword choice | 디스카드, 리버트, 리트라이 | 버리기, 되돌리기, 다시 시도 | Keep established industry loanwords (워크스페이스, 업로드, 프롬프트). Do not transliterate a word when a common Korean UI term exists. |
| KO-27 | Register | 변경 사항을 저장했어요. / 삭제할까요? / 입력해 주세요. in a 합니다체 product | 변경 사항을 저장했습니다. / 삭제하시겠습니까? / 입력해 주십시오. | Product setting: one register per product surface. "-해 주세요" is allowed only if the product's style guide chose the mixed style. The checker flags 해요체 endings by default (`--ko-register`). |

## 5. Worked examples

Sources are the proposed English patterns in `universal-rules.md`.

| Meaning | EN | KO |
|---|---|---|
| In progress | Saving changes. | 변경 사항을 저장하고 있습니다. |
| Done | Changes saved. | 변경 사항을 저장했습니다. |
| Failed | Couldn't save changes. | 변경 사항을 저장하지 못했습니다. |
| No permission | You don't have permission to edit this file. | 이 파일을 편집할 권한이 없습니다. |
| Not created yet | No projects yet. | 아직 프로젝트가 없습니다. |
| Missing input | Enter a project name. | 프로젝트 이름을 입력해 주십시오. |
| No results | No results found. | 검색 결과가 없습니다. |
| Confirmation | Delete this file? | 이 파일을 삭제하시겠습니까? |

The confirmation does not mention permanence or recovery. Add that only when the behavior is confirmed (see `universal-rules.md` section 4):

| Scenario | Title | Body | Primary | Secondary |
|---|---|---|---|---|
| Trash, restorable | 파일을 휴지통으로 이동하시겠습니까? | 휴지통에서 복원할 수 있습니다. | 휴지통으로 이동 | 취소 |
| Permanent | 파일을 영구 삭제하시겠습니까? | 삭제한 파일은 복구할 수 없습니다. | 영구 삭제 | 취소 |
| Toast with undo | {fileName} 파일을 삭제했습니다. (separate key for the action) | | 실행 취소 | |

Counts: 파일 3개. Korean has a single plural category; do not create one/other copies for grammar.
