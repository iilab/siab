

---

lang: ar
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: Using the Tor Browser

---

<p>هناك العديد من الأسباب التي قد تمنع تور من العمل بشكل سليم. بعض الأمور الشائعة موضحة هنا، مع حلول مقترحة. تأكد من أن كل البرامج الموجودة في باقة ڤيداليا مثبتة وتعمل بشكل سليم. كل الوظائف المذكورة في هذا القسم متاحة عبر <i>لوحة تحكم ڤيداليا</i>.</p>

<p><strong>ملاحظة</strong>: إعادة تشغيل ويندوز هو أحد أفضل الطرق للتأكد من أن البرمجيات المثبتة حديثا تعمل كما يجب. جزء كبير من الأعطال الشائعة يمكن حله بهذه الطريقة!</p>

<h3>4.1 كيف تستعرض سجل الرسائل</h3>

<p>يمكنك مشاهدة سجل رسائل تور في أي وقت يعمل فيه، حتى أثناء محاولته القيام بالاتصال الأولي. يمكن أن يساعدك هذا في معرفة ما إذا كان يعمل، وما قد يكون سبب عطله إذا كان لا يعمل.</p>

<p><strong>انقر</strong> على: <img alt="Tor/screenshots-ar/12.png" src="/sites/securitybkp.ngoinabox.org/files/u5/tor-ar/12.png" title="Tor/screenshots-ar/12.png" /></p>

<p><i>سجل الرسائل</i> الذي سيظهر سيشبه <i>شكل 13</i>.</p>

<p><img alt="Tor/screenshots-ar/17.png" src="/sites/securitybkp.ngoinabox.org/files/u5/tor-ar/17.png" title="Tor/screenshots-ar/17.png" /></p>

<p><i>شكل 13: سجل رسائل ڤيداليا</i></p>

<p>يبين هذا السجل أن تور قد بدأ. وسيواصل عرض رسائل عن حال عمل تور. يجب ألا تقلق من تحذير "experimental software" (برمجيات قيد التجربة). فعلى الرغم مما تقوله هذه الرسالة، تور هو أكثر برمجيات المجهولية المتاحة اختبارا. هناك بعض رسائل الأعطال التي يجب أن تتحقق منها إن كنت تعاني من مشاكل مع تور:</p>

<ul>
	<li><i>connection_create_listener(): Could not bind to 127.0.0.1:9050: Address already in use. Is Tor already running?</i></li>
</ul>

<p>يعني هذا أن عملية تور أخرى قد بدأت من قبل. أبسط حل في هذه الحالة هو غلق ڤيداليا وإعادة تشغيل الحاسوب.</p>

<ul>
	<li><i>Vidalia was unable to start Tor. Check your settings to ensure the correct name and location of your Tor executable is specified</i></li>
</ul>

<p>يحدث هذا العطل عندما يتعذّر على ڤيداليا العثور على ملف تور التنفيذي <i>tor.exe</i>. ابحث عن هذا الملف على حاسوبك وحدد مكانه في لسان <i>عامة</i> من نافذة <i>تضبيطات ڤيداليا</i>.</p>

<ul>
	<li><i>I have learned some directory information, but not enough to build a circuit</i></li>
</ul>

<p>قد تتكر هذه الرسالة عند بدء تشغيل تور، وقد تستمر لفترة إذا كان اتصالك بالإنترنت بطيئا. تعني ببساطة أن تور مازال ينزّل معلومات شبكة المجهولية.</p>

<p>عندما يصبح تور جاهزا لاستخدامه، ستظهر هذه الرسالة في السجل:</p>

<ul>
	<li><i>Tor has successfully opened a circuit. Looks like client functionality is working.</i></li>
</ul>

<p><img alt="Tor/screenshots-ar/18.png" src="/sites/securitybkp.ngoinabox.org/files/u5/tor-ar/18.png" title="Tor/screenshots-ar/18.png" /></p>

