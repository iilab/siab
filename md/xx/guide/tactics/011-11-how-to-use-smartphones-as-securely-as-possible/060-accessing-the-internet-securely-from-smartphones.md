

---

lang: xx
community: guide
type: tactics
legacy: True
child: True
weight: 6
depth: 3
title: Accessing the Internet Securely from Smartphones

---

As discussed in [***Chapter 7: How to keep your Internet communication private***](/en/chapter-7) and [***Chapter 8: How to remain anonymous and bypass censorship on the Internet***](/en/chapter-8), access to content on the Internet, or publishing material online such as photos or videos, leaves many traces of who and where you are and what you are doing. This may put you at risk. Using your smartphone to communicate with the Internet magnifies this risk.

### Access through WiFi or Mobile Data ###

Smartphones allow you to control how you access the Internet: via a wireless connection provided by an access point (such as an internet cafe), or via a mobile data connection, such as GPRS, EDGE, or UMTS provided by your mobile network operator. 

Using a WiFi connection reduces the traces of data you may be leaving with your mobile phone service provider (by not having it connected with your mobile phone subscription). However, sometimes a mobile data connection is the only way to get online. Unfortunately mobile data connection protocols (like EDGE or UMTS) are not open standards. Independent developers and security engineers cannot examine these protocols to see how they are being implemented by mobile data carriers. 

In some countries mobile access providers operate under different legislation than internet service providers, which can result in more direct surveillance by governments and carriers.

Regardless of which path you take for your digital communications with a smartphone, you can reduce your risks of data exposure through the use of anonymising and encryption tools.

### Anonymise ###

To access content online anonymously, you can use an Android app called [**Orbot**](https://www.torproject.org/docs/android.html.en). Orbot channels your internet communication through Tor's anonymity network. 

<div class=getstarted markdown=1>
Hands-on: Get started with the [*Orbot Guide*](/en/Orbot_main)
</div>

Another app, Orweb, is a web browser that has privacy enhancing features like using proxies and not keeping a local browsing history. Orbot and Orweb together circumvent web filters and firewalls, and offer anonymous browsing.

<div class=getstarted markdown=1>
Hands-on: Get started with the [*Orweb Guide*](/en/Orweb_main)
</div>

### Proxies ###

The mobile version of [*Firefox*](/en/glossary#Firefox) – [**Firefox mobile**](http://f-droid.org/repository/browse/?fdid=org.mozilla.firefox) can be equipped with proxy add-ons, which direct your traffic to a proxy server. From there your traffic goes to the site you are requesting. This is helpful in cases of censorship, but still may reveal your requests unless the connection from your client to the proxy is encrypted. We recommend the [**Proxy Mobile**](https://guardianproject.info/apps/proxymob-firefox-add-on/) add-on (also from [**Guardian Project**](https://guardianproject.info/), which makes proxying with Firefox easy. Is also the only way to channel Firefox mobile communications to Orbot and use the [*Tor*](/en/glossary#Tor) network. 

