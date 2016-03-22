

---

lang: en
community: guide
type: tools
os: android
weight: 098
title: TextSecure for Android

---

**TextSecure** is an Android-platform mobile phone application to send encrypted text messages (SMS). It can also send encrypted messages using your phone's data connection (which might be WiFi or mobile data) . Either way, the messages you send and receive are stored in an encrypted container on your phone.

# Required reading


:[Use mobile phones as securely as possible](../../../tactics/mobile phones)


:[Use smartphones as securely as possible](../../../tactics/smartphones)


:[TextSecure for Android](textsecure-for-android)

# What you will get from this guide

- Text messages to other TextSecure users can be encrypted when sent.
- Text messages are stored in an encrypted database on your device, protected by a passphrase. 
- If your phone is lost or stolen, your messages will remain unreadable to those without the passphrase. 

# 1. Introduction to TextSecure

- Using this application will prevent anyone from being able to read the content of your text messages, but will not hide the fact that you are sending messages.

- TextSecure will only hide who the messages are being sent to when your phone connects to Internet and messages are sent over data connection through *WhisperSync* server. Traditional SMS, encrypted or not, will still disclose the recipient(s) to your mobile phone company.

- In some countries, an encryption programme such as **TextSecure** may attract attention, be illegal or subject to legal constraints.

## 1.0 Other tools like TextSecure

