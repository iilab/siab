

---

lang: tr
community: guide
type: tactics
legacy: True
child: True
weight: 3
depth: 3
title: Firewalls

---

Bir güvenlik duvarı internetten gelen veriyi bir bilgisayarda ilk gören programdır. Ayrıca dışarı gönderilen bilgiyi ele alan en son programdır. Bir binanın girişine konumlanmış, kimin girip kimin çıkabileceğine karar veren bir güvenlik görevlisi gibi, bir güvenlik duvarı gelen ve giden verileri alır, inceler ve onlar hakkında karar verir. Doğal olarak, hacker'lara ve virüslere bilgisayarınıza erişim için açık bir yol sağlamamak için, internetten ve yerel ağlardan güvenmediğiniz bağlantılara karşı kendinizi savunmanız yaşamsal önemdedir. Doğrusu, bilgisayarınızın dışa doğru bağlantılarını izlemek de aynı derecede önemlidir.

İyi bir güvenlik duvarı bilgisayarınızdaki her programın erişim izinlerini seçmenize izin verir. Bu programlardan biri dış dünyayla bağlantı kurmaya çalıştığında, güvenlik duvarınız, programı tanıdığı ve bu tür bağlantılar için ona izin verdiğinizi doğrulayabildiği durumlar hariç, girişimi engelleyecek ve size bir uyarı verecektir. Bu büyük ölçüde var olan [*kötü amaçlı yazılımların*](/tr/glossary#Malware) virüs yaymasını ya da bilgisayarınıza hacker'ları davet etmesini engellemek içindir. Bu açıdan bir güvenlik duvarı, hem ikinci bir savunma hattı hem de bilgisayarınızın güvenliğinin tehdit edildiğini anlamanıza yardım edebilecek bir erken uyarı sistemi sağlar. 



### Güvenlik Duvarı Yazılımı ###


Microsoft Windows’un son sürümleri şimdilerde otomatik olarak açılan yerleşik güvenlik duvarı içeriyor. Ne yazık ki Windows güvenlik duvarı birçok açıdan sınırlıdır, örneğin, dışa dönük bağlantıları incelemez. Ancak bilgisayarınızı güvenli tutmak konusunda daha başarılı bir program olan [*Comodo Personal Firewall*](/tr/glossary#Comodo_Firewall) adlı mükemmel bir [*ücretsiz yazılım*](/tr/glossary#Freeware) programı bulunmaktadır.

<div class=getstarted markdown=1> Uygulama: [***Comodo Firewall Rehberi***](/en/comodofirewall_main) ile uygulamaya başlayın
</div>



### Güvenilmez ağ bağlantılarını engellemek  ###
- Hassas işler için kullanacağınız bilgisayara sadece önemli programları kurun ve onları güvenilir kaynaklardan edindiğinizden emin olun. Kullanmadığınız herhangi bir programı ise kaldırın. 
- Kullanmadığınız zamanlarda bilgisayarınızın internet bağlantısını kapatın ve geceleri bilgisayarınızı tamamen kapatın. 
- Windows şifrenizi kimseyle paylaşmayın. 
- Kullanmadığınız 'Windows hizmetlerini' açtıysanız onları kapatmanız gerekir. Bu konuda daha fazla bilgi için [***Okuma önerileri***](/tr/chapter_1_5)’ne bakınız.
- Çalıştığınız yerdeki tüm bilgisayarlarda bir güvenlik duvarının kurulu olduğundan emin olun </li>
- Kurulu güvenlik duvarı yoksa, çalıştığınız yerdeki bütün yerel ağı korumak için ek bir güvenlik duvarı kurmayı düşünmelisiniz. Birçok ticari geniş bant [*ağ geçitleri*](/tr/glossary#Router) kullanması kolay bir güvenlik duvarı içerir, ve onu çalışır hale getirmek ağınızı çok daha güvenli kılabilir. Bu konuda nereden başlayacağınızı bilmiyorsanız, ağınızı kurmaya yardım eden kişilerden destek isteyebilirsiniz.




<div class=background markdown=1>
Asani: Demek ki sen benden anti-virüs, anti-casus yazılım ve güvenlik duvarı yazılımları kurmamı istiyorsun? Bilgisayarım bütün bunlarla baş edebilir mi?

Muhindo: Kesinlikle. Doğrusu bu üç araç, bugünlerde internette güvenli kalmak için asgari olmazsa olmaz programlardır. Bu programlar birlikte çalışacak şekilde tasarlanmıştır, öyle ki bunların tümünü kurmanın hiçbir sorun çıkarmaması gerekir. Yine de iki anti-virüs programını ya da iki güvenlik duvarını aynı anda çalıştırmak istememen gerektiğini hatırlamalısın.
</div>

