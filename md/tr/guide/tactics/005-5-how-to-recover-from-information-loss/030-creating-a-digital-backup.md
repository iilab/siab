

---

lang: tr
community: guide
type: tactics
legacy: True
child: True
weight: 3
depth: 3
title: Creating a digital backup

---

Burada ele alınan veri tiplerinden bir yedekleme stratejisi oluştururken, insanların hakkında en çok endişe duydukları veri tipi ‘elektronik belgeler’dir. Bu kavram her ne kadar muğlaksa da genellikle, kaydını kendinizin tuttuğu, ya çift tıklayarak ya da belirli bir uygulamanın dosya menüsünü kullanarak, manüel olarak açtığınız dosyaları işaret eder. Özellikle, diğer örneklerin yanı sıra metin dosyalarını, sözcük işlem belgelerini, sunumları, pdf’leri ve veri depolarını kapsar. Örneğin, e-posta mesajlarının aksine, elektronik belgeler internet üzerinden uzaktaki kopyalarıyla senkronize edilmezler. 

Elektronik belgeleri yedeklerken program veritabanlarını da yedeklemeyi hatırlamalısınız. Örneğin bir takvim uygulaması ya da bir elektronik adres defteri kullanıyorsanız, bu programların verilerini depolamak için kullandığı klasörü de bulmanız gerekir. Umalım ki bu veritabanları elektronik belgelerinizle aynı konumda olsun, bunlar Windows tabanlı bilgisayarlarda genellikle *Belgelerim* klasörünün altında saklanır. Durum bu değilse, uygun klasörleri düzenli yedeklemenize eklemeniz gerekir. 

