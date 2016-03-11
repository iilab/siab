

---

lang: tr
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 4
depth: 3
title: Portable Thunderbird with GPG and Enigmail

---

## 5.1 Thunderbird’ün Kurulumlu ve Taşınabilir Versiyonları Arasındaki Farklar ##

**Taşınabilir Thunderbird’ü** kullanmanın en önemli faydası e-postalarınızın yerel kopyalarınızı çıkarılabilir sürücü ya da USB bellek çubuğuna kaydedebilmenizdir. Buna ek olarak, hem Taşınabilir Thunderbird programı hem de e-postalarınızin bütün yerel kopyaları **TrueCrypt** tarafından şifrelenmiş disk bölümü içinde saklanabilir. Bu sayede, e-postalarınızın güvenliğini geliştirir ve e-posta hesaplarınızı ve kullandığınız adresleri saklayabilirsiniz. Fakat unutmayın ki harici aygıtınız ya da USB bellek çubuğunuz ve de taşınabilir araçlarınız sadece kullandığınız bilgisayar kadar güvenlidir, ve reklam destekli yazılımlar, kötü niyetli yazılımlar, casus yazılımlar ve virüslere maruz kalma riskini taşıyabilirler.

**Not**: E-posta iletişiminizin gizlilik ve güvenliğini korumak için, bu sayfanın sonunda açıklandığı gibi **GnuPG Portable’ı** indirip çıkartmanızı şiddetle tavsiye ediyoruz.

