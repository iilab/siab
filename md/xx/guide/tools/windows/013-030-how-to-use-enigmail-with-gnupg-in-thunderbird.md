

---

lang: xx
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
- [**4.5 How to Send and Receive Encrypted Emails**](#4.5)

<a name="4.0"></a>
## 4.0 An Overview of GnuPG, Enigmail and Private-Public Key Encryption ##

**Enigmail** is a **Mozilla Thunderbird** add-on that lets you protect the privacy of your email communication. **Enigmail** is an interface that lets you use **GnuPG** encryption program from within **Thunderbird**.  The **Engimail** interface is represented as *Enigmail* in the **Thunderbird** menu bar. 

**Engimail** is based on [**public-key cryptography**](http://en.wikipedia.org/wiki/Public-key_cryptography).
In this method, each individual must generate their own personal key pair. The first key is known as the *private key*. It is protected by a password or passphrase, both to be guarded and *never* shared with *anyone*. 

The second key is known as the *public key*. This key can be shared with any of your correspondents. Once you have a correspondent’s *public key* you can begin sending encrypted emails to this person. Only they will be able to decrypt and read your emails, because they are the only person who has access to the matching *private key* that you encrypted the message to.

Similarly, if you send a copy of your own *public key* to your email contacts and keep the matching *private key* secret, only you will be able to read encrypted messages from those contacts.

**Enigmail** also lets you **digitally sign** your messages. The recipient of your message who has a copy of your *public key* will be able to verify that the email comes from you, and that its content was not tampered with in transit. Similarly, if you have a correspondent's *public key*, you can verify the digital signatures on their signed messages. All *encrypted* messages should also be *signed*, as we will set up below.

<a name="4.1"></a>
## 4.1 How to Install Gpg4win and Enigmail ##

Please refer to the [**download section**](/en/thunderbird_main) for instructions on how to download **Gpg4win** which includes **GnuPG**.

### 4.1.1 How to Install Gpg4win ###

Installing **Gpg4win** resembles other software installations you may have performed and can be done by doing the following steps: 

**Step 1**. **Double click** ![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-102.png) to begin the installation process. The *Open File - Security Warning* dialog box may appear.

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-012.png)

If it does, **click** **Yes** to continue with the installation.

Select your appropriate language:

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-013.png)

To reach the Gpg4win Setup screen

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-014.png)

Select **Next**, and continue through the License Agreement

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-015.png)

You only need to install the GnuPG component, you can deselect all other software:

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-016.png)

**NOTE**: if you would like to have File Explorer integration of GnuPG, so that you can right-click on files and encrypt them and other extended functionality, you can always re-run the Gpg4win installer and install these additional components.

You can keep the default installation location:

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-017.png)

Have it install links in your **Start Menu** if you would like:

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-018.png)

And the default Start Menu folder.

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-019.png)

Then click **Install**:

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-020.png)

After this process has completed itself, the *Installation Complete* screen will appear:

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-021.png)

You can uncheck **Show me the README file** and select **Finish** to complete the **GnuPG** installation through **Gpg4win**.

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-022.png)

<a name="4.1.2"></a>
### 4.1.2 How to Install the Enigmail Add-on ###

After you have successfully installed the **GnuPG** software you are now ready to install the **Enigmail** add-on. 

To install **Enigmail**, perform the following steps: 

 **Step 1**. **Open Thunderbird**, then **click** ![](/sbox/screen/thunderbird-en-1/24a.png) to display the *Thunderbird Menu* and **select Add-ons** to activate the *Add-ons Manager* window and search for Enigmail in the search bar. If you have previously enabled viewing the **Menu Bar**, you can navigate there by selecting Tools > Addons as well.

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-043.png)

**Step 2**. **Click** **Install** to begin installing Enigmail   

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-044.png)

**Step 3**. When the installation is complete, you will be prompted to **restart now** **Thunderbird**, which you can do when all of your work is saved.

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-045.png)

