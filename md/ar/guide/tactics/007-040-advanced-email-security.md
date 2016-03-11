

---

lang: ar
community: guide
type: tactics
legacy: True
child: True
weight: 4
depth: 3
title: Advanced Email Security

---

<p>الأدوات و&nbsp;المفاهيم المتناولة في هذا القسم موجهة للمستخدمين المتقدمين.</p>

<h2>تعمية البريد بالمفتاح العلني</h2>

<p>يمكن باستخدام تقنية <a href="/ar/glossary#encryption">التعمية</a> بالمفتاح العلني إيجاد قدر كبير من الحماية للمراسلات أيا كانت درجة السرية التي يتيحها مقدم الخدمة أثناء نقل الرسائل و&nbsp;تخزينها، و&nbsp;أيا كانت طبيعة قناة الاتصال. بتطبيق هذه التقنية يتحول نص كل رسالة - و&nbsp;مرفقاتها - إلى صيغة لا يمكن لغير المرسل إليه قراءتها، لأن النص المعمى لا يمكن تظهيره إلى النص الصريح مرة أخرى دون حيازة مفتاح. تكمن ميزة هذه التقنية عن تقنية التعمية التناظرية في انتفاء الحاجة إلى تبادل <strong>سر مشترك</strong> قبل إجراء الاتصال؛ أي لا توجد حاجة لتبادل مفاتيح سرية أو&nbsp;كلمات سر مسبقا، و&nbsp;بهذا تنتفي الحاجة إلى وجود قناة اتصال آمنة.</p>

<div class="backgroundscenario">
<p><span class="actorname">پابلو</span>: لكن كيف تعمل هذه الطريقة؟</p>

<p><span class="actorname">كلوديا</span>: بالرياضيات. فأنت تعمي الرسالة إلى المرسل إليها باستخدام <em>مفتاحها العلني</em> و&nbsp;هو كما يبدو من اسمه ليس مما ينبغي الحفاظ على سريته، بل يحبذ تداوله و&nbsp;نشره. و&nbsp;عندما تتلقى الرسالة فإنها تستخدم <em>مفتاحها السري</em> الذي لا يحوزه سواها لتظهير الرسالة. و&nbsp;بالمثل، فهي عندما تريد أن تراسلك فإنها تعمي الرسالة إليك باستخدام مفتاحك العلني الذي يمكنها أن تحصل عليه من أماكن عديدة أو&nbsp;أن ترسله أنت إليها دون أن تعبأ بأن يقع في يد غيركما.</p>
</div>

<p>يمكن استخدام هذه التقنية مع أي خدمة بريد، لأن الصيرورة تجري على نص الرسالة ذاتها قبل إرسالها و&nbsp;لا تتطلب شيئا من مقدم الخدمة. كما يمكن استخدام التقنية ذاتها لحماية أية بيانات رقمية أثناء تخزينها أو&nbsp;نقلها عبر أي وسيط.</p>

<p>استخدام تقنية <a href="/ar/glossary#encryption">التعمية</a> هذه قد تجلب الانتباه إلى من يستخدمها، فبينما يُنظر إلى تعمية قناة الاتصال التي تستخدم للاتصال الآمن بالمواقع ببروتوكول https و&nbsp;ما شابهه بقدر أقل من الحساسية، فإن التعمية بالمفتاح العلني قد تثير شكوكا. في بعض القضاءات التي يُجرَّمُ فيها استخدام التعمية فإن رسالة معماة تُلتقط أثناء إرسالها قد تتسبب في إدانة مرسلها حتى لو تعذر معرفة فحواها. ففي بعض الأحيان نضطر إلى الموازنة ما بين ضمان الخصوصية و&nbsp;البقاء دون مستوى الشبهات. يمكن باستخدام لأساليب الحفاظ على المجهولية أثناء التراسل عبر الإنترنت التقليل من هذا الخطر، كما يمكن بتقنيات <a href="/ar/glossary#steganography">الاستغانوغرافيا</a> إخفاء حقيقة استخدام التعمية.</p>

<h2>تعمية و&nbsp;استيثاق رسائل البريد</h2>

