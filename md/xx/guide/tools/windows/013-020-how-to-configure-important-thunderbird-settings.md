

---

lang: xx
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Configure Important Thunderbird Settings

---

List of sections on this page:

- [**3.0 How to Improve Usability**](#3.0)
- [**3.1 How to Disable the HTML Feature**](#3.1)
- [**3.2 How to Configure the Privacy Options**](#3.2)
- [**3.3 How to Configure the Security Tabs**](#3.2)
- [**3.4 How to Enable the Account Settings Junk Mail Filter**](#3.3)

<a name="3.0"></a>
## 3.0 How to Improve Usability ##

When you first run **Thunderbird**, a pop-up bar on the bottom will ask you if you want to report information about your use of **Thunderbird** to Mozilla. You can select **No**
  
![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-050.png)

To more easily find menu items, you can enable the **Menu Bar** to **right-clicking** by the top of **Thunderbird** and enabling it

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-029.png)

Most of us want to receive email sent to us as soon as possible. Let us check for new messages every minute, rather than every 10 minutes as is the **Thunderbird** default.

**Step 1**. **Select Tools > Account Settings** in **Thunderbird** to and select *Server Settings* under your email account.

**Step 2**. Change **Check for new messages every "10" minutes to "1" minute.

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-035.png)

We recommended disabling the *Global Search and Indexer* feature in **Thunderbird* to optimize its performance. Depending on the quantity and size of your emails, it may reduce the speed of your system, by continuously and unnecessarily over-writing of information to your hard drive. 

To turn off the *Global Search and Indexer* option, perform the following steps: 

**Step 1**. **Select Tools > Options** in **Thunderbird** to activate the *Options* window.

**Step 2**. **Click** **Advanced** to activate its associated tab and disable the *Enable Global Search and Indexer*:

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-029.png)

<a name="3.1"></a>
## 3.1 How to Disable HTML Features ##

**Thunderbird** lets you use **HyperText Markup Language** (**HTML**) to compose and read messages. This lets you receive and send messages that include colours, fonts, images and other formatting features. However, **HTML** is the same language used for Web pages; viewing messages with **HTML** formatting may expose you to malicious content in emails.
 
To disable the **HTML** formatting feature, perform the following step: 

**Step 1**. **Click** ![](/sbox/screen/thunderbird-en-1/24a.png) to display the *Thunderbird Menu* and **select Options> View > Message Body As > Plain Text** as follows: 

![](/sbox/screen/thunderbird-en-1/25.png)

*Figure 1: The View menu displaying the Message Body submenu with the Plain Text option selected*

You can also change the default options so that emails you write are in Plain Text and not HTML. 

**Step 1**. **Click** ![](/sbox/screen/thunderbird-en-1/24a.png) to display the *Thunderbird Menu* and **select Options> Account Settings** and *Composition & Addressing* under your email address: 

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-056.png)

*Figure 2: The Composition & Addressing screen with *Compose messages in HTML format unchecked*

<a name="3.2"></a>
### 3.2 How to Configure the Privacy Options ###

Make sure to disable the ability of cookies and remote content to track your email reading habits:

**Step 1**. **Select Tools > Options** in **Thunderbird** to activate the *Options* window.

**Step 2**. **Click** **Privacy** to activate its associated tab and disable any selected options:

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-035.png)

*Figure 2: The Privacy Options windows with all options unchecked*

<a name="3.3"></a>
### 3.3 How to Configure the Security Tabs ###

### The Junk tab ###

**Thunderbird** has two built-in junk mail filters that can help you determine which of your incoming messages are spam. By default, these filters are disabled, so you must enable them for use. Even after they have been enabled, you will continue to receive junk mail, but **Thunderbird** will automatically sort them into the *Junk* folder. 

Email scams - also referred to as *phishing* emails - usually attempt to make you click on a link that is embedded in the email. Frequently, these links direct your browser to a web site that will attempt to infect your computer with a virus. In other cases, the link will take you to a web site that appears to be legitimate, to deceive you into entering a valid user name and password, which can then be used or sold by the entity or people for commercial or malicious purposes. **Thunderbird** can help to identify and warn you about emails like this.

The first set of assorted junk mail and security controls are accessed through the *Options - Security* window through which the majority of these privacy and security options are configured. To access them, perform the following steps:

**Step 1**. **Select Menu > Options** to activate the *Options* window.

