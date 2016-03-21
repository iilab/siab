

---

lang: en
community: guide
type: tools
os: linux
weight: 025
title: VeraCrypt for Linux - Secure file storage

---

**VeraCrypt** encrypts your data and prevents anyone who does not have your passphrase from accessing them. It works like an electronic safe in which you can securely store your files.

# Required reading


:[](../../../tactics/secure file storage)


:[](veracrypt-for-linux-secure-file-storage)

# What you will get from this guide

- The ability to protect your files if your computer or USB storage device gets lost, stolen or confiscated
- The ability to access and modify the same set of sensitive files on Windows, Mac OS X and Linux computers
- A secure way to backup important files 

# 1. Introduction to VeraCrypt

[**VeraCrypt**](https://veracrypt.codeplex.com/) is *free software* that allows you to encrypt your files. It is an updated version of the discontinued [TrueCrypt](http://www.truecrypt.org/) project and is available for Microsoft Windows, Mac OS X and GNU Linux. It addresses the [security vulnerabilities](https://securityinabox.org/en/blog/12-11-2015/truecrypts-security-flaws-what-now) that were detected in TrueCrypt. 


## 1.0 Things you should know about VeraCrypt before you start

VeraCrypt will protect your files by encrypting them with a passphrase. It creates a protected area, called a *volume*, on your computer or external storage device. This entire volume lives inside a single file called a *container*, which you can open (or *mount*) and close (or *dismount*) using VeraCrypt. You can safely store your files inside this container.

VeraCrypt can also create and manage encrypted volumes that occupy *all* of the space on a particular storage device. However, this guide focuses on the use of *containers*.

VeraCrypt uses *on-the-fly encryption* to protect your data. On-the-fly encryption transparently encrypts files as they are being written to a volume and  transparently decrypts them as they are being read. You can copy files to and from a VeraCrypt volume in the same way that you would copy them to and from a normal folder or USB storage device.

VeraCrypt supports both *standard encrypted volumes* and *hidden volumes*. Either one will keep your files confidential, but *hidden volumes* allow you to hide your important information behind less sensitive data in order to protect it even if you are forced to reveal your VeraCrypt passphrase. This guide covers the creation and use of both *standard volumes* and *hidden volumes*.

Remember, if you forget your passphrase, you will lose access to your data! There is no way to recover a lost passphrase. Also, keep in mind that the use of encryption is illegal in some jurisdictions.

For more information about VeraCrypt, see:

* The [official documentation](https://veracrypt.codeplex.com/documentation)
* The [official FAQ](https://veracrypt.codeplex.com/wikipage?title=FAQ)


## 1.1 Other tools like VeraCrypt

Many **GNU Linux** distributions, including [**Ubuntu**](http://www.ubuntu.com/), support full-disk encryption as a standard feature. We recommend enabling full-disk encryption when you install Linux, as it is far easier than doing so later. In addition, you can use the built in **Disk Utility** on most Linux distributions to create an encrypted volume on a USB storage device. Unlike VeraCrypt, however, this will only allow you to access your files on other Linux computers. You can use VeraCrypt to move files between Linux, Mac OS X and Windows.

For **Mac OS X** you can use the built-in **FileVault** utility for full-disk encryption (or to encrypt just your home directory). **Mac OS X** also has a **Disk Utility** that can create encrypted volumes on USB storage devices, but you will only be able to access these volumes on a Mac. 

Full-featured editions of **Windows** since **Windows 7** contain the [**BitLocker**](http://windows.microsoft.com/en-us/windows7/products/features/bitlocker) full-disk encryption utility. (This includes Windows 7 Ultimate, Windows 7 Enterprise, Windows 8 Pro, Windows 8 Enterprise and Windows 10 Pro). 

Both **FileVault** (for **Mac OS X**) and **BitLocker** (for **Windows**) are proprietary software. As a result, the security they provide can not be independently verified. Nonetheless, it is a good idea to enable them if possible. You can use **VeraCrypt**, in addition to these built-in tools, to protect your most sensitive files and to move them between Linux, Mac OS X and Windows computers.


# 2. Install VeraCrypt

Before you download VeraCrypt, check to see if you are running a a 32-bit system or a 64-bit system: 

**Step 1.** Launch *Terminal* 

**Step 2.** Execute the following command in *Terminal*:

`uname –m`

- If you are running a **32-bit** system, *Terminal* will display `i686` or `i386`. 
- If you're running a **64-bit** system, it will display `x86_64`. 

**Step 3.** **Browse** to the VeraCrypt download page at [**https://veracrypt.codeplex.com/releases**](https://veracrypt.codeplex.com/releases/). 

**Step 4.** In the **Other Available Downloads** section, **click** the *newest version* of the **VeraCrypt Linux Setup** application. (Currently, this is **VeraCrypt Linux Setup 1.16** but future releases will have higher version numbers.) 

After you have downloaded VeraCrypt you can install it on your computer by following the steps below. 

**Step 5**. **Launch** your file browser and **navigate** to the location where you downloaded the VeraCrypt installer archive in *Step 4* (currently **veracrypt-1.16-setup.tar.bz2**)

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v02-001.png)

*Figure 1: The VeraCrypt installer archive*

**Step 6.** **Double click** the file you downloaded in *Step 4* to view its contents.

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v02-202.png) 

*Figure 2: Extraction of VeraCrypt using Archive Manager*

**Step 7.** **Right-click** the VeraCrypt setup utility that is appropriate for your system and **select** *Extract*.

- For a **32-bit** system, this is currently **veracrypt-1.16-setup-gui-x86**
- For a **64-bit** system, this is currently **veracrypt-1.16-setup-gui-x64**

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-203.png) 

*Figure 3: Choosing where to extract the VeraCrypt Setup file*

**Step 8.** **Choose** a location for the VeraCrypt Setup file and click **[Extract]**. (In this section, we will extract it to the Desktop.

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-204.png)

*Figure 4: Archive Manager window showing that the extraction of VeraCrypt is complete*

**Step 9.** When the extraction is done, **click** **[Close]**, then **quit** the *Archive Manager*.

**Step 10.** Find the folder into which you extracted your VeraCrypt Setup file. (In this section, we extracted **veracrypt-1.16-setup-gui-x64** to the *Desktop*)

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v02-205.png)  

*Figure 5: Location of extracted VeraCrypt file*

At this point, you may have to change your *file browser's* preferences in order to launch the installer itself. This is covered in *Steps 11 through 14* below

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v02-200.png)

*Figure 6: Preferences for the Nautilus file browser*

**Step 11**. **Click** *Edit* in your file browser's menu and **select** *Preferences* to open the preferences screen

**Step 12**. **Click** the *Behavior* tab

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v02-201.png)

