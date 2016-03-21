

---

lang: ru
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Export and Import Keys

---

- [**Как экспортировать свой открытый ключ**](#3.1)
- [**Как импортировать чужой открытый ключ**](#3.2)
- [**Как проверить открытый ключ**](#3.3)

<a name="3.1"></a>
## Как экспортировать свой открытый ключ ##

Перед тем, как обмениваться шифрованными сообщениями, нужно обменяться с адресатом открытыми ключами. Чтобы другие люди могли посылать вам шифровки, они должны использовать ваш открытый ключ. Но он хранится "где-то в программе", не так ли? Давайте его экспортируем. 

Щелкаем по кнопке Менеджера ключей.

![](/sbox/screen/gpg4usb-ru/02.png)

Выбираем ключ (ставим галочку рядом с именем) и щелкаем на панели управления по кнопке "Экспортировать в файл". Сохраняем файл на диск.

![](/sbox/screen/gpg4usb-ru/09.png)

Файл будет иметь несколько длинное и корявое название вроде *John Doe johndoe@gmail.com(015A8EAF8C28FA30)_pub* и расширение *.asc*. Суффикс *pub* в имени файла указывает, что экспортирован только открытый ключ (public key). Кстати, этот файл имеет обычный текстовый формат: при желании можете заглянуть внутрь с помощью какого-нибудь редактора (например, "Блокнота") и посмотреть, как он выглядит.

![](/sbox/screen/gpg4usb-ru/10.png)

Фраза "BEGIN PGP PUBLIC KEY BLOCK" означает "Начало блока открытого ключа PGP". Это стандарт для всех открытых ключей. 

Gpg4usb позволяет не только сохранять выбранный ключ на диск, но и копировать его в буфер обмена с помощью соседней кнопки на панели инструментов Менеджера ключей:

![](/sbox/screen/gpg4usb-ru/11.png)

<a name="3.2"></a>
## Как импортировать чужой открытый ключ ##

Чтобы посылать шифрованные сообщения другу, вам нужно использовать его открытый ключ. Предположим, друг успел экспортировать свой ключ (как показано выше) и отправить вам файл с ключом. Наша задача — импортировать этот ключ в нашу программу gpg4usb.

Щелкаем по кнопке импорта ключей на панели инструментов. В появившемся списке выбираем первый пункт "Файл".

![](/sbox/screen/gpg4usb-ru/12.png)

Находим на диске файл с ключом, выбираем его и убеждаемся, что ключ нашего друга появился в списке.

<a name="3.3"></a>
## Как проверить открытый ключ ##

Иногда можно быть вполне уверенным, что полученный вами открытый ключ действительно принадлежит вашему другу (например, если он передает вам его лично в руки на флэшке). Но часто прямой связи нет. При определенных обстоятельствах злоумышленник может подсунуть вместо ключа друга другой, "фальшивый", иначе говоря — свой собственный. И тогда злоумышленник сможет прочесть шифрованное сообщение, которое вы отправили другу (а вот друг не сможет). Как удостовериться, что ключ настоящий?

- **Свяжитесь** с другом по какому-нибудь другому каналу связи, например, по Skype.
- **Удостоверьтесь,** что действительно говорите с нужным человеком (звук его голоса и картинка помогут рассеять сомнения).
- Попросите друга передать вам **отпечаток его ключа.**

Отпечаток ключа — серия знаков, которой сопровождается каждый ключ. Сам по себе он не секретный, но уникальный. Если отпечаток того ключа, который вы получили (например) по электронной почте, и отпечаток, которым поделился ваш друг в Skype, совпадут, значит, у вас в руках правильный, настоящий ключ.

Чтобы увидеть отпечаток, достаточно щелкнуть правой кнопкой мыши по ключу и выбрать в контекстном меню "Показать свойства ключа".

![](/sbox/screen/gpg4usb-ru/13.png)

В появившемся окне можно видеть отпечаток ключа. Соседняя кнопка позволяет скопировать отпечаток в буфер обмена.

Вашему адресату нужно повторить эти шаги. Убедитесь, что отпечатки совпадают. Если нет, попробуйте снова обменяться открытыми ключами (возможно, через другие адреса e-mail или вообще другим способом связи) и еще раз проверьте отпечатки. Если они полностью совпадают, можно быть уверенным, что вы обладаете правильными ключами.
