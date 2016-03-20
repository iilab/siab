
---

lang: en
community: guide
type: tactics
weight: 035
title: Keep your online communication private

---

The convenience, cost-effectiveness and flexibility of email and instant messaging make them extremely valuable for individuals and organizations with even the most limited access to the Internet. For those with faster and more reliable connections, software such as [*Jitsi*](https://jitsi.org/), [*Skype*](/en/glossary#Skype) and other *Voice-over-IP* [*VoIP*](/en/glossary#VoIP) tools also share these characteristics. Unfortunately, these digital alternatives to traditional means of communication can not always be relied upon to keep sensitive information private. Of course, this is nothing new. Postal mail, telephone calls and text messages are all vulnerable as well, particularly when used by those who may have been targeted for surveillance by the authorities. 

# What you can learn from this guide

- Why most webmail and instant messaging services are not secure
- How to create a new and more secure email account
- How to improve the security in your current email account
- How to use a secure instant messaging service
- What to do if you think someone might be accessing your email
- How to verify the identity of an email correspondent

## Introduction to secure communication
One important difference between digital, Internet-based communication techniques and more traditional methods, is that the former often allow you to determine your own level of security. If you send emails, instant messages and [*VoIP*](/en/glossary#VoIP) conversations using insecure methods, they are almost certainly less private than letters or telephone calls. In part, this is because a few powerful computers can automatically search through a large amount of digital information to identify senders, recipients and specific key words. Greater resources are required to carry out the same level of surveillance on traditional communication channels. However, if you take certain precautions, the opposite can be true. The flexibility of Internet communication tools and the strength of modern [*encryption*](/en/glossary#Encryption) can now provide a level of privacy that was once available only to national military and intelligence organizations.

By following the guidelines and exploring the software discussed in this guide, you can greatly improve your communication security. The [*RiseUp*](/en/glossary#RiseUp)  email service, the Off the Record [*OTR*](/en/glossary#OTR) plugin for the [*Pidgin*](/en/glossary#Pidgin)  instant messaging program, Mozilla [*Firefox*](/en/glossary#Firefox)  and the [*Enigmail*](/en/glossary#Enigmail) add-on for the Mozilla [*Thunderbird*](/en/glossary#Thunderbird)  email client are all excellent tools. While using them, however, you should keep in mind that the privacy of a given conversation is never one hundred percent guaranteed. There is always some threat that you did not consider, be it a [*keylogger*](/en/glossary#Keylogger) on your computer, a person listening at the door, a careless email correspondent or something else entirely. The goal of this guide is to help you reduce even the threats that do not occur to you, while avoiding the extreme position, favoured by some, that you should not send anything over the Internet
that you are not willing to make public. 

{{ snippet: ./035-snippet_01.md }}





# Securing your email

There are a few important steps that you can take in order to increase the security of your email communication. The first is to make sure that only the person to whom you send a given message is able to read it. This is discussed in the  [*Keeping your webmail private*](secure-communication#497) and  [*Switching to a more secure emailaccount*](secure-communication#498) sections, below. Going beyond the basics, it is sometimes critical that your email contacts have the ability to verify that a particular message truly came from you and not from someone who might be attempting to impersonate you. One way to accomplish this is described under [*Advanced email security*](secure-communication#505), in the [*Encrypting and authenticating individual email messages*](secure-communication#508) section.

You should also know what to do if you think the privacy of your email account may have been violated. The [**Tips on responding to suspected email surveillance**](secure-communication#500) section addresses this question. 

Remember, too, that secure email will not do you any good if everything you type is recorded by spyware and periodically sent over the Internet to a third party. Our guide [**How to protect your computer from malware and hackers**](malware) offers some advice on how to prevent this sort of thing, and our guide [**How to create and maintain secure passwords**](passwords) will help you protect your accounts for the email and instant messaging tools described below. 



## Keeping your webmail private
The Internet is an open network through which information typically travels in a readable format. If a normal email message is intercepted on the way to a recipient, its contents can be read quite easily. And, because the Internet is just one large, worldwide network that relies on intermediary computers to direct traffic, many different people may have the opportunity to intercept a message in this way. Your [*Internet Service Provider*](/en/glossary#ISP) is the first recipient of an email message as it begins its journey to the recipient. Similarly, the recipient's [*ISP*](/en/glossary#ISP)  is the last stop for your message before it is delivered. Unless you take certain precautions, your messages can be read or tampered with at either of these points, or anywhere in between.


{{ snippet: ./035-snippet_02.md }}

It has long been possible to secure the Internet connection between your computer and the websites that you visit. You often encounter this level of security when entering passwords or credit card information into websites. The technology that makes it possible is called Secure Sockets Layer [*SSL*](/en/glossary#SSL) [*encryption*](/en/glossary#Encryption) . You can tell whether or not you are using [*SSL*](/en/glossary#SSL) by looking closely at your Web browser's **address bar**. 

All Web addresses normally begin with the letters **HTTP**, as can be seen in the example below:

![](/sites/siabnext.ttc.io/files/media/riseup-http.png)

When you are visiting a secure website, its address will begin with **HTTPS**. 

![](/sites/siabnext.ttc.io/files/media/riseup-https.png)

The extra **S** on the end signifies that your computer has opened a secure connection to the website. You may also notice a 'lock' symbol, either in the **address bar** or in the **status bar** at the bottom of your browser window. These are clues to let you know that anyone who might be monitoring your Internet connection will no longer be able to eavesdrop on your communication with that particular website.

In addition to protecting passwords and financial transactions, this type of  [*encryption*](/en/discussion#Encryption) is perfect for securing your webmail. However, many webmail providers do not offer secure access, and others require that you enable it explicitly, either by setting a preference or by typing in the **HTTPS** manually. You should always make sure that your connection is secure before logging in, reading your email, or sending a message. 

You should also pay close attention if your browser suddenly begins to complain about invalid [*security certificates*](/en/glossary#Security_certificate) when attempting to access a secure webmail account. It could mean that someone is tampering with the communication between your computer and the server in order to intercept your messages. Finally, if you rely on webmail to exchange sensitive information, it is important that your browser be as reliable as possible. Consider installing Mozilla [*Firefox*](/en/glossary#Firefox) and its security-related add-ons.


{{ tool: ../tools/windows/firefox }}



{{ snippet: ./035-snippet_03.md }}



## Switching to a more secure email account

Few webmail providers offer [*SSL*](/en/glossary#SSL) access to your email. Yahoo and Hotmail, for instance, provide a secure connection *only* while you log in, to protect your password, but your messages themselves are sent and received insecurely. In addition, Yahoo, Hotmail and some other free webmail providers insert the [*IP address*](/en/glossary#IP_address) of the computer you are using into all of the messages you send.

Gmail accounts, on the other hand, use a secure connection during log-in and all the way until you log out. You can confirm this along the way by looking at the address bar and observing the URL starting with 'https', where the 's' denotes a secure connection.  And, unlike Yahoo or Hotmail, Gmail avoids revealing your [*IP address*](/en/glossary#IP_address) to email recipients. However, it is not recommend that you rely entirely on Google for the confidentiality of your sensitive email communication. Google scans and records the content of its users' messages for a wide variety of purposes and has, in the past, conceded to the demands of governments that restrict digital freedom. See the ***Further reading*** section for more information about Google's privacy policy.

If possible, you should create a new [*RiseUp*](/en/glossary#RiseUp) email account by visiting [*https://mail.riseup.net*](https://mail.riseup.net).[*RiseUp*](/en/glossary#RiseUp) offers free email to activists around the world and takes great care to protect the information stored on their servers. They have long been a trusted resource for those in need of secure email solutions. And, unlike Google, they have very strict policies regarding their users' privacy and no commercial interests that might some day conflict with those policies. In order to create a new [*RiseUp*](/en/glossary#RiseUp) account, however, you will need two 'invite codes.' These codes can be given out by anyone who already has a  [*RiseUp*](/en/glossary#RiseUp) account. If you have a bound copy of this booklet, you should have received your 'invite codes' along with it. Otherwise, you will need to find two  [*RiseUp*](/en/glossary#RiseUp) users and ask them each to send you a code.


{{ tool: ../tools/internet/riseup }}

Both Gmail and [*RiseUp*](/en/glossary#RiseUp) are more than just webmail providers. They can also be used with an email client, such as Mozilla [*Thunderbird*](/en/glossary#Thunderbird) , that supports the techniques described under [***Advanced email security***](secure-communication#505) . Ensuring that your email client makes an [*encrypted*](/en/glossary#Encryption)  connection to your provider is just as important as accessing your webmail through **HTTPS**. If you use an email client, see the [***Thunderbird Guide***](thunderbird/windows) for additional details. A the very least, however, you should be sure to enable [*SSL*](/en/glossary#SSL)  or [*encryption*](/en/glossary#Encryption) for both your incoming and outgoing mail servers.

Regardless of what secure email tools you decide to use, keep in mind that every message has a sender and one or more recipients. You yourself are only part of the picture. Even if you access your email account securely, consider what precautions your contacts may or may not take when sending, reading and replying to messages. Try to learn where your contacts' email providers are located, as well. Naturally, some countries are more aggressive than others when it comes to email surveillance. **To ensure private communication, you and your contacts should all use secure email services hosted in relatively safe countries.** And, if you want to be certain that messsages are not intercepted between your email server and a contact's email server, you might all choose to use accounts from the same provider.  [*RiseUp*](/en/glossary#RiseUp) is one good choice.

{{ snippet: ./035-snippet_04.md }}



## Additional tips on improving your email security

- Always use caution when opening email attachments that you are not expecting, that come from someone you do not know or that contain suspicious subject lines. When opening emails like this, you should ensure that your anti-virus software is up-to-date and pay close attention to any warnings displayed by your browser or email program.
- Using anonymity software like [*Tor*](/en/glossary#Tor), which is described in our guide [**How to remain anonymous and bypass censorship on the Internet**](anonymity-and-circumvention), can help you hide your chosen email service from anyone who might be monitoring your Internet connection. And, depending on the extent of Internet filtering in your country, you may need to use [*Tor*](/en/glossary#Tor), or one of the other [*circumvention*](/en/glossary#Circumvention)  tools described in our guide on [**anonymity and bypassing censorship**](anonymity-and-circumvention), just to access a secure email provider such as [*RiseUp*](/en/glossary#RiseUp) or Gmail.
- When creating an account that you intend to use while remaining anonymous from your own email recipients, or from public forums to which you might post messages by email, you must be careful not to register a username or 'Full Name' that is related to your personal or professional life. In such cases, it is also important that you avoid using Hotmail, Yahoo, or any other webmail provider that includes your[*IP address*](/en/glossary#IP_address) in the messages you send.
- Depending on who might have physical access to your computer, clearing email-related traces from your temporary files might be just as important as protecting your messages as they travel across the Internet. See our guide [**How to destroy sensitive information**](destroy-sensitive-information) and the [***CCleaner Guide***](ccleaner/windows) for details.
- You may consider using several different, anonymous email accounts for communicating with different groups of people to protect of your contact network. You may also use different email accounts for signing up to Internet services which require email accounts.
- After all above precautions it is still very important to beware of what you write in the messages and what impact would it have if it fell into the wrong hands. One way of increasing the security of information exchange is to develop a code system for sensitive information exchange, so you would not use real names of the people, real addresses of places, etc. 



# Tips on responding to suspected email hacking and surveillance

**If you suspect your email account has been hacked or compromised**, you can take steps to reduce the damage done. While it is difficult to be certain, there may be clues such as:

- you notice any changes to your email account content or settings that you didn't make;
- your email contacts notify you that they have received an email that you didn't send;
- you cannot login to your email account, though you are sure your password and other settings are correct; 
- you are regularly not receiving some email messages from your colleagues that they insist that they sent to you; 
- some private information that was sent or received exclusively by email was made known to a third party, though neither you nor your correspondent shared it with anyone else;
- if on your account activity log (if your email provider offers one) you see that your account was accessed at time that you do not remember or from a place (or IP address) that you did not go to.

In such situations you may want to take some cautionary action:

- **Stop using this email account for sensitive information exchange**, at least until you understand the situation better.

- **Change your password as soon as possible**. See our guide [**Know how to create and maintain secure passwords**](passwords). In order to be able to change the password for your account (or for other accounts) you need to become familiar with how you do this on your email system, so that when you need to, you can do so quickly. **Change password for all other accounts with the same or similar passwords** as they may also be compromised. Use different and strong passwords for each account. You may also want to change passwords for all other accounts that you have. Consider using [**KeePass**](keepass/windows) to store and manage all your passwords. **Change your security question answers** (if you use them) for all accounts, so they are impossible to guess, or find the answer through researching information about you. This is a precaution in the case your computer was infected with spyware which would then put your other accounts at risk.

- **Enable two-factor authentication**, if your email provider supports it, as a way to prevent anyone who may have obtained your password from accessing your account. Have a look at the [Two Factor Auth](https://twofactorauth.org/#email) website to see if your provider offers this feature. When signing in with two-factor authentication, you will be asked to present a single use code in addition to your username and password. Typically, this code will be sent to you (by SMS text message, for example) or generated using a separate application on a mobile device or computer. It will be different each time you attempt to sign in. You will not be able to access your account without it, but neither will anyone else. [Google](https://www.google.com/landing/2step/), [Facebook](https://www.facebook.com/help/148233965247823) and [Twitter](https://blog.twitter.com/2013/getting-started-with-login-verification) all provide helpful guides on how to enable two-factor authentication for their respective services.

- **If you are not able to log in** to your account to change the passwords, consider getting in contact with your email provider to try to reclaim your account. Some email providers have special procedures in place to help users in such situation. It is helpful to know these procedures ahead of time.

- **Mitigate information loss and impact** to your community. It is important to make a response plan. Knowing what sensitive kinds of information you had in your account and determining the persons with whom you exchange information via that account, decide whom you should alert and what other accounts you will have to revisit or close. Determine what services (web, financial, etc.) you need to revisit or cancel. It is important that you **check the folders of your account** (if you can) to research on what could have been sent from your account and to act accordingly. To **inform your contacts** you will need to keep a separate backup of your address book. Also **review your account settings** to see possible changes that has been made. Check accounts signature option for links and malware, forwarding options that would allow to copy emails that you receive to third account, away message, display name, etc.

- **Research how your account was compromised.** Was it because of having a weak password, or due to malware infection, etc. The more you will establish about this, the better you will be able to respond to the situation and better you will be able to protect your contacts.

- **Review security of all of your devices** that access emails from this account, and devices on which you stored the password to this email account. See our guides on [**How to protect your computer from malware and hackers**](malware), [**How to protect your information from physical threats**](physical) and [**How to use smartphones as securely as possible**](smartphones). Review your anti-virus software (see the [**Avast! - Anti-Virus**](avast/windows) and [**Spybot - Anti-Spyware**](spybot/windows) tools guides). Scan your computer but get familiar with Avast! by reading [**Things you should know before you start**](avast/wíndows#412). If you are not certain that you are able to clean your device, consider reinstalling all software including the operating system from a clean source. Consider switching to more secure programs like [**Firefox**](firefox/windows), [**Thunderbird**](thunderbird/windows), [**LibreOffice**](http://www.libreoffice.org/) and other [**Free and Open Source Programs**](/en/glossary#FOSS). After making the above improvements to the security of your devices, change your account passwords again to new, stronger ones.

- Consider **reporting hacking of your account** to your email provider.

- **Consider using another, more secure account**, e.g. one that notifies you of and prevent access from unusual places or devices. Consider using account that is hosted outside of your country. Consider using email encryption - read [**gpg4usb - email text and files encryption**](gpg4usb/windows) or [**Thunderbird with Enigmail and GPG - Secure Email Client**](thunderbird/windows). 

- Consider avoiding storing read emails on the email server in your email account. Instead download them to your secured computer. Analyse security of the way you access your account and devices that you use for this.

It is important that you act quickly and precisely in the situation like this. Having prepared and rehearsed plan may help you.


**If you suspect that someone is already monitoring your email**, you may want to create a new account and keep the old one as a decoy. Remember, though, that any account with which you have exchanged email in the past may now be under surveillance as well. As a result, you should observe some additional precautions:

- Both you and your recent email contacts should create new accounts and connect to them only from locations, such as Internet cafes, that you have never used before. We recommend this strategy in order to prevent connections from your usual computer, which may be monitored, from giving away the location of your new account. As an alternative, if you must login to your new account from your normal location, you can use one of the tools described in our guide  [**How to remain anonymous and bypass censorship on the Internet**](anonymity-and-circumvention), to hide these connections.
- Exchange information about these new email addresses only through secure channels, such as a face-to-face meetings, secure instant messages or encrypted [*VoIP*](/en/glossary#VoIP) conversations. 
- Keep the traffic on your old account mostly unchanged, at least for a while. It should appear to the eavesdropper as if you are still using that account for sensitive communication. Presumably, you will want to avoid revealing critical information, but you should try not to make it obvious that you are doing so. As you can imagine, this may be somewhat challenging. 
- Make it difficult to link your actual identity to your new account. Do not send email between the new account and your old accounts (or the accounts of any contacts whom you think may also be monitored). 
- Be aware of what you write when using your new account. It is best to avoid using real names and addresses or phrases like 'human rights' or 'torture.' Develop an informal code system with your email contacts and change it periodically. 
- Remember, email security is not just about having strong technical defences. It is about paying attention to how you and your email contacts communicate with each other, and about remaining disciplined in your non-technical security habits. 



# Securing other Internet communication tools

Much like email, instant messaging and [*VoIP*](/en/glossary#VoIP) software can be secure or insecure, depending on the tools you choose and how you use them.




## Securing your instant messaging software

Instant messaging, also called 'chat,' is not normally secure, and can be just as vulnerable to surveillance as email. Luckily, there are programs that can help secure the privacy of your chat sessions. Just like with email, though, a secure communications channel requires that both you and your instant messaging contacts use the same software and take the same security precautions.

There is a chat program called [*Pidgin*](/en/glossary#Pidgin) that supports many existing instant messaging protocols, which means that you can easily begin using it without having to change your account name or recreate your list of contacts. In order to have private, [*encrypted*](/en/glossary#Encryption) conversations through [*Pidgin*](/en/glossary#Pidgin) , you will need to install and activate the *Off-the-Record [*OTR*](/en/glossary#OTR)* plug-in. Fortunately, this is a fairly simple process. 


{{ tool: ../tools/windows/pidgin }}



{{ snippet: ./035-snippet_05.md }}



## Securing your VoIP software

[*VoIP*](/en/glossary#VoIP) calls to other [*VoIP*](/en/glossary#VoIP) users are generally free of charge. Some programs allow you to make inexpensive calls to phones as well, including international numbers. Needless to say, these features can be extremely useful. Some of today's more popular [*VoIP*](/en/glossary#VoIP) programs include [Skype](http://www.skype.com) (see below), [Jitsi](http://jitsi.org/), [Google Hangouts](http://www.google.com/hangouts), and [Yahoo! Voice](http://voice.yahoo.com/).

Normally, voice communication over the Internet is no more secure than unprotected email and instant messaging. When using voice communication to exchange sensitive information it is important to choose a tool that encrypts the call all the way from your computer to the recipient's computer. It also best to use Free and Open-Source Software, preferably those reviewed, tested, and recommended by a trusted community. Taking above criteria we would recommend that you try [*Jitsi*](http://jitsi.org/) as your choice for VoIP.


{{ tool: ../tools/windows/jitsi }}




## Notice about Skype's security

[*Skype*](/en/glossary#Skype) is a very common instant messaging and VoIP tool that also supports calls to landlines and mobile phones. Despite its popularity, several issues make this software not a secure choice. Some of these issues are described below.

While according to Skype, it [*encrypts*](/en/glossary#Encryption) both messages and voice calls, this would only happen when both communicating sides are using Skype programs. Skype does not encrypt calls to phone or text sent as SMS messages.

If both communicating sides are using (a genuine) Skype program, its encryption may make the call nominally more secure than an ordinary call over phone. But because Skype is a closed-source program, making an independent audit and evaluation of its proclamations about encryption impossible, it is thus impossible to verify how well Skype is protecting the users and their information and communication. Our guide [**How to protect your computer from malware and hackers**](malware) addresses the virtues of *Free and Open-Source Software* [*FOSS*](/en/glossary#FOSS) in the [**Keeping your software up-to-date**](malware#392) section.

As mentioned, while we can't recommend Skype as a secure communication tool, it is very important to take some precautions if one still decides to use Skype as a tool for their sensitive communication:

- Download and install Skype only from its official website [www.skype.com](http://www.skype.com) to avoid a Skype program infected with spyware. It is important to always double-check the URL to make sure you are connecting to the official site. In some countries the Skype website is blocked, and/or several fake sites claiming to be Skype's official site are in operation. In many such cases, the version of Skype available is likely infected with malware designed to spy on any communication. Use circumvention tools described in our guide on [**Anonymity and bypassing censorship**](anonymity-and-circumvention) to connect to the Skype website and download a genuine version of Skype program whenever you want to install or upgrade to newest version of the software.
- It is very important to change your Skype password regularly. Skype allows for multiple logins from different locations and does not inform you about the number of simultaneous sessions. This poses a big risk that if your password is compromised, anyone with that password can also be logged in. All logged sessions receive all the text communication and have access to calls history. Changing the password is the only way to disable such rogue sessions (by forcing a re-login).
- It is also advisable to set the privacy settings on Skype so that it does not keep a history of chats.
- It is recommended to disable the Skype setting which automatically accepts incoming files, as this has occasionally been used to introduce malware/spyware onto computers.
- Always independently verify the identity of the person with whom you are communicating. It is easier to do this when voice chatting, especially if you know the person you want to talk to.
- Decide if your Skype username should identify your or have any relationship to your real name, or the name of you organisation.
- Always have alternative ways for communicating - Skype can become unavailable at any moment.
- Be careful of what you say - develop a code system to discuss sensitive topics without using specific terminology.

Despite Skype's popularity, the above concerns make it questionable for a secure experience, and we recommend you start using tools like Jitsi for VoIP and [*Pidgin*](/en/glossary#Pidgin) with the [*OTR*](/en/glossary#OTR) plugin for secure instant messaging.



# Advanced Email Security

The tools and concepts discussed below are recommended for experienced computer users.




## Using Public Key Encryption in Email

It is possible to achieve a greater level of email privacy, even with an unsecured email account. In order to do this, you will need to learn about public key  [**encryption**](/en/glossary#Encryption). This technique allows you to encode individual messages, making them unreadable to anyone but the intended recipients. The ingenious aspect of public key [**encryption**](/en/glossary#Encryption) is that you do not have to exchange any secret information with your contacts about how you are going to encode messages in the future.

{{ snippet: ./035-snippet_06.md }}

This technique can be used with any email service, even one that lacks a secure communication channel, because individual messages are [**encrypted**](/en/glossary#Encryption) before they leave your computer. 

Remember that by using [**encryption**](/en/glossary#Encryption), you could attract attention to yourself. The type of [**encryption**](/en/glossary#Encryption) used when you access a secure website, including a webmail account, is often viewed with less suspicion than the type of public key [**encryption**](/en/glossary#Encryption) being discussed here. In some circumstances, if an email containing this sort of [**encrypted**](/en/glossary#Encryption)  data is intercepted or posted on a public forum, it could incriminate the person who sent it, regardless of the content of the message. You might sometimes have to choose between the privacy of your message and the need to remain inconspicuous.


## Encrypting and authenticating individual messages
Public key [**encryption**](/en/glossary#Encryption) may seem complicated at first, but it is quite straightforward once you understand the basics, and the tools are not difficult to use. Simple, user-friendly and portable, the **gpg4usb** program can encrypt email messages and files even when you are not connected to the Internet.


{{ tool: ../tools/windows/gpg4usb }}

The **Mozilla** [**Thunderbird**](/en/glossary#Thunderbird) email program can be used with an extension called [**Enigmail**](/en/glossary#Enigmail) to encrypt and decrypt email messages quite easily.


{{ tool: ../tools/windows/thunderbird }}

The authenticity of your email is another important aspect of communication security. Anyone with Internet access and the right tools can impersonate you by sending messages from a fake email address that is identical to your own. The danger here is more apparent when considered from the perspective of the recipient. Imagine, for example, the threat posed by an email that appears to be from a trusted contact but is actually from someone whose goal is to disrupt your activities or learn sensitive information about your organisation.

Given that we cannot see or hear our correspondents through email, we typically rely on a sender's address to verify her identity, which is why we are so easily fooled by fake emails. [**Digital signatures**](/en/glossary#Digital_signature), which also rely on public key [**encryption**](/en/glossary#Encryption), provide a more secure means of proving one's identity when sending a message. The [***portable gpg4usb***](gpg4usb/windows) guide or [***How to use Enigmail with Thunderbird***](thunderbird/windows#746) section of the [***Thunderbird Guide***](thunderbird/windows) explains in detail how this is done.


{{ snippet: ./035-snippet_07.md }}


# Further reading

- To learn more about faking an email identity, refer to the *2.5 Spoofing* section of the [Digital Security and Privacy for Human Rights Defenders](http://www.frontlinedefenders.org/esecman) book. 
- In addition to the *Riseup* and *Thunderbird* Hands-on Guides, there are a number of websites that explain how to use your email program with various popular email providers while leaving a copy of your messages on the mail server:
- The [Riseup website](https://help.riseup.net/en/email-clients)
- Instructions on [using Gmail](https://mail.google.com/support/bin/topic.py?topic=12769)
- Instructions on  [how to import your gmail contacts into Thunderbird](http://email.about.com/od/mozillathunderbirdtips/qt/et_gmail_addr.htm) 
- For details on how to use other email services in this way, search the help section of the provider's website for keywords like 'POP', 'IMAP' and 'SMTP'.
- There is a well-known attack on the security of SSL encryption known as the  [Man in the Middle attack](https://secure.wikimedia.org/wikipedia/en/wiki/Man-in-the-middle_attack)
- The [Gmail Privacy Policy](https://www.google.com/intl/en/privacy/privacy-policy.html), which you must accept when creating a Gmail account, explains that, &quot;Google maintains and processes your Gmail account and its contents to provide the Gmail service to you and to improve our services.&quot; In fact, all email providers scan your messages, to some extent, so that they can offer anti-spam services and other such features. Gmail goes a bit futher, however, in order to provide 'targeted advertising' based on the actual content of your email. This could be dangerous if information stored by Google were to be intentionally or accidentally exposed.
- A series of interviews in 2008 addressed the  [privacy and encryption policies](http://news.cnet.com/8301-13578_3-9962106-38.html) of several major instant messaging services. 
