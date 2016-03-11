

---

lang: en
community: guide
type: tools
os: os-x
weight: 080
title: Tor Browser for Mac OS X - Online anonymity and circumvention

---

The **Tor Browser** keeps your online activities private. It disguises your identity and protects your Web traffic from many forms of Internet surveillance. **Tor** can also be used to bypass Internet filters.

# Required reading


{{ required_reading: ../../anonymity and circumvention }}


{{ tool: ./080-tool.md }}

# What you will get from this guide

- The ability to conceal your digital identity from the websites that you visit
- The ability to conceal your traffic from [**Internet Service Providers (ISPs)**](/en/glossary#ISP) and basic surveillance tools
- The ability to bypass Internet censorship and filtering rules
- Protection from insecure and potentially malicious websites through the *HTTPS Everywhere* and *NoScript* browser add-ons

# 1. Introduction to the Tor Browser

**Note:** If you are in a location where access to the **Tor Project** website is blocked, you can use email to request a download link that is more likely to work. Just send an email to **gettor@torproject.org** with the version you need (**Windows**, **OSX** or **Linux**) in the body of the message. You will receive a response that includes a link to the **Tor Browser** archive via **Dropbox**, **Google Docs** or **Github**. Further details about this feature are available on the [Tor Project website](https://www.torproject.org/projects/gettor.html).

## 1.1 Things you should know about the Tor Browser before you start

The [Tor Browser](https://www.torproject.org/projects/torbrowser.html.en) operates on the [Tor network](https://www.torproject.org), which runs on Free and Open Source Software (FLOSS) and which is designed to enable *online anonymity* and *censorship circumvention*. 

The Tor software bounces your communications around a distributed network of relays run by volunteers throughout the world, which makes your traffic appear to come from a different [*IP address*], often in a different country. As a result, Tor hides your *IP address* from the websites you access while also hiding the websites you access from third parties who might be monitoring your traffic. Tor is designed in such a way that not even the Tor relays themselves can know *both* your location on the Internet *and* the websites you visit.

Tor also takes steps to encrypt communications into and throughout its network. However, this protection does not extend all the way to websites that are accessible through unencrypted channels (that is, websites that do *not* support HTTPS). 

Because the **Tor Browser** hides the connection between you and the websites you visit, it allows you to browse the Web anonymously and avoid online tracking. It it also useful for circumventing online filters so that you can access content from (or publish content to) websites that would otherwise be restricted.

**Note:** There is a trade-off between anonymity and speed. Tor provides anonymity by bouncing your traffic through volunteer servers in various parts of the world, it will almost always be slower than a direct connection to the Internet.

**Definitions:**

* **Bridge Relay:** A Bridge Relay is a Tor server that is not publicly advertised. If you use a bridge, it can provide you with access to the Tor network even if Tor is blocked in your country.

* **Port:** A port is an access point through which software communicates with services running on other networked computers. If a URL (such as www.securityinabox.org, gives you the 'street address' of a service, then the port tells you which 'door' to use once you reach the correct destination. Port 80 is typically used for HTTP websites that do not support encryption, and port 443 is used for secure websites that support HTTPS. 

* **Proxy:** A proxy is a software intermediary that runs on your computer, on your local network, or somewhere else on the Internet, that helps to relay your communication toward its final destination. 

* **Route:** A route is the communication path on the internet between your computer and the destination server.

## 1.2 Other Tools Like the Tor Browser

**GNU Linux, Mac OS X, and other Microsoft Windows Compatible Programs**:

The **Tor Browser** is available for **Mac OS X**, **GNU Linux**, **Microsoft Windows** and **Android** operating systems. **Tor** is the most recommended and rigorously tested tool for keeping your online activities anonymous. But we would like to list some other recommended solutions here:


* [**Riseup VPN**](https://help.riseup.net/en/riseup-vpn/) is a free **Virtual Private Network** (**VPN**) proxy server for **Linux**, **Mac OS X**, **Android** and **Microsoft Windows**.
* [**Psiphon3**](http://www.psiphon3.com/) is a free commercial **Virtual Private Network** (**VPN**) solution for **Microsoft Windows** and **Android**.
* [**Lantern**](https://getlantern.org/) is a free and open source circumvention tool for **Linux**, **Mac OS X** and **Windows**.

# 2. Download and install the Tor Browser





## 2.1 Download the Tor Browser

**Step 1**. Download the **Tor Browser** for **Mac OS X** using one of two options.

**Option 1**. **Go to** the [Tor download page](https://www.torproject.org/download/download-easy.html.en). Make sure you're actually on the secure version of the **https://www.torproject.org/download/download-easy.html.en** website before downloading anything. (The **'https'** part encrypts the connection between your browser and the website, thus making it harder for an attacker to modify the file you're going to download.)

The link above goes to Tor’s ‘easy download’ page, which is designed to identify the operating system you’re using and present you with the correct version of **Tor Browser** for your computer: *Tor Browser for Mac*. **Click [Download]** to begin the file download.

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-101-download.png)

*Figure 1: Tor Browser ‘Easy’ Download Page*

**Option 2**. If you are in a location where access to the *Tor Project* website is blocked, you can request a copy of the **Tor Browser Bundle** installer via email.  To do this, send an email to **gettor@torproject.org** with the version of Tor you want in the body of the email (e.g., **Windows** if you have a Windows computer, **OSX** if you use an Mac Computer, or **Linux** if you use a Linux-based computer). 

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-102-gettorrequest.png)

*Figure 2: Emailed request to gettor@torproject.org for the OS X version of Tor Browser*

You will receive a reply to your email with a link to download the installer via several locations online. Further details about this feature are available on the [Tor Project website](https://www.torproject.org/projects/gettor.html).

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-103-gettoresponse.png)

*Figure 3: Email response from gettor@torproject.org with Tor Browser download links for Mac OS X*

## 2.2 Install the Tor Browser

The **Tor Browser** is a modified version of **Firefox** that is pre-configured to send all of its traffic through the *Tor Network*. When you launch the **Tor Browser**, it will automatically start Tor before displaying a browser window. The Tor Browser incorporates many additional privacy- and anonymity-related features, and is by far the safest way to use Tor.  
 
To install the **Tor Browser**, follow the steps below: 

**Step 1**. **Navigate** to the folder in which you saved the **Tor Browser** package (a .dmg file beginning with ‘Tor Browser). In this example, we assume you saved file in your *Downloads* file.

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-201-desktop.png)

*Figure 1: The Downloads folder containing the Tor Browser .dmg  file*

**Step 2**. **Double-click** the **Tor Browser** .dmg file to mount it as a disk image. It should show up as in a new window (*Figure 2*, below) and under *Devices* in the left-hand sidebar of a normal *Finder* window.

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-202-mounted-dmg.png)

*Figure 2: Inside the mounted Tor Browser disk image*

**Step 3**. Drag the **TorBrowser.app** into your *Applications* folder.

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-203-drag-app.png)

*Figure 3: Dragging the mounted TorBrowser.app into the Applications folder*

It should then copy over into *Applications*.

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-204-copy-app.png)

*Figure 4: Progress window for copying TorBrowser.app into the Applications folder*

**Step 4**. Before we start using **TorBrowser**, we should **unmount** (or **'eject'**) the **TorBrowser** disk image. Find *Tor Browser* under *Devices* in the *Finder sidebar*. **Click** on the {**eject**} icon next to it in the sidebar to **unmount** the disk image.

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-205-eject.png)

*Figure 5: Unmounting (or ejecting) the TorBrowser disk image*

# 3. Configuring the Tor Browser’s connection to the Tor Network

The first time you launch the **Tor Browser**, it will ask you how it should connect to the Internet: 

* **Direct Access:** Select this option if your access to the Internet is unrestricted and if the use of Tor is not blocked, banned, or monitored where you are located. 

* **Restricted Access:** Select this option if your access to the Internet is restricted or if the use of Tor is blocked, banned, or monitored where you are located. 

After you initially configure and launch the **Tor Browser**, it will continue to connect to the Tor network with no additional configuration. But you can change these settings at any time from within the **Tor Browser**. You may need to change them when you are traveling, or if the situation changes in your country. To do so, see [Section 3.3](#2348), *How to reconfigure access to the Tor network*.

## 3.1 How to connect to the Tor network - Direct Access

If access to the Internet (and to the Tor Network) are not restricted in your location, perform the following steps to configure the **Tor Browser**: 

**Step 1**. **Navigate** to the **Tor Browser** in your *Applications* folder.

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-301-open-tor-browser.png)

*Figure 1: The Tor Browser in the Applications folder*

**Step 2**. **Double-click** the **Tor Browser** app. 

**Step 3**. Depending on your security settings in *System Preferences*, you may now see a notification (*Figure 2*) telling you that **Tor Browser** is from an *’unidentified developer’*. 

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-302-open-gatekeeper.png)

