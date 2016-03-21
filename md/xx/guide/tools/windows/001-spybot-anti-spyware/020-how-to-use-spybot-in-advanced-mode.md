

---

lang: xx
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Use Spybot in Advanced Mode

---

- [**3.0 About Advanced Mode**](#3.0)
- [**3.1 Advanced Mode Tools**](#3.1)
- [**3.2 Advanced Mode - Rootkit Scan**](#3.2)


<a name="3.0"></a>
## 3.0 About Advanced Mode ##

**Spybot** has *Default* and *Advanced* sections. The *Advanced Mode* lets you configure settings and perform additional task.

**Click** ![](/sbox/screen/spybot-en-1/16.png) in the *Start Center* window to display the *Advanced Tools* and *Professional Tools* options.

![](/sbox/screen/spybot-en-1/15a.png)

*Figure 1: Advanced Tools*


<a name="3.1"></a>
## 3.1 Advanced Mode Tools ## 

The free version of *Spybot* lets you use only some of the options available in the *Advanced Tools* and *Professional Tools* sections:

- **Report Creator** can be used to assist *Spybot* Technical Support teams in the event that you need help with *Spybot* software. The level of support available will usually depend on the version of software you are running - paid verse free  for example. While support forums are a useful source of knowledge to help decide if a file is harmful or not, we do recommend caution before submitting any files or logs from your computer if anonymity is a concern for you.

- **Settings** section lets you configure Language, Scope of scanning, Browsers Spybot-S&D will scan, etc.

- **Startup Tools** section lets you review in details processes active on your computer, programs that are run when your computer is starting, your system scheduled tasks, plugins, system services, installed programs, etc.

- **Rootkit Scan** section checks your computer operating system for presence of *rootkits*, malicious programs that hide at the system level, which makes them undetectable by standard anti-malware tools

<a name="3.2"></a>
## 3.2 Advanced Mode - Rootkit Scan ##

The **Rootkit Scan** can be used to flag suspicious files and registry entries for further analysis or for removing them. The steps below will show how to perform a *Rootkit Scan*.

**Step 1**. **Click** ![](/sbox/screen/spybot-en-1/61.png) from the *Advanced Tools* pane to activate the window below. Note *Quick scan test results*. 

![](/sbox/screen/spybot-en-1/57.png)

*Figure 5: Rootkit Scan*

**Step 2**. **Click** ![](/sbox/screen/spybot-en-1/58.png)

**Step 3**. **Select** the drives and registry entries you wish to scan. We recommend selecting all of the items available. **Click** ![](/sbox/screen/spybot-en-1/04.png). *Note* this scan can take long time (perhaps about an hour) to complete.

![](/sbox/screen/spybot-en-1/59.png)

*Figure 6: Rootkit Scan - select drives*

![](/sbox/screen/spybot-en-1/60.png)

*Figure 7: Rootkit Scan in progress*

When the scan has completed, *Search for rootkits* will display any suspicious files found. You can then review the findings and options to determine if the file is legitimate.  

![](/sbox/screen/spybot-en-1/62.png)

*Figure 7: Search for rootkits*

**Step 4**. **Right click** any found items to display the options:

![](/sbox/screen/spybot-en-1/63.png)

*Figure 8: rootkits scan options*

**Step 5**. **Select** *Show properties* to display details.

**Step 6**. **Select** *Scan file for malware* if this option is available. This will activate the *File Scan* window. The result of the scan will be shown as below.

![](/sbox/screen/spybot-en-1/64.png)

*Figure 9: File Scan - clean file*

**Note** Items with rootkit properties detected are not necessarily malware. Deleting such could cause an issue to another program. Refer to section **2.5 How to Scan for Threats** and **2.6 How to Restore a File** when dealing with files found during the *Rootkit Scan*

**Step 7**. When you sure that the item found is suspicious you may **Delete** it from your system.

If you are not sure about the found items, you may ask for ‘help’ in Spybot [RootAlyzer Forum](http://forums.spybot.info/forumdisplay.php?f=46) before you delete anything. The deletion is final and can not be recovered through the Quarantine. If you still want to remove the found items it is strongly recommended to [create a system restore point](http://windows.microsoft.com/en-us/windows/system-restore-faq) before doing that.


