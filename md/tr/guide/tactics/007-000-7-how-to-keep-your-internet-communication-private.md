

---

lang: tr
community: guide
type: tactics
legacy: True
child: False
weight: 007
title: 7. How to keep your Internet communication private

---

E-postanın ve anlık mesajlaşmanın kullanım kolaylığı, düşük maliyeti ve esnekliği internete en sınırlı erişimi olan kişiler ve kuruluşlar için bile bunları aşırı değerli kıldı. Daha hızlı ve güvenli bağlantıları olanlar için [*Jitsi*](https://jitsi.org/), [*Skype*](/tr/glossary#Skype) ve diğer *IP Üzerinden Ses* [*VoIP*](/tr/glossary#VoIP) araçları gibi yazılımlar da bu özellikleri paylaşır. Ne yazık ki geleneksel iletişim araçlarına alternatif olarak gelen bu dijital araçlara hassas bilgilerin gizliliğini korumak hususunda her zaman güvenilemez. Postayla gönderilen mektuplar, telefonla yapılan aramalar ve yazılı mesajlar da saldırıya açıktır; özellikle yetkililerin takibinin hedefi olanlar tarafından kullanıldığında.  

Dijital, internet-tabanlı iletişim teknikleriyle daha geleneksel yöntemler arasındaki bir önemli farklılık, ilkinin kendi güvenlik düzeyinizi belirlemenize çoğu zaman izin vermesidir. Güvenli olmayan yöntemlerle e-postalar, anlık mesajlar ve [*VoIP*](/tr/glossary#VoIP) gönderileri göndermek, mektuplardan ve telefon görüşmelerinden neredeyse kesinlikle daha az gizlidir. Kısmen bu, birkaç güçlü bilgisayarın büyük miktardaki dijital bilgi içinden göndericileri, alıcıları ve belirli anahtar sözcükleri tespit etmek için otomatik olarak tarayabilmesindendir. Geleneksel iletişim kanalları üzerinden aynı düzeyde bir takibi gerçekleştirmek için çok daha büyük kaynaklar gerekir. Bununla beraber belirli önlemleri alırsanız tersi de doğrudur. İnternet iletişim araçlarının esnekliği ve modern [*şifrelemenin*](/tr/glossary#Encryption) gücü, sadece ulusal ordu ve istihbarat örgütleri için mümkün olan bir gizlilik düzeyini günümüzde sağlayabilir.

Burada verilen tavsiyeleri izleyerek ve bu bölümde ele alınan yazılımları inceleyerek iletişim güvenliğinizi büyük oranda artırabilirsiniz. [*RiseUp*](/tr/glossary#RiseUp) e-posta hizmeti, [*Pidgin*](/tr/glossary#Pidgin) anlık mesajlaşma programı için Off the Record [*OTR*](/tr/glossary#OTR)  (Kayıt Dışı) eklentisi, Mozilla [*Firefox*](/tr/glossary#Firefox) ve Mozilla [*Thunderbird*](/tr/glossary#Thunderbird) e-posta sunucusu için [*Enigmail*](/tr/glossary#Enigmail) eklentilerinin hepsi mükemmel araçlardır. Bununla beraber bunları kullanırken verili bir haberleşmenin gizliliğinin hiçbir zaman yüzde yüz garanti edilemeyeceğini aklınızda bulundurmalısınız. Her zaman göz önünde bulundurmadığınız bazı tehditler bulunur; diyelim bilgisayarınızda bir [*keylogger*](/tr/glossary#Keylogger) bulunması, kapınızı dinleyen biri, dikkatsiz bir e-posta alıcısı ya da tamamen farklı bir olasılık... Bu bölümün amacı, aklınıza gelmeyen tehditleri bile azaltmak için size yardımcı olmaktır. Ancak bu bölümde bunu yaparken, bazılarının tercih ettiği ‘kamuya açık etmek istemediğin hiçbir bilgiyi internetten göndermemelisin’ seçeneğinden kaçınacağız. 


<div class="background" markdown="1">
Claudia ve Pablo, Güney Afrika ülkelerinden birindeki bir insan hakları STK’siyle birlikte çalışmaktadır. Bölgede ordu tarafından işlenen insan hakları ihlalleri konusunda aylar boyunca tanıklıklar topladıktan sonra Claudia ve Pablo elde ettikleri verileri korumak için adımlar atmaya başlamıştır. Sadece ihtiyaçları olan bilgiyi ellerinde tuttular ve bu bilgiyi, birçok fiziksel konumda yedeklenmiş bir TrueCrypt bölmesinde depoladılar. Bir raporda bu tanıklıkların belirli bölümlerini yayınlamaya hazırlanırken bir başka ülkedeki meslektaşlarıyla hassas bilgileri tartışmaları gerektiğini fark ettiler. Her ne kadar adları ve konumları belirtmemek konusunda hemfikirlerse de bu konu üzerinde yapılacak olan e-posta ve anlık mesajlaşma iletişimlerinin güvenli olmasından emin olmak istemektedirler. Claudia iletişim güvenliğinin önemini ele almak amacıyla bir toplantı için çağrı yaptıktan sonra ofistekilerin bir sorusu olup olmadığını sordu.
</div>


### Bu bölümden ne öğrenebilirsiniz ###

- Birçok webmail ve anlık mesajlaşma hizmetinin neden güvenli olmadığını 
- Yeni ve daha güvenli bir e-posta hesabının nasıl oluşturulacağını 
- Halihazırdaki e-posta hesabınızın güvenliğini nasıl arttıracağınızı 
- Güvenli bir anlık mesajlaşma hizmetini nasıl kullanılacağını 
- Birilerinin e-posta hesabınıza eriştiğini düşünüyorsanız ne yapılabileceğini 
- Bir e-posta alıcısının kimliğinin nasıl doğrulanacağını

