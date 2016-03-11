

---

lang: xx
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: How to Install TrueCrypt and Create Standard Volumes

---

List of sections on this page: 

- [**2.0 How to Install TrueCrypt**](#2.0)
- [**2.1 About TrueCrypt**](#2.1)
- [**2.2 How to Create a Standard Volume**](#2.2)
- [**2.3 How to Create a Standard Volume on a USB Memory Stick**](#2.3)
- [**2.4 How to Create a Standard Volume (Continued)**](#2.4)

<a name="2.0"></a>
## 2.0 How to Install TrueCryrpt ##

**Step 1**. **Double click** ![](/sbox/screen/truecrypt-en/01.png); the *Open File - Security Warning* dialog box may appear. If it does, **click** ![](/sbox/screen/truecrypt-en/05.png) to activate the  **TrueCrypt** *License* screen.

**Step 2**. **Check** the *I accept and agree to be bound by the license terms* option to enable the *Accept* button; **click** ![](/sbox/screen/truecrypt-en/03.png) to activate the following screen:

![](/sbox/screen/truecrypt-en/04.png)

*Figure 1: The Wizard Mode in the default Install mode*

- *Install* mode: This option is for users who do not wish to hide the very fact that they use **TrueCrypt** on their computer.

- *Extract* mode: This option is for users who wish to carry a portable version of **TrueCrypt** on a USB memory stick and do not wish to have **TrueCrypt** installed on their computer.

**Note**: Some of the options (for example, entire partition and disk encryption) will not work when **TrueCrypt** is extracted only.

**Note**: Although the default *Install* mode is recommended here, you may still use **TrueCrypt** in portable mode later on. To learn more about using the **TrueCrypt Traveller** mode, please refer to [**Portable TrueCrypt page**](http://securityinabox.org/en/truecrypt_portable). 

**Step 3**. **Click** ![](/sbox/screen/truecrypt-en/05.png) to activate the following screen:

![](/sbox/screen/truecrypt-en/06.png)

*Figure 2: The Setup Options window*

**Step 4**. **Click** ![](/sbox/screen/truecrypt-en/07.png) to activate the *Installing* screen to begin installing **TrueCrypt** on your system.

**Step 5**. **Click** ![](/sbox/screen/truecrypt-en/08.png) and then ![](/sbox/screen/truecrypt-en/11.png) to activate the following screen:

![](/sbox/screen/truecrypt-en/09.png)

*Figure 3: The TrueCrypt Setup confirmation dialog box*

**Step 6**. **Click** ![](/sbox/screen/truecrypt-en/10a.png) to complete the **TrueCrypt** installation.

**Note**: All users are strongly encouraged to consult [**TrueCrypt** help documentation](http://andryou.com/truecrypt/docs/index.php) after completing this tutorial. 

<a name="2.1"></a>
## 2.1 About TrueCrypt ##

**TrueCrypt** is a program which secures your files by preventing anyone without the correct password from accessing them. It functions like an electronic safe, letting you lock up your files so that only someone with the correct password can open them. **TrueCrypt** works by letting you set up *volumes* or sections on your computer where you can securely store files. When you create data in, or move data to these volumes, **TrueCrypt** will automatically encrypt that information. As you open or take your files out, it automatically decrypts them for use. This process is called *on-the-fly* encryption. 

<a name="2.2"></a>
## 2.2 How to Create a Standard Volume ##

**TrueCrypt** lets you create two kinds of volumes: *Hidden* and *Standard*. In this section, you will learn how to create a *Standard Volume* in which to store your files. 

To begin using **TrueCrypt** to create a *Standard Volume*, perform the following steps: 

**Step 1**. **Double click** ![](/sbox/screen/truecrypt-en/52.png) or **Select Start > Programs > TrueCrypt > TrueCrypt** to open **TrueCrypt**.

**Step 2**. **Select** a drive from the list in the **TrueCrypt** pane as follows:

![](/sbox/screen/truecrypt-en/12.png)

*Figure 4: The TrueCrypt console*

**Step 3**. **Click** ![](/sbox/screen/truecrypt-en/13.png) to activate the *TrueCrypt Volume Creation Wizard* as follows:

![](/sbox/screen/truecrypt-en/14.png)

*Figure 5: The TrueCrypt Volume Creation Wizard window* 

There are three options for encrypting a *Standard Volume* in *figure 5*. In this chapter, we will use the *Create an encrypted file container* option. Please refer to the [**TrueCrypt**](http://www.truecrypt.org/docs/) documentation for the description of other two options.

**Step 4**. **Click** ![](/sbox/screen/truecrypt-en/05.png) to activate the following screen:

![](/sbox/screen/truecrypt-en/15.png)

*Figure 6: The Volume Type window*

The *TrueCrypt Volume Creation Wizard Volume Type* window lets you specify whether you would prefer to create a *Standard* or *Hidden* **TrueCrypt** volume. 

**Important**: For more information about *How to Create a Hidden Volume*, please refer to the [**Hidden Volumes**](/en/truecrypt_hiddenvolumes) page. 

**Step 5**. **Check** the *Standard TrueCrypt Volume* option. 

**Step 6**. **Click** ![](/sbox/screen/truecrypt-en/05.png) to activate the following screen:

![](/sbox/screen/truecrypt-en/16.png)

*Figure 7: The Volume Creation Wizard - Volume Location pane*

You can specify where you would like to store your *Standard Volume* in the *Volume Creation Wizard - Volume Location* screen. This file can be stored like any other file. 

**Step 7**. Either **type** in the name of the file into the text field, or **click** ![](/sbox/screen/truecrypt-en/17.png) to activate the following screen:

![](/sbox/screen/truecrypt-en/18.png)

*Figure 8: The Specify Path and File Name navigation window*

**Note**: A **TrueCrypt** Volume is contained inside a normal file. This means that it can be moved, copied or even deleted! You need to remember both the location and name of the file. However, you must choose new file name for the volume you create (also refer to section [**2.3 How to Create a Standard Volume on a USB Memory Stick**](#2.3)). In this tutorial, we will create our Standard Volume in the **My Documents** folder, and name the file *My Volume* as shown in *figure 8* above. 

**Tip**: You can use any file name and file extension. For example, you can name your Standard Volume *recipes.doc,* so that it will look like a *Word* document, or *holidays.mpg*, so it will look like a movie file. This is one way you can help disguise the existence of your Standard Volume. 

**Step 8**. **Click** ![](/sbox/screen/truecrypt-en/19.png) to close the *Specify Path and File Name* window and return to the *Volume Creation Wizard* window as follows:

![](/sbox/screen/truecrypt-en/20.png)

*Figure 9: The TrueCrypt Volume Creation Wizard displaying the Volume Location pane*

**Step 9**. **Click** ![](/sbox/screen/truecrypt-en/05.png) to activate *figure 10*. 

<a name="2.3"></a>
## 2.3 How to Create a Standard Volume on a USB Memory Stick ##

To create a **TrueCrypt** *Standard Volume* on a USB memory stick, perform steps 1 to 7 in section [**2.2 How to Create a Standard Volume**](#2.2), where you activate the *Select a TrueCrypt Volume* screen. Instead of choosing *My Documents* as your file location, **navigate** to and then **choose** your USB memory stick. Then, **enter** a file name and create the *Standard Volume* there. 

<a name="2.4"></a>
## 2.4 How to Create a Standard Volume (continued) ##

At this stage, you are ready to choose a specific encryption method (or *algorithm* as it is referred to on the screen) to encode the data that will be stored in your *Standard Volume*. 

![](/sbox/screen/truecrypt-en/21.png)

*Figure 10: The Volume Creation Wizard Encryption Options pane*

**Note**: You may leave the default options here as they appear. All algorithms presented in the two options here are considered secure. 

**Step 10**. **Click** ![](/sbox/screen/truecrypt-en/05.png)
 to activate the *TrueCrypt Volume Creation Wizard* screen as follows:

![](/sbox/screen/truecrypt-en/22.png)

*Figure 11: The Volume Creation Wizard displaying the Volume Size pane*

The *Volume Size* pane lets you specify the size of the *Standard Volume*. In this example, it is set at 10 megabytes. However, you may specify a different size. Consider the size of the documents and file types you would like to store, and then set an appropriate volume size for them. 

**Tip**: If you would like to backup your Standard Volume to a CD later on, then you should set the size to 700MB or less.

**Step 11**. **Type** in your specific volume size into the text field, and then **click** ![](/sbox/screen/truecrypt-en/05.png) to activate the following screen:

![](/sbox/screen/truecrypt-en/23.png)

*Figure 12: The TrueCrypt Volume Creation Wizard featuring the Volume Password pane*

**Important**: Choosing a secure and strong password is among the most important tasks you will perform when creating a *Standard Volume*. A good password will protect your encrypted volume, and the stronger the password you choose, the better. You don't have to create your own passwords, or even remember them, if you use a password generation
program like **KeePass**. Please refer to [**KeePass**](/keepass_main), to learn more information about password creation and storage.

**Step 12**. **Type** your password and then **re-type** your password into the *Confirm* text fields.

**Important**: The *Next* button will remain disabled until passwords in both text fields match. If your password is not particularly safe or secure, you will see a warning advising you of this. Consider changing it! Although **TrueCrypt** will still work with any password you have chosen, your data may not be very secure. 

**Step 13**. **Click** ![](/sbox/screen/truecrypt-en/05.png) to activate the following screen:

![](/sbox/screen/truecrypt-en/24.png)

*Figure 13: The TrueCrypt Volume Creation Wizard featuring the Volume Format pane*

**TrueCrypt** is now ready to create a *Standard Volume*. Move your mouse randomly within the *TrueCrypt Volume Creation Wizard* window for few seconds. The longer you move the mouse, the better the quality of the encryption key.

**Step 14**. **Click** ![](/sbox/screen/truecrypt-en/25.png) to begin creating your standard volume.

**TrueCrypt** will now create a file named *My Volume* in the *My Documents* folder as earlier specified. This file will contain a **TrueCrypt** *Standard Volume*, 10 Megabytes in size, that you can use to securely store your files. 

After a *Standard Volume* has been successfully created, the following dialog box will appear: 

![](/sbox/screen/truecrypt-en/26.png)

*Figure 14: The TrueCrypt volume has been successfully created message screen*

**Step 15**. **Click** ![](/sbox/screen/truecrypt-en/27.png) to complete
creating your *Standard Volume* and return to the **TrueCrypt** console.

**Step 16**. **Click** ![](/sbox/screen/truecrypt-en/28.png) to close *TrueCrypt Volume Creation Wizard*.

