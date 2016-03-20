

---

lang: xx
community: guide
type: tools
legacy: True
child: True
os: android
weight: 2
depth: 3
title: Orbot and Orfox - Usage

---

### 3. How to Use Orbot and Orfox ###

- [**3.0 Basic Usage**](#3.0)
    - [**3.0.1 Starting and Stopping Orbot**](#3.0.1)
    - [**3.0.2 Browsing the internet anonymously with Orfox**](#3.0.2)


- [**3.1 Advanced Usage**](#3.1)
    - [**3.1.1 New Identity**](#3.1.1)
    - [**3.1.2 Using Bridges**](#3.1.2)
    - [**3.1.3 Auto Starting Orbot**](#3.1.3)

---

<a name="3.0"></a>
## 3.0 Basic Usage ##

<a name="3.0.1"></a>
## 3.0.1 Starting and Stopping Orbot ##

**Step 1:** **Touch and hold** the grey **Orbot** icon in the centre of the screen until it turns yellow and says *Orbot is starting*.

![](/sites/siabnext.ttc.io/files/media/orbot-android-en-013.png) ![](/sites/siabnext.ttc.io/files/media/orbot-android-en-014.png) 

*Figures 1 and 2: Activating Orbot*

**Step 2:** The first time you start **Orbot** a notification will appear to confirm you connected successfully to the **Tor** network. **Tap** ![](/sbox/screen/orbot-en-1/016.png) to see the green **Orbot** indication that **Orbot** is running.

![](/sites/siabnext.ttc.io/files/media/orbot-android-en-015.png) ![](/sites/siabnext.ttc.io/files/media/orbot-android-en-016.png) 

*Figures 3 and 4: Orbot finishes connecting*

**Note:** You wil only see the notification screen (Fig. 3) the first time you start **Orbot** after installation.

**Step 3:** To disconnect **Orbot** you **touch and hold** the green **Orbot** until it turns grey.  Or if you want to disconnect and quit **Orbot**, **tap** the menu icon (![](/sbox/screen/orbot-en-1/019.png)) in the top right of the screen and select ![](/sbox/screen/orbot-en-1/020.png) .

![](/sites/siabnext.ttc.io/files/media/orbot-android-en-017.png)

*Figures 5: Exiting Orbot*


<a name="3.0.2"></a>
## 3.0.2 Browsing the internet anonymously with Orfox ##

In order to browse or chat on the internet anonymously, you need to install an app (browser or chat) which can route your communication through a proxy in conjunction with **Orbot**. **Orfox** serves this function.  After you start **Orbot**, then go to **Orfox** and click on *Check Tor Connection* to make sure that you are connected to the Onion Network.  If you are connected you will get a message that looks like the following:

![](/sites/siabnext.ttc.io/files/media/orbot-android-en-018.png)

Thus, you can begin to browse the internet anonymously with Orfox.  *To note: Orfox has certain options available by default including NoScript and HTTPS Everywhere which increase your browsing security*.

 
<a name="3.1"></a>
## 3.1 Advanced Usage ##

<a name="3.1.1"></a>
## 3.1.1 New Identity ##
If at any stage you want to appear to come from a new location, you can get a *new identity* from **Orbot** by **swiping** *left* or *right* on the green **Orbot** image.  The image will briefly spin and then display *You've switched to a new Tor Identity*.


![](/sites/siabnext.ttc.io/files/media/orbot-android-en-020.png)

*Figure 6: Getting a new Tor Identity*

<a name="3.1.2"></a>
## 3.1.2 Using Bridges ##

If **Tor** access is restricted or you wish to disguise the fact that you are using **Tor**, you can configure **Orbot** to use **bridges**.

**Step 1:** **Tap** the ![](/sbox/screen/orbot-en-1/023.png) icon at the top of the screen to be brought to the settings screen.

**Step 2:** Scroll down to the **bridges** section and check the box next to *Use Bridges*.

![](/sbox/screen/orbot-en-1/024.png)

*Figure 7: Enabling Bridges*

**Step 3:** **Tap** the *Bridges* section underneath *Use Bridges* to be presented with a screen to enter the *IP address* of the *bridge* you want to use. Once correctly entered, **tap** ![](/sbox/screen/orbot-en-1/025.png). Restart **Orbot** to begin using the *bridge*.

![](/sbox/screen/orbot-en-1/026.png)

*Figure 8: Adding a bridge*

**Note:** to learn more about how to get bridge addresses see the [Tor Hands on Guide](/en/tor_anonymitynetwork#3.3).

<a name="3.1.3"></a>
## 3.1.3 Auto Starting Orbot ##

To make sure you never forget to start **Orbot** it can be configured to start when you turn on your Android Device.

**Step 1:** **Tap** the ![](/sbox/screen/orbot-en-1/023.png) icon at the top of the screen to be brought to the settings screen.

**Step 2:** **Check** the *Start Orbot on boot* option at the top of the settings screen.

![](/sbox/screen/orbot-en-1/027.png)

*Figure 9: Starting Orbot automatically*


