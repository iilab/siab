

---

lang: ar
community: guide
type: tactics
legacy: True
child: True
weight: 2
depth: 3
title: Hiding your sensitive information

---

<p>إحدى مساوئ وجود خِزانة في المكتب أو&nbsp;البيت هو أنها تكون بادية و&nbsp;قد تلفت انتباها غير مرغوب فيه. و&nbsp;بالمثل تكون لدى بعض الناس مخاوف معقولة من أن يدينوا أنفسهم قانونيا إذا ما استخدموا <a href="/ar/glossary#encryption">التعمية</a>، و&nbsp;مع أن المبررات المشروعة لاستخدام التعمية أكثر من الدوافع الإجرامية فإن هذا لا يقلل من خطر التجريم القانوني. يوجد سببان رئيسيان قد يدفعان لإعادة التفكير في استخدام التعمية و&nbsp;أدوات مثل <a href="/ar/TrueCrypt">تروكربت</a>؛ أولهما خطر الإدانة القانونية، و&nbsp;ثانيهما لفت الانتباه إلى موضع حفظ أكثر البيانات حساسية.</p>

<h2 id="legal_risk">خطر الإدانة القانونية</h2>

<p>استخدام التعمية مُجَرَّمٌ في بعض القضاءات، و&nbsp;هذا قد يعني أن مجرد تنزيل أو&nbsp;تنصيب أو&nbsp;استخدام برمجيات التعمية قد يكون جريمة في حد ذاته؛ و&nbsp;في حال كون الشرطة أو&nbsp;الجيش أو&nbsp;المخابرات أو&nbsp;الأجهزة الأمنية الأخرى من ضمن أولئك الذين تسعى لحماية البيانات منهم فإن مخالفة تلك القوانين قد يهيئ ذريعة للتحقيق في نشاط منظمتك أو&nbsp;مساءلتك قانونيا؛ و&nbsp;الواقع أن التهديدات من هذا النوع قد لا تكون لها علاقة بمدى قانونية استخدام التعمية على الإطلاق، إذ قد يكون مجرد ربط شخصك أو&nbsp;منظمتك باستخدام التعمية كافيا لتعريضك لاتهامات بالإجرام، بغض النظر عن طبيعة البيانات المُعمِّاة؛ و&nbsp;في هذه الحالة عليك التَّمَعُّن في مسألة استخدام مثل هذه الأدوات و&nbsp;ما إذا كانت مناسبة لحالتك. إن كان هذا هو الحال فقد تكون لديك بعض الخيارات البديلة التالية:</p>

<ul>
	<li>تفادي استخدام برمجيات تأمين البيانات تماما، و&nbsp;هو ما يعني أن تحفظ و&nbsp;حَسْبُ البيانات غير السِّرية أو&nbsp;أن تبتكر نظاما من الشفرات لتمويه البيانات السرية.</li>
	<li>استخدام تقنية <a href="/ar/glossary#steganography">الاستگانوغرافيا</a> لإخفاء البيانات السرية عوضا عن تعميتها، أو بعد تعميتها. توجد أدوات تطبق تقنيات عديدة لتحقيق هذا، و&nbsp;يتطلب استخدامها بعض الدراسة و&nbsp;الإعداد، كما يجب التكتم بقدر الإمكان على الأدوات و التقنيات التي تستخدمها، لأنه على غير التعمية التي يكون السر الوحيد فيها هو المفتاح أو&nbsp;كلمة السر فإن وسيلة الإخفاء ذاتها ينبغي الحفاظ على سريتها؛ و&nbsp;مع هذا يبقى احتمال الإدانة من قِبَل كل من يكتشف وسيلة لاستخراج البيانات المخفاة.</li>
	<li>حفظ البيانات الحساسة كمرفقات في حساب بريد إلكتروني على الوب مؤَمَّن، إلا أن هذا يتطلب اتصالا جيدا بالإنترنت و&nbsp;خبرة معقولة لإيجاد الخدمة و&nbsp;الأدوات المناسبة، كما يتطلب حرصا لعدم حفظ البيانات السرية على وسائط غير مؤمنة و&nbsp;تركها عليها.</li>
	<li>حفظ البيانات الحساسة بعيدا عن الحاسوب، مثلا على شذرات ذاكرة يو‌إس‌بي أو&nbsp;وسيط محمول آخر؛ إلا أن هذه الوسائط أكثر عرضة من الحواسيب للضياع و&nbsp;المصادرة، كما أن حمل بيانات حسّاسة و&nbsp;التجول بها قد يُشكِّل خطرا على حاملها، و&nbsp;هو ليس محبذا.</li>
