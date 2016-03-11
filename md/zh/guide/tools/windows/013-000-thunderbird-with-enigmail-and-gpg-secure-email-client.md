

---

lang: zh
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 013
title: Thunderbird with Enigmail and GPG - Secure Email Client

---

**主页**

- [**www.mozilla.com/thunderbird**](http://www.mozilla.com/thunderbird/)
- [**www.enigmail.mozdev.org**](http://enigmail.mozdev.org/home/index.php)
- [**www.gnupg.org**](http://www.gnupg.org/)

**电脑要求**

- Windows所有版本

**本指南中使用的版本**

- Thunderbird 3.1.5 
- Enigmail 1.1.2
- GNU Privacy Guard (GnuPG) 2.0.4 

**授权许可**

- 免费和开源软件

**要求阅读**

- 指引手册 [**第七章：如何使您的互联网通信保持私密**](/zh/chapter-7)

**级别**：1：入门，**2： 一般，3：中等，**4：有经验的，5：高级

**上手时间**：40 分钟

**您将得到**：

- 通过单个程序管理不同电邮账户的能力
- 在断开互联网连接后阅读和撰写信件的能力
- 使用公钥加密以保护您的电子邮件的私密性的能力


**GNU/Linux、Mac OS和其他Microsoft Windows兼容的程序：**

**Mozilla Thunderbird**电子邮件客户端适用于**GNU Linux**、**Mac OS**、**Microsoft Windows**和其他操作系统。从数字安全的角度来看，管理多个电邮账户是一项复杂的任务；因此，我们*强烈推荐*您使用**Mozilla Thunderbird**。**Thunderbird**这款跨平台的、免费和开源程序所拥有的安全优势，比与之相仿的商业软件如**Microsoft Outlook**要更为显著。然而，如果您宁愿使用**Mozilla Thunderbird**以外的程序，我们推荐以下的免费开源代替品：

- [**Claws Mail**](http://www.claws-mail.org/)适用于**GNU Linux**和**Microsoft Windows**；
- [**Sylpheed**](http://sylpheed.sraoss.jp/en/)适用于**GNU Linux**、**Mac OS**和**Microsoft Windows**；
- [**Alpine**](http://www.washington.edu/alpine/)适用于**GNU Linux**、**Mac OS**和**Microsoft Windows**。

###1.1在开始之前您应该先了解这款工具###

**Mozilla Thunderbird**是一款跨平台的、免费和开源的电子邮件客户端，用于接收、发送和储存电子邮件。电邮客户端是一款能让您无需通过互联网浏览器来即可下载和管理您的电子邮件的电脑程序。您可以通过单个程序管理多个电邮账户。在使用**Thunderbird**之前，您必须拥有一个电子邮件账户。如果您愿意，您也可以创建[**Gmail**](https://www.google.com/accounts/NewAccount?service=mail)或[**RiseUp**](http://securityinabox.org/en/riseup_createaccount)电子邮件账户。

**Enigmail**是一个为**Thunderbird**而开发的附加扩展。它能让用户使用由**GNU Privacy Guard**（**GnuPG**）所提供的身份验证和加密功能。

**GnuPG**是一个公钥加密程序，用于生成和管理加密和解密电邮信息的相配钥匙，以保障您的电邮通信的私密性和安全性。要使用**Enigmail**，必须安装**GnuPG**，这将在本章稍后进行论述。

