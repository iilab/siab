

---

lang: en
community: guide
type: tools
os: windows
weight: 025
title: TrueCrypt for Windows - secure file storage

---

**Truecrypt** keeps your files secure by preventing anyone without the correct password from opening them. It works like an electronic *safe*, which you can use to securely lock up your files.


# Required reading


{{ required_reading: ../../secure file storage }}


{{ tool: ./025-tool.md }}

# What you will get from this guide

- The ability to effectively protect your files from intruders or unauthorized access.
- The ability to easily and securely store copies of your important files.

# 1. Introduction to TrueCrypt





## 1.0 Other tools like TrueCrypt

Many **GNU Linux** distributions, for instance [**Ubuntu**](http://www.ubuntu.com/), support on-the-fly encryption-decryption for the entire disk as a standard feature. You can decide to use it when you install the system. In addition we also recommend to switch on encryption of home folder during installation. You can also add the encryption functionality to your **Linux** system by using an integration of [**dm-crypt**](http://www.saout.de/misc/dm-crypt/) and [**cryptsetup and LUKS**](https://gitlab.com/cryptsetup/cryptsetup). Another approach is to use [**ScramDisk for Linux SD4L**](http://sd4l.sourceforge.net/), a free and open source on-the-fly encryption-decryption program.

For the **Mac OS** you can use **FileVault**, which is part of the operating system, to provide *on-the-fly* encryption and decryption for the content of your entire disk and/or your home folder, and all the sub-folders.

As alternative program on **Microsoft Windows** we recommend using:

* [DiskCryptor](https://diskcryptor.net/wiki/Main_Page) is a free, open source encryption solution that offers encryption of all disk partitions, including the system partition.
* [**AxCrypt**](http://www.axantum.com/AxCrypt/) is a free and open source program that can encrypt separate files.

On MS Windows 7 Ultimate or Enterprise editions or MS Windows 8 Pro and Enterprise editions you will find [**BitLocker**](http://windows.microsoft.com/en-us/windows7/products/features/bitlocker) available to encrypt entire disk. Note that BitLocker is a Microsoft owned, closed, proprietary software which is not independently audited to establish what level of the protection and privacy it offers to your information.


## 1.1 Things you should know about TrueCrypt before you start

**On 28 May 2014, the TrueCrypt website began telling visitors that development of the tool had ceased. The developers offered a "new" version of TrueCrypt (*v7.2*) with extremely limited functionality. (It was released specifically to encourage users to migrate their content to some other encryption tool.) TrueCrypt will indeed become unsafe, if it is not maintained. For the time being, however, most security experts feel that it remains a strong encryption tool. We recommend that you continue using TrueCrypt version *7.1a*. or switch to one of the alternatives mentioned in [Other tools like TrueCrypt](#600).**

**TrueCrypt** will protect your data from being accessed by locking it with a password that you will create. If you forget that password, you will lose access to your data! **TrueCrypt** uses a process called encryption to protect your files. Please bear in mind that the use of encryption is illegal in some countries. Rather than encrypting specific files, **TrueCrypt** creates a protected area, called a *volume*, on your computer. You can safely store your files inside this encrypted volume. 

**TrueCrypt** offers the ability to create a standard encrypted volume or a hidden volume. Either one will keep your files confidential, but a
hidden volume allows you to hide your important information behind less sensitive data in order to protect it, even if you are forced to reveal
your **TrueCrypt** volume. This guide explains both volumes in detail. 


# 2. Install TrueCrypt and Create Standard Volumes

**TrueCrypt** is a program which secures your files by preventing anyone without the correct password from accessing them. It functions like an electronic safe, letting you lock up your files so that only someone with the correct password can open them. **TrueCrypt** works by letting you set up *volumes* or sections on your computer where you can securely store files. When you create data in, or move data to these volumes, **TrueCrypt** will automatically encrypt that information. As you open or take your files out, it automatically decrypts them for use. This process is called *on-the-fly* encryption. 


## 2.0 Install TrueCrypt

**Step 1**. **Double click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-01.png); the *Open File - Security Warning* dialog box may appear. If it does, **click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-05.png) to activate the  **TrueCrypt** *License* screen.

**Step 2**. **Check** the *I accept and agree to be bound by the license terms* option to enable the *Accept* button; **click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-03.png) to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/truecrypt-win-04.png)

*Figure 1: The Wizard Mode in the default Install mode*

- *Install* mode: This option is for users who do not wish to hide the very fact that they use **TrueCrypt** on their computer.

- *Extract* mode: This option is for users who wish to carry a portable version of **TrueCrypt** on a USB memory stick and do not wish to have **TrueCrypt** installed on their computer.

**Note**: Some of the options (for example, entire partition and disk encryption) will not work when **TrueCrypt** is extracted only.

**Note**: Although the default *Install* mode is recommended here, you may still use **TrueCrypt** in portable mode later on. To learn more about using the **TrueCrypt Traveller** mode, please refer to [**Portable TrueCrypt page**](#616). 

**Step 3**. **Click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-05.png) to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/truecrypt-win-06.png)

