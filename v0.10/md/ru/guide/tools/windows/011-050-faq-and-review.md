

---

lang: ru
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 5
depth: 3
title: FAQ and Review

---

<div class="background" markdown="1">
## Вопросы ##

**Вопрос:** Существуют ли другие клиенты мгновенных сообщений, которые поддерживают OTR?

**Ответ:** Да, например, Miranda (<a href="http://miranda-im.org" class="ext-link">http://miranda-im.org</a>).

**Вопрос:** Можно ли установить Pidgin на два компьютера, но пользоваться одним аккаунтом ICQ?

**Ответ:** Можно, однако придется создавать ключ и проходить процедуру аутентификации на каждом компьютере отдельно.

**Вопрос:** Что если наоборот: компьютер один, а ICQ-аккаунтов несколько? Можно ли настроить одну рабочую копию Pidgin на использование нескольких аккаунтов?

**Ответ:** Можно.

**Вопрос:** Если у меня Pidgin, а у друга, скажем, &quot;стандартная&quot; программа ICQ, сможем ли мы общаться?

**Ответ:** Сможете. Главное, чтобы вы оба общались в одной и той же системе (по протоколу ICQ). Тогда неважно, какой именно клиент установлен у вас или у него. Однако &quot;стандартная&quot; программа ICQ не поддерживает OTR, поэтому защищенного разговора в такой связке не получится.

**Вопрос:** Существует ли портативная версия Pidgin, которая может работать, например, с USB-флешки?

**Ответ:** Да, портативная версия доступна для скачивания с сайта <a href="http://portableapps.com/" class="ext-link">http://portableapps.com</a>.
</div>

## Мини-тест ##

**1. Можно ли связываться двум пользователям ICQ, один из которых использует Pidgin, а другой – &quot;стандартную&quot; программу ICQ?**

- Можно
- Можно, если эта версия программы ICQ входит в список программ, поддерживаемых Pidgin
- Можно, если в программе ICQ установлен дополнительный модуль поддержки Pidgin
- Нет, нужно, чтобы программы были одинаковые

**2. Как устанавливается OTR?**

- Входит в состав Pidgin и включается по умолчанию
- Входит в состав Pidgin, но требует активации вручную
- Устанавливается как дополнительный модуль Pidgin
- Устанавливается как отдельно запускаемая, независимая программа

**3. Как инициируется OTR-защита разговоров в Pidgin?**

- Делается автоматическая попытка включить защиту; если не получается, разговор продолжается без защиты
- Делается автоматическая попытка включить защиту; если не получается, разговор не идет
- Включение защиты производит только сам пользователь (вручную)
- По выбору пользователя может быть установлен любой из этих режимов

**4. Что нужно создать прежде, чем пользоваться OTR?**

- OTR-аккаунт
- Шифровальный ключ
- Пароль для доступа к OTR
- Персональный сертификат

**5. Как подтвердить доверие собеседнику?**

- Щелкнуть по кнопке &quot;Я доверяю этому собеседнику&quot
- Использовать встроенную в Pidgin процедуру аутентификации
- Подписать его открытый ключ своим закрытым ключом
- Все собеседники по умолчанию обладают доверием, ничего подтверждать не нужно

**6. Сообщения, защищенные OTR, ...**

- ...всегда записываются в журнал
- ...никогда не записываются в журнал
- ...записываются в журнал по выбору пользователя
- ...записываются в журнал, исходя из смысла/секретности информации

**7. Что из написанного ниже можно назвать &quot;отпечатком&quot; в терминологии Pidgin?**

- Sincerely yours, Mike Goldblum
- CE300980 7D3EA5B0 4E2F249C D4C6C1D5 2CFA68B1
- f&amp;3<span class="new ticket">#8</span>sfj*1
- Ну, такие капиллярные линии...

*(Хотите [проверить правильность своих ответов](/ru/test#pidgin)?)*

