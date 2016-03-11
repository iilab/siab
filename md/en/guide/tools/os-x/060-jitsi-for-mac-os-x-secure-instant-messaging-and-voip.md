

---

lang: en
community: guide
type: tools
os: os-x
weight: 060
title: Jitsi for Mac OS X - Secure instant messaging and VoIP

---

**Jitsi** is cross-platform, [**free and open-source software**](/en/glossary#FOSS) for **Instant Messaging** (**IM**), **Voice over IP** (**VoIP**) and video chat. It is compatible with many popular IM and telephony services and provides reliable *end-to-end* encryption for text chats (and somewhat experimental *end-to-end* encryption for voice chats).

# Required reading


{{ required_reading: ../../secure communication }}


{{ tool: ./060-tool.md }}

# What you will get from this guide

- Secure, end-to-end encrypted voice and video chat 
- The ability to encrypt your communications so that even your account providers cannot access the content of your communications
- The ability to use different accounts with various protocols (including **Jabber/XMPP**, **SIP**, **Google Talk**, **Facebook**, and **Yahoo Messenger**) simultaneously from within one program

# 1. Introduction to Jitsi

**Jitsi** is cross-platform, [**free and open-source software**](/en/glossary#FOSS) for **Instant Messaging** (**IM**), [**Voice over IP**](/en/glossary#VoIP) (**VoIP**) and video chat. It is compatible with many popular IM and telephony protocols, including *Jabber/XMPP*, *Facebook Messenger*, *AIM*, *ICQ*, *MSN*, *Yahoo! Messenger* and *SIP*. It provides *end-to-end* encryption for text chats through the [**Off-the-Record** (**OTR**)](/en/glossary#OTR) protocol. It also supports end-to-end encrypted voice chat using *ZRTP*.

**Important:** If you *and those with whom you communicate* use **OTR** encryption for text chats and **ZRTP** encryption for voice chats, **Jitsi** will protect the *content* of your conversations from service providers like **Google** and **Facebook**. However, these providers can still monitor certain *metadata* about the conversations you have through **Jitsi**. Examples include: 

- The list of users with whom you communicate 
- The frequency and duration of those conversations
- The fact that you are using encryption to ‘hide’ your communication

They can share this information with third parties, including other companies and governments. For conversations where such *metadata* could be sensitive, you *and those with whom you communicate* should consider using a trusted, independent service provider.

## 1.0 Things you should know about Jitsi before you start

**Jitsi** allows you to use your existing accounts to communicate securely through the use of *end-to-end* encryption. This not only makes the content of your communication inaccessible to various third parties, such as government or corporate surveillance platforms, it also protects your conversations from those who operate the chat services themselves (such as **Facebook**, if you are using **Facebook Messenger**, or **Google**, if you are using **Google Talk**). 

**Note:** **Jitsi** was written in the **Java** programming language. As such, **Java** must be installed on your computer in order for it to work. Though **Java** itself does not represent a significant security risk, ***Java** browser extensions are often found to contain vulnerabilities that allow malicious websites to assume control of your computer or install malware. If your browser has a **Java** plugin installed, we strongly recommend that you [disable it](https://www.java.com/en/download/help/disable_browser.xml).*


## 1.1 Other tools like Jitsi

**Jitsi** is available for **Mac OS**, **GNU Linux**, and **MS Windows**. It can be used to communicate with other **XMPP** or **SIP** clients that support end-to-end encryption through **OTR** (for *text chat*) or **ZRTP** (for *voice chat*). Examples are recommended below: 

- For encrypted *text chat*: [**Adium**](https://adium.im/) (**Mac OS X**),[**Pidgin**](https://pidgin.im/) (**MS Windows** and **GNU Linux**), [**Miranda**](http://www.miranda-im.org/) (**MS Windows**),  [**ChatSecure**](https://guardianproject.info/apps/chatsecure/) ([**Android**](../chatsecure/android) and **iOS**).

- For encrypted *voice chat*: **CSipSimple** (**Android**), [**Linphone**](http://www.linphone.org/) (**GNU Linux**, **MS Windows**, **Mac OS X**, **Android**, **iOS**, and others.)


# 2. Download and Install Jitsi





## 2.1 Download Jitsi

To install the latest stable version of **Jitsi**, follow the steps below:

**Step 1**. **Go** to the [Jitsi download page](https://jitsi.org/Main/Download). 

**Tip**: Make sure you're on the secure version of the  [Jitsi download page](https://jitsi.org/Main/Download) before you download anything. (The **'https'** part encrypts the connection between your browser and the website, thus making it harder for an attacker to modify the file you're going to download.)

**Step 2**. **Select** the appropriate **Jitsi** *Mac OS X Package* for your computer’s *operating system*. 

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-201-jitsi-dwnld-page.png)

*Figure 1: Jitsi’s Download Page*

If you are using **OS X** versions 10.8 and above, **click** on the main *Mac OS X Packages* link directly below the *apple icon*. If you are using versions 10.6 or 10.7, **click** on the *’No-JRE Packages Mac OS X 10.6/10.7’* link. Most users with up-to-date operating systems will click on the main *Mac OS X Packages* link.

**Tip**: If you are unsure of which version your *operating system* is, **click** on the *apple icon* in the menu at the top of your screen, then **scroll** down to **select** *About This Mac*. A window will appear that includes the current version number of your *operating system*.

**Step 3**. **Click** to **download** the appropriate version of **Jitsi**. **Save** it to your *Downloads* folder.

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-202-dwnload-jitsi.png)

*Figure 2: Downloading Jitsi*

## 2.2 Install Jitsi

To install **Jitsi**, follow the steps below: 

**Step 1**. **Navigate** to the folder in which you saved the **Jitsi** package (titled *‘jitsi-latest.dmg'* or *‘jitsi-no-jre-latest.dmg’*). In this example, we saved it in the *Downloads* file.

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-203-saved-jitsi-file.png)

*Figure 1: The Downloads folder containing the Jitsi .dmg file*

**Step 2**. **Double-click** the **Jitsi** .dmg file to mount it as a disk image. It should show up in a new window (*Figure 2*, below) and under *Devices* in the left-hand sidebar of a normal *Finder* window.

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-204-mounted-dmg.png)

*Figure 2: Inside the mounted Jitsi disk image*

**Step 3**. Drag the **Jitsi.app** into the *Applications* folder.

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-205-drag-app.png)

*Figure 3: Dragging the mounted Jitsi.app into the Applications folder*

It will then copy over into *Applications*.

**Step 4**. Before we start using **Jitsi**, we should **unmount** (or **'eject'**) the **Jitsi** disk image. Find *Jitsi* under *Devices* in the *Finder sidebar*. **Click** on the {**eject**} icon next to it in the sidebar to **unmount** the disk image.

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-206-eject.png)

