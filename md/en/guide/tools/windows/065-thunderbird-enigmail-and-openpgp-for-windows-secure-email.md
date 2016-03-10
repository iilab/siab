

---

lang: en
community: guide
type: tools
os: windows
weight: 065
title: Thunderbird, Enigmail and OpenPGP for Windows - secure email

---

**Mozilla Thunderbird** is a free and open source email client for receiving, sending and storing emails. You can manage multiple email accounts through a single program. **Enigmail** and **GnuPG** will give you access to authentication, digital signing and encryption to ensure the privacy and security of your email communication. 

# Required reading


{{ required_reading: ../../secure communication }}


{{ tool: ./065-tool.md }}

# What you will get from this guide

- The ability to manage different e-mail accounts through a single program.
- The ability to read and compose messages after disconnecting from the Internet.
- The ability to use public key encryption to keep your email private.

# 1. Introduction to Thunderbird





## 1.0 Other tools like Thunderbird

The **Mozilla Thunderbird** is an email client is available for **GNU Linux**, **Mac OS**, **Microsoft Windows** and other operating systems. Managing multiple email accounts is a complex task from the digital security viewpoint; therefore, we *strongly recommend* that you use **Mozilla Thunderbird** for this purpose. The security advantages available in **Thunderbird**, a cross-platform *free* and *open source* program, are even more important when compared to its commercial equivalents like **Microsoft Outlook**. However, if you would prefer to use a program other than **Mozilla Thunderbird**, we recommend the following free and open source alternatives:

* [**Claws  Mail**](http://www.claws-mail.org/) available for **GNU Linux** and **Microsoft Windows**;
* [**Sylpheed**](http://sylpheed.sraoss.jp/en/) available for for **GNU Linux**, **Mac OS** and **Microsoft Windows**;
* [**Alpine**](http://www.washington.edu/alpine/) available for **GNU Linux**, **Mac OS** and **Microsoft Windows**.

Note: Although we recommend using **Enigmail/GnuPG** for its ease of use with Thunderbird, you still can also use stand-alone encryption tools such as gpg4usb in conjunction with Thunderbird. Please read [gpg4usb](../gpg4usb/windows) chapter to see other way to encrypt your email using public key encryption method.

## 1.1 Things you should know about Thunderbird, Enigmail and GPG before you start

**Mozilla Thunderbird** is a cross-platform, free and open source email client for receiving, sending and storing emails. An email client is a computer application that lets you download and manage your email messages without an Internet browser. You can manage multiple email accounts using a single program. You must have an existing email account before using **Thunderbird**. You may also create [**RiseUp**](../riseup/internet) email accounts if you wish.

**Gnu Privacy Guard** (**GPG**) is free and open-source software capable of encrypting, decrypting and digitally signing messages and files. It also generates and manages the public/private *key pairs* that are used to carry out these encryption operations. This guide was written for **GPG** version 1.4.18

**Enigmail** is a **Thunderbird** add-on that allows you to access the authentication and encryption features provided by **GnuPG** (which must be installed for **Enigmail** to work). This guide was written for **Enigmail** version 1.7.

**TorBirdy** is a **Thunderbird** add-on that allows you to send and receive email while relying on [Tor](../torbrowser/windows) to circumvent online filtering and protect your anonymity. This guide was written for **TorBirdy** version 0.1.2

# 2. Install Thunderbird and setup accounts

To begin installing **Thunderbird**, perform the following steps:

## 2.0 Install Thunderbird

**Step 1**. **Double click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_01.png); the *Open File - Security Warning* dialog box may appear. If it does, **click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_02.png) to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/thunderbird_03.png)

*Figure 1: The Extracting status progress bar*

After the **Thunderbird** files have completed extracting themselves, the *Welcome to the Mozilla Thunderbird Setup Wizard* window appears.

**Step 2**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_04.png) to activate the *Mozilla Thunderbird - Setup Type* window. 

**Step 3**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_04.png) at the *Choose setup options* window. The default setup is *Standard*.

**Step 4**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_04.png) to accept the default settings and activate the following screen:

![](/sites/siabnext.ttc.io/files/media/thunderbird_05.png)

*Figure 2: The Mozilla Thunderbird - Summary screen*

**Step 5**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_06.png) to start the installation process. The **Mozilla Thunderbird - Installing** progress status window appears. After the installation process is complete, the following screen appears:

![](/sites/siabnext.ttc.io/files/media/thunderbird_07.png)

*Figure 3: The Completing the Mozilla Thunderbird Setup Wizard screen*

**Step 6**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_08.png) to complete the installation process.

**Tip**: **Thunderbird** will automatically launch itself if the *Launch Mozilla Thunderbird now* check box is enabled, as shown in *figure 3* above. To open the program in the future, either **double click** the **Thunderbird** desktop icon, or **select > Programs > Mozilla Thunderbird > Mozilla Thunderbird**.


## 2.1 Disable Global Search and Indexer

**Warning**: The *Global Search and Indexer* feature in **Thunderbird** *must* be turned off to optimize its performance. Depending on the quantity and size of your emails, it may reduce the speed of your system, by continuously and unnecessarily over-writing of information to your hard drive. As your hard drive becomes increasingly full, it will slow down many unrelated system operations.

To turn off the *Global Search and Indexer* option, perform the following steps: 

**Step 1**. **Select Tools > Options** in the **Thunderbird** console to activate the *Options* window.

**Step 2**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_09.png) to activate its associated tab as follows:

![](/sites/siabnext.ttc.io/files/media/thunderbird_10.png)

*Figure 4: The Options window displaying the Advanced tab*

**Step 3**. **Click** the *Enable Global Search and Indexer* check box in the *Advanced Configuration* section to *disable* this option as shown below: 

![](/sites/siabnext.ttc.io/files/media/thunderbird_11.png)

*Figure 5: The Advanced Configuration section*

Now that you have successfully disabled this option, you are ready to register an email account in **Thunderbird**.

## 2.2 Register an Email Account in Thunderbird

The *System Integration* window will appear at first login. This window can be set to *Use Thunderbird as the default client for: Email*. Alternatively, you can choose to *Skip Integration* .

**Step 1**. At the *Welcome to Thunderbird* window **click** *Skip this and use my existing email* option so that it resembles the following screen:
 
![](/sites/siabnext.ttc.io/files/media/thunderbird_12.png)

*Figure 6: Welcome to Thunderbird screen*

**Step 2**. **Type** in your name, email address and password in the corresponding text fields; **click** the check box to disable the *Remember my password* option so that your screen resembles *figure 7* below.

![](/sites/siabnext.ttc.io/files/media/thunderbird_13.png)

*Figure 7: The Mail Account Setup window*

**Step 3**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_14.png) to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/thunderbird_15.png)

*Figure 8: The Mail Account Setup window with the **IMAP (remote folders)** option enabled*



## 2.3 IMAP and POP: Descriptions and usage

**Internet Message Access Protocol** (**IMAP**) and **Post Office Protocol** (**POP**) are two different methods used to store and receive emails.

