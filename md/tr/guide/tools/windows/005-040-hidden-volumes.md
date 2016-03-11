

---

lang: tr
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 4
depth: 3
title: Hidden Volumes

---

Bu sayfadaki konuların listesi:

- [**5.0 Gizli Birimler Hakkında**](#5.0)
- [**5.1 Gizli Birim Nasıl Oluşturulur**](#5.1)
- [**5.2 Gizli Birim Nasıl Bağlanır**](#5.2)
- [**5.3 Gizli Disk Özelliğini Güvenli bir Şekilde Kullanmak için İpuçları**](#5.3)

<a name="5.0"></a>
## 5.0 Gizli Birimler Hakkında ##

**TrueCrypt’te** *Gizli Birim* sizin şifrelenmiş *Standart Biriminizde* saklanır fakat varlığı gizlenmiştir. Standart biriminizi bağladığınız veya açtığınız zaman bile, gizli birimin varlığını kanıtlamak mümkün değildir. Standart biriminizin yerini ve şifresini söylemeye zorlanırsanız, içindekiler ortaya çıkabilir ama onun içindeki gizli birim ortaya **çıkmaz**.

Gizli bölmesi olan bir çanta düşünün. İfşa edilmesini veya kaybolmasını önemsemediğiniz dosyaları çantanın normal bölmelerinde tutar, önemli ve özel dosyalarınızı ise gizli bölmesine koyarsınız. Gizli bölmenin amacı (özellikle de iyi yapılmış olanın), kendi varlığını ve dolayısıyla içindeki belgeleri gizlemektir. 

<a name="5.1"></a>
## 5.1 Gizli Birim Nasıl Oluşturulur? ##

**TrueCrypt** *Gizli Birimi* yaratmak, **TrueCrypt** *Standart Birimi* yaratmaya benzer. Bölme, ekran ve pencerelerin bazıları tamimiyle aynıdır. 


**1. Adım**. **TrueCrypt’i açın**..

**2. Adım**. *TrueCrypt Birim Oluşturma Sihirbazı’nı* etkinleştirmek için ![](/sbox/screen/truecrypt-tr/13.png)’u **tıklayın**.

**3. Adım**. Verili olan *Create and encrypted file container* (Şifreli dosya muhafazası oluştur) seçeneğini kabul edin ve ![](/sbox/screen/truecrypt-tr/03.png)’yi **tıklayın**. 

**4. Adım**. *Hidden TrueCrypt Volume* (Gizli TrueCrypt Birimi) seçeneğini aşağıdaki gibi **işaretleyin**:

![](/sbox/screen/truecrypt-tr/37.png)

*Şekil 1: TrueCrypt Birim Oluşturma Sihirbazı ve seçilmiş olan Gizli TrueCrypt Birimi seçeneği*

**5. Adım**. Aşağıdaki ekrani etkinleştirmek için ![](/sbox/screen/truecrypt-tr/03.png)’yi **tıklayın**:

![](/sbox/screen/truecrypt-tr/38.png)

*Şekil 2: TrueCrypt Birim Yaratma Sihirbazı – Mod penceresi*

- *Direct mode* (Direkt mod): Bu seçenek, varolan bir *Standart Birim* içerisinde bir *Gizli Birim*oluşturmanızı sağlar.

- *Normal mode* (Normal mod): Bu seçenek, içine *Gizli Birim'i* saklayacağınız yepyeni bir *Standart Birim* oluşturmanızı sağlar.

Bu örnekte *Direkt modu* kullanacağız. . 

**Not**: Yeni bir *Standart Birim* ile başlamayı tercih ederseniz, [**2.2 Standart Bir Birim Nasıl Oluşturulur**](/tr/truecrypt_standardvolumes#2.2) bölümündeki işlemleri tekrar edebilirsiniz.

**6. Adım**. *Direkt mod* seçeneğini **seçin** ve *TrueCrypt Birim Oluşturma – Birim Yeri* penceresini etkinleştirmek için ![](/sbox/screen/truecrypt-tr/03.png)’yi **tıklayın**.

**Not**: Seçmeden önce *Standart Birimin* bağlanmamış olduğundan emin olun.

**7. Adım**. Aşağıdaki ekranı etkinleştirmek için ![](/sbox/screen/truecrypt-tr/17.png)’i **tıklayın**:

![](/sbox/screen/truecrypt-tr/29.png)

*Şekil 3: TrueCrypt Birim Oluşturma Sihirbazı – TrueCrypt Birimi Seç penceresi*

**8. Adım**. *TrueCrypt Birimi Seç* penceresini kullanarak birimin yerini *Şekil 3’teki* gibi **belirleyin**.  

**9. Adım**. *TrueCrypt Birim Oluşturma Sihirbazı’na* dönmek için  ![](/sbox/screen/truecrypt-tr/30.png)’ı **tıklayın**.

**10. Adım**. *Parolayı Girin* ekranını etkinleştirmek için ![](/sbox/screen/truecrypt-tr/27.png)’ı **tıklayın**.

**11. Adım**. Aşağıdaki ekranı etkinleştirmek için *Standart Birim* yaratırken kullandığınız şifreyi *Parola* metin alanına **girin**.

![](/sbox/screen/truecrypt-tr/46.png)

*Şekil 4: TrueCrypt Birim Oluşturma Sihirbazı – Gizli Birim Mesaj sekmesi*

**12. Adım**. *Hidden Volume Encryptions Options* (Gizli Birim Şifreleme Seçenekleri) ekranını etkinleştirmek için, mesajı okuduktan sonra ![](/sbox/screen/truecrypt-tr/27.png)’ı **tıklayın**.

**Not**: *Encryption Algorithm* (Gizli Birim için Şifreleme Algoritması) ve *Hash Algorithm* (Hash Algoritması) seçeneklerini verili olduğu gibi bırakın. 

**13. Adım**. Aşağıdaki ekranı etkinleştirmek için ![](/sbox/screen/truecrypt-tr/03.png)’yi **tıklayın**: 

![](/sbox/screen/truecrypt-tr/41.png)

*Şekil 5: TrueCrypt Birim Oluiturma Sihirbazı – Gizli Birim Boyutu penceresi*

*Gizli Biriminizin* boyutunu belirlemeniz istenecektir. 

**Not**: Saklanacak olan belgelerin niteliğine, niceliğine ve boyutuna göre karar verin. *Standart Birim* için yer ayırın. *Gizli Birim* için eldeki bütün alanı seçerseniz, orijinal *Standart Birime* yeni dosya koyamazsınız. 

Eğer *Standart Biriminiz* 10 megabayt ise ve Gizli Biriminizi 5 megabayt olarak belirlerseniz (yukarıdaki *Şekil 6’da* göründüğü gibi), iki tane 5 megabayttan oluşan biriminiz olacak (biri standart, biri gizli). 

*Standart Birimde* sakladığınız bilgilerin belirlemiş olduğunuz 5 megabaytı geçmemesine dikkat edin. Çünkü **TrueCrypt** programı *Gizli Birimin* varlığını otomatik olarak tespit etmez ve üzerine yazabilir. Belirlemiş olduğunuz boyutu aşarsanız saklamış olduğunuz tüm dosyaları kaybetme riskini doğurursunuz. 

**14. Adım**. İstediğiniz gizli birim boyutunu gerekli metin kutusuna *Şekil 6’da* göründüğü gibi **yazın**.

**15. Adım**. *Gizli Birim Parolası* penceresini etkinleştirmek için ![](/sbox/screen/truecrypt-tr/03.png)’yi **tıklayın**.

Gizli biriminiz için standart biriminizi koruyandan *farklı* bir şifre yaratmalısınız. Her zamanki gibi güçlü bir şifre seçmeyi unutmayın. Güçlü şifreler yaratma konusunda daha fazla bilgi için lütfen [**KeePass**](http://securityinabox.org/en/keepass_main) bölümüne bakın. 

**İpucu**: TrueCrypt birimlerinizin içeriğini ifşa etmeye zorlanacağınızı düşünüyorsanız, standart birim şifrenizi **KeePass’te** saklayın ve gizli birim için yalnızca sizin bileceğiniz ve hatırlayacağınız bir şifre seçin. Bu sayede gizli biriminiz ile ilgili hiçbir iz bırakmamış olursunuz. 

**16. Adım**. Bir şifre yaratıp iki kere **girin** ve aşağıdaki ekranı etkinleştirmek için ![](/sbox/screen/truecrypt-tr/03.png)’yi **tıklayın**:

![](/sbox/screen/truecrypt-tr/42.png)

*Şekil 6: TrueCrypt Birim Yaratma Sihirbazı – Gizli Birim Format sekmesi*

*File System* (Dosya Sistemi) ve *Cluster* Küme opsiyonlarını verili olduğu gibi bırakın.

**17. Adım**. Şifrelemenin kriptografik gücünü arttırmak için imleci ekranda **gezdirin** ve sonra gizli birimi biçimlendirmek için  ![](/sbox/screen/truecrypt-tr/25.png)’i **tıklayın**.

*Gizli birim biçimlendirildikten sonra, aşağıdaki ekran belirecektir:* 

![](/sbox/screen/truecrypt-tr/43.png)

*Şekil 7: TrueCrypt Birim Oluşturma Sihirbazı mesaj ekranı*

**Not**: *Şekil 8*, başarılı bir şekilde gizli birim yarattığınızı gösterir ve dosyalarınızı standart birime saklarken yanlışlıkla gizli birimin üzerini yazma riskine karşı sizi uyarır. 

**18. Adım**. *Hidden Volume Created* (Gizli Birim Oluşturuldu) penceresini etkinleştirmek için ![](/sbox/screen/truecrypt-tr/27.png)’ı **tıklayın** ve **TrueCrypt** konsoluna geri dönmek için ![](/sbox/screen/truecrypt-tr/28.png)’yi **tıklayın**.

Artık, standart biriminizin içinde bir gizli birim var. Bu standart birimin şifresine sahip olan birinin bile erişemeyeceği bir şekilde dosyalarınızı saklayabilirsiniz gizli birimin içine. 

<a name="5.2"></a>
## 5.2 Gizli Birim Nasıl Bağlanır ##

*Gizli Birimi* bağlamak veya kullanıma açmak, *Standart Birim* işlemleri ile aynıdır. Tek fark, *Gizli Birim* için oluşturduğunuz şifreyi kullanmanız gerekmesidir. 

*Gizli Birimi* *oluşturmak* ve açmak için aşağıdaki adımları takip edin:

**1. Adım**. Listeden bir sürücü **seçin** (bu örnekte, *K* sürücüsü):

![](/sbox/screen/truecrypt-tr/44.png)

*Şekil 8: TrueCrypt Birimi ekranında seçili bir sürücü*

**2. Adım**. *Bir TrueCrypt Birimi Seçin* penceresini etkinleştirmek için ![](/sbox/screen/truecrypt-tr/17.png)’i **tıklayın**.

**3. Adım**. **TrueCrypt** birimi dosyasını (standart birim ile aynı dosya) **bulun** ve **seçin**.

**4. Adım**. **TrueCrypt** konsoluna dönmek için ![](/sbox/screen/truecrypt-tr/30.png)’ı **tıklayın**.

**5. Adım**. *Parolayı Girin* uyarı ekranını aşağıdaki gibi etkinleştirmek için ![](/sbox/screen/truecrypt-tr/31.png)’yı **tıklayın**. 

![](/sbox/screen/truecrypt-tr/32.png)

*Şekil 9: Parolayı Girin ekranı*

**6. Adım**. Gizli biriminizi yaratırken kullandığınız şifreyi **girin** ve ![](/sbox/screen/truecrypt-tr/33.png)’ı **tıklayın**. 

Gizli biriminiz aşağıdaki gibi bağlandı (veya açıldı)::

![](/sbox/screen/truecrypt-tr/45.png)

*Şekil 10: Yeni oluşturulmuş Gizli Birimi gösteren TrueCrypt ana ekranı*

**7. Adım**. *Gizli Birime* yukarıdaki girişe **çift tıklayarak** veya *Bilgisayarım* penceresinden ulaşın. 

<a name="5.3"></a>
## 5.3 Gizli Disk Özelliğini Güvenli bir Şekilde Kullanmak için İpuçları ##

Gizli disk özelliğinin amacı, güç sahibi birisi sizden şifrelenmiş dosyalarınızı ifşa etmenizi isterse, şifrelerinizi *veriyormuş gibi yaparak* hassas bilgilerinizi saklamaya devem edebilmenizi sağlamaktır. Verileriniz korumanın yanı sıra, bu durum, kendi güvenliğinizi ve meslektaş ve partnerlerinizin güvenliğini daha fazla riske atmamanıza da yardımcı olur. Bu yöntemin etkili olması için, dosyalarınızı görmek isteyen kişilerin onlara sunduklarınızdan tatmin olacağı ve sizi bırakacağı bir durum yaratmalısınız. 

Bunun için aşağıdaki önerilerden bazılarını takip etmek isteyebilirsiniz: 

- Standart birime, görünmesini önemsemediğiniz bazı gizli belgeler koyun. Bu bilgiler, onları şifreli bir birimde tutmanızı haklı çıkaracak kadar hassas olmalı. 

- Unutmayın ki dosyalarınızı görmek isteyen kişiler gizli birimlerden haberdar olabilir. Fakat, **TrueCrypt’i** olması gerektiği gibi kullanıyorsanız, bu kişiler sizin gizli birimleriniz olduğunu kanıtlayamaz ve böylelikle inkarınız daha gerçekçi olur. 

- Standart birimdeki dosyaları haftalık olarak güncelleyin. Böylelikle o dosyaları gerçekten kullanıyor gibi görünebilirsiniz. 

**TrueCrypt** birimini her bağlayışınızda, *Dış birime yazarken gizli birime gelecek hasara karşı koru* seçeneğini seçebilirseniz. Bu *çok* önemli bir özelliktir ve gizli biriminizdeki şifreli içeriğin üzerine yazma veya bu içeriği yanlışlıkla silme gibi risklerden uzak durarak, standart biriminize “yem” dosyalar koyabilmenizi sağlar.  

Daha önce de belirttiğimiz gibi, standart birimdeki depolama sınırlarını aşmak gizli dosyalarınıza zarar verebilir. **TrueCrypt** birimi bağlamaya zorlandığınız zaman *Gizli Birimi Koru* seçeneğini etkinleştirmeyin. Yoksa, gizli biriminizin şifresini girmek zorunda kalır ve bu birimin varlığını ifşa etmiş olursunuz. Fakat, kimse yokken yem dosyalarınızı güncellerken bu seçeneği *her zaman* etkinleştirmelisiniz. 

*Gizli Birimi Koru* özelliğini kullanmak için aşağıdaki adımları takip ediniz:

**1. Adım**. Yukarıdaki *Şekil 10’da* görünen *Parolayı Girin* uyarı ekranındaki ![](/sbox/screen/truecrypt-tr/47.png)’nı **tıklayın**. Bu şekilde *Bağlama Özellikleri* penceresini aşağıda göründüğü gibi etkinleştirebilirsiniz:

![](/sbox/screen/truecrypt-tr/48.png)

*Şekil 11: Bağlama Özellikleri penceresi*

**2. Adım**. *Dış birime yazarken gizli birime gelecek hasara karşı koru* seçeneğini **seçin**. 

**3. Adım**. Gizli Birim şifrenizi **yazın** ve ![](/sbox/screen/truecrypt-tr/33.png)’ı **tıklayın**.

**4. Adım**. Standart bağlamak oluşturmak için  ![](/sbox/screen/truecrypt-tr/31.png)’yı **tıklayın**. Başarılı bir şekilde bağlandıktan sonra, gizli biriminize zarar vermeden yem dosyalar ekleyebilirsiniz.

**5. Adım**. İçeriğini düzenledikten sonra standart biriminizin bağlantısını kesmek veya kullanımdan çıkarmak için ![](/sbox/screen/truecrypt-tr/49.png)’i **tıklayın**. 

**Hatırlatma**: Bunu sadece standart biriminizdeki dosyaları güncellerken yapmanız gerekir. Standart biriminizi ifşa etmeye zorlanırsanız, *Gizli Birimi Koru* seçeneğini seçmemelisiniz. 