*Figure 4: Unmounting (or ejecting) the Jitsi disk image*

## 2.3 Install Java

**Jitsi** is written in the **Java** programming language and—at the time of writing—requires an older, 'legacy' version of **Java** in order to run on **Mac OS X**. 

Therefore, the first time you run **Jitsi**, you will probably see a message (as seen in *Figure 1*, below) informing you that you need to install the legacy **Java SE 6 runtime** in order to open and use **Jitsi**. (This same legacy version of **Java** is also called *'Java for OS X 2015-001'* by **Apple**, as seen in *Figure 2*, below.)

To install this required legacy version of **Java**, follow the steps below: 

**Step 1**. **Locate Jitsi** in your *Applications* folder and **double-click** to open it. 

**Step 2**. If you need to install the legacy **Java SE 6 runtime**, the alert in *Figure 1* will pop up.  

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-207-java-runtime-alert.png)

*Figure 1: Alert window notifying the user to install the legacy Java SE 6 runtime for Jitsi*

If you already have this version of **Java** installed, **Jitsi** will open without this installation message, and you can skip to **Section 3**, [**Adding accounts to Jitsi**](#2477). 

**Step 3**. **Click** on *’More Info…’* in the alert window. This will open up a [webpage](https://support.apple.com/kb/DL1572?locale=en\_US) in your browser where you can download the required legacy version of **Java 6** from **Apple**.

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-208-java-dwnload-page.png)

*Figure 2: Apple support page for legacy Java 6*

**Step 4**. To download the legacy version of **Java 6**, **click** on the [Download] button at the top of the webpage. **Save** the file to your *Downloads* file. 

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-209-java-dwnload.png)

*Figure 3: Download progress bar in Firefox*

**Step 5**. **Navigate** to the folder in which you saved the **Jitsi** file (titled ‘JavaForOSX.pkg’). In this example, we saved it in the *Downloads* file.

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-210-saved-java-file.png)

*Figure 4: The Downloads folder containing the Jitsi .pkg file*

**Step 6**. **Double-click** the **Java** .pkg file to mount it as a *disk image*. It should show up in a new window (*Figure 5*, below) and under *Devices* in the left-hand sidebar of a normal *Finder* window.

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-211-mounted-java-pkg.png)

*Figure 5: Inside the mounted Jitsi disk image*

**Step 7**. **Double-click** *JavaForOSX.pkg* in the mounted *disk image*. It will open the installer for the legacy version of **Java for OS X 2015-001**.

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-212-java-installer.png)

*Figure 6: Installer for Java*

**Step 8**. There is no special installation details for **Java**. **Click [Continue]** through the *Read Me* section, then **review** and **agree** to the *License* agreement. To **install Java** in the default location for installation (*Macintosh HD*), input an admin-level password to authorize the installation of **Java**.

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-213-java-installation-complete.png)

*Figure 7: Java installation complete*

When you are finished, the installer will show that *the installation was successful*.

**Step 9**. **Click [Close]** to exit the *Installer*.

**Step 10**. Before we continue, we should **unmount** (or **'eject'**) the **Java** *disk image*. Find *Java for OS X 2015-001* under *Devices* in the *Finder sidebar*. **Click** on the {**eject**} icon next to it in the sidebar to **unmount** the *disk image*.

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-214-eject-java-pkg.png)

*Figure 8: Unmounting (or ejecting) the Java disk image*

## 2.4 Running Jitsi for the first time

When you have the newest version of **Jitsi** and the legacy version of **Java SE 6** installed, you can open **Jitsi** for the first time. Depending on your *System Preferences* for **Mac OS X**, you may see a few messages when you run **Jitsi** for the first time. 

To navigate these and run **Jitsi** for the first time, follow the steps below: 

**Step 1**. As with most **Mac OS X** apps downloaded from sources *other* than those downloaded from **Apple’s** official **App Store**, you’ll see a confirmation alert the first time you open **Jitsi**.

