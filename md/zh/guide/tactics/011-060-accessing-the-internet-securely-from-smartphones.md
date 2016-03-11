

---

lang: zh
community: guide
type: tactics
legacy: True
child: True
weight: 6
depth: 3
title: Accessing the Internet Securely from Smartphones

---

在[***第7章：如何使您的互联网通信保持私密***](/zh/chapter-7)和[***第8章：如何保持匿名与绕过互联网审查***](/zh/chapter-8)，我们讨论过：访问互联网或发布照片、视频时，都会留下用户的身份、地址和操作活动等信息。这可能给用户带来风险。使用智能手机上网加大了这种风险。

###通过WiFi或移动数据网络上网###

您可以控制智能手机的上网方式：通过某个接入点（如网吧）提供的无线连接上网，或通过移动网络运营商提供的移动数据连接功能（如GPRS、EDGE或UMTS）上网。

WiFi连接会减少手机服务提供商掌握的用户上网痕迹（因为它与手机订购业务没有关联）。然而，在某些情况下，用户只能通过移动数据连接上网。遗憾的是，移动数据连接协议（如EDGE、UMTS）并不是开放标准。独立开发人员和安全工程师无法检查这些协议，以便弄清移动数据运营商对它们的执行情况。

在某些国家，移动接入服务提供商和互联网服务提供商遵循不同的法律，这可能会导致政府和运营商更直接地监控手机服务。
不管您以何种方式进行智能手机数字通信，都可以通过匿名和加密工具，减少数据泄露的风险。

###匿名###

要匿名访问在线内容，您可以使用一款名叫 [*Orbot**](https://www.torproject.org/docs/android.html.en)的Android应用程序。Orbot会通过Tor的匿名网络传送互联网通信内容。

<div class=getstarted markdown=1>
上手指南：[*Orbot指南*](/zh/Orbot_main)
</div>

还有一款应用程序是Orweb网页浏览器。它能够加强隐私保护，如使用代理、不保留本地浏览记录。Orbot和Orweb可以共同避开网络过滤器和防火墙，并让用户匿名浏览网页。

<div class=getstarted markdown=1>
上手指南：[*Orweb指南*](/zh/Orweb_main)
</div>

###代理服务器###

移动版[*火狐*](/zh/ossary#Firefox)浏览器——[**火狐移动**](http://f-droid.org/repository/browse/?fdid=org.mozilla.firefox)可以配置代理插件，将用户数据导向代理服务器。用户数据再从代理服务器流向用户所请求的网站。这可以帮助用户逃避互联网审查，但除非客户端与代理服务器之间的连接被加密，否则用户的访问请求仍可能被泄露出去。我们推荐用户使用[**移动代理**](https://guardianproject.info/apps/proxymob-firefox-add-on/)插件（也来自[**Guardian Project**](https://guardianproject.info/)）。通过它，用户可以更方便地为火狐设置代理服务器。这也是将火狐移动通信内容导向Orbot和使用[*Tor*](/zh/glossary#Tor)网络的唯一途径。