- **Internet Message Access Protocol** (**IMAP**): When using **IMAP** all your folders (including *Inbox*, *Drafts*, *Templates*, *Sent*, *Trash* and all other folders) reside on the email server. Therefore, you may access these folders from a different computer. All messages will reside on the server and initially, only the email messages headers or title bars (containing information like the date and time, message subject, name of sender, etc.) are downloaded for display on your computer. Full messages are downloaded when you open them. **Thunderbird** may also be configured to store copies of messages from all or some of the folders on your computer, so that you may work with them offline (that is, without using an Internet connection). In **IMAP** when you delete emails or folders, you do so on *both* your local computer and on the server.

-  **Post Office Protocol version 3** (**POP3**): When using **POP3** only the *Inbox* (a folder into which new incoming messages are delivered) resides on the server; all other folders are located on your local computer only. You may choose between leaving messages in the *Inbox* folder on the server after you have downloaded them to your computer, or you may delete them from the server. If you access your email account from a different computer, you will only be able to view messages in the *Inbox* folder (new messages, and old messages which you have not deleted). Note that depending on the server configuration copies of your sent emails may be stored on the server in *Sent* folder. It is worth checking this yourself.

**Step 4**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_16.png) to create your account, and activate the **Thunderbird** console with the email account displayed in the sidebar at left as follows:

![](/sites/siabnext.ttc.io/files/media/thunderbird_17.png)

*Figure 9: The Mozilla Thunderbird main user interface displaying the newly created riseup account*

**Note**: To add another email account, **click Local Folders > Accounts > Create a new account: Email** to activate *figure 7* in this section, and repeat **step 2** to **step 4**.

After you have successfully registered your email accounts in **Thunderbird**, the next time you open the main user interface, you will be prompted to enter your password for each account as follows: 

![](/sites/siabnext.ttc.io/files/media/thunderbird_20.png)

*Figure 10: The Mail Server Password Required window*

**Note**: Although password recording or 'remembering' features are generally not recommended from an internet privacy and security standpoint, **Thunderbird** does support a *Master Password* feature. This feature enables you to use one password to protect any passwords related to your different accounts, entered during the setup process. For more information about this feature, please refer to section [**3.3 How to Configure the Security tabs in Thunderbird**](#743) - **The Password tab**.

## 2.4 Register Blogs, News Feeds and Newsgroup Accounts

To create and register an account for blogs, news feeds and newsgroups, perform the following steps:

**Step 1**. Select your account from the sidebar on the left and **click Accounts > Feeds** to activate the *Feed Account Wizard* window below:

![](/sites/siabnext.ttc.io/files/media/thunderbird_21.png)

*Figure 11: Feed Account Wizard - Account Name window*

**Step 2**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_04.png) to activate the following screen: 

![](/sites/siabnext.ttc.io/files/media/thunderbird_22.png)

*Figure 12: The Account Wizard - Congratulations window*

**Step 5**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_08.png) to complete the account setup process, and return to the **Thunderbird** console.

Now that you have properly configured **Thunderbird** for optimal usage, please proceed to the following section on [**How to Configure the Security Settings in Thunderbird**](#740).



# 3. Security Options in Thunderbird

In the context of **Mozilla Thunderbird**, security generally refers to protecting your computer from harmful or malicious email messages. Some may be just spam, others may contain spyware and viruses. There are several settings which must be configured, disabled or enabled within **Mozilla Thunderbird** to strengthen its ability to defend your system from attacks originating from emails. It is also *absolutely crucial* that you have anti-malware and firewall software installed. 

For more information on preventing harmful or malicious software, please refer to the **How-to Booklet** chapter on [**Protecting your Computer from Viruses, Malware and Hackers**](../malware) for more information about tools such as [**Avast**](../avast/windows), [**Comodo Firewall**](../comodo/windows) and [**Spybot**](../spybot/windows).

## 3.1 Disable the Preview Pane in Thunderbird

The **Thunderbird** main window is divided into three areas: The left sidebar displays the folders for your email accounts, the right side shows a list of messages, and the bottom pane displays a *preview* of a selected email message. The preview is automatically visible as soon as a message has been selected. 

**Note**: If an email contains any malicious code, then *preview* message pane could activate it; therefore it is a good idea to disable it. 

![](/sites/siabnext.ttc.io/files/media/thunderbird_23.png)

*Figure 1: The Thunderbird main user interface*

To disable the preview pane, perform the following step: 

**Step 1**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_24a.png) to display the *Thunderbird Menu* and **select Options > Layout > Massage Pane F8** to disable it as follows: 

![](/sites/siabnext.ttc.io/files/media/thunderbird_24.png)

*Figure 2: The Options menu displaying the Layout sub-menu and Message Pane option deselected*

The *Message Pane* will disappear, and you must **double-click** an email message to read its contents. If an email message looks suspicious (perhaps it has an unexpected or irrelevant subject title, or comes from an unknown sender), you now can choose to delete it without having to preview its content.

## 3.2 Disable the HTML Feature in Thunderbird

**Thunderbird** lets you use **HyperText Markup Language** (**HTML**) to compose and read messages. This lets you receive and send messages that include colours, fonts, images and other formatting features. However, **HTML** is the same language used for Web pages; viewing messages with **HTML** formatting, may expose you to malicious emails which pose some of the same kinds of threats posed by web pages. 
 
To disable the **HTML** formatting feature, perform the following step: 

**Step 1**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_24a.png) to display the *Thunderbird Menu* and **select Options> View > Message Body As > Plain Text** as follows: 

![](/sites/siabnext.ttc.io/files/media/thunderbird_25.png)

*Figure 3: The View menu displaying the Message Body submenu with the Plain Text option selected*


## 3.3 Configure Security Options

**Thunderbird** has two built-in junk mail filters that can help you determine which of your incoming messages are spam. By default, these filters are disabled, so you must enable them for use. Even after they have been enabled, you will continue to receive junk mail, but **Thunderbird** will automatically sort them into the *Junk* folder. 

Email scams - also referred to as *phishing* emails - usually attempt to make you click on a link that is embedded in the email. Frequently, these links direct your browser to a web site that will attempt to infect your computer with a virus. In other cases, the link will take you to a web site that appears to be legitimate, to deceive you into entering a valid user name and password, which can then be used or sold by the entity or people for commercial or malicious purposes. 

**Thunderbird** can help to identify and warn you about emails like this. Additional tools that can help prevent infection from malicious websites are described in the [**Other Useful Mozilla Add-Ons**](../firefox/windows#803) section of the **Firefox** chapter.

The first set of assorted junk mail and security controls are accessed through the *Options - Security* window through which the majority of these privacy and security options are configured. To access them, perform the following steps:

**Step 1**. **Select Menu > Options** to activate the *Options* window.

**Step 2**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_26.png) to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/thunderbird_27.png)

*Figure 4: The Security window displaying its associated tabs*

### The Junk tab ###

**Step 1**. **Check** the relevant options in the *Junk* tab as shown in *figure 4* above, to enable **Thunderbird** to delete email that you have determined to be junk mail. Additional junk mail settings are described later on in this section. 

### The Email Scams tab ###

