

---

lang: tr
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: How to Clean the Windows Registry in CCleaner

---

List of sections on this page:  

- [**4.0 Başlamadan Önce**](#4.0)
- [**4.1 Windows Kayıt Defteri CCleaner Kullanarak Nasıl Temizlenir**](#4.1)
- [**4.2 2 Kayıt Defteri Yedekleme Dosyası Nasıl Geri Kazanılır?**](#4.2)

<a name="4.0"></a>
## 4.0 Başlamadan Önce ##

**CCleaner**, sisteminizde yapılandırma bilgilerini, donanım ve yazılım ayarlarınızı saklayan bir veri tabanı oluşturan **Windows Kayıt Defteri’ni** temizlemenize olanak sağlar. Sistem yapılandırma bilgilerinizi değiştirdiğiniz, yazılım indirdiğiniz veya başka rutin işlemler yaptığınız zaman, bu değişiklikleri **Windows Kayıt Defteri’nde** belirir ve kaydedilir. 

Zaman içinde, **Windows Kayıt Defteri** zamanı geçmiş yapılandırma bilgi ve ayarlarını, kullanılmayan programların izlerini biriktirir. **CCleaner** *Kayıt Defteri* seçeneği bu tip bilgileri gözden geçirmenize ve silmenize olanak verir. Böylece, sisteminizin genel işlevini ve hızını geliştirmiş ve dijital gizliliğinizi ve güvenliğinizi korumuş olursunuz.  

**İpucu**: **Windows Kayıt Defteri** taraması haftada bir ya da ayda bir yapılmalıdır. 

<a name="4.1"></a>
## 4.1 Windows Kayıt Defteri CCleaner Kullanarak Nasıl Temizlenir ##

**1. Adım**. Aşağıdaki ekranı etkinleştirmek için ![](/sbox/screen/ccleaner-tr/30.png)’ne **tıklayın**:

![](/sbox/screen/ccleaner-tr/31.png)

*Şekil 1: Kayıt Defteri modunda CCleaner kullanıcı arayüzü *

**CCleaner** *Kayıt Defteri* penceresi, *Kayıt Defteri Bütünlüğü* listesi ve tespit edilen problemler ile ilgili bilgileri gösteren bir sekmeye ayrılmıştır. 

**2. Adım**. *Kayıt Defteri Bütünlüğü* listesindeki maddeleri **işaretleyin** (*Şekil 1’de* göründüğü gibi) ve ![](/sbox/screen/ccleaner-tr/32.png)’yı **tıklayın**. Bu şekilde, kayıt ile ilgili problemler çözülmek üzere taranacaktır. Bir süre sonra sonuçlar şu şekilde görünür:

![](/sbox/screen/ccleaner-tr/33.png)

*Şekil 2: Çözülecek problemler listesini gösteren sonuç sekmesi* 

**Windows Kayıt Defterini** temizlemeye başlamadan önce almanız gereken bir önlem, kayıt defterinizi yedeklemektir. **Windows Kayıt Defteri** temizlendikten sonra bir problem oluşursa, yedekleme dosyalarınızı kullanarak **Windows Kayıt Defterinizi** eski haline getirebilirsiniz. 

**3. Adım**. Aşağıda görünen iletişim kutusunu etkinleştirmek için ![](/sbox/screen/ccleaner-tr/34.png)’ü **tıklayın**:

![](/sbox/screen/ccleaner-tr/35.png)

*Şekil 3: Onay iletişim kutusu*

**İpucu**: Yedek kayıt defterini nereye sakladığınızı unutursanız, .reg dosya uzantısını aratabilirsiniz. 

**4. Adım**. Kayıt defterinizi yedeklemek için ![](/sbox/screen/ccleaner-tr/36.png)’i **tıklayın** ve aşağıdaki ekranı etkinleştirin:

![](/sbox/screen/ccleaner-tr/37.png)

*Şekil 4: Farklı Kaydet yer belirleme tarayıcısı*

**5. Adım**. Dosyanızı yedeklemek için bir yer belirledikten sonra ![](/sbox/screen/ccleaner-tr/38.png)’i **tıklayın** ve aşağıdaki iletişim kutusunu etkinleştirin: 

![](/sbox/screen/ccleaner-tr/39.png)

*Şekil 5: Sorunu çöz/Seçili Tüm Sorunları çöz iletişim kutusu*

**Not**: Gelişmiş veya uzman kullanıcılar, ihtiyaçlarına göre, bazı problemleri çözerken bazılarını yok saymak isteyebilirler. Ortalama düzeydeki yeni kullanıcıların tüm seçili problemleri çözmesini tavsiye ederiz.

**6. Adım**. Sorunları teker teker görüntülemek için  ![](/sbox/screen/ccleaner-tr/41.png) veya ![](/sbox/screen/ccleaner-tr/40.png)’ figürlerini **tıklayın** ve daha sonra çözmek istediğiniz sorunları seçerek ![](/sbox/screen/ccleaner-tr/42.png)’ü tıklayın. 

**7. Adım**. Seçilen *tüm* problemleri çözmek için ![](/sbox/screen/ccleaner-tr/43.png)’ü **tıklayın** ve temizleme işlemini tamamlamak için ![](/sbox/screen/ccleaner-tr/44.png)’ı **tıklayın**. 

**İpucu**: Çözülecek problem kalmayana kadar **2. Adım** ile **7. Adım** arasındaki adımları tekrar edin. 

Böylelikle, Windows Kayıt Defteri başarılı bir şekilde temizlenmiştir. 

<a name="4.2"></a>
## 4.2 Kayıt Defterinin Yedekleme Dosyası Nasıl Geri Kazanılır?##

**Windows Kayıt Defteri'ni** temizlemenin sisteminizin işleyişinde bir soruna yol açtığını düşünüyorsanız, **4.1** bölümünün **üçüncü ile beşinci adım** arasında yarattığınız kayıt defteri yedekleme dosyasını kullanarak orijinal kayıt defterinizi geri getirebilir ve sisteminizin sorunlarını giderebilirsiniz. 

Orijinal kayıt defterini geri getirmek için aşağıdaki adımları takip ediniz:

**1. Adım**. *Çalıştır* penceresini etkinleştirmek için **Başlat > Çalıştır’ı seçin** ve aşağıda göründüğü gibi *regedit* **yazın**:

![](/sbox/screen/ccleaner-tr/45.png)

*Şekil 6: Çalıştır penceresi*

**2. Adım**. Aşağıdaki ekranı etkinleştirmek için ![](/sbox/screen/ccleaner-tr/22.png)’ı **tıklayın**: 

![](/sbox/screen/ccleaner-tr/46.png)

*Şekil 7: Kayıt Defteri Düzenleyicisi*

**3. Adım**. *Kayıt Defteri Dosya Aktar* ekranını etkinleştirmek için *Kayıt Defteri Düzenleyicisi menüsünden **Dosya  > İçe Aktar’ı seçin** ve daha sonra ![](/sbox/screen/ccleaner-tr/47.png)’ü **seçin**. 

**4. Adım**. Aşağıdaki iletişim kutusunu etkinleştirmek için ![](/sbox/screen/ccleaner-tr/48.png)’ı **tıklayın**: 

![](/sbox/screen/ccleaner-tr/49.png)

*Şekil 8: Kayıt Defteri yedeklemenin gerçekleştiğini onaylayan Kayıt Defteri Editörü iletişim kutusu*

**5. Adım**. Kayıt Defteri yedekleme dosyasını geri getirme işlemini tamamlamak için ![](/sbox/screen/ccleaner-tr/22.png) ’ı **tıklayın**. 