*Figure 7: The file browser's Behavior tab*

**Step 13.** Under *Executable text files*, make sure that *Ask each time* is selected.

**Step 14.** **Click** **[Close]**

**Step 15.** **Double-click** the VeraCrypt setup file (currently **veracrypt-1.16-setup-gui-x64**) to choose whether you want to *Display* the setup file or *Run* it

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v02-002.png)

*Figure 8: Actions you can take when double-clicking an executable text file*

**Step 16.** **Click** **[Run]** to start the VeraCrypt installer

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-207.png)

*Figure 9: Installing VeraCrypt*

**Step 17.**  Click **[Install VeraCrypt]** to display the License Terms

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-208.png) 

*Figure 10: Agreeing to the license terms of VeraCrypt*

**Step 18.** **Read** VeraCrypt's license terms and **click** **[I accept and agree to be bound by the license terms]**. 

VeraCrypt will briefly explain how to uninstall it.

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-209.png)

*Figure 11: Reviewing the option to uninstall VeraCrypt*

**Step 19.** **Click** **[OK]** 

**Step 20.** **Type** the passphrase you use to log in to your computer and press *Enter* to complete the VeraCrypt installation

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-210.png)  

*Figure 12: Installation of VeraCrypt*

**Step 21.** **Press** *Enter* to close the window shown in *Figure 8*

**IMPORTANT**: If having encryption software on your computer could get you into serious trouble, you should remove VeraCrypt entirely, then extract it onto a USB storage device in *portable mode*.

**Note**: Users are encouraged to consult the [**VeraCrypt** Beginner's Tutorial](https://veracrypt.codeplex.com/wikipage?title=Beginner%27s%20Tutorial) after working through this guide.


# 3. Create a standard volume

VeraCrypt lets you create two kinds of encrypted volumes: **Hidden** volumes and **standard** volumes. 

* **Standard volumes** protect your files with a passphrase that must be entered in order to access them.
* **Hidden volumes** have *two* passphrases. You can enter one of them to open a *decoy* standard volume in which you should store less sensitive files that you are willing to "give up" if necessary. Entering the other passphrase will open the hidden volume containing your truly sensitive files.

In this section, you will learn how to create a **standard volume**. If you want to create a *hidden volume*, you should complete this section, then continue on to [Creating a hidden volume](#2330).

To create a *standard volume* with VeraCrypt, perform the following steps.

**Step 1**. **Launch** VeraCrypt to open the main application window

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-301.png)

*Figure 1: The main VeraCrypt window*

**Step 2**. **Click** **[Create Volume]** to activate the following *VeraCrypt Volume Creation Wizard* window: 

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-302.png)

*Figure 2: Volume Creation Wizard window*

A VeraCrypt *container file* is an encrypted volume that is stored within a single file. This *container* can be renamed, moved, copied or deleted like any other file. In this section, we will create a *container* file. Please refer to the [VeraCrypt documentation](https://veracrypt.codeplex.com/documentation) to learn more about the other option. 

**Step 3**. **Click** **[Next]** to select which type of volume you would like to create:

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-303.png)

*Figure 3: The Volume Type window*

The "*VeraCrypt Volume Creation Wizard Volume Type*" window lets you specify whether you want to create a *Standard* or *Hidden* volume. 

**Note**: For more information about *How to Create a Hidden Volume*, please refer to the [**Hidden volumes**](#2330) section. 

**Step 4**. Make sure that *Standard VeraCrypt Volume* is selected and **click** **[Next]** to choose a name and location for your VeraCrypt *container* file.

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-304.png)

*Figure 4: The Volume Creation Wizard - Volume Location input*

**Step 5**. **Click** **[Select File…]** to choose a location for your VeraCrypt container file and specify a name for it.

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v02-003.png)

