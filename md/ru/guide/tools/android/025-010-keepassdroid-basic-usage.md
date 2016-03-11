

---

lang: ru
community: guide
type: tools
legacy: True
child: True
os: android
weight: 1
depth: 3
title: KeePassDroid - Basic Usage

---

- [**Установка KeePassDroid**](#2.0)
- [**Создание базы паролей**](#2.1)
- [**Добавление записи**](#2.2) 
- [**Работа с паролями**](#2.3)

<a name="2.0"></a>
## Установка KeePassDroid ##

- Устанавливаем связь Android-устройства с интернетом, заходим на страницу **KeePassDroid** в [**Google Play**](https://play.google.com/store/apps/details?id=com.android.keepass).

![](/sbox/screen/keepassdroid-ru/001.png)

- Нажимаем на кнопку *"Установить".* Вы увидите, к каким ресурсам вашего устройства **KeePassDroid** хочет получить доступ. Если согласны с этими условиями, нажмите *"Принять".*

![](/sbox/screen/keepassdroid-ru/002.png)

- Может появиться дополнительное окно с предупреждением о том, что программу имеет смысл скачивать только при достаточно хорошем соединении wi-fi. Нажимаем *"Продолжить".* 

![](/sbox/screen/keepassdroid-ru/003.png)

- Когда программа установлена, можно запустить ее.

![](/sbox/screen/keepassdroid-ru/004.png)

**Примечание.** Программа **KeePassDroid** также может быть установлена [непосредственно с сайта Google](https://code.google.com/p/keepassdroid/downloads/list?can=1&q=) или альтернативного сайта [F-Droid](https://f-droid.org/repository/browse/?fdfilter=keepass&fdid=com.android.keepass).

<a name="2.1"></a>
## Создание базы паролей ##

Все пароли хранятся в защищенной базе, которую нужно создать.

![](/sbox/screen/keepassdroid-ru/005.png)

- Щелкаем по значку программы и запускаем **KeePassDroid**.

![](/sbox/screen/keepassdroid-ru/006.png)

- Поскольку базы еще нет, щелкаем по кнопке *Создать*. 

![](/sbox/screen/keepassdroid-ru/007.png)

- Перед нами окно "Изменение пароля базы". Нужно придумать пароль, который будет защищать базу от несанкционированного доступа (мастер-пароль). Этот пароль должен быть уникальным и стойким. Этот пароль вам придется запомнить. Только с его помощью вы сможете открывать свою базу паролей. Во второй строке следует повторить пароль.

![](/sbox/screen/keepassdroid-ru/008.png)

**Примечание.** Мастер-пароль можно впоследствии изменить. (Мы рекомендуем периодически менять пароли, включая этот).

**Примечание.** Советуем обратить внимание на главу нашего руководства [**Как создавать и хранить надежные пароли**](/ru/chapter_3_1).

- Поле "Файл-ключ" можно не заполнять. Это поле служит для того, чтобы открывать базу с помощью как пароля, так и привязки к определенному (выбранному вами) файлу. Если выбранный файл отсутствует, база открыта не будет.

- Щелкаем **OK**. Поздравляем, защищенная база для хранения паролей создана.

![](/sbox/screen/keepassdroid-ru/009.png)

**Примечание.** Если вы используете программу **KeePassDroid** или **KeePass** на другом устройстве, можно скопировать базу на это устройство и пользоваться там.

<a name="2.2"></a>
## Добавление записи ##

Для удобства работы **KeePassDroid** хранит информацию о паролях в группах. По умолчанию предлагаются группы **Email** и **Internet**. Эти названия можно изменить, сами группы удалить (если они вам не нужны), и, конечно, вы можете создавать собственные группы. Для этого нужно щелкнуть по кнопке "Новая группа" и ввести название.

![](/sbox/screen/keepassdroid-ru/010.png)

Вы также можете выбрать значок из списка, предложенного **KeePassDroid**.

![](/sbox/screen/keepassdroid-ru/011.png)

Экран добавления записи о пароле содержит несколько полей.

![](/sbox/screen/keepassdroid-ru/012.png)

(Ни одно из полей, кроме первого, не является обязательным).

  - **Название**. У каждой записи о пароле должно быть название, по которому его можно будет опознать и найти в базе. В данном примере это почтовый сервис Gmail.
  - **Логин**. Имя пользователя, которое вместе с паролем служит для входа в систему.
  - **Ссылка**. Адрес интернет-сайта, куда осуществляется вход.
  - **Пароль**: Пароль для доступа к вашему аккаунту. Рядом находится кнопка генератора паролей - удобного способа придумывать случайный пароль.
  - **Подтверждение**. Повторный ввод пароля.
  - **Комментарий**. Здесь можно указать любую информацию. Например, настройки почтового сервера: *POP3 SSL, pop.gmail.com, Port 995; SMTP TLS, smtp.gmail.com, Port: 465*.

**Примечание.** Изменяя пароль в базе **KeePassDroid**, вы не изменяете его автоматически на сайте. **KeePassDroid** - безопасный сейф для хранения паролей. Программа лишь хранит ваши данные, ничего более.

- Нажмите **Сохранить**.

Ваш новый пароль появится в группе.

<a name="2.3"></a>
## Работа с паролями ##

Хранимый в **KeePassDroid** пароль может быть весьма длинным и сложным, запомнить его нелегко. К счастью, можно копировать пароль из базы в буфер памяти, а затем вставлять в приложение.

- Открываем базу паролей и запись с нужным паролем.
- Щелкаем по кнопке меню программы.

![](/sbox/screen/keepassdroid-ru/013.png)

- Открывается окно с несколькими позициями. Здесь можно выбрать и поместить в буфер памяти логин или пароль.

![](/sbox/screen/keepassdroid-ru/014.png)

- Открываем нужный сайт (как вариант - приложение), щелкаем по соответствующему полю, а затем по всплывающему слову *"Вставить"*.

![](/sbox/screen/keepassdroid-ru/015.png)
