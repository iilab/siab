

---

lang: en
community: guide
type: tools
os: linux
weight: 065
title: Thunderbird, Enigmail and OpenPGP for Linux - Secure Email

---

**Mozilla Thunderbird** is free and open source software that allows you to exchange and store email for multiple accounts with multiple service providers. **Enigmail** and **GnuPG** improve the security and privacy of your email correspondence by adding support for end-to-end encryption to **Thunderbird**. They also allow you to sign your messages digitally and verify the digital signatures of others.

# Required reading


{{ required_reading: ../../secure communication }}


{{ required_reading: ../../secure file storage }}


{{ tool: ./065-tool.md }}

# What you will get from this guide

- The ability to manage different email accounts through a single program
- The ability to read and compose messages after disconnecting from the Internet
- The ability to authenticate (through digital signing), encrypt and decrypt emails

# 1. Introduction to Thunderbird

**Thunderbird** is a cross-platform, free and open source email client for receiving, sending and storing emails. An email client is a computer application that lets you download and manage your emails without a browser, as well as manage multiple email accounts at once. You need to have an existing email account before using Thunderbird. Most Linux distributions come with Thunderbird installed by default.
 
**Gnu Privacy Guard (GPG)** is free and open source software capable of encrypting, decrypting and digitally signing messages and files. It also generates and manages the public and private key pairs that are used for encryption and decryption. 

**Enigmail** is a Thunderbird add-on that allows you to access the authentication and encryption features provided by GnuPG (which must be installed for Enigmail to work). 

## 1.1. Other tools like Thunderbird

Thunderbird is an email client available for GNU Linux and other operating systems. Managing multiple email accounts is a complex task from a digital security point of view. Therefore, we strongly recommend that you use Thunderbird for this purpose. The security advantages available in Thunderbird, a cross-platform free and open source program, are even more important when compared to its commercial equivalents like Microsoft Outlook. However, if you would prefer to use a program other than Mozilla Thunderbird, we recommend the following free and open source alternatives:

* [**Claws Mail**](http://www.claws-mail.org/): available for GNU Linux and Microsoft Windows;
* [**Sylpheed**](http://sylpheed.sraoss.jp/en/): available for for GNU Linux, Mac OS and Microsoft Windows;
* [**Alpine**](http://www.washington.edu/alpine/): available for GNU Linux, Mac OS and Microsoft Windows.

# 2. How to set-up Thunderbird

Most Linux distributions (including Ubuntu 14.04, which is used for this guide) come with Thunderbird installed by default. If you're using Ubuntu, search for Thunderbird in your system's dashboard and open it. Once you've opened Thunderbird, you can start to set it up and to add your email accounts, as described in the sections below.

## 2.1. How to add email accounts to Thunderbird

As soon as you open Thunderbird, the following window should appear:

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-201.png)

You can add your (existing) email account to Thunderbird through the following steps:

**Step 1:** Click on “**Skip this and use my existing email**”.
 
**Step 2:** Fill in your name, email address and password in the corresponding text fields of the following window:

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-202.png)

**Step 3:** Click on the check box to disable the “**Remember password**” option and subsequently click on “**Continue**”. The following window should appear:

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-203.png)

**Step 4:** Here you can select either “**IMAP**” or “**POP3**”, depending on how you want to store and receive emails.

**Internet Message Access Protocol (IMAP):** When using IMAP all your folders (including Inbox, Drafts, Templates, Sent, Trash and all other folders) reside on the email server. This allows you to access these folders from a different computer. All messages will reside on the server and initially, only the email messages headers or title bars (containing information like the date and time, message subject, name of sender, etc.) are downloaded for display on your computer. Full messages are downloaded when you open them. Thunderbird can also be configured to store copies of messages from all or some of the folders on your computer, so that you can work with them offline (that is, without using an Internet connection). In IMAP when you delete emails or folders, you do so on both your local computer and on the server.

