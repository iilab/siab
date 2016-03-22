

---

lang: xx
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: How to Install Cobian Backup and Archive Your Files

---

List of sections on this page:

- [**2.0 How to Install Cobian Backup**](#2.0)
- [**2.1 How to Backup Your Directories and Files**](#2.1)
- [**2.2 How to Create a Backup File**](#2.2)
- [**2.3 How to Schedule Your Backup Task**](#2.3)

-------

<a name="2.0"></a>
## 2.0 How to Install Cobian Backup ##

**Installation Note**: Before you begin the installation process, verify that you have both the latest versions of the **Microsoft Windows Installer** and the **Microsoft.NET Framework**. 

Installing **Cobian Backup** is a relatively easy and quick procedure. To begin installing **Cobian Backup**, perform the following steps:

**Step 1**. **Double click** ![](/sbox/screen/cobian-en/01.png); the *Open File - Security Warning* dialog box may appear. If it does, **click** ![](/sbox/screen/cobian-en/02.png) to activate the light blue *Extracting the resource* progress status bar, followed a few moments later by the following screen:

![](/sbox/screen/cobian-en/03.png)

*Figure 1: The Cobian Setup Please select a language window*

**Step 2**. **Click** ![](/sbox/screen/cobian-en/04.png) to activate the *Please read and accept the license agreement* screen; **check** the *I accept* option, and then **click** ![](/sbox/screen/cobian-en/04.png) again to activate the following screen:

![](/sbox/screen/cobian-en/05.png)

*Figure 2: The Select an installation directory window*

**Step 3**. **Click** ![](/sbox/screen/cobian-en/04.png) to activate the following screen:

![](/sbox/screen/cobian-en/06.png)

*Figure 3: The Installation type and Service options window*

**Step 4**. **Check** the *Use Local System account* option in the *Service options* pane, so that your own resembles *Figure 3* above. 

**Important**: This option ensures that **Cobian Backup** will be running silently in the background all the time, so that your backups will occur as scheduled.

**Step 5**. **Click** ![](/sbox/screen/cobian-en/04.png) to activate the following message prompt:

![](/sbox/screen/cobian-en/07.png)

*Figure 4: The Cobian Backup 10 message prompt* 

**Step 6**. **Click** ![](/sbox/screen/cobian-en/08.png) to activate the next installation screen, and then **click** ![](/sbox/screen/cobian-en/04.png) to continue with the installation process.

**Step 7**. **Click** ![](/sbox/screen/cobian-en/09.png) to complete the installation process. After the installation process has been completed, the **Cobian Backup** icon will appear in the **Windows System Tray** as follows: ![](/sbox/screen/cobian-en/10.png)

<a name="2.1"></a>
## 2.1 How to Backup Your Directories and Files ##

In this section you will learn how to perform a simple backup or archive of a specified files and/or folders. **Cobian Backup** uses a *backup task* which can be configured to include a specified group of files and/or folders. A backup task can be set to run on a specified day and time.

To create a new backup task, perform the following step:

**Step 1**. **Click** ![](/sbox/screen/cobian-en/11.png) to create a new backup task, and activate the *New task* window as follows:

![](/sbox/screen/cobian-en/12.png)

*Figure 2: The New task pane*

The left sidebar lists a number of tabs and their associated screens - used to set different backup options and parameters - are displayed in the pane at right. All the options in the *General* tab are described below:

### 2.1.1 Option Descriptions ###

*Task Name*: This *Task Name* text field lets you enter a name for the backup task. Use a name that identifies the nature of the backup. For example, if the backup is going to contain video files, you could name it *Video Backup*.

*Disabled*: This option *must* be left unchecked. 

**Warning**: Enabling the *Disabled* option will override the rest of the options, and prevent the backup task from running.

*Include Subdirectories*: This option lets you include all the subdirectories/folders within a selected directory/folder for the backup task. This is an efficient method for backing up a large number of folders and/or files. As an example, if you select the *My Documents* folder and check this option, then all files and folders in *My Documents* will be included in the backup task.

*Create separated backups using timestamps*: This option lets you specify that the date and time of the backup task will be automatically included in the folder name containing your backup file. This is a good idea because it means that you will easily be able to identify when the backup was performed.

*Use file attribute logic*: This option is only relevant when you choose to perform an incremental or differential backup (see below). File attributes contain information about the file.

**Note**: The following option is only available for **Windows OS** versions more recent than *and* including **Windows XP**.

*Use Volume Shadow Copy*: This option lets you backup files which are locked.

**Cobian Backup** verifies this information to determine whether there has been a change in the source file from the last time a backup was performed. If you then run an *Differential* or *Incremental* backup, the file will be updated. 

**Note**: You will only be able to run a full or 'dummy backup' if you *disable this option* (the dummy backup option is explained below).

### 2.1.2 Backup type Descriptions ###

*Full*: This option means that *every* single file in the source location will be copied to your backup directory. If you have enabled the *Create separated backups using timestamp* option, you will have several copies of the same source (identified by the time and date of the backup in the folder title). Otherwise, **Cobian Backup** will overwrite the previous version (if any).

*Incremental*: This option means the program will verify if the files selected for backup have been changed since the last backup was performed. If there has been no change, it will be skipped over during the backup process, saving backup time. The *Use file attribute logic* option needs to be checked in order to perform this backup.

*Differential*: The program will check if the source has been changed from the last **full** backup. If there is no need to copy that file, it will be skipped, saving backup time. If you have run a full backup before on the same set of files, then you can continue backing it up, using the Differential method.

*Dummy task*: You can use this option to get your computer to run or shut down programs at certain times. This is a more advanced option which is not really relevant to our basic backup procedure.

**Step 2**. **Click** ![](/sbox/screen/cobian-en/13.png) to confirm your search options and parameters for your backup task.

<a name="2.2"></a>
## 2.2 How to Create a Backup File ##

To begin creating a backup file, perform the following steps:

**Step 1**. **Click** ![](/sbox/screen/cobian-en/14.png) in the left sidebar of the *New task* window to display a *blank* version of the following screen:

![](/sbox/screen/cobian-en/15.png)

*Figure 3: The New task (MyBackup) window displaying the Source and Destination panes*

**Step 2**. **Select** the files you want to back up. (In *Figure 3* above, the *My Documents* folder is selected.)

**Step 3**. **Click** ![](/sbox/screen/cobian-en/16.png) in the *Source* pane to activate the following menu:

![](/sbox/screen/cobian-en/17.png)

*Figure 4: The Source pane - Add button menu*

**Step 4**. **Select** *Directory* if you want to back up an entire directory, and *Files* to back up individual files. To specify individual files or directories to be backed up, select *Manually*, and type in the file path or directory for your backup. 

**Note**: You can add as many files or directories as you like. If you wish to back up files currently on your **FTP** server, choose the *FTP site* option (you will need to have the appropriate server login details).

When you have selected the files and/or folders, they will appear in the *Source* area. As you can see in *Figure 3* above, the *My Documents* folder is displayed there, meaning this folder will now be included in the backup task.

The *Destination* pane specifies where the backup will be stored.

**Step 5**. **Click** ![](/sbox/screen/cobian-en/16.png) in the *Destination pane* to activate the following menu:

![](/sbox/screen/cobian-en/18.png)

*Figure 5: The Destination pane - Add button menu*

**Step 6**. **Select** *Directory* to open a browser window where you select the destination folder for your backup file.

**Note**: If you want to create several versions of the backup file, you may specify several folders here. If you selected the *Manually* option, you must type in the full path to the folder where you want to keep the backup. To use a remote Internet server to store your archive, **select** the *FTP site* option (you will need to have the appropriate server login details).

The screen should now resemble the example above example with file(s) and/or folder(s) in the source area and folder(s) in the destination area. However, don't click *OK* just yet! You still need to set a schedule for your backup.

<a name="2.3"></a>
## 2.3 How to Schedule Your Backup Task ##

For your automatic backup to work, you need to fill in the *Schedule* section. This section lets you specify when you want the backup to be performed.

To set the schedule options, perform the following steps:

**Step 1**. **Select** ![](/sbox/screen/cobian-en/19.png) from the left sidebar, to activate the following pane:

![](/sbox/screen/cobian-en/20.png)

*Figure 6: The Properties for myBackup displaying the Schedule type pane*

The *Schedule type* options are listed in the drop-down menu, and described below:

*Once*: The backup will be done once only at the date and time specified in the *Date/Time* area.

*Daily*: The backup will be done every day at the time specified in the *Date/Time* area.

*Weekly*: The backup will be done on the days of the week selected. In the example above, the backup will be done on Fridays. You may select other days also. The backup will be done on all days selected at the time specified in the *Date/Time* area.

*Monthly*: The backup will be done on the days typed into the days of the month box at the time specified in the *Date/Time* area.

*Yearly*: The backup will be done on the days typed into the days of the month box, during the month specified, and at the time specified in the *Date/Time* area.

*Timer*: The backup will be done repeatedly at intervals specified in the Timer text box in the *Date/Time* area.

*Manually*: You will have to run the backup yourself from the main program window.

**Step 2**. **Click** ![](/sbox/screen/cobian-en/13.png) to confirm the options and settings for the backup schedule as follows:

![](/sbox/screen/cobian-en/21.png)

*Figure 7: The New task window displaying a configured Schedule type pane*

Once you have decided on a backup schedule, you have completed the final step. The backup will now run on the folders specified according to the schedule you have chosen.