<p><i>شكل 14: رسالة نجاح تور في الاتصال</i></p>

<p>توضح هذا الرسالة أن تور قد كون مسارا عبر شبكته ويعمل بشكل سليم. إذا كنت تستعمل فيرفكس، فسيبقى تفعيل زز تور قبل أن تستطيع تصفح المواقع خفية. إذا كنت تستخدم تطبيقا آخر فسيكون عليك ضبط إعدادات الوسيط (بروكسي) ليتصل بالإنترنت عبر تور.</p>

<p>إذا فشل السجل في عرض أي معلومات جديدة خلال خمس عشرة دقيقة بعد عرض رسالة "Opening Control listener" أو "Tor has learned some directory information, but not enough to build a circuit"، فقد تحتاج لضبط إعدادات شبكة تور. من الممكن أن اتصالك الحالي بالإنترنت يتطلب استخدام وسيط وب معين أو أنه يحجب منافذ بعينها. من الممكن أيضا أن حكومتك أو مزود خدمة الإنترنت بدأ في حجب الوصول إلى شبكة تور.</p>

<h3>4.2 إعدادات شبكة تور</h3>

<p>هناك بعض الخطوات التي قد تحتاج لاتخاذها إذا وجدت أن تور أصبح لا يعمل كما ينبغي أو فشل في الاتصال أول مرة بعد تثبيته. جرب تغيير تضبيطات الشبكة المتعلقة بالوسيط أو المحطات الجسر، كما يلي.</p>

<p><strong>خطوة 1</strong>. <strong>أوقف</strong> خدمة تور في ڤيداليا.</p>

<p><strong>خطوة 2</strong>. <strong>افتح</strong> شاشة <i>تضبيطات ڤيداليا</i>.</p>

<p><strong>خطوة 3</strong>. <strong>انقر</strong>: <img alt="Tor/screenshots-ar/19.png" src="/sites/securitybkp.ngoinabox.org/files/u5/tor-ar/19.png" title="Tor/screenshots-ar/19.png" /></p>

<p><img alt="Tor/screenshots-ar/20.png" src="/sites/securitybkp.ngoinabox.org/files/u5/tor-ar/20.png" title="Tor/screenshots-ar/20.png" /></p>

<p><i>شكل 15: شاشة التضبيطات في لوحة تحكم ڤيداليا</i></p>

<p>بعد انتهائك من هذه التضبيطات، <strong>انقر</strong> على زر <strong>موافقة</strong> لغلق نافذة تضبيطات الشبكة، ثم <strong>شغل</strong> خدمة تور من ڤيداليا.</p>

<h4>4.2.1 تستخدام وسيط شبكة</h4>

<p>إذا كنت محتاج لخادوم وسيط لتصل إلى الإنترنت فضع تفاصيله في هذه النافذة. عامة يشيع هذا في شبكات الشركات والجامعات، لقد قد تحتاج لها أحيانا في مقاهي الإنترنت أو حتى لكل البلد في بعض الدول. إذا لم تعرف معلومات الوسيط المطلوبة بشكل واضح فاسأل مدير الشبكة أة أي شخص آخر يستخدم نفس الاتصال.</p>

<p><strong>خطوة 1</strong>. <strong>أشّر</strong> على خيار <i>أستخدم وسيطا للوصول إلى الإنترنت</i>.</p>

<p><strong>خطوة 2</strong>. <strong>أدخل</strong> تفاصيل الوسيط في الحقول المتاحة:</p>

<p><img alt="Tor/screenshots-ar/25.png" src="/sites/securitybkp.ngoinabox.org/files/u5/tor-ar/25.png" title="Tor/screenshots-ar/25.png" /></p>

<p><strong>شكل 16: قسم تفاصيل الوسيط<i> </i></strong></p>

<h4>4.2.2 القيود على المنافذ</h4>

