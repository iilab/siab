

---

lang: en
community: guide
type: tools
os: os-x
weight: 075
title: Firefox and Security Add-Ons for Mac OS X - Secure Web Browser

---

**Mozilla Firefox** is a [**free and open source software (FOSS)**](/en/glossary#FOSS) web browser for which many *add-ons* are available. Some of these *add-ons* are designed to protect your privacy and security when you browse the web.

# Required reading


{{ required_reading: ../../secure communication }}


{{ tool: ./075-tool.md }}

# What you will get from this guide

- A stable and secure internet browser whose features can be enhanced by numerous add-ons.
- The ability to protect yourself from potentially dangerous programs and malicious websites.
- The ability to wipe the digital traces of your browsing activity.

# 1. Introduction to Firefox

This guide assumes that you already know how to use a web browser and will not cover the basic functions of **Firefox**. It will focus on security-related settings and *add-ons*.

## 1.0 Things to know about Firefox before you start

**Firefox** has many easy-to-use *add-ons* that improve your privacy and security when you browse the Web. You can choose which *add-ons* to install, and decide how to configure them, depending on your circumstances. If you are using a computer that is managed by someone else (if you're at an Internet cafe, for example, or in your place of work), you might have to make these adjustments repeatedly.

In addition to basic **Firefox** settings, this guide covers the installation and basic configuration of the following *add-ons*:

* [**HTTPS Everywhere**](https://www.eff.org/https-everywhere)  
* [**Privacy Badger**](https://www.eff.org/privacybadger)
* [**NoScript**](https://noscript.net/) 
* [**Click&Clean**](http://www.hotcleaner.com/)  

The *Resources* section of Tactical Tech's [**MyShadow website**](https://myshadow.org/resources) covers additional privacy-enhancing browser *add-ons*.

**Important:** The overwhelming majority of malware and spyware infections originate from webpages. It is important that you always consider whether it is safe to visit unknown websites, particularly those that are sent to you by email. Before you decide to open unknown or suspicious webpages, we recommend that you scan the web address using the following page scanners:

* [www.virustotal.com](http://www.virustotal.com/) 
* [www.onlinelinkscan.com](http://onlinelinkscan.com/) 
* [www.phishtank.com](http://www.phishtank.com/index.php) 

You can also check the reputation of a website using the scanners listed below:

* [http://safeweb.norton.com](http://safeweb.norton.com/) 
* [www.urlvoid.com](http://www.urlvoid.com/) 

## 1.1 Other tools like Firefox

**Microsoft Windows, GNU/Linux, and other Mac OS X, Compatible Programs:**

The **Mozilla Firefox** Web browser is available for **GNU/Linux**, **Mac OS X**, **Microsoft Windows**, **Android**, and **iOS**. Websites are the most common source of [malware](/en/glossary#Malware) infection, so accessing them securely is vital. We recommend that you use **Mozilla Firefox** and install the add-ons covered in this guide. If you would prefer to use a program other than **Mozilla Firefox**, the alternatives below are also available for **GNU/Linux**, **Mac OS X** and **Microsoft Windows**:

- [**Google Chromium**](https://download-chromium.appspot.com/) (Chromium is the [open source](/en/glossary#FOSS) version of **Chrome**.)
- [**Google Chrome**](http://www.google.com/chrome/)
- [**Opera**](http://www.opera.com/)
- [**Tor Browser**](https://www.torproject.org/download/download-easy.html.en)


# 2. Install and configure Firefox





## 2.1 Install and launch Firefox

To install the latest stable version of **Firefox**, follow the steps below:

**Step 1**. Go to the [Firefox download page](https://www.mozilla.org/en-US/firefox/new/).

![](/sites/securityinabox.org/files/media/firefox-osx-en-v01-101-ff-download-pg.png)

*Figure 1: Firefox download button*

**Step 2**.  **Click** the **[Free Download]** button to download Firefox. **Firefox** will detect your *Operating System* (**Mac OS X**) and recommend the best version of **Firefox** for you.

**Step 3**. The download should start automatically. 

![](/sites/securityinabox.org/files/media/firefox-osx-en-v01-103-ff-auto-download.png)

*Figure 2: Automatic download of Firefox*

**Save** the file somewhere convenient. In this example, we will assume the downloaded Firefox file is in your *Downloads* folder.

![](/sites/securityinabox.org/files/media/firefox-osx-en-v01-104-save-file-to-desktop.png)

*Figure 3: Saving Firefox .dmg file to the Downloads folder*

**Step 4**. **Navigate** to the folder where you saved the **Firefox** file. In this example, we assume you saved file in your *Downloads* file.

![](/sites/securityinabox.org/files/media/firefox-osx-en-v01-105-locate-dmg.png)

*Figure 4: The Downloads folder containing the Firefox disk image*

**Step 5**. **Double-click** the Firefox disk image (a file ending in ‘.dmg’) to mount it as a disk image. It should show up as in a new window (*Figure 5*, below) and under *Devices* in the sidebar in a normal *Finder* window.

![](/sites/securityinabox.org/files/media/firefox-osx-en-v01-106-mounted-ff-dmg.png)

*Figure 5: Inside the mounted Firefox disk image*

**Step 6**. Drag the **Firefox.app** into your *Applications* folder.

![](/sites/securityinabox.org/files/media/firefox-osx-en-v01-107-drag-app.png)

*Figure 6: Dragging the mounted TorBrowser.app into the Applications folder*

It should then copy over into *Applications*.

![](/sites/securityinabox.org/files/media/firefox-osx-en-v01-108-copy-app.png)

*Figure 7: Progress window for copying Firefox.app into the Applications folder *

**Step 7**. Before we start using **Firefox**, we should **unmount** (or **'eject'**) the ** Firefox** disk image. Find *Firefox* under *Devices* in the *Finder sidebar*. **Click** on the {**eject**} icon next to it in the sidebar to **unmount** the disk image.

![](/sites/securityinabox.org/files/media/firefox-osx-en-v01-109-eject.png)

*Figure 8: Unmounting (or ejecting) the Firefox disk image*

**Step 8**. Now that we’ve installed Firefox, let’s open it up for the first time. First, **Navigate** to the **Firefox** app in your *Applications* folder.

**Step 9**. **Double-click** the **Firefox** app to launch it.

**Step 10**: An alert will pop up to ask you if you’re sure you want to open *”Firefox.app”*. **Click** **[Open]**.

![](/sites/securityinabox.org/files/media/firefox-osx-en-v01-110-confirmation-prompt.png) 

*Figure 9: Final confirmation prompt*

## 2.2 Configure search engines

You can configure **Firefox** to use a search engine of your choice. To do so, follow the steps below:

**Step 1**. **Click** on **Firefox** in the main menu, then **scroll** down to   **select** *Preferences*.
 
![](/sites/securityinabox.org/files/media/firefox-osx-en-v01-111-open-ff-prefs.png)

*Figure 1: Selecting Preferences in the Firefox menu*

**Step 2**. **Click** *Search* in the side bar of the *Preferences* screen.

![](/sites/securityinabox.org/files/media/firefox-osx-en-v01-112-search-prefs.png)

*Figure 2: Choosing a default search engine in Firefox Preferences*

You can now choose your default search engine and decide which other search engines should be accessible through the **Firefox** search box. We recommend [**DuckDuckGo**](https://duckduckgo.com/about) as a default search engine because it does not track or profile its users, nor share its users' personal information with third parties. 

Other privacy-focused search engines that you can choose to add as search engine options to select in the **Firefox** toolbar’s search bar include:

- [**StartPage**](https://www.startpage.com/)
- [**Ixquick**](https://www.ixquick.com/)
- [**Disconnect**](https://disconnect.me/search/)

## 2.3 Configure privacy options

You can configure privacy options for **Firefox** by following the steps below:

![](/sites/securityinabox.org/files/media/firefox-osx-en-v01-111-open-ff-prefs.png)

*Figure 1: Selecting Preferences in the Firefox menu*

**Step 2:** **Click** *Privacy* in the side bar of the *Preferences* screen.
 
The *Privacy* screen is divided into three sections: **Tracking**, **History**, and **Location bar**.

![](/sites/securityinabox.org/files/media/firefox-osx-en-v01-113-privacy-prefs.png)

*Figure 2: The Privacy Preferences for Firefox*

You can now change the **Firefox** settings related to privacy, third-party tracking, and browsing history by following the steps below:

**Step 3**. Many websites collect information about you and allow third parties to gather data about the websites you visit. This is called *tracking*. [**Do Not Track**](http://donottrack.us/) is a system that enables users to opt out of tracking by websites they do not visit, including analytics services, advertising networks, and social platforms. 

To **enable** *Do Not Track* in **Firefox**, and minimise the tracking of your online activity, **select** the two options under the *Tracking* section. It is important to understand, however, that companies have the ability to ignore your choice and track you anyway. Here is a [**list**](http://donottrack.us/implementations) of companies' commitments to honoring *Do Not Track* requests.

**Step 4**. The *History* section lets you manage your **Firefox** *browsing history* preferences. Your browsing history is a list of websites you have visited using **Firefox**. The default option is *Remember my browsing and download history*, which means that **Firefox** will remember your browsing, download, form, and search histories. It will also accept *cookies* from the websites you visit. These *cookies* allow websites to record information on your device that **Firefox** will send back to them and their advertising partners.

To prevent this, in the first option under *History* that starts with *Firefox will:*, you can **change** *Remember history* to *Never remember history*. Or you can **change** it to *Use custom settings for history* and set more detailed preferences in the *History* section.

**Step 5**. The *Location Bar* section lets you choose the sources that **Firefox** will use to recommend Web address when you start typing in the *Address bar*. By default, it uses bookmarked Web addresses, open tabs, and websites that are in your browser history. You can uncheck any of these sources as you prefer.

## 2.4 Configure security options

You can configure the **Firefox** security settings by following the steps below:

**Step 1:** **Click** on **Firefox** in the main menu, then **scroll** down to **select** *Preferences*.
 
![](/sites/securityinabox.org/files/media/firefox-osx-en-v01-111-open-ff-prefs.png)

*Figure 1: Selecting Preferences in the Firefox menu*

**Step 2:** Click *Security* in the side bar of the *Preferences* screen. 

![](/sites/securityinabox.org/files/media/firefox-osx-en-v01-114-security-prefs.png)

*Figure 2: The Security Preferences for Firefox*

You can now change the security settings  for **Firefox**.

**Step 3**. All of the boxes under **General** should be checked by default. If they are not, we recommend **checking** them so that **Firefox** will: 

- Warn you when websites try to install add-ons. 
- Block reported web attacks.
- Block reported Web forgeries. 

**Step 4**. The boxes under *Passwords* relate to **Firefox's** built-in password manager. If you check the *Use a master password* box, **Firefox** will encrypt the website passwords that it saves and prompt you for a *master password* whenever it needs to enter one for you. 

**We recommend using an offline password manager, such as [KeePassX](../keepassx/os-x), to store your passwords. But, *if* you choose to allow Firefox to manage your website passwords, you should check the second box.**

## 2.5 Configure advanced options

You can configure various advanced preferences for **Firefox** by following the steps below:

**Step 1**. **Click** on **Firefox** in the main menu, then **scroll** down to **select** *Preferences*.
 
![](/sites/securityinabox.org/files/media/firefox-osx-en-v01-111-open-ff-prefs.png)

*Figure 1: Selecting Preferences in the Firefox menu*

**Step 2**. Click *Advanced* in the side bar of the *Preferences* screen. 

![](/sites/securityinabox.org/files/media/firefox-osx-en-v01-115-advanced-prefs.png)

*Figure 2: The Advanced Preferences for Firefox*

**Step 3**. The *Advanced preferences* section is designed with the advanced or experienced **Firefox** user in mind. You can explore and change the *Advanced preferences* for **Firefox** as you prefer. The screen contains five tabs: 

- *General* includes various usability options.
- *Data Choices* enables you to choose whether or not you allow your data to be shared with **Mozilla**.
- *Update* allows you to determine how **Firefox** will handle automatic updates (including updates to your preferred search engines)
- *Network* allows you to add and manage proxy settings, cached web content, and offline user data
- *Certificates* allows you to decide how **Firefox** should manage *SSL certificates* for sites that provide *https* encryption.

**Step 4**. The *General* tab includes a useful option that allows **Firefox** to prevent web sites from automatically redirecting you to another page or reloading themselves without your consent or knowledge. Users of *all* levels will benefit from enabling this preference.

**Click** on the *General* tab if you are not in that section already.

![](/sites/securityinabox.org/files/media/firefox-osx-en-v01-116-advanced-gen-prefs.png)

*Figure 3: The General tab of the Advances preferences screen*

**Step 5.** **Check** the *Warn me when websites try to redirect or reload the page* box. (It is the third option under *Accessibility*.)

# 3. Firefox add-ons

In **Firefox**, an *add-on* is a lightweight software program that adds new features or extends existing functionalities. As such, *add-ons* are sometimes referred to as *extensions*. (For example, the [NoScript](http://noscript.net/) add-on, extends **Firefox** functionality to block scripts from defined servers.)

A *plugin* is a piece of software typically designed to enable the use of third-party software within the **Firefox** browser. An example of a common *plugin* would be the **Flash** *plugin* designed to display **Adobe Flash** content within the **Firefox** browser window.

**Tip**: The **Adobe Flash** and **Oracle Java** browser *plugins* are often found to contain security vulnerabilities that could allow a remote user to assume control of your computer or to install [*malware*](/en/glossary#Malware). It is strongly advised that you disable both of those plugins in **Firefox**. For more information about how to disable or remove **Java**, please refer to **Oracle's** [steps to disable Java for all browsers on your computer](https://www.java.com/en/download/help/disable_browser.xml) or their [guide on how to uninstall Java from your computer](https://www.java.com/en/download/help/uninstall_java.xml).

In the next section, we explain how to install and configure the following **Firefox** *add-ons*:

* [**HTTPS Everywhere**](http://www.eff.org/https-everywhere/)
* [**Privacy Badger**](https://www.eff.org/privacybadger)
* [**Click&Clean**](http://www.hotcleaner.com/)
* [**NoScript**](http://noscript.net/)

We have chosen the above *add-ons* as because they are designed to increase  your privacy and security. Other privacy-friendly *add-ons* for **Firefox** can be found through the [**Resources section of Tactical Tech's MyShadow project**](https://myshadow.org/resources).

## 3.1 HTTPS Everywhere

![](/sites/securityinabox.org/files/media/firefox-osx-en-v01-301-https-everywhere.jpg) 

**HTTPS Everywhere** is a **Firefox** *add-on* that helps users use encrypted connections to websites when they are available. Many websites offer [SSL](/en/glossary#SSL) [encryption](/en/glossary#Encryption) that you can recognize when a website address starts with *https*. But many websites default to *unencrypted* connections with addresses that start with *http*, even though they have the ability to provide an encrypted connection.

When you connect to a website that starts with *http*, it means that all the information and data you receive and send to that website’s servers can be seen and intercepted by any intermediary between you and that website (including your [Internet Service Provider](/en/glossary#ISP)).

But when you connect to a website that starts with *https*, your connection to the website is encrypted. This makes it more difficult for the information and data you receive and send to that website’s to be seen and intercepted. 

The *HTTPS Everywhere add-on* addresses these problems by connecting to websites using *https* encryption when available. 

To install the *HTTPS Everywhere add-on*, follow the steps below:

**Step 1**. Select **Tools > Add-ons** in the main **Firefox** menu. (Or you can **use** the shortkey combination **Shift + Command + A**.)

![](/sites/securityinabox.org/files/media/firefox-osx-en-v01-302-open-addons.png) 

*Figure 1: Accessing add-ons in Firefox*

**Step 2**. In the “**Get Add-ons**” section, type **HTTPS Everywhere** in the search bar and **press enter**. 

![](/sites/securityinabox.org/files/media/firefox-osx-en-v01-308-get-addons.png) 

*Figure 2: The Add-ons Manager in Firefox*

You should now have a list of *add-on* search results, including one for **HTTPS Everywhere**. 

![](/sites/securityinabox.org/files/media/firefox-osx-en-v01-304-addons-search-result.png)  

*Figure 3: Finding the HTTPS Everywhere add-on for Firefox*

**Step 3**. **Click** on the **[Install]** button next to **HTTPS Everywhere** to download the *add-on*. 

![](/sites/securityinabox.org/files/media/firefox-osx-en-v01-305-https-everywhere-dwnlded.png)

*Figure 4: HTTPS Everywhere add-on downloaded*

**Step 4**. **Click** the *Restart Now* link to install **HTTPS Everywhere**. 

**Step 5**. After **Firefox** has restarted, it will return to the same screen in the *add-ons manager* where we searched for the **HTTPS Everywhere**, but the **HTTPS Everywhere** *add-on* will no longer be in the search results. 

In order to **verify** that **HTTPS Everywhere** has been installed successfully, **click** on *Extensions* in the menu on the left side of the *add-ons manager*. **HTTPS Everywhere** should be listed along with your other installed *add-ons*.

![](/sites/securityinabox.org/files/media/firefox-osx-en-v01-306-extensions.png)

*Figure 5: HTTPS Everywhere installed*

**Step 6**.  To access the preferences for **HTTPS Everywhere**, **click** on  *Preferences* next to its name in the installed *Extensions* tab of **Firefox**’s *Add-ons Manager* (as seen in *Figure 5*).

![](/sites/securityinabox.org/files/media/firefox-osx-en-v01-307-https-evrywhere-prefs.png)

*Figure 6: HTTPS Everywhere's Preferences screen*

**Step 7**. **HTTPS Everywhere** offers the option of using *EFF’s* **SSL Observatory**, which warns you about insecure connections or attacks on your browser. We strongly recommend that you use this for better browser security.

To use the **SSL Observatory**, **check** the box next to *Use the Observatory?*

## 3.2 Privacy Badger

![](/sites/securityinabox.org/files/media/privacy-badger-small.jpeg) 

[Privacy Badger](https://www.eff.org/privacybadger) is a browser *add-on* which prevents third-party companies from tracking your online activities. It accomplishes this by preventing third-party tracking content from loading in the webpages you visit. It is available as an *add-on* for **Firefox**, the **Tor Browser**, **Chrome**, and **Chromium**.

**Privacy Badger** is unique because it blocks *all* third-party companies from tracking you when you access websites. This differentiates it from similar third-party extensions such as [Ghostery](https://myshadow.org/ghostery), [Disconnect](https://disconnect.me/) and [Adblock Plus](https://myshadow.org/adblock-plus), which all require custom configuration to block aggressive trackers. 

To install **Privacy Badger**, follow the steps below:

**Step 1**. Select **Tools > Add-ons** in the main **Firefox** menu. (Or you can **use** the shortkey combination **Shift + Command + A**.)

![](/sites/securityinabox.org/files/media/firefox-osx-en-v01-302-open-addons.png) 

*Figure 1: Accessing add-ons in Firefox*

**Step 2**. In the “**Get Add-ons**” section, type **Privacy Badger** in the search bar and **press enter**. 

![](/sites/securityinabox.org/files/media/firefox-osx-en-v01-308-get-addons.png) 

*Figure 2: The Add-ons Manager in Firefox*

You should now have a list of *add-on* search results, including one for **Privacy Badger**. 

![](/sites/securityinabox.org/files/media/firefox-osx-en-v01-309-privacy-badger-search-results.png)  

*Figure 3: Finding the Privacy Badger add-on for Firefox*

**Step 3**. **Click** on the **[Install]** button next to **Privacy Badgere** to download the *add-on*. 

![](/sites/securityinabox.org/files/media/firefox-osx-en-v01-305-https-everywhere-dwnlded.png)

*Figure 4: Privacy Badger add-on downloaded*

The **Privacy Badger** *add-on* does *not* need you to restart **Firefox** in order for it to work.

When the **Privacy Badger** *add-on* is installed, **Firefox** will open **Privacy Badger's** "Thank you" page in a new browser tab. (Keep this tab open for **Step 5** below.)

![](/sites/securityinabox.org/files/media/firefox-osx-en-v01-310-privacy-badger-thankyou.png)

*Figure 5:Privacy Badger's "Thank You" page*

**Step 4**. In order to verify that **Privacy Badger** has been installed successfully, **click** on *Extensions* in the menu on the left side of the *add-ons manager*. **Privacy Badger** should be listed along with your other installed *add-ons*.

![](/sites/securityinabox.org/files/media/firefox-osx-en-v01-311-ff-extensions-privacy-badger.png)

*Figure 6: Privacy Badger installed*

**Step 5**. To learn more about using **Privacy Badger**, return to **Privacy Badger's** "Thank you" page in the other browser tab (as seen in *Figure 5* above).

## 3.3 Click&Clean

![](/sites/securityinabox.org/files/media/click-n-clean-icon.png)

[**Click&Clean**](http://www.hotcleaner.com/) is an *add-on* designed to automatically delete private data upon closing **Firefox**. This includes clearing records from your download history, deleting browsing history, and removing cookies, including **Flash Local Shared Objects** (**LSO**). It also deletes temporary files and empties your local cache. 

**Note**: [**Click&Clean**](http://www.hotcleaner.com/clickclean_chrome.html) is also available on **Chrome**. Alternatively, users may also consider using external applications, like **CCleaner** for [**Apple OS X**](https://www.piriform.com/ccleaner-mac) and [**Windows**](../ccleaner/windows), or [**BleachBit**](http://bleachbit.sourceforge.net/) for **Linux** and **Windows**.

To install the **Click&Clean** *add-on*, follow the steps below:

**Step 1**. Select **Tools > Add-ons** in the main **Firefox** menu. (Or you can **use** the shortkey combination **Shift + Command + A**.)

![](/sites/securityinabox.org/files/media/firefox-osx-en-v01-302-open-addons.png) 

*Figure 1: Accessing add-ons in Firefox*

**Step 2**. In the “**Get Add-ons**” section, type **Click&Clean** in the search bar and **press enter**. 

![](/sites/securityinabox.org/files/media/firefox-osx-en-v01-308-get-addons.png) 

*Figure 2: The Add-ons Manager in Firefox*

You should now have a list of *add-on* search results, including one for **Click&Clean**. 

![](/sites/securityinabox.org/files/media/firefox-osx-en-v01-312-click-n-clean-search-results.png)  

*Figure 3: Finding the Click&Clean add-on for Firefox*

**Step 3**. **Click** on the **[Install]** button next to **Click&Cleane** to download the *add-on*. 

![](/sites/securityinabox.org/files/media/firefox-osx-en-v01-313-click-n-clean-dwnlded.png)

*Figure 4: Click&Clean add-on downloaded*

**Step 4**. **Click** the *Restart Now* link to install **Click&Clean**. 

**Step 5**. After **Firefox** has restarted, you will be taken to **Click&Clean’s** website on a new browser tab.

In order to **verify** that **Click&Clean** has been installed successfully, return to **Firefox’s** *add-ons manager* tab. **Click** on *Extensions* in the menu on the left side of the *add-ons manager*. **Click&Clean** should be listed along with your other installed *add-ons*.

![](/sites/securityinabox.org/files/media/firefox-osx-en-v01-314-extensions-w-click-n-clean.png)

*Figure 5: Click&Clean installed*

**Step 6**. The **Click&Clean** icon should now appear in the **Firefox** toolbar as a blue toilet paper roll. If you **click** on the arrow next to it, you can see its menu of options. These include viewing and deleting cookies, incognito browsing, clearing browsing data, and more.

![](/sites/securityinabox.org/files/media/firefox-osx-en-v01-315-click-n-clean-menu.png)

*Figure 6: The Click&Clean drop-down menu*

**Step 7**. In the **Click&Clean** drop-down menu, scroll down to **select** *Preferences*. In the **preference section** you can set preferences that manage and limit the data that websites can access, as well as the browsing data stored on your computer.  

![](/sites/securityinabox.org/files/media/firefox-osx-en-v01-316-click-n-clean-preferences.png)

*Figure 7: The Click&Clean Preferences screen*

## 3.4 NoScript

![](/sites/securityinabox.org/files/media/noscript-icon.jpg)

[NoScript](http://noscript.net/) is a **Firefox** *add-on* that helps protect you by preventing potentially malicious code from running within your browser when you access websites. 

When you install the **NoScript** *add-on*, online content written to run using Java, Java Script, Flash, Silverlight and other programs are blocked by default, protecting you from the potential exploitation of security vulnerabilities. 

Since not all content is malicous, and there are many sites we know and trust, you can tell **NoScript** to allow content to run on approved (or *‘whitelisted’*) websites. (For example, it’s common to *whitelist* our online banking and news websites.) 

When you first start using **NoScript**, you will have to begin adding trusted websites to your *whitelist*. After a while, you will have to do this less often, as **NoScript** will remember the sites you’ve added to your *whitelist*. 

There are more ways to utilize **NoScript** as you browse the web. You can *temporarily allow* websites to run content. You also have the ability to unblock specific content on a webpage  while continuing to block other content on the same page. 

Installing NoScript is quick and easy and you can literally install this add-on to your browser within 2 minutes. You can do this through the following steps:

To install the **NoScript** *add-on*, follow the steps below:

**Step 1**. Select **Tools > Add-ons** in the main **Firefox** menu. (Or you can **use** the shortkey combination **Shift + Command + A**.)

![](/sites/securityinabox.org/files/media/firefox-osx-en-v01-302-open-addons.png) 

*Figure 1: Accessing add-ons in Firefox*

**Step 2**. In the “**Get Add-ons**” section, type **NoScript** in the search bar and **press enter**. 

![](/sites/securityinabox.org/files/media/firefox-osx-en-v01-308-get-addons.png) 

*Figure 2: The Add-ons Manager in Firefox*

You should now have a list of *add-on* search results, including one for **NoScript**. 

![](/sites/securityinabox.org/files/media/firefox-osx-en-v01-317-noscript-search-results.png)  

*Figure 3: Finding the NoScript add-on for Firefox*

**Step 3**. **Click** on the **[Install]** button next to **NoScript** to download the *add-on*. 

![](/sites/securityinabox.org/files/media/firefox-osx-en-v01-318-noscript-dwnlded.png)

*Figure 4: NoScript add-on downloaded*

**Step 4**. **Click** the *Restart Now* link to install **NoScript**. 

**Step 5**. After **Firefox** has restarted, you will be taken to **NoScript’s** website on a new browser tab.

In order to **verify** that **NoScript** has been installed successfully, return to **Firefox’s** *add-ons manager* tab. **Click** on *Extensions* in the menu on the left side of the *add-ons manager*. **NoScript** should be listed along with your other installed *add-ons*.

![](/sites/securityinabox.org/files/media/firefox-osx-en-v01-319-extensions-w-noscript.png)

*Figure 5: NoScript installed*

# FAQ

**Q:** Why would I want so many different add-ons to defend myself against malicious websites? If NoScript protects me from potentially dangerous scripts, for example, why do I also need other add-ons which function in a similar way?

**A:** It is often a good idea to use more than one tool to address the same general security issue (anti-virus programs are an important exception to this rule, since they tend to conflict with one another). These Firefox add-ons use very different techniques to protect your browser from a variety of threats. NoScript, for example, blocks all scripts from unknown websites, but users tend to 'whitelist' the websites they visit frequently, which allows them to load potentially-malicious scripts. NoScript users also tend to allow unknown sites to load scripts, on a temporary basis, if those scripts are necessary for the page to function properly.