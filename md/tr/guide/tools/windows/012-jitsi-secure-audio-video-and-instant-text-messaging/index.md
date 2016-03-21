

---

lang: tr
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 012
title: Jitsi - Secure Audio, Video and Instant Text Messaging 

---

**Homepage**

- [**https://jitsi.org/**](https://jitsi.org/)

**Computer Requirements**

- All Windows Versions

**Version used in this guide**

- 2.4

**Last revision of this chapter**

- January 2014

**License**

- Free and Open-Source Software

**What you will get in return**: 

- The ability to have a private and secure integrated communications system, that includes video chat sessions.
- The ability to encrypt your communication independently of your account providers.
- The ability to register and use different accounts (e.g. **Facebook**, **Google Talk**, **Yahoo Messenger**) simultaneously.

**GNU Linux, Mac OS and other Microsoft Windows Compatible Programs**:

**Jitsi** is available for **GNU Linux**, **Mac OS**, as well as **MS Windows** (and soon for **Android OS**). Other programs that **Jitsi** can communicate with using independent **OTR** or **ZRTP** encryption are recommended below:

- For **text messaging**: [**Pidgin**](/en/pidgin_main) (**MS Windows** and **GNU Linux**), [**Miranda**](http://www.miranda-im.org/) (**MS Windows**), [**Adium**](https://adium.im/) (**Mac OS X**), [**ChatSecure**](https://guardianproject.info/apps/chatsecure/) (**Android OS** and **iOS** formerly known as [**Gibberbot**](/en/Gibberbot_main)) 

- For **voice calls**: **CSipSimple** (**Android OS**), [**Linphone**](http://www.linphone.org/) (**GNU Linux**, **MS Windows**, **Mac OS X**, **Android OS**, **iOS**, and others.)

**1.1 Things you should know about this tool before you start**

**Jitsi** supports many different account types and communication protocols and can thus communicate with correspondents who use different programs. Some of those programs will offer similar features to improve the security of your communication (like programs mentioned in section above), which support independent text and voice encryption (**OTR** and **ZRTP**). Other programs, especially proprietary ones (for instance **Facebook** chat or **Google Talk** ), may not have those features implemented. However, you will still be able to communicate with contacts who are using those proprietary programs with help of **Jitsi* just without the added benefits of **Jitsi's* security features.

Regardless of whether you communicate by text, voice or video, providers of services like **Facebook Chat**, **Google Talk**, **Yahoo! Messanger**, **Skype** or **Viber** have access to your communication sessions and may offer this access to third-parties, such as corporations or governments. **Jitsi** lets you communicate in a private and safe manner using your existing accounts with the help of added encryption. This makes the content of your communication inaccessible to account providers and potential third-parties. In order to protect your private chat sessions and conversations, **Jitsi** uses cryptographic methods including **Off-the-Record** ([**OTR**](/en/glossary#OTR)) for text chats, and **ZRTP/SRTP** for voice calls.

Another notable difference between **Jitsi** and programs like **Skype** is that it enables users to keep using their existing accounts from different service providers, independent of the program developers. This also means that you need to set up an account prior to being able to use **Jitsi**.

**Note**: **Jitsi** uses **Java** programming language. As such, the Java program must be installed on your computer in order for it to work. **Oracle Java** is known to contain many security vulnerabilities that may let remote users assume control of your computer and install spyware to access or monitor all your communication and data. It is **strongly** advised that you minimise the number of programs able to use Java on your computer. Please refer to [**Disabling Java associated plugins in Firefox**](/en/firefox_addons#3.2) and refer to [**steps to disable Java for all browsers on your computer**](https://www.java.com/en/download/help/disable_browser.xml). However as you will see later in this chapter, despite the use of **Java**, there are a number of security benefits when using **Jitsi**.