## 5.2 Taşınabilir Thunderbird Nasıl İndirilip Çıkartılır? ##
**1. Adım**. [**http://portableapps.com/apps/internet/Thunderbird_portable**](http://portableapps.com/apps/internet/Thunderbird_portable)'ı **tıklayarak** ilgili indirme sitesini açın.

**2. Adım**. ![](/sbox/screen/thunderbirdportable-en-1/01.png)’ı **tıklayarak** **Source Forge** indirme sitesini etkinleştirin.

**3. Adım**.  ![](/sbox/screen/thunderbirdportable-en-1/02.png)’ı **tıklayarak** ![](/sbox/screen/thunderbirdportable-en-1/03.png) kurulum dosyasını bilgisayarınıza kaydedin ve onu içine indirdiğiniz dosyayı **bulun**.

**4. Adım**. ![](/sbox/screen/thunderbirdportable-en-1/03.png)’yi **çift tıklayın**; *Dosyayı Aç - Güvenlik Uyarısı* kutusu açılabilir. Açılırsa ![](/sbox/screen/thunderbirdportable-en-1/04.png)’ı **tıklayarak** aşağıdaki ekranı etkinleştirin:

![](/sbox/screen/thunderbirdportable-en-1/05.png)

*Şekil 1: Mozilla Thunderbird Taşınabilir Sürüm | Portableapps.com Kurucu penceresi*

**5. Adım**. ![](/sbox/screen/thunderbirdportable-en-1/06.png)’i **tıklayarak** aşağıdaki ekranı etkinleştirin:

![](/sbox/screen/thunderbirdportable-en-1/07.png)

*Şekil 2. Kurulum Yerini Seçiniz penceresi*

**6. Adım**.  ![](/sbox/screen/thunderbirdportable-en-1/08.png)’ı **tıklayarak** aşağıdaki gibi *Dosya Tarama* penceresini etkinleştirin:

![](/sbox/screen/thunderbirdportable-en-1/09.png)

*Şekil 3: Dosya Tarama penceresi*

**7. Adım**. Yukarıdaki *Şekil 3’te* görüldüğü gibi harici sürücünüz ya da USB bellek çubuğunuzdaki hedef dosyaya **ilerleyin**, daha sonra ![](/sbox/screen/thunderbirdportable-en-1/10.png)’i **tıklayarak** **Mozilla Thunderbird, Taşınabilir Sürüm’ün** yerini onaylayın ve *Kurulum Yerini Seçiniz* penceresine geri dönün. 

**8. Adım**. ![](/sbox/screen/thunderbirdportable-en-1/11.png)’ı **tıklayarak** *Kurulum* penceresini etkinleştirin ve **Mozilla Thunderbird, Taşınabilir Sürüm** dosyasının çıkartılmasını bekleyin, ve sonrasında ![](/sbox/screen/thunderbirdportable-en-1/12.png)’yı **tıklayarak** çıkarım işlemini bitirin.

**9. Adım**. **Mozilla Thunderbird, Taşınabilir Sürüm** dosyasının kaydedildiği kaldırılabilir sürücü ya da USB bellek çubuğuna doğru **ilerlerin**.

**10. Adım**. Kaldırılabilir aracınıza ya da USB bellek çubuğunuza **çift tıklayın**, şöyle bir görüntü karşınıza çıkmalı:

![](/sbox/screen/thunderbirdportable-en-1/13.png)

*Şekil 4. Mozillla Thunderbird Taşınabilir Sürümü gösteren Thunderbird Taşınabilir dizini*

## 5.3 Thunderbird için Taşınabilir GPG Nasıl İndirilir ve Çıkartılır? ##

**1. Adım**. [**http://portableapps.com/support/thunderbird_portable#encryption**](http://portableapps.com/support/thunderbird_portable#encryption) **tıklayarak** indirme sitesine yönlendirilin.

**2. Adım**. ![](/sbox/screen/thunderbirdportable-en-1/17.png)’yı **tıklayarak**, *GPG_for_Thunderbird_Portable_1.4.16.paf.exe‘yi* indirme penceresini etkinleştirin ve sonra  ![](/sbox/screen/thunderbirdportable-en-1/02.png)’i **tıklayarak** ![](/sbox/screen/thunderbirdportable-en-1/18.png) kurulum dosyasını kaydedin ve dosyayı kaydettiğiniz yere **ilerleyin**.

**3. Adım**. ![](/sbox/screen/thunderbirdportable-en-1/18.png)’yi **çift tıklayın**; *Dosyayı Aç – Güvenlik Uyarısı* kutusu açılabilir. Açılırsa  ![](/sbox/screen/thunderbirdportable-en-1/04.png)’ı **tıklayarak** aşağıdaki ekranı etkinleştirin:

![](/sbox/screen/thunderbirdportable-en-1/19.png)

*Şekil 5: Kurulum Dili Penceresi*

**4. Adım**. ![](/sbox/screen/thunderbirdportable-en-1/10.png)’yi tıklayarak Thunderbird için **GPG | Taşınabilir Uygulamalar Kurucusu** penceresini etkinleştirin, ve sonrasında ![](/sbox/screen/thunderbirdportable-en-1/06.png)’i **tıklayarak** aşağıdaki ekranı etkinleştirin:

![](/sbox/screen/thunderbirdportable-en-1/20.png)

*Şekil 6: Kurulum Yerini Seçiniz penceresi*

**5. Adım**. ![](/sbox/screen/thunderbirdportable-en-1/08.png)'ı **tıklayarak** aşağıdaki gibi *Dosyayı Tara* penceresini etkinleştirin:

![](/sbox/screen/thunderbirdportable-en-1/21.png)

*Şekil 7: Dosyayı Tara penceresi*

**6. Adım**. **Taşınabilir Thunderbird’ü** yüklediğiniz dizine **ilerleyin**, ![](/sbox/screen/thunderbirdportable-en-1/10.png)’i **tıklayarak** *Kurulum Yerini Seçiniz* penceresine (*Şekil 7*) geri dönün ve sonra ![](/sbox/screen/thunderbirdportable-en-1/11.png)’ı **tıklayarak** **Taşınabilir GnuPG’yi** çıkarmaya başlayın ve bu işlem bittiğinde ![](/sbox/screen/thunderbirdportable-en-1/12.png)’i **tıklayın**.

## 5.4 Enigmail Nasıl İndirilir ve Kurulur? ##

**Enigmail** e-posta iletişiminizin gizliliğini korumanızı sağlayan bir **Mozilla Thunderbird** eklentisidir. **Enigmail** basitçe **GnuPG** şifreleme programını **Thunderbird** içinde kullanmanızı sağlayan bir arayüzdür. *Enigmail* arayüzü **Thunderbird** konsol çubuğunda görünür.

**1. Adım**. [**https://www.enigmail.net/download/**](https://www.enigmail.net/download/) **tıklayarak** indirme sitesine yönlendirilin.

**2. Adım**. *İşletim sisteminiz nedir?* (mesela *Windows*) ve *Hangi e-posta istemcisini kullanıyorsunuz?* (mesela *Thunderbird 31*) sorularını cevaplandırın ve *enigmail-1.7.2-tb-win.xpi‘yi* indirme penceresini etkinleştirmek için *Enigmail x.x.x‘i (mesela 1.7.2) İndir* linkini **tıklayın** ve sonrasında ![](/sbox/screen/thunderbirdportable-en-1/25.png)’i **tıklayarak** (/sbox/screen/thunderbirdportable-en-1/26.png)’i bilgisayarınıza kaydedin.

**3. Adım**. **Thunderbird Taşınabilir** dizinini **açın** ve ![](/sbox/screen/thunderbirdportable-en-1/14.png)’yi **çift tıklayarak** **Thunderbird Taşınabilir’i** açın.

**4. Adım**. ![](/sbox/screen/thunderbirdportable-en-1/27.png)’ü **tıklayarak** *Thunderbird Menü’sünü* görüntüleyin ve aşağıda görüldüğü gibi *Thunderbird Taşınabilir* ana konsolunda **Eklentileri seçin**:

![](/sbox/screen/thunderbirdportable-en-1/28.png)

*Şekil 8: Eklentiler öğesi seçilmiş Thunderbird Taşınabilir ana konsolu*

Bu aşağıdaki ekranı etkinleştirecektir:

![](/sbox/screen/thunderbirdportable-en-1/29.png)

*Şekil 9: Thunderbird Taşınabilir Eklentiler penceresi*

**5. Adım**. Ana *Eklentiler* bölmesinde Enigmail Eklentisi beliriyorsa ![](/sbox/screen/thunderbirdportable-en-1/30.png)’ı **tıklayın**. Belirmiyorsa ![](/sbox/screen/thunderbirdportable-en-1/31.png)’ı yıklayın ve *Eklentiyi Dosyadan Kur’u* aşağıda görüldüğü gibi **seçin**.

![](/sbox/screen/thunderbirdportable-en-1/32.png)

*Şekil 10: Eklentiler için Araçlar menüsü*

**6. Adım**. **Enigmail** eklentisini kaydettiğiniz dizine (büyük ihtimalle *İndirilenler* Dizinine) **ilerleyin** ve **Enigmail** eklenti dosyasını **seçin**.

**7. Adım**. *Yazılım Kurulumları* dizininde  ![](/sbox/screen/thunderbirdportable-en-1/33.png)’ı **tıklayın**.

**8. Adım**. ![](/sbox/screen/thunderbirdportable-en-1/34.png)’ı **tıklayarak** **Enigmail** kurulumunu tamamlayın ve **Thunderbird Taşınabilir’i** **tekrar başlatın**.

Bütün bu adımları tamamladıktan sonra, lütfen [**Thunderbird**](/tr/thunderbird_main) bölümüne bakarak e-posta hesaplarınızı kaydetmek ve programı yapılandırmakla devam edin.