### 4.1.3 How to Confirm that Enigmail and GnuPG are Working ###

Before you can begin using **Enigmail** and **GnuPG** to authenticate and encrypt your emails, you must first ensure that they are both communicating with each other.

**Select Enigmail > Preferences** to display the *Enigmail Preferences* screen:

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-057.png)

*Figure 7: The Enigmail Preferences window*

If **GnuPG** has been successfully installed, it will state "GnuPG was found in [location path]" in the *Files and Directories* section; otherwise, you may receive a pop-up alert resembling the following:

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-058.png)

*Figure 8: The Enigmail Alert pop-up message*

**Tip**: If you have received this message, it may indicate that you did not install **GnuPG** or you have installed it in different location. If you installed **GnuPG** in a different location, **check** the *Override with* option to enable the *Browse...* button, and then **click** ![](/sbox/screen/thunderbird-en-1/69.png) to activate the *Locate GnuPG program* and manually navigate to the location of the *gpg2.exe* file on your computer, otherwise please go back to [4.1 How to Install Enigmail and GnuPG](#4.1).

<a name="4.2"></a>
## 4.2 How to Generate Key Pairs and Configure Enigmail to Work with Your Email Accounts ##

Once you have confirmed that **Enigmail** and **GnuPG** are working properly, you can configure one or more of your email accounts to use **Enigmail** to generate one or more private/public key pairs.

### 4.2.1 How to Use the Enigmail Wizard to Generate a Key Pair ###

**Engimail** provides two ways of generating a private-public key pair; the first uses the *Enigmail Setup Wizard* and the second uses the *Key Management* screen. 

We will use the *Enigmail Setup Wizard* to generate a key pair:

**Step 1**. If **Setup Wizard** window is not already activated **select Enigmail > Setup Wizard** to open the *Enigmail Setup Wizard* screen as follows: 

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-059.png)

**Step 2**. **Select** "I prefer a standard configuration (recommended for beginners)". 

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-061.png)

*Figure 9: The Enigmail Setup Wizard screen*

Confirm the email address listed and selected is the one you would like to create a key pair for. Then create a passphrase that is different from your email passphrase. 

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-062.png)

*Figure 10: The Create Key screen*

**Step 3**. **Click** {Next} to activate the Key Creation screen:

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-063.png)

**Note**: Any key pair generated using *Enigmail Setup Wizard* has a 4096-bit key size and a lifespan of 5 years (which you can extend).

**Step 4**. After the key is generated, you will be prompted to create a revocation certificate. **Click** {Create Revocation Certificate

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-064.png)

You will be prompted to enter your newly created passphrase:

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-065.png)

*Figure 17: The Enigmail Prompt confirmation*

**Note**: If you know that a hostile or malicious party has gained unauthorised access to your private key or you lost access to this key, you may send the revocation certificate to your contacts to let them know that they should not use your matching public key. Keep in mind that you might need to do this if your computer is lost, stolen or confiscated. You are strongly advised to back up your revocation certificate in a safe and separate location from the computer you use for email encryption.

**Step 5**.  **Navigate** to a location where you can store the certificate safely and **click** {Save]:

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-064.png)

Enigmail will alert you that the Revocation Certificate was successfully saved.

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-067.png)

**Step 6**. You will be returned to the Enigmail Setup Wizard, you can select {Next} and {Finish}

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-068.png)

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-069.png)

### 4.2.2 Save a Copy of Your Key Pair in a Safe Place ###

You should save a copy of your key pair in a secure, safe location, such as an encrypted external hard drive or USB.

To Export your keys, navigate to Enigmail > Key Management and *right-click* on your key (it should be bold and have your email address). **Select** Export Keys to File:

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-073.png)

In the dialog, **select** Export Secret Keys

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-074.png)

After you have successfully generated your key pair and safely saved a backup and its associated revocation certificate, you are now ready to exchange public keys with a trusted correspondent.

### 4.2.3 How to Configure Enigmail for Use with Your Email Account ###

