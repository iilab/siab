

---

lang: xx
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Perform Different Scans Using Recuva

---

List of sections on this page:  

- [**3.0 Before You Begin**](#3.0)
- [**3.1 How to Perform a Scan Using the Recuva Wizard**](#3.1)
- [**3.2 How to Perform a Scan without Using the Recuva Wizard**](#3.2)
- [**3.3 How to Perform a Deep Scan Using Recuva**](#3.3)
- [**3.4 An Introduction to the Options Screen**](#3.4)

----

<a name="3.0"></a>
### 3.0 Before You Begin ###

In this section, you will learn how to perform different types of scans, and be introduced to the *General* and *Actions* tabs in the *Options* screen.

**Note**: A scan will simply retrieve and display the files which are potentially recoverable. The actual recovery procedures are discussed in [**4.0 How to Recover and Securely Overwrite Files Using Recuva**](/en/recuva_recover#4.0). 


<a name="3.1"></a>
### 3.1 How to Perform a Scan Using the Recuva Wizard ###

The **Recuva** *Wizard* is recommended in situations where neither the full nor partial name of the file you would like to recover is known. It is also recommended if this is the first time you are using **Recuva**. The **Recuva** *Wizard* lets you set the scan parameters by letting you specify the file type and/or from where the file was deleted. 

To begin scanning for deleted files, perform the following steps:

**Step 1**. **Click** ![](/sbox/screen/recuva-en/15.png) or **select Start > Programs > Recuva > Recuva** to launch the program, and activate the following screen:

![](/sbox/screen/recuva-en/16.png)

*Figure 1: The Welcome to the Recuva Wizard screen*

**Tip**: If you know the exact or even partial name of a file you would like to recover, **click** ![](/sbox/screen/recuva-en/17.png) to go to the *Piriform Recuva* main user interface, and then follow the steps in section **3.2 How to Perform a Scan without Using the Recuva Wizard**.

**Step 2**. **Click** ![](/sbox/screen/recuva-en/18.png) to activate the following screen:

![](/sbox/screen/recuva-en/19.png)

*Figure 2: The Recuva Wizard File type screen*

The *Recuva Wizard File type* displays a list of different file types, and describes what files might be recovered when each option is enabled.

**Step 3**. **Check** the *Other* option as shown in *Figure 2*, and then **click** ![](/sbox/screen/recuva-en/18.png) to activate the following screen:

![](/sbox/screen/recuva-en/20.png)

*Figure 3: The Recuva Wizard File Location screen*

**Note**: The default setting for the *Recuva Wizard File Location* screen is the *I'm not sure* option. This option will extend the scan to all drives as well as removable media, except CDs, DVDs and optical media. It may, therefore, require a longer time to generate results.

Files are most frequently deleted from *Recycle Bin* in the **Windows** operating systems, to minimize the chance of your accidentally deleting private or sensitive information.

**Step 4**. **Check** the *In the Recycle Bin* option as shown in *Figure 3* above, and then **click** ![](/sbox/screen/recuva-en/18.png) to activate the following screen:

![](/sbox/screen/recuva-en/21.png)

*Figure 4: Thank you, Recuva is now ready to search for your files*

**Note**: For this exercise, do not enable the *Deep Scan* option. This scanning technique will be discussed in section **3.3 How to Perform a Deep Scan**. 

**Step 5**. **Click** ![](/sbox/screen/recuva-en/22.png) to begin recovering your deleted files. 

During the file recovery process, two progress status bars appear in quick succession. The *Scanning the drive for deleted files* progress bar lists the deleted files. The *Analyzing the file contents* progress bar groups and sorts the deleted files into file types and degree of recoverability. They also display the duration of the scanning and analysis processes. Your *Piriform Recuva* main user interface may then resemble the following screen:

![](/sbox/screen/recuva-en/23.png)

*Figure 5: The Piriform Recuva main user interface with deleted files*

The *Piriform Recuva* main user interface lists information about each deleted file, arranged in six columns. Each column is described as follows:

**Filename**: This displays the name and file extension of the deleted file. **Click** the *Filename* title to arrange the deleted files in alphabetical order.

**Path**: This displays where the deleted file was found. Given that the *In the Recycle Bin* option was enabled in this example, the file path is *C:RECYCLER* for all the deleted files. **Click** the *Path* title to view all the files listed under a particular directory or file path.

**Last modified**: This displays the last time the file was modified before it was deleted, and can be useful in helping to identify the file you would like to recover. **Click** *Last modified* to list the deleted files according to the oldest or most recent.

**Size**: This displays the size of the file. **Click** *Size* to list the deleted files beginning with the largest or smallest deleted file.

**Status**: This displays the extent to which the file is recoverable, and corresponds to the file status icons discussed in *Figure 6* below. **Click** *Status* to sort the deleted files into the three basic categories, and list them from *Excellent* to *Unrecoverable*.

**Comment**: This displays why a given file may or may not be recoverable, and the extent to which a deleted file has been overwritten in the **Windows Master File Table**. **Click** *Comment* to view the extent to which a file or group of files have been overwritten.

Each file is associated with a coloured status icon which indicates the extent to which each file can be successfully recovered:

![](/sbox/screen/recuva-en/24.png)

*Figure 6: The file status icons*

The following list describes each status icon:

-  **Green**: The chances for a full recovery are excellent.
- **Orange**: The chances for recovery are acceptable.
-    **Red**: The chances for recovery are unlikely.

<a name="3.2"></a>
### 3.2 How to Perform a Scan without Using the Recuva Wizard ###

To access the **Recuva** main user interface directly, (that is, not use the *Recuva Wizard*), perform the following steps: 

**Step 1**. **Click** ![](/sbox/screen/recuva-en/15.png) or **select Start > Programs > Recuva > Recuva** to activate *Figure 1*.

**Step 2**. **Check** the *Do not show this Wizard on startup* option, then **click** ![](/sbox/screen/recuva-en/50.png) to activate the following screen:

![](/sbox/screen/recuva-en/51.png)

*Figure 7: The Recuva main user interface*

The *Piriform Recuva* main user interface is divided into the results pane on the left and the *Preview*, *Info* and *Header* tabs in which to sort and view information about a specific deleted file. It lets you set certain scan options, similar to those in the *Recuva Wizard*. 

**Step 3**. **Click** to activate the drop-down list and **select** the drive to be scanned; the *Local Disk (C:)* is the default and used in this example as follows: 

![](/sbox/screen/recuva-en/52.png)

*Figure 8: The hard drive drop-down list*

The *Filename or path* drop-down list lets you specify the kind of file you are looking for, and loosely corresponds to the *Recuva Wizard File type* screen displayed in *Figure 2*. 

![](/sbox/screen/recuva-en/53.png)

*Figure 9: The File name or path drop-down list*

The *Filename or path* feature is a combination of a text box and drop-down list. It has two main uses: To let you directly search for a specific file, and/or to sort through a list of deleted files, according to file type. 

Alternatively, the *Filename or path* feature can be used to search for files of a specific type, or to sort through a general list of deleted files in the results pane. 

To begin scanning for a file of which all or part of the name is known, perform the following steps:

**Step 1**. **Type** in the name or partial name of a file you would like to recover as follows (in this example, the file *triangle.png* is being scanned):

![](/sbox/screen/recuva-en/54.png)

*Figure 10: The File name or path drop-down list displaying triangle.png*

**Tip**: **Click** ![](/sbox/screen/recuva-en/55.png) to reset the *File name and path* (which appear greyed out).

**Step 2**. **Click** ![](/sbox/screen/recuva-en/56.png) to begin scanning for your deleted file(s); shortly thereafter, a screen will appear resembling the following:

![](/sbox/screen/recuva-en/57.png)

*Figure 11: The Recuva user interface displaying the triangle.png file in the Preview tab*

<a name="3.3"></a>
#### 3.3 How to Perform a Deep Scan Using Recuva ####

The *Enable Deep Scan* option lets you conduct a more thorough scan; naturally, a deep scan takes a longer time, depending on your computer speed and the number of files you have. This option might prove useful if your initial scan does not display the files you would have liked to recover. Although a deep scan may even take hours depending on the amount of data stored on your computer, it may improve your chances of recovering the files you require. 

The **Recuva** *Deep Scan* option can be enabled either through **checking** the *Enable Deep Scan* option in the *Recuva Wizard* (please refer to *Figure 4*). 

**Step 1**. **Click** ![](/sbox/screen/recuva-en/70.png) to activate the *Options* screen, then **click** the *Actions* tab as follows:

![](/sbox/screen/recuva-en/73.png)

*Figure 12: The Options screen displaying the Actions tab* 

**Step 2**. **Check** the *Deep Scan* *(increases scan time)* option, then **click** ![](/sbox/screen/recuva-en/72.png). 

**Step 3**. **Click** ![](/sbox/screen/recuva-en/74.png) to begin scanning for deleted files using the *Deep Scan* option. As mentioned earlier, a deep scan can potentially take a few hours, depending on the size of your hard disk and computer speed:

![](/sbox/screen/recuva-en/78.png)

*Figure 13: The Scan displaying the estimated number of hours required for a deep scan*

<a name="3.4"></a>
### 3.4 An Introduction to the Options Screen ###

In this section, you will learn how to use the different settings to successfully recover and overwrite your private or sensitive information in the *Options* screen. To configure these settings, perform the following steps:

**Step 1**: **Click** ![](/sbox/screen/recuva-en/70.png) to activate the following screen:

![](/sbox/screen/recuva-en/71.png)

*Figure 14: The Options screen displaying the General tab in default mode*

The *Options* screen is divided into the *General*, *Actions* and *About* tabs. 

The *General* tab lets you define a number of important settings, including *Language* (**Recuva** supports a *spectacular* 37 languages seamlessly), *View mode* and disabling or enabling the *Recuva Wizard*. 

![](/sbox/screen/recuva-en/76.png)

*Figure 15: The View mode drop-down list*

The **View Mode** lets you select how you would like to view the deleted files, and can also be enabled whenever you **right click** a file in the *Piriform Recuva*. 

- **List**: This option lets you view the deleted files in a list as shown in *Figure 5*
- **Tree**: This option lets you view the directory path of deleted files in the form of an expandable tree.
- **Thumbnails**: This option lets you view the deleted files as graphics or images where possible. 

Most importantly perhaps, the *Advanced* section of the *General* tab lets you set the number of times your data can be overwritten by random data to protect it from recovery by hostile or malicious parties. 

The *Secure overwriting* drop-down list displays four options for overwriting your private information. Its default mode is *Simple Overwrite* *(1 pass)* displayed in *Figure 14*. A pass refers to the number of times your document, file or folder will be overwritten with random data to render it completely unreadable.

**Step 2**: **Select** the *DOD 5220.22-M (3 passes)* option as follows:

![](/sbox/screen/recuva-en/77.png) 

*Figure 16: The Secure overwriting drop-down list with the DOD 5220.22-M (3 passes) selected*

A single pass may prove quite effective in overwriting a given document, file or folder; however, there are parties with the resources and skills to recover a relatively light secure overwrite. Three passes is a solid balance between the time required to perform a secure overwrite, and the ability to recover that document, file or folder.

**Step 3**. **Click** ![](/sbox/screen/recuva-en/72.png) to save your *General* tab configuration options. 

![](/sbox/screen/recuva-en/75.png)

*Figure 17: The Options screen displaying the Actions tab* 

- **Show files found in hidden system directories**: This option lets you display files in hidden system directories. 

- **Show zero-byte files**: This option lets you show you files that have little to no content, and which are basically irrecoverable. 

- **Show securely deleted files**: This option lets you display files that have been securely deleted in the results pane. 

**Note**: If you have already used **CCleaner** or a similar program, it changes the filename to *ZZZZZZZ.ZZZ* when it securely deletes a file, for security reasons.

- **Deep Scan**: This option lets you scan the entire drive for the deleted document or file; if previous scans have proven ineffective in locating your file, the *Deep Scan* may prove useful. However, it does require more time. Please refer to section **3.3 How to Perform a Deep Scan Using Recuva.**

- **Scan for non-deleted files (for recovery from damaged or reformatted disks)**: This option lets you attempt to recover files from disks that may have sustained physical damage or software-related corruption. 

The *About* tab displays version information, as well as links to the Piriform web site. 

Now that you are more confident about performing different scans and familiar with the settings in the *General* and *Actions* tabs in the *Options* screen, you are ready to learn how to actually recover and/or securely overwrite your private or sensitive information in [**4.0 How to Recover and Securely Overwrite Files Using Recuva**](/en/recuva_recover#4.0)

