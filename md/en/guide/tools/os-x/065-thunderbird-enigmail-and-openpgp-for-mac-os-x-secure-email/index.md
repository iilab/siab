

---

lang: en
community: guide
type: tools
os: os-x
weight: 065
title: Thunderbird, Enigmail and OpenPGP for Mac OS X - secure email

---

**Mozilla Thunderbird** is free and open source software that allows you to exchange and store email for multiple accounts with multiple service providers. **Enigmail** and **GnuPG** improve the security and privacy of your email correspondence by adding support for end-to-end encryption to **Thunderbird**. They also allow you to sign your messages digitally and verify the digital signatures of others.

# Required reading


:[](../../../tactics/secure communication)


:[](../../../tactics/secure file storage)


:[](thunderbird-enigmail-and-openpgp-for-mac-os-x-secure-email)

# What you will get from this guide

- The ability to manage multiple email accounts using a single tool
- The ability to read and compose messages while disconnected from the Internet
- The ability to send and receive encrypted email
- The ability to digitally sign your emails and authenticate signed email from others

# 1. Introduction to Thunderbird

**Thunderbird** is a free and open source, cross-platform email client for sending, receiving and storing email. An *email client* is an application that lets you download and manage your messages — from multiple accounts with multiple providers — without a browser. 

**Gnu Privacy Guard (GPG)** is free and open source software capable of encrypting, decrypting and digitally signing messages and files. It also generates and manages the public and private key pairs that are used for encryption and decryption. 

**Enigmail** is a Thunderbird add-on that allows you to access the encryption and authentication features provided by GnuPG (which must be installed for Enigmail to work). 


## 1.0 Things you should know about Thunderbird before you start

You will need at least one email account to use **Thunderbird**. If you want to create a new account to use with **Thunderbird**, refer to the [**RiseUp** guide](../riseup/internet).

Like all *email clients*, **Thunderbird** makes a copy of your messages available on your computer. This includes the emails you send as well as those you receive. As a result, it is particularly important that you implement device encryption (such as [*FileVault*](https://support.apple.com/en-us/HT204837)) when you decide to use Thunderbird. 

**Thunderbird** cannot protect your device if you open malicious attachments or click on  malicious links. Do not open unsolicited attachments and exercise caution when clicking on links that were sent to you by email. Learn how to [**Protect your device from Malware and Hackers**](../malware) guide.

## 1.1 Other tools like the Thunderbird

**Thunderbird** is available for **Mac OS X**, **GNU/Linux** and **Microsoft Windows**. Securely managing multiple email accounts is a complex task, and we strongly recommend Thunderbird for this purpose. However, if you prefer to use an alternative we recommend the following free and open source tools:

- [**Claws Mail**](http://www.claws-mail.org/) is available for GNU Linux and Microsoft Windows;
- [**Sylpheed**](http://sylpheed.sraoss.jp/en/) is available for for Mac OS X, GNU Linux and Microsoft Windows;
- [**Mailpile**](https://www.mailpile.is/) has a **beta** available for GNU/Linux and Microsoft Windows (and should be available for Mac OS X in the future)

The security advantages of Thunderbird are even more significant when compared to commercial alternatives like *Microsoft Outlook*.


# 2. Install and configure Thunderbird





## 2.1 Install Thunderbird

To install **Thunderbird**, follow the steps below:

**Step 1**. **Browse** to the **Thunderbird** download page at [**https://www.mozilla.org/en-US/thunderbird**](https://www.mozilla.org/en-US/thunderbird/)

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-001.png)

*Figure 1: The Thunderbird download page*

**Step 2**. **Click** **[Free Download]** to choose a location for the **Thunderbird** disk image

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-002.png)

*Figure 2: Choosing a location for the disk image*

**Step 3**. Make sure *DiskImageMounter* is selected next to *Open with* and **click** **[OK]** to download the disk image

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-003.png)

*Figure 3: Downloading the Thunderbird disk image*

After your browser has downloaded the *disk image*, *Finder* will mount it so you can install **Thunderbird** into your *Applications* folder

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-004.png)

*Figure 4: Inside the Thunderbird installer disk image*

**Step 4**. Within the folder shown in *Figure 4*, drag the **Thunderbird** application into the *Applications* folder as shown below

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-005.png)

*Figure 5: Dragging Thunderbird into the Applications folder*

**Step 5**. **Dismount** the **Thunderbird** installer *disk image* by pressing **Command-E** while the *disk image* window is active


## 2.2 Add an email account to Thunderbird

To add an email account to **Thunderbird**, follow the steps below.

**Step 1**. **Launch** **Thunderbird**

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-011.png)

*Figure 1: First launch of Thunderbird*

**Step 2**. (Optional) **Uncheck** the *Always perform this check when starting Thunderbird* box

