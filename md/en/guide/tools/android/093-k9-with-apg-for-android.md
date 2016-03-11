

---

lang: en
community: guide
type: tools
os: android
weight: 093
title: K9 with APG for Android

---

**K-9 Mail** is a free and open source email client for Android devices, that integrates seamlessly with **Android Privacy Guard**. 

**Android Privacy Guard (APG)** is a free and open source application that lets you encrypt, decrypt and sign files, messages or emails using Public Key Encryption (like OpenPGP) or encrypt/decrypt files or messages with symmetric encryption, securing them with a password.

The use of these two tools allows for easy encrypting and decrypting of email messages.

# Required reading


{{ required_reading: ../../secure communication }}


{{ required_reading: ../../mobile phones }}


{{ required_reading: ../../smartphones }}


{{ tool: ./093-tool.md }}

# What you will get from this guide

- The ability to **use encrypted email on your Android device**

# 1. Introduction to K9

**K-9 Mail** is a comprehensive email client that will allow you to send and receive email from one or more email accounts, as well as send and receive them securely when used with [**APG**](../apg/android) to encrypt the contents.

**Note:** Even when you are using encryption for your emails, it is important to remember that the *recipients* and the *subject* can not be hidden from anyone monitoring your email.

Before you start using **K-9 Mail** you will need:

