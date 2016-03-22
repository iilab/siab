

---

lang: es
community: guide
type: tools
legacy: True
child: True
os: android
weight: 2
depth: 3
title: KeePassDroid - Advanced usage

---

## 3. Advanced KeePassDroid usage

- [**3.0 How to Edit an Entry**](#3.0)
- [**3.1 How to Generate Random Passwords**](#3.1)
- [**3.2 How to Lock the KeePassDroid database**](#3.2)
- [**3.3 How to Create a Backup of the Password Database file**](#3.3)
- [**3.4 How to Reset Your Master Password**](#3.4)
- [**3.5 Changing Timeouts**](#3.5)
    - [**3.5.1 Clipboard Timeout**](#3.5.1)
    - [**3.5.2 Lock Database Timeout**](#3.5.2)
    

<a name="3.0"></a>
## 3.0 How to Edit an Entry ##

You can change your password or modify other details stored in the entry. It is generally considered good security practice to change a password every three to six months.

**Step 1**. **Tap** the *Group* that contains the entry you wish to edit and then **tap** the entry to view its contents.

![](/sbox/screen/keepassdroid-en-1/020.png)

*Figure 1: Entry Contents.*

**Step 2**. **Tap** ![](/sbox/screen/keepassdroid-en-1/021.png) to start editing the information. 

![](/sbox/screen/keepassdroid-en-1/023.png)

*Figure 2: Edit information.*

**Step 3**. When you have finished, **tap** ![](/sbox/screen/keepassdroid-en-1/022.png) to save all changes.


<a name="3.1"></a>
## 3.1 How to Generate Random Passwords ##

Long, randomly-generated passwords are strong and secure as their generation is based on mathematical principles and cannot be simply guessed by someone who is trying to break into one of your accounts. **KeePassDroid** supplies a *Password Generator*, to help you with this process. 

![](/sbox/screen/keepassdroid-en-1/024.png)

*Figure 3: Edit password entry screen*

**Step 1**. **Tap** the button ![](/sbox/screen/keepassdroid-en-1/025.png) from within either the *Add Entry* or *Edit Entry* screen (Fig. 3 above), to activate the *Password Generator* screen as follows:

![](/sbox/screen/keepassdroid-en-1/026.png)

*Figure 4: Password Generator.*

The *Password Generator* screen automatically gives you a random, short 8-character password. However, we recommend that you use a longer password. You generate a longer, more secure password by selecting the following options as in our example: 


- **Length** at least 16-characters
- **Check** Upper-case Letter
- **Check** Lower-case Letter
- **Check** Digits
- **Check** Minus
- **Check** Underline 
- **Check** Brackets

**Note:** To generate passwords longer than 16-characters, replace the number in the field with your desired figure. 

See Fig. 4 above.

**Step 2**. **Tap** ![](/sbox/screen/keepassdroid-en-1/027.png) to have **KeePassDroid** generate a new random password.

**Step 3**. **Tap** ![](/sbox/screen/keepassdroid-en-1/028.png) to copy the generated password into your account entry and bring you back to the edit screen.

![](/sbox/screen/keepassdroid-en-1/029.png)

*Figure 5: Entry information*

**Step 4**. **Tap** ![](/sbox/screen/keepassdroid-en-1/030.png) to accept the password and return to the *Entry* screen as follows:

![](/sbox/screen/keepassdroid-en-1/031.png)

*Figure 6: Entry screen*

<a name="3.2"></a>
## 3.2 How to Lock the KeePassDroid database ##

**Step 1**. **Tap** on the **Lock icon** (![](/sbox/screen/keepassdroid-en-1/032.png)) which is at the top of the main screens while **KeePassDroid** is open. This will instantly lock your database. You will be presented with the following screen requiring you to enter your *master password* to unlock. 

![](/sbox/screen/keepassdroid-en-1/033.png)

*Figure 7: Locked Database*

<a name="3.3"></a>
## 3.3 How to Create a Backup of the Password Database ##

The **KeePassDroid** database file on your Android device is denoted by its *.kdb* file extension. You can copy this file to your computer or your USB memory stick. No one else will be able to open the database without the master password.

By default, the database is stored in a folder named *keepass* on your phone. The exact location is */mnt/sdcard/keepass*.

**Note**: You need to have KeePass installed on your computer, or a portable version of KeePass located on your USB memory stick, to be able to open your database which you copied from your Android device. 

Please see [**KeePass chapter**](/en/keepass_main) for more information.

<a name="3.4"></a>
## 3.4 How to Reset your Master Password ##

You can change the Master Password at any time. This can be done once you have opened the password database.

**Step 1**. **tap** the menu icon (![](/sbox/screen/keepassdroid-en-1/016.png)) found on the top right of the main screens. 

![](/sbox/screen/keepassdroid-en-1/034.png)

*Figure 8: Menu options*

**Step 2**. **Tap** ![](/sbox/screen/keepassdroid-en-1/035.png) to activate the following screen:

![](/sbox/screen/keepassdroid-en-1/036.png)

*Figure 9: Enter a new password.*

**Step 3**. Type in your new master password in the **Password** and the **Confirm Password** fields, Then **tap** OK.

![](/sbox/screen/keepassdroid-en-1/037.png)

*Figure 10: Enter a new password*

<a name="3.5"></a>
## 3.5 Changing Timeouts

<a name="3.5.1"></a>
### 3.5.1 Clipboard timeout

For greater security, the password is copied to the clipboard for a limited duration before it is automatically cleared from the clipboard. You have the option to change this duration to **30 seconds**, **1 minute** or **5 minutes**.

There is also an option **Never** but we recommend that you do not select this.

You can see these options in the following screen by going to: **Menu** (![](/sbox/screen/keepassdroid-en-1/016.png)) > **Settings** > **Application** > **Clipboard timeout**

![](/sbox/screen/keepassdroid-en-1/038.png)

*Figure 11: Clipboard timeout options.*

<a name="3.5.2"></a>
### 3.5.2 Lock Database Timeout

You also have the option to lock your database when the application is inactive for a specific time. Your database will automatically lock after 5 minutes of not being used. If you wish to shorten this, **tap**: **Menu** (![](/sbox/screen/keepassdroid-en-1/016.png)) > **Settings** > **Application** > **Application timeout**


![](/sbox/screen/keepassdroid-en-1/039.png)

*Figure 12:* Application timeout options.

**Select** **30 seconds**, **1 minute** or, the default **5 minutes**. As before, there is an option to **Never** timeout, but we recommend against using this.

