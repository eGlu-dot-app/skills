# Direction-specific mistakes

Mistakes depend on the direction of translation: the source language pushes its structure into the target (interference). Read the section for the direction you are working in, plus the target's locale file. IDs here combine source and target (ENKO = English to Korean). Locale-file IDs (KO-15, FR-08) are referenced instead of repeated.

All items are `proposed` error types to check, not frequency findings.

## Contents

1. English source: high-risk words and conventions not to copy
2. English to Korean (ENKO) and Korean to English (KOEN)
3. English to Japanese (ENJA) and Japanese to English (JAEN)
4. English to Chinese (ENZH) and Chinese to English (ZHEN)
5. English to French (ENFR) and French to English (FREN)
6. English to German (ENDE) and German to English (DEEN)
7. English to Spanish (ENES) and Spanish to English (ESEN)
8. en-US and en-GB
9. es-ES and es-419
10. zh-CN and zh-TW
11. CJK shared characters (Korean, Japanese, Chinese)
12. Pivot translation through English

## 1. English source: high-risk words and conventions not to copy

### 1.1 One English word, several concepts

Resolve the concept before translating. If one key serves two concepts, ask for a second key (ALL-12).

| English | Concepts to separate | Examples of the split |
|---|---|---|
| Cancel | stop an operation; end a subscription; cancel an order | de Abbrechen / Kündigen / Stornieren; fr Annuler / Résilier / Annuler la commande; ko 취소 / 구독 해지 or 구독 취소 / 주문 취소 |
| Remove | delete the object; remove from a list; unassign; uninstall | ko 삭제 / 제거 / 해제 / 제거(앱); de Löschen / Entfernen; es Eliminar / Quitar |
| Clear | empty a field; delete history; reset filters; dismiss notifications | ko 지우기 / 기록 삭제 / 필터 초기화 / 모두 지우기 |
| Reset | restore defaults; set a new password | ko 초기화 / 재설정; fr Réinitialiser / Réinitialiser le mot de passe; zh-TW 重設 |
| Free | no cost; available; empty | de kostenlos / verfügbar / frei; es gratis / disponible / libre; ko 무료 / 사용 가능 / 비어 있음 |
| Save | store content; save money ("Save 20%") | de Speichern / sparen; fr Enregistrer / économiser; es Guardar / ahorrar; ko 저장 / 할인 |
| Apply | apply settings; apply a coupon; apply for something | de Übernehmen / Gutschein einlösen / sich bewerben; es Aplicar / Aplicar cupón / Solicitar (es-ES), Postularse or aplicar a (es-419) |
| Order | a purchase; a sort order | fr commande / ordre; de Bestellung / Reihenfolge; es pedido / orden; ko 주문 / 순서 |
| Update | software update (noun); change something (verb); refresh | ko 업데이트 / 수정 or 변경 / 새로고침; ja 更新 covers several of these, so name the object |
| Close | dismiss a window; close an account (delete it) | ko 닫기 / 계정 해지 or 탈퇴; fr Fermer / Supprimer le compte (Clôturer is banking usage) |
| Share | share a link or post; grant access | de Teilen / Freigeben; zh 分享 / 共享 or 共用 |
| Plan | billing tier; project plan | ko 요금제 / 계획; fr Forfait / Plan |
| Charge | billing charge; battery charge | ko 청구 or 결제 / 충전 |
| Review | check something; a rating or written review; code review | ko 검토 / 리뷰 or 후기 / 코드 리뷰 |
| Pin | pin to top; PIN code | ko 고정 / PIN |
| Track | follow progress; analytics tracking; audio track | ko 추적 / 추적 / 트랙 |
| Post | publish; a post (noun); postal mail | ko 게시 / 게시물 / 우편 |
| Block | block a user; a content block | ko 차단 / 블록 |
| Run | execute; one execution (noun) | ko 실행 / 실행 기록 |
| Live | in production; live broadcast | ko 게시됨 or 운영 중 / 라이브 |
| Sign | sign in; sign a document; a sign | ko 로그인 / 서명 / 표지 |
| Account | login account; bank account | es Cuenta / Cuenta bancaria; zh 账号 / 账户 |

