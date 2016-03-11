

---

lang: xx
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 013
title: Thunderbird with Enigmail and GPG - Secure Email Client

---

**Homepage**

- [**www.mozilla.org/thunderbird**](https://www.mozilla.org/thunderbird/)
- [**www.enigmail.net**](http://enigmail.net/)
- [**www.gpg4win.org**](https://gpg4win.org)
- [**trac.torproject.org/projects/tor/wiki/torbirdy**](https://trac.torproject.org/projects/tor/wiki/torbirdy)

**Computer Requirements**

- All Windows Versions

**Versions used in this guide**

- Thunderbird 38.3 
- Enigmail 1.8.2
- Gpg4win 2.2.6, includes GNU Privacy Guard (GnuPG) 2.0.29
- TorBirdy 0.1.4

**Last revision of this chapter**

- October 2015

**License**

- Free and Open-Source Software

**Required Reading**

- Tactics chapter [**7. Keeping your Internet Communication Private**](/chapter-7)
- Tactics chapter [**4. How to protect the sensitive files on your computer**](/chapter-4)

**What you will get in return**: 

- The ability to manage different e-mail accounts through a single program
- The ability to read and compose messages after disconnecting from the Internet
- The ability to use public key encryption to keep your email private 

**GNU Linux, Mac OS and other Microsoft Windows Compatible Programs**:

The **Mozilla Thunderbird** email client is available for **GNU Linux**, **Mac OS**, **Microsoft Windows** and other operating systems. Managing multiple email accounts is a complex task from the digital security viewpoint; therefore, we *strongly recommend* that you use **Mozilla Thunderbird** for this purpose. The security advantages available in **Thunderbird**, a cross-platform *free* and *open source* program, are even more important when compared to its commercial equivalents like **Microsoft Outlook**. However, if you would prefer to use a program other than **Mozilla Thunderbird**, we recommend the following free and open source alternatives:

* [**KMail**](https://userbase.kde.org/KMail) available for **GNU Linux** and **Microsoft Windows**;
* [**Claws Mail**](http://www.claws-mail.org/) available for **GNU Linux** and **Microsoft Windows**;
* [**Sylpheed**](http://sylpheed.sraoss.jp/en/) available for for **GNU Linux**, **Mac OS** and **Microsoft Windows**;
* [**Mailpile**](https://www.mailpile.is/) currently beta and available for **GNU Linux** and **Microsoft Windows** , to be available for **Mac OS** in the future

Note: Although we recommend using **Enigmail** for its ease of use with Thunderbird, you still can also use stand-alone encryption tools such as gpg4usb in conjunction with Thunderbird. Please read [gpg4usb](/en/gpg4usb_portable) chapter to see other way to encrypt your email using public key encryption method.

### 1.1 Things you should know about this tool before you start ###

**Mozilla Thunderbird** is a cross-platform, free and open source email client for receiving, sending and storing emails. An email client is a computer application that lets you download and manage your email messages without an Internet browser. 

Because of this functionality, **Thunderbird** downloads your emails locally onto your computer in order to read and send emails. Therefore it is important to implement device encryption for your Windows computer as described in Tactics chapter [**4. How to protect the sensitive files on your computer**](/chapter-4).

**Thunderbird** cannot protect your device if you open malicious attachments or hyperlinks. Do not open unsolicited attachments and practice caution with any embedded hyperlinks in emails. For more information on preventing harmful or malicious software from being installed on your computer, please refer to the **How-to Booklet** chapter [**1. Protecting your Computer from Viruses, Malware and Hackers**](/chapter-1) for more information about anti-malware and firewall software.

You can manage multiple email accounts using this program. You must have an existing email account before using **Thunderbird**. You may also create [**RiseUp**](/en/riseup_createaccount) email accounts if you wish.

**Enigmail** is an add-on developed for **Thunderbird**. It lets users access the authentication and encryption features provided by **GNU Privacy Guard** (**GnuPG**), which is part of the **Gpg4win** software package.

**GnuPG** is a public key encryption program used to generate and manage the key pairs to be used in encrypting and decrypting messages, to keep your email communications private and secure. **GnuPG** must be installed for **Enigmail** to work, as will be described later in this chapter.

**Gpg4win** is a convenient software package that includes **GnuPG**. It also includes tools to integrate functionality into Windows Explorer so that you can encrypt files on your computer without having to email them. We will only install **GnuPG** from this package but this functionality can always be enabled by reinstalling **Gpg4win** and selecting the appropriate additional software.