[*Thunderbird*](/tr/glossary#Thunderbird) gibi uygulamalar tarafından depolanan e-postalar bir programın veri tabanına özel bir örnektir. Bir e-posta programı kullanıyorsanız, özellikle de mesajınızın sunucuda bir kopyasını depolayamıyorsanız ya da depolamak istemiyorsanız, o halde e-posta veri tabanınızın düzenli yedeklemelerinize dahil olduğundan emin olmalısınız. Görüntü ve video dosyalarınızı, onlarla nasıl etkileşim halinde olduğunuza bağlı olarak, bir programın veri tabanındaki elektronik belgeler ya da nesneler olarak düşünebilirsiniz. Örneğin Windows Media Player ve iTunes gibi uygulamalar, veri tabanları gibi işler. Bu gibi programları kullanıyorsanız, yönetimine yardımcı oldukları gerçek medya dosyalarını nereye depoladıklarını öğrenmek için sabit diskinizi taramanız gerekebilir. 


### Depolama aygıtları ###

Elektronik belgelerinizi yedeklemeden önce, ne tür bir depolama aygıtı kullanacağınıza karar vermelisiniz.

**USB bellekler** - USB bellekler ucuz olabilir ve geniş kapasiteler sunabilir. Defalarca silmesi ya da üzerine yeniden yazması kolaydır. USB belleklerin, kullanım sıklığına ve biçimine bağlı olarak, sınırlı ömürleri vardır ama kullanım süreleri genellikle yaklaşık olarak 10 yıl olarak tahmin edilir.

**Kompakt Diskler (CD’ler)** CD’ler yaklaşık 700 Megabyte (MB) veri depolar. CD’lere yapılacak yedekleme için bir [*CD yazıcısına*](/tr/glossary#CD_burner) ve boş disklere gereksiniminiz olacaktır. Bir CD’yi silmek ve kaydettiğiniz dosyaları yenilemek için bir CD-RW yazıcısına ve yeniden yazılabilir CD’lere gereksinimiz olacaktır. Şimdilerde Windows XP dahil, belli başlı tüm işletim sistemleri, CD’ler ve CD-RW’ler yazabilen dahili bir yazılım içermektedir. Bu disklere yazılan bilgilerin beş ya da on yıl sonra bozulmaya başlayabileceğini aklınızda bulundurmalısınız. Bu süreden daha uzun bir süre bir yedekleme depolamaya gereksinimiz varsa bu CD’leri zaman zaman yeniden oluşturmanız, özel 'uzun ömürlü' diskler satın almanız ya da farklı bir yedekleme yöntemi kullanmanız gerekir.

**Dijital Video Diskler (DVD’ler)** - DVD’ler 4.7 Gigabyte’a (GB) kadar veri depolar. DVD’ler de CD’lere benzer şekilde çalışır ama biraz daha pahalı ekipmanlar gerektirir. Bir DVD ya da [*DVD-RW yazıcısına*](/tr/glossary#CD_burner) uygun disklere gereksinimiz olacaktır. Bir CD’de olduğu gibi normal DVD’ye yazılan veri, eninde sonunda silinmeye başlayacaktır.

**Uzak sunucu** - İyi düzenlenmiş bir ağ yedekleme sunucusu neredeyse sınırsız bir kapasiteye sahip olabilir ama internet bağlantınızın hızı ve istikrarı bunun gerçekçi bir seçenek olup olmayacağını belirleyecektir. Ofisinizde bir yedekleme sunucusu çalıştırmak her ne kadar internetten bilgi kopyalamaktan daha hızlı olsa da, önemli verilerinizin bir kopyasını iki farklı fiziksel konumda saklama gereksiniminizi ihlal eder. İnternette ücretsiz depolama hizmetleri bulunmaktadır ama bilgilerinizi çevrimiçi hale getirme riski üzerinde dikkatle düşünmelisiniz ve bilmediğiniz ya da güvenmediğiniz kuruluşlar ya da kişiler tarafından işletilen sunuculara yedeklemelerinizi yüklemeden önce onları daima şifrelemelisiniz. Birkaç örnek için [***Okuma önerileri***](/tr/chapter_5_5) bölümüne bakınız.

### Yedekleme Yazılımı ###

Cobian Yedekleme; düzenli olarak planlanmış zaman aralıklarıyla çalışması ve sadece son yedeklemeden sonra değiştirilen dosyaları içermesi için otomatik olarak ayarlanabilen, kullanıcı dostu bir araçtır. Ayrıca yedeklemeleri daha küçük hale getirmek için onları sıkıştırabilir.

<div class="getstarted" markdown="1">
Uygulama: [*Cobain Yedekleme Rehberi*](/en/cobian_main) ile uygulamaya başlayın
</div>

Her zaman olduğu gibi, yedekleme dosyalarınızı [*TrueCrypt*](/tr/glossary#TrueCrypt) gibi bir araç kullanarak şifrelemek iyi bir fikirdir. Veri şifreleme konusunda daha fazla bilgi [***Bilgisayarınızdaki hassas dosyaları nasıl korursunuz***](/tr/chapter-4) başlıklı [***4. Bölüm***](/tr/chapter-4)’de bulunabilir.

<div class="getstarted" markdown="1">
Uygulama: [*TrueCrypt - Güvenli Dosya Depolama Rehberi*](/en/truecrypt_main) ile uygulamaya başlayın
</div>
<p>
Bu yedekleme araçlarını kullanırken yedekleme sisteminizin pürüzsüz bir şekilde işlemesine yardım etmek için yapabileceğiniz birkaç şey var:

- Bilgisayarınızdaki dosyaları düzenleyin. Yedeklemeye niyetlendiğiniz tüm elektronik belgeleri içeren klasörleri tek bir konuma, örneğin **Belgelerim** klasörüne taşımaya çalışın.  
- Verilerini uygulama veri tabanında depolayan bir yazılım kullanıyorsanız öncelikle bu veri tabanının konumunu belirlemeniz gerekir. Bu uygun bir konum değilse programınızın veri tabanı için yeni bir konum seçmenize izin verip vermediğine bakın. İzin veriyorsa veri tabanını, elektronik belgelerinizle aynı klasöre yerleştirebilirsiniz. 
- Yedeklemelerinizi gerçekleştirmek için düzenli bir zamanlama planı oluşturun.
- Ofisinizde güvenilir ve güvenli bir yedekleme politikası olmayan tüm çalışanlar için bir prosedür oluşturmaya çalışın. İş arkadaşlarınızın bu sorunun önemini anlamalarına yardımcı olun. 
- Yedeklemenizden verilerinizi kurtarma işlemini test ettiğinizden emin olun. Nihayetinde sizin için gerçekten önemli olanın yedekleme prosedürü değil kurtarma prosedürü olduğunu aklınızda bulundurun!



<div class="background" markdown="1">
Elena: Tamam, işteyken şifreli bir yedek oluşturdum ve onu bir CD’ye kaydettim. Cobian, yedeğimi birkaç gün içinde güncellemek üzere ayarlandı. İş yerindeki masamın kilitlenebilir bir çekmecesi var ve bu yedekleme CD’lerini, kaybolmasınlar ya da bozulmasınlar diye, orada saklamayı planlıyorum.

<i>Nikolai: Ama ya iş yerin yanıp kül olursa? Diğer şeylerle birlikte, bilgisayar, masa, yedekleme CD’leri de…? Ya da web sitendeki forum büyük bir çevresel gösteri planlamaya karar verirse ve yetkililer müdahale eder ve işler çığırından çıkıp örgütüne baskın düzenlerlerse? Küçük masa kilidinin polislerin o CD’lere el koymasını engelleyebileceği konusunda şüpheliyim. Yedeklerini evinde saklamaya ya da senin için saklaması için bir arkadaşına sormaya ne dersin?
</div>

