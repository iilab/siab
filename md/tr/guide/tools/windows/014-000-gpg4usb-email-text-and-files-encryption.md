

---

lang: tr
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 014
title: gpg4usb - email text and files encryption

---

**Ana Sayfa**

- [**http://www.gpg4usb.org/**](http://www.gpg4usb.org/)

**Bilgisayar Gereksinimleri**

- Tüm Windows sürümleri

**Bu kılavuzda kullanılan sürümler**

- 0.3.3

**Bu bölümün son güncellenme tarihi**

- Temmuz 2014

**Lisans**

- Özgür ve Açık Kaynak Yazılım

**Gerekli Okuma**

- Nasıl Yapmalı Kitapçığı'nın [**7. İnternet iletişiminizin gizliliği nasıl korunur**](/tr/chapter-7) bölümü

- [**İnsan Hakları Koruyucuları için Dijital Güvenlik ve Gizlilik **](https://www.frontlinedefenders.org/esecman), **2.4 Kriptoloji – Açık Anahtar Şifreleme** bölümü (38. Sayfa)

**Buradan sağlayacağınız faydalar:**:

- Nerede olursanız olun (örneğin İnternet kafe veya iş), dosya ve yazılı iletilerinizi şifreleyebilme
- İletilerinizi çevrim dışı olduğunuz veya İnternet erişiminizin olmadığı durumlarda şifreleyebilme ve daha sonra İnternet bağlantısı olan bir bilgisayardan gönderebilme

## 1.1 Başlamadan önce bu araç hakkında bilmeniz gerekenler ##

**gpg4usb** yazılı ileti ve dosyaları şifrelemenize ve şifrelerini çözmenize olanak veren, basit, hafif ve taşınabilir bir programdır. **gpg4usb**, **açık-anahtar kriptografisi** ile çalışır. Bu yöntemle, her kullanıcı kendi **anahtar çiftini** oluşturmalıdır. İlk anahtar **kişisel anahtar** olarak bilinir. Bir parola veya şifreyle korunur ve *asla* kimseyle paylaşılmamalıdır.

İkinci anahtar **açık anahtar** olarak bilinir. Bu anahtarı iletişimde olduğunuz insanlarla paylaşabilirsiniz ve onlar da kendi açık anahtarlarını sizinle paylaşabilir. Birisinin açık anahtarını edindiğiniz anda ona şifreli mesajlar göndermeye başlayabilirsiniz. Uyumlu olan tek açık anahtara sahip olan bu kişi olduğu için, şifreli mesajlarınızı okuyabilecek olan tek kişi de odur. 

Aynı şekilde, kendi açık anahtarınızı e-posta ile iletişime geçtiğiniz kişilere gönderir ve onunla eşleşen açık anahtarı saklarsanız, bu kişilerden gelecek şifreli mesajları okuyabilecek tek kişi de siz olursunuz. 

Ayrıca, mesajlarınıza dijital imza da ekleyebilirsiniz. Sizin açık anahtarınıza sahip olan ve mesajınızı alan kişi bu sayede e-postanın sizden geldiğini onaylayabilir ve içeriğinin değiştirilmediğinden emin olabilir. Aynı şekilde, karşı tarafın açık anahtarına sahipseniz, onun mesajlarındaki dijital imzayı kontrol edebilirsiniz. 

**gpg4usb** ile şifreleme anahtar çifti oluşturabilir, açık anahtarı başkalarıyla paylaşmak üzere çıkarabilir, yazılı mesaj oluşturup onu şifreleyebilirsiniz. Açık anahtarı ya/ya da şifrelenmiş mesajı **gpg4usb’ten** kendi e-postanıza kopyalayıp yapıştırabilirsiniz ya da daha sonra göndermek üzere metin dosyası olarak kaydedebilirsiniz. Belge ve dosyalar da şifrelenebilir. 

**Not**: Aklınızda tutun ki, belge ve dosyalarınızın orijinal, şifrelenmemiş versiyonları bilgisayarınızda durmaya devam eder. Bu yüzden, hem siz hem de iletişimde olduğunuz kişiler, gerektiği zaman bunları bilgisayardan silmeyi unutmamalıdır. 

**gpg4usb**, benzer **GPG** ve **PGP** programları ile anahtar ve şifrelenmiş mesaj takası yapmanıza izin verir.   