*Figure 2: OS X’s ‘Gatekeeper’ alert reporting that the Tor Browser is from an ‘unidentified developer’*

We now must ‘approve’ the **Tor Browser** in *System Preferences* in order to use it.

**Step 4**. **Open** *System Preferences* by **clicking** on the Apple icon in the top-level menu and **scrolling** down to **select** *System Preferences*. 

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-303-open-sys-prefs.png)

*Figure 3: Navigating to System Preferences*

**Step 5**. **Click** on *Security & Privacy* in the top row of *System Preferences*.

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-304-sys-prefs-main.png)

*Figure 4: System Preferences*

**Step 6**. In the *Security & Privacy* section of *System Preferences*, you should see your [*Gatekeeper*](https://en.wikipedia.org/wiki/Gatekeeper\_(OS\_X)) settings in the bottom half of the window. (See *Figure 5* below.) *Mac OS X Gatekeeper* restricts which applications you can install on your device.

If your settings are set to only allow apps from the first option, *Mac App Store*, or the second option *Mac App Store and ‘identified developers’*, you need to give your system permission to install the **Tor Browser**. 

Since we’ve tried to open the **Tor Browser**, there should now be a **[Open Anyway]** button after the statement *’“TorBrowser.app” was blocked from opening because it is not from an identified developer.’* In order to make changes, **click** the lock in the bottom corner.

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-305-locked-security-prefs.png)

