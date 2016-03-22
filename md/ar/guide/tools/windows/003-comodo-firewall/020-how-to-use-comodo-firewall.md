

---

lang: ar
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Use COMODO Firewall

---

<p>يوفر <strong>جدار النار كومودو</strong> لوحة تحكم شاملة تحتوي العديد من الخصائص والخيارات. يغطي هذا القسم الخيارات التي تتعلق بتشغيل جدار النار بالإضافة لبعض التلميحات السريعة لتتبع المشاكل.</p>

<p><strong>فائدة</strong>: <strong>انقر</strong>: <img alt="CPF/screenshots-en/09.png" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo/09.png" title="CPF/screenshots-en/09.png" /> لتطلع على الوثائق الشاملة لجدار النار كومودو.</p>

<h3>3.1 كيف تعرض شاشة الملخص</h3>

<p><strong>خطوة 1</strong>. <strong>اختر ابدأ &gt; البرامج &gt; Comodo &gt; ‏Firewall &gt; ‏Comodo Firewall Pro</strong> لتشغل الشاشة الرئيسية كما يلي:</p>

<p><img alt="CPF/screenshots-en/03.png" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo/03.png" title="CPF/screenshots-en/03.png" /></p>

<p><i>شكل 9: شاشة جدار النار كومودو الرئيسية في مشهد الملخص</i></p>

<p>يعرض <i>مشهد الملخص</i> معلومات عامة عن جدار النار كومودو. يوضح أي من خصائص البرامج تعمل، وإعدادات الشبكة، ومعلومات حركة البيانات، و <i>مستوى أمان الحاسوب</i> وغيرها من المعلومات.</p>

<p><strong>هام</strong>: مستوى أمان الحاسوب مضبوط مبدئيا على <i>مخصص</i> (Custom). يمكنك هذا الوضع من ضبط الإعدادات وصلاحيات الوصول المختلفة لكل البرامج.</p>

<p><strong>فائدة لتتبع المشاكل</strong>: إذا فقدت فجأة إمكانية الوصول إلى الإنترنت أو أي اتصال شبكي بعد تثبيت جدار النار كومودو فاسحب مؤشر <i>مستوى أمان الحاسوب</i> إلى إعداد <i>اسمح بالكل</i> (Alllow All). سيعطل هذا جدار النار، ما يفترض أن يعيد كل الاتصالات الشبكية إلى حالتها السابقة. لكن تذكر أن إعداد <i>اسمح بالكل</i> يستخدم <i>فقط</i> لاختبار الوصول إلى الخدمة، ويجب <i>ألا</i> تترك هذا الإعداد بعد أن تستعيد كل اتصالاتك الشبكية.</p>

<h3>3.2 كيف تحدد قواعد الوصول</h3>

<p>سيساعدك هذا القسم على معرفة المزيد عن تحديد قواعد الوصول والصلاحيات في <strong>جدار النار كومودو</strong>.</p>

<p><strong>خطوة 1</strong>. <strong>انقر</strong> على: <img alt="CPF/screenshots-en/10.png" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo/10.png" title="CPF/screenshots-en/10.png" /> لتنشيط شاشة جدار النار كومودو الرئيسية كما يلي:</p>

<p><img alt="CPF/screenshots-en/11.png" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo/11.png" title="CPF/screenshots-en/11.png" /></p>

<p><i>شكل 10: شاشة <span class="underline">جدار النار كومودو</span> في طور <span class="underline">السرية</span></i> لتوقف رسائل عبور جدار النار لبرنامج معين بمنحه صلاحية مرور كاملة:</p>

<p><strong>خطوة 2</strong>. <strong>انقر</strong> على خيار <strong>عرف تطبيقا موثوقا جديدا</strong> (Define a new Trusted Application) لتفتح الشاشة التالية:</p>

<p><img alt="CPF/screenshots-en/12.png" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo/12.png" title="CPF/screenshots-en/12.png" /></p>

<p><i>شكل 11: شاشة تأكيد <span class="underline">تطبيق موثوق</span></i></p>

<p><strong>خطوة 3</strong>. <strong>انقر</strong>: <img alt="CPF/screenshots-en/33.PNG" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo/33.PNG" title="CPF/screenshots-en/33.PNG" /> لتختار التطبيق (ومساره) الذي تريد جعله تطبيقا موثوقا.</p>

<p>في المثال السابق نختار الملف <i>Firefox.exe</i>. ما يعني أن جدار النار سيسمح الآن بكل طلبات <a href="firefox"><strong>فيرفكس</strong></a> للنفاذ إلى حاسوبك والإنترنت.</p>

