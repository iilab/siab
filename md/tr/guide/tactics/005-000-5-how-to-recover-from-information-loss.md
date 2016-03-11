

---

lang: tr
community: guide
type: tactics
legacy: True
child: False
weight: 005
title: 5. How to recover from information loss

---

Dijital verilerin depolanmasının ya da transferinin her yeni yöntemi; söz konusu bilgilerin kaybedilmesinin, çalınmasının ya da tahrip edilmesinin birçok yeni yolunu beraberinde getirmeye eğilimlidir. Yılların emeği; hırsızlık, anlık dikkatsizlik, bilgisayar donanımlarına el konulması sonucunda ya da sadece dijital depolama teknolojisi doğası gereği kırılgan olduğundan bir anda ortadan kaybolabilir. Bilgisayar destekli çalışan profesyoneller arasında yaygın bir deyiş vardır: &quot;Bu, verilerini *kaybedip kaybetmeyeceğin* sorunu değil; *ne zaman* kaybedeceğin sorunudur.&quot; Öyle ise bu sizin başınıza geldiğinde, güncel bir yedeğe ve iyi test edilmiş geri yükleme araçlarına sahip olmanız çok önemlidir. Bir yedekleme sisteminin öneminin size hatırlatıldığı gün, genelde, bir yedekleme sistemine sahip olmaya ihtiyaç duyduğunuz günün ertesi günüdür.

Etkili bir yedekleme politikası oluşturmak, her ne kadar güvenli bilgisayar kullanımının en temel unsuru olsa da göründüğü kadar kolay değildir. Etkili bir yedekleme politikası oluşturmak, bir dizi nedenden dolayı planlama sırasında önünüze ilave engeller çıkarabilir: Özgün verileri ve yedekleri farklı fiziksel konumlara kaydetme gerekliliği, yedeklerin gizli tutulmasının önemi, her biri kendi taşınabilir depolama aygıtına sahip olan ve birbirleriyle bilgi paylaşan farklı insanlar arasında koordinasyonun güçlüğü... Yedekleme ve dosya kurtarma taktiklerine ek olarak, bu bölüm iki özgül araca işaret etmektedir, [*Cobian Backup*](/tr/glossary#Cobian_Backup) ve [*Recuva*](/tr/glossary#Recuva). 

### Arka plan senaryosu ###
<div class="background" markdown="1">Elena Rusça konuşulan bir ülkede, bölgedeki yasa dışı ağaç kesiminin hangi boyutlara ulaştığını göstermek için fotoğrafların, videoların, haritaların ve öykülerin sunumuna dayanan bir web sitesi oluşturmaya başlamış bir çevrecidir. Yıllardır ağaçların kesimi hakkında belgeler, medya dosyaları ve coğrafi bilgiler toplamaktadır ve bunların birçoğu çalıştığı STK’nin ofisindeki Windows işletim sistemli eski bir bilgisayarda depolanmaktadır. Bu bilgiler çevresinde bir web sitesi tasarlarken, bu bilgilerin korunmasının önemini fark etmeye başlar. Özellikle her şeyi web sitesine kopyalamadan önce bilgisayarının zarar görme ihtimali onu endişelendirir. Kurumunun diğer üyeleri de bu bilgisayarı zaman zaman kullanmaktadır. Çalışmasını içeren klasörü biri yanlışlıkla silerse bu klasörü nasıl kurtarabileceğini öğrenmek istemektedir. Yeğeni Nikolai’dan bir yedekleme stratejisi geliştirmek için yardım ister.
</div>

### Bu bölümden ne öğrenebiliriz ###

- Bilgilerinizi nasıl düzenler ve yedeklersiniz 
- Yedeklerinizi nerede muhafaza etmelisiniz
- Yedeklerinizi güvenle nasıl yönetebilirsiniz 
- Yanlışlıkla silinen dosyaları nasıl kurtarırsınız

