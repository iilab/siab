

---

lang: tr
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Configure Important Thunderbird Settings

---

Bu sayfadaki bölümlerin listesi:

- [**3.0 Thunderbird’deki Güvenlik Seçenekleri Hakkında**](#3.0)
- [**3.1 Thunderbird’de Önizleme Bölmesi Nasıl Kapatılır?**](#3.1)
- [**3.2 Thunderbird’de HTML Özelliği Nasıl Kapatılır?**](#3.2)
- [**3.3 Thunderbird’de Güvenlik Sekmeleri Nasıl Yapılandırılır?**](#3.3)
- [**3.4 Hesap Ayarları Gereksiz Posta Filtresi Nasıl Açılır?**](#3.4)

<a name="3.0"></a>
## 3.0 Thunderbird’deki Güvenlik Seçenekleri Hakkında ##

**Mozilla Thunderbird** bağlamında güvenlik, genel olarak bilgisayarınızın zararlı ya da kötü niyetli e-posta iletilerine karşı korumak anlamına gelir. Bunlardan bazıları sadece reklam olabilir, diğerleri casus yazılımlar ya da virüsler içerebilir. **Mozilla Thunderbird’ün** sisteminizi e-postalardan kaynaklanan saldırılardan koruyabilme yetisi güçlendirmek için yapılandırılması, açılması ya da kapatılması gereken birkaç ayar var. Bunun ötesinde, kötü amaçlı yazılım karşıtı ve güvenlik duvarı yazılımlarının da bilgisayarınızda kurulu olması *çok önemlidir*.

Zararlı ya da kötü niyetli yazılımları durdurmaya yönelik ve, [**Avast**](/en/avast_main), [**Comodo Firewall**](/en/comodofirewall_main) ve [**Spybot**](/en/spybot_main) gibi yazılımlar hakkında bilgi almak için lütfen şuraya bakınız: Nasıl Yapmalı Kitapçığı [**1. Bölüm Bilgisayarınızı kötü amaçlı yazılımlara ve hacker'lara karşı nasıl korursunuz**](/tr/chapter-1)

<a name="3.1"></a>
## 3.1 Thunderbird’de Önizleme Bölmesi Nasıl Kapatılır? ##

**Thunderbird** ana pencerisi üç bölgeye ayrılır: soldaki kenar çubuğu e-posta hesaplarınızın dizinlerini, sağ taraf ileti listesini ve alt bölme seçilen bir e-posta iletinizin *önizlenimini* gösterir.  Bu önizlenim bir ileti üstüne tıklanır tıklanmaz otomatik olarak açılır.

**Not**: Bir e-posta kötü niyetli bir kod içeriyorsa, *önizlenim* bölmesi bu kodu etkinleştirebilir; bu yüzden önizlemeyi kaldırmak iyi bir fikirdir.

![](/sbox/screen/thunderbird-tr/23.png)

*Şekil 1: Thunderbird ana kullanıcı arayüzü*

Önizlenim bölmesini kaldırmak için aşağıdaki adımı uygulayın:

**1. Adım**. ![](/sbox/screen/thunderbird-tr/24a.png)’ü **tıklayarak** *Thunderbird Menü’sünü* görün ve **Seçenekler>Yerleşim> İleti Bölmesi F8’i** aşağıdaki gibi **seçin**:

![](/sbox/screen/thunderbird-tr/24.png)

*Figure 2: Düzen alt menüsü ve seçimi kaldırmış İleti Bölmesi opsiyonu açık görülen Seçenekler menüsü*

*İleti bölmesi* kaybolacak. Bundan böyle bir e-posta iletisinin içeriğini görebilmek için ona **çift tıklamanız** gerekli olacak. Artık, şüpheli görünen bir e-posta gördüğünüzde (belki beklenmedik ya da ilgisiz bir konu başlığı varsa, ya da tanınmayan biri tarafından yollanmışsa) e-postayı içeriğini görmeden silmeyi seçebilirsiniz.

<a name="3.2"></a>
## 3.2 Thunderbird’de HTML Özelliği Nasıl Kapatılır? ##

**Thunderbird** iletileri yazma ve okuyabilmeniz için **Zengin Metin İşaret Dili** (**HyperText Markup Language**, **HTML**) kullanır. Bu renk, font, şekil ve diğer biçimlendirme özelliklerini kapsayan iletiler alıp göndermenizi sağlar. Fakat **HTML** aynı zamanda Web sayfaları için kullanılan bir dildir, iletileri **HTML** biçimlendirmesiyle görüntülemek sizi internet sayfalarının oluşturabileceğine benzer tehtitleri barındıran kötü niyetli e-postaların etkilerine açık bırakabilir.
 
**HTML** biçimlendirmesi özelliğini kapatmak için aşağıdaki adımı uygulayın.

**1. Adım**. ![](/sbox/screen/thunderbird-tr/24a.png)’ü tıklayarak *Thunderbird Menüsünü* açın ve aşağıda görüldüğü gibi **Seçenekler>Görünüm>İleti Gövdesi>Düz Metin’i seçin**:

![](/sbox/screen/thunderbird-tr/25.png)

*Şekil 3: İleti Metni altmenüsünde Düz Metin seçeneği seçilmiş Görünüm menüsü*

<a name="3.3"></a>
### 3.3 Thunderbird’de Güvenlik Sekmeleri Nasıl Yapılandırılır? ###

**Thunderbird’ün** iki yerleşik gereksiz posta filtresi size hangi postaların gereksiz posta olduğuna karar vermenizde yardımcı olur, ve bunların kullanılabilmesi için önce ektinleştirilmeleri gereklidir. Bu filtreler etkinleştirildikten sonra gereksiz postaları almaya devam edeceksiniz, ama bunlar **Thunderbird** tarafından otomatik olarak *Gereksiz* dizinine yönlendirilecek. 

Aynı zamanda *e-dolandırıcık* denilen e-postalarla yapılan sahtekarlıklar, genelde sizi e-posta içindeki bir linki tıklamanızı sağlamaya çalışır. Bu linkler çoğunlukla internet tarayacınızı bilsisayarınıza bir virus bulaştırmaya çalışak bir web sitesine yönlendirir. Diğer durumlarda link sizi geçerli bir kullanıcı adı ve şifre girmeye ikna edebilecek kadar meşru görünen bir siteye yönlendirir. Bu verilen kullanıcı adları ve şifreler daha sonra kullanılmak ya da ticari ve de kötü niyetli amaçları olan üçüncü partilere satılmak için saklanır.

**Thunderbird** bunun gibi e-postaları tespit etmenize yardımcı olup sizi uyarma kapasitesine sahiptir. Kötü niyetli web sitelerinden kaynaklanan saldırılara karşı diğer korunma araçları **Firefox** bölümünün [**Diğer Kullanışlı Mozilla Eklentileri**](/tr/firefox_others) kısmında tarif edilmiştir.

Gereksiz posta ve güvenlik kontrolleri farklı yerlerde konumlandırılmıştır. Bunların bir kısmına *Seçenekler - Güvenlik* penceresinden ulaşabilirsiniz. Buradaki kontroller aracılığıyla gizlilik ve güvenlik seçeneklerinin büyük bir kısmı yapılandırılabilir. Bu kontrollere ulaşmak için aşağıdaki adımları takip edin:

**1. Adım**. **Menü > Seçenekler’i seçerek** *Seçenekler* penceresini etkinleştirin.

**2. Adım**. ![](/sbox/screen/thunderbird-tr/26.png)’i tıklayarak aşağıdaki ekranı etkinleştirin:

![](/sbox/screen/thunderbird-tr/27.png)

*Şekil 4: İlgili sekmeleri görünen Güvenlik penceresi*

###Gereksiz Posta sekmesi ###

**1. Adım**. **Thunderbird’ün** sizin gereksiz posta olarak belirlediğiniz postaları silmesi için *Şekil 4’te* gösterildiği gibi *Gereksiz* sekmesindeki ilgili seçenekleri **işaretleyin**.

### E-Posta Sahtekarlığı sekmesi ###

**1. Adım**. **Thunderbird’ün** iletilerinizi e-posta sahtekarlığı için analiz etmesi için ‘Okuduğum ileti şüpheli bir e-posta sahtelarlığıysa beni uyar’ı  asağıda göründüğü gibi **işaretleyin**.

![](/sbox/screen/thunderbird-tr/28.png)

*5. Şekil: E-Posta Sahtekarlığı sekmesi* 

### The Anti-Virus tab ###

**1. Adım**. Aşağıdaki ekranı etkinleştirmek için *Antivirüs* sekmesini **tıklayın**: 

![](/sbox/screen/thunderbird-tr/29.png)

*Şekil 6: Antivirüs sekmesi* 

Bu seçenek iletilerinizin antivirus yazılımınız tarafından taranıp ayrıştırılmasını sağlar. Bu ayar etkin olmazsa, virüslü bir ileti aldığınızda *bütün* *gelen* kutunuzun *karantinaya* alınması mümkündür.

**Not**: Bu adım çalışan bir antivirus programınız olduğunu varsayar. Antivirüs programını nasıl kurup yapılandırabileceğinize dair bilgi almak için lütfen [**Avast**](/tr/avast_main)'a bakın.

### Parolalar Sekmesi ###

**1. Adım**. *Parolalar* sekmesini **tıklayarak** aşağıdaki ekranı **etkinleştirin**: 

![](/sbox/screen/thunderbird-tr/30.png)

*Şekil 7: Parolalar sekmesi*

**Dikkat**: Parolalarınızı gizli tutmanız ve onların güvenliğini sağlamanız için tasarlanmış olan bir program kullanmanızı şiddetle tavsiye ederiz; daha fazla bilgi edinmek için lütfen [**KeePass**](/en/keepass_main)’e başvurun.

**Not**: *Parolalar* sekmesindeki seçenekler, e-posta hesaplarnızı **Thunderbird’de** ilk kaydettiğiniz esnada, *Posta Hesabı Kurulumu* ekranında *Parolaları Hatırla* seçeneğini işaretlediyseniz etkin olacaktır.

**1. Adım**. ![](/sbox/screen/thunderbird-tr/31.png)’ı tıklayarak aşağıdaki ekranı etkinleştirin:

![](/sbox/screen/thunderbird-tr/32.png)

*Şekil 8: Kayıtlı Parolalar penceresi*

*Kayıtlı Parolalar* penceresi bütün hesaplarınızla ilişkili parolalarınızı kaldırmanızı ya da görüntülemenizi sağlar. Yine de, gizliliğinizi ve güvenliğinizi daha da yükseltmek için, bütün e-posta hesaplarınıza erişimi bir *Ana Parola* belirleyerek koruyabilirsiniz. Bu **Thunderbird’ün** parola seçenekleri ile tanıdık olan bir kimsenin sizin hesap parolalarınıza ulaşımını engeller.

**3. Adım**. *Ana parola kullan* seçeneğini *Şekil 7’de* göründüğü gibi **işaretliyerek** aşağıdaki ekranı etkinleştirin.

![](/sbox/screen/thunderbird-tr/34.png)

*Şekil 9: Ana Parolayı Değiştir penceresi*

**5. Adım**. Yeterince güçlü olan ve sadece sizin hatırlayabileceğiniz bir parola **girin** ve ![](/sbox/screen/thunderbird-tr/35.png)’ı **tıklayarak** bunu teyit edin. 

### Web İçeriği ###

Web tarayıcınızın bir web sitesinin kimliğini denetlemek ya da tespit etmek için kullandığı kısa metinlere çerez denir. *Web İçeriği* seçeneği hangi blog, haber akışı ya da haber grubuna ait çerezlerin güvenilir ve emniyetli olduğunu belirlemenizi sağlar.

**1. Adım**. ![](/sbox/screen/thunderbird-tr/36.png)’e tıklayarak Web İçeriği seçeneklerini aşağıda görüldüğü gibi açın:

![](/sbox/screen/thunderbird-tr/37.png)

*Şekil 10: Gizlilik Sekmesi*

**2. Adım**. *Şu ana kadar sakla* altında *Ben Thunderbird’ü kapatana kadar’ı* seçin: bu seçenek çerezleri **Thunderbird’ü** her kapatışınızda çerezleri silerek güvenliğinizi artırır.

<a name="3.4"></a>
### 3.4 Hesap Ayarları - Gereksiz Posta Filtresi Nasıl Açılır? ###

İkinci tür **Thunderbird** gereksiz posta filtresine *Hesap Ayarları – Gereksiz Posta Ayarları* penceresinden ulaşılabilinir. Bu filtreler verili olarak etkin değildir, bu yüzden bunları kullanmak isterseniz etkinleştirmeniz gerekir. Böylelikle gereksiz posta teslim alındığında **Thunderbird** onu otomatik olarak değişik hesaplarla ilgili *Gereksiz* dizinlerine yönlendirir.

**1. Adım**. **Seçenekler > Hesap Ayarları’nı seçerek** *Hesap Ayarları* penceresini etkinleştirin.

**2. Adım**. Kenar çubuğunda görülen belirli bir **Gmail** ya da **RiseUp** hesabıyla ilişkili *Gereksiz Posta Ayarları* seçeneğini seçin.

**3. Adım**. Gereksiz Posta Ayarlarını **etkinleştirin** ve  Hesap Ayarları- Gereksiz Posta Ayarları ekranı aşağıdakine benzesin: 

![](/sbox/screen/thunderbird-tr/38.png)

*Şekil 11: Hesap Ayarları – Gereksiz Posta Ayarları penceresi*

**4. Adım**: ![](/sbox/screen/thunderbird-tr/35.png)’ı tıklarayak *Hesap Ayarları* penceresinin yapılandırılmasını tamamlayın.

**Not**: *Gereksiz Posta Ayarları* her bir hesap için ayrı ayrı yapılandırılmalıdır. Böylelikle, bir **Gmail** ya da **RiseUp** hesabına gelen **Gereksiz Postalar** ilgili *Çöp* dosyasına yerleştirilecektir. Bunun yerine bütün hesaplarınızın gereksiz postalarını sizin belirlediğiniz bir *Yerel Dizine* yönlendirebilirsiniz.

![](/sbox/screen/thunderbird-tr/39.png)

*Şekil 12: Hesap Ayarları - Gereksiz Posta Ayarları penceresi, merkezi bir gereksiz posta dizini için ayarları gösteriyor*

**1. Adım**: *Gereksiz Posta Ayarları’nı* **Seçin**, bu, kenar çubuğunda *Yerel Dizinler’in* hemen altındadır.

**2. Adım**: *Gereksiz Postaları Yönlendir* aşağı açılar listesinden *Yerel Dizinler’i*  *Şekil 12’de* görüldüğü gibi **seçin**.

**3. Adım**.  ![](/sbox/screen/thunderbird-tr/35.png)’ı tıklayarak *Hesap Ayarları* penceresinin yapılandırılmasını tamamlayın.

Şimdi **Thunderbird’deki** farklı güvenlik seçenekleri ve gereksiz posta ayarlarını yapılandırdığınıza göre, lütfen bir sonraki [**Thunderbird’de GnuPG’li Enigmail Nasıl Kullanılır?**](/tr/thuderbird_encryption) bölümüne devam edebilirsiniz.