*Figure 5: Selecting a location and filename for your container*

**Step 6**. **Navigate** to the folder in which you would like to create your container

**Step 7**. **Choose** a filename for your container and **type** it into the field at the top of the window

**Note**: Do not select a file that already exists! And be sure to remember where you put your *container* and what you call it.

In this example, we created a *container* called *volume* on the *Desktop*, but your *container* can have any filename and any file extension. For example, you can name your *container* *recipes.docx* or *holidays.mpg* in hopes that a casual observer will think it is a Microsoft Word document or a video file. This is one way you can help disguise the existence of a VeraCrypt container, but it will not work against someone with the time and resources to search your device thoroughly.

If you want to create a VeraCrypt container on a **USB storage device**, simply navigate to the device (rather than to a folder on your computer) before choosing a filename.

**Step 8**. **Click** **[Save]** once you have determined a location and chosen name for your VeraCrypt container file:

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v02-305.png)

*Figure 6: the filename and location you have chosen for your container*

**Step 9**. **Click** **[Next]** to configure your *Encryption Options*

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-306.png)

*Figure 7: The Volume Creation Wizard Encryption Options window*

Here you can choose a specific method (or *algorithm* ) to use when encrypting and decrypting the files stored within your **VeraCrypt** container. The default options are considered secure, so you should probably leave them as they are.

**Step 10**. **Click** **[Next]** to select a *volume size*

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-307.png)

*Figure 8: The Volume Creation Wizard displaying the Volume Size window*

The *Volume Size* window lets you specify the size of the *container* you are about to create. In this section, we will create a 250 MB volume, but you might want to specify a different size. Consider the number of files — and, more importantly, the *types* of files — you intend to store in your encrypted volume. Image files and videos, in particular, can fill up a small VeraCrypt container very quickly.

**Tip**: If you think you might want to backup your container file on a CD, you should choose a size that is 700 MB or less. For a DVD backup, it should be 4.5 GB or less. If you intend to upload the container file to an online storage service, you will have to determine a reasonable size based on the speed of your Internet connection.

**Step 11**. **Type** the size of the volume you would like to create. *Make sure you select the correct value for **MB** (megabytes) or **GB** (gigabytes)*.

**Step 12**. **Click** **[Next]** to choose a passphrase

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-308.png)

*Figure 9: Volume Creation Wizard featuring the Volume Password window*

**IMPORTANT**: Choosing a strong passphrase is one of the most important steps you will perform when creating a VeraCrypt volume. The stronger the passphrase, the better. Please refer to the [Create and maintain secure passwords](../passwords) and [**KeePassX**](../keepassx/linux) guides to learn more about good password practices. The button labelled "Next" will remain disabled until the two passphrases you have entered match. If your passphrase is weak, you will see a warning. Consider changing it! Though VeraCrypt will accept any passphrase, your data will not be secure unless you choose a strong one.

**Step 13**. Type your passphrase and then re-type it into the *Confirm* field to activate the *Next* button. 

**Step 14**. Click **[Next]** to select a filesystem type

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-309.png)

*Figure 10: Volume Creation Wizard featuring the Volume Format window*

**Note:** The default value ("FAT") will work for most people and is compatible with Linux, Windows and Mac OS X computers. However, if you intend to store files that are larger than 4 GB (for a single file), then you will have to select a different *Filesystem type*. *Linux Ext2* will only work on Linux computers, and *NTFS* will work on Windows computers and *most* Linux computers.

**Step 15.** **Click** **[Next]** after choosing an appropriate *Filesystem type*

VeraCrypt is now ready to create a *standard encrypted volume within a container file*. If you move your mouse within the *VeraCrypt Volume Creation Wizard* window, it will produce random data that will help strengthen the encryption.

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-310.png)

*Figure 11: Volume Creation Wizard featuring the Volume Format window*

**Step 16.** **Click** **[Format]** to begin creating your standard volume. 

VeraCrypt will let you know when it has finished creating your encrypted volume.

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-311.png)

*Figure 12: Volume has been successfully created*

**Step 17.** **Click** **[OK]** 

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-312.png)

*Figure 13: Exit or create another encrypted volume*

**Step 18**. **Click** **[Exit]** to close the *VeraCrypt Volume Creation Wizard* and return to VeraCrypt's main window. (If you click **[Next]**, VeraCrypt will begin walking you through the process of creating another encrypted volume.)

You should now see your 250 MB *container* file in the location you chose in *Step 6*. 


# 4. Creating a hidden volume

In VeraCrypt, a *hidden volume* is stored within your encrypted *standard volume*, but its existence is concealed. Even when your standard volume is *mounted*, it is not possible to confirm the existence of a hidden volume without its passphrase (which is separate from that of the *standard volume*). 

A *hidden volume* is a bit like a secret compartment in a locked briefcase. You store *decoy* files that you do not mind having confiscated in the briefcase while keeping your most sensitive files in the secret compartment. The point of a *hidden volume* is to hide its own existence, thereby hiding the files within it, even if you are forced to reveal the passphrase to your *standard volume*. For this technique to be effective, you must create a situation where the person demanding to see your files will be satisfied by what you show them. To do this, you may want to implement some of the following suggestions: 