**Post Office Protocol version 3 (POP3):** When using POP3 only the Inbox (a folder into which new incoming messages are delivered) resides on the server; all other folders are only located on your local computer. You can choose between leaving messages in the Inbox folder of the server after you have downloaded them to your computer, or you can delete them from the server. If you access your email account from a different computer, you will only be able to view messages in the Inbox folder (new messages, and old messages which you have not deleted). Note that depending on the server configuration copies of your sent emails might be stored on the server in Sent folder. It is worth checking this yourself.

**Step 5:** Once you have selected “**IMAP**” or “**POP3**”, click on “**Done**” to proceed. You should now see the following, confirming that your email account has successfully been imported in Thunderbird:

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-204.png)

To add another email account, simply click on **Local Folders > Accounts > Create a new account > Email** and follow the same steps as described above.
 
After you have successfully added your email accounts in Thunderbird, the next time you open the main user interface, you will be prompted to enter your password for each account as follows:

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-205.png)

You can now use multiple email accounts through Thunderbird. 

## 2.2. How to register blogs, news feeds and newsgroup accounts

To create and register an account for blogs, news feeds and newsgroups, perform the following steps:

**Step 1:** Through Thunderbird, click on **Local Folders > Accounts > Create a new account > Feeds**. The following window should appear:

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-206.png) 

**Step 2:** Click on “**Next**”. The following window should appear:

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-207.png)

**Step 3:** Click on “**Finish**” to complete the account set-up process. When you return to your Thunderbird console, you will see that “**Blogs & News Feeds**” have been added:

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-208.png)

# 3. Security options in Thunderbird

In the context of Thunderbird, security generally refers to protecting your computer from harmful or malicious emails. Some might just be spam, while others might contain spyware and viruses. This section explains how to configure several settings in Thunderbird to strengthen its ability to defend your system from attacks originating from emails. 

For more information on preventing harmful or malicious software, please refer to the [How-to Booklet chapter on Protecting your Computer from Viruses, Malware and Hackers](https://securityinabox.org/en/guide/malware) for more information.

## 3.1. How to disable the preview pane in Thunderbird

The Thunderbird main window is divided into three areas: The left sidebar displays the folders for your email accounts, the right side shows a list of messages, and the bottom pane displays a preview of a selected email message. 

The preview is automatically visible as soon as a message has been selected. However, if an email contains malicious code, the preview message pane could activate it. Therefore it is important to disable it.

To disable the preview pane, perform the following step:

**Step 1:** Click on Thunderbird's menu bar to display the Thunderbird Menu and select **Preferences > Layout > Massage Pane F8** to disable it as follows:

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-301.png)

The Message Pane has now disappeared and you need to double-click on an email message to read its content. If an email message looks suspicious (perhaps it has an unexpected or irrelevant subject title, or comes from an unknown sender), you can now choose to delete it without having to preview its content.

## 3.2. How to disable the HTML feature in Thunderbird

Thunderbird lets you use HyperText Markup Language (HTML) to compose and read messages. This lets you receive and send messages that include colours, fonts, images and other formatting features. However, HTML is the same language used for webpages and viewing messages with HTML formatting might expose you to malicious emails which pose some of the same kinds of threats posed by webpages.

To disable the HTML formatting feature, perform the following step:

**Step 1:** Click on Thunderbird's menu bar to display the Thunderbird Menu and select **View > Message Body As > Plain Text** as follows:

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-302.png)

## 3.3. How to configure privacy and security options

Thunderbird has two built-in junk mail filters that can help you determine which of your incoming messages are spam. By default, these filters are disabled, so you need to enable them for use. Even after they have been enabled, you will continue to receive junk mail, but Thunderbird will automatically sort them into the Junk folder.

Email scams - also referred to as phishing emails - usually attempt to make you click on a link that is embedded in the email. Frequently, these links direct your browser to a website that will attempt to infect your computer with a virus. In other cases, the link will take you to a website that appears to be legitimate, to deceive you into entering a valid user name and password, which can then be used or sold by the entity or people for commercial or malicious purposes. Thunderbird can help identify and warn you about emails like this. 

The first set of assorted junk mail and security controls can be found through the “**Thunderbird Preferences**” window through which you can configure most privacy and security settings. To access them, perform the following steps:

