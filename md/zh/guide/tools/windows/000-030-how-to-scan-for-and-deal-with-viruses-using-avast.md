

---

lang: zh
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: How to Scan for and Deal with Viruses Using avast!

---

本页章节列表：

- [**4.0 开始前的准备**](#4.0)
- [**4.1 发现病毒时的简要处理指南**](#4.1)
- [**4.2 avast!主界面概述**](#4.2)
- [**4.3 如何扫描恶意软件和病毒**](#4.3)
- [**4.4 如何执行完整的系统扫描**](#4.4)
- [**4.5 如何执行文件夹扫描**](#4.5)
- [**4.6 如何执行开机扫描**](#4.6)
- [**4.7 如何处理病毒**](#4.7)
- [**4.8 如何使用病毒隔离区**](#4.8)
- [**4.9 高级病毒处理方式**](#4.9)

----
<aname="4.0"></a>
###4.0 开始前的准备###

用**avast!**处理恶意软件和其他病毒有两个主要步骤。第一步扫描您的电脑并检测出威胁。第二步是删除或是将病毒移入到**avast!** **病毒隔离区**。将恶意软件或病毒删除或移入到病毒隔离区可以有效地阻止它们感染其他计算机系统，例如文件系统或是电子邮件程序。

也许保留这些恶意软件或病毒看起来有点不正常，但如果病毒已经将自己捆绑到被感染的重要文件或敏感信息上，您也许希望尽可能恢复或保存这些被感染的文件。在极少数情况下，**avast!**可能会误报合法的代码或程序是恶意软件或病毒。这种情况一般被称为“主动错误信息”，这些被误报的代码或程序可能对您的系统很重要，您也许需要恢复它们。

**avast!** *病毒隔离区*是一个电子的“死亡区”或是“检疫隔离区”，在那里您可以通过互联网搜索或是发送样本到病毒试验室（*avast!*中的一个可选服务—使用方式：右击一个*病毒隔离区*中的病毒）从而检测病毒并发现它的潜在威胁。双击*病毒隔离区*中的一个病毒文件，*不会*激活或是运行恶意软件或病毒，因为*病毒隔离区*已经把它与您的系统完全隔离了。

**小窍门**：或者，您也可以把自己的重要或敏感信息放到**avast!** *病毒隔离区*来保证它的安全免受病毒攻击。

在这一章节您将会：

- 了解保护您的网络和个人计算机的最好做法；
- 了解主界面的使用，主要是扫描计算机和维护面板；
- 学习如何执行不同的扫描方式；
- 学习如何使用**avast!** *病毒隔离区*。

<aname="4.1"></a>
###4.1 发现病毒时的简要处理指南###

您可以采取很多预防措施来减少恶意软件对您的计算机系统的威胁。例如，避免浏览可疑的或有问题的网站；经常使用像**avast!**或**Spybot**这类杀毒或防间谍程序软件。有时我们需要共享一个局域网或互联网连接。下面的几点请在整个社区网络或工作网络受到病毒攻击时参考：

-把您的计算机连接物理性地从互联网或局域网中断开。如果您使用无线网络，把计算机从无线连接中断开。如果可能，关掉或卸去您的无线网卡。

-如果您的计算机在一个网络中，您应该先把网内所有计算机与互联网的连接断开，然后把计算机与本地网络断开。所有人都停止使用网络并开始运行**avast!**或是类似的可信任的杀毒软件来检测并清除病毒。这个过程看起来可能有点劳神费力，但这对保持网络的完整性以及个人计算机系统的安全性来说非常重要。

-为所有此网络上的计算机设置开机扫描。记下您所扫描到的病毒的名称，这样您就可以研究它们，然后清除或把它们移到**avast!** *病毒隔离区*。请参阅**4.6如何执行开机扫描**学习如何执行开机扫描。

-就算病毒文件被删除或修复，也仍然要重复上述的步骤在*所有*电脑上执行开机扫描直至**avast!**不再显示警告信息。根据恶意软件或是病毒攻击的严重性，您需要可能不只一次运行开机扫描。

更多关于如何处理恶意软件或是病毒的方式，请参阅章节**4.9高级病毒处理方式**。

<aname="4.2"></a>
###4.2 avast!主界面概述###

**avast!**主界面的左侧由四个选卡组成，分别是：摘要、扫描计算机、实时防护和维护。每一个选卡又可以分为若干个子选卡以打开相应的面板。

**第1步**：**点击**![](/sbox/screen/avast-zh/60.png)打开如下窗口：

![](/sbox/screen/avast-zh/61.png)

*示图1：摘要选卡显示目前状态，安全面板*

以下列表简要介绍四个选卡的功能：

**摘要**：这个选卡由*目前状态*和*统计*子选卡组成。*目前状态*子选卡显示**avast!**用于保护您计算机免受恶意软件和病毒攻击的关键组件的工作状态。*统计*面板显示**avast!**功能组件在过去的一周、一个月、一年里的活动。

**扫描计算机**：这个选卡由子选卡*立即扫描*、*开机扫描*和*扫描日志*组成。*扫描计算机*面板显示手动扫描的不同选项。*开机扫描*面板可以设置下次开机时的开机扫描，*扫描日志*以列表的方式显示不同的手动扫描记录。

**实时防护**：这个选卡显示从*文件防护*开始的保护计算机的各种功能的监测程序或“防护”，从这里可以打开实时防护的设置，包括停止和开打实时防护。

**维护**：这个选卡由*更新*、*注册*、*病毒隔离区*和*关于avast!*子选卡组成。*更新*面板可以手动升级程序和病毒库；*注册*面板可以注册您的*avast!*；*病毒隔离区*可以查看在扫描中被**avast!**检测到的恶意软件和病毒，您可以选择处理这些病毒的不同方式，包括：删除、重新扫描或发送到病毒实验室；*关于AVAST!*面板显示您计算机上的**avast!**版本。

**注意**：*扫描计算机*和*维护*面板在处理恶意软件和病毒时非常有用。

<aname="4.3"></a>
###4.3 如何扫描恶意软件和病毒###

在本章节，您将学习各个扫描选项的使用、如何执行完整的系统扫描和文件夹扫描，当然也会学习如何执行开机扫描。

*扫描计算机>立即扫描*面板显示四个**avast!**扫描选项。要打开这个窗口，执行如下步骤：

**第1步**：**点击**![](/sbox/screen/avast-zh/62.png)打开如下窗口：

![](/sbox/screen/avast-zh/63.png)

*示图2：扫描计算机选卡显示立即扫描面板*

以下的简要介绍将帮助您选择合适的扫描方式：

**快速扫描**：在用户时间比较紧的情况下，推荐此项来检测潜在的或可疑的威胁。

**完整的系统扫描**：在用户充足的情况下，推荐使用此项来执行一次对系统的彻底扫描。如果您在计算机上第一次使用杀毒软件，也推荐使用此项。此扫描所需要的时间取决于计算机上的文件、文件夹和硬盘的数量及计算机的速度。请参阅章节**4.4 如何执行完整的系统扫描**。

**可移动媒体扫描**：在扫描外置硬盘、USB闪存和其他媒体，特别是在这些媒体并不属于您的时候，推荐使用此项。它将扫描所有的可移动设备上会在设备连接时自动运行的有害程序。

**选择要扫描的文件夹**：在扫描单个或多个文件夹时，特别是当您怀疑某个文件或文件夹被感染时，推荐使用此项。请参阅章节**4.5 如何执行文件夹扫描**。

**小窍门**：每个扫描项都会显示扫描任务的细节，例如扫描的范围。**点击**![](/sbox/screen/avast-zh/84.png)来查看。如果您是经验比较丰富的高级用户或专家级用户，**点击**![](/sbox/screen/avast-zh/85.png)来自定义您每次病毒扫描任务的参数。

<aname="4.4"></a>
###4.4 如何执行完整的系统扫描###

按照如下步骤执行完整的系统扫描：

**第1步**：**点击** *完整的系统扫描*选项上的![](/sbox/screen/avast-zh/64.png)按钮，打开如下窗口：

![](/sbox/screen/avast-zh/65.png)

*示图3：正在扫描面板显示完整的系统扫描正在进行*

当完整的系统扫描完成后，如果在您的计算机上发现了威胁，*完整的系统扫描*面板会变成如下窗口：

![](/sbox/screen/avast-zh/66.png)

*示图4：扫描结束后显示检测到威胁的警告窗口*

完整的系统扫描显示发现了威胁；请参阅章节[**4.7 如何处理病毒**](/zh/avast-dealingwithviruses#4.7)来学习如何处理这些威胁。

**avast!** *病毒隔离区*是一个在**avast!**安装过程中创建的文件夹，它是电子的“死亡区”或“检疫隔离区”，在这里阻止病毒干扰或在您的计算机进程中运行。

<aname="4.5"></a>
###4.5 如何执行文件夹扫描###

要开始文件夹扫描，请执行以下步骤：

**第1步**：**点击**请选择要扫描的文件夹*中的![](/sbox/screen/avast-zh/64.png)打开如下窗口：

![](/sbox/screen/avast-zh/86.png)

*示图5：选择区域对话框*

您可以在*选择区域*对话框中选择您想要扫描的文件夹。您可以选择扫描一个或多个文件夹。点击每个文件夹前的选择框，相应的文件夹路径会显示在*选中路径：*文字框中。

**第2步**：**点击**![](/sbox/screen/avast-zh/87.png)开始扫描您选中的文件夹，打开如下窗口：

![](/sbox/screen/avast-zh/88.png)

*示图6：文件夹扫描正在进行*

**小窍门**：**avast!**扫描单个文件夹可以通过右击一个文件夹时出现的**微软**的弹出菜单来执行。只需**选择**您想扫描的文件夹名字后面出现的![](/sbox/screen/avast-zh/13.png)来进行扫描。

<aname="4.6"></a>
###4.6 如何执行开机扫描###

**avast!**开机扫描可以在**微软Windows操作系统**开始运行前进行全面的硬盘扫描。在开机扫描进行的时候，大多数的恶意软件和病毒仍然处于停止状态，因为它们还没机会被激活运行或与其他系统进程进行交互，这时可以更容易发现和清除病毒。

开机扫描可以直接读取硬盘，同时避开加载**Windows**的驱动程序和文件系统，这往往是大多计算机病毒最喜欢的攻击目标。这样可以扫描出最顽固的“rootkits”类型病毒——一种极其危险的恶意软件。即使在您只是有点怀疑计算机系统有可能被感染时，也**强烈推荐**您进行开机扫描。

推荐使用*开机扫描*选项对计算机系统进行完整全面的扫描。根据您硬盘上文件数量的多少和计算机的运行速度，开机扫描可能需要一些时间。*开机扫描*总是设定在下一次启动计算机时执行。

执行以下步骤来设定开机扫描：

**第1步**：**点击**![](/sbox/screen/avast-zh/67.png)来打开*开机扫描*面板。

**第2步**：**点击**![](/sbox/screen/avast-zh/68.png)来设定下一次开机时执行开机扫描。

**第3步**：如果您希望立即执行开机扫描，请**点击**![](/sbox/screen/avast-zh/69.png)。

**注意**：开机扫描在操作系统和界面载入之前就开始执行，因此只有一个蓝色屏幕显示如下的进度：

![](/sites/securitybkp.ngoinabox.org/files/u5/Avast_3_2_6.png)

*示图7：avast!开机扫描*

**avast!**每次检测到病毒都会出现提示，并等待您选择*删除*、*忽略*、*移动*或*修复*单个或全部病毒，建议您在任何情况下都*不要*忽略病毒处理。这个命令列表只有在检测到病毒时才会出现。

<aname="4.7"></a>
###4.7 如何处理病毒###

**avast!** *病毒隔离区*是一个在**avast!**安装过程中创建的文件夹。*病毒隔离区*是从您的计算机系统中独立出来的一个文件夹，用来存储杀毒软件扫描出来的恶意软件和病毒以及被感染的文件、文档和文件夹。

如果您已经升级过您的程序和病毒库，那您应该很熟悉*维护*选卡——从这里也能打开**avast!** *病毒隔离区*。

如果要开始处理在扫描中发现的恶意软件和病毒，请执行下列步骤：

**第1步**：**点击**![](/sbox/screen/avast-zh/70.png)打开如下窗口：

![](/sbox/screen/avast-zh/71.png)

*示图8：扫描结果窗口显示检测到威胁*

**第2步**：**点击**![](/sbox/screen/avast-zh/72.png)打开下处理病毒的下拉菜单，如上面的*示图8*所示。

**注意**：在本次操作中，我们要把感染的文件移入*病毒隔离区*，下拉菜单中的其他三个选项功能如下：

**修复**：这个选项会尝试修复被感染的文件。

**删除**：被感染文件将会被永久删除。

**不做处理**：这个选项顾名思义，*绝对不推荐*在处理有潜在危害的恶意软件或病毒时使用此项。

**第3步**：**选择** *移入病毒隔离区*并**点击**![](/sbox/screen/avast-zh/74.png)打开如下窗口：

![](/sbox/screen/avast-zh/75.png)

*示图9：成功将病毒移入病毒隔离区*

<aname="4.8"></a>
###4.8 如何使用病毒隔离区###

当病毒被移入**avast!** *病毒隔离区*后，您就可以从容不迫地考虑如何处理这些病毒了。

**第1步**：**点击**![](/sbox/screen/avast-zh/80.png)，然后**点击**![](/sbox/screen/avast-zh/81.png)打开如下窗口：

![](/sbox/screen/avast-zh/82.png)

*示图10：病毒隔离区中被隔离的病毒*

**第2步**：**右击**列表中的病毒，显示处理病毒的菜单列表，如下图所示：

![](/sbox/screen/avast-zh/83.png)

*示图11：病毒隔离区中的病毒处理弹出菜单*

**注意**：双击*病毒隔离区*中的病毒并不会激活或运行病毒，而只会显示病毒属性或是您在弹出菜单中查看*属性*时相同的信息。

弹出菜单中的各项病毒处理功能如下：

**删除**：此项将不可恢复地删除病毒文件。

**还原**：此项将把病毒还原到它最初的存储位置。

**提取**：此项将把文件或病毒复制到您指定的位置。

**扫描**：此项将在下一次扫描重新提交该病毒。

**提交至病毒实验室……**：此项将向已知病毒数据库提交病毒样本以进行深入分析。选择此项将打开一个提交表格，需要您填写然后发送。

**属性**：此项将会显示关于此病毒的更多细节信息。

**添加……**：使用此项可以浏览您的系统，并将您想要添加的文件移入*病毒隔离区*。此功能非常有用，当您在被突发病毒袭击时可以用来保护您的重要文件。

**刷新全部文件**：此项将更新您的文件列表，这样您就可以看到最新的文件。

<aname="4.9"></a>
###4.9 高级病毒处理方式###

有时候**avast!**、**Comodo防火墙**和**Spybot**提供的防护也不管用；不管再怎么小心，我们的系统还是会被恶意软件和病毒感染。在章节**4.1 发现病毒时的简要处理指南**中已经讲述了一些处理恶意软件和病毒的方法，但还有其他办法来消除您计算机中的病毒威胁。

**方法A：使用杀毒急救CD或DVD**

有一些杀毒软件公司提供免费的杀毒“急救”CD或DVD。这些文件可以以ISO镜像文件格式下载（这是一种可以被刻录成CD或DVD的文件格式）。

使用杀毒软件CD/DVD，请按下列步骤操作：

1. 下载并刻录杀毒软件CD。
*您可以使用免费刻录软件如[**ImgBurn**](http://www.imgburn.com/)来刻录镜像文件。*

2. 把光盘插入被感染的计算机CD/DVD光驱，然后用光驱重启您的计算机。
*通常，您可以在电脑开机时按键盘上的F10或F12键来选择启动位置，注意电脑刚开机时屏幕上的显示信息，学习如何在电脑上操作。*

3. 把您的系统重新接入互联网这样如果有需要的话杀毒软件可以自动升级它的病毒库，启动后杀毒软件将会扫描您的电脑硬盘来检测并清除病毒。

下面是一些急救CD镜像文件的链接：

-[**AVG急救CD**](http://www.avg.com/us-en/avg-rescue-cd)
-[**卡巴斯基急救CD**](http://support.kaspersky.com/viruses/rescuedisk/)
-[**F-Secure急救CD**](http://www.f-secure.com/linux-weblog/files/f-secure-rescue-cd-release-3.00.zip)
-[**BitDefender急救CD**](http://download.bitdefender.com/rescue_cd/)

您也可以在**Windows操作系统**启动后使用下面的工具来扫描您的计算机；不过这些工具只有在您的计算机没有被病毒感染到无法重启的情况下才能使用：

-[**HijackThis**](http://free.antivirus.com/hijackthis/)和**TrendMicro**公司的免费工具[Clean-upTools](http://free.antivirus.com/clean-up-tools/)。
-微软公司的[**RootkitRevealer**](http://technet.microsoft.com/en-us/sysinternals/bb897445.aspx)和[Sysinternals](http://technet.microsoft.com/en-us/sysinternals)。

**注意：**您可以分开使用以上这些工具以增强杀毒的效果。

**方法B：重新安装微软Windows操作系统**

***注意**：在您开始之前，要先确认您有相应的安装序列号，**Windows**系统安装盘和其他一些必需的软件安装文件。这个过程可能比较长，但在没有其他办法清除病毒的情况花这点时间是值得的。*

在极少数的情况下，感染上的病毒非常难以对付，之前推荐的软件工具都没办法清除它，这时我们推荐按下列的步骤来恢复计算机系统：

1. 备份您在计算机上的所有个人文件。

2. 格式化硬盘并重新安装**MicrosoftWindows**操作系统。

3. 在**MicrosoftWindows**操作系统安装成功后更新系统。

4. 安装**avast!**（或其他您喜欢的杀毒软件），并更新杀毒软件和病毒库。

5. 下载并安装您需要的其他软件的最新版本并全部更新。

**注意**：在任何情况下，都不要在上述这些步骤*完成前*将您的*备份文件*存储设备连接到计算机上，因为计算机可能被再次感染。

6. 连接您的备份文件存储设备到计算机，扫描这些文件来检测并清除存在的病毒或其他威胁。

7. 在您发现和清除病毒和其他威胁后，您可以从备份设备中复制您的文件到计算机硬盘上。


