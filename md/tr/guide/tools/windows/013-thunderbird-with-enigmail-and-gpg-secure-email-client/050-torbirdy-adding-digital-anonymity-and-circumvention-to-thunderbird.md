

---

lang: tr
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 5
depth: 3
title: Torbirdy - adding digital anonymity and circumvention to Thunderbird

---

<a name="1.0"></a>
## 6.1 Thunderbird için TorBirdy Nasıl Kurulur? ##

[**TorBirdy’yi** bilgisayarınıza indirdikten](https://addons.mozilla.org/en-us/thunderbird/addon/torbirdy/) sonra, **TorBirdy’yi** kurmaya aşağıdaki adımları takip ederek başlayın:

 **1. Adım**. **Thunderbird’ü açın**, sonra ![](/sbox/screen/thunderbird-TorBirdy-tr/03.png)’ü **tıklayarak** *Thunderbird Menüsü’nü* görün ve **Eklentileri seçerek** *Eklentiler Yöneticisi* penceresini etkinleştirin.

**2. Adım**. Sol yan çubuğundaki ![](/sbox/screen/thunderbird-TorBirdy-tr/04.png)’i **tıklayın**.

**3. Adım**. ![](/sbox/screen/thunderbird-TorBirdy-tr/05.png)’ı **tıklayıp** aşağıda görüldüğü gibi *Eklentiyi Dizinden Yükle’yi* **seçin**:

![](/sbox/screen/thunderbird-TorBirdy-tr/06.png)

*Şekil 1: Bütün Eklentiler için Araçlar menüsü*

**4. Adım**. Aşağıdaki ekranda görüldüğü gibi TorBirdy eklentisini kaydettiğiniz dizine (büyük ihtimalle *İndirilenler* dizini) ilerleyin:

![](/sbox/screen/thunderbird-TorBirdy-tr/07.png)

*Şekil 2: Kululacak Eklentiyi Seç ekranı*

**5. Adım**: ![](/sbox/screen/thunderbird-TorBirdy-tr/08.png)’ı **tıklayarak** aşağıdaki ekranı etkinleştirin:

![](/sbox/screen/thunderbird-TorBirdy-tr/09.png)

*Şekil 3: Yazılım Kurulumu penceresi*

**Önemli**: Bir sonraki adımı uygulamadan önce bütün e-postalarınız gönderilmiş ya da kaydedilmiş olduğundan emin olun!

**6. Adım**. ![](/sbox/screen/thunderbird-TorBirdy-tr/10.png)’u **tıklayın** ve sonra ![](/sbox/screen/thunderbird-TorBirdy-tr/11.png) ’ı **tıklayarak** Thunderbird programını yeniden çalıştırın ve **TorBirdy** eklentisinin kurulumunu tamamlayın.

## 6.2 Thunderbird’de TorBirdy Nasıl Kullanılır? ##

**Thundebird** ile **TorBirdy’yi** kullanabilmek için, önce **Tor Tarayıcı’nın** çalıştığından ve  **Tor ağına** başarıyla bağlandığından emin olmalısınız. **Tor Tarayıcı’yı** henüz kurmadıysanız, lütfen devam etmeden önce  [**Tor Tarayıcı – Dijital Anonimlik ve Atlatma’ya**](/en/tor_main) bakınız.

## 6.2.1 Thunderbird için TorBirdy’yi Etkinleştirin ##

Aşağıdaki adımları takip ederek *Tor Tarayıcı'yı* başlatın ve Thunderbird’ü *Tor* ağı üzerinden çalıştırın
 
**Adım 1**: *Tor Tarayıcı* dizinine **ilerleyin**. ![](/sbox/screen/thunderbird-TorBirdy-tr/18.png)’e **çift tıklayarak** aşağıdaki ekranı etkinleştirin:

![](/sbox/screen/thunderbird-TorBirdy-tr/19.png)

*Şekil 8: Tor Statüsü penceresi*

*Not: Tor Tarayıcı’nı başlatmadan önce açmış olduğunuz bütün Firefox pencelererini kapatmanız önerilir*

Bir müddet sonra, Tor Tarayıcı aşağıdakini gösteren bir tarayıcı penceresi açacaktır:

![](/sbox/screen/thunderbird-TorBirdy-tr/20.png)

*Şekil 9: Tor Tarayıcı; Tor ağına başarıyla bağlanmış*

Şimdi *Tor ağına* *Tor tarayıcısıyla* bağlısınız.

**2. Adım**: Thunderbird’ü **başlatın** ve sorulduğunda parolanızı girin. Aşağıdaki şekilde vurgulandığı gibi TorBirdy statüsü Thunderbird penceresinin sağ kösesinde gösterilecek:

 ![](/sbox/screen/thunderbird-TorBirdy-tr/30.png)  

*Şekil 10: Tor için Etkinleştirilmiş TorBirdy*

## 6.2.2 TorBirdy’nin Tor’u kullanarak bağlandığını teyit edin ##

Aşağıdaki adımları takip ederek TorBirdy ayarlarını deneyin ve teyit edin

**1. Adım**: ![](/sbox/screen/thunderbird-TorBirdy-tr/21.png)’u **tıklayarak** aşağıdaki menüyü etkinleştirin

![](/sbox/screen/thunderbird-TorBirdy-tr/22.png)

*Şekil 11: Torbirdy Seçenekler Menüsü*

**2. Adım**: Aşağıdaki pencereyi açmak için *TorBirdy Seçeneklerini Aç'ı* **seçin**.   *TorBirdy Gelişmiş Seçenekleri* uyarı iletisinde ![](/sbox/screen/thunderbird-TorBirdy-tr/23.png)'ı **tıklayın**

![](/sbox/screen/thunderbird-TorBirdy-tr/25.png)

*Şekil 12: TorBirdy Seçenekler penceresi*

**3. Adım**: ![](/sbox/screen/thunderbird-TorBirdy-tr/24.png)’i **tıklayın**. *Tor* ağı üzerinden başarı ile bağlandıysanız, aşağıdaki iletiyi göreceksiniz (*IP adresleri değişecek):

![](/sbox/screen/thunderbird-TorBirdy-tr/26.png)

*Şekil 13: Tor’u Kullanıyor Musunuz? Penceresi*

**Not**: Tor Tarayıcısı’nı başlatmamışsanız ya da Tor Tarayıcısı yukarıdaki 6.2.1 kısmında gösterildiği gibi Tor Ağı’na bağlanmamışsa, e-posta sunucunuza bağlanamayacak ve muhtemelen Thunderbird’ü başlattığınızda şu iletiyi göreceksiniz:

![](/sbox/screen/thunderbird-TorBirdy-tr/27.png)

*Şekil 14: Bağlantı Reddedildi penceresi*

Not edilmelidir ki, Google Mail gibi bazı e-posta sağlayıcıları *Tor ağı* üstünden e-posta sunucularına bağlantıları geri çevirebilir.

## 6.3 Thunderbird için TorBirdy’yi Etkisizleştirin ##

Thunderbird’ü TorBirdy’siz çalıştırmak isterseniz TorBirdy eklentisini aşağıdaki adımları takip ederek etkisizleştirebilirsiniz:

**1. Adım**: **Thunderbird’ü açın**, ve ![](/sbox/screen/thunderbird-TorBirdy-tr/03.png)’e tıklayarak*Thunderbird Menü’sünü* görüntüleyin. **Eklentileri seçerek** *Eklentiler Yöneticisi* penceresini etkinleştirin

**2. Adım**: Sol yan çubuğundaki ![](/sbox/screen/thunderbird-TorBirdy-tr/04.png)’i **tıklayın**

**3. Adım**: Aşağıdaki ekrandaki ![](/sbox/screen/thunderbird-TorBirdy-tr/29.png)’i **tıklayın**:

![](/sbox/screen/thunderbird-TorBirdy-tr/28.png)

*Şekil 15: TorBirdy Eklentisi’ni Etkisizleştir*

**4. Adım**: ![](/sbox/screen/thunderbird-TorBirdy-tr/11.png)’ı **tıklayarak** Thunderbird’ü yeniden açın ve TorBirdy’yi etkisizleştirmiş olun.