**Step 1**. **Check** the *Tell me if the message I'm reading is a suspected email scam* option to enable **Thunderbird** to analyse messages for email scams as follows: 

![](/sites/siabnext.ttc.io/files/media/thunderbird_28.png)

*Figure 5: The Email Scams tab* 

### The Anti-Virus tab ###

**Step 1**. **Click** the *Anti-Virus* tab to activate the following screen: 

![](/sites/siabnext.ttc.io/files/media/thunderbird_29.png)

*Figure 6: The Anti-Virus tab* 

This option lets your anti-virus software scan and isolate individual messages as they arrive. Without this setting enabled, it is possible that your *entire* *Inbox* folder could be 'quarantined' if you receive an infected message.

**Note**: This assumes that you have a functioning anti-virus program installed. Please refer to [**Avast**](../avast/windows) for more information on how to install and configure anti-virus software.

### The Passwords tab ###

**Step 2**. **Click** the *Passwords* tab to activate the following screen: 

![](/sites/siabnext.ttc.io/files/media/thunderbird_30.png)

*Figure 7: The Passwords tab*

**Important:** We strongly recommend to keep your passwords private and secure using a software designed precisely for this purpose; please refer to [**KeePass**](../keepass/windows) for more information. 

**Note**: The options in the *Password* tab will only work if you checked the *Remember password* option in the first *Mail Account Setup* screen when you registered your email accounts with **Thunderbird**. 

**Step 1**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_31.png) to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/thunderbird_32.png)

*Figure 8: The Saved Passwords window*

The *Saved Passwords* window lets you remove or view all the corresponding passwords for each of your accounts. However, to maximise your privacy and security, you can set a *Master Password* to protect access to your email accounts and make all of your account passwords inaccessible to anyone else familiar with the **Thunderbird** password options.

**Step 3**. **Check** the *Use a master password* option as shown in *figure 7* to enable the *Change Master Password...* button.

**Step 4**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_33.png) to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/thunderbird_34.png)

*Figure 9: Change Master Password window*

**Step 5**. **Type** in an appropriately strong password that only you will remember, and then **click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_35.png) to confirm it as your *Master Password*. 

### Web Content ###

A cookie is a small piece of text which your web browser uses to authenticate or identify a given web site. The *Web Content* option lets you specify which blog, news feed or newsgroup cookies are reliable and safe.  

**Step 1**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_36.png) to display the *Web Content* options as follows:

![](/sites/siabnext.ttc.io/files/media/thunderbird_37.png)

*Figure 10: The Privacy tab*

**Step 2**. **Select** the *I close Thunderbird* item in the *Keep until:* option to delete those cookies whenever you close **Thunderbird** for additional security.


## 3.4 Enable the Account Settings Junk Mail Filter

The second type of **Thunderbird** junk mail filter is available through the *Account Settings - Junks Settings* window. By default, these filters are disabled, so they must be enabled if you wish to use them. Whenever junk emails arrive **Thunderbird** will automatically sort them into the *Junk* folders associated with different accounts. 

**Step 1**. **Select Tools > Account Settings** to activate the *Account Settings* window.

**Step 2**. **Select** the *Junk Settings* option associated with a specific **Gmail** or **RiseUp** account in the sidebar. 

**Step 3**. **Enable** the *Junk Settings* options so that your own *Account Settings - Junk Settings* screen resembles the following: 

![](/sites/siabnext.ttc.io/files/media/thunderbird_38.png)

*Figure 12: The Account Settings - Junk Settings window*

**Step 4**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_35.png) to complete the configuration of the *Account Settings* window.

**Note**: The *Junk Settings* options must be configured separately for each account. As such, junk mail for a **Gmail** or a **RiseUp** account will be placed in its corresponding *Deleted* folder. Alternatively, you may designate a *Local Folder* to receive junk mail from all your accounts. 

![](/sites/siabnext.ttc.io/files/media/thunderbird_39.png)

*Figure 13: The Account Settings - Junk Settings window, displaying the settings for a central junk folder*

**Step 1**. **Select** the *Junk Settings* option directly beneath *Local Folders* in the sidebar.

**Step 2**. **Select** the *Local Folders* item from the *"Junk" folder on:* drop-down list as displayed in *figure 13*.

**Step 3**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_35.png) to complete the configuration of the *Account Settings* window.

Now that you have successfully configured the assorted security options and junk mail settings in **Thunderbird**, please proceed to the following section, [**How to Use Enigmail with GnuPG in Thunderbird**](#745). 


# 4. Install and use Enigmail and GnuPG with Thunderbird

**Enigmail** is a **Mozilla Thunderbird** add-on that lets you protect the privacy of your email communication. **Enigmail** is an interface that lets you use **GnuPG** encryption program from within **Thunderbird**.  The **Engimail** interface is represented as *Enigmail* in the **Thunderbird** console tool bar. 

**Engimail** is based on [**public-key cryptography**](http://en.wikipedia.org/wiki/Public-key_cryptography).
In this method, each individual must generate her/his own personal key pair. The first key is known as the *private key*. It is protected by a password or passphrase, both to be guarded and *never* shared with *anyone*. 

The second key is known as the *public key*. This key can be shared with any of your correspondents. Once you have a correspondent’s *public key* you can begin sending encrypted emails to this person. Only she will be able to decrypt and read your emails, because she is the only person who has access to the matching *private key*.

Similarly, if you send a copy of your own *public key* to your email contacts and keep the matching *private key* secret, only you will be able to read encrypted messages from those contacts.

**Enigmail** also lets you attach *digital signatures* to your messages. The recipient of your message who has a genuine copy of your *public key* will be able to verify that the email comes from you, and that its content was not tampered with on the way. Similarly, if you have a correspondent's *public key*, you can verify the digital signatures on her signed messages.

## 4.1 Install Enigmail and GnuPG

Please refer to the [**download section**](#735) for instructions on how to download **Enigmail** and **GnuPG**.

### 4.1.1. Install GnuPG 

Installing **GnuPG** is quite straightforward, and resembles other software installations you may have performed and can be done by doing the following steps: 

**Step 1**. **Double click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_40.png) to to begin the installation process. The *Open File - Security Warning* dialog box may appear. If it does, **click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_02.png) to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/thunderbird_41.png)

*Figure 1: GNU Privacy Guard Setup Wizard*

**Step 2**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_04.png) to activate the *GNU Privacy Guard Setup - License Agreement* window; after you have completed reading it, **click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_04.png) to activate the *GNU Privacy Guard Setup - Choose Components* window.

**Step 3**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_04.png) to accept the default settings and activate the *GNU Privacy Guard Setup - Install Options - GnuPG Language Selection* window. 

**Step 4**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_04.png) to accept *en-English* as the default language, and activate the *Choose Install Location* window.

**Step 5**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_06.png) to accept the default installation path and activate the *Choose Start Menu Folder* screen.

**Step 6**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_06.png) begin unpacking and installing various **GnuPG** packages. After this process has completed itself, the *Installation Complete* screen will appear.

**Step 7**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_04.png) and then ![](/sites/siabnext.ttc.io/files/media/thunderbird_08.png) to complete installing the **GnuPG** program.

