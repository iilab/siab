

---

lang: zh
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 011
title: Pidgin with OTR - Secure Instant Messaging

---

**官方网站**

- **Pidgin**：[**www.pidgin.im**](http://www.pidgin.im)
- **OTR**：[**www.cypherpunks.ca/otr**](http://www.cypherpunks.ca/otr/)

**计算机系统要求**

- 有网络连接
- 适用于Windows所有版本 

**适用于本说明中的软件版本**

- Pidgin 2.7.11 
- OTR 3.2.0.1 

**许可证**：

- 免费和开放源代码软件

**必读**

操作指南章节[**7. 保持互联网通讯的隐私**](/chapter-7)

**适用阶段**：1：初级，**2：一般**，3：中级，4：有经验，5：高级

**学习使用此工具软件所需要的时间**：30 分钟

**您将得到：**

- 通过单一程序组织和管理一些最流行的即时通讯服务的能力
- 进行私密和已验证聊天会话的能力

**GNU Linux，Mac OS以及其他Microsoft Windows兼容程序：**

**Pidgin**和**OTR**都与**Microsoft Windows**以及**GNU/Linux**兼容。
另外一款与**Microsoft Windows**兼容且支持**OTR**的多协议**即时通讯**程序是[**Miranda IM**](http://www.miranda-im.org/)。如果是**Mac OS**，我们推荐使用[**Adium**](http://adium.im/)，一个支持**OTR**插件的多协议**即时通讯**程序。

## 1.1 关于此工具的用前须知##

**Pidgin**是一款免费和开源**即时通讯**客户端，帮您通过单一程序实现对不同（**即时通讯**）账号的组织和管理。在开始使用**Pidgin**前，必须有一个现有的**即时通讯**账号，将该账号注册到**Pidgin**。例如，如果您有一个**Gmail**账号，您可以通过**Pidgin**使用其**即时通讯**服务**Google Talk**。利用已有**即时通讯**账号的登录信息来注册和访问**Pidgin**账户。

**注**：建议所有用户都尽可能了解其**即时通讯服务供应商**的隐私和安全政策。

**Pidgin** 支持以下**即时通讯** 服务协议：[**AIM**](http://dashboard.aim.com/aim), [**Bonjour**](http://www.apple.com/support/bonjour/)，[**Gadu-Gadu**](http://komunikator.gadu-gadu.pl/)，[**Google Talk**](http://www.google.com/talk/), **Groupwise**，[**ICQ**](http://www.icq.com)，**IRC**，[**MIRC**](http://www.mirc.com/)，[**MSN**](http://www.msn.com/)，[**MXit**](http://www.mxit.com/)，[**MySpaceIM**](http://www.myspace.com/guide/im)，[**QQ**](http://www.qq.com/)，[**SILC**](http://silcnet.org/)，**SIMPLE**，[**Sametime**](http://www.ibm.com/developerworks/downloads/ls/lst/)，[**Yahoo!**](http://messenger.yahoo.com/)，**Zephyr** 以及任一运行**XMPP**通讯协议的**即时通讯**客户端。

**Pidgin**不支持在不同的**即时通讯**服务协议间的通讯。例如，如果您使用**Pidgin**进入**Google Talk**账号，那么您将不能与使用**ICQ**账号的朋友聊天。

但是，**Pidgin**可以在支持的通讯协议基础上管理多个账号。也就是说，您可以同时使用**Gmail** 和**ICQ**账号，并通过使用*任一*（**Pidgin**支持）的指定服务与联系人/好友聊天。

强烈推荐使用**Pidgin**进行会话，它提供了比所替代的通讯客户端更高的安全级别，并且其未绑定任何不必要的可能导致您的隐私和安全受到威胁的广告软件或间谍软件。

**不留记录**（**OTR**）通讯是一个专为**Pidgin**研发的插件。具有以下隐私和安全保护功能：

- **验证**：确认您的联系人的身份。
- **不可还原**：聊天结束后，您或您的任一联系人的发送的信息不能被识别。
- **加密**：没有任何人能够访问和读取您的即时信息。
- **不可追溯**：如果第三方获取了您的隐私密钥，之前的对话内容不会被盗取。

**注**：在安装**OTR**插件前，必须安装**Pidgin**。


