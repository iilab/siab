

---

lang: ru
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: How to Install gpg4usb and Generate a Key Pair

---

Распаковываем архив zip в папку на диске и запускаем приложение **start_windows.exe.** Открывается главное окно программы.

![](/sbox/screen/gpg4usb-ru/01.png)

Перед тем, как что-то зашифровывать (или расшифровывать), нужно выполнить два важных шага: во-первых, создать пару ключей (открытый и секретный), во-вторых, обменяться открытыми ключами с вашими адресатами. О том, как экспортировать открытый ключ из программы, поговорим в следующей части, а сейчас создадим пару ключей.

**Внимание:** Мы описываем запуск "мастера создания ключей" в общем случае (через меню программы). В случае, если **gpg4usb** только что установлена на компьютер, мастер создания ключей запустится автоматически. 

Щелкаем по кнопке Менеджера ключей.

![](/sbox/screen/gpg4usb-ru/02.png)

Выбираем в меню "Ключ" — "Генерировать ключ".

![](/sbox/screen/gpg4usb-ru/03.png)

Появляется следующее окно.

![](/sbox/screen/gpg4usb-ru/04.png)

- **Имя** — имя владельца ключа. Служит для визуального опознания, кому принадлежит ключ (что-то вроде имени на шкафчике). Лучше использовать латиницу, так как не все программы шифрования сегодня "понимают" кириллицу. Из соображений безопасности вы можете не указывать свое настоящее имя. Однако, следует понимать, что этим вы можете сбить с толку тех, кто с вами обменивается шифрованными сообщениями.

- **Адрес email** — адрес электронной почты. Справедливо все то, о чем написано в предыдущем абзаце.

- **Комментарий** — можно пропустить.

- **Истекает** — дата окончания действия ключа. По достижении этой даты открытый ключ уже нельзя будет использовать для шифрования. Обычно это ограничение служит дополнительной страховкой на случай, если ключевая пара окажется скомпрометирована (злоумышленник, завладевший ключами, по крайней мере, не сможет пользоваться ими вечно). Если вам это не нужно, ставим галочку в поле "без срока годности".

- **Длина ключа (бит)** — чем длиннее ключ, тем надежнее защита и дольше длится шифрование/расшифровка. Значение по умолчанию (2048 бит) вполне достаточно.

- **Пароль** — пароль для защиты секретного ключа. (Загляните в раздел ["Как создавать и хранить надежные пароли"](/ru/chapter-3)).

Щелкните по кнопке "ОК".

![](/sbox/screen/gpg4usb-ru/05.png)

По окончании появится финальное окошко:

![](/sbox/screen/gpg4usb-ru/06.png)

Можете убедиться, что ключ появился в списке.

![](/sbox/screen/gpg4usb-ru/07.png)

Значок с двумя ключиками ![](/sbox/screen/gpg4usb-ru/08.png) подразумевает, что это не открытый ключ, а пара ключей (открытый и секретный).

Теперь, когда вы успешно создали пару ключей, нужно экспортировать открытый ключ из программы, чтобы другие люди могли шифровать письма для вас. И, наоборот, импортировать их ключи, чтобы вы могли посылать им шифрованные сообщения. О том, как это сделать, поговорим в следующей части.
