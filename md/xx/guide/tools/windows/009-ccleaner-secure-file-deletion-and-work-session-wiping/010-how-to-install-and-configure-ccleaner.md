

---

lang: xx
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: How to Install and Configure CCleaner

---

List of sections on this page:  

- [**2.0 How to Install CCleaner**](#2.0)
- [**2.1 Before You Begin Configuring CCleaner**](#2.1)
- [**2.2 How to Configure CCleaner**](#2.3)


<a name="2.0"></a>
## 2.0 How to Install CCleaner ##

Installing **CCleaner** is a relatively easy and quick procedure. To begin installing **CCleaner**, perform the following steps:

**Step 1**. **Double click** ![](/sbox/screen/ccleaner-en-1/01.png) to begin the installation process. The *Warning* dialog box may appear. If it does, **click** 
![](/sbox/screen/ccleaner-en-1/25.png) to activate the following screen:

![](/sbox/screen/ccleaner-en-1/03.png)

*Figure 1: Welcome to the CCleaner v4.03 Setup window*

**Step 2**.  **Click** ![](/sbox/screen/ccleaner-en-1/05.png) to activate the *Install Options - Select any additional options* window, and then **click** ![](/sbox/screen/ccleaner-en-1/05.png) again to activate the following screen:

![](/sbox/screen/ccleaner-en-1/07.png)

*Figure 2: The untitled Install Google Chrome as my default browser window*

**Step 3**. **Click** to disable the *Install Google Chrome as my default browser* option as shown in *Figure 2* above, to prevent it from automatically installing itself on your computer. Note, that this screen may not appear in  during your installation.

**Step 4**. **Click** ![](/sbox/screen/ccleaner-en-1/08.png) to activate the *Installing* screen, displaying its installation progress status bar.

**Step 5**. **Click** ![](/sbox/screen/ccleaner-en-1/09.png) to complete installing **CCleaner**, and activate the following pop-up message:

![](/sbox/screen/ccleaner-en-1/10.png)

*Figure 3: The CCleaner Intelligent Cookie Scan pop-up message*

**Step 6**. **Click** ![](/sbox/screen/ccleaner-en-1/11.png) to avoid storing cookies permanently on your computer, and activate the **CCleaner** main console.

![](/sbox/screen/ccleaner-en-1/12.png)

*Figure 4: The Piriform CCleaner main console*

<a name="2.1"></a>
## 2.1 Before You Begin Configuring CCleaner ##

As described in detail in the **How-to Booklet** chapter [**6. How to Destroy Sensitive Information**](/chapter-6), the **Microsoft Windows** standard file deletion methods do not erase the actual data from the disk (even when you have emptied the *Recycle Bin*). This also applies to temporary files. To delete them permanently (that is, to *wipe* them) from the hard disk, the files must be overwritten with random data. **CCleaner** must be configured to overwrite any deleted files in order to securely delete them, as it will not do so in default mode. **CCleaner** can also securely delete old information by wiping any free disk space  (please refer to section **5.3 How to Wipe Free Disk Space Using CCleaner**).

<a name="2.2"></a>
## 2.2 How to Configure CCleaner ##

Before you begin using **CCleaner**, it should be configured to securely delete all temporary files. 

To configure **CCleaner**, perform the following steps:

**Step 1**. Either **click** ![](/sbox/screen/ccleaner-en-1/13.png) or **select Start > Programs > CCleaner** to activate the *Piriform CCleaner* console.

**Step 2**. **Click** ![](/sbox/screen/ccleaner-en-1/14.png) to activate the following screen:

![](/sbox/screen/ccleaner-en-1/15.png)

*Figure 6: The Options tab displaying the default About pane*

**Step 3**. **Click** ![](/sbox/screen/ccleaner-en-1/16.png) to activate the *Settings* pane. The *Settings* pane lets you choose the language you are most comfortable working in, and determine how **CCleaner** will delete temporary files and wipe drives. 

**Note**: The *Secure Deletion* section appears with the *Normal file deletion* option enabled. 

**Step 4**. **Click** the *Secure file deletion (Slower)* option to enable the drop-down list. 

**Step 5**. **Expand** the *Secure file deletion (Slower)* drop-down list and **select** the *Advanced Overwrite (3 passes)* item to resemble the following screen: 

![](/sbox/screen/ccleaner-en-1/17.png)

*Figure 5: The Settings pane displaying the Secure Deletion options*

After you have set this option, **CCleaner** will overwrite the files and folders you have selected for deletion with random data, effectively wiping them from your hard disk. The *passes* in the *Secure deletion* drop-down list, refer to the number of times your data will be overwritten by random data. The greater the number of passes selected, the more times your document, file or folder will be overwritten with random data. This reduces the recoverability of that document, file or folder, but increases the length of time required by the wiping process.  


