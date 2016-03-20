

---

lang: tr
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 016
title: Tor Browser - Digital Anonymity and Circumvention

---

**Ana Sayfa**

[**https://www.torproject.org**](https://www.torproject.org/)

**Bilgisayar Gereksinimleri**

- İnternet bağlantısı
- Bütün Windows sürümleri (XP ve sonrasındakiler)

**Bu rehberde kullanılan sürümler**

- Tor Tarayıcı: 3.5.3

**Bu bölümün son güncellenme tarihi**

- Mart 2014

**Lisans**: 

- Ücretsiz ve Açık-Kaynak Yazılım

**Gerekli Okuma**

- Nasıl Yapmalı Kitapçığının [**8. İnternette nasıl anonim kalınır ve internet sansürü nasıl aşılır**](/tr/chapter-8) bölümü

**Buradan sağlayacağınız faydalar**: 

- Ziyaret ettiğiniz websitelerinden digital kimliğinizi gizleme yetisi
- **İnternet Servis Sağlayıcıları** (**Internet Service Providers, ISPs**) ve diğer gözetleme mekanizmalarından çevrimiçi taramalarınızı gizleme yetisi
- İnternet sansür ve filtreleme kurallarını atlatma yetisi

**GNU Linux, Mac ve Microsoft Windows’a Uyumlu Diğer Programlar**

Tor Tarayıcı GNU Linux, Mac OS, Microsoft Windows ve Android işletim sistemleri için ulaşımdadır. Tor çevrimiçi aktivitelerinizin anonimliğini korumak için en çok tavsiye edilen ve dikkatli bir şekilde test edilen araçtır. Yine de tavsiye edilen diğer çözümlerden bazılarını da burada listelemek isteriz.
		
* [**Riseup VPN**](https://help.riseup.net/en/riseup-vpn/) **Linux**, **MAC**, **Android** ve **Microsoft Windows** için ücretsiz bir Sanal Gizli Ağ (**Virtual Private Network**, **VPN**) proxy sunucusudur.
* [**Psiphon3**](http://www.psiphon3.com/) **Microsoft Windows** ve **Android OS** ücretsiz ticari bir **Sanal Gizli Ağ** (**VPN**) çözümüdür.
* [**Dynaweb FreeGate**](http://www.dit-inc.us/freegate) **Microsoft Windows** için ücretsiz bir proxy aracıdır.
* [**Your Freedom**](http://www.your-freedom.net/) da ücretsiz (ama daha yavaş) bir servis sunan ticari bir proxy aracıdır. **Linux**, **Mac OS** ve **Microsoft Windows** için ulaşıma açıktır.

## 1.1 Başlamadan önce bu araç hakkında bilmeniz gerekenler ##

**Tor Tarayıcı** internet aktiviteleriniz ve alışkanlıklarınızın gizliliği ve güvenliğini artırmak için tasarlanmış bir yazılım aracıdır. Kimliğinizi ve çevrimiçi taramalarınızı internet gözetlemeciliğinin pek çok formundan saklar. **Tor** elektronik kısıtlamaları atlatmanın da güvenli bir yolu olarak faydanıza sunulur ki bloglara ya da haberlere ulaşımınız ya da bunları yayınlamanız mümkün olsun.

**Tor** dünyanın her yerine yayılmış gönüllülerin çalıştırdığı sunucu ağı içinde iletişimleri rotalandırarak *anonimliğinizi* korur. **Tor’u** kullanmak ziyaret ettiğiniz siteleri potansiyel gözetlemecilerden sakladığı gibi, sizin kimliğinizi ve bulunduğunuz yeri o ziyaret ettiğiniz sitelerden gizler. Yazılım, **Tor** ağı içindeki sunucuların hiçbirinin **hem** yerinizi **hem de** ziyaret ettiğiniz siteleri **bilmemesini** sağlıyacak şekilde tasarlanmıştır.

**Tor** kendisine gelen ve kendi ağı içinde ilerleyen iletişimin de şifrelenmesi için adımlar atmaktatır, **fakat** bu önlem şifrelenmemiş kanallardan (https ulaşımı vermeyen) içerik alıp gönderen bir websiteye kadar işleyemez. Yine de bu tür sitelere **Tor** kullanarak ulaşmanın faydası **Tor’un** iletişiminizi **Tor sunucularından** o güvenliksiz sitelere atılan son adıma kadar iletişiminizi koruyor olmasıdır. Böylece iletişiminizin içeriğinin gözlenme ihtimali sadece bu son adıma kısıtlanır.

Tor Tarayıcı Paketi Tor yazılımı ve kullanımı esnasında ekstra güvenlik sağlaması için tasarlanmış Firefox web tarayıcısın modifiye edilmiş bir sürümünü içerir. Bu aket aynı zamanda [**NoScript**](/tr/firefox_noscript) and [**HTTPS-Everywhere**](/tr/firefox_others#5.1) eklentilerini de barındırır. 

**Not**: Anonimliğin korunması bir miktar hız kaybı pahasına sağlanır.  Tor taramalarınızın ananimliğini intenet trafiğinizi dünyanın farklı yerlerindeki gönüllülerin bilgisayarları ve sunucuları arasında dolandırarak koruduğu için kesinlikle bilgisayarınızdaki diğer web tarayıcılarından daha yavaş işleyecektir.

**Tanımlar**: 

- **Köprü Durağı**: Köprü Durağı kaynağı gizli tutulan bir **Tor** sunucusudur. Bir köprü kullanmayı seçerseniz, sunucu size **Tor** ağına ulaşma imkanı verir, **Tor** bulunduğunuz ülkede engellenmiş olsa bile.

- **Port**: Bu bölümde, port  yazılımın ağdaki diğer bilgisayarlarda çalışan servislerle iletişiminin kurulduğu bir ulaşım noktasıdır. Bir URL, mesela **www.google.com**, bir servisin sokak adresini bilmenizi sağlıyorsa, port size hedefinize ulaştığınızda hangi kapıyı kullanmanız gerektiğini söyler. İnternet taramaları esnasında güvenli olmayan siteler için (**http://mail.google.com**) genelde port 80 kullanılırken, port 443 güvenli siteler için kullanılır (**https://mail.google.com**). 

- **Proxy:** Proxy bilgisayarınızda, yerel ağınızda ya da internette başka bir yerde çalışan bir aracı yazılımdır, iletişiminizin hedefinie giderken yönlendirilmesine yardımcı olur.

- **Rota**: Rota bilgisayarınız ile hedef sunucu arasındaki internet iletişim yoludur.

