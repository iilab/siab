

---

lang: ru
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: How to Use Enigmail with GnuPG in Thunderbird

---

List of sections on this page:

- [**4.0 An Overview of Enigmail, GnuPG and Private-Public Key Encryption**](#4.0)
- [**4.1 How to Install Enigmail and GnuPG**](#4.1)
- [**4.2 How to Generate Key Pairs and Configure Enigmail to Work with Your Email Accounts**](#4.2)
- [**4.3 How to Exchange Public Keys**](#4.3)
- [**4.4 How to Validate and Sign a Key Pair**](#4.4)
- [**4.5 How to Encrypt and Decrypt a Message**](#4.5)


<a name="4.0"></a>
## 4.0 An Overview of GnuPG, Enigmail and Private-Public Key Encryption ##

**Enigmail** is a **Mozilla Thunderbird** add-on that lets you protect the privacy of your email communication. **Enigmail** is an interface that lets you use **GnuPG** encryption program from within **Thunderbird**.  The **Engimail** interface is represented as *Enigmail* in the **Thunderbird** console tool bar. 

**Engimail** is based on [**public-key cryptography**](http://en.wikipedia.org/wiki/Public-key_cryptography).
In this method, each individual must generate her/his own personal key pair. The first key is known as the *private key*. It is protected by a password or passphrase, both to be guarded and *never* shared with *anyone*. 

The second key is known as the *public key*. This key can be shared with any of your correspondents. Once you have a correspondent’s *public key* you can begin sending encrypted emails to this person. Only she will be able to decrypt and read your emails, because she is the only person who has access to the matching *private key*.

Similarly, if you send a copy of your own *public key* to your email contacts and keep the matching *private key* secret, only you will be able to read encrypted messages from those contacts.

**Enigmail** also lets you attach *digital signatures* to your messages. The recipient of your message who has a genuine copy of your *public key* will be able to verify that the email comes from you, and that its content was not tampered with on the way. Similarly, if you have a correspondent's *public key*, you can verify the digital signatures on her signed messages.

<a name="4.1"></a>
## 4.1 How to Install Enigmail and GnuPG ##

Please refer to the [**download section**](/en/thunderbird_main) for instructions on how to download **Enigmail** and **GnuPG**.

### 4.1.1 How to Install GnuPG ###

Installing **GnuPG** is quite straightforward, and resembles other software installations you may have performed and can be done by doing the following steps: 

**Step 1**. **Double click** ![](/sbox/screen/thunderbird-en-1/40.png) to to begin the installation process. The *Open File - Security Warning* dialog box may appear. If it does, **click** ![](/sbox/screen/thunderbird-en-1/02.png) to activate the following screen:

![](/sbox/screen/thunderbird-en-1/41.png)

*Figure 1: GNU Privacy Guard Setup Wizard*

**Step 2**. **Click** ![](/sbox/screen/thunderbird-en-1/04.png) to activate the *GNU Privacy Guard Setup - License Agreement* window; after you have completed reading it, **click** ![](/sbox/screen/thunderbird-en-1/04.png) to activate the *GNU Privacy Guard Setup - Choose Components* window.

**Step 3**. **Click** ![](/sbox/screen/thunderbird-en-1/04.png) to accept the default settings and activate the *GNU Privacy Guard Setup - Install Options - GnuPG Language Selection* window. 

**Step 4**. **Click** ![](/sbox/screen/thunderbird-en-1/04.png) to accept *en-English* as the default language, and activate the *Choose Install Location* window.

**Step 5**. **Click** ![](/sbox/screen/thunderbird-en-1/06.png) to accept the default installation path and activate the *Choose Start Menu Folder* screen.

**Step 6**. **Click** ![](/sbox/screen/thunderbird-en-1/06.png) begin unpacking and installing various **GnuPG** packages. After this process has completed itself, the *Installation Complete* screen will appear.

**Step 7**. **Click** ![](/sbox/screen/thunderbird-en-1/04.png) and then ![](/sbox/screen/thunderbird-en-1/08.png) to complete installing the **GnuPG** program.

<a name="4.1.2"></a>
### 4.1.2 How to Install the Enigmail Add-on ###

After you have successfully installed the **GnuPG** software you are now ready to install the **Enigmail** add-on. 

To begin installing **Enigmail**, perform the following steps: 

 **Step 1**. **Open Thunderbird**, then **click** ![](/sbox/screen/thunderbird-en-1/24a.png) to display the *Thunderbird Menu* and **select Add-ons** to activate the *Add-ons Manager* window

**Step 2**. **Click** ![](/sbox/screen/thunderbird-en-1/44.png) in the left hand sidebar - If the Enigmail Add-on has not yet been detected, you will see the message *You do not have any Add-ons of this type installed*   

**Step 3**. If the Enigmail Add-on appears in the main *Extensions* panel **click** ![](/sbox/screen/thunderbird-en-1/46.png). If it does not appear, **click** ![](/sbox/screen/thunderbird-en-1/45a.png) and  **select** *Install Add-on from File* as shown below: 

![](/sbox/screen/thunderbird-en-1/46a.png)

*Figure 3: Tools for All Add-ons menu*

**Step 4**. Navigate to the folder where you have saved the Enigmail extension (most probably your *Downloads* folder) as shown in the following screen:

![](/sbox/screen/thunderbird-en-1/47.png)

*Figure 4: The Select an extension to install*

**Step 5**.  **Click** ![](/sbox/screen/thunderbird-en-1/48.png) to activate the following screen:

![](/sbox/screen/thunderbird-en-1/49.png)

*Figure 5: The Software Installation window*

**Important**: Before you perform step 6, make sure all your online work has been saved!

**Step 6**. **Click** ![](/sbox/screen/thunderbird-en-1/50.png) and then **click** ![](/sbox/screen/thunderbird-en-1/51.png) to complete the **Enigmail** add-on installation. 

To verify your installation of the **Enigmail** add-on was successful, return to the **Thunderbird** main user interface, **click** on ![](/sbox/screen/thunderbird-en-1/24a.png) and check if *Enigmail* appears as one of the option, as follows: 

![](/sbox/screen/thunderbird-en-1/52.png)

*Figure 6: The Thunderbird toolbar with Enigmail highlighted*

### 4.1.3 How to Confirm that Enigmail and GnuPG are Working ###

Before you can begin using **Enigmail** and **GnuPG** to authenticate and encrypt your emails, you must first ensure that they are both communicating with each other.

**Step 1**. **Select Enigmail > Preferences** to display the *Enigmail Preferences* screen as follows:

![](/sbox/screen/thunderbird-en-1/53.png)

*Figure 7: The Enigmail Preferences window*

If **GnuPG** has been successfully installed, the ![](/sbox/screen/thunderbird-en-1/54.png) will be visible in the *Files and Directories* section; otherwise, you may receive a pop-up alert resembling the following:

![](/sbox/screen/thunderbird-en-1/55.png)

*Figure 8: The Enigmail Alert pop-up message*

**Tip**: If you have received this message, it may indicate that you did not install **GnuPG** or you have installed it in different location. If you installed **GnuPG** in a different location, **check** the *Override with* option to enable the *Browse...* button, and then **click** ![](/sbox/screen/thunderbird-en-1/69.png) to activate the *Locate GnuPG program* and manually navigate to the location of the *gpg.exe* file on your computer, otherwise please go back to [4.1 How to Install Enigmail and GnuPG](#4.1).

**Step 2**. **Click** ![](/sbox/screen/thunderbird-en-1/35.png) to return to the **Thunderbird** console.

<a name="4.2"></a>
## 4.2 How to Generate Key Pairs and Configure Enigmail to Work with Your Email Accounts ##

Once you have confirmed that **Enigmail** and **GnuPG** are working properly, you can configure one or more of your email accounts to use **Enigmail** to generate one or more private/public key pairs.

### 4.2.1 How to Use the Enigmail Wizard to Generate a Key Pair ###

**Engimail** provides two ways of generating a private-public key pair; the first uses the *Enigmail Setup Wizard* and the second uses the *Key Management* screen. 

To generate a key pair for the first time using the *Enigmail Setup Wizard*, perform the following steps:

**Step 1**. If **Setup Wizard** window is not already activated **select Enigmail > Setup Wizard** to open the *Enigmail Setup Wizard* screen as follows: 

![](/sbox/screen/thunderbird-en-1/56.png)

*Figure 9: The Welcome to the Enigmail Setup Wizard screen*

**Step 2**. **Click** ![](/sbox/screen/thunderbird-en-1/04.png) to activate the following screen. *Note - this screen will only appear if you have set up key pairing for another account*

![](/sbox/screen/thunderbird-en-1/59.png)

*Figure 10: The Select Identities screen*

**Step 3**. **Click** ![](/sbox/screen/thunderbird-en-1/04.png) to activate the following screen:

![](/sbox/screen/thunderbird-en-1/60.png)

*Figure 11: The Encryption - Encrypt Your Outgoing Emails screen*

**Step 4**. **Click** ![](/sbox/screen/thunderbird-en-1/04.png) to activate the following screen:

![](/sbox/screen/thunderbird-en-1/61.png)

*Figure 12: The Signing - Digitally Sign Your Outgoing Emails screen*

**Step 5**. **Click** ![](/sbox/screen/thunderbird-en-1/04.png) to activate the following screen:

![](/sbox/screen/thunderbird-en-1/62.png)

*Figure 13: The Preferences - Change Your Email Settings to Make Enigmail Work More Reliably screen*

**Step 6**. **Click** ![](/sbox/screen/thunderbird-en-1/04.png) to activate the *Create Key - Create A Key To Sign and Encrypt Email* window. 

**Note**: The first time you attempt to create a key for an email account, the *No OpenPGP Key Found* screen will appear. 

**Step 7**. **Select** *I want to create a new key pair for signing and encrypting my email*

**Step 8**. **Type** a strong passphrase into both the *Password* fields

![](/sbox/screen/thunderbird-en-1/65.png)

*Figure 15: The Create Key - Create A Key To Sign and Encrypt Email window*

**Step 9**. **Click** ![](/sbox/screen/thunderbird-en-1/04.png) to activate the *Summary* screen, which displays the settings used while generating the key pair.

**Step 10**. **Click** ![](/sbox/screen/thunderbird-en-1/04.png) to start the key pair generation, as shown in the following screen:

![](/sbox/screen/thunderbird-en-1/67.png)

*Figure 16: Key Generation - You key is now being generated window*

**Note**: Any key pair generated using *Enigmail Setup Wizard* is automatically has a 4096-bit size, and a lifespan of 5 years.

**Step 11**. After the key is generated, you will be prompted to create a revocation certificate. **Click** ![](/sbox/screen/thunderbird-en-1/76.png) as shown in the following screen:

![](/sbox/screen/thunderbird-en-1/68.png)

*Figure 17: The Enigmail Prompt confirmation*

**Note**: If you know that a hostile or malicious party has gained unauthorised access to your private key or you lost access to this key, you may send the revocation certificate to your contact to let them know that they should not use your matching public key. Keep in mind that you might need to do this if your computer is lost, stolen or confiscated. You are strongly advised to back up and protect your revocation certificate.

**Step 12**. You will be asked to **type in** the password that you associated with your newly created key. And then **navigate** to a location where you can store the certificate safely and **click** ![](/sbox/screen/thunderbird-en-1/78.png) on following screen:

![](/sbox/screen/thunderbird-en-1/70.png)

*Figure 18: Create & Save Revocation Certificate*

**Step 13**. **Click** ![](/sbox/screen/thunderbird-en-1/04.png) to complete generating both a key pair and revocation certificate.

### 4.2.2 How to Generate Additional Key Pairs and Revocation Certificates for another Email Account ###

It is a common practice to have a separate key pair for each email account. Using the same key pair for many email accounts is possible, but may be confusing for your contacts. It is possible to add more than one email account to a single key pair (we do not discuss it in this chapter) what brings some usability benefits, but also associates all those email accounts to one person which may not be desirable.

Follow the steps below if you want to generate additional key pairs for your other email accounts.

**Step 1**. **Select Enigmail > Key Management** to activate the following screen:

![](/sbox/screen/thunderbird-en-1/71.png)

*Figure 19: The Enigmail Key Management Generate menu with New Key Pair item selected*

**Note**: **Check** the *Display All Keys by Default* to view the key pair generated by using the *OpenPGP Setup Wizard* for your first email account, as presented in *figure 19* above and *figure 23* below.

**Step 2**. **Select Generate > New Key Pair** from the *Key Management* as displayed in *figure 19* above to activate the following screen: 

![](/sbox/screen/thunderbird-en-1/72.png)

*Figure 20: The Generate OpenPGP Key screen*

**Step 3**. **Select** an email account from the *Account / User ID* drop-down list, **check** the *Use generated key for the selected identity* option. And create a passphrase to protect your private key.

**Note**: As its name implies, a passphrase is simply a longer password. **Enigmail** is simply prompting you to enter a password that is longer and more secure than a conventional one.

**Important**: Always generate key-pairs with a passphrase, and **never** enable the "no passphrase" option.

![](/sbox/screen/thunderbird-en-1/73.png)

*Figure 21: The Generate OpenPGP Key displaying the Key Expiry tab*

**Note**: The length of time for which a key pair remains valid depends entirely on your privacy and security needs; the more frequently you change your key pairs, the more difficult it becomes for the new key pair to be compromised. However, every time you change key pair you will need to send the new public key to your correspondents, and verify it with each of them.

**Step 4**. **Type** in the appropriate number, and then **select** the desired unit of time (*days*, *months* or *years*) for which the key pair will remain valid. 

**Step 5**. **Click** ![](/sbox/screen/thunderbird-en-1/74.png) to activate the Enigmail Confirm window.

**Step 6**. You will be prompted to generate a certificate as shown in *figure 17*.

**Step 7**. **Click** ![](/sbox/screen/thunderbird-en-1/76.png) to activate the *Create & Save Revocation Certificate* navigation window.

**Note**: If you know that a hostile or malicious party has gained unauthorised access to your private key or you lost access to this key, you may send the revocation certificate to your contact to let them know that they should not use your matching public key. Keep in mind that you might need to do this if your computer is lost, stolen or confiscated. You are strongly advised to back up and protect your revocation certificate.

**Step 8**. Browse to a safe location to store the certificate as shown in the screen below and **click** ![](/sbox/screen/thunderbird-en-1/78.png). You will be then prompted to enter passphrase that you associated with your newly created key.

![](/sbox/screen/thunderbird-en-1/77.png)

*Figure 22: The Create & Save Revocation Certificate*

**Step 9**. **Click** ![](/sbox/screen/thunderbird-en-1/35.png) to complete generating both a key pair and revocation certificate, and return to the following screen:

![](/sbox/screen/thunderbird-en-1/79.png) 

*Figure 23: The Enigmail Key Management window with the key pair displayed*

**Note**: **Check** the *Display All Keys by Default* option to display all the key pairs and their associated accounts. Make sure you are in a safe environment to do this.

After you have successfully generated both your key pair and its associated revocation certificate, you are now ready to exchange public keys with a trusted correspondent.

### 4.2.3 How to Configure Enigmail for Use with Your Email Account ###

To enable **Enigmail** for use with a specific email account, perform the following steps:

**Step 1**.  **Click** ![](/sbox/screen/thunderbird-en-1/24a.png) to display the *Thunderbird Menu* and **select Options > Account Settings**.

**Step 2**. **Select** the *OpenPGP Security* menu item in the sidebar as follows: 

![](/sbox/screen/thunderbird-en-1/80.png)

*Figure 24: The Account Settings - OpenPGP Security screen*

**Step 3**. **Check** the *Enable OpenPGP support* option and **select** the *Use email address of this identity to identify OpenPGP key* option.

**Step 4**. **Click** ![](/sbox/screen/thunderbird-en-1/35.png) to return to the **Thunderbird** console. 

<a name="4.3"></a>
## 4.3 How to Exchange Public Keys ##

Before you can begin sending encrypted email messages to one another, you and your correspondents must exchange public keys. You must also confirm the validity of any key you accept by confirming that it really belongs to its purported sender. 

### 4.3.1 How to Send a Public Key using Enigmail ###

To send a public key using **Enigmail** both your correspondent and you will perform the following steps:

**Step 1**. **Open Thunderbird** and then **click** ![](/sbox/screen/thunderbird-en-1/81.png) to write a new message.

**Step 2**. Select the menu option **Enigmail > Attach My Public Key**.

**Note**: In this method, the **Attachments:** pane is not displayed immediately; it will appear as soon as you send the message.

If you would like to send a different public key, **select** the menu option **Enigmail > Attach Public Key...** and then **select** the key you would like to send.

![](/sbox/screen/thunderbird-en-1/82.png) 

*Figure 25: The Write message pane displaying the attached public key in the Attachments pane.*

**Step 3**. **Click** ![](/sbox/screen/thunderbird-en-1/83.png) to send your email with your attached public key. 

### 4.3.2 How to Import a Public key using Enigmail ###

Both your correspondent and you will perform the same steps when importing each other's public keys.

**Step 1**. **Select** and **open** the email containing your correspondent's public key. The attachment will appear similar to the following: ![](/sbox/screen/thunderbird-en-1/87.png)

**Step 2**. **Click** on the attached file above ![](/sbox/screen/thunderbird-en-1/87a.png). **Enigmail** detects a message containing a public key and it will prompt you to import the key as follows:

![](/sbox/screen/thunderbird-en-1/88.png)

*Figure 26: The Enigmail Confirm Import public key* 

**Step 3**. **Click** ![](/sbox/screen/thunderbird-en-1/89.png) to import your correspondent's public key.

If you have successfully imported the public key, a message resembling the following will appear:

![](/sbox/screen/thunderbird-en-1/90.png)

*Figure 27: The Enigmail Alert screen displays the correspondent's public key*

To confirm that you have successfully imported your correspondent's public key, perform the following step:

**Step 1**. **Select Enigmail > Key Management** to display the *Enigmail Key Management* screen as follows:

![](/sbox/screen/thunderbird-en-1/91.png)

*Figure 28: The Enigmail - Key Management displaying a recently imported public key* 

**Note** that option *Display All Keys by Default* needs to be selected to be able to see the keys
<a name="4.4"></a>
## 4.4 How to Validate and Sign a Key Pair ##

Finally, you must verify that the imported key truly belongs to the person who purportedly sent it, then confirm its 'validity'. This is an important step that both you and your email contacts should follow for each public key that you receive. 

### 4.4.1 How to Validate a Key Pair ###

**Step 1**. **Contact** your correspondent through some means of communication other than email. You can use a telephone, text messages, **Voice over Internet Protocol** (**VoIP**) or any other method, but
you **must** be absolutely certain that you are really talking to the right person. As a result, voice or video conversations and face-to-face meetings work best, if they are convenient and if they can be arranged safely. 

**Step 2**. Both you and your correspondent should verify the 'fingerprints' of the public keys that you have exchanged. A fingerprint is a unique series of numbers and letters that identifies each key. You can use the **Enigmail** *Key Management* screen to view the fingerprint of key pairs you have created and public keys you have imported. 

To view the fingerprint of a particular key pair, perform the following steps:

**Step 1**. **Select Enigmail > Key Management** and then **right-click** on a particular key to activate the pop-up menu: 

![](/sbox/screen/thunderbird-en-1/92.png) 

*Figure 29: The Enigmail Key Management menu with the Key Properties item selected*

**Step 2**. **Select** the *Key Properties* item to activate the following screen: 

![](/sbox/screen/thunderbird-en-1/93.png)

*Figure 30: The Key Properties screen*

Your correspondent should repeat these steps. To confirm fingerprints, read fingerprint of your key to your contact and have them verify that the fingerprint they see on your public key they received matches. Then have your contact do the same for their key's fingerprint. If fingerprints don't match, exchange public keys again and repeat the validation process.

**Note**: The fingerprint itself is not a secret and can be recorded for later verification at your convenience.

### 4.4.2 How to Sign a Valid Public Key ###

After you have verified given correspondent's key, you can *sign* it, to confirm that you consider this key valid.
Signing keys may expose a connection between you and your corespondent when you send signed key to somebody else or export it to the key server. To prevent this from happening always select option *Local signature* below.

To sign a properly validated public key, perform the following steps:

**Step 1**. **Select Enigmail > Key Management** to open the *Key Management* screen.

**Step 2**. **Right-click** your correspondent's public key from the *Key Management* screen (see figure 29 above) and **select** the *Sign Key* item from the menu to activate the following screen:

![](/sbox/screen/thunderbird-en-1/94.png)

*Figure 31: The Enigmail - Sign Key screen*

**Step 3**. **Check** the *I have done very careful checking* option, **select** *Local signature (cannot be exported)*, and then **click** ![](/sbox/screen/thunderbird-en-1/35.png) to sign your correspondent's public key. You may be asked to provide password to your private key. 

#### 4.4.3 How to Manage Your Key Pairs ####

The *Enigmail Key Management* window is used to generate, validate and sign different key pairs. However, you may also perform other tasks by related to key management among them (see figure 29 above): 

- **Manage User IDs** lets you associate more than one email address to a single key pair.
- **Change Expiration Date** lets you change expiration date of your key pair.
- **Change Passphrase** lets you change the password protecting your key pair.
- **Generate & Save Revocation Certificate** lets you generate a new revocation certificate, if you have lost or misplaced the one you created earlier. 

<a name="4.5"></a>
## 4.5 How to Encrypt and Decrypt Email Messages ##

**Important**: The header of any email message - that is its *Subject* and intended recipients including any information in the *To*, *CC* and *BCC* fields - *cannot* be encrypted and will be sent in open text. To ensure the privacy and security of your email exchanges, the subject of your email should be kept non-descriptive not to reveal sensitive information. In addition, you are advised to put all addresses in the *BCC* field when sending emails to a group of people.

When encrypting email messages with attachments, we strongly recommend using the **PGP/MIME** option, as this will extend encryption to include any files and file names attached to your email.

Note that any encrypted email you send with Thunderbird/Enigmail/GnuPG is automatically encrypted to your key along with the chosen recipients of this email, so you are able to decrypt emails in your sent folder.

### 4.5.1 How to Encrypt a Message ###

Once both you and your correspondent have successfully imported and validated and signed each other's public keys, you are ready to begin sending encrypted messages and decrypting received ones.

To encrypt the contents of you email message to your correspondent, perform the following steps:

**Step 1**. **Open** **Thunderbird** and **click** ![](/sbox/screen/thunderbird-en-1/81.png) to write an email.

**Step 2**. To Encrypt the message **click** *Enigmail -> Message will not be encrypted* and **select** *Force Encryption* as shown in the follow screen:

![](/sbox/screen/thunderbird-en-1/84.png) 

*Figure 33: The Force Encryption option*

**Step 3**. To Sign the message **click** *Enigmail -> Message will not be signed* and **select** *Force Sign* 

**Note**: To verify that your message will be both encrypted and signed, check that the following two icons appear **highlighted** at the bottom right corner of the message pane as follows:

![](/sbox/screen/thunderbird-en-1/85.png) 

*Figure 34: Encryption and Signed enabled*

**Step 4**. **Click** ![](/sbox/screen/thunderbird-en-1/83.png) to send the message. You may be prompted for password to use your private key to sign the message.

**Optional step 5**. If you are attaching any file to your message, you may need to **select** the option *Encrypt/sign message as a whole and send it using PGP/MIME* and **click** OK button, in the following screen: 

 ![](/sbox/screen/thunderbird-en-1/86.png) 

*Figure 35:  The Enigmail Prompt screen*

**Note: When you *encrypt each attachment separately* (second option in the figure 35 above) names of the attached files are not encrypted and are being send in clear text! This may result in leaking sensitive information! Using PGP/MIME ensures that all email text, attached files and their names are encrypted and hidden.**

### 4.5.2 How to Decrypt a Message ###

When you receive and open an encrypted message, **Enigmail/OpenPGP** will automatically attempt to decrypt the message when you receive and open it. 
If it does not, select the *Decrypt* button.
This will activate the following screen:

![](/sbox/screen/thunderbird-en-1/96.png)

*Figure 36: The Enigmail Prompt - Please type in your OpenPGP passphrase or your SmartCard PIN*

**Step 1**. **Enter** your passphrase as shown above.

After you have entered your private key passphrase, the message is decrypted and displayed as follows:

![](/sbox/screen/thunderbird-en-1/97.png)

*Figure 37: The newly decrypted message in the message pane.*

You have now successfully decrypted this message. By repeating the steps described in section **4.5 How to Encrypt and Decrypt Email Messages** every time you and your correspondent exchange messages, you can maintain a private, authenticated channel of communication, regardless of who might be attempting to monitor your email exchanges.

### 4.5.3 Extending Security Options###

When using *Enigmail and GnuPG* to secure your privacy it is very important to ensure that **every** email you send is encrypted. This particularly includes replies to encrypted emails, drafts of email you would like to encrypt and quotes from previously encrypted emails. 

**Always enable message encryption (as in the section *4.5.1 How to Encrypt a Message* above) before you start writing it**. In this way you ensure that drafts of the message will only be written to the email server in encrypted form.

We also strongly recommend to **configure Enigmail to alert you before sending an unencrypted email**. The steps below show how to do this:

**Step 1**. **Click** *Enigmail > Preferences* menu and **select** the *Sending* tab.

**Step 2**. **Select** from the *Confirm before sending* - *If unencrypted*  and click OK 

![](/sbox/screen/thunderbird-en-1/99.png)

*Figure 38: Enigmail Preferences - Confirm before sending*

For every unencrypted email you send now you will be alerted that the email will be send unencrypted as shown below. If you intend to send the email encrypted, **click** *Cancel* and follow steps in section 4.5.1 above.
 
![](/sbox/screen/thunderbird-en-1/98.png)

*Figure 39: Enigmail Confirm*

**Note again that** the *Subject, To, CC* and *BCC* fields are **never** encrypted.