**Navigate** to your *Applications* folder, **locate** the **Jitsi** app, and **double-click** to open it.

**Step 2**. You’ll see the pop-up in *Figure 1* below, asking you if *’you’re sure you want to open’* **Jitsi**. **Click [Open]**.

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-215-confirm-open.png)

*Figure 1: Confirmation alert when opening Jitsi for the first time*

**Step 3**. Depending on what your *Firewall* settings are in the *Security & Privacy* section of *System Preferences*, you may also see a second alert as **Jitsi** opens.

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-216-accept-incoming-connections.png)

*Figure 2: Authorization alert for Jitsi to accept incoming connections*

The alert window will ask you if you *’want the application “Jitsi.app” to accept incoming network connections?’* **Click [Allow]**. 

# 3. Adding accounts to Jitsi





## 3.1 Adding accounts to Jitsi

**Jitsi** supports many different services and protocols for *text chat*. The first time you launch **Jitsi**, you will see the window shown in *Figure 1*, which allows you to add the accounts you want to access through **Jitsi**.

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-301-configure-protocols.png)

*Figure 1: Jitsi's initial account configuration screen*

You can use this screen to enter a *username* and *password* for each of the services displayed, for a total of four accounts. But *you must already have accounts for these services* before configuring them for use here in the **Jitsi** client. The sections below describe how to set up accounts for various **IM** and **VoIP** service providers.

**Note:** Both **Google Talk** and **Facebook** may require that you change certain *account settings* before you can access their *text chat* services through **Jitsi**. To learn how, see the following two sections: 

