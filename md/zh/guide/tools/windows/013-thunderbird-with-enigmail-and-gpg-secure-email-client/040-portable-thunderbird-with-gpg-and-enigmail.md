

---

lang: zh
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 4
depth: 3
title: Portable Thunderbird with GPG and Enigmail

---

##1.0 安装版和便携版软件的区别：Thunderbird##

使用**便携版Thunderbird**的最大好处是，您可以将本地的邮件保存在移动存储设备里。除此以外，**便携版Thunderbird**程序本身和您的本地邮件，也都可以放置在**TrueCrypt**的加密卷里，如此一来，既增强了您邮件的安全性，又有效隐藏了您的邮件账户地址。但是任何外接设备或者U盘都会遇到与电脑相似的威胁，如广告软件、恶意间谍软件以及病毒等。 

**注意**：为了保持您邮件通讯过程的安全隐私，我们强烈推荐您下载并安装本章最后列出**便携版GnuPG**软件。

##2.0 如何下载及安装便携版Thunderbird##

**步骤1**：**单击**[**http://portableapps.com/apps/internet/Thunderbird_portable**](http://portableapps.com/apps/internet/Thunderbird_portable)前往至合适的下载站点。

**步骤2**：**单击**![](/sbox/screen/thunderbirdportable-en/01.png)开启**开源社区**下载点。

**步骤3**：**单击**![](/sbox/screen/thunderbirdportable-en/02.png)将![](/sbox/screen/thunderbirdportable-en/03.png)安装文件保存至电脑；然后**前往**指定的下载文件夹。

**步骤4**：**双击**![](/sbox/screen/thunderbirdportable-en/03.png)；*打开文件 - 安全警报*对话框可能会出现，如果是，请**单击**![](/sbox/screen/thunderbirdportable-en/04.png)开启如下界面：

![](/sbox/screen/thunderbirdportable-en/05.png)

*图1：便携版MozillaThunderbird|Portableapps.com安装程序窗口

**步骤5**：**单击**![](/sbox/screen/thunderbirdportable-en/06.png)开启如下界面：

![](/sbox/screen/thunderbirdportable-en/07.png)

*图 2：安装路径选择窗口*

**步骤6**：**单击**![](/sbox/screen/thunderbirdportable-en/08.png)以开启*浏览文件夹*窗口，如下所示：

![](/sbox/screen/thunderbirdportable-en/09.png)

*图3：安装路径窗口*

**步骤7**：**前往**您的移动硬盘或U盘，如*图3*所示，然后**单击**![](/sbox/screen/thunderbirdportable-en/10.png)确认**便携版MozillaThunderbird**文件的安装地址，并回到*选择安装路径*窗口。

**步骤8**：**单击**![](/sbox/screen/thunderbirdportable-en/11.png)以开启*安装*窗口然后开始解压**便携版MozillaThunderbird**文件，然后**单击**![](/sbox/screen/thunderbirdportable-en/12.png)完成解压安装过程。

**步骤9**：**前往移动硬盘或者U盘中**安装**便携版MozillaThunderbird**的地址。

**步骤10**：**双击**打开您的移动存储设备，与下图对照应该相似：

![](/sbox/screen/thunderbirdportable-en/13.png)

*图4：新安装的便携版MozillaThunderbird显示便携版Thunderbird文件夹*

##3.0 如何下载及安装便携版GPG for Thunderbird##

**步骤1**：**单击**[**http://portableapps.com/support/thunderbird_portable#encryption**](http://portableapps.com/support/thunderbird_portable#encryption)打开下载网站。

**步骤2**：**单击**![](/sbox/screen/thunderbirdportable-en/17.png)开启*GPG_for_Thunderbird_Portable_1.4.11.paf.exe*下载窗口，然后**单击**![](/sbox/screen/thunderbirdportable-en/02.png)保存![](/sbox/screen/thunderbirdportable-en/18.png)安装文件；然后**前往**指定的下载文件夹。

**步骤3**：**双击**![](/sbox/screen/thunderbirdportable-en/18.png)；*打开文件 - 安全警报*对话框可能会出现，如果是，请**点击**![](/sbox/screen/thunderbirdportable-en/04.png)开启如下界面：

![](/sbox/screen/thunderbirdportable-en/19.png)

*图6：安装语言选择窗口*

**步骤4**：**双击**![](/sbox/screen/thunderbirdportable-en/10.png)开启**GPG for Thunderbird|便携扩展安装**窗口，然后**单击**![](/sbox/screen/thunderbirdportable-en/06.png)开启如下界面：

![](/sbox/screen/thunderbirdportable-en/20.png)

*图7：安装路径选择窗口*

**步骤5**：**单击**![](/sbox/screen/thunderbirdportable-en/08.png)开启*浏览文件夹*窗口，如下所示：

![](/sbox/screen/thunderbirdportable-en/21.png)

*图8：安装路径窗口*

**步骤6**：**单击**![](/sbox/screen/thunderbirdportable-en/10.png)回到*选择安装路径*窗口（*图7*），然后![](/sbox/screen/thunderbirdportable-en/11.png)开始解压安装**便携版GnuPG**，等到安装完后，**单击**![](/sbox/screen/thunderbirdportable-en/12.png)。

**步骤7**：**前往**指定的移动存储设备，然后**选择***E:\ThunderbirdPortable\App*以验证**便携版GPGforThunderbird**程序已成功解压到目标文件夹.

![](/sbox/screen/thunderbirdportable-en/23.png)

*图9：目标移动设备窗口显示新解压的便携版GPG for Thunderbird程序*

##4.0 如何下载安装Enigmail##

**Enigmail**是**MozillaThunderbird**的一个附加组件，用以保护您的邮件通讯的隐私。其实**Enigmail**只是为用户使用**GnuPG**加密技术提供了一个基于**Thunderbird**的平台。**Engimail**相关选项位于**Thunderbird**界面下的*OpenPGP*工具栏内。

**步骤1**：**单击**[**http://enigmail.mozdev.org/home/index.php.html**](http://enigmail.mozdev.org/home/index.php.html)登录到下载站点。

**步骤2**：**单击**![](/sbox/screen/thunderbirdportable-en/24.png)开启*enigmail-1.1.2-tb-win.xpi*下载窗口，然后**单击**![](/sbox/screen/thunderbirdportable-en/25.png)将![](/sbox/screen/thunderbirdportable-en/26.png)保存到您的电脑里。

**步骤3**：**打开****便携版Thunderbird**文件夹，然后**双击**![](/sbox/screen/thunderbirdportable-en/14.png)来打开**便携版Thunderbird**。

**步骤4**：**选择工具 > 附加组件**，位于**便携版Thunderbird**主界面内，如下所示：

![](/sbox/screen/thunderbirdportable-en/27.png)

*图10：便携版Thunderbird主界面，选择附加组件选项*

*会打开如下界面：*

![](/sbox/screen/thunderbirdportable-en/28.png)

*图11：便携版Thunderbird附加组件窗口*

**步骤5**：**单击**![](/sbox/screen/thunderbirdportable-en/29.png)完成**Enigmail**的安装，并重启**便携版Thunderbird**。

当您成功下载并安装了**便携版Thunderbird**以及**GPGforThunderbird**之后，请参阅[**Thunderbird**](/zh/thunderbird_main)章节来登陆您的邮件账号并开始使用软件。

**安装 Thunderbird, Enigmail, GnuPG**

- *阅读[上手指南](/zh/handsonguides)的简介*
- ***点击以下的 Thunderbird, Enigmail, GnuPG 图标**，“打开”或“运行”安装程序。如有需要，先保存安装程序，找到并双击*
- *在您继续安装之前，请阅读下一部分的“安装说明”*
- *如果您在电脑里保存了安装程序，完成安装后，您可以将其删除*

**Thunderbird:  Enigmail:  GnuPG:**  

[![](/sites/securityinabox.org/files/u12/thunderbird.png)](/sbox/programs/ThunderbirdPortable-zh.exe)
[![](/sites/securityinabox.org/files/u9/enigmail_long.png)](/sbox/programs/enigmail.xpi)
[![](/sites/securityinabox.org/files/u9/GnuPG.png)](/sbox/programs/GPG_for_Thunderbird_Portable_1.4.11.paf.exe)


