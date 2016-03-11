

---

lang: xx
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: Advanced Configurations and Settings

---

List of sections on this page:

- [**4.0 How to Access the COMODO Firewall Advanced Settings windows**](#4.0)
- [**4.1 The Firewall Behavior Settings window**](#4.1)
- [**4.2 The Defense+ Settings window**](#4.2)

-------

<a name="4.0"></a>
## 4.0 How to Access the **COMODO Firewall** Advanced Settings windows ##

The **COMODO Firewall** provides three main components to help protect your computer against threat - a Firewall, Host Intrusion Prevention System (HIPS) and Auto-Sandbox technology.

All three components are displayed in the main user of the **COMODO Firewall** 

![](/sbox/screen/comodo-en-1/21.png)

*Figure 1: The COMODO Firewall main user interface*

Each component can be configured with different levels of security known as *Behavior Settings* which will be discussed in the following sections. The *Behavior Settings* for both the *firewall* and *HIPS* can be change by **clicking** ![](/sbox/screen/comodo-en-1/38.png) to display a drop down menu. The *Auto-Sandbox* feature can be ![](/sbox/screen/comodo-en-1/42.png) or ![](/sbox/screen/comodo-en-1/43.png)  

Alternatively, you may access the options above by performing the following steps:

**Step 1**. **Open** the **COMODO Firewall** main user interface. 

**Step 2**. **Click** *Firewall*, *HIPS* or *Auto-Sandbox* to launch *Advanced Settings* for the respective component
  

![](/sbox/screen/comodo-en-1/39.png) 

*Figure 2: Firewall Advanced Settings* 


![](/sbox/screen/comodo-en-1/40.png)

*Figure 2: HIPS Advanced Settings* 


![](/sbox/screen/comodo-en-1/41.png)

*Figure 3: Sandbox Advanced Settings* 



**Tip**: Settings can also be easily and effectively set using the **COMODO Firewall** connectivity icon located in the *System Tray*. **Right click** the connectivity icon to activate the pop-up menu and sub-menu as follows:

![](/sbox/screen/comodo-en-1/44.png)

*Figure 4: The connectivity icon pop-up menu and the Firewall Security Level sub-menu* 

<a name="4.1"></a>
## 4.1 The Firewall Behavior Settings window ##

The **Firewall Behavior Settings** window lets you customize firewall security by using a variety of features and options, including the firewall security level, the number and type of security alerts received and packet analysis and monitoring.

![](/sbox/screen/comodo-en-1/45.png)

*Figure : The Firewall Settings*

The *Firewall Settings* lets you specify the level of security you think appropriate for **COMODO Firewall**. The drop down menu allows you choose among the following options:

**Block All**: This mode stops all Internet-related traffic and overrides any firewall configurations and rules you have specified. It will neither generate traffic rules for applications, nor record or 'learn' their behaviours.

**Custom Ruleset**: This mode applies *only* the user-defined **COMODO Firewall** security policies and network traffic policies that you have previously defined in the *Security Settings > Firewall > Ruleset* and the *Defense+ > HIPS > HIPS Ruleset* windows. 

**Safe Mode**: This mode is the default setting for the **COMODO Firewall** installations. 


**Tip**: **COMODO Firewall** maintains an internal list of commonly used applications and files verified as safe, and does not issue pop-up alerts for them.  

**Warning**: Both the *Training Mode* and disabling the firewall by unticking the *Enable Traffic Filtering* options are not recommended as they may compromise the effectiveness of **COMODO Firewall** and expose your system to the risk of infection. 

<a name="4.2"></a>
### 4.2 The Defense+ Settings window ###

**Note**: The features and options described in this section require a profound understanding of firewalls and related security issues, and is designed largely with the **Advanced** user in mind.

The HIPS and Sandbox components of the **COMODO Firewall** are enabled by default during the installation process. Both features are grouped under the advanced settings menu as *Defense+* 

Any computer connected to a network is technically speaking, a host computer. The *Defense+* components constantly monitor the activities of all executable files currently residing on your computer. An executable file is simply an application or program, or a part if it, and typically but not exclusively, is identified by the following file extensions: *.bat*, *.exe*, *.dll*, *.sys*, and others. 

*Defense+* components issue pop-up warnings every time an unknown executable file attempts to run, and prompts you to either allow or block its functioning. It may prove important in situations where any type of maleware will attempt to install applications or programs to damage or steal your personal information, reformat your hard disk or hijack your computer, and use it to propagate malware or spam - without your consent or knowledge.

### 4.2.1 The Defense+ Settings - HIPS ###

To change the behaviour settings of HIPS perform the following steps:

**Step 1**. **Click** *HIPS* ![](/sbox/screen/comodo-en-1/46.png) to activiate the screen below 

![](/sbox/screen/comodo-en-1/40.png)

*Figure 5: HIPS Behavior Settings*

**Step 2**. **Click** on the drop down menu to select a security level mode and **click** ![](/sbox/screen/comodo-en-47.png) 

The *HIPS* security levels resemble the *Firewall Behavior* security levels which offers similar options, and lets you choose the optimal level of host intrusion protection for your system. 


**Paranoid Mode**: This mode is the highest available level of security, and monitors all and any executable files apart from those you have specified as safe, including those on the *Trusted Software Vendor* list. It generates the greatest number of security alerts, and system activity is filtered through your configuration settings.  

**Safe Mode**: This mode will automatically 'learn' the behaviours of different application executables, while monitoring critical system activity. Every uncertified application will generate a *Security Alert* whenever it runs. This mode is the most widely recommended for the majority of users. 

**Clean PC Mode**: This mode learns the activities of the applications currently installed on the computer while all new executables introduced to the system are monitored and controlled. 


By unticking the *Enable HIPS*, you can manually disable the host intrusion prevention system. This option is generally not recommended.

  
### 4.2.2 The Defense+ Settings - Sandbox ###


The **Sandbox** component provides a fully functional sandbox called the 'Virtual Desktop'. This is an isolated operating environment for running unknown, untrusted and suspicious applications. Applications executed inside the sandbox/virtual desktop will not affect other processes, programs or data on your real computer. In addition to running suspicious applications inside the sandbox on an ad-hoc basis, you can create a specific list of programs that should always run in the sandbox.

Advanced settings for this powerful feature can be configured by **clicking** ![](/sbox/screen/comodo-en-1/48.png) 

![](/sbox/screen/comodo-en-1/41.png)

*Figure 6: The Defense+ Sandbox Advanced settings*

**Note**: **Experienced** and **Advanced** users are strongly encouraged to **click** ![](/sbox/screen/comodo-en-1/49.png) and **select** *Online Help* to access the extensive **COMODO** online help concerning *HIPS Settings* and *Sandbox Settings*. Alternatively, you can refer to **https://help.comodo.com/topic-72-1-623-7587-Introduction-to-Comodo-Internet-Security.html** to choose from a list of online help topics.


