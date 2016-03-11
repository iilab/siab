

---

lang: zh
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: How to Encrypt Your Backup File

---

List of本页的项目列表：

- [**4.0 关于加密**](#4.0)
- [**4.1 如何加密您的备份文档**](#4.1)
- [**4.2 如何解密您的备份文档**](#4.2)

-------

<a name="4.0"></a>
##4.0 关于加密##

对于那些不想让别人在未经允许的情况下查看他们备份文件的用户来说，加密是一项必不可少的技术。

所谓加密，指的是对数据进行编码或不规则化处理。如果别人没有特定所需的解码口令，就无法加载该信息。要想了解更多关于加密的内容，请参照*使用手册*章节[**4. 如何保护您电脑中的敏感文件**](http://securityinabox.org/zh/chapter-4)。

<a name="4.1"></a>
##4.1 如何加密您的备份文档##

*高级加密*选项列举了可供使用的加密方案。

**第1步**：**单击** *加密方式*下拉栏，可以看到一组不同的加密方法：

![](/sbox/screen/cobian-zh/30.png)

*图1：加密类型下拉栏*

简单起见，我们推荐您从*Blowfish*(128bits)或*Rijndael*(128bits)这两种方案中选择其一。这可以为您的文档提供足够的安全性，而且您访问加密数据时，只要输入密码即可。

**第2步**：**选择**您要使用的*加密*方式。

**注意**：*Rijndael*和*Blowfish*所提供的安全等级大致相同。*DES*相对低些，但是加密过程更快。

**第3步**：在下图所示的位置**输入**并**再次输入以确认**您的密码。

![](/sbox/screen/cobian-zh/31.png)

*图2：加密类型以及密码输入文本框*

您密码的强度会在旁边的“密码等级”上显示。该等级条越靠右，密码的安全系数也就越高。您也可以参照**使用手册**中的章节[**3. 如何创建密码并维护密码安全**](/zh/chapter-3)以及[**KeePass**](/zh/keepass_main)的操作手册，它会介绍如何安全创建和储存密码或口令。

**第4步**：**单击**![](/sbox/screen/cobian-zh/13.png)。

<a name="4.2"></a>
##4.2 如何解密您的备份文档##

给您的备份文档解密并不难，请执行以下步骤：

**第1步**：**选择 > 工具 > Decrypter and Keys**如下所示：

![](/sbox/screen/cobian-zh/32.png)

*图3：工具菜单，选择了密码及解密相关选项*

*密码及解密相关选项窗口，如下所示*

![](/sbox/screen/cobian-zh/33.png)

*图4：Cobian Backup 10密码及解密相关选项窗口*

**第2步**：**单击**![](/sbox/screen/cobian-zh/34.png)选择您要解密的文件。

**第3步**：**单击**![](/sbox/screen/cobian-zh/35.png)选择您要存放解密文档的文件夹。

**第4步**：**选择**您在上面章节[**4.1 如何给您的备份文档加密**](/zh/cobian_encryp#4.1)中选用的相同加密方式，位于*方法*下拉栏里。

![](/sbox/screen/cobian-zh/36.png)

*图5：新方案下拉栏*

**第5步**：**选择**合适的加密方案（您使用过的那个）。

**第6步**：**输入**在*Passphrase*（密码）栏中输入您的密码。

**第7步**：**单击**![](/sbox/screen/cobian-zh/37.png)。

文件就会自动解密并存储到您设定的路径文件夹去了。如果这些文件是被压缩的，您需要解压它们方可使用。欲知具体的解压办法，请参阅[**3.1 如何解压缩您的备份文件**](/zh/cobian_compress#3.1)。

 sections on this page:

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

