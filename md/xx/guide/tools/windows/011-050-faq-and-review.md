

---

lang: xx
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 5
depth: 3
title: FAQ and Review

---

<a name="5.0"></a>
## 5.0 FAQ and Review ##

<div class="background" markdown="1"> 

***Q: Can I use Pidgin-OTR to chat with friends in both MSN and Yahoo***? 

***A**: Although **Pidgin-OTR** supports a number of chat and messaging services, most of the time you have to use the same provider to initiate an **IM** session with your buddy. You both need to use an **IRC** or a **ICQ** account for example. However, services that use **XMPP** protocol (like **RiseUp**, **Google Talk**, **Facebook**, or other **XMPP** servers) may allow chatting between their accounts. Therefore you can chat between account on **RiseUp** and **Google Talk**. Also note that in **Pidgin** you can register and be on-line with several **IM** accounts simultaneously. That's the beauty of using a multi-protocol **IM** client.*

***Q: How may I access my Pidgin-OTR account on another computer?***

***A**: One way is to generate a new private key to use with your **IM** account on that computer. You can start a conversation with your buddy using this new key, but you will need to authenticate your session again. Another option is to copy the encryption keys to the new computer (you can find them in %APPDATA%\\.purple on Windows and ~/.purple on Linux or Mac).*

***Q: What if I forget the login password for my IM account? Or what if someone steals it? Will they have access to my past and future conversations?***

***A**: This is very important question. First of all, if you forget your password and you will not be able to reset it using options offered by the account provider, you will have to generate a new **IM** account. After that, you must inform your buddy about your new account using secure and authenticated email or voice-chat where you can recognise each other.*

*Finally, you must authenticate each other as buddies. If someone has somehow obtained your **IM** password, that person could attempt to impersonate you when using **Pidgin**. Fortunately, he/she won't be able to authenticate the session without having your encryption keys or knowing your shared code word. As such, your buddy may become suspicious. That's why authentication is **so** important.*

*Furthermore, if you followed the instructions above and set the recommended preferences in the **OTR** 'Config' tab, then even someone who steals your password or have access to your computer won't have access to your past conversations, since you chose not to record them.*

</div>

<a name="5.1"></a>
## 5.1 Review Questions ##

- How many times do you need to 'authenticate' your chat session with a given buddy?
- Is it possible to register and simultaneously use multiple **IM** accounts in **Pidgin**? 
- What is a fingerprint in **Pidgin**? 
- What will happen to your **OTR** preferences (including the received keys' fingerprints) when you install **Pidgin- OTR** on another computer?
- What is required to initiate a private and authenticated chat session in **Pidgin**?
- What are the requirements for creating an account in **Pidgin**? 

