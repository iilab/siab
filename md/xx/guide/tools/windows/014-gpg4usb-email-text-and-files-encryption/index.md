

---

lang: xx
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 014
title: gpg4usb - email text and files encryption

---

**Homepage**

- [**http://www.gpg4usb.org/**](http://www.gpg4usb.org/)

**Computer Requirements**

- All Windows Versions

**Versions used in this guide**

- 0.3.3

**Last revision of this chapter**

- July 2014

**License**

- Free and Open-Source Software

**Required Reading**

- How-to Booklet chapter [**7. Keeping your Internet Communication Private**](/chapter-7)

- [**Digital Security and Privacy for Human Rights Defenders**](https://www.frontlinedefenders.org/esecman), chapter **2.4 Cryptology - Public Key Encryption (page 38)**

**What you will get in return**:

- The ability to encrypt files and text messages from wherever you are (for instance, an Internet café or at work) 
- The ability to encrypt the messages *off-line* or when Internet access is unavailable, and then send them from a computer connected to the Internet later.

## 1.1 Things You Should Know about this Tool Before You Start ##

**gpg4usb** is a simple, lightweight and portable program that lets you encrypt and decrypt text messages and files. **gpg4usb** is based on public-key cryptography. In this method, each individual must generate her/his own personal **key pair**. The first key is known as the **private key**. It is protected by a password or passphrase, guarded and *never* shared with anyone.

The second key is known as the **public key**. This key can be shared with any of your correspondents - and your correspondents can share theirs with you. Once you have a correspondent’s public key you can begin sending encrypted emails to this person. Only she will be able to decrypt and read your emails, because she is the only person who has access to the matching private key.

Similarly, if you send a copy of your own public key to your email contacts and keep the matching private key secret, only you will be able to read encrypted messages from those contacts.

You may also attach digital signatures to your messages. The recipient of your message who has a genuine copy of your public key will be able to verify that the email comes from you, and that its content was not tampered with on the way. Similarly, if you have a correspondent's public key, you can verify the digital signatures on her messages.

**gpg4usb** lets you generate an encryption key pair, export public keys to be shared with other people, compose a text message, and encrypt it. You can either simply copy and paste the public key and/or encrypted message from **gpg4usb** to the body of your email, or save them as a text file to be sent later. Documents and files can be encrypted too. 

**Note**: Be mindful that the original, unencrypted versions of your documents and files may still reside on your computer, so both your correspondent and yourself must remember to remove them from computers when necessary.

**gpg4usb** lets you exchange keys and encrypted messages with other similar **GPG** or **PGP** programs.

