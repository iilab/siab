

---

lang: en
community: guide
type: tools
os: linux
weight: 060
title: Jitsi for Linux - Secure instant messaging and VoIP

---

**Jitsi** is cross-platform, [**free and open-source software**](/en/glossary#FOSS) for **Instant Messaging** (**IM**), **Voice over IP** (**VoIP**) and video chat. It is compatible with many popular IM and telephony services and provides reliable *end-to-end* encryption for text chats (and somewhat experimental *end-to-end* encryption for voice chats).

# Required reading


:[Keep your online communication private](../../../tactics/secure communication)


:[Jitsi for Linux - Secure instant messaging and VoIP](jitsi-for-linux-secure-instant-messaging-and-voip)

# What you will get from this guide

- Secure, end-to-end encrypted voice and video chat 
- The ability to encrypt your communications so that even your account providers cannot access the content of your communications
- The ability to use different accounts with various protocols (including Jabber/XMPP, SIP, Google Talk, Facebook, and Yahoo Messenger) simultaneously from within one program

# 1. Introduction to Jitsi

**Jitsi** is cross-platform, [**free and open-source software**](/en/glossary#FOSS) for **Instant Messaging** (**IM**), **Voice over IP** (**VoIP**) and video chat. It is compatible with many popular IM and telephony protocols, including *Jabber/XMPP*, *Facebook Messenger*, *AIM*, *ICQ*, *MSN*, *Yahoo! Messenger* and *SIP*. It provides *end-to-end* encryption for text chats through the [**Off-the-Record** (**OTR**)](/en/glossary#OTR) protocol. It also supports end-to-end encrypted voice chat using *ZRTP*.

**Important:** If you *and those with whom you communicate* use **OTR** encryption for text chats and **ZRTP** encryption for voice chats, Jitsi will protect the *content* of your conversations from service providers like Google and Facebook. However, these providers can still monitor certain *meta-data* about the conversations you have through Jitsi. Examples include: 

- The list of users with whom you communicate 
- The frequency and duration of those conversations
- The fact that you are using encryption to "hide" your communication

They can share this information with third parties, including other companies and governments. For conversations where such *meta-data* could be sensitive, you *and those with whom you communicate* should consider using a trusted, independent service provider for your [XMPP/Jabber chats](#2273) and your [SIP calls](#2387).

## 1.0 Things you should know about Jitsi before you start

Jitsi allows you to use your existing accounts to communicate securely through the use of *end-to-end* encryption. This not only makes the content of your communication inaccessible to various third parties, such as government or corporate surveillance platforms, it also protects your conversations from those who operate the chat services themselves (such as Facebook, if you are using *Facebook Messenger*, or Google, if you are using *Google Talk*). 

**Note:** Jitsi was written in the Java programming language. As such, Java must be installed on your computer in order for it to work. Though Java itself does not represent a significant security risk, *Java browser extensions* are often found to contain vulnerabilities that allow malicious websites to assume control of your computer or install malware. If your browser has a Java plugin installed, we strongly recommend that you [disable it](https://www.java.com/en/download/help/disable_browser.xml).


## 1.1 Other tools like Jitsi

**Jitsi** is available for **GNU Linux**, **Mac OS** and **MS Windows**. It can be used to communicate with other *XMPP* or *SIP* clients that support end-to-end encryption through **OTR** (for text chat) or **ZRTP** (for voice chat). Examples are recommended below: 

- For encrypted **text chat**: [**Pidgin**](https://pidgin.im/) (**MS Windows** and **GNU Linux**), [**Miranda**](http://www.miranda-im.org/) (**MS Windows**), [**Adium**](https://adium.im/) (**Mac OS X**), [**ChatSecure**](https://guardianproject.info/apps/chatsecure/) ([**Android**](../chatsecure/android) and **iOS**).

- For encrypted **voice chat**: **CSipSimple** (**Android**), [**Linphone**](http://www.linphone.org/) (**GNU Linux**, **MS Windows**, **Mac OS X**, **Android**, **iOS**, and others.)


# 2. Install and configure Jitsi

We normally recommend installing Linux applications using the *package manager* or *software center* that comes with your distribution. Unfortunately, the version of Jitsi included in many distributions is outdated and may include known [security](https://web.archive.org/web/20150202001841/https://download.jitsi.org/jitsi/windows/updates/) [vulnerabilities](https://web.archive.org/web/20150801033003/https://download.jitsi.org/jitsi/windows/updates/). We recommend installing the latest *stable* version directly from the developer's website.



## 2.1. Install Jitsi

**Note**: These instructions apply to *Ubuntu* and other Debian-based Linux distributions.

To install Jitsi, follow the steps below:

**Step 1**. **Browse** to the *Jitsi* download page: [https://download.jitsi.org/jitsi/debian/](https://download.jitsi.org/jitsi/debian/)

![](/sites/securityinabox.org/files/media/jitsi-lin-en-v02-006.png)

*Figure 1: The Jitsi download page*

**Step 2**. **Scroll down** and **Click** one of the two files below to download the latest stable Jitsi *Debian package* 

- For 32 bit systems: `jitsi_2.8.5426-1_i386.deb`
- For 64 bit systems: `jitsi_2.8.5426-1_amd64.deb`

If you are not sure if you are using a 32 or 64 bit system, launch the *Terminal* application and execute the following command in *Terminal*:

`uname –m`

If you are running a **32-bit** system, *Terminal* will display `i686` or `i386`. If you're running a **64-bit** system, it will display `x86_64`.

Now that you know whether you are running a 32-bit or 64-bit system, you can download the appropriate Jitsi Debian package.

**Important:** If a *newer* version of jitsi is available, it will look just like the files listed above, but it will have a higher number (instead of `2.8.5426-1`) after `jitsi_` and before `_i386.deb` or `_amd64.deb`. If you see a newer version *on this page*, you should download and install it instead.

Your browser will ask you what to do with the file.

![](/sites/securityinabox.org/files/media/jitsi-lin-en-v02-007.png)

*Figure 2: Downloading the Jitsi package and opening it in the software center*

**Step 3**. Make sure the box next to *Open with* shows the name of your distribution's *software center* 

**Step 4**. **Click** **[OK]** to open the package in your *software center*

![](/sites/securityinabox.org/files/media/jitsi-lin-en-v02-008.png)

*Figure 3: The software center ready to install Jitsi*

**Step 5**. **Click** **[Install]** to activate the authentication screen

**Note**: If you have an older version of Jitsi installed (such as the version that comes built-in to your *package manager*), the screen shown in *Figure 3* will have an **[Upgrade]** button rather than an **[Install]** button. Clicking **[Upgrade]** will safely replace your older version with the one you have just downloaded. Your existing accounts and contacts will remain available.

![](/sites/securityinabox.org/files/media/jitsi-lin-en-v02-010.png)

*Figure 4: The software center requires your passphrase to install Jitsi*

**Step 6**. **Type** the passphrase you use to log in to your computer.

**Step 7**. **Click** **[Authenticate]** to begin installing Jitsi

![](/sites/securityinabox.org/files/media/jitsi-lin-en-v02-011.png)

*Figure 5: The software center installing Jitsi*

When it is done installing Jitsi, the *software center* will display a white checkmark in a green circle and the progress bar will turn into a **[Reinstall]** button.

![](/sites/securityinabox.org/files/media/jitsi-lin-en-v02-012.png)

*Figure 6: The software center after installing Jitsi*

**Step 8**. **Close** the *software center*

## 2.2. Add accounts to Jitsi

Jitsi supports many different protocols and services for chat. The first time you launch it, you will see the window shown in *Figure 1*, which allows you to add the accounts you want to access through Jitsi.

![](/sites/securityinabox.org/files/media/jitsi-lin-en-v01-204-accounts.png)

*Figure 1: Jitsi's initial account configuration screen*

**Note:** Both Google Talk and Facebook may require that you change certain *account settings* before you can access their chat services through Jitsi. To learn how, see the following two sections: 

- [Google Talk](#2271)
- [Facebook Messenger](#2272)

You can use this screen to enter a *username* and *password* for each of the services displayed, thereby adding up to four accounts in one easy step. But *you must already have accounts on these services* to do so. The sections below describe how to set up accounts for various IM and VoIP service providers.

### 2.2.1. How to add a Google Talk account to Jitsi

As shown in *Figure 1* of [the previous section](#2270), the first time you launch Jitsi, you will see an account configuration screen that allows you to add various chat services to the application. After you have added at least one account, this screen will no longer appear. In order to add *additional* accounts, follow the steps below. 

**Step 1**. **Click** *File* in Jitsi's menu bar and **select** *Add new account...* to choose the service or protocol you want to use.

![](/sites/securityinabox.org/files/media/jitsi-lin-en-v01-207-add_accounts.png)

*Figure 1: the Add New Account screen*

**Step 2**. **Select** *Google Talk* from the *Network* list to enter your username and passphrase

![](/sites/securityinabox.org/files/media/jitsi-lin-en-v01-208-new.png)

*Figure 2: Entering a username and password into the Add New Account screen* 

**Step 3**. **Type** your Gmail username. 

**Step 4**. **Type** your Gmail passphrase.

**Step 5**. (Optional) **Uncheck** the *Remember password* box

**Important:** If you want Jitsi to remember your passphrases for you, you should *first* [enable its *Master Password* feature](#2278).

**Step 6**. **Click** **[Add]** 

You can now use Jitsi to communicate through the Google Talk account you have added.

**Note:** If you are using [2-step verification](https://support.google.com/accounts/answer/180744?hl=en) to protect access to your Gmail account, you might see an error like the one shown in *Figure 3* when Jitsi tries to access your account. (It will display the same error if you get your passphrase wrong.) To log in using Jitsi, you will need to generate an "**application-specific password**". To learn how, see [Google's instructions](https://support.google.com/accounts/answer/185833?hl=en).

![](/sites/securityinabox.org/files/media/jitsi-lin-en-v01-209-new.png)

*Figure 3: Google Talk authentication failed (possibly as a result of "2-step verification" settings)*

### 2.2.2. How to add a Facebook account to Jitsi

There are two settings that you might need to change, on the Facebook website, for Jitsi to use Facebook as a chat service.

**Facebook Username** 

Before Jitsi can connect to Facebook, you must assign a *username* to your Facebook account. Unlike most Web services, Facebook does not require you to select a username when you create your account, but it does allow you to create one if you wish. You can confirm your username by signing into your Facebook account. Your username is what appears in the location bar of your browser after *https://www.facebook.com/* when you view your *Timeline* or *Page*. So, if your username is *terrence.the.tester*, you should see *https://www.facebook.com/terrence.the.tester* in your browser's location bar when viewing your *Timeline*. Your username is also part of your Facebook email address (terrence.the.tester@facebook.com, for example). 

If you do not have a Facebook username, you can choose one by signing into your account and selecting **Settings > General** or by browsing to *https://www.facebook.com/username*. Facebook might require that you verify your account before allowing you to select a username. This might require giving Facebook a mobile phone number at which you can receive a text message. For more details see Facebook’s [explanation of usernames](https://www.facebook.com/help/329992603752372/).

**App Settings** 

You must turn on Facebook’s “**application platform**” in order to give Jitsi access to your account. To do this, sign in, select **Settings > Apps** and confirm that that the *Apps, Websites and Plugins* setting is **Enabled**.
 
**Note:** Turning on Facebook’s *application platform* opens up much of your Facebook data to third-party application developers. This data is available not only to the Facebook applications that you use, but also to the Facebook applications used by your friends. After turning on Facebook’s *Apps, Websites and Plugins*, be sure to check the settings under *Apps others use*. This setting allows you to hide some personal information from applications used by your friends. Unfortunately, Facebook does not offer settings to hide all personal information. As long as the *application platform* is *Enabled*, certain categories of data (including your friend list, your gender, and any information you have made public) are accessible to apps used by others. *If this is unacceptable, you should disable Apps, Websites and Plugins and avoid using Jitsi with Facebook Messenger.*

Once have chosen a Facebook username and enabled the *application platform*, you can add your Facebook account to Jitsi. 

As shown in *Figure 1* of [the *Add accounts to Jitsi* section](#2270), the first time you launch Jitsi, you will see an account configuration screen that allows you to add various chat services to the application. After you have added at least one account, this screen will no longer appear. In order to add *additional* accounts, follow the steps below. 

**Step 1**. **Click** *File* in Jitsi's menu bar and **select** *Add new account...* to choose the service or protocol you want to use.

![](/sites/securityinabox.org/files/media/jitsi-lin-en-v01-207-add_accounts.png)

*Figure 1: the Add New Account screen*

**Step 2**. **Select** *Facebook* from the *Network* list to enter your username and passphrase

![](/sites/securityinabox.org/files/media/jitsi-lin-en-v01-new-facebook.png) 

*Figure 2: Entering a username and password into the Add New Account screen* 

**Step 3**. **Type** your Facebook username 

**Step 4**. **Type** your Facebook passphrase. 

**Step 5**. (Optional) **Uncheck** the *Remember password* box

**Important:** If you want Jitsi to remember your passphrases for you, you should *first* [enable its *Master Password* feature](#2278).

**Step 6**. **Click** **[Add]** 

You can now use Jitsi to communicate through the Facebook account you have added.


### 2.2.3. How to add a Jabber/XMPP account to Jitsi

*XMPP* and *Jabber* are different names for the same instant messaging protocol. It is an open standard, and there are [many providers](https://xmpp.net/directory.php) who offer free Jabber/XMPP accounts that you can use with Jitsi. The IM Observatory allows you to [evaluate some security properties of public Jabber/XMPP services](https://xmpp.net/index.php).

If you have experience running online services, you can also install a [Jabber/XMPP server](http://xmpp.org/xmpp-software/servers/) (such as [ejabberd](http://www.process-one.net/en/ejabberd/) or [Prosody IM](http://prosody.im/)) on your own server and provide accounts to members of a particular community or organization.

Below, we recommend a few services that have a great deal of experience protecting their users' privacy. (But remember, you are relying primarily on *OTR* encryption to keep your chats confidential, so you still need to make sure that you and those with whom you communicate know how to use it properly. This is covered in the section on [Using Jitsi for secure instant messaging](#2281).

#### Creating and adding a Jabber.ccc.de account

You can create an account on the *jabber.ccc.de* service (located in Germany) and add it to Jitsi, all at the same time, from within the application. This works for many traditional Jabber/XMPP services.

**Step 1**. **Click** *File* in Jitsi's menu bar and **select** *Add new account...* to choose the service or protocol you want to use.

![](/sites/securityinabox.org/files/media/jitsi-lin-en-v01-207-add_accounts.png)

*Figure 1: the Add New Account screen*

**Step 2**. **Select** *XMPP* from the *Network* list to create your account

![](/sites/securityinabox.org/files/media/jitsi-lin-en-v01-211-xmpp.png)

*Figure 2: the Add New Account screen*

The steps below assume that you do not yet have a *jabber.ccc.de* account. (If you do, just enter your username and passphrase and click **[Add]**.)

**Step 3**. **Select** *Create a new XMPP account*

![](/sites/securityinabox.org/files/media/jitsi-lin-en-v01-212-new.png)

*Figure 3: Creating a new jabber.ccc.de account, within Jitsi, using the Add New Account screen*

**Step 4**. **Type** *jabber.ccc.de* in the *Server* box

**Step 5**. **Choose** a username and **type** it into the *XMPP username* box

**Step 6**. **Choose** a passphrase and type it into the *Password* and *Confirm Password* boxes

**Step 7**. **Click** **[Add]** to request the username you have chosen. 

If the username you requested is unavailable, the registration process will fail, and Jitsi will announce that it: *failed to create your account due to the following error: Could not confirm data.* You can try again by repeating the process with a different username.

**Note**: If you do not log in to your *jabber.ccc.de* account for 12 months, your account will be removed, and your username will be made available for registration by others.


#### Creating a Riseup.net (Jabber/XMPP) account

[**Riseup**](https://help.riseup.net/en/about-us) is a collective dedicated to providing secure services for individuals and organizations committed to political and social justice. Their servers are located in the United States.

If you already have a [Riseup.net email account](../riseup/internet), you can use the same account for their [Jabber/XMPP service](https://www.riseup.net/en/chat). In order to create an account, you will need two *invitation codes* from two different *Riseup.net* members. You can then visit [https://user.riseup.net](https://user.riseup.net) and create an account. Once your account is active, you can add it to Jitsi by following the steps below.


#### Adding an existing Jabber/XMPP account to Jitsi 

As shown in *Figure 1* of [the *Add accounts to Jitsi* section](#2270), the first time you launch Jitsi, you will see an account configuration screen that allows you to add various chat services to the application. After you have added at least one account, this screen will no longer appear. In order to add *additional* accounts, follow the steps below. 

**Step 1**. **Click** *File* in Jitsi's menu bar and **select** *Add new account...* to choose the service or protocol you want to use.

![](/sites/securityinabox.org/files/media/jitsi-lin-en-v01-207-add_accounts.png)

*Figure 1: the Add New Account screen*

**Step 2**. **Select** *XMPP* from the *Network* list to enter your username and passphrase

![](/sites/securityinabox.org/files/media/jitsi-lin-en-v01-211-xmpp.png)

*Figure 2: Entering a username and password into the Add New Account screen* 

**Step 3**. **Type** the username for your Jabber/XMPP account on this service.

![](/sites/securityinabox.org/files/media/jitsi-lin-en-v01-211-super-new.png)

Your username should include the **@** symbol and the *hostname* of the service. For example 

- A *Riseup.net* username might look like:  **ekaterina@riseup.net**
- A *jabber.ccc.de* username might look like: **elena.katerina@jabber.ccc.de**

**Step 4**. **Type** the passphrase for your Jabber/XMPP account on this service.

**Step 5**. (Optional) **Uncheck** the *Remember password* box

**Important:** If you want Jitsi to remember your passphrases for you, you should *first* [enable its *Master Password* feature](#2278).

**Step 6**. **Click** **[Add]** 

You can now use Jitsi to communicate through this Jabber/XMPP account.

### 2.2.4 How to add a SIP account to Jitsi

In this section, we recommend only a single *Session Initiation Protocol (SIP)* provider, *ostel.co* (which is located in United States). There are many free SIP services online, but *ostel.co* appears to offer the most reliable support for end-to-end encryption through *ZRTP*. 

**Note**. Jitsi is less stable when used for encrypted voice chat than it is when used for encrypted text chat. You may find that the *Android* mobile application *CSipSimple* is a more reliable way to use your *ostel.co* account for encrypted VoIP.

#### Creating a free SIP account on ostel.co

Unlike (some) Jabber/XMPP accounts, SIP accounts cannot be registered from within Jitsi itself. To create an *ostel.co* account, follow the steps below

**Step 1.** Visit the *ostel.co* [registration page](https://ostel.co/users/sign_up)

![](/sites/securityinabox.org/files/media/jitsi-lin-en-v02-260.png)

*Figure 1: The ostel.co registration page*

**Step 2**. **Click** **[Sign me up]** to access the *ostel.co* sign-up form

![](/sites/securityinabox.org/files/media/jitsi-lin-en-v02-261.png)

*Figure 2: The ostel.co sign-up form*

**Step 3**. **Type** your email address (this can be any email address)

**Step 4**. **Click** **[Sign up]** to access the username and passphrase selection form

![](/sites/securityinabox.org/files/media/jitsi-lin-en-v02-262.png)

*Figure 3: The ostel.co username and passphrase selection form*

**Step 5**. **Select** or **Type** a "code name"

**Step 6**. **Choose** and enter a passphrase (twice)

**Step 7**. **Click** **[Create my account]** to complete the process of creating an *ostel.co* SIP account

![](/sites/securityinabox.org/files/media/jitsi-lin-en-v02-263.png)

*Figure 4: The ostel.co registration page after creating an account*

Once you have successfully registered with ostel.co, you can add your new SIP account to Jitsi by following the steps below

#### Adding an existing SIP account to Jitsi

As shown in *Figure 1* of [the *Add accounts to Jitsi* section](#2270), the first time you launch Jitsi, you will see an account configuration screen that allows you to add various chat services to the application. After you have added at least one account, this screen will no longer appear. In order to add *additional* accounts, follow the steps below. 

**Step 1**. **Click** *File* in Jitsi's menu bar and **select** *Add new account...* to choose the service or protocol you want to use.

![](/sites/securityinabox.org/files/media/jitsi-lin-en-v01-207-add_accounts.png)

*Figure 1: the Add New Account screen*

**Step 2**. **Select** *SIP* from the *Network* list to enter your username and passphrase

![](/sites/securityinabox.org/files/media/jitsi-lin-en-v01-new-sip.png)

*Figure 2: Entering a username and password into the Add New Account screen* 

**Step 3**. **Type** your *ostel.co* username 

**Step 4**. **Type** your *ostel.co* passphrase. 

**Step 5**. (Optional) **Uncheck** the *Remember password* box

**Important:** If you want Jitsi to remember your passphrases for you, you should *first* [enable its *Master Password* feature](#2278).

**Step 6**. **Click** **[Add]** 

You can now use Jitsi for Voice-over-IP (VoIP) calls through the *ostel.co* SIP service. If you *and those with whom you are communicating* both have *ostel.co* accounts — and if you both configure your applications properly — your conversations will be end-to-end encrypted using the *ZRTP* protocol. To learn more about how to do this, see the section on [Using Jitsi for secure voice and video calls](#2282).



## 2.3. How to change an account password in Jitsi

Many of the accounts that you can use on Jitsi enable you to change your password directly from their web interface, as part of their settings. However, some Jabber/XMPP and SIP accounts don't have a web interface through which you can manage and change your passwords. For such accounts, you can change your passwords through the following steps: 

**Step 1:** Select **Tools > Options** through the menu bar of Jitsi, and then select the “**Accounts**” tab.
 
![](/sites/securityinabox.org/files/media/jitsi-lin-en-v01-214-new.png)

**Step 2:** Click on “**Edit**” to activate the following window:

![](/sites/securityinabox.org/files/media/jitsi-lin-en-v01-215-new.png)

**Step 3:** Click on “**Change account password**” to activate the following window:
 
![](/sites/securityinabox.org/files/media/jitsi-lin-en-v01-216-new.png)

**Step 4:** Enter your new password, re-enter it and then click on “**OK**”.

You have now successfully changed your account's password.

# 3. Strengthen Jitsi's security settings





## 3.1. How to clear and disable your chat history

Jitsi by default stores information about the incoming and outgoing voice/video calls and about the history of all the instant messages that you sent and received. You can access voice/video calls by clicking on the clock icon on the main Jitsi window:

![](/sites/securityinabox.org/files/media/jitsi-lin-en-v01-301-new.png)

You can view your the history of your instant messages by clicking on the hourglass like icon in the chat window while chatting with a contact: 

 ![](/sites/securityinabox.org/files/media/jitsi-lin-en-v01-302-new.png) 

This information is collected and stored on the disk of your computer. **Even if you encrypt the text chat with OTR all the text messages you send and receive are stored on your computer in open text format**. The same information is collected and stored on the disk of the contacts you are communicating with.

To prevent Jitsi from collecting this information (and to remove data that has already been gathered), you and your contact can take the steps described below. 

**HOW TO DISABLE JITSI FROM COLLECTING INFORMATION:**

**Step 1:** Select **Tools > Options** from the menu bar of Jitsi.
 
**Step 2:** Select the **General tab** and *uncheck* the “**Log chat history**” option as shown below:

 ![](/sites/securityinabox.org/files/media/jitsi-lin-en-v01-303-log_chat.png) 

**Step 3:** Select the **Advanced tab**, click on “**Logging**” and *uncheck* the “**Enable packet logging**” option, as shown below:

 ![](/sites/securityinabox.org/files/media/jitsi-lin-en-v01-304-logging.png)

Your changes will take effect after you restart Jitsi. 

**HOW TO REMOVE COLLECTED INFORMATION ABOUT YOUR CALLS AND TEXT MESSAGES:**

**Step 1:** Quit Jitsi.
 
**Step 2:** Go to your home folder and remove the entire log history folder from the Jitsi user profile folder. You can remove a sub-folder if you only want to dispose part of the history. The location of the user profile and log history folders depends on the operating system:

* Linux: from your home folder ~/.jitsi/history_ver1.0
* Mac OS X: from your home folder ~/Library/Application Support/Jitsi/history_ver1.0
* On Windows Vista, 7, 8, this is C:\Users\<Windows login/user name>\AppData\Roaming\Jitsi\history_ver1.0 (Note that "AppData" folder may be hidden. See [how to see hidden files](http://windows.microsoft.com/en-us/windows/show-hidden-files))
* On Windows XP and earlier, this is located in C:\Documents and Settings\<Windows login/user name>\Application Data\Jitsi\history_ver1.0

**Note:** On Linux, the ".jitsi" folder might be hidden. See [how to see hidden files in Ubuntu](http://itsfoss.com/hide-folders-and-show-hidden-files-in-ubuntu-beginner-trick/). See the [How to destroy sensitive information chapter](https://securityinabox.org/en/guide/destroy-sensitive-information) for more on how to dispose information securely.

## 3.2. How to initiate private messaging

It is recommended that you set up Jitsi to require private and encrypted instant messaging whenever possible, through the use of OTR encryption.

You can quickly and easily enable OTR and require encrypted, private instant messaging through the following simple steps:

**Step 1:** Select **Tools > Options** in the menu bar of Jitsi.

**Step 2:** Select the **Security tab**, select its **Chat sub-tab** and then check "**Automatically initiate private messaging**" at the bottom of the screen, as shown below:

![](/sites/securityinabox.org/files/media/jitsi-lin-en-v01-new-pm.png)

## 3.3. How to set a Master password for Jitsi

It might not be best to let Jitsi remember the passwords to your accounts. If you decide otherwise for ease of use, anybody who gets access to your computer will be able to log in to your accounts by simply starting Jitsi. It will also be possible to view your passwords in the Options window. It is therefore strongly recommended to protect passwords to your accounts with a good master password. Once you set up the master password, Jitsi will ask you for it upon starting the program.

You can set a master password for Jitsi through the following steps:

**Step 1:** Select **Tools > Options** in the menu bar of Jitsi.

**Step 2:** Select the **Security tab**, select its **Passwords sub-tab** and check “**Use a master password**” to activate the Master Password window.

**Step 3:** Type in your password in the new window, as shown below. For more on creating a strong password, see [“Create and maintain secure passwords”](https://securityinabox.org/en/guide/passwords).

![](/sites/securityinabox.org/files/media/jitsi-lin-en-v01-306-mp.png)

**Step 4:** Click on “**OK**” to confirm the password and to activate a new window which should say “**Master Password successfully set up**”. Click on “**OK**” to close that window.

**Note:** The “**Change Master Password**” button lets you change the master password. The “**Saved Passwords...**” button lets you access the list of passwords remembered by Jitsi and remove them if needed.

# 4. Encrypt your instant messages and voice calls with Jitsi

After adding at least one account on Jitsi and logging in, you are ready to add your contacts and communicate with them.

## 4.1. Adding contacts in Jitsi

You can add your contacts on Jitsi through the following steps:

**Step 1:** Select **File > Add contact...** in the menu bar of Jitsi. The following window should appear:

![](/sites/securityinabox.org/files/media/jitsi-lin-en-v01-401-new.png)

**Step 2:** Select the account that you would like to add this contact to (e.g. electra.stormborn@riseup.net).
 
**Optional:** You can also add the contact to a group among your other contacts. However, you first need to create the group. You can do this by selecting **File > Create group...** from the menu.

**Step 3:** Type in the username or address of your contact into the “**ID or Number**” field (e.g. sally.the.doer).
 
You can choose the name or nickname for your contact, which will be visible in your contacts list in the Jitsi main window. You can type it into the “**Display name**” field.

**Step 4:** Click on “**Add**” to close the “**Add contact**” window and go back to your main Jitsi window. You will now see your new contact added in your contact list with the note “**Waiting for authorisation**”, until she accepts your request.

**Step 5:** When your contact (e.g. electra.stormborn@riseup.net) logs into her account, a pop-up window will inform her that you have requested to add her to your list of contacts:

![](/sites/securityinabox.org/files/media/jitsi-lin-en-v01-403-new.png)

Your contact can choose one of the following options:

* **Ignore:** in which case your request will continue awaiting authorisation 
* **Deny:** in which case you will receive information that your request was rejected 
* **Authorise:** in which case you will receive information that your contact has accepted your authorisation request, and the entry for your contact in your contact list will become active.

![](/sites/securityinabox.org/files/media/jitsi-lin-en-v01-404-new.png)

Once you have added and authorised your contact, you can click on their name in the contact list and initiate instant messaging, voice or video calls, and desktop sharing, by choosing the relevant icon under their name.

## 4.2. Using Jitsi for secure instant messaging

[Off-the-Record (OTR)](https://otr.cypherpunks.ca/) is a cryptographic protocol that provides end-to-end encryption for instant messaging, which prevents anyone other than the intended recipient from reading your messages. OTR allows you to authenticate one other, which is essential for encryption to work properly. Authentication is done by establishing a "shared secret," by exchanging cryptographic [fingerprints](https://otr.cypherpunks.ca/help/fingerprint.php) or by asking one another questions to which only the other person would know the answer. OTR also provides forward secrecy. This means that even if the encryption key of one OTR user is compromised, your past conversations could be decrypted.

OTR is supported by Jitsi and can be used to encrypt your instant messages. You can enable the encryption of your instant messages through the following steps:

**Step 1:** Select **Tools > Options** in the menu bar of Jitsi.

**Step 2:** Select the **Security tab** and its **Chat sub-tab**. You will then see a window similar to the one included below:

![](/sites/securityinabox.org/files/media/jitsi-lin-en-v01-406-new.png)

**Step 3:** Click on the “**Generate**” button. As a result you will see the fingerprint of the key that has been generated:

![](/sites/securityinabox.org/files/media/jitsi-lin-en-v01-407-new.png)

One encryption key is generated for every account. You only need to do this again if you add a new account or install Jitsi on another device and do not move the existing keys to it. 

**Step 4:** Select a contact from the main Jitsi window and click on the “**send message**” icon (first from the left under the contact's name) to open a text chat window:

![](/sites/securityinabox.org/files/media/jitsi-lin-en-v01-408-new.png)

**Note:** The “**Encrypt chat with OTR**” icon (the open padlock on the right-top side of the window) informs you whether the chat is encrypted or not. 

**Step 5:** Click on the “Encrypt chat with OTR” icon. Note the changes in the window:

![](/sites/securityinabox.org/files/media/jitsi-lin-en-v01-409-new.png)

**Note:** The padlock is now locked. This means that whatever messages you and your contact send to each other are encrypted. Note the message that this is an unverified private conversation and that you should authenticate electra.stormborn@riseup.net.

**Step 6:** Click on the link “**authenticate electra.stormborn@riseup.net**” to open the “**Authenticate Buddy**” window:

![](/sites/securityinabox.org/files/media/jitsi-lin-en-v01-410-new.png)

The message encourages you to compare the fingerprints of your keys with your contact over another channel (not over this chat). In doing this, you can be more certain that you are communicating with your contact and not somebody else. A good choice for key comparisons is to do it face to face, or via video or voice communication as these provide easier means to authenticate the identity of the other person. 

**Step 7:** Once you have compared fingerprints, select the option “**I have**” from the pull-down menu which pertains to the verification of fingerprints and copy-paste your contact's fingerprint. Subsequently, click on “**Authenticate Buddy**”:

![](/sites/securityinabox.org/files/media/jitsi-lin-en-v01-411-new.png)

By closing the “**Authenticate Buddy**” window, you return to the chat window:

![](/sites/securityinabox.org/files/media/jitsi-lin-en-v01-412-new.png)

You can now exchange encrypted instant messages with your contacts.

![](/sites/securityinabox.org/files/media/jitsi-lin-en-v01-encrypted_chat.png)

**Note:** The authentication should be done only once for each account. If the triangle with the exclamation mark returns, it means that you are chatting to somebody who you have not yet authenticated. This can happen when your contact moves to another device with another encryption key (another installation of Jitsi, or another OTR enabled program, etc.). In this case you will need to re-authenticate each other to be sure of the identity of the person with whom you are communicating.

## 4.3. Using Jitsi for secure voice and video calls

Jitsi offers voice and video calls which can independently be encrypted with an open standard called **ZRTP**. You can initiate encrypted voice and video calls through the following steps:

**Step 1:** Click on your contact in your Jitsi contact list and subsequently click on the voice (second icon from the left under the contact's name) or video (third) icon. A new window will appear indicating that Jitsi is establishing the connection:

![](/sites/securityinabox.org/files/media/jitsi-lin-en-v01-413-new.png)

When you or your contact receive an incoming call, you will see the following type of notification:

![](/sites/securityinabox.org/files/media/jitsi-lin-en-v01-414-new.png)

**Step 2:** When you and your contact accept the call, you will receive information that you are connected. The red open padlock means that your call is *not* yet encrypted with ZRTP.

**Step 3:** Wait... 

Your and your contact's programs are establishing an encrypted connection, which might take a moment. If they succeed you will see the letters zrtp appear against an orange background with a closed padlock, as illustrated below: 

![](/sites/securityinabox.org/files/media/jitsi-lin-en-v01-416-new.png)

If they don't succeed in establishing a connection, you can still chat but without encryption. You can disconnect, restart Jitsi and try again to see if this time the programs will connect with encryption. In some cases, ZRTP might not work for calls between the accounts of different providers (such as between Google and Jit.si).

**Step 4:** Observe the section under the letters zrtp and the characters included in the padlock under it. Read these characters to your contact and ask if she sees the same characters. If she does, it means that your communication is encrypted and nobody is interfering with it. You can then click on “**Confirm**”. This will turn the orange zrtp field into green:

![](/sites/securityinabox.org/files/media/jitsi-lin-en-v01-417-new.png)

**Step 5:** You can close the black confirmation section of the window by clicking on the white x sign on the upper-right part of the black section:

![](/sites/securityinabox.org/files/media/jitsi-lin-en-v01-418-new.png)

You can now have encrypted voice and video calls.

**Note:** Jitsi lets you have encrypted voice and video calls with more than one person. ZRTP encryption can be used between the initiator of the call and other parties, but not between the parties themselves.
