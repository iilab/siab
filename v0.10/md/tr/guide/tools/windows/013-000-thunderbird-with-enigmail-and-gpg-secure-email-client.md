

---

lang: tr
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 013
title: Thunderbird with Enigmail and GPG - Secure Email Client

---

**Homepage**

- [**www.mozilla.com/thunderbird**](http://www.mozilla.com/thunderbird/)
- [**www.enigmail.net**](http://enigmail.net/)
- [**www.gnupg.org**](http://www.gnupg.org/)
- [**trac.torproject.org/projects/tor/wiki/torbirdy**](https://trac.torproject.org/projects/tor/wiki/torbirdy)

**Computer Requirements**

- All Windows Versions

**Versions used in this guide**

- Thunderbird 31.0 
- Enigmail 1.7
- GNU Privacy Guard (GnuPG) 1.4.18
- TorBirdy 0.1.2

**Last revision of this chapter**

- September 2014

**License**

- Free and Open-Source Software

**Required Reading**

- How-to Booklet chapter [**7. Keeping your Internet Communication Private**](/chapter-7)

**What you will get in return**: 

- The ability to manage different e-mail accounts through a single program
- The ability to read and compose messages after disconnecting from the Internet
- The ability to use public key encryption to keep your email private 

**GNU Linux, Mac OS and other Microsoft Windows Compatible Programs**:

The **Mozilla Thunderbird** email client is available for **GNU Linux**, **Mac OS**, **Microsoft Windows** and other operating systems. Managing multiple email accounts is a complex task from the digital security viewpoint; therefore, we *strongly recommend* that you use **Mozilla Thunderbird** for this purpose. The security advantages available in **Thunderbird**, a cross-platform *free* and *open source* program, are even more important when compared to its commercial equivalents like **Microsoft Outlook**. However, if you would prefer to use a program other than **Mozilla Thunderbird**, we recommend the following free and open source alternatives:

* [**Claws  Mail**](http://www.claws-mail.org/) available for **GNU Linux** and **Microsoft Windows**;
* [**Sylpheed**](http://sylpheed.sraoss.jp/en/) available for for **GNU Linux**, **Mac OS** and **Microsoft Windows**;
* [**Alpine**](http://www.washington.edu/alpine/) available for **GNU Linux**, **Mac OS** and **Microsoft Windows**.

Note: Although we recommend using **Enigmail/GnuPG** for its ease of use with Thunderbird, you still can also use stand-alone encryption tools such as gpg4usb in conjunction with Thunderbird. Please read [gpg4usb](/en/gpg4usb_portable) chapter to see other way to encrypt your email using public key encryption method.

### 1.1 Things you should know about this tool before you start ###

**Mozilla Thunderbird** is a cross-platform, free and open source email client for receiving, sending and storing emails. An email client is a computer application that lets you download and manage your email messages without an Internet browser. You can manage multiple email accounts using a single program. You must have an existing email account before using **Thunderbird**. You may also create [**RiseUp**](/en/riseup_createaccount) email accounts if you wish.

**Enigmail** is an add-on developed for **Thunderbird**. It lets users access the authentication and encryption features provided by **GNU Privacy Guard** (**GnuPG**).

**GnuPG** is a public key encryption program used to generate and manage the key pairs to be used in encrypting and decrypting messages, to keep your email communications private and secure. **GnuPG** must be installed for **Enigmail** to work, as will be described later in this chapter.