### 1.2 English UI conventions that should not be copied

| Convention in English source | Why it fails elsewhere | Do |
|---|---|---|
| Title Case Buttons | No title case in fr, de, es; no case in CJK | Target casing (ALL-15) |
| "your" on every label | Unneeded in ko, ja, zh; often unneeded in fr, de, es | Drop when the owner is clear (KO-01, JA-01) |
| "has been successfully …" | Translationese in every target | State the result (KO-20, ZHCN-03, FR-13, DE-08, ES-05) |
| "-ing" headings (Getting started, Creating a project) | Gerund calques in es; awkward in fr, de | Getting started: fr Prise en main, de Erste Schritte, es Primeros pasos, ko 시작하기, ja はじめに, zh-CN 入门, zh-TW 入門 |
| "Please" on buttons | Never on buttons in any target | Bare action |
| Idioms and exclamations: You're all set, Oops!, Hang tight, Heads up, Nailed it | Literal versions sound odd or childish | Translate the function: "Setup complete", "Something went wrong", "This may take a minute", "Note" |
| English metaphors and polysemous verbs (land, win, shine, unlock, power) | Literal versions carry the wrong meaning (KO-22) | Write the literal meaning |
| Noun stacks (Project member invitation link expiration date) | Unreadable in target order | Unpack into a phrase or sentence |
| Yes / No buttons | Do not name the action (ALL-05) | Action + Cancel |
| Click here | Often fails link purpose (WCAG 2.4.4 when the context does not name the target; always 2.4.9) and assumes a pointer device | Name the destination |
| Synonym variety (remove / delete / erase for one action) | Reads as different features | One term per concept (ENKO-01 and equivalents) |
| Contractions (can't, don't) | Not a register signal in other languages | Choose target register independently |

## 2. English to Korean and Korean to English

### ENKO: English to Korean

| ID | Type | Avoid | Prefer | Rule |
|---|---|---|---|---|
| ENKO-01 | Term variation | Source says remove, delete, erase for one action; Korean follows with 제거, 삭제, 지우기 | 삭제 everywhere for that concept | English writers vary verbs to avoid repetition. Korean UI repeats one term per concept. The reverse also happens: translators add variety (생성, 만들기, 추가) that the source did not have. Use 만들기 or 생성 for creating something new (one of them, per product) and 추가 for adding an existing item to a container. |
| ENKO-02 | Translationese | ~에 있어서, ~를 통해, ~되어지다, 가지고 있다, ~하는 것이 가능하다, -들 | See KO-15 to KO-19 | Structural calques of "in terms of", "through", double passive, "have", "it is possible to", plural -s. |
| ENKO-03 | Translationese | 관리자에 의해 삭제되었습니다. | 관리자가 삭제했습니다. | ~에 의해 copies the English "by" passive. |
| ENKO-04 | Translationese | 서버로부터 응답이 없습니다. | 서버에서 응답이 없습니다. | ~로부터 copies "from". |
| ENKO-05 | Translationese | 사용자에 대한 권한에 대한 설정 (for "Settings for permissions for users") | 사용자 권한 설정 | Chained ~에 대한 copies "for/about"; compress into a noun phrase. |
| ENKO-06 | Translationese | 3개의 파일을 선택했습니다. | 파일 3개를 선택했습니다. | Number + 의 + noun copies "3 files". |
| ENKO-07 | Translationese | 당신, 그, 그녀, 그들 | Omit, or use the role (관리자, 멤버) | Pronouns copied from English. |
| ENKO-08 | Register | 정말 이 파일을 삭제하시겠습니까? (for "Are you sure you want to delete this file?") | 이 파일을 삭제하시겠습니까? | 합니다체 confirmation questions use -하시겠습니까. Add 정말 only when the action is high risk and the product uses it on purpose. Never switch to 해요체 (삭제할까요?) in a 합니다체 product (KO-27). |
| ENKO-09 | Meaning | Cannot → 하지 않았습니다 | 할 수 없습니다 / 하지 못했습니다 | KO-05. |
| ENKO-10 | Literal metaphor | Land, win, shine, unlock taken literally | Literal meaning | KO-22. |
| ENKO-11 | Modifier order | Long stacked modifiers before the noun (관리자가 승인한 초대를 받은 워크스페이스의 멤버는) | Split condition and action into two clauses | Korean modifiers precede the noun; English post-modifiers become long chains. |
| ENKO-12 | Possessive | 프로젝트의 설정, 사용자의 계정의 비밀번호 | 프로젝트 설정, 계정 비밀번호 | KO-11. |