*Figure 5: The Security & Privacy section of System Preferences*

**Note**: In order to be considered an *’identified developer’* by *Mac OS X*, developers need to [pay annual fees] to Apple. Many developers, especially those working on [Free and Open Source Software (FOSS)] projects, choose not to do this on principle and because of the costs involved. Keep this in mind when installing other FOSS security and privacy tools for *Mac OS X*.

**Step 7**. **Enter** the user name and password for an account with administrative privileges, then **click [Unlock]**. 

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-306-unlock-security-prefs.png)

*Figure 6: 'Unlocking’ Security & Privacy preferences*

**Step 8**. Back in *Security & Privacy* settings, you’ll now be able to **click** the **[Open Anyway]** button in order to open and use the **Tor Browser**.

**Note**: Doing this doesn’t change your *Gatekeeper* settings for future applications you download. It only provides permission for the operating system to open and run **Tor Browser** now and in the future.

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-307-open-anyway.png)

*Figure 7: The ’unlocked’ Security & Privacy section of System Preferences*

**Step 8**: Return to you your *Applications* folder and **double-click** the **Tor Browser** to open it. One final alert will pop up to ask you if you’re sure you want to open *”TorBrowser.app”*. **Click** **[Open]**.

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-308-confirm-open.png)

*Figure 8: Final confirmation prompt*

**Step 9**. You should now see the *Tor Network Settings* window. For **Direct Access** to the Tor Network, **click** **[Connect]**.

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-309-network-settings.png)

*Figure 9: The Tor Network Settings screen*

**Step 10**. To connect directly to the Tor network, **click** **[Connect]**. 

The **Tor Browser** will now establish a circuit for you within the Tor network. This may take a while the first time you run the **Tor Browser**. There will be a progress bar as this runs.

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-310-establishing-circuit.png)

*Figure 10: Establishing a Tor circuit when connecting to the Tor network*

**Step 11**. After a few moments, the **Tor Browser** will open.

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-311-first-launch.png)

*Figure 11: The Tor Browser*