<p>التعمية بالمفتاح العلني تبدو معقدة للوهلة الأولى، إلا أنها تسهل بعد فهم الأساسيات، كما أن أدواتها ليست بالغة الصعوبة. و&nbsp;مع هذا فمن المهم فهم الإطار الذي تعمل فيه لتلافي الأخطاء التي تقلل كثيرا من فائدتها أو&nbsp;تمنح إحساسا زائفا بالأمان. توجد لعميل البريد <a href="/ar/thunderbird_main">ثَندَربِرد</a> ملحقة هي إنِجميل (Enigmail) يمكن استخدامها لتطبيق تقنية التعمية بالمفتاح العلني بنظام <abbr lang="en" title="Pretty Good Privacy">PGP</abbr>.</p>

<div class="HoG_link"><a href="/ar/thunderbird_main">دليل عملي لاستخدام ثندربرد</a></div>

<p>الاستيثاق من صحة و&nbsp;أصالة المراسلات البريدية عنصر هام للغاية عند التراسل عبر الإنترنت، إذ أن كل من لديه اتصال بإنترنت و&nbsp;دراية كافية بكيفية عملها يمكنه أن ينتحل شخصيتك أو&nbsp;يرسل إلى آخرين رسائل تبدو كأنها صادرة عنك و&nbsp;عليها عنوان بريدك الإلكتروني، كما يمكنه كذلك خداعهم ليردوا على مراسلاته ليتلقاها هو. كما يمكن لمن لديه سيطرة على جزء من مسار المراسلات التلاعب في فحواها و&nbsp;تغييره بحيث يخدم أغراضه هو، قبل أن يمرره في الاتجاهين إلى المتراسلين الغافلين عن هذا التلاعب؛ و&nbsp;يمكن لهذا النوع من الهجومات أن يحدث في الوقت الحقيقي، أي مثلا أثناء جلسة تراسل فوري، دون أن يبدو منه شيء لطرفي التراسل الأصليين.</p>

<p>و في هذا ما يدعو إلى القلق من التبعات الخطيرة على الغافلين عن هذا الانتحال، و&nbsp;على سَير الأعمال. خاصة أن المتراسلين عبر الإنترنت يفتقدون عوامل كانت في سياقات الاتصال التقليدية تساعد على التقليل من مخاطر الانتحال، مثل الصوت و&nbsp;الخط و&nbsp;أمارات الاستيثاق التقليدية الأخرى.</p>

<p>للتقليل من المخاطر السابق ذكرها تستخدم تقنية <a href="/ar/glossary#digital_signature">التوقيع الرقمي</a> و&nbsp;هي المبنية بدورها على التعمية بالمفتاح العلني. فبينما تحقق التعمية غرض <em>السرية</em>، فإن التوقيع الرقمي يحقق أغراض <em>الاستيثاق</em> و&nbsp;<em>الصحة</em>، إضافة إلى <em>الإلزام</em> في حال وجود صلة ما بين المفتاح و&nbsp;هوية صاحبه.</p>

<p><a href="/ar/thunderbird_main">قسم استخدام إنجميل مع ثندبرد</a> يتناول هذا.</p>

<div class="backgroundscenario">
<p><span class="actorname">پابلو</span>: لقد حدث من قبل و&nbsp;أخبرني معارف أنهم تلقوا مني رسائل أعلم أني لم أرسلها! و&nbsp;قد وجدنا وقتذاك أنه محض سُخام، إلا أنني الآن أتخيل مدى الضرر الذي كان يمكن أن يحدثه ذلك لو كانت الرسالة تحوي معلومات تتعلق بنا أو&nbsp;بعملنا. و&nbsp;قد سمعت أنه بالإمكان تفادي ذلك باستخدام التوقيع الرقمي، لكن ما هو و&nbsp;كيف يعمل؟</p>

<p><span class="actorname">كلوديا</span>: التوقيع الرقمي مثل التوقيع التقليدي بخط اليد و&nbsp;ختم الشمع، باستثناء أنه لا يمكن تزييفهما. فهو يفيد في التحقق من إذا ما كان المرسل هو حقا من يدعيه و&nbsp;إن كانت فحوى الرسالة قد جرى التلاعب بها من عدمه.</p>
</div>

