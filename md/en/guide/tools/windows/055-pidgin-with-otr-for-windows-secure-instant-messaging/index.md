

---

lang: en
community: guide
type: tools
os: windows
weight: 055
title: Pidgin with OTR for Windows - secure instant messaging

---

**Pidgin** is a free and open source client that lets you organize and manage your different **Instant Messaging (IM)** accounts using a single interface. The **Off-the-Record (OTR)** plug-in designed for use with **Pidgin** ensures authenticated and secure communications between **Pidgin** users.

# Required reading


:[](../../../tactics/secure communication)


:[](pidgin-with-otr-for-windows-secure-instant-messaging)

# What you will get from this guide

- The ability to organize and manage some of the most popular instant messaging services through a single program.
- The ability to have private and authenticated chat sessions.

# 1. Introduction to Pidgin and OTR





## 1.0 Other tools like Pidgin and OTR

**GNU Linux, Mac OS and other Microsoft Windows Compatible Programs:**

**Note:** We recommend [**Jitsi**](../jitsi/windows) as a replacement for **Pidgin**. As well as being able to use **Jitsi** for secure text chat (including with Pidgin users), you can also use it to have secure voice and video communications with other **Jitsi** users. **Jitsi** is available for **Microsoft Windows**, **GNU/Linux**, **Mac OS** and more.