To enable **Enigmail** for use with a specific email account, perform the following steps:

**Step 1**.  **Click** ![](/sbox/screen/thunderbird-en-1/24a.png) to display the *Thunderbird Menu* and **select Options > Account Settings**.

**Step 2**. **Select** the *OpenPGP Security* menu item in the sidebar as follows: 

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-072.png)

*Figure 24: The Account Settings - OpenPGP Security screen*

**Step 3**. **Check** *Enable OpenPGP support*, **select** the *Use email address of this identity to identify OpenPGP key* option, and **check** all other options.

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-103.png)

**Step 4**. **Select** "Enigmail Preferences..." and Switch to Manual encryption settings:

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-071.png)

**NOTE: These settings make sure you attempt to **sign** and **encrypt** your emails within **Thunderbird** by default, and if you accidentally try to send an unencrypted email, Enigmail will prompt you for confirmation before sending the email.

**Step 5**. **Select** {OK} to exit Enigmail Preferences, and {OK} again to exit OpenPGP Options within Account Settings.

<a name="4.3"></a>
## 4.3 How to Exchange Public Keys ##

Before you can begin sending encrypted email messages to one another, you and your correspondents must exchange public keys. You must also confirm the validity of any key you accept by confirming that it really belongs to its purported sender. 

### 4.3.1 How to Share a Public Key over Email ###

To send a public key using **Enigmail**, you can either attach it to an email you send to your correspondent or you can publish it publicly, such as on your website or an online public key repository called *keyserver*.

### Attach Your Public Key to an Email ###

To attach your public key to an email:

**Step 1**. **Open Thunderbird** and then **click** ![](/sbox/screen/thunderbird-en-1/81.png) to write a new message.

**Step 2**. Select the menu option **Enigmail > Attach My Public Key**.

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-106.png)

**Note**: In this method, the **Attachments:** pane is not displayed immediately; it will appear as soon as you send the message.

If you would like to send a different public key, **select** the menu option **Enigmail > Attach Public Key...** and then **select** the key you would like to send and click **Send**.

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-108.png)

**NOTE**: this will not send the email, just attach the Public Key to the draft email. This is a typo in Enigmail!

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-109.png)

*Figure 25: The Write message pane displaying the attached public key in the Attachments pane.*

**Step 3**. **Click** ![](/sbox/screen/thunderbird-en-1/83.png) to send your email with your attached public key. 

### To Publish Your Public Key on a Keyserver ###

Publishing your *public key* to a public keyserver is a convenient way for others to get your key and initiate encrypted email conversations. However using keyservers come with two drawbacks: 
- anyone can upload a key associated to someone's email address without their consent, including a key that they do not use
- uploading a public key to a keyserver is a irrevocable process -- you cannot delete a key from a keyserver, only revoke it (in which case it will still be listed but as revoked)

To upload your public key to a keyserver

**Step 1**. Navigate to Enigimail > Key Management, *right-click* on your key,  and *select* Upload Public Keys to Keyserver

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-117.png)

**Step 2**. Use the default keyserver *pool.sks-keyservers.net* and select *OK*

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-118.png)

**Note**: You only need to upload your key to one keyserver listed, as they synchronize keys between them. If one keyserver is unresponsive, try another on the list of keyservers.
It usually takes a couple of minutes for the keyservers to synchronize a new key that has just been added so be patient trying to find a newly uploaded public key.

### 4.3.2 How to Import a Public Key from an Email ###

Both your correspondent and you will perform the same steps when importing each other's public keys from an email.

**Step 1**. **Select** and **open** the email containing your correspondent's public key. 

**Step 2**. **Right-Click** on the attached file and select Import OpenPGP Key

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-081.png)

**Step 3**. Enigmail will import the key and display a note that it was successfully imported

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-082.png)

*Figure 26: The Enigmail Confirm Import public key* 

To confirm that you have successfully imported your correspondent's public key, you can view it in Enigmail's Key Management window at Enigmail > Key Management

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-110.png)

