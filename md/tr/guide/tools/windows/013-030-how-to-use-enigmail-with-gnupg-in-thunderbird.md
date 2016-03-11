

---

lang: tr
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: How to Use Enigmail with GnuPG in Thunderbird

---

Bu sayfadaki kısımların listesi:

- [**4.0 Enigmail, GnuPG ve Açık-Kişisel Anahtar Şifreleme ile İlgili Genel Bilgiler**](#4.0)
- [**4.1 Enigmail ve GnuPG Nasıl Yüklenir?**](#4.1)
- [**4.2 Anahtar Çiftleri Nasıl Oluşturulur ve Enigmail Kendi E-posta Hesaplarınızla Uyumlu Çalışacak Şekilde Nasıl Yapılandırılır?**](#4.2)
- [**4.3 Açık Anahtarlar Nasıl Paylaşılır?**](#4.3)
- [**4.4 Anahtar Çifti Nasıl Doğrulanır ve İmzalanır?**](#4.4)
- [**4.5 Bir Mesaj Nasıl Şifrelenir ve Bir Mesajın Şifresi Nasıl Çözülür?**](#4.5)

<a name="4.0"></a>
## 4.0 Enigmail, GnuPG ve Açık-Kişisel Anahtar Şifreleme ile İlgili Genel Bilgiler ##

**Enigmail** e-posta iletişim gizliliğinizi korumaya yarayan bir **Mozilla Thunderbird** eklentisidir. **Enigmail** **GnuPG** şifreleme programını **Thunderbird’ün** içinde kullanmanıza izin veren bir arayüzdür. **Enigmail** arayüzü, **Thunderbird** konsol araç çubuğunda *Enigmail* olarak görülür

**Engimail** [**açık-anahtarlı şifreyazımına**](http://tr.wikipedia.org/wiki/Açık_anahtarlı_şifreleme) dayanır. Bu yöntemle kişi kendi kişisel anahtar çiftini oluşturmalıdır. Oluşturulan ilk anahtara *kişisel* anahtar denir. Kişisel anahtar bir kullanıcı şifresi veya parola tarafından korunur ve *asla* *kimse* ile paylaşılmaz. 

İkinci anahtara *açık anahtar* denir. Bu anahtar iletişim kurduğunuz kimseler ile paylaşılabilir. Ancak herhangi bir kişinin *açık anahtarını* edindikten sonra bu kişiye şifrelenmiş e-posta gönderebilirsiniz. Bu kişi eşleşen *kişisel anahtara* erişimi olan tek kişi olduğu için, e-postanızın şifresini çözebilen ve onu okuyabilen tek kişi de odur. 

Aynı şekilde, kendi *açık şifrenizin* bir kopyasını e-posta iletişiminde olduğunuz insanlara gönderir ve eşleşen *kişisel anahtarı* gizli tutarsanız, bu kişilerden gelecek şifreli mesajları yalnızca siz okuyabilirsiniz.

**Enigmail** aynı zamanda mesajlarınıza *dijital imza* eklemenize de olanak verir. *Açık şifrenize* sahip olan kişi, e-postanın sizden geldiğini bu şekilde doğrulayabilir ve içeriğinin bir başkası tarafından değiştirilmediğinden emin olabilir. Benzer bir biçimde, iletişimde olduğunuz kişinin *açık anahtarına* sahipseniz, onun imzalanmış mesajlarındaki dijital imzasını doğrulayabilirsiniz.

<a name="4.1"></a>
## 4.1 Enigmail ve GnuPG Nasıl Yüklenir? ##

**Enigmail** ve **GnuPG’nin** nasıl indirileceği konusunda bilgi almak için lütfen [**indirme kısmına**](/tr/thunderbird_main) bakın. 

### 4.1.1 GnuPG nasıl kurulur? ###

**GnuPG’yi** kurmak oldukça basittir. Daha önce yaptığınız yazılım kurma işlemlerinden farklı değildir ve aşağıdaki adımları izleyerek gerçekleştirilebilir:

**1. Adım**. Kurulum işlemini başlatmak için  ![](/sbox/screen/thunderbird-tr/40.png)’ye **çift tıklayın**. *Dosyayı Aç – Güvenlik Uyarısı* iletişim kutusu ekranda belirirse  ![](/sbox/screen/thunderbird-tr/02.png)'I ) (Çalıştır) **tıklayın**, aşağıdaki ekran belirecek: 

![](/sbox/screen/thunderbird-tr/41.png)

*Şekil 1: GNU Gizlilik Koruma Kurulum Sihirbazı*

**2. Adım**. *GNU Gizlilik Koruma Kurulumu – Lisans Anlaşması* penceresini etkinleştirmek için ![](/sbox/screen/thunderbird-tr/04.png)’yi tıklayın. Okuduktan sonra *GNU Gizlilik Koruma Kurulumu – Bileçen Seçimi* penceresini etkinleştirmek için ![](/sbox/screen/thunderbird-tr/04.png)’yi **tıklayın**. 

**3. Adım**. Varsayılan ayarları kabul etmek ve GNU *Gizlilik Koruma Kurulumu – Kurulum Seçenekleri – GnuPG Dil Seçimi* penceresini etkinleştirmek için ![](/sbox/screen/thunderbird-tr/04.png)’yi **tıklayın**. 

**4. Adım**. Aşağı açılır menüden *Türkçe'yi* seçin ve *Kurulum Yerini Seç* penceresini etkinleştirmek için ![](/sbox/screen/thunderbird-tr/04.png)’yi **tıklayın**.

**5. Adım**. Varsayılan kurulum yolunu kabul etmek ve *Başlangıç Menüsü Dosyası Seç* ekranını etkinleştirmek için ![](/sbox/screen/thunderbird-tr/06.png)’u **tıklayın**. 

**6. Adım**. Paket açmayı ve çeşitli **GnuPG99** paketlerini kurmayı başlatmak için ![](/sbox/screen/thunderbird-tr/06.png)’u **tıklayın**. Bu işlem tamamlandıktan sonra, *Kurulum Tamamlandı* ekranı görünecek.

**7. Adım**. **GnuPG** programı kurulumunu tamamlamak için ![](/sbox/screen/thunderbird-tr/04.png) ve daha sonra ![](/sbox/screen/thunderbird-tr/08.png)'u **tıklayın**.

<a name="4.1.2"></a>
### 4.1.2 Enigmail Eklentisi Nasıl Kurulur? ###

**GnuPG** yazılımının kurulumunu başarı ile gerçekleştirdikten sonra **Enigmail** eklentisini kurmaya hazırsınız.

**Enigmail** kurulumu için aşağıdaki adımları takip edin:

 **1. Adım**. **Thunderbird’ü açın** ve ![](/sbox/screen/thunderbird-tr/24a.png)’i **tıklayın**. Açılan *Thunderbird Menü’sünden* **Eklentileri seçin** ve *Eklenti Yöneticisi* penceresini etkinleştirin.

**2. Adım**. Sol taraftaki kenar çubuğunda ![](/sbox/screen/thunderbird-tr/44.png)’i **tıklayın**. Enigmail Eklenti’si henüz bulunamadıysa, *Kurulmuş Bu Tip Eklentiniz Bulunmamaktadır* mesajını göreceksiniz.   

**3. Adım**. Enigmail Eklentisi *Uzantı* panelinde görünürse ![](/sbox/screen/thunderbird-tr/46.png)’u **tıklayın**. Eğer görünmezse ![](/sbox/screen/thunderbird-tr/45a.png)’i **tıklayın** ve aşağıda göründüğü şekilde *Eklentiyi Dosyadan Kur’u* **seçin**: 

![](/sbox/screen/thunderbird-tr/46a.png)

*Şekil 3: Eklentiler için Araçlar Menüsü*

**4. Adım**. Aşağıda göründüğü gibi Enigmail uzantısını kaydettiğiniz klasöre gidin (büyük ihtimalle *İndirilenler* klasörü):

![](/sbox/screen/thunderbird-tr/47.png)

*Şekil 4: Kurulacak bir Uzantı Seçin*

**5. Adım**. Aşağıdaki ekranı etkinleştirmek için  ![](/sbox/screen/thunderbird-tr/48.png)’ı **tıklayın**:

![](/sbox/screen/thunderbird-tr/49.png)

*Şekil 5: Yazılım Kurulumu Penceresi*

**Önemli**: 6. Adım’ı uygulamadan önce yaptığınız tüm çevrimiçi işlemleri kaydettiğinizden emin olun!

**6. Adım**. ![](/sbox/screen/thunderbird-tr/50.png)’u **tıklayın** ve daha onra **Enigmail** eklentisi kurulumunu tamamlamak için ![](/sbox/screen/thunderbird-tr/51.png)’ı **tıklayın**. 

**Enigmail** eklentisi kurulumunun başarı ile gerçekleştiğinden emin olmak için **Thunderbird** ana kullanıcı arayüzüne geri dönün ve ![](/sbox/screen/thunderbird-tr/24a.png)’i **tıklayın**. *Enigmail’in* aşağıdaki gibi seçenekler arasında yer aldığından emin olun.

![](/sbox/screen/thunderbird-tr/52.png)

*Şekil 6: Thunderbird araç çubuğu ve işaretlenmiş olan Enigmail*

### 4.1.3 Enigmail ve GnuPG’nin Çalıştığından Nasıl Emin Olunur? ###

E-postalarınızın kimlik doğrulamasını yapmak ve onları şifrelemek için **Enigmail** ve **GnuPG** kullanmaya başlamadan önce, bu iki yazılımın birbiri ile iletişim içinde çalıştığından emin olmalısınız.

**1. Adım**. **Enigmail  > Tercihleri’i seçin** ve aşağıda göründüğü gibi *Enigmail Tercihler* ekranına ulaşın:

![](/sbox/screen/thunderbird-tr/53.png)

*Şekil 7: Enigmail Tercihler penceresi*

**GnuPG** başarılı bir şekilde kurulmuşsa *Dosyalar ve Dizinler* bölümünde şunu göreceksiniz: ![](/sbox/screen/thunderbird-tr/54.png). Aksi takdirde, aşağıdakine benzer bir uyarı ile karşılaşabilirsiniz:

![](/sbox/screen/thunderbird-tr/55.png)

*Şekil 8: Enigmail Uyarı Açılır Mesajı*

**İpucu**: Bu mesajı alıyorsanız **GnuPG’yi** kurmadınız veya başka bir yere kurdunuz demektir. **GnuPG’yi** başka bir yere kurduysanız, *Tara...* tuşunu etkinleştirmek seçeneği için *Üstüne Yaz'ı* **işaretleyin**. Daha sonra **GnuPG programını bul'u** etkinleştirmek için ![](/sbox/screen/thunderbird-tr/69.png)'ı **tıklayın** ve bilgisayarınızda *gpg.exe* dosyasının olduğu yere gidin. Bu işlem başarılı olmuyorsa, lütfen [4.1 Enigmail ve GnuPG Nasıl Kurulur?](#4.1) Bölümüne geri dönün. 

**2. Adım**. **Thunderbird** konsoluna geri dönmek için ![](/sbox/screen/thunderbird-tr/35.png)’ı **tıklayın**.   

<a name="4.2"></a>
## 4.2 Anahtar Çiftleri Nasıl Oluşturulur ve Enigmail Kendi E-posta Hesaplarınızla Uyumlu Çalışacak Şekilde Nasıl Yapılandırılır? ##

**Enigmail** ve **GnuPG’nin** düzgün bir şekilde çalıştığından emin olduktan sonra e-posta hesaplarınızdan bir veya birkaçını, bir ya da birden fazla açık-kişisel anahtar çifti oluşturacak şekilde **Enigmail** kullanmaları için yapılandırabilirsiniz. 


### 4.2.1 Anahtar Çifti Oluşturmak için Enigmail Sihirbazı Nasıl Kullanılır? ###

**Enigmail** açık-kişisel anahtar çifti oluşturmak için iki yol sunar. Birincisi *Enigmail Kurulum Sihirbazı*, ikincisi ise *Anahtar Yönetimi* ekranını kullanır. 

*Enigmail Kurulum Sihirbazı* kullanarak ilk defa anahtar çifti oluşturmak için aşağıdaki adımları takip edin:

**1. Adım**. **Kurulum Sihirbazı** penceresi henüz etkin değilse **Enigmail > Kurulum Sihirbazı’nı seçin** ve *Enigmail Kurulum Sihirbazı* ekranını aşağıda göründüğü şekilde açın:

![](/sbox/screen/thunderbird-tr/56.png)

*Şekil 9: Enigmail Kurulum Sihirbazı’na Hoşgeldiniz penceresi*

**2. Adım**. Aşağıdaki ekranı etkinleştirmek için ![](/sbox/screen/thunderbird-tr/04.png)’yi **tıklayın**. *Bu ekran sadece başka bir hesap için anahtar çiftlemeyi kurmuşsanız açılacaktır*.

![](/sbox/screen/thunderbird-tr/59.png)

*Şekil 10: Kimlikleri Seç ekranı*

**3. Adım**. Aşağıdaki ekranı etkinleştirmek için ![](/sbox/screen/thunderbird-tr/04.png)’yi **tıklayın**.

![](/sbox/screen/thunderbird-tr/60.png)

*Şekil 11: Şifreleme – Giden E-postalarınızı Şifreleyin ekranı*

**4. Adım**. Aşağıdaki ekranı etkinleştirmek için ![](/sbox/screen/thunderbird-tr/04.png)'yi **tıklayın**.

![](/sbox/screen/thunderbird-tr/61.png)

*Şekil 12: İmzalama – Giden E-postalarınızı Dijital Olarak İmzalayın ekranı*

**5. Adım**. Aşağıdaki ekranı etkinleştirmek için ![](/sbox/screen/thunderbird-tr/04.png)’yi **tıklayın**.

![](/sbox/screen/thunderbird-tr/62.png)

*Şekil 13: Tercihler – Enigmail’in Daha Düzgün Çalışması İçin E-posta Ayarlarınızı Değiştirin ekranı*

**6. Adım**. *Anahtar Yarat – E-postalarınızı İmzalamak ve Şifrelemek için Anahtar Yarat* penceresini etkinleştirmek için ![](/sbox/screen/thunderbird-tr/04.png)'yi **tıklayın**.

**Not**: Bir e-posta hesabı için ilk defa anahtar yarattığınız zaman, *OpenPGP Anahtarı Bulunamadı* ekranı görünecektir. 

**7. Adım**. *E-postamı imzalamak ve şifrelemek için yeni bir anahtar çifti yaratmak istiyorum’u* **seçin**.

**8. Adım**. Her iki *Parola* alanına güçlü bir parola **girin**. 

![](/sbox/screen/thunderbird-tr/65.png)

*Şekil 15: Anahtar Yarat – E-postalarınızı İmzalamak ve Şifrelemek için Anahtar Yarat penceresi*

**9. Adım**. *Özet* ekranını etkinleştirmek için ![](/sbox/screen/thunderbird-tr/04.png)’yi **tıklayın**. Bu ekran anahtar çifti oluştururken kullanılan ayarları gösterecektir.

**10. Adım**. Aşağıda göründüğü gibi anahtar çifti oluşturmayı başlatmak için ![](/sbox/screen/thunderbird-tr/04.png)’yi **tıklayın**:

![](/sbox/screen/thunderbird-tr/67.png)

*Şekil 16: Anahtar Oluşturma – Şu anda anahtarınız oluşturuluyor penceresi*

**Not**: *Enigmail Kurulum Sihirbazı* tarafından oluşturulan her anahtar çifti otomatik olarak 4096-bit büyüklüğündedir ve 5 yıllık ömrü vardır. 

**11. Adım**. Anahtar oluşturulduktan sonra bir iptal etme sertifikası yaratmak için yönlendirileceksiniz. Aşağıda görüldüğü şekilde ![](/sbox/screen/thunderbird-tr/76.png)’ı **tıklayın**:

![](/sbox/screen/thunderbird-tr/68.png)

*Şekil 17: Enigmail Onay daveti*

**Not**: Zararlı veya kötü niyetli bir tarafın kişisel anahtarınıza izinsiz erişim kazandığını öğrenir veya anahtarınıza erişiminizi kaybederseniz iptal etme sertifikasını iletişimde olduğunuz kişilere gönderebilir ve sizin eşleşmiş Açık anahtarınızı kullanmamaları gerektiğini bildirebilirsiniz. Bilgisayarınızın kaybolması, çalınması veya ele geçirilmesi durumunda da aynı işlemi yapmanız gerekir. İptal sertifikanızı yedeklemenizi ve korumanızı şiddetle öneririz. 

**12. Adım**. Yeni oluşturulan anahtarınız ile bağlantılı olan parolanızı **girmeniz** istenecek. Bu işlemden sonra sertifikanızı güvenli bir şekilde saklayacağınız bir yer **seçin** ve takip eden ekranda ![](/sbox/screen/thunderbird-tr/78.png)’i tıklayın.

![](/sbox/screen/thunderbird-tr/70.png)

*Şekil 18: İptal Etme Sertifikasını Yarat ve Sakla*

**13. Adım**. Anahtar çiftini ve iptal etme sertifikasını oluşturmayı tamamlamak için ![](/sbox/screen/thunderbird-tr/04.png)’yi **tıklayın**.

### 4.2.2 Başka bir E-posta Hesabı için Nasıl Ek Anahtar Çifti ve İptal Etme Sertifikası Oluşturulur? ###

Her e-posta hesabı için ayrı bir anahtar çifti oluşturmak yaygın bir yöntemdir. Birden fazla e-posta hesabı için aynı anahtar çiftini kullanmak mümkündür, fakat bu durum iletişimde olduğunuz kişiler için kafa karıştırıcı olabilir. Tek bir anahtar çiftine birden fazla e-posta hesabı eklenebilir (bu konuya bu bölümde değinmiyoruz) ve bunun belli kullanım faydaları vardır, ama bu yöntem tüm bu e-posta hesaplarını tek bir kişi ile ilişkilendirmiş olur ki bu da istenmeyen bir durum olabilir. 

Diğer e-posta hesaplarınız için ek anahtar çiftleri oluşturmak istiyorsanız aşağıdaki adımları takip edin.

**1. Adım**. Aşağıda görünen ekranı etkinleştirmek için **Enigmail > Anahtar Yönetimi’ni** **seçiniz**:

![](/sbox/screen/thunderbird-tr/71.png)

*Şekil 19: Enigmail Anahtar Yönetimi Oluşturma menüsünde seçilmiş Yeni Anahtar Çifti*

**Not**: İlk e-posta hesabınız için *OpenPGP Kurulum Sihirbazı* ile oluşturulan anahtar çiftini görmek için *Varsayılan Tüm Anahtarları Göster’i* **seçin**. Bu ekranı yukarıdaki *Şekil 19* ve aşağıdaki *Şekil 23’te* görebilirsiniz. 

**2. Adım**. Yukarıdaki *Şekil 19’da* görüldüğü gibi *Anahtar Yönetimi’nden* **Oluştur > Yeni Anahtar Çifti’ni** **seçin**. Bunu yaptığınız zaman aşağıdaki ekranı göreceksiniz: 

![](/sbox/screen/thunderbird-tr/72.png)

*Şekil 20: OpenPGP Anahtarı Oluştur ekranı*

**3. Adım**. *Açılan Hesap – Kullanıcı Kimliği* listesinden bir e-posta hesabı **seçin** ve *Seçilen kimlik için oluşturulan anahtarı kullan’ı* **işaretleyin**. Kişisel anahtarınızı korumak için bir parola oluşturun. 

**Not**: Parola kullanıcı şifresinden daha uzundur. **Enigmail** sizi sıradan bir kullanıcı şifresinden daha uzun ve daha güvenli bir parola kullanmaya teşvik eder. 

**Önemli**: Anahtar çiftlerini her zaman güvenli bir parola ile oluşturun ve **hiçbir zaman** ‘parola istemiyorum’ seçeneğini etkinleştirmeyin.

![](/sbox/screen/thunderbird-tr/73.png)

*Şekil 21: OpenPGP Anahtarı Oluştur ekranında seçili Anahtar Zaman Aşımı sekmesi*

**Not**: Bir anahtar çiftinin geçerli kalma süresi tamamen sizin gizlilik ve güvenlik ihtiyaçlarınıza bağlıdır. Anahtar çiftlerinizi ne kadar sık değiştirirseniz, yeni anahtar çiftinizin tehlike altına girme olasılığı o kadar düşük olur. Bununla birlikte, anahtar çiftinizi her değiştirdiğinizde, iletişimde olduğunuz kişilere açık şifrenizi yeniden göndermeniz ve her biri ile yeniden onaylamanız gerekir. 


**4. Adım**. Uygun bulduğunuz sayıyı **tuşlayın** ve anahtarınızın geçerli kalmasını istediğiniz zaman birimini (*gün*, *ay* veya *yıl*) **seçin**.

**5. Adım**. Enigmail Onaylama penceresini etkinleştirmek için ![](/sbox/screen/thunderbird-tr/74.png)’i **tıklayın**. 

**6. Adım**. *Şekil 17’de* görüldüğü gibi bir sertifika oluşturmak için yönlendirileceksiniz.

**7. Adım**. *İptal Etme Sertifikası Yarat ve Kaydet* gezinim penceresini etkinleştirmek için ![](/sbox/screen/thunderbird-tr/76.png)’ı **tıklayın**. 

**Not**: Eğer zararlı veya kötü niyetli bir tarafın kişisel anahtarınıza izinsiz erişim kazandığını öğrenir veya anahtarınıza erişiminizi kaybederseniz, iptal etme sertifikasını iletişimde olduğunuz kişilere gönderebilir ve sizin eşleşmiş açık anahtarınızı kullanmamaları gerektiğini bildirebilirsiniz. Bilgisayarınızın kaybolması, çalınması veya ele geçirilmesi durumunda da aynı işlemi yapmanız gerekir. İptal sertifikanızı yedeklemenizi ve korumanızı şiddetle öneririz.

**8. Adım**. Sertifikanızı aşağıdaki ekranda görüldüğü gibi kaydedecek güvenli bir yer seçin ve ![](/sbox/screen/thunderbird-tr/78.png)'i **tıklayın**. Sizden yeni yaratılmış anahtarınız için bir parola girmeniz istenecek. 

![](/sbox/screen/thunderbird-tr/77.png)

*Şekil 22: İptal Etme Sertifikası Yaratma ve Kaydetme*

**9. Adım**. Anahtar çifti ve iptal etme sertifikası oluşturmayı tamamlamak için  ![](/sbox/screen/thunderbird-tr/35.png)’ı **tıklayın** ve aşağıda görünen ekrana geri dönün:

![](/sbox/screen/thunderbird-tr/79.png) 

*Şekil 23: Engimail Anahtar Yönetimi penceresinde görünen anahtar çifti*

**Not**: Tüm anahtar çiftlerini ve onlarla ilişkili hesapları görüntülemek için *Varsayılan Tüm Anahtarları Görüntüle* seçeneğini **seçin**. Bunu yaparken güvenli bir ortamda olduğunuzdan emin olun.

Anahtar çiftinizi ve ona ait iptal etme sertifikasını başarılı bir şekilde oluşturduktan sonra açık şifrelerinizi güvendiğiniz kişilerle paylaşmaya hazırsınız. 

### 4.2.3 Enigmail’i E-posta Hesabınız ile Kullanmak için Nasıl Yapılandırmalısınız?###

**Enigmail’i** belli bir e-posta hesabı ile kullanmak için aşağıdaki adımları takip edin: 

**1. Adım**. Thunderbird Menü’sünü açmak için ![](/sbox/screen/thunderbird-tr/24a.png)’i **tıklayın** ve **Seçenekler > Hesap Ayarları’nı seçin**.

**2. Adım**. Kenar çubuğunda *OpenPGP Güvenlik* menüsünü aşağıda göründüğü gibi **seçin**: 

![](/sbox/screen/thunderbird-tr/80.png)

*Şekil 24: Hesap Ayarları - OpenPGP Güvenlik ekranı*

**3. Adım**. *Bu kimlik için OpenPGP desteğini (Enigmail) aç* seçeneğini **işaretleyin** ve *OpenPGP anahtarını tanımak için bu kimliğin e-posta adresini kullan* seçeneğini **seçin**. 

**4. Adım**. **Thunderbird** konsoluna geri dönmek için ![](/sbox/screen/thunderbird-tr/35.png)'ı **tıklayın**. 

<a name="4.3"></a>
## 4.3 Açık Anahtarlar Nasıl Karşılıklı Değiş Tokuş Edilir ##

Birbirinize şifrelenmiş e-posta mesajları göndermeye başlamadan önce, iletişimde olduğunuz kişilerle açık anahtarlarınızı değiş tokuş etmeniz gerekir. Size gelen herhangi bir anahtarı kabul etmeden önce onun gerçekten gönderen kişiye ait olduğunu onaylamanız gerekir.  

### 4.3.1 Enigmail Kullanarak Açık Anahtar Nasıl Gönderilir?###

**Enigmail** kullanarak açık anahtar göndermek için sizin ve iletişimde olduğunuz kişinin aşağıdaki adımları takip etmesi gerekir:

**1. Adım**. **Thunderbird’ü açın** ve yeni bir mesaj yazmak için ![](/sbox/screen/thunderbird-tr/81.png)’yi **tıklayın**. 

**2. Adım**. Menüden **Enigmal > Açık Anahtarımı Ekle** seçeneğini **seçin**.

**Not**: Bu yöntemde **Eklentiler** bölmesi hemen görünmeyebilir, fakat mesajı gönderdiğiniz anda görünecektir. 

Eğer başka bir açık anahtar göndermek isterseniz, menüden **Enigmail > Açık Anahtar Ekle...** seçeneğini **seçin** ve daha sonra göndermek istediğiniz anahtarı **seçin**. 

![](/sbox/screen/thunderbird-tr/82.png) 

*Şekil 25: Eklentiler bölmesindeki eklenmiş açık anahtarı gösteren Mesaj Yaz bölmesi.*

**3. Adım**. Eklenmiş açık anahtarınız ile e-posta göndermek için ![](/sbox/screen/thunderbird-tr/83.png)’i **tıklayın**. 

### 4.3.2 Açık Anahtar Enigmail Kullanarak Nasıl İçeri Aktarılır? ###

Hem siz hem de iletişimde olduğunuz kişi birbirinizin açık anahtarlarını içeri aktarırken aşağıdaki adımları takip etmelisiniz:

**1 Adım**. İletişimde olduğunuz kişinin açık anahtarını içeren e-postayı **seçin** ve **açın**. Ek şu şekilde görünecektir: 1attachment:  ![](/sbox/screen/thunderbird-tr/87.png)

**2. Adım**. ![](/sbox/screen/thunderbird-tr/87a.png)'nun üstüne görünen ek dosyaya **tıklayın**. **Enigmail** açık anahtar içeren e-postayı tanıyacak ve aşağıda göründüğü şekilde sizi  açık anahtarı içeri aktarmaya davet edecektir: 

![](/sbox/screen/thunderbird-tr/88.png)

*Şekil 26: Enigmail Açık Anahtarı İçeri Aktarmayı Onayla* 

**3. Adım**. İletişimde olduğunuz kişinin açık anahtarını içeri aktarmak için İçeri ![](/sbox/screen/thunderbird-tr/89.png)'ı **tıklayın**. 

Açık anahtarı başarılı bir şekilde içeri aktardıysanız, aşağıdakine benzer bir mesaj göreceksiniz:

![](/sbox/screen/thunderbird-tr/90.png)

*Şekil 27: İletişimde olduğunuz kişinin açıkanahtarını gösteren Enigmail Uyarı ekranı*

İletişimde olduğunuz kişinin açık anahtarını başarılı bir şekilde içeri aktardığınızı doğrulamak için, aşağıdaki adımı uygulayın: 

**1. Adım**. *Enigmail Anahtar Yönetimi* ekranını aşağıda göründüğü gibi görüntülemek için **Enigmail > Anahtar Yönetimi’ni seçin**: 

![](/sbox/screen/thunderbird-tr/91.png)

*Şekil 28: Yeni içeri aktarılmış bir açık anahtarı gösteren Enigmail – Anahtar Yönetimi ekranı* 

Anahtarları görmek için *Varsayılan Tüm Anahtarları Göster* seçeneğinin seçili olması gerektiğini **unutmayın**. 

<a name="4.4"></a>
## 4.4 Bir Anahtar Çifti Nasıl Doğrulanır ve İmzalanır?##

Son olarak, içeri aktarılan anahtarın gerçekten de gönderdiği görülen kişi tarafından gönderildiğini doğrulamalı ve geçerliliğinden emin olmalısınız. Bu, gönderilen her açık anahtar için hem sizin hem de e-posta yoluyla iletişimde olduğunuz herkesin uygulaması gereken bir adımdır. 

### 4.4.1 Anahtar Çifti Nasıl Doğrulanır? ###

**1. Adım**. İletişimde olduğunuz kişi ile e-posta olmayan bir yöntem üzerinden **irtibat kurun**. Bu telefon, cep telefonu mesajı, **Voice over Internet Protocol** (**VoIP**) veya herhangi başka bir yöntem olabilir, fakat her durumda doğru kişi ile görüştüğünüzden **tamamıyla emin olun**. Bu bakımdan, eğer imkânınız varsa ve güvenli bir şekilde ayarlayabiliyorsanız ses veya video görüşmeleri veya yüz yüze görüşmeler en uygun yöntemlerdir. 

**2. Adım**. Hem siz hem de iletişimde olduğunuz kişi değiş tokuş ettiğiniz açık anahtarların ‘parmak izlerini’ doğrulamalıdır. Parmak izi, her anahtarı belirleyen özgün sayı ve harf dizlerinden oluşur. Yarattığınız ve içeri aktardığınız anahtar çiftlerinin parmak izlerini görmek için **Enigmail** *Anahtar Yönetimi* ekranını kullanabilirsiniz. 

Bir anahtar çiftinin parmak izlerini görmek için aşağıdaki adımları takip edin:

**1. Adım**. **Enigmail > Anahtar Yönetimi’ni seçin** ve açılır menüyü etkinleştirmek için belli bir anahtarın üzerine **sağ tıklayın**. 

![](/sbox/screen/thunderbird-tr/92.png) 

*Şekil 29: Enigmail Anahtar Yönetimi menüsünde seçili Anahtar Özellikleri*

**2. Adım**. Aşağıdaki ekranı etkinleştirmek için *Anahtar Özellikleri* maddesini **seçin**:

![](/sbox/screen/thunderbird-tr/93.png)

*Şekil 30: Anahtar Özellikleri ekranı*

İletişimde olduğunuz kişi de aynı adımları takip etmelidir. Parmak izlerini doğrulamak için, kendi anahtarınızın parmak izlerini iletişimde olduğunuz kişiye okuyun ve onun almış olduğu açık anahtardaki parmak izleri ile aynı olduğunu doğrulamasını isteyin. Daha sonra, iletişimde olduğunuz kişiden aynısını kendi anahtarlarının parmak izleri için yapmasını isteyin. Eğer parmak izleri birbirleri ile uyumlu değilse, açık anahtarlarınız yeniden değiş tokuş edin ve doğrulama işlemini yeniden yapın.

**Not**: Parmak izinin kendisi gizli tutulmak zorunda değildir ve doğrulama işlemini daha sonra yapmak üzere kaydedilebilir.

### 4.4.2 Doğru bir Açık Anahtar Nasıl İmzalanır ###

İletişimde olduğunuz kişinin anahtarını doğruladıktan sonra, bu anahtarı geçerli kabul ettiğinizi belirtmek için onu *imzalayabilirsiniz*. Anahtarları imzalamak, imzalanmış anahtarı başkasına gönderdiğiniz veya anahtar dağıtıcısına aktardığınız zaman siz ve iletişimde olduğunuz kişi arasındaki bağı görünür hale getirebilir. Bu durumu engellemek için her zaman aşağıdaki *Yerel İmza* seçeneğini seçin. 

Doğrulanmış bir açık anahtarı imzalamak için aşağıdaki adımları takip edin: 

**1. Adım**. *Anahtar Yönetimi* ekranını açmak için **Enigmail > Anahtar Yönetimi’ni seçin**.

**2. Adım**. *Anahtar Yönetimi* ekranından (bkz. yukarıdaki Şekil 29) iletişimde olduğunuz kişinin açık anahtarına **sağ tıklayınız** ve menüden aşağıdaki ekranı etkinleştirmek için **Anahtarı İmzala** maddesini **seçin**:

![](/sbox/screen/thunderbird-tr/94.png)

*Şekil 31: Enigmail – Anahtarı İmzala ekranı*

**3. Adım**. *Çok dikkatle kontrol ettim* seçeneğini **işaretleyin**, *Yerel imza (dışarı aktarılamaz)* seçeneğini **seçin** ve iletişimde olduğunuz kişinin açık anahtarını imzalamak için ![](/sbox/screen/thunderbird-tr/35.png)’ı **tıklayın**. 

#### 4.4.3 Kendi Anahtar Çiftinizi Nasıl Yönetirsiniz? ####

*Enigmail Anahtar Yönetimi* ile birbirinden farklı anahtar çiftleri oluşturabilir, onları doğrulayabilir ve imzalayabilirsiniz. Bununla birlikte, başka anahtar yönetimi işlemlerini de gerçekleştirebilirsiniz (bkz. yukarıdaki Şekil 29).

- **Kullanıcı Kimliklerini Yönet** bir anahtar çiftine birden fazla e-posta adresi bağlamanızı sağlar.
- **Son Kullanma Süresini Değiştir** anahtar çiftinizin son kullanma süresini değiştirmenizi sağlar.
- **Parolayı Değiştir** anahtar çiftinizi koruyan parolayı değiştirmenizi sağlar. 
- **İptal Etme Sertifikası Oluştur ve Sakla**

<a name="4.5"></a>
## 4.5 Bir Mesaj Nasıl Şifrelenir ve Bir Mesajın Şifresi Nasıl Çözülür? ##

**Önemli**: E-posta mesajlarının başlığı – *Konu* kısmı, gönderilen kimselerle ilgili bilgi ve **To**, **CC** ve **BCC** alanlarındaki bilgiler - *şifrelenemez* ve açık metin olarak gönderilir. E-posta iletişimlerinizin gizliliğini ve güvenliğini sağlamak için e-postanızın konu kısmına hassas bilgiler ve e-postanın içeriğini belli edecek tanımlar eklenmemelidir. Ek olarak, bir grup insana e-posta gönderirken tüm adresleri BCC alanına koymanız tavsiye edilir. 

Ek dosyaları bulunan e-posta mesajlarını şifrelerken, **PGP/MIME** seçeneğini kullanmanızı şiddetle tavsiye ederiz. Bu seçenek, e-postanıza eklenmiş olan tüm dosya ve dosya isimlerini de kapsayacak bir şifrelemeyi mümkün kılar. 

Thunderbird/Enigmail/GnuPG kullanarak gönderdiğiniz tüm şifreli e-postalar otomatik olarak sizin ve bu e-postanın alıcılarının anahtarları üzerinden şifrelenir ve bu sayede e-postalarınızın şifresini gidenler dosyasında çözebilirsiniz. 

### 4.5.1 Bir Mesajı Nasıl Şifreleyebilirsiniz ###

Hem siz hem de iletişimde olduğunuz kişi birbirinizin açık anahtarlarını başarılı bir şekilde içeri aktarıp doğruladıktan ve imzaladıktan sonra, şifreli mesajlar göndermeye ve gelen mesajların şifrelerini çözmeye hazır durumdasınız demektir. 

Gönderdiğiniz e-posta mesajının içeriğini şifrelemek için aşağıdaki adımları takip edin:

**1. Adım**. **Thunderbird’ü açın** ve e-posta oluşturmak için ![](/sbox/screen/thunderbird-tr/81.png)’yi **tıklayın**. 

**2. Adım**. Mesajı şifreli hale getirmek için *Enigmail > Mesaj şifrelenmeyecek* seçeneğine **tıklayın** ve aşağıdaki ekranda göründüğü gibi ![](/sbox/screen/thunderbird-tr/81.png)’yi **seçin**:

![](/sbox/screen/thunderbird-tr/84.png) 

*Şekil 33: Şifrelemeyi Zorla seçeneği*

**3. Adım**. Mesaji imzalamak için *Enigmail > Mesaj imzalanmayacak* seçeneğine **tıklayın** ve *Zorla İmzala’yı* **seçin**. 

**Not**: Mesajınızın şifrelenmiş ve imzalanmış olduğunu doğrulamak için, Enigmail araç çubuğunda iki ikonun aşağıda göründüğü gibi **seçili** olduğundan emin olun:

![](/sbox/screen/thunderbird-tr/85.png) 

*Şekil 34: Şifreleme ve İmzalama etkinleştirilmiş*

**4. Adım**. Mesaj göndermek için ![](/sbox/screen/thunderbird-tr/83.png)’i **tıklayın**. Mesajı imzalarken kişisel anahtarınızı kullanmak için parolanızı girmeniz istenebilir. 

**İsteğe Bağlı 5. Adım**. Eğer mesajınıza bir dosya ekliyorsanız, *Tüm Mesajı Şifrele/İmzala PGP/MIME kullanarak yolla* seçeneğini **seçin** ve daha sonra Tamam’ı tıklayın: 

 ![](/sbox/screen/thunderbird-tr/86.png) 

*Şekil 35: Enigmail Bilgi ekranı*

**Not**: *Her ek dosyayı ayrı olarak şifrelerseniz* (yukarıdaki Şekil 35’teki ikinci seçenek), eklenen dosyaların isimleri şifrelenmez ve oldukları gibi görünürler! Bu hassas bilgilerin yayılmasına neden olabilir! PGP/MIME kullanmak, e-posta metninin, tüm ek dosyaların ve isimlerinin şifrelenmiş ve gizli tutulması için çok önemlidir. 

### 4.5.22 Bir Mesajın Şifresi Nasıl Çözülür? ###

Şifrelenmiş bir mesaj aldığınız ve açtığınız zaman, **Enigmail/OpenPGP** otomatik olarak bu mesajın şifresini çözmeye çalışacaktır. Eger bu işlem başlamazsa **Şifre Çöz** tuşuna basın ve aşağıdaki ekranın etkinleştiğini görün: 

![](/sbox/screen/thunderbird-tr/96.png)

*Şekil 36: Enigmail Bilgi – Lütfen OpenPGP parolanızı veya SmartCard PIN’inizi girin*

**1. Adım**. Yukarıda göründüğü gibi parolanızı **girin**.

Kişisel anahtar parolanızı girdikten sonra, mesajın şifresi çözülür ve aşağıdaki gibi görünür:

![](/sbox/screen/thunderbird-tr/97.png)

*Şekil 37: Mesaj bölmesinde henüz şifresi çözülmüş mesaj*

Mesajın şifresini başarı ile çözdünüz. **4.5 Şifrelenmiş E-Posta Mesajları Nasıl Gönderebilirsiniz ve E-posta Mesajlarının Şifresini Nasıl Çözebilirsiniz?** Bölümünde belirtilen adımları her mesaj değiş tokuşunda takip ederek, e-posta değiş tokuşlarınızın gözlenmesini engelleyerek, gizli ve kimlik denetimi yapılmış bir iletişim kanalı oluşturabilir ve bu kanalı kalıcı hale getirebilirsiniz. 

### 4.5.3 Güvenlik Seçeneklerini Genişletmek###

Gizliliğinizi korumak için *Enigmail ve GnuPG* kullanırken, gönderdiğiniz **her** e-postanın şifreli olması çok önemlidir. Bu durum, özellikle, gelen şifreli e-postalara yazılan cevaplar, daha sonra şifreleyeceğiniz e-posta taslakları ve şifrelenmiş e-postalardan yapılan alıntılar için geçerlidir. 

**Her zaman, mesaj şifrelemeyi mesajı yazmaya başlamadan önce etkinleştirin (4.5.1 Bir Mesajı Nasıl Şifreleyebilirsiniz? bölümünde anlatıldığı şekilde)**. Bu şekilde, mesajlarınızın taslaklarının da e-posta dağıtıcısına şifrelenmiş bir şekilde girildiğinden emin olursunuz. 

Ek olarak, **Enigmail’i şifrelenmemiş bir mesajı göndermeden önce sizi uyaracak şekilde yapılandırmanızı** şiddetle tavsiye ederiz. Aşağıdaki adımlar bunu nasıl yapacağınızı gösteriyor: 

**1. Adım**. *Enigmail > Tercihler* menüsüne **tıklayın** ve *Gönderme* sekmesini **seçin**. 

**2. Adım**. *Şifrelenmemiş ise* - *Göndermeden önce onayla’yı* **seçin** ve Tamam’ı tıklayın. 

![](/sbox/screen/thunderbird-tr/99.png)

*Şekil 38: Enigmail Tercihler – Göndermeden önce onayla*

Şifrelenmemiş her e-postayı göndermeden önce, şifrelenmemiş bir e-posta gönderiyor olduğunuza dair aşağıda görüldüğü şekilde uyarılacaksınız. E-postayı şifrelemek istiyorsanız, *İptal et’i* **tıklayın** ve yukarıdaki 4.5.1 bölümündeki adımları takip edin. 
 
![](/sbox/screen/thunderbird-tr/98.png)

*Şekil 39: Enigmail Onay*

*Konu, Kime, CC* ve *BCC* kısımlarındaki bilgilerin **hiçbir zaman** şifrelenmediğini **unutmayın**.