Both **Pidgin** and **OTR** are available for **Microsoft Windows** and for **GNU/Linux**. Another multi-protocol **IM** program for **Microsoft Windows** that supports **OTR** is [**Miranda IM**](http://www.miranda-im.org/). For the **Mac OS** you can use [**Adium**](http://adium.im/), a multi-protocol **IM** program that supports the **OTR** plugin.


## 1.1 Things you should know about Pidgin and OTR before you start

Before you can start using **Pidgin** you must have an existing **IM** account, after which you will register that account to **Pidgin**. For instance, if you have an **Google Account**, you can use their **IM** service **GoogleTalk** with **Pidgin**. The log-in details of your existing **IM** account are used to register and access your account through **Pidgin**. 

**Note**: All users are encouraged to learn as much as possible about the privacy and security policies of their **Instant Messaging account provider**. 

**Pidgin** supports the following **IM** services: [**AIM**](http://dashboard.aim.com/aim), [**Bonjour**](http://www.apple.com/support/bonjour/), [**Gadu-Gadu**](http://komunikator.gadu-gadu.pl/), [**Google Talk**](http://www.google.com/talk/), **Groupwise**, [**ICQ**](http://www.icq.com), **IRC**, [**MSN**](http://www.msn.com/), [**MXit**](http://www.mxit.com/), [**MySpaceIM**](http://www.myspace.com/guide/im), [**SILC**](http://silcnet.org/), **SIMPLE**, [**Sametime**](http://www.ibm.com/developerworks/downloads/ls/lst/), [**Yahoo!**](http://messenger.yahoo.com/), **Zephyr** and any **IM** clients running the **XMPP** messaging protocol.

**Pidgin** does not permit communication between different **IM** services. For instance, if you are using **Pidgin** to access your **Google Talk** account, you will not be able to chat with a friend using an **ICQ** account. 

However, **Pidgin** can be configured to manage multiple accounts based on any of the supported messaging protocols. That is, you may simultaneously use both **Gmail** and **ICQ** accounts, and chat with correspondents using *either* of those specific services (which are supported by **Pidgin**). 

**Off-the-Record** (**OTR**) messaging is a plugin developed specifically for **Pidgin**. It offers the following privacy and security features: 

- **Authentication**: You are assured the correspondent is who you think it is.
- **Deniability**: After the chat session is finished, messages cannot be identified as originating from either your correspondent or you.
- **Encryption**: No one else can access and read your instant messages.
- **Perfect Forward Security**: If third party obtains your private keys, no previous conversations are compromised.

**Note**: **Pidgin** must be installed before the **OTR** plugin.


# 2. Install and Configure Pidgin and OTR

Both **Pidgin** and its associated **Off-the-Record** (**OTR**) automated encryption and authentication plugin must be installed properly for either program to work. Fortunately, the installation process for both the programs is easy and quick.

<a name="2.1"></a>

## 2.1 Install Pidgin

**Step 1**. **Double click** ![](/sites/siabnext.ttc.io/files/media/pidgin-win-01.png); the *Open File - Security Warning* dialog box may appear. If it does, **click** ![](/sites/siabnext.ttc.io/files/media/pidgin-win-02.png) to display the following screen:

![](/sites/siabnext.ttc.io/files/media/pidgin-win-03.png) 

*Figure 1: The Install Language confirmation box*

**Step 2**. **Click** ![](/sites/siabnext.ttc.io/files/media/pidgin-win-04.png) to display the *Welcome to the Pidgin 2.10.9 Setup Wizard* screen.  

**Step 3**. **Click** ![](/sites/siabnext.ttc.io/files/media/pidgin-win-05.png) to display the *License Agreement* screen; after you have read the *License Agreement*, **click** ![](/sites/siabnext.ttc.io/files/media/pidgin-win-05.png) to display the *Pidgin 2.10.9 Setup - Choose Components* window.

**Step 4**. **Click** ![](/sites/siabnext.ttc.io/files/media/pidgin-win-05.png) to display the *Pidgin 2.10.9 Setup - Choose Install Location* window. 

**Step 5**. **Click** ![](/sites/siabnext.ttc.io/files/media/pidgin-win-06.png) to accept the default installation path, and display the *Pidgin 2.10.9 Setup - Installing* window to begin installing the **Pidgin** software.

*A number of folders and files will begin installing themselves in rapid succession; after the installation process has been completed, the Pidgin 2.10.9 Setup - Installation Complete window will appear.*

**Step 6**. **Click** ![](/sites/siabnext.ttc.io/files/media/pidgin-win-05.png) to display the *Completing the Pidgin 2.10.9 Setup Wizard*.

**Note**: During **Step 3** of the installation process, **Pidgin** was configured to be included in the **Start > All Programs** list, and can be launched from there in the future. 

**Step 7**. **Click** ![](/sites/siabnext.ttc.io/files/media/pidgin-win-08.png) to complete installing **Pidgin**.

<a name="2.2"></a>

## 2.2 Install the Off-The-Record (OTR) Plugin

**Step 1**. **Double click** ![](/sites/siabnext.ttc.io/files/media/pidgin-win-09.png); the *Open File - Security Warning* dialog box may appear. If it does, **click** ![](/sites/siabnext.ttc.io/files/media/pidgin-win-02.png) to display the following screen:

![](/sites/siabnext.ttc.io/files/media/pidgin-win-10.png)

*Figure 2: The Welcome to the pidgin-otr 4.0.0-1 Setup Wizard* 

**Step 3**. **Click** ![](/sites/siabnext.ttc.io/files/media/pidgin-win-05.png) to display the *License Agreement* screen; after you have completed reading the *License Agreement*, **click** ![](/sites/siabnext.ttc.io/files/media/pidgin-win-11.png) to display the *pidgin-otr 4.0.0-1 Setup - Choose Install Location* screen.  

**Step 4**. **Click** ![](/sites/siabnext.ttc.io/files/media/pidgin-win-06.png) to begin the installation process.

**Step 5**. **Click** ![](/sites/siabnext.ttc.io/files/media/pidgin-win-08.png) to complete installing the **Pidgin-OTR** messaging software plugin.

After you have completed installing both **Pidgin** and **OTR**. The following icon will appear in the Windows task bar when Pidgin is started from the **Start > All Programs** list:

![](/sites/siabnext.ttc.io/files/media/pidgin-win-12.png)

*Figure 3: The Pidgin-OTR icon outlined in black*

Congratulations! You have successfully completed installing both the **Pidgin** and **OTR** programs!



<a name="2.3"></a>

## 2.3 Overview of Account Registration and Setup Process

There are four basic steps in the **Pidgin** account registration and setup process; registering an existing **IM** account to **Pidgin**, adding a correspondent or *buddy*, getting your buddy to do the same, and lastly accessing the chat window for your first chat session.

Given that chat or **IM** sessions take place between two parties, the examples on this page describe how the various forms and windows appear to *both* buddies/correspondents (represented by two fictional characters, Salima and Terence) at different stages of the account registration and set up process. All examples are based on the **Riseup.net** IM service.

**Note**: Before you can start using **Pidgin**, you must already have an **Instant Messaging** (**IM**) account with one of the providers listed in *Figure 6* below. If you would like to create an **IM** account, we recommend using **Riseup** email account which can be later used for [XMPP communication](https://help.riseup.net/en/chat). Please refer to chapter [**RiseUp - Secure Email Service**](../riseup/internet) for information and instructions on how to create a **Riseup** account. You can also use XMPP account providers listed in the [How to Add Accounts in Jitsi](../jitsi/windows#1499) section, like: [Jit.si](https://jitsi.org/Register/Register) or a Google Account.


## 2.4 Register Your Instant Messaging Account with Pidgin

To register your **IM** account to **Pidgin**, perform the following steps:

**Step 1**. **Click** ![](/sites/siabnext.ttc.io/files/media/pidgin-win-13.png) or **select Start > All Programs > Pidgin** to launch **Pidgin**. The first time you use **Pidgin**, the following screen will appear:

![](/sites/siabnext.ttc.io/files/media/pidgin-win-14.png)

*Figure 4: The Accounts confirmation window*

**Step 2**. **Click** ![](/sites/siabnext.ttc.io/files/media/pidgin-win-15.png) to display a blank *Add Account* window as follows: 

![](/sites/siabnext.ttc.io/files/media/pidgin-win-16.png) 

*Figure 5: The Add Account screen displaying Basic, Advanced and Proxy tabs*

**Step 3**. **Click** the *Protocol* drop-down list to view the **IM** service protocols supported by **Pidgin** as follows: 

![](/sites/siabnext.ttc.io/files/media/pidgin-win-17.png) 

*Figure 6: The Add Account window displaying a list of supported IM protocols*

**Step 4**. **Select** the appropriate **IM** protocol.

**Note**: Different **IM** service providers will display their specific text fields for you to fill in. Some of them are automatically partly filled in. However, all services require that you to enter a username and a password.

**Step 5**. **Type** in your email address (for example, [**terencethetester@riseup.net**](mailto:terencethetester@riseup.net)) in the *Username* field. 

**Step 6**. **Type** in your password for this specific account in the *Password* field. 

**Step 7**. **Type** a nickname you would like to be identified by in the *Local Alias* field. (This field is optional.) 

**Important**: To optimise your privacy and security, do *not* enable the *Remember password* option. It means that **Pidgin** will prompt you for your password whenever you log in to chat on-line. Doing this prevents imposters from logging in and pretending to be you, if you happen leave your computer unattended for some time. Also, remember to **select** the *Quit* item from the *Buddies* drop-down menu after finishing your chat session! 

A completed *Add Account* screen would resemble the following:

![](/sites/siabnext.ttc.io/files/media/pidgin-win-18.png) 

*Figure 7: An example of a completed Add Account form*
 
**Step 8**. **Click** ![](/sites/siabnext.ttc.io/files/media/pidgin-win-19.png) to complete adding your account, and simultaneously display an updated *Accounts* the *Buddy List* screens as follows:

![](/sites/siabnext.ttc.io/files/media/pidgin-win-20.png)      ![](/sites/siabnext.ttc.io/files/media/pidgin-win-21.png)

*Figure 8: An updated Accounts window;*   *Figure 9: The Buddy List in Active mode*

After completing these steps, you are now ready to register your **Pidgin** buddies, by entering their contact information. 

<a name="2.5"></a>

## 2.5 Add a Buddy in Pidgin

Adding buddies or correspondents in **Pidgin** involves adding and saving their contact information. In the example that follows, Terence will add Salima as his buddy.

To add a buddy to your **IM** account in **Pidgin**, perform the following steps:

**Step 1**. **Click** *Buddies* to display its corresponding menu, and then **select** the *+ Add Buddy...* item as follows: 

![](/sites/siabnext.ttc.io/files/media/pidgin-win-22.png)

*Figure 10: The Buddy List menu with the "Add Buddy..." item selected*

This will display the following screen: 

![](/sites/siabnext.ttc.io/files/media/pidgin-win-23.png)

*Figure 11: The Add Buddy window*

**Step 2**. If you have multiple accounts, **select** the account that corresponds to the same messaging service as your 'buddy'.  

**Note**: Both your buddy and yourself *must* be using the *same* messaging service, even if he/she is not using **Pidgin**. You cannot add an **ICQ** or **MSN** buddy to a **Google Talk** account. However, you can register and use multiple accounts based on these supported protocols in **Pidgin**. Whereby you may chat with one buddy using your **XMPP** account and with another using your **ICQ** or **MSN** accounts. 

**Step 3**. **Type** in your buddy's email address in the *Username* field.  

The following step is optional.

**Step 4**. **Type** in an *Alias* or nickname for your buddy in the *(Optional) Alias* field, so that your *Add Buddy* form resembles the following screen: 

![](/sites/siabnext.ttc.io/files/media/pidgin-win-24.png)

*Figure 12: An example of a completed Add Buddy form*

**Step 5**. **Click** ![](/sites/siabnext.ttc.io/files/media/pidgin-win-19.png) to add your buddy.

**Note**: This will send a message to your buddy requesting approval or authorisation of your request, and will appear for your correspondent *Buddy List* as follows:  

![](/sites/siabnext.ttc.io/files/media/pidgin-win-25.png)

*Figure 13: The Authorize buddy request as it appears on Salima's Buddy List*

At this point, your buddy must perform the following step:

**Step 6**. **Click** ![](/sites/siabnext.ttc.io/files/media/pidgin-win-26.png) to add this person as your buddy and display her/him in your *Buddy List* as follows:

![](/sites/siabnext.ttc.io/files/media/pidgin-win-27.png)

*Figure 14: Terence's Buddy List displaying Salima as his buddy*

**Note**: In the example above, Salima's *Alias* or nickname is displayed, adding yet another level of identity protection. 

![](/sites/siabnext.ttc.io/files/media/pidgin-win-30.png)

*Figure 15: Terence's Buddy List window displaying Salima's as his newly created buddy*

After you have added, authorised and confirmed your **Pidgin** chat buddy, he/she must now do the same with your **IM** contact information by repeating **steps 1 through 6** from their own account.

<a name="2.6"></a>

## 2.6 Open an IM window in Pidgin

To open an **IM** chat window in **Pidgin**, perform the following steps:

**Step 1**. **Right click** your buddy's name in the *Buddy List* to display a pop-up menu listing all the tasks you can perform as follows: 

![](/sites/siabnext.ttc.io/files/media/pidgin-win-31.png) 

*Figure 16: The Buddy tasks menu*

**Step 2**. **Select** the *IM* item from the pop-up menu to activate a typical chat window as follows: 

![](/sites/siabnext.ttc.io/files/media/pidgin-win-32.png) 

*Figure 17: A typical chat window in Pidgin*

Now you are almost ready to chat with your buddy using **Pidgin**. First, however, you must configure the **OTR** encryption to ensure that your chat sessions will be private and secure. Seen next page for this.

<a name="2.7"></a>

## 2.7 Re-enable an Account in Pidgin

From time to time, you might find that your IM account has disabled itself in **Pidgin**; perhaps because **Pidgin** program was improperly closed due to Internet connection being interrupted, or your computer frozen. Fortunately, **Pidgin** offers a way to re-enable your account. To do this, perform the following steps:

**Step 1**. **Click** ![](/sites/siabnext.ttc.io/files/media/pidgin-win-13.png) or **select Start > Pidgin** to launch **Pidgin**.

**Step 2**. **Open** the *Accounts* menu, and then **select** the *Manage Accounts* item as follows: 

![](/sites/siabnext.ttc.io/files/media/pidgin-win-33.png)

*Figure 18: The Accounts menu with the *Manage Accounts item selected (re-sized)*

*This will open the following screen:*

![](/sites/siabnext.ttc.io/files/media/pidgin-win-34.png)

*Figure 19: The Accounts window (re-sized) displaying a disabled account*

**Step 3**. **Click** the check box next to your account to activate the **Pidgin** password prompt as follows:   

![](/sites/siabnext.ttc.io/files/media/pidgin-win-35.png)

*Figure 20: The Pidgin password prompt dialog box*

**Step 4**. **Type** in your password so your own **Pidgin** password prompt dialog box resembles the following:

![](/sites/siabnext.ttc.io/files/media/pidgin-win-36.png)

*Figure 21: The Pidgin password prompt dialog box with the Enter password field completed*

**Step 5**. **Click** ![](/sites/siabnext.ttc.io/files/media/pidgin-win-37.png) to complete re-enabling your account as follows:

![](/sites/siabnext.ttc.io/files/media/pidgin-win-38.png)

*Figure 22: An example of a successfully re-enabled account*

**Step 6**. **Click** ![](/sites/siabnext.ttc.io/files/media/pidgin-win-39.png) to close the *Accounts* window.


# 3. Use OTR for Secure Instant Messaging with Pidgin

Both your correspondent and yourself must configure the **OTR** plugin before you can enable private and secure **Instant Messaging** (**IM**) sessions. **OTR** plugin will automatically detect when both parties have installed and properly configured the **OTR** plugin.

**Note**: If you request a private conversation with a friend who has neither installed nor configured **OTR**, it will automatically send a message explaining how they can obtain the **OTR** plugin. 

<a name="3.1"></a>

## 3.1 Configure the Pidgin-OTR Plugin

To enable the **OTR** plugin, perform the following steps: 

**Step 1**. **Double click** ![](/sites/siabnext.ttc.io/files/media/pidgin-win-13.png) or **select** **Start > All Programs > Pidgin** to launch **Pidgin** and activate the *Buddy List* window (please refer to *Figure 1*).

**Step 2**. **Open** the *Tools* menu, and then **select** the *Plugins* item as follows: 

![](/sites/siabnext.ttc.io/files/media/pidgin-win-40.png)

*Figure 1: The Buddy List window with the Plugins item selected from the Tools menu*

This will activate the *Plugins* window as follows:

**Step 2**. **Scroll** down to the *Off-the-Record Messaging* option, then **click** its associated check box to enable it. 

![](/sites/siabnext.ttc.io/files/media/pidgin-win-41.png)

*Figure 2: The Pidgin Plugins window with Off-the-Record Messaging selected*

**Step 3**. **Click** ![](/sites/siabnext.ttc.io/files/media/pidgin-win-42.png) to begin configuring the *Off-the-Record Messaging* windows.

Basically, there are 3 steps involved in configuring **OTR** properly to effectively enable private and secure **IM** sessions and they are explained below: 

- **The First Step**: This involves generating a unique private key associated with your account, and displaying its fingerprint.

The next two steps involve securing the **IM** session and authenticating your buddies.

- **The Second Step**: This involves one party requesting a private and secure messaging session with another party currently on-line. 

- The **The Third Step** involves *authenticating* or verifying the identity of your **Pidgin** *buddy*. (**Note**: In **Pidgin**, a buddy is anyone you correspond with during **IM** sessions.) This process of verifying a buddy's identity is referred to as *authentication* in **Pidgin**. This means establishing that your buddy is *exactly* the person who he/she is claims to be.   

<a name="3.2"></a>

## 3.2 Generate a Private Key and Display its Fingerprint

Secure chat sessions in **Pidgin** are enabled by generating a *private key* for the relevant account. The *Off-the-Record* configuration window is divided into the *Config* and the *Known fingerprints* tabs. The *Config* tab is used to generate a *key* for each of your accounts and to set specific **OTR** options. The *Known fingerprints* tab contains a list of fingerprints of the keys of your contacts. You must possess a key for any buddy with whom you wish to chat privately. 

![](/sites/siabnext.ttc.io/files/media/pidgin-win-43.png)

*Figure 3: The Off-the-Record Messaging screen displaying the Config tab*

**Step 1**. To optimise your privacy, **check** the *Enable private messaging*, *Automatically initiate private messaging* and *Don't log OTR conversations* options in the *Config tab* as shown in *Figure 3* above. 

**Step 2**. **Click** ![](/sites/siabnext.ttc.io/files/media/pidgin-win-44.png) to begin generating your secure key; a screen notifying you that a private key is being generated appears as follows:

![](/sites/siabnext.ttc.io/files/media/pidgin-win-45.png)

*Figure 4: The Generating private key confirmation box*

**Note**: Your buddy must perform the same steps for his/her own account. 

**Step 3**. **Click** ![](/sites/siabnext.ttc.io/files/media/pidgin-win-37.png) after the private key (which resembles the following), has been generated: 

![](/sites/siabnext.ttc.io/files/media/pidgin-win-46.png)

*Figure 5: An example of a fingerprint of the key generated by the OTR engine*

**Important**: You have now created a private key for your account on your computer. This will be used to encrypt your conversations so that nobody else can read them, even if they do manage to monitor your chat sessions. The fingerprint is a long sequence of letters and numbers used to identify the key for a particular account, as shown in *Figure 5* above. 

**Pidgin** automatically saves your fingerprint, and those of your buddies, on the computer you are using, so that you will not have to remember them. If you reinstall **Pidgin** or if you change to another computer you will either have to regenerate your key and re-authenticate your buddies, or you will need to move your key and fingerprints of your buddies to the new computer. To do this you will need to copy content of %APPDATA%\\.purple folder (~/.purple on Linux or Mac) to similar folder on new computer.

<a name="3.3"></a>

## 3.3 Authenticate a Private Conversation

**Step 1**. **Double-click** the account of a buddy who is currently on-line to begin a new **IM** conversation. If both of you have the **OTR** plugin installed and properly configured, you will notice that a new **OTR** button appears at the bottom right corner of your chat window. 

![](/sites/siabnext.ttc.io/files/media/pidgin-win-47.png)

*Figure 6: A Pidgin messaging window displaying the OTR icon outlined in black*

**Step 2**. **Click** ![](/sites/siabnext.ttc.io/files/media/pidgin-win-48.png) to activate its associated pop-up menu, and then **select** the *Start private conversation* item as follows: 

![](/sites/siabnext.ttc.io/files/media/pidgin-win-49.png)

*Figure 7: The pop-up menu with the Start private conversation item selected*

*Your **Pidgin IM** window will then resemble the following screen:*

![](/sites/siabnext.ttc.io/files/media/pidgin-win-50.png)

*Figure 8: The Pidgin IM window displaying the Unverified button*

**Note**: **Pidgin** automatically begin communicating with your buddy's **IM** program, and generating messages whenever you attempt to enable a private and secure chat session. As a result of this, the ![](/sites/siabnext.ttc.io/files/media/pidgin-win-48.png) **OTR** button changes to ![](/sites/siabnext.ttc.io/files/media/pidgin-win-51a.png), indicating that you are now able to have an encrypted conversation with your buddy. 

**Warning**! Although this conversation is now secure, the identity of your buddy has not been *verified* yet. Beware: Your buddy might actually be someone else *pretending* to be your buddy. 

<a name="3.4"></a>

## 3.4 Authenticate the Identity of Your Pidgin Buddy

You may use one of three methods of identification to authenticate your **Pidgin** buddy; you could use any one of the following options:

1) A pre-arranged secret code phrase or word; 
2) Pose a question, the answer to which is only known to both of you; 
3) Manually verify the fingerprints of your key using a different method of communication.