- [Google Talk](#2479)
- [Facebook Messenger](#2480)

### 3.1.1 How to add a Google Talk account to Jitsi

As shown in *Figure 1* of [the previous section](#2478), the first time you launch **Jitsi**, you will see an account configuration screen that allows you to add various chat services to the application. After you have added at least one account, this screen will no longer appear. In order to add *additional* accounts, follow the steps below. 

**Step 1**. **Click** *File* in **Jitsi's** menu and **scroll down** to **select** *Add new account...* to choose the service or protocol you want to use.

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-302-add-new-acct.png)

*Figure 1: Add New Account screen*

**Step 2**. **Select** *Google Talk* from the *Network* drop-down list. 

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-303-new-goog-acct.png)

*Figure 2: Entering Google Talk account details into the Add New Account screen* 

**Step 3**. **Type** the *username* for your **Google Talk** account. 

**Step 4**. **Type** the *password* (or *passphrase*) for your **Google Talk** account. 

**Step 5**. *(Optional)* **Uncheck** the *Remember Password* box.

**Important:** If you want **Jitsi** to remember your **Google Talk** account *password* for you, you should *first* [enable its *Master Password* feature](#2488).

**Step 6**. **Click** **[Add]** 

You can now use Jitsi to communicate through the Google Talk account you have added.

**Note:** If you are using [2-step verification](https://support.google.com/accounts/answer/180744?hl=en) to protect access to your Gmail account, you may see an error like the one shown in *Figure 3* when Jitsi tries to access your account. (It will also display the same error if you get your passphrase wrong.) 

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-304-goog-auth-fail.png)

*Figure 3: Google Talk authentication failed (possibly as a result of "2-step verification" settings)*

To access **Google Talk** using Jitsi, you will need to generate an "**application-specific password**". To learn how, see [Google's instructions](https://support.google.com/accounts/answer/185833?hl=en). When you have generated an *app password* for **Jitsi** within your **Google** account, you will enter that password within **Jitsi** as the main password for your **Google Talk** account.

### 3.1.2 How to add a Facebook account to Jitsi

There are two settings that you may need to change on the **Facebook** website first before **Jitsi** can use **Facebook** for chat: 
- Create a *username* for your **Facebook** account.
- Turn on **Facebook’s** *”application platform”*.

**Step 1**. Assign a *username* to your **Facebook** account on the **Facebook** website.

Before **Jitsi** can connect to **Facebook** to use its chat functionality, you must assign a *username* to your Facebook account. Unlike most Web services, **Facebook** does not require you to select a *username* when you create your account, but it does allow you to create one if you wish. You can confirm your *username* by signing into your **Facebook** account. 

Your *username* is what appears in the address bar of your browser after *https://www.facebook.com/* when you view your *Timeline* or *Page*. So, if your username is *elena.katerina*, you should see *https://www.facebook.com/elena.katerina* in your browser's address bar when viewing your *Timeline*. Your *username* is also part of your **Facebook** email address (*elena.katerina@facebook.com*, for example). 

If you do not have a **Facebook** *username*, you can choose one by signing into your **Facebook** account and selecting **Settings > General** or by **navigating** to *https://www.facebook.com/username*. 

**Facebook** may need you verify your account before allowing you to select a *username*. This could require giving **Facebook** a mobile phone number at which you can receive a text message. For more details see **Facebook’s** [explanation of usernames](https://www.facebook.com/help/329992603752372/).

**Step 2**. Turn on **Facebook’s** *”application platform”* in order to give **Jitsi** access to your **Facebook** account. To do this, **sign in** to **Facebook**, **select** **Settings > Apps**, then **confirm** that the *Apps, Websites and Plugins* setting is **Enabled**.
 
**Note:** Turning on **Facebook’s** *application platform* opens up some of your **Facebook** data to third-party application developers. This data is available not only to the **Facebook** applications that you choose to use, but also to the **Facebook** applications used by your friends. After turning on **Facebook’s** *Apps, Websites and Plugins*, be sure to check the settings under *”Apps others use”*. This setting allows you to hide some personal information from applications used by your friends. Unfortunately, **Facebook** does not offer settings to hide *all* personal information. As long as the *application platform* is *Enabled*, certain categories of data (including your friend list, your gender, and any information you have made public) are accessible to apps used by others. *If this is unacceptable, you should disable Apps, Websites and Plugins and avoid using Jitsi with Facebook Messenger.*

Once have chosen a **Facebook** *username* and enabled the *application platform*, you can add your **Facebook** account to **Jitsi**. 

As shown in *Figure 1* of [the *Add accounts to Jitsi* section](#2478), the first time you launch **Jitsi**, you will see an account configuration screen that allows you to add various chat services to the application. After you have added at least one account, this screen will no longer appear. In order to add *additional* accounts, follow the steps below to add your **Facebook** account to **Jitsi**. 

**Step 3**. **Click** *File* in Jitsi's menu bar and **select** *Add new account...* to choose the service or protocol you want to use.

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-302-add-new-acct.png)

*Figure 1: Add New Account screen*

**Step 4**. **Select** *Facebook* from the *Network* list to enter your username and passphrase

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-305-new-fb-acct.png) 

*Figure 2: Entering a username and password into the Add New Account screen* 

**Step 5**. **Type** your Facebook username 

**Step 6**. **Type** your Facebook passphrase. 

**Step 7**. (Optional) **Uncheck** the *Remember password* box

**Important:** If you want **Jitsi** to remember your account passwords (or passphrases) for you, you should [enable its *Master Password* feature](#2278).

**Step 8**. **Click** **[Add]** 

You can now use **Jitsi** to communicate using your **Facebook** account.

### 3.1.3 How to add a Jabber/XMPP account to Jitsi

**XMPP** and **Jabber** are different names for the same instant messaging (IM) protocol. It is an open standard, and there are [many providers](https://xmpp.net/directory.php) who offer free **Jabber/XMPP** accounts that you can use with **Jitsi**. The IM Observatory allows you to [evaluate some security properties of public Jabber/XMPP services](https://xmpp.net/index.php).

If you have experience running online services, you can also install a [Jabber/XMPP server](http://xmpp.org/xmpp-software/servers/) (such as [ejabberd](http://www.process-one.net/en/ejabberd/) or [Prosody IM](http://prosody.im/)) on your own server and provide accounts to members of a particular community or organization.

Below, we recommend a few services that have a great deal of experience protecting their users' privacy. (But remember, you are relying primarily on **OTR** encryption to keep your chats confidential, so you still need to make sure that you and those with whom you communicate know how to use it properly. This is covered in the section on [Using Jitsi for secure instant messaging](#2491).

#### Creating and adding a jabber.ccc.de account

You can create an account on the *jabber.ccc.de* service (located in Germany) and add it to **Jitsi**, all at the same time, from within the application. This also works for many other traditional **Jabber/XMPP** services.

**Step 1**. **Click** *File* in **Jitsi's** menu bar and **select** *Add new account...* to choose the service or protocol you want to use.

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-302-add-new-acct.png)

*Figure 1: Add New Account screen*

**Step 2**. **Select** *XMPP* from the *Network* list to create your account

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-306-add-new-xmpp-acct.png)

*Figure 2: Adding an XMPP account*

The steps below assume that you do *not* yet have a *jabber.ccc.de* account and need to create one. (If you do, just enter your *username* and *password* and click **[Add]**.)

**Step 3**. **Select** *Create a new XMPP account*.

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-307-create-new-xmpp-acct.png)

*Figure 3: Creating a new XMPP jabber.ccc.de account within Jitsi using the Add New Account screen*

**Step 4**. **Type** *jabber.ccc.de* in the *Server* box.

**Step 5**. **Choose** a username and **type** it into the *XMPP username* box.

**Step 6**. **Choose** a *password* (or *passphrase*) and type it into the *Password* and *Confirm Password* boxes.

**Step 7**. **Click** **[Add]** to request the *username* you have chosen. 

If the *username* you requested is unavailable, the registration process will fail, and **Jitsi** will announce that it *”failed to create your account due to the following error: Could not confirm data.”* You can try again by repeating the process with a different *username*.

**Note**: If you do not log in to your *jabber.ccc.de* account for 12 months, your account will be removed, and your *username* will be made available for registration by others.

#### Creating a Riseup.net (Jabber/XMPP) account

[**Riseup**](https://help.riseup.net/en/about-us) is a collective dedicated to providing secure services for individuals and organizations committed to political and social justice. Their servers are located in the United States.

If you already have a [Riseup.net email account](../riseup/internet), you can use the same account for their [Jabber/XMPP service](https://www.riseup.net/en/chat). I

If you do not have a *Riseup.net* email account, you will need two *invitation codes* from two different *Riseup.net* users in order to create an account. You can then visit [https://user.riseup.net](https://user.riseup.net) to create an account using those *invitation codes*. Once your account is active, you can add it to **Jitsi** by following the steps below.


#### Adding an existing Jabber/XMPP account to Jitsi 

As shown in *Figure 1* of [the *Add accounts to Jitsi* section](#2478), the first time you launch **Jitsi**, you will see an account configuration screen that allows you to add various chat services to the application. After you have added at least one account, this screen will no longer appear. In order to add *additional* accounts, follow the steps below. 

**Step 1**. **Click** *File* in **Jitsi's** menu and **scroll down** to **select** *Add new account...* to choose the service or protocol you want to use.

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-302-add-new-acct.png)

*Figure 1: Add New Account screen*

**Step 2**. **Select** *XMPP* from the *Network* list to enter your *username* and *password* (or *passphrase*).

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-307-create-new-xmpp-acct.png)

*Figure 2: Choosing the entry screen for an existing XMPP/Jabber account in the Add New Account screen* 

**Step 3**. **Type** the *username* for your **Jabber/XMPP** account on this service.

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-308-add-existing-xmpp-acct.png)

*Figure 3: Entering the username and password for an existing  XMPP/Jabber account into the Add New Account screen* 

Your *username* should include the **@** symbol and the *hostname* of the service. For example:

- A *Riseup.net username* might look like:  **ekaterina@riseup.net**
- A *jabber.ccc.de username* might look like: **elena.katerina@jabber.ccc.de**

**Step 4**. **Type** the *password* (or *passphrase*) for your **Jabber/XMPP** account.

**Step 5**. (Optional) **Uncheck** the *Remember password* box.

**Important:** If you want **Jitsi** to remember your *passwords* and/or *passphrases* for you, you should *first* [enable its *Master Password* feature](#2278).

**Step 6**. **Click** **[Add]** 

You can now use **Jitsi** to communicate through this **Jabber/XMPP** account.

### 3.1.4 How to add a SIP account to Jitsi

In this section, we recommend only a single **Session Initiation Protocol (SIP)** provider, **ostel.co** (which is hosted in United States by [The Guardian Project](https://guardianproject.info/)). There are many free **SIP** services online, but **ostel.co** appears to offer the most reliable support for end-to-end encryption using the **ZRTP** protocol. They also *do not* log data related to **ostel.co** users and calls.

**Note**. **Jitsi** is less stable when used for encrypted voice chat than it is when used for encrypted text chat. You may find that the **Android** mobile application **CSipSimple** is a more reliable way to use your *ostel.co* account for encrypted **VoIP**.

#### Creating a free SIP account on ostel.co

Unlike some **Jabber/XMPP** accounts, **SIP** accounts cannot be created from within **Jitsi** itself. To create an **ostel.co** account, follow the steps below

**Step 1.** Visit the **ostel.co** [registration page](https://ostel.co/).

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-309-ostel-home-page.png)

*Figure 1: The ostel.co home page*

**Step 2**. **Click** **[Sign me up]** to access the *ostel.co* sign-up form.

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-310-ostel-email-entry.png)

*Figure 2: The ostel.co email sign-up form*

**Step 3**. **Enter** your email address (this can be any email address).

**Step 4**. **Click [Sign up]** to access the *username* and passphrase selection form

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-311-ostel-registration.png)

*Figure 3: The ostel.co username and password selection form*

**Step 5**. **Select** or **Type** a "code name"

**Step 6**. **Choose** and enter a *password* (or *passphrase*) twice.

**Step 7**. **Click [Create my account]** to complete the process of creating an **ostel.co SIP** account

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-312-ostel-registration-complete.png)

*Figure 4: The ostel.co registration page after successfully creating a new ostel.co account*

Once you have successfully created a new **ostel.co SIP** account, you can add it to **Jitsi** by following the steps below.

#### Adding an existing SIP account to Jitsi

As shown in *Figure 1* of [the *Add accounts to Jitsi* section](#2478), the first time you launch **Jitsi**, you will see an account configuration screen that allows you to add various chat services to the application. After you have added at least one account, this screen will no longer appear. In order to add *additional* accounts, follow the steps below. 

**Step 1**. **Click** *File* in **Jitsi's** menu and **scroll down** to **select** *Add new account...* to choose the service or protocol you want to use.

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-302-add-new-acct.png)

*Figure 1: Add New Account screen*

**Step 2**. **Select** *SIP* from the *Network* list to enter your *username* and *password* (or *passphrase*).

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-313-add-new-sip-acct.png)

*Figure 2: Choosing the entry screen for an existing XMPP/Jabber account in the Add New Account screen* 

**Step 3**. **Type** your *ostel.co username* 

**Step 4**. **Type** your *ostel.co password* (or *passphrase*). 

**Step 5**. (Optional) **Uncheck** the *Remember password* box.

**Important:** If you want Jitsi to remember your passphrases for you, you should *first* [enable its *Master Password* feature](#2488).

**Step 6**. **Click [Add]**.

You can now use **Jitsi** for **Voice-over-IP (VoIP)** calls through the **ostel.co SIP** service. If you *and those with whom you are communicating* both have **ostel.co SIP** accounts and configure them properly, your conversations can have end-to-end encryption using the **ZRTP** protocol. To learn more about how to do this, see the section on [Using Jitsi for secure voice and video calls](#2492).

## 3.2 How to change an account password in Jitsi

Many of the services that you can use in **Jitsi** allow you to change your *password* directly from their web interface, as part of your account settings. However, some **Jabber/XMPP** and **SIP** accounts don't have a web interface through which you can manage and change your *passwords*. For these accounts, you can change your *passwords* by following these steps:

**Step 1**. **Click** *Jitsi* in the main menu at the top of the screen and **scroll down** to **select** *Preferences*.

**Step 2:** **Select** the account you want to change the *password* for, then **click [Edit]** at the bottom..
 
![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-314-edit-acct-pw.png)

*Figure 1: The Preferences window in Jitsi*

**Step 3:** In the next window, **click** the [**Change account password**] button towards the bottom of the page.
 
![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-315-change-acct-pw.png)

*Figure 2: The Account Registration Wizard window*

**Step 4:** In the next window, *Change account password*, enter your new password, re-enter it again, and then click [**OK**].

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-316-change-acct-pw-2.png)

*Figure 3: The Change Account Password screen*

You have now successfully changed your account's *password* from within **Jitsi**!

## 3.3 How to set a master password for Jitsi

It may not be best to let **Jitsi** remember the *passwords* (or *passphrases*) to the accounts you add to **Jitsi**. If you have **Jitsi** remember the *passwords* to each account you add to **Jitsi**, *and* you choose to set a *master password* for ease of use, be aware that it may be possible to view all of your *passwords* *if* they can access **Jitsi** with your *master password*. Similarly, if an unauthorized user accesses your unlocked and unencrypted device after you’ve logged into **Jitsi** with your *master password*, they can use your accounts in **Jitsi** to communicate with others as if they were you.

It is therefore strongly recommended that if you *do* choose to set a *master password* that you protect all your *account passwords* in **Jitsi** with a strong *master password*. Once you set a *master password*, **Jitsi** will ask you for it upon starting the program.

You can set a *master password* for **Jitsi** through the following steps:

**Step 1**. **Click** *Jitsi* in the main menu at the top of the screen and **scroll down** to **select** *Preferences*.

**Step 2:** Select the **Security tab** at the top of the window. Then **click on** the **Passwords sub-tab** and **check** the box next to “**Use a master password**”.

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-317-options-security-passwords.png) 

*Figure 1: The passwords section of Jitsi’s Security Preferences*

**Step 3:** Type in your *master password* in the new window that pops up, as shown below. For more on creating a strong *password* or *passphrase*, see [“Create and maintain secure passwords”](../passwords).

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-318-master-pw.png)

*Figure 2: Setting a master password in Jitsi*

**Step 4:** **Click** on [**OK**] to confirm the *master password*. If it is successfully set, you will see a new window that reads “**Master Password successfully changed**”. Click on [**OK**] to close that window.

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-319-master-pw-changed.png)

*Figure 3: Successfully setting a master password in Jitsi*

**Note:** The [**Change Master Password**] button lets you set and change the *master password* for **Jitsi**. The [**Saved Passwords…] button on the same screen lets you access the passwords you’ve asked **Jitsi** to remember (and to remove them from **Jitsi’s** memory if you choose).

# 4. Strengthen Jitsi's Security Settings





## 4.1 How to clear and disable your chat history in Jitsi

By default, **Jitsi** stores information about the incoming and outgoing voice/video calls and the instant messages that you send and receive. You can access voice/video calls by clicking on the clock icon on the main Jitsi window:

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-401-main-window-top.png)

