

---

lang: ar
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: How to Install and Launch COMODO Firewall 

---

<p><strong>هام</strong>: ستُسأل أثناء تثبيتك <strong>لجدار النار كومودو</strong> عن ما إذا كان لديك "أي جدار ناري شخصي إضافي مثبّت." عليك استخدام جدار ناري واحد على حاسوبك. إذا كنت تستخدم جدارا ناريا أخر فعليك إزالته قبل تثبيت كومودو.</p>

<p><strong>ملاحظة</strong>: يُفعّل <strong>ويندوز إكس.بي بروفشيونال إديشن</strong> (<strong>الحزمة الخدمية 2</strong>) <strong>جدار ويندوز الناري</strong> تلقائيا. سيطلب منك كومودو تعطيل جدار النار تلقائيا. إذا لم تفعل فتستطيع تعطيل جدار ويندوز الناري يدويا عبر الخطوات التالية:</p>

<p><strong>خطوة 1</strong>. <strong>اختر: ابدأ &gt; لوحة التحكم &gt; جدار ويندوز الناري</strong> لتفتح هذه الشاشة:</p>

<p><img alt="CPF/screenshots-en/43.PNG" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo/43.PNG" title="CPF/screenshots-en/43.PNG" /></p>

<p><i>شكل 1: شاشة جدار ويندوز الناري</i></p>

<p><strong>خطوة 2</strong>. <strong>علّم</strong> على خيار <i>‭Off (not recommended)‬</i></p>

<p><strong>خطوة 3</strong>. <strong>انقر</strong> على: <img alt="CPF/screenshots-en/39.PNG" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo/39.PNG" title="CPF/screenshots-en/39.PNG" /> لتعطيل جدار ويندوز الناري.</p>

<h3>2.1 كيف تمنح أو تمنع الوصول</h3>

<p>بعد تثبيت جدار النار كومودو سيطلب منك تحديد الصلاحيات التي تتحكم في كيفية اتصال البرامج الموجودة على حاسوبك بالإنترنت. بشكل عام يُسمح بالطلبات السليمة وتُمنع الطلبات المشبوهة، لكن تمييز الطلبات السليمة من الخبيثة قد يتطلب بعض الخبرة.</p>

<p>في كل مرة يُرسل فيها طلب تظهر نافذة <i>تحذير أمني</i> تشبه هذه:</p>

<p><img alt="CPF/screenshots-en/01.png" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo/01.png" title="CPF/screenshots-en/01.png" /></p>

<p><i>شكل 2: مثال على شاشة التحذير الأمني لجدار النار كومودو</i></p>

<p><strong>ملاحظة:</strong> صممت برمجيات الجدر النارية لتحمي حاسوبك من المخترقين والبرمجيات الخبيثة. قد يحاول كلاهما النفاذ إلى حاسوبك مباشرة أو إرسال معلومات من حاسوبك إلى أطراف أخرى. لذا يحتاج الجدار النار الجديد إلى معرفة أي البرمجيات 'جيدة' ويمنحها صلاحية الوصول بينما يبقى مغلقا في وجه البرمجيات والعمليات الأخرى على حاسوبك. ستحتاج إلى فحص كل الطلبات الجديدة وتقرر هل تسمح بهم أم تمنعهم.</p>

<p><strong>هام</strong>: <i>يجب</i> أن تقرأ المعلومات الموجودة في حقلي <i>Application</i> و <i>Parent</i> في قسم <i>Details</i> من شاشة التحذير الأمني. لاحظ:</p>

<ul>
	<li>التطبيق <i>Application</i> يطلب الاتصال بالإنترنت.</li>
	<li>الأصل <i>Parent</i> هو البرنامج الذي نفذ طلب تشغيل التطبيق.</li>
</ul>

<p>عادة، بضعة تطبيقات فقط ستظهر في حقل <i>Application</i>. قد تشمل هذه متصفح الإنترنت و عميل البريد الإلكتروني وبرمجية التراسل الفوري. قد تتعرف على الكثير من هذه التطبيقات من أسمائها. الطلب الأصل (Parent) - رغم أنه قد لا يوجد دائما - قد يأتي من العديد من المصادر، بعضها سليم وبعضها خبيث.</p>

<p><img alt="CPF/screenshots-en/02.png" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo/02.png" title="CPF/screenshots-en/02.png" /></p>

<p><i>شكل 3: شاشة تحذير أمني تعرض طلب <span class="underline">Generic Host Process for Win32 Services</span></i></p>

