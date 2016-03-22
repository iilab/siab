

---

lang: en
community: guide
type: tools
os: linux
weight: 019
title: KeePassX for Linux - Secure password manager

---

KeePassX is an easy-to-use, cross-platform, [**free and open source (FOSS)**](/en/glossary#FOSS) password manager that allows you to store and manage all of your passwords in one secure, portable database.

# Required reading


:[Create and maintain secure passwords](../../../tactics/passwords)


:[KeePassX for Linux - Secure password manager](keepassx-for-linux-secure-password-manager)

# What you will get from this guide

- The ability to save all your passwords in one convenient and secure database
- The ability to create and store many strong passwords without having to remember them

# 1. Introduction to KeePassX

**KeePassX** is an easy-to-use tool that helps you store and manage your various passphrases inside an encrypted database file. This file is encrypted to a *master passphrase* that you create. **KeePassX** can also generate strong passphrases for your other accounts. 

You can also make copies of your database, which is convenient for backup purposes. However, we do not recommend sending your database by email or storing in online where it can be accessed by others. It *is* encrypted, but it contains so much sensitive information that you should be careful with it nonetheless.

In the sections that follow, you will learn how to:

* Set a *master passphrase*
* Save your newly created password database
* Generate a random password for a particular service
* Extract passwords from **KeePassX** when you need them 
* Change your *master passphrase*

## 1.0 Things you should know about KeePassX before you start

If you use **KeePassX** consistently for a particular account, you do not need to remember that passphrase. In fact, you never even need to *see* it. You can simply copy it from KeePassX and paste it into the login screen. (KeePassX will wipe it from your clipboard memory when you're done.) And, if you use KeePassX to generate random passphrases, they are likely to be much stronger than the ones we come up with ourselves. 

## 1.1 Other tools like KeePassX

**KeePassX** is cross-platform, which means it is available for **GNU Linux**, **Windows** and **Mac OS X**. However, if you wish to try other similar programs we recommend:

* [**1Password**](http://agilewebsolutions.com/products/1Password): a commercial product available for **Mac OS X**, **Microsoft Windows**, **iPhone** and **iPad**.
* [**KeePass**](http://keepass.info/download.html): available for Linux (installable via software centre).

# 2. How to install KeePassX

We recommend downloading and installing KeePassX through your system's software centre through the following steps below:

**Step 1.** Open your system's software center and search for "**KeePassX**". 

![](/sites/securityinabox.org/files/media/keepass-lin-en-v01-201.png)

*Figure 1:* KeePassX in Ubuntu's Software Center

**Step 2.** Click on **"Install"** next to "KeePassX" to install KeePassX on your system. 

**Step 3.** Type the passphrase that you use to log in to your computer. The installation should not take longer than a few minutes. 

![](/sites/securityinabox.org/files/media/keepass-lin-en-v01-202.png)

*Figure 2:* Installation of KeePassX

KeePassX is now installed on your Linux system. 

![](/sites/securityinabox.org/files/media/keepass-lin-en-v01-203.png)

*Figure 3:* KeePassX installed on Ubuntu

# 3. How to create and save a new KeePassX database





## 3.1. How to create a new KeePassX database

**Step 1**. In the **KeePassX** menu, **select** *File*, then *New Database*.

![](/sites/securityinabox.org/files/media/keepass-lin-en-v01-204.png)

*Figure 1: Selecting New Database in the KeePassX menu* 

**Step 2**. **Choose** a strong and memorable *master passphrase*, then **enter** it.

A master passphrase is a password/passphrase which protects all of the other passwords/passphrases that are stored in your KeePassX database. It is very important that your *master passphrase* is unique, long, complex, and difficult to guess. Unfortunately, it must also be memorable. (After all, you can't keep your **KeePassX** *master passphrase* inside **KeePassX**, and writing it down defeats the purpose of using an encrypted password database.) If you forget it, however, you will lose access to everything in your database. So, take your time and come up with a strong and memorable one! If you need help, refer to the tactics guide [Create and maintain secure passwords](../passwords).

![](/sites/securityinabox.org/files/media/keepass-lin-en-v01-205.png)

*Figure 2: Setting a master passphrase for a new database*

**Step 3**. (*Optional*) If you want to see the *master passphrase* you have chosen and entered, you can **click** the {‘eye' button} to the right of the entry field. (Be aware of your current circumstances, however. An untrusted person nearby may see your exposed *master passphrase*!) To re-hide your *master password*, **click** the {'eye' button} again.

![](/sites/securityinabox.org/files/media/keepass-lin-en-v01-206.png)

*Figure 3: Typing in your password*

**Step 4**. **Click** {OK} to proceed.

**Step 5**. **Enter** your chosen *master passphrase* a second time to make sure you got it right. **Click** {OK}.

![](/sites/securityinabox.org/files/media/keepass-lin-en-v01-207.png)

*Figure 4: The password re-entry window*

**Step 6**. (*Optional*) If the two entries don't match, **click** {Back} and **re-enter** your password, then follow steps 3 through 5.

## 3.2. How to save your new KeePassX database

Congratulations, you have *almost* created a new **KeePassX** database. Now you must name and save it, just like you would any other electronic document. Otherwise, your database and any entries you create in it will be lost. (You can tell that a new database is unnamed and unsaved by seeing *“\[new\]“* in the top title bar.)

![](/sites/securityinabox.org/files/media/keepass-lin-en-v01-208.png)

*Figure 1: A new unnamed, unsaved database* 

**Step 1**. In the **KeePassX** menu, **select File > Save Database As**.

![](/sites/securityinabox.org/files/media/keepass-lin-en-v01-209.png)

*Figure 2: Selecting Save Database in the KeePassX menu*

**Step 2**. In this example, we’ll **save** our **KeePassX** database in *Documents*, but you can put it anywhere. 

**Tip**. If you store it on a USB flash memory stick, along with a copy of the **KeePassX** application, you will be able to access and use your database using other computers.

We’ll also **name** our database *passwords.kdb* in this example, but you can name it anything you like. 

**Tip**. If you are worried that someone with access to your computer might see this file and demand that you tell them your master passphrase, you should probably come up with a less conspicuous name.

**Type in a name** for your **KeePassX** database and click *"Save"*.

![](/sites/securityinabox.org/files/media/keepass-lin-en-v01-210.png)

*Figure 3: The ‘Save Database As’ window* 

**Note**: The database no longer has *“\[new\]“* in the top title bar. This has been replaced by the path to your new database, ending with the name you gave it. This means your database has been saved.

**Step 3**. Now that you have saved your **KeePassX** database, let’s be sure you can find and re-open it using your *master passphrase* before we start adding new password entries to it.

There are two ways to close your database:

You can **click** the {red button} in the top left corner of the database to close it.

In the **KeePassX** menu, you can **select** *File*, then *Close Database*.

![](/sites/securityinabox.org/files/media/keepass-lin-en-v01-211.png)

*Figure 4: Selecting Close Database in the KeePassX menu*

**Step 4**. Now let’s find and re-open your new **KeePassX** database with your *master password*. 

**Find** your database in the *Documents* folder (or wherever you chose to save it). **Open** it up by either **double-clicking** the file, or by **selecting the file** and using the shortcut key combination **ctrl+o**.

**Tip:** If your *Finder Preferences* (*Finder Preferences > Advanced*) are set to *‘Show all filename extensions’*, your database will have a *‘.kdb’* filename extension. In this example, it will show up in your *Documents* file as *passwords.kdb*. 

![](/sites/securityinabox.org/files/media/keepass-lin-en-v01-212.png)

*Figure 5: Locating the KeePassX database named ‘passwords’ in Documents*

Congratulations! You are now ready to start using your new **KeePassX** database! 

**Tip**: If you were unable to open your database because you forgot the *master password*, there is no way to open your data base, and there is no way to reset or retrieve your *master password*. If you are unable to remember it, you can create a new database and delete the first one.

# 4. How to create and manage password entries





## 4.1. How to create a new password entry

**Step 1**. The *New Entry* screen lets you add account information, passwords and other important details into your newly created database. In the example that follows, we will create an entry in which to store your password for an email service.

In the **KeePassX** menu, **select** *Entries*, then *Add New Entry*. Or you can use the *Add New Entry* shortcut key combination: **ctrl+y**.

![](/sites/securityinabox.org/files/media/keepass-lin-en-v01-213.png)

*Figure 1: Selecting ‘Add New Entry’ in the KeePassX Entries menu*

**Step 2**. Learn about the various elements in a **KeePassX** entry.

The **Add Entry** window presents you with a number of fields to be completed. None of these fields are mandatory; information submitted here is largely for your own convenience. 

![](/sites/securityinabox.org/files/media/keepass-lin-en-v01-214.png)

*Figure 2: The New Entry window in KeePassX*

A brief explanation of the text fields and elements in a **KeePassX** entry is presented as follows:

- **Group**: **KeePassX** lets you sort your passwords into pre-defined groups. For example: *'Internet'* would be a good place to store passwords that relate to website accounts. **Click** on the drop-down menu to choose a group.

- **Icon**: The icon that will be associated with this account entry. If you **click** on the icon button, you can see the icons available in the *Icon Selection* window. You also have the option to add a custom icon by clicking on the *’Add Custom Icon’* button in the bottom left of the *Icon Selection* window. To select one of the
**KeePassX** icons available, **click** the *Pick* button in the top right corner of the window.

![](/sites/securityinabox.org/files/media/keepass-lin-en-v01-215.png)

*Figure 3: The Icon Selection window*

- **Title**: A name to describe the particular password entry. For example: *‘Gmail password’*.
- **Username**: The user name associated with the password entry. For example: *‘securitybox@gmail.com’*.
- **URL**: The website associated with the password entry. For example: *‘https://mail.google.com'*.
- **Password**: This field has two options: the ability to enter a password that you have created, or the option of generating a new password using the *Password Generator* through the "gen" button. Generating a random password on request using the *Password Generator* will be described in the following section. If you are creating an entry for an account that already exists, you will want to enter the correct password here.
- **Repeat** \[**Password**]\: The confirmation of the password.
- **Quality**: A progress bar that measures password strength in *bits* according to length and randomness. The fuller the quality bar becomes (and the more bits there are), the stronger your chosen password is.
- **Comment**: Here is where you type in descriptive or general information about the account or site for which you are storing information. For example: *Mail server settings: POP3 SSL, pop.gmail.com, Port 995; SMTP TLS, smtp.gmail.com, Port: 465*. Or *Security Question and Answer: Q: Where were you born? A: Jupiter.* Your Comments will be encrypted, along with your passwords, when you close the database. **While it is open, however, your notes may be visible to anyone who can see your screen.**
- **Expires**: **KeePassX** can remind you to change your password after a certain length of time. If you want to set an expiration date, click the "clock" button to specify an expiry date. By doing this, you can add a reminder for yourself to change the password at a specific time (every 3 months,	for example). 
- **Attachment**: Any file related to this account entry that you want to keep secure and associated with the entry. **KeePassX** will encrypt this file when you close your database. Click the first button to the right of the Attachment field to add a file. Examples of attached files could include a list of confidential contacts for that account, or confidential financial information.

**Note**: Creating or modifying the password entries in **KeePass** does not change the passwords on your actual account! Think of **KeePass** as a secure electronic address book for your passwords. It only stores what you write in it, nothing more.

**Step 3**: Create a new **KeePassX** entry for your email account within the *Internet* Group in your **KeePassX** database. Select *Internet* from the *Group* dropdown menu. Then enter the account information for your email account.

Your entry will resemble the following:

![](/sites/securityinabox.org/files/media/keepass-lin-en-v01-216.png)

*Figure 4: New Entry screen in KeePassX with unsaved account information*

**Note**: **If you’d like to generate a new random password for this entry using KeePassX’s *Password Generator*, scroll down to section 4.2 before saving your entry in Step 4 below.**

**Step 4**: **Click** {OK} to save your changes to the *Add Entry* screen.

*Your email password entry now appears in the Internet group.* 

![](/sites/securityinabox.org/files/media/keepass-lin-en-v01-217.png)

*Figure 5: The KeePassX database window*

**Note**: The bottom panel of the database window displays information about the entry selected. This includes creation, editing, expiry date, and any comments you may have recorded in the entry. It does not reveal the username or the password. If an entry has expired, it will *only* show up with **[Expired]** denoted by a red arrow.

## 4.2. How to generate random passwords using the password generator

It is possible to create a strong passphrase yourself, but it is difficult. And it is *especially* difficult if you expect your passphrase to be memorable. It is much easier to generate long, complex and *completely random* passwords that are nearly impossible to remember but guaranteed to be strong. **KeePassX** supplies a *Password Generator* to help with this process. If you are willing and able to rely on **KeePassX** *every time you log in to an account*, you should consider adopting this strategy. To do so, follow the steps below.

You can generate a random password while creating a new entry or while editing an existing entry. If you are creating a new entry, skip to **Step 2**, below. To edit an existing entry:

**Step 1**. **Right-click** the desired entry and **select** *View/Edit Entry*

![](/sites/securityinabox.org/files/media/keepass-lin-en-v01-223.png)

*Figure 1: The ‘right click’ menu for a KeePassX entry*

This will display the (incorrectly titled) *New Entry* screen, as shown below:

![](/sites/securityinabox.org/files/media/keepass-lin-en-v01-216.png)

*Figure 2: A KeePassX entry accessed using the Edit/View Entry option*

**Step 2**. 

---


**Options 1 & 2**: The *Password Generator* can be activated from within the *Add Entry* and *Edit/View Entry* windows by **clicking** the *’Gen’* button to the right of the *Repeat* password text field.

**Options 3 & 4**: Alternatively, you can also access it via the **KeePassX** menu by **clicking on** *Extras*, then **selecting** *Password Generator*. Or you can use the *Password Generator* shortcut key combination: **ctrl+p**.

![](/sites/securityinabox.org/files/media/keepass-lin-en-v01-218.png)

*Figure 2: Accessing the Password Generator using the Edit/View Entry option*

![](/sites/securityinabox.org/files/media/keepass-lin-en-v01-219.png)

*Figure 3: The KeePassX Random Password Generator*

The *Password Generator* presents a variety of options for generating a password. We’ll be using its *Random Password Generator* in this example. You can specify the length of the desired password, the types of characters from which it will be created (such as numbers, special characters, uppercase and lowercase letters), and much more. For our purposes, we can use the default options presented. This means that the generated password will be 25 characters long and made up of lower and upper case letters, numbers, and special characters.

**Step 2**. **Click** the *Generate* button to create a randomly generated password. When complete, **KeePassX** will present the generated password to you in the *New Password* text field, but it will be hidden. 

In most cases, long, randomly generated passwords *aren’t* memorable. But with **KeePassX**, you can generate, securely store, and use these strong passwords for your accounts to keep them safe. Therefore, in most cases, you’ll never need to even look at long, randomly generated passwords like this! (But you will need to copy and paste these passwords into your various accounts, which we’ll cover in section XX below.) In the image below, the new randomly generated password is revealed in order to illustrate the tool:

![](/sites/securityinabox.org/files/media/keepass-lin-en-v01-220.png)

*Figure 4: An exposed password in the KeePassX Random Password Generator*

**Note**: You can view the generated password by **clicking** the *’Eye’* button to the right of the *New Password* text field. But be aware that this may create a security risk if others can see your new, strong, randomly generated password!

**Step 3**. **Click** on *OK* to accept the password and return to the *Add Entry* screen. Your new randomly generated password will now be added into your **KeePassX** entry for you. (If you had another password before generating this new password, it will be replaced by the new password you’ve just created using the *Password Generator*.) 

**Step 4**. **Click** on *OK* in your “New Entry” screen to save the *KeePassX* entry.

**Step 5**. Save your KeePassX database. 

## 4.3. How to edit an existing password entry

You may edit an existing entry in **KeePassX** at any time. You can change your password or modify other details stored in the password entry. It is generally considered good security practice to change a password every three to six months (remembering to also update it on your email system and elsewhere as well).

To edit an entry, perform the following steps:

**Step 1**. First, **Select** the *’Internet’ Group* in the database menu on the left side of the window to see the entries associated with it.

![](/sites/securityinabox.org/files/media/keepass-lin-en-v01-221.png)

*Figure 1: Choosing a group in the main KeePassX database window*

**Step 2**. In this example, we’ll use the **Gmail** account entry we created in Step 4.1 above. Within the *’Internet’ Group*, **Select** the **Gmail** entry we created by **clicking** it within the list of entries inside the *’Internet’ Group* (at the moment, it’s the only entry in your new **KeePassX** database, but eventually your database will have many entries within each group).

![](/sites/securityinabox.org/files/media/keepass-lin-en-v01-222.png)

*Figure 2: Selecting an KeePassX entry in the main KeePassX database window*

**Step 3**. There are three ways to open up the entry in order to edit it. 

**Option 1**. You can ‘right click’ on the selected entry which activates a menu of options.Then scroll down and **click** on *View/Edit Entry*.

![](/sites/securityinabox.org/files/media/keepass-lin-en-v01-223.png)

*Figure 3: The ‘right click’ menu for a KeePassX entry*

**Option 2**. In the **KeePassX** menu, **select** *Entries*, then *View/Edit Entry...*.

![](/sites/securityinabox.org/files/media/keepass-lin-en-v01-224.png)

*Figure 4: Selecting ‘View/Edit Entry’ from the KeePassX menu*

**Option 3**. Use the *View/Edit Entry* short cut key combination: **ctrl+E**. 

**Step 4**. With an open entry, you can add new information or edit any existing information, including the password. (In this example, we’ll add some additional information to the **Comment** field.) To save your changes, **click** {OK}.

![](/sites/securityinabox.org/files/media/keepass-lin-en-v01-225.png)

*Figure 5: Saving edits to a KeePassX entry*

**Note**: Remember that making changes to a **KeePassX** entry *only* updates that entry in your **KeePassX** database. It does not automatically update corresponding information elsewhere, such as a new password for an online account, or the same **KeePassX** entry in any copies or backups of your **KeePassX** database that you have saved elsewhere. Therefore, you will need to make any relevant updates to your account information, as well as new **KeePassX** database backups and copies separately after editing your entry here.

# 5. How to use your entries in KeePassX

One of the best features of **KeePassX** is that it safely stores long, strong passwords for you so you *don’t* have to memorize them or reuse passwords for multiple accounts (which is risky). **KeePassX** lets you copy your usernames and passwords from the database and paste them into your accounts. For greater security, a copied password will only remain in your digital clipboard for about 20 seconds, so it will save time to have your account or website already open and running, so that you can paste the relevant usernames and passwords there as required.

## 5.1. How to sign into an account using KeePassX

In this example, we’ll sign into our email account by copying and pasting our password from our new **KeePassX** entry. Remember that you can also copy and paste your User Name and other information from your **KeePassX** entries as well!

**Step 1**. In the main **KeePassX** database, **select** the Group where your email Entry is stored. (In our example, this is the *Internet* Group.) 

**Step 2**. There are three ways to copy the password from a **KeePassX** Entry to the clipboard. 

**Option 1**. **Right click** on the required password entry to activate a drop-down list of menu options. Scroll down and click on *Copy Password to Clipboard*.

![](/sites/securityinabox.org/files/media/keepass-lin-en-v01-501.png)

*Figure 1: Copying an entry’s password using the right-click menu in the main KeePassX database window*

**Option 2**. As you saw in the **right click** menu above, the *Copy Password to Clipboard* shortcut key combination is the customary one used for copying: **ctrl+C**. 

**Option 3**. Finally, you can use the main **KeePassX** menu by **clicking** on *Entries*, then scrolling down to **select** *Copy Password to Clipboard*.

![](/sites/securityinabox.org/files/media/keepass-lin-en-v01-502.png)

*Figure 2: Copying an entry’s password using the main KeePassX menu*

**Step 3**. Go to the related account or site and **paste** the password into the appropriate field:

![](/sites/securityinabox.org/files/media/keepass-lin-en-v01-503.png)

*Figure 3: A Gmail account displaying a pasted password*

**Tip**: For efficient copying, pasting and switching windows, use the keyboard shortcuts. **Press and hold** the conntrol key, then press C to copy a password. Press and hold the Ctrl key, then press V to paste that password. You can also **Press and hold** the alt key, then press the tab key to switch between open programs and windows.

# 6. How to manage your KeePassX database





## 6.1. How to lock and close KeePassX

**KeePassX** is designed to lock your database for safety reasons, so unauthorized users won’t gain access to the sensitive information inside. When the **KeePassX** database is locked, you will be prompted to enter your *Master Password* in order to unlock and access it again. 

**Optional**: You can change these options (and many others) in the **KeePassX** *Settings*. You can access the settings in the main **KeePassX** menu by **clicking** on **Extras**, then scrolling down to select "**Settings...**". 

To access the database lock options within *Settings*, select **Security** in the left-hand list of categories. 

![](/sites/securityinabox.org/files/media/keepass-lin-en-v01-601.png)

*Figure 1: KeePassX Security Settings window*

**KeePass** also lets you lock the program manually. Practice locking and unlocking your **KeePassX** database using one of the options available. You can **click** on *File*, then scroll down to **select** *Lock Workspace*. Or you can use the *Lock Workspace* shortcut key combination: **ctrl-L**. 

After you’ve locked your **KeePassX** database, it will display two options: *Unlock* (to unlock the database), and *Close Database* (which will require you to open the database again).

![](/sites/securityinabox.org/files/media/keepass-lin-en-v01-602.png)

*Figure 2: Locked KeePassX database (or ‘workspace’)*

## 6.2. How to back-up your KeePassX database

The **KeePass** database file on your computer is denoted by its .kdb file extension. You can put both that database and the **KeePassX** program on a USB memory stick and carry it with you. You can also make multiple copies of your database as backup copies to access from different devices, portable media, or the cloud. Since the database is protected by a *master password* that you create, no one else will be able to open the database without it.

**Step 1**. To make a backup or second copy of your database, click on **File** in the main **KeePassX** menu, then scroll down to select **Save Database As...**. This will allow you to name and save a copy of the database. 

**Tip**. **KeePassX** does not automatically update all copies of a database when changes are made. You have to do this manually. It’s a good habit to regularly replace backup copies of your **KeePassX** database. That way you won’t lose any edits or new entries if you lose your main database!

## 6.3. How to reset your Master passphrase

You can change the *Master Password* at any time. This can be done once you have opened the password database.

**Step 1**. In the main **KeePassX** menu, select **File**, then scroll down to select **Change Master Key**.

 ![](/sites/securityinabox.org/files/media/keepass-lin-en-v01-603.png)

*Figure 1: The Change Master Key screen in KeePassX*

**Step 2**. **Type** in the new *Master Password* twice when prompted to do so.

# FAQ

**KeePassX** is a very easy program to use. The important part is getting into the habit of creating new passwords in **KeePassX**. It may be difficult to get used to the fact that you never have to see a password again, but it is definitely easier than having to remember them!

***Q***: On the outside chance that I forget my master password, is there anything I can do to access **KeePassX** and retrieve my password databases?

***A***: No. There is nothing you can do in that situation. To prevent this from happening, you could use some of the methods for remembering a password or passphrase that are described in the [**Create and maintain strong passwords**](../passwords) guide.

***Q***: And if I uninstall **KeePassX**, what will happen to my passwords?

***A***: The program will be deleted from your computer, but your database (stored in a .kdb file) will remain. You can open this file at any time in the future if you install **KeePassX** again.

***Q***: I think I accidentally deleted the database file!

***A***: Hopefully, you made a backup beforehand. Also, make sure you haven't simply forgotten where you stored the file in the first place. Search your computer for a file with a .kdb extension. If you really have deleted it, you may be able to use recovery software to recover the file.