<p><strong>ملاحظة:</strong> لا يعني هذا أن <span class="underline">جدار النار كومودو</span> سيسمح <i>لأي</i> برمجية بالوصول إلى الإنترنت عبر فيرفكس، بل سيكون عليك إعدادهم كل على حدة.</p>

<p><strong>خطوة 4</strong>. <strong>انقر</strong>: <img alt="CPF/screenshots-en/34.PNG" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo/34.PNG" title="CPF/screenshots-en/34.PNG" /></p>

<p>لعرض كل البرامج التي لها قواعد حاليا:</p>

<p><strong>خطوة 5</strong>. <strong>انقر</strong>: <img alt="CPF/screenshots-en/41.PNG" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo/41.PNG" title="CPF/screenshots-en/41.PNG" /> لتشغيل هذه الشاشة:</p>

<p><img alt="CPF/screenshots-en/13.png" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo/13.png" title="CPF/screenshots-en/13.png" /></p>

<p><i>شكل 12: شاشة <span class="underline">جدار النار كومودو</span> في طور <span class="underline">مراقب التطبيقات</span></i></p>

<p>تعرض شاشة <i>مراقب التطبيقات</i> (Application Monitor) صلاحيات الوصول للبرمجيات المختلفة التي عرّفتها من قبل. كل واحدة تقابل عملية داخل برنامج معين تتطلب النفاذ إلى اتصالك الصادر أو الوارد من الإنترنت.</p>

<p>قم بالخطوات التالية لتحككم في صلاحيات البرامج:</p>

<p><strong>خطوة 1</strong>. <strong>انقر مرتين</strong> على أي من العمليات المسرودة لتفتح شاشة تعرض صلاحياتها.</p>

<p><strong>خطوة 2</strong>. <strong>انقر</strong> على أزرار <strong>أضف</strong> (Add)، أو <strong>حرر</strong> (Edit)، أو <strong>احذف</strong> (Remove) في الزاوية العليا على اليمين من لوحة <i>قواعد التحكم في التطبيقات</i> (Application Control Rules) لتضيف أو تحرر أو تحذف صلاحيات البرنامج.</p>

<p><strong>خطوة 3</strong>. <strong>انقر</strong>: <img alt="CPF/screenshots-en/33.PNG" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo/33.PNG" title="CPF/screenshots-en/33.PNG" />لتحدد موضع مسار الملف التنفيذي للبرنامج ثم أضفه للقائمة.</p>

<p><img alt="CPF/screenshots-en/14.png" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo/14.png" title="CPF/screenshots-en/14.png" /></p>

<p><i>شكل 13: شاشة <span class="underline">قواعد التحكم في التطبيقات</span></i></p>

<h3>3.3 كيف تحدد قواعد الوصول (للمستخدمين ذوي الخبرة فقط)</h3>

<p>هذا القسم للمستخدمين المتقدمين وذوي الخبرة. يمكنك من الضبط الدقيق لإعدادات صلاحيات جدار النار عبر تحديد عناوين أرقام الإنترنت (IP)، واتجاه الاتصال وخيارات أخرى.</p>

<p>في المثال السابق، <i>كل</i> أنشطة <i>فيرفكس</i> مسموح بها. لكن إن أردت ضبط قواعد أكثر تحديدا فقم بهذه الخطوات:</p>

<p><strong>خطوة 1</strong>. <strong>أشّر</strong> على اختيار <i>طبّق هذه المعايير</i> (Apply the following criteria) تحت قسم <i>التطبيق / التطبيق الأصل</i> (Application / Parent Application) كما يلي:</p>

<p><img alt="CPF/screenshots-en/14.png" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo/14.png" title="CPF/screenshots-en/14.png" /></p>

<p><i>شكل 14: شاشة <span class="underline">قواعد التحكم في التطبيق</span></i></p>

<p><strong>خطوة 2</strong>. <strong>اختر</strong> صلاحية وصول من قائمة <i>الإجراءات</i> (Actions) المنسدلة.</p>

<p><strong>خطوة 3</strong>. <strong>اختر</strong> نوع البروتوكول من قائمة <i>البروتوكول</i> المنسدلة.</p>

<p><strong>خطوة 4</strong>. <strong>اختر</strong> اتجاه الاتصال من قائمة <i>الاتجاه</i> (Direction) المنسدلة.</p>

<h3>3.4 كيف تضيف صلاحيات لشبكة المكتب</h3>

<p>سيمنع <strong>جدار النار كومودو</strong> الوصول إلى حاسوبك من شبكة المكتب. قد يمنع أيضا أي طلبات يرسلها حاسوبك إلى الشبكة. قد يؤدى هذا إلى فقدانك لخدمات الشبكة، مثل الوصول إلى الإنترنت، والطباعة، ومشاركة المستندات والخدمات الأخرى. يجب عليك إعداد جدار النار كومودو بحيث يعرف أنك تعمل في شبكة ويسمح بوصولك إلى الشبكة.</p>

