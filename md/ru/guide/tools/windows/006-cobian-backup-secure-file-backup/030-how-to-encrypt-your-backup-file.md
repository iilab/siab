

---

lang: ru
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: How to Encrypt Your Backup File

---

List of sections on this page:

- [**4.0 About Encryption**](#4.0)
- [**4.1 How to Encrypt Your Backup File**](#4.1)
- [**4.2 How to Decrypt Your Backup File**](#4.2)

-------

<a name="4.0"></a>
## 4.0 About Encryption ##

Encryption may be a necessity for those wishing to keep their backup secure from unauthorised access.

Encryption is the process of encoding, or scrambling, data in such a way that it appears unintelligible to anyone who does not have the specific key needed to decode the message. For more information on encryption, please refer to **How-to Booklet** chapter [**4.How to protect the sensitive files on your computer**](http://securityinabox.org/chapter-4)

<a name="4.1"></a>
## 4.1 How to Encrypt Your Backup File ##

The *Strong encryption* pane is used to specify the encryption method to be used.

**Step 1**. **Click** the *Encryption type* drop-down box to activate its list of different encryption methods as follows:

![](/sbox/screen/cobian-en/30.png)

*Figure 1: The Encryption type drop-down list*

To keep things simple, we recommend that you choose from either the *Blowfish* or the *Rijndael* (128 bits) methods. These will provide excellent security for your archive, and let you access the encrypted data with a chosen password.

**Step 2**. **Select** the *Encryption* type you want to use.

**Note**: *Rijndael* and *Blowfish* both offer approximately the same level of security. *DES* is weaker but the encryption process is faster.

**Step 3**. **Type** and **re-type** the password into the two boxes provided as below.

![](/sbox/screen/cobian-en/31.png)

*Figure 2: The The Encryption type and Passphrase text fields*

The strength of the password is indicated by the bar marked 'Passphrase quality'. The further the bar moves to the right, the stronger the passphrase. Refer to the **How-to Booklet** chapter [**3.How to Create and Maintain Secure Passwords**](/chapter-3) and the [**KeePass**](/en/keepass_main) Hands-on guide for instructions on how to create and store secure passphrases (or passwords).

**Step 4**. **Click** ![](/sbox/screen/cobian-en/13.png).

<a name="4.2"></a>
## 4.2 How to Decrypt Your Backup File ##

Decrypting your backup file is easy and quick. To decrypt your backup file, perform the following steps:

**Step 1**. **Select > Tools > Decrypter and Keys** as shown below:

![](/sbox/screen/cobian-en/32.png)

*Figure 3: The Tools menu with Decrypter and Keys item selected*

*This will activate the Decrypter and Keys window as follows:*

![](/sbox/screen/cobian-en/33.png)

*Figure 4: The Cobian Backup 10 Decrypter and Keys window*

**Step 2**. **Click** ![](/sbox/screen/cobian-en/34.png) to select the archive you want to decrypt.

**Step 3**. **Click** ![](/sbox/screen/cobian-en/35.png) to select the folder in which to store the decrypted archive.

**Step 4**. **Select** the same encryption type you selected in section [**4.1 How to Encrypt Your Backup File**](/en/chapter_4_1#4.1), in the *Methods* drop-down list.

![](/sbox/screen/cobian-en/36.png)

*Figure 5: The New Methods drop-down list*

**Step 4**. **Select** the appropriate encryption method (the one you used to encrypt your backup file).

**Step 5**. **Type** your passphrase into the *Passphrase* text fields.

**Step 6**. **Click** ![](/sbox/screen/cobian-en/37.png).

The file(s) will be decrypted to the location that you specified. If the files were also compressed, you will need to decompress them as outlined in section  [**3.1 How to Decompress Your Backup**](/en/chapter_3_1#3.1).