From here, **go to** [Section 4](#2349) to learn how to to use the **Tor Browser** to access websites safely and anonymously.

## 3.2 How to connect to the Tor network - Restricted Access

If you are located in an area where accessing the Tor network directly, as described above, is not possible or risky, you can configure Tor to try and circumvent the obstacles that are in place. 

[**Bridges**] are designed for this purpose. Bridges are Tor relays that are not publicly listed in the main Tor directory. Many [Internet Service Providers (ISPs)] filter connections to known Tor relays and bridges that they discover, but they are not able to block *all* the bridges – especially those that support [**pluggable transports**]. (**Pluggable transports**  ‘obfuscate’ connections to the Tor network by making Tor traffic look like other kinds of ’innocent-looking’ traffic online. This makes it harder to identify and filter access to the Tor network.)

If you suspect that your access to the Tor network is being blocked, you may want to use bridges with **pluggable transports**. You can choose to connect to the Tor network either with **provided bridges** (bridges that are preconfigured and provided with the **Tor Browser**) or with **custom bridges** that you have requested directly from the Tor Project. 

### 3.2.1 How to connect to the Tor network with provided bridges

You can use **provided bridges** to connect to the Tor network by performing the following steps:

**Step 1**. **Access** *Tor Network Settings* one of two ways. 

If this is the first time you’ve run the **Tor Browser** on your device, it will be the first window displayed. 

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-309-network-settings.png)

*Figure 1: Tor Network Settings*

If you’ve already run **Tor Browser**, when you next open and run the **Tor Browser**, you can access these settings by **clicking** the **[Open Settings}** button in the *Tor Status* window.

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-312-tor-status.png)

*Figure 2: The Tor Status window*

**Step 2:** In *Tor Network Settings*, **click** the **[Configure]** button.

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-309-network-settings.png)

*Figure 3: Tor Network Settings*

**Step 3:** **Select** **Yes**, then click **[Continue]**.

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-313-tor-bridges-config-1.png)

*Figure 4: The first bridges configuration screen*

**Step 4**. **Select** *Connect with provided bridges* and **click** **[Next]**.

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-314-tor-bridges-config-2.png)

*Figure 5: The second bridges configuration screen*

**Step 5**. The **Tor Browser** will now ask if you need to use a *local proxy* to access the Internet. The steps below assume that you do not. 

**Tip**: If you *do*, you can check your regular browser settings and copy over your proxy configuration. (In **Firefox** you can find these settings under *Preferences > Advanced > Network > Connection Settings*. In other browsers you may find them under *Internet Options*. You can also use the *Help* feature within your browser for further assistance. 

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-315-local-proxy-config.png)

*Figure 6: The proxy configuration screen*

**Step 6**. **Select** **No**, then **click [Connect]** to launch the **Tor Browser**.

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-316-tor-connecting.png)

*Figure 7: Connecting to the Tor network*

After a few moments, the main **Tor Browser** window will open.

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-311-first-launch.png)

*Figure 8: The Tor Browser*

From here, **go to** [Section 4](#2349) to learn how to to use the **Tor Browser** to access websites safely and anonymously. 

### 3.2.2 How to connect to the Tor network with custom bridges

If necessary, you can obtain **custom bridges** to connect to the Tor network. These bridges are used less than **provided bridges**, which makes them less likely to be filtered by [Internet Service Providers (ISPs)]. You can obtain **custom bridges** directly from [the Tor website] or you can request and recieve bridges via email. 

If your access is not *completely* restricted, you may be able to access Tor’s *BridgeDB* page at **https://bridges.torproject.org/** to get bridge addresses by following the steps felow: 

**Step 1**. **Go** to **https://bridges.torproject.org/**.

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-317-bridges-torproject.png)

*Figure 1: Tor’s [BridgeDB](https://bridges.torproject.org/) website*

**Step 2**. **Click** *Get bridges* in *Step 2*.

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-318-get-bridges.png)

*Figure 2: The [‘Get Bridges!’](https://bridges.torproject.org/options) page on Tor’s [BridgeDB](https://bridges.torproject.org/) website*

**Step 3**. **Click** *Just give me bridges!*

**Step 4**. Fill in the captcha and press **enter**.

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-319-getbridges-captcha.png)

*Figure 3: The [‘Get Bridges!’](https://bridges.torproject.org/options) captcha*

This should display three bridge addresses. 

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-320-bridge-lines.png)