**Step 1:** Select **Edit > Preferences** through your Thunderbird menu bar to activate the “**Thunderbird Preferences**” window.

**Step 2:** Click  on “**Security**” to activate the following screen:

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-303.png)

**SECURITY OPTIONS**

**Junk tab**

Check the relevant options in the Junk tab to enable Thunderbird to delete email that you have determined to be junk mail, as illustrated below: 

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-304.png)

**E-mail Scams tab**

Check the “**Tell me if the message I'm reading is a suspected email scam**” option to enable Thunderbird to analyse messages for email scams as follows:

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-305.png)

**Anti-Virus tab**

Check the “**Allow anti-virus clients to quarantine individual incoming messages**” option as follows:

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-306.png)

This option lets your anti-virus software to scan and isolate individual messages as they arrive. Without this setting enabled, it is possible that your entire Inbox folder could be 'quarantined' if you receive an infected message.

**Note:** This assumes that you have a functioning anti-virus program installed. 

**Passwords tab**

The options in the Password tab will only work if you checked the “**Remember password**” option in the first “**Mail Account Setup**” screen when you added your email accounts to Thunderbird.

Through this tab you can view and remove all the corresponding passwords for each or your accounts, and/or you can set a Master Password to protect access to your email accounts. 

To view or remove your email account passwords that are stored on your computer, click on “**Saved Passwords**”:

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-307.png)

The following window should pop-up:

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-308.png)

You can click on the account for which you want to remove its stored password and subsequently click on “**Remove**”. If you would like to remove all the stored passwords for all your Thunderbird email accounts, click on “**Remove All**”. 

Alternatively, if you would like to use a Master Password to protect your stored passwords, perform the following steps:

**Step 1:** Click on “**Use a master password**” through the Passwords tab.

**Step 2:** Click on “**Change Master Password**” to activate the following screen:

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-309.png)

**Step 3:** Fill in a strong password and then click on “**OK**” to confirm it as your Master Password.
 
**PRIVACY OPTIONS**

Cookies – otherwise known as HTTP cookies – are computer files made of text that a website sends to your computer's hard drive when you visit a website. Companies like the information they store in cookies to your information so that they can personalize your experience when you visit a website. However, as a result of this, third parties are able to track your online activity. 

To enhance your privacy, it is recommended that you configure Thunderbird's privacy settings so as to limit the cookies that are stored on your computer. You can do this through the following steps:

**Step 1:** Click on “**Privacy**” in the “Thunderbird Preferences” window.

**Step 2:** Under the “**Web Content**” section, select “**From visited**” in terms of accepting third-party cookies, and “**I close Thunderbird**”, in terms of how long such cookies should be kept.

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-310.png)

## 3.4. How to enable the account settings junk mail filter

By default, Thunderbird's junk mail filters are disabled, so they need to be enabled if you want to use them. Whenever junk emails arrive Thunderbird will automatically sort them into the Junk folders associated with different accounts. You can do this through the following steps:

**Step 1:** Select **Edit > Account Settings** through your Thunderbird menu bar to activate the Account Settings window. 

**Step 2:** Select the “**Junk Settings**” option associated with a specific email account in the sidebar. 

**Step 3:** Enable the “**Junk Settings**” options as illustrated below: 

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-311.png)

**Step 4:** Click on “**OK**” to complete the configuration of the Account Settings window. 

**Note:** The Junk Settings options can be configured separately for each account. As such, junk mail for a Gmail or a RiseUp account will be placed in its corresponding Deleted folder. 

Alternatively, you can designate a Local Folder to receive junk mail from all your accounts. You can do this through the following steps:

**Step 1:** Select the “**Junk Settings**” option directly beneath “**Local Folders**” in the sidebar.

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-312.png)

**Step 2:** Click on “**Move new junk messages to**”, to determine the destination and retention of junk messages.

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-313.png)

**Step 3:** Select the “**Local Folders**” item from the “**Junk**” folder on: drop-down list as illustrated below:

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-314.png)

