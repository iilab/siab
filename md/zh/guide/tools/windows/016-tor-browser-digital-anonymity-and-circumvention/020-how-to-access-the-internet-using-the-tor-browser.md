

---

lang: zh
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to access the Internet using the Tor Browser

---

本页项目列表：

- [**3.0 关于使用Tor网络**](#3.0)
- [**3.1 如何连接到Tor网络**](#3.1)
- [**3.2 如何手动验证您连接到Tor**](#3.2)
- [**3.3 如何使用Tor浏览互联网**](#3.0)
- [**3.3.1如何为使用Tor而更改Mozilla Firefox的设置**](#3.3.1)
- [**3.3.2 如何为使用Tor而更改Internet Explorer的设置**](#3.3.2)

-------

<a name="3.0"></a>
##3.0 关于访问Tor网络##
要开始匿名上网，您必须启动**Tor浏览器**程序。首先，它将您的系统连接到**Tor网络**。在您的电脑成功连接到**Tor**网络后，**Tor浏览器**将自动启动一个单独包含在**Tor浏览器软件包**里的**便携版Firefox**程序。 

**注**：这里存在匿名和速度之间的权衡。因为**Tor**提供匿名浏览，它肯定比您的电脑使用其他网页浏览器要慢一些。**Tor**通过世界各地志愿者的计算机运行您的通讯，以保护您的隐私和安全。

<a name="3.1"></a>
##3.1 如何连接到Tor网络##

要连接到**Tor**网络，请执行以下步骤：

**第1步**：**找到** *Tor浏览器*文件夹，然后**双击**![](/sbox/screen/tor-en/30.png)激活以下界面：

![](/sbox/screen/tor-zh/24.png)

*图1：Vidalia控制面板正连接到Tor网络*

*Vidalia控制面板*启动连接**Tor**网络时，一个类似于黄色洋葱的图标出现在*系统状态区*，显示如下：![](/sbox/screen/tor-en/31.png)。一旦您的计算机和**Tor**网络连接成功，该图标变为绿色：![](/sbox/screen/tor-en/32.png)。

**注**：要想学习如何有效地使用*Vidalia的控制面板*，请参阅[**如何配置Vidalia控制面板**](/zh/tor_vidaliaControlPanel)页。

几分钟后，**Tor浏览器**将启动一个**Mozilla Firefox**浏览器，界面显示如下：

![](/sbox/screen/tor-zh/33.png)

*图2：Mozilla Firefox中显示“您在使用Tor吗？”标签页*

每当您启动**Tor浏览器**程序，它会自动打开*Vidalia控制面板*（*图1*）和[**https://check.torproject.org/**](https://check.torproject.org/)（*图2*）界面。**Torbutton**扩展将出现在屏幕右下角，如下：![](/sbox/screen/tor-en/34.png)

**注**：但是，如果当您启动**Tor浏览器**时，已经打开了一个**Mozilla Firefox**浏览器，**Torbutton**会在这个浏览器窗口显示禁用模式，如下：![](/sbox/screen/tor-en/35.png)。

**Torbutton**用于配置**Firefox**以保证正确连接到**Tor**网络。只需**点击** **Torbutton**就可以启用或禁用它。

但是，如果您*没有*连接到**Tor**网络，**Torbutton**将处于禁用状态，出现如下界面：

![](/sbox/screen/tor-zh/36.png)

*图3：Mozilla Firefox显示“抱歉。你目前没有使用Tor”标签页*

如果您看到*图3*，**Torbutton**被禁用了（尽管您试图启用它），或者网页是空的，请参阅[**如何解决Tor的常见问题**](/zh/tor_troubleshooting)。

<a name="3.2"></a>


##3.2 如何手动验证您连接到Tor##

手动验证您是否连接到**Tor**网络，请执行以下步骤：

**第1步**：**打开**[**https://check.torproject.org/**](https://check.torproject.org/)网站。这将确认您是否连接了**Tor**网络。

如果您的网络浏览器通过**Tor**网络上网，在您的国家可能被阻止或限制访问的网站，现在可以浏览了，而且您的上网活动将保持私密和安全。您可能还注意到一些网页，如**www.google.com，**，偶尔会显示您的位置在其他国家。在使用**Tor**时，这是正常的。

<a name="3.3"></a>
##3.3 如何使用Tor浏览互联网##

虽然您通过**Tor**网络可以立刻使用**Firefox**浏览网站，我们建议您阅读以下有关配置**Firefox**的部分，以便完善保护您的在线隐私和安全。

<a name="3.3.1"></a>
### 3.3.1 如何为使用Tor而更改Mozilla Firefox的设置###

**Torbutton**是**Mozilla Firefox**的一个附加组件或扩展，它通过堵住**Mozilla Firefox**的某些漏洞来保护您的网上活动的匿名和安全的一个小程序。

**重要**：即使在您使用*Tor*时，恶意网站甚至是**Tor**的服务器*仍然*可以透露有关您的互联网位置和您在网上活动的信息。幸运的是，**Torbutton**的默认配置是比较安全的，但是，我们仍建议您修改以下设置，以便完善保护您的在线隐私和安全。

**注**：对浏览器相关的安全问题有深刻理解的**高级**用户可能会进一步改进这些设置。

*Torbutton偏好*窗口有三个选项卡，让您指定不同的选项：

- **代理设置**选项卡

- **安全设置**选项卡

- **显示设置**选项卡

无论在**Torbutton**处于禁用或启用状态，*Torbutton设置*窗口都可以使用。要激活*Torbutton选项*窗口，执行以下步骤：

**第1步**：**右击** **Torbutton**激活它的菜单，如下：

![](/sbox/screen/tor-zh/t4.png)

*图4：Torbutton菜单*

**第2步**：**选择** *偏好...*项目激活以下界面：

![](/sbox/screen/tor-zh/t5.png)

*图5：Torbutton选项窗口显示代理设置选项卡*

- **代理设置**选项卡

*代理设置*选项卡在**Torbutton**启动时，控制**Firefox**连接互联网。您不需要在此选项卡中更改任何内容。

- **安全设置**选项卡

*安全设置*选项卡是专为深入了解网络安全和网络浏览器**有经验**和**高级**用户设计的。它的默认设置为一般用户提供高度隐私。*安全设置*允许您在**Firefox**配置**Torbutton**管理浏览器历史记录、高速缓冲存储器、cookies和其他功能。

![](/sbox/screen/tor-zh/t6.png)

*图6：安全设置选项卡*

*Tor使用期间停止插件*选项是您可能需要启动的小部分安全设置，但也是*暂时*的。借助**Tor**显示在线视频内容 - 包括[**DailyMotion**](http://www.dailymotion.com/)、[**The Hub**](http://hub.witness.org/)和[**YouTube**](http://www.youtube.com) - 您必须选择**禁用** *使用Tor期间禁用插件*选项。

**注**：您应该只启用受信任网站的插件，并且在访问完这些网站后，您必须返回到*安全设置*选项卡，再次**启用** *使用Tor期间禁用插件*选项。

要了解*安全设置*选项卡每个选项具体功能的详细信息，请参阅[**Torbutton**](https://www.torproject.org/torbutton/)。

- **显示设置**选项卡

*显示设置*选项卡允许您选择如何在**Firefox**状态拦显示**Torbutton**，显示成![](/sbox/screen/tor-en/34.png)或![](/sbox/screen/tor-en/40.png)，还是![](/sbox/screen/tor-en/35.png)或![](/sbox/screen/tor-en/41.png)。无论您如何选择，它都会照常运行。

![](/sbox/screen/tor-zh/t7.png)

*图7：显示设置选项卡*

**提示**：当您浏览完毕，一定要删除网上的临时缓存和cookies。这可以通过在**Firefox** **选择 工具 > 清除最近浏览历史...**来实现，**选择**出现界面中的所有选项并**点击** *立即清除*按钮。要了解更多信息，请参阅**上手指南**的[**Mozilla Firefox**](/zh/firefox_privacy_and_security)一章。

要了解更多关于**Torbutton**的信息，请参阅[**Torbutton FAQ**](https://www.torproject.org/torbutton/torbutton-faq.html.en)。

<a name="3.3.2"></a>

### 3.3.2 如何为使用Tor而更改Internet Explorer的设置###

**注**：虽然**Tor**适用于任何网页浏览器，**Firefox**和**Tor**是为避免被敌对或恶意方察觉/发现的理想组合。**Internet Explorer**应是选择浏览器的下下之策！

但是，如果您一筹莫展，不得不使用**Internet Explorer**，请执行以下步骤：

**第1步**：**打开** **Internet Explorer**网页浏览器。

**第2步**：**选择工具 > Internet选项**激活*Internet选项*界面。

**第3步**：**点击** *连接*选项卡激活以下界面，如*图8*所示：

![](/sbox/screen/tor-en/43.png)

*图8：Internet选项界面的连接选项卡*

**第4步**：**点击**![](/sbox/screen/tor-en/44.png)激活*局域网（LAN）设置*界面如下：

![](/sbox/screen/tor-en/45.png)

*图9：局域网（LAN）设置*

**第5步**：**选择** *使用代理服务器...*选项，如*图9所示*，然后**点击**![](/sbox/screen/tor-en/46.png)激活*代理设置*界面。

**第6步**：**完成**代理设置，如下所示：

![](/sbox/screen/tor-en/47.png)

*图10：已完成代理设置界面实例*

**第7步**：**点击**每一步设置界面的![](/sbox/screen/tor-en/07.png)退出**Internet选项**窗口，并返回**Internet Explorer**浏览器。

**注**：您需要重复**第1步到第4步**来停止使用**Tor**。**第5步**，您应该**禁用** *使用代理服务器...*选项。

**提示**：在完成浏览会话后，您必须通过执行以下步骤删除临时的Internet缓存、cookies和浏览历史记录：

**第1步**：**选择工具 > Internet选项**显示默认*常规*选项卡，如下：

![](/sbox/screen/tor-en/48.png)

*图11：Internet Explorer的常规选项卡*

**第2步**：**点击**![](/sbox/screen/tor-en/49.png)*Temporary Internet files*文档，激活*删除cookies*确认对话框如下：

![](/sbox/screen/tor-en/50.png)

*图12：删除cookies确认对话框*

**第3步**：**点击**![](/sbox/screen/tor-en/07.png)删除Internet cookies。

**第4步**：**点击**![](/sbox/screen/tor-en/51.png)激活*删除文件*确认对话框，然后**点击**![](/sbox/screen/tor-en/53.png)）删除临时Internet文件。

**第5步**：**点击**![](/sbox/screen/tor-en/52.png)激活*Internet选项*确认对话框，**点击**![](/sbox/screen/tor-en/53.png)，然后**点击**![](/sbox/screen/tor-en/07.png)。

**注：**通过**Tor**网络使用**Internet Explorer**,您必须保持**Tor浏览器**和**Vidalia**共同运行并连接到Tor网络。


