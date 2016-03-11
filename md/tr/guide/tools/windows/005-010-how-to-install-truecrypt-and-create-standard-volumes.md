

---

lang: tr
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: How to Install TrueCrypt and Create Standard Volumes

---

Bu sayfadaki kısımların listesi:

- [**2.0 TrueCrypt Nasıl Kurulur**](#2.0)
- [**2.1 TrueCrypt Arayüzü Nasıl Türkçe'ye Çevrilir**](#2.1)
- [**2.2 TrueCrypt Hakkında**](#2.2)
- [**2.3 Standart Bir Birim Nasıl Oluşturulur**](#2.3)
- [**2.4 Standart Bir Birim USB Hafıza Çubuğunda Nasıl Oluşturulur**](#2.4)
- [**2.5 Standart Birim Nasıl Oluşturulur (Devamı)**](#2.5)

<a name="2.0"></a>
## 2.0 TrueCrypt Nasıl Kurulur ##

**1. Adım**. ![](/sbox/screen/truecrypt-tr/01.png)’ye çift tıklayın, *Dosya Aç – Güvenlik Uyarısı* kutusu açılabilir. Açılırsa, **TrueCrypt** *Lisans* ekranını etkinleştirmek için  ![](/sbox/screen/truecrypt-tr/02.png)’i **tıklayın**. 

**2. Adım**. Sonraki düğmesini etkinleştirmek için *I accept and agree to be bound by the license terms* (Lisansın maddelerini kabul ediyorum) kutusunu **işaretleyin** ve aşağıda görünen ekranı etkinleştirmek için ![](/sbox/screen/truecrypt-tr/03.png)’yi **tıklayın**.

![](/sbox/screen/truecrypt-tr/04.png)

*Şekil 1: Verili kurulum modunda Sihirbaz Modu Penceresi*

- *Install Mode (Kurulum modu)*: Bu seçenek, bilgisayarında **TrueCrypt** kullandıklarını saklama ihtiyacı hissetmeyen kullanıcılar içindir. 

- *Extract Mode (Çıkarma modu)*: Bu seçenek, **TrueCrypt’i** bilgisayarlarına yüklemek istemeyen ve USB hafıza çubuğunda taşınabilir bir **TrueCrypt** sürümü kullanmak isteyen kullanıcılar içindir.

**Not**: Çıkarma modu kullanıldığı zaman, tüm bölmeler veya sürücü şifreleme gibi bazı seçenekler çalışmayacaktır. 

**Not**: Burada verili olan *Kurulum* modu önerilse de, daha sonra **TrueCrypt** taşınabilir modu da kullanabilirsiniz. **TrueCrypt Traveller** modu için lütfen [**Taşınabilir TrueCrypt**](http://securityinabox.org/tr/truecrypt_portable) sayfasına bakınız. 

**3. Adım**. Aşağıda görünen ekranı etkinleştirmek için![](/sbox/screen/truecrypt-tr/05.png)’yi **tıklayın**:

![](/sbox/screen/truecrypt-tr/06.png)

*Şekil 2: Kurulum Seçenekleri penceresi*

**4. Adım**. *Kurulum* ekranını etkinleştirmek ve sisteminize **TrueCrypt'i** kurmaya başlamak için ![](/sbox/screen/truecrypt-tr/07.png)’ı **tıklayın**. 

**5. Adım**. Aşağıdaki ekranı etkinleştirmek için önce  ![](/sbox/screen/truecrypt-tr/08.png)’i, daha sonra da ![](/sbox/screen/truecrypt-tr/11.png)’i **tıklayın**. 

![](/sbox/screen/truecrypt-tr/09.png)

*Şekil 3: TrueCrypt Kurulum onayı iletişim kutusu*

**6. Adım**. **TrueCrypt** kurulumunu bitirmek için ![](/sbox/screen/truecrypt-tr/10a.png)’i **tıklayın**.

**Not**: Tüm kullanıcılara bu kılavuzu bitirdikten sonra [**TrueCrypt** yardım belgelerine](http://andryou.com/truecrypt/docs/index.php) bakmalarını öneririz.

<a name="2.1"></a>
## 2.1 TrueCrypt Arayüzü Nasıl Türkçe'ye Çevrilir ##

Her ne kadar mükemmel olmasa da **TrueCrypt** arayüzü Türkçe'ye çevrilmiştir. Aşağıdaki adımları takip ederek, TrueCrypt arayüzünü Türkçe görebilirsiniz:

**1. Adım**. [**https://truecrypt.ch/downloads/**](https://truecrypt.ch/downloads/) sayfasına **gidin** ve sayfayı tr-Turkish-Türkçe satırını görene kadar aşağı kaydırın. Bunun hizasındaki ![](/sbox/screen/truecrypt-tr/tr-01.png)'i **tıklayın**. Aşağıdaki ekran belirecektir

![](/sbox/screen/truecrypt-tr/tr-02.png)

*Şekil 4: Langpack-tr-0.1.0-for truecrypt-7.1.a.zip açılıyor ekranı*

**2. Adım**. *Dosyayı Kaydet'i* **seçip** ![](/sbox/screen/truecrypt-tr/tr-03.png)'ı **tıklayın**.

**3. Adım**.İndirdiğiniz dosyayı **bulun** (mesela Karşıdan İndirilenler klasöründe), üzerine sağ **tıklayın** ve *Ayıkla* yı **seçerek** aşağıdaki ekranı açın:

![](/sbox/screen/truecrypt-tr/tr-05.png)

*Şekil 5: Sıkıştırılmış Klasörleri Ayıkla Ekranı*

**4. Adım**. ![](/sbox/screen/truecrypt-tr/tr-06.png)'ı **tıklayarak** *Hedef Seç* ekranını etkinleştirin. Aşağıda göründüğü gibi **TrueCrypt.exe** dosyasının bulunduğu klasöre (mesela C:\Program Files\TrueCrypt\)  **ilerleyin**. 

![](/sbox/screen/truecrypt-tr/tr-07.png)

*Şekil 6: Hedef Seç Ekranı*

**5. Adım**. ![](/sbox/screen/truecrypt-tr/tr-03.png)'ı **tıklayarak** *Sıkıştırılmış Klasörleri Ayıkla Ekranı'na* geri dönün ve ![](/sbox/screen/truecrypt-tr/tr-09.png)'yı **tıklayın**. Güvenlik uyarısı belirirse ![](/sbox/screen/truecrypt-tr/tr-10.png)'ı **tıklayın**.

**6. Adım**. **TrueCrypt** programını **açın**. Aşağıda göründüğü gibi *Settings* (Ayarlar) ve *Language* (Dil) seçeneklerini **tıklayın**.

![](/sbox/screen/truecrypt-tr/tr-12.png)

*Şekil 7: Dil Ayarları Seçili TrueCrypt Ana Konsolu*

**6. Adım**. Beliren pencerede aşağıda göründüğü gibi Türkçe'yi seçin ve ![](/sbox/screen/truecrypt-tr/tr-14.png)'i **tıklayın**.

![](/sbox/screen/truecrypt-tr/tr-13.png)

*Şekil 8: TrueCrypt - Language (Dil) Ekranı*
.
<a name="2.2"></a>
## 2.2 TrueCrypt Hakkında ##

**TrueCrypt** dosyalarınızı, doğru şifreye sahip olmayan kimselerin onlara ulaşamını engelleyerek, güvenli bir şekilde depolamanızı sağlar. Dosyalarınızı saklayan ve sadece doğru şifreye sahip olan kişinin açmasına olanak sağlayan elektronik bir kasa gibi çalışır. **TrueCrypt**, dosyalarınızı bilgisayarınızda güvenli bir şekilde kilitleyebileceğiniz *birimler* veya bölümler oluşturarak çalışır. Bu birimlerde veri oluşturduğunuz veya var olan verileri bu birimlere taşıdığınız zaman, **TrueCrypt** bu bilgileri otomatik olarak şifreleyecektir. Dosyalarınızı açtığınız veya dışarı çıkardığınızda, onları kullanabilmeniz için otomatik olarak şifrelerini çözecektir. Bu işleme *on-the-fly (anında) şifreleme* denir. 

<a name="2.3"></a>
## 2.3 Standart Bir Birim Nasıl Oluşturulur? ##

**TrueCrypt** iki tür birim oluşturmanıza olanak verir: *Gizli* ve *Standart*. Bu bölümde, dosyalarınızı depolayabileceğiniz bir *Standart Birim* oluşturma konusunda bilgi alacaksınız.

**TrueCrypt** kullanarak *Standart Birim* oluşturmak için aşağıdaki adımları takip edin:
**1. Adım**. ![](/sbox/screen/truecrypt-tr/52.png)’e **çift tıklayın** veya **Başlat > Programlar > TrueCrypt > TrueCrypt'i** **seçin**.

**2. Adım**. **TrueCrypt** bölmesinde, aşağıda göründüğü gibi bir sürücü **seçin**:

![](/sbox/screen/truecrypt-tr/12.png)

*Şekil 9: TrueCrypt konsolu*

**3. Adım**. *TrueCrypt Birim Oluşturma Sihirbazı'nı* aşağıda göründüğü gibi etkinleştirmek için  ![](/sbox/screen/truecrypt-tr/13.png)’u **tıklayın**:

![](/sbox/screen/truecrypt-tr/14.png)

*Şekil 10: TrueCrypt Birim Oluşturma Sihirbazı penceresi* 

*Şekil 10’te* göründüğü gibi *Standart Birim* oluşturmak için üç seçenek vardır. Biz bu bölümde, *Create an encrypted file container* (Şifrelenmiş bir dosya kutusu oluştur) seçeneğini kullanacağız. Diğer iki seçenek ile ilgili bilgi için [**TrueCrypt**](http://www.truecrypt.org/docs/) Birim Oluşturma Sihirbazı belgelerine başvurabilirsiniz. 

**4. Adım**. Aşağıdaki ekranı etkinleştirmek için  ![](/sbox/screen/truecrypt-tr/05.png)’yi **tıklayın**:

![](/sbox/screen/truecrypt-tr/15.png)

*Şekil 11: Birim Tipi penceresi*

*TrueCrypt Birim Oluşturma Sihirbazı Birim Tipi* penceresi *Standart* veya *Gizli* **TrueCrypt** birimi oluşturma tercihinizi belirlemenize olanak sağlar. 

**Önemli**: *Gizli Birim Oluşturma* konusunda daha fazla bilgi için [**Gizli Birim**](/tr/truecrypt_hiddenvolumes) sayfasına başvurabilirsiniz. 

**5. Adım**. *Standard TrueCrypt Volume* (Standart TrueCrypt Birimi) seçeneğini **işaretleyin**.

**6. Adım**. Aşağıdaki ekranı etkinleştirmek için ![](/sbox/screen/truecrypt-tr/05.png)’yi **tıklayın**:

![](/sbox/screen/truecrypt-tr/16.png)

*Şekil 12: Birim Oluşturma Sihirbazı – Birim Yeri bölmesi*

*Volume Creation Wizard - Volume Location* (Birim Oluşturma Sihirbazı - Standart Birim) ekranında *Standart Biriminizi* nerede saklamak istediğinizi belirleyebilirsiniz. Bu dosya herhangi başka bir dosya gibi saklanabilir.

**7. Adım**. Dosyanın ismini metin kutusuna **yazın** veya aşağıdaki ekranı etkinleştirmek için ![](/sbox/screen/truecrypt-tr/17.png)’i **tıklayın**:

![](/sbox/screen/truecrypt-tr/18.png)

*Şekil 13: Yol ve Dosya Adını Belirtin penceresi*

**Not**: **TrueCrypt** Birimi normal bir dosyanın içine saklanır. Bu demektir ki, kopyalanabilir, yeri değiştirilebilir ve hatta silinebilir! Bu yüzden, dosyanın yerini ve ismini hatırlamanız çok önemlidir. Fakat, oluşturduğunuz birim için yeni bir isim seçmelisiniz ([**USB Hafıza Çubuğunda Standart Bir Birim Nasıl Oluşturulur**](#2.4) kısmına başvurabilirsiniz). Bu kılavuzda, Standart Birimi **Belgelerim** klasöründe oluşturacağız ve ismini *Şekil 8’de* gördüğünüz gibi *Birimim* yapacağız. 

**İpucu**: İstediğiniz herhangi bir dosya ismini veya dosya uzantısını kullanabilirsiniz. Örneğin, Standart Biriminizi *tarifler.doc* olarak adlandırabilir ve böylelikle herhangi bir Word belgesi gibi görünmesini sağlayabilirsiniz veya *tatiller.mpg* olarak adlandırıp bir film dosyası gibi gösterebilirsiniz. 

**8. Adım**.  Yol ve Dosya Adını Belirtin pencerelerini kapatmak ve aşağıda göründüğü gibi *Birim Oluşturmama Sihirbazı* penceresine dönmek için  ![](/sbox/screen/truecrypt-tr/19.png)’i **tıklayın**:

![](/sbox/screen/truecrypt-tr/20.png)

*Şekil 14: Birim Yeri bölmesini gösteren TrueCrypt Birim Oluşturma Sihirbazı*

**9. Adım**. *Şekil 10’u* etkinleştirmek için ![](/sbox/screen/truecrypt-tr/05.png)’yi **tıklayın**.

<a name="2.4"></a>
## 2.4 Standart Bir Birim USB Hafıza Çubuğunda Nasıl Oluşturulur ##

USB hafıza çubuğunda **TrueCrypt** *Standart Birim* oluşturmak için, [**2.2 Standart Bir Birim Nasıl Oluşturulur**](#2.2) kısmındaki 1’den 7’ye kadar olan adımları takip edin ve *Select a TrueCrypt Volume* (TrueCrypt Birimi Seçin) ekranını etkileştirin. Daha sonra, dosya yeri olarak **Belgelerim’i** değil USB hafıza çubuğunuzu **seçin**. Bir dosya adı **verin** ve *Standart Biriminizi* burada oluşturun. 

<a name="2.5"></a>
## 2.5 Standart Bir Birim Nasıl Oluşturulur (Devamı) ##

Bu noktada, *Standart Biriminizde* saklanacak verilerinizi kodlamak için spesifik bir şifreleme yöntemi (ya da bu ekranda adlandırıldığı şekliyle *algoritma*) seçmeye hazırsınız. 

![](/sbox/screen/truecrypt-tr/21.png)

*Şekil 15: Birim Oluşturma Sihirbazı Şifreleme Seçenekleri bölmesi*

**Not**: Verili seçenekleri olduğu gibi kabul edebilirsiniz. Her iki seçenekte verilen algoritmalar oldukça güvenli kabul edilir. 

**10. Adım**. *TrueCrypt Birim Oluşturma Sihirbazı* ekraını aşağıda göründüğü gibi etkinleştirmek için  ![](/sbox/screen/truecrypt-tr/05.png)’yi **tıklayın**:

![](/sbox/screen/truecrypt-tr/22.png)

*Şekil 16: Birim Boyutunu gösteren Birim Oluşturma Sihirbazı bölmesi*

*Volume Size* (Birim Boyutu) bölmesi, *Standart Biriminizin/ boyutunu belirlemenize olanak sağlar. Bu örnekte, 10 megabayt olarak belirlenmiştir. Fakat siz farklı bir boyut seçebilirsiniz. Depolamak istediğiniz belgelerin boyutunu ve dosya tiplerini göz önünde bulundurun ve buna uygun bir boyut seçin.  

**İpucu**: Standart Biriminizi daha sonra bir CD’ye yedeklemek istiyorsanız boyutu 700MB veya daha küçük seçmelisiniz.

**11. Adım**. Metin alanına belirlediğiniz birim boyutunu **girin** ve aşağıdaki ekranı etkinleştirmek için  ![](/sbox/screen/truecrypt-tr/05.png)’yi **tıklayın**:

![](/sbox/screen/truecrypt-tr/23.png)

*Şekil 17: Birim Şifresini gösteren TrueCrypt Birim Oluşturma Sihirbazı bölmesi*

**Önemli**: *Standart Birim* oluştururken yapmanız gereken en önemli işlemlerden biri güvenli ve güçlü bir şifre yaratmaktır. İyi bir şifre şifrelenmiş biriminizi korur, bu yüzden ne kadar güçlü bir şifre seçerseniz o kadar güvende olursunuz. Şifrenizi kendiniz belirlemek ve hatırlamak zorunda değilsiniz. Bunun yerine, **KeePass** gibi bir program kullanabilirsiniz. Şifre yaratma ve depolama konusunda daha fazla bilgi için (**KeePass’e**](/tr/keepass_main) bakın. 

**12. Adım**. Şifrenizi ilgili kutuya ve daha sonra bir kez daha *Confirm* (Onayla) kutusuna **yazın**.

**Önemli**: Her iki şifre aynı olmadığı sürece *Sonraki* düğmesi etkinleşmeyecektir. Şifreniz güvenli değilse bu konuda bir uyarı mesajı alacaksınız. Böyle bir durumda şifrenizi değiştirin!  **TrueCrypt** seçeceğiniz herhangi bir şifre ile çalışacak olsa da, şifreniz güçlü değilse verileriniz güvende olmaz. 

**13. Adım**. Aşağıdaki ekranı etkinleştirmek için  ![](/sbox/screen/truecrypt-tr/05.png)’yi **tıklayın**:

![](/sbox/screen/truecrypt-tr/24.png)

*Şekil 18: Birim Formatı gösteren TrueCrypt Birim Oluşturma Sihirbazı bölmesi*

**TrueCrypt**, *Standart Birim* oluşturmaya hazırdır. İmlecinizi *TrueCrypt Birim Oluşturma Sihirbazı* penceresinde birkaç saniye dolaştırın. İmleci ne kadar uzun süre dolaştırırsanız şifreleme kodlarınız o kadar kuvvetli olacaktır. 

**14. Adım**. Standart biriminizi oluşturmak için ![](/sbox/screen/truecrypt-tr/25.png)’i **tıklayın**.

**TrueCrypt**, daha önce belirlendiği üzere *Belgelerim* klasöründe *Birimim* adlı bir dosya oluşturacaktır. Bu dosya, 10 megabayt büyüklüğünde bir **TrueCrypt** *Standart Birim*  oluşturacak ve dosyalarınızı güvenli bir şekilde burada saklamanıza olanak sağlayacaktır. 

*Standart Birim* başarılı bir şekilde oluşturulduktan sonra, aşağıdaki iletişim kutusu görünür:

![](/sbox/screen/truecrypt-tr/26.png)

*Şekil 19: TrueCrypt birimi başarılı bir şekilde oluşturuldu mesajı ekranı*

**15. Adım**. *Standart Birim* oluşturmayı tamamlamak ve **TrueCrypt** konsoluna geri dönmek için ![](/sbox/screen/truecrypt-tr/27.png)’ı **tıklayın**. 

**16. Adım**. *TrueCrypt Birim Oluşturma Sihirbazını* kapatmak için  ![](/sbox/screen/truecrypt-tr/28.png)'ı **tıklayın**.


