

---

lang: tr
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 4
depth: 3
title: More Useful Firefox Add-Ons

---

Bu sayfadaki bölümlerin listesi:

- [**5.0 Eklentiler Hakkında**](#5.0)
- [**5.1 HTTPS Everywhere Nasıl Kullanılır?**](#5.1)
- [**5.2 Adblock Plus Nasıl Kullanılır?**](#5.2)
- [**5.3 Beef Taco (Hedeflenen Reklam Çerezleri Önerileri) Nasıl Kullanılır?**](#5.3)
- [**5.4 Better Privacy Nasıl Kullanılır?**](#5.4)
- [**5.5 Diğer Faydalı Eklentiler**](#5.5)

-------

<a name="5.0"></a>
## 5.0 Eklentiler Hakkında ##
Bu bölümde bahsedilen **Mozilla Firefox uzantıları**, tarayıcı ile yaptığınız işlemlerdeki anonimlik, gizlilik ve güvenliği geliştirmek için tasarlanmıştır. Bu eklentileri indirmek için, lütfen [**Firefox'u indirme**](/tr/firefox_main) bölümüne bakınız. 

<a name="5.1"></a>
##5.1 HTTPS Everywhere Nasıl Kullanılır?##

![](/sbox/screen/firefox-tr/httpseverywherelogo.png)

**HTTPS Everywhere** belirlenen web siteleri ile her zaman şifrelenmiş (https) bir kanal üzerinden iletişim kurmanızı sağlayan bir **Mozilla Firefox** uzantısıdır. Bazı siteler şifreleme imkanı sunsa da, birçoğu şifrelenmemiş bir http adresi üzerinden iletişim kurma eğilimi taşır. **HTTPS Everywhere** eklentisi, bu siteleri **HTTPS** protokolü üzerinden yeniden yazarak bu problemleri çözer. Seçilen bu web siteleri ile bağlantınızın güvenli olması için arka planda sessiz bir biçimde çalışır. Fakat, ancak bu sitelerin kendileri **HTTPS** protokolü kullanıyorsa çalışır. 

**HTTPS Everywhere** eklentisinin kurulumunu başarılı bir şekilde tamamladıktan sonra aşağıdaki ekranı göreceksiniz:

![](/sbox/screen/firefox-tr/75.png)

*Şekil 1: HTTPS Everywhere SSL Observatory kullanmalı mı? uyarı ekranı* 

**1. Adım**: Aşağıdaki ekranı etkinleştirmek için ![](/sbox/screen/firefox-tr/76.png)’i **tıklayın**:

![](/sbox/screen/firefox-tr/77.png)

*Şekil 2: SSL Observatory Tercihler ekranı* 

**Not**: **Firefox** tarayıcınıza daha önce **HTTPS Everywhere** kurduysanız, **Araçlar > HTTPS Everywhere >SSL Observatory Tercihler’i seçin** ve *Observatory Kullan* ve *Yeni bir lisans görüldüğü zaman, hangi ISP’den bağlandığımı Observatory’ye* bildir seçeneklerinin işaretli olmasına dikkat edin. **Tor** kullanmıyorsanız, *Tor’a erişim olmasa da Lisansları Kontrol Et* seçeneğinin **işaretli** olduğundan emin olun. 

<a name="5.2"></a>
## Adblock Plus Nasıl Kullanılır? ##

![](/sbox/screen/firefox-tr/adblockpluslogo.png)

**Adblock Plus**, reklamların görünmesini engelleyen veya kısıtlayan bir içerik süzme uzantısıdır. 

**Adblock Plus** başarılı bir şekilde kurulduktan sonra, aşağıdaki sayfa başlatılacaktır: 
[**chrome://adblockplus/content/ui/firstRun.html**](chrome://adblockplus/content/ui/firstRun.html)
 
![](/sbox/screen/firefox-tr/60.png)

*Şekil 3: Adblock Plus krom içerik sayfası*

**1. Adım**. *Zararlı İçerik Engelleme*, *Sosyal Medya Düğmelerini Kaldır* ve *İzlemeyi Engelle* seçeneklerini (yukarıda *Şekil 1’in* gösterdiği gibi) etkinleştirmek için ![](/sbox/screen/firefox-tr/61.png) ibaresini ![](/sbox/screen/firefox-tr/62.png) haline **getirin**. 

**2. Adım**. Aşağıda görünen ekranı etkinleştirmek için **Araçlar > Adblock Plus > Süzgeç tercihleri...’ni seçin**4:

![](/sbox/screen/firefox-tr/63.png)

*Şekil 4: Üç süzgeç aboneliği gösteren Adblock Plus Süzgeç Tercihleri*

**3. Adım**. Her abonelik kutusunu tek tek **işaretleyin** (yukarıda *Şekil 2’de* göründüğü gibi) ve  ![](/sbox/screen/firefox-tr/64.png) seçeneğini **devre dışı bırakın**. Bu şekilde bu süzgeçlerde listelenmiş olan *tüm* reklamlar filtrelenecektir. 

**4. Adım**. Birden fazla dil kullanıyorsanız,  ![](/sbox/screen/firefox-tr/65.png)’yi **tıklayın** ve farklı süzgeç aboneliklerini görün. Daha sonra,abonelikler açılır listesini etkinleştirmek için  ![](/sbox/screen/firefox-tr/66.png)’i **tıklayın** ve uygun olanı **seçerek** ![](/sbox/screen/firefox-tr/67.png)’yi **tıklayın**. 

**4. Adım**. Süzgeç aboneliklerinizi güncellemek için ![](/sbox/screen/firefox-tr/68.png)’i **tıklayın** ve açılır menüden *Süzgeçleri Güncelle’yi* **seçin**. 
<a name="5.3"></a>

## 5.3 5.3 Beef Taco (Hedefli Reklam Çerezlerini Önleme) Nasıl Kullanılır? ##

![](/sbox/screen/firefox-en/beeftacologo.png)

**Beef Taco**, içinde **Google**, **Microsoft** ve **Yahoo’nun** da olduğu çeşitli şirketlerin reklamları ile bağlantılı çerezleri düzenlemenizi sağlayan bir **Mozilla Firefox** eklentisidir. Hedeflenen Reklam Çerezleri Önerileri olarak bilinen çerezleri otomatik olarak devre dışı bırakacak şekilde yapılandırılabilir. Daha **Deneyimli** ve **Gelişmiş** kullanıcıların, hangi çerezlerin sistemde kalması ve hangilerinin devre dışı bırakılmasına detaylı bir şekilde karar vermelerine de olanak sağlar. 

<a name="5.4"></a>
## 5.4 Better Privacy Nasıl Kullanılır? ##

![](/sbox/screen/firefox-tr/betterprivacylogo.png)

**Better Privacy**, bilgisayarınıza **Flash** kodu tarafından yerleştirilebilen ve LSO (Local Shared Objects) olarak bilinen özel çerezlerden korunmanıza yardımcı olan bir **Mozilla Firefox** eklentisidir. Bu çerezler, **Firefox’un** standart çerez temizleme yöntemleri tarafından temizlenemezler. 

<a name="5.5"></a>
## 5.5 Diğer Faydalı Eklentiler ##
Bu bölümde, web’i daha gizli ve güvenli bir şekilde taramanıza yardımcı olacak, ücretsiz ve açık kaynak (veya açık kaynak olma sürecinde olan) birkaç faydalı eklentiyi bulabilirsiniz. 

### 5.5.1 Cryptocat ###

[![](/sbox/screen/firefox-tr/cryptocatlogo.png)](https://addons.mozilla.org/en-us/firefox/addon/cryptocat/)

**Cryptocat** tarayıcınızda çalışan, açık kaynak, şifreli ve güvenli bir Anlık Mesajlaşma eklentisidir. Bazı durumlarda, diğer yazılı mesaj yazılımlarına göre, kullanması daha kolaydır. **Cryptocat**, tüm üyelerle veya katılımcılarla bire bir mesajlaşabileceğiniz sanal bir mesajlaşma odası yaratır. Tüm mesajlar, gönderilmeden ve alınmadan önce kişinin tarayıcısında şifrelenmiş hale getirilir. **Cryptocat**, **Mozilla Firefox**, **Google Chrome**, **Apple Safari** ve **Mac OS X** app için tarayıcı eklentisi olarak bulunmaktadır. Daha fazla bilgi için, [burayı tıklayın.](https://crypto.cat/) 

### 5.5.2 Disconnect ###

[![](/sbox/screen/firefox-tr/disconnectmelogo.png)](https://addons.mozilla.org/en-us/firefox/user/disconnect/)

**Disconnect** verilerinizi üçüncü taraflardan korumak ve izleyenleri analiz ederek, reklamcılar, analizciler ve sosyaller gibi farklı gruplar oluşturmak için tasarlanmış bir eklentidir. Daha fazla bilgi için, [burayı tıklayın](https://www.disconnect.me/)

### 5.5.3 DuckDuckGo ###

[![](/sbox/screen/firefox-tr/duckduckgologo.png)](https://addons.mozilla.org/en-US/firefox/addon/duckduckgo-ssl/)

**DuckDuckGo** **Google** ve **Bing** gibi arama motorlarına daha gizli ve güvenli bir alternatif sunmak için tasarlanmıştır. **DuckDuckGo** kullanıcı bilgilerini kayıt altına almaz ve paylaşmaz ve bütün kullanıcıların aynı bilgilere erişimi olmasını sağlar. [**DuckDuckGo**](https://duckduckgo.com/) web sitesine doğrudan giderek veya **DuckDuckGo** ikonuna tıklayarak kurabilir ve arama sekmesindeki otomatik arama motorunuz haline getirebilirsiniz. 

### 5.5.4 vtzilla ###

[![](/sbox/screen/firefox-tr/vtzillalogo.png)](https://addons.mozilla.org/en-us/firefox/addon/vtzilla/)

**vtzilla** indirilenleri ve web sitelerini kötücül yazılım ve virüs olup olmadığını anlama amaçlı taramak için tasarlanmıştır. **Vtzilla** eklentisini başarılı bir şekilde kurduktan sonra, **Firefox** arama araç çubuğunun altında **vtzilla** araç çubuğu belirir (ki bu istenirse kaldırılabilir). **Vtzilla** arama kutusuna bir web sitesi adresi yapıştırabilir ve arama isteğinizin **Virus Total** web sitesine yönlendirilmesini sağlayabilirsiniz. Bu web sitesi belirlenen bağlantı veya web sitesine 40’tan fazla kötücül yazılım ve virüs tarayıcısı yönlendirir. Buna ek olarak, **vtzilla**, indirdiğiniz dosyaları da tarayarak var olan anti-virüs programlarına (örneğin [**avast!**](https://securityinabox.org/en/avast_main) gibi) ek bir güvenlik getirir ve bu sayede bilgisayarınızın korunmasını arttırır. Daha fazla bilgi için, [burayı tıklayın](https://www.virustotal.com/en/documentation/browser-extensions/). 

### 5.5.5 ShareMeNot ###

[![](/sbox/screen/firefox-tr/sharemenotlogo.png)](https://addons.mozilla.org/en-us/firefox/addon/sharemenot/)

**ShareMeNot** İnternet üzerindeki sitelere eklenmiş olan üçüncü tarafların düğmelerinin (örneğin Facebook ‘Beğen’ düğmesini veya Twitter ‘tweet’ düğmesi), siz onlara basana kadar sizi takip etmesini engellemek üzere tasarlanmıştır. Daha fazla bilgi için, [burayı tıklayın](http://sharemenot.cs.washington.edu/).

### 5.5.6 Click&Clean ###

[![](/sbox/screen/firefox-tr/clickcleanlogo.png)](https://addons.mozilla.org/en-US/firefox/addon/clickclean/) 

**Click&Clean** **Firefox’u** kapattığınız anda kişisel verilerinizin silinmesi için tasarlanmıştır. Buna, indirilenler tarihiniz, tarama tarihiniz ve **Flash Local Shared Objects** (**LSO**) gibi çerezler de dahildir. Ayrıca, geçici dosyaları siler ve lokal önbelleğinizi de temizler. 

**Not**: Buna alternatif olarak,**Windows** işletim sistemi için [**CCleaner**](https://securityinabox.org/en/ccleaner_main), **Wise Disk Cleaner** veya **Linux** için **Janitor** veya **BleachBit** gibi harici uygulamalar da kullanabilirsiniz.


