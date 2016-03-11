

---

lang: xx
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 016
title: Tor Browser - Digital Anonymity and Circumvention

---

**Homepage**
			
[**https://www.torproject.org**](https://www.torproject.org/)
			
**Computer Requirements**

- Any version of **Windows** (XP or newer)
- An Internet connection		

**Versions used in this guide**

- Tor Browser: 3.5.3

**Last revision of this chapter**

- March 2014

**License** 

- Free and Open-Source Software ([BSD license](https://en.wikipedia.org/wiki/BSD_license))

**Required Reading** 

- How-to Booklet Chapter [**8. How to remain anonymous and bypass censorship on the Internet**](/en/chapter-8) 

**What you will get in return**: 

- The ability to conceal your digital identity from the websites that you visit
- The ability to conceal your on-line destinations from **Internet Service Providers (ISPs)** and other surveillance mechanisms
- The ability to bypass Internet censorship and filtering rules

**GNU Linux, Mac OS and other Microsoft Windows Compatible Programs**:

The **Tor Browser** is available for **GNU Linux**, **Mac OS**, **Microsoft Windows** and **Android** operating systems. **Tor** is the most recommended and rigorously tested tool for keeping your online activities anonymous. But we would like to list some other recommended solutions here:


* [**Riseup VPN**](https://help.riseup.net/en/riseup-vpn/) is a free **Virtual Private Network** (**VPN**) proxy server for **Linux**, **MAC**, **Android** and **Microsoft Windows**.
* [**Psiphon3**](http://www.psiphon3.com/) is a free commercial **Virtual Private Network** (**VPN**) solution for **Microsoft Windows** and **Android OS**.
* [**Dynaweb FreeGate**](http://www.dit-inc.us/freegate) is a free proxy tool for **Microsoft Windows**.
* [**Your Freedom**](http://www.your-freedom.net/) is a commercial proxy tool that also offers a free (though slower) service. It is available for **Linux**, **Mac OS** and **Microsoft Windows**.

## 1.1 Things you should know about this tool before you start ##

The **Tor Browser** is a software tool designed to increase the privacy and security of your Internet activities and habits. It masks your identity and your on-line browsing from many forms of Internet surveillance. **Tor** can also be useful as a secure means of circumventing electronic restrictions so that you may access or publish blogs and news reports.

**Tor** protects your *anonymity* by routing communications through a distributed network of servers run by volunteers from all over the world. Using **Tor** hides the sites you visit from potential onlookers, and hides your location/identity from those sites. The software is designed also to make sure servers in the **Tor** network **don't know** both your location **and** the sites you are visiting.

**Tor** also takes steps to encrypt the communication to and through its network, **but** this measure can not extend all the way to a website which is sending or receiving content over non-encrypted channels (i.e. not providing https access).  Nevertheless, the advantage of using Tor when accessing such sites is that **Tor** can secure your communication up to the step between the last of the **Tor** servers and the non-secure site. This confines the chance to intercept the content to that last step.

The **Tor Browser Bundle** consists of the **Tor** software and a modified version of the **Firefox** web browser, which is designed to provide extra protection while using it. The browser bundle also includes [**NoScript**](/en/firefox_noscript) and [**HTTPS-Everywhere**](/en/firefox_others#5.1) add-ons. 

**Note**: There is a trade-off between anonymity and speed. Because Tor facilitates anonymous browsing by bouncing your traffic through volunteers' computers and servers in various parts of the world, it will definitely be slower than using other web browsers on your computer.

**Definitions**: 

- **Bridge Relay**: A Bridge Relay is a **Tor** server that is not publicly announced. If you choose to use a bridge, the server can provide you with access to the **Tor** network even if **Tor** is blocked in your country.

- **Port:** In this chapter, a port is an access point through which software communicates with services running on other networked computers. If a URL, such as **www.google.com**, gives you the 'street address' of a service, then the port tells you which 'door' to use once you reach the correct destination. When browsing the Web, you typically use port 80 for unsecured sites (**http://mail.google.com**) and port 443 for secured ones (**https://mail.google.com**).

- **Proxy:** A proxy is a software intermediary that runs on your computer, on your local network, or somewhere else on the Internet, that helps to relay your communication toward its final destination.

- **Route:** A route is the communication path on the Internet between your computer and the destination server.

