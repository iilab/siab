

---

lang: en
community: guide
type: tools
os: os-x
weight: 025
title: VeraCrypt for Mac OS X - secure file storage

---

**VeraCrypt** encrypts your sensitive data and prevents anyone who does not have the correct passphrase from accessing them. It works like an electronic safe in which you can securely store your files.

# Required reading


{{ required_reading: ../../secure file storage }}


{{ tool: ./025-tool.md }}

# What you will get from this guide

- The ability to protect your files if your computer or USB storage device lost, stolen or confiscated
- The ability to move your sensitive files between Mac OS X, Windows, and Linux computers without decrypting them
- A secure way to backup important files 

# 1. Introduction to VeraCrypt





## 1.0 Other Tools Like VeraCrypt

**GNU Linux, Mac OS X and other Microsoft Windows Compatible Programs:**

**VeraCrypt** is also available for **GNU Linux** and **Microsoft Windows**.  This guide covers the **Mac OS X** version.

**Mac OS X** offers full-disk encryption with its built-in **FileVault2** utility. We recommend enabling full-disk encryption. In addition, you can use the built in **Disk Utility** to create encrypted volumes on a USB storage devices. Unlike **VeraCrypt**, however, this will only allow you to access your files on other **Mac OS X** devices. You can use **VeraCrypt** to move files between, Mac OS X, Microsoft Windows, and Linux.

Many **GNU Linux** distributions, including **[Ubuntu]**, support full-disk encryption as a standard feature. We recommend enabling full-disk encryption when you install **Linux**, as it is far easier than doing so later. In addition, you can use the built-in **Disk Utility** on most **Linux** distributions to create an encrypted volume on a USB storage device. Unlike **VeraCrypt**, however, this will only allow you to access your files on other **Linux** computers. You can use **VeraCrypt** to move files between **Linux**, **Mac OS X** and **Windows**.

Full-featured editions of **Windows** since **Windows 7** contain the [**BitLocker**](http://windows.microsoft.com/en-us/windows7/products/features/bitlocker) full-disk encryption utility. (This includes Windows 7 Ultimate, Windows 7 Enterprise, Windows 8 Pro, Windows 8 Enterprise and Windows 10 Pro). 

Both **FileVault** (for **Mac OS**) and **BitLocker** (for **Windows**) are proprietary software. As a result, the security they provide can not be independently verified. Nonetheless, it is a good idea to enable them if possible. You can use **VeraCrypt**, in addition to these built-in tools, to protect your most sensitive files and to move them between Linux, Mac OS X and Windows computers.

Additional **Microsoft Windows** alternatives to **VeraCrypt** include:

- [**DiskCryptor**](https://diskcryptor.net/wiki/Main_Page), which is a free and open source tool that encrypts of all disk partitions, including the system partition.
- [**AxCrypt**](http://www.axantum.com/AxCrypt/) is a free and open source tool that can encrypt individual files.

## 1.1 Things you should know about VeraCrypt before you start

**VeraCrypt** will protect your data from being accessed by encrypting it with a passphrase. It uses a process called on-the-fly encryption to protect your files.  On-the-fly encryption means that data is transparently encrypted as it is being written to a storage device and transparently decrypted as it is being read. Files can be copied to and from a mounted VeraCrypt volume just like they are copied to and from any normal storage device.

**VeraCrypt** supports both *standard encrypted volumes* and *hidden volumes*. Either one will keep your files confidential, but a *hidden volume* allows you to hide your important information behind less sensitive data in order to protect it even if you are forced to reveal a **VeraCrypt** passphrase. This guide covers the creation and use of both *standard volumes* and *hidden volumes*.  

But remember, **if you forget your passphrase, you will lose access to your data!** There is no way to recover a lost passphrase. Also, keep in mind that **the use of encryption is illegal in some jurisdictions.**

Finally, **VeraCrypt** leaves traces on devices and where it is used. These traces will not reveal the contents of encrypted files, but they may reveal the fact that **VeraCrypt** was used on that computer.

**Suggested readings:**

- [Official documentation](https://veracrypt.codeplex.com/documentation)
- [Official FAQ](https://veracrypt.codeplex.com/wikipage?title=FAQ)

# 2. Installing OSXFUSE and VeraCrypt





## 2.1 Installing OSXFUSE

**Mac OS X** needs **OSXFUSE** installed with *MacFUSE* compatibility mode activated before we can install and use **VeraCrypt**. 

**Step 1**. **Download** the latest version of **[OSXFUSE]** from [*SourceForge*](http://sourceforge.net/projects/osxfuse/files/). **Save** it to your *Downloads* folder.

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-101-downloadosxfuse.png)

*Figure 1: The OSXFUSE downloads page on SourceForge*

**Step 2**. **Find** the downloaded file in your *Downloads* folder and **double click** to mount it as a disk image. It will now show up under *Devices* in the sidebar of your *Finder* window. 

**Step 3**. There will also now be a new *Finder* window that contains the *Installer* for **OSXFUSE**, titled ‘Install OSXFUSE’. **Double click** this to begin the installation process.

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-102-runosxfuseinstaller.png)

*Figure 2: Mounted OSXFUSE disk image with installer*

**Step 4**. In the *Installer* for **OSXFUSE**, **Continue** through the *Introduction*, and **accept** the *Software License Agreement*. 

**Important**: When you get to *Installation Type*, Be sure you’ve **selected** the **MacFUSE Compatibility Layer**, or else **VeraCrypt** will not work on your device. By default the **MacFUSE Compatibility Layer** is not installed. 

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-103-osxfuseinstaller.png)

*Figure 3: Selecting the MacFUSE Compatibility Layer in the OSXFUSE Installer*

Then **click** **Install** on the next screen. You will probably be prompted to **enter** your administrative password in order to authorize the installation.

**Step 5**. The *Installer* should tell you that the installation was successful. To clean up, pleae **close** the *Installer* window. Then return to your *Finder* window and find the mounted disk image (*’FUSE for OSX’)* in the sidebar to the left under *Devices*. Please **eject** the disk image by clicking the **eject** icon to the right of the *’FUSE for OSX’* name in the sidebar.

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-104-ejectosxfuseinstaller.png)

*Figure 4: Ejecting the OSXFUSE disk image*

**Step 6**. *(Optional)* You may have seen a recommendation to restart your computer after installing **OSXFUSE** in the Introduction section of the **OSXFUSE** Installer. This is probably *not* necessary unless you had an earlier version of **OSXFUSE** or its predecessor **MacFUSE** running during this installation process. For more details, see [this] post.


## 2.2 Installing VeraCrypt

**Step 1**. **Download** the current stable version of *’VeraCryptMacOSX Setup’* from the **VeraCrypt** [downloads](https://veracrypt.codeplex.com/releases) page at https://veracrypt.codeplex.com/releases. (Don’t forget to check the *URL* to be sure it has the secure ‘https’ version of the website!) **Save** the file to your *Downloads* file.

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-201-downloadveracrypt.png)

*Figure 1: The VeraCrypt downloads page*

**Step 2**. **Find** the downloaded file in your *Downloads* folder and **double click** to mount it as a disk image. It will now show up under *Devices* in the sidebar of your *Finder* window. There will also now be a new *Finder* window that contains the *Installer* for **VeraCrypt**, titled *’VeraCrypt_1.16.pkg’*. **Double click** this to begin the installation process.

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-202-mountedveracryptinstaller.png)

*Figure 2: The mounted VeraCrypt disk image with installer*

**Step 3**. In the *Installer* for **VeraCrypt**, **Continue** through the *Introduction*, **accept** the *Software License Agreement*, and **perform** a *’standard installation’* of **VeraCrypt** on the *’Macintosh HD’*. You will probably be prompted to **enter** your administrative password in order to authorize the installation.

**Step 4**. The *Installer* should tell you that the installation was successful. To clean up, please **close** the *Installer* window. Then return to your *Finder* window and find the mounted disk image (*’FUSE for OSX’)* in the sidebar to the left under *Devices*. Please **eject** the disk image by clicking the **eject** icon to the right of the *’FUSE for OSX’* name in the sidebar.

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-203-ejectveracryptinstaller.png)