<p>بعض إعدادات الشبكة أو الحاسوب قد تقيّد الوصول إلى بعض المنافذ. إذا كنت تتصفح المواقع بلا مشكلة، فيمكنك إذا الاعتماد على أن منفذين على الأقل (80 و 443) متاحين. يمكنك ضبط تور ليعمل حصريا عبر هذه المنافذ.</p>

<p><strong>خطوة 1</strong>. <i>أشّر<strong> على خيار </strong></i><strong>جداري الناري يسمح لي بالاتصال عبر منافذ معينة فقط<i>. </i></strong></p>

<p><strong>خطوة 2</strong>. حقل <i>المنافذ المسموحة</i> سيحتوي بالفعل على '80,443'، كما في <i>شكل 17</i> أسفل:</p>

<p><img alt="Tor/screenshots-ar/24.png" src="/sites/securitybkp.ngoinabox.org/files/u5/tor-ar/24.png" title="Tor/screenshots-ar/24.png" /></p>

<p><i>شكل 17: قسم إعدادات جدار النار يحدد المنافذ المفتوحة في الشبكة</i></p>

<h4>4.2.3 استخدام محطة جسر</h4>

<p>إذا لا تستطيع الاتصال بشبكة تور حتى الآن، فأمامك خيارين:</p>

<p><strong>الخيار 1</strong>: راجع <a class="ext-link" href="http://wiki.noreply.org/noreply/TheOnionRouter/TorFAQ"><span class="icon">ويكي أسألة تور الشائعة</span></a> لبعض الاقتراحات.</p>

<p><strong>الخيار 2</strong>: قد تكون مقيما في واحد من البلدان التي تحجب شبكة تور. في هذه الحالة ستحتاج لاستخدام <i>محطة جسر</i> لتصل إلى تور.</p>

