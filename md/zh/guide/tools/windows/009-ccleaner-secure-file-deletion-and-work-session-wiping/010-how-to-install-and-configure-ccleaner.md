

---

lang: zh
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: How to Install and Configure CCleaner

---

本页的小节列表： 

- [**2.0 如何安装CClenaer**](#2.0)
- [**2.1 在您开始配置CCleaner之前**](#2.1)
- [**2.2 如何扫描恶意软件和病毒**](#2.3)

----

<a name="2.0"></a>
### 2.0 如何安装CClenaer###

安装**CCleaner**相当简单快捷。要开始安装**CCleaner**，请执行以下步骤：

**第1步**：**双击**![](/sbox/screen/ccleaner-en/01.png)开始安装过程。一个*“打开文件 - 安全警告”*的对话框也许会出现，如果出现了，**点击**![](/sbox/screen/ccleaner-zh/02.png)激活以下画面：

![](/sbox/screen/ccleaner-zh/03.png)

*图1：安装程序语言选择对话框*

**第2步**：**点击**![](/sbox/screen/ccleaner-zh/04.png)激活*“欢迎来到CCleanerv2.33安装向导”*的画面。

**第3步**：**点击**![](/sbox/screen/ccleaner-zh/06.png)激活*“CCleaner授权协议”*画面。在开始余下的安装过程之前，请阅读*授权协议*。

**第4步**：**点击**![](/sbox/screen/ccleaner-zh/08.png)激活*“选择安装路径”*画面。

**第5步**：**点击**![](/sbox/screen/ccleaner-zh/06.png)激活*“安装选项”*画面。

**注**：*安装选项*出现，同时*添加CCleaner Yahoo!工具栏并从浏览器使用CCleaner*选项被启用。请勿安装**Yahoo!**工具栏，因为它可能对您的互联网隐私和安全造成损害。

**第6步**：**点击** *添加CCleaner Yahoo!工具栏并从浏览器使用CCleaner*选项，从而禁用它，如*图2*所示：

![](/sbox/screen/ccleaner-zh/10.png)

*图2：禁用了Yahoo!工具栏的安装选项*

**第7步**：**点击**![](/sbox/screen/ccleaner-zh/11.png)开始安装**CCleaner**，并激活显示进度条的*“正在安装”*的画面。

**第8步**：**第8步**![](/sbox/screen/ccleaner-zh/13.png)结束安装**CCleaner**，并激活*Piriform CCleaner*用户界面。

![](/sbox/screen/ccleaner-zh/15.png)

*图3：Piriform CCleaner用户界面*

<a name="2.1"></a>
### 2.1 在您开始配置CCleaner之前###

如指引手册[**第六章：如何销毁敏感资料**](/zh/chapter-6)里详细介绍的那样，**Microsoft Windows**标准的文件删除方法并不能将实际数据从硬盘上消除（即使您清空回收站）。临时文件也一样。要将它们从硬盘上永久删除（擦除），必须用随机数据覆写这些文件。必须将**CCleaner**设置为覆写其删除的文件，从而安全地删除它们，因为默认模式不会进行覆写。**CCleaner**也可以通过擦除空闲硬盘空间来安全删除旧信息（见[**5.3如何使用CCleaner擦除空闲硬盘空间**](/zh/ccleaner_faq#5.3)）。

在您开始使用**CCleaner**前，您应该将其设置为安全删除所有临时文件。

**第1步**：**点击**![](/sbox/screen/ccleaner-zh/20.png)或**选择 开始 > 所有程序 > CCleaner** 以开启*Piriform CCleaner*主用户界面。

**第2步**：**点击**![](/sbox/screen/ccleaner-zh/22.png)激活以下画面：

![](/sbox/screen/ccleaner-zh/21.png)

*图4：默认的“关于”面板*

**第3步**：**点击**![](/sbox/screen/ccleaner-zh/23.png)激活*设置*面板。*设置*面板能让您选择最适合您操作的语言、定制**CCleaner**该如何删除临时文件与擦除驱动器。

**注**：已经启动了*正常文件删除*部分的*安全文件删除（较慢）*选项

**第4步**：**点击** *安全文件删除（较慢）*选项，激活下拉列表。

**第5步**：**展开**下拉列表并从*安全文件删除（较慢）*中**选择** *DOD 5220.22 M*，如下：

![](/sbox/screen/ccleaner-zh/24.png)

*图5：设置面板正显示安全删除选项*

在您设置好之后，**CCleaner**会用随机的资料覆写您选中删除的文件和文件夹，把它们有效地从您的硬盘上擦除。在*“安全删除”*下拉列表里的“次数”，是指您的资料将被随机资料覆写的次数。这个数字越大，您的文档、文件和文件夹将被随机资料覆写的次数越多。这将降低那些文档、文件和文件夹的可恢复性，但也增加擦除过程所需的时间长度。

