

---

lang: en
community: guide
type: tools
os: windows
weight: 070
title: gpg4usb for Windows - email and file encryption

---

**gpg4usb** is a free, open source, portable program for encrypting text (email) messages and files. It uses the same Public Key Encryption algorithm as **GPG** and **PGP** programs.

# Required reading


:[](../../../tactics/secure communication)


:[](gpg4usb-for-windows-email-and-file-encryption)

# What you will get from this guide

- The ability to encrypt files and text messages from wherever you are (for instance, an Internet café or at work).
- The ability to encrypt the messages *off-line* or when Internet access is unavailable, and then send them from a computer connected to the Internet later.

# 1. Introduction to gpg4usb





## 1.1 Things You Should Know about gpg4usb Before You Start

**gpg4usb** is a simple, lightweight and portable program that lets you encrypt and decrypt text messages and files. **gpg4usb** is based on public-key cryptography. In this method, each individual must generate her/his own personal **key pair**. The first key is known as the **private key**. It is protected by a password or passphrase, guarded and *never* shared with anyone.

The second key is known as the **public key**. This key can be shared with any of your correspondents - and your correspondents can share theirs with you. Once you have a correspondent’s public key you can begin sending encrypted emails to this person. Only she will be able to decrypt and read your emails, because she is the only person who has access to the matching private key.

Similarly, if you send a copy of your own public key to your email contacts and keep the matching private key secret, only you will be able to read encrypted messages from those contacts.

You may also attach digital signatures to your messages. The recipient of your message who has a genuine copy of your public key will be able to verify that the email comes from you, and that its content was not tampered with on the way. Similarly, if you have a correspondent's public key, you can verify the digital signatures on her messages.

**gpg4usb** lets you generate an encryption key pair, export public keys to be shared with other people, compose a text message, and encrypt it. You can either simply copy and paste the public key and/or encrypted message from **gpg4usb** to the body of your email, or save them as a text file to be sent later. Documents and files can be encrypted too. 

**Note**: Be mindful that the original, unencrypted versions of your documents and files may still reside on your computer, so both your correspondent and yourself must remember to remove them from computers when necessary.

**gpg4usb** lets you exchange keys and encrypted messages with other similar **GPG** or **PGP** programs.

