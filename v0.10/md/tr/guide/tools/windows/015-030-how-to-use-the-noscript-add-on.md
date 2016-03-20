

---

lang: tr
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: How to Use the NoScript Add On

---

Bu sayfadaki kısımların listesi:

- [**4.0 NoScript Hakkında**](#4.0)
- [**4.1 NoScript Nasıl Kullanılır?**](#4.1)


-------

<a name="4.0"></a>
##4.0 NoScript Hakkında##

![](/sites/securitybkp.ngoinabox.org/files/u9/noscript.png)

**NoScript**, bilgisayarınızı İnternet’teki zararlı web sitelerinden korumaya yarayan bir **Mozilla eklentisidir**. Sizin kabul ettiğiniz, güvenilir bulduğunuz web sitelerinin (banka sayfası veya çevrim içi gazete gibi) ‘beyaz listesi’ni yaparak çalışır. Geriye kalan tüm siteler, siz içeriklerinin zararlı olmadığını kanıtlayana kadar, potansiyel olarak zararlı tehlikeli kabul edilir. Güvenilir olduğuna karar verdiğiniz siteleri beyaz listeye ekleyebilirsiniz. 

**NoScript** tüm reklam bantları ve açılır reklamları,**JavaScript** ve **Java** kodlarını ve diğer potansiyel olarak tehlikeli web site özelliklerini otomatik olarak engeller. **NoScript** zararlı içerik ile bir web sitesini göstermek için gerekli olan içeriği birbirinden ayırt edemez. Bu yüzden de, içeriğinin güvenilir olduğuna inandığınız siteler için istisnalar yapılmasını sağlamak size kalmıştır. 


<a name="4.1"></a>
## 4.1 NoScript Nasıl Kullanılır? ##

**NoScript** kullanmaya başlamadan önce, **Araçlar > Eklentiler’i seçerek** *Eklentiler* penceresini etkinleştirin ve **NoScript’in** başarılı bir şekilde kurulduğundan emin olun. 

**Tavsiye**: **NoScript’in** kullanımı en başta zor görünse de (çünkü düzenli olarak ziyaret ettiğiniz web sitelerinin içerikleri düzgün görünmemeye başlayabilir), otomatik engelleme özelliğinin faydasını görmeye hemen başlayacaksınız. Bu sayede, rahatsız edici reklamlardan, açılır mesajlardan ve web sitelerine eklenmiş zararlı kodlardan korunabilirsiniz. 

**NoScript**, **JavaScript**, **Adobe Flash** ve diğer kod benzeri içerikleri yakalayana kadar arka planda sessiz bir şekilde çalışır. Yakaladığı zaman, bu içeriği engelleyecektir ve **Firefox** penceresinin altında aşağıdaki statü çubuğunu çıkaracaktır: 


![](/sbox/screen/firefox-tr/50.png)

*Şekil 1: NoScript statü çubuğu*

**NoScript** statü çubuğu, hangi *nesnelerin* (örneğin reklam ve açılır mesajları) ve *kodların* kendilerini bilgisayarınıza yerleştirmekten alıkoyduğunu gösterir. Aşağıda görünen iki şekil **NoScript’in** nasıl çalıştığını başarılı bir şekilde gösterir: *Şekil 2’de* **NoScript’in** ticari bir web sitesinde **Adobe Flash Player** tarafından oynatılan bir reklamı nasıl engellediğini görebilirsiniz.

![](/sbox/screen/firefox-tr/51.png)

*Şekil 2: NoScript’in ticari bir sitedeki açılır bir reklamı engelleme örneği*

*Şekil 3’te*, **Twitter** web sitesinin, kendisini görüntüleyebilmek için **JavaScript’in** (en azından geçici olarak) etkinleştirilmesi gerektiği iletisini verdiğini görebilirsiniz.

![](/sbox/screen/firefox-tr/52.png)

*Şekil 3: Twitter web sitesinden gelen JavaScript’in etkinleştirilmesi isteği*

**NoScript** zararlı ve gerçek kodları birbirinden ayırt edemediği için, bazı önemli özellikler ve işlevler (örneğin bir araç çubuğu) görünmez hale gelebilir. Bazı web siteleri birden fazla web sitesinden gelen içerik veya kod benzeri içerik gösteriyor olabilir. Örneğin, **www.twitter.com** web sitesinin iki kod kaynağı vardır (*twitter.com* ve *twimg.com*):

![](/sbox/screen/firefox-tr/53.png)

*Şekil 4: NoScript statü barı Seçenekler menüsü örneği*

Bu şartlar altında, kodları engellemek için, *[web sitesi ismi]’e Geçici Olarak İzin Ver* seçeneğini **seçebilirsiniz** (bu örnekte, *twitter.com’a Geçici Olarak İzin Ver*). Bu sayfayı görmeniz için yeterli olmazsa deneme yanılma yöntemi ile seçtiğiniz içeriğin görüntülenmesi için minimum kaç web sitesine ihtiyaç olduğunu belirleyebilirsiniz. **Twitter** örneğinde, **Twitter’ın** düzgün çalışabilmesi için, **twitter.com’a Geçici Olarak İzin Ver** ve **twimg.com’a Geçici Olarak İzin Ver’i** **seçmelisiniz**.

**Uyarı!** **Hiçbir** şart altında, *Kodlara Her Zaman İzin Ver (tehlikeli)* seçeneğini seçmemelisiniz. Mümkün oldukça, *Bu Sayfadaki Tüm Bilgilere İzin Ver* seçeneğini de işaretlememelisiniz. Bazı durumlarda tüm kodlara izin verme seçeneğini işaretlemeniz gerekebilir. Bu durumlarda, bu işlemi gerçekten güvendiğiniz siteler için, geçici olarak ve çevrim içi işlemleriniz bitene kadar yaptığınızdan emin olun. Tehlikeli kodların çevrim içi gizliliğiniz ve güvenliğinizi tehdit eder konuma gelmesi için *bir an* bile yeterlidir. 

Güvendiğiniz ve düzenli olarak ziyaret ettiğiniz web siteleri için, *(web sitesinin ismi)’ne İzin Ver’i* **seçin**. (Yukarıdaki örnekte *twitter.com’a İzin Ver* ve *twimg.com’a İzin Ver* seçilmişti.) Bu seçeneği işaretleyerek **NoScript’in** bu web sitesini kalıcı olarak güvenilir web siteleri listesine eklemesini sağlayabilirsiniz.


