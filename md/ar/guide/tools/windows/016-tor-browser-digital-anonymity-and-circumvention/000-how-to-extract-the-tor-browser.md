

---

lang: ar
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 0
depth: 3
title: How to extract the Tor Browser

---

<p>بعد تثبيت باقة ڤيداليا سترى أيقونات جديدة على <em>سطح المكتب</em> و&nbsp;<kbd>قائمة ابدأ</kbd>. ستحتوي لوحة النظام (تجدها أسفل الشاشة على اليمين -في الواجهة الإنجليزية- أو على اليسار -في الواجهة العربية-) على أيقونة <em>بريڤوكسي</em> <img alt="Tor/screenshots-ar/01.png" src="/sites/securitybkp.ngoinabox.org/files/u5/tor-ar/01.png" title="Tor/screenshots-ar/01.png" /> و&nbsp;أيقونة <em>ڤيداليا</em> <img alt="Tor/screenshots-ar/07.png" src="/sites/securitybkp.ngoinabox.org/files/u5/tor-ar/07.png" title="Tor/screenshots-ar/07.png" />.</p>

<p>يتغير مظهر أيقونة ڤيداليا حسبما إذا كان تور يعمل أم لا. <kbd>انقر بزر الفأرة الأيمن</kbd> على هذه الأيقونة لتشغيل تور أو إيقافه.</p>

<p><img alt="Tor/screenshots-ar/08.png" src="/sites/securitybkp.ngoinabox.org/files/u5/tor-ar/08.png" title="Tor/screenshots-ar/08.png" /></p>

<p><em>شكل 1: قائمة ڤيداليا في لوحة النظام</em></p>

<p>بعد إيقاف خدمة تور، ستظهر الأيقونة كما يلي: <img alt="Tor/screenshots-ar/06.png" src="/sites/securitybkp.ngoinabox.org/files/u5/tor-ar/06.png" title="Tor/screenshots-ar/06.png" /></p>

<p>يمكن كذلك تشغيل <em>بريڤوكسي</em> و&nbsp;<em>ڤيداليا</em> من <kbd>قائمة ابدأ</kbd> عبر هذه الخطوات:</p>

<p><strong>خطوة 1</strong>. <kbd>اختر: ابدأ &gt; Programs ‏&gt; Vidalia Bundle ‏&gt; Privoxy ‏&gt; Privoxy</kbd></p>

<p><strong>خطوة 2</strong>. <kbd>اختر: ابدأ &gt; Programs ‏&gt; Vidalia Bundle ‏&gt; Vidalia</kbd></p>

<p>قبل أن تواصل تأكد من أن ڤيداليا وبريڤوكسي يعملان ويظهران في لوحة النظام.</p>

<h3>2.1 لوحة تحكم ڤيداليا</h3>

<p>توفر <em>لوحة تحكم ڤيداليا</em> واجهة رسومية للكثير من وظائف تور.</p>

<p><img alt="Tor/screenshots-ar/21.png" src="/sites/securitybkp.ngoinabox.org/files/u5/tor-ar/21.png" title="Tor/screenshots-ar/21.png" /></p>

<p><em>شكل 2: لوحة تحكم ڤيداليا</em></p>

<p>عد تشغيلها ستحاول تلقائيا الاتصال بشبكة تور. سيوضّح شريط تقدّم حالة محاولة الاتصال.</p>

<p><img alt="Tor/screenshots-ar/22.png" src="/sites/securitybkp.ngoinabox.org/files/u5/tor-ar/22.png" title="Tor/screenshots-ar/22.png" /></p>

<p><em>شكل 3: مؤشر الحالة بينما يُشغّل تور</em></p>

<p><strong>ملاحظة</strong>: يجب أن يُتِم تور عدة مهام بنجاح قبل أن يتصل بشبكة المجهولية. ستكون محاولتك الأولى أطول من المحاولات اللاحقة بشكل ملحوظ. هذا لأن تور يأخذ بعض الوقت في التعرف على الشبكة وخصائصها، ثم تنزيل المعلومات المطلوبة على حاسوبك.</p>

<p>إذا نجحت محاولة الاتصال فستظهر هذه الشاشة:</p>

