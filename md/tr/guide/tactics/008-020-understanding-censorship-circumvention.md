

---

lang: tr
community: guide
type: tactics
legacy: True
child: True
weight: 2
depth: 3
title: Understanding censorship circumvention

---

Bir web sitesi yukarıda ele alınan yöntemlerden biri kullanılarak engellendiği için doğrudan ziyaret edilemiyorsa, engelin çevresinden dolaşacak bir yol bulmanız gerekecektir. İnterneti filtrelemeyen bir ülkede konuşlanmış güvenli bir [*proxy*](/tr/glossary#Proxy) sunucusu, istediğiniz web sayfalarını bularak ve onları size ulaştırarak, bu tür bir alternatif yolu size sağlayabilir. [*ISP*](/tr/glossary#ISP)’niz açısından siz, internette bir yerlerde bulunan bilinmeyen bir bilgisayarla ([*proxy*](/tr/glossary#Proxy) sunucusuyla) güvenli bir iletişim kurmuş gibi görüneceksiniz.

![](/sites/securitybkp.ngoinabox.org/security/files/img/2-en.png)

Elbette ülkenizde internet sansüründen sorumlu devlet organı (ya da filtreleme yazılımı için güncellemeler sağlayan şirket) eninde sonunda bu ‘bilinmeyen bilgisayar’ın gerçekte bir sansür aşma [*proxy*](/tr/glossary#Proxy)’si olduğunu öğrenecektir. Bu olursa, kullandığınız Proxy’nin [*IP adresi*](/tr/glossary#IP_address) de  [*kara listeye*](/tr/glossary#Blacklist) eklenebilir ve işlemez hale gelir. [*Proxy*](/tr/glossary#Proxy)’lerin engellenmesi genelde zaman alır, bununla beraber sansür aşma araçlarını yaratanlar ve onları güncelleyenler bu tehdidin farkındadır. Onlar aşağıdaki yöntemlerin birini ya da tümünü kullanarak bu tehditle mücadele ederler:

- **Gizli proxy'lerin** kimliğinin saptanması daha güçtür.  Daha az görünür olma eğiliminde olan güvenli [*proxy*](/tr/glossary#Proxy)’leri kullanmanın önemli olmasının nedenlerinden biri budur. Bununla beraber [*şifreleme*](/tr/glossary#Encryption), çözümün sadece bir parçasıdır. Bir [*proxy*](/tr/glossary#Proxy)’nin yöneticileri, gizli kalmak istiyorlarsa, yeni kullanıcılara konumlarını açık ederken bu konuda dikkatli davranmalıdırlar. 
	
- **Tek kullanımlık proxy'ler** engellendikten sonra hızla yenilenebilirdir. Bu durumda kullanıcılara yenilenen [*proxy*](/tr/glossary#Proxy)’leri nasıl bulacaklarını bildirmek çok da güvenli olmayabilir. Bunun yerine, bu türden sansür aşma araçları yeni [*proxy*](/tr/glossary#Proxy)’leri engellenebileceğinden daha hızlı yaygınlaştırmaya çalışır.
	
Nihai olarak, istediğiniz hizmetleri aramak için güvenilir bir [*proxy*](/tr/glossary#Proxy)’e eriştiğiniz sürece yapmanız gereken tek şey uygun internet uygulamalarıyla istediğiniz talepleri göndermek ve geri dönen şeylere bakmaktır. Genellikle bu sürecin ayrıntıları bilgisayarınıza kurduğunuz sansür aşma yazılımı tarafından, tarama ayarlarınızı değiştirerek ya da tarayıcınızı web tabanlı bir [*proxy*](/tr/glossary#Proxy) sayfasına yönlendirerek, otomatik olarak yapılır. Aşağıda ele alınan [*Tor*](/tr/glossary#Tor) anonimlik ağı ilk yöntemi kullanır. Ardından da her biri biraz farklı şekilde çalışan temel tek [*proxy*](/tr/glossary#Proxy) sansür aşma araçları üzerine bir değerlendirme yer alacaktır.


