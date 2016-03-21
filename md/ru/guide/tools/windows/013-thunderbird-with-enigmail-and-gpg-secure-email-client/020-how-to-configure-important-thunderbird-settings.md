

---

lang: ru
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Configure Important Thunderbird Settings

---

- [**О настройках безопасности Mozilla Thunderbird**](#3.0)
- [**Отключение предпросмотра**](#3.1)
- [**Отключение HTML**](#3.2)
- [**Прочие настройки безопасности**](#3.3)
- [**Спам-фильтры**](#3.4)

-------

<a name="3.0"></a>
## О настройках безопасности Mozilla Thunderbird ##

Когда мы говорим о безопасности электронной почты, то в первую очередь имеем в виду защиту от вредоносного кода во входящих письмах и файлах-вложениях. Неприятности также может доставлять спам. **Thunderbird** позволяет изменять настройки безопасности.

Само собой, это не отменяет необходимость иметь на компьютере эффективно работающие антивирус и межсетевой экран. Подробнее о всяком вредоносном коде можно прочесть в главе нашего руководства [**"Как не допустить на компьютер вредителей"**](/chapter-1). Вы можете более подробно познакомиться с антивирусом [**Avast**](/avast_main), "уничтожителем шпионов" [**Spybot**](/spybot_main) и межсетевым экраном [**Comodo Firewall**](/comodofirewall_main).

<a name="3.1"></a>
## Отключение предпросмотра ##

Рабочее окно **Thunderbird** разделено на три основные части. В левом столбце — папки для аккаунта (аккаунтов) email, в правой верхней части — список сообщений, а в нижней правой части — предпросмотр конкретного (выбранного вами) письма. Как только вы выбираете письмо, его содержание показывается в окне предпросмотра.

Если в очередном письме попался вредоносный код, панель предпросмотра автоматически попытается его активировать (вместе с письмом). Поэтому лучше эту область отключить.

![](/sbox/screen/thunderbird-ru/08.png)

Выбираем в меню "Вид" — "Разбивка окна" и снимаем галочку рядом с пунктом "Область просмотра сообщений". (Или просто нажимаем клавишу F8).

![](/sbox/screen/thunderbird-ru/09.png)

Область предпросмотра исчезла с экрана. Чтобы просмотреть сообщение, нужно дважды щелкнуть по его теме. Это убережет вас от случайного открытия подозрительных и потенциально вредных писем. Например, с неизвестным и нежеланным отправителем, глупым или неуместным заголовком. Такие сообщения можно удалить, не просматривая.

<a name="3.2"></a>
## Отключение HTML ##

**Thunderbird** позволяет обмениваться письмами в гипертекстовом формате (HyperText Markup Language, **HTML**). Это дает возможность использовать в письмах разные шрифты, цвета и прочие "красивости". **HTML**  — язык для разработки веб-сайтов. Вредоносный код, который злоумышленники порой размещают на веб-сайтах средствами **HTML**, может навредить вам и в сообщениях email. 
 
Выбираем "Вид" — "Тело сообщения в виде" — "Простого текста".

![](/sbox/screen/thunderbird-ru/10.png)

<a name="3.3"></a>
### 3.3 How to Configure the Security Options ###

**Thunderbird** has two built-in junk mail filters that can help you determine which of your incoming messages are spam. By default, these filters are disabled, so you must enable them for use. Even after they have been enabled, you will continue to receive junk mail, but **Thunderbird** will automatically sort them into the *Junk* folder. 

Email scams - also referred to as *phishing* emails - usually attempt to make you click on a link that is embedded in the email. Frequently, these links direct your browser to a web site that will attempt to infect your computer with a virus. In other cases, the link will take you to a web site that appears to be legitimate, to deceive you into entering a valid user name and password, which can then be used or sold by the entity or people for commercial or malicious purposes. 

**Thunderbird** can help to identify and warn you about emails like this. Additional tools that can help prevent infection from malicious websites are described in the [**Other Useful Mozilla Add-Ons**](/en/firefox_others) section of the **Firefox** chapter.

The first set of assorted junk mail and security controls are accessed through the *Options - Security* window through which the majority of these privacy and security options are configured. To access them, perform the following steps:

**Step 1**. **Select Tools > Options** to activate the *Options* window.

**Step 2**. **Click** ![](/sbox/screen/thunderbird-en/26.png) to activate the following screen:

![](/sbox/screen/thunderbird-en/27.png)

*Figure 4: The Security window displaying its associated tabs*

### The Junk tab ###

**Step 1**. **Check** the relevant options in the *Junk* tab as shown in *figure 4* above, to enable **Thunderbird** to delete email that you have determined to be junk mail. Additional junk mail settings are described later on in this section. 

### The Email Scams tab ###

**Step 1**. **Check** the *Tell me if the message I'm reading is a suspected email scam* option to enable **Thunderbird** to analyse messages for email scams as follows: 

![](/sbox/screen/thunderbird-en/28.png)

*Figure 5: The Email Scams tab* 

### The Anti-Virus tab ###

**Step 1**. **Click** the *Anti-Virus* tab to activate the following screen: 

![](/sbox/screen/thunderbird-en/29.png)

*Figure 6: The Anti-Virus tab* 

This option lets your anti-virus software scan and isolate individual
messages as they arrive. Without this setting enabled, it is possible
that your *entire* *Inbox* folder could be 'quarantined' if you receive an infected message.

**Note**: This assumes that you have a functioning anti-virus program
installed. Please refer to [**Avast**](/en/avast_main) for more information on how to install and configure anti-virus software.

### The Passwords tab ###

**Step 2**. **Click** the *Passwords* tab to activate the following screen: 

![](/sbox/screen/thunderbird-en/30.png)

*Figure 7: The Passwords tab*

**Important:** We strongly recommend to keep your passwords private and secure using a software designed precisely for this purpose; please refer to [**KeyPass**](/en/keepass_main) for more information. 

**Note**: The options in the *Password* tab will only work if you checked the *Remember password* option in the first *Mail Account Setup* screen when you registered your email accounts with **Thunderbird**. 

**Step 1**. **Click** ![](/sbox/screen/thunderbird-en/31.png) to activate the following screen:

![](/sbox/screen/thunderbird-en/32.png)

*Figure 8: The Saved Passwords window*

The *Saved Passwords* window lets you remove or view all the corresponding passwords for each of your accounts. However, to maximise your privacy and security, you can set a *Master Password* make all of  your account passwords inaccessible to anyone else familiar with the **Thunderbird** password options.

**Step 3**. **Check** the *Use a master password* option as shown in *figure 7* to enable the *Change Master Password...* button.

**Step 4**. **Click** ![](/sbox/screen/thunderbird-en/33.png) to activate the following screen:

![](/sbox/screen/thunderbird-en/34.png)

*Figure 9: Change Master Password window*

**Step 5**. **Type** in an appropriately difficult password that only you will remember, and then **click** ![](/sbox/screen/thunderbird-en/35.png) to confirm it as your *Master Password*. The next time you **click** 
![](/sbox/screen/thunderbird-en/33.png), the following screen appears prompting you to enter the master password as follows:

![](/sbox/screen/thunderbird-en/36.png)

*Figure 10: The Password Required screen*

### The Web Content tab ###

A cookie is a small piece of text which your web browser uses to authenticate or identify a given web site. The *Web Content* tab lets you specify which blog, news feed or newsgroup cookies are reliable and safe.  

**Step 1**. **Click** the *Web Content* tab to activate the following screen:

![](/sbox/screen/thunderbird-en/37.png)

*Figure 11: The Web Content tab*

**Step 2**. **Select** the *I close Thunderbird* item in the *Keep until:* option to delete those cookies whenever you close **Thunderbird** for additional security.

<a name="3.4"></a>
### 3.4 How to Enable the Account Settings Junk Mail Filter ###

The second type of **Thunderbird** junk mail filter is available through the *Account Settings - Junks Settings* window. By default, these filters are disabled, so they must be enabled if you wish to use them. Whenever junk emails arrive **Thunderbird** will automatically sort them into the *Junk* folders associated with different accounts. 

**Step 1**. **Select Tools > Account Settings** to activate the *Account Settings* window.

**Step 2**. **Select** the *Junk Settings* option associated with a specific **Gmail** or **RiseUp** account in the sidebar. 

**Step 3**. **Enable** the *Junk Settings* options so that your own *Account Settings - Junk Settings* screen resembles the following: 

![](/sbox/screen/thunderbird-en/38.png)

*Figure 12: The Account Settings - Junk Settings window*

**Step 4**. **Click** ![](/sbox/screen/thunderbird-en/35.png) to complete the configuration of the *Account Settings* window.

**Note**: The *Junk Settings* options must be configured separately for each account. As such, junk mail for a **Gmail** or a **RiseUp** account will be placed in its corresponding *Deleted* folder. Alternatively, you may designate a *Local Folder* to receive junk mail from all your accounts. 

![](/sbox/screen/thunderbird-en/39.png)

*Figure 13: The Account Settings - Junk Settings window, displaying the settings for a central junk folder*

**Step 1**. **Select** the *Junk Settings* option directly beneath *Local Folders* in the sidebar.

**Step 2**. **Select** the *Local Folders* item from the *"Junk" folder on:* drop-down list as displayed in *figure 13*.

**Step 3**. **Click** ![](/sbox/screen/thunderbird-en/35.png) to complete the configuration of the *Account Settings* window.

Now that you have successfully configured the assorted security options and junk mail settings in **Thunderbird**, please proceed to the following section, [**How to Use Enigmail with GnuPG in Thunderbird**](/en/thuderbird_encryption). 


