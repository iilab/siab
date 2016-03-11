

---

lang: zh
community: guide
type: tactics
legacy: True
child: True
weight: 3
depth: 3
title: Securing other Internet communication tools

---

跟电子邮件一样，根据您选择的是什么工具以及如何使用它们，即时通讯和[*VoIP*](/zh/glossary#VoIP)软件可能安全，也可能不安全。

**保障您的即时通讯软件安全**

即时通讯，也称“聊天”，通常是不安全的，很容易像电子邮件一样受到监控。幸好有一些程序有助于保障您的聊天会话的隐私性。跟电子邮件一样，一个安全的通讯渠道要求您与您的即时通讯联系人双方都用相同的软件，并采取相同的安全预防措施。

有一款叫[*Pidgin*](/zh/glossary#Pidgin)的聊天程序支持许多现有的即时通讯协议，这表示您可以轻松地使用它而无需更改您的帐户名称或者重新建立联系人列表。为了适应[*Pidgin*](/zh/glossary#Pidgin)进行私密的、受[*加密*](/zh/glossary#Encryption)保护的会话，您需要安装并激活[*OTR*](/zh/glossary#OTR)“不留记录”插件。还好这只是个相当简单的过程。

<div class="getstarted" markdown="1">
**上手指南：查看** [*Pidgin 指南*](/zh/pidgin_main)并开始使用
</div>

[*Skype*](/zh/glossary#Skype)是一个常见的[*VoIP*](/zh/glossary#VoIP)工具，它同时也支持即时通讯。使用[*Skype*](/zh/glossary#Skype)应该比没有OTR插件的替代品要更为安全，但它有两个缺点。第一，它只允许您与其他Skype用户聊天，而[*Pidgin*](/zh/glossary#Pidgin)则可以跟几乎所有其他即时通讯服务进行安全通讯。第二，因为它并不开放源代码，这就无法验证它的[*加密*](/glossary#Encryption)强度。在[***第一章：如何保护您的电脑免受恶意软件和黑客侵害***](/zh/chapter_1)的[***保持更新您的软件***](/zh/chapter_1_4)一节里说明了“自由开源软件”[*FOSS*](/zh/glossary#FOSS)的优点。简单来说，您最好还是使用带[*OTR*](/zh/glossary#OTR)插件的[*Pidgin*](/zh/glossary#Pidgin)来进行安全的即时通讯。

<div class="background" markdown="1">
Pablo: 如果Yahoo邮箱不安全，那就代表Yahoo聊天也不安全吗？

Claudia: 需要记住的是，如果我们想使用即时通讯来讨论这份报告，我们就需要确保所有有关人员都安装有Pidgin和OTR。这样，我们便可以使用Yahoo聊天或者任何其他聊天服务了。
</div>

**保障您的VoIP软件安全**

[*VoIP*](/zh/glossary#VoIP)用户间的电话传呼一般是免费的。有些程序允许您拨打普通的电话，包括国际号码，而收费并不昂贵。不言而喻，这些功能是极其有用的。现今广受欢迎的VoIP程序有[Skype](http://www.skype.com)、[Gizmo](http://www.gizmoproject.com/)、[Google Talk](http://www.google.com/talk)、[Yahoo! 语音](http://voice.yahoo.com/)和[MSN](http://get.live.com/messenger)。

通常，通过互联网的语音通讯并不比未受保护的电子邮件和即时通讯更加安全。只有[*Skype*](/zh/glossary#Skype)和[*Gizmo*](/zh/glossary#Gizmo)对语音会话提供了加密，而且仅限于您呼叫的是另一位[*VoIP*](/zh/glossary#VoIP)用户，不适用于移动电话和固定电话。另外，因为这两个应用程序都不开源，独立专家们一直无法对它们进行全面的测试以确保它们是安全的。