<p><strong>هام</strong>: قبل أن تبدأ ‌في إعداد المتطلبات الخاصة بالشبكة، تأكد أنك متصل بها.</p>

<p><strong>خطوة 1</strong>. <strong>انقر</strong>: <img alt="CPF/screenshots-en/10.png" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo/10.png" title="CPF/screenshots-en/10.png" /> في شاشة جدار النار كومودو.</p>

<p><strong>خطوة 2</strong>. <strong>انقر</strong>: <img alt="CPF/screenshots-en/28.png" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo/28.png" title="CPF/screenshots-en/28.png" /> لتشغيل <i>مساعد منطقة الشبكة المأمونة</i> (Trusted Network Zone Wizard) لضبط الإعدادات الخاصة بشبكتك.</p>

<p>يتكون <i>مساعد منطقة الشاشة المأمونة</i> من أربع شاشات تشبه <i>شكل 15</i> و <i>شكل 16</i>.</p>

<p><img alt="CPF/screenshots-en/29.png" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo/29.png" title="CPF/screenshots-en/29.png" /></p>

<p><i>شكل 15: شاشة الترحيب بمساعد منطقة الشبكة المأمونة</i></p>

<p><strong>خطوة 3</strong>. <strong>انقر</strong>: <img alt="CPF/screenshots-en/37.PNG" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo/37.PNG" title="CPF/screenshots-en/37.png" /></p>

<p><img alt="CPF/screenshots-en/30.png" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo/30.png" title="CPF/screenshots-en/30.png" /></p>

<p><i>شكل 16: شاشة اختيار المنطقة في <span class="underline">مساعد منطقة الشبكة المأمونة</span></i></p>

<p><strong>خطوة 4</strong>. <strong>اختر</strong> اتصال شبكة المكتب. عادة ما يكون هذا بطاقة الشبكة المحلية/إيثرنت.</p>

<p><strong>خطوة 5</strong>. <strong>انقر</strong>: <img alt="CPF/screenshots-en/37.PNG" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo/37.PNG" title="CPF/screenshots-en/37.png" /></p>

<p><i>سيتعرف كومودو تلقائيا على إعدادات الشبكة وسيُنشئ صلاحيات خاصة لها.</i></p>

<p><strong>خطوة 6</strong>. <strong>انقر</strong>: <img alt="CPF/screenshots-en/37.PNG" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo/37.PNG" title="CPF/screenshots-en/37.png" /></p>

<p><strong>خطوة 7</strong>. <strong>انقر</strong>: <img alt="CPF/screenshots-en/17.png" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo/17.png" title="CPF/screenshots-en/17.png" /> لتؤكد هذه الإعدادات وغيرها من إعدادات الصلاحيات الخاصة.</p>

<p><img alt="CPF/screenshots-en/18.png" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo/18.png" title="CPF/screenshots-en/18.png" /></p>

<p><i>شكل 17: شاشة <span class="underline">جدار النار كومودو</span> في طور <span class="underline">مراقب الشبكة</span></i></p>

<p>لتحدد أنك تريد أن يسمح جدار النار لمرد شبكة آخر معين (طابعة أخرى أو مسيّر) أو حاسوب خارج شبكتك، ففي الشاشة السابقة</p>

<p><strong>خطوة 8</strong>. <strong>انقر</strong>: <img alt="CPF/screenshots-en/40.PNG" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo/40.PNG" title="CPF/screenshots-en/40.png" /> لتشغيل شاشة <span class="underline">قواعد التحكم في الشبكة</span> كما يلي:</p>

<p><img alt="CPF/screenshots-en/19.png" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo/19.png" title="CPF/screenshots-en/19.png" /></p>

<p><i>شكل 18: شاشة <span class="underline">قواعد التحكم في الشبكة</span></i></p>

<p>في هذه الشاشة يمكنك تحديد استثناءات لجدار النار كومودو لتستطيع الوصول إلى موارد الشبكة المختلفة (طابعة أو مسيّر مثلا) أو حاسوب خارج شبكتك.</p>

<p>في المثال السابق تعطي الحاسوب أو الجهاز في العنوان 192.168.234.234 صلاحية الوصول لحاسوبك.</p>

<p><strong>خطوة 9</strong>. <strong>انقر</strong>: <img alt="CPF/screenshots-en/34.PNG" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo/34.PNG" title="CPF/screenshots-en/34.png" /></p>