*Figure 4: Ejecting the VeraCrypt disk image*

# 3. Creating a standard volume

**VeraCrypt** lets you create two kinds of encrypted volumes: *Hidden* volumes and *Standard* volumes. 

- *Standard volumes* protect your files with a passphrase that must be entered in order to access them
- *Hidden volumes* have *two* passphrases. You can enter one of them to open a *decoy* volume containing less sensitive files that you can "give up" if necessary.

In this section, you will learn how to create a *Standard volume*. If you want to create a *Hidden volume*, you should complete this section, then continue on to [Creating a hidden volume](#2260).

To create a *Standard volume* with **VeraCrypt**, perform the following steps.

**Step 1**. **Locate VeraCrypt** in your *Applications* folder and **double click** to open the main application window.

![Main VeraCrypt window](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-301-main-window.png)

*Figure 1: The main VeraCrypt window*

**Step 2**. **Click** **[Create Volume]** to activate the *VeraCrypt Volume Creation Wizard* 

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-302-volume-creation.png)

*Figure 2: Volume Creation Wizard window* 

You have two options for encrypting a *Standard Volume*. In this guide, we will *Create an encrypted file container*. Please refer to the [**VeraCrypt** documentation](https://veracrypt.codeplex.com/documentation) to learn more about the other option. A **VeraCrypt** *container* is an encrypted file-system contained within a normal file. It can be renamed, moved, copied or deleted like any other file. 

**Step 3**. **Click** **[Next]** to select which type of volume you would like to create

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-303-standard-volume.png)

*Figure 3: The Volume Type window*

The *VeraCrypt Volume Creation Wizard Volume Type* window lets you specify whether you want to create a *Standard* or *Hidden* volume. 

**Note**: For more information about *How to Create a Hidden Volume*, please refer to the [**Hidden volumes**](#2260) section. 

**Step 4**. **Click** **[Next]** and choose a name and location for your **VeraCrypt** *container* file

![VeraCrypt's volume creation wizard's volume location input](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-304-volume-location.png)

*Figure 4: The Volume Creation Wizard - Volume Location input*

**Step 5**. **Click** **[Select File…]** to choose a location.

![VeraCrypt's volume creation wizard's file specification dialogue window](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-305-choose-location.png)

*Figure 5: Specify the location and filename of the VeraCrypt container you are about to create*

**Step 6**. Choose a location and specify a name for the **VeraCrypt** *container* file you are about to create. 

You will need to remember where you put it and what you call it. In this section, we will create our *container* on the **Desktop** and name it **My Volume**. If you want to create a **VeraCrypt** standard volume on a USB storage device instead, simply navigate to the device (rather than to your *Desktop*), and enter a file name.

**Tip**: You can use any file name or file extension for your *container*. For example, you can name your container file *recipes.doc,* or *holidays.mpg* in hopes that a casual observer will think it is a *Microsoft Word* document or a video file. This is one way you can help disguise the existence of a **VeraCrypt** container, but it will not work against someone who has the time and resources to search your device thoroughly.

**Step 7**. **Click** **[Save]** to close the *Specify Path and File Name* window and return to the *Volume Creation Wizard* window

![screenshot of VeraCrypt's volume creation wizard's file specification dialogue window showing a specified file](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-306-location-chosen.png)

*Figure 6: Volume Creation Wizard displaying the Volume Location window*

**Step 8**. **Click** **[Next]** to activate the *Encryption Options* screen

![screenshot of VeraCrypt's volume creation wizard's encryption options window](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-307-encryption-options.png)

*Figure 7: The Volume Creation Wizard Encryption Options window*

Here, you can choose a specific method (or *algorithm* ) to use when encrypting and decrypting the files stored within your **VeraCrypt** container. *The default options are considered secure,* so you should probably leave them as they are.

**Step 9**. **Click** **[Next]** and determine how large to make your encrypted volume

![screenshot of VeraCrypt's volume creation wizard's volume size window](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-308-volume-size.png)

*Figure 8: The Volume Creation Wizard displaying the Volume Size window*

The *Volume Size* window lets you specify the size of the *container* you are about to create. In this section, we will create a 250 MB volume, but you might want to specify a different size. Consider the number of files — and, more importantly, the *types* of files — you intend to store in your encrypted volume. Image files and videos, in particular, can fill up a small **VeraCrypt** container very quickly.

**Tip**: If you think you might want to backup your container file on a CD, you should choose a size that is 700 MB or less. For a DVD backup, it should be 4.5 GB or less. If you intend to upload the container file to an online storage service, you will have to determine a reasonable size based on the speed of your Internet connection.

**Step 10**. **Type** your chosen volume size into the text area, then **click** **[Next]** to choose a passphrase

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-309-volume-password.png)

*Figure 9: Volume Creation Wizard featuring the Volume Password window*

**IMPORTANT**: Choosing a strong passphrase is one of the most important steps you will perform when creating a **VeraCrypt** volume. The stronger the passphrase, the better. You don't have to choose your own passphrases (or even remember them!) if you use a *password manager* like **KeePassX**. Please refer to the [Create and maintain secure passwords](../passwords) and [**KeePassX**](../keepassx/os-x) guides to learn more about good passphrase practices.