### KOEN: Korean to English

| ID | Korean | Avoid | Prefer | Rule |
|---|---|---|---|---|
| KOEN-01 | 확인 | Confirm / Check for every case | OK, Got it, Confirm, Verify, Review, or the action (Save, Delete) | EN-04 |
| KOEN-02 | 완료 | Complete! / Registration is completed | Done (button); "Account created" (result) | EN-05 |
| KOEN-03 | 진행하다 | Proceed with payment | Pay / Continue to payment | EN-11 |
| KOEN-04 | 등록 | Register for every case | Add (item), Sign up (account), Submit (form), Register (event, device) | One Korean word, several English actions |
| KOEN-05 | 신청 | Application for every case | Request, Apply, Sign up, Book | Pick the action |
| KOEN-06 | 문의 | Inquiry | Contact us, Get help | EN-14 |
| KOEN-07 | 해당 | The corresponding … | Name the object, or "this" | EN-09 |
| KOEN-08 | 안내 | Guidance | Info, Notice, Tip, or drop it | "Guidance" sounds like instruction from authority |
| KOEN-09 | 오류가 발생했습니다 | An error has occurred. | Something went wrong. / Couldn't load {object}. | Name the failure when known |
| KOEN-10 | 잠시 후 다시 시도해 주세요 | Please try again after a while. | Try again later. | |
| KOEN-11 | 아이디 | ID | Username, or the real identifier (email) | "ID" is ambiguous in English UI |
| KOEN-12 | 마이페이지, SNS, 휴대폰, 노트북 | My page, SNS, hand phone, notebook | Account or Profile, social media, mobile phone, laptop | EN-13 |
| KOEN-13 | 회원 | Member (for every logged-in user) | You, account, user (in admin UI) | "Member" implies a membership program in English |
| KOEN-14 | 화이팅, 수고하셨습니다 | Fighting!, Thank you for your hard work | Good luck. / remove | EN-16 |
| KOEN-15 | Uncountables | informations, feedbacks, advices, softwares | information, feedback, advice, software | EN-01 |
| KOEN-16 | Articles | Enter name of project | Enter a project name | EN-02 |

## 3. English to Japanese and Japanese to English

### ENJA: English to Japanese

| ID | Type | Avoid | Prefer | Rule |
|---|---|---|---|---|
| ENJA-01 | Register | あなたの設定 | 設定 | JA-01 |
| ENJA-02 | Translationese | 保存を行うことができます | 保存できます | JA-03; "can" does not need 〜することができます in UI |
| ENJA-03 | Term variation | 削除, 消去, 除去 for one action | 削除 | One term per concept |
| ENJA-04 | Katakana overuse | コンファーム, リトライ, ディスカード | 確認, 再試行, 破棄 | JA-16 |
| ENJA-05 | Exclamations | おっと！ for Oops! / 完了しました！ | 問題が発生しました。 / 完了しました。 | JA-13 |
| ENJA-06 | Register | ご確認させていただきます | 確認します | JA-12 |
| ENJA-07 | Meaning | Undo → キャンセル | 元に戻す | JA-05 |
| ENJA-08 | Punctuation | "保存" with English quotes, sentence ending "." | 「保存」, 。 | JA-06, JA-14 |
| ENJA-09 | Scope | Delete vs Remove from list both as 削除 with no object | リストから削除 | JA-17 |

