

---

lang: tr
community: guide
type: tactics
legacy: True
child: True
weight: 4
depth: 3
title: Advanced Email Security

---

Aşağıda tartışılan araçlar ve kavramlar deneyimli bilgisayar kullanıcılarına tavsiye edilir.

### E-postada Açık Anahtar Şifrelemesini Kullanmak  ###

Güvenli olmayan e-posta hesaplarıyla bile daha üst düzey bir e-posta güvenliği elde etmek olanaklıdır. Bunu yapmak için açık anahtar [**şifrelemesini**](/tr/glossary#Encryption) öğrenmeniz gerekir. Bu teknik her özgün mesajı kodlayarak mesajınızı göndermek istediğiniz kişi haricinde herkese okunmaz kılar. Açık anahtar [**şifrelemesini**](/tr/glossary#Encryption) hünerli yönü şudur: bağlantıda olduğunuz kişilerle gelecekte mesajlarınızı nasıl şifreleyeceğiniz konusunda herhangi bir gizli bilgi alışverişinde bulunmak zorunda olmazsınız.

<div class="background" markdown="1">
**Pablo**: Ama bu nasıl çalışıyor?
			
**Claudia**: Matematik! Bir e-posta alıcısının özel açık anahtarını kullanarak o kişiye yollamak istediğin e-posta’yı kodlarsın. Açık anahtar özgürce dağıtılabilir. Ardından alıcı, gelen mesajlarını okumak için dikkatle korumak zorunda olduğu gizli ‘özel anahtarı’nı kullanır.  Sırası gelince o kişi, sana yazdıklarını şifrelemek için senin açık anahtarını kullanır. Sonuç olarak açık anahtarlarınızı değiş tokuş etmek zorundasınız, ama anahtarlarınızı, bunları elde etmek isteyen herhangi biri için endişelenmeksizin, herkese açık bir biçimde paylaşabilirsiniz.

</div>

Bu teknik, herhangi bir e-posta servisiyle birlikte, hatta güvenli iletişim kanalları olmayanlarla bile, kullanılabilir çünkü her bir mesaj bilgisayarınızı terk etmeden önce [**şifrelenir**](/tr/glossary#Encryption).

[**Şifreleme**](/tr/glossary#Encryption) kullanarak dikkatleri üzerinize çekebileceğinizi hatırlayın. Bir webmail hesabı dahil, güvenli bir internet sitesine erişirken kullandığınız [**şifrelemenin**](/tr/glossary#Encryption) türü, burada tartışılan açık anahtar [**şifrelemesi**](/tr/glossary#Encryption) türüne göre daha az şüpheli görülür. Bazı durumlarda, bu tür [**şifrelenmiş**](/tr/glossary#Encryption) veri içeren e-postalar ele geçirilir ya da [**şifrelenmiş**](/tr/glossary#Encryption) e-postalar açık bir foruma gönderilirse, bu durum, bunları gönderen kişiyi mesajın içeriğinden bağımsız olarak, suçlu durumuna düşürebilir. Bazen mesajınızın gizliliği ile dikkat çekmeme gereksinimi arasında seçim yapmak zorunda kalabilirsiniz.

### Bir Mesajı Şifrelemek ve Kimliğini Doğrulamak ###

Açık anahtar [**şifrelemesi**](/tr/glossary#Encryption) ilk bakışta karmaşık görünebilir ama temel ilkeleri anladığınızda oldukça kolaydır ve araçları kullanmak da zor değildir. Basit, kullanıcı dostu ve taşınabilir **gpg4usb** programı, internete bağlı olmasanız bile e-posta mesajlarını ve dosyaları şifreleyebilir.

<div class="getstarted" markdown="1">
**Uygulama**: [***Taşınabilir gpg4usb – E-posta metinleri ve dosya şifreleme programı rehberi***](/en/gpg4usb_portable) ile uygulamaya başlayın
</div>

**Mozilla** [**Thunderbird**](/tr/glossary#Thunderbird) e-posta programı [**Enigmail**](/tr/glossary#Enigmail) adı verilen uzantısıyla birlikte e-posta mesajlarını şifrelemede ve onların şifresinin çözülmesinde kolayca kullanılabilir.

<div class="getstarted" markdown="1">
**Uygulama**: [***Enigmail ve GPG ile Thunderbird - Güvenli E-posta İstemcisi Rehberi***](/en/thunderbird_main) ile uygulamaya başlayın
</div>

[**VaultletSuite 2 Go**](/tr/glossary#VaultletSuite), ücretsiz şifrelenmiş e-posta programını kullanmak, programı sağlayan şirkete güvenmeye ve sizin için işlerin bir kısmını yapmalarına izin vermeye istekliyseniz, **Thunderbird**’den bile daha kolaydır.

<div class="getstarted" markdown="1">
**Uygulama**: [***VaultletSuite 2Go – Güvenli E-posta İstemcisi Rehberi***](/en/vaultletsuite_main) ile uygulamaya başlayın
</div>

E-postanızı otantikleştirmek iletişim güvenliğinin bir başka önemli boyutudur. İnternet bağlantısına ve doğru araçlara sahip olan herhangi biri sizinkiyle aynı olan sahte bir e-posta hesabından mesaj göndererek sizi taklit edebilir. Buradaki tehlike alıcının bakış açısından ele alındığında daha görünürdür. Güvenilir bir bağlantıdan geliyormuş gibi görünen ama gerçekte etkinliklerinizi kesintiye uğratmak ya da örgütünüz hakkındaki hassas bilgileri öğrenmek isteyen biri tarafından gönderilen bir e-postanın ortaya koyduğu tehdidi hayal edin.

E-postayla yazıştığımız kişiyi görmeyeceğimizi ya da duyamayacağımızı göz önünde bulundurduğumuzda, kişinin kimliğini doğrulamak için genellikle göndericinin adresine başvururuz, bu nedenledir ki sahte e-postalarla bu kadar kolay aldatılırız. Açık anahtar [**şifrelemesine**](/tr/glossary#Encryption) dayanan [**dijital imzalar**](/tr/glossary#Digital_signature), bir mesaj gönderirken birinin kimliğini doğrulamanın daha güvenli bir aracını sağlar. [***Portable gpg4usb***](/en/gpg4usb_portable) rehberi ya da [***Thunderbird Rehberi***](/en/thunderbird_main)’nin [***Enigmail’la birlikte Thunderbird nasıl kullanılır***](/en/thuderbird_encryption) kısmı bunun nasıl yapılacağını ayrıntılarıyla açıklar.

<div class="background" markdown="1">
**Pablo**: Bir meslektaşım benim e-posta adresimden gönderilen ama aslında benim göndermediğim bir e-posta almıştı. Sonunda bunun sadece bir spam olduğuna karar verdik ama şimdi yanlış zamanda, yanlış bir kişinin e-posta kutusunda sahte bir e-postanın belirmesinin ne büyük bir hasar meydana getirebileceğini hayal edebiliyorum. Bu tür şeylerin dijital imza ile önlenebilindiğini duydum ama nedir bu dijital imza?
			
**Claudia**: Bir dijital imza, mektubunu taşıyan zarfın üzerindeki bal mumundan mühüre benzer ancak dijital imza taklit edilemez. Bu, mesajın gerçek göndericisinin sen olduğunu ve mesajın, alıcısına erişinceye dek değiştirilmediğini kanıtlar.
</div>