**Step 11**. **Type** your passphrase and then **re-type** your passphrase into the *Confirm* field to activate the **[Next]** button. 

**IMPORTANT**: The button labelled "Next" will remain disabled until the two passphrases you have entered match. If your passphrase is weak, you will see a warning. Consider changing it! Though **VeraCrypt** will accept any passphrase, your data will not be secure unless you choose a strong one.

**Step 12**. **Click** **[Next]** and accept the *Volume Format* options

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-310-format-options.png)

*Figure 10: Volume Creation Wizard featuring the Format Options window*

**VeraCrypt** is now ready to create a *standard encrypted volume within a container file*. If you move your mouse within the *VeraCrypt Volume Creation Wizard* window, it will produce random data that will help strengthen the encryption.

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-311-volume-format.png)

*Figure 11: Volume Creation Wizard featuring the Volume Format window*

**Step 13**. **Click** **[Format]** to begin creating your standard volume.

![VeraCrypt's volume creation wizard's volume format progress bar](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-312-format-completed.png)

*Figure 12: Volume Creation Wizard progress bar*

**VeraCrypt** will now create a file named *My Volume* on the *Desktop*, as specified above. This file will contain a 250 MB **VeraCrypt** *standard volume container*, which you can use to store your files securely. **VeraCrypt** will let you know when it is done.

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-313-successfully-created.png)

*Figure 13: Volume has been successfully created*

**Step 14**. **Click** **[OK]** to acknowledge the completion of the creation process and return to the volume creation wizard.

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-314-volume-created.png)

*Figure 14: Exit or create another encrypted volume*

**Step 15**. **Click** **[Exit]** to close *VeraCrypt Volume Creation Wizard* and return to the **VeraCrypt's** main window. (If you **click**  **[Next]**, **VeraCrypt** will begin walking you through the process of creating another encrypted volume.)

You should now see your 250 MB *container* file wherever you created it.

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-315-container-file.png)

*Figure 15: Newly created VeraCrypt container file on the Desktop*

# 4. Creating a hidden volume

In **VeraCrypt**, a *hidden volume* is stored within your encrypted *standard volume*, but its existence is concealed. Even when your standard volume is *mounted*, it is not possible to confirm the existence of a hidden volume without its passphrase (which is separate from that of the *standard volume*). 

A *hidden volume* is a bit like a secret compartment in a locked briefcase. You store *decoy* files that you do not mind having confiscated in the briefcase while keeping your most sensitive files in the secret compartment. The point of a *hidden volume* is to hide its own existence, thereby hiding the files within it, even if you are forced to reveal the passphrase to your *standard volume*. For this technique to be effective, you must create a situation where the person demanding to see your files will be satisfied by what you show them. To do this, you may want to implement some of the following suggestions: 

- Put some confidential documents that you do not mind having exposed in the standard volume. This information must be sensitive enough that it would make sense for you to keep it in an encrypted volume. 

- Update the files in the standard volume on a regular basis. This will create the impression that you really are using those files.

- Be aware that someone demanding to see your files may know about the concept of hidden volumes. If you are using **VeraCrypt** correctly, this person will not be able to *prove* that your hidden volume exists, but they may *suspect*.

As mentioned above, a *hidden volume* is technically stored inside a *standard volume*. This is why VeraCrypt sometimes refers to them as "inner" and "outer" volumes. Fortunately, you do not have to *mount* the latter to access the former. Instead, VeraCrypt allows you to create two separate passphrases: one that opens the outer or ("decoy") *standard volume*  one that opens the inner *hidden volume.*

## 4.1 How to a Create a Hidden Volume

**Tip**: In the *Linux* and *Windows* versions of **VeraCrypt**, there are two different ways to create a *hidden volume*. Both are very similar to the process of creating a *standard volume*. 

- **Normal mode** walks you through the process of creating both a *standard volume* and the *hidden volume* within it. (You are creating a briefcase with a secret compartment.)

- **Direct mode** assumes that you already have a *standard volume* in which you want to create a *hidden volume*. (You already have the briefcase, but you want to add the secret compartment.)

In the **Mac OS X** version of **VeraCrypt**, you can only create a *hidden volume* in *standard mode*, which has you create both a new *standard volume* and the *hidden volume* within it. This means that you *cannot* create a *hidden volume*  use a *standard volume* that you’ve already created (and possibly used).

**Step 1**. **Locate VeraCrypt** in your *Applications* folder and **double click** to open the main application window.

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-301-main-window.png)

*Figure 1: The main VeraCrypt window*

**Step 2**. **Click** **[Create Volume]** to activate the *VeraCrypt Volume Creation Wizard*. 

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-302-volume-creation.png)

*Figure 2: The VeraCrypt Volume Creation screen*

**Step 3**. **Click** **[Next]** to accept the default *Create an encrypted file container* option.

**Step 4**. **Check** the *Hidden VeraCrypt volume* option

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-401-hidden-volume.png)

*Figure 3: Creating a VeraCrypt hidden volume*

**Step 5**. **Click** **[Next]** and choose a name and location for your **VeraCrypt** *container* file

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-304-volume-location.png)

*Figure 4: The Volume Creation Wizard - Volume Location input*

**Step 6**. **Click** **[Select File…]** to choose a location.

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-403-select-choose-location.png)

*Figure 5: Specify the location and filename of the VeraCrypt container you are about to create*

**Step 7**. Choose a location and specify a name for the **VeraCrypt** *container* file you are about to create. 

You will need to remember where you put it and what you call it. In this section, we will create our *container* on the **Desktop** and name it **New Volume**. If you want to create a **VeraCrypt** hidden volume on a USB storage device instead, simply navigate to the device (rather than to your *Desktop*), and enter a file name.

**Tip**: You can use any file name or file extension for your *container* that will include your *hidden volume*. For example, you can name your container file *recipes.doc,* or *holidays.mpg* in hopes that a casual observer will think it is a *Microsoft Word* document or a video file. This is one way you can help disguise the existence of a **VeraCrypt** container, but it will not work against someone who has the time and resources to search your device thoroughly.

**Step 8**. **Click** **[Save]** to close the *Specify Path and File Name* window and return to the *Volume Creation Wizard* window

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-404-select-location-chosen.png)

*Figure 6: Volume Creation Wizard displaying the Volume Location window*

**Step 9**. **Click** **[Next]** to activate the *Encryption Options* screen

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-307-encryption-options.png)