* Put some confidential documents that you do not mind having exposed in the standard volume. This information must be sensitive enough that it would make sense for you to keep it in an encrypted volume. 

* Update the files in the standard volume on a regular basis. This will create the impression that you really are using those files.

* Be aware that someone demanding to see your files might know about the concept of hidden volumes. If you are using VeraCrypt correctly, this person will not be able to *prove* that your hidden volume exists, but he/she might *suspect* it.

As mentioned above, a *hidden volume* is technically stored inside a *standard volume*. This is why VeraCrypt sometimes refers to them as "inner" and "outer" volumes. Fortunately, you do not have to *mount* the latter to access the former. Instead, VeraCrypt allows you to create two separate passphrases: one that opens the outer or ("decoy") *standard volume*  one that opens the inner *hidden volume.*

You can create hidden volumes by following the steps below: 

**Step 1**. **Launch** VeraCrypt to open the main application window

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-301.png)

*Figure 1: The main VeraCrypt window*

**Step 2**. **Click** **[Create Volume]** to activate the following *VeraCrypt Volume Creation Wizard* window: 

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-302.png)

*Figure 2: Volume Creation Wizard window*

A VeraCrypt *container file* is an encrypted volume that is stored within a single file. This *container* can be renamed, moved, copied or deleted like any other file. In this section, we will create a *container* file. Please refer to the [VeraCrypt documentation](https://veracrypt.codeplex.com/documentation) to learn more about the other option. 

**Step 3**. **Click** **[Next]** to select which type of volume you would like to create:

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-401.png) 

*Figure 3: The Volume Type window*

**Step 4**. **Select** ***Hidden VeraCrypt volume*** and click **[Next]**

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-304.png) 

*Figure 4: The Volume Creation Wizard - Volume Location input*

**Step 5**. **Click** **[Select File...]** to select the name and location for a new container file within which we will create both an outer *standard volume* and an inner *hidden volume*.

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v02-004.png) 

*Figure 5: Selecting a location and filename for your container*

**Step 6**. **Navigate** to the folder in which you would like to create your container

**Step 7**. **Choose** a filename for your container and **type** it into the field at the top of the window

**Note**: Do not select a file that already exists! And be sure to remember where you put your *container* and what you call it.

In this example, we created a *container* called *volume2* on the *Desktop*, but your *container* can have any filename and any file extension. For example, you can name your *container* *recipes.docx* or *holidays.mpg* in hopes that a casual observer will think it is a Microsoft Word document or a video file. This is one way you can help disguise the existence of a VeraCrypt container, but it will not work against someone with the time and resources to search your device thoroughly.

If you want to create a VeraCrypt container on a **USB storage device**, simply navigate to the device (rather than to a folder on your computer) before choosing a filename.

**Step 8**. **Click** **[Save]** once you have determined a location and chosen name for your VeraCrypt container file:

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v02-402.png) 

*Figure 6: the filename and location you have chosen for your container*

**Step 9**. Click **[Next]** to configure the *encryption options*

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-403.png)

*Figure 7: VeraCrypt Outer Volume Encryption Options*

Here you can choose a specific method (or *algorithm* ) to use when encrypting and decrypting the files stored within your **VeraCrypt** container. The default options are considered secure, so you should probably leave them as they are.

**Step 10**. **Click** **[Next]** to select a *volume size*

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-404.png)

*Figure 8: VeraCrypt Outer Volume Size*

The *Volume Size* window lets you specify the size of the *container* you are about to create. In this section, we will create a 250 MB volume, but you might want to specify a different size. Consider the number of files — and, more importantly, the *types* of files — you intend to store in your encrypted volume. Image files and videos, in particular, can fill up a small VeraCrypt container very quickly.

**Tip**: If you think you might want to backup your container file on a CD, you should choose a size that is 700 MB or less. For a DVD backup, it should be 4.5 GB or less. If you intend to upload the container file to an online storage service, you will have to determine a reasonable size based on the speed of your Internet connection.

**Step 11**. **Type** the size of the volume you would like to create. *Make sure you select the correct value for **MB** (megabytes) or **GB** (gigabytes)*.

**Step 12**. **Click** **[Next]** to choose a passphrase

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-405.png)

*Figure 9: VeraCrypt Outer Volume Password screen*

**IMPORTANT**: Even though this is the passphrase for your "decoy" volume, you should still choose a strong passphrase. Please refer to the [Create and maintain secure passwords](../passwords) and [**KeePassX**](../keepassx/linux) guides to learn more about good password practices. The button labelled "Next" will remain disabled until the two passphrases you have entered match. If your passphrase is weak, you will see a warning. Consider changing it! Though VeraCrypt will accept any passphrase, your data will not be secure unless you choose a strong one.

**Step 13**. Type your passphrase and then re-type it into the *Confirm* field to activate the *Next* button. 

**Step 14**. Click **[Next]** 

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-406.png)

*Figure 10: VeraCrypt Outer Volume Format screen*

VeraCrypt is now ready to create a *standard volume in a container file*. You will create your *hidden volume* inside this *standard volume* later. If you move your mouse within the *VeraCrypt Volume Creation Wizard* window, it will produce random data that will help strengthen the encryption.

