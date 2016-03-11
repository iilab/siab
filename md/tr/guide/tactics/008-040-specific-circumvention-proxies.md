

---

lang: tr
community: guide
type: tactics
legacy: True
child: True
weight: 4
depth: 3
title: Specific circumvention proxies

---

Aşağıda, internet filtrelemesini aşmanıza yardım edebilecek birkaç özgül araç ve [*proxy*](/tr/glossary#Proxy) bulunmaktadır. Yeni sansür aşma araçları düzenli olarak üretilmekte ve var olanlar sık sık güncellenmektedir; bu konuda daha fazla şey öğrenmek için Security in-a-Box web sitesini ve [*Okuma önerileri*](/tr/chapter_8_5) bölümünde bahsi geçen kaynakları ziyaret etmelisiniz.

**Sanal Özel Ağ (VPN) tabanlı proxy’ler**

Aşağıda listesi verilen VPN proxy’leri, “bağlı" olduğunuz sürece tüm internet bağlantınızı proxy’den geçirir. Bu, ülkenizde engellenen e-posta ve anlık mesaj sağlayıcılarını kullanıyorsanız size yardımcı olabilir.

**Riseup VPN.** Riseup sunucusunda e-posta hesabı olan kullanıcılar içindir. Bu kolektif; güvenli, özel, ücretsiz VPN proxy sunucusuna bağlanma olanağı sunmaktadır. Lütfen [*Riseup VPN*](https://help.riseup.net/en/riseup-vpn) ve [*ona nasıl bağlanılır*](https://we.riseup.net/riseuphelp+en/vpn-howto) konusunda daha fazlasını okuyun.

**Hotspot Shield** kamuya açık, güvenli, ücretsiz, VPN sansür aşma proxy’sidir. Bunu kullanabilmek için [*aracı indir*](http://www.hotspotshield.com/)meniz  ve çalıştırmanız gerekmektedir. Hotspot Shield’ı geliştiren firma reklamlardan gelir elde etmektedir; bu nedenle [*şifreleme*](/tr/glossary#Encryption) sağlamayan web sitelerini ziyaret etmek için onu kullanırken, tarayıcı pencerenizin en tepesinde “banner reklamı” göreceksiniz. Her ne kadar kanıtlaması olanaksızsa da bu firma, aracı kullananların [*IP adreslerini*](/tr/glossary#IP_address) depolamak ya da reklam verenlere göndermek yerine, sildiğini iddia etmektedir. ** 

**Your-Freedom** güvenli, özel, VPN/SOCKS sansür aşma [*proxy*](/tr/glossary#Proxy)’sidir . Bir ücretsiz sansür aşma servisine bağlanmak için kullanılabilecek [*ücretsiz bir yazılımdır*](/tr/glossary#Freeware) . Bant genişliği ve kullanım süresi üzerinde sınırlama (günde 3 saat, haftada 9 saate kadar) bulunmaktadır. Ücret ödeyerek daha hızlı ve daha az sınırlı olan bir ticarî hizmete erişim de mümkündür. Your-Freedom’ı kullanmak için, [*aracı indirmeniz*](http://www.your-freedom.net/index.php?id=3)  ve bir [*hesap oluşturmanız*](http://www.your-freedom.net/index.php?id=170&amp;L=0) gerekmektedir. Her ikisi de [*Your-Freedom web sitesinde*](http://your-freedom.net)  yapılabilir. Ayrıca tarayıcınızı internete bağlanırken [*OpenVPN*](https://www.your-freedom.net/index.php?id=172) proxy kullanacak şekilde düzenlemeniz gerekecektir. Daha fazlasını [*Your-Freedom dokümantasyonunda okuyabilirsiniz*](https://www.your-freedom.net/index.php?id=doc).

**Freegate** açık, güvenli, VPN, ücretsiz yazılım sansür aşma proxy’sidir. [Freegate’in  en son sürümünü indirebilir](http://www.dit-inc.us/freegate) ya da Freegate hakkında [ilginç bir makaleyi  okuyabilirsiniz](http://www.addictivetips.com/windows-tips/freegate-lets-you-access-blocked-websites-at-optimal-speed/).

**SecurityKISS** açık, güvenli, VPN, ücretsiz yazılım sansür aşma proxy’sidir. Bunu kullanabilmek için [ücretsiz bir programı indirmeniz ve çalıştırmanız](http://www.securitykiss.com/resources/download/) gerekmektedir. Bir hesap için kaydolmaya gerek yoktur. Ücretsiz kullanıcılar günlük 300 MB’lık proxy üzerinden internet trafiğiyle sınırlandırılmıştır. Ücretli kullanıcılar için sınırlama yoktur ve kullanabilecekleri daha fazla VPN sunucusu bulunmaktadır. [Daha fazlasını öğrenmek için SecureKISS’in ana sayfasına](http://www.securitykiss.com) bakınız.

<!--
**Psiphon1** may be a good option if you know someone who has a Windows computer that she leaves on, running and connected to a fast, unfiltered Internet connection in another country. In order to use [*Psiphon*](/tr/glossary#Psiphon), you must ask this person to download the program from the [*Civisec webpage*](http://psiphon.civisec.org/), install it, create an account for you, and send you the [*proxy's*](/tr/glossary#Proxy) [*IP address*](/tr/glossary#IP_address) along with your username and password. This will give you access to your own personal account on a trusted, secure, private, web-based circumvention [*proxy*](/tr/glossary#Proxy). Before using it, however, you should verify the  [*proxy's*](/tr/glossary#Proxy) fingerprint as discussed in the  [*Secure and insecure proxies*](/tr/chapter_8_3#Secure_and_insecure_proxies) section, above, and in *Appendix C* of the included [*Psiphon User's Guide*](/tr/glossary#Psiphon_users_guide).
-->

**Psiphon3** internet içeriğine sansürsüz erişim sağlamanız için VPN, SSH ve HTTP Proxy teknolojilerinden yararlanan güvenli, kamuya açık bir araçtır. Kullanabilmek için programı [*Psiphon3’ün ana sayfasından*](http://psiphon3.com) indirmeniz ve hangi modda [*VPN, SSH, SSH+*] kullanmak istediğinizi seçmeniz gerekir. Phiphone3 Android cihazlarla da birlikte çalışmaktadır. Daha fazlasını öğrenmek için lütfen [*ana sayfasına*](http://psiphon3.com) bakınız.


**Web Proxy’leri:**

**Peacefire** çok sayıda açık, web tabanlı [*proxy*](/tr/glossary#Proxy)’i destekler. Bu [*proxy*](/tr/glossary#Proxy)’ler, onlara nasıl eriştiğinize bağlı olarak güvenli ya da güvensiz olabilir. Bir [*Peacefire*](/tr/glossary#Peacefire) [*proxy*](/tr/glossary#Proxy) kullanırken, siz ve proxy arasında güvenli bir bağlantıya sahip olmak için [*HTTPS*](/tr/glossary#SSL) adresi girmelisiniz. Yeni [*proxy*](/tr/glossary#Proxy)’ler  düzenli olarak geniş bir e-posta listesine ilan edilmektedir. Güncellemeleri almak için bu e-posta listesine [*Peacefire web sitesi*](http://peacefire.org/)’nden kayıt olabilirsiniz.