### JAEN: Japanese to English

| ID | Japanese | Avoid | Prefer | Rule |
|---|---|---|---|---|
| JAEN-01 | 確認 | Confirmation (everywhere) | OK, Confirm, Review, Check | EN-04 |
| JAEN-02 | よろしいですか？ | Is it OK? | Delete this file? / Are you sure? (only if the product uses it) | Name the action |
| JAEN-03 | ご注意ください | Please be careful. | Note: … | |
| JAEN-04 | お知らせ | Notice (everywhere) | News, Announcements, Notifications by context | |
| JAEN-05 | 案内 | Guidance | Info, Help, Guide | |
| JAEN-06 | 〜してください | Please do … | Imperative without "please" | EN-03 |
| JAEN-07 | 申し訳ございません | We are deeply sorry for the inconvenience. | Sorry, … (only when the product failed) | Apologize in proportion |
| JAEN-08 | 失敗しました / 完了しました | Failed. / Completed. | Couldn't save. / Saved. | Name the object |
| JAEN-09 | マイページ, ログインID | My page, Login ID | Account, Username | EN-13 |

## 4. English to Chinese and Chinese to English

### ENZH: English to Chinese

| ID | Type | Avoid | Prefer | Rule |
|---|---|---|---|---|
| ENZH-01 | Translationese | 你的文件已经被成功地保存了。 | 文件已保存。 | ZHCN-03, ZHTW-05 |
| ENZH-02 | Translationese | 被 passive for every English passive | 已 + verb, or active | ZHCN-09 |
| ENZH-03 | Translationese | 进行 + verb nominalization | Verb + object | ZHCN-10 |
| ENZH-04 | Translationese | 创建一个新的项目 | 新建项目 | 一个 and 新的 copy "a new" |
| ENZH-05 | Register | 你 and 您 mixed | One address form | ZHCN-11 |
| ENZH-06 | Buttons | 请保存 | 保存 | ZHTW-08 |
| ENZH-07 | Punctuation | ASCII , . ? in Chinese sentences | ，。？ | ZHCN-05 |
| ENZH-08 | Meaning | Not yet → 无法 | 尚未 | ZHCN-06 |
| ENZH-09 | Measure words | 3 文件 / 条 for everything | 3 个文件 | ZHCN-08 |

### ZHEN: Chinese to English

| ID | Chinese | Avoid | Prefer | Rule |
|---|---|---|---|---|
| ZHEN-01 | 温馨提示 | Warm reminder / Kind tips | Note / Tip | |
| ZHEN-02 | 确定 / 確定 | Confirm (everywhere) | OK or the action | EN-04 |
| ZHEN-03 | 操作成功 | Operation successful | Name the result: Saved, Deleted | |
| ZHEN-04 | 系统繁忙 | System is busy | The service is busy. Try again later. | |
| ZHEN-05 | 用户 | The user | You | EN-12 |
| ZHEN-06 | 暂无数据 / 暫無資料 | No data | Nothing here yet / No {objects} yet | Name the object |
| ZHEN-07 | 亲 | Dear | Remove | Marketplace slang has no UI equivalent |
| ZHEN-08 | 登录 | Login (as a verb) | Sign in / Log in | EN-08 |

## 5. English to French and French to English

### ENFR: English to French

| ID | Type | Avoid | Prefer | Rule |
|---|---|---|---|---|
| ENFR-01 | Casing | Paramètres Du Compte | Paramètres du compte | FR-01 |
| ENFR-02 | Punctuation | Supprimer ce fichier? | Supprimer ce fichier ? | FR-02 |
| ENFR-03 | False friends | supporter, librairie, éventuellement, actuellement | prendre en charge, bibliothèque, à terme, en fait | FR-08, FR-09 |
| ENFR-04 | Translationese | avec succès | Drop | FR-13 |
| ENFR-05 | Register | Veuillez for every "please" | Imperative or infinitive | Keep "Veuillez" for formal brands |
| ENFR-06 | Headings | Commençant (Getting started) | Prise en main / Premiers pas | Section 1.2 |
| ENFR-07 | Plural | 0 fichiers | 0 fichier | FR-05 |
| ENFR-08 | Collision | Cancel and Undo both Annuler on one screen | Name the object for Undo | FR-10 |
| ENFR-09 | Variables | Le fichier de {name} | Rephrase | FR-06, FR-07 |

