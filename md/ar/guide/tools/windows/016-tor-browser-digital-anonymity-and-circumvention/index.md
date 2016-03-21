

---

lang: ar
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 016
title: Tor Browser - Digital Anonymity and Circumvention

---

**الموقع على الوب**

[**https://www.torproject.org**](https://www.torproject.org/)

**متطلبات الحاسوب**

- كل إصدارات ويندوز

- اتصال بشبكة الانترنت

- متصفح **موزِلا فيرفكس** لاستخدام ملحقة **توربتن**

**الإصدارة المشروحة في هذا الدليل**

تور: 1.3.18


**مطالعات مطلوبة**

فصل [**المجهولية و تجاوز الرقابة على الإنترنت**](/ar/chapter_08) في دليل الممارسات

**الرخصة**

برمجية حرة

المستوى

- مبتدئ، - عادي - متوسط - **خبير** - متقدم

الوقت المطلوب للبدء في استخدام هذه الأدوات

من 20 إلى 30 دقيقية

**ما ستحصل عليه**

- إمكانية إخفاء هويتك الرقمية عن مواقع الوب التي تزورها

- إمكانية إخفاء وجهتك على الشبكة عن مزودي خدمة الاتصال بالإنترنت و وسائل المراقبة المحلية

- إمكانية تجاوز الحجب على الإنترنت

**لينكس GNU, ماك OS و غيرها من برامج ميكروسوفت ويندوز المتوافقة:**


يتوفر عميل شبكة **تور** للمجهولية بالنسبة لأنظمة تشغيل لينكس GNU و ماك OS و وميكروسوفت ويندوز. ينصح  كثيراً بتور لأنها تخضع لاختبارات صارمة للحفاظ على على اتصالك بالانترنت خاصاً و آمناً. لكننا نود أيضاً اطلاعك على قائمة بحلول أخرى ينصح بها هنا:

[**Hotspot Shield**](http://hotspotshield.com/) و هي شبكة خاصة افتراضية (**VPN**) و تمثل حلاً **لميكروسوفت ويندوز**.

[**Dynaweb FreeGate**](http://www.dit-inc.us/freegate) و هو أداة منفذ مجانية **لميكروسوفت ويندوز**.

[**UltraReach UltraSurf**](http://www.ultrareach.com/) و هو أداة منفذ مجانية **لميكروسوفت ويندوز**.

[**Your Freedom**](http://www.your-freedom.net/) هي أداة منفذ تجارية و التي تتيح لك خدماتها بشكل مجاني (لكن بشكل أبطئ). هي متاحة بالنسبة **للينكس و ماك OS و ميكروسوفت ويندوز**. 

[**Psiphon**](http://psiphon.ca/) هو وكيل ويب, و بالتالي يعمل مع أي نظام تشغيل. 

ننصح بشدة قراءة المستندات التي تم إنشاؤها بواسطة [**سيساوي**](http://sesawe.net/), و هو تحالف عالمي مكرس لتحقيق وصول المعلومات الغير خاضع للرقابة لمستخدمي الانترنت حول العالم.  



**1.1 ما ينبغي معرفته قبل البدء**

**تور** هو أداة برمجية مصممة لزيادة الخصوصية و الأمان لاتصالك و نشاطاتك على الإنترنت. تخفي هويتك و تصفحك للإنترنت عن أشكال عدة من المراقبة. بغض النظر عما إذا كانت المجهولية مهمة بالنسبة لك, يعتبر تور طريقة مفيدة لنشر حرية الإنترنت, و التحايل على الرقابة و القيود الإلكترونية و بذلك يمكنك الدخول أو نشر المدونات و التقارير الإخبارية.

يقوم **تور** بحماية هويتك من خلال توجيه الإتصالات من خلال شبكة موزعة من الخوادم تدار من قبل متطوعين حول العالم. هذا يمنع أي شخص يراقب اتصالك بالإنترنت من معرفة المواقع التي تقوم بزيارتها, و تمنع هذه المواقع من معرفة موقعك الجغرافي. بالنسبة لإدارة مخدم منفذ **تور** أنفسهم, بعضهم قد يعرف أنك تستخدم تور, و البعض الآخر قد يعرف أن شخصاً قد دخل للمواقع التي تزورها, لكن لا أحد يعرف المعلومتين معاً.

يستطيع **تور** تمويه محاولاتك بالاتصال بمواقع محددة, لكنه لم يصمم لإخفاء محتويات اتصالاتك على شبكة الإنترنت. بالنتيجة, يمكنه إضافة طبقة حماية إضافية عند استخدامه مع خدمة أمنة مثل **جيميل و ريزآب**, لكن لا يجب إستخدامه لدخول مزود بريد إلكتروني غير آمن **كالهوتميل و الياهو**, أو أي موقع آخر يقوم بإرسال و إستقبال محتويات حساسة عبر اتصال HTTP الغير آمن.

**تعاريف:**

**منفذ** : في هذا الفصل, المنفذ هو نقطة الدخول حيث تتواصل البرمجيات مع الخدمات العاملة في أجهزة كمبيوتر أخرى متشابكة. إذا كان URL مثلاً WWW.GMAIL.COM  يعطيك "عنوان شارع" لخدمة ما, يقوم المنفذ بإخبارك أي "باب" عليك أن تستخدم للوصول للوجهة المطلوبة. عند تصفح الويب, عادة ما تستخدم المنفذ 80 للمواقع الغير آمنة (http://mail.google.com) و المنفذ 443 للمواقع الآمنة (https://mail.google.com).

**وسيط** : الوسيط هو برمجية وسيطة يتم تشغيلها على حاسوبك و على شبكتك المحلية أو في مكان آخر على شبكة الإنترنت و التي تساعد على تقوية اتصالك اتجاه الوجهة النهائية.

**مسار**: هو مسار الإتصالات عبر الإنترنت بين حاسوبك و المخدم الهدف.

**جسر الترحيل**: هو مخدم تور الذي يوفر الخطوة الأولى في شبكة تور للمجهولية. الجسر اختياري, و مصمم خصيصاً للأشخاص الذين يعيشون في دول تقوم بحجب تور.

