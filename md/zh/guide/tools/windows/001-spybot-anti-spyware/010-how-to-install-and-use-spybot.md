

---

lang: zh
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: How to Install and Use Spybot

---

本页的章节列表：

- [**2.0 如何安装 Spybot**](#2.0)
- [**2.1 关于 Spybot**](#2.1)
- [**2.2 如何在首次使用 Spybot**](#2.2)
- [**2.3 如何更新 Spybot 的检测规则和免疫数据库**](#2.3)
- [**2.4 如何免疫您的系统**](#2.4)
- [**2.5 如何检测系统问题**](#2.5)
- [**2.6 Resident TeaTimer**](#2.6)
- [**2.7 如何使用恢复工具**](#2.7)

-------

<a name="2.0"></a>
## 2.0 如何安装 Spybot ##

**步骤1**：**双击**![](/sbox/screen/spybot-zh/01.png)；一个*“打开文件 – 安全警告”*的对话框可能会出现，如果是，**点击**![](/sbox/screen/spybot-zh/02.png)激活以下的页面：

![](/sbox/screen/spybot-zh/03.png)

*图1：选择安装语言对话框*

**步骤2**：**点击**![](/sbox/screen/spybot-zh/04.png)激活*安装向导 - Spybot Search & Destroy – 欢迎使用 Spybot - Search & Destroy 安装向导*页面。

**步骤3**：**点击**![](/sbox/screen/spybot-zh/05.png)激活*“授权协议”*页面。在开始余下的安装过程之前，请阅读*授权协议*。

**步骤4**：**勾选** *我同意协议*选项激活*下一步*按钮，然后**点击**![](/sbox/screen/spybot-zh/05.png)激活*选择目标文件夹*页面。

**步骤5**：**点击**![](/sbox/screen/spybot-zh/05.png)激活如下页面：

![](/sbox/screen/spybot-zh/06.png)

*图2：“选择组件”页面*

**步骤6**：**勾选**适当的组件如上面的*图2*所示，**点击**![](/sbox/screen/spybot-zh/05.png)激活*选择开始菜单文件夹*。

**步骤7**：**点击**![](/sbox/screen/spybot-zh/05.png) 使用默认的文件夹路径，激活*“选择附加任务”*页面。

**步骤8**：**点击**![](/sbox/screen/spybot-zh/05.png)，激活*准备安装*页面，然后**点击**![](/sbox/screen/spybot-zh/07.png)激活*安装*页面。

**步骤9**：**点击**![](/sbox/screen/spybot-zh/08.png)完成安装过程并启动**Spybot - Search & Destroy**。

<a name="2.1"></a>
## 2.1 关于Spybot##
 
要有效地使用**Spybot**，主要有两部分：

- 更新来自**Spybot**的最新的相关*检测规则*和*免疫数据库*升级。

- 运行**Spybot**。这涉及到使用检测规则和免疫数据库来免疫您的系统，或者使用您之前所下载的升级包来检测您的系统是否受到间谍软件感染，并移除它们。

**注**：请参阅[**3.0 高级选项**](/zh/spybot_advanced)，了解对关键的高级选项的简要概括。

<a name="2.2"></a>
## 2.2 如何首次使用Spybot##

*在您完成了安装与设置过程之后，* **Spybot** *会自动运行并显示*提示*页面，如下图*：

![](/sbox/screen/spybot-zh/09.png)

*图3：提示页面*

**注意**：下次再启动**Spybot**，**双击**![](/sbox/screen/spybot-zh/10.png)或**选择 开始 > 所有程序 > Spybot - Search & Destroy > Spybot - Search & Destroy**。

**步骤1**：**点击**![](/sbox/screen/spybot-zh/11.png)，激活*Spybot - Search & Destroy*（*图8*）和*创建数据库备份*的页面：

![](/sbox/screen/spybot-zh/12.png)

*图4：Spybot-S&D向导 创建注册表备份的页面*

**注意**：我们强烈建议您给注册表创建一个备份。关于**Windows注册表**的综述，请参看[**CCleaner**](//securityinabox.org/zh/ccleaner_windowsregistry#4.0)。

**步骤 2**：**点击** *图4* 中的![](/sbox/screen/spybot-zh/14.png)，创建并保存一个注册表备份。

**步骤3**：**点击**![](/sbox/screen/spybot-zh/15.png)，激活*Spybot – 检查更新*页面。如果您的电脑已连接到网络，请执行以下步骤：

**步骤4**：**点击**![](/sbox/screen/spybot-zh/16.png)，激活*检查更新*窗口，然后直接转到[**2.3 如何更新Spybot的检测规则和免疫数据库**](#2.3). 

- 如果您的电脑*没有*连接到互联网，请执行以下步骤：

**步骤5**：**点击**![](/sbox/screen/spybot-zh/17.png)，激活*现在就对系统免疫*窗口，按照如下步骤来完成对系统的免疫：

![](/sbox/screen/spybot-zh/18.png) 

*图5：免疫过程状态条*

**提示**：如果浏览器因为某些原因没有关闭，在免疫过程前会出现以下提示：

![](/sbox/screen/spybot-zh/19.png)

*图6：检测到未关闭的浏览器窗口*

**步骤6**：**关闭**浏览器窗口并**点击**![](/sbox/screen/spybot-zh/04.png)开始免疫过程

**步骤7**：**点击**![](/sbox/screen/spybot-zh/15.png)然后**点击**![](/sbox/screen/spybot-zh/22.png)回到 处于*免疫*模式中的*Spybot - Search & Destroy*控制面板。

![](/sbox/screen/spybot-zh/13.png)

*图 8：The Spybot - Search & Destroy控制面板*

<a name="2.3"></a>
## 2.3 如何更新Spybot的检测规则和免疫数据库##

**重要**：请务必保持**Spybot**的随时更新。

**步骤1**：在*Spybot-S&D*的左侧菜单栏中**点击**![](/sbox/screen/spybot-zh/23.png)激活*Spybot-S&D Updater*窗口，显示可下载更新的地址。

**步骤2**：**选择**距您最近的地点，然后在上面**点击右键**，再**选择** *Set this server as the preferred download location*选项，如*图9*所示。

- 如果您最近刚更新了检测规则，则会弹出**No newer updates are available**窗口。

- 如果您没有更新检测规则，则会出现*Spybot-S&D Updater*状态栏，显示可下载更新的服务器地址如下所示：

![](/sbox/screen/spybot-zh/24.png)

*图 9：The Spybot-S&D Updater窗口*

**步骤3**：**点击**![](/sbox/screen/spybot-zh/25.png)激活*Spybot-S&D Updater - Please select the updates to download here*窗口。

**步骤4**：**检查**所有可选项，然后**点击**![](/sbox/screen/spybot-zh/26.png)开始下载更新。

![](/sbox/screen/spybot-zh/27.png)

*图 10：The Spybot-S&D Updater显示设置的检测规则、帮助文件和免疫数据库*

**提示**：如果下载更新时出现了错误，**Spybot**允许您重新下载。在成功下载之后，会自动提示您进行系统免疫并检查系统问题，如下图：

![](/sbox/screen/spybot-zh/28.png)

*图 11：信息提示*

**步骤6**：**点击**![](/sbox/screen/spybot-zh/04.png)，然后**点击** ![](/sbox/screen/spybot-zh/29.png)。

*您将回到Spybot - Search & Destroy主菜单*

**提示**：您可以在任何时候对**Spybot**进行更新：**选择 开始 > 所有程序 > Spybot - Search&Destroy > Update Spybot -S&D**。

<a name="2.4"></a>
## 2.4 如何免疫您的系统##

**Spybot**可以“免疫”您的系统，使其不受已知间谍软件的侵害，就像预防疾病打的疫苗一样。

执行以下步骤来免疫您的系统：

**步骤1**：在**Spybot-S&D**侧栏中**点击**![](/sbox/screen/spybot-zh/30.png)或![](/sbox/screen/spybot-zh/31.png)来启动自动免疫进程，如*图 6*所示。

您可能需要最大化窗口来显示全部*免疫*项。

**提示**：如果您担心对系统进行免疫会对其运行效能造成影响，您可以还原或撤销免疫进程。可以通过**点击**![](/sbox/screen/spybot-zh/32.png)来撤销免疫进程，恢复系统之前的状态。

<a name="2.5"></a>
## 2.5 如何检测系统问题##

**提示**：在您开始检测潜在威胁之前，请更新**Spybot** *检测规则*以及*免疫数据库*。

按照以下步骤来检测系统问题以及威胁：

**步骤1**：**点击**![](/sbox/screen/spybot-zh/33.png)激活**Spybot** *Search and Destroy* 窗口。

**步骤2**：**点击**![](/sbox/screen/spybot-zh/34.png)开始检测系统威胁（视您电脑文件的多少，检测时间在20分钟到1小时之内)）。**Spybot**可能会出现以下窗口：

![](/sbox/screen/spybot-zh/35.png)

*图 12：The Spybot - Search & Destroy 程序在检测系统问题*

**步骤3**：**点击**![](/sbox/screen/spybot-zh/36.png)来检查系统问题，如下所示：

![](/sbox/screen/spybot-zh/37.png)

*图 13：The Spybot - Search & Destroy程序在检测系统问题*

*扫描结束后，将会出现如下列表，显示问题的种类、数量等*：

![](/sbox/screen/spybot-zh/38.png)

*图 14：The Spybot - Search & Destroy页面显示可能的问题及威胁*

**步骤 4**：**检查**您要删除的项目。有一些显示的项目可能是您出于某种原因要保留的商业软件。

**提示**：红色字体的项目通常是系统问题或威胁。绿色字体的项目是您的上网浏览记录。如果您想保留某个项目，请取消复选框中的相对项。

**重要**：无论您要删除还是忽略查出的恶意软件，我们都强烈推荐您查阅它们的相关特性及来源. 

**步骤5**：在**Spybot**右侧结果窗口中**点击**![](/sbox/screen/spybot-zh/39.png)以显示该项目的更多信息。如果这里没有信息显示，您可以上网查阅，了解它是如何运行，如何危害您电脑的安全的。对各种系统问题多加了解，可以让您更好地维护电脑安全隐私。

![](/sbox/screen/spybot-zh/40.png)

*图 15：The Spybot-S&D显示更多信息窗格*

**步骤6**：**点击**![](/sbox/screen/spybot-zh/41.png)删除恶意软件。

*一个要求确认的对话框会在此时出现，提醒您是否要删除所有检测到的问题。*

**步骤 7**：如果是，请**点击** *是*按钮。

**提示**：推荐应该一周检查一次系统问题。

<a name="2.6"></a>
## 2.6 Resident TeaTimer ##

**Resident TeaTimer**是**Spybot**的一个后台程序（就是说，即使您没有使用**Spybot**它也会在持续运行）。它会持续监控关键系统进程的运行，防止任何可能的威胁修改关键系统参数或设置。当**TeaTimer**检测到一个已知的恶意或可疑进程时，它会警告用户并提示，让用户选择*允许*或*阻止*该进程（如果证实是恶意程序）。下图是这种情况下的弹窗：

![](/sbox/screen/spybot-zh/42.png)

*图 16：The Spybot - Search & Destroy Resident TeaTimer警告，显示允许或阻止选项*

鉴于有很多程序（包括必要程序及恶意程序）都需要经由系统内部进程运行，**TeaTimer**会频繁地询问您*允许*或*不允许*进行这些改动。在这个示例中，软件提示您**Skype**正在被从**Windows 开始**菜单中删除。其实这种状况在您卸载了某软件后会经常发生。您可以允许这种类型的改动。

**提示**：如果您不了解**TeaTimer**窗口对您的一些建议，请**点击**![](/sbox/screen/spybot-zh/43.png)以查阅更多信息，如下图所示：

![](/sbox/screen/spybot-zh/44.png)

*图 17：Spybot - Search & Destroy 启动屏幕*

安全起见，如果您不确定某个请求可能带来的影响，请选择阻止它。如果您确定这是一个正当请求的话，请勾选*记住这次选择*选项，**Spybot**将不会再提示您相同的警告。

**提示**：在您新安装某个程序，且这个程序试图加入开机启动项的话，**TeaTimer**将会激活并提示您。在卸载程序时也会如此。

**提示**：我们强烈推荐，保持**TeaTimer**随时同步更新。

<a name="2.7"></a>
## 2.7 如何使用恢复工具##

*恢复*工具可以让您恢复或找回之前删除或修改的任何项目。**Spybot**会为之前删除的所有项目保存备份。如果发现删除某个恶意软件后，您的电脑不能正常运行，您就可以通过*恢复*工具来还原它。

请按照以下步骤来恢复之前删除的项目: 

**步骤1**：**点击**![](/sbox/screen/spybot-zh/45.png)激活*恢复*页面，如下所示：

![](/sbox/screen/spybot-zh/46.png)

*图 18：The Spybot Search & Destroy – 文件恢复页面* 

**步骤2**：**查找**您需要恢复之前删除的文件，然后**点击**![](/sbox/screen/spybot-zh/47.png)。

*会出现以下对话框提示您确认*：

![](/sbox/screen/spybot-zh/48.png)

*图 19：确认对话框*

**步骤 3**：**点击**![](/sbox/screen/spybot-zh/49.png)还原选定项目。

**步骤 4**：同样，**点击**![](/sbox/screen/spybot-zh/50.png)，彻底删除所有选中项目。这次被清除的项目将不可恢复。