**Step 4:** Click on “**OK**” to complete the configuration of the Account Settings window.

# 4. How to encrypt and decrypt emails

**GNU Privacy Guard (GnuPG)** is free *cryptographic* software that was developed by the GNU Project. This software is compliant with the OpenPGP standard and was designed to inter-operate with Pretty Good Privacy (PGP), another email encryption program that was initially designed and developed by Phil Zimmermann. Enigmail is a Thunderbird add-on that lets you use the GnuPG encryption program from within Thunderbird.

This section explains how to use email encryption which is based on public-key cryptography. Each individual needs to generate his/her own personal pair of keys which can be used for signing, encrypting and decrypting emails. The first key is called the “**private key**”. It is protected by a password or passphrase, both to be guarded and never shared with anyone.
 
The second key is called the “**public key**”. This key can be shared with any of your correspondents. Once you have a correspondent’s public key you can begin sending encrypted emails to this person. Only he/she will be able to decrypt and read your emails, because he/she is the only person who has access to the matching private key. Similarly, if you send a copy of your own public key to your email contacts and keep the matching private key secret, only you will be able to read encrypted messages from those contacts.

Enigmail also lets you attach **digital signatures** to your messages. The recipient of your message who has a genuine copy of your public key will be able to verify that the email comes from you, and that its content was not tampered with on the way. Similarly, if you have a correspondent's public key, you can verify the digital signature on his/her signed messages.

## 4.1. How to install Enigmail

Most Linux distributions come with GnuPG installed by default. In Ubuntu, the core package required to start using GnuPG is called “**Passwords and Keys**” and can be viewed through the system's software center. 

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-401.png)

You now need to install the Enigmail add-on to Thunderbird so that you can start using GnuPG for email encryption. You can do this through the following steps:

**Step 1:** Select **Tools > Add-ons** through your Thunderbird menu bar. 

**Step 2:** Search for “**Enigmail**” in Thunderbird's Add-ons Manager.
 
![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-402.png)

**Step 3:** Click on “**Install**” to download Enigmail.
 
![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-403.png)

**Step 4:** Restart Thunderbird to install Enigmail.

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-404.png)

Now that you have restarted Thunderbird, you should see “**Enigmail**” included in the menu bar.

## 4.2. How to configure Enigmail and generate encryption keys

You can now configure one or more of your email accounts to use Enigmail to generate one or more pairs of encryption keys.

### 4.2.1. How to generate encryption keys

You can configure Enigmail and generate a pair of encryption keys through the following steps:

**Step 1:** Select **Enigmail > Setup Wizard** through your Thunderbird's menu bar.

**Step 2:** Click on “**Next**” to proceed with the standard configuration (as a beginner) through the following window:

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-405.png)

**Step 3:** Type your passphrase in the following fields to generate a pair of encryption keys for your email account: 

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-406.png)

**Note:** A **passphrase** is a password which protects your private key, which is used to sign, encrypt and decrypt emails and which should not be shared with anyone. As such, it is important to (a) create a strong passphrase and (b) make sure you don't forget or lose your passphrase. To learn how to generate strong passphrases, read more [**here**](https://securityinabox.org/en/guide/passwords).  

**Step 4:** Once you have entered your (strong) passphrase in the required fields, click on “**Next**” to generate your encryption keys.

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-407.png) 

**Step 5:** Wait for several minutes until your keys are generated.

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-408.png)

**Step 6:** Once your private key is generated, click on “**Create Revocation Certificate**” to create a revocation certificate which you can use to revoke your private key if you forget or lose it, or if it gets compromised. 

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-409.png)

**Step 7:** To create your revocation certificate, you will be asked to enter your private key passphrase for the first time and to save your newly created revocation certificate somewhere on your laptop. Once you have done this, click on “**OK**” in the following window to proceed: 

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-410.png)

**Note:** It is recommended that you save your revocation certificate somewhere secure (such as USB stick) to prevent third parties from potentially gaining access to it and revoking your private key. 

**Step 8:** You will now be back on the Enigmail Setup Wizard window. Click on “**Next**” to continue.

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-411.png) 