For more information about public key encryption, see *Chapter 2.4 Cryptology - Public Key Encryption* on page 38 of [Digital Security and Privacy for Human Rights Defenders](https://www.frontlinedefenders.org/esecman/).

# 2. Install gpg4usb and Generate a Key Pair





## 2.0 Install gpg4usb

**gpg4usb** is a portable tool that does not require installation on your computer. The software is disturbed as a zip and should be extracted directly to a USB drive or to a folder on your computer; to begin perform the following steps: 

**Step 1**. **Locate** the **gpg4usb** zipped archive file, and then **extract** all the files to a removable USB drive or a folder on your computer:

![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-01.png)

*Figure 1: The gpg4usb program destination location*

<a name="2.1"></a>

## 2.1 Generate a Key Pair

Before you can begin encrypting and decrypting email, text messages, documents and files, you must take two preparatory steps: first you need to generate or import your encryption key pair and second you need to send your public key to your contacts and receive their public keys and import them to your key ring. We describe how to share public keys on the next page. **gpg4usb** assist you with generating your key pair on the first start of the program. Note that you can always come back to *Getting Started* window from the *Help* -> *Open Wizard* menu.

**Step 1**. To run the **gpg4usb** program for the first time , **find and double click** ![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-02.png) to open the **gpg4usb** folder and then **double click** ![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-03.png). This will activate the *Getting Started* window. Select a language and click *Next*.

**Step 2**. At the *Choose your Action* screen, click *Create a new keypair*.

![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-04.png)

*Figure 2: Choose your Action*

Note the other options to import existing keys available on the First Start Wizard screen. If upgrading from a previous version of gpg4usb, you can choose *import settings and/or keys from gpg4usb*. If using [Thunderbird with Enigmail](../thunderbird/windows), you can choose the option *import keys from GnuPG*. You can also choose to import keys at a later stage by running the wizard again from the *Help* -> *Open Wizard* menu.

**Step 3**. At the *Create a keypair* **click** *Create New Key*.

![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-05.png)

*Figure 3: Create New Key* 

**Step 4**. **Enter** the appropriate data into the corresponding text fields, so that your own window resembles the following:

![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-06.png)

*Figure 4: An example of a completed Generate Key form*

**Important:** 

* Set a secure password to protect your private key (please refer to [**How to create and maintain secure passwords**](../passwords)).
* We advice that you use expiration date and that you set it to less then 5 years.
* We strongly recommend that you generate keys of at least 2048 bit size. Key of a larger size is more secure, but also requires more time to create, encrypt and decrypt texts.

**Note**: You do not need to use your real name and real email address when generating your key. However, using email address of the account you will use to communicate will make it easier for your contacts to associate your key with this account.

**Step 6**. **Click** *OK* to generate the keypair.

![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-07.png)

*Figure 5: Generating a key...*

![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-08.png)

*Figure 6: New key created*

**Step 7**. **Click** *OK* to come back to the **gpg4usb** window. After the keypair has been successfully generated, you will see a screen resembling the following: 

![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-09.png)

*Figure 7: The gpg4usb window, displaying the newly created key pair* 

Now that you have successfully created a key pair, you need to learn how to export your public key to share it with other people, and how to import the public keys of your correspondents.

# 3. Export and Import Keys





## 3.1 Export Your Public Key

You must send your public key to your correspondent before they can send encrypted messages to you. 

To export your public key with **gpg4usb**, perform the following steps:

**Step 1**. **Double click** ![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-02.png) to open the **gpg4usb** folder.

**Step 2**. **Double click** ![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-03.png) to open **gpg4usb** program.

**Step3**. **Click** ![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-10a.png) to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-10.png)

*Figure 1: The Keymanagement window displaying all the key pairs*

**Step 3**. **Check** your own key, as shown in *Figure 1* above.

**Step 4**. **Select** the *Export To File* item from the **Key** menu as shown below:

![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-11.png)

*Figure 2: The Keymanagement window with the Export To File item selected*

This will activate the following screen:

![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-12.png)

*Figure 3: The Export To Folder browse window*

**Step 5**. **Click** ![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-13.png) to save your key pair to the **gpg4usb** program folder.

**Step 6**: **Send** the exported file with your public key as an attachment to your correspondent.


## 3.2 Import a Correspondent's Public Key

Before you can encrypt information and send it to your correspondent, you need to receive and import their public key. To import a correspondent's Public key using **gpg4usb**, perform the following steps:

**Step 1**. **Double click** ![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-03.png) to open the **gpg4usb** program.

**Step 2**. **Click** ![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-14.png) Import to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-15.png)

*Figure 4: The Import Key dialog box*

**Step 3**. **Browse** and select the key you wish to import.

![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-16a.png)

*Figure 5: Open Key*

**Step 4**. **Click** Open to activate following window.

![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-16b.png)

*Figure 6: Key Import Details*

**Step 5**. **Click** OK to close above window and come back to **gpg4usb** main window. It will display newly imported public key as below.

![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-16.png)

*Figure 7: The gpg4usb console displaying the newly imported public key associated with your correspondent's account*

Now that you have successfully imported a correspondent's public key, you must now verify and sign that imported key.

<a name="3.3"></a>

## 3.3 Verify a Key Pair

You must verify that the imported key truly belongs to the person who purportedly sent it and then verify it as being authentic. This is an important step that both you and your email contacts should follow for each public key that you receive.

To verify a key pair, perform the following steps:

**Step 1**. **Contact** your correspondent through some means of communication other than email. 

