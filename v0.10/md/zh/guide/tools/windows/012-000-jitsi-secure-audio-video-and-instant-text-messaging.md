

---

lang: zh
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 012
title: Jitsi - Secure Audio, Video and Instant Text Messaging 

---

**官方网站**

- [**https://jitsi.org/**](https://jitsi.org/)

**系统要求**

- Windows所有版本

**本指南所试用版本**

- 2.4

**最后一次编辑**

- 2014年3月

**授权许可**

- 免费开源软件

**您将学到**：

- 具有隐私并且安全的的通讯系统（包含视频通话）
- 加密你账户的通讯
- 注册并使用不同账户进行通讯（例如：**Facebook**、**Google Talk**、**Yahoo Messenger**）



**GNU Linux, Mac OS 和其他 Microsoft Windows 兼容的程序**

 

**Jitsi**试用于 **GNU Linux**,**Mac OS**,**Windows**，以及即将推出**Android**版本。Jitsi也可以使用独立的**OTR**或**ZRTP**加密协议与其他程序进行通讯,推荐如下：

  - **文本消息**：[**Pidgin**](/zh/pidgin_main)(**Windows**,**Linux**),[**Miranda**](http://www.miranda-im.org/) (**Windows**),[**Adium**](http://adium.im/) (**Mac OS X**),[**ChatSecure**](https://guardianproject.info/apps/chatsecure/)(**Android,iOS,以前称[**Gibberbot**](/zh/Gibberbot_main))

  - **语音通讯**：**CSipSimple**(**Android**),[**Linphone**](http://www.linphone.org/)(**GNU Linux**,**Windows**,**Mac OS X**,**Android**,**iOS**及其他)



**1.1在开始之前您应该先了解这款工具**

**Jitsi**支持多种类型的账户和通讯协议，因此用户可以使用不同程序进行交流。这些程序使用相似的特性来支持独立文本及语音加密（**OTR**和**ZRTP**），从而提高用户通讯安全（例如上面所提到的软件）。其他程序，尤其是有独立客户端的那些（如**Facebook Chat** 和 **Google Talk**），可能没有用到这些特性，但你还是能够使用**Jitsi**和你的联系人进行交谈，只是没有用到**Jitsi**的安全特性。

无论你的通讯是文字、语音或视频，像**Facebook Chat**，**Google Talk**，**Yahoo! Messanger**，**Skype**或是**Viber**的服务提供商,他们都可以获取你的通讯内容，有可能提供给第三方，像某公司或政府部门。**Jitsi**可在你已有的账户上进行加密，以私密并且安全的方式让你进行通讯。因此这让你的交谈内容无法被服务提供商和潜在的第三方窃取。为了保证你的通讯隐私，**Jitisi**用**Off-the-Record**([**OTR**](/zh/glossary#OTR))加密文字通讯，ZRTP/SRTP加密语音通讯。

**Jitsi**和其他程序如**Skype**的另外一个显著区别，是允许用户使用不同服务提供商的已有账户，独立于程序之外，这也意味着你在使用**Jitsi**之前需要设置一个账户。

**注意**：**Jitsi** 使用的是Java语言，所以，Java程序必须已经安装在你的电脑上以保证Jitsi的正常运行。众所周知**Oracle Java**有很多安全漏洞，可能被远程控制电脑安装间谍软件进行访问，或监听你所有的通讯数据。**强烈**建议尽可能少得使用Java的程序。请参阅[**禁用火狐下Java相关的插件**](/zh/firefox_noscript#4.0)”及[**禁用所有浏览器中的Java**](https://www.java.com/en/download/help/disable_browser.xml)。当然，你会在本章节后面看到，除了**Java**以外，在使用**Jitsi**仍有很多安全优势。

