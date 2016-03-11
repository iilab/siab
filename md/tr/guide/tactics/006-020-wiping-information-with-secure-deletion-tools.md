

---

lang: tr
community: guide
type: tactics
legacy: True
child: True
weight: 2
depth: 3
title: Wiping information with secure deletion tools

---

Bu bölümde tavsiye edilenler gibi güvenli bir silme aracı kullandığınızda, hassas bilgilerinizi basitçe silmek yerine bu bilgileri bir başkasıyla değiştirdiğinizi ya da bu bilgilerin ‘üzerine yazmış’ olduğunuzu söylemek daha doğru olacaktır. Yukarıda varsayılan dosya dolabında saklanan belgelerin kurşun kalemle yazılmış olduğunu hayal edecek olursanız, güvenli silme yazılımı sadece içeriği silmekle kalmaz ayrıca her sözcüğün üzerini de karalar. Ve kurşun kalem izi gibi, dijital bilgiler de silinseler ve üzerlerine başka bir şey yazılsa bile, her ne kadar az da olsa, okunabilir. Bu nedenle burada tavsiye edilen araçlar gelişigüzel seçilen verilerle dosyaların üzerine defalarca yazar. Bu işlem,  [*kalıcı silme işlemi*](/tr/glossary#Wiping) ([*wiping*](/tr/glossary#Wiping)) olarak adlandırılır ve bilginin üzerine ne kadar çok yazılırsa birinin özgün içeriği kurtarması da o kadar güçleşir. Uzmanlar genellikle üç ve daha fazla yazma işleminin yapılması gerektiği konusunda hemfikirdir; bazı standartlar ise yedi ve daha fazlasını gerektirir. [*Kalıcı silme*](/tr/glossary#Wiping) yazılımı, otomatik olarak bilginin üzerine makul bir sayıda yazma işlemi yapar ama istediğiniz takdirde bu sayıyı değiştirebilirsiniz.

### Dosyaları kalıcı olarak silmek ### 

Sabit diskinizden ya da depolama aygıtınızdan hassas verilerinize [*kalıcı silme işlemi*](/tr/glossary#Wiping) uygulamanın iki genel yolu vardır. Tek bir dosyaya ya da diskteki 'atanmamış' alanın tamamına [*kalıcı silme işlemi*](/tr/glossary#Wiping) uygulayabilirsiniz. Bu kararı verirken daha önce önerilen diğer varsayımsal örnekleri (uzun raporunuz hazırlanırken her ne kadar sadece bir dosya görünür halde olsa da dosyanın birçok tamamlanmamış kopyasının sabit diskinizin çeşitli yerlerine bırakılmış olabileceği gibi) düşünmeniz yararlı olur. Dosyanın kendisine [*kalıcı silme işlemi*](/tr/glossary#Wiping) uygularsanız, son sürümünü ortadan kaldırdığınızdan emin olabilirsiniz ama diğer kopyaları oldukları yerde bırakmış olursunuz. Aslında bu kopyaları doğrudan hedef almanın bir yolu yoktur çünkü özel bir program kullanılmadığı sürece görünür değillerdir. Bununla beraber depolama aygıtınızdaki tüm boş alana [*kalıcı silme işlemi*](/tr/glossary#Wiping) uygulayarak tüm önceden silinmiş bilgilerin yok edilmesini güvence altına alırsınız. Kötü etiketlenmiş dosya dolabı metaforuna dönersek, bu işlem dolabın tamamını aramaktan ziyade etiketleri çoktan çıkarılmış herhangi bir belgenin üzerini tekrar tekrar silmek ve yeniden yazmakla karşılaştırılabilir.

[*Eraser*](/tr/glossary#Eraser) üceretsiz, kullanması oldukça kolay açık kaynak kodlu bir güvenli silme aracıdır. [*Eraser*](/tr/glossary#Eraser) ile dosyalara üç farklı şekilde [*kalıcı silme işlemi*](/tr/glossary#Wiping) uygulayabilirsiniz:  bir dosyayı seçerek, Geri Dönüşüm Kutusu’nun içeriğini seçerek ya da diskteki ‘atanmamış’ alanın tamamına [*kalıcı silme işlemi*](/tr/glossary#Wiping) uygulayarak. [*Eraser*](/tr/glossary#Eraser) ayrıca aşağıda ele alınan Windows’un  [*swap dosyalarının*](/tr/glossary#Swap_file) içeriğine de [*kalıcı silme işlemi*](/tr/glossary#Wiping) uygulayabilir.

<div class="getstarted" markdown="1">
Uygulama: [*Eraser - Güvenli Dosya Kaldırma Rehberi*](/en/eraser_main) ile uygulamaya başlayın
</div>

Güvenli silme araçları, görünür dosyalarınıza özel olarak [*kalıcı silme işlemi*](/tr/glossary#Wiping) uygulamadığınız sürece bu dosyalara zarar vermez; ancak yine de bu tür yazılımları kullanırken tedbirli olmak önemlidir. Her şeye rağmen kazalar olabilmektedir; insanların **Geri Dönüşüm Kutularını** ve veri kurtarma araçlarını faydalı bulmalarının nedeni de budur. Bir şeyleri sildiğiniz her seferinde verilerinize [*kalıcı silme işlemi*](/tr/glossary#Wiping) uygulamayı alışkanlık haline getirdiyseniz kendinizi basit bir hatadan kurtaramaz durumda bulabilirsiniz. Bilgisayarınızdan büyük miktarda veriye [*kalıcı silme işlemi*](/tr/glossary#Wiping) uygulamadan önce güvenli bir yedeklemeye sahip olduğunuzdan daima emin olun.

<div class="background" markdown="1">
Elena: Microsoft Word ve Open Office gibi kelime işlemci programların, üzerinde çalıştığınız dosyanın zaman zaman geçici kopyalarını oluşturduğunu biliyorum. Diğer programlar da bunu yapıyor mu ya da sadece kendi oluşturduğum ve sildiğim dosyalar için mi endişelenmeliyim?

Nikolai: Aslında programların kişisel verilerinin ve çevrimiçi etkinliklerinin izlerini bilgisayarında bıraktıkları birçok yer vardır. Ziyaret ettiğin web sitelerinden, kısa bir süre önce üzerinde çalıştığın taslak e-postalarından ve buna benzer şeylerden söz ediyorum. Tüm bunlar o bilgisayarı hangi sıklıkla kullandığına bağlı olarak hassas bilgiler olabilir.
</div>

### Geçici verileri kalıcı olarak silmek ###

[*Eraser*](/tr/glossary#Eraser)’ın sabit diskinizdeki tüm atanmamış alana [*kalıcı silme işlemi*](/tr/glossary#Wiping) uygulamanıza izin veren özelliği göründüğü kadar riskli değildir çünkü [*Eraser*](/tr/glossary#Eraser) sadece daha önceden silinmiş içeriği [*kalıcı olarak siler*](/tr/glossary#Wiping). Normal, görünür dosyalar etkilenmeyecektir. Diğer yandan bu olgu ayrı bir sorunu aydınlatmaya hizmet eder: [*Eraser*](/tr/glossary#Eraser) silinmemiş ama oldukça iyi gizlenmiş hassas bilgilerinizin temizlenmesine yardım edemeyecektir. Bu tür verileri içeren dosyalar, muğlak klasörlere tıkılmış olabilir ya da anlamsız dosya adlarıyla depolanmış olabilir. Bu, elektronik belgeler için önemli bir sorun değildir ama bilgisayarınızı her kullandığınızda otomatik olarak biriken bilgiler için oldukça önemli olabilir. Örnekler şunlardır:

- Web sayfalarını gösterirken tarayıcınız tarafından kaydedilen metinleri, resimleri, [*çerezleri*](/tr/glossary#Cookie) ([*cookies*](/tr/glossary#Cookie)), hesap bilgilerini, çevrimiçi formları tamamlamak için kullanılan kişisel verileri ve ziyaret ettiğiniz sitelerden oluşan geçmişi de içeren geçici veriler.
- Yaptığınız işi kaydetmeden bilgisayarınızın çökmesi durumunda işlerinizi kurtarmanıza yardım etmek için çeşitli uygulamalar tarafından kaydedilen geçici dosyalar.  Bu dosyalar diğer potansiyel olarak hassas bilgilerin yanı sıra metinleri, resimleri, tablo verilerini ve diğer dosyaların adlarını içerebilir.
- Kolaylık adına Windows tarafından saklanan dosyalar ve bağlantılar; örneğin, yakın zamanda kullandığınız uygulamalara kısayollar, gizli kalmasını tercih edebileceğiniz klasör bağlantıları ve elbette boşaltmayı unuttuğunuz <b>Geri Dönüşüm Kutusu’nun<b> içeriği.
- Windows [*swap dosyası*](/tr/glossary#Swap_file). Bilgisayarınızın hafızası dolduğunda, örneğin eski bir bilgisayarda aynı anda birçok programı çalıştığınızda olduğu gibi, Windows verilerinizi [*swap dosyası*](/tr/glossary#Swap_file) adı verilen tek bir geniş dosyaya zaman zaman kopyalar. Sonuç olarak bu dosya, web sayfaları, dosya içerikleri, şifreler ve şifrelenmiş dosyalar dahil, hemen hemen her şeyi içerebilir. Bilgisayarınızı kapattığınız zaman bile [*swap dosyası*](/tr/glossary#Swap_file) ortadan kaldırılmaz, bu nedenle onu siz silmelisiniz.

Sıkça rastlanan geçici dosyaları bilgisayarınızdan silmek için CCleaner olarak adlandırılan ücretsiz bir aracı kullanabilirsiniz. [*CCleaner*](/tr/glossary#CCleaner), her biri potansiyel olarak hassas bilgileri açığa çıkardığı bilinen Internet Explorer, Mozilla [*Firefox*](/tr/glossary#Firefox) ve Microsoft Office uygulamaları gibi yazılımların kullanımı sonrasında bilgisayarınızın temizlenmesi için tasarlanmıştır. Bu araç ayrıca Windows’un kendisini de temizler. [*CCleaner*](/tr/glossary#CCleaner) her çalıştırılmadan sonra dosyalarınızı güvenle silme becerisine sahiptir. Böylece, sabit diskinizdeki atanmamış alana [*Eraser*](/tr/glossary#Eraser) kullanarak [*kalıcı silme işlemi*](/tr/glossary#Wiping) uygulamak zorunluluğundan sizi kurtarır.

<div class="getstarted" markdown="1">
Uygulama: [*CCleaner  - Güvenli Dosya Silimi ve Bilgisayar Kullanım Geçmişinin <br>Kalıcı Olarak Silinmesi Rehberi*](/en/ccleaner_main) ile uygulamaya başlayın
</div>

