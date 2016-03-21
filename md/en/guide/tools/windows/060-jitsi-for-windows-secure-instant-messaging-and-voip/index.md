

---

lang: en
community: guide
type: tools
os: windows
weight: 060
title: Jitsi for Windows - secure instant messaging and VoIP

---

**Jitsi** is cross-platform, [**free and open-source software**](/en/glossary#FOSS) for **Instant Messaging** (**IM**), **Voice over IP** (**VoIP**) and video chat. It is compatible with many popular IM and telephony protocols, including *Jabber/XMPP*, *Facebook Messenger*, *AIM*, *ICQ*, *MSN*, *Yahoo! Messenger* and *SIP*. It provides *end-to-end* encryption for text chats through the [**Off-the-Record** (**OTR**)](/en/glossary#OTR) protocol. It also supports end-to-end encrypted voice chat using *ZRTP*, though it tends to be somewhat unstable when used in this way.

# Required reading


:[](../../../tactics/secure communication)


:[](jitsi-for-windows-secure-instant-messaging-and-voip)

# What you will get from this guide

- A private communications tool that supports encrypted text and voice voice chat
- The ability to keep even your instant messaging (IM) providers from seeing the content of your chats

# 1. Introduction to Jitsi





## 1.0 Other tools like Jitsi

**Jitsi** is available for **GNU Linux**, **Mac OS** and **MS Windows**. It can be used to communicate with other *XMPP* or *SIP* clients that support end-to-end encryption through **OTR** (for text chat) or **ZRTP** (for voice chat). Examples are recommended below: 

- For encrypted **text chat**: [**Pidgin**](https://pidgin.im/) (**MS Windows** and **GNU Linux**), [**Miranda**](http://www.miranda-im.org/) (**MS Windows**), [**Adium**](https://adium.im/) (**Mac OS X**), [**ChatSecure**](https://guardianproject.info/apps/chatsecure/) ([**Android**](../chatsecure/android) and **iOS**).

- For encrypted **voice chat**: **CSipSimple** (**Android OS**), [**Linphone**](http://www.linphone.org/) (**GNU Linux**, **MS Windows**, **Mac OS X**, **Android OS**, **iOS**, and others.)


## 1.1 Things you should know about Jitsi before you start

**Jitsi** supports many different account types and communication protocols and can thus communicate with correspondents who use different programs. Some of those programs will offer similar features to improve the security of your communication (like programs mentioned in section above), which support independent text and voice encryption (**OTR** and **ZRTP**). Other programs, especially proprietary ones (for instance **Facebook** chat or **Google Talk** ), may not have those features implemented. However, you will still be able to communicate with contacts who are using those proprietary programs with help of **Jitsi** just without the added benefits of **Jitsi's** security features.

Regardless of whether you communicate by text, voice or video, providers of services like **Facebook Chat**, **Google Talk**, **Yahoo! Messanger**, **Skype** or **Viber** have access to your communication sessions and may offer this access to third-parties, such as corporations or governments. **Jitsi** lets you communicate in a private and safe manner using your existing accounts with the help of added encryption. This makes the content of your communication inaccessible to account providers and potential third-parties. In order to protect your private chat sessions and conversations, **Jitsi** uses cryptographic methods including **Off-the-Record** ([**OTR**](/en/glossary#OTR)) for text chats, and **ZRTP/SRTP** for voice calls.

Another notable difference between **Jitsi** and programs like **Skype** is that it enables users to keep using their existing accounts from different service providers, independent of the program developers. This also means that you need to set up an account prior to being able to use **Jitsi**.

Jitsi allows you to use your existing accounts to communicate securely through the use of *end-to-end* encryption. This not only makes the content of your communication inaccessible to various third parties, such as government or corporate surveillance platforms, it also protects your conversations from those who operate the chat services themselves (such as Facebook, if you are using *Facebook Messenger*, or Google, if you are using *Google Talk*). 

Jitsi allows you to use your existing accounts to communicate securely through the use of *end-to-end* encryption. This not only makes the content of your communication inaccessible to various third parties, such as government or corporate surveillance platforms, it also protects your conversations from those who operate the chat services themselves (such as Facebook, if you are using *Facebook Messenger*, or Google, if you are using *Google Talk*). 

**Note:** Jitsi was written in the Java programming language. As such, Java must be installed on your computer in order for it to work. Though Java itself does not represent a significant security risk, *Java browser extensions* are often found to contain vulnerabilities that allow malicious websites to assume control of your computer or install malware. If your browser has a Java plugin installed, we strongly recommend that you [disable it](https://www.java.com/en/download/help/disable_browser.xml).

# 2. Install and configure Jitsi





## 2.1 Install Jitsi

To install **Jitsi**, perform the following steps:

**Step 1**. **Double click** ![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-02.png); the *Open File - Security Warning* dialogue box may appear. If it does, **click** ![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-03.png) to activate the *Windows Installer* screen, followed by the *Welcome to the Jitsi Setup Wizard* window.  

**Step 2**. **Click** ![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-04.png) to activate the *End User License Agreement* window; **check** the *I accept the terms in the License Agreement* option to enable the *Next* button, and then **click**  ![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-04.png) to activate the *Destination Folder* window.

**Step 3**. **Click** ![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-04.png) to activate the *Additional Tasks* window and accept the default settings as presented.

**Note**: Enabling the *Auto-start when computer restarts or reboots* option may slow down the overall function of your computer, especially if you already have multiple applications configured to run when your computer starts up.

**Step 4**.  **Click** ![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-04.png) to activate the *Ready to Install Jitsi* window, and then **click** ![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-05.png) to activate the *Installing Jitsi* window displaying the installation progress bar.

**Step 5**. **Click** ![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-06.png) to complete the installation process and automatically launch the **Jitsi** *Sign in* window as follows:

![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-07.png)

*Figure 1: The Jitsi Sign in window*

**Note**: In some instances, installing and launching **Jitsi** for the first time triggers a *Windows Security Alert* prompt screen (*Figure 2* below). This alert is normal behaviour for the **MS Windows** operating system, it is ok to continue with using **Jitsi**. Even if you do not click any of the buttons, and simply close the prompt window, **Jitsi** is still able to communicate through the usual public servers such as **Jabber/XMPP or SIP**, **Google Chat** and **Facebook Chat**, or **Yahoo Messenger**. However, clicking the *Allow access* button enables an advanced feature in **Jitsi** called *Registrarless SIP Accounts*. For more information about these special accounts, please refer to the [**Registrarless SIP Accounts**](https://jitsi.org/Documentation/RegistrarlessSIPAccount) page.  

![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-08.png)

*Figure 2: The Windows Security Alert prompt screen*

**Step 6**. **Select** *both* **Private** and **Public** networks check-boxes, and then **click** *Allow access* to see the **Jitsi** Sign in window (as shown in *Figure 1* above) or main user interface window (as shown in *Figure 4* below).


## 2.2 Add accounts to Jitsi

This section describes how to add or set up different kinds of accounts in **Jitsi**. **Jitsi** supports many different account types. Accounts we discuss below are based mostly on the **Jabber/XMPP** and **SIP** communication protocols. Among many services, **Jitsi** lets you use accounts on **Gmail** or **Facebook** to communicate. Since those are one of most popular services used on the Internet, how to add them to Jitsi is shown below, along with how to improve your security when communicating over those accounts, benefiting from **Jitsi**'s independent encryption on the top of protection offered by your account providers. 

Please note that even with **Jitsi** encryption, account providers like **Google** or **Facebook** are monitoring the very fact that you are communicating (and perhaps with whom you are communicating), and may share this information with third-parties, such as corporations or governments. Therefore it is perhaps best to avoid using those accounts for sensitive communication, even with **Jitsi** encryption. We also describe in this section how to create more secure (Jabber/XMPP or SIP) accounts and add them to Jitsi, and we do recommend to use these accounts instead.


### 2.2.1 Add a Google Talk account to Jitsi

**Note**: The example which follows is based on a **Google Talk** account, the set-up process for the other communication protocols listed in *Figure 1* above is similar. Communications or some features (like Jitsi independent encryption of text chat and voice - **OTR** and **ZRTP**) may not work between two or more users of different account providers (like Facebook, Gmail, Yahoo, etc.). However, they should work when communicating between two accounts from the same service provider.

**Step 1**. **Select Start > Jitsi** or **double-click** the **Jitsi** desktop icon to open **Jitsi**.

**Step 2**. In the *sign in* window, **type in** the username and password of the **Gmail** account you would like to use for chat purposes, so that it resembles the following:

![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-09.png)

*Figure 3: The Jitsi "Sign in" window (resized)*

**Note**: You can add multiple accounts using different protocols at the same time. 

**Step 3**. **Click** ![Sign in](/sites/siabnext.ttc.io/files/media/jitsi-en-win-09s.png) to activate your account chat window as follows:

![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-10.png)

*Figure 4: An example of a Jitsi main window after adding a Gmail account*

**Note:** If you closed *Sign in* window, or you want to add another account, you can add it by **selecting *File* > *Add new account...*** menu. In the new window **select Network** as *Google Talk* and **type in** the user name and password of the **Gmail** account as shown on the image below:

![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-11.png)

*Figure 5: "Add new account" window*

To verify that you have registered your **Gmail** account with **Jitsi**, perform the following steps:

**Step 1**. **Select *Tools* > *Options*** in the menu to activate the following window:

![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-12.png)

*Figure 6: The Options window displaying the newly registered Gmail account (resized)*

**Note:** If you are using [2-step verification](https://support.google.com/accounts/answer/180744?hl=en) to protect access to your **Gmail** account, when you try to log in from **Jitsi** with your regular password you may see a message like the one below. To log in using **Jitsi**, you will need to generate an "application-specific password". See Google's [instructions on how to do this](https://support.google.com/accounts/answer/185833?hl=en).

![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-13.png)

*Figure 7: Example of Google Talk login authentication failure*


### 2.2.2 Add a Jabber or SIP account

**Jabber/XMPP** and **SIP** are open standards of text and voice communication. There are [many servers](https://xmpp.net/directory.php) that offer free accounts which you can use with Jitsi. Below we are recommending some of the servers that you could use for sensitive communication. Note that it is also possible to download a [Jabber/XMPP server software](http://xmpp.org/xmpp-software/servers/) (like [ejabberd](http://www.process-one.net/en/ejabberd/) or [Prosody IM](http://prosody.im/)), install it on your own server computer and set it up for private and secure communication between the members of your group, community or organisation.

* **Riseup.net** Jabber/XMPP account

If you have account on the [Riseup.net secure email service](../riseup/internet) (located in the USA) you may [use this account also to communicate over Jabber/XMPP network](https://www.riseup.net/en/chat) by adding this account to Jitsi - see below on how to add existing Jabber/XMPP account.

* **Jabber.ccc.de** and other Jabber/XMPP accounts

You can register an account on Jabber.ccc.de server (located in Germany) by taking following steps:

**Step 1**.  In **Jitsi, select *File* > *Add new account...*** in the menu. In the new window, **select *Network*: XMPP** and **check** the *Create a new XMPP account*** option. In *Server*, **type** jabber.ccc.de, **type** in the XMPP username you would like to create, and **fill in** the *Password* and *Confirm password* fields so that it resembles the following:

![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-14.png)

*Figure 8: Example of the "Add new account" window with the "Create a new XMPP account" option selected*

**Step 2**. **Click *Add***. After successful registration you will be presented with a window similar to *Figure 4* above.

If the username which you requested is already taken by somebody else, the registration process will fail with the message *We failed to create your account due to the following error: Could not confirm data.*  You can try again by repeating the process and selecting a different username.

**Note** that if you do not log in to your jabber.ccc.de for longer than 12 months your account will be automatically removed from the server and the username will become available for registration by other people.

Another Jabber/XMPP server which is worth mentioning is **jit.si**. This server is maintained by the developers of the Jitsi program. You can register account on [**jit.si**](https://jit.si) and many other public Jabber/XMPP servers in the same way as described above in this section. The IM Observatory maintains a [list and ranking of the public Jabber/XMPP servers](https://xmpp.net/directory.php), and also lets you [test any Jabber/XMPP server for security](https://xmpp.net/index.php).

* **ostel.co** SIP account

**SIP** accounts cannot be registered from within the **Jitsi** program. The **ostel.co** server (located in USA) offers [registration on their web page](https://ostel.co/users/sign_up). **Select** a username, password and provide your existing email address and **click** the *Sign up* button on the web page. After successful registration come back to Jitsi program. **Select *File* > *Add new account...*** in the menu, **select Network: SIP**, **type in** your username (e.g. terence.the.tester@ostel.co) and the password you created during the web registration and **click *Add***. See following image for reference:

![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-15.png)

*Figure 9: Example of "Add new account" window for SIP account*

* **Adding existing Jabber/XMPP or SIP account to Jitsi**

If you already have Jabber/XMPP or SIP account you can add it to **Jitsi** by **selecting *File* > *Add new account...*** in the menu and selecting the appropriate **Network** (either XMPP or SIP depending on the account type).


### 2.2.3 Add a Facebook account

**Facebook** has two settings that you may need to change before **Jitsi** can connect to your Facebook Chat.

* **Facebook Username**

**Facebook** requires a username for **Jitsi** to connect to Facebook chat. Many **Facebook** users already have a username. To check your username, **log in** to your **Facebook** account: your username is what appear in the location bar of your browser after *https://www.facebook.com/* when you view your Timeline or Page. Your username is also in your **Facebook** email address for your personal account (ex: username@facebook.com). You can see or change the username or get one by going to your *Account Settings* > *General* section or by visiting [https://www.facebook.com/username](https://www.facebook.com/username). To set username **Facebook** may ask you for your account verification which may require sending SMS to a mobile phone number which you will need to provide to **Facebook** in the process of verification. For more details see [Facebook’s explanation of usernames](https://www.facebook.com/help/329992603752372/).

* **App Settings**

**Facebook’s** “application platform” must be turned on before **Jitsi** can connect to Facebook Chat. Visit your **Facebook** *Account Settings > Apps* section and check that the setting for *Apps you use* is turned *On*. This turns "application platform" on for your account.

**Note** that that turning **Facebook**’s "application platform" opens up much of your **Facebook** data to third-party application developers. This data is available not only to the **Facebook** applications that you use, but also **Facebook** applications used by any of your friends. After turning on **Facebook**’s "application platform", be sure to check the settings under "Apps others use". This setting allows you to hide some personal information from applications used by your friends. Unfortunately, **Facebook** does not offer settings to hide all personal information. Certain categories of information (like your friend list, gender, or info you have made public) are visible as long as **Facebook**’s "application platform" is turned "on". It is up to you to determine whether this is an acceptable tradeoff of your privacy.

Now you are prepared to add your **Facebook** account to **Jitsi**. To do this follow the steps below:

**Step 1**.  From the main menu **select *File > Add New Account...***

**Step 2**.  In the Add New Account dialogue, **Network** menu choose *Facebook*, **enter your username and password** and **Click "Add"**
 
![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-16.png)

*Figure 10: Example of "Add new account..." window for a Facebook account*


## 2.3 Changing an account password in Jitsi

It is important element of security to know how to change the password for each account that one has. Many of the accounts that you can use with Jitsi offer changing password as a part of their setings, which are accessible over web interface. However some Jabber/XMPP and SIP account will not have any web interface to manage them. You can change password for those account using Jitsi by following steps below:

**Step 1**. **select *Tools* > *Options*** in the menu, **select** the ***Accounts*** tab.

![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-17.png)

*Figure 11: Options window with one account selected*

**Step 2**. **click on *Edit*** button on the bottom to activate following window:

![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-18.png)

*Figure 12: Account Registration Wizard window with Change account password button on the bottom*

**Step 3**. **click on *Change account password*** to activate *Change account password* window:

![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-19.png)

*Figure 13: Change account password window*

**Step 4**. ***Enter new password* and *Re-enter password*** and **click on *OK*** button to close this window.

**Step 5**. Close Account Registration Wizard.


# 3. Strengthen Jitsi's security settings





## 3.1 Clear and disable chat history 

**Jitsi** by default stores information about the incoming and outgoing voice/video calls and the history of your text chats -- all messages that you sent and received. You can access voice/video calls by **clicking** on the clock icon on the main Jitsi window:

![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-20.png)

*Figure 14: Top of the Jitsi main window with call history button indicated*

You can see the text chat history by **clicking** on the egg-timer like icon in the text chat window while chatting with a contact:

![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-21.png)

*Figure 15: Chat window with chat history button indicated*

This information is collected and stored on the disk of your computer. **Even if you encrypt the text chat with OTR all the text messages you send and receive are stored on your computer in open text format.** The same information is collected and stored on the disk of the contacts you are communicating with. 

To prevent Jitsi collecting this information (and remove already gathered data), **you and your contact should take the following steps**.

#### To disable Jitsi from collecting the information: ####

**Step 1**.  **select *Tools* > *Options*** in the menu, **select** the ***General*** tab and **uncheck** the ***Log chat history*** option as shown below:

![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-22.png)

*Figure 16: "Options" window, "General" tab with "Log chat history" option unchecked*

**Step 2**. in the *Options* window, first **select the *Advanced*** tab, then **select the *Logging*** section, and then **uncheck the *Enable packet logging*** option as shown below: 

![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-23.png)

*Figure 17: "Options" window, "Advanced" tab, "Logging" section with "Enable packet logging" unchecked*

Your changes will take effect after you **restart Jitsi**.

#### To remove already collected information about your calls and text messages: ####

**Step 1**. **Quit** Jitsi.

**Step 2**. Remove the entire log history folder *history_ver1.0* from the **Jitsi** *user profile* folder. You can remove a sub-folder of *history_ver1.0* if you want to dispose of only part of the history. The location of the *user profile* and *log history* folders depends on the operating system:

* On Windows XP and earlier, this is located in *C:\Documents and Settings\&lt;Windows login/user name&gt;\Application Data\Jitsi\history_ver1.0*.
* On Windows Vista, 7, 8, this is *C:\Users\&lt;Windows login/user name&gt;\AppData\Roaming\Jitsi\history_ver1.0* (**Note** that "AppData" folder may be hidden. See [how to see hidden files](http://windows.microsoft.com/en-us/windows/show-hidden-files)).
* Mac OS X: from your home folder *~/Library/Application Support/Jitsi/history_ver1.0*.
* Linux: from your home folder *~/.jitsi/history_ver1.0* (**Note** that the ".jitsi" folder may be hidden. See [how to see hidden files in Ubuntu](http://itsfoss.com/hide-folders-and-show-hidden-files-in-ubuntu-beginner-trick/)).

See the [How to destroy sensitive information](../destroy-sensitive-information) chapter for more on how to dispose of information securely.


## 3.2 Require private messaging

It is recommended that you set **Jitsi** up to require private and encrypted text messaging using [*OTR*](/en/glossary#OTR) [*encryption*](/en/glossary#encryption) whenever possible. To do this, **select *Tools* > *Options*** in the menu, **select the *Security*** tab, **select the *Chat*** sub-tab and **check *Require private messaging*** at the bottom of the screen as shown below:

![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-24.png)

*Figure 18: "Options" window, "Security" tab, "Chat" sub-tab with "Require private messaging" option indicated*


## 3.3 Set a master passphrase for Jitsi

It is best not to let Jitsi remember passwords to your accounts. If you decide otherwise for ease of use anybody who gets access to your computer will be able to log in to your accounts by simply starting Jitsi. It will also be possible to view your passwords in the *Options* window. It is therefore **strongly recommended** to protect passwords to your accounts with good **master password**. Once you set up  the master password, Jitsi will ask you for it upon starting the program.

**Step 1**. **Open** the *Options* window by **selecting *Tools* > *Options*** in the menu, **select the *Security*** tab and ***Passwords*** sub-tab, and **check *Use a master password*** to activate the ***Master Password*** window.

**Step 2**. In the new window **type in your password** as shown in the picture below. For more on creating a strong password, see [***Create and maintain secure passwords***](../passwords).

![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-25.png)

*Figure 19: The "Master Password" window*

**Step 3**. **Click *OK*** to confirm the password and activate a new window which should say ***Master Password successfully set up***. **Click "OK"** to close it and come back to the *Options* window which should resemble below:

![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-26.png)

*Figure 20: "Options" window, "Security" tab, "Passwords" sub-tab with the "Use a master password" option indicated*	

**Note**: The ***Change Master Password*** button lets you change the master password and the ***Saved Passwords...*** button lets you access the list of passwords remembered by Jitsi and remove them if need be.

# 4. Add contacts and chat with Jitsi

After adding at least one account to Jitsi and logging in, you are ready to add your contacts and communicate with them.


## 4.1 Add contacts to Jitsi

To add a contact to Jitsi follow steps below:

**Step 0**. Open the Jitsi main window by **selecting Start > Jitsi** or **double-clicking** the **Jitsi** desktop icon.

**Step 1**. **select *File* > *Add contact...*** which will open the following window:

![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-30.png)

*Figure 1: Add contact window*

**Step 2**. **Select** which of your accounts you would like to add this contact to (for example *terance.the.tester@jit.si*). 

**Optional**: You may also add the contact to a *group* among your other contacts. However, first you must create the group. You can do this by selecting ***File* > *Create group...*** from the menu). 

**Type in** your contact's user name or address into the ***ID or Number*** field (for example, *sally.the.doer@jit.si*). 

You can choose the name or nickname for the contact, which will be visible in your contacts list in the **Jitsi** main window; **type it into the *Display name*** field. 

**Step 3**. **Click** on *Add* to close the *Add contact* window and come back to Jitsi main window. In your contact list you will now see your new contact added with the note "Waiting for authorisation" as indicated below:

![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-31.png)

*Figure 2: Jitsi main window with added contact waiting for authorisation*
 
**Step 4**. When your contact (sally.the.doer@jit.si) logs in to her account, a pop-up window will inform her that you have requested to add her to your list of contacts:

![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-32.png)

*Figure 3: Window requesting authorisation of a new contact*

Your contact has a choice of selecting the *Ignore* option, in which case your request will continue awaiting authorisation; *Deny*, in which case you will receive information that your request was rejected; and *Authorise*, in which case you will receive information that your contact has accepted your authorisation request, and the entry for your contact in your contact list will become active:

![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-33.png)

*Figure 4: Jitsi main window with the new contact authorised*

## 4.2 Use Jitsi for secure text chat

Now that you added and authorised your contact, you can click on their name in the contact list and initiate text conversation, voice or video calls, and desktop sharing, by choosing the relevant icon under their name:

![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-34.png)

*Figure 5: Selected contact in the Jitsi main window with icons for IM, voice or video call and desktop sharing*

**Step 1**. We will now explore one of Jitsi's most important features: the ability to text chat securely, encrypting your messages with [*OTR*](/en/glossary#OTR). OTR functions in a similar manner to [*GPG/PGP*](/en/glossary#PGP) described in other chapters in this toolkit. Just as with PGP, before you and your contact can encrypt your communications, you both need to configure **Jitsi** to generate your encryption keys. You can do this by **selecting *Tools* > *Options*** menu and **selecting the *Security*** tab and ***Chat*** sub-tab. You will then see a window similar to one shown in the image below:

![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-35.png)

*Figure 6: Part of the chat options window where you can generate encryption keys for your text chats*

**Step 2**. Next, **click** the ***Generate*** button. As a result you will see the fingerprint of the key that has been generated:

![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-36.png)

*Figure 7: Part of the chat options window showing fingerprint for your generated OTR encrypted text chat*

One key is generated per account. You only need to do this again if you add a new account or install Jitsi on another device and do not move the existing keys to it.

Now you are ready to communicate:

**Step 3**. **Select a contact** from Jitsi main window and **click** on the *send message* icon (first from the left under the contact's name) to open a text chat window:

![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-37.png)

*Figure 8: Text chat window with the OTR encryption indicated but **not** engaged*

Note the *Encrypt chat with OTR* icon, the open padlock on the right-top side of the window. This inconspicuous symbol informs you whether the chat is encrypted or not. Now the lock is open (there is a tiny space between handle and the body of the lock!). 

**Step 4**. **click on the *Encrypt chat with OTR* icon**. Note the changes in the window:

![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-38.png)

*Figure 9: Text chat window after clicking on the Encrypt chat with OTR icon*

Observe that the padlock is now locked. This means that whatever messages you and your contact send to each other are encrypted. Note the message that this is an *unverified private conversation* and that you should *authenticate* sally.the.doer@jit.si.

**Step 5**. **click on the link *authenticate sally.the.doer@jit.si*** to open the *Authenticate Buddy* window:

![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-39.png)

*Figure 10: Authenticate Buddy window with fingerprints for you and your contact*

Note the message that encourages you to compare the fingerprints of your keys with your contact over another channel (not this text chat). In doing this, you can be more certain that you are communicating with your contact and not somebody else. A good choice for key comparisons is to do it face to face, or via video or voice communication as these provide easier means to authenticate the identity of the other person. After you compare fingerprints, **select** the option ***I have* verified** the fingerprint from the pull-down menu and **click on *Authenticate Buddy***:

![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-40.png)

*Figure 11: Part of the Authenticate Buddy window after selecting "I have" verified the fingerprint of your contact*

Closing the *Authenticate Buddy* window returns you to the chat window:

![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-41.png)

*Figure 12: Text chat window with authenticated OTR encryption*

Note that padlock no longer includes the orange triangle with the white exclamation mark. This means that you have authenticated your contact. **The authentication should be done only once per contact.** If the triangle with exclamation mark returns, it means that you are chatting to somebody who you have not yet authenticated. This can happen when your contact moves to another device with another encryption key (another installation of Jitsi, or another OTR enabled program, etc.). In this case you will need to re-authenticate each other again to be sure of the identity of person with whom you communicate.

**Jitsi** allows you to text chat with more than one person in the same time. OTR encryption will only work when chatting to one person.


## 4.3 Use Jitsi for secure voice calls 

**Jitsi** offers voice and video chats which can be independently encrypted with open standard called ZRTP. In order to initiate the chat you need to 

**Step 1**. **Click** on the contact in **Jitsi** contact list and **click** on the voice (second icon from the left under the contact's name) or video (third) icon - see figure 5 above. A new window will appear indicating that **Jitsi** is establishing the connection:

![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-42.png)

*Figure 13: Call window indicating Ringing status*

Your contact will see incoming call notification:

![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-43.png)

*Figure 14: Incoming call notification*

**Step 2.** If your contact **accepts the call** you will receive information that you are connected:

![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-44.png)

*Figure 15: Received call window without ZRTP encryption*

**Note** the red open padlock. This means that your call is not yet encrypted with ZRTP.

**Step 3.** **Wait...** Your and your contact's programs are establishing an encrypted connection, which may take a moment. If they succeed you will see the letters *zrtp* appear against an orange backgrond with a closed padlock like below. If they don't succeed in establishing a connection, you still can chat but without encryption. You can disconnect, restart **Jitsi** and try again to see if this time the programs will connect with encryption. ZRTP may not work in calls between accounts from different providers (such as between Google and Jit.si).

![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-45.png)

*Figure 16: Part of the Call window with ZRTP encryption engaged but not yet confirmed*

**Step 4**. **Observe** the section under the letters *zrtp* and padlock with the message "Compare with partner" followed by 4 characters. **Read** these letters to your contact and ask if she sees the same characters. If she does, it means that your communication is encrypted and nobody is interfering with it. You can **click *Confirm***. The orange *zrtp* field will turn green:

![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-46.png)

*Figure 17: Part of the Call window with confirmed ZRTP encryption engaged*

**Step 5**. You may close the black confirmation section of the window by clicking on the white x sign on upper-right part of the black section:

![](/sites/siabnext.ttc.io/files/media/jitsi-en-win-47.png)

*Figure 18: Part of the call window with confirmed ZRTP encryption engaged*

**Jitsi** lets you voice and video chat with more than one person. **Note** that with this communication, ZRTP encryption can be engaged between initiator of the call and other parties, but not between parties themselves.

