

---

lang: zh
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: How to Use the NoScript Add On

---

本页的项目列表:

- [**4.0 关于 NoScript**](#4.0)
- [**4.1 如何使用 NoScript**](#4.1)
- [**4.2 关于点击劫持跨网页脚本（XXS）攻击**](#4.2)

-------

<a name="4.0"></a>
## 4.0 关于NoScript##

![](/sites/securitybkp.ngoinabox.org/files/u9/noscript.png)

**NoScript**是一个非常有用的**扩展**，它可以用来保护您的电脑不受恶意网站的侵袭。这个组件允许您设置一个“白名单”（信任列表）来将您所信任的安全网站放在里面，此外其他一切网站都会被视作具有潜在威胁，从而受到功能限制。只有在您确认一个网站的内容不具威胁时，您才可以将其放进“白名单”。

**NoScript**会自动屏蔽所有横幅广告、弹出广告、**JavaScript**和相关的**Java**代码，以及其他具有潜在威胁的网页特性。但是**NoScript**不能分辨恶意内容以及网页显示所必须的内容。所以您必须根据自身需要作出判断。

<a name="4.1"></a>
## 4.1 如何使用NoScript ##

在您开始使用**NoScript**之前，请确认其正确安装。**选择 工具 > 附加组件**来打开*附加组件*窗口，以确认其安装。

**提示**：尽管 **NoScript**一开始会让您不适应（可能造成一些您以前访问的网站不能正常显示），但您很快就会从它的自动目标拦截功能中受益，它会阻截烦人的广告、弹窗信息以及网页中植入的恶意代码。

**NoScript**会自动在后台运行。当其发现诸如**JavaScript**、**Adobe Flash**等类似脚本内容时，**NoScript**就会阻止其显示，并在**火狐**浏览器下方出现以下状态条：

![](/sbox/screen/firefox-zh/37.png)

*图1：The NoScript status bar*

**NoScript**状态条显示当前拦截到系统正在执行的*目标*（比如广告或弹窗）以及*脚本*。下面两个图显示**NoScript**是怎样起作用的：在*图 2*中，**Noscript**成功拦截了一个商业网站的**Adobe Flash Player**广告信息：
![](/sbox/screen/firefox-zh/38.png)

*图 2：Noscript成功拦截了一个商业网站的弹出广告*

在*图 3*中，**Twitter**网页提示您必须启用（至少临时启用）**JavaScript**支持才能正常显示网页。

![](/sbox/screen/firefox-zh/39.png)

*图 3：Twitter 提示需要JavaScript支持*

由于**NoScript**不能分辨恶意代码与真实代码，一些关键特性或是功能（比如状态栏）将无法正常运行。有时候，有些网站的显示内容，包括类脚本内容等，来源于多个网站。比如，**www.youtube.com**这样的网站就有三处的脚本源：

![](/sbox/screen/firefox-zh/40.png)

*图 4：NoScript状态栏的选项菜单*

这种情况下，如果要解除对脚本内容的限制，请**选择** *临时允许[网站名称]*选项（对于Youtube来说就是*临时允许youtube.com*）。如果这样做，网站内容仍然不能正常显示的话，您就要经过一系列的尝试，选出您想浏览的内容所需要的显示的网站。就**Youtube**而言，您仅需**选择** *临时允许youtube.com*和*临时允许ytimg.com*两个选项就可使其正常工作。

**警告！**：在任何情况下都不要选择：*全局允许脚本（危险）*选项。尽量避免选择*允许本页面所有对象*选项。有些时候，您可能需要允许网站全部脚本以使其正常运行；这种情况下，请确定您正在使用的网站确实可靠，并仅仅暂时性的使用这一功能直到浏览过程结束。因为恶意代码的*一次*感染就有可能使您的安全隐私信息泄露。

<a name="4.2"></a>
## 4.2 关于点击劫持跨网页脚本（XXS）攻击##

您可以通过**NoScript**来保护您的系统免受*跨网站脚本写入*以及*点击劫持*的攻击。*跨网站脚本写入*利用电脑安全的某个弱点，使黑客或入侵者在已有网页中植入恶性代码。*点击劫持*则可以这样来解释：当您点击一个按钮来执行某个命令的时候，它会自动执行另外一个嵌入代码或者脚本程序。除非您使用了**NoScript**，否则您可能无法意识到这两种攻击在进行。

每当一个点击劫持攻击被发动或正在运行时，一个类似下面的窗口就会出现：

![](/sbox/screen/firefox-zh/41.png)

*图 5：一个潜在的点击劫持/用户命令重定向企图 窗口* 

按照窗口的指示来化解*点击劫持*企图，然后**点击**
![](/sbox/screen/firefox-zh/15.png)。

