

---

lang: en
community: guide
type: tools
os: android
weight: 000
title: Basic Android security setup guide

---

This guide lists steps you should consider taking when setting up your Android phone (or device). However, before implementing below changes, it is strongly recommended that you read [**How to use mobile phones as securely as possible**](../mobile-phones) and [**How to use smartphones as securely as possible**](../smartphones). Those two guides will help you make informed decisions about what you store on your Android device and how you communicate with it.


# Required reading


:[Use mobile phones as securely as possible](../../../tactics/mobile phones)


:[Use smartphones as securely as possible](../../../tactics/smartphones)


:[Basic Android security setup guide](basic-android-security-setup-guide)

# What you will get from this guide


# 1. Security-related settings for Android

### 1.1 Access to your phone ###

**Enable** *Lock SIM card*, found under *Settings -> Personal -> Security -> Set up SIM card lock*. This will mean that you must enter a PIN number in order to unlock your SIM card each time your phone is switched on, with out the PIN no phone calls can be made.

**Set up** a *Screen Lock*, found under *Settings -> Personal -> Security -> Screen Lock*, which will ensure that a code, pattern or password needs to be entered in order to unlock the screen once it has been locked. We recommended using the *PIN* or *Password* option, as these are not restricted by length. You can find more information on creating strong passwords in [**How to create and maintain secure passwords**](../passwords).

**Set** the *security lock timer*, which will automatically lock your phone after a specified time. You can specify a value which suits you, depending on how regularly you are willing to have to unlock your phone.

### 1.2 Device Encryption ###

If your device uses Android version 4.0 or newer, you should **turn on** *device encryption*.  This can be done in *Settings -> Personal -> Security -> Encryption*. Before you can utilise device encryption, however, you will be required to set a screen lock password (described above).

**Note:** Before starting the encryption process, ensure the phone is fully charged and plugged into a power source.

### 1.3 Network settings ###

**Turn off** Wi-Fi and Bluetooth by default. Ensure that *Tethering* and *Portable Hotspots*, under *Wireless and Network Settings*, are switched off when not in use.  *Settings -> Wireless & Networks -> More -> Tethering & Mobile hotspot*.

If your device supports *Near Field Communication (NFC)*, this will be switched on by default, and so must be switched off manually.

### 1.4 Location settings ###

**Switch off** *Wireless and GPS* location (under *Location Services*) and mobile data (this can be found under *Settings -> Personal -> Location*). 

**Note**: Only turn on location settings as you need them. It is important not have these services running by default in the background as it reduces the risk of location tracking, saves battery power and reduces unwanted data streams initiated by applications running in the background or remotely by your mobile carrier.

### 1.5 Caller Identity ###

If you want to hide your caller-ID, go to *Phone Dialler -> settings -> Additional Settings -> Caller ID -> hide number*. 

### 1.6 Software Updates ###

To ensure that you phone remains secure it is strongly recommended to keep your software updated. There are two types of updates that need to be checked:

1. The phone operating system:  go to: *settings -> About phone -> updates -> check for updates*.

2. Apps you have installed: Open the **Play store** app, from the *side menu* select **My Apps**.   

**Note:** When updating your phones software it is important to do it from a trusted location such as your internet connection at home instead of somewhere like an internet cafe or coffee shop.


# 2. Apps for Android





## 2.1 Recommended Android Apps

We have a number of Tools Guides for Android apps that we recommend installing on your device. These guides will walk you through installing, configuring and using the apps on your Android Devices.

![](/sites/siabnext.ttc.io/files/media/apg.png)

**[APG](../apg/android)**

**License:** FOSS (GPL v3)  / **Requirements:** Android 1.5 and up.

**Details:** lets you encrypt and decrypt single files or emails, for personal use or to share with others, using either public key cryptography or a passphrase. 

![](/sites/siabnext.ttc.io/files/media/chatsecure.png)

**[ChatSecure](../chatsecure/android)**

**License:** FOSS (GPLv3)    / **Requirements:** Android 1.6 and up.

**Details:**  Is an Instant Messaging client that lets you organize and manage your different Instant Messaging (IM) accounts using a single interface. It will also attempt to encrypt your conversations using OTR when chatting with contacts who also use IM clients that support OTR.