<p><strong>مثال</strong>: في <i>شكل 3</i> <i>التطبيق</i> هو <i>svchost.exe</i> و<i>الأصل</i> هو <i>services.exe</i>. لوحة <i>اعتبارات الخصوصية</i> (Security Considerations) تعرض تفاصيل البرنامج الذي يطلب الوصول إلى الإنترنت عبر <i>الأصل</i> و <i>التطبيق</i>. في هذه الحالة، برنامج سليم يسمى <strong>Windows Explorer</strong> يطلب الوصول إلى الإنترنت. سيكون هذا في الغالب أحد أول شاشات <i>التحذير الأمني</i> التي ستراها بعد تثبيت جدار النار كومودو وإعادة تشغيل الحاسوب.</p>

<p><strong>هام</strong>: بعض الفيروسات الذكية تستطيع محاكاة تطبيقات <strong>ويندوز</strong> السليمة. لا توجد طريقة سهلة لتمييزهم عن طلبات الوصول الحقيقية. يجب أن تكون شديد الحذر عند تنزيل أي شيء من على الإنترنت، وأن تفحص حاسوبا دوريا بحثا عن الفيروسات والبرمجيات الخبيثة.</p>

<p><strong>ملاحظة</strong>: عادة ما تكون الطلبات السليمة ناتجا عن فعل منك. مثلا، عندما تشغل برنامجا جديدا للمرة الأولى فسيطلب منك جدار النار تحديد صلاحيات الوصول. قد يحدث هذا أيضا عند تثبيت أو إزالة البرمجيات. قد تحتاج لبعض الوقت حتى تعتاد على هذا، لكن سريعا ما 'سيتعلم' جدار النار اختياراتك وستتوقف هذه الرسائل.</p>

<p><strong><i>Muhindo</i></strong><i>: إذا إذا تعرفت على أحد البرامج التي ثبتها على حاسوبي فهل من الأمان أن أمنحه الوصول؟</i></p>

<p><strong><i>Assani</i></strong><i>: عليك أن تكون حريصا. كثيرا ما يطلب ويندوز الوصول إلى الإنترنت وسيسألك كومودو منع هذا أو السماح به. ولكن أحيانا تستطيع الفيروسات تقليد برامج أو عمليات ويندوز.</i></p>

<p><strong><i>Muhindo</i></strong><i>: إذن كيف أميز الطلب الحقيقي من الخبيث؟</i></p>

<p><strong><i>Assani</i></strong><i>: عليك التأكد من أن حاسوبك ليس مصابا بالفيروسات أو برمجيات التجسس. لهذا من المهم جدا أن يكون لديك مضادات فيروسات مثل</i> <a href="avast">أڤاست</a> <i>ومضادات التجسس مثل</i> <a href="spybot">سباي‌بوت</a> <i>و أن تفحص حاسوبك بانتظام.</i></p>

<p><img alt="CPF/screenshots-en/23.png" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo/23.png" title="CPF/screenshots-en/23.png" /></p>

<p><i>شكل 4: شاشة تحذير أمني تعرض طلب وصول من كي‌پاس</i></p>

<p>في أوقات أخرى قد يعرض جدار النار كومودو رسالة مختلفة قليلا. في المثال السابق يحاول برنامج <a href="keepass">خزانة كلمات السر كي‌پاس</a> استخدام المتصفح فيرفكس للوصول إلى الإنترنت. و حيث أن كي‌پاس برنامج سليم سبق تثبيته على الحاسوب فيمكننا السماح بهذا الطلب.</p>

<p><strong>فائدة</strong>: <strong>انقر</strong>: <img alt="CPF/screenshots-en/31.png" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo/31.png" title="CPF/screenshots-en/31.png" /> في قسم <i>Details</i> من شاشة <i>التحذير الأمني</i> لتطلع على معلومات هذه العملية.</p>

<p><img alt="CPF/screenshots-en/24.png" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo/24.png" title="CPF/screenshots-en/24.png" /> <img alt="CPF/screenshots-en/25.png" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo/25.png" title="CPF/screenshots-en/25.png" /></p>

<p><i>شكل 5: شاشة <span class="underline">تفاصيل التطبيق</span></i> <i>شكل 6: شاشة <span class="underline">تفاصيل التطبيق</span> في <span class="underline">وضع الأصل</span></i></p>

<p>أو يمكنك البحث عن أسماء هذه العمليات في الإنترنت فربما تجد معلومات عن سلوكها والغرض منها.</p>

<ul>
	<li>إذا أظهر بحثك أنه قد يكون فيروسا، أو لم تستطع تتبع مصدر الرسالة <strong>فانقر</strong>: <img alt="CPF/screenshots-en/35.PNG" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo/35.PNG" title="CPF/screenshots-en/35.PNG" /></li>
</ul>