**Step 3**. **Choose** whether or not you want to make **Thunderbird** your default Email client

- To set **Thunderbird** as your default email client, make sure the box next to *E-mail* is checked and **click** **[Set as Default]**
- To keep your current default email client, **click** **[Skip Integration]**

**Note**: If you use *Apple Mail* (the email client that comes with Mac OS X), you might want to *Skip Integration* for now

Thunderbird will display the *would you like a new email address?* screen

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-012.png)

*Figure 2: Thunderbird offering to help create a new email address*

**Step 4**. **Click** **[Skip this and use my existing email]** to open the *Mail Account Setup* screen

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-013.png)

*Figure 3: The Mail Account Setup screen*

**Step 5**. **Type** the name, email address and password that correspond to the account you wish to access using **Thunderbird**

**Step 6**. **Uncheck** the box next to *Remember my password*

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-014.png)

*Figure 4: Adding account information to the Mail Account Setup screen*

**Step 7**. **Click** **[Continue]**. **Thunderbird** will check the configuration of the email service you have entered.

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-015.png)

*Figure 5: Thunderbird after verifying the configuration of an email service*

You probably want to leave **"IMAP (remote folders)"** selected. *IMAP* stores the master copy of your email folders (including the *Inbox*, *Drafts*, *Templates*, *Sent* and *Trash* folders) on the server and makes a local copy on your device. This allows you to access the same messages from multiple devices while keeping your folders in sync. (**POP**, on the other hand, retrieves your messages from the server and stores them on the first device to which they are downloaded. *This does not mean they are actually deleted from the server*, but it does make it much more difficult to access your email from multiple devices.)

**Step 8**. **Click** **[Done]** to create your account and enter the main **Thunderbird** interface.

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-016.png)

*Figure 6: The main Thunderbird interface*

**Note**: To add another email account, **click** *File* in the menu bar and **select** *New > Existing Mail Account*. This will activate *Figure 3*, above. Then, simply repeat *Steps 5 through 8*.

Each time you launch **Thunderbird**, you will be prompted to enter your passphrase for each account you have added.

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-017.png)

*Figure 7: The Mail Server Password Required screen*

**Step 9**. **Type** your passphrase 

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-018.png)

*Figure 8: Entering a password into the Mail Server Password Required screen*

**Step 10**. **Click** **[OK]** to sign in to your account(s) using **Thunderbird**


# 3. Improve Thunderbird's security and usability

List of sections on this page:

- [**3.0 How to Improve Usability**](#3.0)
- [**3.1 How to Disable the HTML Feature**](#3.1)
- [**3.2 How to Configure the Privacy Options**](#3.2)
- [**3.3 How to Configure the Security Tabs**](#3.2)
- [**3.4 How to Enable the Account Settings Junk Mail Filter**](#3.3)


## 3.1 Improve Thunderbird's usability

To more easily find menu items, you can enable the **Mail Toolbar** by right-clicking at the top of the Thunderbird window and enabling it

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-597.png)


*Figure 1: The Mail Toolbar option* 


Most of us want to receive email sent to us as soon as possible. Let us check for new messages every minute, rather than every 10 minutes as is the **Thunderbird** default.

**Step 1**. **Select Tools > Account Settings** in **Thunderbird** to and select *Server Settings* under your email account.

**Step 2**. Change **Check for new messages every "10" minutes to "1" minute.

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-520.png)


*Figure 2: Server settings with "Check for new messages" set to 1 minute*


We recommended turning off the *Global Search and Indexer* feature in **Thunderbird* to improve performance. 

**Step 1**. In the top menu bar **Click Thunderbird > Preferences** 

**Step 2**. Click **Advanced** and untick *Enable Global Search and Indexer*

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-530.png)


*Figure 3: The advanced tab with "Enable Global Search and Indexer" unticked*



### 3.1.1 Enabling Thunderbird's Junk Mail features

**Thunderbird** has two built-in junk mail filters that can help you determine which of your incoming messages are spam. By default, these filters are disabled, so you must enable them for use. Even after they have been enabled, you will continue to receive junk mail, but **Thunderbird** will automatically sort them into the *Junk* folder. 

Email scams - also referred to as *phishing* emails - usually attempt to make you click on a link that is embedded in the email. Frequently, these links direct your browser to a web site that will attempt to infect your computer with a virus. In other cases, the link will take you to a web site that appears to be legitimate, to deceive you into entering a valid user name and password, which can then be used or sold by the entity or people for commercial or malicious purposes. **Thunderbird** can help to identify and warn you about emails like this.

The first set of junk mail and security controls are found under **Preferences > Security** tab 

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-540.png)

*Figure 1: The Junk Mail tab*


### The Email Scams tab ###

**Step 1**. **Check** the *Tell me if the message I'm reading is a suspected email scam* option to enable **Thunderbird** to analyse messages for email scams as follows: 

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-550.png)

