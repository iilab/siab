

---

lang: tr
community: guide
type: tactics
legacy: True
child: True
weight: 7
depth: 3
title: Advanced Smartphone Security

---

## Akıllı telefonunuza eksiksiz erişimi elde edin ##

Akıllı telefonların birçoğu, kurulu işletim sisteminin, üretici yazılımının ya da cep telefonu operatörlerinin programlarının izin verdiğinden daha fazlasına muktedirdir. Benzer bir biçimde akıllı telefonların bazı işlevleri, kullanıcıların bunları kontrol edememesi ya da değiştirememesi için “kilitlenmiş”tir, ve bunlar erişilemez olarak kalır. Birçok durumda bu işlevler akıllı telefon kullanıcıları için gereksizdir. Bununla beraber bir akıllı telefonun veri ve iletişim güvenliğini arttırabilecek bazı uygulamalar ve işlevler de vardır. Ayrıca güvenlik risklerinden kaçınmak için kaldırılabilecek bazı halihazırda var olan işlevler de mevcuttur.

Bu ve diğer nedenlerle bazı akıllı telefon kullanıcıları, zenginleştirilmiş işlevleri kurmalarına ya da uygun bulmadıkları diğer işlevleri kaldırmalarına ya da azaltmalarına izin verecek uygun ayrıcalıkları elde etmek için, akıllı telefonu çalıştıran çeşitli yazılımları ve programları değiştirmeyi tercih ederler.

Bir akıllı telefonda, hizmet sunucunuz ya da işletim sistemi üreticileri tarafından dayatılan sınırları aşma işlemi (Android araçlarda) ‘rooting’ ya da (iPhone ya da iPad gibi iOS araçlarda) ‘jailbreaking’ olarak adlandırılır. Genellikle başarılı bir rooting ya da jailbreaking, ek uygulamalar kurmak ve kullanmak, aksi halde kilitli olan düzenlemeler üzerinde değişiklikler yapmak ve akıllı telefonun veri depolaması ve hafızası üzerinde tam denetim için gereken tüm ayrıcalıklara sahip olmanız ile sonuçlanır.

**UYARI**: 'Rooting' ya da 'jailbreaking' geri döndürülemez işlemler olabilir ve yazılım yüklemesi ve yapılandırması konusunda deneyim gerektirir. Şunları göz önünde bulundurun: 

- Akıllı telefonunuzu kalıcı olarak işlemez kılma riski vardır.
- Üretici ya da hizmet sunucunuzun garantisi geçersiz hale gelebilir.
- Bazı yerlerde bu işlem yasadışı olabilir.

Ama dikkatli olursanız 'root' edilmiş bir cihaz akıllı telefonunuzu daha güvenli kılmak için onun kontrolünü ele geçirmenin en doğrudan yoludur.

### Alternatif Donanım Yazılımı ###

Donanım yazılımı belirli cihazlarla yakından ilişkili programlara işaret eder. Bunlar cihazın işletim sistemiyle iş birliği içindedir ve akıllı telefonunuzun (hoparlör, mikrofon, kameralar, dokunmatik ekran, hafıza, anahtarlar, antenler, gibi) donanımının temel işlemlerinden sorumludur.

Android bir cihazınız varsa telefon üzerindeki denetiminizi daha da arttırmak için bir donanım yazılımı alternatifi kurmayı düşünebilirsiniz. Bir donanım yazılımı alternatifi kurmak için telefonunuzu “root” etmeniz gerektiğini aklınızda bulundurun.

[**Cyanogenmod**](http://www.cyanogenmod.com), Android telefonlar için donanım yazılımı alternatifine örnektir; telefonunuzun sistem düzeyindeki (yani, telefon üreticisi ya da taşınabilir ağ operatörü tarafından kurulan) uygulamalarını kaldırmanıza izin verir. Bunu yaparak, cihazınızın izlenebileceği bir dizi yolu azaltabilirsiniz; örneğin bilginiz dışında servis sağlayıcınıza gönderilen veriler.

Dahası Cyanogenmod, bir OpenVPN uygulamasıyla birlikte gelmektedir, bu da sizi Open VPN’i manuel olarak kurmak zahmetinden kurtarır. VPN (Virtual Private Network/Sanal Özel Ağ) internet iletişiminizi güvenle “proxy” etmenin yollarından biridir (aşağıya bakınız). 

Ayrıca Cyanogenmod, iletişim geçmişinizin akıllı telefonunuza kaydedilmediği anonimleştirilmiş bir tarama modu sunmaktadır.

Cyanogenmod birçok diğer özelliği beraberinde taşır. Ancak tüm Android cihazlar tarafından desteklenmemektedir. Daha fazla ilerlemeden [desteklenen cihazlar listesi](http://www.cyanogenmod.com/devices)ne göz atın.
 
### Bütün bölümlerin şifrelenmesi ###

Telefonunuz root edildiyse tüm veri depolamasını şifrelemeyi ya da bazı bilgilerinizi telefonunuzda korumak için akıllı telefonunuzda bir bölüm yaratmayı düşünebilirsiniz.

[**Luks Manager**](https://play.google.com/store/apps/details?id=com.nemesis2.luksmanager&hl=en) kullanıcı dostu arayüzüyle bölümlerin kolay ve güçlü bir şekilde şifrelenmesine izin verir. Android cihazınıza önemli veriler depolamaya başlamadan önce bu aracı kurmanızı ve Luks Manager tarafından sağlanan Şifrelenmiş Bölümleri veri depolamak için kullanmanızı şiddetle tavsiye ediyoruz.

Whisper Systems projesi tüm Android cihazınızı şifrelemenize izin verecek [**WhisperCore**](http://www.whispersys.com/whispercore.html) uygulamasını hazırlamaktadır.

### Sanal Özel Ağ (VPN) ###

Bir VPN, cihazınız ve bir VPN sunucusu arasında internet aracılığıyla şifrelenmiş bir tünel sağlar. Bu bir tünel olarak adlandırılır çünkü https’ler gibi, diğer şifrelenmiş trafikten farklı olarak, tüm servisleri, protokolleri ve içeriği gizler. Bir VPN bağlantısı sadece bir kez kurulur ve sadece siz karar verdiğiniz zaman sona erer.

Tüm trafiğiniz proxy ya da VPN sunucusu üzerinden geçtiğinden bir aracının, etkinliklerinizi çözümlemek için sadece proxy’nize girmesi gerektiğini aklınızda bulundurun. Bu nedenle proxy ve VPN hizmeti sunan kurum ya da kişiler arasında dikkatlice seçim yapmak önemlidir. Veri akışınızı dağıtmanız, gizliliği ihlal edilmiş sistemlerin etkisini azaltacağından, farklı proxy’leri ve/ya da VPN’leri kullanmanız ayrıca tavsiye edilebilir.

[**RiseUp VPN**](https://help.riseup.net/en/vpn) sunucusunu kullanmanızı tavsiye ediyoruz. RiseUp VPN’i Cyanogenmod’u kurduktan sonra Android cihazlarda kullanabilirsiniz (bakınız yukarısı). iPhone’larda da RiseUp VPN bağlantısını kurmak kolaydır – [buradan](https://support.apple.com/kb/HT1424) daha fazla bilgi edinebilirsiniz.

