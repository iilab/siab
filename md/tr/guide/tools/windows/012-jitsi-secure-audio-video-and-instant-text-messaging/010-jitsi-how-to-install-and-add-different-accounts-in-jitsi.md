

---

lang: tr
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: Jitsi - How to Install and Add Different Accounts in Jitsi

---

Bu sayfadaki bölümlerin listesi:

- [**2.1 Jitsi nasıl kurulur?**](#2.1)
- [**2.2 Jitsi’ye farklı hesaplar  nasıl eklenir?**](#2.2)
- [**2.2.1 Gmail-Google hesabı nasıl eklenir?**](#2.2.1)
- [**2.2.2 Yeni Jabber/XMPP veya SIP hesabına kaydolmak ve bunu Jitsi’ye eklemek**](#2.2.2)
- [**2.2.3 Facebook hesabı nasıl eklenir?**](#2.2.3)
- [**2.3 Jitsi ile nasıl hesap parolası değiştirilir?**](#2.3)
- [**2.4 Güvenliğini arttırmak için Jitsi nasıl yapılandırılır?**](#2.4)
- [**2.4.1 Arama ve sohbet geçmişini devre dışı bırakma ve silme**](#2.4.1)
- [**2.4.2 Yazılı sohbette özel mesaj isteği**](#2.4.2)
- [**2.4.3 Ana parola ile hesaplarınızın parolalarını koruma**](#2.4.3)

<a name="2.1"></a>
## 2.1 Jitsi nasıl kurulur? ##

Jitsi’yi kurmak için aşağıdaki adımları takip ediniz:

**1. Adım**. ![](/sbox/screen/jitsi-en/02.png)'ye çift tıklayın, 'Dosyayı Aç – Güvenlik Uyarısı' kutusu görünürse *Winows Kurulum* ekranını etkinleştirmek için Çalıştır’ı **tıklayın**. Bu sizi, *Jitsi Kurulum Sihirbazına Hoşgeldiniz* penceresine götürecek.   

**2. Adım**. *Son Kullanıcı Lisans Anlaşması* penceresini etkinleştirmek için ![](/sbox/screen/jitsi-en/04.png)'i **tıklayın**, *Lisans Anlaşasındaki maddeleri kabul ediiyorum’u* tıklayın ve *Hedef Klasör* penceresini etkinleştirmek için  ![](/sbox/screen/jitsi-en/04.png)'i **tıklayın**. 

**3. Adım**. *Ek Görevler* penceresini etkinleştirmek için ![](/sbox/screen/jitsi-en/04.png)'i **tıklayın** ve verili ayarları olduğu gibi **kabul edin**. 

**Not**: *Bilgisayar açıldığında ya da yeniden başladığında otomatik olarak başla* seçeneğini seçmek bilgisayarınızın genel hızını düşürebilir, özellikle de bilgisayarınız açıldığında başlaması için programlanmış birden fazla uygulamanız varsa. 

**4. Adım**. *Jitsi’yi Kurmaya Hazır* penceresini etkinleştirmek için  ![](/sbox/screen/jitsi-en/04.png)'i **tıklayın** ve kurulum ilerleme çubuğunu gösteren *Jitsi’yi Kuruluyor* penceresini etkinleştirmek için  ![](/sbox/screen/jitsi-en/05.png)’ı **tıklayın**. 

**5. Adım**. Kurulum işlemini tamamlamak ve aşağıda göründüğü gibi **Jitsi** *Giriş yap* penceresini otomatik olarak açmak için ![](/sbox/screen/jitsi-en/06.png)'i **tıklayın**:

![](/sbox/screen/jitsi-en/07.png)

*Şekil 1: Jitsi Giriş yap penceresi*

**Not**: Jitsi’nin ilk defa kurulduğu ve başlatıldığı bazı durumlarda, *Windows Güvenlik Uyarısı* ekranı belirebilir (aşağıda *Şekil 2*). **MS Windows** işletim sistemi için bu uyarı normaldir. **Jitsi'yi** kullanmaya devam etmek bir sorun yaratmaz. Düğmelerden herhangi birine basmasanız ve uyarı penceresini kapatsanız bile, **Jitsi**, **Jabber/XMPP** veya **SIP**, **Google Sohbet**, **Facebook Sohbet**, veya **Yahoo Messenger** gibi olağan kamusal servisleri kullanarak iletişim kurmaya yetkindir. Fakat, **Ulaşıma izin ver** düğmesini tıklamak, **Registrarless SIP Hesapları** isimli, gelişmiş bir **Jitsi** özelliğinin çalışmasını sağlar. Bu özel hesaplarla ilgili daha fazla bilgi için, lütfen [**Registrarless SIP Accounts**](https://jitsi.org/Documentation/RegistrarlessSIPAccount) sayfasına bakın. 

![](/sbox/screen/jitsi-en/08.png)

*Şekil 2: Windows Güvenlik Uyarısı ekranı*

**6. Adım**. **Açık** ve **Özel** ağlar kutularının **her ikisini** de işaretleyin ve **Jitsi Giriş yap** penceresini (yukarıdaki *Şekil 1’de* göründüğü gibi) veya ana kullanıcı arayüz penceresini (aşağıdaki *Şekil 4’te* göründüğü gibi) görmek için *Erişime İzin Ver’i* **tıklayın**.

<a name="2.2"></a>
## Jitsi’ye farklı hesaplar  nasıl eklenir? ##

Bu kısım, farklı tipteki hesapların nasıl **Jitsi’ye** ekleneceği ile ilgilidir. **Jitsi**, birçok farklı hesap tipini destekler. Aşağıda belirttiğimiz hesaplar genellikle **Jabber/XMPP** ve **SIP** iletişim protokollerine dayalıdır. Birçok servisin yanı sıra, **Jitsi**, **Gmail** veya **Facebook** hesaplarınızı da kullanmanıza izin verir. Bunlar Internet’te kullanılan en popüler servisler olduğu için, onları **Jitsi’ye** nasıl ekleyebileceğiniz aşağıda gösterilmiştir. Aynı zamanda, bu hesapları kullanırken, hesap sunucularınız tarafından sunulanın üstüne **Jitsi’nin** bağımsız şifrelemesini kullanarak güvenliğinizi nasıl arttıracağınız konusunda da bilgi verilmiştir. Fakat aklınızda bulundurun ki, **Jitsi** şifrelemesi ile bile, **Google** veya **Facebook** gibi hesap sunucuları iletişim halinde olduğunuzu (ve büyük ihtimalle kimlerle iletişim kurduğunuzu) takip eder ve şirketler ve hükümetler gibi üçüncü taraflarla bilgilerinizi paylaşabilir. Bu yüzden, hassas bilgilerin dahil olduğu iletişimler için, **Jitsi** şifrelemesi olsa bile, bu hesapları kullanmamak daha iyi olabilir. Bu bölümde aynı zamanda, nasıl daha güvenli hesaplar (Jabber/XMPP veya SIP) yaratabileceğinizi ve bunları **Jitsi’ye** nasıl ekleyeceğinizi de anlatıyoruz ve bu hesapları kullanmanızı tavsiye ediyoruz. 

<a name="2.2.1"></a>
### Gmail-Google hesabı nasıl eklenir? ###

**Not**: Aşağıdaki örnek bir **Google Talk** hesabından alınmıştır. Yukarıdaki *Şekil 1’de* listelenen diğer iletişim protokollerinin kurulumu benzerdir. İletişim veya bazı özellikler (**Jitsi** bağımsız şifreleme veya yazılı sohbet ve ses – **OTR** ve **ZRTP**), farklı hesap sunucuları (Facebook, Gmail, Yahoo ve benzeri) arasında çalışmayabilir. Fakat, aynı servis sunucusuna sahip hesaplar arasındaki iletişimde çalışmalıdır. 

**1. Adım**. **Başla > Jitsi'yi** **seçin** – veya **Jitsi** masaüstü ikonuna **çift tıkayarak** **Jitsi'yi** açın. 

**2. Adım**. *Giriş yapın* penceresine, **Gmail** hesabınıza ait, sohbet amaçlı kullanmak istediğiniz kullanıcı adı ve parolasını **yazın**. Aşağıdaki gibi görünecektir:

![](/sbox/screen/jitsi-en/09.png)

*Jitsi ‘Giriş Yap’ penceresi (boyutu değiştirilmiş)*

**Not**: Aynı anda farklı protokoller kullanarak birden fazla hesap ekleyebilirsiniz.

**3. Adım**. Hesabınızın sohbet penceresini aşağıda göründüğü gibi etkinleştirmek için  ![Sign in](/sbox/screen/jitsi-en/09s.png)'i **tıklayın**: 

![](/sbox/screen/jitsi-en/10.png)

*Şekil 4: Gmail hesabını ekledikten sonra Jitsi ana penceresi örneği*

**Not**: *Giriş yap* penceresini kapattıysanız ya da başka bir hesap eklemek istiyorsanız, bunu ***Klasör*  > *Yeni hesap ekle...*** menüsünü **seçerek** ekleyebilirsiniz. Yeni pencerede, **Ağ’ı** **Google Talk** olarak **seçin** ve **Gmail** hesabınızın kullanıcı adı ve parolasını aşağıda göründüğü gibi yazın:

![](/sbox/screen/jitsi-en/11.png)

*Şekil 5: ‘Yeni hesap ekle’ penceresi*

**Gmail** hesabınızı **Jitsi’ye** kaydettiğinizden emin olmak için aşağıdaki adımları takip edin:

**1. Adım**. Aşağıdaki pencereyi etkinleştirmek için menüden ***Araçlar* > *Seçenekler’i*** **seçin**:

![](/sbox/screen/jitsi-en/12.png)

*Şekil 6: Yeni kayıtlı Gmail hesabını gösteren Seçenekler menüsü (boyutu değiştirilmiş)*

**Not**: Gmail hesabınıza erişimi korumak için [**2 adımlı doğrulama**](https://support.google.com/accounts/answer/180744?hl=tr) kullanıyorsanız, her zamanki parolanız ile **Jitsi’den** giriş yapmayı denediğiniz zaman aşağıdaki gibi bir mesaj ile karşılaşabilirsiniz. **Jitsi** kullanarak giriş yapmak için, ‘uygulamaya özel parola’ üretmeniz gerekir. Bunu nasıl yapabileceğinizi öğrenmek için [Google'un yönergelerini takip ederek](https://support.google.com/accounts/answer/185833?hl=tr) öğrenin.. 

![](/sbox/screen/jitsi-en/13.png)

*Şekil 7: Google Talk giriş kimlik doğrulama başarısız örneği*

<a name="2.2.2"></a>
### 2.2.2 Yeni Jabber/XMPP veya SIP hesabına kaydolmak ve bunu Jitsi’ye eklemek ###

**Jabber/XMPP** ve **SIP**, yazılı ve sesli iletişim açık standartlarıdır. Jitsi ile birlikte kullanabileceğiniz, bedava hesap sunan birçok [sunucu](https://xmpp.net/directory.php) vardır. Aşağıda, hassas bilgi içeren iletişimde kullanabileceğiniz bazı sunucular tavsiye ediyoruz. Aklınızda tutun ki, [Jabber/XMPP sunucu yazılımı](http://xmpp.org/xmpp-software/servers/) ([ejabberd](http://www.process-one.net/en/ejabberd/) veya [Prosody IM](http://prosody.im/) gibi) indirmek de mümkündür. Bunları kendi sunucu bilgisayarınıza indirebilir, grup, topluluk ve organizasyon üyelerini arasında güzlü ve güvenli iletişim kurmak için kullanabilirsiniz.

* **Riseup.net** Jabber/XMPP hesabı

[Riseup.net güvenli e-posta servisi ](/en/riseup_main) (Amerika bazlıdır) üzerinde hesabınız varsa , bu hesabı Jitsi’ye ekleyerek, [Jabber/XMPP ağı üzerinden iletişim kurmak](https://www.riseup.net/en/chat) için kullanabilirsiniz. Var olan Jabber/XMPP hesabını nasıl ekleyeceğinizi öğrenmek için aşağıya bakın. 

* **Jabber.ccc.de** ve diğer Jabber/XMPP hesapları

Bir hesabı Jabber.ccc.de sunucusu üzerine (Almanya bazlıdır) kaydetmek için aşağıdaki adımları takip ediniz:

**1. Adım**. **Jitsi’de** menüden *Dosya* > *Yeni hesap ekle...*'yi **seçin**. Yeni açılan pencerede, ***Ağ: XMPP’yi* seçin** ve **Yeni XMPP hesabı aç** seçeneğini **işaretleyin**. Sunucuya jabber.ccc.de **yazın**, yaratmak istediğiniz XMPP kullanıcı adını **yazın** ve *Parola*, ardından da *Parolayı Onayla* alanlarını **doldurun**. Ekran aşağıdaki gibi görünecektir:

![](/sbox/screen/jitsi-en/14.png)

*Şekil 8: ‘Yeni XMPP hesabı yarat’ seçili ‘Yeni hesap aç’ penceresi örneği*

**2. Adım**. Ekle’yı **tıklayın**. Başarılı bir kayıt işleminden sonra yukarıdaki *Şekil 4’e* benzeyen bir pencere göreceksiniz. 

Kullanıcı adınız başkası tarafından alınmışsa, kayıt işlemi, *Bir hata yüzünden kayıt işleminiz tamamlanamadı: Veriler onaylanamıyor.* mesajı vererek başarısız olacaktır. Farklı bir kullanıcı adı seçerek işlemi yeniden tekrar edebilirsiniz. 

Jabber.ccc.de hesabınıza 12 aydan uzun bir süre giriş yapmazsanız, hesabınız otomatik olarak sunucudan kaldırılacak ve kullanıcı adınız başkalarının kullanımına açılacaktır. 

Bahsedilmeye değer bir başka Jabber/XMPP sunucusu ise **jit.si’dir**. Bu sunucu **Jitsi** programını geliştirenler tarafından korunur.  [**jit.si**](https://jit.si) ve diğer Jabber/XMPP sunucularında yukarıdaki bölümde anlatıldığı gibi hesap oluşturabilirsiniz. IM Observatory, [kamusal Jabber/XMPP sunucularının listesini](https://xmpp.net/directory.php) tutar ve herhangi bir Jabber/XMPP sunucusunun [güvenliğini test etmenizi sağlar](https://xmpp.net/index.php). 

* **ostel.co** SIP hesabı

**SIP** hesaplarına **Jitsi** programının içinden kayıt olunamaz. **Ostel.co** sunucusu (Amerika bazlıdır) kendi [web sayfalarında](https://ostel.co/users/sign_up) kayıt olma hizmeti sunar. Bir kullanıcı adı ve parola **seçtikten** ve e-posta adresinizi belirttikten sonra web sayfasındaki *Giriş Yap* düğmesine **basın**. Başarılı bir şekilde kayıt yaptıktan sonra Jitsi programına geri **dönün**. Menüden *Dosya*  > *Yeni hesap ekle’yi* **seçin** **Ağ: SIP’yi seçin** ve kullanıcı adınızı (örneğin, terence.the.tester@ostel.co) ve web kaydı esnasında yarattığınız parolayı **girin**, ardından ***Ekle’yi* tıklayın**. Örnek olarak aşağıdaki görüntüye bakabilirsiniz: 

![](/sbox/screen/jitsi-en/15.png)

*Şekil 9: SIP hesabı için ‘Yeni hesap ekle’ penceresi örneği*

* **Var olan Jabber/XMPP veya SIP hesaplarını Jitsi’ye eklemek**

Hali hazırda Jabber/XMPP veya SIP hesabınız varsa, onları, menüden ***Dosya* > *Yeni Hesap ekleyin...*’i seçerek** ve uygun olan **Ağ’ı** (hesap türüne bağlı olarak XMPP veya SIP) belirleyerek **Jitsi’ye** ekleyebilirsiniz.

<a name="2.2.3"></a>
### 2.2.3 Facebook hesabı nasıl eklenir? ###

**Jitsi’nin** Facebook sohbetinize bağlanabilmesi için, **Facebook’taki** iki ayarı değiştirmeniz gerekebilir

* **Facebook Kullanıcı adı**

**Facebook**, **Jitsi’nin** Facebook sohbete bağlanabilmesi için bir kullanıcı adı ister. Birçok **Facebook** kullanıcısının zaten bir kullanıcı adı vardır. Kullanıcı adınıza bakmak için **Facebook** hesabınıza **girin**. Zaman Tüneli veya Sayfanızı görüntülediğinizde konum çubuğunda https://www.facebook.com/ 'dan sonra görünen kullanıcı adınızdır. Aynı zamanda, Kişisel hesabınızın **Facebook** e-posta adresinde de kullanıcı adınızı görebilirsiniz (örneğin, kullanıcıadı@facebook.com). Kullanıcı adınızı görmek, değiştirmek veya ilk defa almak için *Hesap Ayarları* > *Genel* bölümüne gidebilir veya [https://www.facebook.com/username](https://www.facebook.com/username) sayfasını ziyaret edebilirsiniz. Kullanıcı adı oluştururken, **Facebook** hesap onaylamanızı gerçekleştirirken cep telefonu numaranıza mesaj göndermeyi şart koşabilir. Daha fazla detay için, [Facebook'un kullanıcı adı ile ilgili açıklamalarına](https://www.facebook.com/help/329992603752372/) bakabilirsiniz

* **Uygulama Ayarları**

**Jitsi** Facebook Sohbete bağlanmadan önce **Facebook’un** ‘uygulama platformu’ etkinleştirilmeli. **Facebook** *Hesap Ayarları > Uygulamalar* bölümüne gidin ve *Kullandığınız uygulamalar* için *Açık* seçeneğinin işaretli olduğundan emin olun. Bunu yapmak, hesabınız için ‘uygulama platformunu’ açacaktır. 

**Aklınızda tutun** ki, **Facebook’un** ‘uygulama platformu’nu açmak **Facebook** verilerinizin büyük bir kısmını üçüncü taraf uygulama geliştiricilerine açık hale getirir. Bu şekilde, verileriniz sadece kullandığınız **Facebook** uygulamalarına değil, arkadaşlarınızın kullandığı **Facebook** uygulamalarına da açık hale gelir. **Facebook’un** ‘uygulama platformu’nu etkinleştirdikten sonra, ‘Başkalarının kullandığı uygulamalar’ın altındaki ayarları kontrol edin. Bu ayarlar, arkadaşlarınızın kullandığı uygulamalardan bazı kişisel verilerinizi saklayabilmenizi sağlar. Ne yazık ki, **Facebook** bütün kişisel bilgilerinizi saklamanıza izin vermez. Bazı bilgi kategorileri (arkadaş listeniz, cinsiyetiniz ve kamuya açık hale getirdiğiniz bilgiler gibi), **Facebook** ‘uygulama Platformu’ ‘açık’ olduğu sürece görünür hale gelir. Bu durumun güvenliğiniz için ne derece önemli olduğuna karar vermek size kalmıştır. 

Şimdi **Facebook** hesabınızı **Jitsi’ye** eklemeye hazır hale geldiniz. Bunu yapmak için aşağıdaki adımları takip ediniz: 

**1. Adım**. Ana menüden ***Dosya – Yeni hesap ekle...’yi* seçin**

**2. Adım**. Yeni Hesap Ekle diyaloğunda **Ağ** menüsünden *Facebook’u* seçin. **Kullanıcı adı ve parolanızı girin** ve **‘Ekle’yi tıklayın**. 
 
![](/sbox/screen/jitsi-en/16.png)

*Şekil 10: Facebook hesabı için ‘Yeni Hesap Ekle’ penceresi örneği*


<a name="2.3"></a>
## 2.3 Jitsi ile nasıl hesap parolası değiştirilir? ##

Kişinin sahip olduğu her hesabın parolasını nasıl değiştireceğini bilmesi güvenlik açısından önemli bir konudur. Jitsi ile kullanabileceğiniz hesapların bir çoğunun ayarlarının içinde parola değiştirme seçeneği vardır ve bunlar web ara yüzü üzerinden erişilebilirlerdir. Fakat, bazı Jabber/XMPP ve SIP hesaplarının bu ayarlara ulaşabilecek web arayüzleri yoktur. Bu durumlarda, Jitsi kullanarak parolanızı değiştirmek için aşağıdaki adımları takip edebilirsiniz:

**1. Adım**. Menüden ***Araçlar* > *Seçenekler’i* seçin** ve ***Hesaplar*** sekmesini **seçin**

![](/sbox/screen/jitsi-en/17.png)

*Şekil 11: Bir hesap seçili Seçenekler penceresi*

**2. Adım**. Aşağıda görünen pencereyi etkinleştirmek için alt kısımdaki ***Düzenle’yi* tıklayın**:

![](/sbox/screen/jitsi-en/18.png)

*Şekil 12: Alt kısımda Hesap parolanızı değiştirin seçeneği ile birlikte Hesap Kayıt Sihirbazı*

**3. Adım**. *Hesap parolası değiştirme penceresini* etkinleştirmek için ***Hesap Parolası Değiştir’i* tıklayın**:

![](/sbox/screen/jitsi-en/19.png)

*Şekil 13: Hesap parolası değiştirme penceresi*

**4. Adım**. ***Yeni parolanızı* girin ve *yeniden* girin**. Bu pencereyi kapatmak için ***OK'yi* tıklayın**. 

**5. Adım**. Hesap Kayıt Sihirbazını kapatın.

<a name="2.4"></a>
## 2.4 Güvenliğini arttırmak için Jitsi nasıl yapılandırılır? ##

<a name="2.4.1"></a>
### 2.4.1 Arama ve sohbet geçmişini devre dışı bırakma ve silme ###

**Jitsi** verili olarak gelen ve giden ses/video arama bilgilerini ve yazılı sohbetlerinizin (gönderdiğiniz ve size gelen tüm mesajlar) tarihini kayıt altına alır. Ses/video aramalarına ana Jitsi penceresindeki saat ikonunu **tıklayarak** ulaşabilirsiniz:

![](/sbox/screen/jitsi-en/20.png)

*Şekil 14: Arama geçmişi düğmesi işaretli Jitsi ana penceresinin üst kısmı*

Birisi ile sohbet ederken yazılı sohbet penceresindeki kum saatine **tıklayarak** sohbet tarihinizi görebilirsiniz

![](/sbox/screen/jitsi-en/21.png)

*Şekil 15: Sohbet geçmişi işaretli Sohbet penceresi*

Bu bilgiler bilgisayarınızın diskinde toplanır ve saklanır. **Yazılı sohbetinizi OTR kullanarak şifrelemiş olsanız bile, gönderdiğiniz ve aldığınız tüm yazılı mesajlar bilgisayarınızda açık metin formatında saklanır**. Aynı bilgiler sohbet ettiğiniz kişilerin bilgisayarlarında da kayıt altına alınır. 

Jitsi’nin bu bilgileri toplamasını engellemek için (ve hali hazırda saklanmış olan bilgileri silmek için), **siz ve temas halinde olduğunuz kişiler aşağıdaki adımları takip etmelidir**.

#### Jitsi’nin bu bilgileri toplamasını engellemek için: ####

**1. Adım**. Menüden ***Araçlar* > *Seçenekler’i* seçin**. ***Genel*** sekmesini **seçin** ve ***Sohbet geçmişi kaydet*** seçeneğinin işaretini aşağıda göründüğü gibi **kaldırın**:

![](/sbox/screen/jitsi-en/22.png)

*Şekil 16: ‘Seçenekler’ penceresi, ‘Genel’ sekmesi ve işareti kaldırılmış ‘Sohbet geçmişini kaydet’*

**2. Adım**. *Seçenekler* penceresinde, önce ***Gelişmiş*** sekmesini **seçin**, daha sonra ***Kayıt*** bölümünü **seçin** ve ***Paket girişini etkinleştir*** seçeneğinin aşağıda göründüğü gibi **işaretini kaldırın**:

![](/sbox/screen/jitsi-en/23.png)

*Şekil 17: 'Seçenekler' penceresinde, ‘Gelişmiş’ sekmesi, Paket kaydını etkinleştir işareti kaldırılmış durumda*

Yaptığınız değişiklikler, **Jitsi’yi** yeniden başlattığınızda etkinleşecektir. .

#### Hali hazırda kaydedilmiş olan arama ve yazılı mesaj bilgilerinizi silmek için: ####

**1. Adım**. **Jitsi’yi** kapatın. 

**2. Adım**. *history_ver1.0* adındaki geçmiş klasörünün tümünü, **Jitsi** *kullanıcı profili* klasöründen silin. İsterseniz *history_ver1.0* klasörünün alt-klasörlerinden birini de silebilirsiniz. *Kullanıcı profili* ve *kayıt tarihi* klasörlerinin konumu işletim sistemine göre değişir:

* Windows XP ve önceki versiyonlarında bulunduğu yer: *C:\Belgeler ve Ayarlar\<Windows giriş/kullanıcı adı>\Uygulama Verileri\Jitsi\tarih_ver1.0*
* Windows Vista, 7, 8’de bulunduğu yer: *C:\Kullanıcılar\<&lt;Windows giriş/kullanıcı adı&gt;\UygulamaVerileri\Gezici\Jitsi\tarih_ver1.0* (‘Uygulama Verileri’ dosyası saklı olabilir. [Saklı dosyaları nasıl göreceğiniz ile ilgili bilgi için buraya bakınız](http://windows.microsoft.com/tr-tr/windows/show-hidden-files#show-hidden-files=windows-7))
* Mac OS X’te bulunduğu yer: ana klasörden *~/Kütüphane/Uygulama Destek/Jitsi/tarih_ver1.0*
* Linux’ta bulunduğu yer: ana klasörden *~/.jitsi/tarih_ver1.0* (**Not**: ‘jitsi’ klasörü saklı olabilir. [Ubuntu’daki gizli klasörleri nasıl göreceğiniz ile ilgili bilgi için buraya bakınız](http://itsfoss.com/hide-folders-and-show-hidden-files-in-ubuntu-beginner-trick/)). 

Bilgileri güvenli bir şekilde imha için [Hassas bilgiler nasıl imha edilir](/tr/chapter-6) bölümüne de bakabilirsiniz. 

<a name="2.4.2"></a>
### 2.4.2 Yazılı sohbette özel mesaj şartı ###

**Jitsi’yi** [*OTR*](/en/glossary#OTR) [*şifrelemesi*](/en/glossary#encryption) kullanarak gizli ve şifrelenmiş yazılı mesajlaşma uygulayacak şekilde kurmanızı tavsiye ederiz. Bunu yapmak için, menüden ***Araçlar*  > *Seçenekler’i* seçin**, ***Güvenlik*** seçmesini **seçin**, ***Sohbet*** alt-sekmesini **seçin** ve ekranın altındaki ***Özel mesajlaşma şartı koy*** seçeneğini aşağıda göründüğü şekilde **işaretleyin**:

![](/sbox/screen/jitsi-en/24.png)

*Şekil 18: ‘Özel mesajlaşma şartı koy’ seçili, ‘Seçenekler’ penceresi,'Güvenlik' sekmesi ‘Sohbet’ alt-sekmesi*

<a name="2.4.3"></a>
### 2.4.3 Ana parola ile hesaplarınızın parolalarını koruma ###

Jitsi’nin hesaplarınızın parolalarını hatırlamasına izin vermemek en iyisidir. Kullanım kolaylığı açısından tersini yaparsanız, bilgisayarınızı kullanan herhangi biri Jitsi’yi başlatarak tüm hesaplarınıza giriş yapabilir. Aynı zamanda, *Seçenekler* penceresinde parolalarınızı görebilir. Bu yüzden, hesap parolalarınızı güçlü bir **ana parola** ile korumanızı **şiddetle tavsiye ederiz**. Ana parolayı oluşturdulunca, Jitsi her başlatıldığında size bu parolayı soracaktır. 

**1. Adım**. Menüden *Araçlar* > *Seçenekler’i* seçerek *Seçenekler* penceresini **açın**, ***Güvenlik*** sekmesini **seçin**, ***Parolalar*** alt-sekmesini **seçin** ve ***Ana Parola*** penceresini etkinleştirmek için ***Ana parola Kullan’ı*** **işaretleyin**. 

**2. Adım**. Aşağıdaki resimde göründüğü gibi, açılan pencereye **parolanızı girin**. Güçlü parolalar oluşturmak konusunda daha fazla bilgi için, [***Güvenli şifreler nasıl oluşturulur ve muhafaza edilir***](/en/chapter-3) bölümüne bakın. 

![](/sbox/screen/jitsi-en/25.png)

*Şekil 19: ‘Ana Parola’ penceresi*

**3. Adım**. Parolayı onaylamak için ***'OK'i* tıklayın** ve ***Ana Parola başarılı bir şekilde oluşturuldu*** yazısını içeren pencereyi etkinleştirin. Pencereyi kapatmak için ***'OK'i* tıklayın** ve *Seçenekler* penceresine geri dönün. Bu pencere aşağıdaki gibi görünecektir: 

![](/sbox/screen/jitsi-en/26.png)

*Şekil 20: ‘Seçenekler’ penceresi, ‘Güvenlik’ sekmesi, ‘Parolalar’ alt-sekmesi, ‘Ana parola kullan’ seçeneği işaretli*	

**Not**: ***Ana Parolayı Değiştir*** düğmesi ana parolayı değiştirmenize izin verir, ***Kaydedilen Parolalar...*** düğmesi Jitsi tarafından hatırlanan parolalara erişmenizi ve gerektiği zaman onları silmenizi sağlar. 