### 4.1.2 Install the Enigmail Add-on for Thunderbird

After you have successfully installed the **GnuPG** software you are now ready to install the **Enigmail** add-on. 

To begin installing **Enigmail**, perform the following steps: 

 **Step 1**. **Open Thunderbird**, then **click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_24a.png) to display the *Thunderbird Menu* and **select Add-ons** to activate the *Add-ons Manager* window.

**Step 2**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_44.png) in the left hand sidebar - if the Enigmail Add-on has not yet been detected, you will see the message *You do not have any Add-ons of this type installed*.

**Step 3**. If the Enigmail Add-on appears in the main *Extensions* panel **click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_46.png). If it does not appear, **click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_45a.png) and  **select** *Install Add-on from File* as shown below: 

![](/sites/siabnext.ttc.io/files/media/thunderbird_46a.png)

*Figure 3: Tools for All Add-ons menu*

**Step 4**. Navigate to the folder where you have saved the Enigmail extension (most probably your *Downloads* folder) as shown in the following screen:

![](/sites/siabnext.ttc.io/files/media/thunderbird_47.png)

*Figure 4: The Select an extension to install*

**Step 5**.  **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_48.png) to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/thunderbird_49.png)

*Figure 5: The Software Installation window*

**Important**: Before you perform step 6, make sure all your online work has been saved!

**Step 6**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_50.png) and then **click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_51.png) to complete the **Enigmail** add-on installation. 

To verify your installation of the **Enigmail** add-on was successful, return to the **Thunderbird** main user interface, **click** on ![](/sites/siabnext.ttc.io/files/media/thunderbird_24a.png) and check if *Enigmail* appears as one of the option, as follows: 

![](/sites/siabnext.ttc.io/files/media/thunderbird_52.png)

*Figure 6: The Thunderbird toolbar with Enigmail highlighted*

### 4.1.3 Confirm that Enigmail and GnuPG are Working

Before you can begin using **Enigmail** and **GnuPG** to authenticate and encrypt your emails, you must first ensure that they are both communicating with each other.

**Step 1**. **Select Enigmail > Preferences** to display the *Enigmail Preferences* screen as follows:

![](/sites/siabnext.ttc.io/files/media/thunderbird_53.png)

*Figure 7: The Enigmail Preferences window*

If **GnuPG** has been successfully installed, the ![](/sites/siabnext.ttc.io/files/media/thunderbird_54.png) will be visible in the *Files and Directories* section; otherwise, you may receive a pop-up alert resembling the following:

![](/sites/siabnext.ttc.io/files/media/thunderbird_55.png)

*Figure 8: The Enigmail Alert pop-up message*

**Tip**: If you have received this message, it may indicate that you did not install **GnuPG** or you have installed it in different location. If you installed **GnuPG** in a different location, **check** the *Override with* option to enable the *Browse...* button, and then **click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_69.png) to activate the *Locate GnuPG program* and manually navigate to the location of the *gpg.exe* file on your computer, otherwise please go back to [4.1 How to Install Enigmail and GnuPG](#747).

**Step 2**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_35.png) to return to the **Thunderbird** console.


## 4.2 Generate Key Pairs and Configure Enigmail

Once you have confirmed that **Enigmail** and **GnuPG** are working properly, you can configure one or more of your email accounts to use **Enigmail** to generate one or more private/public key pairs.

### 4.2.1 Use the OpenPGP Wizard to Generate a Key Pair

**Engimail** provides two ways of generating a private-public key pair; the first uses the *Enigmail Setup Wizard* and the second uses the *Key Management* screen. 

To generate a key pair for the first time using the *Enigmail Setup Wizard*, perform the following steps:

**Step 1**. If **Setup Wizard** window is not already activated **select Enigmail > Setup Wizard** to open the *Enigmail Setup Wizard* screen as follows: 

![](/sites/siabnext.ttc.io/files/media/thunderbird_56.png)

*Figure 9: The Welcome to the Enigmail Setup Wizard screen*

**Step 2**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_04.png) to activate the following screen. *Note - this screen will only appear if you have set up key pairing for another account*.

![](/sites/siabnext.ttc.io/files/media/thunderbird_59.png)

*Figure 10: The Select Identities screen*

**Step 3**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_04.png) to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/thunderbird_60.png)

*Figure 11: The Encryption - Encrypt Your Outgoing Emails screen*

**Step 4**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_04.png) to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/thunderbird_61.png)

*Figure 12: The Signing - Digitally Sign Your Outgoing Emails screen*

**Step 5**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_04.png) to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/thunderbird_62.png)

*Figure 13: The Preferences - Change Your Email Settings to Make Enigmail Work More Reliably screen*

**Step 6**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_04.png) to activate the *Create Key - Create A Key To Sign and Encrypt Email* window. 

**Note**: The first time you attempt to create a key for an email account, the *No OpenPGP Key Found* screen will appear. 

**Step 7**. **Select** *I want to create a new key pair for signing and encrypting my email*.

**Step 8**. **Type** a strong passphrase into both the *Password* fields.

![](/sites/siabnext.ttc.io/files/media/thunderbird_65.png)

*Figure 15: The Create Key - Create A Key To Sign and Encrypt Email window*

**Step 9**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_04.png) to activate the *Summary* screen, which displays the settings used while generating the key pair.

**Step 10**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_04.png) to start the key pair generation, as shown in the following screen:

![](/sites/siabnext.ttc.io/files/media/thunderbird_67.png)

*Figure 16: Key Generation - You key is now being generated window*

**Note**: Any key pair generated using *Enigmail Setup Wizard* is automatically has a 4096-bit size, and a lifespan of 5 years.

**Step 11**. After the key is generated, you will be prompted to create a revocation certificate. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_76.png) as shown in the following screen:

![](/sites/siabnext.ttc.io/files/media/thunderbird_68.png)

*Figure 17: The Enigmail Prompt confirmation*

**Note**: If you know that a hostile or malicious party has gained unauthorised access to your private key or you lost access to this key, you may send the revocation certificate to your contact to let them know that they should not use your matching public key. Keep in mind that you might need to do this if your computer is lost, stolen or confiscated. You are strongly advised to back up and protect your revocation certificate.

**Step 12**. You will be asked to **type in** the password that you associated with your newly created key. And then **navigate** to a location where you can store the certificate safely and **click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_78.png) on following screen:

![](/sites/siabnext.ttc.io/files/media/thunderbird_70.png)

*Figure 18: Create & Save Revocation Certificate*

**Step 13**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_04.png) to complete generating both a key pair and revocation certificate.


### 4.2.2 Generate Additional Key Pairs and Revocation Certificates

It is a common practice to have a separate key pair for each email account. Using the same key pair for many email accounts is possible, but may be confusing for your contacts. It is possible to add more than one email account to a single key pair (we do not discuss it in this chapter) what brings some usability benefits, but also associates all those email accounts to one person which may not be desirable.

Follow the steps below if you want to generate additional key pairs for your other email accounts.

**Step 1**. **Select Enigmail > Key Management** to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/thunderbird_71.png)

*Figure 19: The Enigmail Key Management Generate menu with New Key Pair item selected*

