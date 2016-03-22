

---

lang: en
community: guide
type: tools
os: linux
weight: 080
title: Tor Browser for Linux - Online anonymity and circumvention

---

The **Tor Browser** keeps your online activities private. It disguises your identity and protects your Web traffic from many forms of Internet surveillance. **Tor** can also be used to bypass Internet filters.

# Required reading


:[Remain anonymous and bypass censorship on the Internet](../../../tactics/anonymity and circumvention)


:[Tor Browser for Linux - Online anonymity and circumvention](tor-browser-for-linux-online-anonymity-and-circumvention)

# What you will get from this guide

- The ability to conceal your digital identity from the websites that you visit
- The ability to conceal your traffic from **Internet Service Providers (ISPs)** and basic surveillance tools
- The ability to bypass Internet censorship and filtering rules
- Protection from insecure and potentially malicious websites through the *HTTPS Everywhere* and *NoScript* browser add-ons

# 1. Introduction to the Tor Browser

[Tor Browser](https://www.torproject.org/projects/torbrowser.html.en) is a modified version of Mozilla Firefox which is free and open source and which enables online anonymity and censorship circumvention. Unlike other browsers, Tor Browser:

* provides online anonymity by hiding users' IP address
* circumvents online censorship by enabling users to access blocked websites and/or webpages
* does not include default online tracking features
* does not make money out of users' data
* is supported and recommended by [some of the world's most renowned security experts](https://www.schneier.com/blog/archives/2013/09/how_to_remain_s.html)

**Note:** If you are in a location where access to the Tor Project website is blocked, you can use email to request a download link that is more likely to work. Just send an email to **gettor@torproject.org** with the version you need (**Windows**, **OSX** or **Linux**) in the body of the message. You will receive a response that includes a link to the Tor Browser archive via **Dropbox**, **Google Docs** or **Github**. Further details about this feature are available on the [Tor Project website](https://www.torproject.org/projects/gettor.html).

## 1.0 Things you should know about the Tor Browser before you start

The [Tor Browser](https://www.torproject.org/projects/torbrowser.html.en) operates on the [Tor network](https://www.torproject.org), which runs on Free and Open Source Software (FLOSS) and which is designed to enable *online anonymity* and *censorship circumvention*. 

The Tor software bounces your communications around a distributed network of relays run by volunteers throughout the world, which makes your traffic appear to come from a different *IP address*, often in a different country. As a result, Tor hides your IP address from the websites you access while also hiding the websites you access from third parties who might be monitoring your traffic. Tor is designed in such a way that not even the Tor relays themselves can know *both* your location on the Internet *and* the websites you visit.

Tor also takes steps to encrypt communications into and throughout its network. However, this protection does not extend all the way to websites that are accessible through unencrypted channels (that is, websites that do not support HTTPS).  

Because the Tor Browser hides the connection between you and the websites you visit, it allows you to browse the Web anonymously and avoid online tracking. It it also useful for circumventing online filters so that you can access content from (or publish content to) websites that would otherwise be restricted.

The following steps illustrate how the Tor network works: 

![](/sites/securityinabox.org/files/media/torproject-lin-en-v01-01.png)

*Figure 1: Step 1 of how Tor works*

![](/sites/securityinabox.org/files/media/torproject-lin-en-v01-02.png)

*Figure 2: Step 2 of how Tor works*

![](/sites/securityinabox.org/files/media/torproject-lin-en-v01-03.png)

*Figure 3: Step 3 of how Tor works*

**Note:** There is a trade-off between anonymity and speed. Tor provides anonymity by bouncing your traffic through volunteer servers in various parts of the world, it will almost always be slower than a direct connection to the Internet.

**Definitions:**

* **Bridge Relay:** A Bridge Relay is a Tor server that is not publicly advertised. If you Bridge, it can provide you with access to the Tor network even if Tor is blocked in your country.

* **Proxy:** A proxy is a software intermediary that runs on your computer, on your local network, or somewhere else on the Internet, that helps to relay your communication toward its final destination. 

* **Route:** A route is the communication path on the internet between your computer and the destination server. 

## 1.1 Other tools like the Tor Browser

**Microsoft Windows, Mac OS, GNU/Linux, Android and iOS compatible programs**:

The **Tor Browser** is available for the **GNU Linux**, **Mac OS**, **Microsoft Windows** and **Android** operating systems. **Tor** is the most rigorously tested tool for keeping your online activities anonymous. Below are a few other tools that are suitable for circumventing online censorship and protecting the confidentiality of your local traffic. Unlike **Tor**, these tools require that you trust the service provider: 

* [**RiseupVPN**](https://help.riseup.net/en/riseup-vpn/) is a free **Virtual Private Network** (**VPN**) proxy server for **Linux**, **MAC**, **Android** and **Microsoft Windows**.
* [**Psiphon**](http://www.psiphon.ca/) is a free commercial **Virtual Private Network** (**VPN**) solution for **Microsoft Windows** and **Android**.
* [**Lantern**](https://getlantern.org/) is a free and open source circumvention tool for **Linux**, **Mac OS X** and **Windows**.


# 2. Download and verify the Tor Browser

Before you download a Tor Browser package for Linux, you must determine whether you are running a **32-bit** or **64-bit** system. Before you extract it, you should verify that it is authentic.


## 2.1 Download the Tor Browser

**Step 1**. Launch the *Terminal* application

**Step 2**. Execute the following command in *Terminal*:

`uname –m`

If you are running a **32-bit** system, *Terminal* will display `i686` or `i386`. If you're running a **64-bit** system, it will display `x86_64`.

Now that you know whether you are running a 32-bit or 64-bit system, you can download the appropriate Tor Browser package.

**Step 3**. Make sure you are on the [**https://www.torproject.org**](https://www.torproject.org/download/download-easy.html.en#linux) download site. (The **“https”** indicates that the connection between your browser and the website is encrypted, which makes it harder for an attacker to modify the file that you are about to download.)

![](/sites/securityinabox.org/files/media/torbrowser-lin-en-v01-001.png) 

*Figure 1: The Tor Browser download links for Linux*

**Step 4**. **Click** the appropriate download link and save the package somewhere convenient (in your *Desktop* or *Documents* folder, for example, or on a USB storage device).

**Step 5**. **Right-click** the ***(sig)*** link, just beneath the download link you clicked in the step above, and save the resulting file to the same directory

You will need the **.asc** file from *Step 5*, above, in order to *verify* the authenticity of the Tor Browser package you downloaded in *Step 4*. That process is described in the following section.


## 2.2 (Optional) Verify the Tor Browser package

Before you extract the Tor Browser package, you should verify that it is authentic. (To learn more about *cryptographic signatures*, have a look at the [GnuPG section of the Thunderbird guide](https://securityinabox.org/en/guide/thunderbird/windows#745) and the [Tor Project's guide on verifying signatures](https://www.torproject.org/docs/verifying-signatures.html.en)). 

GnuPG comes pre-installed on many Linux systems, so you might be able to carry out a basic verification of the Tor Browser's *Open PGP signature* without installing additional software. To do this, perform the following steps:

**Step 1**. Import the *Tor Project's* signing key (**0x4E2C6E8793298290**) by launching *Terminal* and executing the following command: 

`gpg --keyserver x-hkp://pool.sks-keyservers.net --recv-keys 0x4E2C6E8793298290`

In response, *Terminal* should display the following: 

 ![](/sites/securityinabox.org/files/media/importing-key.png) 

*Figure 1:  Terminal after importing a GPG key*

**Step 2**. You can display information about this key by executing the following command in *Terminal*: 

`gpg --fingerprint 0x4E2C6E8793298290`

In response, *Terminal* should display the following: 

 ![](/sites/securityinabox.org/files/media/verifying-signatures.png)

*Figure 2: Terminal confirming that you have successfully imported a GPG key*

**Step 3**.  Using *Terminal*, enter the directory where you saved one of the two Tor Browser package files below: 

- *tor-browser-linux64-5.0.4_en-US.tar.xz* 
- *tor-browser-linux32-5.0.4_en-US.tar.xz*

This directory should should also contain one of the two signature files below: 

- *tor-browser-linux64-5.0.4_en-US.tar.xz.asc* 
- *tor-browser-linux32-5.0.4_en-US.tar.xz.asc* 

**Step 4**. From within that directory, execute one of the following commands in *Terminal* (depending on whether you downloaded the 32-bit or the 64-bit version of the Tor Browser)

- `gpg --verify ./tor-browser-linux32-5.0.4_en-US.tar.xz{.asc*,}`
- `gpg --verify ./tor-browser-linux64-5.0.4_en-US.tar.xz{.asc*,}`

In response, *Terminal* should display the following: 

 ![](/sites/securityinabox.org/files/media/file-verification.png)

*Figure 3: Signature verification*

The above verifies that the *private key* corresponding to the *public key* you imported in *Step 1* was used to generate the signature file that you downloaded in *Step 5* of the previous section (and that this signature file applies to the Tor Browser package that you downloaded in *Step 4* of the previous section). 

**Important**: As you can see, GPG displays a warning about the key used for this signature. This is because you have not actually verified the Tor Project's signing key. The best way to do this is to meet the Tor Project developers in person and ask them for the fingerprint of their signing key. For the purposes of this guide, we are relying on the fact that a well-known Tor Project GPG key (**0x4E2C6E8793298290**) was used to create a signature file that confirms the authenticity of the Tor Browser package that you downloaded. 

# 3. Extract the Tor Browser from the archive

The Tor Browser is a modified version of Firefox that is pre-configured to send all of its traffic through the *Tor Network*. When you launch the Tor Browser, it will automatically start Tor before displaying a browser window. The Tor Browser incorporates many additional privacy- and anonymity-related features, and is by far the safest way to use Tor. You do not have to install the Tor Browser as you would most software. Simply extract it — either to your hard drive or to a USB storage device — and then run it. 
 
To extract the Tor Browser, follow the steps below: 

**Step 1**. **Navigate** to the folder in which you saved the Tor Browser package.

In this section, we assume the package is on your *Desktop*

![](/sites/securityinabox.org/files/media/torbrowser-lin-en-v01-201.png)

*Figure 1: The folder containing the Tor Browser package*

**Step 2**. **Double-click** the *tor-browser-linux64-5.0.4_en-US.tar.xz* file to see the contents of the *archive* file

![](/sites/securityinabox.org/files/media/torbrowser-lin-en-v01-202.png)

*Figure 2: Inside the Tor Browser archive*

**Step 3**. **Click** the *tor-browser_en-US* folder

**Step 4**. **Click** **[Extract]** to choose a location for the Tor Browser application folder

![](/sites/securityinabox.org/files/media/torbrowser-lin-en-v01-203.png)

*Figure 3: Choosing a location for Tor Browser application folder* 

**Step 5**. **Navigate** to a location where you want to extract the Tor Browser application folder

In this section, we will extract the Tor Browser application folder to your *Desktop*

**Step 6**. **Click** **[Extract]** to extract the Tor Browser application folder

![](/sites/securityinabox.org/files/media/torbrowser-lin-en-v01-204.png)

*Figure 4: Extracting the Tor Browser*
 
**Step 7**. When the extraction process is completed, **click** **[Close]** to return to the *archive*

![](/sites/securityinabox.org/files/media/torbrowser-lin-en-v01-205.png)

*Figure 5: Inside the Tor Browser archive*

**Step 8**. Close the archive window.

You can now launch the Tor Browser. (The first time you do so, it will ask you a few configuration questions, which are covered in the following section.)

**Step 9**. **Navigate** to the **tor-browser_en-US** folder that was created when you extracted the Tor Browser package

![](/sites/securityinabox.org/files/media/torbrowser-lin-en-v01-206.png)

*Figure 6: The Tor Browser application folder*

**Step 10**. **Double-click** the **Tor Browser Setup** file to launch the Tor Browser for the first time

![](/sites/securityinabox.org/files/media/torbrowser-lin-en-v01-207.png)

*Figure 7: Inside the Tor Browser application folder before first launch*

After you launch the Tor Browser for the first time, the name of this file will change to **Tor Browser**. From now on, you can launch it by double-clicking this file.

![](/sites/securityinabox.org/files/media/torbrowser-lin-en-v01-208.png)

*Figure 8: Inside the Tor Browser application folder after first launch*

# 4. Launch and configure the Tor Browser

The first time you launch the Tor Browser, it will ask you how it should connect to the Internet: 

* **Direct Access:** Select this option if your access to the Internet is unrestricted and if the use of Tor is not blocked, banned or monitored where you are located. 

* **Restricted Access:** Select this option if your access to the Internet is restricted or if the use of Tor is blocked, banned or monitored where you are located. 

After you configure the Tor Browser on the first launch, it will remember your selection and will not ask you to configure it again. You can change the configuration any time, from within the Tor Browser. This might be necessary if you are travelling or if the situation changes in your country. To do so, see [Section 4.3](#2170), below.


## 4.1. How to connect to the Tor network - Direct Access

If access to the Internet (and to the Tor Network) are not restricted in your location, perform the following steps to configure the Tor Browser: 

**Step 1**. **Navigate** to the Tor Browser application folder

![](/sites/securityinabox.org/files/media/torbrowser-lin-en-v01-207.png)

*Figure 1: The Tor Browser application folder*

**Step 2:** **Double-click** the **Tor Browser Setup** file. This will display the Tor Browser configuration screen

 ![](/sites/securityinabox.org/files/media/tor-running-1.png)

*Figure 2: The Tor Browser configuration screen*

**Step 3:** To connect directly to the Tor network, **click** **[Connect]**. 

![](/sites/securityinabox.org/files/media/tor-running-2.png)

*Figure 3: Connecting to the Tor network*

After a few moments, the Tor Browser will open

 ![](/sites/securityinabox.org/files/media/torbrowser-lin-en-v01-010.png)

*Figure 4: The Tor Browser*

You can now browse the web with the protection of the Tor network. 

## 4.2. How to connect to the Tor network - Restricted Access

If you are connecting from a place where accessing the Tor network directly is not possible or risky, you can configure the Tor Browser to try and circumvent the obstacles that are in place. 
 
[**Bridges**](https://bridges.torproject.org/) are designed for this purpose. They are Tor relays that are not listed in the main Tor directory and which are used to circumvent censorship. Many Internet Service Providers (ISPs) filter connections to known Tor relays, but they are not able to block all the bridges – especially those with **pluggable transports** which obfuscate connections to the Tor network. 

If you suspect that your access to the Tor network is being blocked, you might want to use bridges with pluggable transports. You can choose to connect to the Tor network either with **provided bridges** or with **custom bridges** that you have requested directly from the Tor Project. 

### 4.2.1. How to connect to the Tor network with provided bridges

You can use provided bridges to connect to the Tor network by performing the following steps:

**Step 1**. **Navigate** to the Tor Browser application folder

![](/sites/securityinabox.org/files/media/torbrowser-lin-en-v01-207.png)

*Figure 1: The Tor Browser application folder*

**Step 2:** **Double-click** the **Tor Browser Setup** file. This will display the Tor Browser configuration screen.

 ![](/sites/securityinabox.org/files/media/tor-running-1.png)

*Figure 2: The Tor Browser configuration screen*

**Step 3:** If you have restricted access, **click** **Configure**. 

![](/sites/securityinabox.org/files/media/tor-bridges-config.png)

*Figure 3: The Tor Browser configuration screen*

**Step 4:** **Select** **Yes**

**Step 5.** **Click** **[Next]** to display the *bridge configuration* screen

![](/sites/securityinabox.org/files/media/provided-bridges.png)

*Figure 4: The bridge configuration screen*

**Step 6**. **Select** **Connect with provided bridges**

**Step 7**. **Click** **[Next]** to display the *local proxy configuration* screen

The Tor Browser will now ask if you need to use a *local proxy* to access the Internet. The steps below assume that you do not. If you *do*, you can check your regular browser settings and copy over your proxy configuration. (In Firefox you can find these settings in the *Options > Advanced > Network* tab of *Connection Settings*. In other browsers you might find them under *Internet Options*. You can also use the *Help* feature within your browser for further assistance. 

![](/sites/securityinabox.org/files/media/no-local-proxy.png)

*Figure 5: The proxy configuration screen*

**Step 8**. **Select** **No**

**Step 9**. **Click** **[Connect]** to launch the Tor Browser

![](/sites/securityinabox.org/files/media/tor-running-2.png)

*Figure 6: Connecting to the Tor network*

After a few moments, the Tor Browser will open

 ![](/sites/securityinabox.org/files/media/torbrowser-lin-en-v01-010.png)

*Figure 7: The Tor Browser*

You can now browse the web with the protection of the Tor network. 


### 4.2.2. How to connect to the Tor network with custom bridges

If necessary, you can obtain less commonly-used bridges through which to connect to the Tor network. You can do this directly from the Tor website or you can request for bridges via email. 

If your access is not *completely* restricted, you might be able to get bridge addresses directly from the Tor website by visiting **https://bridges.torproject.org/** and following the steps below: 

**Step 1:** **Click** *Just give me bridges!*

 ![](/sites/securityinabox.org/files/media/just-give-me-bridges.png)

**Step 2:** Fill in the captcha and press **enter**.

 ![](/sites/securityinabox.org/files/media/bridge-captcha.png)

This should display three bridge addresses. 

 ![](/sites/securityinabox.org/files/media/bridge-lines.png)

Alternatively, you can get bridge addresses by sending an email to **bridges@torproject.org**. You are required to send an email using an address from one of the following email service providers: **Riseup**, **Gmail** or **Yahoo**.  

Once you have your custom bridge addresses, you can use them to connect to the Tor network by following the steps below:

**Step 1**. **Navigate** to the Tor Browser application folder

![](/sites/securityinabox.org/files/media/torbrowser-lin-en-v01-207.png)

*Figure 1: The Tor Browser application folder*

**Step 2**. **Double-click** the **Tor Browser Setup** file. This will display the Tor Browser configuration screen

 ![](/sites/securityinabox.org/files/media/tor-running-1.png)

*Figure 2: The Tor Browser configuration screen*

**Step 3**. If you have restricted access, **click** **Configure**. 

![](/sites/securityinabox.org/files/media/tor-bridges-config.png)

*Figure 3: The Tor Browser configuration screen*

**Step 4**. **Select** **Yes**

**Step 5**. **Click** **[Next]** to display the *bridge configuration* screen

 ![](/sites/securityinabox.org/files/media/custom-bridges.png) 

*Figure 4: The bridge configuration screen*

**Step 6**. Select **Enter custom bridges** add your bridge addresses in the field above

**Step 7**. **Click** **[Next]** to display the *local proxy configuration* screen

The Tor Browser will now ask if you need to use a *local proxy* to access the Internet. The steps below assume that you do not. If you *do*, you can check your regular browser settings and copy over your proxy configuration. (In Firefox you can find these settings in the *Options > Advanced > Network* tab of *Connection Settings*. In other browsers you might find them under *Internet Options*. You can also use the *Help* feature within your browser for further assistance. 

![](/sites/securityinabox.org/files/media/no-local-proxy.png)

*Figure 5: The proxy configuration screen*

**Step 8**. **Select** **No**

**Step 9**. **Click** **[Connect]** to launch the Tor Browser

![](/sites/securityinabox.org/files/media/tor-running-2.png)

*Figure 6: Connecting to the Tor network*

After a few moments, the Tor Browser will open

 ![](/sites/securityinabox.org/files/media/torbrowser-lin-en-v01-010.png)

*Figure 7: The Tor Browser*

You can now browse the web with the protection of the Tor network. 

## 4.3. How to reconfigure access to the Tor network

At any stage, if you need to access the Tor Network a different way, for example if you have travelled to a country that blocks Tor, you can update your settings from within the browser. You can do this through the following simple steps:

**Step 1:** Click on the onion icon in your browser and select **“Tor Network Settings”**.

**Step 2:** You will be presented with a new window that will allow you to change how Tor Browser accesses the Internet. Tick the options you want and change their settings. Once satisfied with the changes, click on “OK” and restart the Tor Browser. 

 ![](/sites/securityinabox.org/files/media/tor-network-settings.png)

*Figure 1: Tor network settings*

# 5. Access the web anonymously using the Tor Browser

As an up-to-date, privacy-optimised version of **Firefox**, the **Tor Browser** was designed to be very easy to use. 

**Note:** In keeping with a policy of [*privacy by design*](https://www.privacybydesign.ca/index.php/about-pbd/7-foundational-principles/), the **Tor Browser** is configured in such a way that it does not save your browsing history to your hard drive. Each time you quit the **Tor Browser**, your browsing history will be deleted. 

## 5.1. How to check if the Tor Browser is working

The Tor Browser hides your *IP address* from the websites you visit. If it is working properly, you should appear to be accessing websites from a location on the Internet that 

- Is different from your normal IP address
- Cannot be linked to your physical location

The simplest way to confirm this is by visiting the *Tor Check* website, which is located at [**https://check.torproject.org/**](https://check.torproject.org)

If you are **not** using Tor, it will display the following: 

 ![](/sites/securityinabox.org/files/media/not-using-tor.png)

*Figure 1: Tor Check showing that Tor is not working properly*
 
If you are using Tor, it will display the following:

 ![](/sites/securityinabox.org/files/media/using-tor.png) 

*Figure 2: Tor Check showing that Tor is working properly*

If you want to check your apparent IP address using a service that is not associated with the Tor Project, there are many options online. Examples that support *https* encryption (which makes it more difficult for someone *other* than the service provider "fake" the result) include:

- [https://www.iplocation.net/](https://www.iplocation.net/)
- [https://www.ip2location.com/](https://www.ip2location.com/)

If you access these websites *without* using the Tor Browser, they should display your real IP address, which is linked to your physical location. If you access them through the Tor Browser, they should display a different IP address.  

## 5.2. How to create a new identity

You can create a "new identity" for your Tor Browser. When you do, the Tor Browser will randomly select a new set of Tor relays, which will make you appear to be coming from a different IP address when you visit websites.To do this, follow the steps below:

**Step 1**. **Click** the **green onion** menu in the Tor Browser

 ![](/sites/securityinabox.org/files/media/new-identity.png)

*Figure 1: Creating a new identity in the Tor Browser*

**Step 2**. **Select** *New Identity* from the menu. 

The Tor Browser will clear your browsing history and cookies then restart. Once the it has restarted, you can confirm that you appear to be coming from a new IP address as described in the previous section.

## 5.3. How to enable the NoScript Add-on

Tor Browser comes with the [NoScript](https://noscript.net/) add-on pre-installed. NoScript can additionally protect you from malicious websites and from leaking your real identity through execution of scripts in your Tor Browser, however NoScript is disabled by default in Tor Browser so this additional protection is not readily available.

If you wish to enable the extra protections afforded by NoScript, it can be turned on by opening the NoScript menu and clicking Forbid Scripts Globally and then configuring the various options it provides.

To enable NoScript in the Tor Browser, follow the steps below: 

**Step 1**. **Click** the **NoScript button**  to the left of the green onion in the Tor Browser

 ![](/sites/securityinabox.org/files/media/no-script.png)

*Figure 1: Enabling the NoScript add-on*

**Step 2**. **Select**  *Forbid Scripts Globally (advised)*

Initially, this will appear to "break" many of the websites you visit. If a website fails to load properly, you can add it to your NoScript *whitelist* by clicking the button shown in *Figure 1*, above, and selecting *Temporarily allow all this page*. You can learn more about NoScript in the [Firefox Tool Guide](../firefox/linux). 



## 5.4. How to keep the Tor Browser up-to-date

When updates for the Tor Browser are available, you will be presented with a notice that your browser is out of date. 

![](/sites/securityinabox.org/files/media/torbrowser-lin-en-v01-301.png)

*Figure 1: The Tor Browser's "out of date" warning*

As shown in *Figure 1*, you can update your version of Tor Browser by following the steps below: 

**Step 1**. **Click** the **green onion** button

![](/sites/securityinabox.org/files/media/torbrowser-lin-en-v01-302.png)

*Figure 2: Downloading a Tor Browser update*

**Step 2**. **Select** *Download Tor Browser Update*

This will take you to the Tor Project website, where you can get the latest release. Once you have downloaded the new Tor Browser package, you can follow the instructions in this guide to re-install it.



# FAQ

***Q***: Why should I use the **Tor Browser**?

***A***: The **Tor Browser** is a useful tool if you need to circumvent Internet censorship in order to access certain websites. It's also useful if you don't want your Internet Service Provider (ISP) to know what websites you're visiting, or if you don't want those websites to know your location on the Internet.

***Q***: When I run the **Tor Browser**, do all of my other programs communicate anonymously through the Tor network?

***A***: No, it is important to remember that, by default, the **Tor Browser** only sends its own traffic through Tor network. Your other programs communicate directly with service providers on the Internet. You can verify that you are communicating over the Tor network by loading the *Tor Check* page at **https://check.torproject.org**. Tor also assumes that you will exercise of caution, common sense and good judgement when browsing new or unfamiliar websites.

***Q***: Is my **Tor Browser** traffic encrypted?

***A***: Tor will encrypt all of your communication *within* the Tor network. Keep in mind, however, that *Tor cannot encrypt your traffic after it leaves the Tor network.*  To protect the data you send and receive between your Tor *exit node* and the website with which you are communicating, *you are still relying on HTTPS*.

- [**The *Tor Project* FAQ**](https://www.torproject.org/docs/faq.html.en)
- [**The *Tor Project* help desk**](https://www.torproject.org/about/contact.html.en#support)