*Figure 7: The Volume Creation Wizard Encryption Options window*

Here, you can choose a specific method (or *algorithm* ) to use when encrypting and decrypting the files stored within your **VeraCrypt** container. *The default options are considered secure,* so you should probably leave them as they are.

**Step 10**. **Click** **[Next]** and determine how large to make your encrypted volume

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-308-volume-size.png)

*Figure 8: The Volume Creation Wizard displaying the Volume Size window*

The *Volume Size* window lets you specify the size of the *container* you are about to create. In this section, we will create a 250 MB volume, but you might want to specify a different size, *especially* since you intend to create a *hidden volume* inside it. Consider the number of files — and, more importantly, the *types* of files — you intend to store in both your main encrypted volume *and* your *hidden volume* inside it. Image files and videos, in particular, can fill up a small **VeraCrypt** container very quickly.

**Tip**: If you think you might want to backup your container file on a CD, you should choose a size that is 700 MB or less. For a DVD backup, it should be 4.5 GB or less. If you intend to upload the container file to an online storage service, you will have to determine a reasonable size based on the speed of your Internet connection.

**Step 11**. **Type** your chosen volume size into the text area, then **click** **[Next]** to choose a passphrase

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-309-volume-password.png)

*Figure 9: Volume Creation Wizard featuring the Volume Password window*

**IMPORTANT**: Choosing a strong passphrase is one of the most important steps you will perform when creating a **VeraCrypt** volume. The stronger the passphrase, the better. You don't have to choose your own passphrases (or even remember them!) if you use a *password manager* like **KeePassX**. Please refer to the [Create and maintain secure passwords](../passwords) and [**KeePassX**](../keepassx/os-x) guides to learn more about good passphrase practices.

**Step 12**. **Type** your passphrase and then **re-type** your passphrase into the *Confirm* field to activate the **[Next]** button. 

**IMPORTANT**: The button labelled "Next" will remain disabled until the two passphrases you have entered match. If your passphrase is weak, you will see a warning. Consider changing it! Though **VeraCrypt** will accept any passphrase, your data will not be secure unless you choose a strong one.

**Step 13**. **Click** **[Next]** and accept the *Volume Format* options

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-310-format-options.png)

*Figure 10: Volume Creation Wizard featuring the Format Options window*

**VeraCrypt** is now ready to create a *standard encrypted volume within a container file*. If you move your mouse within the *VeraCrypt Volume Creation Wizard* window, it will produce random data that will help strengthen the encryption.

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-311-volume-format.png)

*Figure 11: Volume Creation Wizard featuring the Volume Format window*

**Step 14**. **Click** **[Format]** to begin creating your standard volume.

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-312-format-completed.png)

*Figure 12: Volume Creation Wizard progress bar*

**VeraCrypt** will now create a file named *New Volume* on the *Desktop*, as specified above. This file will contain a 250 MB **VeraCrypt** *standard volume container*.

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-405-outer-volume-created.png)

*Figure 13: Newly created VeraCrypt container file on the Desktop: The ‘outer volume’ created to contain a inner, ‘hidden volume’*

**Step 15**. **VeraCrypt** will move to its *Outer Volume Contents* screen when your *standard volume container* called *New Volume* has been successfully created. Please **click** **\[Next\]** to start creating your *’inner’*, *hidden volume*. 

*Optional*: You now have the option to open (also known as to ’mount’) your *outer volume* to add files to it before moving on to create your *hidden volume*. We recommend you not do this now. If you do it after you finish creating your *hidden volume*, you’ll have more time to think about what to put into it.

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-406-outer-volume-contents.png)

*Figure 14: The ‘Outer Volume Contents’ screen shown after successfully creating an outer volume during the hidden volume creation process*

**Step 16**. **VeraCrypt** will scan the *outer volume* you have created in preparation for the creation of your inner *hidden volume*. When it is complete, it will show an interim screen. Please **click** **[Next]** to create your *hidden volume*.

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-407-hidden-volume-scan-complete.png)

*Figure 15: The post-scan screen shown before creating the hidden volume*

**Step 17**. You should now be on the *Hidden Volume Encryption Options* screen. Leave the default *Encryption Algorithm* and *Hash Algorithm* settings for the *Hidden Volume* as they are. **Click** **[Next]**.

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-408-hv-encryption-options.png)

*Figure 16: VeraCrypt Hidden Volume Encryption Options screen*

**Step 18**. On the *Hidden Volume Size* screen, will be prompted to specify the size of the *Hidden Volume* you are about to create.

As when you created your *standard volume*, consider the number and types of files you intend to store in your *hidden volume.* Image files and videos, in particular, can fill up a small VeraCrypt container very quickly. Also, make sure to leave some space for *decoy* files in your *standard volume*. If you select the maximum size available for the *Hidden Volume*, you will not be able to put any more files into the existing *standard volume*. 

In this section, we will create a 200 MB *hidden volume* inside a 250 MB *standard volume.*  This will leave a little less than 50 MB of space for *decoy* files. 

**Type** the desired hidden volume size into the corresponding text box, as shown above. Make sure the correct *unit* (KB, MB, GB or TB) is selected! (In our example, we’ll **enter** 200 and **leave** the default MB *unit* selected.) Then **click** **[Next]**.

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-409-hidden-volume-size.png)

*Figure 17: VeraCrypt Hidden Volume Size screen*

**Step 19**. You must now choose a passphrase for the *hidden volume* that is *different* from the one you chose for your *standard volume*.  Again, remember to choose a strong passphrase. Please refer to the [Create and maintain strong passwords](../passwords) section to learn more.

Please **choose** a passphrase and **type** it in twice. Then **click** **[Next]**.

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-410-hidden-volume-passphrase.png)

*Figure 18: VeraCrypt Hidden Volume Password creation screen*

**Tip**: If you use a *password manager* such as **KeePass** and are concerned about being pressured to reveal the contents of your **VeraCrypt** container, you can store the passphrase for your (decoy) *standard volume* in **KeePass**, but you should memorise the passphrase for your *hidden volume.* Otherwise, by handing over your **KeePass** passphrase, you will also reveal your *hidden volume* passphrase. 

**Step 20**. You are now on the *Format Options* screen for your *hidden volume*. The default filesystem type is fine, so **click** **[Next]**. 

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-411-hv-format-options.png)

*Figure 19: VeraCrypt Hidden Volume Format Options screen*

**Step 21**. **VeraCrypt** is now ready to create a *standard encrypted volume within a container file*. If you move your mouse within the *VeraCrypt Volume Creation Wizard* window, it will produce random data that will help strengthen the encryption. 

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-412-hidden-volume-format.png)

