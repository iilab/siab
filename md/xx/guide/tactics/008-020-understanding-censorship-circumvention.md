

---

lang: xx
community: guide
type: tactics
legacy: True
child: True
weight: 2
depth: 3
title: Understanding censorship circumvention

---

If you cannot go directly to a website because it is blocked by one
of the methods discussed above, you will need to find a way around the
obstruction. A secure [*proxy*](/en/glossary#Proxy) server, located in a country that does not
filter the Internet, can provide this kind of detour by fetching the
webpages you request and delivering them to you. From your [*ISP's*](/en/glossary#ISP) 
perspective, you will simply appear to be communicating securely with
an unknown computer (the [*proxy*](/en/glossary#Proxy) server) somewhere on the Internet.

![](/sites/securitybkp.ngoinabox.org/security/files/img/2-en.png)

Of course, the government agency in charge of Internet censorship in
your country (or the company that provides updates for its filtering
software) might eventually learn that this 'unknown computer' is really
a circumvention [*proxy*](/en/glossary#Proxy). If that happens, its  [*IP address*](/en/glossary#IP_address) may itself be added to the [*blacklist*](/en/glossary#Blacklist) , and it will no longer work. It usually takes
some time for[*proxies*](/en/glossary#Proxy) to be blocked, however, and those who create and
update circumvention tools are well aware of this threat. They typically fight back using one or both of the following methods:

- **Hidden proxies** are more difficult to identify. This is one of the reasons why it is important to use secure [*proxies*](/en/glossary#Proxy), which tend to be less obvious.  [*Encryption*](/en/glossary#Encryption) is only part of the solution, however. The operators of a [*proxy*](/en/glossary#Proxy) must also take care when revealing its location to new users if they want it to remain hidden.
	
- **Disposable proxies** can be replaced very quickly after they are blocked. In this case, the process of telling users how to find replacement [*proxies*](/en/glossary#Proxy) may not be particularly secure. Instead, circumvention tools of this type often simply try to
distribute new [*proxies*](/en/glossary#Proxy) faster than they can be blocked.
	
In the end, as long as you can reach a [*proxy*](/en/glossary#Proxy) that you
trust to fetch the services you ask for, all you have to do is send it
your requests and view whatever comes back using the appropriate
Internet application. Typically, the details of this process are handled
automatically by circumvention software that you install on your
computer, by modifying your browser settings or by pointing your
browser to a web-based [*proxy*](/en/glossary#Proxy)  page. The [*Tor*](/en/glossary#Tor) 
anonymity network, described below, uses the first
method. Following that is a discussion of basic, single[*proxy*](/en/glossary#Proxy) 
circumvention tools, each of which works in a slightly different manner.


