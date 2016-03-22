

---

lang: tr
community: guide
type: tactics
legacy: True
child: True
weight: 2
depth: 3
title: Hiding your sensitive information

---

Evinizde ya da ofisinizde bir kasa bulundurmakla ilgili sorun, cebinizde bir tane bulundurmanın sözünü bile etmeyelim, fazla göze çarpma eğiliminde olmasıdır. Birçok insanın [*şifreleme*](/tr/glossary#Encryption) kullanarak kendilerini suçlu duruma düşürmek konusunda mantıklı endişeleri vardır. Veri [*şifrelemenin*](/tr/glossary#Encryption) meşru nedenleri meşru olmayanlarını kat be kat aşsa bile bu tehdidin gerçekliği göz ardı edilemez. Esasında [*TrueCrypt*](/tr/glossary#TrueCrypt) gibi bir aracı kullanmaktan kaçınmak için iki neden vardır: kendi kendinizi suçlu durumuna düşürme ve en hassas bilgilerinizin konumuna açıkça işaret etme riski.

### Kendi kendinizi suçlu durumuna düşürme riskini göz önünde bulundurmak ###

[*Şifreleme*](/tr/glossary#Encryption) birçok ülkede yasa dışıdır ki bu da bu tür bir yazılımı indirmenin, kurmanın ve kullanmanın bir suç olduğu anlamına gelir. Bilgilerinizi, aralarında polis, ordu ya da istihbarat servislerinin de olduğu bir kesim gruptan korumak istiyorsanız, bu yasaları ihlal etmek, etkinliklerinizin araştırılması ya da örgütünüzün yargılanması için bir bahane olarak gösterilebilir. Bu tarz tehditlerin, burada ele alınan araçların yasallığıyla gerçekte hiçbir ilgisi olmayabilir. Sadece bir [*şifreleme*](/tr/glossary#Encryption) yazılımıyla ilişkilendirilmeniz, suç işlediğiniz ya da ([*şifrelenmiş*](/tr/glossary#Encryption) bölümün içinde gerçekte ne olduğundan bağımsız olarak) casusluk yaptığınız gibi suçlamalara maruz kalmanız için yeterli olabilir. Bu nedenledir ki bu tür araçların sizin durumunuza uygun olup olmadığını dikkatle düşünmelisiniz.

Durum buysa birkaç seçeneğiniz bulunmaktadır:

- Veri güvenliği yazılımı kullanmaktan tamamen vazgeçebilirsiniz; bu da sadece gizli olmayan bilgileri saklamanızı ya da hassas dosyalarınızın önemli unsurlarını korumak için bir şifreli sözcük sistemi icat etmenizi gerektirir.
- Hassas bilgilerinizi şifrelemek yerine onları gizlemek için [*steganografi*](/tr/glossary#Steganography) olarak adlandırılan tekniği kullanabilirsiniz. Bu konuda yardımcı olabilecek araçlar bulunmaktadır ama bunları uygun bir şekilde kullanmak çok dikkatli bir hazırlığı gerektirir ve kullandığınız araçları öğrenen herhangi birinin gözünde kendi kendinizi suçlu duruma düşürme riski hâlâ bulunmaktadır.
- Tüm hassas bilgilerinizi güvenli bir webmail hesabında depolamayı deneyebilirsiniz ama bu güvenli bir ağ bağlantısını ve görece ileri düzey bilgisayar ve internet bağlantısı bilgisini gerektirir. Bu teknik, ağ üzerinden [*şifrelemenin*](/tr/glossary#Encryption) dosya [*şifrelemesine*](/tr/glossary#Encryption) göre daha az suç isnad ettiğini ve hassas verileri sabit diskinize kazara kopyalamaktan ve orada bırakmaktan kaçınabileceğinizi varsayar.
- Hassas bilgilerinizi bir USB bellekte ya da harici sabit diskte saklayarak bilgisayarınızdan uzak tutabilirsiniz. Bununla beraber bu tür cihazlar kaybedilmeye ya da el konulmaya daha açıktır; bu nedenle bunlarda hassas, şifrelenmemiş bilgileri taşımak genellikle kötü bir fikirdir.
	
Gerekliyse bu türden bir dizi taktik kullanabilirsiniz. Bununla beraber, kendi kendinizi suçlu durumuna düşürmekten endişe ettiğiniz durumlarda bile [*TrueCrypt*](/tr/glossary#TrueCrypt) kullanmak ve [*şifrelenmiş*](/tr/glossary#Encryption) bölümünüzü olabildiğince gizlemeye çalışmak en güvenli yol olabilir.

Şifrelenmiş bölümünüzü daha az görünür kılmak isterseniz onu farklı bir dosya türü gibi görünecek şekilde yeniden adlandırabilirsiniz. Yaklaşık 700 MB olan geniş bölümleri bir CD imajıymış gibi gizlemek için “.iso” dosya uzantısını kullanmak iyi işleyen bir seçenektir. Daha küçük bölümler için diğer dosya uzantıları daha gerçekçi olabilir. Bu, kasanızı ofisinizin duvarındaki bir tablonun ardına gizlemeye benzer. Sıkı bir aramayı atlatamayabilir ama az da olsa bir koruma sağlar. [*TrueCrypt*](/tr/glossary#TrueCrypt) programını bir program olarak kurmak yerine onu sabit diskinize ya da USB belleğinize kaydettiğiniz sıradan bir dosya gibi yeniden adlandırabilirsiniz. [***TrueCrypt Rehberi***](/en/truecrypt_main) bunu nasıl yapacağınızı açıklamaktadır.

### Hassas bilgilerinizin teşhis edilme riskini göz önünde bulundurmak ###

Çoğu zaman bilgisayarınızda ya da USB belleğinizde bir [*şifreleme*](/tr/glossary#Encryption) yazılımıyla 'yakalanmaktan' çok; şifrelenmiş bölümün, en çok korumak istediğiniz bilgileri tam nerede sakladığınıza işaret etmesinden endişe edersiniz.  Her ne kadar bu bilgileri kimsenin okuyamayacağı gerçek olsa da bir saldırgan, onun orada olduğunu ve onu korumak için adımlar attığınızı bilecektir. Bu, saldırganın erişim elde etmek için girişebileceği, korkutma, şantaj, sorgulama ve işkence gibi çeşitli yöntemlere sizi açık hale getirebilir. İşte bu bağlamda, aşağıda ayrıntılarıyla betimlenen, [*TrueCrypt*](/tr/glossary#TrueCrypt)'in inkâr edilebilirlik özelliği devreye girmektedir.

[*TrueCrypt*](/tr/glossary#TrueCrypt)'in inkâr edilebilirlik özelliği, yazılımın, dosya [*şifreleme*](/tr/glossary#Encryption) araçlarının genel olarak sunduğunun ötesine geçtiği özelliklerden biridir. Bu özellik, en hassas bilgileri, diğerleri gibi yani daha az hassas, gizli veriler gibi gösteren [*steganografi*](/tr/glossary#Steganography)’nin nevi şahsına münhasır bir biçimi olarak düşünülebilir. Bu pek de gizli olmayan bir ofis kasasının içine 'gizli bir taban' kurmaya benzetilebilir. Saldırgan sizin anahtarınızı çalarsa ya da kasanın şifresini vermeniz için sizi korkutursa bulacağı şey korumayı gerçekten önemsediğiniz bilgiler değil, bazı ikna edici 'yem' olarak kullandığınız materyaller olacaktır.

Kasanızın arkasında gizli bir bölme olduğunu sadece siz bileceksiniz. Bu, saldırgana vermiş olduğunuzdan başka bir sır sakladığınızı 'inkâr etmenizi' sağlayacaktır ve herhangi bir nedenden dolayı şifrenizi söylemek zorunda kaldığınızda bilgilerinizi korumanıza yardım edecektir. Bu nedenler, sizin ya da meslektaşınızın, tanıdıklarınızın, arkadaşlarınızın ve aile üyelerinizin güvenliği için hukukî ya da fiziksel tehditleri içerebilir. İnkâr edilebilirliğin amacı, verilerinizi korumayı seçseniz bile potansiyel olarak tehlikeli bir durumdan kaçmanız için size bir şans vermektir. [***Kendi kendinizi suçlu durumuna düşürme riskini göz önünde bulundurmak***](#Considering_the_risk_of_self-incrimination) kısmında tartışıldığı gibi, ofisinizde bir kasayla yakalanmak kabul edilemez sonuçları beraberinde getirmek için yeterliyse, bu özellik daha az yararlıdır.

[*TrueCrypt*](/tr/glossary#TrueCrypt)'in inkâr edilebilirlik özelliği, normal [*şifrelenmiş*](/tr/glossary#Encryption) bölümünüzün içine 'gizli bir bölüm' daha depolayarak işlev görür. Bu gizlenmiş bölümü, normal olarak kullandığınızdan farklı bir alternatif şifre kullanarak açarsınız. Teknik bilgiye sahip bir saldırgan standart bölümünüze erişse bile başka bir gizli bölümün olduğunu kanıtlayamayacaktır. Elbette [*TrueCrypt*](/tr/glossary#TrueCrypt)’in bu yolla bilgi saklayabileceğini çok iyi bilebilir, bu nedenle yem olarak kullandığınız şifreyi verir vermez tehdidin ortadan kalkacağının garantisi yoktur. Çok sayıda insan [*TrueCrypt*](/tr/glossary#TrueCrypt)’i, inkâr edilebilirlik özelliğine izin vermeden kullanmaktadır, bununla beraber verili bir [*şifrelenmiş*](/tr/glossary#Encryption) bölümün bu tür bir 'gizli tabanı'nın olup olmadığını, analiz yoluyla belirlemenin olanaksız olduğu düşünülmektedir. Buna rağmen, gizli bölümünüzü açık bırakmak ya da diğer uygulamaların onun içerdiği dosyalara kısayol oluşturmasına izin vermek gibi daha az teknik yollarla, gizli bölümünüzü açık etmediğinizden emin olmak sizin işinizdir. Alttaki [***Okuma önerileri***](/tr/chapter_4_3) bölümü bu konu hakkında sizi daha fazla bilgiye götürebilir.

<div class="background" markdown="1">
Claudia: Tamam, o zaman standart bölümün içine bazı işe yaramaz dosyaları koyalım ve tüm tanıklıkları da gizli olana taşıyalım. Eski PDF’lerin ya da kullanabileceğimiz başka şeylerin var mı?

Pablo: Ben de bunu düşünüyordum. Demek istediğim, başka seçeneğimiz yoksa yem olarak kullandığımız şifreyi vereceğiz, değil mi? Ama inandırıcı olmak için o dosyaların bir şekilde önemliymiş gibi görünmesini sağlamalıyız. Aksi halde onları neden şifreleyelim ki? Belki de ilgisiz malî dosyalar ya da web sitelerinin şifrelerinin bir listesini ya da bunun gibi bir şeyi kullanmalıyız.

</div>