*Figure 20: Entropy collection during the VeraCrypt Hidden Volume Format process*

Do this for a while, then **click** **[Format]** to format the hidden volume. 

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-413-hv-format-process.png)

*Figure 21: VeraCrypt Hidden Volume Format process*

**Step 22**. When VeraCrypt is done, it will display a warning about protecting the files in your *hidden volume* when adding content to your *standard volume*. Please read the related warnings below, then **click** **[OK]** to proceed past the warning.

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-414-protect-hv-warning.png)

*Figure 22: The VeraCrypt Hidden Volume protection warning message*

**IMPORTANT**: This warning is related to how VeraCrypt hides the existence of your (inner) *hidden volume*. Normally, when you open your (outer) *standard volume*, both VeraCrypt and Windows will *think* that it occupies all of the space available within your encrypted *container* file. About 250 MB in this example. (In fact, we created a 200 MB *hidden volume* and left only about 50 MB for decoy files in our *standard volume*.) VeraCrypt can not warn you if you try to copy a 60 MB file into that 50 MB *standard volume*. This is because, if it *did* warn you, it would reveal to an observer that you had reserved space for a *hidden volume*. Instead, it will allow you to copy that 60 MB file. And, by doing so, *it will delete or corrupt the files inside your hidden volume.* 

In other words, this design is based on the assumption that you would rather *lose* the contents of your *hidden volume* than reveal their existence.

**IMPORTANT**: So, whenever you want to add decoy files to your standard volume, you must check the *protect hidden volume against damage...* box and enter both your *hidden volume* passphrase and your *standard volume* passphrase. If you enable this feature, VeraCrypt *will* be able to warn you if you try to copy too much data into your outer volume. (Clearly, entering both passphrases in front of someone else will reveal the existence of your *hidden volume*, so this is something you should only do in private or in the company of those you trust.)

The specific steps required to modify the contents of your *standard volume* are covered in more detail in Section 5.3, under [Protecting your hidden volume when modifying the contents of your outer volume](#2287)

**Step 21**. Congratulations! You have now finished created your new *hidden volume*. **Click** **[Exit]** to return to the main VeraCrypt window.

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-314-volume-created.png)

*Figure 23: The VeraCrypt Hidden Volume Created screen*

You may now store files in your *hidden volume*. They will remain undetectable even to someone who has obtained the passphrase for your *standard volume*.

# 5. Using your VeraCrypt volumes





## 5.1 Mounting a volume

In **VeraCrypt**, to *mount* a volume is to make it available for use by the operating system. This is how you turn your encrypted **VeraCrypt** *container* file into a virtual storage device (or ‘volume’) in which you can save, modify and access files. Then, when you are done using it, you can *dismount* the volume, which will turn it back into an encrypted *container* file.

To mount a *standard volume*, perform the following steps: 

**Step 1**.  **Locate** **VeraCrypt** in your *Applications* folder and **double click** to open the main application window.

**Step 2**. **Select** one of any of the numbered *’slots’* from the list in the main window of **VeraCrypt**. 

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-501-select-slot.png)

*Figure 1: The main window of VeraCrypt with an available slot selected*

**Note**: In *Figure 1*, we have chosen to mount our encrypted volume in slot *3*. You may choose any of the numbered slots shown each time you mount a volume.

**Step 3**. **Click** **[Select File…]** and locate your VeraCrypt *container* file. (In our example, this will the the initial *standard volume* we created, titled ’My Volume’ and saved on the *Desktop*.)

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-502-select-container.png)

*Figure 2: The ‘Select a VeraCrypt Volume’ screen*

**Step 4**. **Select** the *container* file you want to mount, then **click** **[Open]** to return to the **VeraCrypt** main window. The location of your *container* file will be displayed just to the left of the **[Select File...]** button you clicked earlier.

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-503-mount-volume.png)

*Figure 3: The main window of VeraCrypt with a container selected*

**Step 5**. **Click** **[Mount]** in the bottom left of the main **VeraCrypt** window. 

**Step 6**. For this example, **type** in the passphrase for your *standard volume* in the *Password* box. But remember that you can also open your *hidden* volumes here. 

If your *container* holds a hidden volume, choose one of the options below:

- To open a *hidden volume*, enter your *hidden volume* passphrase

- To open a *standard volume* in a  *container* that holds a *hidden volume*, but *without* the intention of modifying your ‘decoy’ files in the ‘outer’ volume  — **enter** your *standard volume* passphrase. (For example, *while being observed by someone from whom you would like to hide the existence of your *hidden volume*)

- To open a *standard volume* in a *container* that holds a *hidden volume* in order to modify your ‘decoy’ files in the ‘outer’ volume, **please read about [protecting your hidden volume when modifying the contents of its outer volume](#4.3)!** (In this example, you would assume that you are *not* being observed by someone you need to hide your activities from.)

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-504-enter-passphrase.png)

*Figure 4: The Enter Password screen*

**Step 7**. **Click** **[OK]** to begin mounting the *standard volume*.

**Tip**: If the passphrase you entered is incorrect (or if there’s been other errors), **VeraCrypt** will attempt to mount the volume, but then show an alert notifying you that the operation has failed:

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-506-operation-failed.png)

*Figure 5: Alert notifying that the mounting operation has failed*

If it is correct, your encrypted volume will be mounted as follows:

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-507-mount-standard-volume.png)

*Figure 6: The VeraCrypt main window displaying the newly mounted volume*

**Step 8**. **Enter** the mounted volume

There are two ways to enter a mounted volume: 

**Option One**: **Double click** the highlighted entry in the main window of **VeraCrypt** as shown in *Figure 6*, above. This will open up a new empty *Finder* window, as shown in *Figure 7* below:

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-509-enter-drive-veracrypt.png)

*Figure 7: Accessing a mounted volume through the main VeraCrypt window* 

**Option Two**: In the regular *Finder* windows, you’ll also see a new drive mounted under *Devices*, entitled ‘NO NAME’ (as shown in *Figure 8*, below). From here, you can select the drive as you would with an inserted USB flash drive or other mounted media. 

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-508-enter-drive-finder.png)

*Figure 8: Accessing a mounted VeraCrypt volume through the Finder* 

The mounted volume is currently empty. Once you have stored files there, they will be accessible (and editable) whenever you open the volume.

A mounted volume is a virtual disk that behaves like an external storage device, except that it is fully encrypted. You can copy files to and from it just like you would for a USB storage device. By dragging and dropping them, for example, or by saving them directly to the volume from within another application. Files are automatically encrypted when you copy, move or save them to the mounted volume. And, when you move a file *out* of the **VeraCrypt** volume, it is automatically decrypted. If your computer is shutdown or switched off suddenly, the encrypted volume will remain inaccessible until it is mounted again. 

