

---

lang: ar
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 4
depth: 3
title: Hidden Volumes

---

<p>
يمكن باستخدام تروكربت إنشاء مجلد معمى مخفي داخل مجلد تروكربت آخر عادي بحيث لا تظهر محتوياته عند وصل المجلد الخارجي، و لا يمكن حتى إثبات أو استنتاج وجوده عمليا. بالاستعداد مسبقا بهذه الكيفية يمكنك إذا ما أجبرت على الإفصاح عن كلمة سر مخزن بياناتك السري أن تدلي بها و عندها سيمكن فتحه و النفاذ إلى محتوياته التمويهية، إلا أن المحتويات السرية المحفوظة في المجلد المخفي ستظل آمنة.
</p>
<p>
يمكنك تشبيه الأمر بحافظة أوراق بها جيب سري. المستندات الحساسة حقا تحفظ في الجيب السري، بينما تترك مستندات <i>تبدو</i> هامة في جزئها العادي، فإذا ما كان الجيب السري جيد التصميم بحيث لا يكون وجوده ظاهرا فإنه محتوياته ستظل آمنة حتى لو ضاع منك مفتاح الحقيبة أو اضطررت إلى تسليمه.
</p>
<h3>5.1 إنشاء مجلد مخفي</h3>
<p>
إنشاء مجلد تروكربت مخفي مشابه لإنشاء مجلد عادي؛ يمر ببعض الشاشات و الخيارات.
</p>
<p>

<strong>خطوة 1</strong>. <strong>شغل</strong> برمجية تروكربت
</p>
<p>
<strong>خطوة 2</strong>. <strong>انقر</strong> <img src="/sites/securitybkp.ngoinabox.org/files/u5/truecrypt-ar/32.png" alt="source:TrueCrypt/screenshots-ar/32.png" title="source:TrueCrypt/screenshots-ar/32.png">
</p>
<p>
<strong>خطوة 3</strong>. <strong>اختر</strong> <i>أنشئ ملف حاويا معمى</i> في مرشد إنشاء مجلد تروكربت

</p>
<p>
<strong>خطوة 4</strong>. <strong>اختر</strong> <i>أنشء مجلد تروكربت مخفي</i>، كما يلي:
</p>
<p>
<img src="/sites/securitybkp.ngoinabox.org/files/u5/truecrypt-ar/22.png" alt="source:TrueCrypt/screenshots-ar/22.png" title="source:TrueCrypt/screenshots-ar/22.png">
</p>
<p>
<i>شكل 19: خيار إنشاء مجلد مخفي</i>
</p>
<p>

<strong>خطوة 5</strong>. <strong>انقر</strong> <img src="/sites/securitybkp.ngoinabox.org/files/u5/truecrypt-ar/33.png" alt="source:TrueCrypt/screenshots-ar/33.png" title="source:TrueCrypt/screenshots-ar/33.png">
</p>
<p>
هنا ستخير ما بين <i>الطور المباشر</i> الذي في ينشأ المجلد المخفي في داخل مجلد تروكربت عادي موجود بالفعل، أو <i>الطور العادي</i> الذي ينشأ فيه مجلد عادي جديد ثم مجلد مخفي في داخله. في هذا المثال سنختار <i>الطور المباشر</i>.
</p>

<p>
<strong>ملاحظة</strong>: إن كنت تفضل إنشاء مجلد عادي جديد فاتّبع الخطوات المشروحة في <a href="truecrypt_standard#std">القسم 2.1: إنشاء مجلد عادي</a>
</p>
<p>
<img src="/sites/securitybkp.ngoinabox.org/files/u5/truecrypt-ar/23.png" alt="source:TrueCrypt/screenshots-ar/23.png" title="source:TrueCrypt/screenshots-ar/23.png">
</p>
<p>
<i>شكل 20: خيار طور إنشاء مجلد مخفي</i>
</p>
<p>
<strong>خطوة 6</strong>. <strong>اختر</strong> <i>أنشئ مجلدا مخفيا داخل مجلد تروكربت موجود</i>

