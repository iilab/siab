

---

lang: xx
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to access the Internet using the Tor Browser

---

- [**3.0 How to Connect to the Tor Network**](#3.0)
- [**3.1.1 - Direct Access**](#3.1.1)
- [**3.1.2 - Restricted Access**](#3.1.2)
- [**3.2 Reconfigure access to the Tor Network**](#3.2)
- [**3.3 Getting bridge addresses**](#3.3)

<a name="3.0"></a>
## 3.0 How to Connect to the Tor Network ##

The first time that you start the **Tor Browser** you will be prompted to choose how it will access the Internet:

- [Direct Access](#3.1.1):  This option should be selected if your access to the Internet is not restricted and if the use of **Tor** **is not** blocked, banned or monitored where you are.

- [Restricted Access](#3.1.2): This option should be selected if your access to the internet is restricted or if the use of **Tor** **is** blocked, banned or monitored where you are.

These settings can be changed at any stage from within the **Tor Browser** without having to re-install the software. This may need to be done if situations in your location change or if you are visiting a different country.

Any subsequent time that you start the **Tor Browser** it will connect you to the **Tor** network with no additional configuration required. 


<a name="3.1.1"></a>
## 3.1.1 How to Connect to the Tor Network - Direct Access##

To configure the **Tor Browser** to access the **Tor** network directly, perform the following steps:

**Step 1**: **Navigate** to the *Tor Browser* folder, and then **double click** ![](/sbox/screen/tor-en-1/010.png) to activate the following screen:

![](/sbox/screen/tor-en-1/012.png)

*Figure 1: The Tor Network Settings panel*


**Step 2**: **Click** the ![](/sbox/screen/tor-en-1/013.png) button, which will open the **Tor Status** window that shows you the progress as the software connects to the **Tor Network**.

![](/sbox/screen/tor-en-1/014.png)

*Figure 2: The Tor Status windows, showing the connection progress*

A few moments later, the **Tor Browser** will activate a new browser window displaying the following screen:

![](/sbox/screen/tor-en-1/015.png)

*Figure 3: Tor Browser; successfully connected to the Tor network*

You can now browse the web with the protection of the *Tor network*.

**Note**: Every time you launch the **Tor Browser**, it will automatically open the *Tor Status* window (*Figure 2*) before starting the *Tor Browser* (*Figure 3*).


<a name="3.1.2"></a>
## 3.1.2 How to Connect to the Tor Network - Restricted Access##

If you live in an area where accessing the Tor Network directly, as described above, is not possible or risky, you can configure Tor to try and circumvent the obstacles that are in place.

**Step 1**: **Navigate** to the *Tor Browser* folder, and then **double click** ![](/sbox/screen/tor-en-1/010.png) to activate the following screen:

![](/sbox/screen/tor-en-1/012.png)

*Figure 4: The Tor Network Settings panel*

**Step 2**: **Click** the ![](/sbox/screen/tor-en-1/016.png) button which will open a new window. You will be asked three short configuration questions to help you access the **Tor Network**.

**Question 1:** *Proxy Access;*  If you need to access the Internet via a proxy check **yes** and then press ![](/sbox/screen/tor-en-1/017.png). If you do not use a proxy check **no** and then press ![](/sbox/screen/tor-en-1/017.png).

If you selected **yes** above, fill in your proxy settings on the following screen. If you do not know your proxy settings, check your regular browser settings. In **Firefox** you can find them in *Options* > *Advanced* > *Network* tab in *Connection* *Settings* section. In other browsers you may look for *Internet Options*. Use the *Help* feature within your browser for further assistance.

![](/sbox/screen/tor-en-1/018.png)

*Figure 5: Proxy settings screen*

**Question 2:** *Restricted Ports;* If you are accessing the Internet through a firewall that only allows access over certain ports, for example *port 80 or 443* for web browsing, select **yes** and press ![](/sbox/screen/tor-en-1/017.png) to configure the ports, otherwise select **no** and press ![](/sbox/screen/tor-en-1/017.png). 

![](/sbox/screen/tor-en-1/019.png)

*Figure 6: Port restriction configuration screen*

**Question 3:** *Censored Internet connection*; If you live in a country which is actively blocking or monitoring **Tor** traffic you can configure the **Tor Browser** to use a *Bridge* which will disguise the fact that you are using **Tor**. 

Once you have clicked ![](/sbox/screen/tor-en-1/017.png) after *question 2* you will be presented with a screen allowing you to paste in **Bridge addresses**.  See the section [Getting Bridge Addresses](#3.3) for instructions on obtaining bridge addresses.

![](/sbox/screen/tor-en-1/020.png)

*Figure 7: Tor Bridge configuration screen*

Once you have added the **bridge addresses** click ![](/sbox/screen/tor-en-1/021.png) to finish your configuration and connect to the **Tor Network**.

![](/sbox/screen/tor-en-1/014.png)

*Figure 8: The Tor Status windows, showing the connection progress*

A few moments later, the **Tor Browser** will activate a new browser window displaying the following screen:

![](/sbox/screen/tor-en-1/015.png)

*Figure 9: Tor Browser; successfully connected to the Tor network*

You can now browse the web with the protection of the *Tor network*.

**Note**: Every time you launch the **Tor Browser**, it will automatically open the *Tor Status* window (*Figure 8*) before starting the *Tor Browser* (*Figure 9*).

<a name="3.2"></a>
## 3.2 Reconfigure access to the Tor Network ##

At any stage, if you need to access the **Tor Network** a different way, for example if you have travelled to a country that blocks Tor, you can update your settings from within the browser. Click on the ![](/sbox/screen/tor-en-1/022.png) icon and select *Open Network Settings*.

![](/sbox/screen/tor-en-1/023.png)

*Figure 10: Tor Browser options*

You will be presented with a new window (*Figure 11*) that will allow you to change how the **Tor Browser** accesses the Internet. Tick the options you want and change their settings.  Once satisfied with the changes press ![](/sbox/screen/tor-en-1/024.png) and restart the **Tor Browser**.


![](/sbox/screen/tor-en-1/025.png)

*Figure 11: Tor Browser options*


<a name="3.3"></a>
## 3.3 Getting Bridge Addresses ###

In order to configure the **Tor Browser** to use **Bridges** you will need to get bridge addresses.  There are two main ways this can be done:

**Email**:

To get bridges by email, you will need either a Gmail or a Yahoo email account.  Send an email to  bridges@bridges.torproject.org with the subject *get bridges*.  After a few minutes you will receive an email with 3 bridges listed and some additional details.

![](/sbox/screen/tor-en-1/026.png)

*Figure 12: Email with bridges listed*

**Web Site**

If your access is not completely restricted you may be able to get **Bridge** addresses from the Tor website by visiting [https://bridges.torproject.org/](https://bridges.torproject.org/)

After opening the website you will need to perform three steps:

- Click on ![](/sbox/screen/tor-en-1/027.png)

- Click on ![](/sbox/screen/tor-en-1/028.png)

- Fill out the *captcha* and press ![](/sbox/screen/tor-en-1/029.png)

Once you have entered the *captcha* correctly you will be presented with three **Bridge** addresses.

![](/sbox/screen/tor-en-1/030.png)

*Figure 13: Bridge addresses received via the Tor Project website*


**Note**: The *Bridge Database* is designed to prevent anyone from easily learning all of the bridge addresses. At first, it appears to give you the same bridges each time. After a period time, however, it will eventually provide new addresses. 

After you received the bridge addresses copy them to the field in the window as in *Figure 7: Tor Bridge configuration screen* or *Figure 11: Tor Browser options*.

