

---

lang: en
community: guide
type: tools
os: linux
weight: 075
title: Firefox and Security Add-Ons for Linux - Secure Web Browser

---

Mozilla Firefox (or simply known as Firefox) is a free and open source web browser which is enhanced by the availability of numerous add-ons for it, including some that are designed to protect your privacy and security when you browse the web.

# Required reading


:[](../../../tactics/secure communication)


:[](firefox-and-security-add-ons-for-linux-secure-web-browser)

# What you will get from this guide

- A stable and secure internet browser whose features can be enhanced by numerous add-ons.
- The ability to protect yourself from potentially dangerous programs and malicious websites.
- The ability to wipe the digital traces of your browsing activity.

# 1. Introduction to Firefox

This guide assumes that you already know how to use a web browser and will not cover the basic functions of Firefox. It will focus on security-related settings and extensions.

## 1.0 Things you should know about Firefox before you start

Firefox has many easy-to-use *add-ons* that improve your privacy and security when you browse the Web. You can choose which add-ons to install, and decide how to configure them, depending on your circumstances. If you are using a computer that is managed by someone else (at an Internet cafe, for example, or in your place of work), you might have to make these adjustments repeatedly.

In addition to basic Firefox settings, this guide covers the installation and basic configuration of the following add-ons:

* [**HTTPS Everywhere**](https://www.eff.org/https-everywhere)  
* [**Privacy Badger**](https://www.eff.org/privacybadger)
* [**NoScript**](https://noscript.net/) 
* [**Click&Clean**](http://www.hotcleaner.com/)  

The *Resources* section of Tactical Tech's [**MyShadow website**](https://myshadow.org/resources) covers additional privacy-enhancing browser add-ons.

**Important:** The overwhelming majority of malware and spyware infections originate from webpages. It is important that you always consider whether it is safe to visit unknown websites, particularly those that are sent to you by email. Before you decide to open a webpage, we recommend that you scan the web address using the following page scanners:

* [www.virustotal.com](http://www.virustotal.com/) 
* [www.onlinelinkscan.com](http://onlinelinkscan.com/) 
* [www.phishtank.com](http://www.phishtank.com/index.php) 

You can also check the reputation of a website using the scanners listed below:

* [http://safeweb.norton.com](http://safeweb.norton.com/) 
* [www.urlvoid.com](http://www.urlvoid.com/) 

## 1.1 Other tools like Firefox

**Similar tools and alternatives for other operating systems.**

The **Mozilla Firefox** Web browser is available for **GNU/Linux**, **Apple Mac OS X**, **Microsoft Windows** and other operating systems. Websites are the most common source of malware infection, so accessing them securely is vital. We recommend that you use **Mozilla Firefox** and install the add-ons covered in this guide. If you would prefer to use a program other than **Mozilla Firefox**, the alternatives below are also available for **GNU/Linux**, **Apple Mac OS X** and **Microsoft Windows**:

* [**Google Chrome**](http://www.google.com/chrome/) (and Chromium)
* [**Opera**](http://www.opera.com/)
* [**Tor Browser**](https://www.torproject.org/projects/torbrowser.html.en)

# 2. Install and configure Firefox

Many Linux distributions come with Firefox installed by default, and most have a *package management* system or *software center* that makes it easy to install and update Firefox (along with any additional software that it requires to operate).

**Tip**. Many Linux distributions include a trademark-free version of Firefox called *Iceweasel*, which is just the same tool with a different name.


## 2.1. Install or Update Firefox

You probably already have Firefox (or Iceweasel) installed. But, if you do not — or if you need to update it — you can follow the instructions in one of the sections below. *It is extremely important that you keep your Web browser up-to-date.* Firefox is easier to update if you you install it using your *package management* system or *software center*, so we recommend using one of the first two methods below. But, if you need the latest version of Firefox for some reason — or if you want to install Firefox as a *portable application* (on a USB storage device, for example) — the [Install firefox directly from the developer](#2321) section will show you how.

**Tip**: It is normally a good idea to use the most recent version of security-related software, including Web browsers. However, Linux distributions typically incorporate *security updates* for the "older" versions of Firefox in their *package management* systems and *software centers*. Because of this — and because these versions are easier to update — we generally recommend installing and updating Firefox using a *package management* system or a built-in *software center*. 




### 2.1.1 (Optional) Install or update Firefox using a commandline package manager

To install or update Firefox using a the **apt** commandline package manager that comes with many Linux distributions (including *Debian* and *Ubuntu*), follow the steps below.

**Step 1**. Open *Terminal*

**Step 2.** **Execute** the following command in *Terminal*

`sudo apt-get update`

**Step 3.** **Type** the passphrase that you use to log in to your computer and press **Enter**.

This will refresh the list of software that that your *package manager* knows how to install and update.

**Step 4.** **Execute** one of the following commands in *Terminal*

- `sudo apt-get install firefox`
- `sudo apt-get install iceweasel`


### 2.1.2 (Optional) Install or update Firefox using your "software center"

To update Firefox using a graphical *software center* application, follow the steps below:

**Tip:** The instructions in this section are based on the *Ubuntu* Linux distribution, but many other distributions include some kind of  *software center*. Some *Debian* variants also include an application called *Synaptic Package Manager*, which provides similar functionality. **If you do not find an application called *Firefox*, look for one called *Iceweasel*. As mentiond above, it is the same application with a different name.**

**Step 1**. **Launch** *Software Center*

![](/sites/securityinabox.org/files/media/firefox-lin-en-v01-220.png)

*Figure 1: The Ubuntu Software Center*

**Step 2**. **Click** in the *Search* bar

**Step 3**. **Type** "Firefox"

![](/sites/securityinabox.org/files/media/firefox-lin-en-v01-221.png)

*Figure 2: Searching for Firefox*

**Step 4**. **Click** the entry for *Firefox Web Browser*

![](/sites/securityinabox.org/files/media/firefox-lin-en-v01-222.png)

*Figure 3: Software Center showing that Firefox is already installed*

If the button on the right says **[Install]**, you can install Firefox. If it says **[Remove]**, then Firefox is already installed. Even if it is already installed, however, you should make sure it is up-to-date by following the steps below.

**Step 5**. **Launch** the *Software Updater* application that comes with your Linux distribution. (If it does not have one, refer to the [Install or update Firefox using a commandline package manager](#2319) section.) It will automatically begin refreshing the list of software that it knows how to install and update.

![](/sites/securityinabox.org/files/media/firefox-lin-en-v01-223.png)

*Figure 4: Ubuntu's Software Updater refreshing its list of software*

When it is done, it will let you know whether any of the software on your computer (including Firefox) is outdated. 

![](/sites/securityinabox.org/files/media/firefox-lin-en-v01-224.png)

*Figure 5: Ubuntu's Software Updater showing that all software is up-to-date*

If you are up-to-date, you can click **[OK]**. If any of your software needs to be updated, we recommend that you follow *Software Updater's* instructions and update *everything*. You should then restart your computer as soon as it is convenient.

### 2.1.3 (Optional) Install Firefox directly from the developer

To install the latest stable version of Firefox, directly from the developer, follow the steps below:

**Step 1**. Go to the [Firefox download page](https://www.mozilla.org/en-US/firefox/new/)

![](/sites/securityinabox.org/files/media/download-firefox.png)

*Figure 1: Firefox download button*

**Step 2**. **Click** the **[Free Download]** button to download the Firefox archive file

**Step 3**. Save the archive file somewhere convenient, such as on your *Desktop* in your *Documents* folder.

In this section, we will assume the Firefox archive is on your *Desktop*.

**Step 4**. **Navigate** to the folder where you saved the Firefox archive file

![](/sites/securityinabox.org/files/media/firefox-lin-en-v01-201.png)

*Figure 2: The Firefox archive file*

**Step 5**. **Double-click** the Firefox archive file to enter the archive

![](/sites/securityinabox.org/files/media/firefox-lin-en-v01-202.png)

*Figure 3: Inside the Firefox archive*

**Step 6**. **Click** **[Extract]** to choose a location for the Firefox application folder

![](/sites/securityinabox.org/files/media/firefox-lin-en-v01-203.png)

*Figure 4: Choosing a location to extract the Firefox application folder*

**Step 7**. **Navigate** to the location where you want you extract the Firefox application folder

**Step 8**. **Click** **[Extract]** to extract the Firefox application folder

![](/sites/securityinabox.org/files/media/firefox-lin-en-v01-204.png)

*Figure 5: Extracting the Firefox application folder*

**Step 9**. **Click** **[Close]** to return to the Firefox archive

![](/sites/securityinabox.org/files/media/firefox-lin-en-v01-205.png)

*Figure 6: Inside the Firefox archive*

**Step 10**. **Click** the **X** in the upper, right-hand corner to close the Firefox archive

**Step 11**. **Navigate** to the location where you extracted the Firefox application folder in the previous steps

![](/sites/securityinabox.org/files/media/firefox-lin-en-v01-206.png)

*Figure 7: The Firefox application folder*

**Step 12**. Enter the **Firefox** folder

![](/sites/securityinabox.org/files/media/firefox-lin-en-v02-207.png) 

*Figure 8: Inside the Firefox application folder*

**Step 13**. **Double-click** the **firefox** file to launch the Firefox browser

Firefox will ask if you want to make it your default browser, as shown below

![](/sites/securityinabox.org/files/media/firefox-lin-en-v01-208.png)

*Figure 9: The Firefox "Default Browser" screen*

**Step 14**. (Optional) **Uncheck** *Always perform this check when starting Firefox*

**Tip**. If you plan to use this installation on other computers, you should **uncheck** this box.

**Step 15**. **Click** either **[Not now]** or **[Use Firefox as my default browser]** to open the Firefox browser

![](/sites/securityinabox.org/files/media/firefox-lin-en-v01-209.png)

*Figure 10: The Firefox browser window*


## 2.2. Configure search engines

You can configure **Firefox** to use a search engine of your choice. To do so, follow the steps below:

**Step 1:** Select **Edit > Preferences** in your Firefox menu bar.
 
![](/sites/siabnext.ttc.io/files/media/search-preferences.png)

*Figure 1: Firefox search preferences*

**Step 2:** **Click** *Search* in the side bar of the *Preferences* screen.

You can now choose your default search engine and decide which other search engines should be accessible through the Firefox search box. We recommend [**DuckDuckGo**](https://duckduckgo.com/about) as a default search engine because it does not track or profile its users, or share its users' personal information with third parties. 

Other privacy-focused search engines that you can choose to add as search engine options to choose in the **Firefox** toolbar’s search bar include:

- [**StartPage**](https://www.startpage.com/)
- [**Ixquick**](https://www.ixquick.com/)
- [**Disconnect**](https://disconnect.me/search/)

## 2.3. Configure privacy options

You can configure the Firefox privacy settings by following the steps below:

**Step 1:** Select **Edit > Preferences** in your Firefox browser menu bar.

![](/sites/siabnext.ttc.io/files/media/privacy-preferences.png)

*Figure 1: Firefox privacy settings* 

**Step 2:** Click *Privacy* in the side bar of the *Preferences* screen.
 
You can now change the **Firefox** settings related to privacy, third-party tracking, and browsing history by following the steps below:

**Step 3**. Many websites collect information about you and allow third parties to gather data about the websites you visit. This is called *tracking*. [**Do Not Track**](http://donottrack.us/) is a system that enables users to opt out of tracking by websites they do not visit, including analytics services, advertising networks, and social platforms. 

To **enable** *Do Not Track* in **Firefox**, and minimise the tracking of your online activity, **select** the two options under the *Tracking* section. It is important to understand, however, that companies have the ability to ignore your choice and track you anyway. Here is a [**list**](http://donottrack.us/implementations) of companies' commitments to honoring *Do Not Track* requests.

**Step 4**. The *History* section lets you manage your **Firefox** *browsing history* preferences. Your browsing history is a list of websites you have visited using **Firefox**. The default option is *Remember my browsing and download history*, which means that **Firefox** will remember your browsing, download, form, and search histories. It will also accept *cookies* from the websites you visit. These *cookies* allow websites to record information on your device that **Firefox** will send back to them and their advertising partners.

To prevent this, in the first option under *History* that starts with *Firefox will:*, you can **change** *Remember history* to *Never remember history*. Or you can **change** it to *Use custom settings for history* and set more detailed preferences in the *History* section.

**Step 5**. The *Location Bar* section lets you choose the sources that **Firefox** will use to recommend Web address when you start typing in the *Address bar*. By default, it uses bookmarked Web addresses, open tabs, and websites that are in your browser history. You can uncheck any of these sources as you prefer.

## 2.4. Configure security options

You can configure the Firefox security settings by following the steps below:

**Step 1:** Select **Edit > Preferences** in your Firefox browser menu bar.

 ![](/sites/securityinabox.org/files/media/firefox-lin-en-v01-security-pref.png)

*Figure 1: The Firefox security settings*

**Step 2:** Click *Security* in the side bar of the *Preferences* screen. 

You can now modify the Firefox security settings. 

All of the boxes under **General** should be checked. If they are not, we recommend checking them so that Firefox will 

- Warn you when websites try to install add-ons 
- Block reported web attacks 
- Block reported Web forgeries. 

The boxes under **Passwords** relate to Firefox's built-in password manager. If you check the **Use a master password** box, Firefox will encrypt the website passwords that it saves and prompt you for a *master password* whenever it needs to enter one for you. In general, we recommend using an offline password manager, such as [KeePassX](../guide/keepassx/linux), to store your passwords. But, **if you are going to allow Firefox to manage your website passwords, you should check the second box.**


## 2.5. Configure advanced options

You can configure various advanced preferences for **Firefox** by following the steps below:

**Step 1:** Select **Edit > Preferences** in your Firefox browser menu bar. 

![](/sites/securityinabox.org/files/media/advanced-preferences.png)

*Figure 1: The Firefox advanced preferences*

**Step 2:** **Click** *Advanced* in the side bar of the *Preferences* screen.

The *Advanced preferences* screen contains five tabs: 

- **General** includes various usability options
- **Data Choices** allows you to choose what data to send to *Mozilla* about your browser health, security and performance
- **Update** allows you to determine how Firefox will handle automatic updates (including updates to your preferred search engines)
- **Network** allows you to manage proxy settings, cached web content and offline user data
- **Certificates** allows you to decide how Firefox should deal with cryptographic certificates (both when websites request a personal certificate from your browser and when Firefox is trying to determine whether or not an *https* certificate presented by a website is valid)

The **General** tab includes a useful option that allows Firefox to prevent web sites from automatically redirecting you to another page or reloading themselves without your consent or knowledge. 

![](/sites/securityinabox.org/files/media/firefox-lin-en-v01-210.png)

*Figure 2: The General tab of the Advances preferences screen*

**Step 3.** **Check** the *Warn me when websites try to redirect or reload the page* box



# 3. Firefox add-ons

In Firefox an add-on is simply a lightweight software program which adds new features or extends existing functionality. As such, add-ons are sometimes referred to as extensions. The [NoScript](http://noscript.net/) add-on, for example, extends Firefox functionality to block scripts from defined servers.

A plugin is essentially a piece of software usually designed by a third party to enable the use of their software within the Firefox browser. An example of a common plugin would be the Flash plugin designed to display Adobe Flash content within the Firefox browser window.

However, the Adobe Flash and Oracle Java browser plugins are often found to contain security vulnerabilities that could allow a remote user to assume control of your computer or to install malware. It is strongly advised that you disable both of those plugins in Firefox. For more information about how to disable or remove Java, please refer to Oracle's [steps to disable Java for all browsers on your computer](https://www.java.com/en/download/help/disable_browser.xml) or their [guide on how to uninstall Java from your computer](https://www.java.com/en/download/help/uninstall_java.xml).

In this guide, we explain how to install and configure the following Firefox add-ons:

* [**HTTPS Everywhere**](http://www.eff.org/https-everywhere/)
* [**Privacy Badger**](https://www.eff.org/privacybadger)
* [**Click&Clean**](http://www.hotcleaner.com/)
* [**NoScript**](http://noscript.net/)

We have chosen the above add-ons as examples because they are designed to increase  your privacy and security. Furthermore, you can install them directly from your Firefox browser menu bar, which means that they will automatically get updated everytime you update your browser. 

Other privacy-friendly add-ons for Firefox can be found through the [**Resources section of Tactical Tech's MyShadow project**](https://myshadow.org/resources).

## 3.1. HTTPS Everywhere

![](/sites/securityinabox.org/files/media/firefox-osx-en-v01-301-https-everywhere.jpg) 

**HTTPS Everywhere** is an *add-on* that helps **Firefox** connect securely to websites that support [encryption](/en/glossary#Encryption).

When you access a page using a Web address that begins with "http://" (such as *http://www.amazon.com*), your connection is unencrypted. The information you send to and receive from that website can be seen by anyone with the ability to monitor your Internet traffic. This includes your [(ISP)](/en/glossary#ISP) and many surveillance platforms.

When you access a page using a Web address that begins with "https://" (such as *https://www.amazon.com*), your connection will be encrypted, and third parties will find it much more difficult to intercept the data you send and receive. Unfortunately, even websites that *do* support *https* often fail to redirect visitors to the correct Web address. This is the problem that *HTTPS Everywhere* was designed solve.

*HTTPS Everywhere* maintains a list of websites that support *https* and automatically requests an encrypted connection for those websites—even if you click on a link (or enter an address into your browser) that begins with *http*. 

To install *HTTPS Everywhere*, follow the steps below:

**Step 1:** Select **Tools > Add-ons** in your Firefox browser menu bar. 

**Step 2:** In the “**Get Add-ons**” section, type **HTTPS Everywhere** in the search bar and press enter. You should now have a list of all available add-ons in front of you, including HTTPS Everywhere. 

![](/sites/siabnext.ttc.io/files/media/https-everywhere-firefox.png) 

*Figure 1: Finding the HTTPS-Everywhere add-on for Firefox*

**Step 3:** **Click** **[Install]**, next to **HTTPS Everywhere**, to download and install the *add-on*.

![](/sites/siabnext.ttc.io/files/media/https-everywhere-installed.png)

*Figure 2:Installing HTTPS-Everywhere*

**Step 4:** Restart your Firefox browser to install HTTPS Everywhere. 

**Step 5:** Verify that HTTPS Everywhere was installed successfully by selecting **Tools > Add-ons > Extensions** in the Firefox menu bar. HTTPS Everywhere should be displayed, along with your other add-ons.

![](/sites/siabnext.ttc.io/files/media/https-installed.png)

*Figure 3: HTTPS-Everywhere installed*

HTTPS Everywhere is now installed. When you connect to a website that is included in the list maintained by the add-on, and that supports *https*, your connection will be encrypted automatically.

**Note**. When HTTPS Everywhere is working, you should *still* see "https://" in your browser's address bar. If you do not, then your connection is unencrypted.

If you click on “**Preferences**” next to HTTPS-Everywhere, the following window should appear:

![](/sites/siabnext.ttc.io/files/media/https-obervatory-preferences.png)

*Figure 4: HTTPS-Everywhere's "SSL Observatory Preferences" screen*

Here you can choose whether you want to use the **EFF's SSL Observatory**, which warns you about insecure connections or attacks to your browser. We strongly recommend that you use this SSL Observatory for better browser security. 

## 3.2. Privacy Badger

![](/sites/securityinabox.org/files/media/privacy-badger-small.jpeg) 

[Privacy Badger](https://www.eff.org/privacybadger) is a browser *add-on* that prevents third-party companies from tracking your online activities. It is available for **Firefox**, the **Tor Browser**, **Chrome**, and **Chromium**.

To install **Privacy Badger**, follow the steps below:

**Step 1:** Select **Tools > Add-ons** in your Firefox browser menu bar.
 
**Step 2:** In the “**Get Add-ons**” section, type Privacy Badger in the search bar and press enter. You should now have a list of all available add-ons in front of you, including Privacy Badger. 

![](/sites/siabnext.ttc.io/files/media/privacy-badger-firefox.png)

*Figure 1: Finding the Privacy Badger add-on for Firefox*

**Step 3:** **Click** **[Install]**, next to **Privacy Badger**, to download and install the *add-on*. 
 
![](/sites/siabnext.ttc.io/files/media/privacy-badger-installed.png)

*Figure 2: Installing Privacy Badger*

When the addon is installed, Firefox will display Privacy Badger's "Thank you" page

![](/sites/securityinabox.org/files/media/firefox-lin-en-v01-323.png)

*Figure 3:Privacy Badger's "Thank You" page*

**Step 4:** Verify that Privacy Badger was installed successfully by selecting **Tools > Add-ons > Extensions** in the Firefox menu bar. Privacy Badger should be displayed, along with your other add-ons.

![](/sites/securityinabox.org/files/media/firefox-lin-en-v01-324.png)

*Figure 4: Privacy Badger installed*

The **Privacy Badger** *add-on* is now installed and can help prevent (*third party tracking*](/en/glossary#third-party-trackers) of your online activities. You can click **[Preferences]** to change **Privacy Badger's** settings (though the default values are fine).

## 3.3. Click&Clean

![](/sites/securityinabox.org/files/media/click-n-clean-icon.png)

[**Click&Clean**](http://www.hotcleaner.com/) is a browser extension that helps you clear your browsing history with just one click. 

Without privacy enhancing features, a browser can collect different types of information that it stores on the hard disk of your computer. Such data can include your location, browsing history, search history, cookies, cache, active logins and site preferences. This local storage can be deleted by manually cleaning your browser history with a tool like Click&Clean.     

You can install Click&Clean through the following steps:

**Step 1:** Select **Tools > Add-ons** in your Firefox browser menu bar. 

**Step 2:** In the “**Get Add-ons**” section, type **Click&Clean** in the search bar and press enter. You should now have a list of all available add-ons in front of you, including Click&Clean. 

![](/sites/siabnext.ttc.io/files/media/clickandclean-firefox.png)

*Figure 1: Finding the Click&Clean Firefox add-on*

**Step 3:** Click on the “**Install**” button next to Click&Clean to download the add-on (this probably shouldn't take longer than 2 minutes). 

![](/sites/siabnext.ttc.io/files/media/clickandclean-installed.png) 

*Figure 2: Installing Click&Clean*

**Step 4:** Restart your Firefox browser to finish installing Click&Clean. 

**Step 5:** Verify that Click&Clean was installed successfully by selecting **Tools > Add-ons > Extensions** in the Firefox menu bar. Click&Clean should be displayed, along with your other add-ons.

![](/sites/siabnext.ttc.io/files/media/clickandclean-ready.png)

*Figure 3: Click&Clean installed*

Alternatively, just look at your browser – the Click&Clean icon should be there now. If you click on the arrow next to it, you will notice that it offers a variety of features like incognito browsing, privacy testing, cookies, permissions and preferences.

The **privacy test** feature gives you the ability to see what services are running on your browser that you might have forgotten about. The **cookies** feature shows you what cookies are currently stored on your computer. By using the **permissions** feature you can change your browser's default settings to enhance your privacy. These settings/permissions include blocking or asking for permission every time the browser wants to store your passwords, share your location and use your camera and microphone. Examples of how you can set your browser's permissions are included below: 

![](/sites/siabnext.ttc.io/files/media/clickandclean-permissions.png)

*Figure 4: The Click&Clean Permissions screen*

In the **preference section** you can also choose if you want to automate the cleaning of your browser data. You can also clear your browsing history every time you close your browser, so that you do not need to think about your browsing history again.

![](/sites/siabnext.ttc.io/files/media/clickandclean-preferences.png)

*Figure 5: The Click&Clean Preferences screen*

**Note:** As an alternative, you might want to use an external application, like [**BleachBit**](http://bleachbit.sourceforge.net/download/linux), for this purpose..

## 3.4. NoScript

![](/sites/securityinabox.org/files/media/firefox-lin-en-v01-noscript.jpg) 

When you visit a website, your browser automatically downloads content from that site. In addition to text and images, this content often includes *scripts*, which are essentially small programs that run inside your browser. **NoScript** is a **Firefox** *add-on* that prevents your browser from running such programs without your permission.

The vast majority of these scripts are harmless and serve only to make webpages more interactive. Some of them are malicious, however, and some of them are [*third-party trackers*](/en/glossary#third-party-trackers) capable of building a profile of your online activities.

Unfortunately, **No Script** cannot automatically identify which scripts are safe and which are harmful. So, when you first tell it to *Block Scripts Globally*, it will prevent many websites from displaying properly. Once you start *whitelisting* scripts from different locations, however, things will begin returning to normal, and you will still be protected from potentially dangerous Web content.

To install **NoScript**, follow the steps below:

**Step 1:** Select **Tools > Add-ons** in your Firefox browser menu bar. 

**Step 2:** In the “**Get Add-ons**” section, type **NoScript** in the search bar and press enter. You should now have a list of all available add-ons in front of you, including NoScript. 

![](/sites/siabnext.ttc.io/files/media/noscript-firefox.png)

*Figure 1: Finding the NoScript add-on for Firefox*

**Step 3:** **Click** **[Install]**, next to **NoScript**, to download and install the *add-on*. 

![](/sites/siabnext.ttc.io/files/media/noscript-installed.png) 

*Figure 2: Installing NoScript*

**Step 4:** Restart Firefox to install NoScript. 

**Step 5:** Verify that NoScript was installed successfully by selecting **Tools > Add-ons > Extensions** in the Firefox menu bar.NoScript should be displayed, along with your other add-ons.

![](/sites/siabnext.ttc.io/files/media/noscript-preferences.png)

*Figure 3: NoScript installed*

Your browser now supports NoScript and blocks malicious code from running on your computer.

**Step 6**. **Click** **[Preferences]** to modify NoScript's settings. 

![](/sites/siabnext.ttc.io/files/media/noscript-options.png)

*Figure 4: The NoScript Preferences screen*

In general, NoScript's default preferences are fine as they are. Below, we recommend a few small changes.

**Step 7**. **Click** the *Embeddings* tab 

![](/sites/siabnext.ttc.io/files/media/noscript-embeddings.png)

*Figure 5: NoScript's "Ebeddings" preferences*

**Step 8**. **Check** the *Forbid &lt;FRAME&gt;* box

**Step 9**. **Check** the *Forbid &lt;IFRAME&gt;* box

**Step 10**. **Check** *Forbid WebGL* 

**Step 11**. **Click** the *Advanced* tab

![](/sites/siabnext.ttc.io/files/media/noscript-untrusted.png)

*Figure 6: The "Untrusted" sub-tab of NoScript's Advanced preferences*

**Step 12**. **Check** the *Forbid META redirections inside &lt;NOSCRIPT&gt; elements* box

**Step 13**. **Click** **[OK]**


**NoScript's other preferences are divided into six tabs, which are described briefly below:**

1. The **General tab** 
2. The **Whitelist tab** allows you to specify which websites you trust and want to prevent NoScript from blocking. You can also add sites to your *whitelist* here or by using the **NoScript** button when you visit a page that contains scripts blocked by NoScript. We recommended that you do *not* check the *Scripts Globally Allowed* box.
3. The **Embeddings tab** allows you to restrict embedded content on both "untrusted" websites and "trusted" websites that have been added to your *whitelist*.
4. The **Appearance tab** allows you to change the graphical options that NoScript provides when it blocks scripts
5. The **Notifications tab** allows you to decide how NoScript should notify you when it blocks scripts
6. The **Advanced tab** contains six sub-tabs.

The six sub-tabs of NoScript's **Advanced** preferences are described below.

- The **Untrusted sub-tab** allows you to set additional restrictions on websites that are not in your whitelist
- The **Trusted sub-tab** allows you to set additional permissions for websites that *are* in your whitelist
- The **XSS sub-tab** allows you to configure how NoScript protects you from *cross-site scripting (XSS)* attacks
- The **HTTPS sub-tab** allows you to force certain websites to use (or not use) an encrypted *https* connection. It also covers preferences related to the secure transfer of cookies and active Web content.
- The **ABE sub-tab** allows you to configure Application Boundary Enforcement (ABE) firewall rules that restrict web application behaviour.
- The **ClearClick sub-tab** 

Although NoScript might seem a little frustrating at first (as the websites you have always visited may not display properly), you will immediately profit from the automated object-blocking feature. This will restrict pesky advertisements, pop-up messages and malicious code built (or hacked) into web pages.

NoScript will run silently in the background until it detects the presence of JavaScript, Adobe Flash or other script-like content. At that point NoScript will block this content and status bar will appear on the bottom of the Firefox window. The NoScript status bar displays information about which objects (for example, advertisements and pop-up messages) and scripts are currently prevented from executing themselves on your system. But since NoScript does not differentiate between malicious and real code, certain key features and functions (for instance, a tool bar) may be missing. 

Some web pages present content, including script-like content, from more than one website. For example, a website like www.twitter.com has two sources of scripts (twitter.com and twimg.com). To unblock scripts in these circumstances, start by **selecting** the *Temporarily Allow* [website name] option (in this instance, Temporarily allow twitter.com). However, if this does not allow you to view the page you may determine, through a process of trial and error, the minimum number of websites required to view your chosen content. For instance, on Twitter, you need to **select** the *Temporarily allow twitter.com* and *Temporarily allow twimg.com* options, in order for Twitter to work. For websites that you trust and frequently visit, **select** the *Allow [website name]* option. Selecting this option permits NoScript to permanently list that website as trusted.

You can find a number of other useful Firefox add-ons in the [*Resources* section of Tactical Tech's *MyShadow* website](https://myshadow.org/resources).

# FAQ

**Q:** Why would I want so many different add-ons to defend myself against malicious websites? If NoScript protects me from potentially dangerous scripts, for example, why do I also need other add-ons which function in a similar way?

**A:** It is often a good idea to use more than one tool to address the same general security issue (anti-virus programs are an important exception to this rule, since they tend to conflict with one another). These Firefox add-ons use very different techniques to protect your browser from a variety of threats. NoScript, for example, blocks all scripts from unknown websites, but users tend to 'whitelist' the websites they visit frequently, which allows them to load potentially-malicious scripts. NoScript users also tend to allow unknown sites to load scripts, on a temporary basis, if those scripts are necessary for the page to function properly.