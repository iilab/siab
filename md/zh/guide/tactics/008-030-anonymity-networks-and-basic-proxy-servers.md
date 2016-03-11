

---

lang: zh
community: guide
type: tactics
legacy: True
child: True
weight: 3
depth: 3
title: Anonymity networks and basic proxy servers

---

### 匿名网络 ###

匿名网络通常让您的互联网传输“来回弹跳”于多个不同的[*代理*](/zh/glossary#Proxy)之间，从而隐瞒您来自哪里以及要访问什么内容。这会极大地减慢您加载网页或其他互联网服务的速度。然而，就[*Tor*](/zh/glossary#Tor)而言，它同时还提供了可靠、安全和公开的绕行手段，使您无需担心是否可以信任您的[*代理*](/zh/glossary#Proxy)和您所访问网站的运行者。跟往常一样，在使用浏览器交换密码、电子邮件这些敏感信息之前，您必须确保您在使用已加密的[HTTPS](/zh/glossary#SSL)连接到一个安全网站。

您需要安装软件来使用[*Tor*](/zh/glossary#Tor)，您将得到一个同时提供匿名和绕行的工具。每次当您连接上[*Tor*](/zh/glossary#Tor)网络，您都选择了一条随机的路径，贯通三个安全的[*Tor*](/zh/glossary#Tor)[*代理*](/zh/glossary#Proxy)。这能确保不论您的[*ISP*](/zh/glossary#ISP)还是那些[*代理*](/zh/glossary#Proxy)本身都不知道您电脑的[*IP地址*](/zh/glossary#IP_address)以及您所请求的互联网服务所在。您可以从[*Tor*](/zh/glossary#Tor)指南里了解更多详情。

<div class="getstarted" markdown="1">
上手指南：查看[*Tor 指南*](/zh/tor_main)并开始使用
</div>

Tor的长处之一，在于它不仅能与浏览器一起使用，还能用于不同类型的互联网软件。包括Mozilla [*Thunderbird*](/zh/glossary#Thunderbird) 在内的电子邮件程序以及包括[*Pidgin*](/zh/glossary#Pidgin)在内的即时通讯程序，都可以通过Tor运作，以访问被过滤的服务和隐瞒您对这些服务的使用。

### 基础绕行代理 ###

在选择一个基础绕行[*代理*](/zh/glossary#Proxy)的时候，您需要考虑三个重要的问题。首先，它是一个基于网页的代理，还是会要求您更改设置或给电脑安装软件？第二，它是否安全？第三，它是私密的还是公共的？

#### 基于网页的代理和其他代理 ####

基于网页的[*代理*](/zh/glossary#Proxy)可能是最容易使用的。它们只要求您把浏览器指向一个[*代理*](/zh/glossary#Proxy)页面，输入您想查看的被过滤的网址，然后点击一个按钮。[*代理*](/zh/glossary#Proxy)就会在它自己的页面内显示您所请求的内容。您可以照常点击链接，或者如果您想查看另一个网页，就往[*代理*](/zh/glossary#Proxy)里输入一个新网址。您并不需要安装任何软件或更改浏览器设置，这也就是说基于网页的[*代理*](/zh/glossary#Proxy)：

- 容易使用。
- 可在公共电脑上进行使用，例如在不允许您安装软件或修改设置的网吧里。
- 如果您担心因为在电脑上使用绕行软件而被捕，这就可能更安全。
	
基于网页的[*代理*](/zh/glossary#Proxy)也存在一些缺点。它们不总是正确地显示页面，很多基于网页的[*代理*](/zh/glossary#Proxy)无法加载复杂的网页，包括那些以音频流和视频内容为特色的网页。还有，任何一个[*代理*](/zh/glossary#Proxy)在被大量使用时都会变慢，这在使用公共的网页[*代理*](/zh/glossary#Proxy)时更为明显。还有，理所当然地，基于网页的[*代理*](/zh/glossary#Proxy)只能用于网页。比如说您不可以通过一个基于网页的代理来使用即时通讯软件或者电邮客户端来访问被封锁的服务。最后，安全的网页[*代理*](/zh/glossary#Proxy)也只提供有限的保密性，因为它们必须经由您所访问的网站访问和修改返回给您的信息。不然的话，您点击一个链接的时候就不得不离开背后的[*代理*](/zh/glossary#Proxy)，直接访问目标网站。这点在下一节里会进一步讨论。

其他类型的[*代理*](/zh/glossary#Proxy)一般会要求您安装一个程序或者在您的浏览器或操作系统里配置一个外部[*代理*](/zh/glossary#Proxy)地址。第一种情况下，您的绕行软件通常会提供一些开启和关闭该工具的方法，告诉您的浏览器是否去使用[*代理*](/zh/glossary#Proxy)。如前面所说的，像这样的软件通常可以在一个[*代理*](/zh/glossary#Proxy)被封锁后自动更换。如果您必须在您的浏览器或操作系统里配置一个外部[*代理*](/zh/glossary#Proxy)地址，您要知道正确的[*代理*](/zh/glossary#Proxy)地址，它在被封锁或者变得太慢而无法使用的时候也可以更改。

尽管比起基于网页的[*代理*](/zh/glossary#Proxy)在使用上会稍微困难一些，这种绕行方法更可能正确显示复杂的网页，也不会在很多人开始使用某个[*代理*](/zh/glossary#Proxy)服务器时很快就变慢。此外，许多不同的互联网应用软件都可以配合[*代理*](/zh/glossary#Proxy)使用。例子包括浏览器的HTTP[*代理*](/zh/glossary#Proxy)，电邮和聊天程序的SOCKS[*代理*](/zh/glossary#Proxy)，还有可以重新引导您的所有网络流量以避开过滤的VPN[*代理*](/zh/glossary#Proxy)。

#### 安全代理与不安全的代理 ####

在本章，一个安全的[*代理*](/zh/glossary#Proxy)指的是任何能把从用户一方发起的连接进行[*加密*](/zh/glossary#Encryption)的[*代理*](/zh/glossary#Proxy)。一个不安全的[*代理*](/zh/glossary#Proxy)也允许你绕过许多类型的过滤，但如果您的互联网连接被扫描关键词或特定的网址，它就不能用了。通过一个不安全的[*代理*](/zh/glossary#Proxy)去访问一般会被[*加密*](/zh/glossary#Encryption)的网站是个特别坏的主意，例如电邮帐户和银行网站。这样做的话，您可能会暴露本来被隐藏的敏感信息。还有，正如前面所提到的，不安全的[*代理*](/zh/glossary#Proxy)通常比较容易被那些更新互联网过滤软件和政策的人发现和封锁。最后，免费、快速、安全的[*代理*](/zh/glossary#Proxy)的存在，意味着实在没什么理由去凑合着使用一个不安全的代理。

如果您可以通过[*HTTPS*](/zh/glossary#HTTPS)访问一个[*代理*](/zh/glossary#Proxy)页面，您就知道这个基于网页的[*代理*](/zh/glossary#Proxy)是安全的。电邮帐户可能支持安全与不安全的连接，所以您应该一定要使用安全的地址。通常，在这种情况下，您需要认可一个来自浏览器的“安全证书警告”才能继续使用。后面会讨论到的[*Psiphon*](/zh/glossary#Psiphon)和[*Peacefire*](/zh/glossary#Peacefire)[*代理*](/zh/glossary#Proxy)就是这种情况。这样的警告是告诉您，有人——可能是您的ISP或者黑客——可能正在监控您与[*代理*](/zh/glossary#Proxy)之间的连接。虽然会有这些警告，尽可能去使用安全的[*代理*](/zh/glossary#Proxy)仍然是个好主意。然而，在靠这种[*代理*](/zh/glossary#Proxy)来绕行的时候，您应该避免访问安全网站、输入密码或者交换敏感资料，除非可以验证[*代理*](/zh/glossary#Proxy)的[*SSL*](/zh/glossary#SSL)指纹。如果要这么做，您将需要联系[*代理*](/zh/glossary#Proxy)的管理员。

[*Psiphon用户手册*](https://sesawe.net/Using-psiphon-2.html)的*附录C*里说明了您和[*代理*](/zh/glossary#Proxy)的管理员应该遵循哪些步骤，以校验[*代理*](/zh/glossary#Proxy)的指纹。

不论您在访问这个[*代理*](/zh/glossary#Proxy)的时候有没有看到安全证书警告，甚至不论您跟[*代理*](/zh/glossary#Proxy)的运行者是否熟悉到可以在让浏览器认可警告之前校验到[*代理*](/zh/glossary#Proxy)服务器的指纹，您都应该避免通过一个基于网页的[*代理*](/zh/glossary#Proxy)来访问敏感资料，除非您信得过运行[*代理*](/zh/glossary#Proxy)的人。在使用一个单层[*代理*](/zh/glossary#Proxy)服务器来绕行的时候，它的管理员一定会知道您的[*IP地址*](/zh/glossary#IP_address)以及您要访问什么网站。然而，更重要的是，如果这个[*代理*](/zh/glossary#Proxy)是基于网页的，一个恶意的运作者可以取得所有通过您的浏览器和您所访问的网站的信息，包括您的电子邮件内容和您的密码。

对于非基于网页的[*代理*](/zh/glossary#Proxy)，您可能需要调查一下，以确定它是否支持安全连接。本章所推荐的所有[*代理*](/zh/glossary#Proxy)和匿名网络都是安全的。

#### 私密代理与公共代理 ####

公共[*代理*](/zh/glossary#Proxy)接受来自任何人的连接，而私密[*代理*](/zh/glossary#Proxy)则通常会要求用户名和密码的。公共[*代理*](/zh/glossary#Proxy)有着自由使用的显著优点，但假如能被轻易找到，它们可能很快变得过度拥挤。因此，即便公共[*代理*](/zh/glossary#Proxy)在技术的复杂程度和维护的力度上等同私密[*代理*](/zh/glossary#Proxy)，它们通常也比较慢。最后，私密[*代理*](/zh/glossary#Proxy)更倾向于如同营利事业一般运作，或者由管理员给他们直接或间接认识的用户创建帐户。因此，通常能更容易判断一个私密[*代理*](/zh/glossary#Proxy)的运作者的动机是什么。然而，您不应该认为私密[*代理*](/zh/glossary#Proxy)本质上更可信赖。毕竟，营利的目可能导致在线服务暴露它们的用户，这种事情曾经发生过。

简单的、不安全的公共[*代理*](/zh/glossary#Proxy)通常可以在搜索引擎上输入“公共[*代理*](/zh/glossary#Proxy)”这样的关键词找到，但您不应该依赖这样找到的[*代理*](/zh/glossary#Proxy)。如果能选择，最好还是使用一个私密且安全的[*代理*](/zh/glossary#Proxy)，并且是由您亲自认识和信任的人，或者声誉良好的人，拥有专业技术以确保他们的服务器安全的人来运作。是否使用一个基于网页的[*代理*](/zh/glossary#Proxy)，取决于您自己的具体要求与偏好。如在Firefox指南里所说的，在使用[*代理*](/zh/glossary#Proxy)来绕行的时候，用[*Firefox*](/zh/glossary#Firefox)浏览器并安装[*NoScript*](/zh/glossary#NoScript)浏览器扩展都是好主意。这样做可以帮助保护您抵御恶意[*代理*](/zh/glossary#Proxy)和那些试图找出您的真实[*IP地址*](/zh/glossary#IP_address)的网站。最后请记住，就算一个[*加密*](/zh/glossary#Encryption)的[*代理*](/zh/glossary#Proxy)，也不能使一个不安全的网站变得安全。在发送和接受敏感信息之前，您仍然必须确保用上了[*HTTPS*](/zh/glossary#SSL)连接。

如果您无法找到一个提供可靠、廉价、能在您国家访问到的[*代理*](/zh/glossary#Proxy)服务的个人、组织或公司，您应该像在前面的[*匿名网络*](/zh#Anonymity_networks)一节讨论过的那样，考虑使用Tor匿名网络。