### The Secret Code Phrase or Word Method ###

You can arrange a code phrase or word in advance, either by meeting each other in person or by using another communications medium (like a telephone, voice chat by [**Jitsi**](../jitsi/windows) or a mobile phone text message). Once you both type in the same code phrase or word, your session will be authenticated. 

**Note**: The **OTR** secret code word recognition feature is case sensitive, that is, it can determine the difference between capital (A,B,C) letters and lower case (a,b,c) ones. Bear this in mind when inventing a secret code phrase or word!

**Step 1** . **Click** the *OTR* button in the chat window, then **select** the *Authenticate Buddy* item as follows: 

![](/sites/siabnext.ttc.io/files/media/pidgin-win-52.png)

*Figure 9: The Unverified pop-up menu with the Authenticate buddy item selected*

This will activate the *Authenticate Buddy* window, prompting you to select an authentication method. 

**Step 2**. **Click** ![](/sites/siabnext.ttc.io/files/media/pidgin-win-53.png) and **select** *Shared Secret* as follows: 

![](/sites/siabnext.ttc.io/files/media/pidgin-win-54.png)

*Figure 10: The Authenticate buddy screen with the drop-down list revealed* 

**Step 3**. **Enter** the secret code word or phrase as follows:

![](/sites/siabnext.ttc.io/files/media/pidgin-win-55.png)