### FREN: French to English

| ID | French | Avoid | Prefer | Rule |
|---|---|---|---|---|
| FREN-01 | Valider | Validate | Confirm, Submit, OK, or the action | Common UI false friend |
| FREN-02 | Enregistrer | Register | Save | |
| FREN-03 | Identifiant | Identifier | Username, User ID, or Email | |
| FREN-04 | Actuellement | Actually | Currently | |
| FREN-05 | Éventuellement | Eventually | Possibly, if needed | |
| FREN-06 | Formation | Formation | Training, course | |
| FREN-07 | Informations | Informations | Information | EN-01 |
| FREN-08 | Veuillez … | Please … everywhere | Imperative | EN-03 |
| FREN-09 | Résilier | Resiliate | Cancel, end | |
| FREN-10 | Annuler | Cancel (when the context is Undo) | Undo | Check the action |

## 6. English to German and German to English

### ENDE: English to German

| ID | Type | Avoid | Prefer | Rule |
|---|---|---|---|---|
| ENDE-01 | Spelling | Projekt Name, Email Adresse | Projektname, E-Mail-Adresse | DE-03 |
| ENDE-02 | Grammar | Concatenated separable verbs | Full strings | DE-04 |
| ENDE-03 | Meaning | Cancel always Abbrechen | Abbrechen, Kündigen, Stornieren | DE-06 |
| ENDE-04 | False friends | aktuell, eventuell for actual, eventually; kontrollieren for control (steer, manage) | tatsächlich, schließlich, steuern or verwalten | DE-11 |
| ENDE-05 | Translationese | wurde erfolgreich durchgeführt | Result only | DE-08 |
| ENDE-06 | Headings (style option) | "Erstellen eines Projekts" as a help title for "Creating a project" | Projekt erstellen is shorter; both are correct. Erste Schritte for "Getting started" | Section 1.2 |
| ENDE-07 | Apply | Gutschein anwenden | Gutschein einlösen | Section 1.1 |
| ENDE-08 | Genitive | {name}'s Projekt | Projekt von {name} | DE-10 |
| ENDE-09 | Legal | Abo beenden on the § 312k button | Verträge hier kündigen | DE-14 |

### DEEN: German to English

| ID | German | Avoid | Prefer | Rule |
|---|---|---|---|---|
| DEEN-01 | Hinweis | Hint | Note | |
| DEEN-02 | aktuell | actual | current, latest | |
| DEEN-03 | eventuell | eventually | possibly | |
| DEEN-04 | kontrollieren | control | check | |
| DEEN-05 | Handy | handy | mobile phone | |
| DEEN-06 | Abbrechen | Abort | Cancel | "Abort" only in technical contexts |
| DEEN-07 | Bitte beachten Sie | Please note that … everywhere | Note: … | |
| DEEN-08 | Anmelden | Register (when it means sign in) / Sign in (when it means enroll) | Check context: anmelden means sign in, but sich zu etwas anmelden means register for something | |
| DEEN-09 | Datenschutz, Impressum | Data protection, Imprint | Privacy, Legal notice | Legal pages may keep the German term in parentheses |

## 7. English to Spanish and Spanish to English

### ENES: English to Spanish