*Figure 4: Three custom bridge lines from Tor’s [BridgeDB](https://bridges.torproject.org/) website*

Alternatively, you can get bridge addresses by sending an email to **bridges@torproject.org** from a **Riseup**, **Gmail** or **Yahoo** email account. 

To request basic, ‘vanilla’ bridges, include *get bridges* in the body of the email. You will receive three **custom bridges** in response.

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-321-emailed-bridges.png)

*Figure 5: Three custom bridge lines sent from bridges@torproject.org in response to an emailed request*


Once you have your custom bridge addresses, you can use them to connect to the Tor network by following the steps below:

**Step 5**. **Access** *Tor Network Settings* one of two ways. 

If this is the first time you’ve run the **Tor Browser** on your device, it will be the first window displayed. 

If you’ve already run **Tor Browser**, when you next open and run the **Tor Browser**, you can access these settings by **clicking** the **[Open Settings}** button in the *Tor Status* window.

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-312-tor-status.png)

*Figure 6: The Tor Status window*

**Step 6**. In *Tor Network Settings*, **click [Configure]**.

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-309-network-settings.png)

*Figure 7: Tor Network Settings*

**Step 7**. On the first *Tor Bridges Configuration* screen, **Select** **Yes**, then **click [Continue]**.

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-313-tor-bridges-config-1.png)

*Figure 8: The first Tor Bridges Configuration screen*

**Step 8**. On the second *Tor Bridges Configuration* screen, Select **Enter custom bridges**. Then add one or more of your *custom bridge* addresses to the field below.

 ![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-322-enter-bridges.png) 

*Figure 9: Entering custom bridge addresses on the second Tor Bridges Configuration screen*

**Step 9**. **Click [Continue]** to display the *local proxy configuration* screen

The **Tor Browser** will now ask if you need to use a *local proxy* to access the Internet. The steps below assume that you do not. 

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-315-local-proxy-config.png)

*Figure 10: The proxy configuration screen*

**Tip**: If you *do*, you can check your regular browser settings and copy over your proxy configuration. (In **Firefox** you can find these settings under *Preferences > Advanced > Network > Connection Settings*. In other browsers you may find them under *Internet Options*. You can also use the *Help* feature within your browser for further assistance. 

**Step 10**. **Select** **No** on the *Local Proxy Configuration* screen. Then **click** **[Connect]** to launch the **Tor Browser**.

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-316-tor-connecting.png)

*Figure 11: Connecting to the Tor network*

After a few moments, the main **Tor Browser** window will open.

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-311-first-launch.png)

*Figure 12: The Tor Browser*

From here, **go to** [Section 4](#2349) to learn how to to use the **Tor Browser** to access websites safely and anonymously. 

## 3.3 How to reconfigure access to the Tor network

At any stage, if you need to access the Tor Network a different way—-for example, if you have travelled to a country that blocks Tor—-you can update your *Tor Network Settings* from within the main **Tor Browser** window. 

**Step 1**. **Click** on the onion icon in your browser and select **“Tor Network Settings”**.

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-323-network-settings-via-onion.png)

*Figure 1: Accessing Tor Network Settings via the Tor Browser’s onion icon menu*

**Step 2:** You will be presented with a new window that will allow you to change how the **Tor Browser** accesses the Internet. **Select** the options you want. When satisfied with the changes, **click [OK]**. 

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-324-onionmenu-network-settings.png)

*Figure 2: Tor Network Settings*

**Step 3**. To implement your changes, restart the **Tor Browser**.

# 4. Using the Tor Browser to access the web safely and anonymously

As an up-to-date, privacy-optimised version of **Firefox**, the **Tor Browser** was designed to be very easy to use. 