*Figure 11: The Shared Secret screen* 

**Step 4**. **Click** ![](/sites/siabnext.ttc.io/files/media/pidgin-win-56.png) to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/pidgin-win-58.png)

*Figure 12: The Authenticate Buddy window for a fictitious correspondent*

**Note**: *At this time your buddy will see window shown on figure 13 at his/her end and will have to enter the same code word. If they match, your session will be
authenticated.*

![](/sites/siabnext.ttc.io/files/media/pidgin-win-57.png)

*Figure 13: The Authenticate Buddy window for a fictitious correspondent*

Once the session is authenticated, the *OTR* button will change to ![](/sites/siabnext.ttc.io/files/media/pidgin-win-51.png). Your session is now secure and you can be sure that you are really speaking with your buddy.

### The Question and Answer Method ###

Another method of authenticating each other, is the question and answer method. Create a question and an answer to it. After reading the question, your buddy must type in the *exact* answer, and if their answer matches yours, your identity will be automatically authenticated. 

**Step 1**. **Click** the *OTR* menu in active message window to activate its associated pop-up menu, and then **select** *Authenticate Buddy* item (please refer to *Figure 9*).

![](/sites/siabnext.ttc.io/files/media/pidgin-win-50.png)

*Figure 14: A Pidgin chat window displaying the OTR icon*

