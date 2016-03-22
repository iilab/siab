

---

lang: xx
community: guide
type: tactics
legacy: True
child: True
weight: 3
depth: 3
title: Securing other Internet communication tools

---

Much like email, instant messaging and [*VoIP*](/en/glossary#VoIP) software can be secure or insecure, depending on the tools you choose and how you use them.

**Securing your instant messaging software**

Instant messaging, also called 'chat,' is not normally secure, and can be just as vulnerable to surveillance as email. Luckily, there are programs that can help secure the privacy of your chat sessions. Just like with email, though, a secure communications channel requires that both you and your instant messaging contacts use the same software and take the same security precautions.

There is a chat program called [*Pidgin*](/en/glossary#Pidgin) that supports many existing instant messaging protocols, which means that you can easily begin using it without having to change your account name or recreate your list of contacts. In order to have private, [*encrypted*](/en/glossary#Encryption) conversations through [*Pidgin*](/en/glossary#Pidgin) , you will need to install and activate the *Off-the-Record [*OTR*](/en/glossary#OTR)* plug-in. Fortunately, this is a fairly simple process. 

<div class="getstarted" markdown="1">
**Hands-on: Get started with the** [*Pidgin with OTR - Secure Instant Messaging Guide*](/en/pidgin_main)
</div>

<div class="background" markdown="1">
Pablo: If Yahoo webmail is insecure, does that mean that Yahoo Chat is insecure, too?
			
Claudia: The thing to remember is that, if we want to use instant messaging to discuss this report, we need to make sure that everyone involved has Pidgin and OTR installed. If they do, we can use Yahoo chat or any other chat service.
</div>

**Securing your VoIP software**


[*VoIP*](/en/glossary#VoIP) calls to other [*VoIP*](/en/glossary#VoIP) users are generally free of charge. Some programs allow you to make inexpensive calls to phones as well, including international numbers. Needless to say, these features can be extremely useful. Some of today's more popular [*VoIP*](/en/glossary#VoIP) programs include [Skype](http://www.skype.com) (see below), [Jitsi](http://jitsi.org/), [Google Hangouts](http://www.google.com/hangouts), and [Yahoo! Voice](http://voice.yahoo.com/).

Normally, voice communication over the Internet is no more secure than unprotected email and instant messaging. When using voice communication to exchange sensitive information it is important to choose a tool that encrypts the call all the way from your computer to the recipient's computer. It also best to use Free and Open-Source Software, preferably those reviewed, tested, and recommended by a trusted community. Taking above criteria we would recommend that you try [*Jitsi*](http://jitsi.org/) as your choice for VoIP.

<div class="getstarted" markdown="1">
**Hands-on: Get started with the** [*Jitsi - Secure Audio, Video and Instant Messaging Text Communication*](/en/jitsi)
</div>

**Notice about Skype's security**

[*Skype*](/en/glossary#Skype) is a very common instant messaging and VoIP tool that also supports calls to landlines and mobile phones. Despite its popularity, several issues make this software not a secure choice. Some of these issues are described below.

While according to Skype, it [*encrypts*](/en/glossary#Encryption) both messages and voice calls, this would only happen when both communicating sides are using Skype programs. Skype does not encrypt calls to phone or text sent as SMS messages.

If both communicating sides are using (a genuine) Skype program, its encryption may make the call nominally more secure than an ordinary call over phone. But because Skype is a closed-source program, making an independent audit and evaluation of its proclamations about encryption impossible, it is thus impossible to verify how well Skype is protecting the users and their information and communication. [***Chapter 1: How to protect your computer from malware and hackers***](/en/chapter-1) addresses the virtues of *Free and Open-Source Software* [*FOSS*](/en/glossary#FOSS) in the [***Keeping your software up-to-date***](/en/chapter_1_4) section.

As mentioned, while we can't recommend Skype as a secure communication tool, it is very important to take some precautions if one still decides to use Skype as a tool for their sensitive communication:

- Download and install Skype only from its official website [www.skype.com](http://www.skype.com) to avoid a Skype program infected with spyware. It is important to always double-check the URL to make sure you are connecting to the official site. In some countries the Skype website is blocked, and/or several fake sites claiming to be Skype's official site are in operation. In many such cases, the version of Skype available is likely infected with malware designed to spy on any communication. Use circumvention tools described in [Chapter 8](/en/chapter-8) to connect to the Skype website and download a genuine version of Skype program whenever you want to install or upgrade to newest version of the software.
- It is very important to change your Skype password regularly. Skype allows for multiple logins from different locations and does not inform you about the number of simultaneous sessions. This poses a big risk that if your password is compromised, anyone with that password can also be logged in. All logged sessions receive all the text communication and have access to calls history. Changing the password is the only way to disable such rogue sessions (by forcing a re-login).
- It is also advisable to set the privacy settings on Skype so that it does not keep a history of chats.
- It is recommended to disable the Skype setting which automatically accepts incoming files, as this has occasionally been used to introduce malware/spyware onto computers.
- Always independently verify the identity of the person with whom you are communicating. It is easier to do this when voice chatting, especially if you know the person you want to talk to.
- Decide if your Skype username should identify your or have any relationship to your real name, or the name of you organisation.
- Always have alternative ways for communicating - Skype can become unavailable at any moment.
- Be careful of what you say - develop a code system to discuss sensitive topics without using specific terminology.

Despite Skype's popularity, the above concerns make it questionable for a secure experience, and we recommend you start using tools like Jitsi for VoIP and [*Pidgin*](/en/glossary#Pidgin) with the [*OTR*](/en/glossary#OTR) plugin for secure instant messaging.

