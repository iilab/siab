

---

lang: en
community: guide
type: tools
os: windows
weight: 019
title: KeePass - secure password manager

---

KeePass is easy-to-use, cross-platform, free and open-source software (FOSS) that allows you to store all of your passwords in one secure, portable database.

# Required reading


:[Create and maintain secure passwords](../../../tactics/passwords)


:[KeePass - secure password manager](keepass-secure-password-manager)

# What you will get from this guide

- The ability to save all your passwords in one convenient and secure database
- The ability to create and store many strong passwords without having to remember them

# 1. Introduction to KeePass





## 1.0 Other tools like KeePass

**KeePass** is also available for **GNU Linux** and **Mac OS** (in the [**KeePassX**](https://keepassx.org) version). You can find versions of **KeePass** for other platforms like **iPhone**, **BlackBerry**, **Android**, **PocketPC**, etc. However if you wish to try other similar programs we recommend:

* [**Password Safe**](http://passwordsafe.sourceforge.net/) available for **Microsoft Windows** and **GNU Linux**.
* [**1Password**](http://agilewebsolutions.com/products/1Password) available for **Mac OS**, **Microsoft Windows**, **iPhone** and **iPad**.

## 1.1 Things you should know about KeePass before you start

**KeePass** is an easy-to-use, powerful tool that helps you store and manage all your passwords in a highly secure database. You can put both that database and the **KeePass** program on a USB memory stick and carry it with you. The database is protected by a 'master password' that you create. This password is also used to encrypt the entire contents of the database. You can store your existing passwords in **KeePass** or have it generate one for you. **KeePass** doesn't require any prior configuration or specific installation instructions. It's ready to go when you are!


# 2. Install and manage KeePass

In the sections that follow, you will be taught how to install KeePass, create a master password, save your newly-created database, generate a random password for a particular program, create a backup copy of the database and extract the passwords from **KeePass** when needed.

## 2.0 Install KeePass

**Step 1**. **Double click** ![](/sites/siabnext.ttc.io/files/media/keepass-en-win-01.png); the *Open File - Security Warning* dialog box may appear. If it does, **click** ![](/sites/siabnext.ttc.io/files/media/keepass-en-win-02.png) to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/keepass-en-win-03.png)

*Figure 1: The Select Setup Language screen*

**Step 2**. **Click** ![](/sites/siabnext.ttc.io/files/media/keepass-en-win-04.png) to activate the *Setup - KeePass Password Safe – Welcome to the KeePass Password Safe Setup Wizard* screen.

**Step 3**. **Click** ![](/sites/siabnext.ttc.io/files/media/keepass-en-win-05.png) to activate the  *License Agreement* screen. Please read the *License Agreement* before proceeding with the rest of the installation process. 

**Step 4**. **Check** the *I accept the agreement* option to enable the *Next* button, and then **click** ![](/sites/siabnext.ttc.io/files/media/keepass-en-win-05.png) to activate the *Select Destination Location* screen.

**Step 5**. **Click** ![](/sites/siabnext.ttc.io/files/media/keepass-en-win-05.png) to accept the default installation path.

**Step 6**. **Click** ![](/sites/siabnext.ttc.io/files/media/keepass-en-win-05.png) to activate the following screen.

![](/sites/siabnext.ttc.io/files/media/keepass-en-win-06.png)

*Figure 2: The Select Additional Tasks screen* 

**Step 7**. **Check** the ![](/sites/siabnext.ttc.io/files/media/keepass-en-win-07.png) option as shown in above in *figure 2*. 

**Note**: If you enable the *Create a Start Menu folder* option, the *Setup - KeePass Password Safe* installation wizard automatically creates a **KeePass** *Quick Launch* icon in the *Start* menu. 

**Step 8**. **Click** ![](/sites/siabnext.ttc.io/files/media/keepass-en-win-05.png) to launch the *Ready to Install* summary screen, and then **click** ![](/sites/siabnext.ttc.io/files/media/keepass-en-win-08.png) to activate the **Installing** screen and its status progress bar.

A few seconds later the *Completing the KeePass Password Safe Setup Wizard* screen will appear.

**Step 9**. **Check** the *Launch KeePass* option and then **click** ![](/sites/siabnext.ttc.io/files/media/keepass-en-win-09.png) to open **KeePass** immediately, and be directed to the **KeePass** *Plugins and Extensions* web site, if you are connected to the Internet.


## 2.1 Create a new KeePass database

To open **KeePass**, perform the following steps:

**Step 1**. **Select Start > All Programs > KeePass** or **click** the ![](/sites/siabnext.ttc.io/files/media/keepass-en-win-36.png) icon on your desktop to activate the **KeePass** main screen as follows:

![](/sites/siabnext.ttc.io/files/media/keepass-en-win-10.png)

*Figure 3: The KeePass Password Safe console*

Creating a new password database involves two steps. You must come up with a single, unique and strong master password that you will use to lock and unlock your database of passwords. Then, you must save that password database.

To create a new password database, follow these steps:

**Step 1**. **Select File > New** as follows:

![](/sites/siabnext.ttc.io/files/media/keepass-en-win-11.png)

*Figure 4: The KeePass screen with File > New selected*

This will activate the *Create New Password Database* screen as follows:

![](/sites/siabnext.ttc.io/files/media/keepass-en-win-12.png)

*Figure 5: The KeePass Create New Password Database screen*

**Step 2**. **Type** in the master password you have created into the *Master Password* field.

![](/sites/siabnext.ttc.io/files/media/keepass-en-win-13.png)

*Figure 6: The KeePass Set Composite Master Key screen with the Master Password field completed*

You will see an orange-green progress bar underneath the password entry. As you type in a password and the number of characters increases, the amount of green in the bar will increase to show the complexity and strength of your password improving. 

**Tip**:  You should aim to have at least half the bar filled with green when you have finished typing in your password. 

**Step 3**. **Click** ![](/sites/siabnext.ttc.io/files/media/keepass-en-win-14.png) to activate the *Repeat Master Password* screen and confirm the password as follows:

![](/sites/siabnext.ttc.io/files/media/keepass-en-win-15.png)

*Figure 7: The KeePass Repeat Master Password screen*

**Step 4**. **Type** in the same password as before, then **click** ![](/sites/siabnext.ttc.io/files/media/keepass-en-win-14.png).

**Step 5**. **Click** ![](/sites/siabnext.ttc.io/files/media/keepass-en-win-16.png) to see if you are typing in your password correctly.

**Warning**: Do not carry out step 5 if you fear that someone may be looking over your shoulder. 

Once you have successfully typed in the master password twice, the **KeePass** console is activated as follows:

![](/sites/siabnext.ttc.io/files/media/keepass-en-win-17.png)

*Figure 8: The KeePass Password Safe screen in active mode*

After you have created the password database, you need to save it. To save the password database, follow these steps:

**Step 1**. **Select File > Save As** as follows:

![](/sites/siabnext.ttc.io/files/media/keepass-en-win-18.png)

*Figure 9: The KeePass Password Safe screen*

*This will activate the Save As screen as follows*:

![](/sites/siabnext.ttc.io/files/media/keepass-en-win-19.png)

*Figure 10: The Save As screen*

**Step 2**. **Type** in a name for your new password database file.

**Step 3**. **Click** ![](/sites/siabnext.ttc.io/files/media/keepass-en-win-20.png) to save your database.

**Tip**: Remember the location and file name of your database! It will come in very handy when you are creating a backup of it. 

Congratulations! You have successfully created and saved your secure password database. Now you can begin to fill it up with all your current and future passwords.

## 2.2 Add an entry to KeePass

The *Add Entry* screen lets you add account information, passwords and other important details into your newly-created database. In the example that follows, you will be adding entries to store passwords and user names for different websites and email accounts. 

**Step 1**. **Select Edit > Add Entry** in the **KeePass** *Password Safe* screen to activate the *Add Entry* screen as follows:

![](/sites/siabnext.ttc.io/files/media/keepass-en-win-21.png)

*Figure 11: The KeePass Password Safe screen with Edit > Add Entry selected*

![](/sites/siabnext.ttc.io/files/media/keepass-en-win-22.png)

*Figure 12: The KeePass Add Entry screen*

**Note**: The *Add Entry* screen presents you with a number of fields to be completed. None of these fields are mandatory; information submitted here is largely for your own convenience. It may prove useful in situations where you are searching for a particular entry. 

A brief explanation of these different text boxes is presented as follows:

- **Group**: **KeePass** lets you sort your passwords into pre-defined groups. For example: *'Internet'* would be a good place to store passwords that relate to website accounts.

- **Title**: A name to describe the particular password entry. For example: Gmail password.
- **User name**: The user name associated with the password entry. For example: securitybox@gmail.com.
- **URL**: The internet site associated with the password entry. For example: https://mail.google.com.
- **Password**: This feature automatically generates a random password when the *Add Entry* screen is activated. If you are registering a new email account, you can use the 'default' password in this field. You can also use this feature if you want to change an existing password for one generated by **KeePass**. Since **KeePass** will always remember it for you, there is no need to even see the password. A randomly generated password is considered strong (that is, difficult for an intruder to guess or break).

Generating a random password on request will be described in the following section. You can, of course, replace the default password with one of your own. For instance, if you are creating an entry for an account that already exists you will want to enter the correct password here.

- **Repeat Password**: The confirmation of the password.
- **Quality**: A progress bar that measures password strength according to length and randomness. The more green there is on the scale, the stronger your chosen password.
- **Notes**: Here is where you type in descriptive or general information about the account or site for which you are storing information. For example: *Mail server settings: POP3 SSL, pop.gmail.com, Port 995; SMTP TLS, smtp.gmail.com, Port: 465*.

**Note**: Creating or modifying the password entries in **KeePass** does not change your actual passwords! Think of **KeePass** as a secure electronic address book for your passwords. It only stores what you write in it, nothing more.

If you select *Internet* from the *Group* drop-down list, your password entry might resemble the following:

![](/sites/siabnext.ttc.io/files/media/keepass-en-win-24.png)

*Figure 13: The KeePass Add Entry screen - completed*

**Step 2**. **Click** ![](/sites/siabnext.ttc.io/files/media/keepass-en-win-14.png) to save your changes to the *Add Entry* screen.

*Your password entry now appears in the* Internet *group.* 

![](/sites/siabnext.ttc.io/files/media/keepass-en-win-25.png)

*Figure 14: The KeePass Password Safe screen*

**Note**: The bottom panel of this window displays information about the entry selected. This includes creation, editing and expiry time as well as notes you may have recorded in the entry. It does not reveal the password.

- **Expires**: Check this item to activate text boxes in which you can specify an expiry date. By doing this, you could add a reminder for yourself to change the password at a specific time (every 3 months,	for example). When a password has expired, it will appear with a red cross next to its name, as shown in the example below:

![](/sites/siabnext.ttc.io/files/media/keepass-en-win-23.png)

*Figure 15: An example of an expired key in the NetSecureDb*.*kdb* *screen*

## 2.3 Edit a KeePass entry

You may edit an existing entry in **KeePass** at any time. You can change your password or modify other details stored in the password entry. It is generally considered good security practice to change a password every three to six months (remembering to update it on your email system etc. before changing it in KeePass).

To edit an entry, perform the following steps:

**Step 1**. **Select** the correct *Group* in the left-hand side to activate the entries associated with it.

**Step 2**. **Select** the relevant entry, then **right click** on that selected entry to activate the following window: 

![](/sites/siabnext.ttc.io/files/media/keepass-en-win-26.png)

*Figure 16: The KeePass Password Safe screen displaying the Edit menu*

**Step 3**. **Click** ![](/sites/siabnext.ttc.io/files/media/keepass-en-win-14.png) to save any necessary changes to this information, including the password.

To change an existing password (that you previously created yourself) for one generated and recommended by **KeePass**, please read the following section.


## 2.4 Generating random passwords for KeePass entries

Long, random passwords are considered strong in the world of security. Their randomness is based on mathematical principles and cannot simply be 'guessed' by someone who is trying to break into one of your accounts. **KeePass** supplies a  *Password Generator*, to help you with this process. As you have seen above, a random password is automatically generated when you add a new entry. This section will describe how to generate one yourself.

**Note**: The *Password Generator* can be activated from within the *Add Entry* and *Edit/View Entry* screens. Alternatively, **select: Tools &gt; Password Generator**.

**Step 1**. **Click** ![](/sites/siabnext.ttc.io/files/media/keepass-en-win-27.png) from within either the *Add Entry* or *Edit/View Entry* screen, to activate the *Password Generator* screen as follows:

![](/sites/siabnext.ttc.io/files/media/keepass-en-win-28.png)

*Figure 17: The KeePass Password Generator screen*

The *Password Generator* screen presents a variety of choices for generating a password. You can specify the length of the desired password, the pool of characters from which it will be created and much else. For our purposes, we can use the default options presented. This means that the generated password will be 20 characters long and made up of lower and upper case letters, as well as numbers.

**Step 2**. **Click** ![](/sites/siabnext.ttc.io/files/media/keepass-en-win-29.png) to begin the process. When complete, **KeePass** will present the generated password to you.

![](/sites/siabnext.ttc.io/files/media/keepass-en-win-30.png)

*Figure 18: The KeePass Generated Password section*

**Note**: You can view the generated password by **clicking** ![](/sites/siabnext.ttc.io/files/media/keepass-en-win-16.png). However, this creates a security risk as we discussed above. In essence, you will never need to see the generated password. We will explain more about this in section **3.0 Using KeePass Passwords**.

**Step 3**. **Click** ![](/sites/siabnext.ttc.io/files/media/keepass-en-win-31.png) to accept the password and return to the *Add Entry* screen as follows:

![](/sites/siabnext.ttc.io/files/media/keepass-en-win-24.png)

*Figure 19: The KeePass Add Entry screen*

**Step 4**. **Click** ![](/sites/siabnext.ttc.io/files/media/keepass-en-win-14.png) to save this entry.

**Step 5**. **Select File > Save** to save your updated password database.


## 2.5 Minimizing and closing KeePass

You can minimise or exit the **KeePass** program at any time. When you open or restore it again, you will be prompted to enter your *Master Password*. 

**KeePass** minimises itself, appearing in your system tray (at the bottom right corner of the screen) as follows: 
![](/sites/siabnext.ttc.io/files/media/keepass-en-win-39.png).

**KeePass** also lets you lock the program by performing the following steps:

**Step 1**. **Select File > Lock Workspace** to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/keepass-en-win-40.png)

*Figure 20: The KeePass - Safe Before Close/Lock prompt screen*

**Step 2**. **Click** ![](/sites/siabnext.ttc.io/files/media/keepass-en-win-43.png) to save your information and disable the **KeePass** console so it resembles *figure 3*, and the following icon will appear in your *System Tray*:
![](/sites/siabnext.ttc.io/files/media/keepass-en-win-42.png)

To restore **KeePass** perform the following step:

**Step 1**. **Double click** this icon to restore **KeePass** to its normal size, and activate the following screen:

![](/sites/siabnext.ttc.io/files/media/keepass-en-win-33.png)

*Figure 21: The KeePass Open Database - NetSecureDb.kdb screen*

**Step 2**. **Enter** your *Master Password* to open **KeePass**.

To close **KeePass** perform the following step:

**Step 1**. **Select File > Exit** to close the **KeePass** program completely. 

If you have any unsaved changes in the database, **KeePass** will prompt you to save them.


## 2.6 Backup your KeePass database

The **KeePass** database file on your computer is denoted by its .kdb file extension. You can copy this file to a USB memory stick. No one else will be able to open the database without the master password.

**Step 1**. **Select File > Save As** from the main screen, and save a copy of the database to another location.

You can run the entire **KeePass program** from a USB memory stick. Please refer to the [**Portable KeePass**](#1486) section.


## 2.7 Resetting your master passphrase

You can change the *Master Password* at any time. This can be done once you have opened the password database.

**Step 1**. **Select File > Change Master Key**

![](/sites/siabnext.ttc.io/files/media/keepass-en-win-34.png)

*Figure 22: The KeePass Change Master Key screen*

**Step 2**. **Type** in the new *Master Password* twice when prompted to do so.

![](/sites/siabnext.ttc.io/files/media/keepass-en-win-35.png)

*Figure 23: The KeePass Change Master Key screen*


# 3. Use KeePass

Given that a secure password is not easily memorised, **KeePass** lets you copy it from the database and paste it onto whatever account or website requires it. For greater security, a copied password will only remain on the clipboard for about 10 seconds, so it will save time to have your account or website already open and running, so that you can paste the relevant password there as required. 

## 3.1 Sign in to an account using KeePass

**Step 1**. **Right click** on the required password entry to activate a drop-down list, 

**Step 2**. **Select Copy Password** as follows:

![](/sites/siabnext.ttc.io/files/media/keepass-en-win-37.png)

*Figure 1: The KeePass Password Safe screen*

**Step 3**. Go to the related account or site and **paste** the password into the appropriate field:

![](/sites/siabnext.ttc.io/files/media/keepass-en-win-38.png)

*Figure 2: A Gmail Account displaying a pasted password*

**Tip**: For efficient copying, pasting and switching windows, use the keyboard shortcuts. **Press and hold** the *Ctrl* key, then press *C* to copy a password. **Press and hold** the *Ctrl* key, then press *V* to paste that password. **Press and hold** the *Alt* key, then **press** the *tab* key to switch between open programs and windows.

**Note**: By using **KeePass** all the time, you never actually have to see or know what your password is. The copy/paste functions take care of moving it from the database to the required window. If you use the *Random Generator* feature and then transfer this password to a new email account registration process, you will be using a password that you have never seen in plain view. And it still works!


# 4. Portable KeePass





## 4.1 Differences between the installed and portable versions of KeePass

Given that portable tools are not installed on a local computer, their existence and use may remain undetected. However, keep in mind that your external device or USB memory stick, and portable tools are only as safe as the computer you are using, and may risk being exposed to adware, malware, spyware and viruses.

There are no other differences between **Portable KeePass** and the version designed to be installed.


## 4.2 Download and extract portable keepass

**Step 1**. **Click** [**http://keepass.info/download.html**](http://keepass.info/download.html) to be directed to the appropriate download site.

**Step 2**. **Click** ![](/sites/siabnext.ttc.io/files/media/keepassportable-en-win-01.png) to activate the **Source Forge** download page.

**Step 3**. **Click** ![](/sites/siabnext.ttc.io/files/media/keepassportable-en-win-02.png) to save the installation file to your computer; and then **navigate** to it.

**Step 4**. **Right click** ![](/sites/siabnext.ttc.io/files/media/keepassportable-en-win-02.png) to activate the pop-up menu and then **select** the *Extract files...* item to activate the following screen:

![](/sites/siabnext.ttc.io/files/media/keepassportable-en-win-04.png) 

*Figure 1: Select a Destination and Extract Files*

**Step 5**. **Navigate** to the removable drive or USB memory stick as shown in *Figure 2* below, and then **click** ![](/sites/siabnext.ttc.io/files/media/keepassportable-en-win-06.png) to create a new folder in which to extract the ![](/sites/siabnext.ttc.io/files/media/keepassportable-en-win-02.png).

**Step 6**. **Enter** a name for the new folder in either ![](/sites/siabnext.ttc.io/files/media/keepassportable-en-win-08.png) or the document tree as shown in *Figure 3* below: 

![](/sites/siabnext.ttc.io/files/media/keepassportable-en-win-09.png)

*Figure 2: The Extraction path and options window document tree (resized)*

**Note**: Choosing a different name for the **Portable KeePass** folder may make its existence, and the fact that you are using it less obvious.

**Step 7**. **Click** ![](/sites/siabnext.ttc.io/files/media/keepassportable-en-win-10.png) to extract its contents to the newly created **Portable KeePass** folder. 

**Step 8**. **Navigate** to your external drive or USB memory stick, then **open** it to view the **Portable KeePass** folder.

![](/sites/siabnext.ttc.io/files/media/keepassportable-en-win-11.png)

*Figure 3: The destination removable drive window displaying the newly extracted Portable KeePass folder*

**Step 9**. **Double click** ![](/sites/siabnext.ttc.io/files/media/keepassportable-en-win-12.png) to begin using **Portable KeePass**.

Please refer to the [**sections above**](#1477) for instructions on how to manage and use **KeePass**.


# FAQ

**KeePass** is a very easy program to use. The important part is getting into the habit of creating new passwords in **KeePass**. It may be difficult to get used to the fact that you never have to see a password again, but it is definitely easier than having to remember them!

***Q***: *On the outside chance that I forget my master password, is there anything I can do to access **KeePass** and retrieve my password databases?*

***A***: *No. There is nothing you can do in that situation. On the bright side, at least no one else will be able to access your password database! To prevent this from happening, you could use some of the methods for remembering a password that are described in the [**Create and maintain strong passwords**](../passwords) guide.*

***Q***: *And if I uninstall **KeePass**, what will happen to my passwords?*

***A***: *The program will be deleted from your computer; however, your database (stored in a .kdb file) will remain. You can open this file at any time in the future if you install **KeePass** again.*

***Q***: *I think I accidentally deleted the database file!*

***A***: *Hopefully, you made a backup beforehand. Also, make sure you haven't simply forgotten where you stored the file in the first place. Search your computer for a file with a .kdb extension. If you really have deleted it, take a look at the [**Recuva**](../recuva/windows) guide. It could help you to recover the file.*
