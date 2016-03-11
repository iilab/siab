

---

lang: zh
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 4
depth: 3
title: Hidden Volumes

---

List of topics on this page:

- [**5.0 About Hidden Volumes**](#5.0)
- [**5.1 How to Create a Hidden Volume**](#5.1)
- [**5.2 How to Mount a Hidden Volume**](#5.2)
- [**5.3 Tips on How to Use the Hidden Disk Feature Securely**](#5.3)

<a name="5.0"></a>
## 5.0 About Hidden Volumes ##

In **TrueCrypt**, a *Hidden Volume* is stored within your encrypted *Standard Volume*, but its existence is concealed. Even when you 'mount' or open your standard volume, it is not possible either to find or to prove the existence of the hidden volume. If you are forced to reveal your password and the location of your standard volume, then its content may be revealed, but **not** the existence of the hidden volume within. 

Imagine a briefcase with a secret compartment. You keep files that you do not mind having confiscated or losing in the normal section of your
briefcase, and you keep the important and private files in the secret
compartment. The point of the secret compartment (especially a
well-designed one), is to hide its own existence and therefore, the
documents within it. 

<a name="5.1"></a>
## 5.1 How to a Create a Hidden Volume ##

The creation of a **TrueCrypt** *Hidden Volume* is similar to creating a **TrueCrypt** *Standard Volume*: Some of the panes, screens and windows are even the same. 

**Step 1**. **Open** **TrueCrypt**.

**Step 2**. **Click** ![](/sbox/screen/truecrypt-en/13.png) to activate the *TrueCrypt Volume Creation Wizard*. 

**Step 3**. **Click** ![](/sbox/screen/truecrypt-en/05.png) to accept the default *Create an encrypted file container* option.

**Step 4**. **Check** the *Hidden TrueCrypt volume* option as follows: 

![](/sbox/screen/truecrypt-en/37.png)

*Figure 1: The TrueCrypt Volume Creation Wizard with the Hidden TrueCrypt volume option enabled*

**Step 5**. **Click** ![](/sbox/screen/truecrypt-en/05.png) to activate the following screen:

![](/sbox/screen/truecrypt-en/38.png)

*Figure 2: The TrueCrypt Volume Creation Wizard - Mode window*

- *Direct mode*: This option lets you create the *Hidden Volume* within an existing *Standard Volume*.

- *Normal mode*: This option lets you create a completely new *Standard Volume* in which to store the *Hidden Volume*. 

In this example, we will use the *Direct mode*. 

**Note**: If you would rather start a new *Standard Volume*, please repeat the process from section [**2.2 How to Create a Standard Volume**](/en/truecrypt_standardvolumes#2.2).

**Step 6**. **Check** the *Direct Mode* option and then **click** ![](/sbox/screen/truecrypt-en/05.png) to activate the *TrueCrypt Volume Creation - Volume Location* window.

**Note**: Make sure the *Standard Volume* is unmounted before selecting it. 

**Step 7**. **Click** ![](/sbox/screen/truecrypt-en/17.png) to activate the following screen:

![](/sbox/screen/truecrypt-en/29.png)

*Figure 3: The TrueCrypt Volume Creation Wizard - Select a TrueCrypt Volume window*

**Step 8**. **Locate** the volume file using the *Select a TrueCrypt Volume* window as shown in *figure 3*. 

**Step 9**. **Click** ![](/sbox/screen/truecrypt-en/30.png) to return to the *TrueCrypt Volume Creation Wizard*.

**Step 10**. **Click** ![](/sbox/screen/truecrypt-en/05.png) to activate the *Enter password* screen.

**Step 11**. **Type** in password you used when creating the *Standard Volume* into the *Password* text field to activate the following screen:

![](/sbox/screen/truecrypt-en/46.png)

*Figure 4: The TrueCrypt Volume Creation Wizard - Hidden Volume Message pane*

**Step 12**. **Click** ![](/sbox/screen/truecrypt-en/05.png) after you have read the message to activate the *Hidden Volume Encryptions Options* screen.

**Note**: Leave both the default *Encryption Algorithm* and *Hash Algorithm* settings for the *Hidden Volume* as they are. 

**Step 13**. **Click** ![](/sbox/screen/truecrypt-en/05.png) to activate the following screen:

![](/sbox/screen/truecrypt-en/41.png)

*Figure 5: The TrueCrypt Volume Creation Wizard - Hidden Volume Size window*

You will be prompted to specify the size of the *Hidden Volume*. 

**Note**: Consider the kind of documents, their quantity and size that need to be stored. Do leave some space for the *Standard Volume*. If you select the maximum size available for the *Hidden Volume*, you will not be able to put any more new files into the original *Standard Volume*. 

If your *Standard Volume* is 10 Megabytes(MB) in size and you specify a *Hidden Volume* size of 5MB (as shown in *figure 6* above), you will have two volumes (one hidden and one standard volume) of approximately 5MB each. 

Ensure that the information you store in the *Standard Volume* does not exceed the 5MB you have set. This is because the **TrueCrypt** program itself does not automatically detect the existence of the *Hidden Volume*, and it could accidentally overwrite it. You may risk losing all files stored in the hidden volume if you exceed your previously established size. 

**Step 14**. **Type** in the desired hidden volume size into the corresponding text box as shown in *figure 6*. 

**Step 15**. **Click** ![](/sbox/screen/truecrypt-en/05.png) to activate the *Hidden Volume Password* window.

You must now create a *different* password for the hidden volume from the one used to protect your standard volume. Again, remember to choose a strong password. Please refer to the [**KeePass**](http://securityinabox.org/en/keepass_main) chapter to learn more about creating strong passwords. 

**Tip**: If you anticipate being forced to reveal the contents of your **TrueCrypt** volumes, then store your password for the standard volume in **KeePass**, and create a strong password that you only have to remember for hidden volume. This will help you to conceal your hidden volume, as you will not leave any trace of its existence.

**Step 16**. **Create** a password and **type** it in twice, and then **click** ![](/sbox/screen/truecrypt-en/05.png) to activate the following screen:

![](/sbox/screen/truecrypt-en/42.png)

*Figure 6: The TrueCrypt Volume Creation Wizard - Hidden Volume Format pane*

Leave the default *File System* and *Cluster* options as they are. 

**Step 17**. **Move** the mouse cursor around the screen to increase the cryptographic strength of the encryption and then **click** ![](/sbox/screen/truecrypt-en/25.png) to format the hidden volume.

*After the hidden volume has been formatted, the following screen appears:* 

![](/sbox/screen/truecrypt-en/43.png)

*Figure 7: The TrueCrypt Volume Creation Wizard message screen*

**Note**: *Figure 8* both confirms that you have successfully created a hidden volume, as well as warning you against the dangers of overwriting files in the hidden volume when storing files in the standard volume. 

**Step 18**. **Click** ![](/sbox/screen/truecrypt-en/27.png) to activate the *Hidden Volume Created* window, and then **click** ![](/sbox/screen/truecrypt-en/28.png) and return to the **TrueCrypt** console. 

The hidden volume has now been created inside your standard volume. You may now store documents in the hidden volume, which remain invisible even to someone who has obtained the password for that particular standard volume. 

<a name="5.2"></a>
## 5.2 How to Mount the Hidden Volume ##

The method for mounting or making a *Hidden Volume* accessible for use is exactly the same as that for a *Standard Volume*; the only difference is you will use the password that you have just created for the *Hidden Volume*.

To *mount* or open the *Hidden Volume*, perform the following steps: 

**Step 1**. **Select** a drive from the list (in this example, drive *K*):

![](/sbox/screen/truecrypt-en/44.png)

*Figure 8: A mount drive selected in the TrueCrypt Volume screen*

**Step 2**. **Click** ![](/sbox/screen/truecrypt-en/17.png) to activate the *Select a TrueCrypt Volume* window. 

**Step 3**. **Navigate** to and then **select** your *TrueCrypt* volume file (same file as for the standard volume). 

**Step 4**. **Click** ![](/sbox/screen/truecrypt-en/30.png) to return to the **TrueCrypt** console.

**Step 5**. **Click** ![](/sbox/screen/truecrypt-en/31.png) to activate the *Enter Password for* prompt screen as follows:

![](/sbox/screen/truecrypt-en/32.png)

*Figure 9: The Enter Password screen*

**Step 6**. **Type** the password you used to create the hidden volume, and then **click** ![](/sbox/screen/truecrypt-en/33.png). 

Your hidden volume is now mounted (or opened) as follows:

![](/sbox/screen/truecrypt-en/45.png)

*Figure 10: The TrueCrypt main screen displaying the newly mounted Hidden Volume*

**Step 7**. **Double click** on above entry or access it through the *My Computer* window. 

<a name="5.3"></a>
## 5.3 Tips on How to Use the Hidden Disk Feature Securely ##

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

**Step 1**. **Click** ![](/sbox/screen/truecrypt-en/47.png) on the *Enter Password* prompt shown in *figure 10*, above. This will activate the *Mount Options* window as follows:

![](/sbox/screen/truecrypt-en/48.png)

*Figure 11: The Mount Options window*

**Step 2**. **Check** the *Protect hidden volume against damage caused by writing to outer volume* option.

**Step 3**. **Type** in in your Hidden Volume password, and then **click** ![](/sbox/screen/truecrypt-en/33.png).

**Step 4**. **Click** ![](/sbox/screen/truecrypt-en/31.png) to mount your standard volume. After you have successfully mounted it, you will be able to add decoy files without damaging your hidden volume.

**Step 5**. **Click** ![](/sbox/screen/truecrypt-en/51.png) to dismount, or your make your standard volume unavailable for use, when you have finished modifying its contents. 

**Remember**: You only need to do this when you are updating the files in your standard volume. If forced to reveal your standard volume to someone else, you should not use the *Protect hidden volume* feature.