**Step 2**. **Click** ![](/sbox/screen/thunderbird-en-1/26.png) to activate the following screen:

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-036.png)

*Figure 2: The Security window displaying its associated tabs*

### The Email Scams tab ###

**Step 1**. **Check** the *Tell me if the message I'm reading is a suspected email scam* option to enable **Thunderbird** to analyse messages for email scams as follows: 

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-037.png)

*Figure 3: The Email Scams tab* 

### The Anti-Virus tab ###

**Step 1**. **Click** the *Anti-Virus* tab to activate the following screen: 

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-036.png)

*Figure 4: The Anti-Virus tab* 

This option lets your anti-virus software scan and isolate individual messages as they arrive. Without this setting enabled, it is possible that your *entire* *Inbox* folder could be 'quarantined' if you receive an infected message.

**Note**: This assumes that you have a functioning anti-virus program installed. Please refer to [**Avast**](/en/avast_main) for more information on how to install and configure anti-virus software.

### The Passwords tab ###

**Step 2**. **Click** the *Passwords* tab to activate the following screen: 

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-039.png)

*Figure 5: The Passwords tab*

**Important:** We strongly recommend to keep your passwords private and secure using a software designed precisely for this purpose; please refer to [**KeyPass**](/en/keepass_main) for more information. 

**Note**: The options in the *Password* tab will only work if you checked the *Remember password* option in the first *Mail Account Setup* screen when you registered your email accounts with **Thunderbird**. If you have two-factor authentication enabled on your email account, you should use this feature.

**Step 1**. **Click** ![](/sbox/screen/thunderbird-en-1/31.png) to activate the following screen:

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-051.png)

*Figure 6: The Saved Passwords window*

The *Saved Passwords* window lets you remove or view all the corresponding passwords for each of your accounts. If you save passwords within **Thunderbird** you should set a *Master Password* to protect access to your email accounts and make all of your account passwords inaccessible to anyone else familiar with the **Thunderbird** password options.

**Step 3**. **Check** the *Use a master password* option as shown in *figure 7* to enable the *Change Master Password...* button.

**Step 4**. **Click** ![](/sbox/screen/thunderbird-en-1/33.png) to activate the following screen:

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-040.png)

*Figure 7: Change Master Password window*

**Step 5**. **Type** in an appropriately strong password that only you will remember, and then **click** ![](/sbox/screen/thunderbird-en-1/35.png) to confirm it as your *Master Password*. 

<a name="3.4"></a>
### 3.4 How to Enable the Account Settings Junk Mail Filter ###

The second type of **Thunderbird** junk mail filter is available through the *Account Settings - Junks Settings* window. By default, these filters are disabled, so they must be enabled if you wish to use them. Whenever junk emails arrive **Thunderbird** will automatically sort them into the *Junk* folders associated with different accounts. 

**Step 1**. **Select Tools > Account Settings** to activate the *Account Settings* window.

**Step 2**. **Select** the *Junk Settings* option associated with a specific **Gmail** or **RiseUp** account in the sidebar. 

**Step 3**. **Enable** the *Junk Settings* options so that your own *Account Settings - Junk Settings* screen resembles the following: 

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-114.png)

*Figure 11: The Account Settings - Junk Settings window*

**Step 4**. **Click** ![](/sbox/screen/thunderbird-en-1/35.png) to complete the configuration of the *Account Settings* window.

**Note**: The *Junk Settings* options must be configured separately for each account. As such, junk mail for a **Gmail** or a **RiseUp** account will be placed in its corresponding *Deleted* folder. Alternatively, you may designate a *Local Folder* to receive junk mail from all your accounts. 

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-055.png)

*Figure 12: The Account Settings - Junk Settings window, displaying the settings for a central junk folder*

**Step 1**. **Select** the *Junk Settings* option directly beneath *Local Folders* in the sidebar.

**Step 2**. **Select** the *Local Folders* item from the *"Junk" folder on:* drop-down list as displayed in *figure 13*.

**Step 3**. **Click** ![](/sbox/screen/thunderbird-en-1/35.png) to complete the configuration of the *Account Settings* window.

Now that you have successfully configured the assorted security options and junk mail settings in **Thunderbird**, please proceed to the following section, [**How to Use Enigmail with GnuPG in Thunderbird**](/en/thuderbird_encryption). 