*Figure 2: The Setup Options window*

**Step 4**. **Click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-07.png) to activate the *Installing* screen to begin installing **TrueCrypt** on your system.

**Step 5**. **Click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-08.png) and then ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-11.png) to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/truecrypt-win-09.png)

*Figure 3: The TrueCrypt Setup confirmation dialog box*

**Step 6**. **Click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-10a.png) to complete the **TrueCrypt** installation.

**Note**: All users are strongly encouraged to consult [**TrueCrypt** help documentation](http://andryou.com/truecrypt/docs/index.php) after completing this tutorial. 

## 2.1 Create a Standard Volume

**TrueCrypt** lets you create two kinds of volumes: *Hidden* and *Standard*. In this section, you will learn how to create a *Standard Volume* in which to store your files. 

To begin using **TrueCrypt** to create a *Standard Volume*, perform the following steps: 

**Step 1**. **Double click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-52.png) or **Select Start > Programs > TrueCrypt > TrueCrypt** to open **TrueCrypt**.

**Step 2**. **Select** a drive from the list in the **TrueCrypt** pane as follows:

![](/sites/siabnext.ttc.io/files/media/truecrypt-win-12.png)

*Figure 4: The TrueCrypt console*

**Step 3**. **Click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-13.png) to activate the *TrueCrypt Volume Creation Wizard* as follows:

![](/sites/siabnext.ttc.io/files/media/truecrypt-win-14.png)

*Figure 5: The TrueCrypt Volume Creation Wizard window* 

There are three options for encrypting a *Standard Volume* in *figure 5*. In this chapter, we will use the *Create an encrypted file container* option. Please refer to the [**TrueCrypt**](http://www.truecrypt.org/docs/) documentation for the description of other two options.

**Step 4**. **Click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-05.png) to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/truecrypt-win-15.png)

*Figure 6: The Volume Type window*

The *TrueCrypt Volume Creation Wizard Volume Type* window lets you specify whether you would prefer to create a *Standard* or *Hidden* **TrueCrypt** volume. 

**Important**: For more information about *How to Create a Hidden Volume*, please refer to the [**Hidden Volumes**](#612) page. 

**Step 5**. **Check** the *Standard TrueCrypt Volume* option. 

**Step 6**. **Click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-05.png) to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/truecrypt-win-16.png)

*Figure 7: The Volume Creation Wizard - Volume Location pane*

You can specify where you would like to store your *Standard Volume* in the *Volume Creation Wizard - Volume Location* screen. This file can be stored like any other file. 

**Step 7**. Either **type** in the name of the file into the text field, or **click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-17.png) to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/truecrypt-win-18.png)

*Figure 8: The Specify Path and File Name navigation window*

**Note**: A **TrueCrypt** Volume is contained inside a normal file. This means that it can be moved, copied or even deleted! You need to remember both the location and name of the file. However, you must choose new file name for the volume you create (also refer to the [**Create a Standard Volume on a USB Memory Stick**](#606) section). In this tutorial, we will create our Standard Volume in the **My Documents** folder, and name the file *My Volume* as shown in *figure 8* above. 

**Tip**: You can use any file name and file extension. For example, you can name your Standard Volume *recipes.doc,* so that it will look like a *Word* document, or *holidays.mpg*, so it will look like a movie file. This is one way you can help disguise the existence of your Standard Volume. 

**Step 8**. **Click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-19.png) to close the *Specify Path and File Name* window and return to the *Volume Creation Wizard* window as follows:

![](/sites/siabnext.ttc.io/files/media/truecrypt-win-20.png)

*Figure 9: The TrueCrypt Volume Creation Wizard displaying the Volume Location pane*

**Step 9**. **Click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-05.png) to activate *figure 10*. 

<a name="2.2"></a>

## 2.2 Create a Standard Volume on a USB Memory Stick

