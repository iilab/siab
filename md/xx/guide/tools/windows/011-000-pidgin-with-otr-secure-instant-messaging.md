

---

lang: xx
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 011
title: Pidgin with OTR - Secure Instant Messaging

---

**Homepage**

- **Pidgin**: [**www.pidgin.im**](http://www.pidgin.im)
- **OTR**: [**https://otr.cypherpunks.ca/**](https://otr.cypherpunks.ca/)

**Computer Requirements**

- An Internet connection
- All Windows Versions 

**Version used in this guide**

- Pidgin 2.10.9 
- OTR 4.0.0-1 

**Last revision of this chapter**

- August 2014

**License**: 

- Free and Open-Source Software

**Required Reading**

How-to Booklet chapter [**7. Keeping your Internet Communication Private**](/chapter-7)

**What you will get in return**: 

- The ability to organize and manage some of the most popular instant messaging services through a single program 
- The ability to have private and authenticated chat sessions

**GNU Linux, Mac OS and other Microsoft Windows Compatible Programs:**

**Note:** We recommend [**Jitsi**](/en/jitsi) as a replacement for **Pidgin**. As well as being able to use **Jitsi** for secure text chat (including with Pidgin users), you can also use it to have secure voice and video communications with other **Jitsi** users. **Jitsi** is available for **Microsoft Windows**, **GNU/Linux**, **Mac OS** and more.

Both **Pidgin** and **OTR** are available for **Microsoft Windows** and for **GNU/Linux**. Another multi-protocol **IM** program for **Microsoft Windows** that supports **OTR** is [**Miranda IM**](http://www.miranda-im.org/). For the **Mac OS** you can use [**Adium**](http://adium.im/), a multi-protocol **IM** program that supports the **OTR** plugin.

## 1.1 Things you should know about this tool before you start ##

Before you can start using **Pidgin** you must have an existing **IM** account, after which you will register that account to **Pidgin**. For instance, if you have an **Google Account**, you can use their **IM** service **GoogleTalk** with **Pidgin**. The log-in details of your existing **IM** account are used to register and access your account through **Pidgin**. 

**Note**: All users are encouraged to learn as much as possible about the privacy and security policies of their **Instant Messaging account provider**. 

**Pidgin** supports the following **IM** services: [**AIM**](http://dashboard.aim.com/aim), [**Bonjour**](http://www.apple.com/support/bonjour/), [**Gadu-Gadu**](http://komunikator.gadu-gadu.pl/), [**Google Talk**](http://www.google.com/talk/), **Groupwise**, [**ICQ**](http://www.icq.com), **IRC**, [**MSN**](http://www.msn.com/), [**MXit**](http://www.mxit.com/), [**MySpaceIM**](http://www.myspace.com/guide/im), [**SILC**](http://silcnet.org/), **SIMPLE**, [**Sametime**](http://www.ibm.com/developerworks/downloads/ls/lst/), [**Yahoo!**](http://messenger.yahoo.com/), **Zephyr** and any **IM** clients running the **XMPP** messaging protocol.

**Pidgin** does not permit communication between different **IM** services. For instance, if you are using **Pidgin** to access your **Google Talk** account, you will not be able to chat with a friend using an **ICQ** account. 

However, **Pidgin** can be configured to manage multiple accounts based on any of the supported messaging protocols. That is, you may simultaneously use both **Gmail** and **ICQ** accounts, and chat with correspondents using *either* of those specific services (which are supported by **Pidgin**). 

**Off-the-Record** (**OTR**) messaging is a plugin developed specifically for **Pidgin**. It offers the following privacy and security features: 

- **Authentication**: You are assured the correspondent is who you think it is.
- **Deniability**: After the chat session is finished, messages cannot be identified as originating from either your correspondent or you.
- **Encryption**: No one else can access and read your instant messages.
- **Perfect Forward Security**: If third party obtains your private keys, no previous conversations are compromised.

**Note**: **Pidgin** must be installed before the **OTR** plugin.


