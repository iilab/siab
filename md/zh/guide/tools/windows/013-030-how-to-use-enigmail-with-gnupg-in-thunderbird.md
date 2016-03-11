

---

lang: zh
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: How to Use Enigmail with GnuPG in Thunderbird

---

本页的项目列表:

- [**4.0 概览：Enigmail， GnuPG以及个人、公开密钥加密**](#4.0)
- [**4.1 如何安装Enigmail 和GnuPG**](#4.1)
- [**4.2 如何生成密钥对，以及将Enigmail应用于您的电邮**](#4.2)
- [**4.3 如何更换公开密钥**](#4.3)
- [**4.4 如何验证并签署密钥对**](#4.4)
- [**4.5 如何加密或解密邮件**](#4.5)

-------

<a name="4.0"></a>
## **4.0 概览：Enigmail、GnuPG以及个人、公开密钥加密**##

**Enigmail**是**Mozilla Thunderbird**的附加组件，它可以有效保护您邮件通讯的隐私。其实，**Enigmail**只是提供了一个平台，真正发挥作用的是**Thunderbird**中的**GnuPG**加密技术。在**Thunderbird**工具栏中，**Engimail**相关工具位于*OpenPGP*选项里。

**Engimail**基于一种名为[**公钥加密**]的技术(http://en.wikipedia.org/wiki/Public-key_cryptography)。这种技术要求每个用户都需要生成自己的密钥对。第一种密钥叫做*私有密钥*，它通过某个密码或者口令等实行保护，这个密码*不能*和*其他人*分享。

第二种密钥叫做*公开密钥*，可以与您的联系人进行分享。一旦您知道某位联系人的*公开密钥*，您就可以给这个人发送加密的电子邮件。但是，只有她一个人可以解密并阅读您的邮件，因为她是唯一可以获得匹配的*私有密钥*的人。

同样，如果您把自己的*公开密钥*分享给邮件联系人，并且不公开匹配的*私有密钥*，那么只有您可以阅读来自这些联系人的加密信息。

**Enigmail**也可以给您的邮件附上*数字签名*。如果收信人有一份您的有效公开密钥，他就可以知道这封邮件的来源，并且其内容也不会在发送途中被篡改。同样，如果您有另一个人的公开密钥，您也可以识别她信息上的*数字签名*。

<a name="4.1"></a>
## 4.1 如何安装Enigmail以及GnuPG##

关于如何下载**Enigmail**和**GnuPG**，请参照[**下载章节**](http://securityinabox.org/en/thunderbird_main)。

### 4.1.1 如何安装GnuPG###

安装**GnuPG**非常简单，与其他软件的安装过程十分相似。

安装**GnuPG**请按照如下步骤：

**步骤1**：**双击**![](/sbox/screen/thunderbird-en/40.png)开始安装。可能会出现*打开文件-安全警告*的对话框，请**单击**![](/sbox/screen/thunderbird-en/02.png)开启以下界面：

![](/sbox/screen/thunderbird-en/41.png)

*图1：GNU Privacy Guard安装向导*

**步骤2**：**单击**![](/sbox/screen/thunderbird-en/04.png)打开*GNU Privacy Guard Setup - License Agreement*许可协议；看完以后，**单击**![](/sbox/screen/thunderbird-en/04.png)打开*GNU Privacy Guard Setup - Choose Components*窗口。

**步骤3**：**单击**![](/sbox/screen/thunderbird-en/04.png)接受默认设置，并打开*GNU Privacy Guard Setup - Install Options - GnuPG Language Selection*语言选择窗口。

**步骤4**：**单击**![](/sbox/screen/thunderbird-en/04.png)选择*zh_CN - Chinese (simplified)*简体中文作为安装语言，然后打开*Choose Install Location*安装路径窗口。

**步骤5**：**单击**![](/sbox/screen/thunderbird-en/06.png)接受默认安装路径设置，然后打开*Choose Start Menu Folder*界面。

**步骤6**：**单击**![](/sbox/screen/thunderbird-en/06.png)开始解压安装**GnuPG**。安装完成后，会出现*Installation Complete*窗口。

**步骤7**：**单击**![](/sbox/screen/thunderbird-en/04.png)，然后再单击![](/sbox/screen/thunderbird-en/08.png)完成**GnuPG**的安装。

### 4.1.2 如何安装Enigmail###

在成功安装**GnuPG**软件后，您就可以安装**Enigmail**附加组件了。

安装**Enigmail**请执行以下步骤：

**步骤1**：**打开Thunderbird**，然后**选择Tool > 附加组件**打开*附加组件*窗口。您可以看到上面的*获取附加组件*选项。

**步骤2**：**单击**![](/sbox/screen/thunderbird-en/44.png)开启以下界面：

![](/sbox/screen/thunderbird-en/45.png)

*图3：附加组件窗口下的扩展选项*

**步骤3**：**单击**![](/sbox/screen/thunderbird-en/46.png)开启以下界面：

![](/sbox/screen/thunderbird-en/47.png)

*图4：选择要安装的扩展*

**步骤4**：找到您放置**Enigmail**的路径，然后**单击**![](/sbox/screen/thunderbird-en/48.png)开启以下界面：

![](/sbox/screen/thunderbird-en/49.png)

*图5：软件安装提示*

**重要**：在开始这步之前，确认您已经保存了所有的在线文件！

**步骤7**：**单击**![](/sbox/screen/thunderbird-en/50.png)，如**图5*所示，然后**单击**![](/sbox/screen/thunderbird-en/51.png)完成**Enigmail**的安装。

要检查**Enigmail**扩展是否已经成功安装，回到**Thunderbird**主界面查看**Thunderbird**工具条里面是否有*OpenPGP*选项。

![](/sbox/screen/thunderbird-en/52.png)

*图6：Thunderbird工具条，显示OpenPGP选项*

**译者注**：最新的**Thunderbird**汉化版本3.1.1不支持最新版本的**Enigmail**以及**GnuPG**，若要使用最新版的**Enigmail**，请使用5.0以上版本的英文**Thunderbird**。以下帮助内容均以英文版**Thunderbird**5.0为准。


### 4.1.3 如何确认Enigmail和GnuPG在正常运行###

在您开始使用**Enigmail**和**GnuPG**来认证以及加密您的邮件时，首先您要确定它们可以共同正常工作。

**步骤1**：**选择OpenPGP > Preferences**打开*OpenPGP Preferences*界面，如下所示：

![](/sbox/screen/thunderbird-en/53.png)

*图7：OpenPGP偏好设置界面*

如果**GnuPG**已经成功安装，![](/sbox/screen/thunderbird-en/54.png)会出现在*Files and Directories*的选项中；或者，您可能会看到一个弹出提示，如下所示：

![](/sbox/screen/thunderbird-en/55.png)

*图8：OpenPGP Alert弹出信息*

**提示**：如果您看到了这个提示，说明您的文件安装地址有误。**勾选** *Override with*选项以激活*Browse...*按钮，然后**单击**![](/sbox/screen/thunderbird-en/69.png)打开*Locate GnuPG program*，并手动找到您安装*gpg.exe*文件的路径。

**步骤2**：**单击**![](/sbox/screen/thunderbird-en/56.png)回到**Thunderbird**主界面。

<a name="4.2"></a>
## 4.2 如何生成密钥对，以及将Enigmail应用于您的电邮##

当确认**Enigmail**以及**GnuPG**可以正常工作后，您就可以通过**Enigmail**来给电子邮件设置多个个人、公开密钥对了。

### 4.2.1 如何通过OpenPGP向导生成密钥对###

**Enigmail**有两种生成密钥对的方法；第一种是通过*OpenPGP安装向导*，第二种是通过*密钥管理*界面。

第一次使用*OpenPGP安装向导*来生成密钥对，请执行以下步骤：

**步骤1**：**选择OpenPGP > 安装向导**打开*OpenPGP安装向导*界面，如下所示：

![](/sbox/screen/thunderbird-en/58.png)

*图9：欢迎来到OpenPGP安装向导界面*

**步骤2**：**单击**![](/sbox/screen/thunderbird-en/04.png)开启以下界面：

![](/sbox/screen/thunderbird-en/59.png)

*图 10：选择用户身份界面*

**步骤3**：**单击**![](/sbox/screen/thunderbird-en/04.png)开启以下界面：

![](/sbox/screen/thunderbird-en/60.png)

*图11：签名 - 给您的邮件提供数字签名界面*

**步骤4**：**单击**![](/sbox/screen/thunderbird-en/04.png)开启以下界面：

![](/sbox/screen/thunderbird-en/61.png)

*图12：加密选项 - 加密您发出的邮件界面*

**步骤5**：**单击**![](/sbox/screen/thunderbird-en/04.png)开启以下界面：

![](/sbox/screen/thunderbird-en/62.png)

*图13：偏好设置 - 更改您的邮件设置，使OpenPGP运行更加安全界面*

**步骤6**：**单击**![](/sbox/screen/thunderbird-en/63.png)开启以下界面：

![](/sbox/screen/thunderbird-en/64.png)

*图14：偏好设置界面*

**注意**：在*3.3 如何禁用Thunderbird的HTML特性*这一章节里，我们简单向您介绍了HTML中的信息对您的电脑有何危害。*以纯文本形式浏览消息*选项还有*不要加载HTML信息*选项都是为此而设计的：

**步骤7**：**单击**![](/sbox/screen/thunderbird-en/56.png)回到*OpenPGP安装向导*，然后**单击**![](/sbox/screen/thunderbird-en/04.png)打开*Create Key - Create A Key To Sign and Encrypt Email*窗口。

**注意**：首次为某一邮件地址设置密钥的时候，下拉栏里不会有其他的邮件地址显示。

**步骤8**：在每个*密码*栏中**键入**最少8位字符的密码。

![](/sbox/screen/thunderbird-en/65.png)

*图15：Create Key – Create A Key To Sign and Encrypt Email窗口*

**步骤9**：**单击**![](/sbox/screen/thunderbird-en/04.png)以确认这些设置，然后**单击**![](/sbox/screen/thunderbird-en/66.png)回到*Create a Key*界面；您会看到刚才设置的电子邮件地址，如下所示：

![](/sbox/screen/thunderbird-en/67.png)

*图16：新创建的Account/User ID*

**步骤4**：**单击**![](/sbox/screen/thunderbird-en/04.png)打开*Summary*界面，显示一些生成密钥对的相关选项。

**注意**：所有使用*OpenPGP安装向导*生成的密钥对都是一个2048比特的文件，它有5年的使用期限。使用这种方法生成密钥对的话，其上述属性均不能更改。

### 4.2.2 如何生成附加密钥对，以及取消对其他邮件账户的授权###

默认设置下，每个电子邮件账户都会有一个独立的密钥对。如果想要为其他邮件账户设置附加的密钥对，请按照下文所述的步骤。此外，*取消授权*也是密钥对中的一种功能。您可以向您的联系人发送一份证书，来取消某个公开密钥的使用，以防您的私有密钥失窃或无法使用等情况。


**步骤1**：**选择OpenPGP > Key Management**开启以下界面：

![](/sbox/screen/thunderbird-en/70：png)

*图17：OpenPGP密钥管理Generate菜单，选择New Key Pair*

**注意**：**勾选** *Display All Keys by Default*可以看到刚才使用*OpenPGP安装向导*为您首个邮件账户设置的密钥对，如上文**图17*所示。

**步骤2**：**选择Generate>New Key Pair**如上文**图17*所示，以开启以下界面：

![](/sbox/screen/thunderbird-en/71.png)

*图18：The Generate OpenPGP Key界面*

**步骤3**：从*Account/User ID*下拉栏中**选择**一个邮件地址，并**勾选**the*Use generated key for the selected identity*选项，为您的私有密钥创建一个密码口令。

**注意**：密码口令实际上就是一个长度更长的密码：**Enigmail**只是希望您输入一个比普通密码更长的密码，以保证账户安全。

**重要**：生成密钥对时一定要使用密码口令，而且*绝不要*启用"no passphrase"（不使用密码口令）选项。

![](/sbox/screen/thunderbird-en/72.png)

*图19：The Generate OpenPGP Key显示的密钥有效时间选项表*

**注意**：密钥对的有效使用时间完全取决于您所需要的安全等级。密钥对更换的越频繁，新的密钥对也就越难以被破解。但是每次您更换密钥对的时候，您也需要通知您的共享对象，并经过他们的确认后方可继续使用。

**步骤5**：**键入**合适的数字，然后**选择**您认为合适的时间单位（*天*、*月*或*年*）这些是密钥对的有效持续时间：

**步骤6**：**单击**![](/sbox/screen/thunderbird-en/73.png)开启以下界面：

![](/sbox/screen/thunderbird-en/74.png)

*图20：OpenPGP Confirm对话框*

**步骤7**：**单击**![](/sbox/screen/thunderbird-en/73.png)开启以下界面：

![](/sbox/screen/thunderbird-en/75.png)

*图 21：OpenPGP 提示确认 对话框*

**步骤8**：**单击**![](/sbox/screen/thunderbird-en/76.png)打开*Create & Save Revocation Certificate*设置窗口。

**注意**：一旦您发现公开密钥可能被恶意用户方非法闯入，或者您无法使用这个密钥登陆的话，您可以向联系人发送一封取消授权证书，让他们不再使用与您匹配的那个公开密钥。如果您的电脑不幸丢失，被窃或被收缴的话，您将会需要这项功能。所以我们强烈建议在不同电脑上备份取消授权证书。

![](/sbox/screen/thunderbird-en/77.png)

*图22：The OpenPGP Alert确认界面*

**步骤9**：**单击**![](/sbox/screen/thunderbird-en/78.png)开启以下界面；然后**键入**与该账户匹配的密码口令，如下所示：

![](/sbox/screen/thunderbird-en/79.png) 

*图23：请输入OpenPGP口令，完成密钥对生成*

**步骤10**：**单击**![](/sbox/screen/thunderbird-en/56.png)生成对密钥对以及取消授权证书的设置，并回到以下界面：

![](/sbox/screen/thunderbird-en/80.png)

*图24：OpenPGP密钥管理窗口，禁用密钥对选项*

**注意**：**勾选** *Display All Keys by Default*选项可以显示所有的密钥对和它们所对应的账户。请在独自一人并确定安全的情况下使用。

在您成功生成了密钥对以及对应的取消授权证书以后，您就可以与可信的联系人共享公开密钥了。

### 4.2.3 如何设置Enigmail特定用户使用权限###

如果要让**Enigmail**为某个特定邮件账户使用，请执行以下步骤：

**步骤1**：**选择Tool > Account Settings**：

**步骤2**：**选择**侧边栏中的*OpenPGP Security*菜单选项，如下所示：

![](/sbox/screen/thunderbird-en/57.png)

*图 25：账户设置 - OpenPGP安全 界面*

**步骤3**：**勾选** *Enable OpenPGP support*选项并**选择** *Use email address of this identity to identify OpenPGP key*选项，如**图11*所示。

**步骤4**：**单击**![](/sbox/screen/thunderbird-en/56.png)，回到**Thunderbird**主界面。

<a name="4.3"></a>
##4.3 如何更换公开密钥##

在您向其他用户发送加密邮件之前，您和您的联系人必须先交换公开密钥。此外，当您同意交换一个密钥对的时候，也要先确认该请求来自您认识的发送者。

### 4.3.1 如何使用邮件发送公开密钥###

要使用**Enigmail**/**OpenPGP**来发送公开密钥，您和您的及接收者都要执行如下几个步骤：

**步骤1**：**打开Thunderbird**然后**单击**![](/sbox/screen/thunderbird-en/81.png)，写一封新信息。

**步骤2**：选择菜单选项**OpenPGP > Attach My Public Key**。

**注意**：这个时候**Attachments：**（附件）选项不会立刻出现，它会在信件写完的时候出现。

如果您想要发送不同的公开密钥，请选择**OpenPGP > Attach Public Key…**找到并选择您要发送的公开密钥。

![](/sbox/screen/thunderbird-en/82.png)

*图26：写邮件页面，显示附件中的公开密钥*

**步骤3**：**单击**![](/sbox/screen/thunderbird-en/101.png)以发送含有公开密钥的邮件，此时可能会出现下面的窗口：

![](/sbox/screen/thunderbird-en/104.png)

*图28：OpenPGP弹出窗口，提示设置默认加密选项以及签发模式*

**步骤4**：**勾选** *Encrypt/sign message as a whole*选项，然后**单击**![](/sbox/screen/thunderbird-en/56.png)开启**图23*。

**步骤 5**：**输入**您的密码口令，然后**单击**![](/sbox/screen/thunderbird-en/56.png)开启以下界面：

![](/sbox/screen/thunderbird-en/105.png)

*图29：OpenPGP Prompt - 提示保存信息前是否要加密 界面*

**步骤6**：**单击**![](/sbox/screen/thunderbird-en/106.png)，加密并签发您的邮件。

### 4.3.2 如何在Enigmail中添加一个公开密钥###

在您和您的联系人互相添加对方的公开密钥之前，请先了解下面的步骤：

**步骤1**：**选择**并**打开**含有公开密钥的电子邮件。

如果公开密钥是嵌入在电子邮件里的话，*Decrypt*（解密）按钮将会被激活，在并在信息栏中出现下列提示：

![](/sbox/screen/thunderbird-en/84.png)

*图30：点击Decrypt按钮以添加公开密钥*

**步骤2**：**单击**![](/sbox/screen/thunderbird-en/85.png)开始自动检测来信是否含有加密内容。在*Enigmail/OpenPGP*工具检测到含公钥内容时，它会提醒您是否要添加这个密钥，如下所示：

![](/sbox/screen/thunderbird-en/86.png)

*图31：OpenPGP确定要加载邮件中的公开密钥吗？*

**步骤3**：**单击**![](/sbox/screen/thunderbird-en/87.png)开始加载您联系人的公开密钥。

如果密钥成功添加，会出现类似下面的信息提示：

![](/sbox/screen/thunderbird-en/108.png)

*图32：OpenPGP提示界面，显示您联系人的公开密钥*

要确认收到了来自联系人的公开密钥，请执行以下步骤：

**步骤1**：**选择OpenPGP > Key Management**以打开*OpenPGP Key Management*界面，如下所示：

![](/sbox/screen/thunderbird-en/107.png)

*图33：OpenPGP - 密钥管理界面显示新添加的密钥*

<a name="4.4"></a>
## 4.4 如何验证并签署密钥对##

最后，您必须验证新添加的密钥真正来源于其声称的发送者，然后还要确认其确实有效。对您和您的密钥共享者来说，这都是非常重要的一步。请注意看下面的步骤：

### 4.4.1 如何确认密钥对###

**步骤1**：通过一种除电邮外的其他通讯方式*联系*您的共享人。您可以打电话，发短信，*在线语音*（**VoIP**）或通过其他联系方式，但是请*务必*确认您找对了人…最好还是打电话或者面谈，因为这样方便且容易安排。

**步骤2**：您和您的共享人都要确认交换的公开密钥“指纹”。所谓指纹，就是一组特殊的数字或者号码，它用来确认每个人的密钥。您可以在**OpenPGP** *Key Management*界面里查看您创建的密钥对指纹，以及您添加的公开密钥。

要查看某个特定密钥对的指纹，请执行以下步骤：

**步骤 1**：**选择 > OpenPGP > Key Management**，然后**右键点击**某个密钥，打开弹出菜单：

![](/sbox/screen/thunderbird-en/90.png) 

*图34：OpenPGP密钥管理菜单，选择了Key Properties选项*

**步骤2**：**选择** *Key Properties*项，开启以下界面：

![](/sbox/screen/thunderbird-en/91.png)

*图35：The Key Properties界面*

您的联系人也要执行上述的步骤。互相确认各自交换到的指纹与发送者的相匹配。如果不匹配的话，请更换一个公钥，并重复验证步骤。

**注意**：指纹并不属于保密信息。为了方便起见，您可以把它储存起来，方便以后验证。

### 4.4.2 如何签署验证的密钥对###

最后，当您确认了联系人的密钥对真正匹配之后，您必须*签署*它，表明您已经对这个密钥进行了验证。

要签署一个验证的公开密钥，请执行以下步骤：

**步骤1**：**单击**![](/sbox/screen/thunderbird-en/56.png)回到*Key Management*界面。

**步骤2**：**右键点击**您共享者的公钥并**选择** *Sign Key*选项，开启以下界面：

![](/sbox/screen/thunderbird-en/92.png)

*图36：OpenPGP - Sign Key界面*

**步骤3**：**勾选** *I have done very careful checking*选项，然后**单击**![](/sbox/screen/thunderbird-en/56.png)完成对您共享者公钥的签署，完成验证过程，并返回*OpenPGP Key Management*窗口，如下所示：

![](/sbox/screen/thunderbird-en/93.png)

*图37：OpenPGP 密钥管理界面 显示密钥对已验证*

#### 4.4.3 如何管理您的密钥对####

*OpenPGP Key Management*窗口可以用来生成，验证以及签署不同的密钥对。但是它还有其他密钥管理的功能：

- **Change Passphrase**（更换密码口令）：该选项可以更改您的密钥对的密码口令。
- **Manage User IDs**（管理用户ID）：该选项可以使您在同一邮件地址下关联多个密钥对。
- **Generate & Save Revocation Certificate**（生成&保存取消授权证书）：该选项可以生成新的取消证书。如果您不小心丢失了或覆盖了先前创建的证书，可以用到该功能。

<a name="4.5"></a>
## 4.5 如何加密和解密电子邮件##

**重要**：任何邮件的标题信息——就是它的*主题*以及接收者（包括任何*致*XXX、*抄送*、*密送*等信息）——是不能被加密的，它会以纯文本的格式公开发送。为了确保您邮件的隐私性以及安全性，请不要在标题里包含可以泄露邮件内容的信息。此外，在您群发邮件时，我们强烈推荐您把所有收件人地址放进*密送*一栏中。

当加密含有附件的邮件时，我们强烈推荐您使用**PGP/MIME**选项，它会给您邮件的全部文件加密。

### 4.5.1 如何加密信息###

当您和联系人相互添加，验证以及签署了密钥对协议以后，你们就可以互相发送加密信息，并解密查看信息了。

要给您发送的信息加密，请执行以下步骤：

**步骤1**：**打开**您的邮件账户，并**单击**![](/sbox/screen/thunderbird-en/81.png)开始写一封邮件。

**步骤2**：**单击**![](/sbox/screen/thunderbird-en/94.png)开启以下界面：

![](/sbox/screen/thunderbird-en/95.png)

*图38：The OpenPGP Encryption弹出窗口*

**注意**：如果勾选了*Encrypt/sign message as a whole*选项，那么您应该使用推荐的**PGP**/**MIME**方式发送，如**图28*所示。**图35*将不会出现。

**步骤3**：**勾选** *Sign Message*以及*Encrypt Message*选项，如**图32**；然后**单击**![](/sbox/screen/thunderbird-en/56.png)完成签署，并给邮件内容加密。

**注意**：要验证您的邮件已经加密并签署完毕，请检查以下两个图标，在界面的右下角信息栏内，如下所示：

![](/sbox/screen/thunderbird-en/97.png)

*图39：信息加密并签发确认图标*

**步骤4**：**单击**![](/sbox/screen/thunderbird-en/101.png)来发送邮件。软件会提示您输入个人密码以签署邮件。

### 4.5.2 如何解密信息###

当您收到并打开一封加密邮件时，软件将会自动尝试为该信息解密，并会出现以下窗口提示：

![](/sbox/screen/thunderbird-en/79.png)

*图40：OpenPGP提示 - 请输入您的OpenPGP密码口令，或您的SmartCard PIN码*

**步骤1**：**输入**您的口令密码，如**图37**所示。

在输入您的个人密码以后，信息内容被成功解密并显示出来，如下所示：

![](/sbox/screen/thunderbird-en/109.png)

*图41：信息栏中显示的解密信息*

现在您已经成功解密了该信息。如果您在每次与联系人收发信息的时候都能按照**4.5 如何加密和解密电子邮件**中讲述的步骤进行，您很快就可以创建一个私密的专属的信息交流通道，有效防止他人对您邮件内容的监控。