</p>
<p>
<strong>خطوة 7</strong>. <strong>انقر</strong> <img src="/sites/securitybkp.ngoinabox.org/files/u5/truecrypt-ar/33.png" alt="source:TrueCrypt/screenshots-ar/33.png" title="source:TrueCrypt/screenshots-ar/33.png">
</p>
<p>
<strong>خطوة 8</strong>. <strong>اختر</strong> ملف <i>مجلدي</i> المحفوظ في دليل <i>مستنداتي</i> الذي أنشأناه مسبقا.

</p>
<p>
<strong>ملاحظة</strong>: تأكد من كون المجلد مفوصلا قبل المواصلة.
</p>
<p>
<strong>خطوة 9</strong>. <strong>انقر</strong> <img src="/sites/securitybkp.ngoinabox.org/files/u5/truecrypt-ar/35.png" alt="source:TrueCrypt/screenshots-ar/35.png" title="source:TrueCrypt/screenshots-ar/35.png">
</p>
<p>
<img src="/sites/securitybkp.ngoinabox.org/files/u5/truecrypt-ar/24.png" alt="source:TrueCrypt/screenshots-ar/24.png" title="source:TrueCrypt/screenshots-ar/24.png">
</p>
<p>
<i>شكل 21: شاشة اختيار المجلد العادي</i>

</p>
<p>
<strong>خطوة 10</strong>. <strong>أوجد</strong> الملف في شاشة اختيار الملف الحاوي
</p>
<p>
<strong>خطوة 11</strong>. <strong>انقر</strong> <img src="/sites/securitybkp.ngoinabox.org/files/u5/truecrypt-ar/28.png" alt="source:TrueCrypt/screenshots-ar/28.png" title="source:TrueCrypt/screenshots-ar/28.png">
</p>
<p>
ستغلق شاشة اختيار الملف و نعود إلى شاشة المرشد

</p>
<p>
<strong>خطوة 12</strong>. <strong>انقر</strong> <img src="/sites/securitybkp.ngoinabox.org/files/u5/truecrypt-ar/34.png" alt="source:TrueCrypt/screenshots-ar/34.png" title="source:TrueCrypt/screenshots-ar/34.png">
</p>
<p>
<strong>خطوة 13</strong>. <strong>أدخل</strong> كلمة سر المجلد في الحقل.
</p>
<p>
إن أدخلت كلمة السر الصحيحة فإن تروكربت سيظهر رسالة تخبرك أنه سيفحص المجلد العادي ليعرف المساحة الشاغرة فيه - إن وجدت - و يحسب حجم الأقصى الممكن للمجلد المخفي.

</p>
<p>
<strong>خطوة 14</strong>. <strong>انقر</strong> <img src="/sites/securitybkp.ngoinabox.org/files/u5/truecrypt-ar/33.png" alt="source:TrueCrypt/screenshots-ar/33.png" title="source:TrueCrypt/screenshots-ar/33.png">
</p>
<p>
الشاشة التالية تسرد ما تم في الخطوات السابقة و تعلمك بما سيجري في الخطوة اللاحقة.
</p>
<p>
<strong>خطوة 15</strong>. <strong>انقر</strong> <img src="/sites/securitybkp.ngoinabox.org/files/u5/truecrypt-ar/33.png" alt="source:TrueCrypt/screenshots-ar/33.png" title="source:TrueCrypt/screenshots-ar/33.png">

</p>
<p>
<img src="/sites/securitybkp.ngoinabox.org/files/u5/truecrypt-ar/25.png" alt="source:TrueCrypt/screenshots-ar/25.png" title="source:TrueCrypt/screenshots-ar/25.png">
</p>
<p>
<i>شكل 22: شاشة خيارات تعمية المجاد المخفي</i>
</p>
<p>
هذه الشاشة مطابقة للتي قابلتنا عندما أنشأنا المجلد العادي في <a href="truecrypt_standard#std">القسم 2.1: إنشاء مجلد عادي</a>
</p>
<p>
<strong>خطوة 16</strong>. <strong>اختر</strong> خوارزمية تعمية و خوارزمية تلبيد للمجلد المخفي.

