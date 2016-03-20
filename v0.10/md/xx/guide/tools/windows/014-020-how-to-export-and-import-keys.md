

---

lang: xx
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Export and Import Keys

---

List of sections on this page:

- [**3.1 How to Export Your Public Key with gpg4usb**](#3.1)
- [**3.2 How to Import a Correspondent's Public Key with gpg4usb**](#3.2)
- [**3.3 How to Verify a Public Key using gpg4usb**](#3.3)

<a name="3.1"></a>
## 3.1 How to Export Your Public Key with gpg4usb ##

You must send your public key to your correspondent before they can send encrypted messages to you. 

To export your public key with **gpg4usb**, perform the following steps:

**Step 1**. **Double click** ![](/sbox/screen/gpg4usb-en-1/02.png) to open the **gpg4usb** folder.

**Step 2**. **Double click** ![](/sbox/screen/gpg4usb-en-1/03.png) to open **gpg4usb** program 

**Step3**. **Click** ![](/sbox/screen/gpg4usb-en-1/10a.png) to activate the following screen:

![](/sbox/screen/gpg4usb-en-1/10.png)

*Figure 1: The Keymanagement window displaying all the key pairs*

**Step 3**. **Check** your own key, as shown in *Figure 1* above.

**Step 4**. **Select** the *Export To File* item from the **Key** menu as shown below:

![](/sbox/screen/gpg4usb-en-1/11.png)

*Figure 2: The Keymanagement window with the Export To File item selected*

This will activate the following screen:

![](/sbox/screen/gpg4usb-en-1/12.png)

*Figure 3: The Export To Folder browse window*

**Step 5**. **Click** ![](/sbox/screen/gpg4usb-en-1/13.png) to save your key pair to the **gpg4usb** program folder.

**Step 6**: **Send** the exported file with your public key as an attachment to your correspondent.

<a name="3.2"></a>
## 3.2 How to Import a Correspondent's Public Key with gpg4usb ##

Before you can encrypt information and send it to your correspondent, you need to receive and import their public key. To import a correspondent's Public key using **gpg4usb**, perform the following steps:

**Step 1**. **Double click** ![](/sbox/screen/gpg4usb-en-1/03.png) to open the **gpg4usb** program.

**Step 2**. **Click** ![](/sbox/screen/gpg4usb-en-1/14.png) Import to activate the following screen:

![](/sbox/screen/gpg4usb-en-1/15.png)

*Figure 4: The Import Key dialog box*

**Step 3**. **Browse** and select the key you wish to import.

![](/sbox/screen/gpg4usb-en-1/16a.png)

*Figure 5: Open Key*

**Step 4**. **Click** Open to activate following window.

![](/sbox/screen/gpg4usb-en-1/16b.png)

*Figure 6: Key Import Details*

**Step 5**. **Click** OK to close above window and come back to **gpg4usb** main window. It will display newly imported public key as below.

![](/sbox/screen/gpg4usb-en-1/16.png)

*Figure 7: The gpg4usb console displaying the newly imported public key associated with your correspondent's account*

Now that you have successfully imported a correspondent's public key, you must now verify and sign that imported key.

<a name="3.3"></a>
## 3.3 How to Verify a Key Pair Using gpg4usb ##

You must verify that the imported key truly belongs to the person who purportedly sent it and then verify it as being authentic. This is an important step that both you and your email contacts should follow for each public key that you receive.

To verify a key pair, perform the following steps:

**Step 1**. **Contact** your correspondent through some means of communication other than email. 

**Note**: You may use a telephone, text messages, **Voice over Internet Protocol** (**VoIP**) or any other method, but only if you are certain that you are really communicating with the right person. As a result, telephone conversations and face-to-face meetings provide the greatest assurance of the authenticity of a person's identity, if or when they can be arranged safely.

**Step 2**. You and your correspondent should verify that the 'fingerprints' of the public keys that you have exchanged are the same.  

**Note**: A fingerprint is a unique series of numbers and letters that identifies each key. The fingerprint itself is not a secret, and can be recorded and used for verification later if or when required.

To view the fingerprint of key pairs you have created or public keys you have imported, perform the following steps:

**Step 1**. **Select** a key, then **right-click** it to activate its associated pop-up menu.

**Step 2**. **Select** the *Show Keydetails* item as shown below in *Figure 8*. 

![](/sbox/screen/gpg4usb-en-1/17.png)

*Figure 8: The pop-up menu associated with a correspondent's key*

This will activate the following screen:

![](/sbox/screen/gpg4usb-en-1/18.png)

*Figure 9: The Keydetails window with the key fingerprint on the bottom*

**Step 3**. **Compare** this fingerprint with the one your correspondent see in her **gpg4usb** program.

Your correspondent should repeat these steps. Confirm with each other that the fingerprint for the key each of you have exchanged matches the sender's original. If they don't match, exchange your public keys again (perhaps over different email address or communication method) and repeat the verification process.

If the fingerprints match each other *exactly*, then you are ready to securely send encrypted messages and files between each others.

