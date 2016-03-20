

---

lang: tr
community: guide
type: tactics
legacy: True
child: True
weight: 2
depth: 3
title: Remembering and recording secure passwords

---

Yukarıdaki öneriler listesine bakarak, fotografik belleği olmayan birinin bu uzun, karmaşık ve anlamsız şifreleri bir kenara yazmaksızın nasıl izini kaybetmeyeceğini merak ediyor olabilirsiniz.  Her hesap için ayrı bir şifre kullanmanın önemi bunu daha da zor kılıyor. Hatırlaması kolay ama gelişmiş şifre kırıcı programlar kullanan akıllı bir kişinin bile tahmin etmesi güç olan şifreler oluşturmanıza yardım edecek birkaç püf noktası bulunmaktadır. Özel olarak bu amaç için geliştirilmiş olan [*KeePass*](/tr/glossary#KeePass) gibi bir araç kullanarak şifrelerinizi kaydetme seçeneğiniz de bulunmaktadır.


### Güvenli şifreleri hatırlamak ###

Bir şifre seçerken farklı karakter tipleri seçmek önemlidir. Bu çeşitli şekillerde yapılabilir:

- Büyük harf kullanımını çeşitlendirerek, örneğin: 'My naME is Not MR. MarSter' 
- Sayıları ve numaraları birbirinin yerine kullanarak, örneğin: 'a11 w0Rk 4nD N0 p14Y' 
- Belirli simgeleri dahil ederek, örneğin: 'c@t(heR1nthery3'
- Farklı dilleri birleştirerek, örneğin: 'Let Them Eat 1e gateaU au ch()colaT' 

Bu yöntemlerin her biri aksi halde basit olacak olan şifrelerin karmaşıklığını arttırmaya yardım eder ve şifrenizi ezberleme fikrinden tamamen vazgeçmeksizin güvenli bir şifre seçmenize yardımcı olur. Daha yaygın olan yer değiştirme yöntemlerinin bazıları ('o' yerine sıfır ya da 'a' yerine '@' simgesini kullanmak gibi) uzun zaman önce şifre kırma araçlarına dahil edildi ama bunları kullanmak hâlâ iyi bir fikirdir. Bunlar, bu tür araçların bir şifreyi öğrenmesi için gereken zamanı uzatır ve bu tür araçların kullanılamadığı daha yaygın durumlarda şanslı tahminleri engellemeye yardım eder.


Şifre yaratırken, kısaltmaların kullanımı gibi daha geleneksel bir yöntemden ([*mnemonic devices*](/tr/glossary#Mnemonic_device)) de yararlanılabilir. Bu, uzun sözcük öbeklerinin karmaşık görünüşlü sıradan sözcüklere çevrilmesine izin verir:

- 'To be or not to be? That is the question' '2Bon2B?TitQ'a dönüşür 
- 'We hold these truths to be self-evident: that all men are created equal' 'WhtT2bs-e:taMac='a dönüşür
- 'Are you happy today?' 'rU:-)2d@y?'e dönüşür

Bunlar sözcükleri ve sözcük öbeklerini, kendiliğinden karmaşık ve ezberlenebilir kılmak için kendi şifreleme yönteminizi geliştirmenize yardım edecek birkaç örnektir.

Şifreyi daha karmaşık kılmak için gösterilecek küçük bir çabanın güvenliğiniz için büyük bir etkisi vardır. Sadece birkaç karakter bile olsa şifrenin uzunluğunu artırmak ya da sayılar ya da özel karakterler eklemek şifrenin kırılmasını daha güç kılar. Aşağıda yer alan tablo bir hacker'ın şifre kombinasyonlarını birbiri ardına deneyerek, karmaşıklığı gitgide artan şifreleri kırmasının ne kadar süreceğine göstermektedir.

<table border="1">
<tbody>
<tr>
<th>Örnek Şifre </th>
<th>Gündelik kullanımdaki bir bilgisayarla kırması için gerekli zaman</th>
<th>Çok hızlı bir bilgisayarla gerekli olan zaman</th>
</tr>
<tr>
<td>bananas</td>
<td>Bir günden az</td>
<td>Bir günden az</td>
</tr>
<tr>
<td>bananalemonade</td>
<td>2 gün</td>
<td>Bir günden az</td>
</tr>
<tr>
<td>BananaLemonade</td>
<td>3 ay, 14 gün</td>
<td>Bir günden az</td>
</tr>
<tr>
<td>B4n4n4L3m0n4d3</td>
<td>3 yüzyıl, 40 yıl</td>
<td>1 ay, 26 gün</td>
</tr>
<tr>
<td>We Have No Bananas</td>
<td>19151466 yüzyıl</td>
<td>3990 yüzyıl
</td>
</tr>
<tr>
<td>W3 H4v3 N0 B4n4n45</td>
<td>20210213722742 yüzyıl</td>
<td>4210461192 yüzyıl</td>
</tr>
</tbody>
</table>

Elbette yukarıdaki şifrelerden herhangi birinin kırılması için gerekli zaman, saldırının doğasına ve saldırganın elinin altındaki kaynaklara bağlı olarak çeşitlilik göstermektedir. Dahası şifre kırmak için sürekli yeni yöntemler geliştirilmektedir. Ne olursa olsun bu tablo, karakterleri değiştirmenin, iki sözcük ya da daha da iyisi bir sözcük öbeği kullanmanın şifreleri kırmayı daha güç hale getirdiğini göstermektedir.

Yukarıdaki tablo [Passfault](https://passfault.appspot.com/password_strength.html)'un hesaplamalarına dayanmaktadır. Passfault, şifrenizin gücünü sınamanıza olanak veren birkaç web sitesinden biridir. Bununla beraber bu tür kaynaklar, farklı türden şifrelerin göreli etkililiğini sergilemek için iyi olsalar da bu sitelere gerçek şifrenizi girmekten kaçınmalısınız.






### Şifreleri güvenli olarak kaydetmek ###

Bir parça yaratıcılık, tüm şifrelerinizi hatırlamanızı sağlayabilirken; bu şifreleri düzenli aralıklarla değiştirme gereksinimi, yaratıcılığınızı hızla tüketmeniz anlamına gelir. Alternatif olarak, birçok hesabınız için rastgele güvenli şifreler oluşturabilirsiniz ve tümünü hatırlama fikrinden tamamen vazgeçebilirsiniz. Şifrelerinizi hatırlamak yerine [*KeePass*](/tr/glossary#KeePass) gibi taşınabilir, şifrelenmiş [*güvenli bir şifre veri tabanına*](/tr/glossary#Secure_password_database) bu şifreleri kaydedebilirsiniz.

<div class="getstarted" markdown="1">
Uygulama: [***KeePass - Güvenli Şifre Depolama Rehberi***](/en/keepass_main) ile uygulamaya başlayın
</div>

Elbette bu yöntemi kullanırsanız [*KeePass*](/tr/glossary#KeePass) ya da hangi aracı seçerseniz o araç için oldukça güvenli bir şifre oluşturmanız ve bu şifreyi hatırlamanız özellikle önemli hale gelir. Oluşturduğunuz bu 'master' şifre, belirli bir hesabın şifresine ulaşmak istediğiniz her seferinde kullanmanız gereken tek şifredir. Bu yöntem, yukarıdaki tüm önerileri yerine getirmenizi oldukça kolaylaştırır. <i>*[KeePass](/tr/glossary#KeePass)* taşınabilirdir, bu da öncelikli olarak, kullandığınız bilgisayardan uzakta bir şifreye bakmanız gerektiğinde veri tabanını bir USB belleğe yükleyebileceğiniz anlamını gelir.

Her ne kadar çok sayıda hesabı yönetmek zorunda olan herhangi biri için bu en iyi seçenek olsa da bu yöntemi kullanırken birkaç çekinceyi göz önünde bulundurmalısınız. [*KeePass*](/tr/glossary#KeePass) veri tabanınızın yedeğini almanız çok önemlidir. Yedekleme stratejileri konusunda [***Veri Kayıpları nasıl kurtarılır***](/tr/chapter-5) başlıklı [***5. Bölüm***](/tr/chapter-5)'e bakınız. Veri tabanınızın şifrelenmiş olması, veri tabanınızın bir kopyasını içeren bir USB belleği ya da yedekleme sürücüsünü kaybettiğinizde paniklemek zorunda olmadığınız anlamına gelir.

İkinci başlıca çekince çok daha önemli olabilir. [*KeePass*](/tr/glossary#KeePass) master şifrenizi unutursanız şifrenizi ya da veri tabanının içeriğini kurtarmanızın hiçbir yolu yoktur. O halde hem güvenli hem de akılda kalıcı bir master şifre seçtiğinizden emin olun!

Belirli durumlarda bu yöntemin gücü onun zayıflığı haline gelebilir. Birileri sizi Keepass veri tabanı master şifrenizi vermeye zorlarsa, o kişi, bu Keepass veri tabanındaki bütün şifrelerinize erişim elde edecektir. Karşılaşabileceğiniz durum buysa Keepass veri tabanınızı hassas bir dosya olarak ele alabilirsiniz ve onu [***4. Bölüm: Bilgisayarınızdaki hassas dosyaları nasıl korursunuz***](/tr/chapter-4)'da açıkladığımız gibi koruyabilirsiniz. Ayrıca, daha hassas bilgileri koruyan şifreleri içeren ayrı bir Keepass veri tabanı oluşturabilir ve bu veri tabanı için ek önlemler de alabilirsiniz.

<div class="background" markdown="1">
Mansour: Bir dakika. KeePass diğer şifrelerini korumak için tek bir master şifre kullanıyorsa bu tüm hesapların için aynı şifreyi kullanmaktan nasıl daha güvenli olabilir? Demek istediğim kötü niyetli biri master şifreni öğrenirse her şeye erişim elde eder, doğru mu?

Magda: Bu iyi bir düşünce. Master şifreni korumanın çok önemli olduğu konusunda haklısın ama birkaç önemli farklılık var. Bunların birincisi, bu kötü niyetli kişinin sadece şifrene değil KeePass veri tabanı dosyana da ihtiyacı olması. Tüm hesapların için aynı şifreyi kullanırsan, sadece senin şifrene gereksinim duyacaktır. Dahası KeePass’in aşırı güvenli olduğunu biliyoruz, değil mi? Oysa diğer programlar ya da web sitelerinin bu kadar güvenli olup olmadığını bilmiyoruz. Bazıları diğerlerine göre daha güvenli olabilir ve birilerinin zayıf bir web sitesini kırmasını ve ardından da orada öğrendiklerini kullanarak daha güvenli bir hesaba girmek için kullanmasını istemezsin. Üstelik bir şey daha var. KeePass master şifreni değiştirmeni oldukça kolay kılar.
</div>