![](/sites/siabnext.ttc.io/files/media/k9.png) ![](/sites/siabnext.ttc.io/files/media/apg.png)

**[K-9 Mail and APG](../k9/android)**

**License:** FOSS (Apache 2.0)   / **Requirements:** Android 1.5 or up.

**Details:** K-9 Mail is a mail client that integrates with **APG** to allow you easily send and receive GnuPG encrypted emails.

![](/sites/siabnext.ttc.io/files/media/keepassdroid.png)

**[KeePassDroid](../keepassdroid/android)**

**License:** FOSS (GPL v2)  / **Requirements:** Android 1.5 and up.

**Details:** is a secure and easy-to-use password management tool which will store your passwords in an encrypted database on your phone.

![](/sites/siabnext.ttc.io/files/media/obscuracam.png)

**[Obscuracam](../obscuracam/android)**

**License:** FOSS (GPL v3)   / **Requirements:** Varies by device.

**Details:**  is a free camera application for Android devices that has the ability to recognize and hide faces. It allows you to blur or delete the faces of those you photograph in order to protect their identities.

![](/sites/siabnext.ttc.io/files/media/orbot.png)

**[Orbot](../orbot/android)**

**License:** FOSS (BSD)  / **Requirements:** Android 2.3 and up.

**Details:** is an app that is designed to increase the anonymity of your activities on the Internet by sending your connections over the Tor network.

![](/sites/siabnext.ttc.io/files/media/orweb.png)

**[Orweb](../orweb/android)**

**License:** FOSS (GPL v2)  / **Requirements:** Android 1.6 and up.

**Details:** is a web browser that is used in conjunction with Orbot, that allows you to send all your web browsing over the Tor network.

![](/sites/siabnext.ttc.io/files/media/redphone-small.png)

**[RedPhone](../redphone/android)**

**License:** FOSS (GPL v3) / **Requirements:** Android 2.3 and up.

**Details:** Allows you to make encrypted phone calls over the internet.  A valid phone number is required to register.

![](/sites/siabnext.ttc.io/files/media/textsecure.png)

**[TextSecure](../textsecure/android)**

**License:** Freeware (GPL v3) / **Requirements:** Android 2.3 and up.

**Details:** is an app to send encrypted text messages (SMS) via your phone provider and encrypted messages over WiFi and your phones internet connection as well as storing all SMS and messages in an encrypted container on your phone.


## 2.2 Additional Android apps for non-rooted devices

Along with the software covered by our Tools Guides for Android, we also suggest the following apps.

![](/sites/siabnext.ttc.io/files/media/applock.png)

