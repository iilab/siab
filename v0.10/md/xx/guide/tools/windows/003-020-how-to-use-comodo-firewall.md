

---

lang: xx
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Use COMODO Firewall

---

List of sections on this page:

- [**3.0 An Overview of the COMODO Firewall Main User Interface**](#3.0)
- [**3.1 How to view COMODO Firewall Tasks**](#3.1)
- [**3.2 How to Allow and Block Access Using COMODO Firewall**](#3.2)



<a name="3.0"></a>
## 3.0 An Overview of the COMODO Firewall Main User Interface ##

A firewall is a program designed to protect your computer from malicious hackers and malware attempting to directly access your computer, or send information from your computer to a third party. **COMODO Firewall** features an extensive control panel with numerous customisable features and options. **Beginner** level users will quickly learn how to deal with **COMODO Firewall** security alerts, while **Experienced** and **Advanced** users will learn about more complex firewall configuration and management. 

**Comodo Firewall** includes two enhanced security features - *HIPS* and *Sandbox*. By Default, HIPS (host intrusion prevention system) is automatically enabled. Both tools will be discussed in the next section *Advanced Configuration and Settings* 

To view the **COMODO Firewall** main user interface in detail, open in the *Advanced View* as described in the previous section. 

![](/sbox/screen/comodo-en-1/24.png)

*Figure 1: Main User Interface - Advance View*

The *Firewall* pane displays a clear and concise summary of inbound and outbound requests from processes and programs attempting to get through the **COMODO Firewall**. Quite typically, there are more outbound requests than inbound. The default operating mode is *Safe Mode*, and different operating modes will be outlined later in *Advanced Configuration and Settings*. Follow the steps below to view details of and action for active connections. 

**Step 1**: **Click** ![](/sbox/screen/comodo-en-1/25.png) to activate the corresponding detailed summary of the outbound requests at a given moment 

![](/sbox/screen/comodo-en-1/26.png)

*Figure 2: An example of the Active Connections window displaying Internet traffic details*

**Step 2**: **Right-Click** on the application or process to view more information or to stop the process. *Note* stopping an application or process can be useful if your Internet service suddenly slows down or stalls for an unknown reason. If you have reason to suspect a malicious process or program is either downloading itself or in operation, stop the process immediately, you can always re-enable if found to be a false positive.

![](/sbox/screen/comodo-en-1/27.png)

*Figure 3: Active Connections options* 


<a name="3.1"></a>
## 3.1 How to view COMODO Firewall Tasks ##

Access to many tools and features offered by **Comodo Firewall** is available from the *Tasks* panel. A summary of the most commonly used features are listed below. Options range from basic to more advanced settings. 

**Click** ![](/sbox/screen/comodo-en-1/36.png) from the main user interface to display the following:

![](/sbox/screen/comodo-en-1/37.png)

*Figure 4: General Tasks menu* 

  
**General Tasks** : Allows you to quickly perform antivirus scans, update the virus database, manage quarantined files, view CIS event logs, view and manage internet connections.

**Firewall Tasks** : 

- Configure Internet access rights per-application through *Allow* and *Block* Applications
- View and configure access to all wired and wireless networks to which your computer is connected through *Manage Networks*
- Block all network traffic in and out of your computer through *Stop Network Activity*. This may be necessary if you have reason to suspect a malicious process or program is either   downloading itself or in operation.
- Port Stealthing is a security feature whereby ports on an Internet connected PC are hidden from sight
- View *Advanced Settings* menu to specify overall firewall behaviour and configure advanced settings such as application rules, rule sets, network zones and port sets.

**Advanced Tasks** : Allows you to create a *Create Rescue Disk* to run virus scans in pre-boot environments, manage priorities through *Task Manager*, and launch *Advanced Settings* to configure overall behaviour, define custom rulesets and much more.

**Note** The *Sandbox* tool will be outlined later in *Advanced Configuration and Settings* section.

<a name="3.2"></a>
## 3.2 How to Allow and Block Access Using COMODO Firewall ##

**Comodo Firewall** must be configured to 'learn' or record which applications are 'safe' and permit access to them, while blocking requests from unsafe software and rogue processes to your system. It may take a little experience over time to determine which requests are legitimate, and which are threats.

A firewall is simply a set of rules for monitoring inbound and outbound traffic. Every time you click *Allow* or *Block* **COMODO Firewall** generates a rule for that process or program network connection request. **COMODO Firewall** does this for both new or unrecognised processes and programs while permitting those listed in the *Trusted Software Vendors* list, in the *Firewall -> Security settings -> File Rating* window.

Every time **Comodo Firewall** receives a connection request from a new or unrecognised processes and programs, it activates a pop-up *Firewall Alert* prompting you to either *Allow* or *Block* access to your system to and from the Internet. To help you become more familiar with firewall alerts and how to use them, the example below shows the firewall has blocked **Firefox** from running with a *Firewall Alert* resembling the following:

![](/sbox/screen/comodo-en-1/28.png)

*Figure 5: An example of a COMODO Firewall Alert*

**Remember my answer**: This option is used to record whether you allowed or blocked a certain program from accessing **COMODO Firewall**. It will automatically allow or block connection requests from this program the next time it attempts to connect to your computer, based on whatever choice you have specified here. 

**Important**: We strongly recommend disabling the *Remember my answer option* when you first start using **COMODO Firewall**. Decide whether to allow or block different connection requests, and then observe how or if your decision affects your system operation. Enable the *Remember my answer* option if and *only* if you are completely sure of your decision.

**Tip**: Being strict about limiting access to you system is the best approach to computer security. Do not hesitate to block any suspicious or unidentifiable requests. If this causes a normal program to stop functioning correctly, you can allow the process to run next time you receive a firewall alert. 

**Click** ![](/sbox/screen/comodo-en-1/30.png) to activate the *Process Activities List* to learn more about the process or program requesting access, as shown in the following screen:

![](/sbox/screen/comodo-en-1/29.png)

*Figure 6: The firefox.exe Process Activities List*

If you have either determined a request is unsafe, or are simply uncertain about it, based on the information displayed in the *Process Activities List*,  **click** ![](/sbox/screen/comodo-en-1/31.png) to direct **COMODO Firewall** to deny access to your system.

If you have determined that a legitimate program is making a non-malicious request, based on the information displayed in the program *Process Activities List* screen, then **click** ![](/sbox/screen/comodo-en-1/32.png) to allow it access to your system.

Given that **Firefox** is a safe program, **check** the ![](/sbox/screen/comodo-en-1/33.png) option so that **COMODO Firewall** will allow **Firefox** to automatically access your system the next time. 

Alternatively, programs can be be added to the *Allow* or *Block* list by clicking *Tasks* from the main user interface and selecting *Firewall Tasks* as shown below.


![](/sbox/screen/comodo-en-1/35.png)

*Figure 7: Firewall Tasks - Allow Application*


![](/sbox/screen/comodo-en-1/34.png)

*Figure 8: Select and add firefox.exe to the Allow Application List*
  
Your ability to make the correct allow or block decisions will improve as you become more confident and experienced in using **COMODO Firewall**. 