- to have an internet connection on your phone.
- to have an email account that supports either secure POP3 or IMAP connections.
- to have an OpenPGP key-pair and public keys of the people with whom you wish to communicate with. See the [**APG**](../apg/android) guide, for setting up your key pair.
- to be familiar with the concept of public/private key encryption. See the [***Using public key encryption in email***](../secure-communication#506) section of [***Keep your online communication private***](../secure-communication) and the [***Thunderbird with Enigmail and GPG***](../thunderbird/windows) guide.

## 1.0 Other tools like K9 Mail

- [**Thunderbird**](../thunderbird/windows) with Enigmail and GPG  Microsoft Windows, Mac OS and GNU Linux.
- [**Mail.app**](https://www.apple.com/osx/apps/#mail) and [GPG Tools](https://gpgtools.org/) on Mac OS.
- [**Claws Mail**](http://www.claws-mail.org/) on Windows and Linux.
- [**gpg4usb**](/en/gpg4usb_portable) for Microsoft Windows and GNU Linux.
- [**Mailvelope**](https://www.mailvelope.com/) for Microsoft Windows, Mac OS and GNU Linux.
- [**Mailpile**](https://www.mailpile.is/) for Microsoft Windows, Mac OS and GNU Linux.

# 2. Install and configure K9 Mail





## 2.1 Install K9 Mail

**Note:** if you want to be able to send encrypted email, you should install [**APG**](../apg/android) before installing K-9 Mail.

**Step 1.** On your Android device, **download** and **install** the app from the [Google Play](https://play.google.com/store/apps/details?id=com.fsck.k9) store by tapping ![](/sites/siabnext.ttc.io/files/media/k9-en-and-001.png).

![](/sites/siabnext.ttc.io/files/media/k9-en-and-002.png)

*Figure 1: K-9 Mail on the Google Play Store*

**Step 2:**. Before the installation process begins, you will be prompted to review the access that the application will have on your phone. Review this carefully. Once your are happy with the permissions that will be granted, tap ![](/sites/siabnext.ttc.io/files/media/k9-en-and-003.png) and the installation will complete.  If you do not agree with the permissions that will be granted, tap the back button and the installation will be cancelled.

![](/sites/siabnext.ttc.io/files/media/k9-en-and-004.png)

*Figure 2: Permissions required*

**Step 3.** **Tap** *Open* to run the app for the first time.


## 2.2 Configure K9 Mail automatically

After installing **K-9 Mail** and running it for the first time you will be presented with a welcome screen describing the features of the mail client.  Press ![](/sites/siabnext.ttc.io/files/media/k9-en-and-005.png) to begin the account setup.

Where possible, **K-9 Mail** will attempt to configure your account automatically.  If this is not possible, or if you wish to have more control over the account setup process, you can also [**configure it manually**](#1530).


**Step 1:** Enter your email address and email password in the fields provided and tap ![](/sites/siabnext.ttc.io/files/media/k9-en-and-005.png) 

![](/sites/siabnext.ttc.io/files/media/k9-en-and-006.png) 

*Figure 3: Adding email credentials*

**Step 2:** **K-9 Mail** will connect to the internet and attempt to get your account settings.

**Step 3**: Once the settings have been retrieved you will be asked to enter your name as you want it to be displayed on all outgoing email and to give the account a name.  The account name will allow you to distinguish between multiple accounts, should you want to add more.  Tap ![](/sites/siabnext.ttc.io/files/media/k9-en-and-007.png) to complete the account setup.

![](/sites/siabnext.ttc.io/files/media/k9-en-and-008.png) 

*Figure 4: K-9 Mail account setup*

**Step 4:** **K-9 Mail** will display changes to the program since the last version, tap ![](/sites/siabnext.ttc.io/files/media/k9-en-and-009.png) to dismiss this window and be brought to your mail account.

![](/sites/siabnext.ttc.io/files/media/k9-en-and-010.png) 

*Figure 5: Email accounts*

**Step 5:** To make sure the account is working in **K-9 Mail**, **send** yourself an email from your computer and download it from the **K-9 Mail** client. 


## 2.3 Configure K9 Mail manually

**Step 1:** Enter your email address and email password in the fields provided (see *Fig 3*) and tap ![](/sites/siabnext.ttc.io/files/media/k9-en-and-011.png) 

**Step 2:** Select the account type your email is (IMAP/POP/Exchange) and tap the relevant button.

**Note:** you will need to refer to your email client settings on your computer to know what account type your email server uses.

![](/sites/siabnext.ttc.io/files/media/k9-en-and-012.png) 

*Figure 6: Account type selection*

**Step 3:** Next are the incoming server settings. If unsure, refer to the email client on your computer for settings. Always ensure that the *security type* is set to either *STARTTLS* or *SSL/TLS*. **Never** use the *none* option.

![](/sites/siabnext.ttc.io/files/media/k9-en-and-013.png) 

*Figure 7: Incoming Server Settings*

**Step 4.** **K-9 Mail** will then connect to your mail server to check if your settings are correct. It might display a warning about the certificate of your secured connection. *Do not ignore this!* This is the only time you can verify that the certificate really belongs to your mail server. If you ignore this, you can not be sure if you are not subject to a *Man-in-the-Middle attack*, and your communications could be intercepted. You can see a SHA-1 fingerprint at the very end of the warning. Either **check** on your computer if the installed certificate from your mail server has the same fingerprint, or find a way to check your mail server's certificate directly from your provider. 

**Step 5.** **K-9 Mail** asks you to configure your outgoing server settings. Again, **ensure** that *Security Type* is *STARTTLS* or *SSL/TLS*. For all additional settings, **check** your computer's email client or the settings of your email provider.

![](/sites/siabnext.ttc.io/files/media/k9-en-and-014.png)

*Figure 8: Outgoing server settings*

**Step 6.** **K-9 Mail** now asks you how often you want it to automatically poll for email. **Set** the option to *never* and uncheck *enable push mail for this account*, if you only want to receive email when you manually check, otherwise leave the settings as they are to automatically receive email as they arrive to your account.

![](/sites/siabnext.ttc.io/files/media/k9-en-and-015.png)

*Figure 9: Poll frequency*

**Step 7.** The last pieces of information to provide are a nickname for the email account which will be displayed in **K-9 Mail** and to set up the name you wish to be displayed on all outgoing email. (See *Figure 4*)

**Step 8:** To make sure the account is working in **K-9 Mail**, **send** yourself an email from your computer and download it from the **K-9 Mail** client. 


We recommend that you use **K-9 Mail** only in addition to your computer's email client. Therefore it is important that when you download email with your Android phone, it does not delete the email on the server, since you want to receive the email later with your computer, too. By default, **K-9 Mail** is set up this way, but you may want to learn more about the settings which can be found in *accounts*; this can be reached by long pressing on the account you have just set up and selecting *account settings* from the menu. You may also wish to check the *fetching mail* and *sending mail* account option for settings.


# 3. Send and receive encrypted email with K9

One of the main benefits of using **K-9 Mail** over other email clients is that it lets you send and receive *GPG* encrypted email.  Before you can start sending and receiving encrypted email, you need to ensure that you have all your OpenPGP keys imported into APG.  To learn more about this, read the [**APG**](../apg/android) guide.

## 3.1 Send encrypted email with K9

**Step 1:** From any screen in **K-9 Mail** tap the ![](/sites/siabnext.ttc.io/files/media/k9-en-and-016.png) icon to start a new email.

**Step 2:** On the email composition screen add your recipient by either typing in an email address or pressing ![](/sites/siabnext.ttc.io/files/media/k9-en-and-017.png) and selecting one from your address book.

**Step 3:** Enable encrypted email by checking the box next to *encrypt* (![](/sites/siabnext.ttc.io/files/media/k9-en-and-018.png)).

**Step 4:** When finished writing your email, press ![](/sites/siabnext.ttc.io/files/media/k9-en-and-019.png) to send.

**Step 5:** The following screen will ask you to select which GPG keys to encrypt to. Be default the recipient key and your own should already be selected.

**Note:** You should always ensure that your key is selected so that you can read the encrypted email that you had send.

![](/sites/siabnext.ttc.io/files/media/k9-en-and-020.png) ![](/sites/siabnext.ttc.io/files/media/k9-en-and-021.png)

*Figure 10 & 11: email composition and GPG key selection*

**Step 6:** Once all recipient keys have been selected, press ![](/sites/siabnext.ttc.io/files/media/k9-en-and-022.png) to send the email.

**Note:** Currently, **K-9 Mail** can not encrypt attachments, so you will need to [use **APG** to encrypt files you wish to send](../apg/android#1513) before you compose your message. To attach the file, tap ![](/sites/siabnext.ttc.io/files/media/k9-en-and-023.png) and select the encrypted file (ending in *.gpg*).


## 3.2 Receive encrypted email with K9

**Step 1:** Open your *inbox* and tap the email you wish to read.

**Step 2:** Tap the ![](/sites/siabnext.ttc.io/files/media/k9-en-and-024.png) button.

![](/sites/siabnext.ttc.io/files/media/k9-en-and-025.png) ![](/sites/siabnext.ttc.io/files/media/k9-en-and-026.png)

*Figure 12 & 13: Encrypted email and GPG passphrase prompt*

**Step 3:** Enter the passphrase for your GPG key when prompted and press ![](/sites/siabnext.ttc.io/files/media/k9-en-and-027.png) to decrypt the email.

![](/sites/siabnext.ttc.io/files/media/k9-en-and-028.png)

*Figure 14: Successfully Decrypted email*


**Note:** as **K-9 Mail** is currently not able to decrypt encrypted attachments, you will need to save the attachments to your phone and [decrypt them with APG](../apg/android#1513).