*Figure 2: The Email Scams tab* 

### The Anti-Virus tab ###

**Step 1**. **Click** the *Anti-Virus* tab to activate the following screen: 

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-560.png)

*Figure 3: The Anti-Virus tab* 

This option lets your anti-virus software scan and isolate individual messages as they arrive. Without this setting enabled, it is possible that your *entire* *Inbox* folder could be 'quarantined' if you receive an infected message.

**Note**: This assumes that you have a functioning anti-virus program installed. Please refer to [**Avast**](/en/avast_main) for more information on how to install and configure anti-virus software.

### The Passwords tab ###

**Step 2**. **Click** the *Passwords* tab to activate the following screen: 

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-570.png)

*Figure 4: The Passwords tab*

**Important:** We strongly recommend to keep your passwords private and secure using a software designed precisely for this purpose; please refer to [**KeePassX**](../guide/keepassx/os-x) for more information. 

**Note**: The options in the *Password* tab will only work if you checked the *Remember password* option in the first *Mail Account Setup* screen when you registered your email accounts with **Thunderbird**. If you have two-factor authentication enabled on your email account, you should use this feature.

**Step 1**. Click **[Saved Passwords...]** to activate the following screen:

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-571.png)

*Figure 5: The Saved Passwords window*

The *Saved Passwords* window lets you remove or view all the corresponding passwords for each of your accounts. If you save passwords within **Thunderbird** you should set a *Master Password* to protect access to your email accounts and make all of your account passwords inaccessible to anyone else familiar with the **Thunderbird** password options.

**Step 3**. **Check** the *Use a master password* option as shown in *figure 7* to activate the following screen:

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-596.png)

*Figure 6: Change Master Password window*

**Step 5**. **Type** in a strong password that only you will remember, and then click **[OK]** to confirm it as your *Master Password*. 

### How to Enable the Account Settings Junk Mail Filter ###

The second type of **Thunderbird** junk mail filter is available through the *Account Settings - Junks Settings* window. By default, these filters are disabled, so they must be enabled if you wish to use them. Whenever junk emails arrive **Thunderbird** will automatically sort them into the *Junk* folders associated with different accounts. 

**Note**: The *Junk Settings* options must be configured separately for each account. As such, junk mail for a **Gmail** or a **RiseUp** account will be placed in its corresponding *Deleted* folder. Alternatively, you may designate a *Local Folder* to receive junk mail from all your accounts. 

**Step 1**. **Select Tools > Account Settings** to activate the *Account Settings* window.

**Step 2**. **Select** the *Junk Settings* option associated with a specific email account in the sidebar

**Step 3**. **Enable** the *Junk Settings* options so that your own *Account Settings - Junk Settings* screen looks like this screen: 

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-580.png)

*Figure 7: The Account Settings - Junk Settings window*

**Step 4**. Under **Destination and retention** tick *move new messages to:*

**Step 5**. Choose *"Junk" Folder* option on *Local Folders*

**Step 5**. Click **[OK]** to complete the configuration of the *Account Settings* window.

## 3.2 Improve Thunderbird's privacy and security





### 3.2.1 Disable HTML email

**Thunderbird** lets you use **HyperText Markup Language** (**HTML**) to compose and read messages. This lets you receive and send messages that include colours, fonts, images and other formatting features. However, **HTML** is the same language used for Web pages; viewing messages with **HTML** formatting may expose you to malicious content in emails.
 
To disable the **HTML** formatting feature, in the top menu bar click **View > Message body as > Plain text**

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-588.png)

*Figure 1: The View menu displaying the Message Body submenu with the Plain Text option selected*

You can also change the default options so that emails you write are in Plain Text and not HTML. 

**Step 1**. **Click** ![](/sbox/screen/thunderbird-en-1/24a.png) to display the *Thunderbird Menu* and **select Options> Account Settings** and *Composition & Addressing* under your email address: 

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-590.png)

*Figure 2: The Composition & Addressing screen with *Compose messages in HTML format unchecked*


### 3.2.2 Configure Thunderbird's privacy options

Make sure to disable the ability of cookies and remote content to track your email reading habits:

**Step 1**. Choose **Thunderbird > Preference** and then click the **Privacy** tab

**Step 2**. Untick all the options under **Privacy**

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-595.png)

*Figure 1: The Privacy tab*

# 4. Sending and receiving encrypted messages

**GNU Privacy Guard (GnuPG or GPG)** is free and open source *cryptographic* software developed by the GNU Project. It is compliant with the **OpenPGP** standard and was designed to inter-operate with *Pretty Good Privacy (PGP)*, a commercial equivalent developed by Phil Zimmermann and maintained by *Symantec*. On a *Mac*, the **GPG Suite** bundle provides an easy way to install **GnuPG**. **Enigmail** is a Thunderbird add-on that allows you to access GnuPG's encryption features from within Thunderbird.