| ID | Type | Avoid | Prefer | Rule |
|---|---|---|---|---|
| ENES-01 | Punctuation | Eliminar este archivo? | ¿Eliminar este archivo? | ES-01 |
| ENES-02 | False friends | soportado, librería, actualmente, remover (es-ES) | compatible or admitido, biblioteca, en realidad, quitar | ES-07, ES-08, ESES-01 |
| ENES-03 | Translationese | fue guardado exitosamente | Cambios guardados | ES-05 |
| ENES-04 | Headings | Creando un proyecto | Crear un proyecto | ES-06 |
| ENES-05 | Style | Realizar una búsqueda | Buscar | ES-09 |
| ENES-06 | Inclusiveness | Bienvenido | Te damos la bienvenida | ES-04 |
| ENES-07 | Plural | 1.000.000 archivos | 1.000.000 de archivos | ES-13 |
| ENES-08 | Regional | Spain terms in es-419, or the reverse | Section 9 | ES419-01 |

### ESEN: Spanish to English

| ID | Spanish | Avoid | Prefer | Rule |
|---|---|---|---|---|
| ESEN-01 | Realizar | Realize | Do, make, complete, or the specific verb | |
| ESEN-02 | Ingresar | Ingress | Enter, sign in | |
| ESEN-03 | Consultar | Consult | View, check, look up | |
| ESEN-04 | Actualmente | Actually | Currently | |
| ESEN-05 | Asistir a (una reunión) | Assist at | Attend | With a person as object, asistir means help or assist |
| ESEN-06 | Exitosamente / con éxito | Successfully | Drop | EN-06 |
| ESEN-07 | Datos | Datas | Data | |

## 8. en-US and en-GB

See `locales/en.md` section 5 for the spelling and vocabulary tables and the ENGB mistakes.

## 9. es-ES and es-419

Proposed term choices. Each column is a default for that variant, not proof that the other word is unknown there.

| Concept | es-ES | es-419 |
|---|---|---|
| Computer | ordenador | computadora |
| Mobile phone | móvil | celular |
| Click (verb) | hacer clic (pinchar is informal) | hacer clic |
| File | archivo (fichero also used) | archivo |
| Enter (text) | introducir | ingresar |
| Expired | caducado | caducado (Chrome); vencido for cards and documents |
| OK (informal agreement) | vale | de acuerdo, OK |
| Take | coger | tomar (coger is vulgar in several countries) |
| Remove | quitar (remover reads as an anglicism) | quitar (remover also used in some countries) |
| Plural you | vosotros | ustedes |
| Recent past in toasts | present perfect (se ha guardado) | simple past (se guardó) |
| Driving | conducir | manejar |
| Ticket (travel) | billete | boleto |
| Link | enlace | enlace (vínculo used by some products) |
| Mouse | ratón | mouse |

## 10. zh-CN and zh-TW

Character conversion between Simplified and Traditional does not change vocabulary. These pairs are common IT and UI term differences. Proposed; check each against the product's existing UI.

| Concept | zh-Hans-CN | zh-Hant-TW |
|---|---|---|
| Software | 软件 | 軟體 |
| File | 文件 | 檔案 |
| Folder | 文件夹 | 資料夾 |
| Sign in | 登录 | 登入 |
| Sign out | 退出登录 | 登出 |
| Account | 账号 | 帳號 |
| Save | 保存 | 儲存 |
| Settings | 设置 | 設定 |
| Search | 搜索 | 搜尋 |
| Import / Export | 导入 / 导出 | 匯入 / 匯出 |
| Apply (settings) | 应用 | 套用 |
| Undo | 撤销 | 復原 |
| Restore | 恢复 | 還原 |
| Information | 信息 | 資訊 |
| Message | 消息 or 信息 | 訊息 |
| Video | 视频 | 影片 |
| Network | 网络 | 網路 |
| Default | 默认 | 預設 |
| Program | 程序 | 程式 |
| Screen | 屏幕 | 螢幕 |
| Print | 打印 | 列印 |
| Support (compatibility) | 支持 | 支援 |
| Data | 数据 | 資料 |
| User | 用户 | 使用者 |
| Project | 项目 | 專案 |
| Activate | 激活 | 啟用 |
| Menu | 菜单 | 選單 |
| Server | 服务器 | 伺服器 |
| Link | 链接 | 連結 |
| Quality | 质量 | 品質 |
| Memory (RAM) | 内存 | 記憶體 |
| Mouse | 鼠标 | 滑鼠 |
| Cursor | 光标 | 游標 |
| Learn more | 了解详情 | 瞭解詳情 or 了解詳情 (both occur in Taiwan) |
| Quotation marks | “ ” | 「」 |