To create a **TrueCrypt** *Standard Volume* on a USB memory stick, perform steps 1 to 7 in section [**2.1 Create a Standard Volume**](#605), where you activate the *Select a TrueCrypt Volume* screen. Instead of choosing *My Documents* as your file location, **navigate** to and then **choose** your USB memory stick. Then, **enter** a file name and create the *Standard Volume* there. 


## 2.3 Create a Standard Volume (continued)

At this stage, you are ready to choose a specific encryption method (or *algorithm* as it is referred to on the screen) to encode the data that will be stored in your *Standard Volume*. 

![](/sites/siabnext.ttc.io/files/media/truecrypt-win-21.png)

*Figure 10: The Volume Creation Wizard Encryption Options pane*

**Note**: You may leave the default options here as they appear. All algorithms presented in the two options here are considered secure. 

**Step 10**. **Click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-05.png)
 to activate the *TrueCrypt Volume Creation Wizard* screen as follows:

![](/sites/siabnext.ttc.io/files/media/truecrypt-win-22.png)

*Figure 11: The Volume Creation Wizard displaying the Volume Size pane*

The *Volume Size* pane lets you specify the size of the *Standard Volume*. In this example, it is set at 10 megabytes. However, you may specify a different size. Consider the size of the documents and file types you would like to store, and then set an appropriate volume size for them. 

**Tip**: If you would like to backup your Standard Volume to a CD later on, then you should set the size to 700MB or less.

**Step 11**. **Type** in your specific volume size into the text field, and then **click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-05.png) to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/truecrypt-win-23.png)

*Figure 12: The TrueCrypt Volume Creation Wizard featuring the Volume Password pane*

**Important**: Choosing a secure and strong password is among the most important tasks you will perform when creating a *Standard Volume*. A good password will protect your encrypted volume, and the stronger the password you choose, the better. You don't have to create your own passwords, or even remember them, if you use a password generation program like **KeePass**. Please refer to [**KeePass**](../keepass/windows), to learn more information about password creation and storage.

**Step 12**. **Type** your password and then **re-type** your password into the *Confirm* text fields.

**Important**: The *Next* button will remain disabled until passwords in both text fields match. If your password is not particularly safe or secure, you will see a warning advising you of this. Consider changing it! Although **TrueCrypt** will still work with any password you have chosen, your data may not be very secure. 

**Step 13**. **Click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-05.png) to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/truecrypt-win-24.png)

*Figure 13: The TrueCrypt Volume Creation Wizard featuring the Volume Format pane*

**TrueCrypt** is now ready to create a *Standard Volume*. Move your mouse randomly within the *TrueCrypt Volume Creation Wizard* window for few seconds. The longer you move the mouse, the better the quality of the encryption key.

**Step 14**. **Click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-25.png) to begin creating your standard volume.

**TrueCrypt** will now create a file named *My Volume* in the *My Documents* folder as earlier specified. This file will contain a **TrueCrypt** *Standard Volume*, 10 Megabytes in size, that you can use to securely store your files. 

After a *Standard Volume* has been successfully created, the following dialog box will appear: 

![](/sites/siabnext.ttc.io/files/media/truecrypt-win-26.png)

*Figure 14: The TrueCrypt volume has been successfully created message screen*

**Step 15**. **Click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-27.png) to complete creating your *Standard Volume* and return to the **TrueCrypt** console.

**Step 16**. **Click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-28.png) to close *TrueCrypt Volume Creation Wizard*.

# 3. Mount and Dismount a Standard Volume





## 3.1 Mount a Standard Volume

In **TrueCrypt**, to *mount* a *Standard Volume* refers to making the standard volume available for use. In this section, you will learn how to mount your newly created standard volume.  

To begin mounting your standard volume, perform the following steps: 

**Step 1**. **Double click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-52.png) or **Select Start > Programs > TrueCrypt > TrueCrypt** to open **TrueCrypt**.

**Step 2**. **Select** any drive from the list as follows: 

![](/sites/siabnext.ttc.io/files/media/truecrypt-win-12.png)

*Figure 1: The TrueCrypt console*

*In this example the Standard Volume will be mounted as the M: drive.*

**Note**: In *figure 1*, the *M:* drive has been selected for mounting the *standard volume*; however, you may choose another listed drive.

**Step 3**. **Click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-17.png)

*The Select a TrueCrypt Volume screen will appear as follows:*

![](/sites/siabnext.ttc.io/files/media/truecrypt-win-29.png)

*Figure 2: The Select a TrueCrypt Volume screen*

**Step 4**. **Select** the standard volume file that you created, then **click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-30.png) to close *figure 2* and return to the **TrueCrypt** console.

**Step 5**. **Click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-31.png) to activate the *Enter password for* prompt screen as follows:

![](/sites/siabnext.ttc.io/files/media/truecrypt-win-32.png)

*Figure 3: The Enter password prompt screen*

**Step 6**. **Type** the password in the *Password*: text field. 

**Step 7**. **Click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-33.png) to begin mounting the *Standard Volume*.

