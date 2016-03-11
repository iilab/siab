

---

lang: zh
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 005
title: TrueCrypt - Secure File Storage

---

**主页**

[**www.truecrypt.org**](http://www.truecrypt.org/)

**电脑要求**

- Windows 2000/XP/2003/Vista/7
- 安装和创建卷要求管理员权限，访问现有的卷则不需要

**本指南中使用的版本**

- 7.0a

**授权许可**

- 免费和开源软件

**要求阅读**

- 指引手册 [**第四章：如何保护您计算机上的敏感文件**](/zh/chapter-4)
	
**级别** 

- （标准卷）：1：入门，2：一般，**3：中等**，4：有经验的，5：高级
- （隐藏卷）：1：入门，2：一般，3：中等，**4：有经验的**，5：高级

**上手时间**：

- （标准卷）：30分钟
- （标准卷）：30分钟

**您将得到**：

- 有效地保护您的文件免受入侵或未经授权访问的能力
- 轻松和安全地储存您的重要文件的能力

**GNU/Linux、Mac OS和其他Microsoft Windows兼容的程序：**

**注**：在**GNU Linux**和**Mac OS**上，我们也强烈推荐**TrueCrypt**。

许多**GNU Linux**发行版，如[**Ubuntu**](http://www.ubuntu.com/)，支持整个驱动器的快速加/解密，并以之作为一个标准功能。在安装系统的时候，您可以决定是否使用这个功能。您也可以通过[**dm-crypt**](http://www.saout.de/misc/dm-crypt/)和[**crypt setup and LUKS**](http://code.google.com/p/cryptsetup/)的组合来给您的**Linux**系统添加加密功能。另外您也可以使用[**ScramDisk for Linux SD4L**](http://sd4l.sourceforge.net/)，一款免费、开源的快速加/解密程序。

在**Mac OS**上，您可以使用**File Vault**，它是操作系统的一部分，给您的主文件夹以及它的子文件夹提供快速加密和解密功能。也许，您还会觉得免费开源的[**Encrypt This**](http://www.nathansheldon.com/files/)很有用，它能把您选取的个别文件加密成.DMG磁盘镜像。

在**Microsoft Windows**上有很多加密程序。我们推荐以下几款：

- [**FREE CompuSec**](http://www.ce-infosys.com/english/free_compusec/free_compusec.aspx)是一款免费的、专有的快速加/解密程序。它能加密部分或整个电脑硬盘、U盘或CD。**CompuSec**的**DataCrypt**组件也可以用于加密单独的文件。
- [**CryptoExpert 2009 Lite**](http://www.cryptoexpert.com/lite/)是一款免费的、专有的快速加密程序。它能创建加密文件的容器，就像**TrueCrypt**。
- [**AxCrypt**](http://www.axantum.com/AxCrypt/)是一款免费开源程序，用于加密单独的文件。
- [**Steganos LockNote**](https://www.steganos.com/us/products/for-free/locknote/overview/)是一款免费开源程序。您可以用它来加密或解密任何文字。文字会被储存在**LockNote**应用程序里。**LockNote**是便携软件，不要求安装。

### 1.1 在开始之前您应该先了解这款工具###

**TrueCrypt**通过使用您所创建的密码，把您的数据锁起来，以保护它们。如果您忘记了密码，您将失去所有的数据！**TrueCrypt**使用所谓加密的过程来保护您的文件。请记住，在某些国家，使用加密是违法行为。不同于加密特定的文件，**TrueCrypt**在您的电脑上创建受保护的区域，称为*卷*。您可以在这个加密的卷里安全储存您的文件。

**TrueCrypt**提供了创建标准卷和隐藏卷的能力。任意的卷都允许您把文件作为机密保护起来，但隐藏卷还允许您隐藏敏感资料里包含的重要信息，在您被迫揭露您的**TrueCrypt**卷的时候，能起到保护的作用。本指南详细解释这两种卷。


