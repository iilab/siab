
---

lang: en
community: guide
type: tactics
weight: 055
title: Use smartphones as securely as possible

---

In our guide [***How to use mobile phones as securely as possible***](mobile-phones), we discussed the security challenges of using basic mobile phones – including issues with voice communication and text messaging (SMS/MMS) services. Those phones primarily (if not exclusively) use mobile networks to transfer calls and data.

Advances in technology now mean that mobile phones can provide services and features similar to desktop or laptop computers. These smartphones offer many new ways to communicate and capture and disseminate media. To provide these new functionalities, the smartphones not only use the mobile network, but also connect to the internet either via a wifi connection (similar to a laptop at an internet cafe) or via data connections through the mobile network operator.

So while you can, of course, make phone calls with a smartphone, it is better to view smartphones as small computing devices. This means that the other material in this toolkit is relevant to your use of your smartphone as well as your computer.

Smartphones usually support a wide range of functionality – web browsing, email, voice and instant messaging over the internet, capturing, storing and transmitting audio, videos and photos, enabling social networking, multi-user games, banking and many other activities. However, many of these tools and features introduce new security issues, or increase existing risks. 

For instance, some smartphones have built-in geo-location ([*GPS*](/en/Glossary#GPS)) functionality, which means they can provide your precise location to your mobile network operator by default, and to many applications you use on your phone (such as social networking, mapping, browsing and other applications). As mentioned before, mobile phones already relay your location information to your mobile network operator (as part of the normal functions of the phone). However, the additional GPS functionality not only increases the precision of your location information, it also increases the amount of places where this information might be distributed.

It's worth reviewing all the risks associated with mobile phones discussed in our guide [***How to use mobile phones as securely as possible***](mobile-phones) as all of them are also relevant to smartphone use. That guide also covers issues of eavesdropping, interception of SMS or phone calls, SIM card related issues, and best practices.

In this guide we'll take a look at the additional security challenges posed by smartphones.

# What you can learn from this guide

- How to use smartphones as securely as possible

## Introduction to smartphone security

**Purses, Wallets,  Smartphones**

We have an intuitive understanding of the value of keeping our purse or wallet safe, because so much sensitive information is stored in them, and losing them will compromise our privacy and safety.  People are less aware of the amount of personal information being carried in their smartphones, and consider losing a phone a nuisance rather than a risk. If you also think that a smartphone is a computing device which is always connected to a network and is continually carried around, it also highlights the important difference between a holder of discrete, passive information (like a wallet), and an active and interactive item like a smartphone.

A simple exercise can help illustrate this:

Empty the content of your wallet or purse, and take account of sensitive items. Typically you may find:
- Pictures of loved ones (~5 pictures)
- Identification cards (driver's license, membership cards, social security cards)
- Insurance and health information  (~2 cards)
- Money (~5 bills)
- Credit/Debit cards (~3 cards)

Now, examine the contents of your smartphone. A typical smartphone user may find some of the above in higher quantities, and in some cases much more valuable items:

- Pictures of loved ones (~100 pictures)
- Email applications and their passwords
- Emails (~500 emails)
- Videos (~50 videos)
- Social networking applications and their passwords
- Banking applications (with access to the bank accounts)
- Sensitive documents
- Sensitive communication records
- A live connection to your sensitive information 

The more you use smartphones, the more you need to become aware of the associated risks and take appropriate precautions. Smartphones are powerful amplifiers and distributors of your personal data. They are designed to provide as much connectivity as possible and to link to social networking services by default. This is because your personal data is valuable information that can be aggregated, searched and sold. 

In our guide [***How to recover from information loss***](backup) we discussed the importance of backing up data. This applies in particular to smartphones. It can be disastrous if you lose your phone without having a backup of your most important data (such as your contacts) in a secure location. Besides backing up your data, make sure you also know how to restore the data. Keep a hard copy of the steps you need to take so you can do it quickly in an emergency.

In this chapter we'll start by introducing some smartphone basics – a description of various platforms and some basic setup procedures for securing your information and communication. The remaining parts of this chapter will cover specific precautions related to common uses of smartphones.




# Platforms, setup and installation

**Platforms and Operating Systems**

At the time of writing, the most common smartphones in use are Apple's iPhone and Google's Android, followed by Blackberry and Windows phones. The key difference between Android and other operating systems is that Android is, mostly, an Open Source ([*FOSS*](/en/Glossary#FOSS)) system, which allows the operating system to be audited independently to verify if it properly protects users' information and communication. It also facilitates development of security applications for this platform. Many security-aware programmers develop Android applications with user safety and security in mind. Some of these will be highlighted later in this chapter.

Regardless what type of smartphone you are using, there are issues that you should be aware of when you use a phone which connects to the internet and comes with features such as [*GPS*](/en/glossary#GPS) or wireless networking capacities. In this chapter we focus on devices with the Android platform, because, as mentioned above, it's easier to secure data and communications. Nonetheless, basic setup guides and some applications for devices other than Android phones are provided, too.

Blackberry phones have been presented as “secure” messaging and email devices. This is because messages and emails are securely channeled through Blackberry servers, out of the reach of potential eavesdroppers. Unfortunately, more and more governments are demanding access to these communications, citing need for guarding against potential terrorism and organised crime. India, United Arab Emirates, Saudi Arabia, Indonesia and Lebanon are examples of governments which have scrutinized the use of Blackberry devices and demanded access to user data in their countries.

**Feature Phones**

Another category of mobiles are often called 'feature phones' (e.g.  Nokia 7705 Twist or Samsung Rogue). Recently, feature phones have increased their functionalities to include those of some smartphones. But generally, feature phones' operating systems are less accessible, therefore there are limited opportunities for security applications or improvements. We do not specifically address feature phones, although many measures discussed here make sense for feature phones too.

**Branded and locked smartphones**

Smartphones are usually sold branded or locked. Locking smartphones means that the device can only be operated with one carrier, whose SIM card is the only one that will work in the device. Mobile network operators usually brand a phone by installing their own firmware or software. They may also disable some functionalities or add others. Branding is a means for companies to increase revenue by channelling your smartphone use, often also collecting data about how you are using the phone or by enabling remote access to your smartphone.

For these reasons, we recommend that you buy an unbranded smartphone if you can. A locked phone poses a higher risk since all your data is routed through one carrier, which centralises your data streams and makes it impossible to change SIM cards to disseminate the data over different carriers. If your phone is locked, ask someone you trust about unlocking it.

**General Setup**

Smartphones have many settings which control the security of the device. It is important to pay attention to how your smartphone is set up. In the Hands-on Guides below we will alert you to certain smartphone security settings that are available but not active by default, as well as those which are active by default and make your phone vulnerable.


:[Hands-on: get started with Basic Android security setup guide](../../tools/android/basic-setup)

**Installing and updating applications**

The usual way to install new software on your smartphone is to use the iPhone Appstore or Google Play store, log in with your user credentials, and download and install a desired application. By logging-in you associate your usage of the online store with the logged-in user account. The owners of the application store keep records of this user's browsing history and application choices.

The applications which are offered in the official online store are, supposedly, verified by store owners (Google or Apple), but in reality this provides weak protection against what applications will do after being installed on your phone. For example, some applications may copy and send out your address book after you install them on your phone. On Android phones each application needs to request, during the installation process, what it will be permitted to do when it is in use. You should pay close attention to what permissions are requested, and if these permissions make sense for the function of the app you are installing. For example, if you are considering a "news reader" application and you find out that it requests the rights to send your contacts over a mobile data connection to a third party, you should look for alternative applications with appropriate access and rights.
)ites. Some users may want to consider these alternative sites to minimize online contact with Google. One of the alternative store is [**F-Droid**](http://f-droid.org) ('Free Droid'), which only provides [*FOSS*](/en/glossary#FOSS) applications. However please remember that you should trust the site before you download any apps from it. For inexperienced users we recommend that you use Google Play store.

If you don't want to (or are unable to) go online to access apps, you can transfer apps from someone else's phone by sending [*.apk*](/en/glossary#apk) files (short for 'android application package') via bluetooth. Alternetively you could download the .apk file to your device's Micro SD card or use a usb cable to move it there from a PC. When you have received the file, simply long tap on the filename and you will be prompted to install it. (**Note**: be especially careful while using bluetooth - read further in the section on  [***Functions beyond speech and messages***](mobile-phones#546).


# Communicating securely (through voice and messages) with a smartphone





## Secure voice communication

**Basic telephony**

In the section on [***Basic functions, trackability and anonymity***](mobile-phones#544) in our guide, [***How to use mobile phones as securely as possible***](mobile-phones), we discussed different measures you should consider to lower the risk of interception when using the mobile phone operator network for your voice communication.

Using Internet through your smartphone over mobile data connections or WiFi can provide more secure ways to communicate with people, namely by using [*VoIP*](/en/Glossary#VoIP) and employing means to secure this channel of communication. Some smartphone tools can even extend some of this security beyond VoIP, to mobile phone calls as well (See **Redphone** below).

Here we list a few tools and their pros and cons:

**Skype**

The most popular commercial VoIP application, [*Skype*](/en/glossary#skype), is available for all smartphone platforms and works well if your wireless connectivity is reliable. It is less reliable on mobile data connections.

In the section [***Securing other internet communication tools***](secure-communication#501) of our guide [**How to keep your Internet communication private**](secure-communication), we discussed the risks of using Skype, and why, if possible, it should be avoided. In summary, Skype is a non Open-Source software what makes it very difficult to independently confirm its level of security. Additionally, Skype is owned by Microsoft, which has a commercial interest in knowing when you use Skype and from where. Skype also may allow law enforcement agencies retrospective access to all your communications history.

**Other VoIP tools**

Using VoIP is generally free (or significantly cheaper than mobile phone calls) and leaves few data traces. In fact, a secured VoIP call can be the most secure way to communicate.

[**RedPhone**](https://play.google.com/store/apps/details?id=org.thoughtcrime.redphone) is a Free and Open-Source Software application that encrypts voice communication data sent between two devices that run this application. It is easy to install and very easy to use, since it integrates itself into your normal dialing and contact scheme. But people you want to talk to also need to install and use RedPhone. For ease of use, RedPhone uses your mobile number as a way to identify you to your contacts. Unfortunately, this makes it more difficult to use RedPhone without a functioning mobile service plan, even on devices capable of using WiFi to connect to the Internet. RedPhone also uses a central server, which puts the administrators of the service in a powerful position by allowing them to see much of the meta-data related to your encrypted VoIP calls.


:[Hands-on: get started with RedPhone](../../tools/android/redphone)


[**CSipSimple**](http://f-droid.org/repository/browse/?fdid=com.csipsimple&fdpage=4) is a powerful VoIP client for Android phones that is well maintained and comes with many easy set-up wizards for different VoIP services.

[**Open Secure Telephony Network (OSTN)**](https://guardianproject.info/wiki/OSTN) and the server provided by the Guardian project, [**ostel.co**](https://ostel.co), currently offers one of the most secure means to communicate via voice. Knowing and trusting the entity that operates the server for your VoIP communication needs is an important consideration. 

When using CSipSimple, you never directly communicate with your contact, instead all your data is routed through the Ostel server. This makes it much harder to trace your data and find out who you are talking to. Additionally, Ostel doesn't retain any of this data, except the account data that you need to log in. All your speech is securely encrypted and even your meta data, which is usually very hard to disguise, is blurred since traffic is proxied through the ostel.co server. If you download CSipSimple from ostel.co it also comes preconfigured for use with ostel, which makes it very easy to install and use.

*Tool Guides* for CSipSimple and Ostel.co are forthcoming. In the meantime, more information can be found by following the links above.



## Sending messages securely
You should use precautions when sending SMS and using instant messaging or chatting on your smartphone.

**SMS**

As described in [**Use mobile phones as securely as possible**](mobile-phones) (in the section on [***Text based communications***](mobile-phones#545) ), SMS communication is insecure by default. Anyone with access to a mobile telecommunication network can intercept these messages easily and this is an everyday occurrence in many situations. Don't rely on sending unsecured SMS messages in critical situations. There is also no way of authenticating SMS messages, so it is impossible to know if the contents of a message was changed during delivery or if the sender of the message really is the person they claim to be.

**Securing SMS**

[**TextSecure**](https://play.google.com/store/apps/details?id=org.thoughtcrime.securesms) is a [*FOSS*](/en/glossary#FOSS) tool for sending and receiving secure SMS on Android phones. It works both for encrypted and non-encrypted messages, so you can use it as your default SMS application. To exchange encrypted messages this tool has to be installed by both the sender and the recipient of a message, so you will need to get people you communicate with regularly to use it as well. TextSecure automatically detects when an encrypted message is received from another TextSecure user. It also allows you to send encrypted messages to more than one person. Messages are automatically signed making it nearly impossible to tamper with the contents of a message. In our TextSecure hands-on guide we explain in detail the features of this tool and how to use it.


:[Hands-on: get started with TextSecure for Android](../../tools/android/textsecure)

**Secure Chat**

Instant messaging and chatting on your phone can produce a lot of information that is at risk of interception. These conversations might be used against you by adversaries at a later date. You should therefore be extremely wary about what you reveal when you are writing on your phone while instant messaging and chatting.

There are ways to chat and instant message securely. The best way is to use end-to-end encryption, as this will enable you to make sure the person on the other end is who you want. 

We recommend ChatSecure as a secure text chat application for the Android phones. ChatSecure offers easy and strong encryption for your chats with [*Off-the-Record*](/en/glossary#OTR) Messaging protocol. This encryption provides both authenticity (you can verify that you are chatting with the right person) and the independent security of each session so that even if the encryption of one chat session is compromised, other past and future sessions will remain secure.

ChatSecure has been designed to work together with Orbot, so your chat messages can be routed through the [*Tor*](/en/glossary#Tor) anonymizing network. This makes it very hard to trace it or even find out that it happened.

For iPhones, the [**ChatSecure**](https://chatsecure.org) client provides the same features, although it is not easy to use it with the [*Tor*](/en/glossary#Tor) network.

Whichever application you will use always consider which account you use to chat from. For example when you use Google Talk, your credentials and time of your chatting session are known to Google. Also agree with your conversation partners on not saving chat histories, especially if they aren't encrypted.



# Storing Information on your Smartphone

Smartphones come with large data storage capacities. Unfortunately, the data stored on your device can be easily accessible by third parties, either remotely or with physical access to the phone. Some basic precautions to reduce inappropriate access to this information are explained in the [***Basic Set-Up Guide for Android***](basic-setup/android). Additionally, you can take steps to encrypt any sensitive information on your phone by using specific tools.



## Data encryption tools

The [**Android Privacy Guard (APG)**](apg/android) allows OpenGPG encryption for files and emails. It can be used to keep your files and documents safe on your phone, as well when emailing.


:[Hands-on: get started with Android Privacy Guard (APG) for Android devices](../../tools/android/apg)




## Recording passwords securely

You can keep all your needed passwords in one secure, encrypted file by using **Keepass**. You will only need to remember one master password to access all the others. With Keepass you can use very strong passwords for each account you have, as Keepass will remember them for you, and it also comes with a password generator to create new passwords. You can synchronise Keepass password databases between your phone and your computer. We recommned that you synchronise only those passwords that you will actually use on your mobile phone. You can create a separate smaller password database on the computer and syncronise this one instead of coping an entire database with all the passwords that you use to your smartphone. Also, since all the passwords are protected by your master password, it is vital to use very strong password for your Keepass database. See our guide [***How to create and maintain secure passwords***](passwords). 


:[Hands-on: get started with KeePassDroid for Android](../../tools/android/keepassdroid)




# Sending Email from your smartphone

In this section we will briefly discuss the use of email on smartphones. We encourage you to refer to sections [***Securing your email***](secure-communication#496) and [***Tips on responding to suspected email surveillance***](secure-communication#500) in [***our guide How to keep your Internet communication private***](secure-communication) where we discuss basic email security.

In the first instance, consider if you really need to use your smartphone to access your email. Securing a computer and its content is generally simpler than doing so for a mobile device such as a smartphone. A smartphone is more susceptible to theft, monitoring and intrusion. 

If it is absolutely vital that you access your email on your smartphone, there are actions you can take to minimize the risks. 

- Do not rely on smartphone as your primary means for accessing your email. Downloading (and removing) emails from an email server and storing them only on your smartphone is not advised. You can set up your email application to use only copies of emails.

- If you use email encryption with some of your contacts, consider installing it on your smartphone, too. The additional benefit is that encrypted emails will remain secret if the phone falls into wrong hands.

Storing your private encryption key on your mobile device may seem risky. But the benefit of being able to send and store emails securely encrypted on the mobile device might outweigh the risks. Consider creating a mobile-only encrytpion key-pair (using [**APG**](apg/android)) for your use on your smartphone, so you do not copy your encryption private key from your computer to the mobile device. Note that this requires that you ask people you communicate with to also encrypt emails using your mobile-only encryption key. 


:[Hands-on: get started with K9 with APG for Android](../../tools/android/k9)




# Capturing media with your smartphone

Capturing pictures, video or audio with your smartphone can be a powerful means to document and share important events. However, it is important to be careful and respectful of privacy and safety of those pictured, filmed or recorded. For example, if you take photos or record video or audio of an important event, it might be dangerous to you or to those who appear in the recordings, if your phone fell into the wrong hands. In this case, these suggestions may be helpful:

- Have a mechanism to securely upload recorded media files to protected online location and remove them from the phone instantly (or as soon as you can) after recording.

- Use tools to blur the faces of those appearing in the images or videos or distort the voices of audio or videos recordings and store only blurred and distorted copies of media files on your mobile device.

- Protect or remove meta information about time and place within the media files.

[**Guardian Project**](https://guardianproject.info) has created a [*FOSS*](/en/glossary#FOSS) app called [**ObscuraCam**](https://guardianproject.info/apps/obscuracam/) to detect faces on photos and blur them. You can choose the blurring mode and what to blur, of course. Obscuracam also deletes the original photos and if you have set up a server to upload the captured media, it provides easy functionality to upload it. 


:[Hands-on: get started with ObscuraCam for Android](../../tools/android/obscuracam)

At the time of writing, the human rights organisation [**Witness**](http://www.witness.org) is working with the Guardian project on a solution to all three of the above points. 



# Accessing the Internet securely from your smartphone

As discussed in our guide [**How to keep your Internet communication private**](secure-communication) and our guide [**How to remain anonymous and bypass censorship on the Internet**](anonymity-and-circumvention), access to content on the Internet, or publishing material online such as photos or videos, leaves many traces of who and where you are and what you are doing. This may put you at risk. Using your smartphone to communicate with the Internet magnifies this risk.




## Access through WiFi or mobile data

Smartphones allow you to control how you access the Internet: via a wireless connection provided by an access point (such as an internet cafe), or via a mobile data connection, such as GPRS, EDGE, or UMTS provided by your mobile network operator. 

Using a WiFi connection reduces the traces of data you may be leaving with your mobile phone service provider (by not having it connected with your mobile phone subscription). However, sometimes a mobile data connection is the only way to get online. Unfortunately mobile data connection protocols (like EDGE or UMTS) are not open standards. Independent developers and security engineers cannot examine these protocols to see how they are being implemented by mobile data carriers. 

In some countries mobile access providers operate under different legislation than internet service providers, which can result in more direct surveillance by governments and carriers.

Regardless of which path you take for your digital communications with a smartphone, you can reduce your risks of data exposure through the use of anonymising and encryption tools.




## Anonymity on your smartphone

To access content online anonymously, you can use an Android app called [**Orbot**](https://www.torproject.org/docs/android.html.en). Orbot channels your internet communication through Tor's anonymity network. 


:[Hands-on: get started with Orbot for Android](../../tools/android/orbot)

Another app, Orweb, is a web browser that has privacy enhancing features like using proxies and not keeping a local browsing history. Orbot and Orweb together circumvent web filters and firewalls, and offer anonymous browsing.


:[Hands-on: get started with Orweb for Android](../../tools/android/orweb)



## Proxies

The mobile version of [*Firefox*](/en/glossary#Firefox) – [**Firefox mobile**](http://f-droid.org/repository/browse/?fdid=org.mozilla.firefox) can be equipped with proxy add-ons, which direct your traffic to a proxy server. From there your traffic goes to the site you are requesting. This is helpful in cases of censorship, but still may reveal your requests unless the connection from your client to the proxy is encrypted. We recommend the [**Proxy Mobile**](https://guardianproject.info/apps/proxymob-firefox-add-on/) add-on (also from [**Guardian Project**](https://guardianproject.info/), which makes proxying with Firefox easy. Is also the only way to channel Firefox mobile communications to Orbot and use the [*Tor*](/en/glossary#Tor) network. 




# Advanced smartphone security





## Get full access to your smartphone

Most smartphones are capable of more than their installed operating system, manufacturers' software (firmware), or the mobile operators' programmes allow. Conversely, some functionalities are 'locked in' so the user is not capable of controlling or altering these functions, and they remain out of reach. In most cases those functionalities are unnecessary for smartphone users. There are however, some applications and functionalities that can enhance the security of data and communications on a smartphone. Also there are some other existing functionalities that can be removed to avoid security risks.

For this, and other reasons, some smartphone users choose to manipulate the various software and programs running the smartphone in order to gain appropriate privileges to allow them to install enhanced functionalities, or remove or reduce other ones.

The process of overcoming the limits imposed by mobile carriers, or manufacturers of operating systems on a smartphone is called rooting (in case of Android devices), or jailbreaking (in case of iOS devices, like iPhone or iPad). Typically, successful rooting or jailbreaking will result in your having all the privileges needed to install and use additional applications, make modifications to otherwise locked-down configurations, and total control over data storage and memory of the smartphone.

**WARNING**: Rooting or jailbreaking may not be a reversible process, and it requires experience with software installation and configuration. Consider the following:

- There is a risk of making your smartphone permanently inoperable, or 'bricking' it (i.e. turning it into a 'brick').
- The manufacturer or mobile carrier warranty may be voided.
- In some places, this process maybe illegal.

But if you are careful, a rooted device is a straightforward way to gain more control over your smartphone to make it much more secure.




## Alternative firmwares

Firmware refers to programmes that are closely related to the particular device. They are in cooperation with the device's operating system and are responsible for basic operations of the hardware of your smartphone, such as the speaker, microphone, cameras, touchscreen, memory, keys, antennas, etc.

If you have an Android device, you might consider installing a firmware alternative to further enhance your control of the phone. Note that in order to install alternative firmware, you need to root your phone.

An example of an alternative firmware for an Android phone is [**Cyanogenmod**](http://www.cyanogenmod.com) which, for example, allows you to uninstall applications from the system level of your phone (i.e. those installed by the phone's manufacturer or your mobile network operator). By doing so, you can reduce the number of ways in which your device can be monitored, such as data that is sent to your service provider without your knowledge. 

In addition, Cyanogenmod ships by default with an OpenVPN application, which can be tedious to install otherwise. VPN (Virtual Private Network) is one of the ways to securely proxy your internet communication (see below). 

Cyanogenmod also offers an Incognito browsing mode in which history of your communication is not recorded on your smartphone.

Cyanogenmod comes with many other features. However, it is not supported by all Android devices, so before proceeding, check out the [list of supported devices](http://www.cyanogenmod.com/devices).
 



## Full device encryption

If your phone is rooted you may consider encrypting it's entire data storage or creating a volume on the smartphone to protect some information on the phone.

[**Luks Manager**](https://play.google.com/store/apps/details?id=com.nemesis2.luksmanager&hl=en) allows easy, on-the-fly strong encryption of volumes with an user-friendly interface. We highly recommend that you install this tool before you start storing important data on your Android device and use the Encrypted Volumes that the Luks Manager provides to store all your data.




## Virtual Private Network (VPN) security

A VPN provides an encrypted tunnel through the internet between your device and a VPN server. This is called a tunnel, because unlike other encrypted traffic, like https, it hides all services, protocols, and contents. A VPN connection is set up once, and only terminates when you decide.

Note that since all your traffic goes through the proxy or VPN server, an intermediary only needs to have access to the proxy to analyze your activities. Therefore it is important to carefully choose amongst proxy services and VPN services. It is also advisable to use different proxies and/or VPNs since distributing your data streams reduces the impact of a compromised service.

We recommend using the [**RiseUp VPN**](https://help.riseup.net/en/vpn) server. You can use RiseUp VPN on Android device after installing Cyanogenmod (see above). It is also easy to setup connection to RiseUp VPN on the iPhone - read more [here](https://support.apple.com/kb/HT1424).



