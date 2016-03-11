

---

lang: tr
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Export and Import Keys

---

Bu sayfadaki bölümlerin listesi:

- [**3.1 Açık Anahtarınızı gpg4usb Kullanarak Nasıl Gönderirsiniz**](#3.1)
- [**3.2 İletişimde Olduğunuz Kişinin Açık Anahtarını gpg4usb Kullanarak Nasıl İçe Aktarırsınız**](#3.2)
- [**3.3 Bir Açık Anahtarı gpg4usb Kullanarak Nasıl Doğrularsınız**](#3.3)

<a name="3.1"></a>
## Açık Anahtarınızı gpg4usb Kullanarak Nasıl Gönderirsiniz ##

İletişim kurduğunuz kişilerin size şifreli mesaj gönderebilmesi için onlara açık anahtarınızı göndermeniz gerekir. 

Açık anahtarınızı **gpg4usb** kullanarak göndermek için aşağıdaki adımları takip ediniz:

**1. Adım**. **gpg4usb** klasörünü açmak için ![](/sbox/screen/gpg4usb-en-1/02.png)’ye **çift tıklayın**. 

**2. Adım**. **gpg4usb** programını açmak için ![](/sbox/screen/gpg4usb-en-1/03.png)’ye **çift tıklayın**. 

**3. Adım**. Aşağıdaki ekranı etkinleştirmek için ![](/sbox/screen/gpg4usb-en-1/10a.png)’e **tıklayın**.

![](/sbox/screen/gpg4usb-en-1/10.png)

*Şekil 1: Tüm anahtar çiftlerini gösteren Anahtar düzenleme penceresi*

**3. Adım**. Yukarıdaki **Şekil 1’de** göründüğü gibi kendi anahtarınızı işaretleyin.

**4. Adım**. Aşağıda göründüğü gibi **Key**(Anahtar) menüsünden *Export To File'ı* (Dosyaya Aktar)'ı **seçin**:

![](/sbox/screen/gpg4usb-en-1/11.png)

*Şekil 2: Dosyaya Aktar seçeneği seçili Anahtar düzenleme penceresi*

Bu sayede aşağıdaki ekran etkinleşecektir: 

![](/sbox/screen/gpg4usb-en-1/12.png)

*Şekil 3: Dosyaya Aktar tarayıcı penceresi*

**5. Adım**. Anahtar çiftinizi **gpg4usb** program klasörüne kaydetmek için ![](/sbox/screen/gpg4usb-en-1/13.png) ’i **tıklayın**. 

**6. Adım**. Açık anahtarınızı içeren dosyayı istediğiniz kişiye ek dosya olarak **gönderin**.

<a name="3.2"></a>
## 3.2 İletişimde Olduğunuz Kişinin Açık Anahtarını gpg4usb Kullanarak Nasıl İçe Aktarırsınız? ##

Bilgileri şifreleyip iletişimde olduğunuz kişiye göndermeden önce, onun açık anahtarını elinizde bulundurmalısınız. İletişimde olduğunuz kişinin açık anahtarını **gpg4usb** kullanarak içe aktarmak için aşağıdaki adımları takip edin:

**1. Adım**. **gpg4usb** programını açmak için ![](/sbox/screen/gpg4usb-en-1/03.png)’e **çift tıklayın**.

**2. Adım**. Aşağıdaki ekranı etkinleştirmek için ![](/sbox/screen/gpg4usb-en-1/14.png)’i **tıklayın**:

![](/sbox/screen/gpg4usb-en-1/15.png)

*Şekil 4: Anahtarı İçe Aktar iletişim kutusu*

**3. Adım**. Almak istediğiniz anahtarı **bulun** ve **seçin**. 

![](/sbox/screen/gpg4usb-en-1/16a.png)

*Şekil 5: Açık Anahtar*

**4. Adım**. Aşağıdaki ekranı etkinleştirmek için *Open'ı* (Aç’ı) **tıklayın**.

![](/sbox/screen/gpg4usb-en-1/16b.png)

*Şekil 6: Anahtar İçe Aktarma Detayları*

**5. Adım**. Yukarıdaki pencereyi kapatmak için *OK'i* (Tamam’ı) **tıklayın** ve **gpg4usb** ana penceresine geri dönün. Yeni içe aktarılmış anahtar aşağıdaki gibi görünecektir. 

![](/sbox/screen/gpg4usb-en-1/16.png)

*Şekil 7: Yeni içe aktarılmış iletişim kuracağınız kişinin hesabına bağlı olan açık anahtarı gösteren gpg4usb konsolu*

İletişim kuracağınız kişinin açık anahtarını başarı ile içe aktardınız. Şimdi bu anahtarı doğrulayabilir ve imzalayabilirsiniz.

<a name="3.3"></a>
## 3.3 Bir Açık Anahtarı gpg4usb Kullanarak Nasıl Doğrularsınız? ##

Alınan anahtarın gerçekten onu gönderen kişiye ait olup olmadığını doğrulamanız gerekir. İçe aktardığınız her açık anahtar için siz ve iletişimde olduğunuz kişiler bu önemli işlemi tekrarlamalısınız. 

Anahtar çiftini doğrulamak için aşağıdaki adımları takip edin::

**1. Adım**. İletişim kuracağınız kişi ile e-posta haricinde başka bir kanaldan **temas kurun**.

**Not**: Telefon, yazılı mesaj, **Voice over Internet Protocol** (**VoIP**) veya başka bir yöntem kullanabilirsiniz, fakat bunları iletişim kuracağınız kişinin gerçekten o olduğundan emin iseniz yapın. Güvenli bir şekilde ayarlandıkları zaman, telefon görüşmeleri ve yüz yüze buluşmalar kişinin kimliğini doğrulamanız için en güvenli yöntemlerdir. 

**2. Adım**. Siz ve iletişim kurduğunuz kişi değiştiğiniz açık anahtarların ‘parmak izlerini’ doğrulamalısınız.

**Not**: Parmak izi, her anahtarın sahip olduğu kendine özgü sayı ve harflerdir. Parmak izinin kendisi gizli değildir, daha sonra, gerektiği zaman doğrulama işlemi için kullanılmak üzere kaydedilebilir. 

Yarattığınız veya aldığınız açık anahtarların parmak izlerini görmek için aşağıdaki adımları takip edin: 

**1. Adım**. Bir anahtar **seçin**, aşağı açılır menüsünü etkinleştirmek için üzerine **sağ tıklayın**.

**2. Adım**. *Show Keydetails* (Anahtar detaylarını Göster) maddesini aşağıdaki *Şekil 8’de* göründüğü gibi **seçin**.

![](/sbox/screen/gpg4usb-en-1/17.png)

*Şekil 8: İletişim kuracağınız kişinin anahtarı ile ilişkili açılır menü*

Bu şekilde aşağıdaki ekran etkinleşecektir:

![](/sbox/screen/gpg4usb-en-1/18.png)

*Şekil 9: Aşağı bölümünde anahtar parmak izini gösteren Anahtar detayları penceresi*

**3. Adım**. Bu parmak izini, iletişim kuracağınız kişinin kendi **gpg4usb** programında gördüğü ile **karşılaştırın**.

İletişim kuracağınız kişi de bu işlemleri gerçekleştirmelidir. Karşılıklı olarak gönderilen anahtarın gönderen kişinin orijinal anahtarı ile aynı olup olmadığından emin olun. Eğer aynı değillerse yeniden açık anahtar paylaşımı yapın (farklı bir e-posta adresi veya iletişim yöntemi ile) ve doğrulama işlemlerini tekrarlayın. 

Parmak izleri *tam* olarak örtüşüyorsa birbirinize güvenli ve şifreli mesaj ve dosyalar gönderebilir hale geldiniz demektir. 