**Note**: **Check** the *Display All Keys by Default* to view the key pair generated by using the *OpenPGP Setup Wizard* for your first email account, as presented in *figure 19* above and *figure 23* below.

**Step 2**. **Select Generate > New Key Pair** from the *Key Management* as displayed in *figure 19* above to activate the following screen: 

![](/sites/siabnext.ttc.io/files/media/thunderbird_72.png)

*Figure 20: The Generate OpenPGP Key screen*

**Step 3**. **Select** an email account from the *Account / User ID* drop-down list, **check** the *Use generated key for the selected identity* option. And create a passphrase to protect your private key.

**Note**: As its name implies, a passphrase is simply a longer password. **Enigmail** is simply prompting you to enter a password that is longer and more secure than a conventional one.

**Important**: Always generate key-pairs with a passphrase, and **never** enable the "no passphrase" option.

![](/sites/siabnext.ttc.io/files/media/thunderbird_73.png)

*Figure 21: The Generate OpenPGP Key displaying the Key Expiry tab*

**Note**: The length of time for which a key pair remains valid depends entirely on your privacy and security needs; the more frequently you change your key pairs, the more difficult it becomes for the new key pair to be compromised. However, every time you change key pair you will need to send the new public key to your correspondents, and verify it with each of them.

**Step 4**. **Type** in the appropriate number, and then **select** the desired unit of time (*days*, *months* or *years*) for which the key pair will remain valid. 

**Step 5**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_74.png) to activate the Enigmail Confirm window.

**Step 6**. You will be prompted to generate a certificate as shown in *figure 17*.

**Step 7**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_76.png) to activate the *Create & Save Revocation Certificate* navigation window.

**Note**: If you know that a hostile or malicious party has gained unauthorised access to your private key or you lost access to this key, you may send the revocation certificate to your contact to let them know that they should not use your matching public key. Keep in mind that you might need to do this if your computer is lost, stolen or confiscated. You are strongly advised to back up and protect your revocation certificate.

**Step 8**. Browse to a safe location to store the certificate as shown in the screen below and **click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_78.png). You will be then prompted to enter passphrase that you associated with your newly created key.

![](/sites/siabnext.ttc.io/files/media/thunderbird_77.png)

*Figure 22: The Create & Save Revocation Certificate*

**Step 9**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_35.png) to complete generating both a key pair and revocation certificate, and return to the following screen:

![](/sites/siabnext.ttc.io/files/media/thunderbird_79.png) 

*Figure 23: The Enigmail Key Management window with the key pair displayed*

**Note**: **Check** the *Display All Keys by Default* option to display all the key pairs and their associated accounts. Make sure you are in a safe environment to do this.

After you have successfully generated both your key pair and its associated revocation certificate, you are now ready to exchange public keys with a trusted correspondent.

### 4.2.3 Configure Enigmail for Use with Your Email Account

To enable **Enigmail** for use with a specific email account, perform the following steps:

**Step 1**.  **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_24a.png) to display the *Thunderbird Menu* and **select Options > Account Settings**.

**Step 2**. **Select** the *OpenPGP Security* menu item in the sidebar as follows: 

![](/sites/siabnext.ttc.io/files/media/thunderbird_80.png)

*Figure 24: The Account Settings - OpenPGP Security screen*

**Step 3**. **Check** the *Enable OpenPGP support* option and **select** the *Use email address of this identity to identify OpenPGP key* option.

**Step 4**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_35.png) to return to the **Thunderbird** console. 

## 4.3 Exchange Public Keys

Before you can begin sending encrypted email messages to one another, you and your correspondents must exchange public keys. You must also confirm the validity of any key you accept by confirming that it really belongs to its purported sender. 

### 4.3.1 Send a Public Key using Enigmail

To send a public key using **Enigmail** both your correspondent and you will perform the following steps:

**Step 1**. **Open Thunderbird** and then **click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_81.png) to write a new message.

**Step 2**. Select the menu option **Enigmail > Attach My Public Key**.

**Note**: In this method, the **Attachments:** pane is not displayed immediately; it will appear as soon as you send the message.

If you would like to send a different public key, **select** the menu option **Enigmail > Attach Public Key...** and then **select** the key you would like to send.

![](/sites/siabnext.ttc.io/files/media/thunderbird_82.png) 

*Figure 25: The Write message pane displaying the attached public key in the Attachments pane.*

**Step 3**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_83.png) to send your email with your attached public key. 

### 4.3.2 Import a Public key using Enigmail 

Both your correspondent and you will perform the same steps when importing each other's public keys.

**Step 1**. **Select** and **open** the email containing your correspondent's public key. The attachment will appear similar to the following: ![](/sites/siabnext.ttc.io/files/media/thunderbird_87.png)

**Step 2**. **Click** on the attached file above ![](/sites/siabnext.ttc.io/files/media/thunderbird_87a.png). **Enigmail** detects a message containing a public key and it will prompt you to import the key as follows:

![](/sites/siabnext.ttc.io/files/media/thunderbird_88.png)

*Figure 26: The Enigmail Confirm Import public key* 

**Step 3**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_89.png) to import your correspondent's public key.

If you have successfully imported the public key, a message resembling the following will appear:

![](/sites/siabnext.ttc.io/files/media/thunderbird_90.png)

*Figure 27: The Enigmail Alert screen displays the correspondent's public key*

To confirm that you have successfully imported your correspondent's public key, perform the following step:

**Step 1**. **Select Enigmail > Key Management** to display the *Enigmail Key Management* screen as follows:

![](/sites/siabnext.ttc.io/files/media/thunderbird_91.png)

*Figure 28: The Enigmail - Key Management displaying a recently imported public key* 

**Note** that option *Display All Keys by Default* needs to be selected to be able to see the keys.

## 4.4 Validate and Sign a Key Pair

Finally, you must verify that the imported key truly belongs to the person who purportedly sent it, then confirm its 'validity'. This is an important step that both you and your email contacts should follow for each public key that you receive. 

### 4.4.1 Validate a Key Pair

**Step 1**. **Contact** your correspondent through some means of communication other than email. You can use a telephone, text messages, **Voice over Internet Protocol** (**VoIP**) or any other method, but
you **must** be absolutely certain that you are really talking to the right person. As a result, voice or video conversations and face-to-face meetings work best, if they are convenient and if they can be arranged safely. 

**Step 2**. Both you and your correspondent should verify the 'fingerprints' of the public keys that you have exchanged. A fingerprint is a unique series of numbers and letters that identifies each key. You can use the **Enigmail** *Key Management* screen to view the fingerprint of key pairs you have created and public keys you have imported. 

To view the fingerprint of a particular key pair, perform the following steps:

**Step 1**. **Select Enigmail > Key Management** and then **right-click** on a particular key to activate the pop-up menu: 

![](/sites/siabnext.ttc.io/files/media/thunderbird_92.png) 

*Figure 29: The Enigmail Key Management menu with the Key Properties item selected*

**Step 2**. **Select** the *Key Properties* item to activate the following screen: 

![](/sites/siabnext.ttc.io/files/media/thunderbird_93.png)