<p>تتيح لك الجسور الوصول إلى شبكة تور -حتى لو كانت محجوبة في بلدك- بتوفير 'مدخل' خفي إلى الشبكة. لتستطيع استخدام هذه الخاصية ستحتاج إلى إعطاء تور مكان واحدة على الأقل من المحطات الجسور. من الأفضل إدخال ثلاثة عناوين أو أكثر. إذا كنت تعرف وتثق في شخص يستخدم جسرا بالفعل فيمكنك أخذ هذه المعلومات منه. أو يمكنك استخدام إحدى الطريقتين المعتمدتين من مشروع قاعدة بيانات جسور تور. الأول، إرسال بريد إلى [bridges@torproject.org] من أي حساب جيميل، محتويا الكلمات "get bridges" في متن الرسالة. سترد عليك قاعدة البيانات بعناوين ثلاثة جسور. (تذكر يجب أن تلج دائما وأبدا إلى حساب جيميل عبر العنوان <a class="ext-link" href="https://mail.google.com"><span class="icon">https://mail.google.com</span></a> فقط!) كبديل، يمكنك زيارة موقع قاعدة بيانات الجسور في <a class="ext-link" href="https://bridges.torproject.org/"><span class="icon">https://bridges.torproject.org/</span></a> (بينما تستخدم تور)، وسيعرض معلومات عن ثلاثة جسور مختلفة.</p>

<p><strong>ملاحظة</strong>: صممت قاعدة البيانات لتمنع أي شخص من معرفة كل الجسور بسهولة، لذا قد يبدو أنها تعطيك نفس الجسور كل مرة تسأل فيها. إذا انتظرت لبعض الوقت فستعطيك معلومات جديدة.</p>

<p><strong>خطوة 1</strong>. <strong>أشّر</strong> على خيار <i>مزود خدمة الانترنت يحجب شبكة تور</i>.</p>

<p><strong>خطوة 2</strong>. <strong>اكتب</strong> أو <strong>الصق</strong> عنوان جسر في خانة <strong>أضف جسرا</strong>. كما ترى في <i>شكل 18</i>، تشمل معلومات الجسر عنوان IP ورقم منفذ مثل '79.47.201.97:443<i>، وقد تحتوي أيضا سلسلة من الحروف والأرقام في النهاية، مثل </i>80E03BA048BFFEB4144A4359F5DF7593A8BBD47B<i>. </i></p>

<p><strong>خطوة 3</strong>. <strong>انقر</strong>: <img alt="Tor/screenshots-ar/29.png" src="/sites/securitybkp.ngoinabox.org/files/u5/tor-ar/29.png" title="Tor/screenshots-ar/29.png" /></p>

<p><strong>خطوة 4</strong>. كرر الخطوات السابقة لكل عنوان جسر إضافي. ينصح بأن تدخل ثلاثة على الأقل.</p>

<p><img alt="Tor/screenshots-ar/28.png" src="/sites/securitybkp.ngoinabox.org/files/u5/tor-ar/28.png" title="Tor/screenshots-ar/28.png" /></p>

<p><i>شكل 18: إدخال عوان محطة جسر</i></p>

<h3>4.3 إزالة باقة ڤيداليا</h3>

<p>لإزالة الحزم المضمنة في باقة ڤيداليا، قم بالخطوات التالية:</p>

<p><strong>خطوة 1</strong>. <strong>اختر</strong> Select Start ‏&gt; Programs ‏&gt; Vidalia Bundle ‏&gt; Uninstall</p>

<p><strong>خطوة 2</strong>. <strong>اختر</strong> لغة المثبت ثم <strong>انقر<i> </i></strong><i>التالي<strong> </strong></i></p>

<p><strong>خطوة 3</strong>. <strong>أشّر</strong> على الحزم الثلاثة المعروضة في النافذة</p>

<p><img alt="Tor/screenshots-ar/50.png" src="/sites/securitybkp.ngoinabox.org/files/u5/tor-ar/50.png" title="Tor/screenshots-ar/50.png" /></p>

<p><strong>خطوة 4</strong>. <strong>انقر</strong> على <i>التالي</i> ثم <strong>انقر</strong> <i>Uninstall</i>.</p>

<p><strong>المستوى</strong>: <span class="underline"><strong>4: خبير</strong></span></p>

<p>بالإضافة إلى التحكم في استخدام فيرفكس لتور من عدمه أثناء تصفح الإنترنت، يرفع توربتن من سرية ومجهولية جلستك بغلق نقاط ضعف معينة في فيرفكس. بدون توربتن، يظل بإمكان موقع وب أو خادوم تور خبيث كشف بعض المعلومات عن مكانك على الإنترنت ونشاطاتك على الشبكة، حتى وأنت تستخدم تور. لحسن الحظ إعدادات توربتن المبدئية آمنة جدا. يمكنك تغيير هذه الإعدادات، يفضل ألا تفعل إلا إذا كنت تفهم جيدا الأمور المتعلقة بأمن المتصفحات.</p>

<p>تحتوي نافذة <i>تفضيلات توربتن</i> على ثلاثة ألسنة تمكنك من تحديد خيارات مختلفة:</p>

<ul>
	<li>لسان <strong>تضبيطات الوسيط</strong></li>
	<li>لسان <strong>تضبيطات السرية</strong></li>
	<li>لسان <strong>تضبيطات العرض</strong></li>
</ul>

<p>يمكن الوصول إلى نافذة <i>تضبيطات توربتن</i> سواء كان توربتن مفعّل أو معطّل. لتنشيط نافذة <i>تضبيطات توربتن</i>، قم بالخطوات التالية:</p>

<p><strong>خطوة 1</strong>. <strong>انقر بالزر الأيمن</strong> على توربتن لتنشيط قائمته كما يلي:</p>

<p><img alt="Tor/screenshots-ar/36.png" src="/sites/securitybkp.ngoinabox.org/files/u5/tor-ar/36.png" title="Tor/screenshots-ar/36.png" /></p>

<p><i>شكل 19: قائمة توربتن</i></p>

<p><strong>خطوة 2</strong>. <strong>اختر</strong> خيار <strong>التفضيلات...</strong> لتنشيط الشاشة التالية:</p>

<p><img alt="Tor/screenshots-ar/37.png" src="/sites/securitybkp.ngoinabox.org/files/u5/tor-ar/37.png" title="Tor/screenshots-ar/37.png" /></p>

<p><i>شكل 20: نافذة تفضيلات توربتن تعرض لسان تضبيطات الوسيط</i></p>

<h3>5.1 لسان تضبيطات الوسيط</h3>

<p>يتحكم لسان <i>تضبيطات الوسيط</i> في كيفية نفاذ فيرفكس إلى الأنترنت أثناء تفعيل توربتن. لا تحتاج إلى تغيير أي شيء في هذا اللسان.</p>

<h3>5.2 لسان تضبيطات السرية</h3>

<p>لسان <i>تضبيطات السرية</i> موجه للمستخدمين المطلعين جيدا على أمور سرية الإنترنت ومتصفحات الوب. توفر إعداته البدئية مستوى مرتفعا من الخصوصية للمستخدم العادي. يتيح لك هذا اللسان التحكم في تأريخ المتصفح، الذاكرة المخبئية، الكعكات وخصائص أخرى في فيرفكس.</p>

<p><img alt="Tor/screenshots-ar/39.png" src="/sites/securitybkp.ngoinabox.org/files/u5/tor-ar/39.png" title="Tor/screenshots-ar/39.png" /></p>

<p><i>شكل 21: لسان تضبيطات السرية</i></p>

<p>خيار <i>امنع الملحقات أثناء عمل تور</i> واحد من تضبيطات السرية القليلة التي قد ترغب في تغييرها، لكن عليك فعل هذا مؤقتا. لعرض محتوى الفديو على الشبكة، تحتاج بعض المواقع --مثل يوتيوب و DailyMotion و 'The Hub'-- لتعطيل هذا الخيار. عليك تفعيل الملحقات أثناء زيارة المواقع التي تثق بها، بعد أن تنتهي عليك العودة إلى لسان <i>تضبيطات السرية</i> و<i>التأشير</i> على هذا الخيار مرة أخري.</p>

<p>لمزيد من المعلومات عن وظيفة كل خيار في لسان <i>تضبيطات السرية</i>، راجع <a class="ext-link" href="https://www.torproject.org/torbutton/options.html.en"><span class="icon">موقع توربتن</span></a>.</p>

<h3>5.3 لسان تضبيطات العرض</h3>

<p>يتيح لك لسان <i>تضبيطات السرية</i> اختيار كيف يعرض توربتن في شريط حالة فيرفكس، كأيقونة على شكل بصلة أو نص. لا يؤثر هذا على وظيفته.</p>

<p><img alt="Tor/screenshots-ar/38.png" src="/sites/securitybkp.ngoinabox.org/files/u5/tor-ar/38.png" title="Tor/screenshots-ar/38.png" /></p>

<p><i>شكل 22: لسان تضبيطات العرض</i></p>

<p>لمزيد من المعلومات عن توربتن، راجع <a class="ext-link" href="https://www.torproject.org/torbutton/faq.html.en"><span class="icon">أسئلة توربتن الشائعة</span></a>.</p>

<h3>5.4 إزالة توربتن</h3>

<p>لإزالة هذه الإضافة، قم بالخطوات التالية في موزيلا فيرفكس:</p>

<p><strong>خطوة 1</strong>. <strong>اختر: الأدوات &gt; الإضافات</strong></p>

<p><strong>خطوة 2</strong>. <strong>اختر</strong> إضافة توربتن ثم <strong>انقر</strong> على <i>أزل</i></p>

<p><img alt="Tor/screenshots-ar/05.png" src="/sites/securitybkp.ngoinabox.org/files/u5/tor-ar/05.png" title="Tor/screenshots-ar/05.png" /></p>

<p><strong>خطوة 3</strong>. <strong>أعد تشغيل</strong> فيرفكس</p>