**IMPORTANT:** To protect your sensitive files, you must *dismount* your **VeraCrypt** volume when you are not using it. This is especially true when you step away from your computer or encounter a situation where your computer might be confiscated. If you do not dismount your encrypted volumes, **VeraCrypt** is like a safe that you've decided to leave wide open. Assuming you suspend your computer or ‘lock’ your screen, the information it contains will have *some* protection. (In particular, any attempt to gain access to your computer by rebooting it will automatically dismount the **VeraCrypt** volume.) But, the whole point of a safe is to be *more* secure than a regular door lock, right? The same goes for **VeraCrypt**. 

## 5.2 Dismounting a volume and closing VeraCrypt

In **VeraCrypt**, to *dismount* a *volume* is to turn it back into single, encrypted *container* whose contents are no longer visible or available via the operating system. 

Therefore, on the desktop you will *dismount* volumes in order to keep them safely inaccessible from unauthorized users as encrypted *containers*. And if you keep your **VeraCrypt** *container* file on an external USB storage device, it is important to *dismount* it before removing the storage device. 

To dismount a *volume* and ensure that nobody can access the files within it unless they know the appropriate passphrase, perform the following steps: 

**Step 1**. **Select** the volume from the list of mounted volumes in the main **VeraCrypt** window

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-503-mount-volume.png)

*Figure 1: Selecting the Standard Volume to be dismounted*

**Step 2**. **Click** **[Dismount]** to dismount the **VeraCrypt** volume. 

To retrieve a file stored in your standard volume once you have closed or dismounted it, you will have to mount it again.

**Please Note** Even though you can access a mounted volume via the *Finder* window, you cannot fully **dismount** it from here. If you **eject** a mounted **VeraCrypt** volume within the *Finder* window, it will appear to **eject** within *Finder*, but it will not be properly **dismounted**. It will remain visible in its mounted slot within **VeraCrypt** and still require dismounting. Therefore, you should **only** dismount **VeraCrypt** volumes from within **VeraCrypt**.

**IMPORTANT**: To protect the integrity and security of the data in your **VeraCrypt** volumes, make sure to dismount your **VeraCrypt** volume before: 

- Removing the external USB storage device on which your *container* is stored (if you have chosen to keep it on one)
- Putting your computer into *Sleep* mode 
- Leaving your computer unattended 
- Entering a situation in which your computer is more likely than usual to be lost, stolen or confiscated 

**Step 3**. As with all applications in **Mac OS X**, it’s important to know how to completely quit **VeraCrypt**, as opposed to simply closing the **VeraCrypt** application window while the application remains open and running. 

To successfully quit **VeraCrypt** completely, **click** *File* in the main **VeraCrypt** menu, then scroll down to **select** **Quit VeraCrypt**. You can also use the shortcut key combination shown there: **Command-Q**. 

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-510-menu-quit.png)

*Figure 2: Quitting VeraCrypt completely via the main VeraCrypt menu* 

**Tip**. As discussed above, when using the installed version of **VeraCrypt** (as opposed to a portable version), merely closing the *main window* by clicking on the red ‘x’ button in the top left-hand corner of the main **VeraCrypt** window is not enough to exit the application completely. 

## 5.3 Protecting your hidden volume when modifying the contents of its outer volume

As discussed at the end of the section on [Creating a hidden volume](#2260), when you mount a **VeraCrypt** container that contains a *hidden volume*, you can choose to *Protect hidden volume against damage caused by writing to outer volume*. This allows you to add new "decoy" files to your standard volume without the risk of accidentally deleting or corrupting the contents of your hidden volume. You should not activate the *Protect hidden volume* feature when trying to hide the existence of your *hidden volume* from someone who is forcing you to enter your decoy passphrase, however, because doing so requires that you enter *both* of your passphrases (which is a pretty clear indication that you have a *hidden volume* in there somewhere). 

When updating your decoy files in private, however, you should *always* enable this feature. And don't worry, *the box will uncheck itself automatically after you dismount the volume.* 

To use the *Protect hidden volume* feature, perform the following steps:

**Step 1**. **Select** a slot from the list in the main window of **VeraCrypt**.

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-501-select-slot.png)

*Figure 1: The main window of VeraCrypt with an available slot selected*

**Note**: In *Figure 1*, we have chosen to mount our encrypted volume in *slot 3*. You may choose any of the numbered slots whenever you mount a **VeraCrypt** volume.

**Step 2**. **Click** **[Select File…]** and locate a **VeraCrypt** *container* file with a *hidden volume*. In our example, we’ll select the *container* named ‘New Volume’ on the *Desktop*.

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-511-select-hv-container.png)

*Figure 2: The Select a VeraCrypt Volume screen*

**Step 3**. **Select** the *container* file you want to mount, then **click** **[Open]** to return to the **VeraCrypt** main window. The location of your *container* file will be displayed just to the left of the **[Select File...]** button you clicked earlier.

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-512-mount-hidden-volume.png)

*Figure 3: The main window of VeraCrypt with a container selected*

**Step 4**. **Click** **[Mount]** to open the *Enter Password* screen.

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-504-enter-passphrase.png)

*Figure 4: The Enter Password screen*

**Step 5.** **Type** your **outer volume** passphrase in the *Password* box, as if you were going to mount it normally, **but do not click [OK]**

**Step 6.** **Click** **[Mount Options...]**, which will allow you to protect your *hidden volume* while modifying the contents of your *standard volume*

