

---

lang: en
community: guide
type: tools
os: windows
weight: 080
title: TorBrowser for Windows - Digital Anonymity and Circumvention

---

The **Tor Browser** keeps your online activities private. It disguises your identity and protects your Web traffic from many forms of Internet surveillance. **Tor** can also be used to bypass Internet filters.

# Required reading


:[](../../../tactics/anonymity and circumvention)


:[](torbrowser-for-windows-digital-anonymity-and-circumvention)

# What you will get from this guide

- The ability to hide your location on the Internet from the websites you visit
- The ability to conceal which websites you visit from **Internet Service Providers (ISPs)** and surveillance programmes
- The ability to bypass Internet censorship and filtering rules
- Protection from insecure and potentially malicious websites through the *HTTPS Everywhere* and *NoScript* browser add-ons

# 1. Introduction to the Tor Browser

**Note:** If you are in a location where access to the **Tor Project** website is blocked, you can use email to request a download link that is more likely to work. Just send an email to **gettor@torproject.org** with the version you need (**windows**, **OsX** or **Linux**) in the body of the message. You will receive a response that includes a link to the **Tor Browser** archive via **Dropbox**, **Google Docs** or **Github**. Further details about this feature are available on the [Tor Project website](https://www.torproject.org/projects/gettor.html).

## 1.0 Other tools like the Tor Browser

**GNU Linux, Mac OS and other Microsoft Windows Compatible Programs**:

The **Tor Browser** is available for the **GNU Linux**, **Mac OS**, **Microsoft Windows** and **Android** operating systems. **Tor** is the most rigorously tested tool for keeping your online activities anonymous. Below are a few other tools that are suitable for circumventing online censorship and protecting the confidentiality of your local traffic. Unlike **Tor**, these tools require that you trust the service provider: 

* [**Riseup VPN**](https://help.riseup.net/en/riseup-vpn/) is a free **Virtual Private Network** (**VPN**) proxy server for **Linux**, **MAC**, **Android** and **Microsoft Windows**.
* [**Psiphon**](http://www.psiphon.ca/) is a free commercial **Virtual Private Network** (**VPN**) solution for **Microsoft Windows** and **Android**.
* [**Your Freedom**](http://www.your-freedom.net/) is a commercial proxy tool that also offers a free service. It is available for **Linux**, **Mac OS** and **Microsoft Windows**.


## 1.1 Things you should know about the Tor Browser before you start

The **Tor Browser** is a software tool designed to increase the privacy and security of your Internet activities and habits. It masks your identity and your on-line browsing from many forms of Internet surveillance. **Tor** can also be useful as a secure means of circumventing electronic restrictions so that you may access or publish blogs and news reports.

**Tor** protects your *anonymity* by routing communications through a distributed network of servers run by volunteers from all over the world. Using **Tor** hides the sites you visit from potential onlookers, and hides your location/identity from those sites. The software is designed also to make sure servers in the **Tor** network **don't know** both your location **and** the sites you are visiting.

**Tor** also takes steps to encrypt the communication to and through its network, **but** this measure can not extend all the way to a website which is sending or receiving content over non-encrypted channels (i.e. not providing https access).  Nevertheless, the advantage of using Tor when accessing such sites is that **Tor** can secure your communication up to the step between the last of the **Tor** servers and the non-secure site. This confines the chance to intercept the content to that last step.

The **Tor Browser Bundle** consists of the **Tor** software and a modified version of the **Firefox** web browser, which is designed to provide extra protection while using it. The browser bundle also includes [**NoScript**](../firefox/windows#801t) and [**HTTPS-Everywhere**](../firefox/windows#804) add-ons. 

**Note**: There is a trade-off between anonymity and speed. Because Tor facilitates anonymous browsing by bouncing your traffic through volunteers' computers and servers in various parts of the world, it will definitely be slower than using other web browsers on your computer.

**Definitions**: 

- **Bridge Relay**: A Bridge Relay is a **Tor** server that is not publicly announced. If you choose to use a bridge, the server can provide you with access to the **Tor** network even if **Tor** is blocked in your country.

- **Port:** In this chapter, a port is an access point through which software communicates with services running on other networked computers. If a URL, such as **www.google.com**, gives you the 'street address' of a service, then the port tells you which 'door' to use once you reach the correct destination. When browsing the Web, you typically use port 80 for unsecured sites (**http://mail.google.com**) and port 443 for secured ones (**https://mail.google.com**).

- **Proxy:** A proxy is a software intermediary that runs on your computer, on your local network, or somewhere else on the Internet, that helps to relay your communication toward its final destination.

- **Route:** A route is the communication path on the Internet between your computer and the destination server.

# 2. Extract the Tor Browser

The **Tor Browser** is a modified version of **Firefox** that will provide you with all you need to browse the Internet anonymously. This package requires no installation; it simply has to be extracted and run.

To extract the **Tor Browser**, perform the following steps:

**Step 1**. **Double click** ![](/sites/siabnext.ttc.io/files/media/torbrowser-win-001.png); the *Open File - Security Warning* dialog box may appear. If it does, **click** ![](/sites/siabnext.ttc.io/files/media/torbrowser-win-002.png) to activate the program.
The language selection screen will appear next:

![](/sites/siabnext.ttc.io/files/media/torbrowser-win-003.png)

*Figure 1: The language selection screen*

**Choose** the language from the pull-down menu and **click** OK button to activate window below.

**Step 2**: Choose the location to extract the **Tor Browser**.

**Note**: The **Tor Browser** does not automatically install itself in *C:\Program Files* directory path (unlike the majority of the installation procedures for our recommended tools) but instead creates a folder on your *Desktop*.

**Important**: You may also extract and use the **Tor Browser** to a different folder on your computer or to a USB memory stick. This may help you to conceal the fact that you are using **Tor** on your computer.

Either **click** ![](/sites/siabnext.ttc.io/files/media/torbrowser-win-004.png) to accept the default *Desktop* folder and activate window below. Or **click** ![](/sites/siabnext.ttc.io/files/media/torbrowser-win-005.png) to activate the *Browse for Folder* window and navigate to the desired folder path for extracting the **Tor Browser**.

![](/sites/siabnext.ttc.io/files/media/torbrowser-win-008.png)

*Figure 2: An example of the default extraction path for the Tor Browser*

**Step 3**. **Click** ![](/sites/siabnext.ttc.io/files/media/torbrowser-win-004.png) to begin extracting the **Tor Browser**. Once completed you will be presented with a screen confirming the **Tor Browser** is installed and optionally to start it.

![](/sites/siabnext.ttc.io/files/media/torbrowser-win-009.png)

*Figure 4: The extracting process has completed successfully*

Note that the option *Run Tor Browser* is selected on the screen above. Once you **click** on *Finish* button **Tor Browser** will start automatically. 

In this example, after the extraction process has been completed, the **Tor Browser** will appear on your *Desktop* in a folder called *Tor Browser*. To use the *Tor Browser* at any time just **double click** on ![](/sites/siabnext.ttc.io/files/media/torbrowser-win-010.png) in this folder.

![](/sites/siabnext.ttc.io/files/media/torbrowser-win-011.png) 

*Figure 5: The Tor Browser extracted to a directory on the Desktop*

You have now successfully extracted the **Tor Browser**.

# 3. Configure the Tor Browser





## 3.1 How to Connect to the Tor Network

The first time that you start the **Tor Browser** you will be prompted to choose how it will access the Internet:

- [Direct Access](#826):  This option should be selected if your access to the Internet is not restricted and if the use of **Tor** **is not** blocked, banned or monitored where you are.

- [Restricted Access](#827): This option should be selected if your access to the internet is restricted or if the use of **Tor** **is** blocked, banned or monitored where you are.

These settings can be changed at any stage from within the **Tor Browser** without having to re-install the software. This may need to be done if situations in your location change or if you are visiting a different country.

Any subsequent time that you start the **Tor Browser** it will connect you to the **Tor** network with no additional configuration required. 


<a name="3.1.1"></a>

### 3.1.1 Connect to the Tor Network - Direct Access

To configure the **Tor Browser** to access the **Tor** network directly, perform the following steps:

**Step 1**: **Navigate** to the *Tor Browser* folder, and then **double click** ![](/sites/siabnext.ttc.io/files/media/torbrowser-win-010.png) to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/torbrowser-win-012.png)

*Figure 1: The Tor Network Settings panel*


**Step 2**: **Click** the ![](/sites/siabnext.ttc.io/files/media/torbrowser-win-013.png) button, which will open the **Tor Status** window that shows you the progress as the software connects to the **Tor Network**.

![](/sites/siabnext.ttc.io/files/media/torbrowser-win-014.png)

*Figure 2: The Tor Status windows, showing the connection progress*

A few moments later, the **Tor Browser** will activate a new browser window displaying the following screen:

![](/sites/siabnext.ttc.io/files/media/torbrowser-win-015.png)

*Figure 3: Tor Browser; successfully connected to the Tor network*

You can now browse the web with the protection of the *Tor network*.

**Note**: Every time you launch the **Tor Browser**, it will automatically open the *Tor Status* window (*Figure 2*) before starting the *Tor Browser* (*Figure 3*).


<a name="3.1.2"></a>

### 3.1.2 Connect to the Tor Network - Restricted Access

If you live in an area where accessing the Tor Network directly, as described above, is not possible or risky, you can configure Tor to try and circumvent the obstacles that are in place.

**Step 1**: **Navigate** to the *Tor Browser* folder, and then **double click** ![](/sites/siabnext.ttc.io/files/media/torbrowser-win-010.png) to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/torbrowser-win-012.png)

*Figure 4: The Tor Network Settings panel*

**Step 2**: **Click** the ![](/sites/siabnext.ttc.io/files/media/torbrowser-win-016.png) button which will open a new window. You will be asked three short configuration questions to help you access the **Tor Network**.

**Question 1:** *Proxy Access;*  If you need to access the Internet via a proxy check **yes** and then press ![](/sites/siabnext.ttc.io/files/media/torbrowser-win-017.png). If you do not use a proxy check **no** and then press ![](/sites/siabnext.ttc.io/files/media/torbrowser-win-017.png).

If you selected **yes** above, fill in your proxy settings on the following screen. If you do not know your proxy settings, check your regular browser settings. In **Firefox** you can find them in *Options* > *Advanced* > *Network* tab in *Connection* *Settings* section. In other browsers you may look for *Internet Options*. Use the *Help* feature within your browser for further assistance.

![](/sites/siabnext.ttc.io/files/media/torbrowser-win-018.png)

*Figure 5: Proxy settings screen*

**Question 2:** *Restricted Ports;* If you are accessing the Internet through a firewall that only allows access over certain ports, for example *port 80 or 443* for web browsing, select **yes** and press ![](/sites/siabnext.ttc.io/files/media/torbrowser-win-017.png) to configure the ports, otherwise select **no** and press ![](/sites/siabnext.ttc.io/files/media/torbrowser-win-017.png). 

![](/sites/siabnext.ttc.io/files/media/torbrowser-win-019.png)

*Figure 6: Port restriction configuration screen*

**Question 3:** *Censored Internet connection*; If you live in a country which is actively blocking or monitoring **Tor** traffic you can configure the **Tor Browser** to use a *Bridge* which will disguise the fact that you are using **Tor**. 

Once you have clicked ![](/sites/siabnext.ttc.io/files/media/torbrowser-win-017.png) after *question 2* you will be presented with a screen allowing you to paste in **Bridge addresses**. See the section [Getting Bridge Addresses](#829) for instructions on obtaining bridge addresses.

![](/sites/siabnext.ttc.io/files/media/torbrowser-win-020.png)

*Figure 7: Tor Bridge configuration screen*

Once you have added the **bridge addresses** click ![](/sites/siabnext.ttc.io/files/media/torbrowser-win-021.png) to finish your configuration and connect to the **Tor Network**.

![](/sites/siabnext.ttc.io/files/media/torbrowser-win-014.png)

*Figure 8: The Tor Status windows, showing the connection progress*

A few moments later, the **Tor Browser** will activate a new browser window displaying the following screen:

![](/sites/siabnext.ttc.io/files/media/torbrowser-win-015.png)

*Figure 9: Tor Browser; successfully connected to the Tor network*

You can now browse the web with the protection of the *Tor network*.

**Note**: Every time you launch the **Tor Browser**, it will automatically open the *Tor Status* window (*Figure 8*) before starting the *Tor Browser* (*Figure 9*).

## 3.2 Reconfigure access to the Tor Network

At any stage, if you need to access the **Tor Network** a different way, for example if you have travelled to a country that blocks Tor, you can update your settings from within the browser. Click on the ![](/sites/siabnext.ttc.io/files/media/torbrowser-win-022.png) icon and select *Open Network Settings*.

![](/sites/siabnext.ttc.io/files/media/torbrowser-win-023.png)

*Figure 10: Tor Browser options*

You will be presented with a new window (*Figure 11*) that will allow you to change how the **Tor Browser** accesses the Internet. Tick the options you want and change their settings.  Once satisfied with the changes press ![](/sites/siabnext.ttc.io/files/media/torbrowser-win-024.png) and restart the **Tor Browser**.


![](/sites/siabnext.ttc.io/files/media/torbrowser-win-025.png)

*Figure 11: Tor Browser options*


<a name="3.3"></a>

## 3.3 Getting Bridge Addresses

In order to configure the **Tor Browser** to use **Bridges** you will need to get bridge addresses.  There are two main ways this can be done:

**Email**:

To get bridges by email, you will need either a Gmail or a Yahoo email account.  Send an email to  bridges@bridges.torproject.org with the subject *get bridges*.  After a few minutes you will receive an email with 3 bridges listed and some additional details.

![](/sites/siabnext.ttc.io/files/media/torbrowser-win-026.png)

*Figure 12: Email with bridges listed*

**Web Site**

If your access is not completely restricted you may be able to get **Bridge** addresses from the Tor website by visiting [https://bridges.torproject.org/](https://bridges.torproject.org/)

After opening the website you will need to perform three steps:

- Click on ![](/sites/siabnext.ttc.io/files/media/torbrowser-win-027.png)

- Click on ![](/sites/siabnext.ttc.io/files/media/torbrowser-win-028.png)

- Fill out the *captcha* and press ![](/sites/siabnext.ttc.io/files/media/torbrowser-win-029.png)

Once you have entered the *captcha* correctly you will be presented with three **Bridge** addresses.

![](/sites/siabnext.ttc.io/files/media/torbrowser-win-030.png)

*Figure 13: Bridge addresses received via the Tor Project website*


**Note**: The *Bridge Database* is designed to prevent anyone from easily learning all of the bridge addresses. At first, it appears to give you the same bridges each time. After a period time, however, it will eventually provide new addresses. 

After you received the bridge addresses copy them to the field in the window as in *Figure 7: Tor Bridge configuration screen* or *Figure 11: Tor Browser options*.

# 4. Access the Web Anonymously Using the Tor Browser

The **Tor Browser** is designed to be very easy to use, in fact if you are familiar with using a web browser you will be able to use the **Tor Browser** as it is a version of **Firefox** modified for additional privacy and security. 

**Note:** as the **Tor Browser** is designed with privacy in mind, it is configured not to save any information to your hard drive or USB stick.  This means that when you quit the **Tor Browser** all your browsing history is forgotten.

<a name="4.1"></a>

## 4.1 Check to Make Sure the Tor Browser is Working

As with any circumvention software it is recommended to perform simple independent tests to ensure the **Tor Browser** works, by going to any website that will try to identify where are you based from the IP address we visit the site from.

There are a number of free website that do this, such as: [check.torproject.org](https://check.torproject.org), [iplocation.net](http://www.iplocation.net/), [ip2location.com](http://www.ip2location.com/), [whatismyipaddress.com](http://whatismyipaddress.com/), etc. If you access these website directly without using **Tor Browser** or other circumvention tool it should display your real IP address and provide a more or less accurate physical location for you. However if you access those websites using **Tor Browser** or other circumvention tool the location and IP address you will see should be different.

![](/sites/siabnext.ttc.io/files/media/torbrowser-win-031.png)

*Figure 1: Firefox (top) & The Tor Browser (bottom) on the same computer showing Tor status and IP address differences*

<a name="4.2"></a>

## 4.2 Create a New Identity

You can create a *new identity* for your Browser.  This means that new set of random **Tor** proxy servers will be selected for you to use. This will make you appear to come from a new location to the web servers. To do this, click on ![](/sites/siabnext.ttc.io/files/media/torbrowser-win-022.png) and select *New Identity* from the menu.  The *Tor Browser* will briefly close, clearing your *browsing history* and *cookies* and then restart. Once they browser has restarted you can check your new location as described above in section 4.1.

![](/sites/siabnext.ttc.io/files/media/torbrowser-win-032.png)

*Figure 2: Selecting New Identity from TorButton menu*

<a name="4.3"></a>

## 4.3 Enable the NoScript add-on

**Tor Browser** comes with the **NoScript** add-on pre-installed. **NoScript** can additionally protect you from malicious websites and from leaking your real identity through execution of scripts in your **Tor Browser**, however **NoScript** is disabled by default in **Tor Browser** so this additional protection is not readily available. 

If you wish to enable the extra protections afforded by **NoScript**, it can be turned on by opening the **NoScript** menu and clicking *Forbid Scripts Globally* and then configuring the various *options* it provides. 

We recommend that you read more about [**NoScript** in the **FireFox** chapter](../firefox/windows#801). 

![](/sites/siabnext.ttc.io/files/media/torbrowser-win-033.png)

*Figure 3: Enabling NoScript by selecting Forbid Scripts Globally (advised) option*

<a name="4.4"></a>

## 4.4 Keep the Tor Browser Up-To-Date

In **[How-to Booklet chapter 1.4](../malware#392)** we explain how important is keeping your software up to date, the **Tor Browser** is no exception.  When updates are available, the next time you start the **Tor Browser** you will be presented with a notice that your browser is out of date (*Figure 4*) and instructed to click and choose **Download Tor Browser Update**. You will be brought to the **Tor Project** website where you can get the latest release.  Once downloaded you can follow this guide to install the updated **Tor Browser**.


![](/sites/siabnext.ttc.io/files/media/torbrowser-win-034.png)

*Figure 4: Tor Browser showing an update is available*

# FAQ

***Q***: Why should I use the **Tor Browser**?

***A***: The **Tor Browser** is a useful tool if you need to circumvent Internet censorship in order to access certain websites. It's also useful if you don't want your Internet Service Provider (ISP) to know what websites you're visiting, or if you don't want those websites to know your location on the Internet.

***Q***: When I run the **Tor Browser**, do all of my other programs communicate anonymously through the Tor network?

***A***: No, it is important to remember that, by default, the **Tor Browser** only sends its own traffic through Tor network. Your other programs communicate directly with service providers on the Internet. You can verify that you are communicating over the Tor network by loading the *Tor Check* page at **https://check.torproject.org**. Tor also assumes that you will exercise of caution, common sense and good judgement when browsing new or unfamiliar websites.

***Q***: Is my **Tor Browser** traffic encrypted?

***A***: Tor will encrypt all of your communication *within* the Tor network. Keep in mind, however, that *Tor cannot encrypt your traffic after it leaves the Tor network.*  To protect the data you send and receive between your Tor *exit node* and the website with which you are communicating, *you are still relying on HTTPS*.

- [**The *Tor Project* FAQ**](https://www.torproject.org/docs/faq.html.en)
- [**The *Tor Project* help desk**](https://www.torproject.org/about/contact.html.en#support)
