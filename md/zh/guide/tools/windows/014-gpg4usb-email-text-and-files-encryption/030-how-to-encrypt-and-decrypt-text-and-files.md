

---

lang: zh
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: How to Encrypt and Decrypt Text and Files

---

本页的项目列表:

- [**4.0 如何用 gpg4usb加密文字信息 **](#4.0)
- [**4.1 如何用 gpg4usb解密文字信息 **](#4.1)
- [**4.2 如何用 gpg4usb加密文件**](#4.2)
- [**4.3 如何用 gpg4usb解密文件**](#4.3)

-------

<a name="4.0"></a>
## 4.0 如何用gpg4usb 加密文字信息##

文字信息的加密过程简单易行.在如下的示例中, Terence会加密一封发给Salima的电子邮件, 通过如下步骤:

**步骤 1**. **双击** ![](/sbox/screen/gpg4usb-en/03.png)  以打开 **gpg4usb**主界面.

**步骤 2**. 按照示例所示,**编辑**您的文字信息:
![](/sbox/screen/gpg4usb-en/19.png)

*图 1: gpg4usb 主界面以及示例文字信息*

**步骤 3**. **勾选**您的邮件接受者的复选框,如下:
![](/sbox/screen/gpg4usb-en/20.png)

*图 2: gpg4usb主界面显示的,标黑的邮件接收人*

**注意:**如果要给更多联系人发送的邮件加密,只需要在*为…加密*栏对应的复选框里勾选他们就可以了.此外,如果将信息对自己也加密发送,对邮件归档会有好处,这样您也可以知道自己发送了什么信息.
**步骤 4**. **单击** ![](/sbox/screen/gpg4usb-en/21.png) 或从**密码**菜单中**选择 加密**选项来加密您的信息,如下所示:

![](/sbox/screen/gpg4usb-en/22.png)

*图 3: gpg4usb主界面显示的加密信息的示例*

**步骤 5**. **单击** ![](/sbox/screen/gpg4usb-en/23.png) 选择全部加密信息,然后 **单击** ![](/sbox/screen/gpg4usb-en/24.png)将信息复制到剪贴板.
**注意**:您也可以使用快捷键**Ctrl + E**.

**步骤 6**. **打开**您的邮件账户,然后 **打开** 空白的信息页,然后将信息 **粘贴**到上面,如下所示:

![](/sbox/screen/gpg4usb-en/25.png)

*图 4:将用gpg4usb加密的信息文字粘贴到某个Gmail邮件账户里*

**注意**: **富文本格式** (**RTF**)可能会破坏加密信息的格式; 所以最好用纯文本格式编辑信息.如果要把 **RTF** 转换为在**Gmail**的纯文本格式,只需在信息栏上的格式工具条里 **单击** ![](/sbox/screen/gpg4usb-en/26.png)

<a name="4.1"></a>
## 4.1 如何用gpg4usb解密文字信息##

要解密一封加密的电子邮件,请执行如下步骤:

**步骤 1**. **双击** ![](/sbox/screen/gpg4usb-en/03.png)  以打开 **gpg4usb**程序.

**步骤 2**. **打开** 您的邮件账户, 然后 **打开** 邮件.

**步骤 3**. **选择**, **复制**然后将加密的信息 **粘贴**到 **gpg4usb**主界面下的*未命名1.txt*表格中,如下:

![](/sbox/screen/gpg4usb-en/27.png)

*图 5: gpg4usb主界面 显示要解密的信息*

**注意**:如果加密信息出现*图 6*中的双换行符的话,**gpg4usb**可能无法自动解密它.要移除他们,在**编辑**菜单中**选择** *移除双换行符*选项来移除他们,并继续**步骤 4**的加密步骤.

![](/sbox/screen/gpg4usb-en/28.png)

*图 6: gpg4usb主界面 显示要解密的带双换行符的信息*
 
**步骤 4**. **单击** ![](/sbox/screen/gpg4usb-en/29.png) 并键入密钥对中设置的密码,如下图所示:
![](/sbox/screen/gpg4usb-en/30.png)

*图 7: 密码输入弹出窗口*

**步骤 5**. **单击** ![](/sbox/screen/gpg4usb-en/09.png) 以开启**gpg4usb**主界面 如 *图 2* 所示.

<a name="4.2"></a>
## 4.2 如何用gpg4usb 加密文件##

加密文件的方法与加密文字信息的方法类似.在如下的示例中,Salima将会给Terence加密一个文件,使用如下步骤:

**步骤 1**. **双击** ![](/sbox/screen/gpg4usb-en/03.png)  以打开 **gpg4usb**.

**步骤 2**. **单击** ![](/sbox/screen/gpg4usb-en/31.png) 开启以下界面:

![](/sbox/screen/gpg4usb-en/32.png)

*图 8:加密/解密文件窗口, 选择解密选项*

*加密/解密文件* 窗口下拉栏（黑体标出）可以让您选择要加密信息的对应密码以及邮件账户.
**步骤 3**. **勾选** *启用*单选按钮,然后 **单击** ![](/sbox/screen/gpg4usb-en/33.png) 开启下列界面:

![](/sbox/screen/gpg4usb-en/34.png)

*图 9: 打开文件浏览窗口*

**步骤 4**. **单击** ![](/sbox/screen/gpg4usb-en/35.png)添加将要加密的文件,然后回到*加密/ Decrypt*窗口:

![](/sbox/screen/gpg4usb-en/36.png)

*图 10: The 加密/解密文件窗口显示指定要加密的文件*

**步骤 5**. **单击** ![](/sbox/screen/gpg4usb-en/09.png) 开启下列界面:

![](/sbox/screen/gpg4usb-en/38.png)

*图 11:完成确认对话框*

The *完成*确认对话框显示加密文件的目标地址. 加密文件的后缀是*.asc* .比如, *Technical White Paper.doc.asc*. 

**步骤 6**. **单击** ![](/sbox/screen/gpg4usb-en/09.png) 完成加密.

**注意**:您可以分开加密文字和一起发送的文件.

**步骤 7**.打开您的电邮,**定向**至*完成*对话框(*图 11*)中的文件地址,然后将已加密的文件添加至邮件附件中.

**非常重要**:加密文件的文件名**不会被加密**.请不要在文件名中泄露了内容的重要信息!也别忘记,加密文件的源文件仍然在您硬盘的其他地方.

<a name="4.3"></a>
## 4.3 如何用gpg4usb解密文件 ##

在下面的示例中,Terence将会解密Salima给他发送的文件,通过如下步骤:

**步骤 1**. **双击** ![](/sbox/screen/gpg4usb-en/03.png)  以打开 **gpg4usb**.

**步骤 2**. **打开** 您的邮件账户, **打开** 邮件并 **下载** 邮件附件.

**注意**:如果您的联系人给您发送加密文件的同时又发送了加密信息,您可以使用[**4.1 如何用gpg4usb解密文字信息**](/zh/gpg4usb-keysimportexport#4.1) 的方法 来解密文字信息.
**步骤 3**. 在 **gpg4usb**主界面 (as shown in *图 1* above), **单击** ![](/sbox/screen/gpg4usb-en/31.png) 启动 **加密/解密File** 窗口(像在 *图 12*那样). 

**步骤 4**. **单击** ![](/sbox/screen/gpg4usb-en/33.png) 浏览下载的加密文件地址:

![](/sbox/screen/gpg4usb-en/37.png) 

*图 12: The 加密/解密窗口,显示加密文件的路径*

**步骤 5**. **单击** ![](/sbox/screen/gpg4usb-en/09.png) 开启下列界面:

![](/sbox/screen/gpg4usb-en/39.png) 

*图 13: 完成确认对话框显示已解密文件的存储路径 *

**重要**:如果您在网吧或者工作地点等公用电脑操作时,最好把*.asc*后缀的文件复制到您的USB或其他移动存储设备上,并随身携带,这样就可以确保最大限度的安全.