**Note**: If the password you typed is incorrect, **TrueCrypt** will prompt you to re-type your password and **click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-33.png). If the password is correct, the *Standard Volume* will be mounted as follows:

![](/sites/siabnext.ttc.io/files/media/truecrypt-win-34.png)

*Figure 4: The TrueCrypt console displaying the newly mounted Standard Volume*

**Step 8**. **Double click** the highlighted entry in **TrueCrypt** or **double click** the corresponding drive letter in the *My Computer* screen to access the *Standard Volume* (now mounted on drive *M:* on your computer). 

![](/sites/siabnext.ttc.io/files/media/truecrypt-win-35.png)

*Figure 5: Accessing the Standard Volume through the My Computer screen*

**Note**: We have just successfully mounted the *My Volume* standard volume on a virtual disk *M:*. This virtual disk behaves like a real disk, except that it is entirely encrypted. Any files will be automatically encrypted when you copy, move or save them to this virtual disk (a process known as on-the-fly encryption). 

You can copy files to and from the *Standard Volume* just as you would copy them to any normal disk (for example, by dragging-and-dropping them). When you move a file out of the *Standard Volume*, it is automatically decrypted. Conversely if you move a file onto the *Standard Volume*, **TrueCrypt** automatically encrypts it. If your computer crashes or is suddenly switched off, **TrueCrypt** will immediately close the *Standard Volume*. 

**Important**: After transferring files to the **TrueCrypt** volume, make sure that no traces of the files are left behind on the computer or USB memory stick that they came from. Please refer to the chapter on [**How to destroy sensitive information**](../destroy-sensitive-information).

## 3.2 Dismount a Standard Volume

In **TrueCrypt**, to *dismount* a *Standard Volume* simply means to make a volume unavailable for use. 

To close or dismount a *Standard Volume* and make its files accessible only to someone with a password, perform the following steps: 

**Step 1**. **Select** the volume from the list of mounted volumes in the main **TrueCrypt** window as follows:

![](/sites/siabnext.ttc.io/files/media/truecrypt-win-34.png)

*Figure 17: Selecting the Standard Volume to be dismounted*

**Step 2**. **Click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-49.png) to dismount or close your **TrueCrypt** standard volume. 

**Important**: Make sure to dismount your **TrueCrypt** volume before putting your computer to *Standby* or *Hibernate* mode. Better yet, always shut-down your computer or laptop if you plan on leaving it unattended. This will prevent anyone from being able to gain your volume password.

To retrieve a file stored in your standard volume once you have closed or dismounted it, you will have to mount it again.


# 4. Backup your volume

Backing up your documents, files and folders on a regular basis is
critical. Backing up your **TrueCrypt** volume is vital, and (fortunately)
easy to do. Don't forget that your volume must be dismounted before you back it up.

**Step 1**. **Navigate** to your *Standard Volume* file (in *figure 1* below, it is located in the *My Documents* folder). 

![](/sites/siabnext.ttc.io/files/media/truecrypt-win-36.png)

*Figure 1: The My Documents window displaying the My Volume file*

**Step 2**. **Save** the file to an external memory device, like a CD, DVD or a USB memory stick. 

**Tip**: If you have large amounts of data that you want to encrypt and archive repeatedly, why not create a new *Standard Volume* which is the same size as a CD or DVD? This could be used as a secure storage technique. 

Before you back up the standard volume to a removable device, make sure that the device size corresponds to the size of your volume. 

| Backup Medium     | Suggested TrueCrypt Volume Size |
| --------------------------- | ------------------------------------------------- | 
| CD                        | 700mb                                        |
| DVD                      | 3900mb                                      |
| USB memory stick | Suggested 25% of total capacity (e.g. For 128MB USB stick, use 30MB for your Standard Volume) |


# 5. Hidden Volumes

In **TrueCrypt**, a *Hidden Volume* is stored within your encrypted *Standard Volume*, but its existence is concealed. Even when you 'mount' or open your standard volume, it is not possible either to find or to prove the existence of the hidden volume. If you are forced to reveal your password and the location of your standard volume, then its content may be revealed, but **not** the existence of the hidden volume within. 

Imagine a briefcase with a secret compartment. You keep files that you do not mind having confiscated or losing in the normal section of your
briefcase, and you keep the important and private files in the secret
compartment. The point of the secret compartment (especially a
well-designed one), is to hide its own existence and therefore, the
documents within it. 

<a name="5.1"></a>

## 5.1 Create a Hidden Volume

The creation of a **TrueCrypt** *Hidden Volume* is similar to creating a **TrueCrypt** *Standard Volume*: Some of the panes, screens and windows are even the same. 

**Step 1**. **Open** **TrueCrypt**.

