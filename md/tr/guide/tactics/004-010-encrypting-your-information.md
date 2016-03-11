

---

lang: tr
community: guide
type: tactics
legacy: True
child: True
weight: 1
depth: 3
title: Encrypting your information

---

<div class="background" markdown="1">
Pablo: Ama bilgisayarım zaten Windows kullanıcı hesabı şifresiyle korunuyor! Bu yeterince iyi değil mi?

Claudia: Aslında Windows kullanıcı hesabı şifrelerini kırmak genelde oldukça kolaydır. Dahası bilgisayarını bir LiveCD’yle yeniden başlatacak kadar uzun süre ele geçiren herhangi biri, şifre konusunda endişelenmeksizin verilerini kopyalayabilir. Bilgisayarını bir süre için alıp götürebilirlerse daha da büyük bir sorunun içindesin demektir. Böyle bir durumda endişelenmen gereken sadece Windows şifresi değildir. Microsoft Word ya da Adobe Acrobat şifrelerine de güvenmemelisin.
</div>

Bilgilerinizi [*şifrelemek*](/tr/glossary#Encryption), bilgilerinizi kilitli bir kasada tutmak gibidir. Sadece anahtarı olanlar ya da kilidin şifresini bilenler (bu durumda bir [*şifreleme*](/tr/glossary#Encryption) anahtarı ya da şifre) bilgilerinize erişebilir. Bu benzetme, özellikle [*TrueCrypt*](/tr/glossary#TrueCrypt) ve onun gibi araçlar için uygundur. Öyle ki, bu araçlar her seferinde tek bir dosyayı korumak yerine 'şifrelenmiş bölümler' adı verilen güvenli bölümler oluşturur. Bir [*şifrelenmiş*](/tr/glossary#Encryption) bölüme çok sayıda dosyayı koyabilirsiniz ancak bu araçlar bilgisayarınızın ve USB belleğinizin diğer bölümlerinde depolanmış herhangi bir şeyi korumayacaktır.

<div class="getstarted" markdown="1">
**Uygulama:** [***TrueCrypt  - Güvenli Dosya Depolama Rehberi***](/en/truecrypt_main) ile uygulamaya başlayın
</div>

Her ne kadar diğer yazılımlar da benzer güçlü [*şifreleme*](/tr/glossary#Encryption) yöntemleri sağlasa da, [*TrueCrypt*](/tr/glossary#TrueCrypt) bilgi güvenliği stratejinizi tasarlamanıza izin veren birçok önemli özelliğe sahiptir. Tüm dosyalarınız, çalıştığınız sırada oluşturulan tüm geçici dosyalarınız, kurduğunuz tüm programlarınız ve tüm Windows işletim sistemi dosyalarınız dahil, **bilgisayarınızın tüm diskini kalıcı olarak şifreleme** olanağı sunar. TrueCrypt taşınabilir depolama aygıtlarındaki *[şifrelenmiş](/tr/glossary#Encryption)* bölümleri de destekler. Aşağıdaki [***Hassas bilgilerinizi gizlemek***](/tr/chapter_4_2) kısmında betimlenen 'inkâr edebilirlik' özelliğini de sunar. Dahası TrueCrypt [*ücretsiz ve açık kaynak kodlu*](/tr/glossary#FOSS) bir programdır.

<div class="background" markdown="1">
Pablo: Tamam şimdi beni endişelendirdin. Aynı bilgisayardaki farklı kullanıcılara ne olacak? Bu 'Belgelerim' klasörümdeki dosyaları okuyabilecekleri anlamına mı geliyor?

Claudia: Düşünme biçimin hoşuma gitti! Windows şifren saldırganlardan seni koruyamıyorsa aynı bilgisayarda hesabı olan diğer insanlara karşı seni nasıl koruyacak? 'Belgelerim' klasörün normalde herkese açıktır. Diğer kullanıcıların şifrelenmemiş dosyalarını okumak için zekice bir şey yapmalarına gerek yoktur. Haklısın, klasörlerini 'özel' kılsan bile, bir çeşit şifreleme kullanmadığın sürece güvende değilsin.</i>
</div>

### Dosya şiferelemeyi güvenle kullanmak için ipuçları ###

Gizli verileri depolamak hem sizin için hem de birlikte çalıştığınız insanlar için bir risk oluşturabilir. [*Şifreleme*](/tr/glossary#Encryption) bu riski azaltır ama onu ortadan kaldırmaz. Hassas verileri korumanın ilk adımı dolaşımda olan verileri azaltmaktır. Belirli bir dosyayı ya da bir dosyadaki belirli bir bilgi kategorisini depolamak için iyi bir nedeniniz yoksa onu silmelisiniz (bunu güvenli olarak nasıl yapabileceğiniz konusunda daha fazla bilgi için bakınız: [***6. Bölüm: Hassas bilgiler nasıl imha edilir***](/tr/chapter-6)). Atılacak ikinci adım ise [*TrueCrypt*](/tr/glossary#TrueCrypt) gibi iyi bir dosya [*şifreleme*](/tr/glossary#Encryption) aracı kullanmaktır.

<div class="background" markdown="1">
Claudia: Belki de bu ifadeleri bize veren kişilerin kimliklerini açığa çıkarabilecek ayrıntıları saklamamıza gerçekten de ihtiyacımız yok. Ne düşünüyorsun?

Pablo: Katılıyorum. Bu konuda mümkün olduğunca az şey kaydetmeliyiz. Dahası kesinlikle kaydetmek zorunda olduğumuz kişi ve yer adlarını korumak için basit bir şifreleme düşünmeliyiz.			
</div>

Kilitli kasa benzetmesine geri dönecek olursak [*TrueCrypt*](/tr/glossary#TrueCrypt) ya da benzer araçları kullanırken aklınızda bulundurmanız gereken birkaç şey vardır. Kasanız ne kadar güçlü olursa olsun kapısını açık bırakırsanız size bir fayda sağlamayacaktır. [*TrueCrypt*](/tr/glossary#TrueCrypt) bölümünüz kullanıma hazır durumdayken (içeriğine eriştiğiniz her seferinde) verileriniz savunmasız olabilir; o halde içindeki dosyaları gerçekten okuduğunuz ve değiştirdiğiniz zamanlar dışında onu kapalı tutmalısınız. 


[*Şifrelenmiş*](/tr/glossary#Encryption) bölümlerinizi kullanıma hazır durumda bırakmamanız gerektiğini özellikle hatırlamanız gereken bazı durumlar şunlardır:

- Herhangi bir zaman aralığı için bilgisayarınızdan uzaklaştığınızda şifrelenmiş bölümlerinizin bağlantısını kesin. Bilgisayarınızı gece boyunca çalışır bıraktığınızda, siz uzaktayken hassas bilgilerinizin fiziksel ya da uzak saldırganların erişimine açık bırakılmadığından emin olun.
- Bilgisayarınızı uyku moduna sokmadan önce şifrelenmiş bölümlerinizin bağlantısını kesin. Bu genel olarak dizüstü bilgisayarlarında kullanılan ancak masaüstü bilgisayarlarında da bulunabilecek, hem 'askıya alma' hem de 'uyku modu' özellikleri için geçerlidir.
- Bilgisayarınızı bir başkasına devretmeden önce şifrelenmiş bölümlerinizin bağlantısını kesin. Bir güvenlik noktasından ya da sınır kapısından bir dizüstü bilgisayarı geçirirken tüm [*şifrelenmiş*](/tr/glossary#Encryption) bölümlerin bağlantısını kesmeniz ve bilgisayarınızı tamamen kapatmanız önemlidir.
- Arkadaşlarınızınki ya da meslektaşlarınızınki dahil güvenmediğiniz harici bir depolama aygıtını ya da USB belleğini bilgisayarınıza takmadan önce şifrelenmiş bölümlerinizin bağlantısını kesin.
- [*Şifrelenmiş*](/tr/glossary#Encryption) bir bölümü bir USB bellekte saklayacaksanız, aygıtı bilgisayardan ayırmanız bölümün bağlantısını hemen kesmez. Dosyalarınızı aceleyle güvence altına almanız gerekirse de bölümü düzgün bir biçimde kaldırmalısınız. Ardından da harici sürücünün ya da belleğin bağlantısını kesmelisiniz ve bilgisayardan ayırmalısınız. Bunları yapmanın en hızlı yolunu buluncaya kadar biraz pratik yapmak isteyebilirsiniz.
	
[*TrueCrypt*](/tr/glossary#TrueCrypt) bölümünü bir USB bellekte saklamaya karar verdiyseniz, [*TrueCrypt*](/tr/glossary#TrueCrypt) programının da bir kopyasını onunla birlikte tutabilirsiniz. Bu, verilerinize bir başkasının bilgisayarından da erişmenizi sağlar. Genel kurallar hâlâ geçerlidir : bilgisayarın [*kötü amaçlı yazılımlardan*](/tr/glossary#Malware) arındırılmış olduğu konusunda güveniniz tam değilse şifrenizi girmemeli ve hassas verilerinize erişmemelisiniz.