<p><strong>هام</strong>: راجع مدير الشبكة لتعرف الصلاحيات الضرورية لجدار النار.</p>

<h3>3.5 كيف تطلع على سجل النشاط</h3>

<p>يحفظ <strong>جدار النار كومودو</strong> سجلا بكل النشاطات الصادرة والواردة في الأيام الثلاثين الأخيرة. قد يساعدك هذا على اكتشاف البرمجيات الخبيثة التي تحاول الاتصال بالإنترنت من حاسوبك، والمتطفلين الذين يحاولون اختراق حاسوبك.</p>

<p><strong>خطوة 1</strong>. <strong>انقر</strong>: <img alt="CPF/screenshots-en/20.png" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo/20.png" title="CPF/screenshots-en/20.png" /> و <img alt="CPF/screenshots-en/21.png" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo/21.png" title="CPF/screenshots-en/21.png" /> لتطلع على السجلات كما يلي:</p>

<p><img alt="CPF/screenshots-en/22.png" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo/22.png" title="CPF/screenshots-en/22.png" /></p>

<p><i>شكل 19: شاشة <span class="underline">جدار النار كومودو</span> الرئيسية في مشهد السجلات</i></p>

<p>يمكنك هنا الطلاع على كل تقارير الصادر والوارد التي سجلها جدار النار كومودو، شاملة وقت الحدوث ورقم (IP) مصدر ووجهة الحدث. يمكنك أيضا تحديد الحجم الأقصى للسجل (حيث أنه قد يتضخم بسرعة).</p>

<p><strong>ملاحظة:</strong> كثيرا ما تحاول بعض البرمجيات المثبتة على حاسوبك الاتصال بموقع معين بشكل متكرر، لا يعني هذا أنها برمجيات خبيثة فالكثير من هذه البرمجيات صممت هكذا. سيمنع جدار النار كومودو هذه المحاولات غير الضرورية. لا تقلق كثيرا من العدد الكبير الذي يظهر في السجلات.</p>

<p><strong>تحذير</strong>: قد تحاول الكثير من الحواسيب الاتصال بحاسوبك عبر الإنترنت؛ لكن لا يعني هذا دائما أن مخترقا يترصد بحاسوبك. قد يكون مجرد برمجية خبيثة مصمَّمة لاكتشاف الحواسيب غير المؤَمّنة. إذا اكتشفت هذه البرمجية أن حاسوبك بدون جدار نار فعال فقد تغرس فيروسا أو حصان طروادة أو أي من البرمجيات الخبيثة الأخرى. <strong>هذه البرمجيات يستخدمها مخترقي الإنترنت.</strong></p>

<h2>4.0 كيف تُحدّث جدار النار كومودو</h2>

<p>تظهر فيروسات وهجمات اختراق جديدة للحواسيب كل يوم. يجب تحديث <strong>جدار النار كومودو</strong> بانتظام ليستطيع حماية حاسوبك من المتطفلين بشكل فعال. يلتمس البرنامج التحديثات تلقائيا كل يوم، ويمكنك تحديثه يدويا عبر الخطوات التالية.</p>

<p><strong>خطوة 1</strong>. <strong>انقر</strong>: <img alt="CPF/screenshots-en/04.png" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo/04.png" title="CPF/screenshots-en/04.png" /> لتُشغل هذه الشاشة:</p>

<p><img alt="CPF/screenshots-en/05.png" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo/05.png" title="CPF/screenshots-en/05.png" /></p>

<p><i>شكل 20: شاشة التحديث التلقائي في جدار النار كومودو</i></p>

<p><strong>خطوة 2</strong>. <strong>انقر</strong>: <img alt="CPF/screenshots-en/38.PNG" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo/38.PNG" title="CPF/screenshots-en/38.png" /></p>

<p>بعد تنزيل كل التحديثات ستظهر رسالة التأكيد <i>تم تنزيل التحديثات</i> (Updates have been installed) كما يلي:</p>

<p><img alt="CPF/screenshots-en/08.png" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo/08.png" title="CPF/screenshots-en/08.png" /></p>

<p><i>شكل 21: شاشة قواعد التحكم في الشبكة</i><br />
<strong>خطوة 3</strong>. <strong>انقر</strong>: <img alt="CPF/screenshots-en/34.PNG" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo/34.PNG" title="CPF/screenshots-en/34.PNG" /> لتُنهي عملية التثبيت.</p>

<p>إذا نزلت أي تحديثات جديدة سيُطلب منك إعادة تشغيل النظام. لن تصبح التحديثات فعالة إلا بعد إعادة تشغيل الحاسوب، لذا عاجلا أفضل من تأجيله.</p>