**Note:** In keeping with a policy of [*privacy by design*](https://www.privacybydesign.ca/index.php/about-pbd/7-foundational-principles/), the **Tor Browser** is configured in such a way that it does not save your browsing history to your hard drive. Each time you quit the **Tor Browser**, your browsing history will be deleted. 

## 4.1. How to check if the Tor Browser is working

The **Tor Browser** hides your *IP address* from the websites you visit. If it is working properly, you should appear to be accessing websites from a location on the Internet that 

- Is different from your normal *IP address*
- Cannot be linked to your physical location

The simplest way to confirm this is by visiting the *Tor Check* website, which is located at [**https://check.torproject.org/**](https://check.torproject.org). 

When you run the **Tor Browser**, the *’Test Tor Network Settings’* link goes to the *Tor Check* website. *Tor Check* will also tell you what your new ‘exit’ *IP address* is, but it does not tell you which country that *IP address* is ‘in’. 

**Step 1**. To be sure that the **Tor Browser** is working and connecting to the *Tor Network*, **click** on the *’Test Tor Network Settings’* link. (Or you can manually type in [https://check.torproject.org/](https://check.torproject.org/).)

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-311-first-launch.png)

*Figure 1: The Tor Browser*

If you are **not** using Tor, it will display the following: 

 ![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-325-not-configured.png)

*Figure 2: [Tor Check](https://check.torproject.org/) showing that Tor is* not *working properly*
 
If you **are** using Tor, it will display the following:

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-326-configured-browser.png) 

*Figure 3: [Tor Check](https://check.torproject.org/) showing that Tor is working properly*

**Step 2**. *(**Optional**)* It is often useful to see the route your *Tor circuit* is taking through the *Tor Network*, including the country your ‘new’ *IP address* is in. 

To see the details of your current *Tor circuit*, including the country your ‘exit’ *IP address* is located in, **click** on the onion icon in the **Tor Browser** toolbar.

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-327-tor-circuit.png) 

*Figure 4: The ‘Tor circuit for this site’ feature*

**Step 3**. *(**Optional**)* If you want to check your *IP address* using a service that is not associated with the Tor Project, there are many options online. *IP address* information sites that support *https* encryption make it more difficult for someone *other* than your service provider to “fake" the information seen there. Examples of sites that support *https* include:

- [https://www.iplocation.net/](https://www.iplocation.net/)
- [https://www.ip2location.com/](https://www.ip2location.com/)

If you access these websites *without* using the Tor Browser, they should display your real *IP address*, which is linked to your physical location. If you access them through the **Tor Browser**, they should display a different *IP address*--the *IP address* where your *Tor circuit* through the *Tor Network* is ’exiting’.  

## 4.2 How to create a new identity

You can create a *new identity* for your **Tor Browser**. When you do, the **Tor Browser** will randomly select a new set of Tor relays for its *Tor Circuit*, which will make you appear to be coming from a new *IP address* when you visit websites. To do this, follow the steps below:

**Step 1**. **Click** the **onion** icon in the **Tor Browser** toolbar to open the dropdown menu.

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-401-new-identity.png)

*Figure 1: Creating a new identity in the Tor Browser*

**Step 2**. **Select** *New Identity* from the menu. 

The **Tor Browser** will show a confirmation message confirming your request for a *New Identity*. **Click [Yes]**.

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-402-new-identity-restart.png)

*Figure 2: New Identity confirmation message*

The **Tor Browser** will clear your browsing history and cookies then restart. Once it has restarted, you can confirm that you appear to be coming from a new *IP address* as described in the previous section, [How to check if the Tor Browser is working](#2363).

## 4.3 How to enable the No Script Add-on

[NoScript](http://noscript.net/) is a Firefox add-on that provides extra protection for your browser by blocking executable content from running without your permission. 

It was developed to block malicious code which might be embedded in websites from running on your computer when you access such websites. Software like Java, Java Script, Flash, Silverlight and other potentially executable content are blocked by default, protecting you from the potential exploitation of security vulnerabilities. 

While the **Tor Browser** comes with **NoScript** pre-installed, it is disabled by default. This is because **No Script** blocks *all* scripts that are not ‘whitelisted,’ and many users find it confusing at first. You can, however, configure **NoScript** to set different permissions for different websites. Once you start adding sites to your *whitelist* (i.e., your list of ‘safe’ or ‘trusted’ sites that you allow scripts to run on), it becomes much easier to deal with. 

To enable **NoScript** in the **Tor Browser**, follow the steps below: 

**Step 1**. **Click** the **[NoScript]** button  to the left of the green onion in the Tor Browser. It will have a blue ’S’ with a red exclamation point after it (to signify that currently all scripts are allowed per the **Tor Browser’s** default.

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-403-noscript-forbid-globally.png)

*Figure 1: The NoScript add-on*

**Step 2**. **Scroll** down to **select** *Forbid Scripts Globally (advised)*. After you do this, the **NoScript** icon will change to signify that you are forbidding scripts globally. It will now have a red circle with a diagonal slash over the blue ’S’, as seen in *Figure 2* below:

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-404-noscript-forbid-globally-icon.png)

*Figure 2: The NoScript button with ‘Forbid Scripts Globally’ selected*

**Step 3**. Initially, using **NoScript** to forbid scripts globally will appear to ‘break’ many of the websites you visit. But if a website fails to load properly, and you don’t consider that particular site a ‘risky’ one, you can add it to your NoScript *whitelist*.

To do this, **click** on **[NoScript]** button and select *Temporarily allow all this page* or *Temporarily allow [full URL address]*, such as *Temporarily allow https://check.torproject.org* in *Figure 3* below:

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-405-noscript-temp-allow.png)

*Figure 3: Temporarily allowing scripts for a given webpage in NoScript*

For more information about the features of **NoScript** and how to use them, you can learn more in the **NoScript** section of the [Firefox Tool Guide](../firefox/os-x#2385). 

## 4.4 How to keep the Tor Browser up-to-date

When updates for the **Tor Browser** are available, you will be presented with a notice within the main **Tor Browser** window that it is out of date *(Figure 1)*. 

**Tip:** Because updates to the **Tor Browser** are often security- and privacy-related, it’s a good idea to always keep it up to date.

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-406-out-of-date-torbrowser.png)

*Figure 1: The Tor Browser's ‘out of date’ warning*

As shown in *Figure 1*, you can update your version of Tor Browser by following the steps below: 

**Step 1**. **Click** the **green onion** button, then **scroll** down and select *Check for Tor Browser Update*.

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-407-dwnld-torbrowser-update.png)

*Figure 2: Downloading a Tor Browser update*

**Step 2**. **Select** *Download Tor Browser Update*.

The **Tor Browser** update will begin downloading.

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-408-downloading-torbrowser.png)

*Figure 3:Tor Browser download status bar*

**Step 3**. When the download is complete, it will notify you that it is ready to install. **Click [Restart Tor Browser]** to install the **Tor Browser** update.

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-409-tb-update-ready-to-install.png)

