

---

lang: en
community: guide
type: tools
os: os-x
weight: 019
title: KeePassX for Mac OS X - Secure password manager

---

KeePassX is easy-to-use, cross-platform, [**free and open source (FOSS)**](/en/glossary#FOSS) that allows you to store all of your passwords in one secure, portable database.

# Required reading


:[Create and maintain secure passwords](../../../tactics/passwords)


:[KeePassX for Mac OS X - Secure password manager](keepassx-for-mac-os-x-secure-password-manager)

# What you will get from this guide

- The ability to save all your passwords in one convenient and secure database
- The ability to create and store many strong passwords without having to remember them

# 1. Introduction to KeePassX

In the sections that follow, you will learn how to:

* Set a *master passphrase*
* Save your newly created database
* Generate a random password for a particular service
* Extract passwords from **KeePassX** when you need them 
* Change your *master passphrase*

If you use **KeePassX** consistently for a particular account, you never actually have to know (or even see) your password for that application or service. The tool's copy/paste function takes care of moving the relevant password from the database to the required login form, then wiping it from clipboard memory. If, for example, you take advantage of the *Random Password Generator* feature of **KeePassX**, then configure an account to use the generated password, you will be relying on a strong password that you never actually have to look at or memorize. But it will still work! Just remember to backup your **KeePassX** database!

## 1.0 Things you should know about KeePassX before you start

**KeePassX** is a powerful, easy-to-use tool that helps you store and manage all your passwords in a highly secure database. You can put both that database and the **KeePassX** program on a USB memory stick and carry it with you. You can also make multiple copies of your database as backup copies to access from different devices, portable media, or the cloud. The database is protected by a *master passphrase* that you create. This password is also used to encrypt the entire contents of the database. You can store your existing passwords in **KeePassX** and have it generate new passwords for you. **KeePassX** doesn't require any prior configuration or specific installation instructions. It's ready to go when you are!

## 1.1 Other tools like KeePassX

**KeePassX** is cross-platform, which means it is also available for **GNU Linux** and **Windows** (in the [**KeePassX**](https://keepassx.org) version). However, if you wish to try other similar programs we recommend:

* [**1Password**](http://agilewebsolutions.com/products/1Password) is a commercial product available for **Mac OS X**, **Microsoft Windows**, **iPhone** and **iPad**.
* [**KeePass**](http://keepass.info/download.html) is available for **Windows**,  but it is *not* cross-platform.

# 2. Download and install KeePassX





## 2.1 Download KeePassX

**Step 1**. **Go** to the [KeePassX Website](https://www.keepassx.org). To ensure you are at the secure *https* version of the site, click [here](https://www.keepassx.org) or manually enter the full address https://www.keepassx.org manually.

**Step 2**. **Click** the *Downloads* link in the menu on the left side of the page.

![](/sites/securityinabox.org/files/media/keepassx-osx-en-001-gotokeepassx.png)

*Figure 1: KeePassX home page*

**Step 3**. **Click** on the *MacOS X Binary Package* link to download **KeePassX**. 

![](/sites/securityinabox.org/files/media/keepassx-osx-en-002-download.png)

*Figure 2: KeePassX downloads page*

**Step 4**. **Save** it to your *Downloads* folder.

![](/sites/siabnext.ttc.io/files/media/keepassx-osx-en-003-savefile.png)

*Figure 3: Saving the KeePassX .dmg file*


## 2.2 Install KeePass X

**Step 1**. In the *Finder window*, find the downloaded file and **double click** to mount it as a disk image. It will show up under *Devices* in the sidebar of the *Finder* window.

![](/sites/siabnext.ttc.io/files/media/keepassx-osx-en-004-dblclick.png)

*Figure 1: Locating the downloaded KeePassX .dmg file*

**Step 2**. In this guide, we'll be installing **KeePassX** in the *Applications folder* of the desktop. But remember that you can also install and use it on portable media, such as a USB flash memory stick or external disk drive. If you choose install it on a USB flash memory stick, you will be able to launch the application using other computers with compatible operating systems. (Since it is a cross-platform tool, you can also save a version of **KeePassX** for each operating system on your USB drive along with your personal database, enabling you to open and use your database on any other computer.) 

Using the example in this guide, please drag the **KeePassX** icon into the *Applications folder*.

![](/sites/siabnext.ttc.io/files/media/keepassx-osx-en-006-install.png)

*Figure 2: Dragging the KeePassX app into Applications*

**Step 3**. Before we start using **KeePassX**, we should **unmount** (or **'eject'**) the **KeePassX** disk image. Find *KeePassX-0.4.3* under *Devices* in the *Finder sidebar*. **Click** on the {**eject**} icon next to it in the sidebar to **unmount** the disk image.

![](/sites/siabnext.ttc.io/files/media/keepassx-osx-en-007-eject.png)

*Figure 3: Unmounting (or ejecting) the KeePassX disk image*

# 3. Create and save a new KeePassX database





## 3.1 Create a new KeePassX database

**Step 1**. In the **KeePassX** menu, **select** *File*, then *New Database*.

![](/sites/siabnext.ttc.io/files/media/keepassx-osx-en-010-newdb.png)

*Figure 1: Selecting New Database in the KeePassX menu*

**Step 2**. **Choose** a strong and memorable *master passphrase*, then **enter** it.

It is very important that your *master passphrase* be unique, long, complex, and difficult to guess. Unfortunately, it must also be memorable. (After all, you can't keep your **KeePassX** *master passphrase* inside **KeePassX**, and writing it down defeats the purpose of using an encrypted password database.) If you forget it, however, you will lose access to everything in your database. So, take your time and come up with a good one! If you need help, refer to the tactics guide [Create and maintain secure passwords](../passwords).

![](/sites/siabnext.ttc.io/files/media/keepassx-osx-en-011-masterpw.png)

*Figure 2: Setting a master passphrase for a new database*

**Step 3**. (*Optional*) If you want to see the *master passphrase* you have chosen and entered, you can **click** the {‘eye' button} to the right of the entry field. (Be aware of your current circumstances, however. An untrusted person nearby may see your exposed *master passphrase*!) To re-hide your *master password*, **click** the {'eye' button} again.

![](/sites/siabnext.ttc.io/files/media/keepassx-osx-en-012-revealpw.png)

*Figure 3: Revealing your password using the ‘eye’ button*

**Step 4**. **Click** {OK} to proceed.

**Step 5**. **Enter** your chosen *master passphrase* a second time to make sure you got it right. **Click** {OK}.

![](/sites/siabnext.ttc.io/files/media/keepassx-osx-en-013-repeatpw.png)

*Figure 4: The password re-entry window*

**Step 6**. (*Optional*) If the two entries don't match, **click** {Back} and **re-enter** your password, then follow steps 3 through 5.

## 3.2 Save your new KeePassX database

Congratulations, you have *almost* created a new **KeePassX** database. Now you must name and save it, just like you would any other electronic document. Otherwise, your database and any entries you create in it will be lost. (You can tell that a new database is unnamed and unsaved by seeing *“\[new\]“* in the top title bar.)

![](/sites/siabnext.ttc.io/files/media/keepassx-osx-en-014-newdbunsaved.png)

*Figure 1: A new unnamed, unsaved database*

**Step 1**. In the **KeePassX** menu, **select File > Save Database As**.

![](/sites/securityinabox.org/files/media/keepassx-osx-en-015-savedbas.png)

*Figure 2: Selecting Save Database in the KeePassX menu*

**Step 2**. In this example, we’ll **save** our **KeePassX** database in *Documents*, but you can put it anywhere. 

**Tip**. If you store it on a USB flash memory stick, along with a copy of the **KeePassX** application, you will be able to access and use your database using other computers.

We’ll also **name** our database *passwords.kdb* in this example, but you can name it anything you like. 

**Tip**. If you are worried that someone with access to your computer might see this file and demand that you tell them your master passphrase, you should probably come up with a less conspicuous name.

**Type in a name** for your **KeePassX** database and {click} *Save*.

![](/sites/securityinabox.org/files/media/keepassx-osx-en-016-saveas.png)

*Figure 3: The ‘Save Database As’ window*

**Note**: The database no longer has *“\[new\]“* in the top title bar. This has been replaced by the path to your new database, ending with the name you gave it. This means your database has been saved.

![](/sites/securityinabox.org/files/media/keepassx-osx-en-017-saved.png)

*Figure 4: A saved database with a name*

**Step 3**. Now that you have saved your **KeePassX** database, let’s be sure you can find and re-open it using your *master passphrase* before we start adding new password entries to it.

There are three ways to close your database:
You can **click** the {red button} in the top left corner of the database to close it.

In the **KeePassX** menu, you can **select** *File*, then *Close Database*.

![](/sites/securityinabox.org/files/media/keepassx-osx-en-018-closedb.png)

*Figure 5: Selecting Close Database in the KeePassX menu*

Or you can use the *Close Database* shortcut key combination: **Command-W**. (The *Command keys* have this symbol: (![](/sites/siabnext.ttc.io/files/media/osx-command-icon.png)).

**Step 4**. Now let’s find and re-open your new **KeePassX** database with your *master password*. 

**Find** your database in the *Documents* folder (or wherever you chose to save it). **Open** it up by either **double-clicking** the file, or by **selecting the file** and using the shortcut key combination **Command-O**.

**Tip:** If your *Finder Preferences* (*Finder Preferences > Advanced*) are set to *‘Show all filename extensions’*, your database will have a *‘.kdb’* filename extension. In this example, it will show up in your *Documents* file as *passwords.kdb*. 

![](/sites/securityinabox.org/files/media/keepassx-osx-en-019-opendb.png)

*Figure 6: Locating the KeePassX database named ‘passwords’ in Documents*

Congratulations! You are now ready to start using your new **KeePassX** database! 

**Tip**: If you were unable to open your database because you forgot the *master password*, there is no way to open your data base, and there is no way to reset or retrieve your *master password*. If you are unable to remember it, you can create a new database and delete the first one.


# 4. Creating and Managing Password Entries





## 4.1 Create a new entry

**Step 1**. The *New Entry* screen lets you add account information, passwords and other important details into your newly created database. In the example that follows, we will create an entry in which to store your password for the **RiseUp** email service.

In the **KeePassX** menu, **select** *Entries*, then *Add New Entry*. Or you can use the *Add New Entry* shortcut key combination: **Command-Y**.

![](/sites/securityinabox.org/files/media/keepassx-osx-en-020-addnewentry.png)

*Figure 1: Selecting ‘Add New Entry’ in the KeePassX Entries menu*

**Step 2**. Learn about the various elements in a **KeePassX** entry.

The **Add Entry** window presents you with a number of fields to be completed. None of these fields are mandatory; information submitted here is largely for your own convenience. 

![](/sites/securityinabox.org/files/media/keepassx-osx-en-021-newentry.png)

*Figure 2: The New Entry window in KeePassX*

A brief explanation of the text fields and elements in a **KeePassX** entry is presented as follows:
- **Group**: **KeePassX** lets you sort your passwords into pre-defined groups. For example: *'Internet'* would be a good place to store passwords that relate to website accounts. **Click** on the drop-down menu to choose a group.
- **Icon**: The icon that will be associated with this account entry. If you **click** on the icon button, you can see the icons available in the *Icon Selection* window. You also have the option to add a custom icon by clicking on the *’Add Custom Icon’* button in the bottom left of the *Icon Selection* window. To select one of the **KeePassX** icons available, **click** the *Pick* button in the bottom right of the window.

![](/sites/securityinabox.org/files/media/keepassx-osx-en-022-iconselection.png)

*Figure 3: The Icon Selection window*

- **Title**: A name to describe the particular password entry. For example: *‘Gmail password’*.
- **Username**: The user name associated with the password entry. For example: *‘securitybox@gmail.com’*.
- **URL**: The website associated with the password entry. For example: *‘https://mail.google.com'*.
- **Password**: This field has two options: the ability to enter a password that you have created, or the option of generating a new password using the *Password Generator*, which is the button with the eye symbol to the right of the password text field. Generating a random password on request using the *Password Generator* will be described in the following section. If you are creating an entry for an account that already exists, you will want to enter the correct password here.
- **Repeat** \[**Password**]\: The confirmation of the password.
- **Quality**: A progress bar that measures password strength in *bits* according to length and randomness. The fuller the quality bar becomes (and the more bits there are), the stronger your chosen password is.
- **Comment**: Here is where you type in descriptive or general information about the account or site for which you are storing information. For example: *Mail server settings: POP3 SSL, pop.gmail.com, Port 995; SMTP TLS, smtp.gmail.com, Port: 465*. Or *Security Question and Answer: Q: Where were you born? A: Jupiter.* Your Comments will be encrypted, along with your passwords, when you close the database. **While it is open, however, your notes may be visible to anyone who can see your screen.**
- **Expires**: **KeePassX** can remind you to change your password after a certain length of time. If you want to set an expiration date, click the "clock" button to specify an expiry date. By doing this, you can add a reminder for yourself to change the password at a specific time (every 3 months,	for example). 
- **Attachment**: Any file related to this account entry that you want to keep secure and associated with the entry. **KeePassX** will encrypt this file when you close your database. Click the first button to the right of the Attachment field to add a file. Examples of attached files could include a list of confidential contacts for that account, or confidential financial information.

**Note**: Creating or modifying the password entries in **KeePass** does not change your actual passwords! Think of **KeePass** as a secure electronic address book for your passwords. It only stores what you write in it, nothing more.

**Step 3**: Create a new **KeePassX** entry for your **RiseUp** account within the *Internet* Group in your **KeePassX** database. Select *Internet* from the *Group* dropdown menu. Then enter the account information for your **RiseUp** account.

Your entry will resemble the following:

![](/sites/securityinabox.org/files/media/keepassx-osx-en-023-unsavedriseupentry.png)

*Figure 4: New Entry screen in KeePassX with unsaved account information*

**Note**: **If you’d like to generate a new random password for this entry using KeePassX’s *Password Generator*, scroll down to section 4.2 before saving your entry in Step 4 below.**

**Step 4**: **Click** {OK} to save your changes to the *Add Entry* screen.

*Your* RiseUp *password entry now appears in the* Internet *group.* 

![](/sites/securityinabox.org/files/media/keepassx-osx-en-024-dbwithentry.png)

*Figure 5: The KeePassX database window*

**Note**: The bottom panel of the database window displays information about the entry selected. This includes creation, editing, expiry date, and any comments you may have recorded in the entry. It does not reveal the username or the password. If an entry has expired, it will *only* show up in this bottom panel with **[Expired]** (denoted by the red arrow in the figure below).

![](/sites/securityinabox.org/files/media/keepassx-osx-en-025-expired.png)

*Figure 6: An example of an expired key in the database window*


## 4.2 Generating Random Passwords Using the Password Generator

Using long, memorable passphrases *or* generating and using long, random passwords will help keep your accounts secure. Long, random passwords based on mathematical principles cannot simply be 'guessed' by someone who is trying to break into one of your accounts. **KeePassX** supplies a *Password Generator* to help you with this process. This section will describe how to generate one yourself. 

**Step 1**. **Access** the *Password Generator* using one of four options:

**Options 1 & 2**: The *Password Generator* can be activated from within the *Add Entry* and *Edit/View Entry* windows by **clicking** the *’Gen’* button to the right of the *Repeat* password text field.

![](/sites/securityinabox.org/files/media/keepassx-osx-en-031-entryex.png)

*Figure 1: A KeePassX entry accessed using the Edit/View Entry option*

**Options 3 & 4**: Alternatively, you can also access it via the **KeePassX** menu by **clicking on** *Extras*, then **selecting** *Password Generator*. Or you can use the *Password Generator* shortcut key combination: **Command-P**.

![](/sites/securityinabox.org/files/media/keepassx-osx-en-033-pwgentopmenu.png)

*Figure 2: Accessing the Password Generator using the Edit/View Entry option*

![](/sites/securityinabox.org/files/media/keepassx-osx-en-034-pwgen.png)

*Figure 3: The KeePassX Random Password Generator*

The *Password Generator* presents a variety of options for generating a password. We’ll be using its *Random Password Generator* in this example. You can specify the length of the desired password, the types of characters from which it will be created (such as numbers, special characters, uppercase and lowercase letters), and much more. For our purposes, we can use the default options presented. This means that the generated password will be 25 characters long and made up of lower and upper case letters, numbers, and special characters.

**Step 2**. **Click** the *Generate* button to create a randomly generated password. When complete, **KeePassX** will present the generated password to you in the *New Password* text field, but it will be hidden. (The only exception to this is if you accessed the stand-alone *Password Generator* using *Options 3 & 4* above. In this case, you’ll have to copy and paste the new password in manually.) 

In most cases, long, randomly generated passwords *aren’t* memorable. But with **KeePassX**, you can generate, securely store, and use these strong passwords for your accounts to keep them safe. Therefore, in most cases, you’ll never need to even look at long, randomly generated passwords like this! (But you will need to copy and paste these passwords into your various accounts, which we’ll cover in section XX below.) In the image below, the new randomly generated password is revealed in order to illustrate the tool:

![](/sites/securityinabox.org/files/media/keepassx-osx-en-035-pwgenexposedpw.png)

*Figure 4: An exposed password in the KeePassX Random Password Generator*

**Note**: You can view the generated password by **clicking** the *’Eye’* button to the right of the *New Password* text field. But be aware that this may create a security risk if others can see your new, strong, randomly generated password!

**Step 3**. **Click** *OK* to accept the password and return to the *Add Entry* screen as follows. Your new randomly generated password will now be added into your **KeePassX** entry for you. (If you had another password before generating this new password, it will be replaced by the new password you’ve just created using the *Password Generator*.) In the image below, the password text field has been revealed in order to illustrate this.

![](/sites/securityinabox.org/files/media/keepassx-osx-en-036-newpwaddedtoentry.png)

*Figure 5: KeePassX Entry with revealed password copied over from the Password Generator*

**Step 4**. **Click** *OK* to save the *KeePassX* entry.

## 4.3 Edit an existing entry

You may edit an existing entry in **KeePassX** at any time. You can change your password or modify other details stored in the password entry. It is generally considered good security practice to change a password every three to six months (remembering to also update it on your email system and elsewhere as well).

To edit an entry, perform the following steps:

**Step 1**. First, **Select** the *’Internet’ Group* in the database menu on the left side of the window to see the entries associated with it.

![](/sites/securityinabox.org/files/media/keepassx-osx-en-026-selectgroup.png)

*Figure 1: Choosing a group in the main KeePassX database window*

**Step 2**. In this example, we’ll use the **Riseup** account entry we created in Step 4.1 above. Within the *’Internet’ Group*, **Select** the **Riseup** entry we created by **clicking** it within the list of entries inside the *’Internet’ Group* (at the moment, it’s the only entry in your new **KeePassX** database, but eventually your database will have many entries within each group).

![](/sites/securityinabox.org/files/media/keepassx-osx-en-027-selectentry.png)

*Figure 1: Selecting an KeePassX entry in the main KeePassX database window*

**Step 3**. There are three ways to open up the entry in order to edit it. 

**Option 1**. You can ‘right click’ on the selected entry by **holding** down the **Control** key and **clicking** the entry, which activates a menu of options.Then scroll down and **click** on *View/Edit Entry*.

![](/sites/securityinabox.org/files/media/keepassx-osx-en-028-rightclickmenu.png)

*Figure 2: The ‘right click’ menu for a KeePassX entry*

**Option 2**. In the **KeePassX** menu, **select** *Entries*, then *New Database*.

![](/sites/securityinabox.org/files/media/keepassx-osx-en-029-topmenuviewedit.png)

*Figure 3: Selecting ‘View/Edit Entry’ from the KeePassX menu*

**Option 3**. Use the *View/Edit Entry* shortcut key combination: **Command-E**. 

**Step 4**. With an open entry, you can add new information or edit any existing information, including the password. (In this example, we’ll add some additional information to the **Comment** field.) To save your changes, **click** {OK}.

![](/sites/securityinabox.org/files/media/keepassx-osx-en-030-saveentry.png)

*Figure 4: Saving edits to a KeePassX entry*

**Note**: Remember that making changes to a **KeePassX** entry *only* updates that entry in your **KeePassX** database. It does not automatically update corresponding information elsewhere, such as a new password for an online account, or the same **KeePassX** entry in any copies or backups of your **KeePassX** database that you have saved elsewhere. Therefore, you will need to make any relevant updates to your account information, as well as new **KeePassX** database backups and copies seperately after editing your entry here.

# 5. Using your entries in KeePassX

One of the best features of **KeePassX** is that it safely stores long, strong passwords for you so you *don’t* have to memorize them or reuse passwords for multiple accounts (which is risky). **KeePassX** lets you copy your usernames and passwords from the database and paste them into your accounts. For greater security, a copied password will only remain in your digital clipboard for about 10 seconds, so it will save time to have your account or website already open and running, so that you can paste the relevant usernames and passwords there as required.

## 5.1 Sign into an account using KeePassX

In this example, we’ll sign into our **RiseUp** email account by copying and pasting our password from our new **KeePassX** entry. Remember that you can also copy and paste your User Name and other information from your **KeePassX** entries as well!

**Step 1**. In the main **KeePassX** database, **select** the Group where your **RiseUp** Entry is stored. (In our example, this is the *Internet* Group.) 

**Step 2**. There are three ways to copy the password from a **KeePassX** Entry to the clipboard. 

**Option 1**. **Right click** (**Command and click** in **Mac OS X**) on the required password entry to activate a drop-down list of menu options. Scroll down and click on *Copy Password to Clipboard*.

![](/sites/securityinabox.org/files/media/keepassx-osx-en-037-rclickcopypw.png)

*Figure 4: Copying an entry’s password using the right-click menu in the main **KeePassX** database window*

**Option 2**. As you saw in the **right click** menu above, the *Copy Password to Clipboard* shortcut key combination is the customary one used for copying: **Command-C**. 

**Option 3**. Finally, you can use the main **KeePassX** menu by **clicking** on *Entries*, then scrolling down to **select** *Copy Password to Clipboard*.

![](/sites/securityinabox.org/files/media/keepassx-osx-en-038-topmenucopypw.png)

*Figure 5: Copying an entry’s password using the main KeePassX menu*

**Step 3**. Go to the related account or site and **paste** the password into the appropriate field:

![](/sites/securityinabox.org/files/media/keepassx-osx-en-039-pastepw.png)

*Figure 6: A RiseUp Email Account displaying a pasted password*

**Tip**: For efficient copying, pasting and switching windows, use the keyboard shortcuts. **Press and hold** the *Command* key, then press *C* to copy a password. **Press and hold** the *Ctrl* key, then press *V* to paste that password. You can also **Press and hold** the *Command* key, then **press** the *tab* key to switch between open programs and windows.

**Note**: By using **KeePass** all the time, you never actually have to see or know what your password is. The copy/paste functions take care of moving it from the database to the required window. If you use the *Password Generator* feature and transfer your newly generated password using using the copy/paste functions when you register for new accounts, you will be using a password that you have never seen in plain view. And it still works!

# 6. Manage your KeePassX database





## 6.1 Locking, Minimizing, and Closing KeePassX

**KeePassX** is designed to lock your database for safety reasons, so unauthorized users won’t gain access to the sensitive information inside. When the **KeePassX** database is locked, you will be prompted to enter your *Master Password* in order to unlock and access it again. 

By default, **KeePassX** databases will lock after 600 seconds of inactivity. You also have the option to have your database lock whenever you minimize it, but this is not the default setting in **KeePassX**. 

**Optional**: You can change these options (and many others) in the **KeePassX** *Settings*. You can access the settings in the main **KeePassX** menu by **clicking** on *KeePassX*, then scrolling down to **select** *Preferences*. Or you can use the *Preferences* shortcut key combination: **Command-,**. 

To access the database lock options within *Settings*, **select** *Security* in the left-hand list of categories. 

![](/sites/securityinabox.org/files/media/keepassx-osx-en-040-securitysettings.png)

*Figure 1: KeePassX Security Settings window*

**Step 1**. **KeePass** also lets you lock the program manually. Practice locking and unlocking your **KeePassX** database using one of the options available. You can **click** on *File*, then scroll down to **select** *Lock Workspace*. Or you can use the *Lock Workspace* shortcut key combination: **Command-L**. 

After you’ve locked your **KeePassX** database, it will display two options: *Unlock* (to unlock the database), and *Close Database* (which will require you to open the database again).

![](/sites/securityinabox.org/files/media/keepassx-osx-en-041-lockeddb.png)

*Figure 2: Locked KeePassX database (or ‘workspace’)*

## 6.2 Backup your KeePassX Database

The **KeePass** database file on your computer is denoted by its .kdb file extension. You can put both that database and the **KeePassX** program on a USB memory stick and carry it with you. You can also make multiple copies of your database as backup copies to access from different devices, portable media, or the cloud. Since the database is protected by a *master password* that you create, no one else will be able to open the database without it.

**Step 1**. To make a backup or second copy of your database, **click** *File* in the main **KeePassX** menu, then scroll down to **select** *Save As*. This will allow you to name and save a copy of the database. 

**Tip**. **KeePassX** does not automatically update all copies of a database when changes are made. You have to do this manually. It’s a good habit to regularly replace backup copies of your **KeePassX** database. That way you won’t lose any edits or new entries if you lose your main database!

## 6.3 Resetting your Master Passphrase

You can change the *Master Password* at any time. This can be done once you have opened the password database.

**Step 1**. In the main **KeePassX** menu, **Select** *File*, then scroll down to select *Change Master Key*.

![](/sites/securityinabox.org/files/media/keepassx-osx-en-042-changemasterkey.png)

*Figure 1: The Change Master Key screen in KeePassX*

**Step 2**. **Type** in the new *Master Password* twice when prompted to do so.

# FAQ

**KeePassX** is a very easy program to use. The important part is getting into the habit of creating new passwords in **KeePassX**. It may be difficult to get used to the fact that you never have to see a password again, but it is definitely easier than having to remember them!

***Q***: On the outside chance that I forget my master password, is there anything I can do to access **KeePassX** and retrieve my password databases?

***A***: No. There is nothing you can do in that situation. On the bright side, at least no one else will be able to access your password database! To prevent this from happening, you could use some of the methods for remembering a password or passphrase that are described in the [**Create and maintain strong passwords**](../passwords) guide.

***Q***: And if I uninstall **KeePassX**, what will happen to my passwords?

***A***: The program will be deleted from your computer, but your database (stored in a .kdb file) will remain. You can open this file at any time in the future if you install **KeePassX** again.

***Q***: I think I accidentally deleted the database file!

***A***: Hopefully, you made a backup beforehand. Also, make sure you haven't simply forgotten where you stored the file in the first place. Search your computer for a file with a .kdb extension. If you really have deleted it, you may be able to use recovery software to recover the file.