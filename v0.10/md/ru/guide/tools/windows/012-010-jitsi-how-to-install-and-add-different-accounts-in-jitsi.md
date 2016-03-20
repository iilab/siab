

---

lang: ru
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: Jitsi - How to Install and Add Different Accounts in Jitsi

---

- [**Установка Jitsi**](#2.1)
- [**Добавление аккаунтов в Jitsi**](#2.2)
- [**Добавление аккаунта Gmail/Google**](#2.2.1)
- [**Создание аккаунта Jabber/XMPP или SIP и добавление его в Jitsi**](#2.2.2)
- [**Добавление аккаунта Facebook**](#2.2.3)
- [**2.3 How to change password for account with Jitsi**](#2.3)
- [**2.4 How to configure Jitsi to improve it's security**](#2.4)
- [**2.4.1 Disable and remove call and chat history**](#2.4.1)
- [**2.4.2 Require private messaging when text chatting**](#2.4.2)
- [**2.4.3 Protect passwords to your accounts with master password**](#2.4.3)

<a name="2.1"></a>
## Установка Jitsi ##

- Запускаем исполняемый файл. Первый экран программы "Jitsi Setup" с общей информацией. Нажимаем "Next".
- Лицензионное соглашение. Ставим галочку в поле "I accept the terms of the License Agreement" (мы согласны) и снова нажимаем "Next".
- Выбор папки установки. Кнопка "Change" поможет, если вы захотите сменить папку.
- Окно "Additional Tasks" (дополнительные задачи). Оставляем все как есть и нажимаем "Next".
- **Jitsi** сообщает, что все готово к установке. Нажимаем кнопку "Install".

![](/sbox/screen/jitsi-ru/01.png)

- Когда установка завершена, вы увидите окно с галочкой в поле "Launch Jitsi" и кнопкой "Finish". Нажимаем на эту кнопку.
- В Windows вы можете увидеть сообщение брандмауэра (межсетевого экрана), который ограничивает функции **Jitsi** в публичных местах. Если вы увидите такое окно

![](/sbox/screen/jitsi-ru/02.png)

не пугайтесь. Это предупреждение вполне нормально для **Windows**. Даже если вы не станете ничего выбирать, а просто закроете это окно, **Jitsi** все равно сможет связываться с миром через обычные публичные серверы, такие как **Jabber/XMPP или SIP**, **Google Chat** и **Facebook Chat** или **Yahoo Messenger**. Впрочем, если вы щелкаете по кнопке "Разрешить доступ", то в **Jitsi** будет доступна функция "SIP-аккаунтов без регистрации". Более подробную информацию об этих специальных аккаунтах можно узнать, если обратиться к материалу [**SIP-аккаунты без регистрации**](https://jitsi.org/Documentation/RegistrarlessSIPAccount).  

![](/sbox/screen/jitsi-ru/03.png)

- Это окно входа в **Jitsi**.

<a name="2.2"></a>
## Добавление аккаунтов в Jitsi ##

Как добавить аккаунт? **Jitsi** поддерживает много разных типов аккаунтов, главным образом, по протоколам связи **Jabber/XMPP** и **SIP**. Среди прочих **Jitsi** поддерживает аккаунты **Gmail** и **Facebook**, одни из наиболее популярных в Интернете. Далее мы рассмотрим, как добавить эти аккаунты в **Jitsi** и повысить уровень безопасности для этих аккаунтов. Независимое шифрование **Jitsi** выгодно усиливает безопасность, которую гарантируют провайдеры. Учтите, однако, что несмотря на шифрование **Jitsi**, провайдеры вроде **Google** и **Facebook** отслеживают сам факт вашего подключения (и, возможно, вашего адресата) и могут делиться этой информацией с третьими сторонами, например, другими компаниями и правительствами. Поэтому может быть разумно вообще не использовать эти сервисы для важной переписки, даже с шифрованием **Jitsi**. В этом руководстве мы расскажем, как создать более безопасный аккаунт (Jabber/XMPP или SIP) и добавить его в **Jitsi**; такие аккаунты мы советуем использовать вместо обычных.

<a name="2.2.1"></a>
### Добавление аккаунта Gmail/Google ###

**Примечание.** Мы рассматриваем в качестве примера аккаунт **Google Talk**. Настройки для других протоколов связи, которые видны на картинке, похожи по своей сути. Иногда сама связь или некоторые функции (в частности, независимое шифрование **Jitsi** текстовых и голосовых сообщений - **OTR** и **ZRTP**) могут не работать между двумя и более пользователями разных провайдеров (например, Facebook, Gmail, Yahoo и т.д.). Однако, между аккаунтами одного и того же провайдера все должно работать.

- **Пуск > Jitsi**, или запускаем **Jitsi** по щелчку на иконке на рабочем столе.
- Вводим логин и пароль аккаунта **Gmail**, который вы хотите использовать для чатов.

![](/sbox/screen/jitsi-ru/04.png)

- Щелкаем по кнопке "Войти".

**Примечание.** Вы можете использовать несколько аккаунтов с разными протоколами одновременно. 

![](/sbox/screen/jitsi-ru/05.png)

**Примечание.** Если вы случайно закрыли окно входа или просто хотите добавить другой аккаунт, вы можете это сделать через меню *Файл* > *Добавить новую учетную запись...*. В новом окне указываем сеть (например, *Google Talk*), вводим имя пользователя и пароль  **Gmail** account as shown on the image below:

![](/sbox/screen/jitsi-ru/06.png)

Хотите убедиться, что ваш аккаунт связан с **Jitsi**? Выберите в меню программы *Инструменты* > *Опции*:

![](/sbox/screen/jitsi-ru/07.png)

В открывшемся окне видно, что наш аккаунт (в данном случае тестовый) связан с **Jitsi**.

**Примечание.** Если вы используете [двухэтапную аутентификацию](https://support.google.com/accounts/answer/180744?hl=ru) для защиты доступа к своему аккаунту **Gmail**, то при попытке залогинивания в **Jitsi** со своим обычным паролем вы можете получить сообщение об ошибке. Тогда для входа в **Jitsi** нужно использовать "пароль приложения". Подробнее о паролях приложений можно узнать [в документации Google](https://support.google.com/accounts/answer/185833?hl=ru).

![](/sbox/screen/jitsi-ru/08.png)

<a name="2.2.2"></a>
### Создание аккаунта Jabber/XMPP или SIP и добавление его в Jitsi ###

**Jabber/XMPP** и **SIP** - открытые стандарты для текстовых и голосовых сообщений. ation. Есть [много серверов](https://xmpp.net/directory.php), которые предлагают бесплатные аккаунты для использования с **Jitsi**. Ниже мы порекомендуем некоторые серверы. Вы сможете использовать их для передачи важной информации. [Серверное программное обеспечение Jabber/XMPP](http://xmpp.org/xmpp-software/servers/) (например, [ejabberd](http://www.process-one.net/en/ejabberd/) или [Prosody IM](http://prosody.im/)) можно скачать, установить на свой сервер и настроить для частных коммуникаций внутри вашей группы, организации или сообщества.

* Аккаунт Jabber/XMPP от **Riseup.net**

Если у вас уже есть учетная запись в [системе безопасной почты Riseup.net](/ru/riseup_main) (США), вы можете [использовать этот аккаунт и для связи по протоколу Jabber/XMPP](https://www.riseup.net/en/chat). Нужно просто добавить аккаунт в **Jitsi**. Ниже мы показываем, как добавить существующий аккаунт Jabber/XMPP.

* Аккаунт Jabber/XMPP от **Jabber.ccc.de** и другие

Можно зарегистрировать аккаунт на сервере Jabber.ccc.de (Германия).

- В программе **Jitsi** выбираем в меню *Файл* > *Добавить новую учетную запись...*. 
- В строке "Сеть" выбираем *XMPP*, *Создать новую учетную запись XMPP*. В поле *Сервер* указываем *jabber.ccc.de*. В поле *"Имя пользователя XMPP* вводим желаемое имя пользователя. Придумываем пароль и вводим его два раза (в поля *"Пароль"* и *"Подтвердите пароль"*). Поле *"Порт"* оставляем без изменений.

![](/sbox/screen/jitsi-ru/09.png)

- Щелкаем по кнопке "Добавить". После успешной регистрации вы снова увидите рабочее окно **Jitsi**. В меню *Инструменты* - *Опции* теперь можно видеть две учетные записи:

![](/sbox/screen/jitsi-ru/10.png)

Если вы выберете имя пользователя, которое уже занято, программа сообщит об ошибке.

**Примечание.** Если вы не работаете со своим аккаунтом jabber.ccc.de больше 12 месяцев, аккаунт будет автоматически удален с сервера, а имя пользователя станет доступно для регистрации другими клиентами.

Еще один сервер Jabber/XMPP, о котором стоит упомянуть - **jit.si**. Этот сервер поддерживают сами разработчики программы **Jitsi**. Можно регистрировать аккаунт на [**jit.si**](https://jit.si) и многих других серверах Jabber/XMPP. Последовательность действий будет такая же, как описано выше. Группа IM Observatory поддерживает [список и рейтинг открытых серверов Jabber/XMPP](https://xmpp.net/directory.php), а также дает возможность [протестировать любой Jabber/XMPP-сервер с точки зрения безопасности](https://xmpp.net/index.php).

* Аккаунт SIP от **ostel.co**

Аккаунты **SIP** нельзя зарегистрировать из **Jitsi**. Следует обратиться к серверу **ostel.co** (США), который предлагает [зарегистрироваться](https://ostel.co/users/sign_up). Щелкаем кнопку "Sign Me Up!", выбираем имя пользователя и пароль. Указываем действующий адрес e-mail и щелкаем по кнопке. После успешной регистрации на сайте ostel.co возвращаемся в **Jitsi**. Выбираем в меню *Файл* > *Добавить новую учетную запись...*. В поле "Сеть" указываем *SIP*, а в поле "Идентификатор SIP" - имя пользователя, которое вводили на сайте ostel.co (в формате имя_пользователя@ostel.co). Вводим пароль, щелкаем "Добавить".

![](/sbox/screen/jitsi-ru/11.png)

SIP-аккаунт добавлен в **Jitsi**.

![](/sbox/screen/jitsi-ru/12.png)

Если у вас уже есть аккаунт Jabber/XMPP или SIP, можете добавить его в **Jitsi** через меню *File* > *Добавить новую учетную запись...*** и выбрав соответствующий тип сети (XMPP или SIP соответственно).

<a name="2.2.3"></a>
### Добавление аккаунта Facebook ###

Есть две опции **Facebook**, которые нам нужно проверить перед тем, как **Jitsi** сможет использовать Facebook Chat.

* **Имя пользователя Facebook**

Что такое имя пользователя **Facebook**? Нет, мы говорим не о вашей реальной фамилии, которую вы можете использовать в этой социальной сети. Тогда что же?  Зайдите в **Facebook** и посмотрите, что написано в панели вашего браузера после адреса *https://www.facebook.com/*, когда вы находитесь на своей "стене". Кроме того, имя пользователя фигурирует в адресе электронной почты **Facebook** (например, username@facebook.com). В настойках **Facebook** можно изменить имя пользователя; кроме того, это может быть сделано r change the username or get one by going to your *Account Settings* > *General* section or by visiting [https://www.facebook.com/username](https://www.facebook.com/username). To set username **Facebook** may ask you for your account verification which may require sending SMS to a mobile phone number which you will need to provide to **Facebook** in the process of verification. For more details see [Facebook’s explanation of usernames](https://www.facebook.com/help/329992603752372/).

* **App Settings**

**Facebook’s** “application platform” must be turned on before **Jitsi** can connect to Facebook Chat. Visit your **Facebook** *Account Settings > Apps* section and check that the setting for *Apps you use* is turned *On*. This turns "application platform" on for your account.

**Note** that that turning **Facebook**’s "application platform" opens up much of your **Facebook** data to third-party application developers. This data is available not only to the **Facebook** applications that you use, but also **Facebook** applications used by any of your friends. After turning on **Facebook**’s "application platform", be sure to check the settings under "Apps others use". This setting allows you to hide some personal information from applications used by your friends. Unfortunately, **Facebook** does not offer settings to hide all personal information. Certain categories of information (like your friend list, gender, or info you have made public) are visible as long as **Facebook**’s "application platform" is turned "on". It is up to you to determine whether this is an acceptable tradeoff of your privacy.

Now you are prepared to add your **Facebook** account to **Jitsi**. To do this follow the steps below:

**Step 1**.  From the main menu **select *File > Add New Account...***

**Step 2**.  In the Add New Account dialogue, **Network** menu choose *Facebook*, **enter your username and password** and **Click "Add"**
 
![](/sbox/screen/jitsi-en/16.png)

*Figure 10: Example of "Add new account..." window for a Facebook account*


<a name="2.3"></a>
## 2.3 How to change password for account with Jitsi ##

It is important element of security to know how to change the password for each account that one has. Many of the accounts that you can use with Jitsi offer changing password as a part of their setings, which are accessible over web interface. However some Jabber/XMPP and SIP account will not have any web interface to manage them. You can change password for those account using Jitsi by following steps below:

**Step 1**. **select *Tools* > *Options*** in the menu, **select** the ***Accounts*** tab

![](/sbox/screen/jitsi-en/17.png)

*Figure 11: Options window with one account selected*

**Step 2**. **click on *Edit*** button on the bottom to activate following window:

![](/sbox/screen/jitsi-en/18.png)

*Figure 12: Account Registration Wizard window with Change account password button on the bottom*

**Step 3**. **click on *Change account password*** to activate *Change account password* window:

![](/sbox/screen/jitsi-en/19.png)

*Figure 13: Change account password window*

**Step 4**. ***Enter new password* and *Re-enter password*** and **click on *OK*** button to close this window.

**Step 5**. Close Account Registration Wizard.

<a name="2.4"></a>
## 2.4 How to configure Jitsi to improve it's security ##

<a name="2.4.1"></a>
### 2.4.1 Disable and remove call and chat history ###

**Jitsi** by default stores information about the incoming and outgoing voice/video calls and the history of your text chats -- all messages that you sent and received. You can access voice/video calls by **clicking** on the clock icon on the main Jitsi window:

![](/sbox/screen/jitsi-en/20.png)

*Figure 14: Top of the Jitsi main window with call history button indicated*

You can see the text chat history by **clicking** on the egg-timer like icon in the text chat window while chatting with a contact:

![](/sbox/screen/jitsi-en/21.png)

*Figure 15: Chat window with chat history button indicated*

This information is collected and stored on the disk of your computer. **Even if you encrypt the text chat with OTR all the text messages you send and receive are stored on your computer in open text format.** The same information is collected and stored on the disk of the contacts you are communicating with. 

To prevent Jitsi collecting this information (and remove already gathered data), **you and your contact should take the following steps**.

#### To disable Jitsi from collecting the information: ####

**Step 1**.  **select *Tools* > *Options*** in the menu, **select** the ***General*** tab and **uncheck** the ***Log chat history*** option as shown below:

![](/sbox/screen/jitsi-en/22.png)

*Figure 16: "Options" window, "General" tab with "Log chat history" option unchecked*

**Step 2**. in the *Options* window, first **select the *Advanced*** tab, then **select the *Logging*** section, and then **uncheck the *Enable packet logging*** option as shown below: 

![](/sbox/screen/jitsi-en/23.png)

*Figure 17: "Options" window, "Advanced" tab, "Logging" section with "Enable packet logging" unchecked*

Your changes will take effect after you **restart Jitsi**.

#### To remove already collected information about your calls and text messages: ####

**Step 1**. **Quit** Jitsi.

**Step 2**. Remove the entire log history folder *history_ver1.0* from the **Jitsi** *user profile* folder. You can remove a sub-folder of *history_ver1.0* if you want to dispose of only part of the history. The location of the *user profile* and *log history* folders depends on the operating system:

* On Windows XP and earlier, this is located in *C:\Documents and Settings\&lt;Windows login/user name&gt;\Application Data\Jitsi\history_ver1.0*
* On Windows Vista, 7, 8, this is *C:\Users\&lt;Windows login/user name&gt;\AppData\Roaming\Jitsi\history_ver1.0* (**Note** that "AppData" folder may be hidden. See [how to see hidden files](http://windows.microsoft.com/en-us/windows/show-hidden-files)).
* Mac OS X: from your home folder *~/Library/Application Support/Jitsi/history_ver1.0*
* Linux: from your home folder *~/.jitsi/history_ver1.0* (**Note** that the ".jitsi" folder may be hidden. See [how to see hidden files in Ubuntu](http://itsfoss.com/hide-folders-and-show-hidden-files-in-ubuntu-beginner-trick/))

See the [How to destroy sensitive information](/en/chapter-6) chapter for more on how to dispose of information securely.

<a name="2.4.2"></a>
### 2.4.2 Require private messaging when text chatting ###

It is recommended that you set **Jitsi** up to require private and encrypted text messaging using [*OTR*](/en/glossary#OTR) [*encryption*](/en/glossary#encryption) whenever possible. To do this, **select *Tools* > *Options*** in the menu, **select the *Security*** tab, **select the *Chat*** sub-tab and **check *Require private messaging*** at the bottom of the screen as shown below:

![](/sbox/screen/jitsi-en/24.png)

*Figure 18: "Options" window, "Security" tab, "Chat" sub-tab with "Require private messaging" option indicated*

<a name="2.4.3"></a>
### 2.4.3 Protect passwords to your accounts with master password ###

It is best not to let Jitsi remember passwords to your accounts. If you decide otherwise for ease of use anybody who gets access to your computer will be able to log in to your accounts by simply starting Jitsi. It will also be possible to view your passwords in the *Options* window. It is therefore **strongly recommended** to protect passwords to your accounts with good **master password**. Once you set up  the master password, Jitsi will ask you for it upon starting the program.

**Step 1**. **Open** the *Options* window by **selecting *Tools* > *Options*** in the menu, **select the *Security*** tab and ***Passwords*** sub-tab, and **check *Use a master password*** to activate the ***Master Password*** window.

**Step 2**. In the new window **type in your password** as shown in the picture below. For more on creating a strong password, see [***How to create and maintain secure passwords***](/en/chapter-3).

![](/sbox/screen/jitsi-en/25.png)

*Figure 19: The "Master Password" window*

**Step 3**. **Click *OK*** to confirm the password and activate a new window which should say ***Master Password successfully set up***. **Click "OK"** to close it and come back to the *Options* window which should resemble below:

![](/sbox/screen/jitsi-en/26.png)

*Figure 20: "Options" window, "Security" tab, "Passwords" sub-tab with the "Use a master password" option indicated*	

**Note**: The ***Change Master Password*** button lets you change the master password and the ***Saved Passwords...*** button lets you access the list of passwords remembered by Jitsi and remove them if need be.