An *Authenticate Buddy* window will pop up prompting you to choose the method for authentication. 

**Step 2**. **Click** the drop-down menu and **select** the *Question and Answer* item as follows:  

![](/sites/siabnext.ttc.io/files/media/pidgin-win-60.png)

*Figure 15: The Authenticate buddy screen*

**Step 3**. **Enter** a question and its corresponding answer. This question will be sent to your buddy. 

![](/sites/siabnext.ttc.io/files/media/pidgin-win-61.png)

*Figure 16: The Questions and Answer screen*

If your buddy's answer matches yours, then your identities will have been mutually authenticated or verified, and both parties are who they claim to be! 

Once the session has been authenticated, the *OTR* button will change to ![](/sites/siabnext.ttc.io/files/media/pidgin-win-51.png). Your session will now be secure and you can be certain of your chat buddy's identity.

### Manual fingerprint verification ###

The third method of authenticating each other, is the fingerprint verification. In this method you need to exchange displayed fingerprints (see figure 17 below) for your buddy and yourself over another communication channel (like secure email or voice call). If exchanged fingerprints are the same you can select ***I have** verified that this is in fact the correct fingerprint* and  **Authenticate** the session.

![](/sites/siabnext.ttc.io/files/media/pidgin-win-79.png)

*Figure 17: The Manual fingerprint verification screen*

