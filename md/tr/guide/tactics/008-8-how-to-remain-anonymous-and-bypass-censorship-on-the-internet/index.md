

---

lang: tr
community: guide
type: tactics
legacy: True
child: False
weight: 008
title:  8. How to remain anonymous and bypass censorship on the Internet

---

Tüm dünyada birçok ülke, ülkelerindeki internet kullanıcılarının belirli sitelere ve internet hizmetlerine erişimini engelleyen yazılımlar kurdu. Şirketler, okullar, ve halka açık kütüphaneler; çalışanlarını, öğrencilerini ve abonelerini rahatsız edici ya da zararlı olduğunu düşündükleri materyallere karşı korumak için sık sık benzer yazılımlar kullanır. Bu türden bir filtrleleme teknolojisinin bir dizi farklı türü vardır. Bazı filtreler bir siteyi [*IP adresi*](/tr/glossary#IP_address) üzerinden engellerken diğerleri belirli [*alan adlarını*](/tr/glossary#Domain_name) kara listeye alır ya da tüm şifrelenmemiş internet iletişimini belirli anahtar sözcüklere bakarak tarar.

Hangi filtreleme yönteminin mevcut olduğundan bağımsız olarak, ülkenizin dışındaki aracı bilgisayarlara sizin için engellenmiş hizmetlere erişmesi için itimat ederek, bu filtreleme yöntemlerini aşmak neredeyse her zaman olanaklıdır. Bu süreç, [*sansür aşma*](/tr/glossary#Circumvention) olarak adlandırılır ve aracı olan bilgisayarlar da [*proxy*](/tr/glossary#Proxy)'ler olarak adlandırılır. [*Proxy*](/tr/glossary#Proxy)’lerin de farklı türleri vardır. Bu bölüm önce, çoklu-proxy anonimlik ağları üzerine kısa bir tartışmayı ele alacak; ardından da temel [*sansür aşma*](/tr/glossary#Circumvention) [*proxy*](/tr/glossary#Proxy)’lerine ve onların nasıl çalıştığına dair daha ayrıntılı bir açıklamaya geçecektir.

İnternet filtrelerini aşmak için her iki yöntem de etkilidir ancak ilki, internet etkinliklerinizi olabildiğince anonim kılmak için internet hızınızdan ödün vermeye istekliyseniz yerinde bir seçimdir. [*Proxy*](/tr/glossary#Proxy)’nizi yöneten kişilere ve kuruluşlara güveniyorsanız ve performans sizin için anonimlikten daha önemliyse, temel bir [*sansür aşma*](/tr/glossary#Circumvention) [*proxy*](/tr/glossary#Proxy)’si size daha iyi bir hizmet sunabilir.

### Arka plan senaryosu ###
<div class="background" markdown="1">
Mansour ve Magda Arapça konuşulan bir ülkede yaşayan kardeşlerdir. Anonim olarak insan hakları ihlallerini yayınladıkları ve siyasal değişim için bir kampanya yürüttükleri bir blogları vardır. Ülkelerindeki yetkililer, web sitelerinin sunucusu başka bir ülkede konuşlandığından sitelerini kapatamamıştır; ancak diğer etkinliklerinden yola çıkarak blog’un yöneticileri hakkında sık sık daha çok şey öğrenmeye çalışmaktadırlar.
Mansour ve Magda yetkililerin güncellemelerini izleyebileceğinden ve kim olduklarını bulabileceklerinden kaygı duymaktadır. Dahası sadece web sitesini güncellemeye devam edebilmek için değil; aynı zamanda kendi ülkelerindeki okuyucularına sansür aşmak için gerekli uygun önerilerde bulunmak için, hükümetin eninde sonunda web sitelerini filtreleyeceği güne hazırlanmak istemektedirler.
</div>

### Bu bölümden ne öğrenebilirsiniz ###
- Kendi ülkenizin içinden engellenmiş bir web sitesine nasıl erişileceğini
- Ziyaret ettiğiniz web sitelerinin konumunuzu bilmesini nasıl engelleyeceğinizi
- Sizin [*ISP*](/tr/glossary#ISP)’nizin ya da ülkenizdeki herhangi bir izleme/denetleme organının, sizin hangi web sitesini ya da internet hizmetini ziyaret ettiğinizi tespit etmesini nasıl engelleyeceğinizi

