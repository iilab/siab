

---

lang: tr
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 5
depth: 3
title: Advanced Options, FAQ and Review

---

Bu sayfadaki kısımların listesi:

- [**6.0 Gelişmiş Seçenekler**](#6.0)
- [**6.1 CCleaner Kullanarak Nasıl Program Kaldırılır?**](#6.1) 
- [**6.2 CCleaner’la BaşlangıçProgramları Nasıl Devre dışı Bırakılır?**](#6.2)
- [**6.3 CCleaner Kullanarak Boş Disk Alanı Nasıl Temizlenir?**](#6.3)
- [**6.4 Sık Sorulan Sorular ve Özet**](#6.4)
- [**6.5 Özet Soruları**](#6.5)

<a name="6.0"></a>
## Gelişmiş Seçenekler  ##

Bilgisayar sisteminizin etkin çalışmasını sağlayan iki **CCleaner** özelliği vardır. *Bunlar aşağıda açıklandıkları gibi Geri Yükle (Kaldır)* ve *Başlangıçta* özellikleridir . Bu bölümde ayrıca belirlenen bir diskteki boş alanları nasıl *yok edeceğinizi* veya öğrenebilirsiniz. 



<a name="6.1"></a>
## 6.1 CCleaner Kullanarak Nasıl Program Kaldırılır ##

**Önemli**: Sileceğiniz veya kaldıracağınız programın bilgisayarınızın genel işleyişi için önemli olmadığından emin olun.

**CCleaner'ı** başlatmadan önce, daha önce kurduğunuz fakat kullanmadığınız veya istemediğiniz yazılımları silerek, onların geçici dosyalarını ve klasörlerini de silmiş olursunuz. Bu sayede, silinecek olan geçici dosya ve klasör sayısını ve temizleme işleminin süresini azaltmış olursunuz. 

**CCleaner** *Program Kaldırma* özelliği, **Kontrol Panelinde** bulunan **Program Kaldırma** özelliği ile aynı işlevi görür. **CCleaner Program Kaldırma** özelliği programları daha etkin ve çabuk bir biçimde listeler.

Kullanılmayan programları kaldırmak için aşağıdaki adımları takip edin:

**1. Adım**. *Piriform CCleaner* konsolunu etkinleştirmek için ![](/sbox/screen/ccleaner-tr/13.png)’e **tıklayın** ya da **Başlat > Programlar > CCleaner'ı seçin**. 

**2. Adım**. Aşağıdaki ekranı etkinleştirmek için  ![](/sbox/screen/ccleaner-tr/50.png)’a ve daha sonra ![](/sbox/screen/ccleaner-tr/51.png)’a **tıklayın**. 

![](/sbox/screen/ccleaner-tr/52.png)

*Şekil 1: Geri Yükle (Kaldır) sekmesini gösteren Araçlar opsiyonu*

**Not: *Kaldırılacak Programlar* listesinin sağında yer alan düğmeler, ancak kaldırılacak program seçildikten sonra etkin hale gelir.

**3. Adım**. *Kaldırılacak Programlar* listesinden bir program **seçin** ve seçtiğiniz programı kaldırmak için ![](/sbox/screen/ccleaner-tr/53.png)’a **tıklayın**.

**İpucu**: Gelişmiş ve deneyimli kullanıcılar, belli bir yazılım korsanını saklayabilmek için *Yeniden Adlandır* ve *Sil* özelliklerini faydalı bulabilirler. Bu programlardan her biri bu programın varlığından bir tek sizin haberdar olmanızı sağlar ve sizi kurulmuş programları listeleyebilecek zararlı taraflardan korur. 

**4. Adım**. Programa yeni bir isim vermek için ![](/sbox/screen/ccleaner-tr/54.png)’a **tıklayın** ya da programı kaldırmadan listeden silmek için ![](/sbox/screen/ccleaner-tr/55.png)’i **tıklayın**. 

<a name="6.2"></a>
## 6.2 CCleaner’la Başlangıç Programları Nasıl Devre dışı Bırakılır##

Başlangıç programları bilgisayarınızı başlattığınız zaman otomatik olarak başlar. Başlangıç, sınırlı sistem kaynaklarını kullanarak ve bilgisayarınızın başlama süresini uzatabilir.

**1. Adım**. Aşağıdaki ekranı etkinleştirmek için ![](/sbox/screen/ccleaner-tr/50.png)’a ve daha sonra  ![](/sbox/screen/ccleaner-tr/56.png)’ya **tıklayın**. 

![](/sbox/screen/ccleaner-tr/57.png) 

*Şekil 1: Başlangıçta bölmesini gösteren Araçlar seçeneği*

**2. Adım**. *Başlangıçta* bölmesinde listelenen programlardan birini **seçin** ve programı devre dışı bırakmak için ![](/sbox/screen/ccleaner-tr/58.png)’i **tıklayın**. Böylelikle, bilgisayarınızı başlattığınız zaman bu program otomatik olarak başlamayacaktır. 

<a name="6.3"></a>
## 6.3 CCleaner Kullanarak Boş Disk Alanı Nasıl Temizlenir ##

**Windows** işletim sisteminde, bir dosyayı silmek sadece o dosyaya verilen referansı silmek anlamına gelir ve programın gerçek verilerini devre dışı bırakmaz. Zaman geçtikçe sürücünüzün bu kısmına yeni veriler yazılacaktır ama bilgili bir kullanıcı bu dosyanın bir kısmını veya tümünü yeniden oluşturabilir. Bunun olmasını engellemek için sabit diskinizdeki bu alanı temizlemeniz gerekir. **CCleaner** aynı zamanda **Ana Dosya Cetvelini (Master File Table, MFT) ** temizlemenize olanak sağlar. 

**Ana Dosya Cetvelini (Master File Table, MFT)**, tüm dosyaların isim, yer ve diğer bilgilerini içeren bir dizindir. **Microsoft Windows** bir dosya sildiği zaman, verimlilik açısından, sadece bu dosyanın dizin girişini silinmiş gibi gösterir. Fakat dosyanın **MFT** girişi ve içeriği sabit diskinizde yer tutmaya devam eder. 

**Not**: Disk ve **MFT** temizliği olukça uzun sürer ve bu süre bu işlemde kaç geçiş (passes) yapıldığına göre değişir.

Bir sürücüyü temizlemek için aşağıdaki adımları takip ediniz: 

**1. Adım**. *Sürücü Temizleyici* bölmesini etkinleştirmek için önce ![](/sbox/screen/ccleaner-tr/50.png)’a, sonra da  ![](/sbox/screen/ccleaner-tr/62.png)’ye **tıklayın**. 

**2. Adım**. ![](/sbox/screen/ccleaner-tr/04.png)'a **tıklayarak** aşağı açılır listeyi etkinleştirin ve *Sadece Boş Alan* veya *Tüm Sürü (Bütün bilgiler silinecek)* seçeneklerinden birini **seçin** ve Güvenlik aşağı açılır menüsünden ![](/sbox/screen/ccleaner-tr/59.png)’yı **seçin**. 

**Uyarı**: Tüm belge, dosya, klasör ve boş alanlarınızın silinmesini istediğinizden *tamamen* eminseniz *Tüm Sürü (Bütün bilgiler silinecek)* seçeneğini seçin.

**3. Adım**. Silinecek sürücü ile ilişkili işaret kutucuğunu **işaretleyin** ve ![](/sbox/screen/ccleaner-tr/64.png)’i etkinleştirin. Aşağıdakine benzer bir pencere ile karşılaşacaksınız:

![](/sbox/screen/ccleaner-tr/65.png)

*Şekil 3: İlgili seçenekleri etkinleşmiş Sürücü Temizleyici bölmesi*

**4. Adım**. Seçtiğiniz disk(ler)in temizliğini başlatmak için ![](/sbox/screen/ccleaner-tr/64.png)’i **seçin**. 

<a name="6.4"></a>
## 6.4 Sık Sorulan Sorular ve Gözden Geçirme ##

<div class="background" markdown="1">

***Soru: CCleaner’ı devre dışı bırakırsam, daha önce silmiş olduğum materyal silinmiş olmaya devam eder mi?***

***Cevap**: Evet, CCleaner’ı düzgün bir şekilde yapılandırdıysanız, sildiğiniz dosyalar kalıcı olarak silinir.*

***Soru: CCleaner’ı bir USB çubuğuna kopyalarsam, bir İnternet kafede yapmış olduğum işlemlerin izlerini o bilgisayarda silebilir miyim? Bu şekilde kullanmanın bir sakıncası var mı?***

***Cevap**:  Yok, hayır, bu şekilde kullanılabilir. [**CCleaner’ın taşınabilir bir versiyonu**](/tr/ccleaner_portable) vardır. Çalıştığınız İnternet kafe, USB hafıza çubuğundan program kullanımına izin veriyorsa, orada yaptığınız işlemlerin izlerini silmek için **CCleaner** kullanabilirsiniz. Yine de İnternet kafede izlenebileceğinizi aklından çıkarmayın. Ayrıca, USB hafıza çubuğunu İnternet kafedeki bilgisayara bağlayarak virüslere açık hale getirmiş olduğunuzu unutmayın.*

***Soru: CCleaner ile temizlik yaparken sadece bir kere çalıştırırsam, verilerim başkaları tarafından yeniden oluşturulabilir mi? 7 geçişi (passes)  kullanırsam nasıl bir değişiklik olur?***

***Cevap**: TVerilerinizi temizlemek için ne kadar geçiş kullanırsanız, silmek istediğiniz verilerin tekrar bulunması o kadar zor hale gelir. Fakat, bu işlemi ne kadar çok kez tekrarlarsanız, silme işlemi de o kadar uzun sürer.* 

***Soru: Windows Kayıt Defterini silmek, bilgisayarımda yakın zamanda kurduğum ve kullandığım programların izlerini silmek içi yeterli midir?***

***Cevap**: İdeal olarak, programlara ait tüm dosyaları **CCleaner** kullanarak silmeniz gerekir. Bu sayede geçici dosyaları, **Kayıt Defterini** ve diskinizdeki boş alanları, kullandığınız yazılımların ve bunlarla yaptığınız işlemlerin izlerini de silebilirsiniz.*

</div>

<a name="6.5"></a>
## 6.5 Gözden Geçirme Soruları ##

- CClaner bilgisayarınızdan ne tür bilgileri siler?
- Bunu nasıl yapar?
- Verilerinizi güvenli bir şekilde gizlemek için bu işlemi kaç geçişle yapmalısınız?
- **Windows Kayıt Defteri** nedir ve neden temizlenmesi önerilir?
- **Windows Kayıt Defteri'ni** temizlemeden önce neler yapmalısınız?


