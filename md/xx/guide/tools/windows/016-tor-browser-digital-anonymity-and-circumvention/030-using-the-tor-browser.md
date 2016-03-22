

---

lang: xx
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: Using the Tor Browser

---

- [**4.0 Using the Tor Browser**](#4.0)
- [**4.1 Additional checking if the Tor Browser works**](#4.1)
- [**4.2 How to create a new identity**](#4.2)
- [**4.3 Enabling NoScript add-on**](#4.3)
- [**4.3 Tor Browser updates**](#4.3)


<a name="4.0"></a>
## 4.0 Using the Tor Browser ##

The **Tor Browser** is designed to be very easy to use, in fact if you are familiar with using a web browser you will be able to use the **Tor Browser** as it is a version of **Firefox** modified for additional privacy and security. 

**Note:** as the **Tor Browser** is designed with privacy in mind, it is configured not to save any information to your hard drive or USB stick.  This means that when you quit the **Tor Browser** all your browsing history is forgotten.

<a name="4.1"></a>
## 4.1 Additional checking if the Tor Browser works ##

As with any circumvention software it is recommended to perform simple independent tests to ensure the **Tor Browser** works, by going to any website that will try to identify where are you based from the IP address we visit the site from.

There are a number of free website that do this, such as: [check.torproject.org](https://check.torproject.org), [iplocation.net](http://www.iplocation.net/), [ip2location.com](http://www.ip2location.com/), [whatismyipaddress.com](http://whatismyipaddress.com/), etc. If you access these website directly without using **Tor Browser** or other circumvention tool it should display your real IP address and provide a more or less accurate physical location for you. However if you access those websites using **Tor Browser** or other circumvention tool the location and IP address you will see should be different.

![](/sbox/screen/tor-en-1/031.png)

*Figure 1: Firefox (top) & The Tor Browser (bottom) on the same computer showing Tor status and IP address differences*

<a name="4.2"></a>
## 4.2 How to create a new identity ##

You can create a *new identity* for your Browser.  This means that new set of random **Tor** proxy servers will be selected for you to use. This will make you appear to come from a new location to the web servers. To do this, click on ![](/sbox/screen/tor-en-1/022.png) and select *New Identity* from the menu.  The *Tor Browser* will briefly close, clearing your *browsing history* and *cookies* and then restart. Once they browser has restarted you can check your new location as described above in section 4.1.

![](/sbox/screen/tor-en-1/032.png)

*Figure 2: Selecting New Identity from TorButton menu*

<a name="4.3"></a>
## 4.3 Enabling NoScript add-on ##

**Tor Browser** comes with **NoScript** add-on pre-installed. **NoScript** can additionally protect you from malicious websites and from leaking your real identity through execution of scripts in your **Tor Browser**, however **NoScript** is disabled by default in **Tor Browser** so this additional protection is not readily available. 

If you wish to enable the extra protections afforded by **NoScript**, it can be turned on by opening the **NoScript** menu and clicking *Forbid Scripts Globally* and then configuring the various *options* it provides. 

We recommend that you read more about [**NoScript** in the **FireFox** chapter](/en/firefox_noscript). 

![](/sbox/screen/tor-en-1/033.png)

*Figure 3: Enabling NoScript by selecting Forbid Scripts Globally (advised) option*

<a name="4.4"></a>
## 4.4 Tor Browser updates ##

In **[How-to Booklet chapter 1.4](/en/chapter_1_4)** we explain how important is keeping your software up to date, the **Tor Browser** is no exception.  When updates are available, the next time you start the **Tor Browser** you will be presented with a notice that your browser is out of date (*Figure 4*) and instructed to click and choose **Download Tor Browser Update**. You will be brought to the **Tor Project** website where you can get the latest release.  Once downloaded you can follow this guide to install the updated **Tor Browser**.


![](/sbox/screen/tor-en-1/034.png)

*Figure 4: Tor Browser showing an update is available*

