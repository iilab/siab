

---

lang: xx
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: How to Encrypt and Decrypt Text and Files

---

List of sections on this page:

- [**4.0 How to Encrypt Text Messages with gpg4usb**](#4.0)
- [**4.1 How to Decrypt Text Messages with gpg4usb**](#4.1)
- [**4.2 How to Encrypt Files with gpg4usb**](#4.2)
- [**4.3 How to Decrypt Files with gpg4usb**](#4.3)

<a name="4.0"></a>
## 4.0 How to Encrypt Text Messages with gpg4usb ##

In the example that follows, Terence will encrypt an email for his friend Salima, using the following steps:

**Step 1**. **Double click** ![](/sbox/screen/gpg4usb-en-1/03.png) to open the **gpg4usb** console.

**Step 2**. **Compose** your message as shown in the example below:

![](/sbox/screen/gpg4usb-en-1/19.png)

*Figure 1: The gpg4usb console displaying an example of a message*

**Step 3**. **Check** the check box associated with the intended recipient of your email as follows:

![](/sbox/screen/gpg4usb-en-1/20.png)

*Figure 2: The gpg4usb console displaying the intended recipient*

**Note:** You can encrypt a message to more than one recipient by simply checking their corresponding check boxes in the *Encrypt for:* pane. Also, it may prove useful for your personal records to encrypt that message to yourself, so you can read what you sent later. 

**Step 4**. Either **click** ![](/sbox/screen/gpg4usb-en-1/21.png) or **select Encrypt** from the **Crypt** menu to encrypt your message as follows:

![](/sbox/screen/gpg4usb-en-1/22.png)

*Figure 3: The gpg4usb console displaying an example of an encrypted message*

**Step 5**. **Click** ![](/sbox/screen/gpg4usb-en-1/23.png) to select the entire encrypted message, and then **click** ![](/sbox/screen/gpg4usb-en-1/24.png) to copy the message to the clipboard.

**Note**: Alternatively, you may use the short-cut keys associated with each item in the menu, in this case **Ctrl + E** will encrypt the message, **Ctrl + A** will select the entire encrypted message, and **Ctrl + C** will copy the message to the clipboard.

**Step 6**. **Open** your email account and then **open** a blank message page, and then **paste** this message so that it resembles the following:

![](/sbox/screen/gpg4usb-en-1/25.png)

*Figure 4: An example of a message encrypted in gpg4usb pasted into a Gmail account email*

**Note**: **Rich Text Formats** (**RTF**) can corrupt the encrypted message format; hence, it is better to compose your messages in plain text. To convert **RTF** into plain text in **Gmail** simply **click** *More Options* and **select** *Plain Text Mode*  displayed at the foot of the message pane as shown below:

 ![](/sbox/screen/gpg4usb-en-1/26.png)

*Figure 5: Gmail Format Options*

<a name="4.1"></a>
## 4.1 How to Decrypt Text Messages with gpg4usb ##

To decrypt an encrypted email, perform the following steps:

**Step 1**. **Double click** ![](/sbox/screen/gpg4usb-en-1/03.png) to open the **gpg4usb** program.

**Step 2**. **Open** your email account, and then **open** the message.

**Step 3**. **Select**, **copy** and then **paste** the encrypted message into the **gpg4usb** console *untitled1.txt* tab as follows:

![](/sbox/screen/gpg4usb-en-1/27.png)

*Figure 6: The gpg4usb console displaying a message for decryption*

**Note**: If the encrypted text appears with double line breaks as shown in *Figure 7* below, **gpg4usb** might not be able to automatically decrypt it. To remove these double line breaks, **click** on ![](/sbox/screen/gpg4usb-en-1/27b.png) (or **select** *Remove double Linebreaks* from the **Edit** menu) to remove them and then continue the decryption process at **Step 4**.

![](/sbox/screen/gpg4usb-en-1/28.png)

*Figure 7: The gpg4usb console displaying a message for decryption with double linebreaks*
 
**Step 4**. **Click** ![](/sbox/screen/gpg4usb-en-1/29.png) and enter the password you assigned when generating a key pair, as shown in the following screen:

![](/sbox/screen/gpg4usb-en-1/30.png)

*Figure 8: The Enter Password prompt window*

**Step 5**. **Click** *OK* to activate a **gpg4usb** console resembling *Figure 2* above.

<a name="4.2"></a>
## 4.2 How to Encrypt Files with gpg4usb ##

The process for encrypting a file is similar to encrypting text messages; in the example that follows, Salima will encrypt a file for Terence, using the following steps:

**Step 1**. **Double click** ![](/sbox/screen/gpg4usb-en-1/03.png) to open the **gpg4usb** program.

**Step 2**. **Click** ![](/sbox/screen/gpg4usb-en-1/31.png) and *Encrypt File* to activate the following screen:

![](/sbox/screen/gpg4usb-en-1/32.png)

*Figure 9: The Encrypt File window*

The *Encrypt File* window scroll list (outlined in black) lets you select the email account and corresponding key you will use to encrypt a message to.

**Step 3**. **Click** ![](/sbox/screen/gpg4usb-en-1/33.png) beside *Input* item to activate the following screen:

![](/sbox/screen/gpg4usb-en-1/34.png)

*Figure 10: The Open File browser window*

**Step 4**. **Click** ![](/sbox/screen/gpg4usb-en-1/35.png) to attach the file to be encrypted and return to the *Encrypt* window as follows:

![](/sbox/screen/gpg4usb-en-1/36.png)

*Figure 11: The Encrypt File window displaying the file designated for encryption*

**Step 5**. **Click** *OK* to activate the following screen:

![](/sbox/screen/gpg4usb-en-1/38.png)

*Figure 12: The Done confirmation dialog box*

The *Done* confirmation dialog box shows you where the newly encrypted file resides. An encrypted file can also be identified by either a *.asc* file extension, for example, *Meeting Minutes.doc.asc*. 

**Step 6**. **Click** *OK* to complete the file encryption process.

**Note**: You can encrypt a text message you might send along with the encrypted file separately. 

**Step 7**. Using your email account, **navigate** to the location specified in the *Done* confirmation dialog box (*Figure 12*), and then attach the encrypted file to you email as you would any other file. 

**IMPORTANT**: Observe that the name of the file is **not encrypted**. Make sure that this name does not reveal any important information! Do not forget that an  unencrypted version of the file continues to reside on the disk.

<a name="4.3"></a>
## 4.3 How to Decrypt Files with gpg4usb ##

In the example that follows, Terence will decrypt the file Salima has sent to him, using the following steps:

**Step 1**. **Double click** ![](/sbox/screen/gpg4usb-en-1/03.png) to open the **gpg4usb** program.

**Step 2**. **Open** your email account, **open** the message and **download** the attached file.

**Note**: If your correspondent has sent a message accompanying the encrypted file, you may decrypt that message by using the method outlined in section [**4.1 How to Decrypt Text Messages with gpg4usb**](https://securityinabox.org/en/node/2276#4.1)

**Step 3**. In the **gpg4usb** console (as shown in *Figure 1* above), **click** ![](/sbox/screen/gpg4usb-en-1/31.png) and **Decrypt File** window (as in *Figure 13* below). 

**Step 4**. **Click** ![](/sbox/screen/gpg4usb-en-1/33.png) beside *Input* item to browse to the location of the downloaded encrypted file as follows:

![](/sbox/screen/gpg4usb-en-1/37.png) 

*Figure 13: The Decrypt window, displaying the path to the encrypted file*

**Step 5**. **Click** *OK* to activate the following screen:

![](/sbox/screen/gpg4usb-en-1/39.png) 

*Figure 14: The Done confirmation dialog box displaying the location of the decrypted file*

**Important**: If you are working from an internet café or at workstations other people may have access to decrypted version of the file, it is better to copy the *.asc* file to your USB or portable drive, and take it with you so you may decrypt it in the privacy of your own home.