**[Applock](https://play.google.com/store/apps/details?id=com.domobile.applock)**

**License:** Commercial  / **Requirements:** Dependant on device.

**Details:** Allows you to password protect apps on your phone so that they can not be run with out entering the correct passphrase. For example protect your Mail app with additional passphrase.


![](/sites/siabnext.ttc.io/files/media/avira.png)

**[Avira](https://play.google.com/store/apps/details?id=com.avira.android)**


**License:** Commercial  / **Requirements:** Android 2.2 and up.

**Details:** Anti-Virus software that will scan your phone for malicious apps and files.  It will also allow you to locate your phone if lost.


![](/sites/siabnext.ttc.io/files/media/cerberus.png)

**[Cerberus](https://play.google.com/store/apps/details?id=com.lsdroid.cerberus)**


**License:** Proprietary   / **Requirements:** Android 4.0.3 and up.

**Details:** An anti-theft solution that will allow you to locate your phone if lost or stolen.  It will also allow you to remotely lock or wipe the contents of your phone.

![](/sites/siabnext.ttc.io/files/media/firefox.png)

**[Firefox](https://play.google.com/store/apps/details?id=org.mozilla.firefox)**

**License:** FOSS  / **Requirements:** Dependant on device

**Details:** brings the experience of [Firefox Browser for the desktop](../firefox/windows) to your mobile phone.

![](/sites/siabnext.ttc.io/files/media/notecipher.png)

**[Notecipher](https://play.google.com/store/apps/details?id=info.guardianproject.notepadbot)**

**License:** FOSS (Apache v2)   / **Requirements:** Android 3.0 and up.

**Details:** A note taking application that stores all notes in an encrypted container protected by a passphrase.

![](/sites/siabnext.ttc.io/files/media/openvpn.png)

**[OpenVPN for Android](https://play.google.com/store/apps/details?id=de.blinkt.openvpn)**

**License:** FOSS (GPL v2)   / **Requirements:** Android 4.0 and up.

**Details:** Allows you to tunnel your apps, that connect to the internet, over OpenVPN based VPNs, protecting you from monitoring.

![](/sites/siabnext.ttc.io/files/media/panicbutton.png)

**[Panic Button](https://play.google.com/store/apps/details?id=org.iilab.pb)**

**License:** FOSS (GPL v3)  / **Requirements:** Android 2.3.3 and up.

**Details:** Allows you to secretly trigger your phone to send an SMS letting a predefined list of contacts know you may be in danger.

![](/sites/siabnext.ttc.io/files/media/psiphon3.png)

**[Psiphon3](https://s3.amazonaws.com/0ubz-2q11-gi9y/en.html)**

**License:** FOSS (GPL v3)   / **Requirements:** Dependant on device.

**Details:** helps you to try and circumvent censorship and monitoring by tunneling your internet connection over a number of different encrypted tunnel types such as VPNs and Proxies.

![](/sites/siabnext.ttc.io/files/media/spideroak.png)

**[Spideroak](https://play.google.com/store/apps/details?id=com.spideroak.android)**

**License:** Proprietary  / **Requirements:** Dependant on device.

**Details:** is a file synchronisation tool that will allow you to easily share files between your computers and Android devices via an intermediary 3rd party server on the internet.  All files are encrypted by the app before being uploaded to the Spideroak servers.


![](/sites/siabnext.ttc.io/files/media/surespot.png)

**[Surespot](https://play.google.com/store/apps/details?id=com.twofours.surespot)**

**License:** FOSS (GPL v3+) / **Requirements:** Android 2.3.3 and up.

**Details:** an secure messaging app that provides end to end encryption for all messages and files sent. No personal details (phone, email) are required for registration.


## 2.3 Additional Android apps for rooted devices

The following apps are for advanced users of Android and require your phone to be [rooted](/en/glossary#rooting).

![](/sites/siabnext.ttc.io/files/media/afwall.png)

**[AFwall+](https://play.google.com/store/apps/details?id=dev.ukanth.ufirewall)**

**License:** FOSS (GPL v3)   / **Requirements:** Android 2.2 and up.

**Details:** A firewall for your android device that allows you to control what apps can access the internet.

![](/sites/siabnext.ttc.io/files/media/cryptfs.png)

**[CryptFS](https://play.google.com/store/apps/details?id=org.nick.cryptfs.passwdmanager)**

**License:** FOSS (Apache v2)  / **Requirements:** Android 3.0 and up.

**Details:** lets you to change your Android disk encryption password meaning you can have a one passphrase to decrypt the phone when you turn it on and a different one to unlock the phone during normal use.

![](/sites/siabnext.ttc.io/files/media/cryptonite.png)

**[Cryptonite](https://play.google.com/store/apps/details?id=csh.cryptonite)**

**License:** FOSS (GPL v2)  / **Requirements:** Android 2.2 and up.

**Details:** allows you to create encrypted, passphrase protected, containers on your Android device that you can store sensitive files in.

![](/sites/siabnext.ttc.io/files/media/snoopsnitch.png)

**[SnoopSnitch](https://play.google.com/store/apps/details?id=de.srlabs.snoopsnitch)**

**License:** FOSS (GPL v3)  / **Requirements:** Android 4.1 - 4.4 and only [specific handsets](https://opensource.srlabs.de/projects/snoopsnitch#Requirements).

**Details:** is an Android app that collects and analyses mobile radio data to make you aware of your mobile network security and to warn you about threats like fake base stations (IMSI catchers), user tracking and over-the-air updates.

![](/sites/siabnext.ttc.io/files/media/xprivacy.png)

**[X-Privacy](https://play.google.com/store/apps/details?id=biz.bokhorst.xprivacy.installer)**

**License:** FOSS (GPL v3)  / **Requirements:** Android 4.0.3 and up.

**Details:** is an app that will prevent your Android device from leaking sensitive information (such as your phone number, contacts, location, etc) to other installed apps on your phone. While x-privacy is free, there is a Pro version that can be purchased, which allows you to download *restriction rules* rather than you having to make them your self.