**Note**: You may use a telephone, text messages, **Voice over Internet Protocol** (**VoIP**) or any other method, but only if you are certain that you are really communicating with the right person. As a result, telephone conversations and face-to-face meetings provide the greatest assurance of the authenticity of a person's identity, if or when they can be arranged safely.

**Step 2**. You and your correspondent should verify that the 'fingerprints' of the public keys that you have exchanged are the same.  

**Note**: A fingerprint is a unique series of numbers and letters that identifies each key. The fingerprint itself is not a secret, and can be recorded and used for verification later if or when required.

To view the fingerprint of key pairs you have created or public keys you have imported, perform the following steps:

**Step 1**. **Select** a key, then **right-click** it to activate its associated pop-up menu.

**Step 2**. **Select** the *Show Keydetails* item as shown below in *Figure 8*. 

![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-17.png)

*Figure 8: The pop-up menu associated with a correspondent's key*

This will activate the following screen:

![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-18.png)

*Figure 9: The Keydetails window with the key fingerprint on the bottom*

**Step 3**. **Compare** this fingerprint with the one your correspondent see in her **gpg4usb** program.

Your correspondent should repeat these steps. Confirm with each other that the fingerprint for the key each of you have exchanged matches the sender's original. If they don't match, exchange your public keys again (perhaps over different email address or communication method) and repeat the verification process.

If the fingerprints match each other *exactly*, then you are ready to securely send encrypted messages and files between each others.

# 4. Encrypt and Decrypt Text and Files





## 4.0 Encrypt Text

In the example that follows, Terence will encrypt an email for his friend Salima, using the following steps:

**Step 1**. **Double click** ![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-03.png) to open the **gpg4usb** console.

**Step 2**. **Compose** your message as shown in the example below:

![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-19.png)

*Figure 1: The gpg4usb console displaying an example of a message*

**Step 3**. **Check** the check box associated with the intended recipient of your email as follows:

![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-20.png)

*Figure 2: The gpg4usb console displaying the intended recipient*

**Note:** You can encrypt a message to more than one recipient by simply checking their corresponding check boxes in the *Encrypt for:* pane. Also, it may prove useful for your personal records to encrypt that message to yourself, so you can read what you sent later. 

**Step 4**. Either **click** ![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-21.png) or **select Encrypt** from the **Crypt** menu to encrypt your message as follows:

![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-22.png)

*Figure 3: The gpg4usb console displaying an example of an encrypted message*

**Step 5**. **Click** ![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-23.png) to select the entire encrypted message, and then **click** ![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-24.png) to copy the message to the clipboard.

**Note**: Alternatively, you may use the short-cut keys associated with each item in the menu, in this case **Ctrl + E** will encrypt the message, **Ctrl + A** will select the entire encrypted message, and **Ctrl + C** will copy the message to the clipboard.

**Step 6**. **Open** your email account and then **open** a blank message page, and then **paste** this message so that it resembles the following:

![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-25.png)

*Figure 4: An example of a message encrypted in gpg4usb pasted into a Gmail account email*

**Note**: **Rich Text Formats** (**RTF**) can corrupt the encrypted message format; hence, it is better to compose your messages in plain text. To convert **RTF** into plain text in **Gmail** simply **click** *More Options* and **select** *Plain Text Mode*  displayed at the foot of the message pane as shown below:

 ![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-26.png)

*Figure 5: Gmail Format Options*

<a name="4.1"></a>

## 4.1 Decrypt Text

To decrypt an encrypted email, perform the following steps:

**Step 1**. **Double click** ![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-03.png) to open the **gpg4usb** program.

**Step 2**. **Open** your email account, and then **open** the message.

**Step 3**. **Select**, **copy** and then **paste** the encrypted message into the **gpg4usb** console *untitled1.txt* tab as follows:

![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-27.png)

*Figure 6: The gpg4usb console displaying a message for decryption*

