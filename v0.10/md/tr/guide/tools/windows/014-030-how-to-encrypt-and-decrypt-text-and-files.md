

---

lang: tr
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: How to Encrypt and Decrypt Text and Files

---

Bu sayfadaki bölümlerin listesi:

- [**4.0 Yazılı İletiler gpg4usb Kullanarak Nasıl Şifrelenir**](#4.0)
- [**4.1 Yazılı İletilerin Şifresi gpg4usb Kullanarak Nasıl Çözülür**](#4.1)
- [**4.2 Dosyalar gpg4usb Kullanarak Nasıl Şifrelenir**](#4.2)
- [**4.3 Dosyaların Şifresi gpg4usb Kullanarak Nasıl Çözülür**](#4.3)

<a name="4.0"></a>
## 4.0 Yazılı Mesajlar gpg4usb Kullanarak Nasıl Şifrelenir ##

Aşağıdaki örnekte Terence arkadaşı Salima’ya, aşağıdaki adımları takip ederek bir şifreli e-posta gönderecek:

**1. Adım**. **gpg4usb** konsolunu açmak için ![](/sbox/screen/gpg4usb-en-1/03.png)’ye **çift tıklayın**.

**2. Adım**. Mesajınızı aşağıdaki örnekte göründüğü gibi **yazın**: 

![](/sbox/screen/gpg4usb-en-1/19.png)

*Şekil 1: Bir mesaj örneği gösteren gpg4usb konsolu*

**3. Adım**. E-postayı göndereceğiniz kişi ile ilişkili kutuyu aşağıdaki gibi **seçin**:

![](/sbox/screen/gpg4usb-en-1/20.png)

*Şekil 2: E-posta gönderilecek kişiyi gösteren gpg4usb konsolu*

**Not**: Bir iletiyi, *Encrypt for* (Bunlar için Şifrele) bölmesinde bulunan ilgili kutuları tıklayarak birden fazla alıcı için şifreleyebilirsiniz. Kişisel kayıtlarınız için, iletiyi kendiniz için de şifrelemeyi faydalı bulabilirsiniz, çünk, böylece iletiyi daha sonra kendiniz de okuyabilirsiniz.

**4. Adım**. ![](/sbox/screen/gpg4usb-en-1/21.png)'i tıklayarak yada **Crypt** (Şifreleme) menüsünden **select Encrypt'i** (Şifrelemeyi Seç'ı) **tıklayarak** iletinizi aşağıdaki gibi şifreleyebilirsiniz:

![](/sbox/screen/gpg4usb-en-1/22.png)

*Şekil 3: Şifrelenmiş bir ileti örneğini gösteren gpg4usb konsolu*

**5. Adım**. ![](/sbox/screen/gpg4usb-en-1/23.png)'ı **tıklayarak** şifreli iletinin tümüyle seçin, ve  ![](/sbox/screen/gpg4usb-en-1/24.png)'yi tıklayarak iletiyi panoya kopyalayın.

**Not**: Alternatif olarak, menüdeki herbir  unsur ile ilişkili klavye kısa yollarını kullabilirsiniz, bu durumda **Ctrl+E** iletiyi şifreler, **Ctrl+A** iletinin tümünü seçer, **Ctrl+C** iletiyi panoya kopyalar.

**6. Adım**. E-posta hesabınızı **açın** ve yeni bir ileti yazma penceresini **açın** sonrasında bu iletiyi aşağıdakine benzeyecek şekilde yapıştırın:

![](/sbox/screen/gpg4usb-en-1/25.png)

*4. Şekil: gpg4usb'de şifrelenip Gmail hesabındaki bir e-postaya yapıştırılmış bir şifreli ileti örneği*

**Not**: **Rich Text Formats** (**RTF**, Zengin Metin Formatları) şifreli ileti formatını bozabilir; bu yüzden, iletilerinizi düz metinle yazmak daha iyidir. **Gmail'de** **RTF'yi** düz metne çevirmek için *Seçenekler'i* **tıklayın**, ve ileti bölümünün en altındaki **Düz metin mod'unu** **seçin**. 

 ![](/sbox/screen/gpg4usb-en-1/26.png)

*Şekil 5: Gmail Format Seçenekleri*

<a name="4.1"></a>
## 4.1 Yazılı İletilerin Şifresi gpg4usb Kullanarak Nasıl Çözülür ##

Şifrelenmiş bir e-postanın şifresini çözmek için aşağıdaki adımları takip edin:

**1. Adım**. **gpg4usb** programını açmak için ![](/sbox/screen/gpg4usb-en-1/03.png)’ye **çift tıklayın**.

**2. Adım**. E-posta hesabınızı ve iletiyi **açın**. 

**3. Adım**. Şifrelenmiş mesajı **seçin**, **kopyalayın** ve **gpg4usb** konsolu *untitled1.txt* sekmesine aşağıdaki gibi **yapıştırın**: 

![](/sbox/screen/gpg4usb-en-1/27.png)

*Şekil 6: Şifresi çözülecek mesajı gösteren gpg4usb konsolu*

**Not**: Şifreli metin, aşağıda *Şekil 7’de* göründüğü gibi çift satır aralıkları ile görünüyorsa, **gpg4usb** otomatik olarak şifresini çözmeyebilir. Bu çift satır aralıklarını yok etmek için ![](/sbox/screen/gpg4usb-en-1/27b.png)’e **tıklayın** (ya da **Edit** [Düzenle] menüsünden *Remove double Linebreaks'i* [Çift Satır Aralıklarını Kaldır’ı] seçin). Böylelikle, **4. Adım’da** tarif edilen şifre çözme işlemine devam edebilirsiniz. 

![](/sbox/screen/gpg4usb-en-1/28.png)

*Şekil 7: Çift satır aralıklarına sahip şifresi çözülecek bir ileti gösteren gpg4usb konsolu*
 
**4. Adım**. ![](/sbox/screen/gpg4usb-en-1/29.png)’e **tıklayın** ve aşağıda göründüğü gibi anahtar çifti oluştururken yarattığınız şifreyi **girin**.

![](/sbox/screen/gpg4usb-en-1/30.png)

*Şekil 8: Şifre Gir uyarı penceresi*

**5. Adım**. Yukarıdaki *Şekil 2’de* göründüğü gibi **gpg4usb** konsolunu etkinleştirmek için **OK'i** (Tamam’ı) **tıklayın**. 

<a name="4.2"></a>
## 4.2 Dosyalar gpg4usb Kullanarak Nasıl Şifrelenir? ##

Bir dosyayı şifreleme işlemi yazılı iletileri şifrelemeye benzer. Aşağıdaki örnekte, Salima aşağıdaki adımları takip ederek Terence için bir dosyayı şifreleyecek. 

**1.Adım**. **gpg4usb** programını açmak için ![](/sbox/screen/gpg4usb-en-1/03.png)’yi **tıklayın**.

**2. Adım**. Aşağıdaki ekranı etkinleştirmek için ![](/sbox/screen/gpg4usb-en-1/31.png)’ı ve *Encrypt File*'ı (Dosyayı Şifrele’yi) **tıklayın**:

![](/sbox/screen/gpg4usb-en-1/32.png)

*Şekil 9: Dosyayı Şifrele penceresi*

*Encrypt File* Dosyayı Şifrele penceresndeki kaydırma listesi (siyah ile gösterilmiş) iletinin şifrelenecek olan e-posta hesabını ve onunla bağlantılı anahtarı seçmenizi sağlar. 

**3. Adım**. Aşağıdaki ekranı etkinleştirmek için *Input* (Girdi) maddesinin yanındaki ![](/sbox/screen/gpg4usb-en-1/33.png)’ya **tıklayın**.

![](/sbox/screen/gpg4usb-en-1/34.png)

*Şekil 10: Dosya Aç tarama penceresi*

**4. Adım**. Şifrelenecek dosyayı eklemek için ![](/sbox/screen/gpg4usb-en-1/35.png)’ı **tıklayın** ve *Encrypt* (Şifrele) ekranına aşağıda göründüğü gibi dönün:

![](/sbox/screen/gpg4usb-en-1/36.png)

*Şekil 11: Şifrelenecek olan dosyayı gösteren Dosya Şifrele penceresi*

**5. Adım**. Aşağıdaki ekranı etkinleştirmek için **OK'yi** (Tamam’ı) **tıklayın**:

![](/sbox/screen/gpg4usb-en-1/38.png)

*Şekil 12: Tamamlandı onaylama iletişim kutusu*

*Tamamlandı* onaylama iletişim kutusu, yeni şifrelenmiş dosyaların nerede olduğunu gösterir. Şifrelenmiş bir dosya, *.asc* dosya uzantısı sayesinde de tanınabilir, örneğin, *Meeting Minutes.doc.asc*.

**6. Adım**. Dosya şifreleme işlemini tamamlamak için *OK'i* (Tamam’ı) **tıklayın**.

**Not**: Şifrelenmiş bir dosya ile göndereceğiniz iletiyi ayrıca şifreleyebilirsiniz.

**7. Adım**. E-posta hesabınızı kullanarak *Tamamlandı* onaylama iletişim kutusunda belirtilen yere **gidin** (*Şekil 12*) ve şifrelenmiş dosyayı herhangi bir dosya ekler gibi e-postanıza **ekleyin**. 

**ÖNEMLİ**: Dosyanın adının **şifrelenmemiş** olduğuna dikkatinizi çekeriz. Bu adın hassas bilgiler içermediğinden emin olun! Ayrıca, aklınızda tutun ki bu dosyanın şifrelenmemiş bir versiyonu diskinizde yer almaya devam eder.

<a name="4.3"></a>
## 4.3 Dosyaların Şifresi gpg4usb Kullanarak Nasıl Çözülür ##

Aşağıdaki örnekte, Terence aşağıdaki adımları takip ederek Salima’nın ona gönderdiği dosyanın şifresini çözecek:

**1. Adım**. **gpg4usb** programını açmak için ![](/sbox/screen/gpg4usb-en-1/03.png)’yi **çift tıklayın**. 

**2. Adım**. E-posta hesabınızı ve iletiyi **açın** ve eklenmiş dosyayı **indirin**. 

**Not**: İletişim içinde olduğunuz kişi şifrelenmiş dosyayla birlikte bir mesaj da göndermişse, bu mesajı, [**4.1. Yazılı İletilerin Şifresi gpg4usb Kullanarak Nasıl Çözülür?**](/tr/gpg4usb-encryptdecrypt#4.1) bölümünde anlatılan yöntemi kullanarak çözebilirsiniz. 

**3. Adım**. **gpg4usb** konsolunda (yukarıdaki *Şekil 1’de* gösterildiği gibi),  ![](/sbox/screen/gpg4usb-en-1/31.png)’a ve **Decrypt File** (Dosyanın Şifresini Çöz) penceresine **tıklayın** (aşağıdaki *Şekil 13’te* göründüğü gibi). 

**4. Adım**. İndirilen şifrelenmiş dosyayı bulmak için aşağıda göründüğü gibi *Input* (Girdi) maddesinin yanındaki ![](/sbox/screen/gpg4usb-en-1/33.png)’ya **tıklayın**.

![](/sbox/screen/gpg4usb-en-1/37.png) 

*Şekil 13: Şifrelenmiş dosyaya giden yolu gösteren Şifre Çöz penceresi*

**5. Adım**. Aşağıdaki ekranı etkinleştirmek için *OK'yi* (Tamam’ı) **tıklayın**: 

![](/sbox/screen/gpg4usb-en-1/39.png) 

*Şekil 14: Şifresi çözülmüş dosyanın yerini gösteren Tamamlandı onaylama iletişim kutusu*

**Önemli**: Bir İnternet kafede veya iş yerinde çalışıyorsanız, diğer kişilerin şifresi çözülmüş dosyaya erişimi olabilir. **.asc** uzantısına sahip dosyayı USB veya taşınabilir sürücüye kopyalamak ve evinize götürüp şifre çözme işlemini orada güvenli bir şekilde yapmak daha iyidir. 


