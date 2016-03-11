

---

lang: xx
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 5
depth: 3
title: Advanced Options, FAQ and Review

---

List of sections on this page:  

- [**6.0 Advanced Options**](#6.0)
- [**6.1 How to Uninstall Programs Using CCleaner**](#6.1)
- [**6.2 How to Disable Auto-Start Programs in CCleaner**](#6.2)
- [**6.3 How to Wipe Free Disk Space Using CCleaner**](#6.3)
- [**6.4 FAQ and Review**](#6.4)
- [**6.5 Review Questions**](#6.5)


<a name="6.0"></a>
## 6.0 Advanced Options  ##

Two **CCleaner** features which could improve the overall efficiency of your computer system are the *Uninstall* and *Startup* features are described in the sections that follow. Also, you will learn how to permanently delete or *wipe* any free space on a specified drive.

<a name="6.1"></a>
## 6.1 How to Uninstall Programs Using CCleaner ##

**Important**: Make sure the program to be deleted or uninstalled is not essential to the proper functioning of your computer system before you begin doing so.

By deleting unused or unwanted previously installed software before running **CCleaner**, you may also remove their temporary files and folders. This may reduce the number of temporary files and folders to be deleted, as well as the length of time for the cleaning process.  

The **CCleaner** *Uninstall* feature is the equivalent of the **Uninstall a program** feature found in **Control Panel**. The *Uninstall* feature lists the programs more clearly and quickly.

To begin uninstalling obsolete programs, perform the following steps:

**Step 1**. Either **click** ![](/sbox/screen/ccleaner-en-1/13.png) or **select Start > Programs > CCleaner** to activate the *Piriform CCleaner* console.

**Step 2**. **Click** ![](/sbox/screen/ccleaner-en-1/50.png) and then **click** ![](/sbox/screen/ccleaner-en-1/51.png) to activate the following screen:

![](/sbox/screen/ccleaner-en-1/52.png)

*Figure 1: The Tools option displaying the Uninstall pane*

**Note**: The buttons on the right of the *Programs to Remove* list are only enabled after a program has been selected for removal.

**Step 3**. **Select** a program from the *Programs to Remove* list, and then **click** ![](/sbox/screen/ccleaner-en-1/53.png) to uninstall the selected program.

**Tip**: Advanced or experienced users will find the *Rename* and *Delete* features useful in keeping the existence of certain software private. Either feature ensures only you know about the existence of this program, keeping it safe from hostile or malicious parties which may list installed programs.

**Step 4**. **Click** ![](/sbox/screen/ccleaner-en-1/54.png) to rename that program. Alternatively, **click** ![](/sbox/screen/ccleaner-en-1/55.png) to delete a program from that list, but *without* actually uninstalling it. 

<a name="6.2"></a>
## 6.2 How to Disable Auto-Start Programs in CCleaner ##

An auto-start program is configured to automatically start itself whenever you turn your computer on. Auto-start programs may start making demands on finite system resources, and slow down your computer at start-up time. 

**Step 2**. **Click** ![](/sbox/screen/ccleaner-en-1/50.png) and then **click** ![](/sbox/screen/ccleaner-en-1/56.png) to activate the following screen:

![](/sbox/screen/ccleaner-en-1/57.png) 

*Figure 2: The Tools option displaying the Startup pane*

**Step 3**. **Select** a program from those listed in the *Startup* pane and then **click** ![](/sbox/screen/ccleaner-en-1/58.png) to disable the program so it does not automatically start running when you turn on your computer. 

<a name="6.3"></a>
## 6.3 How to Wipe Free Disk Space Using CCleaner ##

In the **Windows** operating system, deleting a file merely removes a reference to that file, but may not remove its actual data. Although the area of that drive will eventually be overwritten with new files over time, a knowledgeable individual could rebuild either all or sections of that file. However, you can prevent this from happening by wiping the free space on your hard disk. **CCleaner** also lets you wipe the **Master File Table**.

The **Master File Table (MFT)** is an index of all file names, their locations, and other information. When **Microsoft Windows** deletes a file it only marks the index entry for that file as deleted for reasons of efficiency. The **MFT** entry for the file and the content of the file continue to reside on the hard disk.

**Note**: Performing a disk and **Master File Table** wipe consumes a considerable amount of time, and the amount of time required depends on the number of passes set.

To set the drive you would like to wipe, perform the following steps:

**Step 1**. **Click** ![](/sbox/screen/ccleaner-en-1/61.png) and then **click** ![](/sbox/screen/ccleaner-en-1/62.png) to activate the *Drive Wiper* pane. 

**Step 2**. **Click** the *Wipe* ![](/sbox/screen/ccleaner-en-1/04.png) to activate its drop-down list, and then **select**  either the *Free Space* or the *Entire drive (All data will be erased)* item, and then **select** ![](/sbox/screen/ccleaner-en-1/59.png) from the *Security* drop-down list.

**Warning**: Only select the *Entire drive (All data will be erased)* item if you are *completely* certain that you want your documents, files and folders *and* free space erased.

**Step 3**. **Click** the check box associated with the drive to be erased, and enable the ![](/sbox/screen/ccleaner-en-1/64.png); your window should now resemble the following:

![](/sbox/screen/ccleaner-en-1/65.png)

*Figure 3: The Drive Wiper pane with the relevant options enabled*

**Step 4**. **Click** ![](/sbox/screen/ccleaner-en-1/64.png) to begin wiping your selected drive(s).

<a name="6.4"></a>
## 6.4 FAQ and Review ##

<div class="background" markdown="1">

***Q: If I uninstall CCleaner, will material deleted previously remain that way?***

***A**: Yes*. If you have configured and run **CCleaner** *properly, deleted files will stay deleted - permanently.*

***Q: If I copy CCleaner to a USB memory stick, can I use it on a computer in an Internet café to erase traces of my work there? Is there any reason I cannot use it this way?***

***A**: Yes! There is a [portable version of **CCleaner**](/en/ccleaner_portable). If the Internet café you are working at lets you run programs from a USB memory stick, then yes, you can use the portable version of **CCleaner** to erase traces of your having worked there. However, do keep in mind that you could be monitored at the Internet café. Also, you may run the risk of infection by connecting your USB memory stick to the computer at the Internet café.*

***Q: If I only use one pass of CCleaner, will it be possible for somebody to recover my data? What about if I use 7 passes?***

***A**: The more passes used for wiping data, the less chance anyone has of recovering that data. However, increasing the number of passes used in wiping data also increases the length of the wiping process.* 

***Q: Is cleaning the Windows Registry sufficient for removing all obvious signs of my having temporarily installed and used certain programs on my computer?***

***A**: Ideally, you should delete all the files related to this program, use **CCleaner** to delete temporary files, clean the **Windows Registry** and wipe a free space on the disk to remove all traces of software and the tasks you performed with it.*

</div>

<a name="6.5"></a>
## 6.5 Review Questions ##

- What kind of information does **CCleaner** remove from your computer?
- How does it do this?
- What difference does the number of passes you choose make when you securely overwrite your data?
- What is the **Windows Registry**, and why are you recommended to clean it?
- What should you do before you clean the **Windows Registry**? 