**GnuPG**  relies on a form of *public-key cryptography* that requires each user to generate his or her own pair of *keys*. This *key pair* can be used to encrypt, decrypt and sign digital content such as email messages. It includes a *private key* and a *public key*: 

- Your **private key** is extremely sensitive. Anyone who managed to obtain a copy of this key would be able to read encrypted content that was meant only for you. They could also sign messages so they appeared to have *come from* you. Your *private key* is, itself, encrypted to a passphrase that you will choose when generating your *key pair*. You should choose a strong passphrase and take care not to let anyone gain access to your *private key*. You will use your *private key* to decrypt messages sent to you by those who have a copy of your *public key*.
 
- Your **public key** is meant to be shared with others and can not be used to determine the value of your *private key*. Once you have a correspondent’s public key, you can begin sending her encrypted messages. Only she will be able to decrypt and read these messages because only she has access to the *private key* that matches the *public key* you are using to encrypt them. Similarly, in order for someone to send *you* encrypted email, they must obtain a copy of your *public key*. It is important to verify that the *public key* you are using to encrypt email actually does belong to the person with whom you are trying to communicate. If you or your correspondent are tricked into encrypting email with the wrong public key, your conversation will not be secure.

**GnuPG** and **Enigmail** also let you attach **digital signatures** to your messages. If you *sign* a message using your *private key*, any recipient with a copy of your *public key* can verify that it was sent by you and that its content was not tampered with. Similarly, if you have a correspondent's *public key*, you can verify his digital signatures.

## 4.1 Install GPG Suite and Enigmail

This section walks you through the installation of **GPGSuite** and **Enigmail**.

### 4.1.1 Install GPG Suite

To install GPG Suite, follow the steps below: 

**Step 1**. **Browse** to the **GPG Suite** download page at [**https://gpgtools.org/gpgsuite.html**](https://gpgtools.org/gpgsuite.html)

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-401.png)

*Figure 1: The GPG Suite download page* 

**Step 2**. **Click** **[Download GPG Suite]** to download the installer *disk image*

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-402.png)

*Figure 2: Choosing what to do with the GPG Suite installer disk image when it is downloaded* 

**Step 3**. Make sure *DiskImageMounter (default)* is selected next to *Open with* and **click** **[OK]**

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-403.png)

*Figure 3: Downloading the GPG Suite installer disk image* 

After your browser has downloaded the *disk image*, *Finder* will mount it so you can install **GPG Suite**
 
![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-404.png)

*Figure 4: Inside the GPG Suite installer disk image* 

**Step 4**. **Double-click** the **Install** icon on the left to begin the process of installing **GPG Suite**. 

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-405.png)

*Figure 5: The GPG Suite installer* 

**Step 5**. **Click** **[Continue]** to choose a location for the installation

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-406.png)

*Figure 5: Accepting the default install location for GPG Suite* 

**Step 6**. **Click** **[Install]** to install to enter your login passphrase 

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-407.png)

*Figure 6: The GPG Suite installer asking for your login passphrase*

**Step 7**. **Type** the passphrase you use to log in to your computer

**Step 8**. **Click** **[Install Software]** to install **GPG Suite**

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-408.png)

*Figure 7: The installation of GPG Suite*

When the installer is done, it will launch the **GPG Keychain** application so that you can generate your *GnuPG* *public* and *private* *key pair*. 

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-409.png)

*Figure 8: The GPG Suite key generation screen*

We will return to key generation in *Section 4.2*. For now, you can quit *GPG Keychain* by following the steps below.

**Step 9**. **Click** **[Cancel]** to close the key generation screen

**Step 10**. To quit *GPG Keychain*, **press** **Command-Q**.

Next,  you should quit the installer and *dismount* the installation *disk image* by following the steps below: 

**Step 11**. **Switch** back to the *Install GPG Suite* installer application

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-410.png)

*Figure 9: The GPG Suite installer when it is done*

**Step 12**. **Click** **[Close]** to quit the installer

**Step 13**. **Switch** back to *Finder* 

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-411.png)

*Figure 10: Inside the GPG Suite installation volume*

**Step 14**. **Dismount** the **GPG Suite** installer *disk image* by pressing **Command-E** while the *disk image* window is active


### 4.1.2 Install Enigmail

To install **Enigmail**, follow the steps below.

**Step 1**. **Launch** **Thunderbird** and sign in to your account

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-413.png)

*Figure 1: Thunderbird*

**Step 2**. **Click** ![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-414.png) 

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-415.png)

*Figure 2: Opening the Add-ons Manager*

**Step 3**. **Select** *Add-ons* to open the *Add-ons Manager*

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-416.png)

*Figure 3: The Thunderbird Add-ons Manager*

