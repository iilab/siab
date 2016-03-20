

---

lang: xx
community: guide
type: tactics
legacy: True
child: True
weight: 2
depth: 3
title: Communicating (Voice and Messages) via Smartphone

---

## Talking Securely ##

### Basic telephony ###

In the section on [***Basic functions, trackability and anonymity***](/en/chapter_10_2_2) in [***Chapter 10: How to use mobile phones as securely as possible***](/en/chapter-10) we discussed different measures you should consider to lower the risk of interception when using the mobile phone operator network for your voice communication.

Using Internet through your smartphone over mobile data connections or WiFi can provide more secure ways to communicate with people, namely by using [*VoIP*](/en/Glossary#VoIP) and employing means to secure this channel of communication. Some smartphone tools can even extend some of this security beyond VoIP, to mobile phone calls as well (See **Redphone** below).

Here we list a few tools and their pros and cons:

### Skype ###

The most popular commercial VoIP application, [*Skype*](/en/glossary#skype), is available for all smartphone platforms and works well if your wireless connectivity is reliable. It is less reliable on mobile data connections.

In the section [***Securing other internet communication tools***](/en/chapter_7_3) of [***Chapter 7: How to keep your Internet communication private***](/en/chapter-7), we discussed the risks of using Skype, and why, if possible, it should be avoided. In summary, Skype is a non Open-Source software what makes it very difficult to independently confirm its level of security. Additionally, Skype is owned by Microsoft, which has a commercial interest in knowing when you use Skype and from where. Skype also may allow law enforcement agencies retrospective access to all your communications history.

### Other VoIP ###

Using VoIP is generally free (or significantly cheaper than mobile phone calls) and leaves few data traces. In fact, a secured VoIP call can be the most secure way to communicate.

[**CSipSimple**](http://f-droid.org/repository/browse/?fdid=com.csipsimple&fdpage=4) is a powerful VoIP client for Android phones that is well maintained and comes with many easy set-up wizards for different VoIP services.

[**Open Secure Telephony Network (OSTN)**](https://guardianproject.info/wiki/OSTN) and the server provided by the Guardian project, [**ostel.co**](https://ostel.co), currently offers one of the most secure means to communicate via voice. Knowing and trusting the entity that operates the server for your VoIP communication needs is an important consideration. 

When using CSipSimple, you never directly communicate with your communication partner, instead all your data is routed through the Ostel server. This makes it much harder to trace your data and find out who you are talking to. Additionally, Ostel doesn't retain any of this data, except the account data that you need to log in. All your speech is securely encrypted and even your meta data, which is usually very hard to disguise, is blurred since traffic is proxied through the ostel.co server. If you download CSipSimple from ostel.co it also comes preconfigured for use with ostel, which makes it very easy to install and use.

[**RedPhone**](https://play.google.com/store/apps/details?id=org.thoughtcrime.redphone) is a Free and Open-Source Software application that encrypts voice communication data sent between two devices that run this application. It is easy to install and very easy to use, since it integrates itself into your normal dialing and contact scheme. But people you want to talk to also need to install and use RedPhone. For ease of use RedPhone uses your mobile number as your identificator (like a user name on other VoIP services). However it also becomes easier to analyze the traffic it produces and trace it back to you, through your mobile number. RedPhone uses a central server, which is a point of centralization and thus puts RedPhone in a powerful position (of having control over some of this data). 

Hands-on Guides for CSipSimple, Ostel, and Redphone are forthcoming. In the meantime, more information can be found by following the above links.

## Sending Messages Securely ##

You should use precautions when sending SMS and using instant messaging or chatting on your smartphone.

### SMS ###

As described in [***Chapter 10***](/en/chapter-10) (in the section on [***Text based communications***](/en/chapter_10_2_3) ), SMS communication is insecure by default. Anyone with access to a mobile telecommunication network can intercept these messages easily and this is an everyday occurrence in many situations. Don't rely on sending unsecured SMS messages in critical situations. There is also no way of authenticating SMS messages, so it is impossible to know if the contents of a message was changed during delivery or if the sender of the message really is the person they claim to be.

### Securing SMS ###

[**TextSecure**](https://play.google.com/store/apps/details?id=org.thoughtcrime.securesms) is a [*FOSS*](/en/glossary#FOSS) tool for sending and receiving secure SMS on Android phones. It works both for encrypted and non-encrypted messages, so you can use it as your default SMS application. To exchange encrypted messages this tool has to be installed by both the sender and the recipient of a message, so you will need to get people you communicate with regularly to use it as well. TextSecure automatically detects when an encrypted message is received from another TextSecure user. It also allows you to send encrypted messages to more than one person. Messages are automatically signed making it nearly impossible to tamper with the contents of a message. In our TextSecure hands-on guide we explain in detail the features of this tool and how to use it.

<div class=getstarted markdown=1>
Hands-on: Get started with the [*TextSecure Guide*](/en/textsecure_main)
</div>

### Secure Chat ###

Instant messaging and chatting on your phone can produce a lot of information that is at risk of interception. These conversations might be used against you by adversaries at a later date. You should therefore be extremely wary about what you reveal when you are writing on your phone while instant messaging and chatting.

There are ways to chat and instant message securely. The best way is to use end-to-end encryption, as this will enable you to make sure the person on the other end is who you want. 

We recommend [**Gibberbot**](https://securityinabox.org/en/gibberbot_main)* as a secure text chat application for the Android phones. Gibberbot offers easy and strong encryption for your chats with [*Off-the-Record*](/en/glossary#OTR) Messaging protocol. This encryption provides both authenticity (you can verify that you are chatting with the right person) and the independent security of each session so that even if the encryption of one chat session is compromised, other past and future sessions will remain secure.

Gibberbot has been designed to work together with Orbot, so your chat messages can be routed through the [*Tor*](/en/glossary#Tor) anonymizing network. This makes it very hard to trace it or even find out that it happened.

<div class=getstarted markdown=1>
Hands-on: Get started with the [*Gibberbot Guide*](/en/gibberbot_main)
</div>

For iPhones, the [**ChatSecure**](https://chatsecure.org) client provides the same features, although it is not easy to use it with the [*Tor*](/en/glossary#Tor) network.

A Hands-on Guide for ChatSecure is forthcoming. In the meantime, more information can be found on its [homepage](https://chatsecure.org). 

Whichever application you will use always consider which account you use to chat from. For example when you use Google Talk, your credentials and time of your chatting session are known to Google. Also agree with your conversation partners on not saving chat histories, especially if they aren't encrypted.

* [22/01/2014] *Gibberbot is now known as ChatSecure. An updated hands-on guide is forthcoming.*