*Figure 1: The top of the main window in Jitsi*

And you can view the the history of your instant messages by clicking on the triangle to the right of the *hourglass icon* in an active chat window (the window shown while actively chatting with a contact): 

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-402-chat-window-history-top.png) 

*Figure 2: Viewing the history menu at the top of an active chat window with a contact*

If you allow **Jitsi** to log and store the history of your calls and chats, be aware that data is stored in plain text on the disk of your computer. **And even if you encrypt the text of your chats with OTR when they are in transit, all the text messages you send and receive are stored on your computer in an unencrypted state. The metadata about your calls and text chats are also logged and stored on your computer.** The same information is collected and stored on the disk of the contacts you are communicating with.

To prevent **Jitsi** from collecting this information—and to remove data that has already been gathered—you and your contacts can take the steps described below to change the default *”History”* setting on your devices: 

### 4.1.1 How to disable the logging of chat history in Jitsi

**Step 1**. There are two ways to disable the logging of chat history in **Jitsi**.

***Option 1:*** Within a chat window with a contact, **click** on the triangle to the right of the *hourglass icon* to reveal the history menu. **Scroll down** to **select** *Turn off history  for all chats and contacts*.

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-406-turn-off-all-chat-history.png) 

*Figure 1: Erasing all chat history in Jitsi via the history menu within a chat window*

