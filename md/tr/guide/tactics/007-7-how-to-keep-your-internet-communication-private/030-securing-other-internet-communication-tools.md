

---

lang: tr
community: guide
type: tactics
legacy: True
child: True
weight: 3
depth: 3
title: Securing other Internet communication tools

---

E-postaya benzer bir biçimde anlık mesajlaşma ve [*VoIP*](/tr/glossary#VoIP) yazılımı, seçtiğiniz araçlara ve onları nasıl kullandığınıza bağlı olarak güvenli ya da güvensiz olabilir.

**Anlık mesajlaşma yazılımınızı güvenli kılmak**

‘Sohbet/chat’ olarak da adlandırılan anlık mesajlaşma, normalde güvenli değildir ve e-posta kadar izlenmeye açık olabilir. Sohbet oturumlarınızın gizliliğini güvenlik altına almaya yardım edebilecek programlar bulunmaktadır. Ancak e-postalarda olduğu gibi, güvenli bir iletişim kanalı hem sizin hem de anlık mesajlaştığınız kişilerin aynı yazılımı kullanmasını ve aynı güvenlik önlemlerini almasını gerektirir.

Var olan birçok anlık mesajlaşma protokolünü destekleyen, hesap adınızı değiştirmek ya da bağlantıda olduğunuz kişiler listesini yeniden oluşturmak zorunda kalmaksızın kolayca kullanmaya başlayabileceğiniz, [*Pidgin*](/tr/glossary#Pidgin) adı verilen bir sohbet programı bulunmaktadır. [*Pidgin*](/tr/glossary#Pidgin) aracılığıyla özel ve [*şifrelenmiş*](/tr/glossary#Encryption) konuşmalar yapmak için *Off the Record [*OTR*](/tr/glossary#OTR)* eklentisini kurmanız ve aktif hale getirmeniz gerekmektedir. Bu oldukça basit bir süreçtir.

<div class="getstarted" markdown="1">
**Uygulama**: [*OTR eklentili Pidgin – Güvenli Anlık Mesajlaşma Rehberi*](/en/pidgin_main) ile uygulamaya başlayın
</div>

<div class="background" markdown="1">
Pablo: Yahoo webmail servisi güvensizse bu Yahoo Sohbet’in de güvensiz olduğu anlamına mı geliyor?
			
Claudia: Hatırlanması gereken şey, anlık mesajlaşmayı bu raporu tartışmak için kullanmak istiyorsak bu işe dahil olan herkesin Pidgin ve OTR yazılımlarını yüklemiş olduğundan emin olmak. Yüklemişlerse Yahoo Sohbet ya da diğer sohbet hizmetlerini kullanabiliriz.
</div>

**VoIP yazılımınızı güvenli kılmak**


Diğer [*VoIP*](/tr/glossary#VoIP) kullanıcılarıyla yapılan [*VoIP*](/tr/glossary#VoIP) görüşmeleri genelde ücretsizdir. Bazı programlar uluslararası numaralar dahil, telefonlarla da ucuz görüşmeler yapmanıza izin verebilir. Bu özelliklerin çok yararlı olduğunu söylemeye gerek bile yok. [Skype](http://www.skype.com) (aşağıya bakınız), [Jitsi](http://jitsi.org/), [Google Talk](http://www.google.com/talk), [Yahoo! Voice](http://voice.yahoo.com/), ve [MSN Messenger](http://explore.live.com/windows-live-messenger), günümüzün daha popüler [*VoIP*](/tr/glossary#VoIP) programlarından bazılarıdır.

Normal olarak, internet üzerinden sesli iletişim korumasız e-posta ve anlık mesajlaşmadan daha güvenli değildir. Hassas bilgileri paylaşmak için sesli iletişimi kullanırken bilgisayarınızdan alıcının bilgisayarına kadar olan yol boyunca görüşmenizi şifreleyen bir araç seçmek önemlidir. Güvenilir bir topluluk tarafından gözden geçirilmiş, sınanmış ve tavsiye edilmiş Ücretsiz ve Açık-Kaynak Kodlu bir Yazılımı kullanmak en iyisi olacaktır. Yukarıdaki kriterleri göz önünde bulundurarak VoIP seçiminiz olarak [*Jitsi*](http://jitsi.org/)’yi denemenizi öneriyoruz.


**Skype'ın güvenliği hakkında uyarı**

[*Skype*](/tr/glossary#Skype) sabit ve cep telefonlarını aramayı da destekleyen, oldukça yaygın olarak kullanılan bir anlık mesajlaşma ve VoIP aracıdır.  Popülerliğine rağmen birçok sorun bu yazılımı güvenli bir seçim olmaktan çıkarır. Bu sorunlardan bazıları aşağıda tanımlanmıştır.

Skype’a göre o hem mesajları hem de sesli aramaları [*şifrelemektedir*](/tr/glossary#Encryption), bu sadece iletişimin her iki tarafının da Skype programı kullanması durumunda gerçekleşir. Skype telefon aramalarını ve SMS mesajları olarak gönderilen metinleri şifrelememektedir.

İletişimin her iki tarafı da (orijinal) Skype programı kullanıyorsa, Skype görüşmesinin şifrelenmesi onu, telefon üzerinden yapılan sıradan bir aramadan görünüşte daha güvenli kılmaktadır. Ama Skype’ın kapalı-kaynak kodlu bir program olması, bağımsız bir denetimi ve şifreleme konusundaki iddialarının değerlendirilmesini olanaksız kılmaktadır. Bu nedenledir ki Skype’ın kullanıcılarını, kullanıcıların bilgilerini ve iletişimini ne kadar iyi koruduğunu doğrulamak olanaksızdır. [***Bilgisayarınızı kötü amaçlı yazılımlara ve hacker'lara karşı nasıl korursunuz***](/tr/chapter-1) başlıklı [***1. Bölüm***](/tr/chapter-1)’ün [***Yazılımlarınızı güncel tutmak***](/tr/chapter_1_4) kısmı, *Ücretsiz ve Açık-Kaynak Kodlu Yazılım* [*FOSS*](/tr/glossary#FOSS)’un erdemlerine işaret eder.

Daha öncede belirtildiği gibi, güvenli bir iletişim aracı olarak her ne kadar Skype’ı tavsiye edemiyorsak da, hassas iletişimleriniz için bir araç olarak Skype’ı kullanmaya yine de karar verdiyseniz bazı önlemler almanız önemlidir:

- Casus yazılım bulaşmış bir Skype programından kaçınmak için, Skype’ı sadece resmî web sitesinden, [www.skype.com](http://www.skype.com), indirin ve kurun. URL’yi daima iki kez kontrol etmek resmî siteye bağlandığınızdan emin olmak için önemlidir. Bazı ülkelerde Skype web sitesi engellenmiştir ve/veya Skype’ın resmî sitesi olduğunu iddia eden birçok sahte site bulunmaktadır. Bu tür birçok durumda, erişilebilir durumdaki Skype sürümlerine, herhangi bir iletişimi izlemek için tasarlanmış kötü amaçlı yazılımların bulaşmış olması olasıdır. Yazılımın en son sürümünü kurmak ya da bir üst sürüme geçmek istediğiniz her seferinde, Skype web sitesine bağlanmak için [8. Bölüm](/tr/chapter-8)’de açıklanan sansür aşma araçlarını kullanın ve orijinal bir Skype programı indirin.
- Düzenli aralıklarla Skype şifrenizi değiştirmeniz önemlidir. Skype farklı konumlardan çoklu girişe izin vermektedir ve eş zamanlı oturumların sayısı hakkında size bilgi vermemektedir. Bu büyük bir risk taşımaktadır, şifreniz tehlikedeyse bu şifreyle herhangi biri de giriş yapabilir. Giriş yapılan oturumlar, tüm yazılı mesajlara ve arama geçmişine erişimi de elde eder. Şifre değiştirmek bu tür düzenbaz oturumları (yeniden giriş yapmaya zorlayarak) engellemenin tek yoludur. 
- Skype’ın gizlilik ayarlarını sohbet geçmişini saklamayacak şekilde değiştirmek de tavsiye edilebilir. 
- Skype’ın gelen dosyaları otomatik olarak kabul etme ayarlarını kapatmanız tavsiye edilir. Öyle ki bu yöntem zaman zaman kötü amaçlı/casus yazılımları bilgisayarınıza bulaştırmak için kullanılır. 
- İletişimde olduğunuz kişinin kimliğini daima bağımsız olarak doğrulayın. Konuşmak istediğiniz kişiyi tanıyorsanız, sesli sohbet sırasında bunu yapmak kolaydır. 
- Skype kullanıcı adınızın gerçek adınızla ya da kuruluşunuzun adıyla aynı ya da onunla herhangi bir ilişkisinin olup olmaması gerektiğine karar verin. 
- Daima alternatif iletişim yollarına sahip olun –Skype her an kullanılamaz hale gelebilir. 
- Ne söylediğinize dikkat edin -spesifik bir terminoloji kullanmaksızın hassas konuları tartışmak için bir kodlama sistemi geliştirin. 

Skype’ın popülerliğine rağmen, yukarıda değinilen kaygılar, güvenli bir deneyim için onu tartışmalı hale getirir. VoIP için Jitsi’yi ve güvenli anlık mesajlaşma için [*OTR*](/tr/glossary#OTR) eklentisiyle [*Pidgin*](/tr/glossary#Pidgin)’i kullanmaya başlamanızı öneriyoruz.