Notice that when you **Select > Buddy List > Tools > Plugins > Off The Record Messaging > Configure Plugin**, the *Known fingerprints* tab now displays your buddy's account, and a message that their identity has been verified. 

![](/sites/siabnext.ttc.io/files/media/pidgin-win-62.png)

*Figure 18: The Off-the-Record Messaging screen displaying the Known Fingerprints tab*

Congratulations! You may now chat privately. The next time you and your buddy chat (using the same computers), you should only have to request a secure connection (as on figure 7 above) and have your buddy accept it. Your session should already be authenticated.

# 4. Portable Pidgin and OTR for Windows





## 4.1 Differences between the Installed and Portable Versions of Pidgin

Given that portable tools are *not* installed on a local computer, their existence and use will remain undetected. However, keep in mind that your external device or USB memory stick and portable tools are only as safe as the computer you are using, and may risk being exposed to adware, malware, spyware and viruses. 

There are no other differences between **Portable Pidgin** and the version designed to be installed on a local computer.


## 4.2 Download and Extract Portable Pidgin

To begin downloading and extracting **Portable Pidgin**, perform the following steps:

**Step 1**. **Click** [**http://portableapps.com/apps/internet/pidgin_portable**](http://portableapps.com/apps/internet/pidgin_portable) to be directed to the appropriate download site.

**Step 2**. **Click** ![](/sites/siabnext.ttc.io/files/media/pidginportable-win-01.png) to activate its associated **Source Forge** download page.

**Step 3**. **Click** ![](/sites/siabnext.ttc.io/files/media/pidginportable-win-02.png) to save the ![](/sites/siabnext.ttc.io/files/media/pidginportable-win-03.png) installation file to your computer; then **navigate** to it.

**Step 4**. **Double click** ![](/sites/siabnext.ttc.io/files/media/pidginportable-win-03.png); the *Open File - Security Warning* dialog box may appear. If it does, **click** ![](/sites/siabnext.ttc.io/files/media/pidginportable-win-04.png) to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/pidginportable-win-05.png)

