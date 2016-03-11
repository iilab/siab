

---

lang: zh
community: guide
type: tactics
legacy: True
child: True
weight: 2
depth: 3
title: Understanding censorship circumvention

---

如果一个网站被前面所提及的其中一种方法封锁了，导致您无法直接访问，您就要想办法绕过此障碍。在没有互联网过滤的国家的安全[*代理*](/zh/glossary#Proxy)服务器可以提供这种绕行，它先获取您所请求的网页，再递送回给您。在您的[*ISP*](/zh/glossary#ISP)看来，您只是在互联网的某处与一台未知的电脑（[*代理*](/zh/glossary#Proxy)服务器）进行安全通讯。

![](/sites/securitybkp.ngoinabox.org/security/files/img/2-en.png)

当然，在您的国家主管互联网审查的政府机构（或向过滤软件提供更新的公司）可能最终会发现这台“未知的电脑”其实是个绕行[*代理*](/zh/glossary#Proxy)。要是这样，它的[*IP地址*](/zh/glossary#IP_address)就可能被添加进[*黑名单*](/zh/glossary#Blacklist)里，它也就再也不能用了。然而，[*代理*](/zh/glossary#Proxy) 通常不会在短时间内遭到封锁，而创建和更新绕行工具的人们也很清楚这个威胁。他们会使用以下的其中一种或两种方法来回击：

- **隐藏的代理** 隐藏的[*代理*](/zh/glossary#Proxy)更难被鉴别。这是使用安全[*代理*](/zh/glossary#Proxy)的重要性之一，它没有那么显眼。然而[*加密*](/zh/glossary#Encryption)只是其中一个环节。如果一个[*代理*](/zh/glossary#Proxy)的运行者希望保持隐蔽，他们在向新用户透露位置时必须小心谨慎。
	
- **一次性的代理** 能在遭到封锁后被迅速更换。这种情况下，要告诉新用户如何寻找替代[*代理*](/zh/glossary#Proxy)，此过程则也许不会特别安全。然而，通常这种类型的绕行工具分发得要比遭到封锁的速度更快。
	
最后，只要您可以得到一个您信任的[*代理*](/zh/glossary#Proxy)，来为您获取您所要求的服务，您就只管发送请求，然后使用适当的工具去查阅它返回给您的内容。通常，这道程序的细节都由您安装在电脑上的绕行工具来自动处理，它会修改您的浏览器设置，或者使其指向一个基于网页的[*代理*](/zh/glossary#Proxy)页面。后文描述到的[*Tor*](/zh/glossary#Tor)匿名绕行工具使用的是第一种方法。再后面会讨论关于一些基础级别的、单层的代理绕行工具，它们的工作原理都稍有不同。


