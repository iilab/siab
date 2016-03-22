

---

lang: xx
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 005
title: TrueCrypt - Secure File Storage

---

**On 28 May 2014 TrueCrypt developers web page started to inform users that TrueCrypt development is discontinued as of now. The circumstances behind this situation are not clear yet. The developers web page is offering a new version 7.2 of TrueCrypt with some functionality removed. Despite this new release we recommend that you continue to use older version 7.1a (see Downloading instructions), until we know more about what has happen and what plans are for the future of TrueCrypt development. For alternatives to TrueCrypt please have a look at the "GNU Linux, Mac OS and other Microsoft Windows Compatible Programs" section below.**

**Homepage**

**www.truecrypt.org**

**Computer Requirements**

- Windows 2000/XP/2003/Vista/7
- Administrator rights required for installation or to create volumes but not to access existing volumes 

**Version used in this guide**

- 7.1a

**Last revision of this chapter**

- May 2014

**License**

- Free and Open Source Software 

**Portable Version**

- [**Hands-on guides for portable TrueCrypt**](https://securityinabox.org/en/truecrypt_portable)

**Required Reading**

- How-to Booklet chapter [**4. How to protect the sensitive files on your computer**](/chapter-4)

**What you will get in return**: 

- The ability to effectively protect your files from intruders or unauthorized access
- The ability to easily and securely store copies of your important files 


**GNU Linux, Mac OS and other Microsoft Windows Compatible Programs:**

**Note**: **TrueCrypt** is also available on **GNU Linux** and **Mac OS**. 

Many **GNU Linux** distributions, for instance [**Ubuntu**](http://www.ubuntu.com/), support on-the-fly encryption-decryption for the entire disk as a standard feature. You can decide to use it when you install the system. In addition we also recommend to switch on encryption of home folder during installation. You can also add the encryption functionality to your **Linux** system by using an integration of [**dm-crypt**](http://www.saout.de/misc/dm-crypt/) and [**cryptsetup and LUKS**](http://code.google.com/p/cryptsetup/). Another approach is to use [**ScramDisk for Linux SD4L**](http://sd4l.sourceforge.net/), a free and open source on-the-fly encryption-decryption program.

For the **Mac OS** you can use **FileVault**, which is part of the operating system, to provide *on-the-fly* encryption and decryption for the content of your entire disk and/or your home folder, and all the sub-folders.

As alternative program on **Microsoft Windows** we recommend using:

* [DiskCryptor](https://diskcryptor.net/wiki/Main_Page) is a free, open source encryption solution that offers encryption of all disk partitions, including the system partition.
* [**AxCrypt**](http://www.axantum.com/AxCrypt/) is a free and open source program that can encrypt separate files.

On MS Windows 7 Ultimate or Enterprise editions or MS Windows 8 Pro and Enterprise editions you will find [**BitLocker**](http://windows.microsoft.com/en-us/windows7/products/features/bitlocker) available to encrypt entire disk. Note that BitLocker is a Microsoft owned, closed, proprietary software which is not independently audited to establish what level of the protection and privacy it offers to your information.

### 1.1 Things you should know about this tool before you start ###

**TrueCrypt** will protect your data from being accessed by locking it with a password that you will create. If you forget that password, you will lose access to your data! **TrueCrypt** uses a process called encryption to protect your files. Please bear in mind that the use of encryption is illegal in some countries. Rather than encrypting specific files, **TrueCrypt** creates a protected area, called a *volume*, on your computer. You can safely store your files inside this encrypted volume. 

**TrueCrypt** offers the ability to create a standard encrypted volume or a hidden volume. Either one will keep your files confidential, but a
hidden volume allows you to hide your important information behind less
sensitive data in order to protect it, even if you are forced to reveal
your **TrueCrypt** volume. This guide explains both volumes in detail. 


