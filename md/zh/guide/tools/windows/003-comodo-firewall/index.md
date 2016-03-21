

---

lang: zh
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 003
title: Comodo Firewall

---

**主页**

[**www.comodo.cn**](http://www.comodo.cn)

**电脑要求**

- Windows2000/XP/2003/Vista
- 安装程序需要管理员权限

**本指南中使用的版本**

- 5.0.16

**授权许可**

- 免费

**要求阅读**:

- 指引手册[**第一章：如何保护您的计算机免受恶意软件和黑客侵害**](/zh/chapter-1)

**适用阶段**：1：入门，2：一般，**3：中等**，4：有经验的，5：高级

上手时间：60分钟

**您将学到**：

- 有效并且高效地保护您的电脑和网络安全，免受敌对份子、网络黑客、恶意软件、病毒和其他软件或程序威胁的能力。

- 通过配置简便的软件界面来管理在您电脑上的所有程序所发出的连接到互联网的请求的能力。

**GNU/Linux、Mac OS和其他Microsoft Windows兼容的程序：**

**GNU/Linux**内置了([**netfilter/iptables**](http://www.netfilter.org/))防火墙和非常好的网络安全设置。还有各种对用户友好的不同界面，我们特别推荐[**GUFW**](https://help.ubuntu.com/community/Gufw)(**Graphical Uncomplicated Firewall**)（请看[**更多信息**](http://blog.bodhizazen.net/linux/firewall-ubuntu-gufw/)）。

**Mac OS**有一个可靠而强大的内置防火墙，可以通过能增强其现有的能力的各种附加界面来改善功能。其中有：[**NoobProof**](http://www.hanynet.com/noobproof/)或[**IPSecuritas**](http://www.lobotomo.com/products/IPSecuritas/)。对于经济条件允许的用户，我们推荐[**Little Snitch**](http://www.obdev.at/products/littlesnitch/index.html)将您的互联网隐私安全和个人信息保护提高一个级别。

对**Microsoft Windows**而言，除了**COMODO防火墙**还有不少好选择。用户觉得[**ZoneAlarm Free Firewall**](http://www.zonealarm.com/security/en-us/zonealarm-pc-security-free-firewall.htm)或[**Outpost Firewall Free**](http://free.agnitum.com/)是同样高效的替代品。

###1.1 在开始之前，您应该先了解这款工具###

防火墙就像您电脑的门卫。它有一套关于何种信息应该进出您的电脑的规矩。防火墙是接收和分析来自互联网的外来数据的第一个程序，也是扫描向外发送至互联网的信息的最后一个程序。

它能防止黑客或其他入侵者获取储存在您电脑上的信息，防止恶意软件未经您的许可发送信息至互联网上。**Comodo防火墙**是一款备受好评的知名防火墙。它是免费软件，这意味着您无需为使用它而购买授权许可。

运行一个自定义的防火墙程序，在一开始需要花费相当的时间和努力，以保证所有设定都正确且适合您使用电脑的习惯。经过初学阶段之后，防火墙会不间断地工作，不怎么需要您操心了。

**警告**：在没有安装和运行防火墙之前，切勿连接到互联网！即使您的调制解调器或路由器有它们自己的防火墙，我们也强烈推荐您在电脑上再安装一个防火墙。



