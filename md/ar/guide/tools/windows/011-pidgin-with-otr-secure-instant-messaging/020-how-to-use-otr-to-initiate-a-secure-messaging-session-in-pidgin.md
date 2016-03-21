

---

lang: ar
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Use OTR to Initiate a Secure Messaging Session in Pidgin

---

<p>ينبغي على كلا الطرفين المتواصلين تثبيت وإعداد ملحقة OTR قبل أن يستطيعا إقامة جلسات دردشة سرية. يتعرف بدجن تلقائيا على وجود وإعداد الملحقة عند كلا الطرفين. إذا طلبت محادثة خاصة مع صديق لم يُثبّت OTR بعد، ستُرسل له رسالة توضح كيفية الحصول على الملحقة.</p>

<h3 id="a3.1كيفتفعلملحقةOTR">3.1 كيف تُفعّل ملحقة OTR</h3>

<p>تفعيل ملحقة OTR في بدجن هو أول خطوة إقامة جلسات تراسل خاصة مؤمنة. لتفعّل ملحقة OTR، عليك اتباع الخطوات التالية.</p>

<p><strong>خطوة 1.</strong> اختر <span class="underline">الأدوات</span> &gt; <span class="underline">الملحقات</span> من نافذة قائمة الأصدقاء في بدجن كما يلي:</p>

<p><img alt="Pidgin/screenshots-ar/19.png" src="/sites/securitybkp.ngoinabox.org/files/u5/pidgin-ar/19.png" title="Pidgin/screenshots-ar/19.png" /></p>

<p><i>شكل 16: قائمة <strong>الأدوات</strong> باختيار <strong>الملحقات</strong></i></p>

<p>سيفتح هذا شاشة الملحقات كما في الشكل أدناه.</p>

<p><strong>خطوة 2.</strong> انزل لأسفل حتى تصل إلى <i>خيار التراسل الخاص</i> و أشّر أمامها لتفعلها.</p>

<p><img alt="Pidgin/screenshots-ar/20.png" src="/sites/securitybkp.ngoinabox.org/files/u5/pidgin-ar/20.png" title="Pidgin/screenshots-ar/20.png" /></p>

<p><i>شكل 17: نافذة ملحقات بدجن باختيار ملحقة OTR</i></p>

<p><strong>اضغط</strong> <img alt="Pidgin/screenshots-ar/21.png" src="/sites/securitybkp.ngoinabox.org/files/u5/pidgin-ar/21.png" title="Pidgin/screenshots-ar/21.png" /> لتبدأ شاشة إعداد التراسل الخاص.</p>

<h3 id="a3.2توليدمفتاحللتعمية">3.2 توليد مفتاح للتعمية</h3>

<p>تتم الدردشة المؤمّنة في بدجن عبر توليد 'مفتاح سري' للحساب المستخدم. نافذة إعداد التراسل الخاص مقسمة إلى لساني 'الضبط' و 'البصمات المعروفة'. يستخدم لسان 'الضبط' لتوليد 'مفتاح' لكل حساب من حساباتك و لضبط خيارات OTR الخاصة. يحتوي لسان 'البصمات المعروفة' على مفاتيح أصدقائك. يجب أن تحوز مفتاحا علنيا لكل صديق تريد الدردشة معه بخصوصية.</p>

<p><img alt="Pidgin/screenshots-ar/22.png" src="/sites/securitybkp.ngoinabox.org/files/u5/pidgin-ar/22.png" title="Pidgin/screenshots-ar/22.png" /></p>

<p><i>شكل 18: نافذة <strong>Off-the-record</strong> يظهر فيها لسان <strong>اضبط</strong></i></p>

<p><strong>خطوة 1.</strong> لتحسين خصوصيتك، انقر على خيارات 'فعّل التراسل الخاص'، و 'ابدأ التراسل الخاص تلقائيا' و 'لا تُسجّل محادثات OTR' في لسان 'الضبط' كما هو موضح أعلاه.</p>

