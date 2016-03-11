

---

lang: tr
community: guide
type: tools
legacy: True
child: False
os: internet
weight: 010
title: RiseUp - Secure Email Service

---

**Ana Sayfa**

[**https://riseup.net/**](https://riseup.net/)

**Bilgisayar Gereksinimleri**

- İnternet bağlantısı
- **RiseUp** en uyumlu **Firefox** web tarayıcısı ile çalışır

**Bu bölümün son güncellenme tarihi**

- Ağustos 2014

**Lisans**

- Ücretsiz Servis

**Gerekli Okuma**

- Nasıl Yapmalı Kitapçığının [7. Bölümü, İnternet İletişiminizin Gizliliği Nasıl Korunur](/tr/chapter-7) 

**Buradan sağlayacağınız faydalar**: 

- Topluluk odaklı tasarlanmış ve reklamlardan bağımsız bir e-posta hesabı
- E-postanıza internet veya herhangi bir e-posta programı üzerinden ulaşma ve şifrelenmiş bir bağlantı üzerinden özel e-posta iletişiminizi sağlama olanağı
- E-posta adresinizi değiştirme, e-posta gelen kutunuzun kapasitesini ayarlama ve başkalarını **RiseUp** kullanmaya davet etme olanağı

<a name="alternatives"></a>
**Alternatif E-posta Servisleri:**

**RiseUp** İnternet gizliliği ve güvenliğini savunan güvenilir kişiler tarafından geliştirilmiş güvenli bir e-posta servisi olmasına rağmen, alışılmışın dışında bir e-posta servisi kullanmaniz dikkatleri istenmeyen bir şekilde üzerinize çekebilir. Bazı durumlarda ülkenizdeki popüler bir e-posta servisini kullanarak bu durumu engellemeniz anlamlı olabilir. Amaç, bunu yaparken minimum güvenlik gereksinimlerinden hiçbir şekilde taviz vermemenizdir. Bir e-posta servisi seçerken aşağıda belirtilen noktaları göz önünde bulundurmanızı tavsiye ederiz:

1. Bilgileri (giriş bilgileriniz ve e-postalarınız dahil olmak üzere) aktarmak için **şifrelenmiş kanalları** (**https** ve IMAP, POP3 ve SMTP’ler gibi diğer SSL şifrelenmiş protokol tipleri gibi) kullanmaya izin veriyor mu ve şifreleme ile ilgili herhangi başka bir problem çıkarıyor mu (örneğin şifreleme sertifikaları ile ilgili problemler)?

2. **E-posta sunucuları güvenli bir şekilde yönetiliyor mu**? Bilgileriniz en güvenli şekilde saklamak için en iyi yöntemleri kullanan profesyoneller tarafından mı işletiliyor? Onların herhangi bir amaç uğruna (ticari, politik, dini vb.) bilgilerinizi üçüncü şahısların erişimine *açmayacağına* güveniyor musunuz?

3. Sunucuların coğrafi konumlarını, **hangi ülkenin yargı sistemi altında olduklarını** ve şirketlerin nereye bağlı olduğunu biliyor musunuz? Bu bilgilerin sizin e-posta aktiviteleriniz ve bilgilerinizin gizlilik ve güvenlik ayarları açısından ne anlama geldiğini biliyor musunuz?

Dünyanın belli yerlerinde **Google Mail**, daha iyi bir ‘kamufle olma’ olanağı sunarak, (ticari doğası gereği) güvenliğinizden fazla ödün vermenizi gerektirmeyerek **RiseUp’a** iyi bir alternatif sunabilir. 

### 1.1 Başlamadan önce bu araç hakkında bilmeniz gerekenler ###

**RiseUp**, politik ve sosyal adalet için çalışan kişiler ve kurumlar için gizli ve güvenli bir barındırma, listeleme ve posta servisleri sağlamaya adanmış bir kolektiftir. Servisleri ücretsiz olduğu için ve RiseUp aktiviteleriniz takip etmediği için, e-posta hesabınız, reklam odaklı ve güvenli olmayan sağlayıcılara kıyasla çok daha küçüktür. Yeni bir hesap, ancak hali hazırda kullanıcı olan iki kişi tarafından gönderilen davet kodu ile oluşturulabilir. [RiseUp hakkında daha fazla bilgi alabilmek için sitelerini ziyaret edebilirsiniz](https://help.riseup.net/en/about-us).

**RiseUp** sadece, bilgisayarınız ve sunucunuz arasında güvenli bir iletişim kuran **Güvenli Soket Katmanı** (**Secure Sockets Layer**, **SSL**) üzerinden çalışır. Bu güvenlik, e-postanızı güvenli **POP**, **IMAP** ve **SMTP** bağlantıları (e-posta istemci programların e-postalarınızı indirmek ve göndermek için kullandığı protokoller) üzerinden bir istemci programda okuduğunuz zaman sağlanır. **RiseUp**  **Mozilla Thunderbird** ile uyumlu bir şekilde çalışır. **RiseUp** e-posta hesabınıza ulaşmak için **Mozilla Thunderbird’ü** nasıl indireceğinizi öğrenmek için lütfen  [**Thunderbird**](http://securityinabox.org/tr/thunderbird_main) ile ilgili bölüme bakınız.

**RiseUp** e-posta hesaplarına ek olarak aşağıdakileri de sağlar: 

- E-posta grup iletişimleri için [**E-posta Listesi**](https://lists.riseup.net/);
- [**CrabGrass**](https://we.riseup.net/) adlı, gruplar ve ağlar arasındaki organizasyonu sağlamak için ve küresel adalet hareketinin ihtiyaçlarına gore tasarlanmış, kendi ücretsiz ve açık kaynak sosyal ağ uygulaması;
- [**EtherPad**](https://pad.riseup.net/) adlı, birden fazla kullanıcının aynı anda aynı belge üzerinde çalışmasını sağlayan ortaklaşa belge düzenleme platformu;
- [**OpenVPN**](https://help.riseup.net/en/vpn) İnternet’i **RiseUp** sunucuları üzerinden taramaya izin veren şifrelenmiş vekil sunucu. Vekil sunucular üzerine daha fazla bilgi edinmek için [İnternette nasıl anonim kalınır ve internet sansürü nasıl aşılır](/tr/chapter-8) adlı 8. Bölüm’e bakınız;
- [**Jabber/XMPP**](https://help.riseup.net/en/chat) adlı hızlı mesaj, metin, ses ve video konuşma sunucusu. Bu sunucuyu, diğer programların yanı sıra [Jitsi](/tr/jitsi), [Pidgin](/tr/pidgin_main), Adium, and ChatSecure gibi programlar aracılığıyla kullanabilirsiniz. [Diğer internet iletişim araçlarını güvenli kılmak](/tr/chapter_7_3) veya [7. Bölüm, İnternet iletişiminizin gizliliği nasıl korunur](/tr/chapter-7) bölümüne bakabilirsiniz. 
.