*Figure 30: The Key Properties screen*

Your correspondent should repeat these steps. To confirm fingerprints, read fingerprint of your key to your contact and have them verify that the fingerprint they see on your public key they received matches. Then have your contact do the same for their key's fingerprint. If fingerprints don't match, exchange public keys again and repeat the validation process.

**Note**: The fingerprint itself is not a secret and can be recorded for later verification at your convenience.


### 4.4.2 Sign a Valid Public Key

After you have verified given correspondent's key, you can *sign* it, to confirm that you consider this key valid.
Signing keys may expose a connection between you and your corespondent when you send signed key to somebody else or export it to the key server. To prevent this from happening always select option *Local signature* below.

To sign a properly validated public key, perform the following steps:

**Step 1**. **Select Enigmail > Key Management** to open the *Key Management* screen.

**Step 2**. **Right-click** your correspondent's public key from the *Key Management* screen (see figure 29 above) and **select** the *Sign Key* item from the menu to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/thunderbird_94.png)

*Figure 31: The Enigmail - Sign Key screen*

**Step 3**. **Check** the *I have done very careful checking* option, **select** *Local signature (cannot be exported)*, and then **click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_35.png) to sign your correspondent's public key. You may be asked to provide password to your private key. 


### 4.4.3 How to Manage Your Key Pairs 

The *Enigmail Key Management* window is used to generate, validate and sign different key pairs. However, you may also perform other tasks by related to key management among them (see figure 29 above): 

- **Manage User IDs** lets you associate more than one email address to a single key pair.
- **Change Expiration Date** lets you change expiration date of your key pair.
- **Change Passphrase** lets you change the password protecting your key pair.
- **Generate & Save Revocation Certificate** lets you generate a new revocation certificate, if you have lost or misplaced the one you created earlier. 


## 4.5 Encrypt and Decrypt Email Messages

**Important**: The header of any email message - that is its *Subject* and intended recipients including any information in the *To*, *CC* and *BCC* fields - *cannot* be encrypted and will be sent in open text. To ensure the privacy and security of your email exchanges, the subject of your email should be kept non-descriptive not to reveal sensitive information. In addition, you are advised to put all addresses in the *BCC* field when sending emails to a group of people.

When encrypting email messages with attachments, we strongly recommend using the **PGP/MIME** option, as this will extend encryption to include any files and file names attached to your email.

Note that any encrypted email you send with Thunderbird/Enigmail/GnuPG is automatically encrypted to your key along with the chosen recipients of this email, so you are able to decrypt emails in your sent folder.

### 4.5.1 Encrypt a Message

Once both you and your correspondent have successfully imported and validated and signed each other's public keys, you are ready to begin sending encrypted messages and decrypting received ones.

To encrypt the contents of you email message to your correspondent, perform the following steps:

**Step 1**. **Open** **Thunderbird** and **click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_81.png) to write an email.

**Step 2**. To Encrypt the message **click** *Enigmail -> Message will not be encrypted* and **select** *Force Encryption* as shown in the follow screen:

![](/sites/siabnext.ttc.io/files/media/thunderbird_84.png) 

*Figure 33: The Force Encryption option*

**Step 3**. To Sign the message **click** *Enigmail -> Message will not be signed* and **select** *Force Sign*.

**Note**: To verify that your message will be both encrypted and signed, check that the following two icons appear **highlighted** at the bottom right corner of the message pane as follows:

![](/sites/siabnext.ttc.io/files/media/thunderbird_85.png) 

*Figure 34: Encryption and Signed enabled*

**Step 4**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_83.png) to send the message. You may be prompted for password to use your private key to sign the message.

**Optional step 5**. If you are attaching any file to your message, you may need to **select** the option *Encrypt/sign message as a whole and send it using PGP/MIME* and **click** OK button, in the following screen: 

 ![](/sites/siabnext.ttc.io/files/media/thunderbird_86.png) 

*Figure 35:  The Enigmail Prompt screen*

**Note: When you *encrypt each attachment separately* (second option in the figure 35 above) names of the attached files are not encrypted and are being send in clear text! This may result in leaking sensitive information! Using PGP/MIME ensures that all email text, attached files and their names are encrypted and hidden.**

### 4.5.2 Decrypt a Message

When you receive and open an encrypted message, **Enigmail/OpenPGP** will automatically attempt to decrypt the message when you receive and open it. 
If it does not, select the *Decrypt* button.
This will activate the following screen:

![](/sites/siabnext.ttc.io/files/media/thunderbird_96.png)

*Figure 36: The Enigmail Prompt - Please type in your OpenPGP passphrase or your SmartCard PIN*

**Step 1**. **Enter** your passphrase as shown above.

After you have entered your private key passphrase, the message is decrypted and displayed as follows:

![](/sites/siabnext.ttc.io/files/media/thunderbird_97.png)

*Figure 37: The newly decrypted message in the message pane.*

You have now successfully decrypted this message. By repeating the steps described in section **4.5 How to Encrypt and Decrypt Email Messages** every time you and your correspondent exchange messages, you can maintain a private, authenticated channel of communication, regardless of who might be attempting to monitor your email exchanges.

### 4.5.3 Extending Security Options

When using *Enigmail and GnuPG* to secure your privacy it is very important to ensure that **every** email you send is encrypted. This particularly includes replies to encrypted emails, drafts of email you would like to encrypt and quotes from previously encrypted emails. 

**Always enable message encryption (as in the section *4.5.1 How to Encrypt a Message* above) before you start writing it**. In this way you ensure that drafts of the message will only be written to the email server in encrypted form.

We also strongly recommend to **configure Enigmail to alert you before sending an unencrypted email**. The steps below show how to do this:

**Step 1**. **Click** *Enigmail > Preferences* menu and **select** the *Sending* tab.

**Step 2**. **Select** from the *Confirm before sending* - *If unencrypted*  and click OK.

![](/sites/siabnext.ttc.io/files/media/thunderbird_99.png)

*Figure 38: Enigmail Preferences - Confirm before sending*

For every unencrypted email you send now you will be alerted that the email will be send unencrypted as shown below. If you intend to send the email encrypted, **click** *Cancel* and follow steps in section 4.5.1 above.
 
![](/sites/siabnext.ttc.io/files/media/thunderbird_98.png)

*Figure 39: Enigmail Confirm*

**Note again that** the *Subject, To, CC* and *BCC* fields are **never** encrypted.

# 5. Portable Thunderbird





## 5.0 Differences between the Installed and Portable Versions of Thunderbird

The essential benefit of using **Portable Thunderbird** is that you may store local copies of your emails on the removable drive or USB memory stick. In addition to this, both the **Portable Thunderbird** program itself, as well as all local copies of your emails, can be concealed within a **TrueCrypt** encrypted volume. As such, you improve the security of your emails and conceal your email accounts and addresses you use. However, keep in mind that your external device or USB memory stick, and portable tools are only as safe as the computer you are using, and may risk being exposed to adware, malware, spyware and viruses.

**Note**: To maintain the privacy and your security of your email communications, you are strongly recommended to download and extract **GnuPG Portable** as outlined at the end of this page.


