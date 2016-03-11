

---

lang: zh
community: guide
type: tactics
legacy: True
child: True
weight: 2
depth: 3
title: Communicating (Voice and Messages) via Smartphone

---

智能手机的数据存储能力很强。不幸的是，第三方可以轻易地通过远程或物理方式，接触到手机上存储的数据。[***Android基本设置指南***](/zh/android_basic)中介绍了减少手机被入侵风险的部分基本预防措施。此外，您还可以采取加密措施，使用特定工具对手机上的敏感信息进行加密。

###数据加密工具###

[**Android隐私卫士（APG）**](/zh/APG_main)可以对文件和电子邮件进行OpenGPG加密。有了它，您就可以将文件和资料安全地存储在手机上，并通过电子邮件安全发送文件和资料。

<div class=getstarted markdown=1>
上手指南：[*APG指南*](/zh/APG_main)
</div>

[**Cryptonite**](https://code.google.com/p/cryptonite/)也是一种[*FOSS*](/zh/glossary#FOSS)文件加密工具。对于使用自定义固件并具有root权限的特制Android手机，Cryptonite具有更多高级功能。请参阅[***高级智能手机应用***](/zh/chapter_11_7)部分，了解更多信息。

<div class=getstarted markdown=1>
上手指南：[*Cryptonite指南*](/zh/Cryptonite_main)
</div>

###密码安全保护###

您可以使用**KeePass**将所有密码保存在一个安全的加密文件中。您只需记住一个主密码，即可找到所有其他的密码。有了KeePass，您就可以为每个账户设置复杂的密码，KeePass会帮您记住它们，而且KeePass还带有密码生成器，可以创建新密码。您可以在手机和电脑上将KeePass密码数据库同步起来。我们建议您只同步那些真正需要在手机上使用的密码。您可以在电脑上单独创建一个小密码数据库，将其与手机同步，而不是将储存有全部密码的整个数据库都复制到智能手机上。此外，由于所有密码都受主密码的保护，请务必为KeePass数据库设置非常强大的密码。参见[***第3章：如何创建与维护安全密码***](/zh/chapter-3)。

<div class=getstarted markdown=1>
上手指南：[*KeePassDroid指南*](/zh/KeepassDroid_main)
</div>