</ul>

<p>عند اللزوم يمكن اتِّباع عدد من هذه الأساليب مع بعضها؛ و&nbsp;مع هذا ففي حالات خشية التجريم القانوني فقد يكون من الأنسب استخدام التعمية على أي حال مع السعي إلى تمويه وجود البيانات المُعمِّاة بقدر المستطاع.</p>

<p>مثلا يمكن إخفاء وجود <a href="/ar/glossary#volume">مجلدات</a> تروكربت المعماة بتسميتها بحيث تبدو كملفات من نوع آخر، فمثلا استخدام امتداد الاسم <span dir="ltr">.iso</span> لتنكيرها في هيئة ملف صورة قرص مدمج يناسب ملفات المجلدات التي يتراوح حجمها حول 700 ميجابيات، يمكن كذلك استخدام امتدادات ملفات صيغ الفيديو و&nbsp;الأوديو، مع ملاحظة أن هذه الملفات لن تعمل مع المشغلات أو&nbsp;التطبيقات المستخدمة أصلا لأي من الأنواع المذكورة. هذا يشبه إلى حد ما إخفاء الخِزانة خلف لوحة على الجدار، فهو لن يصمد في وجه الباحث المتمعن إلا أنه على الأقل لن يجلب انتباها زائدا.</p>

<p>يمكن كذلك تغيير اسم ملف برمجية تروكربت ذاته و&nbsp;المجلد الحاوي ملفاته و&nbsp;حفظها في غير الموضع الذي تنصب فيه عادة البرمجيات، و&nbsp;حفظها عوضا عن ذلك كملف عادي على شذرة ذاكرة و&nbsp;استخدامها منها بلا تنصيب. <a href="/ar/TrueCrypt">فصل تروكربت</a> يشرح كيفية عمل ذلك.</p>

<h2>خطر كشف وجود البيانات الحسّاسة</h2>

<p>عادة ما يكون قلقنا من احتمال أن <em>نُضبط متلبسين باستخدام برمجيات التعمية</em> أقل من قلقنا من أن وجود حاوية بيانات معماة يشير بجلاء إلى وجود البيانات الأكثر حساسية و&nbsp;التي نرغب في حمايتها بأكثر ما يمكن. و&nbsp;مع أنه لا يمكن لغير من يحوز المفتاح الاطلاع عليها إلا أن المهاجم، و&nbsp;قد صار يعرف بوجودها و&nbsp;أنك اتخذت إجراءات لحمايتها، قد يصبح أكثر إصرارا على استخراجها، مما قد يعرضك لتهديدات غير تقنية، مثل التهديد أو&nbsp;الابتزاز أو&nbsp;الاستجواب مع التعذيب، و&nbsp;هو احتمال وارد في البلاد التي يمكن أن تعمل فيها الجهات الأمنية خارج حدود القانون و&nbsp;بمخفى عن الرقابة، كما أنه أسهل و&nbsp;قد يكون أكثر جدوى من محاولة استخدام الأساليب التقنية لاكتشاف كلمات السر و&nbsp;كسر التعمية. هذا هو السياق الذي قد تفيد فيه <em>وظيفة دعم <a href="/ar/glossary#plausible_deniability">حُجِّيَّة الإنكار</a></em> في تروكربت.</p>