*Figure 28: The Enigmail - Key Management displaying a recently imported public key* 

**Note** that option *Display All Keys by Default* needs to be selected to be able to see the keys

You can also change the display in Key Management to show Fingerprints rather than Key ID, which are much less likely to have the same value.

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-11.png)

### 4.3.3 How to Import a Public Key from a Keyserver ###

To search the keyservers for a public key to import

**Step 1**. *Navigate* to *Engimail > Key Management*, and within Key Management go to *Keyserver > Search for Keys*

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-120.png)

**Note**: You can use the email address of your contact or the key ID of their public key to find their key

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-123.png) ![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-122.png)
*Figure X*: using email address and key ID to search for a contact's public key

If there are any public keys associated with the email address or key ID, they will be listed
![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-126.png)
*Figure X*: The Download OpenPGP Keys window

Make sure the key is *checked* and click *OK* to import the key.
![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-127.png)
*Figure X*: dialog confirming the key has been imported

<a name="4.4"></a>
## 4.4 How to Validate and Sign a Key Pair ##

Finally, you must verify that the imported key is the correct or 'valid' key associated with the email address and person you want to securely communicate with. 

### 4.4.1 How to Validate a Key Pair ###

**Step 1**. You want to receive the 'fingerprint' of your contact's public key using some other method. If you know your contact, you can meet in-person, use a telephone, **Voice over Internet Protocol** (**VoIP**) or any other method you would feel confident you are really talking to the right person. As a result, voice or video conversations and face-to-face meetings work best, if they are convenient and if they can be arranged safely. One of the easier ways of sharing the 'fingerprint' of your public key offline is to print it on your business card and personally give it to your contact.

**Step 2**. Both you and your correspondent should verify the 'fingerprints' of the public keys that you have exchanged. A fingerprint is a unique series of numbers and letters that identifies each key. You can use the **Enigmail** *Key Management* screen to view the fingerprint of key pairs you have created and public keys you have imported. 

To view the fingerprint of a particular key pair, perform the following steps:

**Step 1**. **Select Enigmail > Key Management** and then **right-click** on a particular key to activate the pop-up menu: 

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-085.png)

*Figure 29: The Enigmail Key Management menu with the Key Properties item selected*

**Step 2**. **Select** the *Key Properties* item to activate the following screen: 

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-086.png)

*Figure 30: The Key Properties screen*

Your correspondent should repeat these steps. To confirm fingerprints, read fingerprint of your key to your contact and have them verify that the fingerprint they see on your public key they received matches. Then have your contact do the same for their key's fingerprint. If fingerprints don't match, exchange public keys again and repeat the validation process.

**Note**: The fingerprint itself is not a secret and can be recorded for later verification at your convenience.

### 4.4.2 How to Sign a Valid Public Key ###

After you have verified given correspondent's key, you can *sign* it, to confirm that you consider this key valid.

**Note**: Signing keys may expose a connection between you and your corespondent when you send signed key to somebody else or export it to the key server. To prevent this from happening always select option *Local signature* below.

To sign a properly validated public key, perform the following steps:

**Step 1**. **Select Enigmail > Key Management** to open the *Key Management* screen.

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-131.png)

**Step 2**. **Right-click** your correspondent's public key from the *Key Management* screen (see figure 29 above) and **select** the *Sign Key* item from the menu to activate the following screen:

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-130.png)

*Figure 31: The Enigmail - Sign Key screen*

**Step 3**. **Check** the *I have done very careful checking* option, **select** *Local signature (cannot be exported)*, and then **click** ![](/sbox/screen/thunderbird-en-1/35.png) to sign your correspondent's public key. You may be asked to provide password to your private key. 

When you have a signed a key, you also implicitly *trust* that key, which changes the color of the dialog above a signed or encrypted email from blue to green:

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-084.png) 

*Figure X: Email from contact whose key is not signed or trusted*

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-129.png) 

*Figure X: Email from contact whose key is signed or trusted*