**Step 9:** You should now view the following window which confirms that Enigmail has successfully been set up and is ready to use. Click on “**Finish**” to start using Enigmail. 

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-412.png)

### 4.2.2. How to view and manage your key properties

Once you have generated your encryption keys, you can view and manage their properties through the following steps:

**Step 1:** Select **Enigmail > Key Management** through your Thunderbird menu bar. This will activate your Enigmail Key Management window:

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-413.png)

**Step 2:** Select **View > Key Properties** through your Enigmail Key Management window. The following window, displaying the properties of your keys, should appear:

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-414.png)

The Key Properties window displays, among other things, your public key ID and its fingerprint. For example, the **public key ID** for electra.stormborn@gmail.com is **0x2398A398**, while the associated **fingerprint** is **60BB F18B ECD8 305C 48DE A1F0 90D9 88CD 2398 A398**. This window also displays the expiration date of your keys (e.g. 26.11.2020).   

You are required to share your public key with your correspondents so that they are able to send encrypted emails to you. You can also share your key's fingerprint with your correspondents, so that they can validate that that key actually belongs to you. However, make sure to never share your private key (passphrase) with anyone, as that is used to encrypt and decrypt your emails. 

**Step 3:** The Key Properties window also displays the expiration date of your keys (e.g. 26.11.2020). If you would like to change the expiration date, select **Select action... > Change Expiration Date** and the following should appear:

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-415.png)

Through this window, you can change the expiration date of your keys. 

**Step 4:** If you would like to change the passphrase which protects your private key, select **Select action... > Change Passphrase**. You will be prompted to type in your current passphrase and to subsequently set a new one. It's highly recommended that you change your passphrases quite frequently so that you can reduce the probability of it getting compromised. 

**Step 5**: In the unfortunate event that your private key does get compromised or that you forget your passphrase, you can revoke your key by selecting **Select action... > Revoke Key**.

 Once the following window appears, click on “**Revoke Key**”:
  
![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-416.png)

### 4.2.3. How to generate additional encryption keys

It's a common practice to have a separate key pair for each email account. Using the same key pair for many email accounts is possible and does have some usability benefits. However, we don't recommend this practice, as having various email accounts linked to a single key pair makes it easier for third parties to map out all the people you are associated to through those accounts. As such, we recommend the creation of separate key pairs for each email account. 

Once you have added an additional email account to Thunderbird (as explained in previous sections), you can generate new keys for it through the following steps:

**Step 1:** Select **Enigmail > Key Management** through your Thunderbird's menu bar.
 
**Step 2:** Select **Generate > New Key Pair** through your Enigmail Key Management window.
 
**Step 3:** Select the different/additional email address you would like to generate a new key pair for (e.g. electra.stormborn@outlook.com) and type in a strong passphrase (twice) to protect your private key in the associated fields, as illustrated below:

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-417.png)

To learn how to generate strong passphrases, read more [**here**](https://securityinabox.org/en/guide/passwords). Through this window, you can also choose in how many years you would like your key to expire in.

**Step 4:** Once you have entered a strong passphrase, click on “**Generate key**” to generate a new key pair for your additional email address. 

**Step 5:** Click on “**Generate Key**” to confirm that you want to generate public and private keys for your other email address. 

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-418.png)

Wait for several minutes until your new key pair is generated. 

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-419.png)

**Step 6:** Once your keys are generated, click on “**Generate certificate**” to generate a revocation certificate (as previously explained). 

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-420.png) 

Then save your revocation certificate somewhere secure (e.g. USB stick) and type in your new passphrase for the first time. 

**Step 7:** Click on “**OK**” in the following window to proceed.

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-421.png)

**Step 8:** Through your Enigmail Key Management window, you can now see that your new key pair for your other email account has been created:

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-422.png)

### 4.2.4. How to configure Enigmail with your email account

To enable Enigmail for use with a specific email account, perform the following steps:

**Step 1:** Click on the icon which displays the Thunderbird Menu and select **Preferences > Account settings**, as illustrated below:

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-423.png)