## 11. CJK shared characters

Words written with the same or equivalent Han characters can mean different things in Korean (Sino-Korean reading), Japanese and Chinese. Do not reuse a term because the characters match.

| Characters | ko | ja | zh | UI risk |
|---|---|---|---|---|
| 登錄 / 登録 / 登录 | 등록: register, add | 登録: register, sign up (新規登録) | 登录: sign in | zh 登录 is not "register". ja 登録 is not "sign in". |
| 設定 / 设置 | 설정: settings | 設定: settings; 設置: install (equipment) | 设置: settings | ja 設置 is not Settings. |
| 保存 | 보존: preserve, conserve | 保存: save | 保存: save | Translate ja/zh 保存 as ko 저장, not 보존. |
| 更新 | 갱신: renew (subscription, certificate) | 更新: update, refresh, renew | 更新: update | ja 更新 maps to ko 업데이트, 새로고침, 갱신 depending on the object. |
| 対応 / 對應 | 대응: respond to (an incident) | 対応: supported, compatible, handled | 对应: correspond | ja 対応していません = not supported (ko 지원하지 않습니다). |
| 検討 | 검토: review, examine | 検討: consider | | ja 検討中 = under consideration. |
| 確認 / 确认 | 확인: check, OK, confirm | 確認: check, confirm | 确认: confirm | One word covers several English actions (EN-04). |
| 確定 / 确定 | 확정: finalize | 確定: finalize, confirm a conversion | 确定: OK (dialog button) | zh 确定 as a button is OK, not "finalize". |
| 退出 | 퇴출: expulsion | 退出: leave (a room) | 退出: exit, sign out | zh 退出登录 is sign out; ko 퇴출 is never sign out. |
| 應用 / 应用 | 응용: application (applied use) | 応用: applied use | 应用: app; apply | zh 应用 can be "app" or "apply"; name the object. |
| 案内 / 안내 | 안내: notice, guidance, information | 案内: guide, information | | Not "guidance" in English (KOEN-08, JAEN-05). |
| 解約 / 해약 | 해약 (rare in UI; 해지 is common) | 解約: cancel a contract | | ko subscription cancellation is usually 해지 or 취소. |
| 削除 / 삭제 | 삭제: delete | 削除: delete and remove | 删除: delete | ja uses 削除 for both delete and remove (JA-17). |

### Korean and Japanese directly

When translating ja → ko or ko → ja without English, the shared vocabulary makes literal transfer tempting:

- ja 〜を行う / ko ~를 진행하다: both are nominalization habits; neither should be copied into the other as a calque of the other's habit.
- ja 〜させていただく does not map to ko ~하겠습니다 in every case; use the target product register (합니다체 by default in this skill).
- A Japanese loanword does not imply that Korean uses the same loanword, or a loanword at all (ja キャンセル vs ko 취소; ja コピー vs ko 복사).
- Counters differ: ja ファイル3件 vs ko 파일 3개.
- Quotation: ja 「保存」 vs ko '저장' or "저장" by product style.

## 12. Pivot translation through English

If the source is French, German or Spanish (or Korean, Japanese, Chinese) and the target is another non-English language, translate from the original when possible. A pivot through English loses:

- Grammatical gender and formality (Sie and du both become "you").
- Concept splits that English collapses: fr "Annuler" may be Undo or Cancel; English "Cancel" then becomes de "Abbrechen" when the source meant Undo ("Rückgängig machen").
- Regional choices (es-ES vs es-419, zh-CN vs zh-TW).

When a pivot is unavoidable, carry the concept ID and the original string alongside the English text, and resolve the concept from the original.
