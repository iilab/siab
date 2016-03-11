

---

lang: xx
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Mount the Standard Volume

---

List of sections on this page:

- [**3.0 How to Mount a Standard Volume**](#3.0)
- [**3.1 How to Dismount a Standard Volume**](#3.1)

<a name="3.0"></a>
## 3.0 How to Mount a Standard Volume ##

In **TrueCrypt**, to *mount* a *Standard Volume* refers to making the standard volume available for use. In this section, you will learn how to mount your newly created standard volume.  

To begin mounting your standard volume, perform the following steps: 

**Step 1**. **Double click** ![](/sbox/screen/truecrypt-en/52.png) or **Select Start > Programs > TrueCrypt > TrueCrypt** to open **TrueCrypt**.

**Step 2**. **Select** any drive from the list as follows: 

![](/sbox/screen/truecrypt-en/12.png)

*Figure 1: The TrueCrypt console*

*In this example the Standard Volume will be mounted as the M: drive.*

**Note**: In *figure 1*, the *M:* drive has been selected for mounting the *standard volume*; however, you may choose another listed drive.

**Step 3**. **Click** ![](/sbox/screen/truecrypt-en/17.png)

*The Select a TrueCrypt Volume screen will appear as follows:*

![](/sbox/screen/truecrypt-en/29.png)

*Figure 2: The Select a TrueCrypt Volume screen*

**Step 4**. **Select** the standard volume file that you created, then **click** ![](/sbox/screen/truecrypt-en/30.png) to close *figure 2* and return to the **TrueCrypt** console.

**Step 5**. **Click** ![](/sbox/screen/truecrypt-en/31.png) to activate the *Enter password for* prompt screen as follows:

![](/sbox/screen/truecrypt-en/32.png)

*Figure 3: The Enter password prompt screen*

**Step 6**. **Type** the password in the *Password*: text field. 

**Step 7**. **Click** ![](/sbox/screen/truecrypt-en/33.png) to begin mounting the *Standard Volume*.

**Note**: If the password you typed is incorrect, **TrueCrypt** will prompt you to re-type your password and **click** ![](/sbox/screen/truecrypt-en/33.png). If the password is correct, the *Standard Volume* will be mounted as follows:

![](/sbox/screen/truecrypt-en/34.png)

*Figure 4: The TrueCrypt console displaying the newly mounted Standard Volume*

**Step 8**. **Double click** the highlighted entry in **TrueCrypt** or **double click** the corresponding drive letter in the *My Computer* screen to access the *Standard Volume* (now mounted on drive *M:* on your computer). 

![](/sbox/screen/truecrypt-en/35.png)

*Figure 5: Accessing the Standard Volume through the My Computer screen*

**Note**: We have just successfully mounted the *My Volume* standard volume on a virtual disk *M:*. This virtual disk behaves like a real disk, except that it is entirely encrypted. Any files will be automatically encrypted when you copy, move or save them to this
virtual disk (a process known as on-the-fly encryption). 

You can copy files to and from the *Standard Volume* just as you would
copy them to any normal disk (for example, by dragging-and-dropping
them). When you move a file out of the *Standard Volume*, it is
automatically decrypted. Conversely if you move a file onto the
*Standard Volume*, **TrueCrypt** automatically encrypts it. If your computer crashes or is suddenly switched off, **TrueCrypt** will immediately close the *Standard Volume*. 

**Important**: After transferring files to the **TrueCrypt** volume, make
sure that no traces of the files are left behind on the computer or USB
memory stick that they came from. Please refer to chapter [**6. How to destroy sensitive information**](/en/chapter-6).

<a name="3.1"></a>
## 3.1 How to Dismount the Standard Volume ##

In **TrueCrypt**, to *dismount* a *Standard Volume* simply means to make a volume unavailable for use. 

To close or dismount a *Standard Volume* and make its files accessible only to someone with a password, perform the following steps: 

**Step 1**. **Select** the volume from the list of mounted volumes in the main **TrueCrypt** window as follows:

![](/sbox/screen/truecrypt-en/34.png)

*Figure 17: Selecting the Standard Volume to be dismounted*

**Step 2**. **Click** ![](/sbox/screen/truecrypt-en/49.png) to dismount or close your **TrueCrypt** standard volume. 

**Important**: Make sure to dismount your **TrueCrypt** volume before putting your computer to *Standby* or *Hibernate* mode. Better yet, always shut-down your computer or laptop if you plan on leaving it unattended. This will prevent anyone from being able to gain your volume password.

To retrieve a file stored in your standard volume once you have closed or dismounted it, you will have to mount it again.


