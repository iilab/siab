

---

lang: xx
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: How to Install Thunderbird

---

List of sections on this page:

- [**2.0 How to Install Thunderbird**](#2.0)
- [**2.1 How to Setup an Email Account in Thunderbird**](#2.1)

<a name="2.0"></a>
## 2.0 How to Install Thunderbird ##

To begin installing **Thunderbird**, perform the following steps:

**Step 1**. **Double click** ![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-092.png); it will first need to extract the software from the download

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-002.png)

*Figure 1: The Extracting status progress bar*

Afterwards, a **User Account Control** security warning dialog box may appear. 

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-003.png)

*Figure 2: Installation warning dialog*

If it does, **click** **Yes** to begin the installation wizard.

The *Welcome to the Mozilla Thunderbird Setup Wizard* window should appear.

**Step 2**. **Click** **Next** to activate the *Mozilla Thunderbird - Setup Type* window. 

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-093.png)

**Step 3**. **Click** **Next** at the *Choose setup options* window. The default setup is *Standard* 

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-094.png)

**Step 4**. **Click** **Next** to accept the default settings and activate the following screen:

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-095.png)

*Figure 3: The Mozilla Thunderbird - Summary screen*

**Step 5**. **Click** **Install** to start the installation process. The **Mozilla Thunderbird - Installing** progress status window appears. 

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-096.png)

After the installation process is complete, the following screen appears:

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-096.png)

*Figure 4: The Completing the Mozilla Thunderbird Setup Wizard screen*

**Step 6**. **Click** **Finish** to complete the installation process.

**Tip**: **Thunderbird** will automatically launch itself if the *Launch Mozilla Thunderbird now* check box is enabled, as shown in *figure 4* above. To open the program in the future, either **double click** the **Thunderbird** desktop icon ![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-098.png) or select: **Start Menu > All Apps > Mozilla Thunderbird**.

<a name="2.1"></a>
## 2.1 How to Setup an Email Account in Thunderbird ## 

The *System Integration* window will appear at first login. Deselect **Always perform this check when starting Thunderbird**. You can be set it to *Use Thunderbird as the default client for: Email* or you can choose to *Skip Integration*. 

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-010.png)

**Step 1**. At the *Welcome to Thunderbird* window **click** *Skip this and use my existing email* option:

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-011.png)

**Step 2**. **Type** in your name, email address and password in the corresponding text fields; **click** the check box to disable the *Remember my password* option.

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-024.png)

*Figure 5: The Mail Account Setup window*

**Step 3**. **Click** **Continue** to activate the following screen:

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-025.png)

*Figure 6: The Mail Account Setup window with the **IMAP (remote folders)** option enabled*

Most users will want to select **IMAP**, where all your folders (including *Inbox*, *Drafts*, *Templates*, *Sent*, *Trash* and all other folders) reside on the email server, enabling you to access these folders from different devices (laptop, phone, desktop) and have all of your emails in sync between these devices. **POP** instead downloads emails from the server to whatever device first accesses them, removing the ability for other devices to access those emails.

**Step 4**. **Click** **DONE** to create your account and enter the main **Thunderbird** interface with the email account displayed in the sidebar at left:

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-026.png)

*Figure 7: The Mozilla Thunderbird main user interface displaying our email account*

**Note**: To add another email account, **click File > New > Existing Mail Account** to activate *Figure 5* in this section, and repeat **Step 2** to **Step 4**.

After you have successfully registered your email accounts in **Thunderbird**, the next time you open the main user interface, you will be prompted to enter your password for each account as follows: 

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-047.png)

*Figure 8: The Mail Server Password Required window*

**Note**: If your email account has two-factor authentication enabled (highly recommended if this is an option from your email provider), you will not be inputting your main email password but rather an application-specific password created just for **Thunderbird**. Because of this, you should select *Use Password Manager to remember this password* since it will be a dedicated password just for this software:

![](/sites/securityinabox.org/files/media/thunderbirdenigmail-win-en-048.png)

**Thunderbird** supports a *Master Password* feature that enables you to use one password to protect any passwords related to your different accounts, entered during the setup process. For more information about this feature, please refer to section [**3.3 How to Configure the Security tabs in Thunderbird**](/en/thunderbird_security#3.3) - **The Password tab**.

Now that you have properly configured **Thunderbird** with your email account, please proceed to the following section [**How to Configure Important Settings in Thunderbird**](/en/thunderbird_security).

