

---

lang: tr
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Mount the Standard Volume

---

Bu sayfadaki kısımların listesi:

- [**3.0 Standart Bir Birim Nasıl Bağlanır**](#3.0)
- [**3.1 Standart Bir Birimin Bağlantısı Nasıl Kesilir**](#3.1)

<a name="3.0"></a>
## 3.0 Standart Bir Birim Nasıl Bağlanır ##

**TrueCrypt’te** *Standart Birim'i* bağlamak, standart birimi kullanıma açmak anlamına gelir. Bu bölümde, yeni yarattığınız standart birimi nasıl kullanacağınızı öğreneceksiniz.   

Standart birimi bağlamak çin aşağıdaki adımları takip edin:

**1. Adım**. **TrueCrypt‘i** açmak için ![](/sbox/screen/truecrypt-tr/52.png)’a **çift tıklayın** veya **Başlat > Programlar > TrueCrypt > TrueCrypt'i seçin**.

**2. Adım**. Listeden, aşağıda göründüğü gibi herhangi bir sürücüyü **seçin**:

![](/sbox/screen/truecrypt-tr/12.png)

*Şekil 1: TrueCrypt konsolu*

*Bu örnekte standart birim M: sürücüsü olarak oluşturulacak.*

**Not**: *Şekil 1’de M:* sürücüsü *standart birimi* bağlamak üzere seçilmiştir fakat siz isterseniz listeden başka bir sürücü seçebilirsiniz.

**3. Adım**.  ![](/sbox/screen/truecrypt-tr/17.png)’i **tıklayın**.

*Bir TrueCrypt Birimi Seçin ekranı aşağıdaki gibi görünecektir:*

![](/sbox/screen/truecrypt-tr/29.png)

*Şekil 2: Bir TrueCrypt Birimi Seçin ekranı*

**4. Adım**. Yarattığınız standart birim dosyasını **seçin** ve *Şekil 2’yi* kapatmak için ![](/sbox/screen/truecrypt-tr/30.png)’ı **tıklayın** ve **TrueCrypt** konsoluna geri dönün. 

**5. Adım**. *.... İçin Parolayı Girin* uyarı ekranını aşağıdaki gibi etkinleştirmek için  ![](/sbox/screen/truecrypt-tr/31.png)’yı **tıklayın**.

![](/sbox/screen/truecrypt-tr/32.png)

*Şekil 3: .... İçin Parolayı Girin*

**6. Adım**. *Şifre*: metin alanına şifrenizi **girin**.

**7. Adım**. *Standart Birimi* bağlamak için   ![](/sbox/screen/truecrypt-tr/33.png)’ı **tıklayın**.

**Not**: Girdiğiniz şifre hatalıysa, **TrueCrypt** şifrenizi yeniden girmenizi ve ![](/sbox/screen/truecrypt-tr/33.png)’ı **tıklamanızı** isteyecek. Şifre doğruysa, *Standart Birim* aşağıdaki gibi oluşturulacak:

![](/sbox/screen/truecrypt-tr/34.png)

*Şekil 4: Yeni bağlanan Standart Birimi gösteren TrueCrypt konsolu*

**8. Adım**. **TrueCrypt’teki** altı çizili girişe **çift tıklayın** veya *Bilgisayarım* ekranındaki gerekli sürücüyü belirten harfe **çift tıklayın** ve *Standart Birime* erişin (bilgisayarınızdaki sürücü *M:’ye* çıkarılmış olan). 

![](/sbox/screen/truecrypt-tr/35.png)

*Şekil 5: Standart Birime Bilgisayarım ekranından erişme*

**Not**: *Birimim* standart birimini başarılı bir şekilde sanal sürücü *M:’de* oluşturduk. Bu sanal sürücü gerçek bir sürücü gibidir fakat tamamen şifrelenmiştir. Herhangi bir dosyayı bu sanal sürücüye kopyaladığınız, taşıdığınız veya kaydettiğiniz zaman otomatik olarak şifrelenecektir (buna anında şifreleme de denilebilir).

Herhangi normal bir diskte yaptığınız gibi, *Standart Birime* dosya kopyalayabilir veya oradan dosya alabilirsiniz (örneğin seçip bırakarak). Bir dosyayı *Standart Birim'den* çıkardığınız zaman, otomatik olarak şifresi çözülür. Aynı şekilde, bir dosyayı *Standart Birime* koyduğunuz zaman, TrueCrypt onu otomatik olarak şifreler. Bilgisayarınız aniden çöker veya kapanırsa, TrueCrypt, *Standart Birimi* hemen kapatacaktır. 

**Önemli**: dosyaları **TrueCrypt** birimine geçirdiğinizde, bu dosyaların bilgisayarınızda veya USB hafıza çubuğunuzda izi kalmadığından emin olun. [**6. Hassas bilgiler nasıl imha edilir?**](/tr/chapter-6)  bölümüne bakabilirsiniz.

<a name="3.1"></a>
## 3.1 Standart Bir Birimin Bağlantısı Nasıl Kesilir##

**TrueCrypt’te** *Standart Birimin* bağlantısını kesmek, onu kullanımdan çıkarmak anlamına gelir. 

*Standart Birimi* kapatmak veya bağlantısını kesmek ve dosyalarını sadece elinde şifresi olan kişilere erişimli hale getirmek için, aşağıdaki adımları takip edin:

**1. Adım**. **TrueCrypt** Ana konsolunda , oluşturulmuş birimler listesinden istediğiniz birimi aşağıdaki gibi **seçin**

![](/sbox/screen/truecrypt-tr/34.png)

*Şekil 17: Kaldırılacak olan Standart Birimi seçme*

**2. Adım**. **TrueCrypt** standart biriminizin bağlantısını kesmek için ![](/sbox/screen/truecrypt-tr/49.png)’i **tıklayın**. 

**Önemli**: **TrueCrypt** biriminizin bağlantısını bilgisayarınızı *Hazırda Bekleme* veya *Uyku* moduna çevirmeden önce kestiğinizden emin olun. Aslında, bilgisayarınızı kullanmayacağınız zamanlarda kapatmanız en iyisidir. Bu sayede, birim şifrenizin başkaları tarafından ulaşılmasını engellemiş olursunuz. 

Bağlantısını kestikten sonrastandart birime saklanmış bir dosyaya ulaşmak için, birimi yeniden bağlamanız gerekir.


