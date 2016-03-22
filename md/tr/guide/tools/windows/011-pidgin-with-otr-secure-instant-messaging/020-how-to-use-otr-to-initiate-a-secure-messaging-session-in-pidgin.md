

---

lang: tr
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Use OTR to Initiate a Secure Messaging Session in Pidgin

---

Bu sayfadaki kısımların listesi:

- [**3.0 Pidgin ve OTR Hakkında**](#3.0)
- [**3.1 Pidgin-OTR Eklentisi Nasıl Yapılandırılır?**](#3.1)
- [**3.2 İlk Adım – Bir Özel Anahtar Nasıl Oluşturulur ve Parmak İzi Nasıl Görüntülenir?**](#3.2)
- [**3.3 İkinci Adım – Bir Mesajlaşma Oturumu Nasıl Onaylanır?**](#3.3)
- [**3.4 Üçüncü Adım – İrtibatta Olduğunuz Kişinin Kimliği Nasıl Teyit Edilir?**](#3.4)


<a name="3.0"></a>
## 3.0 Pidgin ve OTR Hakkında ##

Gizli ve güvenli **Anlık Mesajlaşma** oturumları açabilmeniz için hem sizin hem de irtibatta olduğunuz kişinin **OTR** eklentisini yapılandırması gerekir. **OTR** eklentisi her iki katılımcının da uygun bir şekilde bu eklentiyi yükleyip yapılandırdığını otomatik olarak saptar. 

**Not**: **OTR’yi** kurmamış ya da yapılandırmamış olduğunuz bir arkadaşınıza özel bir sohbet talebinde bulunursanız, otomatik olarak **OTR’yi** nereden bulabileceğini açıklayan bir mesaj yollanır.

<a name="3.1"></a>
## 3.1 Pidgin-OTR Eklentisi Nasıl Yapılandırılır? ##

**OTR** eklentisini etkinleştirmek için aşağıdaki  adımları takip edin: 

**1. Adım**. ![](/sbox/screen/pidgin-tr/13.png)’e **çift tıklayarak**, ya da **Başlangıç > Programlar > Pidgin’i** seçerek **Pidgin’i** ve *Arkadaş Listesi* penceresini açın (Lütfen Şekil 1’e bakın).

**2. Adım**. *Araçlar* menüsünü **Açın** ve sonrasında *Eklentiler* öğesini aşağıdaki gibi **seçin**:

![](/sbox/screen/pidgin-tr/40.png)

*Şekil 1:  Araçlar menüsünden Eklentiler öğesi seçilmiş Arkadaş Listesi penceresi*

Bu *Eklentiler* penceresini aşağıdaki gibi açacak:

**3. Adım**. Pencereyi *Off-the-Record Messaging'a* doğru **aşağı kaydırın**, sonrasında ilintili kutuyu **işaretleyin**. 

![](/sbox/screen/pidgin-tr/41.png)

*Şekil 2: Off-The-Record Messaging'in seçili olduğuğu Pidgin Eklentiler penceresi*

**4. Adım**. ![](/sbox/screen/pidgin-tr/42.png)’i **tıklayarak** *Off-the-Record Mesajlaşma* pencerelerini yapılandırmaya başlayın.

Etkin bir şekilde özel ve güvenli **anlık mesajlaşma** oturumları açabilmek için **OTR’nin** yapılandırılmasının temelde 3 adımı vardır, ve bunlar aşağıda açıklanmıştır.

- **Birinci Adım**: Bu hesabınıza özgün bir özel anahtar oluşturmayı ve onun parmak izini görüntülemeyi içerir.

Bir sonraki adımlar *anlık mesajlaşma* oturumunu güvenlik altına almayı ve arkadaşlarınızın kimliğini doğrulamayı içerir..

- **İkinci Adım**: Bu bir katılımcının o anda çevrimiçi olan diğer katılımcıya özel ve güvenli bir sohbet oturumu açma talebini içerir.

- **Üçüncü adım** **Pidgin** *arkadaşınızın* *kimliğini doğrulamayı* içerir. (**Not**: **Pidgin’de**, **anlık mesajlaşma** oturumlarıyla irtibat kurmaya çalıştığınız herkes bir arkadaştır.) Bir arkadaşın kimliğini doğrulamaya **Pidgin’de** **kimlik doğrulama** denir.  Bu arkadaşınızın *kesinlikle* iddia ettiği kişi olduğunu tesbit etmek demektir.  

<a name="3.2"></a>
## 3.2 İlk Adım – Bir Özel Anahtar Nasıl Oluşturulur ve Parmak izi nasıl Görüntülenir?##

**Pidgin’de** güvenli sohbet oturumları ilgili hesap için bir *özel anahtar* oluşturmakla etkinleştirilebilir. *Off-the-Record* yapılandırma penceresi *Yapılandırma* ve *Tanınan pakmak izleri* sekmeleriyle ayrılmıştur. *Yapılandırma* sekmesi  her bir hesap için bir *özel anahtar* oluşturmak için ve belirli *OTR* seçeneklerini ayarlamak için kullanılır. *Tanınan parmak izleri* sekmesi  irtibat kurduğunuz kişilerin parkmak izlerinin bir listesini barındırır. Özel bir sohbet yapmak istediğiniz her bir arkadaşınız için bir anahtarınız olmalı.

![](/sbox/screen/pidgin-tr/43.png)

*Şekil 3: Yapılandırma sekmesi açılmış Off-the-Record Mesajlaşma ekranı*

**1. Adım**. Gizliliğinizi olabildiğince artırmak için *Gizli mesajlaşmayı etkinleştirin*, *gizli mesajlaşmayı otomatik olarak başlat*, ve *OTR sohbetlerini arşivleme* seçeneklerini Şekil 3’teki gibi **işaretleyin**.

**2. Adım**.![](/sbox/screen/pidgin-tr/44.png)’i tıklayarak güvenli anahtarınızı oluşturmaya başlayın; size özel anahtarın oluşturulduğunu belirten aşağıdakine benzer bir mesaj belirecek:

![](/sbox/screen/pidgin-tr/45.png)

*Şekil 4: Özel anahtar oluşturuluyor onaylama kutusu*

**Not**: Arkadaşınız da kendi hesabı için aynı adımları takip etmeli

**3. Adım**. Aşağıdakine benzer bir özel anahtar oluşturulduğunda![](/sbox/screen/pidgin-tr/37.png)’i **tıklayın**.

![](/sbox/screen/pidgin-tr/46.png)

*Şekil 5: OTR motoru tarafından oluşturulan bir anahtarın örnek bir parmak izi *

**Önemli**: Şimdi hesabınız için bilgisayarınızda bir özel anahtar yarattınız. Bu konuşmalarınızı şifrelemek için kullanılacak. Böylece sohbet oturumlarınız gözlemlense bile kimse mesajlarınızı okuyamayacak. Parmak izi *Şekil 5’te* gösterildiği gibi belirli bir hesap için bir anahtarı tanımlamaya yarayan uzun bir harf ve rakamlar serisidir.

**Pidgin** sizin ve arkadaşlarınızın parmak izlerini otomatik olarak kaydeder, böylelikle sizin bunları hatırlamanıza gerek kalmaz. **Pidgin’i** yeniden kurar ya da başka bir bilgisayara geçerseniz, ya anahtarınızı yeniden oluşturmaki ve arkadaşlarınızın kimliğini yeniden doğrulamalısınız, ya da anahtarınızı ve de arkadaşlarınızın parmak izlerini yeni bilgisayara aktarmalısınız. Bunu yapmak için %APPDATA%\.purple (Linux ya da Mac’de  ~/.purple) klasörünün içeriğini yeni bilgisayardaki benzer klasöre kopyalamanız gerekir.

<a name="3.3"></a>
## 3.3 İkinci Adım – Bir Mesajlaşma Oturumu Nasıl Onaylanır? ##

**1. Adım**. Şu an çevrimiçi olan bir arkadaşın hesabı üstüne **çift tıklayarak** yeni bir **anlık mesajlaşma** oturumu açın. İkiniz de **OTR** eklentisini uygun bir şekilde kurmuş ve yapılandırmışsanız, sohbet pencerenizin sağ alt köşesinde yeni bir **OTR** düğmesinin belirdiğini fark edeceksiniz. 

![](/sbox/screen/pidgin-tr/47.png)

*Şekil 6: Siyahla çerçevelenmiş OTR ikonu görülen bir Pidgin mesajlaşma penceresi*

**2. Adım**. ![](/sbox/screen/pidgin-tr/48.png)’ı **tıklayarak** açılan menüyü etkinleştirin ve sonrasında *Gizli oturum başlat* öğesini aşağıdaki gibi **seçin**:

![](/sbox/screen/pidgin-tr/49.png)

*Şekil 7:Gizli oturum başlat öğesi seçilmiş olan menü*

*Pidgin anlık mesajlaşma pencereniz bundan sonra şuna benzeyecek:*

![](/sbox/screen/pidgin-tr/50.png)

*Şekil 8: Unverified düğmesini gösteren Pidgin anlık mesajlaşma penceresi*

**Not**: **Pidgin** arkadaşınızın **anlık mesajlaşma** programıyla iletişime otomatik olarak başlar ve özel ve güvenli sohbet oturumlarını başlatmaya yeltendiğinizde mesajları otomatik olarak gönderir. Bunun sonucunda![](/sbox/screen/pidgin-tr/48.png) **OTR** düğmesi ![](/sbox/screen/pidgin-tr/51a.png)’a döner, bu da şu anda arkadaşınızla şifreli bir görüşmede olduğunuzu gösterir.

**Uyarı**! Bu görüşme şimdi güvenli olsa da arkadaşınızın kimliği henüz *teyit edilmedi*. Dikkat edin: arkadaşınız sandığınız kişi aslında arkadaşınızmış *gibi davranan* başka biri olabilir.

<a name="3.4"></a>
## 3.4 Üçüncü Adım – İrtibatta Olduğunuz Kişinin Kimliği Nasıl Teyit Edilir? ##

**Pidgin** arkadaşınızın kimliğinden emin olabilmek için üç metoddan birini kullanabilirsiniz, 1) önceden belirlediğiniz gizli bir kod kullanabilirsiniz, 2) cevabını sadece ikinizin bildiği bir soru sorabilirsiniz, 3) farklı bir iletişim metoduyla anahtarlarınızın parmak izlerini elle kontrol edebilirsiniz.

### Gizli Kod Metodu ###

Önceden ya yüzyüze bir konuşmada ya da başka bir iletişim vasıtasıyla (telefon, [**Jitsi**](/en/jitsi)’de sesli sohbet, ya da cep telefonu mesajları gibi) bir kod kelime ya da cümleye karar verebilirsiniz. İkiniz de aynı kodu girdiğinizde oturumunuz özgünlüğü teyit edilir.

**Not**: **OTR** gizli kod tanıma özelliği büyük (A,B,C) ve küçük (a,b,c,) harflere duyarlıdır. Gizli kodunuzu belirlerken bunu aklınızda tutun!

**1. Adım**. Sohbet penceresindeki *OTR* düğmesini **tıklayın**, ve aşağıda göründüğü gibi *Arkadaşının kimliğini doğrula’yı* seçin:

![](/sbox/screen/pidgin-tr/52.png)

*Şekil 9: Arkadaşının kimliğini doğrula öğesi seçilmiş Teyit edilmemiş menüsü*

Bu sizi doğrulama metodunu girmeye davet eden *Arkadaşının kimliğini doğrula* penceresini etkinleştirecek.

**2. Adım**.  ![](/sbox/screen/pidgin-tr/53.png)’ı tıklayın ve aşağıdaki gibi *Paylaşılan Sır’ı* seçin: 

![](/sbox/screen/pidgin-tr/54.png)

*Şekil 10: Aşağı açılır listesi gösterilen Arkadaşının kimliğini doğrula penceresi* 

**3. Adım**. Gizli kodu aşağıdaki gibi **girin**:

![](/sbox/screen/pidgin-tr/55.png)

*Şekil 11: Paylaşılan Sır penceresi* 

**4. Adım**. ![](/sbox/screen/pidgin-tr/56.png)’i **tıklayarak** aşağıdaki ekranı etkinleştirin:

![](/sbox/screen/pidgin-tr/58.png)

*Şekil 12: Kurmaca bir irbitat için Arkadaşının Kimliğini Doğrula penceresi*

**Not**: *Bu anda arkadaşınız Şekil 13’te görülen pencereyi görecek ve aynı kodu girmesi gerekecek. Eğer kodlar birbirine uyarsa, oturumunuz teyit edilmiş olacak.*

![](/sbox/screen/pidgin-tr/57.png)

*Şekil 13: Kurmaca bir irtibat için Arkadaşının Kimliğini Doğrula penceresi*

Oturum teyit edildiğinde *OTR* düğmesi ![](/sbox/screen/pidgin-tr/51.png)’e dönecek. Bu haliyle oturumunuz güvenli ve gerçekten arkadaşınızla konuştuğunuzdan emin olabilirsiniz.

### Soru Cevap Metodu ###

Birbirinizin kimliğini doğrulamanın bir başka yolu da soru cevap metodudur. Bir Soru ve cevabını yaratın. Soruyu okuduktan sonra arkadaşınız *tamamen* aynı cevabı verebilmeli, ve cevaplar birbirini tutarsa, kimlikleriniz otomatik olarak doğrulanacak. 

**1. Adim**. Etkin olan bir ileti penceresinde *OTR* menüsünü **tıklayarak** ilgili açılan menüyü etkinleştirin, ve sonrasında *Arkadaşının Kimliğini Doğrula* öğesini **seçin** (lütfen *9. Şekil’e* bakın).
.
![](/sbox/screen/pidgin-tr/50.png)

*Şekil 14: OTR ikonu görünen bir Pidgin sohbet penceresi*

**2. Adım**. Aşağı açılır menüyü **tıklayın** ve *Soru Cevap* öğesini aşağıdaki gibi **seçin**:

![](/sbox/screen/pidgin-tr/60.png)

*Şekil 15: Arkadaşının kimliğini doğrula ekranı*

**3. Adım**: Bir soru ve cevabını **girin**. Bu soru arkadaşınıza gönderilecek.

![](/sbox/screen/pidgin-tr/61.png)

*Şekil 16: Soru Cevap ekranı*

Arkadaşınızın cevabı sizinkiyle aynıysa, ikinizin de kimliği doğrulanmış, ya da her iki katılımcı da olduğunu iddia ettiği kişi demektir!

Oturumunuzun özgünlüğü teyit edildiğinde *OTR* düğmesi ![](/sbox/screen/pidgin-tr/51.png)’a dönecek. Böylelikle oturumunuz güvenli olacak ve arkadaşınızın kimliğinden emin olabileceksiniz..

###Elle parmak izi kontrolü ###

Birbirinizin kimliğini doğrulamanın üçüncü yolu parmak izi kontrolüdür. Bu metodla görünür parmak izlerinizi başka bir iletişim kanalından (güvenli e-posta ya da sesli görüşme gibi) teğiş tokuş etmeniz gerekir (aşağıdaki Şekil 17’ye bakınız). Değiş tokuş edilen parmak izleri aynı ise, *Bunun gerçekten de doğru parkmak izi olduğunu **doğruladım’ı*** tıklayarak oturumun özgünlüğünü **teyit edebilirsiniz.**

![](/sbox/screen/pidgin-tr/79.png)

*Şekil 17: Elle parmak izi kontrolü ekranı*

**Arkadaş listesi > Araçlar > Eklentiler > Off the Record Messaging > Eklenti > Eklentiyi Yapılandır’ı** **seçtiğinizde**, *Tanınan parmak izleri* sekmesi arkadaşınızın hesabını ve kimliğinin doğrulandığını gösterir. 

![](/sbox/screen/pidgin-tr/62.png)

*Şekil 18: Tanına Parmak İzleri sekmesi görünen Off-the-Record Mesajlaşma ekranı*

Tebrikler! Şimdi gizli bir şekilde sohbet edebilirsiniz. Arkadaşınızla bir sonraki sohbetinizde (aynı bilgisayarları kullanarak), sadece güvenli bir bağlantı talep etmeniz ve arkadaşınızın kabul etmesi yeterli olacak (yukarıdaki Şekil 7 gibi). Oturumunuz böylelikle teyit edilmiş olacak.

