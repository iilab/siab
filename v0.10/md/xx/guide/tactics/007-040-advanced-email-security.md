

---

lang: xx
community: guide
type: tactics
legacy: True
child: True
weight: 4
depth: 3
title: Advanced Email Security

---

The tools and concepts discussed below are recommended for experienced computer users.

### Using Public Key Encryption in Email ###

It is possible to achieve a greater level of email privacy, even with an unsecured email account. In order to do this, you will need to learn about public key  [**encryption**](/en/glossary#Encryption). This technique allows you to encode individual messages, making them unreadable to anyone but the intended recipients. The ingenious aspect of public key [**encryption**](/en/glossary#Encryption) is that you do not have to exchange any secret information with your contacts about how you are going to encode messages in the future.

<div class="background" markdown="1">
**Pablo**: But how does all this work?
			
**Claudia**: Clever mathematics! You encode messages to a given email contact using her special 'public key', which she can distribute freely. Then, she uses her secret 'private key', which she has to guard carefully, in order to read those messages. In turn, your contact uses your public key to encrypt messages that she writes to you. So, in the end, you do have to exchange public keys, but you can share them openly, without having to worry about the fact that anybody who wants your public key can get it.

</div>

This technique can be used with any email service, even one that lacks a secure communication channel, because individual messages are [**encrypted**](/en/glossary#Encryption) before they leave your computer. 

Remember that by using [**encryption**](/en/glossary#Encryption), you could attract attention to yourself. The type of [**encryption**](/en/glossary#Encryption) used when you access a secure website, including a webmail account, is often viewed with less suspicion than the type of public key [**encryption**](/en/glossary#Encryption) being discussed here. In some circumstances, if an email containing this sort of [**encrypted**](/en/glossary#Encryption)  data is intercepted or posted on a public forum, it could incriminate the person who sent it, regardless of the content of the message. You might sometimes have to choose between the privacy of your message and the need to remain inconspicuous.

### Encrypting and Authenticating Individual Messages ###

Public key [**encryption**](/en/glossary#Encryption) may seem complicated at first, but it is quite straightforward once you understand the basics, and the tools are not difficult to use. Simple, user-friendly and portable, the **gpg4usb** program can encrypt email messages and files even when you are not connected to the Internet.

<div class="getstarted" markdown="1">
**Hands-on: Get started with the** [***Portable gpg4usb - email text and files encryption program guide***](/en/gpg4usb_portable)
</div>

The **Mozilla** [**Thunderbird**](/en/glossary#Thunderbird) email program can be used with an extension called [**Enigmail**](/en/glossary#Enigmail) to encrypt and decrypt email messages quite easily.

<div class="getstarted" markdown="1">
**Hands-on: Get started with the** [***Thunderbird with Enigmail and GPG - Secure Email Client Guide***](/en/thunderbird_main)
</div>

The authenticity of your email is another important aspect of communication security. Anyone with Internet access and the right tools can impersonate you by sending messages from a fake email address that is identical to your own. The danger here is more apparent when considered from the perspective of the recipient. Imagine, for example, the threat posed by an email that appears to be from a trusted contact but is actually from someone whose goal is to disrupt your activities or learn sensitive information about your organisation.

Given that we cannot see or hear our correspondents through email, we typically rely on a sender's address to verify her identity, which is why we are so easily fooled by fake emails. [**Digital signatures**](/en/glossary#Digital_signature), which also rely on public key [**encryption**](/en/glossary#Encryption), provide a more secure means of proving one's identity when sending a message. The [***portable gpg4usb***](/en/gpg4usb_portable) guide or [***How to use Enigmail with Thunderbird***](/en/thuderbird_encryption) section of the [***Thunderbird Guide***](/en/thunderbird_main) explains in detail how this is done.

<div class="background" markdown="1">
**Pablo**: I had a colleague once who received an email from me that I didn't send. We decided, in the end, that it was just spam, but now I'm imagining how much damage could be done if a fake email appeared in the wrong person's inbox at the wrong time. I've heard you can prevent this kind of thing with digital signatures, but what are they?
			
**Claudia**: A digital signature is like a wax seal over the flap of an envelope with your letter inside, except that it can't be forged. It proves that you are the real sender of the message and that it hasn't been tampered with along the way.
</div>