**Step 4**. **Type** "Enigmail" into the search field in the upper, right-hand corner of the *Add-ons Manager* and **press** *Enter*

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-417.png)

*Figure 4: Finding the Enigmail add-on*

**Step 5**. **Click** **[Install]** next to the entry for **Enigmail** to begin installing the add-on.

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-418.png)

*Figure 5: Installing the Enigmail add-on*

When **Thunderbird** is done installing the add-on, it will let you know

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-419.png)

*Figure 6: The Enigmail add-on installed*

**Step 6**. **Click** *Restart now* to restart **Thunderbird** and complete the installation of **Enigmail**

When **Thunderbird** restarts, it will automatically launch the **Enigmail** *Setup wizard*

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-420.png)

*Figure 7: The Enigmail Setup wizard*

If you are ready to generate your **GnuPG** *key pair* and configure **Enigmail** now, simply **click** **[Continue]** and move on to *Step 2* of [*Section 4.2 - Generate Key pairs and Configure Enigmail*](#2454). Otherwise, you can **click** **[Cancel]** and return to [*Section 4.2*](#2454) later.


## 4.2 Generate a key pair and configure Enigmail

This section covers the generation of a **GnuPG** *key pair* and the configuration of **Enigmail**.

### 4.2.1 Generate encryption keys

To generate a **GnuPG** *key pair*, follow the instructions below.

**Step 1**. **Click** ![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-414.png) and **select** **Enigmail > Setup Wizard** 

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-433.png)![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-434.png)

*Figure 1: Launching the Enigmail Setup Wizard*

**Step 2**. This will open the **GnuPG** *Setup Wizard* 

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-421.png)

*Figure 2: The Enigmail Setup Wizard*

**Step 3**. Make sure the *I prefer a standard configuration (recommended for beginners)* option is selected and **click** **[Continue]** 

You may see a warning about your **GnuPG** version, as shown below

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-422.png)

*Figure 3: GnuPG version warning*

If you do, **click** **[OK]**. Otherwise, simply continue on to the *Create Key* screen shown in *Figure 4*, below. 

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-423.png)

*Figure 4: Choosing a passphrase for your new GnuPG key pair*

**Step 4**. **Choose** a strong passphrase and **type** it into the two fields shown on this screen.

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-424.png)

*Figure 5: Choosing a passphrase for your GnuPG key pair*

**Note:** This passphrase will be used to encrypt your private key, which is what allows you to sign emails you send and decrypt emails you receive. It should not be shared with anyone. As such, it is important that you choose a strong passphrase and that you do not forget it. To learn more about generating strong passphrases and backing them up securely, see the [**Create and maintain secure passwords**](../passwords) guide.

**Step 5**. **Click** **[Continue]** to generate your GnuPG key pair

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-425.png)

*Figure 6: Enigmail generating a new GnuPG key pair*

When Enigmail has finished generating your GnuPG *key pair*, it will let you know, and a *Generate Revocation Certificate* button will appear. 

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-426.png)

*Figure 7: Enigmail ready to generate a revocation certificate*

A *revocation certificate* is a file that you can upload to a public *keyserver* – or send to those with whom you communicate using GnuPG – should you  need to revoke this *key pair*. You might need to do this if, for example: 

- Your *private key* is compromised
- You lose your *private key*
- You forget the passphrase for your *private key* 

**Step 6**. **Click** **[Create Revocation Certificate]** to enter your login passphrase

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-427.png)

*Figure 8: Enigmail asking for your login passphrase*

**Step 7**. **Type** the passphrase you chose when creating your **GnuPG** *key pair*

**Step 8**. **Click** **[OK]** to choose a name and location for your *revocation certificate*

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-428.png)

*Figure 9: Choosing a name and location for your revocation certificate*

In this example, we will put the *revocation certificate* in the *Documents* folder, but you can store it anywhere safe.

**Step 9**. **Click** **[Save]** to display *Enigmail's* warning about the importance of keeping your *revocation certificate* safe.

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-429.png)

*Figure 10: Revocation certificate warning*

**Step 10**. **Click** **[OK]** to return to the *Setup Wizard*

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-430.png)

*Figure 11: The Enigmail Setup Wizard*

**Step 11**. **Click** **[Continue]** to complete the key generation process

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-431.png)

*Figure 12: The Enigmnail Thank you screen*

**Step 12**. **Click** **[Done]** to exit the *Setup Wizard* and return to **Thunderbird**


### 4.2.2 Configure Enigmail to work with your email account

You must enable **Enigmail** for each email account, in **Thunderbird**, through which you want to send and receive **GnuPG** encrypted email. To do so, follow the steps below.

**Step 1**. **Click** ![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-414.png) and **select** **Preferences > Account Settings** 

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-435.png)![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-436.png)

*Figure 1: Opening Thunderbird's Account Preferences*