</p>
<p>
<strong>تلميحة</strong>: اختر للمجلد المخفي خوارزمية تعمية تختلف عن التي اخترتها للمجلد الخارجي (العادي) الذي سينشأ داخله.
</p>
<p>
<strong>خطوة 17</strong>. <strong>انقر</strong> <img src="/sites/securitybkp.ngoinabox.org/files/u5/truecrypt-ar/33.png" alt="source:TrueCrypt/screenshots-ar/33.png" title="source:TrueCrypt/screenshots-ar/33.png">
</p>
<p>
<img src="/sites/securitybkp.ngoinabox.org/files/u5/truecrypt-ar/26.png" alt="source:TrueCrypt/screenshots-ar/26.png" title="source:TrueCrypt/screenshots-ar/26.png">
</p>
<p>
<i>شكل 23: شاشة حجم المجلد المخفي</i>

</p>
<p>
في هذه الخطة تحدد حجم المجلد المخفي.
</p>
<p>
<strong>هام</strong>: خذ في حسبانك أنواع و أحجام الملفات المتوقع تخزينها، و تذكر أن تترك بعض المساحة في المجلد الخارجي (العادي) شاغرة لأنك لو خصصت الحجم الأقصى للمجلد المخفي فلن يمكنك بعد إنشائه تخزين ملفات إضافية في المجلد الخارجي. لاحظ أنه إن كان حجم المجلد الخارجي 10 ميجابايتات و أنشأت داخله مجلدا مخفيا حجمه 5 ميجابايتات فسيكون لديك مجلدان كل منهما حجمه 5 ميجابايتات، و سيكون عليك عندها أن تتيقن عند إضافة ملفات إلى المجلد الحارجي من أن حجم محتوياته الإجمالي لن يزيد على خمسة الميجابايتات التي حسبناها. هذا حيوي لأن تروكربت ذاته لا يستطيع تحسس وجود ملف مخفي داخل الملف الخارجي (لا توجد طريقة عملية، تذكر؟)، لذا فمن الممكن أن يكتب فوق أجزاء منه و يعطبه مما قد يؤدي إلى ضياع كل محتوياته من ملفات.
</p>
<p>
<strong>خطوة 18</strong>. <strong>أدخل</strong> حجم الملف المخفي الذي تريده في الحقل. لأجل هذا المثال سندخل 5 م.بايت.
</p>
<p>
<strong>خطوة 19</strong>. <strong>انقر</strong> <img src="/sites/securitybkp.ngoinabox.org/files/u5/truecrypt-ar/33.png" alt="source:TrueCrypt/screenshots-ar/33.png" title="source:TrueCrypt/screenshots-ar/33.png">

</p>
<p>
الآن ينبغي أن تضع كلمة سر للملف المخفي. هنا كذلك تذكر أن تؤلف كلمة سر قوية و ارجع إلى <a class="wiki" href="/trac.cgi/wiki/Arabic/manual/KeePass">قسم كي‌باس</a> للمزيد عن مقومات كلمة السر القوية. إضافة إلى هذا فإن<strong>كلمة السر للمجلد المخفي يجب أن تكون مختلفة</strong> عن التي وضعتها للمجلد الخارجي، و إلا فلن تتمكن من وصل المجلد المخفي.
</p>
<p>
<strong>تلميحة</strong>: إن كنت تتوقع موقفا يمكن فيه أن تُرغم على الإفصاح عن كلمة سر تروكربت فضع للمجلد الخارجي كلمة سر يمكنك تذكرها و للمجلد المخفي كلمة سر معقدة و يمكن أن تستخدم كي‌باس لحفظها.
</p>
<p>
<strong>هام</strong>: تذَكَّر عندما تغيِّر كلمة سر المجلد المخفي أن تكون الكلمة الجديدة التي تضعها مختلفة عن كلمة سر المجلد الخارجي و إلا فلن تتمكن من وصل المجلد الخارجي مجددا و لن تتمكن من النفاذ إلى محتوياته بعد تغيير كلمة السر.

</p>
<p>
<strong>خطوة 20</strong>. <strong>أدخل</strong> كلمة السر ثم <strong>أكدها</strong>
</p>
<p>
<strong>خطوة 21</strong>. <strong>انقر</strong> <img src="/sites/securitybkp.ngoinabox.org/files/u5/truecrypt-ar/33.png" alt="source:TrueCrypt/screenshots-ar/33.png" title="source:TrueCrypt/screenshots-ar/33.png">
</p>

