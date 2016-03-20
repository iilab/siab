

---

lang: tr
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 009
title: CCleaner - Secure File Deletion and Work Session Wiping

---

**Ana Sayfa**

[**www.ccleaner.com**](http://www.ccleaner.com)
 
**Bilgisayar Gereksinimleri**

- Tüm Windows Sürümleri

**Bu Rehberde Kullanılan Sürüm**

- 5.06

**Lisans**

- Ücretsiz Yazılım

**Bu bölümün güncellendiği tarih**

- Ağustos 2014

**Gerekli Okumalar**

**Nasıl Yapmalı** kitapçığı, [**6. Hassas bilgiler nasıl imha edilir**](/tr/chapter-6) bölümü

**Buradan sağlıyacağınız faydalar**:

- Etkinliklerinizin ve bilgisayarınıza geçici olarak kaydedilmiş belgelerin izlerini kalıcı olarak silebilmek
- Bilgisayarınıza bağlı disklerdeki boş alanları temizleyebilmek
- Windows Kayıt Defterini temizleyebilmek
- Bilgisayarınız başladığında hangi programların açılacağını kontrol edebilmek 

**GNU Linux, Mac OS ve Microsoft Windows ile çalışan diğer programlar**

**GNU Linux** ve **Microsoft Windows** ile uyumlu başka bir geçici dosya silici ve yok edici program,  [**BleachBit'tir**](http://bleachbit.sourceforge.net/). **BleachBit**, 70 popüler uygulamanın geçici dosyalarını, işletim sisteminizin geçici dosyalarını ve hard diskinizdeki geçici dosyaları silmenize olanak verir. Taşınabilir versiyonu bulunan bir açık kaynak program olan **BleachBit**, 32 dilde kullanıma hazırdır. 

**CCleaner’in Mac OS** ile uyumlu bir versiyonu da bulunur. Fakat kullanıcılar, çalışma oturumlarının izlerini silmek için **Titanium’s Software'den, OnyX** ve **Maintenance**](http://www.titanium.free.fr/) gibi ücretsiz araçları da tercih edebilirler. *Çöp Kutunuzu* güvenli bir şekilde temizlemek için, *Bul* menüsünü açın ve *Bul > Çöp Kutusunu güvenli boşalt’ı* **seçin**. *Çöp kutunuzu* her zaman güvenli bir şekilde boşaltmak için, *Bul  > Tercihler’i* **seçin** ve *Gelişmiş* sekmesine **tıklayın**. *Çöp kutusunu güvenli boşalt* seçeneğini seçin. Diskteki boş bölümü temizlemek için, *Disk Yardımcı Programı* sistem uygulamasını **çalıştırın**, disk bölmesini **seçin**, *Sil* sekmesini **seçin** ve *Boş Alanı Sil* düğmesine **tıklayın**. 

## 1.1 Başlamadan once bu araçla ilgili bilmeniz gerekenler ##

Bilgisayar sisteminizde veya bir İnternet tarayıcındaki verili ayarlar, otomatik olarak, bu konuda bilgili olan ve kötü amaçlı tarafların takip edebileceği bir veri izi yaratır. Her İnternet tarayıcısı veya sözcük işlemcisi veya programı kullandığınızda, bilgisayar siteminize geçici veriler ve dosyalar kaydeder. En son görülmüş belge ve web sayfalarının listesini de oluşturabilir. Örneğin, İnternet tarayıcınıza herhangi bir web adresi yazdığınız zaman, o harflerle başlayan diğer adreslerin listesini, aşağıda göründüğü gibi gösterir:

![](/sbox/screen/ccleaner-tr/00.png)

*Şekil 1: Farklı URL'leri gösteren bir İnternet tarayıcısı adres çubuğu*

Tarama geçmişleri bazı durumlarda işe yarasa da, gezmiş olduğunuz web sitelerinin tespit edilmesine neden olabilir. Ayrıca, bu web sitelerinde görünen imajlar veya e-posta adresleri ve İnternet forumlarına girilmiş olan bilgiler aracılığıyla, aktivitelerinizin tespit edilmesine yarayabilecek geçici bir veri tabanı oluşturur. 

Bir programı her kullanışınızda oluşan geçici verileri ortadan kaldırmak için, ger programın kendi dizinini açmanız ve program dosyalarını manuel olarak seçip silmeniz gerekir. **CCleaner** size bu programların listesini sunar ve silmek istediğiniz geçici dosyalara sahip olan programları seçmenizi sağlar. 

**Önemli**: **CCleaner**, bilgisayarınıza kaydedilmiş gerçek dosyalara dokunmadan sadece geçici dosyaları siler fakat yine de belgelerinizin düzenli olarak yedeklemenizi **şiddetle tavsiye ederiz** (yedekleme konusunda daha fazla bilgi için lütfen Nasıl Yapmalı kitapçığı*nın, [**5. Veri kayıpları nasıl kurtarılır**](/tr/chapter-5) bölümüne bakın).

**CCleaner’ı** çalıştırdıktan sonra tüm tarayıcı ve yakın tarihli belge geçmişinizi kaybedebilirsiniz. Bu da bu programın amacıdır, bu program bilgisayar sisteminizin maruz kaldığı virüs ve kontrol mekanizmalarını minimuma indirir. 