<p><strong>خطوة 2.</strong> <strong>انقر:</strong> <img alt="Pidgin/screenshots-ar/23.png" src="/sites/securitybkp.ngoinabox.org/files/u5/pidgin-ar/23.png" title="Pidgin/screenshots-ar/23.png" /> لتبدأ توليد مفتاحك. بعد قليل ستظهر شاشة تعلمك بتمام توليد مفتاحك كما يلي:</p>

<p><img alt="Pidgin/screenshots-ar/24.png" src="/sites/securitybkp.ngoinabox.org/files/u5/pidgin-ar/24.png" title="Pidgin/screenshots-ar/24.png" /></p>

<p><i>شكل 19: نافذة توليد مفتاح سري</i></p>

<p>سيكون على صديقك اتباع ذات الخطوات على حاسوبه.</p>

<p><strong>هام:</strong> لقد أنشأت الآن مفتاحا سريا لحسابك، سيُستخدم هذا لتعمية محادثاتك حتى لا يستطيع أي شخص آخر قراءتها، حتى لو استطاعوا التنصت على محادثاتك مع أصدقائك. البصمة هي تتابع طويل من الأرقام والحروف يُستخدم لتعريف مفتاح حساب معيّن. يُشبه ما يلي:</p>

<p><i>البصمة: 55A3638C 5DCF5BB8 0C7A2815 70DA5122 06507354</i></p>

<p>يحفظ ويتحقق بدجن آليا من بصمة مفتاحك و بصمات مفاتيح أصدقائك، لذا لن تحتاج لتذكرها.</p>

<h3 id="a3.3استيثاقمحادثةخاصة">3.3 استيثاق محادثة خاصة</h3>

<p>هناك ثلاث خطوات قصيرة لتوكيد سرية وخصوصية محادثتك. الخطوة <strong>الأولى</strong> -التي قمنا بها للتو- تتضمن توليد مفتاح لحسابك. الخطوة <strong>الثانية</strong> أن تطلب أنت وصديقك محادثة مُؤمنة. الخطوة <strong>الثالثة</strong> هي التحقق من أن صديقك هو بالفعل من تظنه. عملية التأكد من هويّة شخص آخر تعرف بالاستيثاق.</p>

<h4 id="a3.3.1الخطوةالثانية">3.3.1 الخطوة الثانية</h4>

<p><strong>خطوة 1.</strong> ابدأ محادثة فورية مع صديقك، المتصل حاليا، بالنقر مرتين على حسابه. ستُلاحظ (إذا كان لدى كل منكما ملحقة OTR مثبّتة ومضبوطة) ظهور أيقونة 'OTR' أسفل شاشة الدردشة.</p>

<p><img alt="Pidgin/screenshots-ar/12.png" src="/sites/securitybkp.ngoinabox.org/files/u5/pidgin-ar/12.png" title="Pidgin/screenshots-ar/12.png" /></p>

<p><i>شكل 20: نافذة دردشة تظهر فيها أيقونة OTR</i></p>

<p><strong>خطوة 2.</strong> <strong>انقر:</strong> على <img alt="Pidgin/screenshots-ar/26.png" src="/sites/securitybkp.ngoinabox.org/files/u5/pidgin-ar/26.png" title="Pidgin/screenshots-ar/26.png" /></p>

<p>ستقول نافذة الدردشة:</p>

<p><strong>تجري محاولة بدء محادثة خاصة مع user@example...</strong></p>

<p><strong>لم يُستوثق من user@example بعد. يجب عليك الاستيثاق من هذا الصديق.</strong></p>

<p><strong>بدأت محادثة غير مستوثقة مع user@example.</strong></p>

<p>وسيتغير زر OTR ليبدو مثل <img alt="Pidgin/screenshots-ar/33.png" src="/sites/securitybkp.ngoinabox.org/files/u5/pidgin-ar/33.png" title="Pidgin/screenshots-ar/33.png" /></p>