**Step 2**. **Click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-13.png) to activate the *TrueCrypt Volume Creation Wizard*. 

**Step 3**. **Click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-05.png) to accept the default *Create an encrypted file container* option.

**Step 4**. **Check** the *Hidden TrueCrypt volume* option as follows: 

![](/sites/siabnext.ttc.io/files/media/truecrypt-win-37.png)

*Figure 1: The TrueCrypt Volume Creation Wizard with the Hidden TrueCrypt volume option enabled*

**Step 5**. **Click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-05.png) to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/truecrypt-win-38.png)

*Figure 2: The TrueCrypt Volume Creation Wizard - Mode window*

- *Direct mode*: This option lets you create the *Hidden Volume* within an existing *Standard Volume*.

- *Normal mode*: This option lets you create a completely new *Standard Volume* in which to store the *Hidden Volume*. 

In this example, we will use the *Direct mode*. 

**Note**: If you would rather start a new *Standard Volume*, please repeat the process from [**Create a Standard Volume**](#605) section.

**Step 6**. **Check** the *Direct Mode* option and then **click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-05.png) to activate the *TrueCrypt Volume Creation - Volume Location* window.

**Note**: Make sure the *Standard Volume* is unmounted before selecting it. 

**Step 7**. **Click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-17.png) to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/truecrypt-win-29.png)

*Figure 3: The TrueCrypt Volume Creation Wizard - Select a TrueCrypt Volume window*

**Step 8**. **Locate** the volume file using the *Select a TrueCrypt Volume* window as shown in *figure 3*. 

**Step 9**. **Click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-30.png) to return to the *TrueCrypt Volume Creation Wizard*.

**Step 10**. **Click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-05.png) to activate the *Enter password* screen.

**Step 11**. **Type** in password you used when creating the *Standard Volume* into the *Password* text field to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/truecrypt-win-46.png)

*Figure 4: The TrueCrypt Volume Creation Wizard - Hidden Volume Message pane*

**Step 12**. **Click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-05.png) after you have read the message to activate the *Hidden Volume Encryptions Options* screen.

**Note**: Leave both the default *Encryption Algorithm* and *Hash Algorithm* settings for the *Hidden Volume* as they are. 

**Step 13**. **Click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-05.png) to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/truecrypt-win-41.png)

*Figure 5: The TrueCrypt Volume Creation Wizard - Hidden Volume Size window*

You will be prompted to specify the size of the *Hidden Volume*. 

**Note**: Consider the kind of documents, their quantity and size that need to be stored. Do leave some space for the *Standard Volume*. If you select the maximum size available for the *Hidden Volume*, you will not be able to put any more new files into the original *Standard Volume*. 

If your *Standard Volume* is 10 Megabytes(MB) in size and you specify a *Hidden Volume* size of 5MB (as shown in *figure 6* above), you will have two volumes (one hidden and one standard volume) of approximately 5MB each. 

Ensure that the information you store in the *Standard Volume* does not exceed the 5MB you have set. This is because the **TrueCrypt** program itself does not automatically detect the existence of the *Hidden Volume*, and it could accidentally overwrite it. You may risk losing all files stored in the hidden volume if you exceed your previously established size. 

**Step 14**. **Type** in the desired hidden volume size into the corresponding text box as shown in *figure 6*. 

**Step 15**. **Click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-05.png) to activate the *Hidden Volume Password* window.

You must now create a *different* password for the hidden volume from the one used to protect your standard volume. Again, remember to choose a strong password. Please refer to the [**KeePass**](../keepass/windows) chapter to learn more about creating strong passwords. 

**Tip**: If you anticipate being forced to reveal the contents of your **TrueCrypt** volumes, then store your password for the standard volume in **KeePass**, and create a strong password that you only have to remember for hidden volume. This will help you to conceal your hidden volume, as you will not leave any trace of its existence.

**Step 16**. **Create** a password and **type** it in twice, and then **click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-05.png) to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/truecrypt-win-42.png)

*Figure 6: The TrueCrypt Volume Creation Wizard - Hidden Volume Format pane*

Leave the default *File System* and *Cluster* options as they are. 

**Step 17**. **Move** the mouse cursor around the screen to increase the cryptographic strength of the encryption and then **click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-25.png) to format the hidden volume.

*After the hidden volume has been formatted, the following screen appears:* 

![](/sites/siabnext.ttc.io/files/media/truecrypt-win-43.png)

*Figure 7: The TrueCrypt Volume Creation Wizard message screen*

**Note**: *Figure 8* both confirms that you have successfully created a hidden volume, as well as warning you against the dangers of overwriting files in the hidden volume when storing files in the standard volume. 