![VeraCrypt's Enter Password screen](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-513-protect-hidden-volume.png)

*Figure 5: VeraCrypt's Mount Options screen*

**Step 7.** **Check** the box labelled *Protect hidden volume against damage caused by writing to outer volume*

**Step 8.** **Type** your *hidden volume* passphrase where indicated and **click** **[OK]**.

**Step 10.** **Click** **[OK]** to mount your *standard volume* while protecting your *hidden volume* from accidental damage. VeraCrypt will let you know when it's done.

![VeraCrypt's Enter Password screen](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-514-hv-protected.png)

*Figure 7: VeraCrypt's "Hidden volume is now protected" screen*

**Step 11.** **Click** **[OK]** to return to the main **VeraCrypt** window.

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-515-enter-protected-volume.png)

*Figure 8: VeraCrypt's "Hidden volume is now protected" screen*

**Step 12.** Enter the mounted volume in one of the two ways we described entering a *standard volume* in [Section 3](#2257) above: 

1. **Double click** the highlighted slot (*slot 3*) with the mounted volume in the main window of **VeraCrypt** as shown in *Figure 8*, above. This will open up a new empty *Finder* window.

2. In the regular *Finder* windows, you’ll also see a new drive mounted under *Devices*, entitled ‘NO NAME’ (as shown in *Figure 9*, below). From here, you can select the drive as you would with an inserted USB flash drive or other mounted media. 

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-508-enter-drive-finder.png)

*Figure 9: Accessing a mounted VeraCrypt volume through the Finder*

The volume in our example above is empty. But, once you have stored "decoy" files in your *standard volume*, they will be accessible whenever you mount it. And, if you have protected your *hidden volume* with the steps above, you will now be able to add or modify files safely. 

**Step 13**. **Modify** the contents of your standard (‘decoy’) volume as appropriate for you. 

**Tip**: Remember what the maximum amount of space is in your ‘outer’ *standard volume* vis-a-vis your ‘inner’, *hidden volume*. In our example, we have *less* than 50 MB (approximately 46 MB). Taking the earlier step of protecting our *hidden volume* helps prevent us from accidentally *overwriting* the content in that *hidden volume* if we attempt to put more than the available 46 MB available in our ‘outer’ *standard volume*.

**When you are done modifying the contents of your standard volume, you can dismount it by following the usual steps**, which are described under [Dismounting a volume](#2283), above. And, the next time you go to mount a volume, **remember** that the *Protect hidden volume against damage caused by writing to outer volume* box will be *unchecked* by default.

# 6. Managing your VeraCrypt containers





## 6.1 Importing content from a TrueCrypt volume into a VeraCrypt volume

**VeraCrypt** can mount **TrueCrypt** volumes. Given that **TrueCrypt** is no longer maintained, however, you should move your files to a **VeraCrypt** volume as soon as possible. The easiest way to do this is to: 

1. Create a new **VeraCrypt** volume as large as (or larger than) your existing **TrueCrypt** volume, 
2. Open both volumes at the same time, and 
3. Copy everything from the **TrueCrypt** volume to the **VeraCrypt** volume

This section assumes that you already have—or are able to create—one or more appropriately sized **VeraCrypt** volumes. If not, please refer to Section 3, [Creating a standard volume](#2257), and, if appropriate, Section 4, [Creating a hidden volume](#2260). 

The steps below address the process of moving files from a **TrueCrypt** *standard volume* to a **VeraCrypt** *standard volume* that has already been mounted. If you have files in *both* the *standard* and *hidden* volumes of a **TrueCrypt** container, simply make sure that your **VeraCrypt** volumes are large enough, then work through the following steps twice — once for each volume.

With the **VeraCrypt** main window open, and your new **VeraCrypt** volume mounted, carry out the following steps:

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-507-mount-standard-volume.png)

*Figure 1: VeraCrypt's main window showing a mounted volume*

**Step 1**. **Click** a numbered slot that is not already taken by a mounted **VeraCrypt** volume.

**Step 2**. **Click** **[Select File...]** to choose the **TrueCrypt** container you’d like to move files *from*. (In this example, the **TrueCrypt** container is named ‘My TC Volume’, and is stored on the *Desktop*.)

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-601-find-tc-container.png)

*Figure 2: Choosing a TrueCrypt container*

**Step 3**. **Navigate** to your **TrueCrypt** container.

**Step 4**. **Click** **[Open]** to return to the *main **VeraCrypt** window*.

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-602-mount-tc-container.png)

*Figure 3: VeraCrypt’s main window with a TrueCrypt container selected*

**Step 5**. **Click** **[Mount]** to move to the *password screen*.

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-603-tc-container-password.png)

*Figure 4: The VeraCrypt password screen in TrueCrypt Mode*

**Step 6**.  **Check** the **TrueCrypt Mode** box.

**Step 7**. **Type** the passphrase for your **TrueCrypt** volume.

**Step 8**. **Click** **[OK]** to return to the *main window*.

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-604-enter-tc-container.png)

*Figure 5: VeraCrypt's main window with both volumes mounted* 

**Step 9**. **Double click** the slot number for your mounted **TrueCrypt** volume to enter it.

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-509-enter-drive-veracrypt.png)

*Figure 6: Inside the mounted TrueCrypt volume*

**Step 10**. Return to the *main window*.

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-605-enter-vc-container.png)

*Figure 7: VeraCrypt's main window with both volumes mounted* 

**Step 11**. **Double click** the slot number for your mounted **VeraCrypt** container to enter it.

**Step 12**. **Select** the contents of your **TrueCrypt** volume and drag them to window representing your **VeraCrypt** volume. 

After your files have been copied over, you should then*dismount* both volumes. 

**Step 13**. Return to **VeraCrypt's** *main window*

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-604-enter-tc-container.png)

*Figure 8: VeraCrypt's main window*

**Step 14**. **Select** the slot number for your mounted **TrueCrypt** volume

**Step 15**. **Click** **[Dismount]** to dismount your **TrueCrypt** volume

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-606-dismount-vc.png)

*Figure 9: VeraCrypt's main window*

**Step 16**. **Select** the slot number for your mounted **VeraCrypt** volume

**Step 17**. **Click** **[Dismount]** to dismount your **VeraCrypt** volume

## 6.2 Backing up your container

Backing up your documents, files, and folders on a regular basis is critical. Backing up your **VeraCrypt** volume is vital, and (fortunately) easy to do. 

**IMPORTANT:** Don't forget that your **VeraCrypt** volumes must be dismounted before you back them up! Automatic backup tools may create *unencrypted* backups of the contents of your VeraCrypt containers if you run them while the volumes are mounted. And making unencrypted backups of encrypted data is usually a bad idea.

**Step 1**. **Navigate** to your encrypted *container file*. (In *figure 1*, below, the *container* is a file called *My Volume* on the *Desktop*). 

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-607-backup-container.png)

*Figure 1: The Desktop folder containing a VeraCrypt container called "My Volume"*

**Step 2**. **Copy** the file to an external memory device, like a CD, DVD, or USB storage device. 

**Tip**: You can also use **VeraCrypt** to make special encrypted backups of files that you do *not* normally keep inside a **VeraCrypt** volume on your computer. This may be a good option if you want to keep them confidential and inaccessable to unauthorized users on the external memory device you’re backing them up to. To do this, simply create a temporary *standard volume* **VeraCrypt** container of the appropriate size, mount it, copy the files you want to back up into the volume, dismount it, and save the *container* to a CD, DVD, or USB storage device. Each time you want to make a new backup, you can replace the contents with an updated set of files.

