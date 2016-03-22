

---

lang: zh
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: How to Install TrueCrypt and Create Standard Volumes

---

本页所列章节：

- [**2.0 如何安装TrueCrypt**](#2.0)
- [**2.1 关于TrueCrypt**](#2.1)
- [**2.2 如何创建标准加密卷**](#2.2)
- [**2.3 如何在USB存储棒上创建标准加密卷**](#2.3)
- [**2.4 如何创建标准加密卷 (续)**](#2.4)

-------

<a name="2.0"></a>
## 2.0 如何安装 TrueCryrpt ##

**第1步**：**双击**![](/sbox/screen/truecrypt-zh/01.png)，*打开文件–安全警告*对话框可能弹出。如果弹出，**点击**![](/sbox/screen/truecrypt-zh/02.png)激活**TrueCrypt** *许可证书*界面。

**第2步**：**点选***我接受并同意许可证书条款的约束*选项，启用*接受*按钮；**点击**![](/sbox/screen/truecrypt-zh/03.png)激活如下界面：

![](/sbox/screen/truecrypt-zh/04.png)

*图1：默认安装模式中的向导模式*

- *安装*模式：该选项适用于不打算隐瞒在电脑上使用**TrueCrypt**这一事实的用户。

- *提取*模式：该选项适用于希望在USB存储棒上使用移动版**TrueCrypt**而不希望在电脑上安装**TrueCrypt**的用户。

**注**：**TrueCrypt**仅为提取模式时，某些选项（如全部分区和磁盘加密）将无法使用。

**注**：虽然建议使用默认*安装*模式，但之后还是可以使用**TrueCrypt**的移动模式。

**第3步**：**点击**![](/sbox/screen/truecrypt-zh/05.png)激活如下界面：

![](/sbox/screen/truecrypt-zh/06.png)

*图2：启动选项窗口*

**第4步**：**点击**![](/sbox/screen/truecrypt-zh/07.png)激活*安装*界面开始在您的系统安装**TrueCrypt**。

**第5步**：**点击**![](/sbox/screen/truecrypt-zh/08.png)激活如下界面：

![](/sbox/screen/truecrypt-zh/09.png)

*图3：TrueCrypt启动确认对话框*

**第6步**：**点击**![](/sbox/screen/truecrypt-zh/10.png)登录**TrueCrypt**网站，完成**TrueCrypt**安装，然后**点击**![](/sbox/screen/truecrypt-zh/11.png)。

**注**：强烈鼓励所有用户在完成本指南后查阅**TrueCrypt**的帮助文件。

<a name="2.1"></a>
## 2.1 关于TrueCrypt##

**TrueCrypt**是一个通过防止没有正确密码的人访问文件来保护您的文件的程序。它的功能就像一个电子保险箱，可以锁定文件，只有正确的密码才可以打开加密的文件。**TrueCrypt**通过启用*加密卷*或区域可以帮您安全地存储文件。当您在这些加密卷中创建数据或将数据移动到这些加密卷时，**TrueCrypt**会自动对该信息进行加密。当您打开或移出文件时，它就自动对其进行解密以便使用。这个过程被称为“联机”加密。

<a name="2.2"></a>
## 2.2 如何创建标准加密卷##

**TrueCrypt**可以创建两类加密卷：*隐藏*及*标准*。在此部分，您将了解如何创建存储文件的*标准加密卷*。

按照下列步骤使用**TrueCrypt**创建*标准加密卷*：

**第1步**：**双击**![](/sbox/screen/truecrypt-zh/52.png)或**选择开始> 程序> TrueCrypt > TrueCrypt**打开**TrueCrypt**。

**第2步**：**选择** **TrueCrypt**窗格中的驱动器列表，如下：

![](/sbox/screen/truecrypt-zh/12.png)

*图4：TrueCrypt主界面*

**第3步**：**点击**![](/sbox/screen/truecrypt-zh/13.png)激活*TrueCrypt加密卷创建向导*如下：

![](/sbox/screen/truecrypt-zh/14.png)

*图5：TrueCrypt加密卷创建向导窗口*

*图5*中有三个选项用于加密*标准加密卷*。在此章节中，我们将使用*创建文件型加密卷*选项。请参阅[**TrueCrypt**](http://www.truecrypt.org/docs/)文件中关于另外两个选项的描述。

**第4步**：**点击**![](/sbox/screen/truecrypt-zh/05.png)激活如下界面：

![](/sbox/screen/truecrypt-zh/15.png)

*图6：卷类型窗口*

*TrueCrypt加密卷创建向导 - 卷类型*窗口让您指明创建*标准*还是*隐藏*的**TrueCrypt**加密卷。

**重要**：关于*如何创建隐藏卷*的更多信息，请参阅[**隐藏卷**](/en/truecrypt_hiddenvolumes)页面。

**第5步**：**点选** *标准TrueCrypt加密卷*选项。

**第6步**：**点击**![](/sbox/screen/truecrypt-zh/05.png)激活如下界面：

![](/sbox/screen/truecrypt-zh/16.png)

*图7：加密卷创建向导 - 加密卷位置窗口*

您可以在*加密卷创建向导 - 加密卷位置*界面指定存储文件的位置。该文件与其他文件一样存储。

**第7步**：在文本字段内**输入**文件名称或**点击**![](/sbox/screen/truecrypt-zh/17.png)都可以激活如下界面：

![](/sbox/screen/truecrypt-zh/18.png)

*图8：指定路径和文件名导航窗口*

**注**：**TrueCrypt**加密卷包含在普通文件夹内。这意味着它可以被移动、复制甚至删除！您必须记住文件的位置和名称。否则，您必须为您创建的加密卷选择一个新的文件名（请参阅[**2.3 如何在USB存储棒上创建标准加密卷**](#2.3)部分）。在本指导中，我们将在**我的文档**文件夹下创建我们的标准加密卷，并命名为*图8*中所示的*我的加密卷*文件夹。

**提示**：您可以使用任何文件名和文件扩展名。例如，您可以将您的标准加密卷命名为*recipes.doc*，那么它将看起来像一个*Word*文档，或*holidays.mpg*将看起来像一个视频文件。这是帮助您掩饰标准加密卷的一种方法。

**第8步**：**点击**![](/sbox/screen/truecrypt-zh/19.png)关闭*指定路径和文件名*窗口并返回*加密卷创建向导*窗口，如下：

![](/sbox/screen/truecrypt-zh/20.png)

*图9：TrueCrypt加密卷创建向导显示加密卷位置窗格*

**第9步**：**点击**![](/sbox/screen/truecrypt-zh/05.png)激活*图10*。

<a name="2.3"></a>
## 2.3 如何在USB存储棒上创建标准加密卷##

按照[**2.2 如何创建标准加密卷**](#2.2)部分的第1步至第7步，激活*选择TrueCrypt加密卷*界面，在USB存储棒上创建**TrueCrypt** *标准加密卷*。不要选择*我的文档*作为文件位置，**找到**并**选择**USB储存棒，然后**输入**文件名并创建*标准加密卷*。

<a name="2.4"></a>
## 2.4 如何创建标准加密卷（续）##

在此阶段，您可以选择一个指定的加密方式（或该界面上的现实的*算法*）将要存储于*标准加密卷*内的数据译成密码。

![](/sbox/screen/truecrypt-zh/21.png)

*图10：加密卷创建向导加密选项窗格*

**注**：可以直接使用所显示的默认选项。两个选项内的所有算法都是安全的。

**第10步**：**点击**![](/sbox/screen/truecrypt-zh/05.png)激活*TrueCrypt加密卷创建向导*界面，如下：

![](/sbox/screen/truecrypt-zh/22.png)

*图11：加密卷创建向导显示加密卷大小窗格*

*加密卷大小*窗格可以让您指定*标准加密卷*的大小。在此示例中，加密卷被设置成10MB。但您可以设置不同的尺寸。根据您想要存储的文件和文件夹的大小和类型设置一个适合的加密卷尺寸。

**提示**：如果您想在CD上备份您的标准加密卷，最好将加密卷的大小设置为700MB或稍小尺寸。

**第11步**：在文本字段内**输入**指定的加密卷大小，然后**点击**![](/sbox/screen/truecrypt-zh/05.png)激活如下界面：

![](/sbox/screen/truecrypt-zh/23.png)

*图12：TrueCrypt加密卷创建向导 - 加密卷密码窗口*

**重要**：创建*标准加密卷*时一个非常重要的任务是选择一个安全且强度高的密码。一个好的密码可以保护您的加密卷，您选择的密码强度越高越好。如果您使用类似**KeePass**程序生成的密码就没有必要创造或记忆自己的密码了。关于密码创造和存储的更多信息请参阅[**KeePass**](/keepass_main)。

**第12步**：**输入**密码后在*确认*文本字段**重新输入**密码。

**重要**：*下一步*按钮在文本字段内输入符合的密码前仍是禁用状态。如果您的密码不是特别安全或保密，您将会看到一个警告提示信息。请更改密码！虽然**TrueCrypt**会通过您所选的密码工作，但您的数据却不是很安全。

**第13步**：**点击**![](/sbox/screen/truecrypt-zh/05.png)激活如下界面：

![](/sbox/screen/truecrypt-zh/24.png)

*图13：TrueCrypt加密卷创建向导的加密卷格式化窗格*

**TrueCrypt**现已准备好创建*标准加密卷*。在此*TrueCrypt加密卷创建向导*窗口内随机移动鼠标。移动鼠标时间越长，密钥的加密强度越好。

**第14步**：**点击**![](/sbox/screen/truecrypt-zh/25.png)开始创建标准加密卷。

**TrueCrypt**在之前指定的*我的文档*文件夹创建一个命名为*我的加密卷*文件夹。该文件夹将包含一个**TrueCrypt** *标准加密卷*，大小为10MB，可以安全地存储您的文件。

*标准加密卷*成功创建后，将弹出下面的对话框：

![](/sbox/screen/truecrypt-zh/26.png)

*图14：TheTrueCrypt加密卷已成功创建的信息界面*

**第15步**：**点击**![](/sbox/screen/truecrypt-zh/27.png)完成*加密卷*的创建并返回到**TrueCrypt**主界面。

**第16步**：**点击**![](/sbox/screen/truecrypt-zh/28.png)关闭*TrueCrypt加密卷创建向导*。


