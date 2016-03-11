

---

lang: xx
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: How to Scan for and Deal with Viruses Using avast!

---

List of sections on this page:  

- [**4.0 Before You Begin**](#4.0)
- [**4.1 A Short Guide to Dealing with Virus Outbreaks**](#4.1)
- [**4.2 An Overview of the avast! Main User Interface**](#4.2)
- [**4.3 How to Scan for Malware and Viruses**](#4.3)
- [**4.4 How to Perform a Full System scan**](#4.4)
- [**4.5 How to Perform a Folder Scan**](#4.5)
- [**4.6 How to Perform a Boot-time Scan**](#4.6)
- [**4.7 How to Deal with Viruses**](#4.7)
- [**4.8 How to Use the Virus Chest**](#4.8)
- [**4.9 Advanced Virus Removal Methods**](#4.9)
- [**4.10 Smart Scan**](#4.10)



<a name="4.0"></a>
### 4.0 Before You Begin ###

There are two basic parts to dealing with malware and other assorted viruses when using **avast!**. The first is scanning your computer to identify such threats. The second involves either deleting or moving such threats to the **avast!** *Virus Chest*. Deleting and/or moving malware and viruses to the *Virus Chest* effectively prevents them from interacting with other programs or files on the computer.

It may seem unusual to store malware or viruses in the *Virus Chest*. However, if they have attached themselves to important or sensitive information, you may want to recover or save that infected document, file or program as far as possible. Also in rare instances, **avast!** may misidentify legitimate files or programs as being malware or a virus, events referred to as 'false positives', those files or programs might be important to you or your computer operation, and you may want to examine them carefully, cure and recover.

The **avast!** *Virus Chest* is an electronic 'dead zone' or 'quarantine', where you can examine the virus and determine its potential threat by either researching it on the Internet, or submitting it to a virus laboratory - an option available in **avast!** when you right-click a virus listed in the *Virus Chest*. Double clicking a virus in the *Virus Chest* will *not* activate or run the malware or virus because the *Virus Chest* keeps it isolated from the rest of your system. 

**Tip**: Alternatively, you can transfer important or sensitive information to the **avast!** *Virus Chest* to keep it safe during a virus attack.

<a name="4.1"></a>
### 4.1 A Short Guide to Dealing with Virus Outbreaks ###

There are a number of precautions you can take to limit hostile or malicious threats to your computer system; for instance using updated anti-virus or anti-spyware programs like **avast!** and **Spybot**, avoiding dubious or problematic web sites or documents sent to you, or exercising extreme cation when inserting removable media to your computer. Please read more about those steps in [Preventing virus infection](/en/chapter_1_1) section of chapter [1. How to protect your computer from malware and hackers](/en/chapter-1). However, despite the precautions we sometimes find our computer infected by a virus. The following points are offered for consideration when dealing with a virus attack:
 
- Disconnect your computer from the Internet or the local network - physically. If you have a wireless connection, disconnect your computer from the wireless network itself. If possible, switch off and/or remove your wireless card. You should disconnect from the Internet all computers that are sharing a local network with your computer.

- Schedule a boot-time scan for all computers on the local network. Write down the names of any viruses that you find, so that you can research them - and then delete them, or move them to the **avast!** *Virus Chest*. To learn how to perform a boot-time scan, please refer to section [**4.6 How to Perform a Boot-time Scan**](#4.6).

- Even if a virus has been either deleted or repaired, repeat the previous step, and run boot-time scans on *all* computers, until **avast!** no longer displays any warning messages. Depending on the severity of the malware or virus attack, you may not have to perform a boot-time scan more than once.

For more information about dealing with malware or virus outbreaks, please refer to section [**4.9 Advanced Virus Removal Methods**](#4.9).

<a name="4.2"></a>
### 4.2 An Overview of the avast! Main User Interface ###

The **avast!** main user interface displays numerous tabs on the left side of the window including: *Overview*, *Scan*, *Tools*, and *Settings*. All the *Scan*, *Tools* and *Settings* tabs contain a menu of items discussed below.

To launch the main user interface **click** ![](/sbox/screen/avast-en-1/22.png) from the system tray (usually bottom-right corner of your computer screen)

![](/sbox/screen/avast-en-1/56.png)

*Figure 1: The Main User Interface* 

The following list briefly describes the functions of the main tabs and sub menus:

**Overview**: The main user interface page displays the working status of **avast!**.

**Scan**: This tab can be used to launch different scanning options including:

- *Smart scan* can perform scans below one-by-one;
- *Scan for viruses* like: *Quick Scan*, *Full System Scan*, *Removable Media Scan*, *Select Folder to Scan* and *Boot-time Scan* - discussed in details below;
- *Scan for outdated software*;
- *Scan for network threats* can check the security configuration of your home router and advise of settings that may need to be updated;
- *Scan for performance issues* - is only fully available in paid version of avast!;

**Tools**: This tab features a sub menu of tools including *Software Update*, *Browser Cleanup* and *Rescue Disk* described in Section [**3.2 avast! Additional Tools**](/en/howtouseavast#3.2)

**Settings**: This tab features a menu including *General*, *Active Protection*, *Antivirus* and *Update* as described below:

- **General** includes a section on 'Maintenance' were you can configure the *Logs* and *Virus Chest* size and history.

- **Active Protection** menu allows you configure settings for *File System*, *Mail* and *Web* scanning. **Note** it is recommended that you do not change the default settings unless you understand the impact of enabling/disable specific settings.

- **Antivirus** menu allows you to configure global settings for scanning including *Exclusions* and *Alerts*

- **Update** menu displays the current *Program* and *Virus Definitions* installed and allow manual update of both as described in Section [**3.1 How to Manually Update avast!**](/en/howtouseavast#3.1)

<a name="4.3"></a>
### 4.3 How to Scan for Malware and Viruses ###

In this section, you will learn about the available scan options, and how to use them. You will also learn how to perform a full system scan and a folder scan, as well as a boot-time scan. 

The *Scan* pane displays the five scan options available in **avast!**; to view them:

**Step 1**. **Click** ![](/sbox/screen/avast-en-1/57.png) 

**Step 3**. **Click** ![](/sbox/screen/avast-en-1/95.png) to activate the following screen:

![](/sbox/screen/avast-en-1/96.png)

*Figure 2: The Scan tab displaying the default Quick Scan option*

The following brief descriptions will help you to choose the appropriate scan option:

**Quick scan**: This option is recommended for users with a limited amount of time in which to scan for a potential or suspected threat.

**Full system scan**: This option is recommended when users have sufficient time to schedule a thorough scan of your system. It is also recommended if this is the first time you are using an anti-virus software on your computer. The duration of this scan depends on the number of documents, files, folders and hard drives on your computer, and the computer speed. Please refer to section [**4.4 How to Perform a Full system scan**](#4.4).

**Removable media scan**: This option is recommended for scanning external hard drives, USB flash drives, and other media, particularly those which are not your own. It will scan any removable device for malicious programs that automatically run whenever the device is connected.

**Select folder to scan**: This option is recommended for scanning either a specific folder or multiple folders, especially if you know or suspect, that a particular file or folder might be infected. Please refer to section [**4.5 How to Perform a Folder scan**](#4.5).

**Boot-time scan**: The boot-time scan lets you perform a full scan of your hard drive before the **Microsoft Windows** operating system fully starts running. This option is recommended for a complete and thorough scan of your computer system and may require some time. Please refer to section [**4.6 How to Perform a Boot-time Scan**](#4.6).

**Tip**:  **Clicking** ![](/sbox/screen/avast-en-1/59.png) lets you see and refine the details of the given scan, for instance, the areas being scanned.

<a name="4.4"></a>
### 4.4 How to Perform a Full System scan ###

**Step 1**. **Select** *Full System scan* option from the menu (see figure 2 above).

**Step 2**. **Click** ![](/sbox/screen/avast-en-1/60.png) to activate the following screen:

![](/sbox/screen/avast-en-1/61.png)

*Figure 3: The Scan pane displaying Full system scan/scan running...* 

After the full system scan has been completed, and if a threat to your computer has been found, the *Full system scan* pane may resemble the following screen:

![](/sbox/screen/avast-en-1/62.png)

*Figure 4: The Scan complete item displaying infected files found*

If the full system scan has revealed any threats **click** on ![](/sbox/screen/avast-en-1/69.png) button to open result page. please refer to section [**4.7 How to Deal with Viruses**](#4.7) for further steps.

<a name="4.5"></a>
### 4.5 How to Perform a Folder Scan ###

**Step 1**. **Select *Select folder to scan*** option from the menu (see figure 2 above).

**Step 2**. **Click** ![](/sbox/screen/avast-en-1/60.png) to activate the following screen:

![](/sbox/screen/avast-en-1/63.png)

*Figure 5: The Select the areas dialog box*

The *Select the areas* dialog box lets you specify the folder you would like to scan. You can select more than one folder for scanning purposes. As you check the boxes besides each folder, the folder path is displayed in the *Selected paths:* text field. 

**Step 3**. **Click** ![](/sbox/screen/avast-en-1/64.png) to begin scanning your folders, and activate the following screen:

![](/sbox/screen/avast-en-1/65.png)

*Figure 6: The Folder scan in progress.* 

**Tip**: **avast!** lets you scan individual folders though a pop-up menu that appears whenever you right-click on a folder. Simply **Select** *![](/sbox/screen/avast-en-1/66.png) Scan...* which appears besides the name of the folder you would like to scan for viruses.

If the folder scan has revealed any threats  **click** on ![](/sbox/screen/avast-en-1/69.png) button to open result page. please refer to section [**4.7 How to Deal with Viruses**](#4.7) for further steps.

<a name="4.6"></a>
### 4.6 How to Perform a Boot-time Scan ###

The **avast!** boot-time scan lets you perform a full scan of your hard drive before the **Microsoft Windows** operating system fully starts running. At the moment the boot-time scan is performed, all (or majority) of malware programs and viruses are still dormant, that is, they have not had the opportunity to activate themselves, or interact with other system processes yet. As such, they may be easier exposed and removed. The boot-time scan also directly accesses the disk, bypassing the drivers for the **Windows** file system, which may be infected. This further helps find more viruses and 'rootkits' - the name for a particularly malignant form of malware. 

It is **strongly recommended** that you run a boot-time scan even if there is only a remote suspicion that your computer system may be compromised or infected. The **boot-time scan** and the **rescue disk** (described in section [3.2.3 Rescue Disk](/en/howtouseavast#3.3.3)) options are the most complete and thorough scan of a computer system avast! has to offer. The boot-time scan may require some time, depending on your computer speed and the amount of data and number of hard drives you may have. 

To scan your system at boot time, perform the following steps:

**Step 1**. **Click** ![](/sbox/screen/avast-en-1/57.png) to activate the *Scan* pane.

**Step 2**. **Select** ![](/sbox/screen/avast-en-1/67.png) option from the drop down menu.   

**Step 3**. **Click** ![](/sbox/screen/avast-en-1/60.png) to schedule a boot-time scan the next time you start your computer.

**Step 3**. **Restart your computer** to start scanning.

**Note**: A boot-time scan starts before the operating system and interface are fully loaded; as such the progress of the scanning is displayed in the text on your screen as follows: 

![](/sbox/screen/avast-en-1/68.png)

*Figure 7: The avast! Boot-time scheduled scan*

**avast!** will prompt you for a response if viruses are detected. You select possible actions by pressing keys with appropriate numbers on your keyboard. We recommend that you **select key 2** *Fix all automatically* to let avast! deal with all the viruses automatically.

Note that moving infected file to the virus chest or removing it may result in some information or functionality of your system being inaccessible. In extreme situation, when a virus infected files vital for the functioning of the operating system, moving to chest or removing this file may result in your computer not being able to successfully start operating system again.

<a name="4.7"></a>
### 4.7 How to Deal with Viruses ###

Section 4.5 and 4.6 above demonstrated how to make avast! manually scan for viruses. When a virus is found in any of those scans avast! informs you about this as shown in *figure 8*. To begin dealing with any malware or viruses detected during a scan, perform the following steps:

![](/sbox/screen/avast-en-1/100.png)

*Figure 8: The Scan completed - threat detected*


**Step 1**. **Click** ![](/sbox/screen/avast-en-1/69.png) to activate the  following screen:

![](/sbox/screen/avast-en-1/70.png)

*Figure 9: The SCAN RESULTS window displaying THREAT DETECTED! warning*

**Step 2**. To display the drop-down list of possible actions to be applied, **click** the arrow beneath *Actions* as shown below.


![](/sbox/screen/avast-en-1/72.png)

*Figure 10: Actions - Move to chest* 


**Note**: In this exercise, we are concerned with moving infected files to the *Quarantine(Virus Chest)*. However, the drop-down list displays three other options and they are described below:

**Repair**: This action will attempt to repair the infected file.

**Delete**: This action will delete - permanently - the infected file.

**Do nothing**: This action means exactly what it says, and is *definitely not recommended* for treating potentially harmful malware or virus threats.

**Step 3**. **Select** the *Move to Chest* item, and then **click** ![](/sbox/screen/avast-en-1/71.png) 


![](/sbox/screen/avast-en-1/73.png)

*Figure 11: The detected threat has been moved to the Quarantine (Virus Chest)*

**avast!** is also constantly monitoring the computer for viruses and malware in the background as you continue to work. 
When *avast!* detects malware or a suspicious file, it will alert you with a message similar to the screen shot below. 

![](/sbox/screen/avast-en-1/81.png)

*Figure 12: The Virus found*

The default action will move the file to the *Quarantine (Virus Chest)*. The next section describes how to deal with any malware or viruses detected during a scan that have been moved to the *Quarantine Virus Chest*

<a name="4.8"></a>
### 4.8 How to Use the Virus Chest ###

During the **avast!** installation process, the **avast!** *Virus Chest* was created on your hard drive. The *Virus Chest* is a special folder isolated from the rest of your computer system, and used to store malware and viruses detected during the scan, as well as infected or threatened documents, files or folders. 

You can access content of the *Virus Chest* and decide how to deal with the files collected there:

**Step 1**. **Click** ![](/sbox/screen/avast-en-1/57.png) and **click** ![](/sbox/screen/avast-en-1/74.png) to activate the following screen:

![](/sbox/screen/avast-en-1/75.png)

*Figure 13: The Virus Chest displaying one virus*

**Step 2**: **Right click** on each item to display the menu of actions that can be applied to a selected file as follows:

![](/sbox/screen/avast-en-1/76.png)

*Figure 14: The pop-up menu of actions for viruses in the Virus Chest*

**Note**: Double clicking an item in the *Virus Chest* will not activate, open or run it. It will only display the file properties, basically the same information you would obtain by selecting *Properties* from the pop-up menu.

The following list describes the actions used to deal with viruses in the pop-up menu as follows:

**Delete**: The file will be deleted from the *Virus Chest* irreversibly.

**Restore**: The file will be restored to its original location.

**Extract**: The file will copied to a folder you will specify.

**Scan**: The file will be scanned.

**Submit to virus lab...**: Selecting this option will activate a virus submission form for you to fill out and submit the file for further analysis to avast! company lab. Do not submit files that may contain sensitive information!

**Properties**: This option will reveal more details about the file. 

**Add...**: This option lets you browse your system for other files you would like to add to the *Virus Chest*. This is potentially very useful if you have files you would like to protect during a virus outbreak.

**Refresh all files**: This option will update the list of the files in the *Virus Chest*, so that you will be able to view the latest files.

<a name="4.9"></a>
### 4.9 Advanced Virus Removal Methods ###

Sometimes the protection offered by **avast!**, **Comodo Firewall** and **Spybot** is simply not sufficient; despite best efforts, our computer system may become infected by malware and other viruses. In section [**4.1 A Short Guide to Dealing with Virus Outbreaks**](#4.1), a few methods were offered for dealing with persistent malware and viruses. However, there *is* more that can be done to eliminate such threats from your computer.

**Method A: Using Anti-malware Rescue CDs/DVDs or USB**

Some anti-malware software companies offer a free anti-virus 'rescue' CD/DVD. These can be downloaded in ISO image format (that is, a format that can be easily burned onto a CD or DVD or put on USB memory). 

To begin using these anti-malware rescue CDs/DVDs/USB, perform the following tasks:

1. Download specific rescue ISO (see the list below) and burn the anti-malware rescue program to a CD/DVD or put it on USB.  <br>
*You can use free program like [**ImgBurn**](http://www.imgburn.com/) to burn the image to the disk. Or you can use free program like [**Universal USB Installer**](http://www.pendrivelinux.com/universal-usb-installer-easy-as-1-2-3/) to put the image on the USB*<br>
**Note:** It is best to perform this step on some other, not infected computer if you can.

2. Insert the disk to CD/DVD player or connect USB to infected computers, and then restart your computer from this USB or CD/DVD.  <br>
*Often you can do this by pressing key F10 or F12 or Esc on your keyboard just after switching on the computer. Pay special attention to the instruction on the screen of your computer while it starts to learn how to do this on your computer. Search in the internet for the instructions on how to start (boot) your computer from USB or CD/DVD. Instructions may differ for each computer.*

3. Once the infected computer starts from the USB/CD/DVD re-connect it to the Internet so that the anti-malware rescue program will be able to update its virus definitions if necessary. <br>
*It may be better to connect to the Internet using cable connection if available*.

4. Begin scanning your computer hard drives to remove infections and malware threats. 

The following is a list of anti-virus rescue images available for free:

- [**Avira AntiVir Rescue CD**](https://www.avira.com/en/download/product/avira-rescue-system)
- [**AVG Rescue CD**](http://www.avg.com/us-en/avg-rescue-cd)
- [**BitDefender Rescue CD**](http://www.bitdefender.com/support/How-to-create-a-BitDefender-Rescue-CD-627.html)
- [**F-Secure Rescue CD**](http://www.f-secure.com/en/web/labs_global/rescue-cd)
- [**Kaspersky Rescue CD**](http://support.kaspersky.com/viruses/rescuedisk/)
- [**Dr.Web Live Rescue CD**](http://www.freedrweb.com/livecd/)

You may also find following resources with additional tools and methods very interesting and helpful:

- [**How to easily clean an infected computer (Malware Removal Guide)**](http://malwaretips.com/blogs/malware-removal-guide-for-windows/)
- [**Malware Removal Guide for Windows**](http://www.selectrealsecurity.com/malware-removal-guide)

**Note:** You can use each tool listed above separately to maximise your ability to effectively clean your computer.

**Method B: Re-Installing the Microsoft Windows Operating System**

In rare instances, a virus infection can be *so* destructive that the software tools recommended earlier may be rendered useless. In situations like this, we recommend that you perform the following tasks: 

***Note**: Before you begin, make sure you have all the appropriate license or serial numbers, and installation copies for the **MS Windows** operating system and other programs you require. This procedure may be time consuming but worth the effort if you can't eliminate malware and virus threats the other way.*

1. Create a backup copy of all your personal files on the computer.

2. Reinstall the **Microsoft Windows** operating system formatting the entire disk.

3. Update the **Microsoft Windows** operating system after the installation has been completed.

4. Install **avast!** (or your preferred anti-virus program) and update it.

5. Install whatever programs you require. Remember to download the latest versions and all the updates for each program. <br><br>**Note**: Under no circumstances should you connect your backup disk to your computer *before* you have successfully performed these tasks. You might risk infecting your computer again.

6. Connect your backup disk to your computer and scan it thoroughly to detect and eliminate any existing problems. 

7. After you have detected and deleted any problems, you may copy your files from the backup disk to the computer hard drive.

<a name="4.10"></a>
### 4.10 Smart Scan ##

*Smart Scan* can perform several scans discussed in this chapter all at once. This is a convenient way to run a 'health check' for malware detection, software updater and network security. In the example below, Smart Scan detects some out of date software that requires updating. 

**Step 1**. **Click** ![](/sbox/screen/avast-en-1/57.png) and ![](/sbox/screen/avast-en-1/36.png) to activate the screen shown below:


![](/sbox/screen/avast-en-1/84.png)

*Figure 19 : Smart Scan*

When *Smart Scan* has completed, the status of each scan will be displayed as shown in the screen below. 

![](/sbox/screen/avast-en-1/85.png)

*Figure 20 : Smart Scan - Issues found*

**Step 2**. **Click** ![](/sbox/screen/avast-en-1/86.png) to begin reviewing any issues detected. *Note GrimeFighter is not available in the free version of avast!* 

![](/sbox/screen/avast-en-1/39.png)

*Figure 21 : Software Updater screen*

**Step 3**. **Click** ![](/sbox/screen/avast-en-1/40.png) to begin updating each application that needs this.


![](/sbox/screen/avast-en-1/38.png)

*Figure 22: Software updated*

**Step 4**. Follow steps 1 to 3 above to reassess the health of your computer


