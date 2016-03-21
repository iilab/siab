

---

lang: fa
community: guide
type: tactics
legacy: True
child: True
weight: 2
depth: 3
title: Wiping information with secure deletion tools

---

اگر از ابزارهای پاکسازی امن، که در این فصل راجع به آن‌ها صحبت و توصیه شده است، برای حذف اطلاعات استفاده شود، آنگاه می‌توان با اطمینان خاطر بیشتری ادعا کرد که اطلاعات مزبور فقط پاک نشده اند، بلکه فضای اشغال شده توسط آن‌ها با فایل‌های جدیدتری جایگزین یا به عبارتی بر روی آن فضا بازنویسی شده است. به عنوان مثال اگر فرض کنید که اسناد موجود در آن کابینت بایگانی همگی با مداد نوشته شده باشند، نرم افزارهای پاکسازی امن نه تنها محتویات آن‌ها را پاک می کنند، بلکه بر روی هر یک از کلمات موجود در متن آن اسناد، کلمات دیگری را بصورت ناخوانا می‌نویسند و دوباره پاک می‌کنند تا باقی مانده جای مداد اول قابل خواندن نباشد. همانند بقایای به جای مانده از نگارش مدادی، اطلاعات دیجیتال نیز حتی پس از آنکه پاک شده و مطلبی دیگر بر روی آن‌ها بازنویسی شده باشد، هنوز و البته به صورت ضعیف قابل خوانده شدن هستند. به همین دلیل نرم افزارهایی که در اینجا به شما توصیه می‌شوند عمل بازنویسی را بصورت تصادفی و در دفعات متعدد بر روی اطلاعات پاک شده انجام می دهند. این فرآیند را [*پاکسازی کامل*](glossary#Wiping) می گویند. هرچه تعداد دفعات بازنویسی بر روی اطلاعات پاک شده بیشتر باشد بازیابی محتویات اصلی فایل دشوارتر خواهد بود. متخصصین فن در این زمینه معتقدند که عمل بازنویسی بایستی به تعداد سه بار یا بیشتر تکرار شود. البته برخی دیگر نیز بر تعداد هفت دفعه یا بیشتر تأکید دارند. نرم‌افزار [*پاکسازی کامل*](glossary#Wiping) بصورت خودکار چندین بار بر روی اطلاعات پاک شده بازنویسی می‌کند که تعداد آن را می‌توانید با تغییر تنظیمات برنامه به طور دلخواه تغییر دهید. 


### پاکسازی کامل فایل‌ها ###
 
دو روش متداول برای [*پاکسازی کامل*](glossary#Wiping) اطلاعات محرمانه شما از روی سخت دیسک یا وسایل ذخیره ساز رایانه ای وجود دارد. در روش اول ، یک فایل خاص و در روش دوم، فضای تخصیص نیافته یا به عبارتی فضای خالی روی دیسک یا وسیل ذخیره ساز، [*پاکسازی کامل*](glossary#Wiping) می شود. در هنگام انتخاب یک از این روش‌ها یا بکارگیری هر دوی آن‌ها بد نیست که مثال فرضی مربوط به نگارش آن گزارش طولانی را بخاطر بیاورید. اگر بیاد داشته باشید، گفته شد که در هنگام تهیه چنین اسنادی، نسخه های ناقصی از فایل اصلی در قسمت‌های مختلف فضای سخت دیسک رایانه پراکنده می‌شود (نسخه هایی که توسط سیستم عامل و بدون اطلاع شما بوجود می آیند) اما شما به عنوان کاربر فقط یک نام یک فایل(فایل اصلی) را در فهرست فایل‌های خود مشاهده می کنید. اگر فقط آن فایل را پاکسازی کامل کنید، آن نسخ بطور صد در صد از روی رایانه شما پاک می‌شود اما نسخه های ناقصی که پیشتر از آن‌ها صحبت شد همچنان درجای خود باقی خواهند ماند. در‌واقع به هیچ عنوان نمی‌توان آن نسخه ها را هدف قرار داد چرا که جز با در اختیار داشتن نرم افزارهای مخصوص قادر به مشاهده آن‌ها نخواهید بود. اما در صورت انجام [*پاکسازی کامل*](glossary#Wiping) «فضای تخصیص نیافته» یا در‌واقع فضای خالی موجود بر روی دیسک، حذف کامل تمامی اطلاعاتی که از قبل پاک شده‌اند تضمین می شود. اگر دوباره مثال کابینت بایگانی را یادآوری کنیم، پاکسازی فضای تخصیص نیافته بدان می‌ماند که در سرتاسر کابینت به جستجو پرداخته و محتوای پرونده هایی را که یرچسب آن‌ها برداشته شده است پاک نموده و بارها بر روی آن‌ها مطالب نامفهوم و ناخوانا نوشت. 

نرم‌افزار [*Eraser*](glossary#Eraser) که یک ابزار پاکساری امن می‌باشد جزو نرم افزارهای رایگان، آزاد و متن باز بوده که نحوه کار با آن نیز بسیار ساده است. با استفاده از [*Eraser*](glossary#Eraser) می‌توان به سه روش مختلف نسبت به پاکسازی کامل اطلاعات اقدام نمود: از طریق انتخاب یک فایل خاص، انتخاب محتویات **Recycle Bin**، یا [*پاکسازی کامل*](glossary#Wiping) تمامی فضاهای خالی موجود بر روی وسیله ذخیره ساز. با کمک Eraser همچنین می‌توان محتویات [*فایل تبادلی*](glossary#Swap_file) (Swap File) ویندوز را نیز پاکسازی نمود. در بخش بعدی بطور مفصل در این رابطه بحث خواهد شد.



<div class="getstarted" markdown="1">
Hands-on: Get started with the [*Eraser Guide*](eraser_main)
</div>


اگرچه ابزارهای [*پاکسازی کامل*](glossary#Wiping) به فایلهایی جز آنچه که قصد و نظر شماست، آسیب نمی رسانند، اما رعایت احتیاط لازم در هنگام کار با چنین نرم افزارهایی، ضروررت دارد. اتفاقات ناخواسته گاهی اوقات پیش می آیند، و شاید به همین خاطر است که بسیاری از کاربران وجود **Recycle Bin** و نرم افزارهای بازیابی فایل را مفید می دانند. اگر برحسب عادت، در هر بار که اطلاعات غیر دلخواه خود را حذف می‌کنید، عمل [*پاکسازی کامل*](glossary#Wiping) را نیز بر روی آن‌ها انجام دهید، آنگاه اگر بخشی از اطلاعاتتان را به اشتباه پاک کرده باشید، دیگر هیچ راهی برای بازیابی آن‌ها وجود نخواهد داشت. بنابراین همواره پیش از [*پاکسازی کامل*](glossary#Wiping) حجم بزرگی از اطلاعات، اطمینان یابید که نسخه پشتیبان آن را در محلی امن نگهداری می کنید. 


<div class="background" markdown="1">
الینا: من میدانم که برنامه‌های کلمه پردازی چون مایکروسافت ورد و اوپن آفیس در هنگامی که کاربر دارد بر روی یک فایل کار میکند، گاهی اوقات نسخه های کپی موقتی از آن فایل تهیه می کنند. آیا برنامه‌های دیگر نیز چنین کاری می کنند، یا شاید فقط باید نگران فایل‌هایی باشم که خودم بوجود آورده و پاک می کنم؟

نیکولای: در واقع، جاهای متعددی در رایانه وجود دارد که برنامه‌های مختلف رد پاهایی از اطلاعات شخصی و فعالیتهای آنلاین کاربران در آنجا باقی می گذارند. منظور من وبسایتهایی است که به دیدن آن‌ها رفته اید، پیشنویس های ایمیل و چیزهای دیگری از این قبیل می باشد. این اطلاعات بسته به اینکه چقدر از یک رایانه خاص استفاده می‌کنید می‌توانند بسیار حساس باشند.
</div>


### پاکسازی کامل اطلاعات موقت ###

شیوه ای که نرم‌افزار [*Eraser*](glossary#Eraser) با کمک آن عمل [*پاکسازی کامل*](glossary#Wiping) فضای خای موجود بر روی سخت دیسک یا سایر وسایل ذخیره ساز را انجام می دهد، آنقدرها که تصور می‌شود زیانبار نیست. بطور کلی نرم‌افزار [*Eraser*](glossary#Eraser) در طی عملیات پاکسازی به فایلهای عادی و قابل مشاهده آسیب نمی رساند. بعبارت دیگر این واقعیت نشانگر آنست که این ابزار به اطلاعاتی که هنوز پاک نشده‌اند کاری ندارد، بلکه وظیف آن پاکسازی کامل داده‌هایی است که از چشم شما کاملاً پوشیده اند. فایل‌هایی که چنین شرایطی دارند ممکن است مثلاً در شاخه ها و زیرشاخه های گمنام مخفی بوده و یا تحت نام های بی‌معنی ذخیره شده باشند. این امر در مورد اسناد الکترونیک چندان دردسرساز نیست اما در مورد داده‌هایی که با هر بار استفاده از رایانه صورت خودکار ایجاد شده و در جایی بر روی سخت دیسک ذخیره می شوند، نقش بسیار مهمی ایفا می کند. از جمله این اطلاعات می‌توان به موارد زیر اشاره کرد:

- داده‌های موقتی که در زمان مرور صفحات وب، توسط مرورگر شما ذخیره می شوند. اینگونه داده‌ها شامل متون، تصاویر، کوکی ها، اطلاعات اکانت ها، اطلاعاتی که در هنگام پر کردن فرم‌های آنلاین وارد کرده اید، و تاریخ نگار وبسایت های مشاهده شده، می باشند. 
- فایلهای موقتی که توسط برنامه‌های کاربردی مختلف در رایانه شما یا تجهیزات ذخیره ساز نگهداری می شوند. معمولاًاینگونه فایل‌های موقتی به این علت ایجاد می‌شوند که کار در هنگام کار بابر روی یک فایل، رایانه دچار اشکال شود و شما فرصت ذخره فایل را نداشته باشید، امکان بازیابی فایل وجود داشته باشد. فایلهای موقتی ممکن است شامل فایلهای متنی، تصاویر،فایلهای صفحه گسترده، نام سایر فایل ها، و سایر اطلاعات بالقوه محرمانه باشد.
- فایل‌ها و لینک هایی که توسط ویندوز و صرفاً جهت سهولت انجام امور، ذخیره می شوند. از جمله این موارد می‌توان به میانبرهای برنامه‌های کاربردی، لینک های ارجاع به شاخه‌هایی که ترجیحاً بصورت مخفی نگهداری می شوند، و البته محتویات Recycle Bin در صورتی که تخلیه آن فراموش شده باشد، اشاره کرد.
- [*فایل تبادلی*](glossary#Swap_file) (Swap File) ویندوز. در مواقعی که به خاطر اجرای چندین برنامه به طور همزمان حافظه رایانه شما پر می‌شود (معمولاً در رایانه ای قدیمی تر) ویندوز در برخی اوقات داده‌هایی را که در حال استفاده از آن هستید در یک فایل منفرد بزرگ به نام [*فایل تبادلی*](glossary#Swap_file) (Swap File) ذخیره می کند. در نتیجه این فایل می‌تواند تقریباً حاوی هر چیزی از جمله صفحات وب، اسناد، رمزهای عبور، یا کلیدهای رمزنگاری باشد. [*فایل تبادلی*](glossary#Swap_file) (Swap File) حتی در صورت خاموش شدن رایانه از بین نمی رود، بنابراین می باید آن را شخصاً پاک نمایید.

یکی از ابزارهایی که برای پاک کردن فایلهای موقتی متداول موجود بر روی یارانه ها مورد استفاده قرار می گیرد، نرم‌افزار [*CCleaner*](glossary#CCleaner) است. [*CCleaner*](glossary#CCleaner) رایگان افزاری است که می‌توان از آن برای پاکسازی فایلهای موقتی ایجاد شده ناشی از استفاده از مرورگرهایی چون Internet Explorer و Mozilla [*Firefox*](glossary#Firefox) ، فایلهای موقتی که در اثر استفاده از برنامه‌های کاربردی مجموعه مایکروسافت آفیس (که ید طولایی در افشای اطلاعات محرمانه کار بران دارند) پدید می آیند، و همچنین فایلهای موقتی که توسط سیستم عامل ویندوز ایجاد می شوند، استفاده کرد. [*CCleaner*](glossary#CCleaner) می‌تواند این فایلها برای همیشه از روی رایانه شما محو نماید، و بدینترتیب نیاز به استفاده از برنامه‌هایی همچون [*Eraser*](glossary#Eraser) را پس از هر باز اجرا کردن [*CCleaner*](glossary#CCleaner) را مرتفع می کند.



<div class="getstarted" markdown="1">
Hands-on: Get started with the [*CCleaner Guide*](ccleaner)
</div>