## 5.1 Download and Extract Portable Thunderbird

**Step 1**. **Click** [**http://portableapps.com/apps/internet/Thunderbird_portable**](http://portableapps.com/apps/internet/Thunderbird_portable) to be directed to the appropriate download site.

**Step 2**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_diff_01.png) to activate the **Source Forge** download site.

**Step 3**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_diff_02.png) to save the ![](/sites/siabnext.ttc.io/files/media/thunderbird_diff_03.png) installation file to your computer; and then **navigate** to it.

**Step 4**. **Double click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_diff_03.png); the *Open File - Security Warning* dialog box may appear. If it does, **click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_diff_04.png) to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/thunderbird_diff_05.png)

*Figure 1: The Mozilla Thunderbird, Portable Edition | Portableapps.com Installer window*

**Step 5**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_diff_06.png) to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/thunderbird_diff_07.png)

*Figure 2: The Choose Install Location window*

**Step 6**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_diff_08.png) to activate the *Browse for Folders* window as follows:

![](/sites/siabnext.ttc.io/files/media/thunderbird_diff_09.png)

*Figure 3: The Browse for Folder window*

**Step 7**. **Navigate** to your destination external drive or USB memory stick, as shown in *Figure 3* above, then **click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_diff_10.png) to confirm the location of the **Mozilla Thunderbird, Portable Edition** file, and return to the *Choose Install Location* window. 

**Step 8**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_diff_11.png) to activate the *Installing* window and begin extracting the **Mozilla Thunderbird, Portable Edition** file, and then **click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_diff_12.png) to complete the extraction process.

**Step 9**. **Navigate** to the removable drive or USB memory stick which the **Mozilla Thunderbird, Portable Edition** file was saved.

**Step 10**. **Double click** to open your removable device or USB memory stick, and it should resemble the following:

![](/sites/siabnext.ttc.io/files/media/thunderbird_diff_13.png)

*Figure 4: The newly installed Mozilla Thunderbird Portable Edition displaying the Thunderbird Portable folder*


## 5.2 Download and Extract Portable GPG for Thunderbird

**Step 1**. **Click** [**http://portableapps.com/support/thunderbird_portable#encryption**](http://portableapps.com/support/thunderbird_portable#encryption) to be directed to the download site.

**Step 2**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_diff_17.png) to activate the *GPG_for_Thunderbird_Portable_1.4.16.paf.exe* download window, and then **click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_diff_02.png) to save the ![](/sites/siabnext.ttc.io/files/media/thunderbird_diff_18.png) installation file; and then **navigate** to it.

**Step 3**. **Double click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_diff_18.png); the *Open File - Security Warning* dialog box may appear. If it does, **click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_diff_04.png) to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/thunderbird_diff_19.png)

*Figure 6: The Installer Language window*

**Step 4**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_diff_10.png) to activate the **GPG for Thunderbird | Portable Apps Installer** window, and then **click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_diff_06.png) to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/thunderbird_diff_20.png)

*Figure 7: The Choose Install Location window*

**Step 5**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_diff_08.png) to activate the *Browse for Folder* window as follows:

![](/sites/siabnext.ttc.io/files/media/thunderbird_diff_21.png)

*Figure 8: The Browse for Folder window*

**Step 6**. **Browse** to the same folder where you save **Portable Thunderbird** to, and **click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_diff_10.png) to return to the *Choose Install Location* window (*Figure 7*) and then ![](/sites/siabnext.ttc.io/files/media/thunderbird_diff_11.png) to begin extracting **Portable GnuPG**, and then **click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_diff_12.png) after the extraction process has been completed.

## 5.3 Download and Install Enigmail

**Enigmail** is a **Mozilla Thunderbird** add-on that lets you protect the privacy of your email communication. **Enigmail** is  simply an interface that lets you use **GnuPG** encryption program from within **Thunderbird**.  The **Engimail** interface is shown in the **Thunderbird** console tool bar. 

**Step 1**. **Click** [**https://www.enigmail.net/download/**](https://www.enigmail.net/download/) to be directed to the download site.

**Step 2**. **Select** *What is your operating system?* (e.g. *Windows*) and *What email client do you use?* (e.g. *Thunderbird 31*) and **click** on link *Download Enigmail x.x.x* (e.g. *Download Enigmail 1.7.2*) to activate the *enigmail-1.7.2-tb-win.xpi* download window, and then **click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_diff_25.png) to save ![](/sites/siabnext.ttc.io/files/media/thunderbird_diff_26.png) to your computer.

**Step 3**. **Open** the **Thunderbird Portable** folder, and then **double click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_diff_14.png) to open **Thunderbird Portable**.

**Step 4**. **Click** on ![](/sites/siabnext.ttc.io/files/media/thunderbird_diff_27.png) to display the *Thunderbird Menu* and **select Add-ons**  in the **Thunderbird Portable** main console as follows:

![](/sites/siabnext.ttc.io/files/media/thunderbird_diff_28.png)

*Figure 10: The Thunderbird Portable main console with the Add-ons item selected*

This will activate the following screen:

![](/sites/siabnext.ttc.io/files/media/thunderbird_diff_29.png)

*Figure 11: The Thunderbird Portable Add-ons window*

**Step 5**. If the Enigmail Add-on appears in the main *Extensions* panel **click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_diff_30.png). If it does not appear, **click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_diff_31.png) and  **select** *Install Add-on from File* as shown below: 

![](/sites/siabnext.ttc.io/files/media/thunderbird_diff_32.png)

*Figure 12: Tools for All Add-ons menu*

**Step 6**. Navigate to folder where you have saved the **Enigmail** add-on (most probably your *Downloads* folder) and **select** the add-on file.

**Step 7**.  **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_diff_33.png) at the *Software Installations* folder.

**Step 8**. **Click** ![](/sites/siabnext.ttc.io/files/media/thunderbird_diff_34.png) to complete the **Enigmail** installation, and restart **Thunderbird Portable**.

After you have successfully completed all above steps, please refer to the [**Thunderbird**](../thunderbird/windows) chapter to begin registering your email accounts and configuring it for use.

# 6. Torbirdy - adding digital anonymity and circumvention to Thunderbird

![](/sites/siabnext.ttc.io/files/media/torbirdy_01.png)

**TorBirdy** is an Add-on for Thunderbird that can be used to send and receive emails via the Tor network, thus protect your communication with the email server you use, increase the anonymity of your messages and potentially circumvent censorship. **TorBirdy** is a great addition to **Enigmail and GnuPG** encryption.

