

---

lang: ar
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 008
title: Eraser - Secure File Removal

---

**الموقع**:

[www.heidi.ie/eraser](http://www.heidi.ie/eraser)

**متطلبات الحاسوب**:

- كل إصدارات وندوز

**الإصدارة المستخدمة في هذا الدليل**:

- 5.86a <br>

**ملاحظة**: قد تجد نسخًا أحدث في موقع البرنامج، ولكنها لم تُضف إلى هذا الدليل لأنها تتطلب تنصيب برنامج **.Net** على نظام التشغيل **وندوز** وهذا قد يستغرق وقتًا طويلًا لدى أصحاب الاتصالات منخفضة السرعة

**الرخصة**:

- برمجية حرة مفتوحة المصدر

**مطالعات مطلوبة**:

- فصل [**تدمير البيانات الحسَّاسة**](/ar/chapter_06) في **دليل الممارسات**



**المستوى**:
- مبتدئ، **- عادي**، - متوسط، - خبير، - متقدم

**الوقت المطلوب للبدء في استخدام هذه الأداة**: 20 دقيقة

**ما الذي ستسحصل عليه**:

- القدرة على [محو](/ar/glossary#delete_vs_wipe) الملفات غير المرغوبة من الحاسوب
- إمكانية محو بيانات الملفات المحذوفة القابلة للاسترجاع

**لينكس GNU, ماك OS و غيرها من برامج ميكروسوفت ويندوز المتوافقة:**

في **جنو\لينكس** توجد حزمة **secure-delete** التي يمكن [استخدامها من الطرفية](http://www.ghacks.net/2010/08/26/securely-delete-files-with-secure-delete/) لمحو الملفات والمجلدات بأمان، ول[مسح](/ar/glossary#delete_vs_wipe) المساحات الفارغة في قرصك الصلب. يمكن أن يستخدم هذا البرنامج كذلك [مدمجًا مع مدير ملفات رسومي](http://techthrob.com/2010/07/07/adding-a-secure-delete-option-to-nautilus-file-manager-in-linux/).

في نظام **ماك أو إس** يمكنك استخدام زر **Secure Empty Trash...** من قائمة **فايندر** لحذف الملفات والمجلدات نهائيًا. كما يمكنك أن تستخدم أداة **Disk Utility** لمحو قرص كامل أو مساحة فارغة في قرص داخلي أو خارجي.

في **ميكروسوفت وندوز** يمكنك استخدام [**سيكلينر**](/ar/ccleaner) لحذف الملفات والمجلدات من **سلة المهملات** نهائيًا بدلًا من استخدام **إريسر** المشروح في هذا الفصل. يمكن أن يمحو **سيكلينر** كذلك المساحات الفارغة في القرص الصلب. كما ننصح بأداة أخرى لحذف الملفات وهي [**فريريسر**](http://www.freeraser.com/).

كما نود أن ننصح بهذه الأداة متعددة المنصات: [DBAN - Darik's Boot And Nuke](http://www.dban.org/). إنها حزمة تُحرق على قرص سي‌دي ثم تقلع منها حاسوبك. تتيح لك الحزمة محو محتويات أي قرص صلب تكتشفه، مما يجعلها الحل الأمثل لتدمير البيانات الجماعي أو الطارئ.

**1.1 ما تنبغي معرفته قبل البدء**

يُستخدم **إريسر** لمحو  البيانات الحساسة من الحاسوب نهائيًا بحيث لا يمكن استعادتها، وهو يفعل هذا بطمس البيانات التي تريد حذفها عن طريق كتابة بيانات فوقها. يمكنك انتقاء الملفات أو المجلدات التي تود محوها بهذه الطريقة. يمكن باستخدام **إريسر** كذلك محو بيانات قد لا تكون حتى مدركًا وجودها على الحاسوب، مثل ملفات كنت قد حذفتها فيما سبق مستخدمًا حذف **وندوز** العادي، أو نسخًا مؤقتة من مستندات كنت تعمل عليها في الماضي.

- محو الملفات باستخدام **إريسر** يمكن أن يتم حسب الطلب أو أن يُجَدول ليشتغل في أوقات محددة
- إذا جدولت **إريسر** ليشتغل في وقت محدد فإن الحاسوب لابد أن يكون عاملًا في الوقت المعين وإلا لن يجري المحو
- بعد محو ملف ما باستخدام **إريسر** فإنه لن يمكن استرجاعه بأدوات استرجاع الملفات المحذوفة
- لزيادة الأمان، يجب أن تضبط **إريسر** ليطمس الملفات بين 3 و7 مرات.
- يمكن أن يستخدم **إريسر** لمحو المساحة الشاغرة من الحاسوب. أي محو كل آثار عمل الماضي والتي لم تكن قد محيت كما ينبغي ويمكن استعادتها.

