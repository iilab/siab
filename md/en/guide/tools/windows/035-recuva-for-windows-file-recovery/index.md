

---

lang: en
community: guide
type: tools
os: windows
weight: 035
title: Recuva for Windows - file recovery

---

**Recuva** is an easy-to-use data recovery tool. It lets you scan for and retrieve previously deleted documents, files, folders and other information, including emails, images and video formats. **Recuva** also uses secure overwriting techniques for erasing important, private or sensitive information.

# Required reading


:[Recover from information loss](../../../tactics/backup)


:[Recuva for Windows - file recovery](recuva-for-windows-file-recovery)

# What you will get from this guide

- The ability to perform different scanning techniques.
- The ability to recover previously deleted files on your computer.
- The ability to securely delete private or sensitive information.

# 1. Introduction to Recuva





## 1.0 Other tools like Recuva

**GNU Linux, Mac OS and other Microsoft Windows Compatible Programs**:

For **GNU Linux** users, we recommend [**R-Linux**](http://www.r-tt.com/data_recovery_linux/).  
**Mac OS** users will apprerciate [**TestDisk** and **PhotoRec**](http://www.cgsecurity.org/), which are also compatible with **Microsoft Windows** and **GNU Linux**.  
In addition to **Recuva**, there are other free file recovery programs compatible with **Microsoft Windows** that are well worth recommending:

- [**NTFS Undelete**](http://ntfsundelete.com/)
- [**Disk Digger**](http://diskdigger.org/)
- [**PCInspector File Recovery**](http://www.pcinspector.de/Default.htm?language=1)
- [**FileRestorePlus**](http://undeleteplus.com/)


## 1.1 Things you should know about Recuva before you start

In situations where private or sensitive files may have been mistakenly deleted, **Recuva** can help you to scan for and restore some of them. As discussed in the chapter on [**How-to Destroy Sensitive Information**](../destroy-sensitive-information), a file deleted using the standard **Windows** operating system *Delete* function, even after the *Recycle Bin* has been emptied, might still exist on the computer.

However, there are circumstances under which **Recuva** cannot retrieve information. If you have permanently deleted or *wiped* any temporary files by running **CCleaner** with the *Secure file deletion (Slower)* option enabled, those files are virtually unrecoverable. **Recuva** cannot recover files after programs like **CCleaner** or **Eraser** have been used to wipe free disk space or if **Windows** itself has already overwritten any previously occupied space. **Recuva** also cannot recover damaged documents and files.

**Recuva** can also be used to securely overwrite your private or sensitive data.

# 2. Install Recuva

Installing **Recuva** is a relatively easy and quick procedure. To begin installing **Recuva**, perform the following steps:

**Step 1**. **Double click** ![](/sites/siabnext.ttc.io/files/media/recuva-win-13.png); the *Open File - Security Warning* dialog box may appear. If it does, **click** ![](/sites/siabnext.ttc.io/files/media/recuva-win-02.png) to activate the following dialog box:  

![](/sites/siabnext.ttc.io/files/media/recuva-win-03.png)

*Figure 1: The Installer Language dialog box*

**Step 2**. **Click** ![](/sites/siabnext.ttc.io/files/media/recuva-win-04.png) to activate the *Welcome to the Recuva Setup Wizard* screen.

**Step 3**. **Click** ![](/sites/siabnext.ttc.io/files/media/recuva-win-06.png) to activate the *License Agreement* screen. Please read the *License Agreement* before proceeding with the rest of the installation process.

**Step 4**. **Click** ![](/sites/siabnext.ttc.io/files/media/recuva-win-07.png) to activate the *Choose Install Location* screen.

**Step 5**. **Click** ![](/sites/siabnext.ttc.io/files/media/recuva-win-06.png) to activate the *Install Options* screen.

**Note**: The *Install Options* screen appears with the *Install optional Yahoo! toolbar* option enabled. Do *not* install the **Yahoo!** toolbar, which may compromise your Internet privacy and security. 

**Step 6**. **Check** the *Install optional Yahoo! toolbar* check box to disable it as shown in *Figure 2* below:

![](/sites/siabnext.ttc.io/files/media/recuva-win-09.png)

*Figure 2: The Install Options screen with the optional Yahoo! toolbar disabled*

**Step 7**. **Click** ![](/sites/siabnext.ttc.io/files/media/recuva-win-10.png) to begin installing **Recuva**. This will activate the installation progress bar that will disappear after the installation has completed itself in a few minutes.

**Step 8**. **Click** ![](/sites/siabnext.ttc.io/files/media/recuva-win-12.png) to complete installing **Recuva**.

Now that you have successfully installed **Recuva**, you are ready to begin recovering and/or overwriting private and sensitive information. Please continue to section [**3.0 How to Perform Different Scans Using Recuva**](../recuva/windows#644).

# 3. Perform Various Scans Using Recuva

In this section, you will learn how to perform different types of scans, and be introduced to the *General* and *Actions* tabs in the *Options* screen.

**Note**: A scan will simply retrieve and display the files which are potentially recoverable. The actual recovery procedures are discussed in [**4.0 How to Recover and Securely Overwrite Files Using Recuva**](#649). 


## 3.1 Perform a Scan Using the Recuva Wizard

The **Recuva** *Wizard* is recommended in situations where neither the full nor partial name of the file you would like to recover is known. It is also recommended if this is the first time you are using **Recuva**. The **Recuva** *Wizard* lets you set the scan parameters by letting you specify the file type and/or from where the file was deleted. 

To begin scanning for deleted files, perform the following steps:

**Step 1**. **Click** ![](/sites/siabnext.ttc.io/files/media/recuva-win-15.png) or **select Start > Programs > Recuva > Recuva** to launch the program, and activate the following screen:

![](/sites/siabnext.ttc.io/files/media/recuva-win-16.png)

*Figure 1: The Welcome to the Recuva Wizard screen*

**Tip**: If you know the exact or even partial name of a file you would like to recover, **click** ![](/sites/siabnext.ttc.io/files/media/recuva-win-17.png) to go to the *Piriform Recuva* main user interface, and then follow the steps in section **3.2 How to Perform a Scan without Using the Recuva Wizard**.

**Step 2**. **Click** ![](/sites/siabnext.ttc.io/files/media/recuva-win-18.png) to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/recuva-win-19.png)

*Figure 2: The Recuva Wizard File type screen*

The *Recuva Wizard File type* displays a list of different file types, and describes what files might be recovered when each option is enabled.

**Step 3**. **Check** the *Other* option as shown in *Figure 2*, and then **click** ![](/sites/siabnext.ttc.io/files/media/recuva-win-18.png) to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/recuva-win-20.png)

*Figure 3: The Recuva Wizard File Location screen*

**Note**: The default setting for the *Recuva Wizard File Location* screen is the *I'm not sure* option. This option will extend the scan to all drives as well as removable media, except CDs, DVDs and optical media. It may, therefore, require a longer time to generate results.

Files are most frequently deleted from *Recycle Bin* in the **Windows** operating systems, to minimize the chance of your accidentally deleting private or sensitive information.

**Step 4**. **Check** the *In the Recycle Bin* option as shown in *Figure 3* above, and then **click** ![](/sites/siabnext.ttc.io/files/media/recuva-win-18.png) to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/recuva-win-21.png)

*Figure 4: Thank you, Recuva is now ready to search for your files*

**Note**: For this exercise, do not enable the *Deep Scan* option. This scanning technique will be discussed in section **3.3 How to Perform a Deep Scan**. 

**Step 5**. **Click** ![](/sites/siabnext.ttc.io/files/media/recuva-win-22.png) to begin recovering your deleted files. 

During the file recovery process, two progress status bars appear in quick succession. The *Scanning the drive for deleted files* progress bar lists the deleted files. The *Analyzing the file contents* progress bar groups and sorts the deleted files into file types and degree of recoverability. They also display the duration of the scanning and analysis processes. Your *Piriform Recuva* main user interface may then resemble the following screen:

![](/sites/siabnext.ttc.io/files/media/recuva-win-23.png)

*Figure 5: The Piriform Recuva main user interface with deleted files*

The *Piriform Recuva* main user interface lists information about each deleted file, arranged in six columns. Each column is described as follows:

**Filename**: This displays the name and file extension of the deleted file. **Click** the *Filename* title to arrange the deleted files in alphabetical order.

**Path**: This displays where the deleted file was found. Given that the *In the Recycle Bin* option was enabled in this example, the file path is *C:RECYCLER* for all the deleted files. **Click** the *Path* title to view all the files listed under a particular directory or file path.

**Last modified**: This displays the last time the file was modified before it was deleted, and can be useful in helping to identify the file you would like to recover. **Click** *Last modified* to list the deleted files according to the oldest or most recent.

**Size**: This displays the size of the file. **Click** *Size* to list the deleted files beginning with the largest or smallest deleted file.

**Status**: This displays the extent to which the file is recoverable, and corresponds to the file status icons discussed in *Figure 6* below. **Click** *Status* to sort the deleted files into the three basic categories, and list them from *Excellent* to *Unrecoverable*.

**Comment**: This displays why a given file may or may not be recoverable, and the extent to which a deleted file has been overwritten in the **Windows Master File Table**. **Click** *Comment* to view the extent to which a file or group of files have been overwritten.

Each file is associated with a coloured status icon which indicates the extent to which each file can be successfully recovered:

![](/sites/siabnext.ttc.io/files/media/recuva-win-24.png)

*Figure 6: The file status icons*

The following list describes each status icon:

-  **Green**: The chances for a full recovery are excellent.
- **Orange**: The chances for recovery are acceptable.
-    **Red**: The chances for recovery are unlikely.

<a name="3.2"></a>

## 3.2 Perform a Scan without Using the Recuva Wizard

To access the **Recuva** main user interface directly, (that is, not use the *Recuva Wizard*), perform the following steps: 

**Step 1**. **Click** ![](/sites/siabnext.ttc.io/files/media/recuva-win-15.png) or **select Start > Programs > Recuva > Recuva** to activate *Figure 1*.

**Step 2**. **Check** the *Do not show this Wizard on startup* option, then **click** ![](/sites/siabnext.ttc.io/files/media/recuva-win-50.png) to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/recuva-win-51.png)

*Figure 7: The Recuva main user interface*

The *Piriform Recuva* main user interface is divided into the results pane on the left and the *Preview*, *Info* and *Header* tabs in which to sort and view information about a specific deleted file. It lets you set certain scan options, similar to those in the *Recuva Wizard*. 

**Step 3**. **Click** to activate the drop-down list and **select** the drive to be scanned; the *Local Disk (C:)* is the default and used in this example as follows: 

![](/sites/siabnext.ttc.io/files/media/recuva-win-52.png)

*Figure 8: The hard drive drop-down list*

The *Filename or path* drop-down list lets you specify the kind of file you are looking for, and loosely corresponds to the *Recuva Wizard File type* screen displayed in *Figure 2*. 

![](/sites/siabnext.ttc.io/files/media/recuva-win-53.png)

*Figure 9: The File name or path drop-down list*

The *Filename or path* feature is a combination of a text box and drop-down list. It has two main uses: To let you directly search for a specific file, and/or to sort through a list of deleted files, according to file type. 

Alternatively, the *Filename or path* feature can be used to search for files of a specific type, or to sort through a general list of deleted files in the results pane. 

To begin scanning for a file of which all or part of the name is known, perform the following steps:

**Step 1**. **Type** in the name or partial name of a file you would like to recover as follows (in this example, the file *triangle.png* is being scanned):

![](/sites/siabnext.ttc.io/files/media/recuva-win-54.png)

*Figure 10: The File name or path drop-down list displaying triangle.png*

**Tip**: **Click** ![](/sites/siabnext.ttc.io/files/media/recuva-win-55.png) to reset the *File name and path* (which appear greyed out).

**Step 2**. **Click** ![](/sites/siabnext.ttc.io/files/media/recuva-win-56.png) to begin scanning for your deleted file(s); shortly thereafter, a screen will appear resembling the following:

![](/sites/siabnext.ttc.io/files/media/recuva-win-57.png)

*Figure 11: The Recuva user interface displaying the triangle.png file in the Preview tab*

<a name="3.3"></a>
#### 3.3 How to Perform a Deep Scan Using Recuva ####

The *Enable Deep Scan* option lets you conduct a more thorough scan; naturally, a deep scan takes a longer time, depending on your computer speed and the number of files you have. This option might prove useful if your initial scan does not display the files you would have liked to recover. Although a deep scan may even take hours depending on the amount of data stored on your computer, it may improve your chances of recovering the files you require. 

The **Recuva** *Deep Scan* option can be enabled either through **checking** the *Enable Deep Scan* option in the *Recuva Wizard* (please refer to *Figure 4*). 

**Step 1**. **Click** ![](/sites/siabnext.ttc.io/files/media/recuva-win-70.png) to activate the *Options* screen, then **click** the *Actions* tab as follows:

![](/sites/siabnext.ttc.io/files/media/recuva-win-73.png)

*Figure 12: The Options screen displaying the Actions tab* 

**Step 2**. **Check** the *Deep Scan* *(increases scan time)* option, then **click** ![](/sites/siabnext.ttc.io/files/media/recuva-win-72.png). 

**Step 3**. **Click** ![](/sites/siabnext.ttc.io/files/media/recuva-win-74.png) to begin scanning for deleted files using the *Deep Scan* option. As mentioned earlier, a deep scan can potentially take a few hours, depending on the size of your hard disk and computer speed:

![](/sites/siabnext.ttc.io/files/media/recuva-win-78.png)

*Figure 13: The Scan displaying the estimated number of hours required for a deep scan*

<a name="3.4"></a>

## 3.3 Perform a Deep Scan Using Recuva

The *Enable Deep Scan* option lets you conduct a more thorough scan; naturally, a deep scan takes a longer time, depending on your computer speed and the number of files you have. This option might prove useful if your initial scan does not display the files you would have liked to recover. Although a deep scan may even take hours depending on the amount of data stored on your computer, it may improve your chances of recovering the files you require. 

The **Recuva** *Deep Scan* option can be enabled either through **checking** the *Enable Deep Scan* option in the *Recuva Wizard* (please refer to *Figure 4*). 

**Step 1**. **Click** ![](/sites/siabnext.ttc.io/files/media/recuva-win-70.png) to activate the *Options* screen, then **click** the *Actions* tab as follows:

![](/sites/siabnext.ttc.io/files/media/recuva-win-73.png)

*Figure 12: The Options screen displaying the Actions tab* 

**Step 2**. **Check** the *Deep Scan* *(increases scan time)* option, then **click** ![](/sites/siabnext.ttc.io/files/media/recuva-win-72.png). 

**Step 3**. **Click** ![](/sites/siabnext.ttc.io/files/media/recuva-win-74.png) to begin scanning for deleted files using the *Deep Scan* option. As mentioned earlier, a deep scan can potentially take a few hours, depending on the size of your hard disk and computer speed:

![](/sites/siabnext.ttc.io/files/media/recuva-win-78.png)

*Figure 13: The Scan displaying the estimated number of hours required for a deep scan*

<a name="3.4"></a>

## 3.4 Introduction to the Options Screen

In this section, you will learn how to use the different settings to successfully recover and overwrite your private or sensitive information in the *Options* screen. To configure these settings, perform the following steps:

**Step 1**: **Click** ![](/sites/siabnext.ttc.io/files/media/recuva-win-70.png) to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/recuva-win-71.png)

*Figure 14: The Options screen displaying the General tab in default mode*

The *Options* screen is divided into the *General*, *Actions* and *About* tabs. 

The *General* tab lets you define a number of important settings, including *Language* (**Recuva** supports a *spectacular* 37 languages seamlessly), *View mode* and disabling or enabling the *Recuva Wizard*. 

![](/sites/siabnext.ttc.io/files/media/recuva-win-76.png)

*Figure 15: The View mode drop-down list*

The **View Mode** lets you select how you would like to view the deleted files, and can also be enabled whenever you **right click** a file in the *Piriform Recuva*. 

- **List**: This option lets you view the deleted files in a list as shown in *Figure 5*
- **Tree**: This option lets you view the directory path of deleted files in the form of an expandable tree.
- **Thumbnails**: This option lets you view the deleted files as graphics or images where possible. 

Most importantly perhaps, the *Advanced* section of the *General* tab lets you set the number of times your data can be overwritten by random data to protect it from recovery by hostile or malicious parties. 

The *Secure overwriting* drop-down list displays four options for overwriting your private information. Its default mode is *Simple Overwrite* *(1 pass)* displayed in *Figure 14*. A pass refers to the number of times your document, file or folder will be overwritten with random data to render it completely unreadable.

**Step 2**: **Select** the *DOD 5220.22-M (3 passes)* option as follows:

![](/sites/siabnext.ttc.io/files/media/recuva-win-77.png) 

*Figure 16: The Secure overwriting drop-down list with the DOD 5220.22-M (3 passes) selected*

A single pass may prove quite effective in overwriting a given document, file or folder; however, there are parties with the resources and skills to recover a relatively light secure overwrite. Three passes is a solid balance between the time required to perform a secure overwrite, and the ability to recover that document, file or folder.

**Step 3**. **Click** ![](/sites/siabnext.ttc.io/files/media/recuva-win-72.png) to save your *General* tab configuration options. 

![](/sites/siabnext.ttc.io/files/media/recuva-win-75.png)

*Figure 17: The Options screen displaying the Actions tab* 

- **Show files found in hidden system directories**: This option lets you display files in hidden system directories. 

- **Show zero-byte files**: This option lets you show you files that have little to no content, and which are basically irrecoverable. 

- **Show securely deleted files**: This option lets you display files that have been securely deleted in the results pane. 

**Note**: If you have already used **CCleaner** or a similar program, it changes the filename to *ZZZZZZZ.ZZZ* when it securely deletes a file, for security reasons.

- **Deep Scan**: This option lets you scan the entire drive for the deleted document or file; if previous scans have proven ineffective in locating your file, the *Deep Scan* may prove useful. However, it does require more time. Please refer to section **3.3 How to Perform a Deep Scan Using Recuva.**

- **Scan for non-deleted files (for recovery from damaged or reformatted disks)**: This option lets you attempt to recover files from disks that may have sustained physical damage or software-related corruption. 

The *About* tab displays version information, as well as links to the Piriform web site. 

Now that you are more confident about performing different scans and familiar with the settings in the *General* and *Actions* tabs in the *Options* screen, you are ready to learn how to actually recover and/or securely overwrite your private or sensitive information in **4.0 How to Recover and Securely Overwrite Files Using Recuva**.

# 4. Recover and Securely Overwrite Files Using Recuva

In this section, you will learn how to recover a previously deleted file, as well as how to securely overwrite any private or sensitive information. 

**Recuva** lets you create a new folder for storing your recovered files. Although **Recuva** does let you use existing folders, for reasons of safety and security, we recommend that you copy your recovered files to a removable device like a backup drive or USB memory stick.  

**Important**: Although **Recuva** does an excellent job of securely overwriting information, it may leave a file marker indicating the existence of such a file. To protect your privacy and security, it makes sense to save any important, private or sensitive information to a removable device, and not to the original location or path.

<a name="4.1"></a>

## 4.1 Recover a Deleted File

To begin recovering a deleted file, perform the following steps:

**Step 1**. **Connect** your removable disk or a USB memory stick to your computer.

**Step 2**. **Check** the check box next to a file you want to recover to enable the *Recover...* button or **double click** that file to both check *and* highlight that file.

**Step 3**. **Click** ![](/sites/siabnext.ttc.io/files/media/recuva-win-25.png) to activate the *Browse For Folder* screen.

**Step 4**. **Select** a destination and then **click** ![](/sites/siabnext.ttc.io/files/media/recuva-win-27.png) to create your recovery folder as shown in *Figure 1* below. 

![](/sites/siabnext.ttc.io/files/media/recuva-win-26.png)

*Figure 1: The Browse For Folder dialog box displaying the newly created folder on a removable device*

**Note**: In this example, the folder for storing your recovered documents and files has been given an obvious label. However, keeping your digital privacy and security in mind, we encourage you to be more careful in labelling your own folder.  

**Step 5**. **Click** ![](/sites/siabnext.ttc.io/files/media/recuva-win-30.png) to begin the file recovery process; a progress status screen appears as follows:

![](/sites/siabnext.ttc.io/files/media/recuva-win-31.png)

*Figure 2: The Recovering files progress status screen*

After the files have been recovered, a confirmation will appear resembling the following screen:

![](/sites/siabnext.ttc.io/files/media/recuva-win-32.png)

*Figure 3: The Operation Completed screen*

**Note**: **Recuva** supports multiple file recovery. Simply check the check boxes of the files you would like to recover and perform **steps 3** to **5**.

Now that you are comfortable with recovering a previously deleted file, you are ready to learn how to use the pop-up menu to perform multiple file recoveries and secure overwriting of files.

<a name="4.2"></a>

## 4.2 How to Use the Pop-up Menu

**Recuva** offers different options for selecting the documents, files or folders you would like to delete or securely overwrite.
 
- **Checking** is generally used to quickly select several non-contiguous or separate files for recovery or secure overwriting. 
- **Highlighting** is generally used to quickly select contiguous multiple files in a block or group for recovery or secure overwriting.   

**Right click** on a deleted file displayed in the **Recuva** main to activate the following pop-up menu: 

![](/sites/siabnext.ttc.io/files/media/recuva-win-34.png) 

*Figure 4: The pop-up menu*

**Recover Highlighted**: This item lets you recover all or any highlighted deleted file(s).

**Recover Checked**: This item lets you recover a checked deleted file.

**Check Highlighted**: This item lets you check a highlighted deleted file.

**Uncheck Highlighted**: This item lets you uncheck a highlighted deleted file.

As you recall, the **View Mode** can also be set in the *General* tab in the *Options* screen. This item lets you select how you would like to view the deleted files. 

- **List**: This option lets you view the deleted files in a list as in *Figure 5*
- **Tree**: This option lets you view the directory path of deleted files in the form of an expandable tree.
- **Thumbnails**: This option lets you view the deleted files as graphics or images where possible. 

**Highlight Folder**: This option lets you select multiple deleted files according to their directory path, and lets you perform the actions listed in the pop-up menu on them. 

**Secure Overwrite Highlighted**: This option lets you securely overwrite a highlighted deleted file.

**Secure Overwrite Checked**: This option lets you securely overwrite a checked deleted file, changing its status icon to red.

<a name="4.3"></a>

## 4.3 Securely Overwrite a Deleted File

To securely overwrite a deleted file, perform the following steps:

**Step 1**. **Check** the individual file you would like to have securely overwritten, and then right click the check box it to activate the pop-up menu.

**Step 2**. **Select** ![](/sites/siabnext.ttc.io/files/media/recuva-win-35.png) to activate the following confirmation dialog box:

![](/sites/siabnext.ttc.io/files/media/recuva-win-36.png)

*Figure 5: The Secure overwrite confirmation dialog box* 

**Step 3**. **Click** ![](/sites/siabnext.ttc.io/files/media/recuva-win-37.png) to begin the overwriting process; depending on the size and status of the file as well as the *Secure overwriting* option you selected in the *General* tab in the *Options* screen, this could take some time. After the overwriting process has been completed, a screen resembling the following appears:

![](/sites/siabnext.ttc.io/files/media/recuva-win-38.png)

*Figure 6: The Operation complete screen*

You have successfully completed recovering and securely overwriting files using **Recuva** previously deleted files. To review your knowledge of **Recuva**, please continue to the **FAQ and Review** section.

# 5. Portable Recuva





## 5.0 Differences between the Installed and Portable Versions of Recuva

Given that portable tools are not installed on a local computer, their existence and use may remain undetected. However, keep in mind that your external device or USB memory stick, and portable tools are only as safe as the computer you are using, and may risk being exposed to adware, malware, spyware and viruses.

There are no other differences between **Portable Recuva** and the version designed to be installed.


## 5.1 Download and Extract Recuva Portable

To begin downloading and extracting **Recuva Portable**, perform the following steps:

**Step 1**. **Click** [**http://www.piriform.com/recuva/download/portable**](http://www.piriform.com/recuva/download/portable) to be directed to the appropriate download site, and automatically activate the following screen:

**Step 2**. **Click** ![](/sites/siabnext.ttc.io/files/media/recuvaportable-win-02.png) to save the ![](/sites/siabnext.ttc.io/files/media/recuvaportable-win-03.png) installation file to your computer; and then **navigate** to it.

**Step 3**. **Right click** to activate the **Windows** pop-up menu, and then **select** the Extract files... item as shown in *Figure 1* below: 

![](/sites/siabnext.ttc.io/files/media/recuvaportable-win-04.png)

*Figure 1: The Windows pop-up menu with the Extract files... item selected*

*This will activate the following window:*

**Step 4**. **Navigate** to the removable drive or USB memory stick as shown in *Figure 2* below, and then **click** ![](/sites/siabnext.ttc.io/files/media/recuvaportable-win-05.png) to create a new folder in which to extract the installation file.

![](/sites/siabnext.ttc.io/files/media/recuvaportable-win-06.png)

*Figure 2: The Extraction path and options navigation window*

**Step 5**. **Enter** a name for the new folder in the document tree as shown in *Figure 3* below:

![](/sites/siabnext.ttc.io/files/media/recuvaportable-win-07.png)

*Figure 3: The Extraction path and options window document tree (resized)*

Alternatively, you may type in a folder name in the accompanying drop-down list: ![](/sites/siabnext.ttc.io/files/media/recuvaportable-win-08.png)

**Note**: Although for the purposes of this example, the new folder is entitled Recuva Portable, users may choose different name.

**Step 6**. **Click** ![](/sites/siabnext.ttc.io/files/media/recuvaportable-win-09.png) to begin extracting its contents to newly created folder.

**Step 7**. **Navigate** to your destination external drive or USB memory stick, as shown in *Figure 4* below, then **open** it to confirm that the **Portable Recuva** program was successfully extracted.

![](/sites/siabnext.ttc.io/files/media/recuvaportable-win-10.png)

*Figure 4: The Portable Recuva program extracted to the destination folder on a designated external hard drive*

**Step 8**. **Double click** ![](/sites/siabnext.ttc.io/files/media/recuvaportable-win-11.png) to activate the **Portable Recuva** wizard.

Please refer to the [**Recuva**](../recuva/windows) chapter to begin configuring and using it.


# FAQ

***Q***: Are there file types which are impossible for **Recuva** to recover?

***A***: No, **Recuva** can recover all file types.

***Q***: Can I recover a file that has been securely deleted?

***A***: Once it's been securely deleted, it's gone forever.

***Q***: I've noticed that sometimes, even after I've securely deleted a file, it's still marked as recoverable. How is this possible?

***A***: It's possible that you are seeing a file marker, an indicator of where the original file was located. However, if you recover and open that file, you will find its contents unreadable.

***Q***: I deleted a file accidentally; having created it less than five minutes ago, I thought it would be easily recoverable. How come **Recuva** was unable to recover it?

***A***: Ironically, a document or file existing for only few minutes has  greater likelihood of being overwritten by temporary files than one which has existed for a longer period. **Recuva** doesn't easily recover files which have been deleted almost immediately after creation.

***Q***: After I've cleaned my computer system using **CCleaner**, can that data be recovered later?

***A***: Depending on the skill and resources available to someone attempting such a recovery, it's possible. It also depends on the secure deletion settings you used for cleaning your temporary files and the **Windows Registry** in **CCleaner**. To minimize their ability to recover your private and sensitive information, enable the Secure Deletion option in **CCleaner**, and wipe any empty space on hard drives and in the **Windows Master File Table**. In **Recuva**, you can increase the number of passes for securely overwriting data as well. This is a great question because it also shows you how different tools complement each other, in your efforts to protect your digital privacy and security.