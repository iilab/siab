

---

lang: xx
community: guide
type: tactics
legacy: True
child: True
weight: 3
depth: 3
title: Anonymity networks and basic proxy servers

---

### Anonymity networks ###

Anonymity networks typically 'bounce' your Internet traffic around between various secure [*proxies*](/en/glossary#Proxy) in order to disguise where you are coming from and what you are trying to access. This can significantly reduce the speed at which you are able to load websites and other Internet services. In the case of [*Tor*](/en/glossary#Tor) , however, it also provides a reliable, secure and public means of circumvention that saves you from having to worry about whether or not you trust the individuals who operate your [proxies](/en/glossary#Proxy) and the websites you visit. As always, you must ensure that you have an encrypted connection, [HTTPS](/en/glossary#SSL), to a secure website before exchanging sensitive information, such as passwords and emails, through a browser.

You will have to install software to use [*Tor*](/en/glossary#Tor), but the result is a tool that provides anonymity as well as circumvention. Each time you connect to the [*Tor*](/en/glossary#Tor) network, you select a random path through three secure [*Tor*](/en/glossary#Tor) [*proxies*](/en/glossary#Proxy). This ensures that neither your [*ISP*](/en/glossary#ISP) nor the [*proxies*](/en/glossary#Proxy) themselves know both your  computer's [*IPaddress*](/en/glossary#IP_address) and the location of the Internet services you request. You can learn much more about this tool from the Tor Guide.

<div class="getstarted" markdown="1">
Hands-on: Get started with the [*Tor - Digital Anonymity and Circumvention Guide*](/en/tor_main)
</div>

One of Tor's strengths is that it does not just work with a browser but can be used with various types of Internet software. Email programs, including Mozilla  [*Thunderbird*](/en/glossary#Thunderbird),and instant messaging programs,including [*Pidgin*](/en/glossary#Pidgin), can operate through Tor, either to access filtered services or to hide your use of those services.

### Basic circumvention proxies ###

There are three important questions that you should consider when selecting a basic circumvention [*proxy*](/en/glossary#Proxy) . First, is it a web-based tool or does it require you to change settings or install software on your computer? Second, is it secure? Third, is it private or public?

#### Web-based and other proxies:####

Web-based [*proxies*](/en/glossary#Proxy) are probably the easiest to use. They require only that you point your browser at a [*proxy*](/en/glossary#Proxy) webpage, enter the filtered address you wish to view and click one button. The [*proxy*](/en/glossary#Proxy) will then display the requested content inside its own webpage. You can follow links normally or enter a new address into the [*proxy*](glossary#Proxy) if you want to view a different page. You do not need to install any software or change any browser settings, which means that web-based [*proxies*](/en/glossary#Proxy) are:

- Easy to use
- Reachable from public computers, such as those at Internet cafes, that may not allow you to install programs or change settings
- Potentially safer if you are concerned about being 'caught' with circumvention software on your computer
	
Web-based [*proxies*](glossary#Proxy)  tend to have certain disadvantages, as well. They do not always display pages correctly, and many web-based [*proxies*](/en/glossary#Proxy) will fail to load complex websites, including those that feature streaming audio and video content. Also, while any [*proxy*](/en/glossary#Proxy) will slow down as it gains more users, this tends to be more of an issue with public web-based [*proxies*](/en/glossary#Proxy). And, of course, web-based [*proxies*](/en/glossary#Proxy) only work for webpages. You can not, for example, use an instant messaging program or an email client to access blocked services through a web-based [*proxy*](/en/glossary#Proxy). Finally, secure web-based [*proxies*](/en/glossary#Proxy)  offer limited confidentiality because they must themselves access and modify the information returned to you by the websites you visit. If they did not, you would be unable to click on a link without leaving the [*proxy*](/en/glossary#Proxy) behind and attempting to make a direct connection to the target webpage. This is discussed further in the following section.

Other types of [*proxies*](/en/glossary#Proxy) generally require you to install a program or configure an external [*proxy*](/en/glossary#Proxy) address in your browser or operating system. In the first case, your circumvention program will typically provide some way of turning the tool on and off, which will tell your browser whether or not to use the [*proxy*](/en/glossary#Proxy). Software like this often allows you to change  [*proxies*](/en/glossary#Proxy) automatically if one is blocked, as discussed above. If you have to configure an external [*proxy*](/en/glossary#Proxy) address in your browser or operating system, you will need to learn the correct [*proxy*](/en/glossary#Proxy) address, which may change if that [*proxy*](/en/glossary#Proxy) is blocked or slows down so much that it becomes unusable.

Although it may be slightly more difficult to use than a web-based [*proxy*](/en/glossary#Proxy),this method of circumvention is more likely to display complex pages correctly and may take longer to slow down as more people begin to use a given [*proxy*](/en/glossary#Proxy) server. Furthermore, [*proxies*](/en/glossary#Proxy) can be found for a number of different Internet applications. Examples include HTTP [*proxies*](/en/glossary#Proxy) for browsers, SOCKS [*proxies*](/en/glossary#Proxy)  for email and chat programs and VPN [*proxies*](/en/glossary#Proxy), which can redirect all of your Internet traffic to avoid filtering.

#### Secure and insecure proxies: ####

A secure [*proxy*](/en/glossary#Proxy), in this chapter, refers to any [*proxy*](/en/glossary#Proxy)  that supports [*encrypted*](/en/glossary#Encryption) connections from its users. An insecure [*proxy*](/en/glossary#Proxy) will still allow you to bypass many types of filtering, but will fail if your Internet connection is being scanned for key words or particular website addresses.It is a particularly bad idea to use an insecure [*proxy*](/en/glossary#Proxy) when accessing websites that are normally  [*encrypted*](/en/glossary#Encryption), such as webmail accounts and banking websites. By doing so, you may expose sensitive information that would normally be hidden. And, as mentioned previously, insecure [*proxies*](/en/glossary#Proxy) are often easier for those who update Internet filtering software and policies to discover and block. In the end, the fact that free, fast, secure [*proxies*](/en/glossary#Proxy) exist means that there are very few good reasons to settle for an insecure one.

You will know that a web-based [*proxy*](/en/glossary#Proxy) is secure if you can access the [*proxy*](glossary#Proxy) webpage itself using an [*HTTPS*](/en/glossary#HTTPS) address. As with webmail services, secure and insecure connections may be supported, so you should be certain to use the secure address. It may happen that, in such cases, you will be asked to accept a 'security certificate warning' from your browser in order to continue. This is the case for the [*Peacefire*](/en/glossary#Peacefire) [*proxy*](/en/glossary#Proxy), discussed below. Warnings like this tell you that someone, such as your ISP or a hacker, could be monitoring your connection to the [*proxy*](/en/glossary#Proxy). Despite these warnings, it may be still a good idea to use secure [*proxies*](/en/glossary#Proxy) whenever possible. However, when relying on such  [*proxies*](/en/glossary#Proxy) for circumvention, you should avoid visiting secure websites unless you verify the [*proxy's*](glossary#Proxy) [*SSL*](/en/glossary#SSL)
fingerprint. In order to do this, you will need a way of securely communicating with the [*proxy's*](/en/glossary#Proxy) administrator. **It is best not to enter passwords or exchange sensitive information when using web proxies in general.**

You should also avoid accessing sensitive information through a web-based [*proxy*](/en/glossary#Proxy) unless you trust the person who runs it. This applies regardless of whether or not you see a security certificate warning when you visit the  [*proxy*](/en/glossary#Proxy). It even applies if you know the [*proxy*](/en/glossary#Proxy)  operator well enough to verify the server's *fingerprint* before directing your browser to accept the warning. When you rely on a single [*proxy*](/en/glossary#Proxy) server for circumvention, its administrator will always know your [*IP address*](/en/glossary#IP_address) and which website/s you are accessing. More importantly, however, if that [*proxy*](/en/glossary#Proxy) is web-based, a malicious operator could gain access to all of the information that passes between your browser and the websites you visit, including the content of your webmail and your passwords.

For [*proxies*](/en/glossary#Proxy) that are not web-based, you may have to do a little research to determine whether or not secure connections are supported. All of the  [*proxies*](/en/glossary#Proxy) and anonymity networks recommended in this chapter are secure. 

#### Private and public proxies: ####

Public [*proxies*](/en/glossary#Proxy) accept connections from anyone, whereas private [*proxies*](/en/glossary#Proxy) typically require a username and password. While public [*proxies*](/en/glossary#Proxy) have the obvious advantage of being freely available, assuming they can be found, they tend to become overcrowded very quickly. As a result, even though public [*proxies*](/en/glossary#Proxy) may be as technically sophisticated and well-maintained as private ones, they are often relatively slow. Finally, private [*proxies*](/en/glossary#Proxy) tend to be run either as for-profit businesses or by administrators who create accounts for users that they know personally or socially. Because of this, it is generally easier to determine what motivates the operators of a private  [*proxy*](/en/glossary#Proxy). You should not assume, however, that private  [*proxies*](/en/glossary#Proxy) are therefore fundamentally more trustworthy. After all, the profit motive has led online services to expose their users in the past.

Simple, insecure, public [*proxies*](/en/glossary#Proxy) can often be found by searching for terms like 'public proxy' in a search engine, but you should not rely on  [*proxies*](/en/glossary#Proxy) discovered this way. Given the choice, it is better to use a private, secure [*proxy*](/en/glossary#Proxy) run by people that you know and trust, either personally or by reputation, and who have the technical skill to keep their server secure. Whether or not you use a web-based [*proxy*](/en/glossary#Proxy) will depend on your own particular needs and preferences. Any time you are using a [*proxy*](/en/glossary#Proxy) for circumvention, it is also a good idea to use the [*Firefox*](/en/glossary#Firefox)  browser and to install the [*NoScript*](/en/glossary#NoScript) browser extension, as discussed in the [*Firefox Guide*](/en/firefox_main). Doing so can help protect you both from malicious  [*proxies*](/en/glossary#Proxy) and from websites that might try to discover your real  
[*IP address*](/en/glossary#IP_address). Finally, keep in mind that even an [*encrypted*](/en/glossary#Encrypted) [*proxy*](/en/glossary#Proxy) will not make an insecure website secure. You must still ensure that you have an [*HTTPS*](/en/glossary#SSL) connection before sending or receiving sensitive information.

If you are unable to find an individual, organisation or company whose  [*proxy*](/en/glossary#Proxy) service you consider trustworthy, affordable and accessible from your country, you should consider using the Tor anonymity network, which is discussed above, under [*Anonymity networks*](#Anonymity_networks).