<p><strong>هام</strong>: من الأفضل أن تتخذ الأحوط وتمنع الطلبات التي لا تتعرف عليها. إذا أدى هذا إلى توقف أحد البرامج عن العمل بشكل سليم فيمكنك السماح بهذه العملية عندما يسألك عنها جدار النار مرة ثانية. الحيطة والصرامة في منع العمليات هي الطريقة الأمثل لضمان أمان الحاسوب.</p>

<ul>
	<li>إذا تأكدت من أنه طلب وصول صالح <strong>فانقر</strong>: <img alt="CPF/screenshots-en/32.PNG" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo/32.PNG" title="CPF/screenshots-en/32.PNG" /></li>
</ul>

<p><strong>ملاحظة</strong>: أحيانا يحاول نفس البرنامج الوصول إلى الإنترنت بطرق مختلفة، بعضها كان خفيا عنك في السابق. لا تقلق إذا تكرر طلب السماح لنفس البرنامج. بعد أن يعمل جدار النار كومودو لأسبوع أو ما شابه فستختفي أغلب شاشات <i>التحذير الأمني</i>.</p>

<p>هذا مثال على أداة خبيثة تطلب الوصول إلى الإنترنت عبر <strong>إنترنت إكسبلورر</strong>:</p>

<p><img alt="CPF/screenshots-en/26.png" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo/26.png" title="CPF/screenshots-en/26.png" /></p>

<p><i>شكل 7: شاشة تحذير أمني تعرض طلبا خبيثا من Wallbreaker.exe</i></p>

<p><strong>خطوة 1</strong>. <strong>انقر</strong>: <img alt="CPF/screenshots-en/31.png" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo/31.png" title="CPF/screenshots-en/31.png" /> إذا بدا اسم الأصل مريبا ولا علاقة له بأي برمجية ثبّتها على حاسوبك.</p>

<p><i>سيكشف هذا مصدره الحقيقي ومعلومات عنه كما يلي</i>:</p>

<p><img alt="CPF/screenshots-en/27.png" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo/27.png" title="CPF/screenshots-en/27.png" /></p>

<p><i>شكل 8: شاشة <span class="underline">تفاصيل التطبيق</span> في <span class="underline">وضع الأصل</span> ل‍ Wallbreaker.exe</i></p>

<p>بغض النظر عن القليل المعروف عن هذا التطبيق، فالبحث في جوجل عن <i>wallbreaker.exe</i> قد يكشف عن غرضه الحقيقي.</p>

<p><strong>خطوة 2</strong>. <strong>انقر</strong> زر <strong>امنع</strong> (Deny)، ثم افحص حاسوبك بمضاد فيروسات ومضاد تجسس مثل <a href="spybot">سپاي‌بوت</a>.</p>

<p><strong>فائدة</strong>: أشِّر على اختيار <i>تذكر إجابتي لهذا التطبيق</i> (Remember my answer for this application) حتى يتذكر جدار النار كومودو هذا القرار ولن تظهر هذه النافذة بعينها مرة أخرى في المستقبل.</p>

<p><strong><i>Salima</i></strong><i>: هناك الكثير من البرامج المثبتة على حاسوبي خلال سنوات، ماذا لو كنت لا أتذكرهم كلهم؟</i></p>

<p><strong><i>Assani</i></strong><i>: قد لا تتذكر أحيانا اسم برنامج ما. وكثيرا ما توجد برمجيات على حاسوبك نسيت وجودها، أو لم تثبتها بنفسك. ربما وضعه شخص آخر يستعمل الحاسوب وقد يكون سليما أو برمجية خبيثة. هذا ما تحتاج لفحصه، لكن لا تقلق فبمجرد قيامك بعملية التحقق من البرنامج مرة فلن تحتاج لتكرارها ثانيا. بعد عدة أيام سيكون من النادر أن ترى هذه الرسائل.</i></p>

<p><strong><i>Salima</i></strong><i>: وماذا يحدث لو قررت تنزيل برنامج جديد في المستقبل؟</i></p>

<p><strong><i>Assani</i></strong><i>: عندها سيسألك جدار النار إذا كنت تريد إضافة هذه البرنامج إلى قائمة البرامج المسموح لها بالوصول إلى الإنترنت.</i></p>

<p><strong>فائدة</strong>: رفض طلب اتصال بالإنترنت يعني أنك تعتبر هذه البرنامج أو العملية فيروسا أو برمجية خبيثة. يجب أن تحافظ على مضاد الفيروسات والبرمجيات الخبيثة محدثا وأن تفحص حاسوبك بشكل منتظم، <i>خاصة</i> بعد أن تستلم طلبا مشبوها لعبور جدار النار.</p>


