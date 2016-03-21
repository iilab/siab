

---

lang: en
community: guide
type: tools
os: windows
weight: 040
title: Eraser for Windows - secure file removal

---

**Eraser** is used to permanently delete sensitive data. It can also clean a digital storage device of all recoverable data.

# Required reading


:[](../../../tactics/destroy sensitive information)


:[](eraser-for-windows-secure-file-removal)

# What you will get from this guide

- The ability to permanently delete unwanted files from your computer.
- The ability to delete all recoverable files that are currently invisible on your computer.

# 1. Introduction to Eraser





## 1.0 Other tools like Eraser

**GNU Linux, Mac OS and other Microsoft Windows Compatible Programs**:

On the **GNU/Linux**, the secure-delete package can be [**used from the terminal**](http://www.ghacks.net/2010/08/26/securely-delete-files-with-secure-delete/) to both securely delete files and folders, or wipe free space on the disk. Secure-delete can also be [**integrated with a graphical file manager**](http://techthrob.com/2010/07/07/adding-a-secure-delete-option-to-nautilus-file-manager-in-linux/).

On the **Mac OS** you can use the **Finder** menu *Secure Empty Trash...* item to permanently get rid of files and folders. You may also use the **Mac OS** generic program *Disk Utility* to securely erase entire disk or a free space on internal or external disks.

On **Microsoft Windows** apart from **Eraser** described in this chapter one can also use [**CCleaner**](../ccleaner/windows) to securely delete files and folders from **Recycle Bin**. **CCleaner** can also wipe free space on the disk. Another recommended tool that can be used to securely delete files is [**Freeraser**](http://www.freeraser.com/).

We would also like to recommend the following multiplatform tool: [**DBAN - Darik's Boot And Nuke**](http://www.dban.org/). It is a package which you burn onto a CD and start your computer from. **DBAN** allows you securely delete the whole content of any hard disk that it detects, which makes it the *ideal* utility for bulk or emergency data destruction.

## 1.1 Things you should know about Eraser before you start

**Eraser** is used to permanently delete or *wipe* sensitive data from your computer. It does this by writing over the data you want to delete. You can select files or folders to be wiped in this way. **Eraser** will also delete copies of files that may exist in your computer without your knowledge. This includes files you have previously deleted using the standard **Windows** deletion method, and copies of documents you have worked on in the past. 

- Deleting files with **Eraser** can be performed on demand or scheduled to run at a specified times.
- If you schedule **Eraser** to run at a certain time, then your computer must be switched on at the specified time or the wipe will not happen. 
- Once you have deleted a file using **Eraser**, it cannot be recovered using a file recovery program.
- For greater security, you should set **Eraser** to overwrite files selected for deletion between 3 and 7 times.
- **Eraser** can be used to wipe the free space off your computer. This refers to permanently wiping all past traces of work that may not have been properly deleted and could, in theory, be recoverable.


# 2. Install and Configure Eraser





## 2.0 Install Eraser

Installing **Eraser** is an easy and quick process. To begin installing **Eraser**, perform the following steps:

As described in the How-to Booklet chapter [**Destroying Sensitive Information**](../destroy-sensitive-information), **Eraser** wipes data from your hard disk by overwriting it with random information. The more times you overwrite the data, the less likely that it will be recovered.

**Step 1**. **Double click** ![](/sites/siabnext.ttc.io/files/media/eraser-win-01.png); the *Open File - Security Warning* dialog box may appear. If it does, **click** ![](/sites/siabnext.ttc.io/files/media/eraser-win-02.png) to activate the *InstallAware Wizard*; after some moments, the *Welcome to the InstallAware Wizard for Eraser* screen will appear.

**Step 2**. **Click** ![](/sites/siabnext.ttc.io/files/media/eraser-win-03.png) to activate the *License Agreement* screen, and then **click** checkbox to enable the *I accept the terms of the license agreement* option, and then **click** ![](/sites/siabnext.ttc.io/files/media/eraser-win-03.png) again to activate the *Important Information* window.

**Step 3**. **Click** ![](/sites/siabnext.ttc.io/files/media/eraser-win-03.png) after reading the contents displayed in the scrolling window to activate the *Destination Folder* window and then **click** ![](/sites/siabnext.ttc.io/files/media/eraser-win-03.png) again.

**Step 4**. **Click** ![](/sites/siabnext.ttc.io/files/media/eraser-win-03.png) to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/eraser-win-04.png)

*Figure 1: The Select Program Folder window*

**Step 5**. **Check** the *Only for me (current user)* option to ensure that only you are permitted to use **Eraser**, and then **click** ![](/sites/siabnext.ttc.io/files/media/eraser-win-03.png) to activate the *Completing the InstallAware Wizard for Eraser* window.

**Step 6**. **Click** ![](/sites/siabnext.ttc.io/files/media/eraser-win-03.png) and then **click** ![](/sites/siabnext.ttc.io/files/media/eraser-win-05.png) to complete the installation process, and to run **Eraser** as follows:

![](/sites/siabnext.ttc.io/files/media/eraser-win-06.png)

*Figure 2: The Eraser main user interface*

## 2.1 Configure Eraser

**Note**: It is recommended that you overwrite the data at least three times.

**Tip**: Each overwrite or *pass* takes time and therefore, the more passes you make, the longer the erasing process will take. This will be especially noticeable when erasing large files, or wiping free space.

The number of passes can be set by accessing the *Preferences: Erasing* menu.

**Step 1**. **Select > Edit > Preferences > Erasing...** as follows: 

![](/sites/siabnext.ttc.io/files/media/eraser-win-07.png)

*Figure 3: The Eraser [On-Demand] screen displaying the Edit menu options*

The Preferences: Erasing window appears as follows:

![](/sites/siabnext.ttc.io/files/media/eraser-win-08.png)

*Figure 4: The Eraser Preferences: Erasing window*

The *Preferences: Erasing* screen describes how the files are to be overwritten.

*Description*: This column lists the name of the overwrite procedure.

*Passes*: This column lists how many times the data will be overwritten.

In this example, we will overwrite our data using the *Pseudorandom Data* method. By default, only one pass is made when using this option. However, for extra security we will increase the number of passes.

**Step 2**. **Select** the *# 4 Pseudorandom Data* option as shown in *Figure 2*.

**Step 3**. **Click** ![](/sites/siabnext.ttc.io/files/media/eraser-win-09.png) to activate the *Passes* screen as follows:

![](/sites/siabnext.ttc.io/files/media/eraser-win-10.png)

*Figure 3: The Eraser Passes screen*

**Step 4**. **Set** the number of passes to between three and seven (remember the time/security trade-off).

**Step 5**. **Click** ![](/sites/siabnext.ttc.io/files/media/eraser-win-11.png) to return to the *Passes* screen.

\# 4 Pseudorandom Data should now resemble the following:

![](/sites/siabnext.ttc.io/files/media/eraser-win-12.png)

*Figure 4: The Eraser Erase screen with pane showing item 4 selected*

**Tip**: Make sure the check boxes labelled *Cluster Tip Area* and *Alternate Data Streams* are checked as follows (they are checked by default):

![](/sites/siabnext.ttc.io/files/media/eraser-win-13.png)

*Figure 5: The Eraser Cluster Tip Area and Alternate Data Streams check boxes in default mode*

- *Cluster Tip Area*: A computer hard disk is divided into small segments called 'clusters'. Usually, a file spans several clusters, and often a file will not completely fill the last cluster. The unused space on this last cluster is called the cluster tip area. This cluster tip area may contain sensitive information from the other file that was written over this cluster before and occupied more of the cluster. Information from a cluster tip may be readable by a data recovery specialist. So, **check** the *Cluster Tip Area* check box for greater security.
- *Alternate Data Streams*: When a file is stored on your computer, it may come in different parts. For example, this text contains both text and images. These would be stored on your computer in different locations or 'streams'. So, **check** the *Alternate Data Streams* check box to ensure that all data associated with the file is deleted.

**Step 6**. **Click** ![](/sites/siabnext.ttc.io/files/media/eraser-win-11.png).

You have now set the overwrite method for **Eraser** to wipe files. You should also set the same options for the *Unused Disk Space* feature that appears on the next tab in the *Preferences: Erasing* screen. However, you may set the number of passes to a *reasonable* figure -- taking into consideration that a free-space wipe will take around two hours per pass.


# 3. How to Use Eraser





## 3.0 Use Eraser in Windows Explorer

It is common for people to use **Eraser** through the **My Computer Windows Explorer** programs, rather than through the **Eraser** program itself. 

**Step 1**. **Open** a folder containing a file you want to delete permanently.

**Step 2**. **Right-click** on this file. Two new options appear on the pop-up menu, *Erase* and *Eraser Secure Move* as follows:

![](/sites/siabnext.ttc.io/files/media/eraser-win-14.png)

*Figure 1: Erase and Eraser Secure Move options*

We are going to use the *Erase* option to permanently delete this file.

**Step 3**. **Select** the **Erase** item from the menu, as shown in *Figure 1* above.

*The Confirm Erasing pop up dialog box will appear as follows*:

![](/sites/siabnext.ttc.io/files/media/eraser-win-15.png)

*Figure 2: The Confirm Erasing pop up dialog box*

If the file displayed in the pop up dialog box is the one you want to delete permanently, perform the following step:

**Step 4**. **Click** ![](/sites/siabnext.ttc.io/files/media/eraser-win-16.png) to *permanently* erase or wipe the file from your computer.

**Warning**: Any file deleted in this manner with be *irretrievably* and permanently deleted. Therefore, you must be completely sure that you really want to erase a particular file, or group of files. 

To securely move a file/s from one location to another (for example, from your computer to a USB memory stick):

**Step 5**. **Select** ![](/sites/siabnext.ttc.io/files/media/eraser-win-17.png)

You will need to answer the same warning prompt, as above, to continue.

<a name="3.1"></a>

## 3.1 Wipe Unused Disk Space

Erasing unused disk space involves wiping all traces of previously existing files from the 'empty space' of your hard drive/portable storage device. This empty space usually contains files that were not deleted properly (please refer to the [**Recuva**](../recuva/windows) **Hands-on** guide and the **How-to Booklet** on [**How to destroy sensitive information*](../destroy-sensitive-information) from more information about this).

**Step 1**. **Select Start > Programs > Eraser > Eraser**.

**Tip**: You can perform the wiping task on demand or you can schedule it to occur at a specified time. 

**Important**: This process could take between 2 and 5 hours to complete and will slow your computer down while it operates. It maybe a good idea to run or schedule the free space wipe when you are not using your computer (or have gone home/to bed for the night). 

## 3.2 Use the On-Demand Task Feature

To create an *On-Demand* task for wiping *unused disk space*, perform the following steps:

**Step 1**. **Click** ![](/sites/siabnext.ttc.io/files/media/eraser-win-18.png)

**Step 2**. **Select File > New Task** as follows: 

![](/sites/siabnext.ttc.io/files/media/eraser-win-19.png)

*Figure 3: Selecting a New Task in the File menu*

The *Unused space on drive* option should be selected. 

**Step 3**. **Choose** the drive you want to clear the free space on. (In this example, the *Local Disk (C:)* has been selected. This is usually the primary hard drive on most computers.) 

![](/sites/siabnext.ttc.io/files/media/eraser-win-20.png)

*Figure 4: The Eraser Task Properties screen*

**Step 4**. **Click** ![](/sites/siabnext.ttc.io/files/media/eraser-win-21.png) to create, and then run the task which will appear in the **Eraser** user interface.

**Step 5**. **Right-click** the task to activate the pop-up menu as follows:

![](/sites/siabnext.ttc.io/files/media/eraser-win-22.png)

*Figure 5: The Eraser screen with Run selected*

**Step 6**. **Select Run** to activate the **Eraser** pop up dialog box as follows:

![](/sites/siabnext.ttc.io/files/media/eraser-win-23.png)

*Figure 6: The Eraser pop up dialog box*

**Step 7**. **Click** ![](/sites/siabnext.ttc.io/files/media/eraser-win-16.png).

*The **Eraser** progress status window displays the wiping process on the unused disk space as follows:*

![](/sites/siabnext.ttc.io/files/media/eraser-win-24.png)

*Figure 7: The Eraser window in the process of wiping unused disk space*

<a name="3.3"></a>

## 3.3 Use the Scheduler

Since we may not always remember to do this kind of computer 'housekeeping', **Eraser** has an option that lets you schedule a wiping task so that it runs at an appointed time every day, or one day per week.

**Step 1**. **Click** ![](/sites/siabnext.ttc.io/files/media/eraser-win-25.png) in the **Eraser** main screen.

**Step 2**. **Select File > New Task** as follows:

![](/sites/siabnext.ttc.io/files/media/eraser-win-26.png)

*Figure 8: Selecting a New Task in the File menu*

This will activate a window similar screen to *Figure 4* (in which you created an on-demand task). 

**Step 3**. **Set** these options as outlined in section [**3.2 How to Use the on-Demand Tasks Option**](#667).

![](/sites/siabnext.ttc.io/files/media/eraser-win-27.png)

*Figure 9: The Eraser Task Properties screen displaying the Schedule tab*

**Step 4**. **Click** the *Schedule* tab to activate its associated pane with two configurable settings: 

![](/sites/siabnext.ttc.io/files/media/eraser-win-28.png)

*Figure 10: The Eraser Schedule tab*

**Step 5**. **Select** day or event item that best suits your needs from the *Every* drop-down list.

**Step 6**. **Enter** the time that best suits your needs in the *At* timer, which can only be entered in a 24-hour format.

**Step 7**. After you have set a time and day, **click** ![](/sites/siabnext.ttc.io/files/media/eraser-win-21.png).

*The scheduled task will appear as follows*:

![](/sites/siabnext.ttc.io/files/media/eraser-win-29.png)

*Figure 11: The Eraser Scheduled task list*

**Note**: The computer must be switched on for the scheduled task to run.

## 3.4 Remove a Task

After you have run either an on-demand task or a scheduled task, you may want to remove it from your task list. 

To remove an on-demand task, perform the following steps:

**Step 1**. **Click** ![](/sites/siabnext.ttc.io/files/media/eraser-win-18.png) to display its corresponding task list as follows:

![](/sites/siabnext.ttc.io/files/media/eraser-win-30.png)

*Figure 12: The Eraser task list*

**Step 2**. **Select** the task you want to remove, as shown in *Figure 12* above. 

**Step 3**. **Right-click** to activate the pop-up menu and **select** the *Delete* item to remove the task from the task list. (Alternatively, you may **click** ![](/sites/siabnext.ttc.io/files/media/eraser-win-31.png) located beneath the **Eraser** menu bar.

The process for removing a *Scheduled Task* is almost identical. To remove a scheduled task, perform the following step:

**Step 1**. **Click** ![](/sites/siabnext.ttc.io/files/media/eraser-win-25.png), and then **repeat** **steps** 2 and 3, as described in this section.

<a name="3.5"></a>

## 3.5 Erase the Windows Recycle Bin

**Eraser** also allows you to erase any traces of documents you may have deleted from the **Windows Desktop Recycle Bin**. 

To access this feature, perform the following steps:

**Step 1**. **Right click** anywhere on the **Recycle Bin** icon to activate the **Eraser** pop-up menu as follows:

![](/sites/siabnext.ttc.io/files/media/eraser-win-32.png)

*Figure 13: The Eraser pop-up menu for the Recycle Bin*

**Step 2**. **Select** the appropriate item from the pop-up menu to begin erasing your **Recycle Bin**.

# 4. Portable Eraser





## 4.0 Differences between the Installed and Portable Versions of Eraser

Given that portable tools are not installed on a local computer, their existence and use may remain undetected. However, keep in mind that your external device or USB memory stick, and portable tools are only as safe as the computer you are using, and may risk being exposed to adware, malware, spyware and viruses.

**Portable Eraser** does not require the **.Net Framework** in order to run, and the extraction and installation time required is minimal. Aside from that, there are no other differences between **Portable Eraser** and the version designed to be installed on a local computer.


## 4.1 Download and Extract Portable Eraser

To begin downloading and extracting **Portable Eraser**, perform the following steps:

**Step 1**. **Click** [**http://portableapps.com/apps/utilities/eraser_portable**](http://portableapps.com/apps/utilities/eraser_portable) to be directed to the appropriate download site.

**Step 2**. **Click** ![](/sites/siabnext.ttc.io/files/media/eraserportable-win-01.png) to activate the **Source Forge** download page.

**Step 3**. **Click** ![](/sites/siabnext.ttc.io/files/media/eraserportable-win-02.png)
 to save the ![](/sites/siabnext.ttc.io/files/media/eraserportable-win-03.png) installation file to your computer; then navigate to it.

**Step 4**. **Double click** ![](/sites/siabnext.ttc.io/files/media/eraserportable-win-03.png); the *Open File - Security Warning* dialog box may appear. If it does, **click** ![](/sites/siabnext.ttc.io/files/media/eraserportable-win-04.png) to activate the *Eraser Portable | PortableApps.com Installer* window.

**Step 5**. **Click** ![](/sites/siabnext.ttc.io/files/media/eraserportable-win-06.png) to activate the following screen: 

![](/sites/siabnext.ttc.io/files/media/eraserportable-win-07.png)

*Figure 2: The Choose Install Location window*

**Step 6**. **Click** ![](/sites/siabnext.ttc.io/files/media/eraserportable-win-08.png) to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/eraserportable-win-09.png)

*Figure 3: The Browse for Folder window*

**Step 7**. **Click** ![](/sites/siabnext.ttc.io/files/media/eraserportable-win-10.png) to create and **type** in a name for the newly created folder as shown below:

![](/sites/siabnext.ttc.io/files/media/eraserportable-win-11.png)

*Figure 4: The Browse for Folder window displaying the newly created folder*

**Note**: Choose a different name for the **Portable Eraser** folder, so it may appear less obvious that you are using it.

**Step 8**. **Click** ![](/sites/siabnext.ttc.io/files/media/eraserportable-win-12.png) to confirm the destination folder into which **Portable Eraser** will be extracted, and to return to the *Choose Install Location* window. 

**Step 9**. **Click** ![](/sites/siabnext.ttc.io/files/media/eraserportable-win-13.png) to begin the extraction process, and then **click** ![](/sites/siabnext.ttc.io/files/media/eraserportable-win-14.png) after the extraction process has been completed.

**Step 10**. **Navigate** to your destination external drive or USB memory stick, as shown in *Figure 5* below, then **open** it to confirm that the **Portable Eraser** program has been successfully extracted.

![](/sites/siabnext.ttc.io/files/media/eraserportable-win-15.png)

*Figure 5: The Portable Eraser program extracted to the destination folder on a designated external hard drive (resized)*

**Step 11**. **Double click** ![](/sites/siabnext.ttc.io/files/media/eraserportable-win-16.png) to launch **Portable Eraser**.

Please refer to the [**Eraser**](../eraser/windows) chapter to begin configuring and using it.

# FAQ

***Q***: Can I use **Eraser** on files on my USB memory stick?

***A***: Yes. You can wipe the files through using the **Windows Explorer** menu. And you can also wipe unused space on a USB memory stick by creating the appropriate task in **Eraser**.

***Q***: If I don't want to use **Eraser** anymore, is it easy to uninstall? If I do so, will it affect my computer in any way? And will my files stay deleted?

***A***: You can uninstall **Eraser** from the Start menu as follows: **Start &gt; Programs &gt; Eraser &gt; Uninstall Eraser**. This will not affect other programs on your computer in any way, and the files you have wiped with **Eraser** will not be recoverable.

***Q***: Are there any **Windows** files that **Eraser** does not wipe?

***A***: All the files you can see in your computer can be wiped. Even some files that you cannot see (such as recoverable files in unused space) will be wiped if you set the right options mentioned above.

***Q***: Does **Eraser** wipe file names as well as the files themselves?

***A***: Yes, all parts of the file are wiped, however you should use [**CCleaner**](../ccleaner/windows) to wipe the recent documents list.

***Q***: Will anyone ever be able to access the deleted files?

***A***: Recovering data from files that have been overwritten is a highly complex and expensive process. It takes a disproportionate amount of time to recover a file that has only been overwritten once, let alone three to seven times. When using **Eraser** properly you may be sure that data has been securely deleted.
