

---

lang: xx
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: How to Install gpg4usb and Generate a Key Pair

---

List of sections on this page:

- [**2.0 How to Install gpg4usb**](#2.0)
- [**2.1 How to Generate a Key Pair with gpg4usb**](#2.1)

<a name="2.0"></a>
## 2.0 How to Install gpg4usb ##

**gpg4usb** is a portable tool that does not require installation on your computer. The software is disturbed as a zip and should be extracted directly to a USB drive or to a folder on your computer; to begin perform the following steps: 

**Step 1**. **Locate** the **gpg4usb** zipped archive file, and then **extract** all the files to a removable USB drive or a folder on your computer:

![](/sbox/screen/gpg4usb-en-1/01.png)

*Figure 1: The gpg4usb program destination location*

<a name="2.1"></a>
## 2.1 How to Generate a Key Pair with gpg4usb ##

Before you can begin encrypting and decrypting email, text messages, documents and files, you must take two preparatory steps: first you need to generate or import your encryption key pair and second you need to send your public key to your contacts and receive their public keys and import them to your key ring. We describe how to share public keys on the next page. **gpg4usb** assist you with generating your key pair on the first start of the program. Note that you can always come back to *Getting Started* window from the *Help* -> *Open Wizard* menu.

**Step 1**. To run the **gpg4usb** program for the first time , **find and double click** ![](/sbox/screen/gpg4usb-en-1/02.png) to open the **gpg4usb** folder and then **double click** ![](/sbox/screen/gpg4usb-en-1/03.png). This will activate the *Getting Started* window. Select a language and click *Next*

**Step 2**. At the *Choose your Action* screen, click *Create a new keypair*

![](/sbox/screen/gpg4usb-en-1/04.png)

*Figure 2: Choose your Action*

Note the other options to import existing keys available on the First Start Wizard screen. If upgrading from a previous version of gpg4usb, you can choose *import settings and/or keys from gpg4usb*. If using [Thunderbird with Enigmail](/en/thunderbird_main), you can choose the option *import keys from GnuPG*. You can also choose to import keys at a later stage by running the wizard again from the *Help* -> *Open Wizard* menu.

**Step 3**. At the *Create a keypair* **click** *Create New Key*

![](/sbox/screen/gpg4usb-en-1/05.png)

*Figure 3: Create New Key* 

**Step 4**. **Enter** the appropriate data into the corresponding text fields, so that your own window resembles the following:

![](/sbox/screen/gpg4usb-en-1/06.png)

*Figure 4: An example of a completed Generate Key form*

**Important:** 

* Set a secure password to protect your private key (please refer to chapter [**3. How to create and maintain secure passwords**](/en/chapter-3)).
* We advice that you use expiration date and that you set it to less then 5 years.
* We strongly recommend that you generate keys of at least 2048 bit size. Key of a larger size is more secure, but also requires more time to create, encrypt and decrypt texts.

**Note**: You do not need to use your real name and real email address when generating your key. However, using email address of the account you will use to communicate will make it easier for your contacts to associate your key with this account.

**Step 6**. **Click** *OK* to generate the keypair.

![](/sbox/screen/gpg4usb-en-1/07.png)

*Figure 5: Generating Key...*

![](/sbox/screen/gpg4usb-en-1/08.png)

*Figure 6: New Key Created*

**Step 7**. **Click** *OK* to come back to the **gpg4usb** window. After the keypair has been successfully generated, you will see a screen resembling the following: 

![](/sbox/screen/gpg4usb-en-1/09.png)

*Figure 7: The gpg4usb window, displaying the newly created key pair* 

Now that you have successfully created a key pair, you need to learn how to export your public key to share it with other people, and how to import the public keys of your correspondents.

