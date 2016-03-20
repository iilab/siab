

---

lang: tr
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: How to Install and Configure CCleaner

---

List of sections on this page:  

- [**2.0 CCleaner Nasıl Kurulur**](#2.0)
- [**2.1 CCleaner’ı Yapılandırmaya Başlamadan Önce**](#2.1)
- [**2.2 CCleaner Nasıl Yapılandırılır**](#2.3)


<a name="2.0"></a>
## 2.0 CCleaner Nasıl Kurulur ##

**Ccleaner** kurmak görece olarak kolay ve hızlı bir işlemdir. **CCleaner’ı** kurmaya başlamak için aşağıdaki adımları takip edin:

**1. Adım**. Kurulum işlemini başlatmak için ![](/sbox/screen/ccleaner-tr/01.png)’e **çift tıklayın**. Uyarı iletişim kutusu açılabilir. Açılırsa *Evet’i* **tıklayın** ve aşağıdaki ekranı etkinleştirin:

![](/sbox/screen/ccleaner-tr/03.png)

*Şekil 1: CCleaner v5.06 Kurulum Sihirbazına Hoş Geldiniz penceresi*

**2. Adım**. Aşağı Açılır Menü'den Türkçe'yi kurulum dili olarak seçin *Yükleme Seçenekleri – Ek seçenekler...* penceresini etkinleştirmek için ![](/sbox/screen/ccleaner-tr/05a.png)’i **tıklayın**.

![](/sbox/screen/ccleaner-tr/09a.png)

*Şekil 2: Yükleme Seçenekleri – Ek Seçenekler... penceresi*

**3.Adım**:  *Yükleme Seçenekleri – Ek seçenekler...* penceresinde *Akıllı Çerez (cookie) aramayı geç seçeneğinin işaretini yukarıdaki gibi kaldırın ve aşağıdaki ekranı etkinleştirmek için ![](/sbox/screen/ccleaner-tr/05b.png)’yi ya da  ![](/sbox/screen/ccleaner-tr/08.png)’u **tıklayın**:

![](/sbox/screen/ccleaner-tr/07.png)

*Şekil 3: Google Chrome’u verili tarayıcı penceresi olarak kur*

**3. Adım**.  *Google Chrome’u verili tarayıcı penceresi olarak kur* seçeneğini, yukarıdaki *Şekil 2’de* göründüğü gibi **etkisizleştirin**. Bu sayede *Google Chrome'un* kendisini bilgisayarınıza otomatik olarak kurmasını engellemiş olursunuz. Bu ekran görünmeyebilir de. 

**4. Adım**. Kurulum gelişim statü çubuğunu gösteren *Kurulum* ekranını etkinleştirmek için ![](/sbox/screen/ccleaner-tr/08.png)’u **tıklayın**. 

**5. Adım**. **CCleaner** kurulumunu bitirmek için  ![](/sbox/screen/ccleaner-tr/09.png)’i **tıklayın** ve CCleaner ana konsolunu açın.

![](/sbox/screen/ccleaner-tr/12.png)

*Şekil 4: Piriform CCleaner ana konsolu*

<a name="2.1"></a>
## 2.1 CCleaner’ı Yapılandırmaya Başlamadan Önce##

**Nasıl Yapmalı Kitapçığı** [**6. Hassas bilgiler nasıl imha edilir**](/tr/chapter-6) Bölümü’nde detaylı bir şekilde anlatıldığı gibi , **Microsoft Windows** standart dosya silme yöntemleri, diskinizdeki temel verileri silmez (*Geri Dönüşüm Kutusunu* boşaltsanız bile). Bu geçici dosyalar için de geçerlidir. Onları sabit diskinizden kalıcı olarak silmek için (ya da *ortadan kaldirmak* için), dosyaların üzerine rastgele verilerin yazılması gerekir. **CCleaner**, silinen dosyaların güvenli bir şekilde silinmesi için onların üzerine yazacak şekilde yapılandırılmalıdır, çünkü verili modunda bunu yapmaz. **CCleaner** aynı zamanda, diskin boş alanlarını temizleyerek eskiden silinmiş dosyaları da temizleyebilir (bunun için lütfen **5.3 CCleaner Kullanarak Boş Alan Nasıl Temizlenir** bölümüne bakın). 

<a name="2.2"></a>
## 2.2 CCleaner Nasıl Yapılandırılır ##

**CCleaner** kullanilmaya başlamadan önce, tüm geçici dosyaları güvenli silecek şekilde yapılandırılmalıdır. 

**CCleaner’i** yapılandırmak için aşağıdaki adımları takip ediniz: 

**1. Adım**. *Piriform CCleaner* konsolunu etkinleştirmek için ![](/sbox/screen/ccleaner-tr/13.png)’e **tıklayın** ya da **Başlat  >  Programlar  >  CCleaner’ı seçin**. 

**2. Adım**. Aşağıdaki ekranı etkinleştirmek için ![](/sbox/screen/ccleaner-tr/14.png)’ı **tıklayın**. 

![](/sbox/screen/ccleaner-tr/15.png)

*Şekil 6: Verili Hakkında sekmesini gösteren Seçenekler penceresi*

**3. Adım**. *Ayarlar* sekmesini etkinleştirmek için ![](/sbox/screen/ccleaner-tr/16.png)’i **tıklayın**. *Ayarlar* sekmesinde istediğiniz dili seçebilir ve **CCleaner’ın** geçici dosyaları nasıl sileceğini ve diskleri nasıl temizleyeceğini seçebilirsiniz. 

**Not**: *Güvenli Dosya Silme* bölümü, *Normal dosya silme* seçeneği seçili olarak belirir. 

**4. Adım**. Aşağı açılır listeyi etkinleştirmek için *Güvenli dosya silme (yavaş)* seçeneğini **tıklayın**.

**5. Adım**. *Güvenli dosya silme (yavaş)* aşağı açılır menüsünü **tıklayın** ve aşağıdaki ekranı etkinleştirmek için *Gelişmiş Üstüneyazma (3 passes)* seçeneğini **seçin**. 

![](/sbox/screen/ccleaner-tr/17.png)

*Şekil 5: Güvenli Silme seçeneklerini gösteren Ayarlar sekmesi*

Bu ayarı yaptıktan sonra, **CCleaner**, rastgele verilerle silmeyi seçtiğiniz dosya ve klasörlerin üzerine yazacak ve onları sabit diskinizden etkin bir şekilde silecektir. Güvenli sil aşağı açılır menüsündeki ‘kere’ seçeneği, sileceğiniz dosyaların üzerine kaç kere rastgele veri yazılacağını belirler. Bu sayıyı ne kadar arttırırsanız, silinecek olan dosya veya klasörlerinizin üzerine o kadar çok rastgele veri yazılacaktır. Bu durum dosya, belge veya klasörlerinizi geri getirmenizi zorlaştırır ama silme işleminin süresini de uzatır. 
  

