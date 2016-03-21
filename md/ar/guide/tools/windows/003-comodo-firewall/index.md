

---

lang: ar
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 003
title: Comodo Firewall

---

**الموقع**:

[**www.personalfirewall.comodo.com**](http://www.personalfirewall.comodo.com)

**متطلبات الحاسوب**:

- وندوز 2000/XP/2003/فستا
- صلاحيات المدير من متطلبات التنصيب

**الإصدارة المشروحة في هذا الدليل**:

- 5.0.16

**الرخصة**:

- [برمجية مجانية](https://securityinabox.org/ar/glossary#freeware)

**مطالعات مطلوبة**:

- فصل [**حماية الحاسوب من البرمجيات الخبيثة و من المخترقين**](https://securityinabox.org/ar/chapter_01) في **دليل الممارسات**.

**المستوى**: 1: مبتدئ، 2: عادي، **3: متوسط، 4: خبير**، 5: متقدم

**الوقت المطلوب للبدء في استخدام هذه الأداة**: 60 دقيقة

**ما ستحصل عليه**:

- زيادة حصانة الحاسوب و الشبكة المحلية في مواجهة [المخترقين](https://securityinabox.org/ar/glossary#hacker) و[البرمجيات الخبيثة](https://securityinabox.org/ar/glossary#malware) وتهديدات أخرى.
- إمكانية التحكم في كل تدفقات البيانات التي تسعى البرمجيات على الحاسوب لإخراجها عبر الإنترنت، عبر واجهة برمجية سهلة الإعداد.


**برمجيات أخرى متوافقة مع جنو\لينكس، و ماك أو إس و وندوز**:

يأتي مع **جنو/لينكس** جدار ناري ملحق اسمه ([**netfilter/iptables**](http://www.netfilter.org/)) بالإضافة إلى ضبط ممتاز للشبكة. توجد عدة واجهات مستخدمة سهلة لضيط الجدار الناري،ونحن ننصح ببرنامج [**GUFW**](https://help.ubuntu.com/community/Gufw) (**الجدار الناري الرسومي غير المعقد**). ([**للمزيد**](http://blog.bodhizazen.net/linux/firewall-ubuntu-gufw/)).

**ماك أو إس** به جدار ناري داخلي قوي ويمكن إضافة عدة ملحقات للواجهة لتحسين إمكانياته، ومنها: [**NoobProof**](http://www.hanynet.com/noobproof/) و[**IPSecuritas**](http://www.lobotomo.com/products/IPSecuritas/). ولأصحاب الميزانية المحدودة ننصح ببرنامج [**Little Snitch**](http://www.obdev.at/products/littlesnitch/index.html) لتقوي خصوصيتك على الإنترنت وتزيد من الأمان وحماية معلوماتك الشخصية.

يوجد الكثير من البدال لجدار **كومودو** الناري لنظام **ميكروسوفت وندوز**. قد يكون [**ZoneAlarm Free Firewall**](http://www.zonealarm.com/security/en-us/zonealarm-pc-security-free-firewall.htm) أو [**Outpost Firewall Free**](http://free.agnitum.com/) بديلان لهما الفعالية ذاتها.


**1.1 ما ينبغي معرفته قبل البدء**

[الجدار الناري](https://securityinabox.org/ar/glossary#firewall) أشبه ببواب أو حارس للحاسوب المتصل بالإنترنت، إذ لديه قواعد
تحدد ما تدفقات البيانات المسموح بخروجها من الحاسوب و خروجها إليه و ما لا يُسمح
بخروجه. يتلقى الجدار الناري المعلومات القادمة من الإنترنت قبل أي برمجية أخرى و
يفحصها، و كذلك يكون آخر ما تمر عليه المعلومات الخارجة بعد البرمجيات الأخرى
وقبل خروجها إلى الإنترنت مباشرة. لذا فهو يستخدم لمنع المخترقين من التسلل إلى
النظام بالاتصال بالحاسوب، و كذلك لمنع [البرمجيات الخبيثة](https://securityinabox.org/ar/glossary#malware) المنزرعة في
النظام من تسريب بيانات إلى الإنترنت دون إذن.

**جدار النار كومودو** برمجية جدار ناري معروفة وموثوقة، كما أنه [برمجية
مجانية](https://securityinabox.org/ar/glossary#freeware) مما يعني إمكانية استخدامه دون شراء رخصة استخدام. قد يستغرق استخدام
جدار النار بعض الوقت حتى تطوع إعداداته و تتناسب مع استخدامك للحاسوب، يعدها
يعمل جدار النار بسلاسة بلا تدخل يذكر.

**تحذير**: لا تتصل أبدًا بالإنترنت دون جدار ناري، حتى لو كانت [نبيطة](https://securityinabox.org/ar/glossary#device) الاتصال،
أو [المودم](https://securityinabox.org/ar/glossary#modem)، أو [المسيّر](https://securityinabox.org/ar/glossary#router)، تضم جدارًا ناريًا داخلها. ننصح بشدة أن تثبت جدارًا
ناريًا على الحاسوب.