***Option 2:*** **Click** *Jitsi* in the main menu at the top of the screen and **scroll down** to **select** *Preferences*.

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-403-chat-history-settings.png) 

*Figure 2: Message settings within Jitsi’s General Preference section, including the ‘Log chat history’ setting*

**Select** the *General* tab at the top of the window. Then **uncheck** the *Log chat history* option as seen in *Figure 2* above.

**Step 2**. within **Jitsi’s** *Preferences* (**Jitsi > Preferences**), **select** the **Advanced** tab, then click on *Logging* in the left-hand window. Then **uncheck** the *Enable packet logging* option, as seen in *Figure 2* below:

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-404-disable-packet-logging.png)

*Figure 2: Logging settings within Jitsi’s Advanced Preference section*

### 4.1.2 How to remove any existing chat history logs in Jitsi

After disabling logging in [Section 4.1.1](#2495) above, it’s a good idea to also ensure that any old **Jitsi** logs are also removed. To do this, follow the steps below:

**Step 1**. Within an chat window with a contact, click on the triangle to the right of the *hourglass icon* to reveal the history menu. 

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-405-erase-all-chat-history.png) 

*Figure 1: Erasing all chat history in Jitsi via the history menu within a chat window*

**Step 2**. **Scroll down** to select *Erase all chat history in Jitsi*.