**Step 18**. **Click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-27.png) to activate the *Hidden Volume Created* window, and then **click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-28.png) and return to the **TrueCrypt** console. 

The hidden volume has now been created inside your standard volume. You may now store documents in the hidden volume, which remain invisible even to someone who has obtained the password for that particular standard volume. 

<a name="5.2"></a>

## 5.2 Mount the Hidden Volume

The method for mounting or making a *Hidden Volume* accessible for use is exactly the same as that for a *Standard Volume*; the only difference is you will use the password that you have just created for the *Hidden Volume*.

To *mount* or open the *Hidden Volume*, perform the following steps: 

**Step 1**. **Select** a drive from the list (in this example, drive *K*):

![](/sites/siabnext.ttc.io/files/media/truecrypt-win-44.png)

*Figure 8: A mount drive selected in the TrueCrypt Volume screen*

**Step 2**. **Click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-17.png) to activate the *Select a TrueCrypt Volume* window. 

**Step 3**. **Navigate** to and then **select** your *TrueCrypt* volume file (same file as for the standard volume). 

**Step 4**. **Click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-30.png) to return to the **TrueCrypt** console.

**Step 5**. **Click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-31.png) to activate the *Enter Password for* prompt screen as follows:

![](/sites/siabnext.ttc.io/files/media/truecrypt-win-32.png)

*Figure 9: The Enter Password screen*

**Step 6**. **Type** the password you used to create the hidden volume, and then **click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-33.png). 

Your hidden volume is now mounted (or opened) as follows:

![](/sites/siabnext.ttc.io/files/media/truecrypt-win-45.png)

*Figure 10: The TrueCrypt main screen displaying the newly mounted Hidden Volume*

**Step 7**. **Double click** on above entry or access it through the *My Computer* window. 

<a name="5.3"></a>

## 5.3 Tips on Using a Hidden Volume Securely

The purpose of the hidden disk feature is to escape a potentially dangerous situation by *appearing* to hand over your encrypted files, when someone in a position of power demands to see them, without actually being forced to reveal your most sensitive information. In addition to protecting your data, this may allow you to avoid further jeopardizing your own safety or exposing your colleagues and partners. For this technique to be effective, you must create a situation where the person demanding to see your files will be satisfied by what you show them and let you go.

To do this, you may want to implement some of the following suggestions: 

- Put some confidential documents that you do not mind having exposed in the standard volume. This information must be sensitive enough that it would make sense for you to keep it in an encrypted volume. 

- Be aware that someone demanding to see your files may know about
hidden volumes. If you are using **TrueCrypt** correctly, however, this person will not be able to prove that your hidden volume exists, which will make your denial more believable.

- Update the files in the standard volume on a weekly basis. This will
create the impression that you really are using those files.

Whenever you mount a **TrueCrypt** volume, you can choose enable the *Protect hidden volume against damage caused by writing to outer volume* feature. A *very* important feature, it lets you add new 'decoy' files to your standard volume without the risk of you accidentally deleting or overwriting the encrypted contents of your hidden volume. 

As mentioned earlier, exceeding the storage limit on your standard volume may otherwise destroy your hidden files. Do not enable the *Protect hidden volume* feature when forced to mount a **TrueCrypt** volume, because doing so requires you to enter the secret password to your hidden volume and will clearly reveal that volume's existence. When you are updating your decoy files in private, however, you should *always* enable this option.

To use the *Protect hidden volume* feature, perform the following steps:

**Step 1**. **Click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-47.png) on the *Enter Password* prompt shown in *figure 10*, above. This will activate the *Mount Options* window as follows:

![](/sites/siabnext.ttc.io/files/media/truecrypt-win-48.png)

*Figure 11: The Mount Options window*

**Step 2**. **Check** the *Protect hidden volume against damage caused by writing to outer volume* option.

**Step 3**. **Type** in in your Hidden Volume password, and then **click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-33.png).

**Step 4**. **Click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-31.png) to mount your standard volume. After you have successfully mounted it, you will be able to add decoy files without damaging your hidden volume.

**Step 5**. **Click** ![](/sites/siabnext.ttc.io/files/media/truecrypt-win-51.png) to dismount, or your make your standard volume unavailable for use, when you have finished modifying its contents. 

**Remember**: You only need to do this when you are updating the files in your standard volume. If forced to reveal your standard volume to someone else, you should not use the *Protect hidden volume* feature.

# 6. Portable TrueCrypt





## 6.1 Differences between the Installed and Portable versions of TrueCrypt

Given that portable tools are not installed on a local computer, their existence and use may remain undetected. However, keep in mind that your external device or USB memory stick, and portable tools are only as safe as the computer you are using, and may risk being exposed to adware, malware, spyware and viruses.