<p>
<img src="/sites/securitybkp.ngoinabox.org/files/u5/truecrypt-ar/27.png" alt="source:TrueCrypt/screenshots-ar/27.png" title="source:TrueCrypt/screenshots-ar/27.png">
</p>
<p>
<i>شكل 24: شاشة تهيئة المجلد المخفي</i>
</p>
<p>
اقبل الخيارات المبدئية لظام الملفات و العناقيد.
        
<strong>خطوة 22</strong>. <strong>حرك</strong> مؤشر الفأرة في حدود النافذة لمدة معقولة لتوليد قيم عشوائية.
</p>
<p>
<strong>خطوة 23</strong>. <strong>انقر</strong> <img src="/sites/securitybkp.ngoinabox.org/files/u5/truecrypt-ar/39.png" alt="source:TrueCrypt/screenshots-ar/39.png" title="source:TrueCrypt/screenshots-ar/39.png">

</p>
<p>
عندما تتم تهيئة المجلد المخفي فإن رسالة تنبيه ستظهر كالتالي:
</p>
<p>
<img src="/sites/securitybkp.ngoinabox.org/files/u5/truecrypt-ar/30.png" alt="source:TrueCrypt/screenshots-ar/30.png" title="source:TrueCrypt/screenshots-ar/30.png">
</p>
<p>
<i>شكل 25: رسالة تمام إنشاء مجلد مخفي</i>
</p>
<p>
هذه الرسالة تنبهك إلى خطورة احتمال تلف المجلد الداخلي في حال ما حفظت ملفات في المجلد الخارجي.
</p>
<p>
اصرف هذه الرسالة، ثم واصل.
</p>

<p>
<strong>خطوة 24</strong>. <strong>انقر</strong> <img src="/sites/securitybkp.ngoinabox.org/files/u5/truecrypt-ar/36.png" alt="source:TrueCrypt/screenshots-ar/36.png" title="source:TrueCrypt/screenshots-ar/36.png">
</p>
<p>
المجلد المخفي تم إنشاؤه داخل المجلد العادي، مما يمكنك من حفظ ملفات تظل مخبأة حتى عن من يحصل على كلمة سر المجلد الخارجي.
</p>
<h3>5.2 كيفية وصل مجلد مخفي</h3>
<p>
الآن و قد أنشأنا مجلدا مخفيا، فكيف لنا النفاذ إلى محتواه؟ الإجابة سهلة: بالطريقة ذاتها التي ننفذ بها إلى محتوى مجلد عادي. لكننا سندخل كلمة سر المجلد المخفي عوضا عن كلمة سر المجلد العادي، و هذه هي الطريقة الوحيدة التي يحدد تروكربت بها إن كان سيفتح المجلد المخفي أم العادي.
</p>

<p>
لوصل (فتح) المجلد المخفي، اتَّبع الخطوات التالية:
</p>
<p>
<img src="/sites/securitybkp.ngoinabox.org/files/u5/truecrypt-ar/29.png" alt="source:TrueCrypt/screenshots-ar/29.png" title="source:TrueCrypt/screenshots-ar/29.png">
</p>
<p>
<i>شكل 26: شاشة وصل مجلد مختار في تروكربت</i>
</p>
<p>
<strong>خطوة 1</strong>. <strong>اختر</strong> حرف سوّاقة، مثلا 'K'
</p>

<p>
<strong>خطوة 2</strong>. <strong>انقر</strong>: <img src="/sites/securitybkp.ngoinabox.org/files/u5/truecrypt-ar/35.png" alt="source:TrueCrypt/screenshots-ar/35.png" title="source:TrueCrypt/screenshots-ar/35.png">
</p>
<p>
<strong>خطوة 3</strong>. <strong>أوجد</strong> ثم  <strong>اختر</strong> الملف الذي يحوي مجلد تروكربت.
</p>