# 5. Add contacts and encrypt your instant messages in Jitsi

After adding and logging into one or more accounts, you are ready to add contacts and communicate with them in **Jitsi**.

## 5.1 Adding contacts in Jitsi

For accounts where you have already have contacts, they should also show up in **Jitsi** when you add your accounts there. But if you need to add new contacts in Jitsi, you can follow the steps below:

**Step 1**. **Click** *File* in **Jitsi's** menu and **scroll down** to **select** *Add contact…*. The following window should appear:

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-501-add-new-contact.png)

*Figure 1: The Add Contact screen*

**Step 2**. **Select** the account that you would like to add this contact to. (In our example, this account is ekaterina@riseup.net).
 
**Step 3**. ***(Optional)*** You can add the contact to the preset *Buddies* group, or create a new, custom group that you name. To add your contact to a new, custom group, you first need to create the group. You can do this by selecting *File > Create group...* in **Jitsi’s** main menu.

**Step 4**. **Enter** the *username* or *email address* of your new contact into the *ID or Number* field. (In our example, we’ve added *ono@riseup.net*).
 
**Step 5**. ***(Optional)*** You can also choose the *Display name* for your contact, which will be how your new contact appears in the main Jitsi window. 

**Step 6**. **Click [Add]**. You will now see your new contact in your contact list with the note *”Waiting for authorisation”* until they accept your *Add Contact* request.

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-502-waiting-for-contact-auth.png)

*Figure 2: A recently added contact awaiting authorisation*

**Step 7**. When your newly added contact logs into their account, a pop-up window will inform them that you have requested to add them to your list of contacts:

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-503-auth-requested.png)

*Figure 3: A Contact Request Authorisation as received by a recently added contact*

Your contact can choose one of the following options:

* **Ignore:** Your request will continue awaiting authorisation by the contact you added. 
* **Deny:** You will be notified that your request was rejected.
* **Authorise:** You will be notified that your contact has accepted your authorisation request, and the entry for your contact in your contact list will become active.

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-504-chat-started.png)

*Figure 4: Starting a text chat with a newly added and authorised contact*

Once you have added and authorised your contact, you can click on their name in your contact list and initiate instant messaging, voice or video calls, and desktop sharing by choosing the relevant icon under their name. In *Figure 4* above, *ekaterina@riseup.net* has started a text chat with her recently added and authorised contact *ono@riseup.net*.

## 5.2 Using Jitsi for secure instant messaging

[**Off-the-Record (OTR)**](https://otr.cypherpunks.ca/) is a cryptographic protocol that provides *end-to-end encryption* for instant messaging. When used correctly, *end-to-end encryption* prevents anyone other than the intended recipient from reading your messages. **OTR** allows you to *authenticate* those you communicate with, which is essential for encryption to work properly. **OTR** also provides *forward secrecy*. This means that even if the encryption key of one **OTR** user is compromised, your past conversations cannot be decrypted.

Most messaging clients and services *do not* support **OTR**. **Jitsi** *does* support **OTR** for all the *instant messaging* accounts you can register within **Jitsi**, which is one of the reasons we recommend using **Jitsi** for secure messaing. 

You can enable *end-to-end encryption* of your instant messages in **Jitsi** by following these steps:

**Note:** **Google** also has a service called *off the record* that is *different* from the *end-to-end encryption* provided by **OTR**. **Google’s** *off the record* only keeps particular **Google Talk** conversation logs from being accessed within your **Google Talk** accounts. (There is also no evidence that **Google** isn’t still logging and storing the **Google Talk** conversations you have using their *off the record* option.)

**Step 1**. **Click** *Jitsi* in the main menu at the top of the screen and **scroll down** to **select** *Preferences*.

**Step 2:** Select the **Security tab** at the top of the window. Then **click on** the *Chat* sub-tab. You will then see a window similar to the one included below:

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-505-options-chat.png) 

*Figure 1: The chat section of Jitsi’s Security Preferences, showing no OTR key present for the ekaterina@riseup.net Jabber/XMPP account*

**Step 3:** To create an **OTR** encryption key, **click** on the [**Generate**] button. You will then see the fingerprint of the new **OTR** key that has been generated:

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-506-options-chat.png)

*Figure 2: The chat section of Jitsi’s Security Preferences, showing a new OTR key fingerprint for the ekaterina@riseup.net Jabber/XMPP account*

An encryption key is only generated for each account you choose to generate one for by following **Step 3** above. You only need to do this again if you add a new account or install **Jitsi** on another device and do not move your existing keys to it. 

**Step 4**. In order to communicate using the *end-to-end encryption* of **OTR**, those you communicate with also need to have generated an **OTR** key for the account they want to use to communicate with. They also need to be using a client like **Jitsi** that allows them to use **OTR**.

Therefore, in order to use **OTR**, **identify** a contact who also has an **OTR** key and is using a client that supports **OTR**. 

**Step 5**. Then **select** that contact in the main **Jitsi** window and click on the **send message** icon (first from the left under the contact's name) to open a text chat window:

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-507-otr-convo-0.png)

*Figure 3: Initiating a chat conversation in Jitsi, still pending encryption using OTR*