**Step 15**.  **Click** **[Format]** to begin creating your outer volume. This will require administrative privileges.

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v02-407.png)

*Figure 11: Administrator privileges screen*

**Step 16**. **Type** the passphrase you use to login to your computer into the pop-up window and **click** **[OK]**

When VeraCrypt has finished creating your *outer volume*, it will display the *Outer Volume Contents* screen. It may also open a file browser window showing the contents of your (currently empty) VeraCrypt volume.

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-408.png)

*Figure 12: VeraCrypt Outer Volume Contents screen*

This screen suggests that you put some "decoy" files into your *outer volume*. You will have a chance to do this later on, as well.

**Step 17**. **Click** **[Next]** to determine how much space you have for your *hidden volume*

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-409.png)

*Figure 13: VeraCrypt Hidden Volume screen*

**Step 18**. **Click** **[Next]** to select *Encryption Options* for your *hidden volume* 

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-410.png)

*Figure 14: VeraCrypt Hidden Volume Encryption Options screen*

Here you can choose a specific method (or *algorithm* ) to use when encrypting and decrypting the files stored within your *hidden volume*.  The default options are considered secure, so you should probably leave them as they are.

**Step 19**. **Click** **[Next]** to choose a size for your *hidden volume*

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-411.png)

*Figure 15: VeraCrypt Hidden Volume Size screen*

**Note:** The hidden volume cannot be larger than the amount of free space in the volume you just created.

**Step 20**. **Click** **[Next]** to choose a passphrase for your *hidden volume* 

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-412.png)

*Figure 16: VeraCrypt Hidden Volume Password screen*

**Step 21**. **Choose** a strong passphrase to protect your hidden volume and **type** it in. Enter it a second time into the *Confirm* field. 

**Note:** Your hidden volume password must be different from your standard volume password. If you choose the same password for both, you will not be able to access your hidden volume.

**IMPORTANT:** Choosing a strong passphrase — especially for your *hidden volume* — is one of the most important steps you will perform when creating a VeraCrypt volume. The stronger your *hidden volume* passphrase the better. And, because you might not want to record this particular passphrase in a *password manager* like [**KeePass**](../keepassx/linux), you should try to [come up with something that is both strong and memorable](../passwords).

**Step 22**. **Click** **[Next]** to select a filesystem type

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-413.png)

*Figure 17: VeraCrypt Format Options screen*

**Note:** The default value ("FAT") will work for most people and is compatible with Linux, Windows and Mac OS X computers. However, if you intend to store files that are larger than 4 GB (for a single file), then you will have to select a different *Filesystem type*. *Linux Ext2* will only work on Linux computers, and *NTFS* will work on Windows computers and *most* Linux computers.

**Step 23**. **Click** **[Next]** after choosing an appropriate *Filesystem type*

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-414.png)

*Figure 18: VeraCrypt Hidden Volume Format screen*

**Step 24**. **Click** **[Format]** to begin creating your *hidden volume*. 

VeraCrypt will let you know when it is done creating your *hidden volume*. 

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-415.png)

*Figure 19: The VeraCrypt Hidden Volume protection warning message*

**Step 25**. **Click** **[OK]** to display the *Volume Created* screen

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-416.png)

*Figure 20: VeraCrypt Hidden Volume created*

**Step 26**. **Click** **[Exit]**  to close the VeraCrypt *Volume Creation Wizard* and return to VeraCrypt's main window. (If you click [Next], VeraCrypt will begin walking you through the process of creating another encrypted volume.)

You can now store files in your *hidden volume*. They will remain undetectable even to someone who has obtained the passphrase for your *standard volume*.


# 5. Using your VeraCrypt volume

This section of this guide explains how to use standard and hidden VeraCrypt volumes on Linux. 

## 5.1. How to mount a volume

In VeraCrypt, to *mount* a volume is to make it available for use. When you successfully mount a volume it appears as if you have attached a portable storage device to your computer. You can use this disk as usual to access, create, modify or delete files and folders. When you are done using it, you can *dismount* it and the new disk will disappear.You mount a hidden volume the same way as a standard volume. Depending on which passphrase you enter, VeraCrypt will determine whether to mount the standard or hidden volume.

To mount your volume, perform the following steps: 

**Step 1**. Open VeraCrypt through your system's dashboard and the following main application window will appear:

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-301.png)

*Figure 1: The main window of VeraCrypt*

**Step 2**. Select any slot available from the list in the main window of VeraCrypt:

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-501.png)

*Figure 2: The main window of VeraCrypt with an available drive selected*

**Note**: We have chosen to mount our encrypted volume on drive 4. You can choose any of the drive numbers shown each time you mount a volume.

**Step 3**. Click on **[Select File…]** and locate your VeraCrypt *container* file. Select the *container* file you want to mount, then click **[Open]** to return to the **VeraCrypt** main window. The location of your *container* file will be displayed just to the left of the **[Select File...]** button you clicked earlier.

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-502.png)

*Figure 3: The main window of VeraCrypt with a container selected*

**Step 4**. Click **[Mount]** to enter your passphrase.

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-503.png)

*Figure 4: The Enter Password screen*

**Step 5**. Type your passphrase in the *Password* box. 