**Step 2:** Select “**OpenPGP Security**” under your email account in the left side of the Account Settings window. Click on “**Use email address of this identity to identify OpenPGP**”, as illustrated below: 

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-424.png)

**Step 3:** Through this window you can also determine your default settings. For example, you can choose to sign all email messages by default, as illustrated below:

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-425.png)

**Step 4:** Click on “**OK**” to return to the Thunderbird console. 

## 4.3. How to exchange public keys

Before you can start sending encrypted email messages to one another, you and your correspondents need to exchange public keys. You also need to confirm the validity of any key you accept by confirming that it really belongs to its purported sender.

### 4.3.1. How to send a public key using Enigmail

To send a public key using Enigmail both you and your correspondent will need to perform the following steps:

**Step 1:** Open Thunderbird and click on “**Write**” to write an email.
 
**Step 2:** Select **Enigmail > Attach Public Key...**
 
**Step 3:** Select the email account you would like your public key to be attached for, as illustrated below:

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-426.png)

**Step 4:** Once you click on “**Send**”, you will notice that your public key has been attached to your email.

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-427.png) 

**Step 5:** Click on “**Send**” to send your email with your public key attached to it.

### 4.3.2. How to import a public key using Enigmail

Both you and your correspondent need to perform the following steps when importing each other's public keys:

**Step 1:** Right click on the attachment of your correspondent's public key, which would be attached at the end of the email and would look similar to the following:

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-428.png)

**Step 2:** Click on “**Import OpenPGP Key**”.

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-429.png) 

**Step 3:** Click on “**OK**” to import your correspondent's public key. 

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-430.png)

**Step 4:** To confirm that your correspondent's public key has successfully been imported, select **Enigmail > Key Management**. You should be able to view your correspondent's public key in your Enigmail Key Management window. 

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-431.png)

## 4.4. How to validate and sign a key pair

It's important to verify that the imported key actually belongs to the person who sent it and to confirm its 'validity'. This is a step that both you and your email contacts should follow for each public key that you receive.

### 4.4.1. How to validate a key pair

You can validate your correspondent's public key, contact him/her through some means of communication other than email. You can use a telephone, text messages, Voice over Internet Protocol (VoIP) or any other method, but you should be absolutely certain that you are really talking to the right person. As a result, voice or video conversations and face-to-face meetings work best, if they are convenient and if they can be arranged safely.

Both you and your correspondent should verify the 'fingerprints' of the public keys that you have exchanged. A fingerprint is a unique series of numbers and letters that identifies each key. You can use the Enigmail Key Management screen to view the fingerprint of key pairs you have created and public keys you have imported.

To view the fingerprint of a particular key pair, perform the following steps:

**Step 1:** Select **Enigmail > Key Management** through your Thunderbird's menu bar.

**Step 2:** Select an email address and subsequently select **View > Key Properties** through your Enigmail Key Management window.

**Step 3:** Through your Key Properties window, you will be able to view the fingerprint of your selected email address.

For example, the fingerprint of electra.stormborn@gmail.com is 60BB F18B ECD8 305C 48DE A1F0 90D9 88CD 2398 A398. 

Your correspondent should repeat these steps. To confirm fingerprints, read the fingerprint of your key to your contact and have them verify that the fingerprint they see on your public key matches with what they received. Then have your contact do the same for their key's fingerprint. If fingerprints don't match, exchange public keys again and repeat the validation process.

**Note:** The fingerprint itself is not a secret and can be recorded for later verification at your convenience.

### 4.4.2. How to sign a valid public key

Once you have verified a correspondent's key, you can sign it, to confirm that you consider this key valid. However, signing keys can expose a connection between you and your corespondent when you send a signed key to somebody else or export it to a key server. To prevent this from happening always select the “**Local signature**” option included below.

You can sign a validated public key through the following steps:

**Step 1:** Select **Enigmail > Key Management** to open your Enigmail Key Management window.

**Step 2:** Right click on your correspondent's public key from the Enigmail Key Management window and select the “**Sign Key**” item from the menu, as illustrated below:

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-432.png)