**Note**: If the encrypted text appears with double line breaks as shown in *Figure 7* below, **gpg4usb** might not be able to automatically decrypt it. To remove these double line breaks, **click** on ![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-27b.png) (or **select** *Remove double Linebreaks* from the **Edit** menu) to remove them and then continue the decryption process at **Step 4**.

![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-28.png)

*Figure 7: The gpg4usb console displaying a message for decryption with double linebreaks*
 
**Step 4**. **Click** ![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-29.png) and enter the password you assigned when generating a key pair, as shown in the following screen:

![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-30.png)

*Figure 8: The Enter Password prompt window*

**Step 5**. **Click** *OK* to activate a **gpg4usb** console resembling *Figure 2* above.

<a name="4.2"></a>

## 4.2 Encrypt Files

The process for encrypting a file is similar to encrypting text messages; in the example that follows, Salima will encrypt a file for Terence, using the following steps:

**Step 1**. **Double click** ![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-03.png) to open the **gpg4usb** program.

**Step 2**. **Click** ![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-31.png) and *Encrypt File* to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-32.png)

*Figure 9: The Encrypt File window*

The *Encrypt File* window scroll list (outlined in black) lets you select the email account and corresponding key you will use to encrypt a message to.

**Step 3**. **Click** ![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-33.png) beside *Input* item to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-34.png)

*Figure 10: The Open File browser window*

**Step 4**. **Click** ![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-35.png) to attach the file to be encrypted and return to the *Encrypt* window as follows:

![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-36.png)

*Figure 11: The Encrypt File window displaying the file designated for encryption*

**Step 5**. **Click** *OK* to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-38.png)

*Figure 12: The Done confirmation dialog box*

The *Done* confirmation dialog box shows you where the newly encrypted file resides. An encrypted file can also be identified by either a *.asc* file extension, for example, *Meeting Minutes.doc.asc*. 

**Step 6**. **Click** *OK* to complete the file encryption process.

**Note**: You can encrypt a text message you might send along with the encrypted file separately. 

**Step 7**. Using your email account, **navigate** to the location specified in the *Done* confirmation dialog box (*Figure 12*), and then attach the encrypted file to you email as you would any other file. 

**IMPORTANT**: Observe that the name of the file is **not encrypted**. Make sure that this name does not reveal any important information! Do not forget that an  unencrypted version of the file continues to reside on the disk.

<a name="4.3"></a>

## 4.3 Decrypt Files

In the example that follows, Terence will decrypt the file Salima has sent to him, using the following steps:

**Step 1**. **Double click** ![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-03.png) to open the **gpg4usb** program.

**Step 2**. **Open** your email account, **open** the message and **download** the attached file.

**Note**: If your correspondent has sent a message accompanying the encrypted file, you may decrypt that message by using the method outlined in the [**Decrypt Text**](#782)section

**Step 3**. In the **gpg4usb** console (as shown in *Figure 1* above), **click** ![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-31.png) and **Decrypt File** window (as in *Figure 13* below). 

**Step 4**. **Click** ![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-33.png) beside *Input* item to browse to the location of the downloaded encrypted file as follows:

![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-37.png) 

*Figure 13: The Decrypt window, displaying the path to the encrypted file*

**Step 5**. **Click** *OK* to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/gpg4usb-win-39.png) 

*Figure 14: The Done confirmation dialog box displaying the location of the decrypted file*

**Important**: If you are working from an internet café or at workstations other people may have access to decrypted version of the file, it is better to copy the *.asc* file to your USB or portable drive, and take it with you so you may decrypt it in the privacy of your own home.


# FAQ

***Q***: Does **gpg4usb** have to be used from USB memory stick?

***A***: No. It can be extracted to and run from your computer hard disk.

***Q***: How many accounts may I generate key pairs for?

***A***: As many as you need.

***Q***: I like the fact that simple cut-and-paste operations are used here.

***A***: Indeed. However, don't forget that your email subject header remain unencrypted. Therefore, be careful and don't enter a subject title which is descriptive or may give you away potentially!
