

---

lang: zh
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: Using the Tor Browser

---

本页项目列表：

- [**4.0 关于Vidalia控制面板**](#4.0)
- [**4.1 如何查看Tor的连接**](#4.1)
- [**4.2 如何查看和配置Vidalia控制面板设置**](#4.2)
- [**4.3 如何停止和启动Tor程序**](#4.3)

-------

<a name="4.0"></a>
##4.0 关于Vidalia控制面板##

您现在熟悉的*Vidalia控制面板*是**Tor**程序的主控制台。*Vidalia控制面板*允许您配置重要的**Tor**设置、查看连接参数。要打开**Vidalia控制面板**，请按以下说明进行操作：

**如果您正在运行Tor浏览器**，**双击**![](/sbox/screen/tor-en/32.png)启动*Vidalia控制面板*。

**提示**：如果您右击绿色洋葱形状的图标，*Vidalia控制面板*会以一个弹出的菜单的格式出现，如下所示：

![](/sbox/screen/tor-en/73.png)

*图1：Vidalia控制面板弹出菜单*


**如果您没有运行Tor浏览器**，**前往** **Tor浏览器**文件夹，然后**双击**![](/sbox/screen/tor-en/60.png)激活*Vidalia控制面板*，并自动连接到**Tor**网络，如下所示：

![](/sbox/screen/tor-zh/v2.png)

*图2：Vidalia控制面板显示成功连接到Tor网络*

<a name="4.1"></a>
##4.1 如何查看Tor的连接##

**第1步**：**点击**![](/sbox/screen/tor-en/62.png)激活以下界面：

![](/sbox/screen/tor-zh/v3.png)

*图3：Tor网络地图*

*Tor网络地图*列出了所有可用的**Tor**轮换服务器，其中包括当前运行的**Tor**匿名网络。左侧边栏列出这些可用的带宽和地理位置的服务器。

- **点击**![](/sbox/screen/tor-en/64.png)列出这些按照递增或递减可用带宽的服务器顺序，或以它们所在国的字母顺序列出。

世界地图下方有两个方框，*连接*框和轮换细节框。在*连接*框显示您的匿名连接路径所通过的随机选择的**Tor**服务器。

- **选择**一个在*连接*列表中的服务器，查看在地图中由绿线连接的您通过**Tor**网络的实际路径。

相邻的方框显示列在左侧边栏的*轮换*名单中一个服务器连接的细节，*图3*所示，显示一个加拿大轮换服务器*settingOrange*的连接细节。

**注**：*Tor网络地图*通过视图呈现相当抽象的概念和复杂的信息，以阐明*Tor*是如何运行的。

<a name="4.2"></a>
##4.2 如何查看和配置Vidalia控制面板设置##

**第1步**：**点击**![](/sbox/screen/tor-en/65.png)激活以下界面：

![](/sbox/screen/tor-zh/v4.png)

*图4：在Vidalia控制面板中设置界面*

*常规*选项卡允许您设定是否在**Windows**系统启动时运行**Vidalia**，然后是否运行**Tor**程序。

如果您喜欢手动启动**Vidalia**程序，只需**点击**禁用*系统启动时运行Vidalia*选项。

**注**：推荐**入门**或**一般**水平的用户接受默认设置，如*图4*所示。

**第2步**：**点击**![](/sbox/screen/tor-en/67.png)确认您的设置。

虽然**Tor**程序的默认语言是英文，*外观*选项卡允许您为*Vidalia控制面板*指定另一种语言。它还可以让您修改它的外观。

![](/sbox/screen/tor-zh/v5.png)

*图5：Vidalia面板的外观选项卡*

<a name="4.3"></a>

##4.3 如何停止和启动Tor程序##

**第1步**：**点击**![](/sbox/screen/tor-en/69.png)*Vidalia快捷*面板停止运行**Tor**程序；*Vidalia控制面板* *状态*区域显示如下：

![](/sbox/screen/tor-zh/v6.png)

*图6：Tor状态区域 - Tor未运行*

**第2步**：**点击**![](/sbox/screen/tor-en/71.png)启动**Tor**程序；几秒钟以后，*Vidalia控制面板* *状态*区域将显示如下：

![](/sbox/screen/tor-en/72.png)

*图7：Tor状态区域 - 连接到网络！*