- Android: [surespot](https://www.surespot.me/), [ChatSecure](https://guardianproject.info/apps/chatsecure/)
- iOS: [surespot](https://www.surespot.me/), [ChatSecure](https://chatsecure.org/)
- Microsoft Windows: [Jitsi](../jitsi/windows), [Pidgin](../pidgin/windows)
- Mac OS:  [Jitsi](https://jitsi.org), [Adium](https://www.adium.im/)
- Linux: [Jitsi](https://jitsi.org/), [Pidgin](https://www.pidgin.im/)


# 2. Install TextSecure





## 2.1 Installation process

**Step 1.** On your Android device, **download** and **install** the app from the [Google Play](https://play.google.com/store/apps/details?id=org.thoughtcrime.securesms) store by tapping ![](/sites/siabnext.ttc.io/files/media/textsecure_001.png).

![](/sites/siabnext.ttc.io/files/media/textsecure_002.png)

*Figure 1: TextSecure on the Google Play Store*

**Step 2:**. Before the installation process begins, you will be prompted to review the access that the application will have on your phone. Review this carefully. Once your are happy with the permissions that will be granted, press ![](/sites/siabnext.ttc.io/files/media/textsecure_003.png) and the installation will complete.  If you do not agree with the permissions that will be granted, press the back button and the installation will be cancelled.

![](/sites/siabnext.ttc.io/files/media/textsecure_004.png)

*Figure 2: Permissions required*

**Step 3.** **Tap** *Open* to run the app for the first time

# 3. Configuration and first-time setup





## 3.1 TextSecure Registration

**Step 1:** Begin the registration process by choosing the country your SIM card was purchased and entering your phone number and press ![](/sites/siabnext.ttc.io/files/media/textsecure_005.png)

**Step 2:** Verify that the number you entered is correct and press ![](/sites/siabnext.ttc.io/files/media/textsecure_006.png), otherwise press ![](/sites/siabnext.ttc.io/files/media/textsecure_007.png) and correct your phone number.


![](/sites/siabnext.ttc.io/files/media/textsecure_008.png) ![](/sites/siabnext.ttc.io/files/media/textsecure_009.png)

*Figure 3 & 4: Registration screen and confirming number*

**Step 3:** **TextSecure** will proceed with the registration. During this process you will receive one SMS to complete registration. 

**Note:** If for some reason you do not receive the SMS you will be given the option to receive an automated phone call where you will hear a 6-digit code, this code once entered will complete the registration.

![](/sites/siabnext.ttc.io/files/media/textsecure_010.png) ![](/sites/siabnext.ttc.io/files/media/textsecure_011.png)

*Figure 5 & 6: Registration completing and Voice verification screens*


## 3.2 Importing messages

As **TextSecure** can securely store your SMS messages, it is recommended that you import the messages from your current SMS app.

**Step 1:** After registration is complete, **TextSecure** will open and you will be presented with an option to import your messages from your current default SMS app. Press ![](/sites/siabnext.ttc.io/files/media/textsecure_012.png)

![](/sites/siabnext.ttc.io/files/media/textsecure_013.png) 

*Figure 7: Import messages into TextSecure*

Once the import process is complete you will have access to all your old messages via TextSecure and you should delete them from your other application.

## 3.3  Making TextSecure the default application

After your old messages have been imported you should make **TextSecure** the default SMS application, to ensure that all new incoming messages appear in it and not the old application. This can be done by tapping ![](/sites/siabnext.ttc.io/files/media/textsecure_012.png) when prompted.

![](/sites/siabnext.ttc.io/files/media/textsecure_014.png) 

*Figure 8: Set TextSecure as the default SMS application*

## 3.4 Encrypted Storage

Along with the ability to send encrypted messages, **TextSecure** also allows you to store all your messages in an encrypted container protected by a passphrase, so if someone gains access to your phone they will not be able to access your messages when **TextSecure** is locked.  After a set period of time, if you have not looked at any messages, **TextSecure** will automatically lock and you will have to enter your passphrase the next time you want to read your messages.


**Step 1:** Tap on ![](/sites/siabnext.ttc.io/files/media/textsecure_015.png) in the top right of your screen to bring up the menu and select ![](/sites/siabnext.ttc.io/files/media/textsecure_016.png).

**Step 2:** Scroll down to the *PASSPHRASE* section and uncheck **Disable Password**.

**Step 3:** When prompted enter a *passphrase* that will be used to protect the messages stored on your phone and tap ![](/sites/siabnext.ttc.io/files/media/textsecure_017.png).


![](/sites/siabnext.ttc.io/files/media/textsecure_018.png) ![](/sites/siabnext.ttc.io/files/media/textsecure_019.png) 

*Figure 9 & 10: passphrase options and setting a password*

**Step 4:** To have **TextSecure** automatically lock after a period of inactivity check the box next to **Timeout passphrase** (See *Fig 9* above).

**Step 5:** Tap **Timeout interval** and in the next screen enter the desired period of time you want **TextSecure** to lock if unused and tap ![](/sites/siabnext.ttc.io/files/media/textsecure_020.png). 

![](/sites/siabnext.ttc.io/files/media/textsecure_021.png) 

*Figure 11: TextSecure timeout settings*

# 4.Sending and Receiving messages

**Note:** To send encrypted messages to your contacts, they *must* also have **TextSecure** installed, otherwise the message will be sent  as an insecure SMS.

**TextSecure** can send messages as SMS using your mobile phone company to relay the message. With this option, even if your recipient is using **TextSecure** and the SMS is encrypted, your mobile phone company will know that you are sending a (encrypted) message to this particular recipient. If your phone is connected to the Internet, either using a data connection offered by your mobile phone company or using local wifi, **TextSecure** will instead send the message over an encrypted connection with a **WhisperSync** server. In this instance, your mobile phone company will not know who you are sending your messages to.


## 4.1 Messaging Individuals

**Step 1:** Open **TextSecure** and tap ![](/sites/siabnext.ttc.io/files/media/textsecure_022.png) at the top of your screen to bring up your contact list.

**Step 2:** Tap on the contact you wish to message.

**Note:** The contact list will display at the top all your contacts who also use **TextSecure** (under the **TextSecure  Users** heading) and then your full contact list (including TextSecure users) in the **All Contacts** section.

![](/sites/siabnext.ttc.io/files/media/textsecure_023.png) 

*Figure 1: TextSecure contact list*

**Step 3:** Compose your message in the box and tap ![](/sites/siabnext.ttc.io/files/media/textsecure_024.png) to send.

**Note** If you send a message to another **TextSecure** user and you are connected to the Internet, the default option is to send it via Internet. If you want to send an encrypted SMS (using your mobile phone company) or an insecure SMS instead of an encrypted message *long press* ![](/sites/siabnext.ttc.io/files/media/textsecure_024.png) to bring up the alternative sending options.

![](/sites/siabnext.ttc.io/files/media/textsecure_025.png) ![](/sites/siabnext.ttc.io/files/media/textsecure_026.png) 

*Figure 2 & 3: Sent message / Alternative sending options*

**Things You Should Know**

Your sent messages are given different background colours / indicators to help you identify how they were sent:

Blue with a ![](/sites/siabnext.ttc.io/files/media/textsecure_027.png) icon:  The message was sent encrypted via Internet.

![](/sites/siabnext.ttc.io/files/media/textsecure_028.png)

*Figure 4: Encrypted message send via mobile data*

Green with a ![](/sites/siabnext.ttc.io/files/media/textsecure_029.png) icon: The message was sent as an encrypted SMS.

![](/sites/siabnext.ttc.io/files/media/textsecure_030.png)

*Figure 5: Encrypted SMS*

Green: The message was sent as an insecure SMS.

![](/sites/siabnext.ttc.io/files/media/textsecure_031.png)

*Figure 6: Insecure SMS*

A ![](/sites/siabnext.ttc.io/files/media/textsecure_032.png) icon in your message indicates that it has been delivered. **Note:** the ![](/sites/siabnext.ttc.io/files/media/textsecure_032.png) only appears by default when messages are sent via Internet; to see them when sending SMS you need to enable **SMS delivery report** in **settings**.

The messages you receive from your contact will always be grey.  If they have a ![](/sites/siabnext.ttc.io/files/media/textsecure_033.png) icon, they were received encrypted. If there is no ![](/sites/siabnext.ttc.io/files/media/textsecure_033.png) icon the message was received insecurely.


## 4.2 Messaging Groups

**TextSecure** also allows you to message multiple people at once.

**Note:** If at least one of the people you are messaging does *not* use **TextSecure**, the messages will be sent as an MMS and **not** encrypted.

**Step 1:** Tap on ![](/sites/siabnext.ttc.io/files/media/textsecure_015.png) in the top right of your screen to bring up the menu and select ![](/sites/siabnext.ttc.io/files/media/textsecure_034.png).

**Step 2:** Enter a name for your chat group and tap ![](/sites/siabnext.ttc.io/files/media/textsecure_035.png) to add your contacts.

**Step 3:** Tap the box to the right of each contacts name to add them to the group and press ![](/sites/siabnext.ttc.io/files/media/textsecure_036.png).

![](/sites/siabnext.ttc.io/files/media/textsecure_037.png) ![](/sites/siabnext.ttc.io/files/media/textsecure_038.png)

*Figure 7 & 8: Contact selection & Group Creation*

**Step 4:** Tap ![](/sites/siabnext.ttc.io/files/media/textsecure_036.png) to complete the creation of the group and be brought back to the **TextSecure** main screen.

**Step 5:** Tap on the group you have created and begin messaging the group.

![](/sites/siabnext.ttc.io/files/media/textsecure_039.png)

*Figure 9: Group conversation*


## 4.3 Sending Files

**TextSecure** allows you to send images, video and audio files to your contact.

**Step 1:** Start a conversation with the person you want to send the file to.

**Step 2:** Tap on ![](/sites/siabnext.ttc.io/files/media/textsecure_015.png) in the top right of your screen to bring up the menu and select ![](/sites/siabnext.ttc.io/files/media/textsecure_040.png).

**Step 3:** Choose from the list the type of file that you want to send - Picture / Video / Audio

**Step 4:** Select the file you want to send.

**Step 5:** Verify that the file you want to send is in the compose window and press ![](/sites/siabnext.ttc.io/files/media/textsecure_024.png) to send.

![](/sites/siabnext.ttc.io/files/media/textsecure_041.png) ![](/sites/siabnext.ttc.io/files/media/textsecure_042.png)

*Figure 10 & 11: File type selection / Image sent to contact*


# 5. Verify the identity of your contact

To confirm that the messages you are sending and receiving are with the right person, you should both verify your **TextSecure** identities with each other.

## 5.1 Reading Fingerprints

The Following steps will need to be performed by both parties.

**Step 1:** Open an existing conversation with your contact and tap ![](/sites/siabnext.ttc.io/files/media/textsecure_043.png) at the top of the screen.

**Step 2:** Tap ![](/sites/siabnext.ttc.io/files/media/textsecure_044.png) from the pull-down menu.

**Step 3:** You will be presented with a 66-character fingerprint of your **TextSecure** identity and that of your contacts. These should be read to each other, and verify that you both have the same fingerprints for each other, either in person or via a medium that allows you to confirm visually or audibly to whom you are talking.

![](/sites/siabnext.ttc.io/files/media/textsecure_045.png) 

*Figure 12: TextSecure fingerprints*

## 5.2 Scanning Fingerprints

**Note:** To verify fingerprints by *scanning* you need to have [Barcode Scanner](https://play.google.com/store/apps/details?id=com.google.zxing.client.android) installed on your phone. If it is not available on your phone at the time of scanning **TextSecure** will download and install the app for you.

The Following steps will need to be performed by both parties.

**Step 1:** Open an existing conversation with your contact and tap ![](/sites/siabnext.ttc.io/files/media/textsecure_043.png) at the top of the screen.

**Step 2:** Tap ![](/sites/siabnext.ttc.io/files/media/textsecure_044.png) from the pull-down menu.

**Step 3:** You will be presented with a 66-character fingerprint of your **TextSecure** identity and that of your contacts. 

**Step 4** On both your phones tap on ![](/sites/siabnext.ttc.io/files/media/textsecure_046.png).

**Step 5:** On your phone tap ![](/sites/siabnext.ttc.io/files/media/textsecure_047.png) and your contact should tap ![](/sites/siabnext.ttc.io/files/media/textsecure_048.png). Your contact's phone will display a QR code and your phone will open **Barcode Scanner**.

**Step 6:** Use **Barcode Scanner** on your phone to scan your contact's *QR code*.

![](/sites/siabnext.ttc.io/files/media/textsecure_049.png) ![](/sites/siabnext.ttc.io/files/media/textsecure_050.png) 

*Figure 13 & 14: Your contact's QR code / Barcode scanner*

**Step 7:** Once the QR code has been successfully scanned **TextSecure** will check that the identity is valid.

![](/sites/siabnext.ttc.io/files/media/textsecure_051.png) 

*Figure 15: TextSecure identity verified*

**Step 8:** Once you have verified your contact's **TextSecure** identity, they should repeat the above steps to verify yours.


# 6. Export your messages

**Note:** While **TextSecure** allows you to export your messages, the  messages in the backup file will **not** be encrypted and you should take additional steps to protect its contents.



## 6.1 Exporting the messages

**Step 1:** Tap on ![](/sites/siabnext.ttc.io/files/media/textsecure_015.png) in the top right of the main **TextSecure** screen to bring up the menu and select ![](/sites/siabnext.ttc.io/files/media/textsecure_052.png).

**Step 2:** The next screen will open on the *import* options, tap ![](/sites/siabnext.ttc.io/files/media/textsecure_053.png).

**Step 3:** On the *export* screen tap ![](/sites/siabnext.ttc.io/files/media/textsecure_054.png).

**Step 4:** Confirm that you want to export the unencrypted messages to the storage on your phone by tapping ![](/sites/siabnext.ttc.io/files/media/textsecure_053.png).

**Step 5:** **TextSecure** will confirm the export has completed by displaying ![](/sites/siabnext.ttc.io/files/media/textsecure_055.png).  You will find a file called *Textsecure.xml* on your phone's storage that contains your **unencrypted** messages.

![](/sites/siabnext.ttc.io/files/media/textsecure_056.png) ![](/sites/siabnext.ttc.io/files/media/textsecure_057.png) 

*Figure 16 & 17: TextSecure Export and Export confirmation screens*