This will open the *Account Preferences* screen

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-437.png)

*Figure 2: Thunderbird's Account Preferences screen*

**Step 2**. **Click** *OpenPGP Security* under the account with which you want to send and receive encrypted email

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-438.png)

*Figure 3: Enigmail's OpenPGP settings for an email account in Thunderbird*

This screen allows you to set various **Enigmail** preferences related to email encryption. If you generated your **GnuPG** *key pair* by following the instructions in the previous section – after adding a single account to **Thunderbird** – that account should already be configured to work with **Enigmail**. It should also be linked to the *key pair* you generated. If it is not, continue with *Step 3*, below. If it is, you can skip to *Figure 6*.

**Step 3**. **Check** the box next to *Enable OpenPGP support (Enigmail) for this identity*

**Step 4**. **Click** **[Select Key...]** to open the *Select OpenPGP Key for Encryption* window

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-440.png)

*Figure 4: Enigmail's Select OpenPGP Key for Encryption screen*

**Step 5**. **Select** the *key pair* you want to use for this email account

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-441.png)

*Figure 5: Selecting a key pair for a particular email account in Thunderbird*

**Step 6**. **Click** **[Select Key...]** to link this *key pair* with this email account and return to the *OpenPGP Security* settings screen

Below, we recommend two optional, non-default settings.

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-439.png)

*Figure 6: Configuring Enigmail for this email account*

**Step 7**. **Check** the *Use PGP/MIME by default* box

With this box checked, **Enigmail** is better able to encrypt email attachments, including their filenames.

**Step 8**. **Check** the *sign encrypted messages* box

With this box checked, **Enigmail** will digitally sign all encrypted email sent through this account unless you specifically tell it not to. Unencrypted messages will remain unsigned by default.

**Step 9**. **Click** **[OK]** to return to **Thunderbird**


### 4.2.3 View and manage your key properties

Once you have generated your **GnuPG** *key pair* and configured your email account to work with **Enigmail**, you can view and manage the properties of your *key pair* by following the steps below.

**Step 1**. **Click** ![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-414.png) and **select** **Enigmail > Key Management** 

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-442.png) ![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-443.png)

*Figure 1: Opening Enigmail's Key Management screen*

This will activate your Enigmail Key Management screen

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-444.png)

*Figure 2: Enigmail's Key Management screen*

**Step 2**. **Double-click** the name of your *key pair* to view or edit its properties 

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-445.png)

*Figure 3: key pair properties*

The Key Properties window displays important information about your **GnuPG** *key pair*: 

- **Key ID**: The *key ID* shown above for *ekaterina@riseup.net* is **0xFA4CD1D2**. (This corresponds to the last eight digits of the full *key fingerprint* below.)
- **Key fingerprint**: The *key fingerprint* for the same *key pair* is **93A4 EDCD 2C9A B746 F209 AD2A 0EF3 0EA3 FA4C D1D2**. *Your key fingerprint is not something you need to keep secret*. In fact, it is meant to be shared.
- **Expiration date**: This *key pair* will no longer work after 18 December, 2020.

Before others can send you encrypted email, they must have a copy of your *public key*. You can learn more about sharing keys in [*Section 4.3*](#2455). Your *key fingerprint* is an important part of how others can make sure that the key they have for you is *actually yours*. We discuss *key verification* in [*Section 4.4*](#2456). 

#### (Optional) Changing the expiration date of a key pair

If you need to change the expiration date of your **GnuPG** *key pair*, follow the steps below. This is most useful as a way to *extend* the expiration date, as it approaches, if you need more time to generate a new *key pair* and inform those with whom you communicate using encrypted email. 

**Step 1:** **Click** **[Select action...]** and **select** *Change Expiration Date*

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-446.png)

*Figure 4: Changing the expiration date of a GnuPG key pair*

This will activate the *change expiration date* screen shown below

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-447.png)

*Figure 5: Changing the expiration date of a GnuPG key pair*

**Note**: The number of years shown at the bottom of the screen does not necessarily match the current expiration date. If you click *[OK]* without changing anything, you may temporarily reduce the life-span of your *key pair*.

**Step 2**. **Type** the number of years, starting from today, that you would like this *key pair* to function.

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-448.png)

*Figure 6: Changing the expiration date of a GnuPG key pair*

**Step 3**. **Click** **[OK]** to enter the passphrase for your private key

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-449.png)

*Figure 7: Entering a private key passphrase*

**Step 4**. **Type** your passphrase

**Step 5**. **Click** **[OK]** to change the expiration date of your **GnuPG** *key pair*


#### (Optional) Changing the passphrase for a private key

If you would like to change the passphrase that protects your private key, **click** **[Select action...]** and **select** *Change Passphrase* from the **Enigmail** *Key Properties* screen. You will be prompted for your current passphrase and asked to enter a new one (twice). We recommend changing your passphrase from time to time just in case it has been compromised without your knowledge. 



