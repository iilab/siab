

---

lang: tr
community: guide
type: tactics
legacy: True
child: True
weight: 2
depth: 3
title: Communicating (Voice and Messages) via Smartphone

---

## Güvenle Konuşmak ##

### Temel Telefon işlevi ###

[***Cep telefonları nasıl olabildiğince güvenli kullanılır***](/tr/chapter-10) başlıklı [***10. Bölüm***](/tr/chapter-10)’ün [***Temel işlevler, takip edilebilirlik ve anonimlik***](/tr/chapter_10_2_2) kısmında sesli iletişim için cep telefonu operatör ağını kullanırken dinlenmeniz riskini en aza indirmek için düşünmeniz gereken farklı önlemleri tartışmıştık.

Akıllı telefonunuz aracılığıyla, taşınabilir veri bağlantıları ya da WiFi üzerinden interneti kullanmak, iletişim için daha güvenli yollar sağlayabilir; örneğin VoIP kullanmak ve bu iletişim kanalını güvenli hale getirmek için gerekli araçlara başvurmak gibi... Bazı akıllı telefon araçları bu güvenliği [*VoIP*](/tr/Glossary#VoIP)’in bile ötesine, cep telefonu görüşmelerine de taşıyabilir (bakınız aşağıda **Redphone**).

Burada birkaç aracı ve onların olumlu ve olumsuz yanlarını listeliyoruz:

### Skype ###

En popüler ticari VoIP uygulaması olan [*Skype*](/tr/glossary#skype), tüm akıllı telefon platformları için kullanılabilirdir ve kablosuz bağlantınız güvenilirse iyi de işlemektedir. Taşınabilir veri bağlantılarında Skype daha az güvenilirdir.

[***İnternet iletişiminizin gizliliği nasıl korunur***](/tr/chapter-7) başlıklı [***7. Bölüm***](/tr/chapter-7)’ün [***Diğer internet iletişim araçlarını güvenli kılmak***](/tr/chapter_7_3) kısmında Skype kullanmanın risklerini ve mümkünse neden kullanmaktan kaçınmak gerektiğini ele almıştık. Özet olarak Skype Açık Kaynak Kodlu bir yazılım değildir ve bu, Skype’ın güvenlik düzeyini bağımsız olarak sınamayı güçleştirir. Dahası Skype, onu ne zaman ve nereden kullandığınızı bilmekte ticarî çıkarları olan Microsoft’a aittir. Skype yasa uygulayıcı makamların tüm iletişim geçmişinize geriye dönük olarak erişimine izin de verebilir.

### Diğer VoIP ###

VoIP’i kullanmak genel olarak ücretsizdir (ya da cep telefonlarıyla arama yapmaktan çok daha ucuzdur) ve çok az veri izi bırakır. Gerçekten de güvenli kılınmış bir VoIP konuşması en güvenli iletişim yolu olabilir.

Farklı VoIP hizmetleri için basit kurma sihirbazlarıyla birlikte sunulan, [**CSipSimple**](http://f-droid.org/repository/browse/?fdid=com.csipsimple&fdpage=4), Android telefonlar için iyi ve güçlü bir VoIP programıdır.

[**Open Secure Telephony Network (OSTN)**](https://guardianproject.info/wiki/OSTN) ve Guardian projesi tarafından sağlanan bir sunucu olan [**ostel.me**](https://ostel.me), günümüzde sesli olarak iletişimin en güvenli araçlarından birini sunmaktadır. VoIP iletişimleriniz için sunucu işleten kuruluşu bilmek ve güvenmek ciddi bir değerlendirmeyi gerektirir.

CSipSimple kullanırken hiçbir zaman doğrudan iletişim partnerinizle iletişim kurmazsınız, bunun yerine tüm verileriniz Ostel sunucusu aracılığıyla yönlendirilir. Bu, verilerinizin izini sürmeyi ve kimle görüştüğünüzü bulmayı güçleştirir. Dahası Ostel, giriş yapmanız için gerekli olan hesap bilgileriniz dışında hiçbir veriyi elinde tutmaz. Tüm konuşmanız güvenli bir biçimde şifrelenir ve hatta gizlemesi oldukça zor olan meta verileriniz bile, trafik ostel.me sunucusu aracılığıyla iletildiğinden, okunması güç hale gelir. CSipSimple’ı ostel.me sitesinden indirirseniz, programınız ostel.me’yle kullanılmak üzere önceden düzenlenmiş olarak gelecektir; bu da uygulamanın kurulumunu ve kullanımını oldukça kolaylaştırmaktadır.

[**RedPhone**](https://play.google.com/store/apps/details?id=org.thoughtcrime.redphone), bu uygulamayı işleten iki araç arasında gönderilen sesli iletişim verilerini şifreleyen, ücretsiz ve Açık Kaynak Kodlu bir yazılımdır. Program kendisini normal arama ve kişiler şemanızla bütünleştirdiğinden kurulumu ve kullanımı oldukça kolaydır. Ama konuşmak istediğiniz kişilerin de RedPhone’u kurmuş ve kullanıyor olması gerekir. Kullanım kolaylığı için RedPhone, tanımlayıcınız olarak (diğer VoIP servislerinde kullanıcı adı gibi) sizin cep numaranızı kullanır. Ancak bu nedenle Redphone’un ürettiği trafiği çözümlemek ve cep numaranız aracılığıyla size kadar izini sürmek çok daha kolay hale gelir. RedPhone merkezî bir sunucu kullanmaktadır, ki bu bir merkezîleşme sorunudur ve böylece RedPhone’u güçlü bir konuma (bu verilerin üzerinde denetim sahibi olma konumuna) getirir.

CSipSimple, Ostel.me ve Redphone için Uygulama Rehberleri hazırlanmaktadır. Daha fazla bilgiye yukarıdaki bağlantıları takip ederek ulaşabilirsiniz.

## Güvenli Mesaj Gönderme ##

Akıllı telefonunuzla SMS gönderirken, anlık mesajlaşma ya da sohbet programları kullanırken bazı önlemler almalısınız.

### SMS ###

[***10. Bölüm***](/tr/chapter-10)’de ([***Yazılı iletişim***](/tr/chapter_10_2_3) kısmında) betimlendiği gibi, SMS iletişimi standart olarak güvenli değildir. Taşınabilir telekomünikasyon ağına erişimi olan herkes bu mesajları kolayca ele geçirebilir ve bu, birçok durumda her gün meydana gelen bir şeydir. Kritik durumlarda güvenli olmayan SMS mesajı göndermeye güvenmeyin. SMS mesajlarının sahiciliğini kanıtlamanın hiçbir yolu yoktur bu nedenle SMS’in gönderimi aşamasında mesajın içeriğinin değiştirilip değiştirilmediğini ya da mesajı gönderen kişinin olduğunu iddia ettiği kişi olup olmadığını bilmek mümkün değildir.

### SMS’leri Güvenli Kılmak ###

[**TextSecure**](https://play.google.com/store/apps/details?id=org.thoughtcrime.securesms) Android telefonlar için güvenli SMS gönderimi ve alımı için tasarlanmış bir [*FOSS*](/tr/glossary#FOSS) aracıdır. Hem şifrelenmiş hem de şifrelenmemiş mesajlarla çalıştığından bu uygulamayı standart SMS uygulamanız olarak kullanabilirsiniz. Şifrelenmiş mesajları alıp vermek için, bu araç hem göndericide hem de mesajın alıcısında kurulu olmalıdır. Bu nedenle düzenli olarak iletişim içinde olduğunuz kişilerin de bu uygulamayı edinmesini sağlamanız gerekir. TextSecure bir başka TextSecure kullanıcısından şifreli bir mesaj aldığını otomatik anlar. Ayrıca birden fazla kişiye şifreli mesaj göndermenize izin verir. Mesajlar, mesajın içeriğine zarar verilmesini neredeyse olanaksız kılarak, otomatik olarak imzalanır. TextSecure Uygulama Rehberi’nde bu aracın özellikleri ve nasıl kullanılacağı detaylı bir şekilde açıklanmıştır.

<div class=getstarted markdown=1>
Uygulama: [*TextSecure Rehberi*](/en/textsecure_main) ile uygulamaya başlayın     
</div>

### Güvenli Çevrimiçi Sohbet ###

Telefonunuzla anlık mesajlaşma ve çevrimiçi sohbet, dinlenme riski taşıyan birçok bilgi üretebilir. Bu haberleşmeler düşmanlarınız tarafından ileriki bir tarihte size karşı kullanılabilir. Bu nedenle anlık mesajlaşma ve çevrimiçi sohbet sırasında telefonunuza yazarken neleri ifşa ettiğiniz konusunda son derece şüpheci olmalısınız.

Güvenli çevrimiçi sohbet ve anlık mesajlaşma yolları vardır. Bunun en iyi yolu diğer uçtaki kişinin mesajlaşmak istediğiniz kişi olduğundan emin olmanızı sağlayan uçtan uca şifrelemedir.

Biz Android telefonlar için güvenli bir yazılı sohbet uygulaması olan [**Gibberbot**](https://guardianproject.info/apps/gibber/)’u tavsiye ediyoruz. Gibberbot [*Off-the-Record*](/tr/glossary#OTR) Mesajlaşma protokolüyle birlikte sohbetini için basit ve güçlü bir şifreleme sunar. Bu şifreleme, hem kimlik doğrulama özelliği (doğru kişiyle sohbet ettiğinizi doğrulayabilirsiniz)  hem de her seans için bağımsız güvenlik sunar, öyle ki bir sohbet seansının şifrelemesinin gizliği ihlal edilse bile geçmiş ve gelecek seanslar güvenli olarak kalacaktır.

Gibberbot, Orbot’la birlikte çalışacak şekilde tasarlanmıştır. Böylece çevrimiçi sohbet mesajlarınız [*Tor*](/tr/glossary#Tor) anonimleştirici ağından yönlendirilebilir. Bu, mesajlarınızın izini sürmeyi ya da çevrimiçi sohbetin gerçekleştiğini bile anlamayı oldukça güçleştirir.

<div class=getstarted markdown=1>
Uygulama: [*Gibberbot Rehberi*](/en/gibberbot_main) ile uygulamaya başlayın
</div>

[**ChatSecure**](https://chatsecure.org) uygulaması, iPhone’lar için de aynı özellikleri sunar ancak onu [*Tor*](/tr/glossary#Tor) ağıyla birlikte kullanmak kolay değildir.

ChatSecure için bir Uygulama Rehberi hazırlanmaktadır. Bu arada ChatSecure’ün [anasayfasında](https://chatsecure.org) daha fazla bilgi bulunabilir. 

Hangi uygulamayı kullanırsanız kullanın çevrimiçi sohbet için hangi hesabı kullanacağınızı daima göz önünde bulundurun. Örneğin Google Talk kullandığınızda, kimliğiniz ve sohbet seansının zamanı Google için bilinir hale gelir. Ayrıca görüştüğünüz kişilerle, sohbet geçmişini, özellikle şifrelenmemişse, kaydetmemek üzere anlaşın.