<p><img alt="Tor/screenshots-ar/23.png" src="/sites/securitybkp.ngoinabox.org/files/u5/tor-ar/23.png" title="Tor/screenshots-ar/23.png" /></p>

<p><em>شكل 4: شاشة حالة تور - تور يعمل</em></p>

<p>إذا لم ينجح الاتصال لسبب ما فراجع <a href="tor_troubleshooting">قسم 4: معالجة أعطال تور</a>.</p>

<h3>2.2 كيف تتصفح الإنترنت مستخدما تور</h3>

<p>الخطوة الثانية -قبل أن تتمكن من تصفح المواقع مستخدما تور- هي إعداد متصفح الوب. من فضلك اقرأ أحد الأقسام التالية حسب المتصفح الذي تريد استخدامه مع تور. ننصح بشدة استخدام المتصفح <a href="firefox">موزيلا فَيَرفُكس</a>.</p>

<h4>2.2.1 تعليمات موزيلا فيرفكس</h4>

<p><strong>خطوة 1</strong>. <kbd>افتح</kbd> فيرفكس.</p>

<p>ستلاحظ -بعد تثبيت باقة ڤيداليا- وجود زر جديد في الزاوية اليسرى السفلية من نافذة المتصفح.</p>

<p><img alt="Tor/screenshots-ar/30.png" src="/sites/securitybkp.ngoinabox.org/files/u5/tor-ar/30.png" title="Tor/screenshots-ar/30.png" /></p>

<p>هذه إضافة <em>توربتن</em>، وستستخدمها لتخبر المتصفح أن يصل للمواقع إما عبر تور أو عبر اتصال الانترنت العادي. عند تثبيته أول مرة سيكون معطلا وسيكتب عليه <em>تور معطّل</em>.</p>

<p><strong>خطوة 2</strong>. <kbd>انقر</kbd>: على توربتن ليصبح <img alt="Tor/screenshots-ar/31.png" src="/sites/securitybkp.ngoinabox.org/files/u5/tor-ar/31.png" title="Tor/screenshots-ar/31.png" /></p>

<p>متصفحك مُعدّ الآن ليصل إلى صفحات الوب خفية عبر تور.</p>

<p><strong>فائدة</strong>: بعد الانتهاء من التصفح تأكد من أن تحذف مخبئية الإنترنت والكعكات. يمكنك عمل هذا في فيرفكس باختيار: <kbd>أدوات &gt; امسح البيانات الشخصة</kbd> مع التأشير على كل الخيارات الموجودة ثم نقر زر امسح البيانات الشخصية الآن. لمزيد من المعلومات طالع <a href="firefox">دليل فيرفكس</a>.</p>

<h4>2.2.2 تعليمات إنترنت إكسبلورر</h4>

<p><strong>ملاحظة</strong>: بالرغم من إمكانية استخدام تور مع أي متصفح وب، عليك تجنب الاعتماد على إنترنت إكسبلورر إذا كانت المجهولية تهمك. سيكون الكشف عن هويتك أصعب بكثير إذا استخدمت فيرفكس وإضافة توربتن.</p>

<p><strong>خطوة 1</strong>. <kbd>افتح</kbd> متصفح الوب إنترنت إكسبلورر.</p>

<p><strong>خطوة 2</strong>. اختر: <kbd>أدوات &gt; خيارات الإنترنت</kbd> لتنشيط شاشة <em>خيارات الإنترنت</em></p>

<p><strong>خطوة 3</strong>. <kbd>انقر على لسان Connections&gt; لتنشيط الشاشة الموضحة في شكل 5 أسفل: </kbd></p>

<p><img alt="Tor/screenshots-ar/02.png" src="/sites/securitybkp.ngoinabox.org/files/u5/tor-ar/02.png" title="Tor/screenshots-ar/02.png" /></p>

<p><em>شكل 5: لسان الاتصالات في شاشة خيارات إنترنت إكسبلورر</em></p>

<p><strong>خطوة 4</strong>. <kbd>انقر</kbd> على زر <em>LAN Settings</em> لتنشيط شاشة <em>Local Area Network (LAN) Settings</em> كما يلي:</p>