<p>وظيفة حجية الإنكار إحدى مميزات تروكربت، و&nbsp;هي توظف نوعا خاصا من الاستگانوغرافيا لتمويه وجود البيانات الحساسة المعماة خاف بيانات أخرى معماة أقل حساسية؛ و&nbsp;هو مماثل لوجود جيب سري في خزانة مقفولة بمفتاح، بحث إذا تمكن المهاجم من الحصول على المفتاح أو&nbsp;إجبارك على فتحها تحت التهديد فسيجد ما يمكن أن يظنه المواد المطلوبة و&nbsp;قد يدفعه هذا إلى الاكتفاء بما حصل عليه دون أن ينتبه إلى وجود ما يهمك إخفاؤه حقا في الجيب السري. و&nbsp;لأنك وحدك تعرف بوجود الجيب السري يمكنك أن تنكر وجود أي شيء آخر، لو سُئلت، و&nbsp;قد يقنع هذا المهاجم. قد يفيد هذا في الحالات التي تُجبر فيها على الإفصاح عن كلمة السر لسبب ما، خشية تهديد مادي أو&nbsp;قانوني، و&nbsp;حجية الإنكار تمنحك خيار مواصلة حماية البيانات شديدة الحساسية مع حماية نفسك أو&nbsp;غيرك من الخطر. لكن كما هو موضح في <a href="#legal_risk">قسم خطر الإدانة القانونية</a> فإن هذا الأسلوب قد يكون غير مجدٍ إذا ما كان لمجرد استخدام التعمية في حد ذاته عواقب وخيمة.</p>

<p>تعمل وظيفة دعم حجية الإنكار بطريق إنشاء مجلد مُعَمَّى مخفي داخل مجلد مُعمّى آخر، و&nbsp;يلزم لفتح المجلد المخفي و&nbsp;النفاذ إلى محتوياته معرفة كلمة سر تختلف عن المستخدمة لفتح المجلد الخارجي، لذا فإن تمَكَّن مهاجم من فتح المجلد الخارجي - بتعاونك، لأن كسر التعمية غير مجدٍ - فإنه حتى و&nbsp;إن كان ذا خبرة تقنية فلن يمكنه التيقن من وجود أو&nbsp;عدم وجود مجلد مخفي داخله، و&nbsp;لا إثبات ذلك ما دُمتَ تنكره، حتى مع أنه قد يعرف أن مثل هذه الوظيفة توجد في تروكربت، مما قد يدفعه إلى تركك لحالك، إلا أن هذا كما هو جليٌّ غير مؤكد و&nbsp;راجع إلى سلطة المهاجم الذي يملك إكراهك.</p>

<p>يستخدم عديدون تروكربت للتعمية دون استخدام وظيفة دعم حجية الإنكار، و&nbsp;المُجمَع عليه إلى الآن أنه لا يمكن حتى بطرق التحليل التقني تحديد وجود مجلد مخفي داخل أي مجلد تروكربت مُعمّى من عدمه؛ هذا إن اتبعت الطريقة السليمة و&nbsp;التوصيات لاستخدامه لتلافي ترك مؤشرات ثانوية قد تشير إلى وجوده أو&nbsp;استخدامه، مثل مدخلات في سجلات التطبيقات أو اختصارات على سطح المكتب أو قوائم آخر المستندات.</p>

<div class="backgroundscenario">
<p><span class="actorname">كلَوديا</span>: حسن، لنضع بعض الملفات غير الهامة في المجلد الخارجي و&nbsp;بعدها ننقل ملفات شهاداتنا الحسّاسة إلى المجلد المخفي في داخله. ألديك بعض الملفات القديمة أو&nbsp;ما شابه؟</p>

<p><span class="actorname">پابلو</span>: كنت أفكر في هذا أيضا..أقصد..أن الفكرة هي أن نفصح عن كلمة السِّر التمويهية إن لم يكن أمامنا خيار سوى ذلك، صحيح؟ لكن لكي تكون هذه الحيلة مقنعة ينبغي أن تبدو تلك الملفات هامة، أليس كذلك؟ و&nbsp;إلا فلِمَ تجشمنا عناء تعميتها! ربما وجب علينا أن نضع فيها مستندات مالية غير ذات علاقة بالموضوع، أو&nbsp;كلمات سر حسابات على مواقع حقيقة لكنها غير هامة، أو&nbsp;تقارير عن العمل لا يحوي بيانات سرية يمكن أن تهدد أحدًا.</p>
</div>