## 4.3 Exchanging public keys

Before you can start sending encrypted email messages to one another, you and your correspondents need to exchange public keys. You also need to confirm the validity of any key you accept by confirming that it really belongs to its purported sender.

### 4.3.1 Sending your public key as an email attachment

To send a public key using Enigmail both you and your correspondent will need to perform the following steps:

**Step 1:** Open Thunderbird and click on “**Write**” to write an email.
 
**Step 2:** Select **Enigmail > Attach Public Key...**
 
**Step 3:** Select the email account you would like your public key to be attached for, as illustrated below:

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-501.png)

**Step 4:** Once you click on “**Send**”, you will notice that your public key has been attached to your email.

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-502.png) 

**Step 5:** Click on “**Send**” to send your email with your public key attached to it.

### 4.3.3 Importing a public key attached to an email

Both you and your correspondent need to perform the following steps when importing each other's public keys:

The attachment should be visible in the lower, left-hand corner of the email in which it was sent

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-503.png)

*Figure 1: A public key attached to an email*

**Step 1:** Hold down **Control** and **click** the attachment 

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-504.png) 

*Figure 2: The context menu for a public key attached to an email* 

**Step 2:** **Click** *Import OpenPGP Key* to import your correspondent's *public key*

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-505.png) 

*Figure 3: The context menu for a public key attached to an email* 

**Step 3:** **Click** **[OK]** to close the window telling you that the *key(s) were successfully imported*.

To confirm that you now have your correspondent's *public key*, and to see details about it, **select**  **Enigmail > Key Management** from the **Thunderbird** menu to activate the **Enigmail** *Key Management* screen. 

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-506.png)

*Figure 4: A new public key displayed in Enigmail's Key Management screen*

## 4.4 Validating and signing public keys

It's important to verify that the imported key actually belongs to the person who sent it and to confirm its 'validity'. This is a step that both you and your email contacts should follow for each public key that you receive.

### 4.4.1 Validating someone else's public key

To validate your correspondent's public key, contact him using a means of communication that allows you to be absolutely certain that you are talking to the right person. In-person meetings are best, but voice and video conversations are acceptable if you are confident you can recognise his voice or appearance. *This conversation does not have to be confidential,* as long as you refrain from discussing sensitive topics. You will be exchanging *public keyr* fingerprints, which need not be kept secret.

Both you and your correspondent should verify the *fingerprints* of the public keys you have exchanged. A *fingerprint* is a unique series of numbers and letters that identifies a **GnuPG** *key pair*. You can use the **Enigmail** *Key Management* screen to view the *fingerprint* of the *key pairs* you have generated and of the *public keys* you have imported.

To view the *fingerprint* of a particular *key pair*, follow the steps below.

**Step 1:** Select **Enigmail > Key Management** through **Thunderbird's** menu bar.

**Step 2:** **Double-click** a *key pair* to open the **Enigmail** *Key Properties* window.

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-445.png)

*Figure 1: Enigmail's Key Properties screen*

**Step 3:** In the *Key Properties* window, you will be able to see the fingerprint of the selected *key pair*.

For example, the fingerprint of ekaterina@riseup.net is **93A4 EDCD 2C9A B746 F209 AD2A 0EF3 0EA3 FA4C D1D2**

Your correspondent should carry out these steps as well. To verify fingerprints, read the fingerprint of your key to your correspondent and have him verify that the fingerprint he has for your public key matches what you have. Then have your correspondent do the same for his fingerprint. If the fingerprints don't match, exchange public keys again and repeat the verification process.

**Note:** The fingerprint itself is not a secret and can be recorded for later verification at your convenience.

### 4.4.2 Signing someone else's valid public key

Once you have verified a correspondent's key, you should *sign it*. This will tell **Enigmail** to remember that you consider this key valid. 

**Important**: If you sign some else's public key, then make *your signed copy* of *their key* available publicly, it can easily expose the fact that you exchange sensitive information with that person. To prevent this from happening by accident, **always check the *Local signature* box when signing a correspondent's public key**.

You can sign a validated public key by following the steps below.

**Step 1**. **Select** **Enigmail > Key Management** from the Thunderbird menu to open the **Enigmail** *Key Management* window.

**Step 2**. Hold down **Control** and **click** the *public key* you want to sign. 

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-507.png)

*Figure 1: Signing someone else's public key*

**Step 3**. **Select** **Sign Key** 

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-508.png)

*Figure 2: Making sure that Enigmail to signs this key locally to avoid exposing your relationship with its owner*

**Step 4**. Make sure your *key pair* is selected next to *Key for signing*

**Step 5**. **Click** *I have done very careful checking*

