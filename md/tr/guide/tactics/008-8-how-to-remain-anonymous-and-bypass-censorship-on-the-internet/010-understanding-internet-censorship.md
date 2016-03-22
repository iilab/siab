

---

lang: tr
community: guide
type: tactics
legacy: True
child: True
weight: 1
depth: 3
title: Understanding Internet censorship

---

[OpenNet Initiative (ONI)](http://opennet.net/) ve [Reporters Without Borders (RSF)](http://www.rsf.org/) gibi örgütler tarafından gerçekleştirilen araştırmalar, birçok ülkenin sosyal, siyasal ve 'ulusal güvenlik' gibi oldukça çeşitli içerikleri filtrelediğine; ancak bu ülkelerin nadiren neyin engellendiğinin kesin listesini yayınladığına işaret etmektedir. Doğal olarak yurttaşlarının internete erişimini engellemek isteyen ülkeler, bu filtreleri aşmak için gerekli araç ve yöntemleri öneren proxy’leri ve web sitelerini de engellemek için özel bir çaba sarf etmektedir.

İnsan Hakları Evrensel Bildirgesi’nin 19. maddesinde belirtilen ‘bilgiye sınırsız erişim güvencesi’ne rağmen, son birkaç yıldır internet sansürüne katılan ülke sayısı çarpıcı bir biçimde artmaya devam etmektedir.  İnternet filtreleme uygulaması dünya çapında yaygınlaşırken aktivistler, programcılar ve gönüllüler tarafından yaratılan, uygulanan ve yaygınlaştırılan sansür aşma araçlarına erişim de yaygınlaşıyor.

İnternet sansürünü aşmanın çeşitli yollarını incelemeden önce, bu filtrelerin nasıl çalıştığına ilişkin temel bir kavrayış geliştirmelisiniz. Bunu yaparken, internete bağlanmanın büyük ölçüde basitleştirilmiş modelini göz önünde bulundurmanız yararlı olabilir.

### İnternet bağlantınız ###

![](/sites/securitybkp.ngoinabox.org/security/files/img/1-en.png)

Evinizden, ofisinizden, okulunuzdan, kütüphanenizden ve internet kafeden internete bağlanmanızın ilk adımı bir <i>İnternet Servis Sağlayıcısı [*ISP*](/tr/glossary#ISP) aracılığıyla yapılır. [*ISP*](/tr/glossary#ISP), çeşitli internet hizmetlerinin sizi tanıması ve size e-posta ve talep ettiğiniz web sayfaları gibi bilgileri göndermesi için bilgisayarınıza kullanabileceği bir [*IP adresi*](/tr/glossary#IP_address) atar. [*IP adresinizi*](/tr/glossary#IP_address) öğrenen herhangi biri hangi şehirde olduğunuzu anlayabilir. Bununla beraber, ülkenizdeki belirli bağlantıları olan kuruluşlar bu bilgiyi kesin konumunuzu belirlemek için kullanabilir.


- **ISP’niz**, internete bir modem aracılığıyla erişiyorsanız, hangi binada olduğunuzu ve hangi telefon hattını kullandığınızı bilecektir. 	
- **İnternet kafeniz, kütüphaneniz ya da iş yeriniz**, verili bir zamanda hangi bilgisayarı kullandığınızın yanı sıra hangi porttan ya da kablosuz erişim noktasından bağlandığınızı da bilecektir.	
- **Devlet organları**, yukarıda belirtilen kuruluşlar üzerindeki nüfuzlarının bir sonucu olarak bu ayrıntıların tümünü biliyor olabilir.
	
Bu aşamada, [*ISP*](/tr/glossary#ISP)’niz, siz dâhil bütün kullanıcılarını dünyanın geri kalanına bağlamak için ülkenizin ağ altyapısına tabidir.  Bağlantınızın diğer ucundaki eriştiğiniz web sitesi ya da internet hizmeti de, kendi ülkesindeki bir [*ISP*](/tr/glossary#ISP) ’den IP adresini alarak, benzer bir süreçten geçer.  Tüm teknik ayrıntılar olmaksızın bile bunun gibi bir temel model, filtreleri aşmanızı ve internette anonim kalmanızı sağlayan çeşitli araçları ele alırken yardımcı olabilir.

### Web siteleri nasıl engellenir ###

Esasında, bir web sayfasını ziyaret ettiğinizde, sitenin [*IP adresini*](/tr/glossary#IP_address) [*ISP*](/tr/glossary#ISP)’nize göstererek  web sunucusunun [*ISP*](/tr/glossary#ISP)’siyle sizi bağlamasını istiyorsunuz. Bu işlem, filtrelenmemiş internet bağlantınız varsa tam olarak bu şekilde gerçekleşir. Ancak, interneti sansürleyen bir ülkedeyseniz, ISP’niz ilk önce yasaklanmış web sitelerinin [*kara listesine*](/tr/glossary#Blacklist) bakacak ve ardından da isteğinizi yerine getirip getirmemeye karar verecektir.

Bazı durumlarda, [*ISP*](/tr/glossary#ISP)’lerin kendileri yerine, filtreleme ile uğraşan merkezi bir kurum olabilir. Birçok durumda bir [*kara liste*](/tr/glossary#Blacklist), [*IP adresleri*](/tr/glossary#IP_addresses) yerine www.blogger.com gibi [*alan adlarını*](/tr/glossary#Domain_names) içerir. Ve bazı ülkelerde filtreleme yazılımları, belirli internet adreslerini engellemeye çalışmak yerine, bağlantınızı izler. Bu tür yazılımlar gönderdiğiniz talepleri ve size dönen sayfaları hassas anahtar sözcüklere bakarak tarar ve ardından da sonuçları görmenize izin verip vermemeye karar verir.

Ve daha da kötüsü, bir web sayfası engellendiğinde bunu bilemeyebilirsiniz bile. Bazı filtreler neden belirli bir sayfanın sansür edildiğini açıklayan engelleme sayfası sağlarken, diğerleri yanıltıcı bir hata mesajı görüntüler. Bu mesajlar, örneğin sayfanın bulunamadığını ya da adresin yanlış yazıldığını ima edebilir.

İnternet sansürü konusunda ülkenizde kullanılan filtreleme teknolojilerinin güçlü ve zayıf yanlarını araştırmaya çalışmak yerine, bir ‘en kötü durum bakış açısı’ geliştirmek genellikle en kolayıdır. Bir başka deyişle şunları varsayabilirsiniz:

- İnternet trafiğinizin anahtar sözcüklerle izlendiğini
- Filtrelemenin doğrudan [*ISP*](/tr/glossary#ISP) düzeyinde uygulandığını
- Engellenen sitelerin hem [*IP adresleri*](/tr/glossary#IP_address) hem de [*alan adları*](/tr/glossary#Domain_name) üzerinden [*kara listeye*](/tr/glossary#Blacklist) alındığını
- Engellenmiş bir sitenin neden yüklenmediği konusunda size muğlak ya da yanlış yönlendirici bir yanıt verilebileceğini
	
En etkili sansür aşma araçları, hangi filtreleme yönteminin kullanıldığından bağımsız olarak kullanılabilir olduğundan bu karamsar tahminlerde bulunmanın genelde bir zararı olmaz.

<div class="background" markdown="1">
Mansour: Bir gün bloğa erişemediğimi ama bir başka ülkedeki arkadaşımın bloğa erişimle ilgili bir sorun yaşamadığını fark edersem bu, web sitesisini devletin engellediği anlamına mı gelir?

Magda: Tam olarak öyle değil. Web sitesine sadece buradan erişmek isteyen insanları etkileyen bazı sorunlar olabilir. Ya da bilgisayarında sadece belirli türden web sayfalarına erişirken ortaya çıkan bazı sorunlar olabilir. Bu sorunu test etmek için web sitesini, bir sansür aşma aracıyla ziyaret etmeyi deneyebilirsin. Nihayetinde bu araçların çoğu harici proxy sunucularına bağlıdır ki bu da bir başka ülkedeki bir arkadaşından senin için bir web sitesini sınamasını istemekle aynı işe yarar.
</div>