*Figure 1: The Language Installer window*

**Step 5**. **Click** ![](/sites/siabnext.ttc.io/files/media/pidginportable-win-06.png) to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/pidginportable-win-07.png)

*Figure 2: The Pidgin Portable | PortableApps.com window*

**Step 6**. **Click** ![](/sites/siabnext.ttc.io/files/media/pidginportable-win-08.png) to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/pidginportable-win-09.png)

*Figure 3: The Choose Components window*

**Note**: **Click** to enable the ![](/sites/siabnext.ttc.io/files/media/pidginportable-win-10.png) option, and include multilingual support if you would prefer to use **Portable Pidgin** in a language other than English. Enabling this option will make the extraction process a little bit longer. 

**Step 7**. **Click** ![](/sites/siabnext.ttc.io/files/media/pidginportable-win-08.png) to activate the *Choose Install Location* window, and then **click** ![](/sites/siabnext.ttc.io/files/media/pidginportable-win-11.png) to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/pidginportable-win-12.png)

*Figure 4: The Browse for Folder window*

**Step 8**. **Navigate** to the destination external hard drive or USB memory stick, **select** it and then **click** ![](/sites/siabnext.ttc.io/files/media/pidginportable-win-13.png) to confirm its location, and to return to the *Choose Install Location* window. 

**Step 9**. **Click** ![](/sites/siabnext.ttc.io/files/media/pidginportable-win-14.png) to begin extracting **Portable Pidgin** to the specified folder; then **click** ![](/sites/siabnext.ttc.io/files/media/pidginportable-win-15.png) to complete the installation process.

**Step 10**. **Navigate** to your destination external drive or USB memory stick, as shown in *Figure 5* below, and then **open** it to confirm that the **Portable Pidgin** program was successfully extracted.

![](/sites/siabnext.ttc.io/files/media/pidginportable-win-16.png)

*Figure 5: The Browse for Folder window*

Before you may begin using **Portable Pidgin** in a safe and secure manner, you must first download and extract its complementary portable **Off-the-Record** (**OTR**) plugin. 


## 4.3 Download and Extract Portable Pidgin OTR

