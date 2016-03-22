

---

lang: tr
community: guide
type: tactics
legacy: True
child: True
weight: 1
depth: 3
title: Securing your email

---

E-posta iletişiminizin güvenliğini arttırmak için atabileceğiniz birkaç önemli adım vardır. Bunlardan ilki verili bir mesajı sadece gönderdiğiniz kişinin okuyabileceğinden emin olmaktır. Bunlar, aşağıda [*Webmail’inizin gizliliğini korumak*](/tr/chapter_7_1#Keeping_your_webmail_private) ve [*Daha güvenli bir e-posta hesabına geçmek*](/tr/chapter_7_1#Switching_to_a_more_secure_email_account) kısımlarında ele alındı. Başlangıç düzeyinin ötesine geçecek olursak, e-posta alıcılarınızın, belirli bir mesajın sizmişsiniz gibi yapan birinden değil de gerçekten sizden geldiğini doğrulayabilmeleri kimi zaman yaşamsal öneme haizdir. Bunu yapmanın bir yolu, [*İleri düzey e-posta güvenliği*](/tr/chapter_7_4)’nin [*Bir mesajı şifrelemek ve kimliğini doğrulamak*](/tr/chapter_7_4#Encrypting_and_authenticating_individual_email_messages) kısmında, ele alınmıştır.

E-posta hesabınızın gizliliğinin ihlal edildiğini düşündüğünüzde ne yapmanız gerektiğini de bilmelisiniz. [*E-postaların izlendiğinden şüphe edildiğinde yapabilecekleriniz üzerine ipuçları*](/tr/chapter_7_2) kısmı bu soruya işaret etmektedir.

Yazdığınız her şey bir casus yazılımla kaydediyor ve düzenli olarak internet üzerinden üçüncü kişilere gönderiliyorsa güvenli e-postanın size bir faydasının olmayacağını da hatırlayın. [*Bilgisayarınızı kötü amaçlı yazılımlara ve hacker'lara karşı nasıl korursunuz*](/tr/chapter-1) başlıklı [*1. Bölüm*](/tr/chapter-1) bu tür bir şeyden kaçınmak için bazı tavsiyeler sunmaktadır ve [*Güvenli şifreler nasıl oluşturulur ve muhafaza edilir*](/tr/chapter-3) başlıklı [*3. Bölüm*](/tr/chapter-3), aşağıda ele alınan e-posta ve anlık mesajlaşma araçları için hesaplarınızı korumanıza yardım edecektir.

### Webmail’inizin gizliliğini korumak ###

İnternet açık bir ağdır ve bu ağ aracılığıyla bilgi okunabilir bir formatta yolculuk eder. Normal bir e-posta mesajı, alıcısına doğru giderken ele geçirilirse içeriği kolayca okunabilir. İnternet, trafiği yönlendirmek için aracı bilgisayarlara tabi olan, bütün dünyaya yayılmış bir büyük ağ olduğundan, birçok farklı kişinin bir mesajı ele geçirmek için fırsatı olabilir. *İnternet Servis Sağlayıcınız [*ISP*](/tr/glossary#ISP)*, alıcısına doğru gezintisine başlarken bir e-posta mesajının ilk alıcısıdır. Benzer bir şekilde alıcınızın [*ISP*](/tr/glossary#ISP)’si, mesajınızın teslim edilmeden önceki son durağıdır. Belirli önlemler almazsanız, mesajınız bu noktalardan herhangi birinde ya da bunların arasındaki herhangi bir noktada okunabilir veya değiştirilebilirdir.

<div class="background" markdown="1">
Pablo: Ortaklarımızdan biriyle bütün bunlar hakkında konuştum ve o bana, o ve meslektaşlarının şifresini paylaştıkları bir webmail hesabının ‘Taslaklar’ klasörünün altında önemli mesajlarını kimi zaman kaydettiklerini söyledi. Bu bana garip göründü ama işe yarayabilir mi? Demek istiyorum ki, hiçbir zaman gerçekten gönderilmediğinden, herhangi birinin mesajları okumasını engelleyebilir mi?

Claudia: Bilgisayarında bir e-posta okuduğun her seferinde, okuduğun sadece bir ‘taslak’ bile olsa, onun içeriği sana internet üzerinden gönderilir. Aksi halde okuduğun mail senin ekranında beliremez değil mi? Öyle ki, birileri seni gözetim altına aldıysa sadece e-posta mesajlarını izlemiyordur. Bilgisayarına gelen ve bilgisayarından giden tüm okunabilir bilgiyi tarayabilirler. Bir başka deyişle bu taktik, bu paylaşılan webmail hesabına herkes güvenli bir şekilde bağlanmadığı sürece işlemez. Eğer herkes güvenli bağlanıyorsa zaten ayrı hesaplar oluşturmanın ya da “gönder” düğmesine tıklamanın hiçbir sakıncası yoktur.
</div>

Bilgisayarınız ile ziyaret ettiğiniz web sitesi arasındaki internet bağlantısını güvenli kılmak uzun zamandan beri olanaklı. Web sitelerine şifreler ya da kredi kartı bilgileri girerken bu güvenlik düzeyiyle sık sık karşılaşırsınız. Bunu olanaklı kılan teknoloji, Güvenli Soket Katmanı [*SSL*](/tr/glossary#SSL) [*şifreleme*](/tr/glossary#Encryption) olarak adlandırılır. [*SSL*](/tr/glossary#SSL) kullanıp kullanmadığınızı internet tarayıcınızın **adres çubuğuna** yakından bakarak söyleyebilirsiniz. 

Normalde tüm web adresleri, aşağıdaki örnekte görülebileceği gibi, **HTTP** harfleriyle başlar:

![](/sites/securitybkp.ngoinabox.org/files/u7/01.png)

Güvenli bir web sitesini ziyaret ederken adres **HTTPS** ile başlayacaktır. 

![](/sites/securitybkp.ngoinabox.org/files/u7/02.png)

Sondaki fazladan **S** bilgisayarınızın web sitesine güvenli bir bağlantı açtığını gösterir. Tarayıcı pencerenizin **adres çubuğunda** ya da alttaki **durum çubuğunda** bir ‘kilit’ simgesi de görebilirsiniz. Bunlar, internet bağlantınızı izleyebilen herhangi birinin artık iletişiminizi bu bağlandığınız web sitesi aracılığıyla izleyemeyeceğini bilmenizi sağlayan ipuçlarıdır.

Şifre ve mali işlemlerinizin korunmasına ek olarak bu tip bir [*şifreleme*](/tr/discussion#Encryption), webmail’inizi güvenli kılmak için mükemmeldir. Bununla birlikte birçok webmail hizmet sağlayıcısı güvenli erişim sunmamaktadır ve bazı webmail hizmetleriyse bir seçenek belirterek ya da **HTTPS**’i elle yazarak izin vermenizi talep etmektedir. Siteye giriş yapmadan, e-postanızı okumadan ya da bir mesaj göndermeden önce bağlantınızın güvenli olduğundan daima emin olun.

Güvenli bir webmail hesabına erişmeye çalışırken tarayıcınız aniden geçersiz [*güvenlik sertifikalarından*](/tr/glossary#Security_certificate)  şikâyet etmeye başlarsa dikkatli olmalısınız. Bu, birilerinin mesajlarınızı ele geçirmek için bilgisayarınız ve sunucu arasındaki iletişime müdahale ediyor olduğu anlamına gelebilir. Son olarak hassas bilgi alışverişinde bulunmak için webmail’e başvuracaksanız, tarayıcınızın olabildiğince güvenli olması önemlidir. Mozilla [*Firefox*](/tr/glossary#Firefox)’u ve onun güvenlikle ilgili eklentilerini kurmayı düşünün.

<div class="getstarted" markdown="1">
Uygulama: [*Eklentileriyle Firefox - Güvenli İnternet Tarayıcısı Rehberi*](/en/firefox_main) ile uygulamaya başlayın
</div>			

<div class="background" markdown="1">
Pablo: Bu rapor üzerinde bizimle birlikte çalışacak olanlardan biri iş yerinin dışındayken Yahoo webmail hesabını kullanmayı tercih ediyor. Ve Hotmail kullanan bir başkasını da hatırlar gibiyim. Bu kişilere mesaj gönderirsem başkaları da mesajlarımı okuyabilir mi?

Claudia: Muhtemelen. Yahoo, Hotmail ve diğer birçok webmail hizmet sağlayıcısı, kullanıcı mesajlarının güvenliğini korumayan, güvenli olmayan web sitelerine sahip. Güvenli olarak bu tanıklıkları ele almak istiyorsak bazı kişilerin alışkanlıklarını değiştirmek zorundayız.
</div>		

### Daha güvenli bir e-posta hesabına geçmek ###

Webmail hizmet sağlayıcılarının çok azı e-postanıza [*SSL*](/tr/glossary#SSL) erişimi sunmaktadır. Yahoo ve Hotmail, örneğin, sadece giriş yaptığınızda şifrenizi korumak için güvenli bir bağlantı sunmaktadır ancak mesajlarınızın kendisi güvenli olmayan bir şekilde gönderilir ve alınır. Dahası, Yahoo, Hotmail ve diğer ücretsiz webmail hizmet sağlayıcıları gönderdiğiniz bütün mesajlarınıza kullandığınız bilgisayarın [*IP adresini*](/tr/glossary#IP_address) de ekler.

Öte yandan Gmail hesapları giriş yapmanızdan çıkışınıza kadar güvenli bir bağlantı kullanır. Bunu, sürecin başından sonuna kadar adres çubuğuna bakarak ve URL’nin 'https' ile başladığını ('s' burada güvenli bir bağlantıya işaret etmektedir) gözlemleyerek doğrulayabilirsiniz. Yahoo ya da Hotmail’in aksine Gmail, e-posta alıcılarına [*IP adresinizi*](/tr/glossary#IP_address) açık etmekten kaçınır. Ancak hassas e-posta iletişiminizin gizliliği için tamamen Google’a güvenmeniz tavsiye edilmez. Google çok çeşitli nedenlerle kullanıcılarının mesajlarını tarar ve kaydeder; ve geçmişte dijital özgürlüğü sınırlayan hükümetlerin taleplerini yerine getirmişti. Google'ın gizlilik politikası hakkında daha fazla bilgi için [***Okuma önerileri***](/tr/chapter_7_5) bölümüne bakınız.

Olanaklıysa [*https://mail.riseup.net*](https://mail.riseup.net) adresini ziyaret ederek yeni bir RiseUp e-posta hesabı oluşturmalısınız. [*RiseUp*](/tr/glossary#RiseUp) dünyanın her yerindeki aktivistlere ücretsiz e-posta hizmeti sunmaktadır ve sunucularında kaydedilen bilginin korunması konusunda büyük çaba sarf etmektedir. Onlar uzun zamandan beri güvenli bir e-posta çözümü arayışında olanlar için güvenilir bir kaynak olmuştur. Ve Google’ın aksine kullanıcılarının gizliliği konusunda oldukça katı bir politikaları vardır ve bir gün bu politikalarla çatışabilecek hiçbir ticari çıkarları yoktur. Yeni bir [*RiseUp*](/tr/glossary#RiseUp) hesabı oluşturmak için iki ‘davet kodu’na ihtiyacınız olacaktır. Bu kodlar halihazırda bir [*RiseUp*](/tr/glossary#RiseUp) hesabı olan herhangi biri tarafından verilebilir. Bu kitapçığın basılı bir kopyasına sahipseniz, onunla birlikte ‘davet kodlarınızı’ da almış olmanız gerekir. Aksi halde iki [*RiseUp*](/tr/glossary#RiseUp) kullanıcısı bulmanız ve her birine size bir kod göndermesi için sormanız gerekmektedir.

<div class="getstarted" markdown="1">
Uygulama: [*RiseUp – Güvenli E-posta Hizmeti Rehberi*](/en/riseup_main) ile uygulamaya başlayın</div>	

Hem Gmail hem de [*RiseUp*](/tr/glossary#RiseUp) bir webmail hizmeti sağlayıcısından daha fazlasıdır. Onlar, [***İleri düzey e-posta güvenliği***](/tr/chapter_7_4) başlığı altında betimlenen teknikleri destekleyen Mozilla [*Thunderbird*](/tr/glossary#Thunderbird) gibi bir e-posta istemcisiyle birlikte de kullanılabilir. E-posta istemcinizin e-posta sağlayıcınızla [*şifrelenmiş*](/tr/glossary#Encryption) bir bağlantı yaptığından emin olmak, webmail’inize **HTTPS** ile erişmek kadar önemlidir. Bir e-posta istemcisi kullanıyorsanız ek ayrıntılar için [***Thunderbird Rehberi***](/en/thunderbird_main)’ne bakınız. En azından, hem gelen hem de giden e-posta sunucularınız için [*SSL*](/tr/glossary#SSL)’e ya da [*şifrelemeye*](/tr/glossary#Encryption) izin verdiğinizden emin olun.

<div class="background" markdown="1">
Pablo: Öyle ise RiseUp kullanmaya mı başlamalıyım yoksa sadece güvenli 'https' adresine geçerek Gmail kullanmaya devam edebilir miyim?

Claudia: Bu sana kalmış ama bir e-posta hizmet sağlayıcısı seçerken kesinlikle göz önünde bulundurman gereken birkaç şey var. Birincisi, hesabına güvenli bir bağlantı sunuyor mu? Gmail sunuyor, o zaman Gmail tamam. İkincisi, hizmet yöneticilerinin e-postalarını gizli tutacaklarına ve okumayacaklarına ya da onları başkalarıyla paylaşmayacaklarına güveniyor musun? Buna sen karar vereceksin. Ve son olarak bu sağlayıcıyla özdeşleşmenin kabul edilebilir olup olmadığını düşünmen gerekir. Bir başka deyişle aktivistler arasında popüler olan, sonu ‘riseup.net’le biten bir e-posta adresini kullanman başına iş açar mı yoksa daha yaygın kullanımı olan ‘gmail.com’ adresini kullanmak mı ihtiyacını karşılar?
</div>

Hangi güvenli e-posta araçlarını kullanmaya karar vermenizden bağımsız olarak, her mesajın bir göndereni ve bir ya da daha fazla alıcısı olduğunu göz önünde bulundurun. Siz sadece resmin bir parçasısınız. E-posta hesabınıza güvenli olarak erişseniz bile bağlantıda olduğunuz kişilerin mesaj gönderirken, okurken ve yanıtlarken hangi önlemleri aldığını ya da almadığını düşünün. Yazıştığınız kişilerin e-posta sağlayıcılarının nerede konumlandığını öğrenmeye çalışın. Doğal olarak bazı ülkeler e-postaları izlemek konusunda diğerlerine göre daha saldırgandır. **Özel iletişimi güvence altına almak için siz ve yazıştığınız kişilerin tümü görece güvenli ülkelerde tutulan güvenli e-posta hizmetleri kullanmalısınız.** Ve mesajlarınızın e-posta sunucunuz ve alıcının e-posta sunucusu arasında ele geçirilmediğinden emin olmak için aynı sağlayıcıdan hesaplar seçmelisiniz. [*RiseUp*](/tr/glossary#RiseUp) iyi bir seçimdir.
 
### E-posta güvenliğinizi arttırmak için ek ipuçları ### 

- Beklemediğiniz, bilmediğiniz birinden gelen ya da şüpheli konu satırı içeren e-postaların eklerini açarken daima dikkatli olun. Bu tür e-postaları açarken anti-virüs yazılımınızın güncel olduğundan emin olun ve tarayıcınızın ya da e-posta programınızın gösterdiği herhangi bir uyarıya dikkat edin. 
- [***İnternette nasıl anonim kalınır ve internet sansürü nasıl aşılır***](/tr/chapter-8) başlıklı [***8. Bölüm***](/tr/chapter-8)’de anlatılan [*Tor*](/tr/glossary#Tor) gibi anonimlik yazılımlarını kullanmanız seçtiğiniz e-posta hizmetini, internet bağlantınızı izliyor olabilecek herhangi birinden gizlemenize yardım edebilir. Ülkenizdeki internet filtrelemesinin boyutlarına bağlı olarak, [*RiseUp*](/tr/glossary#RiseUp) ya da Gmail güvenli e-posta sağlayıcılarına erişmek için dahi, [*Tor*](/tr/glossary#Tor) ya da [***8. Bölüm***](/tr/chapter-8)’de anlatılan diğer [*sansür aşma*](/tr/glossary#Circumvention) araçlarından birini kullanmanız gerekebilir.
- E-posta alıcılarınıza ya da e-posta aracılığıyla mesaj gönderebileceğiniz genel forumlara anonim kalmak amacıyla kullanmak istediğiniz bir hesap oluştururken, kendi kişisel ya da meslekî yaşamınızla ilişkisi olan bir kullanıcı adı ya da ad ve soyadla kayıt yaptırmamaya dikkat etmelisiniz. Bu tür durumlarda, gönderdiğiniz mesaja [*IP adresinizi*](/tr/glossary#IP_address) ekleyen Hotmail, Yahoo ve herhangi bir diğer webmail sağlayıcısını kullanmaktan kaçınmanız da önemlidir.
- Bilgisayarınıza fiziksel olarak kimlerin eriştiğine bağlı olarak, geçici dosyalarınızdan e-posta ilişkili izleri temizlemek, mesajlarınızı internette yol alırken korumak kadar önemli olabilir. Ayrıntılar için [***Hassas bilgiler nasıl imha edilir***](/tr/chapter-6) başlıklı [***6. Bölüm***](/tr/chapter-6)’e ve [***Ccleaner Rehberi***](/en/ccleaner_main)’ne bakınız.
- Bağlantıda olduğunuz kişilerin oluşturduğu ağı korumak amacıyla farklı gruplarla haberleşmek için birden fazla farklı, anonim e-posta hesabı kullanmayı düşünebilirsiniz. Kaydolmak için e-posta hesabı gerektiren internet servisleri için farklı farklı e-posta hesapları kullanabilirsiniz. 
- Yukarıda verilen bütün önlemleri aldıktan sonra bile mesajlarınıza ne yazdığınıza çok dikkat etmek ve mesajlarınızın yanlış ellere geçmesi durumunda bunun nasıl bir etkisi olacağını iyi değerlendirmek hâlâ çok önemlidir. Değiş tokuş edilen bilginin güvenliğini arttırmanın bir yolu, hassas bilgileri değiş tokuş ederken insanların gerçek isimlerini, yerlerin gerçek adresini vb. kullanmayacağınız bir kod sistemi geliştirmektir. 

