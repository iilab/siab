

---

lang: zh
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: How to Install Thunderbird

---

本页的项目列表：

- [**2.0 如何安装 Thunderbird**](#2.0)
- [**2.1 如何禁用Thunderbird 中的“全局搜索以及索引”选项**](#2.1)
- [**2.2 如何在Thunderbird里添加电邮账号**](#2.2)
- [**2.3 如何在Thunderbird里添加博客，新闻源，或新闻组账户**](#2.3)

-------

<a name="2.0"></a>
## 2.0 如何安装 Thunderbird##

安装**Thunderbird**是个很容易的过程。要安装 **Thunderbird**，请按照以下步骤执行：

**步骤1**：**双击**![](/sbox/screen/thunderbird-zh/01.png)；然后可能会出现*打开文件 -安全警报*对话框。如果是，请**单击**![](/sbox/screen/thunderbird-zh/02.png)打开以下界面：

![](/sbox/screen/thunderbird-zh/03.png)

*图 1：文件提取进度条*

当**Thunderbird**完全提取安装完成后，会出现*欢迎来到Mozilla Thunderbird安装向导*窗口。

**步骤 2**：**单击**![](/sbox/screen/thunderbird-zh/04.png)，打开*Mozilla Thunderbird - 安装类型*窗口。

**步骤3**：**单击**![](/sbox/screen/thunderbird-zh/04.png)，接受默认设置，并打开以下窗口：

![](/sbox/screen/thunderbird-zh/05.png)

*图2：Mozilla Thunderbird - 概述窗口*

**步骤4**：**单击**![](/sbox/screen/thunderbird-zh/06.png)开始安装。然后将会出现**Mozilla Thunderbird - 正在安装**安装进程窗口。待安装完成，会出现以下窗口：

![](/sbox/screen/thunderbird-zh/07.png)

*图3：正在完成Mozilla Thunderbird安装向导窗口*

**步骤5**：**单击**![](/sbox/screen/thunderbird-zh/08.png)以完成安装。

**提示**：如果您勾选了*立即运行Mozilla Thunderbird*选项，**Thunderbird**将会自动运行，如*图3*。下次打开程序的时候，您可以**双击** **Thunderbird**的桌面图标，或**选择 > 程序 > Mozilla Thunderbird > Mozilla Thunderbird**。

<a name="2.1"></a>
## 2.1如何禁用Thunderbird的“全局搜索以及索引”选项##

**警告**：*必须* *关闭* *全局搜索以及索引*功能才能使*Thunderbird*达到最优运行状态。鉴于您会接收到各种容量不同的邮件，可能会降低您的系统运行速度。该选项会持续向您的硬盘写入信息，这是完全没有必要的。随着硬盘空间逐渐变满，它会影响到其他的系统运行。

要关闭*全局搜索以及索引*选项，请按照以下步骤执行：

**步骤1**：在**Thunderbird**控制台中**选择 工具 > 选项**来打开*选项*窗口。

**步骤2**：**单击** ![](/sbox/screen/thunderbird-zh/09.png)打开以下界面：

![](/sbox/screen/thunderbird-zh/10.png)

*图 4：高级选项窗口*

**步骤3**：**单击** *高级配置*中的*启用全局搜索以及索引*勾选框来*禁用*该选项，如下所示：

![](/sbox/screen/thunderbird-zh/11.png)

*图5：高级配置选项*

好了，现在您已经禁用这项功能了。赶快在**Thunderbird**中添加一个电邮地址吧。

<a name="2.2"></a>
## 2.2 如何在Thunderbird里添加电邮账号## 

*导入向导 - 导入设置以及邮件窗口*仅会在您首次运行**Thunderbird**时出现。

**步骤 1**：**反选** *不导入任何数据*选项，如窗口中所示：
 
![](/sbox/screen/thunderbird-zh/12.png)

*图 6：导入向导 - 导入设置以及邮件夹*

**步骤2**：**单击**![](/sbox/screen/thunderbird-zh/04.png)打开以下界面：

![](/sbox/screen/thunderbird-zh/13.png)

*图7：邮件账户设置窗口*

**步骤3**：在相应的文本框中**输入**您的姓名，邮件地址以及密码；然后取消*记住密码*选项，如*图7*所示。

**步骤4**：**单击**![](/sbox/screen/thunderbird-zh/14.png)打开以下界面：

![](/sbox/screen/thunderbird-zh/15.png)

*图 8：邮件账户设置窗口，并启用了**IMAP - 从多处计算机访问您的文件夹及消息（推荐）**选项*

##IMAP和POP：简介与用途###

**互联网信息访问协议**（**IMAP**）以及**邮局协议**（**POP**）是两种不同的邮件储存、接收方式。

- **互联网信息访问协议**（**IMAP**）：如果您选择使用**IMAP**模式，邮箱中的所有文件夹（包括*收件箱*、*草稿箱*、*模板*、*已发邮件*、*垃圾邮件*等）都会放置在服务器上，因此您可以从不同电脑访问这些文件夹。平时邮件信息都将保存在服务器上，只有消息头、标题栏（包含诸如时间、标题、发送者等信息）会被下载显示在电脑里，在您打开邮件时才会下载完整的邮件信息。通过设置，**Thunderbird**也可以储存部分或全部邮件的副本，使您可以在脱机状态（无网络连接）下使用它们。在**IMAP**模式下，当删除邮件或整个文件夹时，您在电脑上的操作与服务器是同步的。


- **邮局协议**（**POP**）：如果您选择使用**POP**模式，只有*收件箱*（接收新邮件的文件夹）会放置在服务器上。其他的文件夹都会在您的电脑里。在将邮件下载至电脑后，您可以选择仍将它们留在服务器的*收件夹*中，或者删除它们。如果您从另一台电脑登陆邮箱的话，您将只能看到收件夹的邮件（包括新邮件以及未被删除的邮件）。

**步骤5**：**单击**![](/sbox/screen/thunderbird-zh/16.png)来创建您的账号，然后启动**Thunderbird**，可以看到左侧工具栏*全部文件夹*显示您的电子邮件，如图：

![](/sbox/screen/thunderbird-zh/17.png)

*图9：Mozilla Thunderbird用户主界面显示新创建的gmail账号*

**提示**：如果要加入其他的电邮地址，**选择 文件 > 新建 > 邮件账户...**来打开*图7*，然后重复**步骤3**到**步骤5**的过程。

在您成功在**Thunderbird**中添加了电邮地址以后，下次再打开主界面时，您会被要求输入账户的密码，如下图：

![](/sbox/screen/thunderbird-zh/20.png)

*图10：需要邮件服务器密码窗口*

**提示**：尽管基于安全隐私等因素考虑，保存密码或自动记忆等功能通常是不推荐使用的。但**Thunderbird**支持一种名为*主密码*的特性，该特性允许您使用一个密码来保护您不通账号下的各种密码（在输入过程中）。想了解更多该特性的信息，请参见章节[**3.3 如何设置Thunderbird安全选项**](/zh/thunderbird_security#3.3) - **口令选项卡**。

<a name="2.3"></a>
## 2.3 如何在Thunderbird里添加博客、新闻源或新闻组账户##

要创建或添加一个博客，新闻源或新闻组账户，请按照以下步骤执行：

**步骤1**：**选择 > 文件 > 新建 > 其他账户**来打开*账户向导 > 新建账户设置*窗口。

**步骤2**：**勾选**任意*博客和新闻收取点*或*新闻组账户*中的一种账户类型，然后单击**单击**![](/sbox/screen/thunderbird-zh/04.png)打开以下界面：

![](/sbox/screen/thunderbird-zh/21.png)

*图11：账户向导 - 账户名称窗口*

**步骤 3**：**单击**![](/sbox/screen/thunderbird-zh/04.png)打开以下界面：

![](/sbox/screen/thunderbird-zh/22.png)

*图12：账户向导-恭喜您！窗口*

**步骤5**：**单击**![](/sbox/screen/thunderbird-zh/08.png)完成账号设置，并返回**Thunderbird**主页面。

好了，在您的精心调试下，**Thunderbird**可以发挥最佳使用效能了。下面请转到这一章[**如何配置Thunderbird的安全选项**](/zh/thunderbird_security)。


