

---

lang: zh
community: guide
type: tactics
legacy: True
child: True
weight: 1
depth: 3
title: Encrypting your information

---

<div class="background" markdown="1">
Pablo: 我的电脑已经有Windows 登录密码的保护了，这还不够吗？

Claudia: 其实，Windows登录密码通常很容易被破解。而且，只要有足够的时间，任何能接触您的电脑的人都可以用一张Live CD来重启您的电脑，并复制数据而无需担心密码。如果他们设法把电脑带走一段时间，您的麻烦可能会更大。不仅Windows 密码需要您操心，微软的Word或Adobe Acrobat的密码也不值得您信任。
</div>

[*加密*](/zh/glossary#Encryption)您的数据有点像把它们锁在保险箱里。只有持有钥匙或知道锁的暗码（这里指密钥或者密码）的人才能访问这些数据。这个比喻尤其适用于[*TrueCrypt*](/zh/glossary#TrueCrypt)及类似工具。这些工具不是每次仅能保护一个文件，它们能创建名为“加密卷”的安全容器，您可以把很多文件同时放进[*加密卷*](/zh/glossary#Encryption)里，但这些工具不能保护储存在您计算机或U盘以外其他地方的文件。

<div class="getstarted" markdown="1">
上手指南：查看 [***TrueCrypt 指南***](/truecrypt_main)并开始使用。
</div>

虽然其他工具也能提供同样强度的*[加密](/zh/glossary#Encryption)*，但[*TrueCrypt*](/zh/glossary#TrueCrypt)是为尽可能简化这种安全文件储存而特别设计的，而且它还支持把*[加密卷](/zh/glossary#Encryption)*放在便携存储设备上。它是[*自由开源软件*](/zh/glossary#FOSS)，在下一部分“如何隐藏您的敏感数据”里将讲述到的它的 “隐藏的TrueCrypt加密卷”特色功能，使[*TrueCrypt*](/zh/glossary#TrueCrypt)大大优越于许多内置的[*专有*](/zh/glossary#Proprietary_software)[*加密*](/zh/glossary#Encryption)工具，例如Windows XP 的“bitlocker”。

<div class="background" markdown="1">
Pablo: 好吧，现在您让我担心了。那么电脑上的其他用户又如何呢？他们可以访问“我的文档”里的文件吗？

Claudia: 我很欣赏您的思路！如果您的Windows密码不能抵御入侵者，它又怎么能抵御在同一台电脑上有帐户的其他人呢？实际上，您的“我的文档”通常是对任何人可见的。所以其他用户根本不需要耍小聪明就能读取您未加密的文件。您刚才说得对，就算文件夹被标记为“私密”，这仍然不够安全，除非您采取了某些保护措施。
</div>

### 安全地使用文件加密的小窍门 ###

保存机密文件对您和您的同事来说可能都是个风险。 [*加密*](/zh/glossary#Encryption)能降低风险，但不能彻底消除风险。保护敏感资料的第一步就是要减少所保存的数量。除非您有充分的理由去保存某个文件，或一个文件里的某类信息，否则您就应该删除它（参看[***第六章：如何销毁敏感资料***](/zh/chapter-6)以了解更多关于安全删除的内容）。第二步就是使用一个优秀的文件[*加密*](/zh/glossary#Encryption)工具，如[*TrueCrypt*](/zh/glossary#TrueCrypt)。

<div class="background" markdown="1">
Claudia: 那么也许我们不应该保存那些能鉴别出证人身份的证词？您说呢？

Pablo: 我同意。我们也应该尽可能记录得少一些。还有，我们应该想出一个简单的密码来保护那些必须记录下来的姓名和地址。	
</div>

回到保险箱的比喻上来。在使用[*TrueCrypt*](/zh/glossary#TrueCrypt)及此类工具时，您应该谨记若干事项。不论您的保险柜多么稳固，柜门大开总不会给您带来多少好处。当您的[*TrueCrypt*](/zh/glossary#TrueCrypt)卷完成加载（您能访问里面的内容），您的数据就很容易受到损害，所以除非您真的需要阅读或修改里面的文件，您应该关闭它。

在以下几种情况下，请切记不要把[*加密*](/zh/glossary#Encryption)卷遗忘在加载状态：

- 当您离开计算机，不论时间有多长，都要卸载加载。就算您经常让计算机彻夜运行，您也要确保在您离开期间，实体或远程的入侵者无法访问您的敏感文件。

- 在使计算机进入睡眠模式前卸载加载。这同时适用于常见于笔记本电脑，并且也可能在台式计算机上出现的“睡眠”和“休眠”功能。

- 在让别人使用您的计算机前断开加载。在携带笔记本电脑通过安检或越过边境的时候，断开所有[*加密*](/zh/glossary#Encryption)卷并且彻底关闭您的计算机，这点很重要。

- 在插入陌生的U盘或外部存储设备前断开加载，包括那些来自于朋友或同事的存储设备。

- 如果您把一个[*加密*](/zh/glossary#Encryption)卷保存在U盘里，请记住，移除设备可能并不会立即卸载加载。即使您需要在匆忙中收藏起您的文件，您也需要正确地卸载加载，然后把外置驱动器或U盘移除。您需要多加练习直到找到完成此举的最快途径。
	
如果您决定把您的[*TrueCrypt*](/zh/glossary#TrueCrypt)加密卷保存在U盘上，您也可以把一份[*TrueCrypt*](/zh/glossary#TrueCrypt)程序的副本放在一起。这能使您可以在别人的计算机上访问您的数据。然而，还是老规矩：如果您不确定该计算机上有没有[*恶意软件*](/zh/glossary#Malware)，您就不应该在该计算机上输入您的密码或访问敏感数据。


