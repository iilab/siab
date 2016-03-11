

---

lang: tr
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: How to Install gpg4usb and Generate a Key Pair

---

Bu sayfadaki bölümlerin listesi:

- [**2.0 gpg4usb Nasıl Kurulur?**](#2.0)
- [**2.1 gpg4usb Kullanarak Nasıl Anahtar Çifti Oluşturulur?**](#2.1)

<a name="2.0"></a>
## 2.0 gpg4usb Nasıl Kurulur? ##

**gpg4usb** taşınabilir bir alettir ve bilgisayarınıza kurmanız gerekmez. Yazılım sıkıştırılmış dosyada dağıtılır ve doğrudan USB sürücüsüne veya bilgisayarınızdaki bir dosyaya ayıklanır. Başlamak için aşağıdaki adımları takip ediniz:

**1. Adım**. **gpg4usb** sıkıştırılmış arşiv dosyasını bulun ve içeriğinin tümünü taşınabilir USB sürücüsüne veya bilgisayarınızdaki bir  klasöre **ayıklayın**:

![](/sbox/screen/gpg4usb-en-1/01.png)

*Şekil 1: gpg4usb programı hedef klasör yeri*

<a name="2.1"></a>
## 2.1 gpg4usb Kullanarak Anahtar Çifti Nasıl Oluşturulur? ##

E-posta, yazılı ileti, belge ve dosyalarınızı şifreleme ve şifrelerini çözmeye başlamak için, öncelikle iki işlem gerçekleştirmelisiniz. Öncelikle şifreleme anahtar çifti oluşturmalı veya taşımalısınız, sonra da iletişimde olacağınız kişilere açık anahtarınızı göndermeli ve onlarınkini edinmeli ve kendi anahtarlığınıza eklemelisiniz. Açık anahtarların nasıl paylaşıldığını bir sonraki bölümde anlatacağız. **gpg4usb**, programı ilk başlattığınız zaman anahtar çifti oluşturmanıza yardımcı olur. Başlangıç (Getting Started) penceresine her zaman *Yardım* -> *Sihirbazı Aç* (*Help* -> *Open Wizard*) menüsüne her zaman gidebilirsiniz.

**1. Adım**. **gpg4usb** programını ilk defa çalıştırmak için, önce ![](/sbox/screen/gpg4usb-en-1/02.png)’yi **bulup** üstüne **çift tıklayın** ve **gpg4usb** klasörünü açın ve [!](/sbox/screen/gpg4usb-en-1/03.png)’e **çift tıklayın**. bu şekilde *Getting Started* (Başlangıç) penceresini etkinleştireceksiniz. Bir dil seçin ve *Next'i* (İleri’yi) **tıklayın** (Bu programın ne yazık ki Türkçe sürümü henüz yoktur).

**2. Adım**. *Choose your Action* (Eyleminizi Seçin) ekranında, *Create a new keypair'i* (Yeni bir anahtar çifti oluştur’u) **tıklayın**.

![](/sbox/screen/gpg4usb-en-1/04.png)

*Şekil 2: Eyleminizi Seçin*

İlk Başlangıç Sihirbazı ekranında var olan anahtarları buraya taşıma seçeneklerini bulabilirsiniz. Eğer **gpg4usb’yi** güncelliyorsanız, *import settings and/or keys from **gpg4usb'yi*** (**gpg4usb’den** ayarları ve/veya anahtarları aktar'ı) seçebilirsiniz. [Enigmail ile Thunderbird](/tr/thunderbird_main) kullanıyorsanız, *import keys from GnuPG* (GnuPG’den anahtarları taşı) seçeneğini seçebilirsiniz. *Help* -> *Open Wizard* (Yardım -> Sihirbazı Başlat) menüsünden sihirbazı çalıştırarak anahtarlarınızı daha sonra da taşıyabilirsiniz. 

**3. Adım**. *Create a keypair'de* (Anahtar çift oluştur’da) *Create New Key'i* (Yeni Anahtar Oluştur’u) **tıklayın**.

![](/sbox/screen/gpg4usb-en-1/05.png)

*Şekil 3: Yeni Anahtar Oluştur* 

**4. Adım**. İlgili metin alanlarına verileri **girmenizden** sonra pencereniz aşağıdakine benzeyecektir: 

![](/sbox/screen/gpg4usb-en-1/06.png)

*Şekil 4: Doldurulmuş Anahtar Oluşturma formu örneği*

**Önemli:** 

* Kişisel anahtarınızı korumak için güvenli bir şifre oluşturun (lütfen [**3. Güvenli şifreler nasıl oluşturulur ve muhafaza edilir**](/tr/chapter-3) bölümüne bakın).
* Expiration date (Zaman aşımına uğrama) seçeneğini seçip 5 yıldan daha az bir süreye ayarlamanızı öneririz.
* En az 2048 bit büyüklüğünde anahtarlar oluşturmanızı şiddetle tavsiye ederiz. Daha büyük anahtarlar daha güvenlidir ama oluşturması, metinleri şifrelemesi ve şifre çözmesi daha çok zaman alır. 

**Not**: Anahtarınızı oluştururken gerçek isminizi ve gerçek e-posta adresinizi kullanmanız gerekmez. Fakat, iletişim kuracağınız hesabın e-posta adresini kullanmanız, iletişim kuracağınız kişilerin anahtarınızı bu hesap ile bağlantılandırmasını kolaylaştırır.

**6. Adım**. Anahtar çiftini oluşturmak için **OK'i** (Tamam’ı) **tıklayın**.

![](/sbox/screen/gpg4usb-en-1/07.png)

*Şekil 5: Anahtar Oluşturuluyor...*

![](/sbox/screen/gpg4usb-en-1/08.png)

*Şekil 6: Yeni Anahtar Oluşturuldu*

**7. Adım**. **gpg4usb** penceresine geri dönmek için *OK'i* (Tamam’ı) **tıklayın**. Anahtar çifti başarı ile oluşturulduktan sonra, aşağıdakine benzer bir ekran göreceksiniz: 

![](/sbox/screen/gpg4usb-en-1/09.png)

*Şekil 7: Yeni oluşturulmuş anahtar çiftini gösteren gpg4usb penceresi* 

Anahtar çiftinizi oluşturduğunuza göre, açık anahtarınızı diğer insanlarla nasıl paylaşacağınızı ve onların açık anahtarlarını nasıl taşıyacağınızı öğrenebilirsiniz. 