If your *container* does not include a *hidden volume*, simply **type** your *standard volume* passphrase and **click** **[OK]**. If it does include a *hidden volume*, choose one of the options below:

* To open the *hidden volume*, enter your *hidden volume* passphrase

* To open the *standard volume* **while being observed by someone from whom you would like to hide the existence of that volume**, enter your *standard volume* passphrase

* To open the *standard volume* and **modify your "decoy" files (presumably while you are not being observed)**, please read about [protecting your hidden volume when modifying the contents of its outer volume](#2334).

**Step 6**. Click **[OK]** to mount the volume. Doing so will require administrative privileges

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v02-407.png)

*Figure 5: Administrative privileges screen*

**Step 7.** **Type** the passphrase you use to login to your computer and press *Enter*

If either your VeraCrypt or your administrative passphrase was incorrect, VeraCrypt will ask you to try again. If they were both correct, VeraCrypt will mount your encrypted volume as shown below.

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v02-504.png)

*Figure 6: The VeraCrypt main window displaying the newly mounted volume*

**Step 8**. Enter the mounted volume.

There are two ways to enter a mounted volume: 

1. **Double click** the highlighted entry in the main window of VeraCrypt as shown above
2. **Navigate** to the folder normally, as you would to an external USB storage device

The volume shown below is empty. Once you have stored files there, they will be able to access or modify them whenever your volume is mounted.

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v02-506.png)

*Figure 7: Inside the mounted VeraCrypt volume*

**IMPORTANT:** While your VeraCrypt volume is mounted, the files inside are not protected and are freely accessible to anyone with access to your computer. To protect your sensitive files, you must dismount your VeraCrypt volume when you are not using it. Keep this in mind when you step away from your computer and in circumstances where you face an increased risk of confiscation or theft. Leaving your encrypted volumes mounted is like owning a safe and leaving the door wide open. If you shut down, restart or switch off your computer, your encrypted volume will be inaccessible until it is mounted again. You might want to practice doing one of these things as quickly as possible.


## 5.2. How to dismount a volume

In VeraCrypt, to dismount a volume is to make it unavailable for usage. To dismount a volume and ensure that nobody can access the files within it unless they know the appropriate passphrase, perform the following steps:

**Step 1**. Select the volume from the list of mounted volumes in the main VeraCrypt window.

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-507.png)

*Figure 1: Selecting the Standard Volume to be dismounted*

**Step 2**. Click on **[Dismount]** to dismount the **VeraCrypt** volume. 

To retrieve a file stored in your standard volume once you have closed or dismounted it, you will have to mount it again.

**IMPORTANT**: Make sure to dismount your VeraCrypt volume before: 

* Putting your computer into *Standby* or *Hibernate* mode 
* Leaving your computer unattended 
* Entering a situation in which your computer is more likely than usual to be lost, stolen or confiscated 
* Removing the USB storage device in which you have saved your *container* (if relevant) 

**Step 3**. **Right-click** on the VeraCrypt icon in the *Windows system tray* and **select** **[Quit]** to exit VeraCrypt.

**Tip**. Merely closing the *main window* by clicking **[Exit]** is not enough to quit the application completely. 

## 5.3. How to protect a hidden volume when modifying the content of its outer volume

As discussed at the end of the section on [Creating a hidden volume](#2330), when you mount a VeraCrypt volume, you can choose to *Protect hidden volume against damage caused by writing to outer volume*. This allows you to add new "decoy" files to your standard volume without the risk of accidentally deleting or corrupting the contents of your hidden volume. You should not activate the *Protect hidden volume* feature when trying to hide the existence of your *hidden volume* from someone who is forcing you to enter your decoy passphrase, however, because doing so requires that you enter *both* of your passphrases (which is a pretty clear indication that you have a *hidden volume* in there somewhere). 

When updating your decoy files in private, however, you should *always* enable this feature. 

To use the *Protect hidden volume* feature, perform the following steps:

**Step 1**. Select a drive from the list in the main window of VeraCrypt:

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-501.png)

*Figure 1: The main window of VeraCrypt with an available drive selected*

**Step 2**. Select the container file you want to mount, then click **[Open]** to return to the VeraCrypt main window. The location of your container file will be displayed just to the left of the [Select File...] button you clicked earlier.

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-502.png)

*Figure 2: The main window of VeraCrypt with a container selected*

**Step 4**. Click **[Mount]** to open the *Enter Password* screen

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-503.png)

*Figure 3: The Enter Password screen*

**Step 5.** Type your **outer volume** passphrase in the *Password* box, as if you were going to mount it normally, **but do not click [OK]**

**Step 6.** Click **[Options]** instead, which will allow you to protect your *hidden volume* while modifying the contents of your *standard volume*

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-508.png)

*Figure 4: Protecting hidden volume when mounting outer volume*

**Step 7.** Check the box labelled *Protect hidden volume against damage caused by writing to outer volume*.

**Step 8.** Type your *hidden volume* passphrase where indicated.

**Step 9.** Click **[OK]** and then subsequently type in your *system's* password in the pop-up window.

**Step 10.** Click **[OK]** to mount your *standard volume* while protecting your *hidden volume* from accidental damage. VeraCrypt will let you know when it's done.

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-509.png)

