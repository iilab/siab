

---

lang: zh
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 001
title: Spybot - Anti-Spyware

---

**主页**

[**www.safer-networking.org/cs**](http://www.safer-networking.org/cs)

**电脑要求**

- Windows所有版本

**本指南中使用的版本**

- 1.6.2

**授权许可**

- 免费软件

**要求阅读**

**指引手册** [**第一章：如何保护您的计算机免受恶意软件和黑客侵害**](/zh/chapter-1)

**级别**：1：入门，**2：一般**，3：中等，4：有经验的，5：高级

**上手时间**：20 分钟

**您将得到**：

- **移除**不同种类的恶意软件和（或）间谍软件的能力。
- 在您的电脑系统被恶意的问题和威胁感染之前获得**免疫**的能力。


**GNU/Linux、Mac OS和其他Microsoft Windows兼容的程序**

在**GNU Linux**和**Mac OS**操作系统上，目前其实并没有恶意软件（间谍软件、病毒等等）。要自我保护，我们建议您：**1）**定期升级您的操作系统，和安装在上面的所有程序； **2）**使用[*Avast*](/zh/avast)一章里列出的反病毒软件；**3）**使用[*Comodo*](/zh/comodofirewall_main)一章里列出的防火墙软件；**4）**使用一个像[*Firefox*](/zh/firefox)这样的安全浏览器，和可以防止在网页被开启时下载任何脚本的[*NoScript*](/zh/firefox_noscript)扩展。这些预防措施能保证您的**GNU Linux**或**Mac OS**电脑受到很好的保护。

运行**Microsoft Windows**的电脑，其安全状况则很不一样。每天都有数以千计的新型恶意软件被创造出来。攻击方法也变得越来越复杂。对于运行**Microsoft Windows**的电脑，前一段里描述到的预防措施是**必须遵循**的。除此之外，我们强烈推荐本章里描述到的**Spybot**。

然而，如果已经采取了这些预防措施，您的电脑仍然受到了感染，而您发现还需要其他工具，我们推荐以下这些：

1. 安装[**SuperAntiSpyware**](http://superantispyware.com)，更新恶意软件定义库，然后扫描您的电脑。

2. 安装[**Malwarebytes Anti-Malware**](http://www.malwarebytes.org/mbam.php)，执行一次快速扫描，当完成后再进行一次正常扫描，移除在结果中显示的检测到的恶意软件。

3. 使用其他免费反间谍软件程序，如[**Microsoft Windows Defender**](http://www.microsoft.com/windows/products/winfamily/defender)、[**Ad-Aware Internet Security**](http://www.lavasoft.com/) 或 [**SpywareBlaster**](http://www.javacoolsoftware.com/spywareblaster.html)。


### 1.1 在开始之前您必须先了解这款工具###

**Spybot S&D**是一款受欢迎的免费程序，用于检测和移除您电脑上不同种类的广告软件、恶意软件和间谍软件。一旦安装了 **Spybot**，它还能使您的系统免疫于广告软件、恶意软件和间谍软件，不让它们感染您的电脑。

广告软件是会在您的电脑上显示广告资料的软件。某些种类的广告软件运作起来很像间谍软件，会侵袭您的隐私与安全。

恶意软件（如木马和蠕虫）是未经您的同意或在您不知晓的情况下，损害或劫持您的电脑运作的程序。

间谍软件是会采集数据、观察和记录您的隐私信息，跟踪您的上网行为的软件。跟恶意软件一样，它频繁地在您的电脑里秘密运行。因此，安装一个像**Spybot**这样的软件会帮助您保护您的系统还有您自己。

**Spybot**还会安装一个附加的应用程序，叫**TeaTimer**。它会保护您的电脑免受新型恶意软件的感染。

**注**：**Windows Vista**上有它自带的反间谍软件程序**Windows Defender**。然而，**Windows Vista**似乎允许**Spybot**正常工作而不引起冲突。


