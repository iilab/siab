

---

lang: tr
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: Using the Tor Browser

---

- [**4.0 Tor Tarayıcı Kullanımı**](#4.0)
- [**4.1 Tor Tarayıcı'nın çalışıp çalışmadığına dair ek kontrol**](#4.1)
- [**4.2 Yeni bir kimlik Nasıl Yaratılır?**](#4.2)
- [**4.3 NoScript eklentisinin etkinleştirilmesi**](#4.3)
- [**4.3 Tor Tarayıcı güncellemeleri**](#4.3)


<a name="4.0"></a>
## 4.0 Tor Tarayıcı Kullanımı ##

**Tor Tarayıcı** kullanımı kolay olmak üzere tasarlanmıştır. **Firefox’un** daha fazla gizlilik ve güvenlik sağlamak amacı ile değiştirilmiş bir versiyonu olduğu için, herhangi bir web tarayıcısı kullanmayı biliyorsanız, **Tor Tarayıcı'yı** kullanmanız oldukça kolay olacaktır. 

**Not:** Tor Tarayıcı gizlilik amaçlı tasarlandığı için, hard diskinize veya USB çubuğuna bilgi kaydetmemek üzere yapılandırılmıştır. Bu şu anlama gelir, Tor Tarayıcı’ndan çıktığınız zaman tüm tarama tarihiniz silinir. 

<a name="4.1"></a>
## 4.1 4.1 Tor Tarayıcı'nın çalışıp çalışmadığına dair ek kontrol ##

Her atlatıcı yazılım için olduğu gibi, **Tor Taraycı’nın** iyi çalıştığından emin olmak için basit bağımsız testler yapmanızı öneririz. Bunu, siteyi ziyaret ettiğiniz IP adresi üzerinden konumunuzu belirlemeye çalışan herhangi bir web sitesine giderek yapabilirsiniz. 

Bunu ücretsiz yapan birkaç web sitesi vardır, örneğin [check.torproject.org](https://check.torproject.org), [iplocation.net](http://www.iplocation.net/), [ip2location.com](http://www.ip2location.com/), [whatismyipaddress.com](http://whatismyipaddress.com/). Bu sitelere **Tor Tarayıcı** veya herhangi benzeri bir önleyici araç kullanmadan eriştiğiniz zaman gerçek IP adresinizi gösterirler ve konumunuzu aşağı yukarı doğru olan bir şekilde belirlerler. Fakat bu sitelere **Tor Tarayıcısı** veya herhangi benzeri bir atlatıcı araç kullanarak erişirseniz, konum ve IP adresinin farklı göründüğünü göreceksiniz. 

![](/sbox/screen/tor-tr/031.png)

*Şekil 1: Aynı bilgisayarda, Tor statüsü ve IP adres farklarını gösteren Firefox (yukarıda) ve Tor Tarayıcısı (aşağıda)*

<a name="4.2"></a>
## 4.2 Yeni bir kimlik Nasıl Yaratılır? ##

Tarayıcınızda kullanmak üzere *yeni bir kimlik* yaratabilirsiniz. Bu demektir ki, kullanmanız için bir dizi yeni ve rastgele **Tor** proxy sunucusu seçilecektir. Bu sayede web sunucularına yeni bir konumdan ulaşıyor gibi görüneceksiniz. Bunu yapmak için ![](/sbox/screen/tor-tr/022.png)’e **tıklayın** ve menüden *Yeni Kimlik’i* seçin. **Tor Tarayıcı** kısa bir süre için kapanacak, *tarama geçmişinizi* ve *çerezlerinizi* silerek yeniden açılacaktır. Tarayıcı yeniden başladıktan sonra 4.1 bölümünde tarif edildiği gibi yeni konumunuza bakabilirsiniz. 

![](/sbox/screen/tor-tr/032.png)

*Şekil 2: TorButton menüsünden Yeni Kimlik seçimi*

<a name="4.3"></a>
## 4.3 NoScript eklentisinin etkinleştirilmesi ##

**Tor Tarayıcı** önceden yüklenmiş **NoScript** eklentisi ile birlikte gelir. **NoScript**, **Tor Tarayıcı'da** komut çalışması yaparak zararlı web sitelerine ve gerçek kimliğinizi ifşa etmeye karşı ek koruma sağlar. Fakat, **NoScript** **Tor Tarayıcı’da** verili olarak devre dışı bırakılmıştır, bu yüzden de sağladığı ek koruma hemen hazır değildir. 

**NoScript’in** getirdiği ek korumalardı etkinleştirmek istiyorsanız, bunu **NoScript** menüsünü açıp *Global olarak Komutları Engelle’yi* tıklayarak ve sunduğu çeşitli *seçenekleri* yapılandırarak yapabilirsiniz. 

[**Firefox** bölümünden **NoScript**](/tr/firefox_noscript) hakkında daha çok bilgi edinmenizi tavsiye ederiz.

![](/sbox/screen/tor-tr/033.png)

*Şekil 3: Global olarak Komutları Engelle (tavsiye edilen) seçeneğini seçerek NoScript’in etkinleştirilişi*

<a name="4.4"></a>
## 4.4 Tor Browser updates ##

[**Nasıl Yapmaklı Kitapçığı 1.4 kısmında**](/tr/chapter_1_4) yazılımlarınızı güncellemenin ne kadar önemli olduğundan bahsetmiştik. Bu durum **Tor Tarayıcı** için de geçerlidir. Yeni bir güncelleme hazır olduğunda **Tor Tarayıcı'yı** açarken tarayıcınızın güncellenmeye ihtiyacı olduğuna dair bir uyarı alacaksınız (*Şekil 4*) ve *Tor Tarayıcı Güncellemesini İndir’i* tıklamanız istenecek. Bu şekilde, en son sürümüne ulaşabileceğiniz **Tor Projesi** web sitesine yönlendirileceksiniz. Son sürümü indirdikten sonra bu kılavuzu kullanarak güncellenmiş Tor Tarayıcı'yı kurabilirsiniz. 

![](/sbox/screen/tor-tr/034.png)

*Şekil 4: Güncelleme olduğunu gösteren Tor Tarayıcı*