**Step 1**. **Click** [**http://sourceforge.net/projects/portableapps/files/Pidgin-OTR%20Portable/Pidgin-OTR%20Portable%203.2%20Rev%202/**](http://sourceforge.net/projects/portableapps/files/Pidgin-OTR%20Portable/Pidgin-OTR%20Portable%203.2%20Rev%202/) to be directed to the appropriate download site.

**Step 2**. **Click** ![](/sites/siabnext.ttc.io/files/media/pidginportable-win-17.png) to activate the *Pidgin-OTR_Portable_3.2_Rev_2.paf.exe* download window, and then **click** ![](/sites/siabnext.ttc.io/files/media/pidginportable-win-02.png) to save the 
![](/sites/siabnext.ttc.io/files/media/pidginportable-win-18.png) installation file to your computer.

**Step 3**. **Double click** ![](/sites/siabnext.ttc.io/files/media/pidginportable-win-18.png) to *Open File - Security Warning* dialog box may appear. If it does, **click** ![](/sites/siabnext.ttc.io/files/media/pidginportable-win-04.png) to activate the *Installer Language* window (please refer to *Figure 1*).

**Step 4**. **Click** ![](/sites/siabnext.ttc.io/files/media/pidginportable-win-06.png) to activate the *Pidgin-OTR Portable | PortableApps.com* window (please refer to *Figure 2* to which it resembles).

**Step 5**. **Click** ![](/sites/siabnext.ttc.io/files/media/pidginportable-win-08.png) to activate the *Choose Install Location* window (please refer to *Figure 3* above to which it resembles).

**Step 6**. **Click** ![](/sites/siabnext.ttc.io/files/media/pidginportable-win-11.png) to activate its associated *Browse for Folder* window (please refer to *Figure 4* above). 

**Step 7**. **Navigate** to the destination external hard drive or USB memory stick, **select** it and then **click** ![](/sites/siabnext.ttc.io/files/media/pidginportable-win-13.png) to confirm its location, and to return to the *Choose Install Location* window.

**Step 8**. **Click** ![](/sites/siabnext.ttc.io/files/media/pidginportable-win-14.png) to begin extracting **Portable Pidgin** to the specified folder; **click** ![](/sites/siabnext.ttc.io/files/media/pidginportable-win-15.png) to complete the installation process.

**Step 9**. **Navigate** to your destination external drive or USB memory stick, as shown in *Figure 5* above, and then **open** the **Portable Pidgin** program folder.

**Step 10**. **Double click** ![](/sites/siabnext.ttc.io/files/media/pidginportable-win-19.png) to launch **Portable Pidgin**.

Please refer to the [**Pidgin**](../pidgin/windows) guide to begin configuring and using it.

# FAQ

***Q***: Can I use Pidgin-OTR to chat with friends in both MSN and Yahoo? 

***A***: Although **Pidgin-OTR** supports a number of chat and messaging services, most of the time you have to use the same provider to initiate an **IM** session with your buddy. You both need to use an **IRC** or a **ICQ** account for example. However, services that use **XMPP** protocol (like **RiseUp**, **Google Talk**, **Facebook**, or other **XMPP** servers) may allow chatting between their accounts. Therefore you can chat between account on **RiseUp** and **Google Talk**. Also note that in **Pidgin** you can register and be on-line with several **IM** accounts simultaneously. That's the beauty of using a multi-protocol **IM** client.

***Q***: How may I access my Pidgin-OTR account on another computer?

***A***: One way is to generate a new private key to use with your **IM** account on that computer. You can start a conversation with your buddy using this new key, but you will need to authenticate your session again. Another option is to copy the encryption keys to the new computer (you can find them in %APPDATA%\\.purple on Windows and ~/.purple on Linux or Mac).

***Q***: What if I forget the login password for my IM account? Or what if someone steals it? Will they have access to my past and future conversations?

***A***: This is very important question. First of all, if you forget your password and you will not be able to reset it using options offered by the account provider, you will have to generate a new **IM** account. After that, you must inform your buddy about your new account using secure and authenticated email or voice-chat where you can recognise each other. 

Furthermore, you must authenticate each other as buddies. If someone has somehow obtained your **IM** password, that person could attempt to impersonate you when using **Pidgin**. Fortunately, he/she won't be able to authenticate the session without having your encryption keys or knowing your shared code word. As such, your buddy may become suspicious. That's why authentication is **so** important. 

Finally, if you followed the instructions above and set the recommended preferences in the **OTR** 'Config' tab, then even someone who steals your password or have access to your computer won't have access to your past conversations, since you chose not to record them.