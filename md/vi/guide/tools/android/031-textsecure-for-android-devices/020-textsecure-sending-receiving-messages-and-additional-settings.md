

---

lang: vi
community: guide
type: tools
legacy: True
child: True
os: android
weight: 2
depth: 3
title: TextSecure - Sending/Receiving Messages and Additional Settings

---

- [**3.0 Sending and Receiving messages**](#3.0)
    - [**3.0.1 Messaging Individuals**](#3.0.1)
    - [**3.0.2 Messaging Groups**](#3.0.2)
- [**3.1 Identity Verification**](#3.1)
    - [**3.1.1 Reading Fingerprints**](#3.1.1)
    - [**3.1.2 Scanning Fingerprints**](#3.1.2)
- [**3.2 Export your messages**](#3.2)

<a name="3.0"></a>
## 3.0 Sending and Receiving messages

**Note:** To send encrypted messages to your contacts, they *must* also have **TextSecure** installed, otherwise the message will be sent  as an insecure SMS.

**TextSecure** can send messages as SMS using your mobile phone company to relay the message. With this option, even if your recipient is using **TextSecure** and the SMS is encrypted, your mobile phone company will know that you are sending a (encrypted) message to this particular recipient. If your phone is connected to the Internet, either using a data connection offered by your mobile phone company or using local wifi, **TextSecure** will instead send the message over an encrypted connection with a **WhisperSync** server. In this instance, your mobile phone company will not know who you are sending your messages to.

<a name="3.0.1"></a>
## 3.0.1 Messaging Individuals

**Step 1:** Open **TextSecure** and tap ![](/sbox/screen/textsecure-en-1/022.png) at the top of your screen to bring up your contact list.

**Step 2:** Tap on the contact you wish to message.

**Note:** The contact list will display at the top all your contacts who also use **TextSecure** (under the **TextSecure  Users** heading) and then your full contact list (including TextSecure users) in the **All Contacts** section.

![](/sbox/screen/textsecure-en-1/023.png) 

*Figure 1: TextSecure contact list*

**Step 3:** Compose your message in the box and tap ![](/sbox/screen/textsecure-en-1/024.png) to send.

**Note** If you send a message to another **TextSecure** user and you are connected to the Internet, the default option is to send it via Internet. If you want to send an encrypted SMS (using your mobile phone company) or an insecure SMS instead of an encrypted message *long press* ![](/sbox/screen/textsecure-en-1/024.png) to bring up the alternative sending options.

![](/sbox/screen/textsecure-en-1/025.png) ![](/sbox/screen/textsecure-en-1/026.png) 

*Figure 2 & 3: Sent message / Alternative sending options*

**Things You Should Know**

Your sent messages are given different background colours / indicators to help you identify how they were sent:

Blue with a ![](/sbox/screen/textsecure-en-1/027.png) icon:  The message was sent encrypted via Internet.

![](/sbox/screen/textsecure-en-1/028.png)

*Figure 4: Encrypted message send via mobile data*

Green with a ![](/sbox/screen/textsecure-en-1/029.png) icon: The message was sent as an encrypted SMS.

![](/sbox/screen/textsecure-en-1/030.png)

*Figure 5: Encrypted SMS*

Green: The message was sent as an insecure SMS.

![](/sbox/screen/textsecure-en-1/031.png)

*Figure 6: Insecure SMS*

A ![](/sbox/screen/textsecure-en-1/032.png) icon in your message indicates that it has been delivered. **Note:** the ![](/sbox/screen/textsecure-en-1/032.png) only appears by default when messages are sent via Internet; to see them when sending SMS you need to enable **SMS delivery report** in **settings**.

The messages you receive from your contact will always be grey.  If they have a ![](/sbox/screen/textsecure-en-1/033.png) icon, they were received encrypted. If there is no ![](/sbox/screen/textsecure-en-1/033.png) icon the message was received insecurely.


<a name="3.0.2"></a>
## 3.0.2 Messaging Groups

**TextSecure** also allows you to message multiple people at once.

**Note:** If at least one of the people you are messaging does *not* use **TextSecure**, the messages will be sent as an MMS and **not** encrypted.

**Step 1:** Tap on ![](/sbox/screen/textsecure-en-1/015.png) in the top right of your screen to bring up the menu and select ![](/sbox/screen/textsecure-en-1/034.png).

**Step 2:** Enter a name for your chat group and tap ![](/sbox/screen/textsecure-en-1/035.png) to add your contacts.

**Step 3:** Tap the box to the right of each contacts name to add them to the group and press ![](/sbox/screen/textsecure-en-1/036.png).

![](/sbox/screen/textsecure-en-1/037.png) ![](/sbox/screen/textsecure-en-1/038.png)

*Figure 7 & 8: Contact selection & Group Creation*

**Step 4:** Tap ![](/sbox/screen/textsecure-en-1/036.png) to complete the creation of the group and be brought back to the **TextSecure** main screen.

**Step 5:** Tap on the group you have created and begin messaging the group.

![](/sbox/screen/textsecure-en-1/039.png)

*Figure 9: Group conversation*

<a name="3.0.3"></a>
## 3.0.3 Sending Files

**TextSecure** allows you to send images, video and audio files to your contact.

**Step 1:** Start a conversation with the person you want to send the file to.

**Step 2:** Tap on ![](/sbox/screen/textsecure-en-1/015.png) in the top right of your screen to bring up the menu and select ![](/sbox/screen/textsecure-en-1/040.png).

**Step 3:** Choose from the list the type of file that you want to send - Picture / Video / Audio

**Step 4:** Select the file you want to send.

**Step 5:** Verify that the file you want to send is in the compose window and press ![](/sbox/screen/textsecure-en-1/024.png) to send.

![](/sbox/screen/textsecure-en-1/041.png) ![](/sbox/screen/textsecure-en-1/042.png)

*Figure 10 & 11: File type selection / Image sent to contact*

<a name="3.1"></a>
## 3.1 Identity Verification

To confirm that the messages you are sending and receiving are with the right person, you should both verify your **TextSecure** identities with each other.

<a name="3.1.1"></a>
## 3.1.1 Reading Fingerprints

The Following steps will need to be performed by both parties.

**Step 1:** Open an existing conversation with your contact and tap ![](/sbox/screen/textsecure-en-1/043.png) at the top of the screen.

**Step 2:** Tap ![](/sbox/screen/textsecure-en-1/044.png) from the pull-down menu.

**Step 3:** You will be presented with a 66-character fingerprint of your **TextSecure** identity and that of your contacts.  These should be read to each other, and verify that you both have the same fingerprints for each other, either in person or via a medium that allows you to confirm visually or audibly to whom you are talking.

![](/sbox/screen/textsecure-en-1/045.png) 

*Figure 12: TextSecure fingerprints*

<a name="3.1.2"></a>
## 3.1.2 Scanning Fingerprints

**Note:** To verify fingerprints by *scanning* you need to have [Barcode Scanner](https://play.google.com/store/apps/details?id=com.google.zxing.client.android) installed on your phone. If it is not available on your phone at the time of scanning **TextSecure** will download and install the app for you.

The Following steps will need to be performed by both parties.

**Step 1:** Open an existing conversation with your contact and tap ![](/sbox/screen/textsecure-en-1/043.png) at the top of the screen.

**Step 2:** Tap ![](/sbox/screen/textsecure-en-1/044.png) from the pull-down menu.

**Step 3:** You will be presented with a 66-character fingerprint of your **TextSecure** identity and that of your contacts. 

**Step 4** On both your phones tap on ![](/sbox/screen/textsecure-en-1/046.png).

**Step 5:** On your phone tap ![](/sbox/screen/textsecure-en-1/047.png) and your contact should tap ![](/sbox/screen/textsecure-en-1/048.png). Your contact's phone will display a QR code and your phone will open **Barcode Scanner**.

**Step 6:** Use **Barcode Scanner** on your phone to scan your contact's *QR code*.

![](/sbox/screen/textsecure-en-1/049.png) ![](/sbox/screen/textsecure-en-1/050.png) 

*Figure 13 & 14: Your contact's QR code / Barcode scanner*

**Step 7:** Once the QR code has been successfully scanned **TextSecure** will check that the identity is valid.

![](/sbox/screen/textsecure-en-1/051.png) 

*Figure 15: TextSecure identity verified*

**Step 8:** Once you have verified your contact's **TextSecure** identity, they should repeat the above steps to verify yours.

<a name="3.2"></a>
## 3.2 Export your messages

**Note:** While **TextSecure** allows you to export your messages, the  messages in the backup file will **not** be encrypted and you should take additional steps to protect its contents.

**Step 1:** Tap on ![](/sbox/screen/textsecure-en-1/015.png) in the top right of the main **TextSecure** screen to bring up the menu and select ![](/sbox/screen/textsecure-en-1/052.png).

**Step 2:** The next screen will open on the *import* options, tap ![](/sbox/screen/textsecure-en-1/053.png).

**Step 3:** On the *export* screen tap ![](/sbox/screen/textsecure-en-1/054.png).

**Step 4:** Confirm that you want to export the unencrypted messages to the storage on your phone by tapping ![](/sbox/screen/textsecure-en-1/053.png).

**Step 5:** **TextSecure** will confirm the export has completed by displaying ![](/sbox/screen/textsecure-en-1/055.png).  You will find a file called *Textsecure.xml* on your phone's storage that contains your **unencrypted** messages.

![](/sbox/screen/textsecure-en-1/056.png) ![](/sbox/screen/textsecure-en-1/057.png) 

*Figure 16 & 17: TextSecure Export and Export confirmation screens*