*Figure 5: VeraCrypt's "Hidden volume is now protected" screen*

**Step 11.** Click on **[OK]** to return to the main VeraCrypt window.

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v02-005.png)

*Figure 6: VeraCrypt main window*

**Step 12.** Enter the mounted volume.

As when mounting a volume normally, there are two ways to enter a mounted volume: 

1. **Double click** the highlighted entry in the main window of VeraCrypt.
2. **Navigate** to the folder normally, as you would to an external USB storage device 

The volume shown below is empty. But, once you have stored "decoy" files in your *standard volume*, they will be accessible whenever you mount it. And, if you have protected your *hidden volume* with the steps above, you will be able to add or modify files. 

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-506.png)

*Figure 7: Inside the mounted VeraCrypt standard volume with a protected hidden volume*

**When you are done modifying the contents of your standard volume, you can dismount it by following the usual steps**, which are described under [Dismounting a volume](#2333), above. The next time you go to mount a volume, the *Protect hidden volume against damage caused by writing to outer volume* box will be *unchecked* by default.

# 6. Managing your VeraCrypt container

In this section you will learn how to import content from a TrueCrypt volume, how to back up your VeraCrypt containers and how to change your passphrases for them. 

## 6.1. How to import content from a TrueCrypt container

VeraCrypt can mount **TrueCrypt** volumes. Given that TrueCrypt is no longer maintained, you should probably move your files to a VeraCrypt volume as soon as possible. The easiest way to do this is to: 

1. Create a new VeraCrypt volume as large as (or larger than) your existing TrueCrypt volume 
2. Open both volumes at the same time 
3. Copy everything from the TrueCrypt volume to the VeraCrypt volume

For the first item, above, see [Creating a standard volume](#2329) (and, if appropriate, [Creating a hidden volume](#2330)). This section assumes that you already have one or more appropriately sized VeraCrypt volumes. The steps below address the process of moving files from a TrueCrypt *standard volume* to a VeraCrypt *standard volume* that has already been mounted. If you have files in *both* the *standard* and *hidden* volumes of a TrueCrypt container, simply make sure that your VeraCrypt volumes are large enough, then work through the following steps twice — once for each volume.

With the VeraCrypt *main window* open, and your new VeraCrypt volume mounted, carry out the following steps:

**Step 1**. Click on a drive letter that is *not* already taken by a mounted **VeraCrypt** volume.

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-510.png)

*Figure 1: VeraCrypt's main window showing a mounted volume*

**Step 2**. Click on **[Select File…]** and locate your VeraCrypt container file. Select the container file you want to mount, then click on **[Open]** to return to the VeraCrypt main window. The location of your container file will be displayed just to the left of the [Select File...] button you clicked earlier.

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-511.png)

*Figure 2: VeraCrypt's main window with a TrueCrypt container selected*

**Step 3**. Click on **[Mount]** to enter the passphrase for your **TrueCrypt** volume.

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-512.png)

*Figure 3: The VeraCrypt password screen in TrueCrypt mode*

**Step 6**. Check the **TrueCrypt Mode** box.

**Step 7**. Type the passphrase for your *TrueCrypt* volume.

**Step 8**. Click on **[OK]** to return to the *main window*. 

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-513.png)

*Figure 4: VeraCrypt's main window with both volumes mounted*

**Step 9**. Double click on the drive letter for your mounted **TrueCrypt** volume to enter it. 

**Step 10**. Return to the *main window* and double click on the drive letter for your mounted **VeraCrypt** container to enter it.

**Step 11**. Select the contents of your **TrueCrypt** volume and drag them to the window representing your **VeraCrypt** volume. 

After your files have been copied over, you should *dismount* both volumes. 

**Step 12**. Return to **VeraCrypt's** *main window*.

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-513.png)

*Figure 5: VeraCrypt's main window*

**Step 13**. Select the drive letter for your mounted **TrueCrypt** volume.

**Step 14**. Click on **[Dismount]** to dismount your **TrueCrypt** volume.

**Step 15**. Select the drive letter for your mounted **VeraCrypt** volume.

**Step 16**. Click **[Dismount]** to dismount your **VeraCrypt** volume.

## 6.2. How to change one or both passphrases for a VeraCrypt container

To change the passphrase of a VeraCrypt *volume*, start from the *main screen* and follow the steps below. These steps apply to both *standard volumes* and *hidden volumes* within VeraCrypt *containers*. However, if you want to change *both* passphrases, you will need to go through this process twice.

**Step 1**. Click on **[Select File...]** to choose the *container* for which you want to change the passphrase. 

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-301.png)

*Figure 1: VeraCrypt's main window*

**Step 2.** Select a container file and click on "**Open**" to return to the main window.

**Step 3**. Click on **[Volumes Tools...]** and  select **[Change Volume Password...]**.

This will activate the **Change Password** screen:

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-602.png)

*Figure 2: VeraCrypt's Change Password screen*

**Tip:** If you have both a standard volume and a hidden volume in this container, VeraCrypt will automatically determine which password to change based on what you enter in the Current Password field. If you want to change both passwords, you will need to go through this process twice.

**Step 4**. Type in your current passphrase. 

**Step 5**. Type your new passphrase twice. 