You can [download TorBirdy](https://addons.mozilla.org/en-us/thunderbird/addon/torbirdy/) from Mozilla Thunderbird Add-ons server. 

The following components are required to be started and configured on your computer to use the TorBirdy:

- Thunderbird (please refer to [**Thunderbird with Enigmail and GPG - Secure Email Client**](../thunderbird/windows) chapter);
- Tor Browser (please refer to [**Tor Browser - Digital Anonymity and Circumvention**](../torbrowser/windows) chapter).

It should be noted that TorBirdy is still considered in development and testing. There are other alternatives methods available that can be used to protect the communication between Thunderbird and your email server such as VPN or SSH proxy - please refer to the chaapter on [**How to remain anonymous and bypass censorship on the Internet**](../anonymity-and-circumvention).

## 6.1 How to Install TorBirdy for Thunderbird

After you [download  **TorBirdy**](https://addons.mozilla.org/en-us/thunderbird/addon/torbirdy/) to your computer, begin installing **TorBirdy** by performing the following steps: 

 **Step 1**. **Open Thunderbird**, then **click** ![](/sites/siabnext.ttc.io/files/media/torbirdy_03.png) to display the *Thunderbird Menu* and **select Add-ons** to activate the *Add-ons Manager* window.

**Step 2**. **Click** ![](/sites/siabnext.ttc.io/files/media/torbirdy_04.png) in the left hand sidebar.

**Step 3**. **Click** ![](/sites/siabnext.ttc.io/files/media/torbirdy_05.png) and  **select** *Install Add-on from File* as shown below: 

![](/sites/siabnext.ttc.io/files/media/torbirdy_06.png)

*Figure 1: Tools for All Add-ons menu*

**Step 4**. Navigate to the folder where you have saved the TorBirdy add-on (most probably your *Downloads* folder) as shown in the following screen:

![](/sites/siabnext.ttc.io/files/media/torbirdy_07.png)

*Figure 2: The Select an extension to install*

**Step 5**.  **Click** ![](/sites/siabnext.ttc.io/files/media/torbirdy_08.png) to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/torbirdy_09.png)

*Figure 3: The Software Installation window*

**Important**: Before you perform the next step make sure all your emails have been sent or saved! 

**Step 6**. **Click** ![](/sites/siabnext.ttc.io/files/media/torbirdy_10.png) and then **click** ![](/sites/siabnext.ttc.io/files/media/torbirdy_11.png) to restart Thunderbird program and complete the **TorBirdy** add-on installation.



## 6.2 How to Use TorBirdy in Thunderbird

Before you can use **TorBirdy** with **Thunderbird**, you must ensure that **Tor Browser** is running and is successfully connected to the **Tor network**. If you have not set up the **Tor Browser** yet please refer to [**Tor Browser - Digital Anonymity and Circumvention**](../torbrowser/windows) before proceeding further.

### 6.2.1 Enable TorBirdy for Thunderbird

Follow the steps below to launch the *Tor Browser* and run Thunderbird via the *Tor* network.
 
**Step 1**: **Navigate** to the *Tor Browser* folder, and then **double click** ![](/sites/siabnext.ttc.io/files/media/torbirdy_18.png) to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/torbirdy_19.png)

*Figure 8: The Tor Status window*

*Note: it is recommended to close any Firefox windows you have opened before launching the Tor Browser*.

A few moments later, the **Tor Browser** will open a new browser window displaying the following:

![](/sites/siabnext.ttc.io/files/media/torbirdy_20.png)

*Figure 9: Tor Browser; successfully connected to the Tor network*

You are now connected to the *Tor network* through *Tor Browser*.

**Step 2**: **Launch** Thunderbird and enter your password at the prompt. The status of TorBirdy will be shown in the right hand corner of the Thunderbird window as highlighted below.


 ![](/sites/siabnext.ttc.io/files/media/torbirdy_30.png)  

*Figure 10: The TorBirdy Enabled for Tor*


### 6.2.2 Confirm TorBirdy is connecting using Tor

Follow the steps below to test and confirm the TorBirdy settings.

**Step 1**: **Click** on ![](/sites/siabnext.ttc.io/files/media/torbirdy_21.png) to activate the following menu: 

![](/sites/siabnext.ttc.io/files/media/torbirdy_22.png)

*Figure 11: The TorBirdy Preferences Menu*

**Step 2**: **Select** *Open TorBirdy Preferences* to open the window below. **Click** ![](/sites/siabnext.ttc.io/files/media/torbirdy_23.png) to the *TorBirdy Advanced Settings* warning message:

![](/sites/siabnext.ttc.io/files/media/torbirdy_25.png)

*Figure 12: The TorBirdy Preferences window*

**Step 3**: **Click** on ![](/sites/siabnext.ttc.io/files/media/torbirdy_24.png). If you have connected successfully through the *Tor* network, you will see the following message (*IP addresses will change*).

![](/sites/siabnext.ttc.io/files/media/torbirdy_26.png)

*Figure 13: Are You Using Tor? window*

**Note** If you have not started the Tor Browser or Tor Browser did not connect to Tor Network as shown in section 6.2.1 above, you will not be able to connect to your email server and you may see the following message after you start Thunderbird:

![](/sites/siabnext.ttc.io/files/media/torbirdy_27.png)

*Figure 14: Connection Refused window*

It is worth noting that some email providers such as Google Mail may refuse a connection to the email server via the *Tor network*.

## 6.3 Disable TorBirdy for ThunderbirdS

You can disable the TorBirdy Add-on if you wish to run Thunderbird without TorBirdy by following steps below:

**Step 1**. **Open Thunderbird**, then **click** ![](/sites/siabnext.ttc.io/files/media/torbirdy_03.png) to display the *Thunderbird Menu* and **select Add-ons** to activate the *Add-ons Manager* window.

**Step 2**. **Click** ![](/sites/siabnext.ttc.io/files/media/torbirdy_04.png) in the left hand sidebar.

**Step 3**: **Click** on ![](/sites/siabnext.ttc.io/files/media/torbirdy_29.png) on the screen below: 

![](/sites/siabnext.ttc.io/files/media/torbirdy_28.png)

*Figure 15: Disable TorBirdy Extension*

**Step 4**: **Click** ![](/sites/siabnext.ttc.io/files/media/torbirdy_11.png) to restart Thunderbird and conclude disabling TorBirdy.

# FAQ

***Q***: *What happens if I just install **Enigmail** and not **GnuPG**?*

***A***: That's simple, really. **Enigmail** just won't work. After all, it's the **GnuPG** software that provides the encryption engine that **Enigmail** uses.

***Q***: *How many email accounts can I set up in **Thunderbird**?*

***A***: As many as you like! **Thunderbird** is an email manager and can easily handle 20 or more email accounts!

***Q***: *My friend has a **Gmail** account. Should I convince him to install **Thunderbird**, **Enigmail** and **GnuPG**?*

***A***: That would be ideal. Just make sure he configures all of his security settings in exactly the same way as you did. Then the two of you will have an extremely effective way of communicating in privacy and safety!

***Q***: *Remind me one more time, which parts of an email message does **Enigmail** encrypt?*

***A***: **Enigmail** encrypts the content of the message. It doesn't encrypt the subject line of the message, your email address or the name you chose to associate with that email account. So, if you're trying to send a confidential message, make sure the subject line doesn't give you away! And, if you want to stay anonymous, avoid displaying or even using your real name when you create your email account.

***Q***: *I still don't understand the purpose of digitally signing my messages.*

***A***: A digital signature proves that you're the real sender of a particular message and that the message hasn't been tampered with on its way to your intended recipient. Think of it as the electronic equivalent of the wax seal on an envelope, which contains a very important letter.
