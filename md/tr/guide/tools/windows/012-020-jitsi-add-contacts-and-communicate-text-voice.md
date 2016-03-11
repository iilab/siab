

---

lang: tr
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: Jitsi - Add contacts and communicate text & voice

---

Bu sayfadaki bölümlerin listesi:

- [**3.1 Jitsi’ye kişi (arkadaş) ekleme**](#3.1)
- [**3.2 OTR şifreleme ile yazılı sohbet (Anlık Mesajlaşma)**](#3.2)
- [**3.3 ZRTP şifreleme ile sesli ve görüntülü sohbet**](#3.3)


<a name="3.1"></a>
## 3.1 Jitsi’ye kişi (arkadaş) ekleme  ##

Jitsi’ye bir hesap ekledikten ve giriş yaptıktan sonra, daha fazla kişi eklemeye ve onlarla iletişim kurmaya hazırsınız. 

Jitsi’ye bir kontakt eklemek için aşağıdaki adımları takip ediniz:

**0. Adım**. **Başla > Jitsi’yi seçerek** veya masaüstündeki **Jitsi** ikonuna **çift tıklayarak** Jitsi ana penceresin açın. 

**1. Adım**. ***Dosya* > *Kontakt ekle...*’yi seçin** ve aşağıda görünen pencereyi açın: 

![](/sbox/screen/jitsi-en/30.png)

*Şekil 1: Kontakt ekle penceresi*

**2. Adım**. Kişiyi hangi hesabınıza eklemek istediğinizi **seçin** (örneğin, erance.the.tester@jit.si).

**İsteğe bağlı**: Kişiyi belli arkadaşlarınızdan oluşan bir *gruba* da ekleyebilirsiniz. Fakat önce bu grubu oluşturmalısınız. Bunu menüden ***Dosya* – *Grup oluştur...'u* seçerek** yapabilirsiniz. 

***Kimlik veya Numara*** alanına kişinin kullanıcı adı veya adresini **yazın** (örneğin, sally.the.doer@jit.si).

Kişi için, **Jitsi** ana penceresindeki arkadaş listenizde görünecek bir isim veya rumuz seçebilirsiniz. Bunu ***Görünen isim*** alanına **yazabilirsiniz**. 
 

**3. Adım**. *Kişi ekleme* penceresini kapatmak ve Jitsi ana sayfasına geri dönmek için *Ekle’yi* **tıklayın**. Arkadaş listenizde yeni eklenen kişileri, ‘kimlik doğrulama bekleniyor’ notu ile birlikte, aşağıdaki gibi göreceksiniz: 

![](/sbox/screen/jitsi-en/31.png)

*Şekil 2: Kimlik doğrulama bekleyen yeni eklenmiş kişileri gösteren Jitsi ana sayfası*
 
**4. Adım**. Eklediğiniz kişi (sally.the.doer@jit.si) kendi hesabına giriş yaptığı zaman onu arkadaş listenize eklemek istediğinizi söyleyen açılır bir pencere ile karşılaşacak. 

![](/sbox/screen/jitsi-en/32.png)

*Şekil 3: Yeni eklenen kişiye kimlik doğrulama isteği gönderen pencere*

Eklediğiniz kişi, *Yoksay’ı* seçebilir, bu durumda gönderdiğiniz istek yetkilendirilmeyi beklemeye devam edecektir. Bunu yapması halinde, isteğinizin *reddedildiğine* dair bilgi alacaksınız. *‘Doğrulama’yı* seçerse, eklediğiniz kişinin yetkilendirme isteğinizi kabul ettiğine dair bilgi alacaksınız ve kişi arkadaş listenizde aktif hale gelecek: 

![](/sbox/screen/jitsi-en/33.png)

*Şekil 4: Yetkilendirilmiş yeni kişiyi gösteren Jitsi ana penceresi*

<a name="3.2"></a>
## 3.2 OTR şifreleme ile yazılı sohbet (Anlık Mesajlaşma)

Kişiyi ekleyip kimlik doğruladıktan sonra arkadaş listenizde isminin üzerine tıklayıp yazılı, sesli veya görüntülü sohbet başlatabilir, isminin altındaki uygun ikonu seçerek masaüstü paylaşımında bulunabilirsiniz:

![](/sbox/screen/jitsi-en/34.png)

*Şekil 5: Jitsi ana sayfasında seçili kişiler ve yazılı, sesli veya görüntülü sohbet ve masaüstü paylaşımı ikonları*

**1. Adım**. Şimdi Jitsi’nin en önemli özelliklerinden bir tanesine değineceğiz: mesajlarınızı [*OTR*](/tr/glossary#OTR) kullanarak şifreleme ve böylelikle güvenli bir şekilde yazılı sohbet etme. OTR, bu kılavuzdaki diğer bölümlerde incelenmiş olan [*GPG/PGP*](/tr/glossary#PGP)'ye benzer bir şekilde çalışır. Aynı PGP gibi, hem sizin hem de iletişim halinde olduğunuz kişinin iletişiminizi şifrelemeden önce, şifreleme anahtarlarınızı oluşturmak için **Jitsi’yi** yapılandırmanız gerekir. Bunu, menüden ***Araçlar*** > ***Seçenekler’i*** **seçerek** yapabilirsiniz. Ardından, ***Güvenlik*** sekmesini ve ***Sohbet*** alt-sekmesini **seçin**. Aşağıda görünene benzer bir pencere ile karşılaşacaksınız: 

![](/sbox/screen/jitsi-en/35.png)

*Şekil 6: Yazılı sohbetleriniz için şifreli anahtarlar oluşturabileceğiniz sohbet seçenekleri penceresinin bir kısmı*

**2. Adım**. ***Oluştur*** düğmesine **basın**. Oluşturulan anahtarın parmak izini göreceksiniz: 

![](/sbox/screen/jitsi-en/36.png)

*Şekil 7: Oluşturulmuş OTR şifreli yazılı sohbetinizin parmak izini gösteren sohbet seçenekleri penceresinin bir kısmı*

Her hesap için bir anahtar oluşturulur. Yeni bir hesap eklediğiniz veya Jitsi’yi başka bir cihaza indirdiğiniz zaman bu işlemi yeniden yapmanız gerekir. Var olan anahtarları oraya taşıyamazsınız. 

Şimdi iletişim kurmaya hazırsınız: 

**3. Adım**. Jitsi ana sayfasından bir **kişi seçin** ve *mesaj gönder* ikonunu **tıklayın** (kişinin isminin altındaki soldaki ilk ikon). Aşağıdaki yazılı sohbet penceresi açılacaktır: 

![](/sbox/screen/jitsi-en/37.png)

*Şekil 8: OTR şifrelenmiş yazılı sohbet penceresi, işaretli fakat devreye girmemiş*

Pencerenin sağ üst köşesindeki asma kilide ve *Sohbeti OTR ile şifrele* ikonuna dikkat ediniz. Çok kolay göze çarpmayan bu ikon sohbetin şifreli olup olmadığı konusunda bilgi verir. Resimdeki anahtar açık (kilidin gövdesi ve kolu arasında çok küçük bir boşluk var!). 

**4. Adım**. ***Sohbeti OTR ile şifrele* ikonunu tıklayın**. Pencerede olan değişikliklere dikkat edin

![](/sbox/screen/jitsi-en/38.png)

*Şekil 9: Sohbeti OTR ile şifrele ikonunu tıkladıktan sonra yazılı sohbet penceresi*

Asma kilidin şimdi kapalı olduğunu görebilirsiniz. Bu, iletişim kurduğunuz kişi ile birbirinize gönderdiğiniz mesajların şifreli olduğu anlamına gelir. Bunun *onaylanmamış gizli bir iletişim* olduğuna dair bir mesaj alacaksınız, sally.the.doer@jit.si’nin *kimliğini doğrulamanız* gerekir

**5. Adım**. ***sally.the.doer@jit.si’nin kimliğini doğrulamanız*** için **bağlantıya tıklayın** ve *Arkadaşının Kimliğini Doğrula* penceresini açın: 

![](/sbox/screen/jitsi-en/39.png)

*Şekil 10: Siz ve iletişimde olduğunuz kişinin parmak izlerini gösteren Arkadaşının Kimliğini Doğrula penceresi*

İletişimde olduğunuz kişi ile anahtarlarınızın parmak izlerini, bu yazılı sohbet dışındaki başka bir kanal üzerinden karşılaştırmanızı isteyen mesaja dikkat edin. Bunu yaparak, iletişim kurduğunuz kişinin gerçekten o olduğundan emin olabilirsiniz. Anahtar karşılaştırması yapmak için en iyi yöntem yüz yüze olmak ya da görüntülü veya sesli iletişim kurmaktır. Bu yöntemlerle karşınızdaki kişinin kimliğini doğrulamak daha kolaydır. Parmak izlerini karşılaştırdıktan sonra, aşağı açılır menüden ***Parmak izini doğruladım*** seçeneğini **seçin** ve ***Arkadaşının Kimliğini Doğrula’yı* tıklayın**:

![](/sbox/screen/jitsi-en/40.png)

*Şekil 11: Parmak izini ‘doğruluyorum’ seçeneğini seçtikten sonra Arkadaşın Kimliğini Doğrula penceresinin bir kısmı*

*Arkadaşını Doğrula* penceresini kapatmak sizi sohbet penceresine götürecektir:

![](/sbox/screen/jitsi-en/41.png)

*Şekil 12: Doğrulanmış OTR şifreleme ile Yazılı sohbet penceresi*

Asma kilidin artık beyaz ünlem işareti içeren turuncu üçgeni göstermediğini görebilirsiniz. Bu arkadaşınızın kimliğiniz doğruladığınız anlamına gelir. **Kimlik doğrulama her kişi için bir kere yapılmalıdır**. Ünlem işaretli üçgen yeniden belirirse, kimliğini doğrulamadığınız birisi ile sohbet ediyorsunuz demektir. Bu, arkadaşınız başka bir şifrelenmiş anahtar ile (farklı bir Jitsi kurulumu veya OTR tarafından etkin kılınmış başka bir program) farklı bir cihaz kullandığında gerçekleşebilir. Bu durumda, iletişim kurduğunuz kişinin kimliğinden emin olmak için  birbirinizin kimliklerini yeniden doğrulamanız gerekir.

**Jitsi** aynı anda birden fazla kişi ile sohbet etmenize olanak sağlar. OTR şifreleme ise bir kişi ile sohbet ederken çalışır. 

<a name="3.3"></a>
## 3.3 ZRTP şifreleme ile sesli ve görüntülü sohbet ##

**Jitsi**, ZRTP adlı açık bir standart tarafından bağımsız olarak şifrelenebilen sesli ve görüntülü sohbet imkanı sağlar. Oturumu açmak için:

**1. Adım**. **Jitsi** iletişim listesinden iletişim kuracağınız kişiye **tıklayın** ve ses (kişinin isminin altındaki soldan ikinci ikon) veya video (üçüncü) ikona tıklayın. Yukarıdaki Şekil 5 bunu nasıl yapacağınızı gösterir. **Jitsi’nin** bağlantıyı kurduğunu gösteren yeni bir pencere açılacaktır:

![](/sbox/screen/jitsi-en/42.png)

*Şekil 13: Çalma statüsü belirten arama penceresi*

İletişim kurduğunuz kişi gelen arama bildirimini görecektir:

![](/sbox/screen/jitsi-en/43.png)

*Şekil 14: Gelen arama bildirimi*

**2. Adım**. Arkadaşınız **aramayı kabul ederse** bağlantı kurduğunuza dair bilgilendirileceksiniz: 

![](/sbox/screen/jitsi-en/44.png)

*Şekil 15: ZRTP şifrelemesiz gelen arama penceresi*

Kırmızı asma kilidin açık olduğunu görebilirsiniz. Bu, aramanızın henüz ZRTP ile şifrelenmemiş olduğunu gösterir. 

**3. Adım**. **Bekle...** Sizin ve iletişim kurduğunuz kişinin programlarının şifrelenmiş bir bağlantı kurması bir süre alabilir. Bu işlem başarı ile gerçekleşirse,turuncu bir arka planda, aşağıda göründüğü gibi kapalı bir asma kilit ile birlikte *zrtp* harflerini göreceksiniz. Bu bağlantıyı kurmayı başaramazlarsa, sohbet etmeye devam edebilirsiniz, fakat sohbetiniz şifrelenmemiş olur. Bağlantıyı kesip **Jitsi’yi** yeniden başlatabilir ve programların şifreli bir bağlantı kurmalayı yeniden denemesine izin verebilirsiniz. Farklı sunuculara sahip (Google ve Jit.si gibi) hesaplar arasındaki aramalarda ZRTP’nin çalışmama olasılığı vardır. 

![](/sbox/screen/jitsi-en/45.png)

*Şekil 16: Etkinleşmiş fakat doğrulanmamış ZRTP şifreleme ile Arama penceresinin bir kısmı*

**4. Adım**. *zrtp* harflerinin ve asma kilidin altındaki kısımda ‘Partneriniz ile kıyaslayın’ yazan ve 4 karakter ile devam eden bir mesaj **göreceksiniz**. Bu harfleri iletişimde olduğunuz kişiye **okuyun** ve onda da aynı karakterlerin olup olmadığını sorun. Eğer varsa iletişiminiz şifrelenmiş demektir ve kimse bu iletişime dahil olamaz. ***Onayla’yı* tıklayabilirsiniz**. Turuncu *zrtp* alanı yeşile dönecektir: 

![](/sbox/screen/jitsi-en/46.png)

*Şekil 17: Devreye girmiş ve onaylanmış ZRTP şifrelemesi ile Arama ekranının bir kısmı*

**5. Adım**. Siyah kısmın sağ üst köşesindeki beyaz x işaretine tıklayarak pencerenin siyah onaylama kısmını kapatabilirsiniz: 

![](/sbox/screen/jitsi-en/47.png)

*Şekil 18: Devreye girmiş ve onaylanmış ZRTP şifrelemesi ile Arama ekranının bir kısmı*

**Jitsi**, birden fazla kişi ile sesli ve görüntülü sohbet etmenize olanak sağlar. Dikkat edin ki bu tür iletişim esnasında, ZRTP şifreleme, aramayı başlatan kişi ve diğer taraflar arasında devreye girebilir, diğer katılımcıların kendi aralarında değil.

