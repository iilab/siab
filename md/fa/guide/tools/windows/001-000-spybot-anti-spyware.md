

---

lang: fa
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 001
title: Spybot - Anti-Spyware

---

			
**صفحه اول تارنما**

[**www.safer-networking.org/en**](http://www.safer-networking.org/en)

**نیازهای رایانه ای**

- تمامی نسخه‌ی های ویندوز


**نسخه‌ی مورد استفاده در این راهنما**

- 1.6.2

**مجوز**

- نرم‌افزار آزاد


**منابع مورد نیاز برای مطالعات بیشتر**

- کتابچه راهنما فصل ۱. چگونه از رایانه‌ی خود در برابر ویروس‌ها، بدافزارها، و هکرها مراقبت کنیم


**سطح یادگیری**: ۱. مبتدی، **۲. متوسط**، ۳. میانه، ۴. با تجربه، ۵. پیشرفته


**مدت زمان لازم برای شروع به استفاده از ابزار**: ۲۰ دقیقه

آنچه با مطالعه این راهنما خواهید آموخت:

- امکان **پاک کردن** انواع مختلف بدافزار و/یا جاسوس افزار
- امکان **ایمن سازی** سیستم رایانه‌ی خود پیش از آنکه به بدافزارها آلوده شده یا در معرض تهدید قرار گیرد



**گنولینوکس، سیستم عامل مک، و سایر برنامه‌های هم سازگار با ویندوز**:

سیستم عامل‌های **گنو لینوکس** و **مک**، در حال حاضر عاری از بدافزارها (جاسوس افزار، ویروس، و غیره) هستند. برای آنکه از خود در قبال این نرم افزارهای مخرب حفاظت کنید توصیه می‌کنیم که: **۱)** سیستم عامل و تمامی نرم افزارهای نصب شده بر روی رایانه‌ی خود را به طور منظم به-هنگام کنید؛ **۲)** از برنامه‌های ضد ویروسی که در فصل [*Avast*](avast) شده‌اند استفاده کنید؛ **۳)** از برنامه دیوار آتش که در فصل [*Comodo*](comodo) شرح آن آمده است استفاده کنید؛ **۴)** از مرورگرهای ایمنی چون [*Firefox*](firefox) همراه با افزونه [*NoScript*](firefox_noscript) که مانع از دریافت شدن اسکریپت های متصل به صفحات وب در هنگام مرور آن‌ها می‌شود، استفاده کنید. این روش‌های پیشگیری رایانه های مبتنی بر **گنولینوکس** و **مک** را به خوبی محافظت خواهند کرد.

وضعیت امنیتی رایانه های مبتنی بر سیستم عامل **ویندوز** بسیار متفاوت است. هزاران بدافزار جدید روزانه خلق می‌شوند. روش‌های حمله به رایانه به طور فزاینده ای پیچیده‌تر می‌شوند. روش‌های پیشگیری که در پاراگراف بالا بدان‌ها اشاره شد برای رایانه های مبتنی بر **ویندوز** جنبه **اجباری** دارد. به علاوه، استفاده از نرم‌افزار **Spybot** که شرح آن در این راهنما خواهد آمد نیز قویاً توصیه می‌شود.

با وجود این، چنانچه علیرغم این روش‌های احتیاطی، رایانه‌ی شما آلوده شد و احساس کردید که به ابزارهای دیگری نیاز دارید، محصولات زیر به شما توصیه می‌کنیم:

۱. برنامه [**SuperAntiSpyware**](http://superantispyware.com) را نصب کرده، تعاریف جاسوس افزارها را به-هنگام کنید، و سپس رایانه‌ی خود را اسکن نمایید.
۲. برنامه [**Malwarebytes Anti-Malware**](https://www.malwarebytes.org/mbam.php) نصب کرده، *Quick Scan* را اجرا و پس از پایان آن *Scan* را انجام دهید، و سپس هرگونه بدافزار شناسایی شده که در بخش *Show Results* به نمایش در می‌آید را پاک کنید.
۳. از نرم افزارهای ضد جاسوس افزار باز دیگر مانند: [**Microsoft Windows Defender**](http://www.microsoft.com/windows/products/winfamily/defender)، [**Ad-Aware Internet Security**](http://www.lavasoft.com/)، یا [**SpywareBlaster**](http://www.javacoolsoftware.com/spywareblaster.html) استفاده کنید.


### ۱.۱ نکاتی که پیش از شروع به استفاده از این ابزار باید از آن مطلع باشید ###

**Spybot S&D** یک نرم‌افزار باز محبوب برای شناسایی و پاک کردن انواع مختلف تبلیغ افزار، بدافزار، و جاسوس افزار از روی رایانه‌ی شماست. این برنامه همچنین رایانه‌ی شما را در برای تبلیغ افزارها، بدافزارها، و جاسوس افزارها ایمن کرده و مانع از آلوده شده رایانه‌تان به آن‌ها می‌شود. 

تبلیغ افزار شامل هرگونه نرم افزاری است که تبلیغات و آگهی‌ها را بر روی رایانه‌ی شما به نمایش در می‌آورد. برخی از انواع تبلیغ افزارها همانند جاسوس افزار عمل نموده و قادرند که به حریم خصوصی و امنیت شما خدشه وارد کنند.

جاسوس افزار به برنامه‌هایی گفته می‌شود که داده‌های شما را جمع آوری کرده، اطلاعات شخصی شما را مشاهده و ضبط می‌کنند، و عادات اینترنتیتان را ردیابی می‌کنند. همانند بدافزارها، جاسوس افزارها نیز به صورت مخفیانه در حال اجرا شدن بر روی رایانه‌ی شما هستند. به همین دلیل، با نصب کردن برنامه‌ای مانند **Spybot** از شما و رایانه‌ی شما محافظت خواهد شد.

**Spybot** همچنین برنامه ضمیمه ای به نام **TeaTimer** را نیز نصب می‌کند. این برنامه رایانه‌ی شما را در برابر آلودگی به بدافزارهای جدید محافظت می‌کند. 


**توجه**: **ویندوز ویستا** دارای برنامه ضد جاسوس افزاری به نام **Windows Defender** است که از پیش در آن قرار داده شده است. اما، به نظر می‌رسد که برنامه **Spybot** بدون هیچ مشکلی در **ویندوز ویستا** کار می‌کند.

