

---

lang: en
community: guide
type: tools
os: android
weight: 097
title: Orweb for Android

---

**Orweb** is an free Android-platform mobile phone application, created by the [Guardian Project](https://guardianproject.info/) for browsing the internet anonymously in conjunction with [**Orbot**](../orbot/android).

# Required reading


{{ required_reading: ../../anonymity and circumvention }}


{{ required_reading: ../../mobile phones }}


{{ required_reading: ../../smartphones }}


{{ tool: ./097-tool.md }}

# What you will get from this guide

- The ability to conceal your digital identity from the websites you visit
- The ability to conceal the websites you visit
- The ability to bypass Internet censorship and online filtering

# 1. Introduction to Orweb

**Note:** There is a [bug](http://xordern.net/ip-leakage-of-mobile-tor-browsers.html) in the current version of **Orweb** (0.6.1 and older) that may leak information about you, such as your IP address, to the website owners if you are viewing HTML5 based videos. **Orweb** will still allow you to circumvent censorship and prevent you from being spied on by your *Internet Service Provider* (ISP) but we do not recommend it to be used to view sites that may be considered hostile. For more information on the issue see the developers' [response](https://guardianproject.info/2014/06/30/recent-news-on-orweb-flaws/).

**Orweb** will only work properly after installing and configuring [**Orbot**](../orbot/android).

Remember, if you previously created a mail or blog without using **Orweb**, the site will still know your real location even if you return using **Orweb**.

If you want stronger anonymity while using **Orweb** other steps need to be taken including:

- never access accounts made in your real name.
- never give your personal data.
- never do the same things that you do when not trying to be anonymous.

## 1.0 Other tools like Orweb

- iOS: [OnionBrowser](https://mike.tig.as/onionbrowser/) (non-free)
- Android: [Firefox](https://play.google.com/store/apps/details?id=org.mozilla.firefox) with [ProxyMobile](https://addons.mozilla.org/en-US/mobile/addon/proxy-mobile/)


# 2. Install Orweb

**Step 1:** On your Android device, **download** and **install** the app from the [Google Play store](https://play.google.com/store/apps/details?id=info.guardianproject.browser) store by tapping ![](/sites/siabnext.ttc.io/files/media/orweb-and-002.png).

![](/sites/siabnext.ttc.io/files/media/orweb-and-001.png)

*Figure 1: Orweb in the Google Play store*

**Note:** **Orweb** can also be downloaded [directly](https://guardianproject.info/releases/orweb-latest.apk) or from the third party [F-Droid](https://f-droid.org/repository/browse/?fdfilter=orweb&fdid=info.guardianproject.browser) store.

**Step 2:** Before the installation process begins, you will be prompted to review the access the application will have on your phone. Review this carefully. Once your are happy with the permissions that will be granted, press ![](/sites/siabnext.ttc.io/files/media/orweb-and-003.png) to start the installation. If you do not agree with the permissions that will be granted, press the back button and the installation will be cancelled.

![](/sites/siabnext.ttc.io/files/media/orweb-and-004.png)

*Figure 2: Permissions required*

**Step 3:** Once **Orweb** downloads and installation has completed, you can press ![](/sites/siabnext.ttc.io/files/media/orweb-and-005.png) to start the application.

# 3. Start Orweb

**Step 1:** To open Orweb you **tap** the application's icon.

![](/sites/siabnext.ttc.io/files/media/trans-orweb.png)

**Step 2:** **Orweb** will launch and automatically try to connect to *https://check.torproject.org*, to ensure that its connection to the **Tor** network is working. If it can connect, you will see a message telling you that your *browser is configured to use Tor*. If **Orweb** can not connect to the website you will see an error message in the browser. If this happens, it is suggested that you check that [Orbot](../orbot/android) is installed and running on your android device if this happens.

![](/sites/siabnext.ttc.io/files/media/orweb-and-006.png) ![](/sites/siabnext.ttc.io/files/media/orweb-and-007.png)

*Figure 1 & 2: Orweb successfully connected and Orweb connection failure screens*

**Step 3:** To browse to websites, **tap** the area at the top of the screen to the right of ![](/sites/siabnext.ttc.io/files/media/orweb-and-008.png) and type in the address you want to visit. Press **Go** on the onscreen keypad.

![](/sites/siabnext.ttc.io/files/media/orweb-and-009.png) ![](/sites/siabnext.ttc.io/files/media/orweb-and-010.png)

*Figure 3 & 4: Browsing to a new website*


# 4. Change your UserAgent

If you want to hide the type of device that you are using from the websites you visit, **Orweb** can be configured to pretend to be a number of different devices.

**Step 1:** **Tap** on the menu icon (![](/sites/siabnext.ttc.io/files/media/orweb-and-011.png)) found in the top right of the screen and **tap** ![](/sites/siabnext.ttc.io/files/media/orweb-and-012.png).

![](/sites/siabnext.ttc.io/files/media/orweb-and-013.png)

*Figure 5: Settings Menu*

**Step 2:** Once in the *settings* section, scroll down to the **Privacy** section and **tap** ![](/sites/siabnext.ttc.io/files/media/orweb-and-014.png).

![](/sites/siabnext.ttc.io/files/media/orweb-and-015.png)

*Figure 6: User Agent option screen*

**Step 3:** You will be presented with a list of *User Agents*. **Tap** your choice (e.g. Tap *iPhone*  to set it.  Now any time you visit a website, it will think you are using an *iPhone*).

![](/sites/siabnext.ttc.io/files/media/orweb-and-016.png)

*Figure 7: A list of possible User Agents*


# 5. Clear your browser history

**Step 1:** To manually clear your browsing history and cache, and to hide the websites you have been visiting on your phone, **tap** on the menu icon (![](/sites/siabnext.ttc.io/files/media/orweb-and-011.png)) and press ![](/sites/siabnext.ttc.io/files/media/orweb-and-017.png).

**Step 2:** To automatically remove your browsing history and cache as you go to a new page, **Tap** on the menu icon (![](/sites/siabnext.ttc.io/files/media/orweb-and-011.png)) followed by ![](/sites/siabnext.ttc.io/files/media/orweb-and-012.png).

**Step 3:** In the **settings** screen, scroll down and **tap** *Clear Back History*.

![](/sites/siabnext.ttc.io/files/media/orweb-and-018.png)

*Figure 8: Setting the Clear Back History option*

Note: When you set this, you will not be able to press the back button to view web pages you have already visited.


# 6. Clear your cookies

**Note:** Deleting cookies will sign you out of any websites that you were logged into.

**Step 1:** **Tap** on the menu icon (![](/sites/siabnext.ttc.io/files/media/orweb-and-011.png)) found in the top right of the screen and **tap** **Settings**.

**Step 2:** Scroll down to the **Cookies** section and press ![](/sites/siabnext.ttc.io/files/media/orweb-and-019.png).

**Step 3:** **Tap** ![](/sites/siabnext.ttc.io/files/media/orweb-and-020.png) to confirm the deleting of cookies.

![](/sites/siabnext.ttc.io/files/media/orweb-and-021.png)

*Figure 9: Confirm deletion of cookies*