**Step 6**. Click on **[OK]** to begin generating a new key. 

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-603.png)

*Figure 3: VeraCrypt's Random Pool Enrichment screen*

**Step 7.** Click on "**Continue**" through the above screen.

You have given VeraCrypt your new passphrase. It will now use that passphrase (along with a pool of *random data*) to generate a new *header key*. VeraCrypt will use that *header key* to protect the *master key* that encrypts your actual data. **The master key itself does not change when you change your passphrase.**

**IMPORTANT:** Because of the way VeraCrypt manages its encryption keys, it is *not* a good idea to copy your own *container* and give it to someone else, then have them change the passphrase on their copy. (Even if you *also* change the passphrase on *your* copy.) 

While they would not be able to open *your* volume with *their* passphrase, they could, theoretically: 

* Access their own *header key* using their own passphrase; 
* Use that *header key* to decrypt the (shared!) *master key*; 
* Obtain a copy of your *container*, at some point in the future; and 
* Use the shared *master key* to decrypt *your* data

Similarly, if you ever suspect that someone might have *both* a copy of your container *and* knowledge of your passphrase, you should not just change your passphrase. You should instead generate an entirely *new* container (with a new passphrase, of course), then copy over your files and delete the old container.

VeraCrypt will let you know when it is done generating a new key for your encrypted volume

![](/sites/securityinabox.org/files/media/veracrypt-lin-en-v01-604.png)

*Figure 4: VeraCrypt passphrase successfully changed*

**Step 8**. Click on **[OK]** to complete the process of changing your passphrase.

# FAQ

***Q***: Am I going to have to spend all my time typing passphrases into **VeraCrypt**?

***A***: No, you only need to enter your passphrase once to open an encrypted volume. After that, you can access your files without a passphrase until you close the volume

***Q***: Can I uninstall **VeraCrypt** if I don't want it any more? If I do, will my files remain encrypted?

***A***: Yes. You can uninstall **VeraCrypt** by opening *Terminal*, typing `sudo veracrypt-uninstall.sh` and entering the passphrase you use to login to your computer. You can later reinstall **VeraCrypt** to access the files in your containers, which will remain encrypted and will not be deleted when you remove **VeraCrypt**. Similarly, if you transfer your encrypted *container file* another computer, you will need your passphrase and the **VeraCrypt** program to open it.

***Q***: What kinds of information require encryption?

***A***: Ideally, you should encrypt all your documents, pictures and any other files that contain private and sensitive information. And, if your operating system supports it, you should configure *full disk encryption* so that *all* of your files are encrypted whenever your computer is turned off

***Q***: How secure will my files be?

***A***: **VeraCrypt** has been independently tested and reviewed by security experts to verify how well it performs and to determine whether or not it provides all of the functions it claims to support. The results suggest that **VeraCrypt** offers a very high level of protection. However, choosing a strong passphrase is essential to the security of your data.

***Q***: Why would I use a *hidden volume*?

***A***: **VeraCrypt's** *standard volumes* protect your files with strong encryption. *Hidden volumes*, which provide the same level of encryption, are designed to give you more options if someone demands your **VeraCrypt** passphrase. Rather than giving up your *hidden volume* passphrase, you can give up your *standard volume* passphrase. If asked, you can deny that you have a *hidden volume*. To use this feature properly, however, you will a strong grasp of your own security environment, a good understanding of how **VeraCrypt** works and a convincing set of "decoy" files in your *standard volume*.

***Q***: How do I mount my original *standard volume*, rather than the one that's hidden?

***A***: It all depends on which passphrase you enter in the password screen. If you enter the *standard volume* passphrase, **VeraCrypt** will mount the *standard volume*. If you enter the *hidden volume* passphrase, **VeraCrypt** will mount the *hidden volume*. That way, if someone demands that you open your **VeraCrypt** container, you can mount the *standard volume* and deny the existence of a *hidden volume*. Under the right circumstances, this might be enough to get you off the hook and out of trouble.

***Q***: Is it possible to inadvertently damage or delete a *hidden volume*?

***A***: Yes. If you continue adding files to your *standard volume* until you run out of space for your hidden volume, your *hidden volume* will be damaged or destroyed. There is an option when you mount the standard volume that you can use to protect your *hidden volume* from being damaged when modifying the contents of your *standard volume*. You should not use this option while being observed, as it reveals the existence of a *hidden volume*.

***Q***: Can I change the size of a VeraCrypt volume after creating it? 

***A***: No. You will have to create a new container with a larger volume, then move your files form the old volume to the new one. You can do this by mounting both volumes at the same time. This applies to both standard and hidden volumes.

***Q***: Can I use tools like **chkdsk** on the contents of a mounted **VeraCrypt** volume?

***A***: **VeraCrypt** volumes behave like normal storage devices, so it is possible to use any file system checking/repairing/defragmenting tools on the contents of any mounted **VeraCrypt** volume.

***Q***: Is it possible to change the passphrase for a *hidden volume*?

***A***: Yes. The passphrase change feature applies to both *standard* and *hidden volumes*. Just type the passphrase for the *hidden volume* into the Current Password field of the Password Change screen.

- [**Official VeraCrypt FAQ**](https://veracrypt.codeplex.com/wikipage?title=FAQ)