<p>
<strong>خطوة 4</strong>. <strong>انقر</strong>: <img src="/sites/securitybkp.ngoinabox.org/files/u5/truecrypt-ar/28.png" alt="source:TrueCrypt/screenshots-ar/28.png" title="source:TrueCrypt/screenshots-ar/28.png">
</p>
<p>
ستُغلق شاشة <i>اختر مجلد تروكربت</i> و نعود إلى شاشة تروكربت الرئيسية.
</p>
<p>
<strong>خطوة 5</strong>. <strong>انقر</strong>: <img src="/sites/securitybkp.ngoinabox.org/files/u5/truecrypt-ar/37.png" alt="source:TrueCrypt/screenshots-ar/37.png" title="source:TrueCrypt/screenshots-ar/37.png"> مظهرا شاشة <i>أدخل كلمة سرّ…</i> كالتالية:

</p>
<p>
<img src="/sites/securitybkp.ngoinabox.org/files/u5/truecrypt-ar/14.png" alt="source:TrueCrypt/screenshots-ar/14.png" title="source:TrueCrypt/screenshots-ar/14.png">
</p>
<p>
<i>شكل 27: شاشة إدخال كلمة سرّ</i>
</p>
<p>
<strong>خطوة 6</strong>. <strong>أدخل</strong> كلمة السر التي كنت وضعتها عند إنشاء المجلد المخفي.
</p>
<p>
<i>المجلد المخفي الآن موصول (مفتوح)</i>

</p>
<p>
سترى مدخلة كالتالية في شاشة تروكربت:
</p>
<p>
<img src="/sites/securitybkp.ngoinabox.org/files/u5/truecrypt-ar/31.png" alt="source:TrueCrypt/screenshots-ar/31.png" title="source:TrueCrypt/screenshots-ar/31.png">
</p>
<p>
<i>شكل 28: شاشة تروكربت الرئيسية يظهر فيها المجلد المخفي الموصول للتو</i>
</p>
<p>
تعرض تلك الشاشة المعلومات التالية:
</p>
<ul><li>الموضع - c:My DocumentsMy Volume
</li><li>الحجم - 5.0 ميجابايتات
</li><li>خوارزمية التعمية: - AES-TwoFish-Serpent

</li><li>نوع المجلد - مخفي
</li></ul><p>
للنفاذ إلى المجلد المخفي يمكنك إما أن <strong>تنقر مرتين</strong> على هذه المدخلة أو أن تفتحها بطريق نافذة <strong>الحاسوب</strong> بالنقر على حرف السواقة المخصص للمجلد (في مثالنا هذا هو K).
</p>
<h3>5.3 تلميحات عن كيفية استخدام القرص المخفي</h3>
<p>
الغرض من القرص المخفي هو الإفلات من موقف قد يكون خطرا <i>بالتظاهر</i> بالإفصاح للخصم عما يريد معرفته - النفاذ إلى ملفاتك - دون الكشف عنها فعليا، و الأهم، دون التعرض لسلامتك. لتحقيق هذا يجب عليك إيجاد ظرف يقنَع فيه الخصم بنتائج سعيه لانتزاع المعلومات، و بالتالي يدفعه لتركك و شأنك.

</p>
<p>
لتكون هذه الطريقة فعالة يمكنك اتباع الإرشادات التالية:
</p>
<ul><li>ضع في المجلد الخارجي بعض الوثائق قليلة الأهمية و التي لا يهمك الكشف عنها. يجب أن تبدو تلك الوثائق مقنعة بما يكفي للخصم عندما يجبرك عن الكشف عن وثائقك.
</li><li>حدِّث الملفات التي في المجلد الخارجي كل أسبوع أو أسبوعين بحيث تعطي الانطباع بأنك فعلا تستخدم تلك الملفات.
</li><li>لاحظ أن الخصم قد يكون على دراية بقدرة تروكربت على إنشاء مجلدات مخفية فهذا ليس سرا، لكنه بالرغم من ذلك لا يمكنه عمليا إثبات وجود مثل تلك المجلدات المخفية إذا أصررت على إنكار وجودها، و هو ما قد يدفعه لتركك. لكن إن كان هذا سيعرض سلامتك للخطر فربما عليك الامتناع عن استخدام تروكربت أو التعمية عموما.
</li></ul>