**Step 3:** Through the following window that will appear, check the “**I have done very careful checking**” option and select “**Local signature (cannot be exported)**” - to prevent the exposure of your connection with the person whose key you are signing. Then click on “OK” to sign your correspondent's public key. You might be asked to provide the passphrase which protects your private key. 

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-433.png)

## 4.5. How to encrypt and decrypt email messages

The header of any email message - its *Subject* and intended recipients including any information in the *To*, *cc* and *bcc* fields - cannot be encrypted and will be sent in open text. To ensure the privacy and security of your exchanged emails, the subject of your email should be kept non-descriptive as to not reveal sensitive information. In addition, you are advised to put all addresses in the *bcc* field when sending emails to a group of people.

When encrypting email messages with attachments, we strongly recommend using the **PGP/MIME** option, as this will extend encryption to include any files and file names attached to your email.

Note that any encrypted email you send with Thunderbird/Enigmail/GnuPG is automatically encrypted to your key along with the chosen recipients of this email, so you are able to decrypt emails in your sent folder.

### 4.5.1. How to encrypt an email

Once both you and your correspondent have successfully imported and validated and signed each other's public keys, you are ready to begin sending encrypted messages and decrypting received ones.

You can encrypt the content of your email messages through the following steps:

**Step 1:** Open Thunderbird and click on “**Write**” to write an email.

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-434.png)

**Step 2:** To encrypt and sign your email, click on “**Enigmail**” and in its drop-down menu, click on “**Encryption**” and on “**Signing**” so that they can appear “**ON**”. 

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-435.png)

To verify that this email will be both signed and encrypted, the following message should appear on top of your email address:

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-436.png)

**Step 3:** Click on “**Send**” to send your (encrypted and signed) email. You will be asked to type in your passphrase so that your private key can be used for the signing and encryption of the email. 

**Optional step 4:** If you are attaching a file to your email, you will be asked to choose whether you would like your attachment to be signed and encrypted as well. You can do this by selecting “**Encrypt and sign the message as a whole and send it using PGP/MIME**” and by subsequently clicking on “**OK**”.

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-437.png) 

**Note:** When you encrypt each attachment separately (second option above) the names of the attached files are not encrypted and are being sent in clear text. This can result in leaking sensitive information. Using PGP/MIME ensures that all email text, attached files and their names are encrypted and hidden.

### 4.5.2. How to decrypt an email

When you receive and open an encrypted message, Enigmail/OpenPGP will automatically prompt you to decrypt it by typing your passphrase in the pop-up window. 

Once you have typed it in, the encrypted email will be decrypted. 

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-438.png)

### 4.5.3. How to extend security options

You can further configure Enigmail to ensure that you are alerted before sending an unencrypted email and that your draft emails are encrypted. You can do this through the following steps:

**Step 1:** Select **Enigmail > Preferences** to open your Enigmail Preferences window.

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-439.png)

**Step 2:** Click on “**Sending**” to configure your security options.

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-440.png)

**Step 3:** Click on “**Manual encryption settings**”, configure your settings as illustrated below and click on “**OK**”: 

![](/sites/securityinabox.org/files/media/thunderbird-lin-en-v01-441.png)

For every unencrypted email you send now you will be alerted that the email will be sent unencrypted.

# FAQ

**Q: How many email accounts can I set up on Thunderbird?**

**A:** As many as you like! Thunderbird is an email manager and can easily handle 20 or more email accounts.

**Q: Remind me one more time, which parts of an email message does Enigmail encrypt?**

**A:** Enigmail encrypts the content of the message. It doesn't encrypt the subject line of the message, your email address or the name you chose to associate with that email account. So if you're trying to send a confidential message, make sure the subject line doesn't give you away! And if you want to stay anonymous, avoid displaying or even using your real name when you create your email account.

**Q: I still don't understand the purpose of digitally signing my messages.**

**A:** A digital signature proves that you're the real sender of a particular message and that the message hasn't been tampered with on its way to your intended recipient. Think of it as the electronic equivalent of the wax seal on an envelope, which contains a very important letter.