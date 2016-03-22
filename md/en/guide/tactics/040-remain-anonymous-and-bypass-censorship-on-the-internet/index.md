
---

lang: en
community: guide
type: tactics
weight: 040
title: Remain anonymous and bypass censorship on the Internet

---

Many countries around the world have installed software that prevents Internet users within those countries from accessing certain websites and Internet services. Companies, schools and public libraries often use similar software to protect their employees, students and patrons from material that they consider distracting or harmful. This kind of filtering technology comes in a number of different forms. Some filters block a site based on its [*IP address*](/en/glossary#IP_address), while others blacklist certain [*domain names*](/en/glossary#Domain_name) or search through all unencrypted Internet communication, looking for specific keywords.

Regardless of what filtering methods are present, it is nearly always possible to evade them by relying on intermediary computers, outside your country, to reach blocked services for you. This process is often called *censorship circumvention*, or simply [*circumvention*](/en/glossary#Circumvention), and the intermediary computers are called [*proxies*](/en/glossary#Proxy). [*Proxies*](/en/glossary#Proxy), too, come in many different forms. This guide includes a brief discussion of multiple-proxy anonymity networks followed by a more thorough description of basic [*circumvention*](/en/glossary#Circumvention) [*proxies*](/en/glossary#Proxy) and how they work. 

Both of these methods are effective ways to evade Internet filters, although the former is most appropriate if you are willing to sacrifice speed in order to keep your Internet activities as anonymous as possible. If you know and trust the individual or organization that operates your [*proxy*](/en/glossary#Proxy), or if performance is more important to you than anonymity, then a basic [*circumvention*](/en/glossary#Circumvention) [*proxy*](/en/glossary#Proxy) might serve you better.


# What you can learn from this guide

- How to access a website that is blocked from within your country
- How to prevent websites that you visit from knowing your location 
- How to ensure that neither your [*ISP*](/en/glossary#ISP) nor a surveillance organization in your country can determine which websites and Internet services you visit

## Introduction to anonymity and circumvention


:[Snippet](snippets/snippet_01)





# Understanding Internet censorship
Research carried out by organisations like the [OpenNet Initiative](http://opennet.net/) (ONI) and [Reporters Without Borders](http://www.rsf.org/) (RSF) indicates that many countries filter a wide variety of social, political and 'national security' content, while rarely publishing precise lists of what has been blocked. Naturally, those who wish to control their citizens' access to the Internet also make a special effort to block known proxies and websites that offer tools and instructions to help people circumvent these filters.

Despite the guarantee of free access to information enshrined in Article 19 of the Universal Declaration of Human Rights, the number of countries engaged in Internet censorship has continued to increase dramatically over the past few years. As the practice of Internet filtering spreads throughout the world, however, so does access to the circumvention tools that have been created, deployed and publicised by activists, programmers and volunteers. 

Before exploring the various ways to bypass Internet censorship, you should first develop a basic understanding of how these filters work. In doing so, it may be helpful to consider a greatly-simplified model of your connection to the Internet.





## Your Internet connection

The first step of your connection to the Internet is typically made through an <i>Internet Service Provider[*ISP*](/en/glossary#ISP)  at your home, office, school, library or Internet cafe. The [*ISP*](/en/glossary#ISP) assigns your computer an [*IPaddress*](/en/glossary#IP_address), which various Internet services can use to identify you and send you information, such as the emails and webpages you request. Anyone who learns your [*IP address*](/en/glossary#IP_address) can figure out what city you are in. Certain well-connected organisations in your country, however, can use this information to determine your precise location.

- **Your ISP** will know which building you are in or which phone line you are using if you access the Internet through a modem.	
- **Your Internet cafe, library or business** will know which computer you were using at a given time, as well as which port or wireless access point you were connected to.	
- **Government agencies** may know all of these details, as a result of their influence over the organisations above.
	
At this stage, your [*ISP*](/en/glossary#ISP) relies on the network infrastructure in your country to connect its users, including you, with the rest of the world. On the other end of your connection, the website or Internet service you are accessing has gone through a similar process, having received its own IP addresses from an [*ISP*](/en/glossary#ISP) in its own country. Even without all of the technical details, a basic model like this can be helpful when considering the various tools that allow you get around filters and remain anonymous on the Internet.




## How websites are blocked

Essentially, when you go to view a webpage, you are showing the site's [*IP address*](/en/glossary#IP_address) to your [*ISP*](/en/glossary#ISP) and asking it to connect you with the webserver's [*ISP*](/en/glossary#ISP). And, if you have an unfiltered Internet connection, it will do precisely that. If you are in a country that censors the Internet, however, it will first consult a [*blacklist*](/en/glossary#Blacklist) of forbidden websites and then decide whether or not to comply with your request.

In some cases, there may be a central organisation that handles filtering in place of the [*ISPs*](/en/glossary#ISP) themselves. Often, a [*blacklist*](/en/glossary#Blacklist) will contain [*domain names*](/en/glossary#Domain_names), such as www.blogger.com, rather than [*IPaddresses*](/en/glossary#IP_addresses). And, in some countries, filtering software monitors your connection, rather than trying to block specific Internet addresses. This type of software scans through the requests that you make and the pages that are returned to you, looking for sensitive key words and then deciding whether or not to let you see the results.

And, to make matters worse, when a webpage is blocked you may not even know it. While some filters provide a 'block page' that explains why a particular page has been censored, others display misleading
error messages. These messages may imply that the page cannot be found, for example, or that the address was misspelled.

In general, it is easiest to adopt a worst-case perspective toward Internet censorship, rather than trying to research all of the particular strengths and weaknesses of the filtering technologies used in your country. In other words, you might as well assume that: 

- Your Internet traffic is monitored for keywords
- Filtering is implemented directly at the [*ISP*](/en/glossary#ISP) level
- Blocked sites are [*blacklisted*](/en/glossary#Blacklist) by both their  [*IP addresses*](/en/glossary#IP_address) and their [*domain names*](/en/glossary#Domain_name)
- You may be given an unclear or misleading reason to explain why a blocked site fails to load. 
	
Because the most effective circumvention tools can be used regardless of which filtering methods are in place, it does not generally do any harm to make these pessimistic assumptions


:[Snippet](snippets/snippet_02)




# Understanding censorship circumvention
If you cannot go directly to a website because it is blocked by one of the methods discussed above, you will need to find a way around the obstruction. A secure [proxy](/en/glossary#Proxy) server, located in a country that does not filter the Internet, can provide this kind of detour by fetching the webpages you request and delivering them to you. From your [ISP's](/en/glossary#ISP) perspective, you will simply appear to be communicating securely with an unknown computer (the [proxy](/en/glossary#Proxy) server) somewhere on the Internet.

Of course, the government agency in charge of Internet censorship in your country (or the company that provides updates for its filtering software) might eventually learn that this 'unknown computer' is really a circumvention [*proxy*](/en/glossary#Proxy). If that happens, its  [*IP address*](/en/glossary#IP_address) may itself be added to the [*blacklist*](/en/glossary#Blacklist) , and it will no longer work. It usually takes
some time for[*proxies*](/en/glossary#Proxy) to be blocked, however, and those who create and update circumvention tools are well aware of this threat. They typically fight back using one or both of the following methods:

- **Hidden proxies** are more difficult to identify. This is one of the reasons why it is important to use secure [*proxies*](/en/glossary#Proxy), which tend to be less obvious.  [*Encryption*](/en/glossary#Encryption) is only part of the solution, however. The operators of a [*proxy*](/en/glossary#Proxy) must also take care when revealing its location to new users if they want it to remain hidden.
	
- **Disposable proxies** can be replaced very quickly after they are blocked. In this case, the process of telling users how to find replacement [*proxies*](/en/glossary#Proxy) may not be particularly secure. Instead, circumvention tools of this type often simply try to distribute new [*proxies*](/en/glossary#Proxy) faster than they can be blocked.
	
In the end, as long as you can reach a [*proxy*](/en/glossary#Proxy) that you trust to fetch the services you ask for, all you have to do is send it your requests and view whatever comes back using the appropriate
Internet application. Typically, the details of this process are handled automatically by circumvention software that you install on your computer, by modifying your browser settings or by pointing your browser to a web-based [*proxy*](/en/glossary#Proxy)  page. The [*Tor*](/en/glossary#Tor) anonymity network, described below, uses the first method. Following that is a discussion of basic, single[*proxy*](/en/glossary#Proxy) circumvention tools, each of which works in a slightly different manner.



# Anonymity networks and basic proxy servers





## Anonymity networks

Anonymity networks typically 'bounce' your Internet traffic around between various secure [*proxies*](/en/glossary#Proxy) in order to disguise where you are coming from and what you are trying to access. This can significantly reduce the speed at which you are able to load websites and other Internet services. In the case of [*Tor*](/en/glossary#Tor) , however, it also provides a reliable, secure and public means of circumvention that saves you from having to worry about whether or not you trust the individuals who operate your [proxies](/en/glossary#Proxy) and the websites you visit. As always, you must ensure that you have an encrypted connection, [HTTPS](/en/glossary#SSL), to a secure website before exchanging sensitive information, such as passwords and emails, through a browser.

You will have to install software to use [*Tor*](/en/glossary#Tor), but the result is a tool that provides anonymity as well as circumvention. Each time you connect to the [*Tor*](/en/glossary#Tor) network, you select a random path through three secure [*Tor*](/en/glossary#Tor) [*proxies*](/en/glossary#Proxy). This ensures that neither your [*ISP*](/en/glossary#ISP) nor the [*proxies*](/en/glossary#Proxy) themselves know both your  computer's [*IPaddress*](/en/glossary#IP_address) and the location of the Internet services you request. You can learn much more about this tool from the Tor Guide.


:[Hands-on: get started with TorBrowser for Windows - Digital Anonymity and Circumvention](../../tools/windows/torbrowser)

One of Tor's strengths is that it does not just work with a browser but can be used with various types of Internet software. Email programs, including Mozilla  [*Thunderbird*](/en/glossary#Thunderbird),and instant messaging programs,including [*Pidgin*](/en/glossary#Pidgin), can operate through Tor, either to access filtered services or to hide your use of those services.


## Basic circumvention proxies

There are three important questions that you should consider when selecting a basic circumvention [*proxy*](/en/glossary#Proxy) . First, is it a web-based tool or does it require you to change settings or install software on your computer? Second, is it secure? Third, is it private or public?



## Web-based and other proxies

Web-based [*proxies*](/en/glossary#Proxy) are probably the easiest to use. They require only that you point your browser at a [*proxy*](/en/glossary#Proxy) webpage, enter the filtered address you wish to view and click one button. The [*proxy*](/en/glossary#Proxy) will then display the requested content inside its own webpage. You can follow links normally or enter a new address into the [*proxy*](/en/glossary#Proxy) if you want to view a different page. You do not need to install any software or change any browser settings, which means that web-based [*proxies*](/en/glossary#Proxy) are:

- Easy to use
- Reachable from public computers, such as those at Internet cafes, that may not allow you to install programs or change settings
- Potentially safer if you are concerned about being 'caught' with circumvention software on your computer
	
Web-based [*proxies*](/en/glossary#Proxy)  tend to have certain disadvantages, as well. They do not always display pages correctly, and many web-based [*proxies*](/en/glossary#Proxy) will fail to load complex websites, including those that feature streaming audio and video content. Also, while any [*proxy*](/en/glossary#Proxy) will slow down as it gains more users, this tends to be more of an issue with public web-based [*proxies*](/en/glossary#Proxy). And, of course, web-based [*proxies*](/en/glossary#Proxy) only work for webpages. You can not, for example, use an instant messaging program or an email client to access blocked services through a web-based [*proxy*](/en/glossary#Proxy). Finally, secure web-based [*proxies*](/en/glossary#Proxy)  offer limited confidentiality because they must themselves access and modify the information returned to you by the websites you visit. If they did not, you would be unable to click on a link without leaving the [*proxy*](/en/glossary#Proxy) behind and attempting to make a direct connection to the target webpage. This is discussed further in the following section.

Other types of [*proxies*](/en/glossary#Proxy) generally require you to install a program or configure an external [*proxy*](/en/glossary#Proxy) address in your browser or operating system. In the first case, your circumvention program will typically provide some way of turning the tool on and off, which will tell your browser whether or not to use the [*proxy*](/en/glossary#Proxy). Software like this often allows you to change  [*proxies*](/en/glossary#Proxy) automatically if one is blocked, as discussed above. If you have to configure an external [*proxy*](/en/glossary#Proxy) address in your browser or operating system, you will need to learn the correct [*proxy*](/en/glossary#Proxy) address, which may change if that [*proxy*](/en/glossary#Proxy) is blocked or slows down so much that it becomes unusable.

Although it may be slightly more difficult to use than a web-based [*proxy*](/en/glossary#Proxy),this method of circumvention is more likely to display complex pages correctly and may take longer to slow down as more people begin to use a given [*proxy*](/en/glossary#Proxy) server. Furthermore, [*proxies*](/en/glossary#Proxy) can be found for a number of different Internet applications. Examples include HTTP [*proxies*](/en/glossary#Proxy) for browsers, SOCKS [*proxies*](/en/glossary#Proxy)  for email and chat programs and VPN [*proxies*](/en/glossary#Proxy), which can redirect all of your Internet traffic to avoid filtering.



## Secure and insecure proxies
A secure [*proxy*](/en/glossary#Proxy), in this guide, refers to any [*proxy*](/en/glossary#Proxy)  that supports [*encrypted*](/en/glossary#Encryption) connections from its users. An insecure [*proxy*](/en/glossary#Proxy) will still allow you to bypass many types of filtering, but will fail if your Internet connection is being scanned for key words or particular website addresses.It is a particularly bad idea to use an insecure [*proxy*](/en/glossary#Proxy) when accessing websites that are normally  [*encrypted*](/en/glossary#Encryption), such as webmail accounts and banking websites. By doing so, you may expose sensitive information that would normally be hidden. And, as mentioned previously, insecure [*proxies*](/en/glossary#Proxy) are often easier for those who update Internet filtering software and policies to discover and block. In the end, the fact that free, fast, secure [*proxies*](/en/glossary#Proxy) exist means that there are very few good reasons to settle for an insecure one.

You will know that a web-based [*proxy*](/en/glossary#Proxy) is secure if you can access the [*proxy*](/en/glossary#Proxy) webpage itself using an [*HTTPS*](/en/glossary#HTTPS) address. As with webmail services, secure and insecure connections may be supported, so you should be certain to use the secure address. It may happen that, in such cases, you will be asked to accept a 'security certificate warning' from your browser in order to continue. This is the case for the [*Peacefire*](/en/glossary#Peacefire) [*proxy*](/en/glossary#Proxy), discussed below. Warnings like this tell you that someone, such as your ISP or a hacker, could be monitoring your connection to the [*proxy*](/en/glossary#Proxy). Despite these warnings, it may be still a good idea to use secure [*proxies*](/en/glossary#Proxy) whenever possible. However, when relying on such  [*proxies*](/en/glossary#Proxy) for circumvention, you should avoid visiting secure websites unless you verify the [*proxy's*](/en/glossary#Proxy) [*SSL*](/en/glossary#SSL) fingerprint. In order to do this, you will need a way of securely communicating with the [*proxy's*](/en/glossary#Proxy) administrator. **It is best not to enter passwords or exchange sensitive information when using web proxies in general.**

You should also avoid accessing sensitive information through a web-based [*proxy*](/en/glossary#Proxy) unless you trust the person who runs it. This applies regardless of whether or not you see a security certificate warning when you visit the  [*proxy*](/en/glossary#Proxy). It even applies if you know the [*proxy*](/en/glossary#Proxy)  operator well enough to verify the server's *fingerprint* before directing your browser to accept the warning. When you rely on a single [*proxy*](/en/glossary#Proxy) server for circumvention, its administrator will always know your [*IP address*](/en/glossary#IP_address) and which website/s you are accessing. More importantly, however, if that [*proxy*](/en/glossary#Proxy) is web-based, a malicious operator could gain access to all of the information that passes between your browser and the websites you visit, including the content of your webmail and your passwords.

For [*proxies*](/en/glossary#Proxy) that are not web-based, you may have to do a little research to determine whether or not secure connections are supported. All of the  [*proxies*](/en/glossary#Proxy) and anonymity networks recommended in this guide are secure. 




## Public and private proxies

Public [*proxies*](/en/glossary#Proxy) accept connections from anyone, whereas private [*proxies*](/en/glossary#Proxy) typically require a username and password. While public [*proxies*](/en/glossary#Proxy) have the obvious advantage of being freely available, assuming they can be found, they tend to become overcrowded very quickly. As a result, even though public [*proxies*](/en/glossary#Proxy) may be as technically sophisticated and well-maintained as private ones, they are often relatively slow. Finally, private [*proxies*](/en/glossary#Proxy) tend to be run either as for-profit businesses or by administrators who create accounts for users that they know personally or socially. Because of this, it is generally easier to determine what motivates the operators of a private  [*proxy*](/en/glossary#Proxy). You should not assume, however, that private  [*proxies*](/en/glossary#Proxy) are therefore fundamentally more trustworthy. After all, the profit motive has led online services to expose their users in the past.

Simple, insecure, public [*proxies*](/en/glossary#Proxy) can often be found by searching for terms like 'public proxy' in a search engine, but you should not rely on  [*proxies*](/en/glossary#Proxy) discovered this way. Given the choice, it is better to use a private, secure [*proxy*](/en/glossary#Proxy) run by people that you know and trust, either personally or by reputation, and who have the technical skill to keep their server secure. Whether or not you use a web-based [*proxy*](/en/glossary#Proxy) will depend on your own particular needs and preferences. Any time you are using a [*proxy*](/en/glossary#Proxy) for circumvention, it is also a good idea to use the [*Firefox*](/en/glossary#Firefox)  browser and to install the [*NoScript*](/en/glossary#NoScript) browser extension, as discussed in the [*Firefox Guide*](firefox/windows). Doing so can help protect you both from malicious  [*proxies*](/en/glossary#Proxy) and from websites that might try to discover your real [*IP address*](/en/glossary#IP_address). Finally, keep in mind that even an [*encrypted*](/en/glossary#Encrypted) [*proxy*](/en/glossary#Proxy) will not make an insecure website secure. You must still ensure that you have an [*HTTPS*](/en/glossary#SSL) connection before sending or receiving sensitive information.

If you are unable to find an individual, organisation or company whose  [*proxy*](/en/glossary#Proxy) service you consider trustworthy, affordable and accessible from your country, you should consider using the Tor anonymity network, which is discussed above, under [*Anonymity networks*](#519).



# Specific circumvention proxies

Below are a few specific tools and [*proxies*](/en/glossary#Proxy) that can help you circumvent Internet filtering. New circumvention tools are produced regularly, and existing ones are updated frequently, so you should visit the online Security in-a-Box website, and the resources mentioned in the **Further reading** section below, to learn more.

**Virtual Private Network (VPN) based proxies**

VPN proxies listed below make your entire Internet  connection pass through the proxy while you are "connected". This  can be helpful if you use email or instant messaging providers that are filtered in your country

**Riseup VPN.** It is for users who have email accounts on the *Riseup* server. The collective offers the possibility of connecting to a secure, private, free VPN proxy server. Please read [*more about Riseup VPN*](https://help.riseup.net/en/riseup-vpn) and on [*how to connect to it*](https://we.riseup.net/riseuphelp+en/vpn-howto).

**Your-Freedom** is a private, secure, VPN/SOCKS circumvention [*proxy*](/en/glossary#Proxy). It is a [*freeware*](/en/glossary#Freeware) tool that that can be used to access a free circumvention service. There are restrictions on bandwidth and for how long can you can use it (3 hours per day, up to 9 hours per week). You can also pay a fee to access a commercial service, which is faster and has fewer limitations. In order to use Your-Freedom, you will need to [*download  the tool*](http://www.your-freedom.net/index.php?id=3) and [*create an account*](http://www.your-freedom.net/index.php?id=170&amp;L=0), both of which can be done at the  [*Your-Freedom website*](https://www.your-freedom.net/). You will also need to configure your browser to use the [*OpenVPN*](https://www.your-freedom.net/index.php?id=172) proxy when connecting to the Internet. You can [*read more in Your-Freedom documentation*](https://www.your-freedom.net/index.php?id=doc).

**Freegate** is a public, secure, VPN, freeware circumvention proxy. You can [download the latest version of Freegate](http://www.dit-inc.us/freegate) or [read interesting article about it](http://www.addictivetips.com/windows-tips/freegate-lets-you-access-blocked-websites-at-optimal-speed/).

**SecurityKISS** is a public, secure, VPN, freeware circumvention proxy. To use it you need to [download and run a free program](http://www.securitykiss.com/resources/download/). There is no need to register an account. Free users are restricted to a 300 MB per day usage limit and by higher Internet traffic through the proxy. Paid subscription offers restriction-free usage and more VPN servers.  Please see the [SecurityKISS homepage to learn more](http://www.securitykiss.com).

**Psiphon3** is a secure, public circumvention tool that utilizes VPN, SSH and HTTP Proxy technology to provide you with uncensored access to Internet content. In order to use it you need to download the program from the [*Psiphon3 homepage*](http://psiphon3.com) and run it to select which mode you would like to use *VPN, SSH, SSH+*. Psiphon3 works with Android devices as well. Please see the  [*homepage*](http://psiphon3.com) to learn more. 


**Web Proxies:**

**Peacefire** maintains a large number of public, web-based [*proxies*](/en/glossary#Proxy), which can be secure or insecure, depending on how you access them. When using a [*Peacefire*](/en/glossary#Peacefire) [*proxy*](/en/glossary#Proxy), you must enter the [*HTTPS*](/en/glossary#SSL) address in order to have a secure connection between yourself and the [*proxy*](/en/glossary#Proxy). New [*proxies*](/en/glossary#Proxy) are announced to a large mailing list on a regular basis. You can sign up to receive updates at the [*Peacefire website*](http://peacefire.org/).



# Further reading

- See the *2.5 Internet Surveillance and Monitoring* and *2.6 Censorship circumvention* chapters of the [*Digital Security and Privacy Manual for Human Rights Defenders*](http://www.frontlinedefenders.org/esecman) book.
- The FLOSS Manuals website contains a guide on [*How to Bypass Internet Censorship*](https://www.howtobypassinternetcensorship.org/).
- The [*Internet Censorship Wiki*](http://en.cship.org/wiki/Main_Page),
 written by Freerk, is available in English, German and Spanish.
- The CitizenLab has produced [*Everyone's guide to by-passing Internet Censorship*](http://citizenlab.org/guides/everyones-guide-english.pdf), which is being translated into Burmese, English, French, Russian, Spanish and Urdu.
- Reporters Without Borders has released a second edition of its [*Handbook for Bloggers and Cyberdissidents*](http://www.rsf.org/IMG/pdf/Bloggers_Handbook2.pdf), which is available in Arabic, Burmese, Chinese, English, Farsi, French, Russian and Spanish.
- Ethan Zuckerman of Global Voices Online has published a useful guide to  [*Anonymous Blogging with Wordpress and Tor*](http://advocacy.globalvoicesonline.org/tools/guide/).
