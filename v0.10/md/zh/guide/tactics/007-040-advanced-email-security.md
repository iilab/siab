

---

lang: zh
community: guide
type: tactics
legacy: True
child: True
weight: 4
depth: 3
title: Advanced Email Security

---

以下讨论到的工具和概念仅向有经验的电脑用户推荐。

### 在电子邮件中使用公钥加密 ###

哪怕对于不安全的电邮帐户而言，要达到更高级别的电邮隐私还是有可能的。想做到这点，您要学会公钥[*加密*](/zh/glossary#Encryption)。这项技术允许您对每封邮件进行编码，使邮件无法被目标收件人以外的任何人读懂。公钥[*加密*](/zh/glossary#Encryption)的精巧之处在于，您无需与您的联系人交换关于你们以后将要如何把邮件进行编码的任何秘密信息。

<div class="background" markdown="1">
Pablo: 但原理到底是怎样的呢？

Claudia: 聪明的算法啊！你使用由邮件联系人任意分发的独特的“公共钥匙”来给邮件进行编码。然后，她使用她谨慎保管的“私人钥匙”来阅读那些邮件。反之亦然，你的联系人使用你的公钥来加密她想写给你的邮件。因此，最终你们还是得交换公钥，但您们可以公开分享公钥，而无需担心企图获取你们公钥的人知道后会有什么后果。
</div>

这项技术可以配合任何电邮服务使用，就算是那种缺乏安全通讯通道的电邮服务，也能使用。因为每一封邮件在从您的电脑发出之前都已被[*加密*](/zh/glossary#Encryption)。

记住，使用[*加密*](/zh/glossary#Encryption)的话，您可能会引起注意。当您访问一个安全网站，包括电邮帐户时所使用的[*加密*](/zh/glossary#Encryption)类型，比起这里所讨论到的公钥[*加密*](/zh/glossary#Encryption)类型来说，通常没那么可疑。在有些情况下，如果一封包含这种[*加密*](/zh/glossary#Encryption)内容的电子邮件被成功截获，或者被发布到一个公开论坛上，不管内容是什么，都有可能会连累到发送邮件的人。有时候您得在邮件的隐私与保持低调之中作出选择。


### 加密与鉴定不同的邮件信息 ###

公钥[*加密*](/zh/glossary#Encryption)在一开始貌似比较复杂，但只要您理解了它的原理，它其实是很简单的，而这些工具也不难使用。Mozilla [*Thunderbird*](/zh/glossary#Thunderbird)电邮程序可以和一个叫[*Enigmail*](/zh/glossary#Enigmail)的扩展一起使用，轻松地加密和解密邮件信息。

<div class="getstarted" markdown="1">
**上手指南：查看**  [***Thunderbird 指南***](/zh/thunderbird_main)并开始使用
</div>

[*VaultletSuite 2 Go*](/zh/glossary#VaultletSuite)是一款免费的电邮加密程序，如果您愿意信任提供此软件的公司，并允许他们替您完成一部分工作，它比Thunderbird更容易使用。

<div class="getstarted" markdown="1">
**上手指南：查看** [***VaultletSuite 2Go 指南***](/vaultletsuite_main)并开始使用
</div>

鉴定您的电子邮件是通讯安全的另一个重要方面。任何能够访问互联网并且拥有适当工具的人，都可以通过一个跟您的电邮地址一模一样的假地址来发送信息，以达到冒充您的目的。从收件人的角度去看，这点的危害性就更加明显了。请想象一下以下情况所构成的威胁，比方说一封电子邮件，它表面上像是发自一个可信的联系人，但其实是来自于意图扰乱您的行动或者窃取关于您组织的敏感资料的其他人。

因为我们不能透过电子邮件看到或听到对方，我们一般都靠发送者的地址来证实其身份，这也是我们容易被假冒邮件欺骗的原因。同样依靠公钥[*加密*](/zh/glossary#Encryption)的[*数字签名*](/zh/glossary#Digital_signature)在发送邮件时提供了一个更为安全的自我证明方法。在[***Thunderbird指南***](/zh/thunderbird_main)的[***如何同时使用Thunderbird与Enigmail***](/zh/thuderbird_encryption)一节里有详细解释。

<div class="background" markdown="1">
Pablo: 有一次，一个同事收到了来自我的邮件，但我从来没有发送过。我们最后认定它只是垃圾邮件，但现在我不禁想象，假如一封假冒电邮在错误的时候出现在错误的对象的收件箱里，这将带来多大的损害啊。我听说可以通过数字签名来防止这种事情发生，但数字签名到底是什么？

Claudia: 一个数字签名就像信封上的封印，信封里装有你的信件，只是这个封印无法被伪造。它能证明你是该信件的真正发送者，以及它在中途并未遭到篡改。
</div>