<p><img alt="Tor/screenshots-ar/03.png" src="/sites/securitybkp.ngoinabox.org/files/u5/tor-ar/03.png" title="Tor/screenshots-ar/03.png" /></p>

<p><em>شكل 6: إعدادات الشبكة المحلية.</em></p>

<p><strong>خطوة 5</strong>. أشّر على خيار <kbd>Use a proxy server...</kbd> ثم انقر على زر <kbd>Advanced</kbd> لتنشيط شاشة <em>Proxy Settings</em>.</p>

<p><strong>خطوة 6</strong>. <strong>املأ</strong> حقول إعدادات الوسيط (proxy) كما يظهر في <em>شكل 7</em>:</p>

<p><img alt="Tor/screenshots-ar/04.png" src="/sites/securitybkp.ngoinabox.org/files/u5/tor-ar/04.png" title="Tor/screenshots-ar/04.png" /></p>

<p><em>شكل 7: إعدادات الوسيط في إنترنت إكسبلورر</em></p>

<p><strong>خطوة 7</strong>: انقر على زر <kbd>موافق</kbd> ثلاث مرات، أو حتى تعود لنافذة المتصفح الرئيسية.</p>

<p><strong>ملاحظة</strong>: ستحتاج لتكرار <em>الخطوات 1 إلى 4</em> لإيقاف استخدام تور. وبدلا من <em>خطوة 5</em> سيكون عليك <em>إزالة التأشير</em> عن خيار <em>Use a proxy server...</em>.</p>

<p><strong>فائدة</strong>: بعد الانتهاء من التصفح تأكد من أن تحذف مخبئية الإنترنت والكوكيز. يمكنك عمل هذا في إنترنت إكسبلورر 6.0 باختيار: <kbd>أدوات &gt; خيارات الإنترنت</kbd> ثم النقر على <kbd>احذف الكوكيز</kbd> ثم انقر <kbd>موافق</kbd>، و&nbsp;نقر <kbd>احذف الملفات</kbd> ثم انقر <kbd>موافق</kbd> و&nbsp;نقر <kbd>أخل التاريخ</kbd> ثم انقر <kbd>نعم</kbd> ثم انقر <kbd>موافق</kbd></p>

<h3>2.3 كيف تتحقق من اتصالك بتور</h3>

<p><strong>خطوة 1</strong>. <kbd>افتح</kbd> موقع <a class="ext-link" href="https://check.torproject.org/"><span class="icon">https://check.torproject.org/</span></a>. سيؤكد ما إذا كنت تتصل عبر شبكة تور أم لا.</p>

<p><img alt="Tor/screenshots-ar/34.png" src="/sites/securitybkp.ngoinabox.org/files/u5/tor-ar/34.png" title="Tor/screenshots-ar/34.png" /></p>

<p><em>شكل 8: شاشة 'هل تستخدم تور؟' في موزيلا فيرفكس</em></p>

<p>تهانينا، متصفحك يتصل بالإنترنت عبر تور. المواقع المحجوبة في بلدك ستصبح متاحة الآن، وستظل اتصالاتك الشبكية مجهولة لأي شخص قد يراقب اتصالك بالإنترنت. ستلاحظ أيضا أن بعض المواقع -مثل <a href="http://www.google.com">www.google.com</a>- ستفترض أحيانا أنك موجود في بلد آخر. هذا طبيعي عند استخدام تور.</p>

<p>إذا كانت ثمة مشاكل في اتصال تور فستظهر هذه الشاشة:</p>

<p><img alt="Tor/screenshots-ar/40.png" src="/sites/securitybkp.ngoinabox.org/files/u5/tor-ar/40.png" title="Tor/screenshots-ar/40.png" /></p>

<p><em>شكل 9: شاشة تور لا يعمل</em></p>

<p>إن طالعتك هذه الرسالة أو إن لم تعرض الشاشة أي شيء فراجع <a href="tor_troubleshooting">قسم 4.0 معالجة أعطال تور</a>.</p>

<p><strong>تحذير</strong>: إذا كنت تستخدم أي إضافة خدمة وسيط في فيرفكس (مثل FoxyProxy)، فعليك تعطيلها قبل تفعيل توربتن وإلا فقد لا يعمل تور كما ينبغي.</p>