Before you back up your **VeraCrypt** container, make sure the back up medium has enough room to accommodate it:

| Backup medium | Suggested VeraCrypt container size |
|---------------|------------------------------------|
| CD            | 700 MB                             |
| DVD           | 3.9 GB                             |
| USB  storage  | (various)                          |

## 6.3 Changing one or both passphrases for a container

To change the passphrase of a **VeraCrypt** volume, start from the *main screen* and follow the steps below. These steps apply to both *standard volumes* and *hidden volumes* within **VeraCrypt** *containers*. However, if you want to change *both* passphrases, you will need to go through this process twice.

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-501-select-slot.png)

*Figure 1: VeraCrypt's main window*

**Step 1**. **Click** **[Select File...]** to choose the *container* for which you want to change the passphrase. (In this example, we’ll change the passphrase for our *standard volume* named ‘My Volume’, saved on our *Desktop*.)

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-608-find-container.png)

*Figure 2: Selecting a container file in VeraCrypt*

**Step 2**. **Select** your **VeraCrypt** *container*.

**Step 3**. **Click** **[Open]** to return to the *main window*.

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-609-container-selected.png)

*Figure 3: VeraCrypt's main window*

**Step 4**. In the main **VeraCrypt** menu, **click** on *Volumes*, then **scroll** down to **select [Change Volume Password]**.

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-610-volume-change-pwd.png)

*Figure 4: Changing the passphrase of a VeraCrypt volume*

This will activate the *Change Password* screen.

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-611-enter-passwords.png)

*Figure 5: VeraCrypt's Change Password screen*

**Tip:** If you have both a *standard volume* and a *hidden volume* in this *container*, **VeraCrypt** will automatically determine which one to change based on what you enter in the *Current Password* box. Again, if you want to change both, you will need to go through this process twice.

**Step 6**. **Type** your current passphrase. 

**Step 7**. **Type** your new passphrase twice. 

**Step 8**. **Click** **[OK]** to begin generating a new key. 

**IMPORTANT**: Because of the way **VeraCrypt** manages its encryption keys, it is *not* a good idea to copy your own *container* and give it to someone else, then have them change the passphrase on their copy. (Even if you *also* change the passphrase on *your* copy.) 

While they would not be able to open *your* volume with *their* passphrase, they could decrypt the unique underlying ‘master key’ that does *not* change when you change your passphrase. 

Because of this, if you ever suspect that someone might have *both* a copy of your *container* *and* know your passphrase, you should **not** simply change your passphrase in response. You should instead generate an entirely new *container* (with a new passphrase, of course), then copy over your files and delete the old container.

**Step 9**. When it is ready, **VeraCrypt** will display the *Random Pool Enrichment* screen. 

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-612-new-pw-random-pool.png)

*Figure 6: VeraCrypt's Random Pool Enrichment screen*

By moving your mouse around within the *Random Pool Enrichment* screen, you can increase the strength of the encryption that **VeraCrypt** provides.

**Step 9**. **Click** **[Continue]** to continue the process of changing your passphrase.

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-616-pwd-change-progress.png)

*Figure 7: VeraCrypt's password change progress bar*

**VeraCrypt** will let you know when it is done generating a new key for your encrypted volume.

![](/sites/securityinabox.org/files/media/veracrypt-osx-en-v01-617-pwd-changed.png)

*Figure 7: VeraCrypt passphrase successfully changed*

**Step 10**. **Click** **[OK]** to complete the process of changing your passphrase.

# FAQ

***Q***: Am I going to have to spend all my time typing passphrases into **VeraCrypt**?

***A***: No, you only need to enter your passphrase once to open an encrypted volume. After that, you can access your files without a passphrase until you close the volume

***Q***: Can I uninstall **VeraCrypt** if I don't want it any more? If I do, will my files remain encrypted?

***A***: Yes. You can later reinstall **VeraCrypt** to access the files in your containers, which will not be deleted when you remove **VeraCrypt**. Similarly, if you transfer your encrypted *container file* another computer, you will need your passphrase and the **VeraCrypt** program to access it.

***Q***: What kinds of information require encryption?

***A***: Ideally, you should encrypt all your documents, pictures and any other files that contain private and sensitive information. And, if your operating system supports it, you should configure *full disk encryption* so that *all* of your files are encrypted whenever your computer is turned off

***Q***: How secure will my files be?

***A***: **VeraCrypt** has been independently tested and reviewed by security experts to verify how well it performs and to determine whether or not it provides all of the functions it claims to support. The results suggest that **VeraCrypt** offers a very high level of protection. However, choosing a strong passphrase is essential to the security of your data.

***Q***: Why would I use a *hidden volume*?

***A***: **VeraCrypt's** *hidden volume* feature offers unique "plausible deniability" properties for information stored on your computer. To use it properly, however, you will not only need a good understanding of how **VeraCrypt** works, but also a strong grasp of your own security environment.

***Q***: How do I mount my original *standard volume*, rather than the one that's hidden?

***A***: It all depends on which passphrase you enter in the password screen. If you enter the *standard volume* passphrase, **VeraCrypt** will mount the *standard volume*. If you enter the *hidden volume* passphrase, **VeraCrypt** will mount the *hidden volume*. That way, if someone demands that you open your **VeraCrypt** container, you can mount the *standard volume* and deny the existence of a *hidden volume*. Under the right circumstances, this might be enough to get you off the hook and out of trouble.

***Q***: Is it possible to inadvertently damage or delete a *hidden volume*?

***A***: Yes. If you continue adding files to your *standard volume* until you run out of space for your hidden volume, your *hidden volume* will be damaged or destroyed. There is an option on the **VeraCrypt** password screen that you can use to protect your *hidden volume* from being damaged when modifying the contents of your *standard volume*. You should not use this option while being observed, as it reveals the existence of a *hidden volume*.

***Q***: Can I change the size of my *hidden volume* after creating it?

***A***: No. You will have to create another *hidden volume* and move files to it manually.

***Q***: Can I use tools like **chkdsk** on the contents of a mounted **VeraCrypt** volume?

***A***: **VeraCrypt** volumes behave like normal storage devices, so it is possible to use any file system checking/repairing/defragmenting tools on the contents of any mounted **VeraCrypt** volume.

***Q***: Is it possible to change the passphrase for a *hidden volume*?

***A***: Yes. The passphrase change feature applies to both *standard* and *hidden volumes*. Just type the passphrase for the *hidden volume* into the Current Password field of the Password Change screen.

- [**Official VeraCrypt FAQ**](https://veracrypt.codeplex.com/wikipage?title=FAQ)
