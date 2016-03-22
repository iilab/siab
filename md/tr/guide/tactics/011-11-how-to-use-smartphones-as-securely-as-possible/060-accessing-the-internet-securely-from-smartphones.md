

---

lang: tr
community: guide
type: tactics
legacy: True
child: True
weight: 6
depth: 3
title: Accessing the Internet Securely from Smartphones

---

[***İnternet iletişiminizin gizliliği nasıl korunur***](/tr/chapter-7) başlıklı [***7. Bölüm***](/tr/chapter-7)’de ve [***İnternette nasıl anonim kalınır ve internet sansürü nasıl aşılır***](/tr/chapter-8) başlıklı [***8. Bölüm***](/tr/chapter-8)’de ele aldığımız gibi, internetteki içeriğe erişim ya da fotoğraf veya video gibi malzemeleri çevrimiçi yayınlamak, kim olduğunuz ve nerede, ne yapıyor olduğunuz hakkında birçok iz bırakır.  Bu sizi risk altına sokabilir. Akıllı telefonunuzu internet üzerinden iletişim için kullanmanız bu riski büyütür.

### WiFi ya da Taşınabilir Veri Üzerinden Erişim ###

Akıllı telefonlar internete nasıl erişebileceğinizi denetim altında tutmanıza şu şekillerde izin verir: (bir internet kafede olduğu gibi) bir erişim noktası tarafından sağlanan kablosuz bağlantı aracılığıyla ya da GPRS, EDGE, ya da UMTS gibi taşınabilir ağ operatörlerinin sağladığı taşınabilir veri bağlantısı aracılığıyla.

Bir WiFi bağlantısı kullanmak, cep telefonu servis sağlayıcısıyla geride bırakıyor olabileceğiniz veri izlerini azaltmanızı sağlar (internete cep telefonu aboneliğinizle bağlanmadığınız durumlarda). Bununla beraber bazen bir taşınabilir ağ bağlantısı çevrim içi olmanın tek yoludur. Ne yazık ki taşınabilir ağ bağlantısı protokolleri (EDGE ya da UMTS gibi) açık standartlar değildir. Bağımsız geliştiriciler ya da güvenlik mühendisleri bu protokollerin taşınabilir ağ taşıyıcıları tarafından nasıl uygulandığını görmek için bunları inceleyemez.

Bazı ülkelerde taşınabilir erişim sağlayıcıları, internet servis sağlayıcılarından faklı yasalarla çalışır ki bu, devletlerin ve telefon şirketlerinin daha doğrudan gözetimiyle sonuçlanabilir.

Akıllı telefonlarla dijital iletişiminiz için hangi yolu seçtiğinizden bağımsız olarak, anonimleştirici araçları ve şifreleme araçlarını kullanarak verilerinizi ifşa etme riskini azaltabilirsiniz.

### Anonimleştirme ###

Çevrimiçi içeriğe anonim olarak erişmek için Orbot adındaki Android uygulamayı kullanabilirsiniz. [**Orbot**](https://www.torproject.org/docs/android.html.en), Tor’un anonim ağı aracılığıyla internet iletişiminizi yönlendirir.

<div class=getstarted markdown=1>
Uygulama: [*Orbot Rehberi*](/en/Orbot_main) ile uygulamaya başlayın
</div>

Bir başka uygulama olan Orweb ise, proxy’ler kullanmak ve yerel tarama geçmişi tutmamak gibi gizliliği arttıran özellikleri olan bir internet tarayıcısıdır. Orbot ve Orweb birlikte internet filtrelerini ve güvenlik duvarlarını devre dışı bırakır ve anonim tarama hizmeti sunar.

<div class=getstarted markdown=1>
Uygulama: [*Orweb Rehberi*](/en/Orweb_main) ile uygulamaya başlayın
</div>

### Proxyler ###

[*Firefox*](/tr/glossary#Firefox)’un taşınabilir sürümü [**Firefox mobile**](http://f-droid.org/repository/browse/?fdid=org.mozilla.firefox), trafiği proxy sunucularına yönlendiren proxy eklentileriyle donatılabilir. Trafiğiniz buradan istediğiniz siteye gider. Bu, sansür durumlarında yardımcı olabilir ama istemcinizle proxy’niz arasındaki bağlantının şifrelenmemiş olması durumunda siteye ulaşım isteğinizi ifşa edebilir. Firefox’la proxy kullanmayı kolaylaştıran [**Guardian Project**](https://guardianproject.info/) tarafından sunulan [**Proxy Mobile**](https://guardianproject.info/apps/proxymob-firefox-add-on/)  eklentisini tavsiye ediyoruz. Bu, Firefox taşınabilir iletişimlerini Orbot’a yönlendirmenin ve [*Tor*](/tr/glossary#Tor) ağını kullanmanın tek yoludur.

