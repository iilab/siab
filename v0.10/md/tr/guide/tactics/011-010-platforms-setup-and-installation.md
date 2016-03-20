

---

lang: tr
community: guide
type: tactics
legacy: True
child: True
weight: 1
depth: 3
title: Platforms, Setup and Installation

---

### Platformlar ve İşletim Sistemleri ###

Bu kitabın yazımı sırasında kullanımdaki en yaygın akıllı telefonlar Apple'ın iPhone’u, Google'ın Android’i ve onları Blackberry ve Windows Phone izliyor. Android ve diğer işletim sistemleri arasındaki en önemli farklılık Andoid’in, çoğu zaman, Açık Kaynak Kodlu ([*FOSS*](/tr/Glossary#FOSS)) bir sistem, yani kullanıcının bilgilerini ve iletişimini düzgün bir biçimde koruyup korumadığını doğrulamak için bağımsız olarak denetlemeye izin veren bir işletim sistemi olmasıdır. Bu işletim sistemi ayrıca bu platform için güvenlik uygulamalarının geliştirilmesini de kolaylaştırır. Güvenlik farkındalığına sahip birçok programcı, kullanıcı güvenliğini göz önünde bulundurarak Android uygulamaları geliştirir. Bölümün ilerleyen kısımlarında bunlardan bazılarının üzerinde durulacaktır. 

Kullandığınız akıllı telefonun türü ne olursa olsun, internete bağlanan ve [*GPS*](/tr/glossary#GPS) ya da kablosuz internet kapasitesi gibi özellikleri beraberinde taşıyan bir telefonu kullanırken farkında olmanız gereken sorunlar vardır. Bu bölümde Android platformlu araçlar üzerine odaklanacağız, çünkü yukarıda da belirttiğimiz gibi, Android platformlu araçlarda veri ve iletişimi korumak daha kolaydır. Bununla birlikte, bu bölümde temel kurma rehberleri ve Android telefonlarından farklı araçların bazı uygulamaları da verilecektir.

Blackberry telefonları ‘güvenli’ mesajlaşma ve e-posta araçları olarak sunulmuştu. Bunun nedeni mesajların ve e-postaların, potansiyel kulak misafirlerinin erişimine engel olacak şekilde, Blackberry sunucuları aracılığıyla güvenli bir biçimde aktarılmasıydı. Ne yazık ki, hükümetler, potansiyel terörizme ve örgütlü suça karşı güvenlik gereksinimine vurgu yaparak, gittikçe daha çok bu iletişim bilgilerine erişim talep etmektedir. Hindistan, Birleşik Arap Emirliği, Sudi Arabistan ve Lübnan, Blackberry araçlarının kullanımını inceleyen ve ülkelerindeki kullanıcıların bilgilerini talep eden hükümetlerden birkaçıdır.

### Eski Nesil Cep Telefonları ###

Cep telefonlarının bir başka kategorisi sık sık ‘Eski Nesil Cep Telefonları’ olarak adlandırılır (örneğin, Nokia 7705 Twist ya da Samsung Rogue). Kısa bir süre önce eski nesil cep telefonları bazı akıllı telefonlarınkileri de içerecek şekilde işlevlerini arttırdı. Ancak genel olarak bu telefonların işletim sistemleri daha az erişilebilirdir ve bu nedenle de güvenlik uygulamaları ve geliştirme için var olan olanaklar sınırlıdır. Her ne kadar burada ele aldığımız önlemler bu tür telefonlar için de anlamlı olsa da, eski nesil cep telefonlarına özel olarak atıfta bulunmayacağız.

### Operatör markalı ve kilitlenmiş akıllı telefonlar ###

Akıllı telefonlar genellikle operatör markalı ya da kilitlenmiş olarak satılır. Akıllı telefonları kilitlemek şu anlama gelir: cihaz tek bir taşıyıcıyla işletilebilir ve bu taşıyıcı, cihazı aldığınızda beraberinde gelen SIM karttır. Taşınabilir ağ operatörleri kendi donanım yazılımını ya da yazılımını yükleyerek bir telefonu üretir ve markalaştırır. Ayrıca bazı işlevleri çalıştırılamaz kılabilir ya da başkalarını ekleyebilirler. Markalaştırma, şirketlerin akıllı telefon kullanımınızı yönlendirerek, çoğu zaman da telefonunuzu nasıl kullandığınız hakkında veri toplayarak ya da akıllı telefonunuza uzaktan erişimi mümkün kılarak gelir arttırmak için kullanılan bir araçtır.

Bu nedenlerden dolayı, mümkünse operatör markasız akıllı telefon almanızı tavsiye ediyoruz. Kilitlenmiş bir telefon, tüm verilerinizi, veri akışlarınızı merkezileştiren tek bir taşıyıcıya yönlendirildiğinden ve verileri farklı taşıyıcılar üzerinden dağıtmak için SIM kartlarını değiştirmeyi olanaksız kıldığından daha yüksek bir risk kaynağıdır. Telefonunuz kilitlenmiş ise güvendiğiniz birinden onun kilidini açmasını isteyin.

### Genel Kurulum ###

Akıllı telefonların aracın güvenliğini kontrol eden birçok ayarı vardır. Akıllı telefonunuzun nasıl kurulduğuna dikkat etmeniz önemlidir. Aşağıdaki Uygulama Rehberleri’nde sizi bazı akıllı telefon güvenlik ayarları konusunda uyaracağız. Öyle ki bazı akıllı telefonların güvenlik ayarları bulunsa da bunlar öntanımlı olarak aktif değildir. Yahut bazı akıllı telefonlarda bu güvenlik ayarları öntanımlı olarak aktiftir ve telefonunuzu korumasız hale getirir.

<div class=getstarted markdown=1>
Uygulama: [*Android için Temel Kurulum Rehberi*](/en/android_basic) ile uygulamaya başlayın
</div>


### Uygulamaları kurmak ve güncellemek ###

Akıllı telefonunuza yeni yazılım yüklemenin alışılagelmiş yolu, iPhone Appstore’a ya da Google Play store’a kullanıcı kimlik bilgileriyle giriş yapmak ve istediğiniz uygulamayı indirerek kurmaktır. Giriş yaparak, kullanıcı hesabınızı çevrimiçi dükkânı kullanmanızla ilişkilendirmiş olursunuz. Uygulama dükkânının sahipleri, kullanıcının tarama geçmişinin ve uygulama tercihlerinin kayıtlarını tutar.

Resmî  çevrimiçi dükkânlarda sunulan uygulamalar, varsayımsal olarak, dükkân sahiplerince (Google ya da Apple) onaylanmışlardır ama gerçekte bu onaylama, uygulamanın telefonunuza kurulduktan sonra neler yapacağına karşı çok zayıf bir güvence sağlar. Örneğin bazı uygulamalar telefonunuza kurulduktan sonra adres defterinizi kopyalar ve dışarıya gönderir. Android telefonlar, her uygulama kurulumu aşamasında, bu uygulamalar kullanılırken nelere izin verildiğini size onaylatmak zorundadır. Hangi izinlerin istendiğine ve bu izinlerin kurmakta olduğunuz uygulamanın işleviyle anlamlı bir uyum içerisinde olup olmadığına çok dikkat etmelisiniz. Örneğin bir “haber okuma” uygulaması kurmayı düşünüyorsanız ve bu uygulamanın kişiler listenizi, taşınabilir veri bağlantısı üzerinden üçüncü kişilere gönderme hakkını talep ettiğini fark ederseniz, uygun erişim ve haklara sahip başka bir uygulama aramalısınız.

Android uygulamaları resmî Google kanalları dışındaki kaynaklarda da sunulmaktadır. Bu indirme sitelerini kullanmak için tek yapmanız gereken *Güvenlik ayarları*’nızdaki *Bilinmeyen Kaynaklar* kutusunu işaretlemenizdir. Bazı kullanıcılar Google’la çevrimiçi teması asgariye indirmek için bu alternatif siteleri gözden geçirmek isteyebilir. Alternatif dükkânlardan bir tanesi, sadece [*FOSS*](/tr/glossary#FOSS) uygulamaları sunan [**F-Droid**](http://f-droid.org)’dir ('Free Droid'). Ayrıca bir siteden herhangi bir uygulama indirmeden önce ona güveniyor olmanız gerektiğini lütfen hatırlayın. Deneyimsiz kullanıcılar için Google Play dükkânını kullanmalarını tavsiye ederiz.

Uygulamalara erişmek için çevrimiçi olmak istemiyorsanız, uygulamaları başkalarının telefonundan Bluetooth aracılığıyla [*.apk*](/tr/glossary#apk) (‘android uygulama paketi’nin kısaltılmış hali) dosyalarını göndererek aktarabilirsiniz. Alternatif olarak .apk dosyalarını aracınızın Micro SD kartına indirebilir ya da bir usb kablo ile bir PC’den karta aktarabilirsiniz. Dosyaları aldıktan sonra dosya adına uzun süre tıkladığınızda uygulamayı kurmak için uyarılacaksınız. (**Not**: özellikle bluetooth kullanırken dikkatli olun - [***10. Bölüm***](/tr/chapter-10)’deki [***Sesli iletişim ve mesajlaşmanın ötesindeki işlevler***](/tr/chapter_10_2_4) kısmını okuyun).