*Figure 4: Tor Browser update ready to install*

**Step 4**. When the upload is complete, the **Tor Browser** will automatically restart. The final screen of the **Tor Browser**  software update window will notify you that the update was successfully installed. **Click [OK]**.

![](/sites/securityinabox.org/files/media/torbrowser-osx-en-v01-410-tb-update-successful-install.png)

*Figure 5: Successful Tor Browser update notification*

# FAQ

***Q***: Why should I use the **Tor Browser**?

***A***: The **Tor Browser** is a useful tool if you need to circumvent Internet censorship in order to access certain websites. It's also useful if you don't want your [*Internet Service Provider (ISP)*](/en/glossary#ISP) to know what websites you're visiting, or if you don't want those websites to know your location on the Internet.

***Q***: When I run the **Tor Browser**, do all of my other programs communicate anonymously through the Tor network?

***A***: No, it is important to remember that, by default, the **Tor Browser** only sends its own traffic through Tor network. Your other programs communicate directly with service providers on the Internet. You can verify that you are communicating over the Tor network by loading the *Tor Check* page at **https://check.torproject.org**. Tor also assumes that you will exercise of caution, common sense and good judgement when browsing new or unfamiliar websites.

***Q***: Is my **Tor Browser** traffic encrypted?

***A***: Tor will encrypt all of your communication *within* the Tor network. Keep in mind, however, that *Tor cannot encrypt your traffic after it leaves the Tor network.*  To protect the data you send and receive between your Tor *exit node* and the website with which you are communicating, *you are still relying on HTTPS*.

- [**The *Tor Project* FAQ**](https://www.torproject.org/docs/faq.html.en)
- [**The *Tor Project* help desk**](https://www.torproject.org/about/contact.html.en#support)