**Note**: Other options (such as *I have not checked at all*) may not allow you to send encrypted message to the owner of this key. And, due to a bug in **Enigmail**, it may be difficult to change this setting later. Accordingly, we recommend that you always select *I have done very careful checking* when signing a correspondent's *public key*.

**Step 6**. **Check** the **Local signature (cannot be exported)** box

**Important**: Unless you are very confident with **GnuPG** – and know for a fact that the owner of this *public key* wants your signature of his key to be public – you should check this box.

**Step 7**. **Click** **[OK]** to enter the passphrase for your private key

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-509.png)

*Figure 3: Entering the passphrase for your private key to sign someone else's public key*

**Step 8**. **Type** the passphrase for your private key

**Step 9**. **Click** **[OK]** to sign this public key. This will tell **Enigmail** that you have verified the identity of its owner, which will allow you to send him encrypted email.

## 4.5 Encrypting and decrypting email messages

The header of any email message - its *Subject* and intended recipients including any information in the *To*, *cc* and *bcc* fields - cannot be encrypted and will be sent in open text. To ensure the privacy and security of your exchanged emails, the subject of your email should be kept non-descriptive as to not reveal sensitive information. In addition, you are advised to put all addresses in the *bcc* field when sending emails to a group of people.

When encrypting email messages with attachments, we strongly recommend using the **PGP/MIME** option, as this will extend encryption to include any files and file names attached to your email.

Note that any encrypted email you send with Thunderbird/Enigmail/GnuPG is automatically encrypted to your key along with the chosen recipients of this email, so you are able to decrypt emails in your sent folder.

### 4.5.1 Sending encrypted email

Once both you and your correspondent have successfully imported and validated and signed each other's public keys, you are ready to begin sending encrypted messages and decrypting received ones.

You can encrypt the content of your email messages through the following steps:

**Step 1**. In Thunderbird, **click** **[Write]** and compose an email to a recipient for whom you have a signed *public key*

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-510.png)

*Figure 1: Thunderbird's Compose Window*

After you enter a ***To:*** address, the following message should appear in the upper, right-hand corner of the window *if you have a verified public key for the recipient*: 

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-512.png)

*Figure 2: Enigmail letting you know that it is ready to encrypt and sign a message*

If this message *does* appear, you can skip to *Step 6*, below. If it *does not*, you can explicitly request that **Enigmail** encrypt and sign the message by following the step below. (However, this will not work unless you have a valid public key for the recipient.)

**Step 2**. **Click** ***Enigmail:***, in the upper, left-hand corner of the *compose window*, just beneath the **[Send]** button. 

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-511.png)

*Figure 3: Enabling encryption manually*

**Step 3**. **Check** the *Encrypt Message* box

**Step 4**. **Check** the *Sign Message* box

**Step 5**. **Click** **[OK]** to return to the *compose window*

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-510.png)

*Figure 4: Thunderbird's Compose Window*

**Step 6**. **Click** **[Send]** to enter the passphrase for your private key 

**Step 7**. **Type** the passphrase for your private key

**Step 8**. **Click** **[OK]** to send your (encrypted and signed) message.

### 4.5.2 Decrypting an email from someone else

When you open an encrypted message, **Enigmail** will automatically prompt you for the passphrase to your private key so that it can decrypt the message. Simply **type** your passphrase and **click** **[OK]**. **Enigmail** will add some information to the top of the message letting you know whether or not the message was signed and by whom: 

![](/sites/securityinabox.org/files/media/thunderbird-mac-en-v01-514.png)


# FAQ

***Q***: What happens if I just install **Enigmail** and not **GnuPG**?

***A***: That's simple, really. **Enigmail** just won't work. After all, it's the **GnuPG** software that provides the encryption engine that **Enigmail** uses.

***Q***: How many email accounts can I set up in **Thunderbird**?

***A***: As many as you like! **Thunderbird** is an email manager and can easily handle 20 or more email accounts!

***Q***: My friend has a **Gmail** account. Should I convince him to install **Thunderbird**, **Enigmail** and **GnuPG**?

***A***: That would be ideal. Just make sure he configures all of his security settings in exactly the same way as you did. Then the two of you will have an extremely effective way of communicating in privacy and safety!

***Q***: Remind me one more time, which parts of an email message does **Enigmail** encrypt?

***A***: **Enigmail** encrypts the content of the message. It doesn't encrypt the subject line of the message, your email address or the name you chose to associate with that email account. So, if you're trying to send a confidential message, make sure the subject line doesn't give you away! And, if you want to stay anonymous, avoid displaying or even using your real name when you create your email account.

***Q***: I still don't understand the purpose of digitally signing my messages.

***A***: A digital signature proves that you're the real sender of a particular message and that the message hasn't been tampered with on its way to your intended recipient. Think of it as the electronic equivalent of the wax seal on an envelope, which contains a very important letter.