<p>يعني هذا أن محادثتك مع صديقك الآن معمّاة. لكن هذه المحادثة غير مستوثقة. قد يكون صديقك في الحقيقة شخصا آخر جالسا خلف ذاك الحاسوب، أو شخصا ينتحل شخصية صديقك. هنا ستحتاج إلى مشاركة كلمة سر (متنفق عليه مسبقا) للاستيثاق من بعضكم البعض.</p>

<h4 id="a3.3.2الخطوةالثالثة">3.3.2 الخطوة الثالثة</h4>

<p>للاستيثاق من صديقك في بدجن يجب أن يعرف كليكما (ويكتب) نفس الكلمة السرية. يمكنكما الاتفاق على هذه الكلمة السرية مسبقا، إما أثناء مقابلة وجها لوجه أو باستخدام وسيلة اتصال أخرى (كالهاتف، أو الدردشة الصوتية عبر skype، أو رسالة نصية بالهاتف المحمول). بمجرد أن يكتب كلاكما نفس كلمة السر، ستستوثق الجلسة.</p>

<p><strong>خطوة 1.</strong> في نافذة الرسائل، انقر يمينا على زر OTR واختر 'استوثق من الصديق'</p>

<p><img alt="Pidgin/screenshots-ar/25.png" src="/sites/securitybkp.ngoinabox.org/files/u5/pidgin-ar/25.png" title="Pidgin/screenshots-ar/25.png" /></p>

<p><i>شكل 21: قائمة أوامر OTR باختيار أمر <strong>استوثق من الصديق</strong></i></p>

<p>ستنبثق رسالة تسألك إدخال كلمة السر</p>

<p><img alt="Pidgin/screenshots-ar/28.png" src="/sites/securitybkp.ngoinabox.org/files/u5/pidgin-ar/28.png" title="Pidgin/screenshots-ar/28.png" /></p>

<p><i>شكل 22: نافذة <strong>استوثق من الصديق</strong></i></p>

<p><strong>خطوة 2.</strong> اكتب كلمة السر (حساسة لحالة الحروف اللاتينية الكبيرة و الصغيرة) ثم <strong>اضغط</strong> موافق</p>

<p>سيرى صديقك ذات النافذة على ناحيته وسيكون عليه إدخال نفس كلمة السر. إذا تطابقتا، ستستوثق الجلسة.</p>

<p>بمجرد استيثاق الجلسة سيتغير زر 'OTR' ليبدو هكذا <img alt="Pidgin/screenshots-ar/27.png" src="/sites/securitybkp.ngoinabox.org/files/u5/pidgin-ar/27.png" title="Pidgin/screenshots-ar/27.png" />. جلستك الآن مؤمنة ويمكنك أن تطمأن إلى أنك تُحادث صديقك سرا و لا أحد غيره.</p>

<p>تهانينا، يمكنك الدردشة بخصوصية الآن. في المرة التالية التي تدردش فيها مع صديقك (مستخدمين ذات الحاسوبين)، يُمكنكما تخطي الخطوتين الأولى والثالثة. عليك فقط طلب محادثة مؤمنة وعلى صديقك أن يقبلها.</p>

<p>لاحظ أنه بالعودة إلى قائمة <span class="underline">الأصدقاء</span> &gt; <span class="underline">الأدوات</span> &gt; <span class="underline">الملحقات</span> &gt; <span class="underline">التراسل الخاص</span> &gt; <span class="underline">اضبط الملحقة</span> فإن لسان 'البصمات المعروفة' يحتوي الآن على حساب صديقك وملاحظة بأن الهوية مستوثقة.</p>

<p><img alt="Pidgin/screenshots-ar/32.png" src="/sites/securitybkp.ngoinabox.org/files/u5/pidgin-ar/32.png" title="Pidgin/screenshots-ar/32.png" /></p>

<p><i>شكل 23: نافذة <strong>التراسل الخاص</strong> يظهر فيها لسان <strong>البصمات المعروفة</strong></i></p>


