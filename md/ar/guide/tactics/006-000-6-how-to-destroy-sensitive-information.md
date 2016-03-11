

---

lang: ar
community: guide
type: tactics
legacy: True
child: False
weight: 006
title: 6. How to destroy sensitive information

---

<p>تناولَت الفصول السابقة عددا من الممارسات و&nbsp;الأدوات التي يمكن أن تُعِين على حماية البيانات الهامة، لكن ماذا يكون الحال إن رأيتَ أنك لم تعد بحاجة إلى ملفات معينة؟ إن أردت على سبيل المثال أن تحتفظ بالمحفوظة المعماة لوثائق قديمة كنسخة أرشيفية و&nbsp;أردت حذف النسخة الأصلية من حاسوب العمل، فكيف السبيل إلى فعل هذا؟</p>

<p>قد يبدو للوهلة الأولى أن الحل هو <a href="/ar/glossary#deletion_vs_wiping">حذف</a> الملفات غير المرغوب فيها، لكن كما جاء في <a href="/ar/chapter_05_4">فصل تدارك حذف البيانات غير المقصود</a> فإنه توجد أدوات قد يمكن باستخدامها استرجاع ملفات سبق حذفها، و&nbsp;ذلك بسبب الطريقة التي يعمل بها تخزين البيانات على الوسائط الرقمية. و&nbsp;للتيقن من أن البيانات المحذوفة لا يمكن استرجاعها من قبل طرف آخر ينبغي استخدام برمجيات خاصة <a href="/ar/glossary#deletion_vs_wiping">تمحوها</a> محوا آمنا، كمثل مفرمة الأوراق التي توجد في المكتب؛ أداة مثل <a href="/ar/eraser">إريسر</a>.</p>

<p>حذف البيانات المتقادمة هو أحد استخدامات المحو، لكنك ما أن تدرك ما قد يجده خصم ما من معلومات عن منظمتك و&nbsp;نشاطك في كمّ الملفات التي كنت تظن أنك حذفتها في حين يمكنه استرجاعها، فإن استخدامات أخرى سترد على ذهنك، مثل محو سواقات الأقراص الصلبة المتقادمة قبل التخلص منها، و&nbsp;محو سجلات نشاط استخدام التطبيقات في الحاسوب، و&nbsp;تأريخ تصفح الوب، و&nbsp;الذاكرة المخبئية و&nbsp;الملفات المؤقتة. <a href="/ar/ccleaner">سيكلينر</a> هي الأداة الأخرى المشروحة في هذا الفصل و&nbsp;تساعد في محو الأنواع الثلاثة الأخيرة من البيانات و&nbsp;أنواع أخرى من المعلومات التي تولدها الحواسيب و&nbsp;تحفظها تلقائيا دون تدخُّلٍ من المستخدم.</p>

<div class="backgroundscenario">
	<h2>سيناريو تطبيقي</h2>
	<p><span class="actorname">إلِينا</span> ناشطة بيئية في دولة ناطقة بالروسية، و&nbsp;هي تدير موقعا على الوب تزداد شهرته باضطراد لتوثيقه الأنشطة غير المشروعة التي تدمر الغابات في المنطقة، و&nbsp;هي تحتفظ بنسخ احتياطية من محتوى الموقع في منزلها و&nbsp;في المكتب و&nbsp;على حاسوبها المحمول، و&nbsp;من ضمن هذه المعلومات سجلات الزوار و&nbsp;مداخلاتهم في منتدى الموقع. تنوي إِلينا السفر قريبا إلى دولة أخرى لتحضر مؤتمرا للناشطين البيئيين، و&nbsp;قد أبلغها بعضهم أن حواسيبهم قد أخذت عند المعابر الحدودية لمدة تزيد على الساعة و فحصت محتوياتها، و&nbsp;لأجل حماية بياناتها الحسّاسة و&nbsp;لسلامة النشطاء المتداخلين في موقعها فقد وضعت محفوظتها التي في المنزل و&nbsp;المكتب في مجلدات معماة باستخدام تروكربت و&nbsp;حذفت النسخة على حاسوبها. و&nbsp;هي تستشير ابن أختها نِيكولاي، و&nbsp;قد نبَّهها أنه عليها أن تفعل ما يزيد على مجرّد حذف المحفوظة القديمة إن كانت تخشى أن يُفحص حاسوبها عند الحدود أو&nbsp;يصادر.</p>
</div>

<h2>ما يتناوله هذا الفصل</h2>
<ul>
	<li>محو البيانات الحسّاسة من الحاسوب بحيث لا تُسترجع</li>
	<li>تمحو البيانات المخزنة على وسائط محمولة مثل الأقراص المدمجة وشذرات الذاكرة</li>
	<li>تقليل قدرة المهاجمين من معرفة معلومات عن الوثائق التي عَمِلتَ عليها مؤخرا على الحاسوب</li>
	<li>محو وسيط التخزين بحيث لا يمكن استرجاع الملفات التي كانت قد حذفت سابقا</li>
</ul>