**Step 6**. The *padlock icon* in the top right-hand side of the window informs you whether the chat is encrypted or not. It also notifies you whether or not you’ve *authenticated* your contact’s identity or not. 

- If the lock is *closed*, the chat is encrypted.
- If the lock is *open*, the chat isn’t encrypted.
- If there is a *yellow triangle with an exclamation point* in the corner of the *locked padlock*, the chat is encrypted, but you still need to *authenticate* your contact’s identity (as seen in *Figure 4* below). You do this by authenitcating each others’ **OTR** fingerprints or by successfully answering a *shared secret* that one of you sends to the other.

To encrypt your conversation, **click** on the *padlock icon*. **Note** the changes in the window and to the *padlock icon*:

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-508-otr-convo-1.png)

*Figure 4: Initiating an OTR encrypted conversation, still pending authentication*

The *padlock icon* is now locked. This means that whatever messages you and your contact send to each other are encrypted. 

But also notice the *yellow triangle with an exclamation point* in the corner of the *locked padlock*. This means it is an encrypted conversation, but that you still need to authenticate your contact (in this example, *mansour@riseup.net*). As an additional reminder, there is also a prompt in the conversation window reminding you to *authenticate* your contact.

**Step 7**. **Click** on the *’You should authenticate…’* link in the chat window to open the *Authenticate Buddy* window. (In our example, this sentence reads *’You should authenticate mansour…’.*) The default authentication option will be *Question authentication*, as seen in *Figure 5* below:

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-510-question-auth-buddy.png)

*Figure 5: The Authenticate Buddy window, with the default ‘question authentication’ method shown*

**Step 8**. In the *Authenticate Buddy* window, you are asked how you would like to authenticate your contact. There are three authentication options available in **Jitsit**:
- **Fingerprint authentication:**Exchanging and verifying the unique cryptographic [fingerprints](https://otr.cypherpunks.ca/help/fingerprint.php)for each contact’s **OTR** key.
- **Question authentication:** By asking one another questions to which only the other person would know the answer 
- **Shared secret authentication:** By pre-arranging a shared word or phrase that both contacts need to enter exactly the same way—this is also known as *shared secret*. 

**Note:** While all three of these authentication options are available in **Jitsi**, keep in mind that they are not available in all **OTR**-enable clients, so your contact may not have all three types of authentication options available to them. (For example, **Adium** for **Mac OS X** does not have all three authentication options available.)

**Step 9**. In our example, we’ll choose the **fingerprint authentication** option (which we also recommend). 

To *authenticate* using fingerprints, **select** the **fingerprint authentication** option from the *’How would you like to authenticate?’* pull-down menu: 

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-509-fingerprint-auth-buddy.png)

*Figure 6:The Authenticate Buddy window, with the ‘fingerprint authentication’ method shown*

**Step 10**. At this point, you can see each other’s *’purported’* fingerprint within the *Authenticate Buddy* screen. But to ensure that no one is *pretending* to be your contact, you now need to **exchange your fingerprints with each other using a *different* communications channel than Jitsi**. It should be via a means of communication that you consider trusted and reliable for communicating with that person. It may be via email, phone, SMS, or another method. 

**Tip:** It is useful to include *your* **OTR** fingerprint in your email signature, on your website, and/or on your physical business cards. This provides a *second channel* exchange of your **OTR** fingerprint for when someone needs to authenticate your identity.

**Step 11**. **Compare** the fingerprint your contact has sent you using another communications channel other than **Jitsi** with what you see as their **OTR** fingerprint within the *Authenticate Buddy* screen. 

**Step 12**. If the two fingerprints match (the one your contact sent you outside of **Jitsi**, plus what you can see as their **OTR** fingerprint within the *Authenticate Buddy* screen in **Jitsi**) you can *authenticate* your contact! 

**Paste** the fingerprint you received through another channel into the text field towards the bottom of the window that reads *‘Please enter the fingerprint you received…’*. That text field should turn *green*, and it will also change *’I have not’* to *I have* in the verification sentence above the field. 

Then **click**  the **[Authenticate Buddy]** button at the bottom of the screen. 

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-511-fingerprint-auth-successful.png)

*Figure 7: A successful ‘fingerprint authentication’ in the Authenticate Buddy window*

*(If the two fingerprints *don’t* match, there may be an error. Work to authenticate your contact’s identity using another method, or ask them to double-check their **OTR** fingerprints — it may be that they are using a different **OTR** fingerprint and key on a different device, but forgot to send you the correct **OTR** fingerprint for the device they’re using.)*

**Step 13**. Back in the chat window, the *locked padlock icon* will now have a *green triangle with a check mark* to signify that you have successfully authenticated your contact, and the conversation is encrypted.

![](/sites/securityinabox.org/files/media/jitsi-osx-en-v01-512-encrypted-authed-convo.png)

*Figure 8: A chat conversation with end-to-end encryption using OTR in Jitsi with an authenticated contact*

You can now exchange encrypted instant messages with your contact!

**Note:** The authentication process should be done only once for each contact’s **OTR** fingerprint. If the *triangle with the exclamation mark* returns to the *padlock icon*, it means that you are chatting with someone who you have not yet authenticated. This can happen when your contact moves to another device with another **OTR** encryption key (another installation of **Jitsi**, or another **OTR**-enabled program, etc.). In this case you will need to re-authenticate each other to be sure of the identity of the person with whom you are communicating.
