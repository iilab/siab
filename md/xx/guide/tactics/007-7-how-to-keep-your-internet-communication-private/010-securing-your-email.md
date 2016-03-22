

---

lang: xx
community: guide
type: tactics
legacy: True
child: True
weight: 1
depth: 3
title: Securing your email

---

There are a few important steps that you can take in order to increase the security of your email communication. The first is to make sure that only the person to whom you send a given message is able to read it. This is discussed in the  [*Keeping your webmail private*](/en/chapter_7_1#Keeping_your_webmail_private) and  [*Switching to a more secure emailaccount*](/en/chapter_7_1#Switching_to_a_more_secure_email_account) sections, below. Going beyond the basics, it is sometimes critical that your email contacts have the ability to verify that a particular message truly came from you and not from someone who might be attempting to impersonate you. One way to accomplish this is described under [*Advanced email security*](/en/chapter_7_4), in the [*Encrypting and authenticating individual email messages*](/en/chapter_7_4#Encrypting_and_authenticating_individual_email_messages) section.

You should also know what to do if you think the privacy of your
email account may have been violated. The [*Tips on responding to
suspected email surveillance*](/en/chapter_7_2) section addresses this
question. 

Remember, too, that secure email will not do you any good if
everything you type is recorded by spyware and periodically sent over the Internet to a third party.[*Chapter 1: How to protect your computer from malware and hackers*](/en/chapter-1) offers some advice on how to prevent this sort of thing, and [*Chapter 3: How to create and maintain secure passwords*](/en/chapter-3) will help you protect your accounts for the email and instant messaging tools described below. 

### Keeping your webmail private ###

The Internet is an open network through which information typically travels in a readable format. If a normal email message is intercepted on the way to a recipient, its contents can be read quite easily. And, because the Internet is just one large, worldwide network that relies on intermediary computers to direct traffic, many different people may have the opportunity to intercept a message in this way. Your *Internet Service Provider [*ISP*](/en/glossary#ISP)* is the first recipient of an email message as it begins its journey to the recipient. Similarly, the recipient's [*ISP*](/en/glossary#ISP)  is the last stop for your message before it is delivered. Unless you take certain precautions, your messages can be read or tampered with at either of these points, or anywhere in between.

<div class="background" markdown="1">
Pablo: I was talking to one of our partners about all this, and she
said that she and her colleagues sometimes just save important messages
in the 'Drafts' folder of a webmail account where they all share a
password. It sounds kind of strange to me, but would it work? I mean,
wouldn't that prevent anyone from reading the messages, since they're
never actually sent?

Claudia: Any time you read an email on your computer, even if it's just a 'draft,' its contents have been sent to you over the Internet. Otherwise, it couldn't appear on your screen, right? The thing is, if someone has you under surveillance, they don't just monitor your email messages, they can scan all readable information going to and from your computer. In other words, this trick wouldn't work unless everyone connects securely to that shared webmail account. And, if they do, then it really doesn't hurt to create separate accounts or to go ahead and hit that 'send' button.
</div>

It has long been possible to secure the Internet connection between your computer and the websites that you visit. You often encounter this level of security when entering passwords or credit card information into websites. The technology that makes it possible is called Secure Sockets Layer [*SSL*](/en/glossary#SSL) [*encryption*](/en/glossary#Encryption) . You can tell whether or not you are using [*SSL*](/en/glossary#SSL) by looking closely at your Web browser's **address bar**. 

All Web addresses normally begin with the letters **HTTP**, as can be seen in the example below:

![](/sites/securitybkp.ngoinabox.org/files/u7/01.png)

When you are visiting a secure website, its address will begin with **HTTPS**. 

![](/sites/securitybkp.ngoinabox.org/files/u7/02.png)

The extra **S** on the end signifies that
your computer has opened a secure connection to the website.
You may also notice a 'lock' symbol, either in the **address bar** or in the **status bar** at the bottom of your browser window. These are clues to let you know that anyone who might be monitoring your Internet connection will no longer be able to eavesdrop on your communication with that particular website.

In addition to protecting passwords and financial transactions, this type of  [*encryption*](/en/discussion#Encryption) is perfect for securing your webmail. However, many webmail providers do not offer secure access, and others require that you enable it explicitly, either by setting a preference or by typing in the **HTTPS** manually. You should always make sure that your connection is secure before logging in, reading your email, or sending a message. 

You should also pay close attention if your browser suddenly begins to complain about invalid [*security certificates*](/en/glossary#Security_certificate) when attempting to access a secure webmail account. It could mean that someone is tampering with the communication between your computer and the server in order to
intercept your messages. Finally, if you rely on webmail to exchange sensitive information, it is important that your browser be as reliable as possible. Consider installing Mozilla [*Firefox*](/en/glossary#Firefox) and its security-related add-ons.

<div class="getstarted" markdown="1">
Hands-on: Get started with the [*Firefox with add-ons - Secure Web Browser Guide*](/en/firefox_main)
</div>			

<div class="background" markdown="1">
Pablo: One of the guys who's going to be working on this report with
us tends to use his Yahoo webmail account when he's not in the
office.And I seem to remember somebody else using Hotmail. If I send a
message to these guys, can other people read it?

Claudia: Probably. Yahoo, Hotmail and plenty of other webmail
providers have insecure websites that don't protect the privacy of
their users' messages. We're going to have to change some people's
habits if we want to be able to discuss these testimonies securely.
</div>		

### Switching to a more secure email account ###

Few webmail providers offer [*SSL*](/en/glossary#SSL) access to your email. Yahoo and Hotmail, for instance, provide a secure connection *only* while you log in, to protect your password, but your messages themselves are sent and received insecurely. In addition, Yahoo, Hotmail and some other free webmail providers insert the [*IP address*](/en/glossary#IP_address) of the computer you are using into all of the messages you send.

Gmail accounts, on the other hand, use a secure connection during log-in and all the way until you log out. You can confirm this along the way by looking at the address bar and observing the URL starting with 'https', where the 's' denotes a secure connection.  And, unlike Yahoo or Hotmail, Gmail avoids revealing your [*IP address*](/en/glossary#IP_address) to email recipients. However, it is not recommend that you rely entirely on Google for the confidentiality of your sensitive email communication. Google scans and records the content of its users' messages for a wide variety of purposes and has, in the past, conceded to the demands of governments that restrict digital freedom. See the [***Further reading***](/en/chapter_7_5) section for more information about Google's privacy policy.

If possible, you should create a new [*RiseUp*](/en/glossary#RiseUp) email account by visiting [*https://mail.riseup.net*](https://mail.riseup.net).[*RiseUp*](/en/glossary#RiseUp) offers free email to activists around the world and takes great care to protect the information stored on their servers. They have long been a trusted resource for those in need of secure email solutions. And, unlike Google, they have very strict policies regarding their users' privacy and no commercial interests that might some day conflict with those policies. In order to create a new [*RiseUp*](/en/glossary#RiseUp) account, however, you will need two 'invite codes.' These codes can be given out by anyone who already has a  [*RiseUp*](/en/glossary#RiseUp) account. If you have a bound copy of this booklet, you should have received your 'invite codes' along with it. Otherwise, you will need to find two  [*RiseUp*](/en/glossary#RiseUp) users and ask them each to send you a code.

<div class="getstarted" markdown="1">
Hands-on: Get started with the [*RiseUp  - Secure Email Service Guide*](/en/riseup_main)
</div>	

Both Gmail and [*RiseUp*](/en/glossary#RiseUp) are more than just webmail providers. They can also be used with an email client, such as Mozilla [*Thunderbird*](/en/glossary#Thunderbird) , that supports the techniques described under [***Advanced email security***](/en/chapter_7_4) . Ensuring that your email client makes an [*encrypted*](/en/glossary#Encryption)  connection to your provider is just as important as accessing your webmail through **HTTPS**. If you use an email client, see the [***Thunderbird Guide***](/en/thunderbird_main) for additional details. A the very least, however, you should be sure to enable [*SSL*](/en/glossary#SSL)  or [*encryption*](/en/glossary#Encryption) for both your incoming and outgoing mail servers.

<div class="background" markdown="1">
Pablo: So, should I switch to using RiseUp or I can keep using Gmail, and just switch to the secure 'https' address?

Claudia: It's your call, but there are a few things you should
definitely consider when choosing an email provider. First, do they
offer a secure connection to your account? Gmail does, so you're OK
there. Second, do you trust the administrators to keep your email
private and not to read through it or share it with others? That one's
up to you. And, finally, you need to think about whether or not it's
acceptable for you to be identified with that provider. In other words,
will it get you in trouble to use an email address that ends in
'riseup.net', which is known to be popular among activists, or do you
need a more typical 'gmail.com' address?
</div>

Regardless of what secure email tools you decide to use, keep in mind that every message has a sender and one or more recipients. You yourself are only part of the picture. Even if you access your email account securely, consider what precautions your contacts may or may not take when sending, reading and replying to messages. Try to learn where your contacts' email providers are located, as well. Naturally, some countries are more aggressive than others when it comes to email surveillance. **To ensure private communication, you and your contacts should all use secure email services hosted in relatively safe countries.** And, if you want to be certain that messsages are not intercepted between your email server and a contact's email server, you might all choose to use accounts from the same provider.  [*RiseUp*](/en/glossary#RiseUp) is one good choice.
 
### Additional tips on improving your email security ### 

- Always use caution when opening email attachments that you are not expecting, that come from someone you do not know or that contain suspicious subject lines. When opening emails like this, you should ensure that your anti-virus software is up-to-date and pay close attention to any warnings displayed by your browser or email program.
- Using anonymity software like [*Tor*](/en/glossary#Tor), which is described in [***Chapter 8: How to remain anonymous and bypass censorship on the Internet***](/en/chapter-8), can help you hide your chosen email service from anyone who might be monitoring your Internet connection. And, depending on the extent of Internet filtering in your country, you may need to use [*Tor*](/en/glossary#Tor), or one of the other [*circumvention*](/en/glossary#Circumvention)  tools described in [***chapter 8***](/en/chapter-8), just to access a secure email provider such as [*RiseUp*](/en/glossary#RiseUp) or Gmail.
- When creating an account that you intend to use while remaining anonymous from your own email recipients, or from public forums to which you might post messages by email, you must be careful not to register a username or 'Full Name' that is related to your personal or professional life. In such cases, it is also important that you avoid using Hotmail, Yahoo, or any other webmail provider that includes your[*IP address*](/en/glossary#IP_address) in the messages you send.
- Depending on who might have physical access to your computer, clearing email-related traces from your temporary files might be just as important as protecting your messages as they travel across the Internet. See [***Chapter 6: How to destroy sensitive information***](/en/chapter-6) and the [***CCleaner Guide***](/en/ccleaner_main) for details.
- You may consider using several different, anonymous email accounts for communicating with different groups of people to protect of your contact network. You may also use different email accounts for signing up to Internet services which require email accounts.
- After all above precautions it is still very important to beware of what you write in the messages and what impact would it have if it fell into the wrong hands. One way of increasing the security of information exchange is to develope a code system for sensitive information exchange, so you would not use real names of the people, real addresses of places, etc. 

