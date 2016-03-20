

---

lang: ru
community: guide
type: tactics
legacy: True
child: True
weight: 2
depth: 3
title: Communicating (Voice and Messages) via Smartphone

---

### Основы голосовой связи ###

Когда мы говорили про слежку и анонимность ([**глава 10, "Как сделать мобильный телефон максимально безопасным"**](/ru/chapter-10), то обсуждали, что следует предпринять для снижения риска перехвата ("прослушки"). Речь шла о голосовой сотовой связи.

Смартфон умеет подключаться к интернету по сотовой сети или по wi-fi. Разговор можно сделать более безопасным, например, с помощью [*VoIP*](/ru/Glossary#VoIP) и дополнительных средств защиты. Некоторые программы для смартфонов умеют делать это и для обычных мобильных телефонов (см. далее **RedPhone**).

### Skype ###

Самая популярная коммерческая программа VoIP. [*Skype*](/ru/glossary#skype) доступен для всех платформ смартфонов и хорошо работает при надежном соединении wi-fi. Связь по каналам мобильных операторов обычно не так хороша для Skype.

В главе про интернет-пейджеры ([**"Как скрыть Интернет-переписку от посторонних"**](/ru/chapter-7)) мы обсуждали, насколько безопасен Skype и почему его следует (насколько это возможно) избегать. Вкратце: Skype — программа без открытого кода. Очень трудно оценить, безопасен ли Skype на самом деле. Владельцем программы является корпорация Microsoft. Коммерческий интерес — знать, когда вы пользуетесь Skype и откуда. Наконец, Skype может дать правоохранительным органам доступ к истории ваших коммуникаций.

### Другие программы VoIP ###

Обычно использование VoIP не предусматривает оплаты (или заметно дешевле звонков по телефону). Да и следов данных остается куда меньше. Возможно, защищенный звонок VoIP — самый надежный способ связи на сегодняшний день.

[**CSipSimple**](http://f-droid.org/repository/browse/?fdid=com.csipsimple&fdpage=4) — мощный клиент VoIP для платформы Android. **CSipSimple** активно развивается, доступны удобные шаблоны настроек для разных служб VoIP.

[**Open Secure Telephony Network (OSTN)**](https://guardianproject.info/wiki/OSTN) и сервер [**Ostel**](https://ostel.co/), поддерживаемый Guardian, — проект, который сегодня предлагает одно из самых безопасных средств голосовой связи. При использовании **CSipSimple** вы не связываетесь напрямую с вашим собеседником. Все данные проходят через сервер **Ostel.** Поэтому отследить ваш разговор и установить личность собеседников гораздо труднее. Кроме того, **Ostel** не хранит никакие данные (кроме логина и пароля, которые нужны для входа на сервер). Ваши разговоры шифруются. То же касается мета-данных, которые обычно весьма трудно спрятать. Установить программу и начать ею пользоваться весьма просто.

[**RedPhone**](https://play.google.com/store/apps/details?id=org.thoughtcrime.redphone) — бесплатная программа с открытым кодом, которая шифрует голосовые коммуникации. Ее легко использовать, здесь те же понятия, что и в телефонной связи. Ваш собеседник, разумеется, тоже должен установить **RedPhone**. Для простоты **RedPhone** использует в качестве идентификатора номер вашего мобильного телефона (а не логин, как другие сервисы VoIP). Это удобно, однако создает дополнительные риски: становится проще отслеживать трафик и адресатов. В системе **RedPhone** используется центральный сервер, через который проходят все данные. Тот, кто контролирует сервер, вполне может контролировать сами данные.

## SMS ##

В главе 10 ([**"Текстовые сообщения"**](/ru/chapter_10_5)) мы уже говорили, что SMS небезопасны по своей природе. Всякий, кто имеет доступ к мобильной телекоммуникационной сети, в принципе, может легко перехватывать сообщения. Так оно и происходит, причем довольно часто. В критической ситуации не следует полагаться на небезопасные SMS. Нет способа определить подлинность SMS-сообщения. Нельзя сказать наверняка, прошло ли сообщение "как надо" или кто-то изменил содержание по пути. Удостовериться, что письмо отправлено именно тем, кто его подписал, тоже не получится.

[**TextSecure**](https://play.google.com/store/apps/details?id=org.thoughtcrime.securesms) — бесплатная программа с открытым кодом для обмена SMS на смартфонах с ОС Android. Поддерживается шифрование сообщений. Можно использовать с **TextSecure** любое/привычное приложение для SMS. Для шифрования нужно, чтобы **TextSecure** был установлен на смартфонах отправителя и получателя. Программа автоматически определяет, когда на смартфон приходит сообщение, зашифрованное с помощью **TextSecure**. Также можно отправлять шифрованные сообщения сразу нескольким людям. Сообщения снабжаются цифровой подписью, поэтому каким-либо образом изменить их не получится.

### Безопасный чат ###

Обмен мгновенными текстовыми сообщениями по смартфону создает дополнительный поток информации, который подвержен риску. Эти разговоры могут быть использованы злоумышленниками. Поэтому лучше быть особенно осторожным, когда набираете текстовые сообщения на смартфоне. Есть несколько способов повысить безопасность мобильного чата. Лучший — использовать шифрование на стороне и отправителя, и адресата. Вы будете уверены, что общаетесь именно с тем человеком, который нужен. 

Для iPhone и Android-устройств можно рассмотреть приложение [**ChatSecure**](https://chatsecure.org). Программа позволяет применить стойкое шифрование к текстовым сообщениям с помощью протокола [**Off-the-Record**](/ru/glossary#OTR). **ChatSecure** — бесплатная программа с открытым кодом.
