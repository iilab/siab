

---

lang: en
community: guide
type: tools
os: android
weight: 090
title: Android Privacy Guard (APG) for Android devices

---

**Android Privacy Guard** (APG) is free and open source software, created by [Thialfiar](http://www.thialfihar.org/), that allows you to encrypt and decrypt files and email messages on Android devices. Although not all features of OpenPGP are currently available, APG's implementation allows you to encrypt, decrypt and sign files and messages using a public/private key pair. You can also encrypt individual files *without* a public/private key pair by relying on symmetric encryption and a strong passphrase. For email encryption, we recommend that you use APG [in combination with K9 Mail](../k9/android), an email client for Android devices. 

# Required reading


:[](../../../tactics/passwords)


:[](../../../tactics/secure communication)


:[](../../../tactics/mobile phones)


:[](../../../tactics/smartphones)


:[](android-privacy-guard-apg-for-android-devices)

# What you will get from this guide

- The ability to use encryption for single files and for email communication.

# 1. Introduction to APG

- **APG** integrates with the [**K9 Email Client for Android**](../k9/android) to support mobile email encryption. First, however, you need to know how email encryption works. This is explained under [**Advanced Email Security**](../secure-communication#505) in [**Keep your online communication private**](../secure-communication).
- **APG** can also encrypt and decrypt files locally on your device, using either a passphrase or public/private keypair. 
- Due to the nature of data storage on smartphones, it may not be possible to securely delete the private key that you generate or import.


## 1.0 Other tools like APG

- **Android:** [OpenKeychain](http://www.openkeychain.org/).
- **iOS:** [oPenGP](https://itunes.apple.com/us/app/opengp/id414003727).
- **Microsoft Windows:** [gpg4usb](../gpg4usb/windows), [Thunderbird+Enigmail+GPG](../thunderbird/windows), [Mailvelope](https://www.mailvelope.com/), [Mailpile](https://www.mailpile.is/).
- **Mac OS:** Thunderbird+Enigmail+GPG, [Mailvelope](https://www.mailvelope.com/), [Mailpile](https://www.mailpile.is/).
- **GNU Linux:**  gpg4usb, Thunderbird+Enigmail+GPG, [Mailvelope](https://www.mailvelope.com/), [Mailpile](https://www.mailpile.is/).


# 2. Install and configure APG





## 2.1 Install APG

**Step 1.** On your Android device, **download** and **install** the app from the [Google Play](https://play.google.com/store/apps/details?id=org.thialfihar.android.apg) by pressing ![](/sites/siabnext.ttc.io/files/media/apg_001.png).

![](/sites/siabnext.ttc.io/files/media/apg_002.png)

*Figure 1: APG on the Google Play Store*

**Step 2.** Before the installation process begins, you will be prompted to review the access that the application will have on your phone. Review this carefully. Once your are happy with the permissions that will be granted, press 
![](/sites/siabnext.ttc.io/files/media/apg_003.png) and the installation will complete. If you do not agree with the permissions that will be granted, press the back button and the installation will be cancelled.

![](/sites/siabnext.ttc.io/files/media/apg_004.png)

*Figure 2: Permissions required*

**Step 3.** In order to encrypt files or messages when you first start **APG**, you will be asked either to [*create*](#1514) new public and private keys on your phone or [*import*](#1515) existing GPG keys.

![](/sites/siabnext.ttc.io/files/media/apg_005.png)

*Figure 3: APG Key import/creation screen*

**Note:** If you want to send encrypted files or messages to other people, you will either need to import their public keys or decide on a shared password.


## 2.2 (Option 1) Create new public and private keys

If you do not already have your private and public GPG key or wish to use a separate GPG keys for your Android device you can use **APG** to
create them.

**Step 1:** When you open **APG** for the first time click the ![](/sites/siabnext.ttc.io/files/media/apg_006.png) button.

**Step 2:** Wait 2 - 3 minutes while your GPG keys are generated. You will be able to assign your name and email address to the key in the next step.

**Step 3:** In the following screen (*Figure 4*).

- we strongly recommend that you protect your GPG keys with **password**. To do this press ![](/sites/siabnext.ttc.io/files/media/apg_007.png) and provide strong password;
- fill in your ***name*, *email address***;
- it is important that you set an **expiry date** on the GPG keys, after which time the keys can no longer be used to encrypt files.

![](/sites/siabnext.ttc.io/files/media/apg_008.png)

*Figure 4: GPG Key information*

**Step 4:** Once all the information is correct, tap ![](/sites/siabnext.ttc.io/files/media/apg_009.png) at the top of the screen to be brought back to the main **APG** screen, where you will see a list of all your keys (see Figure 4).

## 2.3 (Option 2) Import keys from a file

To use GPG keys that you created on another device or computer, or to import the public keys of your contact:

**Step 1:** Copy the GPG key(s) to your Android device via USB or save them from the email that you received on the Android device.

**Step 2:** In APG, click the ![](/sites/siabnext.ttc.io/files/media/apg_010.png) button.

**Step 3:** On the following screen click the ![](/sites/siabnext.ttc.io/files/media/apg_011.png) button at the top of your screen to open a file browser.

**Step 4:** From the file browser, select the key(s) you wish to import.

**Step 5:** Review the keys you will import and tap ![](/sites/siabnext.ttc.io/files/media/apg_012.png) to add the GPG keys to APG. You may decide which keys you do not wish to import by deselecting appropriate checkbox for the keys.

![](/sites/siabnext.ttc.io/files/media/apg_013.png)

*Figure 5: APG key import review screen*

**Step 6:** Once you have imported all the desired GPG keys you will be brought back to the main screen where you will see a list of all your keys.

![](/sites/siabnext.ttc.io/files/media/apg_014.png)

*Figure 6: APG key list*

## 2.4 (Option 3) Import keys from the clipboard

GPG keys can be sent in the body of an email instead of as an attachment to import a key.

**Step 1:** Copy the GPG key from your email to the clipboard.

![](/sites/siabnext.ttc.io/files/media/apg_038.png)

*Figure 7: GPG key in the body of an email*

**Step 2:** Open **APG** and expand the side menu on any **APG** screen by pressing ![](/sites/siabnext.ttc.io/files/media/apg_015.png) at the top left of your screen.

**Step 3:** Select ![](/sites/siabnext.ttc.io/files/media/apg_039.png) to bring up the import key screen.

**Step 4:** Tap ![](/sites/siabnext.ttc.io/files/media/apg_040.png) at the top of the screen to display the import options menu and select ![](/sites/siabnext.ttc.io/files/media/apg_041.png).

**Step 5:** Tap ![](/sites/siabnext.ttc.io/files/media/apg_042.png) to copy the key from the clipboard.

**Step 6:** Tap ![](/sites/siabnext.ttc.io/files/media/apg_043.png) at the bottom of the screen to finish importing the key into **APG**.

![](/sites/siabnext.ttc.io/files/media/apg_044.png) ![](/sites/siabnext.ttc.io/files/media/apg_045.png)

*Figure 8 & 9: APG Import options / GPG key copied from clipboard*


# 3. Sharing and verifying public keys

In order for your contacts to be able to send you encrypted email, you will first need to send them your *public key*.

## 3.1 Key Management - Share your public key as a file

**Step 1:** From the main **APG** window tap on your key's entry to bring you to the *info* screen (*See Figure 9*) for your GPG key.

**Step 2:** Tap on ![](/sites/siabnext.ttc.io/files/media/apg_046.png) to display the menu and select ![](/sites/siabnext.ttc.io/files/media/apg_047.png).

**Step 3:** Select the location and file name you want to save your public key to and press ![](/sites/siabnext.ttc.io/files/media/apg_048.png).


![](/sites/siabnext.ttc.io/files/media/apg_049.png) ![](/sites/siabnext.ttc.io/files/media/apg_050.png)

*Figure 10 & 11: Key info and export to file / Save GPG key to location*

**Step 4:** The saved file can not be given to your contacts, for example via email or IM.

## 3.2 Key Management - Share your public key from the clipboard

**Step 1:** From the main **APG** window tap on your key's entry to bring you to the *info* screen (*See Figure 9 above*) for your GPG key.

**Step 2:** Tap ![](/sbox/screen/apg-en-1/051.png) to bring up sharing options and select ![](/sites/siabnext.ttc.io/files/media/apg_052.png).

**Step 3:** In the following menu select ![](/sites/siabnext.ttc.io/files/media/apg_053.png) to copy your GPG public key to the clipboard:

![](/sites/siabnext.ttc.io/files/media/apg_054.png)

*Figure 12: APG key sharing options*

**Step 4:** Paste the public key into an email or IM chat session to your contact.

## 3.3 Key Management - Verifying identities

In order to ensure that you have received the correct GPG public key for your colleague and not someone trying to impersonate them, it is very important that you verify the GPG keys fingerprints either in person or via a medium that you can verify who you are talking to such as a video call or telephone call.

**Step 1:** From the main **APG** window tap on your key's entry to bring you to the *info* screen (*See Figure 9 above*)for your GPG key. Your contact should do the same and tap on the key they have for you.

**Step 2:** Locate the **Fingerprint** line under the **MASTER KEY** heading and read out the 40 character long string one line at a time.

![](/sites/siabnext.ttc.io/files/media/apg_055.png)

*Figure 13: Key fingerprint*

**Step 3:** Your contact should verify that the fingerprint you read out, is the fingerprint displayed for your key on their phone or computer.

**Step 4:** Repeat steps 1 to 3 but tap on your contacts key at the first step.

# 4. Encrypting and decrypting messages with APG

**APG** provides two ways for you to encrypt files on your Android device.  **Public key** encryption is the desired option to use when sending files to other people as you will not have to share any passphrase with them. However you will need to receive public key from each person you wish to encrypt files to in advance. **Passphrase** encryption can be useful to be able to decrypt a file at a later date without the need to have access to a public key. But this method require sharing the passphrase used to encrypt the file in order to decrypt it later.

Message encryption in **APG** can be useful if you want to store encrypted notes in another application or send encrypted email or message via a service that you can not use [K-9 Mail](../k9/android) with (eg. webmail, social networking message, etc.). 


## 4.1 Encrypting messages - public key

**Step 1:** Expand the side menu on any **APG** screen by pressing ![](/sites/siabnext.ttc.io/files/media/apg_015.png) at the top left of your screen.

**Step 2:** Select ![](/sites/siabnext.ttc.io/files/media/apg_016.png) to bring up the encryption screen.

**Step 3:** To view the list of possible recipients press ![](/sites/siabnext.ttc.io/files/media/apg_017.png).  **Note:** If you want to be able to decrypt the message at a later time, you will need to remember to include yourself in the list of recipients.

**Step 4:** On the Recipient selection screen, tick all the people that need to be able to decrypt the message and press ![](/sites/siabnext.ttc.io/files/media/apg_018.png).


![](/sites/siabnext.ttc.io/files/media/apg_019.png)

*Figure 22: Recipient selection*

**Step 5:** Choose how to encrypt your message. Tapping ![](/sites/siabnext.ttc.io/files/media/apg_034.png) will allow you to send the encrypted message to another application on your phone such as an email client. Tapping ![](/sites/siabnext.ttc.io/files/media/apg_035.png) will copy the encrypted message to your clipboard allowing you to paste the message anywhere that you can paste, such as an online forum.


## 4.2 Encrypting messages - passphrase

**Step 1:** Expand the side menu on any **APG** screen by pressing ![](/sites/siabnext.ttc.io/files/media/apg_015.png) at the top left of your screen.

**Step 2:** Select ![](/sites/siabnext.ttc.io/files/media/apg_016.png) to bring up the encryption screen.

**Step 3:** Press the ![](/sites/siabnext.ttc.io/files/media/apg_020.png) or ![](/sites/siabnext.ttc.io/files/media/apg_021.png) buttons to either side of **PUBLIC KEY** to change the encryption type to **PASSPHRASE**.

**Step 4:** Enter a strong password in the fields provided.

**Step 5:** Enter the message you want to encrypt.

![](/sites/siabnext.ttc.io/files/media/apg_036.png)

*Figure 23: Message composed, ready for encryption*

**Step 5:** Choose how to use your encrypted message.  Tapping ![](/sites/siabnext.ttc.io/files/media/apg_034.png) will allow you to send the encrypted message to another application on your phone such as an email client. Tapping ![](/sites/siabnext.ttc.io/files/media/apg_035.png) will copy the encrypted message to your clipboard allowing you to paste the message any where that you can paste, such as an online forum.


**Note**: If you plan to share the encrypted message with a contact you will need to relay the *passphrase* to them in a secure way, such as in person. It should never be sent to anyone over email or IM if it is not encrypted.

## 4.3 Decrypting messages with APG

**Step 1:** Copy the entire contents of the encrypted message that you received in the other app to the clipboard by long-taping on the message and selecting copy button.

**Step 2:** Switch to APG app and expand the side menu on any **APG** screen by pressing ![](/sites/siabnext.ttc.io/files/media/apg_015.png) at the top left of your screen.

**Step 3:** Select ![](/sites/siabnext.ttc.io/files/media/apg_028.png) to bring up the encryption screen.

**Step 4:** APG will automatically detect that the clipboard has an encrypted message in it and ask you for either your GPG password, if the sender used public key encryption, or for the message password, if you used the *passphrase* encryption.


![](/sites/siabnext.ttc.io/files/media/apg_037.png)

*Figure 24: Message decryption with GPG key*

**Step 5** The decrypted message will be displayed in a text window inside APG.

# 5. Encrypting and decrypting files with APG

As with message encryption **public key** is the preferred encryption method but password encryption will allow you to decrypt on a phone or computer that does not have a **private key** installed but does have **APG** or **GPG** software.


## 5.1 Encrypting files - public key

**Step 1:** Expand the side menu on any **APG** screen by pressing ![](/sites/siabnext.ttc.io/files/media/apg_015.png) at the top left of your screen.

**Step 2:** Select ![](/sites/siabnext.ttc.io/files/media/apg_016.png) to bring up the encryption screen.

**Step 3:** To view the list of possible recipients press ![](/sites/siabnext.ttc.io/files/media/apg_017.png).  **Note:** If you want to be able to decrypt the file yourself at a later time, you will need to remember to include yourself in the list of recipients.

**Step 4:** On the Recipient selection screen, tick all the people you want to be able to decrypt the file and press ![](/sites/siabnext.ttc.io/files/media/apg_018.png).

![](/sites/siabnext.ttc.io/files/media/apg_019.png)

*Figure 14: Recipient selection*

**Step 5:** Press the ![](/sites/siabnext.ttc.io/files/media/apg_020.png) or ![](/sites/siabnext.ttc.io/files/media/apg_021.png) buttons to either side of **MESSAGE** to change the encryption type to **FILE**.

**Step 6:** Tap ![](/sites/siabnext.ttc.io/files/media/apg_022.png) to open the file browser and select the file you want to encrypt.

![](/sites/siabnext.ttc.io/files/media/apg_023.png)

*Figure 15: File encryption screen with advanced settings*

**Step 7:** press ![](/sites/siabnext.ttc.io/files/media/apg_024.png) to choose a file name and location to save the file to.

![](/sites/siabnext.ttc.io/files/media/apg_025.png)

*Figure 16: Save encrypted files*

**Step 8:** Tap ![](/sites/siabnext.ttc.io/files/media/apg_026.png) to complete the encryption process.

## 5.2 Encrypting files - passphrase

**Step 1:** Expand the side menu on any **APG** screen by pressing ![](/sites/siabnext.ttc.io/files/media/apg_015.png) at the top left of your screen.

**Step 2:** Select ![](/sites/siabnext.ttc.io/files/media/apg_016.png) to bring up the encryption screen.

**Step 3:** Press the ![](/sites/siabnext.ttc.io/files/media/apg_020.png) or ![](/sites/siabnext.ttc.io/files/media/apg_021.png) buttons to either side of **PUBLIC KEY** to change the encryption type to **PASSPHRASE**.

**Step 4:** Enter a strong password in the fields provided.

**Step 5:** Press the ![](/sites/siabnext.ttc.io/files/media/apg_020.png) or ![](/sites/siabnext.ttc.io/files/media/apg_021.png) buttons to either side of **MESSAGE** to change the encryption type to **FILE**.

**Step 6:** Tap ![](/sites/siabnext.ttc.io/files/media/apg_022.png) to open the file browser and select the file you want to encrypt.

![](/sites/siabnext.ttc.io/files/media/apg_027.png)

*Figure 17: Save encrypted files with a passphrase*

**Step 7:** press ![](/sites/siabnext.ttc.io/files/media/apg_024.png) to choose a file name and location to save the file to.

![](/sites/siabnext.ttc.io/files/media/apg_025.png)

*Figure 18: Save encrypted files*

**Step 8:** Tap ![](/sites/siabnext.ttc.io/files/media/apg_026.png) to complete the encryption process.


**Note**: If you plan to share the encrypted file with a contact you will need to  relay the *passphrase* to them in a secure way, such as in person. It should never be sent to anyone over email or IM if it is not encrypted.

## 5.3 Decrypting files with APG

**Step 1:** Expand the side menu on any **APG** screen by pressing ![](/sites/siabnext.ttc.io/files/media/apg_015.png) at the top left of your screen.

**Step 2:** Select ![](/sites/siabnext.ttc.io/files/media/apg_028.png) to bring up the encryption screen.

**Step 3:** Tap the ![](/sites/siabnext.ttc.io/files/media/apg_020.png) or ![](/sites/siabnext.ttc.io/files/media/apg_021.png) buttons to either side of **MESSAGE** to change the encryption type to **FILE**.

**Step 4:** Tap ![](/sites/siabnext.ttc.io/files/media/apg_022.png) to open the file browser and select the file you want to decrypt.

![](/sites/siabnext.ttc.io/files/media/apg_029.png)

*Figure 19: File selected to decrypt*

**Step 7:** press ![](/sites/siabnext.ttc.io/files/media/apg_030.png) after which you will be prompted for your GPG keys password if public key encryption was used or for the file password if you used the *passphrase* encryption.

![](/sites/siabnext.ttc.io/files/media/apg_031.png)

*Figure 20: Enter your GPG password*

**Step 8:** Tap ![](/sites/siabnext.ttc.io/files/media/apg_026.png) to choose a location to save the decrypted document.

![](/sites/siabnext.ttc.io/files/media/apg_032.png)

*Figure 21: Enter your GPG password*

**Step 9:** Tap ![](/sites/siabnext.ttc.io/files/media/apg_026.png) to complete the decryption process.
