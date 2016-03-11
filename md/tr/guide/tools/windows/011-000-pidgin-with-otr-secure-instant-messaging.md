

---

lang: tr
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 011
title: Pidgin with OTR - Secure Instant Messaging

---

**Ana Sayfa**

- **Pidgin**: [**www.pidgin.im**](http://www.pidgin.im)
- **OTR**: [**https://otr.cypherpunks.ca/**](https://otr.cypherpunks.ca/)

**Bilgisayar Gereksinimleri**

- İnternet bağlantısı
- Bütün Windows sürümleri

**Bu rehberde kullanılan sürümler**

- Pidgin 2.10.9 
- OTR 4.0.0-1 

**Bu bölümün son güncellenme tarihi**

- Ağustos 2014

**Lisans**: 

- Ücretsiz ve Açık-Kaynak Yazılım

**Gerekli Okuma**

Nasıl Yapmalı Kitapçığının [7. Bölümü, İnternet İletişiminizin Gizliliği Nasıl Korunur](/tr/chapter-7) 

**Buradan sağlayacağınız faydalar**: 

- En popüler anlık mesajlaşma servislerinden bazılarını tek bir program ile organize edip yönetebilme olanağı
- Özel ve kimlik denetimli sohbet edebilme olanağı

**GNU Linux, Mac ve Microsoft Windows’a Uyumlu Diğer Programlar**

**Not:** **Pidgin’e** alternatif olarak [**Jitsi’yi**](/en/jitsi) öneriyoruz. **Jitsi’yi** güvenli metin bazlı sohbetlerin yanında (ki bunu **Jitsi** üzerinden **Pidgin** kullanıcılarıyla da yapabilirsiniz), diğer **Jitsi** kullanıcılarıyla güvenli ses ve video iletişimleri kurmak için kullanabilirsiniz. **Jitsi** **Microsoft Windows**, **GNU/Linux**, **Mac OS** ve diğer işletim sistemleri için kullanıma açıktır.

Hem **Pidgin** hem de **OTR**; **Microsoft Windows** ve **GNU/Linux** için kullanıma açıktır. **OTR’yi** destekleyen **Microsoft Windows** için bir diğer anlık mesajlaşla programı da [**Miranda IM’dir**](http://www.miranda-im.org/). **Mac OS** için **OTR** eklentisini destekleyen cok protokollü [Adium’u](http://adium.im/) kullanabilirsiniz.

## 1.1 Başlamadan önce bu araç hakkında bilmeniz gerekenler ##

**Pidgin’i** kullanmaya başlamadan önce bir **anlık mesajlaşma** hesabınız olmalı, ancak bundan sonra o hesabı **Pidgin’e** kaydedebilirsiniz. Örnek olarak, bir **Google** hesabınız varsa, onların **anlık mesajlaşma** servisi **GoogleTalk’ı** **Pidgin** ile kullanabilirsiniz. Varolan **anlık mesajlaşma** hesabınızın giriş detayları hesabınıza **Pidgin** aracılığıyla ulaşabilmek için kullanılır.

**Not:** Bütün kullanıcılar **Anlık Mesajlaşma hesabı sağlayıcılarının** gizlilik ve güvenlik politikaları hakkında mümkün olduğunca bilgi edinmeye teşvik edilir. 

**Pidgin** şu **anlık mesajlaşma** servislerini destekler: [**AIM**](http://dashboard.aim.com/aim), [**Bonjour**](http://www.apple.com/support/bonjour/), [**Gadu-Gadu**](http://komunikator.gadu-gadu.pl/), [**Google Talk**](http://www.google.com/talk/), **Groupwise**, [**ICQ**](http://www.icq.com), **IRC**, [**MSN**](http://www.msn.com/), [**MXit**](http://www.mxit.com/), [**MySpaceIM**](http://www.myspace.com/guide/im), [**SILC**](http://silcnet.org/), **SIMPLE**, [**Sametime**](http://www.ibm.com/developerworks/downloads/ls/lst/), [**Yahoo!**](http://messenger.yahoo.com/), **Zephyr** ve **XMPP** mesajlaşma protokolünü takip eden bütün **anlık mesajlaşma** istemcileri.

**Pidgin** değişik **anlık mesajlaşma** servisleri arasında iletişime izin vermez.  Örnek olarak siz **Pidgin’i** **GoogleTalk** hesabınıza ulaşmak için kullanıyorsanız, **ICQ** hesabını kullanan bir arkadaşınızla sohbet etmeniz mümkün değildir.

Yine de, **Pidgin** desteklediği bütün mesajlaşma protolleri üstünden çalışan hesaplarınızın hepsini birden yönetmeniz için yapılandırılabilir. Böylece, hem **Gmail** hem de **ICQ** hesabınızı aynı anda kullanabilir, ve arkadaşlarınızla bunlardan **biri** aracılığıyla (çünkü ikisi de **Pidgin** tarafından desteklenir) sohbet edebilirsiniz. 

**Off-the Record** (**OTR**) mesajlaşma özellikle **Pidgin** için geliştirilmiş bir eklentidir. Aşağıdaki gizlilik ve güvenlik özelliklerini kullanımınıza sunar: 

- **Kimlik Denetleme**: İrtibatta olduğunuz kimsenin kimliğinden hep emin olursunuz.
- **İnkar Edebilme**: Sohbet oturumu bittikten sonra, mesajlarınızın sizden ya da irtibatta bulunduğunuz kişiden kaynaklandığı gösterilemez.
- **Şifreleme**: Sizden başka kimse anlık mesajlarınıza ulaşamaz ya da onları okuyamaz.
- **Mükemmel İleri Yönlendirme Güvenliği**: Üçüncü şahıslar özel anahtarlarınızı ele geçirecek dahi olsa, eski sohbetlerinizden hiçbiri tehlike altında değildir.

**Not**: **OTR** eklentisinden önce **Pidgin** indirilmelidir.

