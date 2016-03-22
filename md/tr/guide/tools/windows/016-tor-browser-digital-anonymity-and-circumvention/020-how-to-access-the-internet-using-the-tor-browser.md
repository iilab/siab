

---

lang: tr
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to access the Internet using the Tor Browser

---

- [**3.0 Tor Ağı’na Nasıl Bağlanabilirsiniz?**](#3.0)
- [**3.1.1 - Direkt Erişim**](#3.1.1)
- [**3.1.2 - Kısıtılı Erişim**](#3.1.2)
- [**3.2 Tor Ağına Erişimi Yeniden Yapılandırma**](#3.2)
- [**3.3 Köprü Adreslerini Alma**](#3.3)

<a name="3.0"></a>
## 3.0 Tor Ağı’na Nasıl Bağlanabilirsiniz? ##

**Tor Tarayıcı’yı** ilk defa çalıştırdığınızda internete nasıl bağlanmak istediğiniz sorulacak:

- [Direkt Erişim](#3.1.1):  Bu seçenek bulunduğunuz yerde internete erişiminız kısıtlanmamış ve **Tor** kullanımı bloke edilmemiş, yasaklanmamış, ya da kontrol altında tutulmamış ise seçilmelidir.

- [Kısıntılı Erişim](#3.1.2): Bu seçenek bulunduğunuz yerde internete erişiminiz kısıtlanmış ise ya da **Tor** kullanımı bloke edilmiş, yasaklanmış ya da kontrol altına alınmış ise seçilmelidir.

Bu ayarlar **Tor** Tarayıcı’nın içinden, yazılımı yeniden kurmadan, herhangi bir zamanda değiştirilebilir. Bu, bulunduğunuz konumdaki şartlar değiştiği zaman ya da farklı bir ülkeyi ziyaret ediyorsanız yapmanız gereken bir şey olabilir.

Daha sonra, **Tor Tarayıcı’yı** başlattığınız zaman, ek bir yapılandırma gerektirmeden **Tor** ağına bağlanmanızı sağlayacaktır.


<a name="3.1.1"></a>
## 3.1.1 Tor Ağına Nasıl Bağlanabilirsiniz? - Direkt Erişim##

**Tor Tarayıcı’yı**, **Tor** ağına direkt olarak erişecek şekilde yapılandırmak için aşağıdaki adımları takip etmelisiniz:

**1.Adım**. *Tor Tarayıcı* klasörüne **gidin** ve ![](/sbox/screen/tor-tr/010.png)’yi **çift tıklayın**. Aşağıdaki ekranı göreceksiniz:

![](/sbox/screen/tor-tr/012.png)

*Şekil 1: Tor Ağ Ayarları paneli*


**2. Adım**. ![](/sbox/screen/tor-tr/013.png) düğmesini **tıklayın** ve **Tor Statüsü** penceresini açın. Bu pencereden, yazılımın **Tor Ağına** bağlanma gelişimini görebilirsiniz.

![](/sbox/screen/tor-tr/014.png)

*Şekil 2: Tor statüsü penceresi ve bağlanma gelişimi*

Birkaç saniye sonra, **Tor Tarayıcı**, aşağıdaki ekranı gösteren yeni bir tarayıcı penceresini etkin kılacaktır:

![](/sbox/screen/tor-tr/015.png)

*Şekil 3: Tor ağına başarılı bir şekilde bağlanmış Tor Tarayıcı*

Şimdi, web’i *Tor ağı* güvenliği ile tarayabilirsiniz.

**Not**: **Tor Tarayıcı'yı** her başlattığınızda, *Tor Tarayıcı* başlamadan önce (Şekil 3) otomatik olarak Tor Statüsü penceresi (Şekil 2) açılacaktır. 

<a name="3.1.2"></a>
## 3.1.2 Tor Ağına Nasıl Bağlanabilirsiniz? - Kısıtlı Erişim##

Tor Ağına erişimin, yukarıda tarif edildiği gibi, mümkün olmadığı ya da riskli olduğu bir bölgede yaşıyorsanız, Tor’u bu engelleri aşacak şekilde yapılandırmayı deneyebilirsiniz.

**1. Adım**: *Tor Tarayıcı* klasörüne idin, ![](/sbox/screen/tor-tr/010.png)’yı **çift tıklayın** ve aşağıdaki ekranı etkinleştirin:

![](/sbox/screen/tor-tr/012.png)

*Şekil 4: Tor Ağı Ayarlar paneli*

**2. Adım**: ![](/sbox/screen/tor-tr/016.png) düğmesini **tıklayın** ve yeni bir pencere açın. **Tor Ağına** erişmenize yardımcı olacak üç kısa yapılandırma sorusu sorulacak. 

**1. Soru**: *Proxy Erişimi;* İnternete proxy üzerinden erişmeniz gerekiyorsa **evet’i** işaretleyin ve ![](/sbox/screen/tor-tr/017.png)’e basın. Proxy kullanmıyorsanız, **hayır’ı** işaretleyin ve ![](/sbox/screen/tor-tr/017.png)’e basın. 

Yukarıda **evet’i** işaretlediyseniz, bir sonraki ekranda proxy ayarlarınızı girin. Proxy ayarlarınızı bilmiyorsanız, her zaman kullandığınız tarayıcı ayarlarına bakın. **Firefox’ta** ayarları, *Bağlantı Ayarları* bölümünde *Seçenekler*>*Gelişmiş*>*Ağ* sekmesi’nde bulabilirsiniz. Diğer tarayıcılarda, *İnternet Seçenekleri* bölümüne bakabilirsiniz. Daha fazla yardım için tarayıcınızdaki *Yardım* özelliğini kullanabilirsiniz. 

![](/sbox/screen/tor-tr/018.png)

*Şekil 5: Proxy ayarları ekranı*

**Soru 2**: **Kısıtlı Portlar**, İnternet’e, web tarama için, *port 80 ya da 443* gibi, sadece belli portlara erişime olanak veren bir güvenlik duvarı üzerinden erişiyorsanız, **evet’i** seçin ve portları yapılandırmak için ![](/sbox/screen/tor-tr/017.png)’ye basın. Durum bu değilse, **hayır’ı** seçin ve ![](/sbox/screen/tor-tr/017.png)’e basın. 

![](/sbox/screen/tor-tr/019.png)

*Şekil 6: Port kısıtlama yapılandırma ekranı*

**Soru 3**: *Sansürlü İnternet bağlantısı*, **Tor** trafiğini aktif olarak engelleyen veya denetleyen bir ülkede yaşıyorsanız, **Tor** kullandığınızı gizleyen bir *Köprü* kullanarak **Tor Tarayıcısı’nı** yapılandırabilirsiniz. 

*2. sorudan* sonra ![](/sbox/screen/tor-tr/017.png)’i tıklayınca, *Köprü adreslerini* girmenize izin veren bir ekranla karşılaşacaksınız. Köprü adresleri almak ile ilgili daha fazla bilgi almak için [Köprü Adresleri Alma](#3.3) bölümüne bakabilirsiniz. 

![](/sbox/screen/tor-tr/020.png)

*Şekil 7: Tor Bridge etkinleştirme ekranı*

*Köprü adreslerini* ekledikten sonra yapılandırmanızı bitirmek için ![](/sbox/screen/tor-tr/021.png)’i tıklayın ve **Tor Ağına** bağlanın. 

![](/sbox/screen/tor-tr/014.png)

*Şekil 8: Tor Statüsü pencereleri ve bağlantı gelişimi*

Birkaç saniye sonra, **Tor Tarayıcı**, aşağıdaki ekranı gösteren yeni bir tarayıcı penceresi etkinleştirecek:

![](/sbox/screen/tor-tr/015.png)

*Şekil 9: Tor ağına başarılı bir şekilde bağlanmış Tor Tarayıcı*

Şimdi *Tor ağı* koruması ile web’i tarayabilirsiniz. 

**Not**: **Tor Tarayıcı'yı** her başlattığınızda, *Tor Tarayıcı'dan* önce (*Şekil 9*) otomatik olarak *Tor Statü penceresi* açılacaktır (*Şekil 8*).

<a name="3.2"></a>
## 3.2 Tor Ağına erişimi yeniden yapılandırma ##

Herhangi bir noktada, **Tor Ağı'na** farklı bir şekilde bağlanmanız gerektiğinde mesela Tor’a erişimi engelleyen bir ülkeye gittiğiniz zaman, Tor Ağına farklı bir şekilde erişmeniz gerektiğinde, tarayıcı içerisinde ayarlarınız güncelleyebilirsiniz. ![](/sbox/screen/tor-tr/022.png)  ikonunu tıklayın ve *Ağ Ayarlarını Aç’ı* seçin.

![](/sbox/screen/tor-tr/023.png)

*Şekil 10: Tor Tarayıcı seçenekleri*

**Tor Tarayıcı’nın** İnternet’e erişme şeklini değiştirmenize olanak veren yeni bir pencere açılacak (*Şekil 11*). İstediğiniz seçenekleri işaretleyin ve ayarları değiştirin. İstediğiniz değişiklikleri yaptıktan sonra ![](/sbox/screen/tor-tr/024.png)’e basın ve **Tor Tarayıcı’yı** yeniden başlatın. 

![](/sbox/screen/tor-tr/025.png)

*Şekil 11: Tor Tarayıcı seçenekleri*

<a name="3.3"></a>
## 3.3 Köprü Adreslerini Alma ###

**Tor Tarayıcı’yı** **Köprüleri** kullanmak üzere yapılandırmak için köprü adresleri almanız gerekir. Bunu yapmanın iki yolu vardır: 

**E-posta**:

Köprüleri E-posta yoluyla almak için, Gmail ya da Yahoo hesabına sahip olmanız gerekir. bridges@bridges.torproject.org adresine *get bridges* konulu bir e-posta gönderin. Birkaç dakika sonra, 3 köprünün ve diğer detayların yer aldığı bir e-posta alacaksınız. 

![](/sbox/screen/tor-tr/026.png)

*Şekil 12: Köprüleri gösteren e-posta*

**Web Sitesi**:

Erişiminiz tamamen kısıtlı değilse  [https://bridges.torproject.org/](https://bridges.torproject.org/) websitesine giderek **köprü** adresleri alabilirsiniz. 

Websitesini açtıktan sonra üç adım takip etmelisiniz:

- ![](/sbox/screen/tor-tr/027.png)'ı tıklayın

- ![](/sbox/screen/tor-tr/028.png)'ı tıklayın

- *Captcha'yı* girin ve press ![](/sbox/screen/tor-tr/029.png)'a basın

*Captcha’yı* doğru bir şekilde girdiğinizde **Köprü** adresleri size verilecek. 

![](/sbox/screen/tor-tr/030.png)

*Şekil 13: Tor Projesi websitesinden alınmış Köprü adresleri*


**Not**: *Köprü Veri Tabanı* birilerinin tüm köprü adreslerini kolayca öğrenmesini engellemek üzere tasarlanmıştır.  İlk başta size her seferinde aynı köprüleri veriyor gibi görünebilir. Bir süre sonra, yeni adresler sunmaya başlayacaktır. 

Köprü adreslerini aldıktan sonra onları *Şekil 7: Köprü yapılandırma ekranı* veya *Şekil 11: Tor Tarayıcı seçenekleri*'nde görülen pencerelerdeki alanlara yapıştırın.