#### 4.4.3 How to Manage Your Key Pairs ####

The *Enigmail Key Management* window is used to generate, validate and sign different key pairs. However, you may also perform other tasks by related to key management among them (see figure 29 above): 

- **Manage User IDs** lets you associate more than one email address to a single key pair.
- **Change Expiration Date** lets you change expiration date of your key pair.
- **Change Passphrase** lets you change the password protecting your key pair.
- **Generate & Save Revocation Certificate** lets you generate a new revocation certificate, if you have lost or misplaced the one you created earlier. 

<a name="4.5"></a>
## 4.5 How to Send and Receive Encrypted Emails ##

**Important**: The header of any email message - that is its *Subject* and intended recipients including any information in the *To*, *CC* and *BCC* fields - *cannot* be encrypted and will be sent in open text. To ensure the privacy and security of your email exchanges, the subject of your email should be kept non-descriptive not to reveal sensitive information. In addition, you are advised to put all addresses in the *BCC* field when sending emails to a group of people.

When encrypting email messages with attachments, we have set up *Enigmail* to use **PGP/MIME** which will hide the number and name of  any files you attach to your email. If you choose *inline PGP* for an email with attachments, the names of the attached files are not encrypted and are sent in clear text.

**Note**: that any encrypted email you send with Thunderbird/Enigmail/GnuPG is automatically encrypted to your key along with the chosen recipients of this email, so you are able to decrypt emails in your sent folder.

### 4.5.1 How to Send an Encrypted Email ###

Once both you and your correspondent have successfully imported and validated and signed each other's public keys, you are ready to begin sending and receiving encrypted messages.

To encrypt the contents of you email message to your correspondent, perform the following steps:

**Step 1**. **Open** **Thunderbird** and **click** ![](/sbox/screen/thunderbird-en-1/81.png) to write an email.

**Step 2**. Write your email! Remember the subject line is not encrypted. **Note:** that *lock* and *pencil* are highlighted to remind you the email will be  *encrypted* and *signed*

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-106.png) 

*Figure 34: Encryption and Signed enabled*

**Optional**: to include an attachment, select the *Attach* button and the file you would like to attach to the email.

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-135.png) 

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-138.png) 

*Figure X*: The attachment is displayed in the draft email message window.

**Step 3**. **Click** ![](/sbox/screen/thunderbird-en-1/83.png) to send the message. You may be prompted for your private key passphrase to use your private key to encrypt and sign the message.

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-90.png) 

##### To send an inline PGP rather than PGP/MIME email ####

If your recipient does not use **Thunderbird** for encrypted email, they may not be able to easily read PGP/MIME emails. For example, programs like **GpgOL for Outlook**, **Mailvelope**, or **K-9 Mail on Android** have difficulty with *PGP/MIME*. You can choose to send them encrypted emails instead with *inline PGP*. **Note**: emails encrypted with *inline PGP* do not protect the name or number of attachments your email has.

**Step 1: In the composition window of your email, *select* **Enigmail:** under the *Send* button:

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-140.png) 

**Step 2: *select* **Use inline PGP** and click *OK* to return to your email draft.

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-142.png) 

### 4.5.2 How to Decrypt an Email ###

When you receive and open an encrypted message, **Enigmail/OpenPGP** will automatically attempt to decrypt the message when you receive and open it. 
If it does not, select the *Decrypt* button. This will activate the following screen:

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-090.png)

*Figure 36: The Enigmail Prompt - Please type in your OpenPGP passphrase or your SmartCard PIN*

**Step 1**. **Enter** your passphrase as shown above.

After you have entered your private key passphrase, the message is decrypted and displayed as follows:

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-084.png)

*Figure 37: The newly decrypted message in the message pane.*

You have now successfully decrypted this message. By repeating the steps described in section **4.5 How to Encrypt and Decrypt Email Messages** every time you and your correspondent exchange messages, you can maintain a private, authenticated channel of communication, regardless of who might be attempting to monitor your email exchanges.