As with many of the portable software tools documented here, **Portable TrueCrypt** allows you to use a powerful and simple file encryption tool without being detected. Having **Portable TrueCrypt** on removable device or USB memory stick lets you use it from different workstations.

There are very few differences between both the installed and portable versions of **Portable TrueCrypt**, the main one being that **Portable TrueCrypt** does not permit the encryption of the entire disk or system disk. 

See [more information regarding the differences between **TrueCrypt** and **Portable TrueCrypt**](http://andryou.com/truecrypt/docs/truecrypt-portable.php).


## 6.2 Downloading, Extracting and Using Portable TrueCrypt

**Note**: The folder into which **Portable TrueCrypt** is to be extracted must be created manually on the removable device, USB memory stick or computer disk before the extraction process.

**Step 1**. **Navigate** to chosen destination where you would like to extract the **Portable TrueCrypt** program to, and then **right-click** to activate its associated menu.

**Step 2**. **Select** the *New* item to activate its sub-folder, and then **select** the *Folder* sub-menu item, as shown in *Figure 1* below:

![](/sites/siabnext.ttc.io/files/media/truecryptportable-win-01.png)

*Figure 1: The Windows explorer folder and sub-folder*

**Step 3**. **Enter** the name of the folder.

**Note**: You may give this folder a less obvious name to conceal the existence of the **Portable TrueCrypt** program.

**Portable TrueCrypt** can be extracted from the same archive as installation version:

**Step 1**.  **Navigate** to **TrueCrypt** installation file on your computer.

**Step 2**. **Double click** ![](/sites/siabnext.ttc.io/files/media/truecryptportable-win-06.png); the *Open File - Security Warning* dialog box may appear; if it does, **click** ![](/sites/siabnext.ttc.io/files/media/truecryptportable-win-08c.png) to activate the **TrueCrypt** installation wizard. 

**Step 5**. **Check** the **Extract** option to extract **TrueCrypt** portable to a removable drive or USB device as shown in *Figure 3* below:

![](/sites/siabnext.ttc.io/files/media/truecryptportable-win-08.png)

*Figure 3: The Wizard Mode - Select one of the modes window*

**Step 6**. **Click** ![](/sites/siabnext.ttc.io/files/media/truecryptportable-win-09.png) to activate following two screens:

![](/sites/siabnext.ttc.io/files/media/truecryptportable-win-08a.png)
![](/sites/siabnext.ttc.io/files/media/truecryptportable-win-08b.png)

**Click** ![](/sites/siabnext.ttc.io/files/media/truecryptportable-win-17.png) and ![](/sites/siabnext.ttc.io/files/media/truecryptportable-win-08c.png) respectively to activate the **Extraction Options** window as follows: 

![](/sites/siabnext.ttc.io/files/media/truecryptportable-win-10.png)

*Figure 4: The Extraction Options window*

**Step 7**. **Click** ![](/sites/siabnext.ttc.io/files/media/truecryptportable-win-11.png) to activate the *Browse for Folders* window as follows:

![](/sites/siabnext.ttc.io/files/media/truecryptportable-win-12.png)

*Figure 5: The Browse for Folder window*

**Step 8**. **Navigate** to your destination folder on either the external drive or USB memory stick, and then **click** ![](/sites/siabnext.ttc.io/files/media/truecryptportable-win-17.png), to return the *Extraction Options* window as follows: 

![](/sites/siabnext.ttc.io/files/media/truecryptportable-win-14.png)

*Figure 6: The Extraction Options window displaying the destination folder*

**Step 9**. **Click** ![](/sites/siabnext.ttc.io/files/media/truecryptportable-win-13.png) to begin extracting **TrueCrypt** to your removable drive or USB memory stick; a few seconds later, the following windows will appear:

![](/sites/siabnext.ttc.io/files/media/truecryptportable-win-16.png)

*Figure 7: The TrueCrypt pop-up confirmation dialog box and Extraction Complete window*

**Step 10**. **Click** ![](/sites/siabnext.ttc.io/files/media/truecryptportable-win-17.png) and then **click** ![](/sites/siabnext.ttc.io/files/media/truecryptportable-win-18.png) to complete the installation process.

*If the ![](/sites/siabnext.ttc.io/files/media/truecryptportable-win-19.png) option was enabled (as it usually is by default), the following screen will appear:*

![](/sites/siabnext.ttc.io/files/media/truecryptportable-win-20.png)

*Figure 8: An example of Portable TrueCrypt extracted to a removable drive*

**Step 11**. **Navigate** to and then **double click** ![](/sites/siabnext.ttc.io/files/media/truecryptportable-win-21.png) to run **Portable TrueCrypt**.

Please refer to the [**Truecrypt**](../truecrypt/windows) chapter in the **Hands-on Guide** section from this point onwards, for instructions on how to use **TrueCrypt**. 


## 6.3 How to Remove Traces of Portable TrueCrypt

**Important**: After you have successfully extracted **Portable TrueCrypt** to your external/removable device, you must **delete** the installation file from your computer to further eliminate any traces of you having downloaded and installed **Portable TrueCrypt**.

**Step 1**. **Navigate** to the folder in which **Portable TrueCrypt** was downloaded, and then **right click** the ![](/sites/siabnext.ttc.io/files/media/truecryptportable-win-06.png) installation file to activate the **Windows** pop-up menu; then, **select** the **Delete** command to move it to your **Recycle Bin**.

**Step 2**. **Double click** ![](/sites/siabnext.ttc.io/files/media/truecryptportable-win-23.png) to open its associated window, and then **select** and **delete** the file. 

**Note**: If you have [**CCleaner**](../ccleaner/windows) installed, you can use it to eliminate all traces of your having ever downloaded and installed **Portable TrueCrypt**.


# FAQ

***Q***: Am I going to have to spend all my time typing passwords into **TrueCrypt**?

***A***: No, you only need to type the password in once, when you're opening the Standard Volume. When you've done that, you can open any file in it without putting in the password each time.

***Q***: Can I easily uninstall **TrueCrypt** if I don't want it any more? If I do, will my files remain encrypted?

***A***: Yes, **TrueCrypt** can be easily removed by **selecting Start > All Programs > Truecrypt > Uninstall Truecrypt**. You can later install TrueCrypt again to access files in any volume you created. If you transfer the volume to another computer, you will still need your password and the **TrueCrypt** program to access it.

***Q***: Will different versions of **Windows** bring up different screens when we try to load and use **TrueCrypt**?

***A***: Their appearance may be slightly different, but the content will remain the same.

***Q***: What kinds of information require encryption?

***A***: Ideally, you should encrypt all your documents, pictures and any other files that contain private and sensitive information. Should you lose your computer, or if it is confiscated, the information within your **TrueCrypt** volume will remain secure.

***Q***: How secure will our files be?

***A***: **TrueCrypt** has been independently tested and reviewed by security experts to see how well it performs and whether it performs all the functions it claims to. Overall results show that **TrueCrypt** offers a very high level of protection. Choosing a strong password is essential to the security of your volume. The hidden disk feature in **TrueCrypt** offers a unique level of security for information stored on the computer. The user needs to have an excellent grasp of the program and its basic functions, as well as an expert assessment of their own security situation, and of when the hidden disk feature might be useful. 

***Q***: Remind me again, how do I mount my original standard volume, rather than the one that's hidden?

***A***: It all depends on what password you enter in the Password box. If you enter the Standard Volume password, then **TrueCrypt** will mount that Standard Volume. If you enter the Hidden Volume password, then **TrueCrypt** will mount that Hidden Volume. If someone demands that you open your **TrueCrypt** volume so that they can see what type of information is there, you open the standard volume. Hopefully this will be enough to get you off the hook and out of trouble.

***Q***: Is it possible to inadvertently damage or delete the hidden volume?

***A***: Yes. If you continue to add files to the **TrueCrypt** Standard Volume until the there isn't sufficient empty space (for the hidden disk to exist), then your hidden disk will be automatically overwritten. There is an option in the **TrueCrypt** menu that can protect your hidden disk from being overwritten, but switching this option on may identify the existence of the hidden disk to an adversary when the volume is open.

***Q***: Can I change the size of the hidden disk after creating it?

***A***: No. You will have to create another hidden disk and move files to it manually.

***Q***: Can I use tools like **chkdsk**, **Disk Defragmenter**, and others on the contents of a mounted **TrueCrypt** volume?

***A***: **TrueCrypt** volumes behave like real physical disk devices, so it is possible to use any file system checking/repairing/defragmenting tools on the contents of any mounted **TrueCrypt** volume.

***Q***: Is it possible to change the password for a Hidden Volume? 

***A***: Yes. The Password change feature applies to both Standard and Hidden Volumes. Just type the password for the hidden volume in the 'Current Password' field of the 'Volume Password Change' prompt screen.

***Q***: When should I use the hidden disk feature?

***A***: Use the **TrueCrypt** hidden disk feature when you need to hide the existence of certain information on your computer. Note that this is different from using a Standard Volume, where you are protecting access to the information.

See [detailed FAQ about **TrueCrypt**](http://andryou.com/truecrypt/faq.php).
