

---

lang: xx
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: How to Install and Configure Eraser

---

List of sections on this page:

- [**2.0 How to Install Eraser**](#2.0)
- [**2.1 How to Configure Eraser**](#2.1)

-------

<a name="2.0"></a>
## 2.0 How to Install Eraser ##

Installing **Eraser** is an easy and quick process. To begin installing **Eraser**, perform the following steps:

As described in the How-to Booklet chapter [**6. Destroying Sensitive Information**](/chapter-6), **Eraser** wipes data from your hard disk by overwriting it with random information. The more times you overwrite the data, the less likely that it will be recovered.

**Step 1**. **Double click** ![](/sbox/screen/eraser-en/01.png); the *Open File - Security Warning* dialog box may appear. If it does, **click** ![](/sbox/screen/eraser-en/02.png) to activate the *InstallAware Wizard*; after some moments, the *Welcome to the InstallAware Wizard for Eraser* screen will appear.

**Step 2**. **Click** ![](/sbox/screen/eraser-en/03.png) to activate the *License Agreement* screen, and then **click** checkbox to enable the *I accept the terms of the license agreement* option, and then **click** ![](/sbox/screen/eraser-en/03.png) again to activate the *Important Information* window.

**Step 3**. **Click** ![](/sbox/screen/eraser-en/03.png) after reading the contents displayed in the scrolling window to activate the *Destination Folder* window and then **click** ![](/sbox/screen/eraser-en/03.png) again.

**Step 4**. **Click** ![](/sbox/screen/eraser-en/03.png) to activate the following screen:

![](/sbox/screen/eraser-en/04.png)

*Figure 1: The Select Program Folder window*

**Step 5**. **Check** the *Only for me (current user)* option to ensure that only you are permitted to use **Eraser**, and then **click** ![](/sbox/screen/eraser-en/03.png) to activate the *Completing the InstallAware Wizard for Eraser* window.

**Step 6**. **Click** ![](/sbox/screen/eraser-en/03.png) and then **click** ![](/sbox/screen/eraser-en/05.png) to complete the installation process, and to run **Eraser** as follows:

![](/sbox/screen/eraser-en/06.png)

*Figure 2: The Eraser main user interface*

<a name="2.1"></a>
## 2.1 How to Configure Eraser ##

**Note**: It is recommended that you overwrite the data at least three times.

**Tip**: Each overwrite or *pass* takes time and therefore, the more passes you make, the longer the erasing process will take. This will be especially noticeable when erasing large files, or wiping free space.

The number of passes can be set by accessing the *Preferences: Erasing* menu.

**Step 1**. **Select > Edit > Preferences > Erasing...** as follows: 

![](/sbox/screen/eraser-en/07.png)

*Figure 3: The Eraser [On-Demand] screen displaying the Edit menu options*

*The Preferences: Erasing window appears as follows:*

![](/sbox/screen/eraser-en/08.png)

*Figure 4: The Eraser Preferences: Erasing window*

The *Preferences: Erasing* screen describes how the files are to be overwritten.

*Description*: This column lists the name of the overwrite procedure.

*Passes*: This column lists how many times the data will be overwritten.

In this example, we will overwrite our data using the *Pseudorandom Data* method. By default, only one pass is made when using this option. However, for extra security we will increase the number of passes.

**Step 2**. **Select** the *# 4 Pseudorandom Data* option as shown in *Figure 2*.

**Step 3**. **Click** ![](/sbox/screen/eraser-en/09.png) to activate the *Passes* screen as follows:

![](/sbox/screen/eraser-en/10.png)

*Figure 3: The Eraser Passes screen*

**Step 4**. **Set** the number of passes to between three and seven (remember the time/security trade-off).

**Step 5**. **Click** ![](/sbox/screen/eraser-en/11.png) to return to the *Passes* screen.

\# 4 Pseudorandom Data should now resemble the following:

![](/sbox/screen/eraser-en/12.png)

*Figure 4: The Eraser Erase screen with pane showing item 4 selected*

**Tip**: Make sure the check boxes labelled *Cluster Tip Area* and *Alternate Data Streams* are checked as follows (they are checked by default):

![](/sbox/screen/eraser-en/13.png)

*Figure 5: The Eraser Cluster Tip Area and Alternate Data Streams check boxes in default mode*


- *Cluster Tip Area*: A computer hard disk is divided into small segments called 'clusters'. Usually, a file spans several clusters, and often a file will not completely fill the last cluster. The unused space on this last cluster is called the cluster tip area. This cluster tip area may contain sensitive information from the other file that was written over this cluster before and occupied more of the cluster. Information from a cluster tip may be readable by a data recovery specialist. So, **check** the *Cluster Tip Area* check box for greater security.
- *Alternate Data Streams*: When a file is stored on your computer, it may come in different parts. For example, this text contains both text and images. These would be stored on your computer in different locations or 'streams'. So, **check** the *Alternate Data Streams* check box to ensure that all data associated with the file is deleted.

**Step 6**. **Click** ![](/sbox/screen/eraser-en/11.png).

You have now set the overwrite method for **Eraser** to wipe files. You should also set the same options for the *Unused Disk Space* feature that appears on the next tab in the *Preferences: Erasing* screen. However, you may set the number of passes to a *reasonable* figure -- taking into consideration that a free-space wipe will take around two hours per pass.


