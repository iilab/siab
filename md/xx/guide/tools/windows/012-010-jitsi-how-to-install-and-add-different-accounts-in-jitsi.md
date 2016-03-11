

---

lang: xx
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: Jitsi - How to Install and Add Different Accounts in Jitsi

---

List of sections on this page:

- [**2.1 How to Install Jitsi**](#2.1)
- [**2.2 How to Add Accounts in Jitsi**](#2.2)
- [**2.2.1 How to Add a Gmail/Google Account**](#2.2.1)
- [**2.2.2 Registering new Jabber/XMPP or SIP account and adding it to Jitsi**](#2.2.2)
- [**2.2.3 How to Add a Facebook Account**](#2.2.3)
- [**2.3 How to change password for account with Jitsi**](#2.3)
- [**2.4 How to configure Jitsi to improve it's security**](#2.4)
- [**2.4.1 Disable and remove call and chat history**](#2.4.1)
- [**2.4.2 Require private messaging when text chatting**](#2.4.2)
- [**2.4.3 Protect passwords to your accounts with master password**](#2.4.3)

<a name="2.1"></a>
## 2.1 How to Install Jitsi ##

To install **Jitsi**, perform the following steps:

**Step 1**. **Double click** {jitsi-latest-x86.exe} or  {jitsi-latest-x64.exe} which you have just downloaded; the *Open File - Security Warning* dialogue box may appear. If it does, **click** {Run} to activate the *Windows Installer* screen, followed by the *Welcome to the Jitsi Setup Wizard* window.  

![](/sites/securityinabox.org/files/media/jitsi-win-en-001-welcome-to-installation.png)

*Figure 1: The Jitsi Setup Wizard*

**Step 2**. **Click** {Next} to activate the *End User License Agreement* window; **check** the *I accept the terms in the License Agreement* option to enable the *Next* button, and then **click**  {Next} to activate the *Destination Folder* window. Afterwards, **Click** {Next} to activate the *Additional Tasks* window and accept the default settings as presented.

![](/sites/securityinabox.org/files/media/jitsi-win-en-004-additional-tasks.png)

*Figure 2: The Jitsi Additional Task Options*

**Note**: Enabling the *Auto-start when computer restarts or reboots* option may slow down the overall function of your computer, especially if you already have multiple applications configured to run when your computer starts up.

**Step 3**.  **Click** {Next} to activate the *Ready to Install Jitsi* window, and then **click** {Install} to activate the *Installing Jitsi* window displaying the installation progress bar. The *User Account Control Warning* may appear which asks "Do you want to allow this app to install software on your PC?", click {Yes} to allow it to install **Jitsi**.
 
![](/sites/securityinabox.org/files/media/jitsi-win-en-006-user-account-control-warning.png)

*Figure 3: User Control Warning While Installing Jitsi*

**Step 4**. **Click** {Finish} to complete the installation process and automatically launch the **Jitsi** *Sign in* window as follows:

![](/sites/securityinabox.org/files/media/jitsi-win-en-012-configure-all-account-in-one-page.png)

*Figure 4: The Jitsi Sign in Page*

**Note**: In some instances, installing and launching **Jitsi** for the first time triggers a *Windows Security Alert* prompt screen (*Figure 5* below). This alert is normal behaviour for the **MS Windows** operating system, it is ok to continue with using **Jitsi**. Even if you do not click any of the buttons, and simply close the prompt window, **Jitsi** is still able to communicate through the usual public servers such as **Jabber/XMPP or SIP**, **Google Hangout** (formerly Google Talk) and **Facebook Chat**, or **Yahoo Messenger**. However, clicking the {Allow access} button enables an advanced feature in **Jitsi** called *Registrarless SIP Accounts*. For more information about these special accounts, please refer to the [**Registrarless SIP Accounts**](https://jitsi.org/Documentation/RegistrarlessSIPAccount) page.  

![](/sites/securityinabox.org/files/media/jitsi-win-en-010-firewall-access-requirement.png)

*Figure 5: The Windows Security Alert prompt screen*

**Step 6**. **Select** *both* **Private** and **Public** networks check-boxes, and then **click** {Allow access} to see the **Jitsi** Sign in window (as shown in *Figure 1* above) or main user interface window (as shown in *Figure 4* below).

**Note**: It may show you "Error accessing your Mircrosoft Outlook contacts" window, just **Check** "Don't show this message again" and click {OK} to lead to *Sgin in* window.

<a name="2.2"></a>
## 2.2 How to Add Accounts in Jitsi ##

This section describes how to add or set up different kinds of accounts in **Jitsi**. **Jitsi** supports many different account types. Accounts we discuss below are based mostly on the **Jabber/XMPP** and **SIP** communication protocols. Among many services, **Jitsi** lets you use accounts on **Gmail** or **Facebook** to communicate. Since those are one of most popular services used on the Internet, how to add them to Jitsi is shown below, along with how to improve your security when communicating over those accounts, benefiting from **Jitsi**'s independent encryption on the top of protection offered by your account providers. However please note that even with **Jitsi** encryption, account providers like **Google** or **Facebook** are monitoring the very fact that you are communicating (and perhaps with whom you are communicating), and may share this information with third-parties, such as corporations or governments. Therefore it is perhaps best to avoid using those accounts for sensitive communication even with **Jitsi** encryption. We also describe in this section how to create more secure (Jabber/XMPP or SIP) accounts and add them to Jitsi, and we do recommend to use these accounts instead.

<a name="2.2.1"></a>
### 2.2.1 How to Add a Gmail/Google Account ###

**Note**: The example which follows is based on a **Google Hangout** account, the set-up process for the other communication protocols listed in *Figure 4* above is similar. Communications or some features (like Jitsi independent encryption of text chat and voice - **OTR** and **ZRTP**) may not work between two or more users of different account providers (like Facebook, Gmail, Yahoo, etc.). However, they should work when communicating between two accounts from the same service provider.

**Step 1**. **Select *Start* > *Jitsi*** or **double-click** the **Jitsi** desktop icon to open it.

**Step 2**. If you see a window like *Figure 4* (*sign in* window), **type in** the username and password of the **Gmail** account you would like to use for chat purposes. If you closed *Sign in* window, or you want to add another account, you can add it by **selecting *File* > *Add new account...*** menu. In the new window **select Network** as *Google Talk* and **type in** the user name and password of the **Gmail** account as shown on the image below:

![](/sites/securityinabox.org/files/media/jitsi-win-en-015-add-new-account-gmail-completed.png)

*Figure 6: The Jitsi "Sign in" window*

**Note**: You can add multiple accounts using different protocols at the same time. 

**Step 3**. **Click** {Add} to activate your account chat window as follows:

![](/sites/securityinabox.org/files/media/jitsi-win-en-026-show-hide-call-history.png)

*Figure 7: An example of a Jitsi main window after adding a Gmail account*

**Note:** If you are using [2-step verification](https://support.google.com/accounts/answer/180744?hl=en) to protect access to your **Gmail** account, when you try to log in from **Jitsi** with your regular password you may see a message like the one below. To log in using **Jitsi**, you will need to generate an "application-specific password". See Google's [instructions on how to do this](https://support.google.com/accounts/answer/185833?hl=en).

![](/sites/securityinabox.org/files/media/jitsi-win-en-016-gmail-athuntication-error.png)

*Figure 8: Example of Google Hangout login authentication failure*






To verify that you have registered **Gmail** account(s) with **Jitsi**, perform the following steps:

**Step 1**. **Select *Tools* > *Options*** in the menu to activate the following window:

![](/sites/securityinabox.org/files/media/jitsi-win-en-023-list-of-added-accounts.png)

*Figure 9: The Options window displaying the newly registered Gmail account (resized)*

<a name="2.2.2"></a>
### 2.2.2 Registering new Jabber/XMPP or SIP account and adding it to Jitsi ###

**Jabber/XMPP** and **SIP** are open standards of text and voice communication. There are [many servers](https://xmpp.net/directory.php) that offer free accounts which you can use with Jitsi. Below we are recommending some of the servers that you could use for sensitive communication. Note that it is also possible to download a [Jabber/XMPP server software](http://xmpp.org/xmpp-software/servers/) (like [ejabberd](http://www.process-one.net/en/ejabberd/) or [Prosody IM](http://prosody.im/)), install it on your own server computer and set it up for private and secure communication between the members of your group, community or organisation.

* **Riseup.net** Jabber/XMPP account

If you have account on the [Riseup.net secure email service](/en/riseup_main) (located in the USA) you may [use this account also to communicate over Jabber/XMPP network](https://www.riseup.net/en/chat) by adding this account to Jitsi - see below on how to add existing Jabber/XMPP account.

* **jit.si** Jabber/XMPP account

This server is maintained by the developers of the Jitsi program. You can register account on [**jit.si**](https://jit.si) and many other public Jabber/XMPP servers in the same way as described above in this section. The IM Observatory maintains a [list and ranking of the public Jabber/XMPP servers](https://xmpp.net/directory.php), and also lets you [test any Jabber/XMPP server for security](https://xmpp.net/index.php).

* You can register an account on any **Jabber** server by taking following steps:

**Step 1**.  In **Jitsi, select *File* > *Add new account...*** in the menu. In the new window, **select *Network*: XMPP** and **check** the *Create a new XMPP account*** option. In *Server*, **type** jabber.ccc.de, **type** in the XMPP username you would like to create, and **fill in** the *Password* and *Confirm password* fields so that it resembles the following:

![](/sites/securityinabox.org/files/media/jitsi-win-en-035-create-new-xmpp-account.png)

*Figure 8: Example of the "Add new account" window with the "Create a new XMPP account" option selected*

**Step 2**. **Click** {Add}. After successful registration you will be presented with a window similar to *Figure 8* above.

If the username which you requested is already taken by somebody else, the registration process will fail with an error message like *User is already exist.*  You can try again by repeating the process and selecting a different username.

**Note**: In some case, if you do not log in to your account for longer than a certain period of time (e.g. 12 months) your account will be automatically removed from the server and the username will become available for registration by other people.

* **ostel.co** SIP account

**SIP** accounts cannot be registered from within the **Jitsi** program. The **ostel.co** server (located in USA) offers [registration on their web page](https://ostel.co/users/sign_up). **Select** a username, password and provide your existing email address and **click** the {Sign up} button on the web page. After successful registration come back to Jitsi program. **Select *File* > *Add new account...*** in the menu, **select Network: SIP**, **type in** your username (e.g. sarah.jozani@ostel.co) and the password you created during the web registration and **click** {Add}. See following image for reference:

![](/sites/securityinabox.org/files/media/jitsi-win-en-020-add-new-account-sip-completed.png)

*Figure 9: Example of "Add new account" window for SIP account*

* **Adding existing Jabber/XMPP or SIP account to Jitsi**

If you already have Jabber/XMPP or SIP account you can add it to **Jitsi** by **selecting *File* > *Add new account...*** in the menu and selecting the appropriate **Network** (either XMPP or SIP depending on the account type).

<a name="2.2.3"></a>
### 2.2.3 How to Add a Facebook Account ###

**Facebook** has two settings that you may need to change before **Jitsi** can connect to your Facebook Chat.

* **Facebook Username**

**Facebook** requires a username for **Jitsi** to connect to Facebook chat. Many **Facebook** users already have a username. To check your username, **log in** to your **Facebook** account: your username is what appear in the location bar of your browser after *https://www.facebook.com/* when you view your Timeline or Page. You can see or change the username or get one by going to your *Account Settings* > *General* section or by visiting [https://www.facebook.com/username](https://www.facebook.com/username). To set username **Facebook** may ask you for your account verification which may require sending SMS to a mobile phone number which you will need to provide to **Facebook** in the process of verification. For more details see [Facebook’s explanation of usernames](https://www.facebook.com/help/329992603752372/).

* **App Settings**

**Facebook’s** “Apps” must be enabled before **Jitsi** can connect to Facebook Chat. Visit your **Facebook** *Account Settings* > *Apps* section and check that the setting for *Apps, Websites and Plugins* is *Enabled*.

**Note** that that turning **Facebook**’s "Apps" opens up much of your **Facebook** data to third-party application developers. This data is available not only to the **Facebook** applications that you use, but also **Facebook** applications used by any of your friends. After enabling **Facebook**’s "Apps", be sure to check the settings under "Apps Others Use". This setting allows you to hide some personal information from applications used by your friends. Unfortunately, **Facebook** does not offer settings to hide all personal information. Certain categories of information (like your friend list, gender, or info you have made public) are visible as long as **Facebook**’s "application platform" is turned "on". It is up to you to determine whether this is an acceptable trade-off of your privacy.

Now you are prepared to add your **Facebook** account to **Jitsi**. To do this follow the steps below:

**Step 1**.  From the main menu **select *File > Add New Account...***

**Step 2**.  In the Add New Account dialogue, **Network** menu choose *Facebook*, **enter your username and password** and **Click** {Add}
 
![](/sites/securityinabox.org/files/media/jitsi-win-en-022-add-new-account-facebook-completed.png)

*Figure 10: Example of "Add new account..." window for a Facebook account*


<a name="2.3"></a>
## 2.3 How to change password for account with Jitsi ##

It is an important element of security to know how to change the password for each account that one has. Many of the accounts that you can use with Jitsi offer changing password as a part of their settings, which are accessible over web interface. However some Jabber/XMPP and SIP account will not have any web interface to manage them. You can change password for those account using **Jitsi** by following steps below:

**Step 1**. **select *Tools* > *Options*** in the menu, **select** the ***Accounts*** tab

![](/sites/securityinabox.org/files/media/jitsi-win-en-023-list-of-added-accounts.png)

*Figure 11: List of the Added Accounts to Jitsi*

**Step 2**. **click** on {Edit} button on the bottom to activate following window:

![](/sites/securityinabox.org/files/media/jitsi-win-en-024-change-account-password-button.png)

*Figure 12: Account Registration Wizard window with Change account password button on the bottom*

**Step 3**. **click** on {Change account password} to activate *Change account password* window:

![](/sites/securityinabox.org/files/media/jitsi-win-en-025-change-account-password.png)

*Figure 13: Change account password window*

**Step 4**. ***Enter new password* and *Re-enter password*** and **click** on {OK} button to close this window.

<a name="2.4"></a>
## 2.4 How to configure Jitsi to improve it's security ##

<a name="2.4.1"></a>
### 2.4.1 Disable and remove call and chat history ###

**Jitsi** by default stores information about the incoming and outgoing voice/video calls and the history of your text chats, all messages that you sent and received. You can access voice/video calls by **clicking** on the clock icon on the main Jitsi window:

![](/sites/securityinabox.org/files/media/jitsi-win-en-026-show-hide-call-history.png)

*Figure 14: Top of the Jitsi main window with call history button indicated*

You can see the text chat history by **clicking** on the egg-timer like icon in the text chat window while chatting with a contact:

![](/sites/securityinabox.org/files/media/jitsi-win-en-028-chat-history-menu.png)

*Figure 15: Chat window with chat history button indicated*

This information is collected and stored on the disk of your computer. **Even if you encrypt the text chat with OTR all the text messages you send and receive are stored on your computer in open text format.** The same information is collected and stored on the disk of the contacts you are communicating with. 

To prevent Jitsi collecting this information (and remove already gathered data), **you and your contact should take the following steps**.

#### To disable Jitsi from collecting the information: ####

**Step 1**.  **select *Tools* > *Options*** in the menu, **select** the ***General*** tab and **uncheck** the ***Log chat history*** option as shown below:

![](/sites/securityinabox.org/files/media/jitsi-win-en-029-disable-log-chat-history.png)

*Figure 16: "Options" window, "General" tab with "Log chat history" option unchecked*

**Step 2**. in the *Options* window, first **select** the **Advanced** tab, then **select** the **Logging** section, and then **uncheck** the **Enable packet logging** option as shown below: 

![](/sites/securityinabox.org/files/media/jitsi-win-en-032-disable-packet-logging.png)

*Figure 17: "Options" window, "Advanced" tab, "Logging" section with "Enable packet logging" unchecked*

Your changes will take effect after you **restart Jitsi**.

#### To remove already collected information about your calls and text messages: ####

**Step 1**. **Quit** Jitsi.

**Step 2**. Remove the entire log history folder *history_ver1.0* from the **Jitsi** *user profile* folder. You can remove a sub-folder of *history_ver1.0* if you want to dispose of only part of the history. The location of the *user profile* and *log history* folders depends on the operating system:

* On Windows XP and earlier, this is located in *C:\Documents and Settings\WINDOWS_USERNAME\Application Data\Jitsi\history_ver1.0*
* On Windows Vista, 7, 8, this is *C:\Users\WINDOWS_USERNAME\AppData\Roaming\Jitsi\history_ver1.0* (**Note** that "AppData" folder may be hidden. See [how to see hidden files](http://windows.microsoft.com/en-us/windows/show-hidden-files)).
**Note** that you have to put your Windows login credential (username) in place of WINDOWS_USERNAME in the link above. If you use **Windows File Explorer** you need to **click** the folder matches your username.
* Mac OS X: from your home folder *~/Library/Application Support/Jitsi/history_ver1.0*
* Linux: from your home folder *~/.jitsi/history_ver1.0* (**Note** that the ".jitsi" folder may be hidden. See [how to see hidden files in Ubuntu](http://itsfoss.com/hide-folders-and-show-hidden-files-in-ubuntu-beginner-trick/))

See the [How to destroy sensitive information](/en/guide/destroy-sensitive-information) chapter for more on how to dispose of information securely.

<a name="2.4.2"></a>
### 2.4.2 Require private messaging when text chatting ###

It is recommended that you set **Jitsi** up to require private and encrypted text messaging using [*OTR*](/en/glossary#OTR) [*encryption*](/en/glossary#encryption) whenever possible. To do this, **select *Tools* > *Options*** in the menu, **select** the **Security** tab, **select** the **Chat** sub-tab and **check *Require private messaging*** at the bottom of the screen as shown below:

![](/sites/securityinabox.org/files/media/jitsi-win-en-033-require-private-messaging.png)

*Figure 18: "Options" window, "Security" tab, "Chat" sub-tab with "Require private messaging" option indicated*

<a name="2.4.3"></a>
### 2.4.3 Protect passwords to your accounts with master password ###

It is best not to let Jitsi remember passwords to your accounts. If you decide otherwise for ease of use anybody who gets access to your computer will be able to log in to your accounts by simply starting Jitsi. It will also be possible to view your passwords in the *Options* window. It is therefore **strongly recommended** to protect passwords to your accounts with good **master password**. Once you set up  the master password, Jitsi will ask you for it upon starting the program.

**Step 1**. **Open** the *Options* window by **selecting *Tools* > *Options*** in the menu, **select the *Security*** tab and ***Passwords*** sub-tab, and **check *Use a master password*** to activate the ***Master Password*** window.

**Step 2**. In the new window **type in your password** as shown in the picture below. For more on creating a strong password, see [***How to create and maintain secure passwords***](en/guide/passwords).

![](/sites/securityinabox.org/files/media/jitsi-win-en-031-set-a-master-password.png)

*Figure 19: The "Master Password" window*

**Step 3**. **Click** {OK} to confirm the password and activate a new window which should say ***Master Password successfully set up***. **Click** {OK} to close it and come back to the *Options* window which should resemble below:

![](/sites/securityinabox.org/files/media/jitsi-win-en-034-change-master-password.png)

*Figure 20: "Options" window, "Security" tab, "Passwords" sub-tab with the "Use a master password" option indicated*	

**Note**: The {Change Master Password...} button lets you change the master password and the {Saved Passwords...} button lets you access the list of passwords remembered by Jitsi and remove them if need be.

