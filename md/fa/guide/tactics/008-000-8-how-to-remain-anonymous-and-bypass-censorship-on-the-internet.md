

---

lang: fa
community: guide
type: tactics
legacy: True
child: False
weight: 008
title:  8. How to remain anonymous and bypass censorship on the Internet

---

در برخی از کشورهای جهان نرم‌افزارهایی بر سر راه شبکه اینترنت قرارداده شده است که مانع از دست‌رسی کاربران به برخی تارنماها و سرویس‌های اینترنتی می‌شود. حتا در برخی شرکت‌ها، مدارس، و کتاب‌خانه‌های عمومی از چنین نرم‌افزارهایی استفاده می‌شود تا کاربران به مطالبی که از نظر مدیران آن مراکز برای آن‌ها مناسب نیست، دست‌رسی نداشته باشند. به طور کلی فن‌آوری فیلترینگ دارای گونه‌های مختلفی است. برخی فیلترها، تارنما را بر اساس [*آدرس IP*](/fa/glossary#IP_address) آن‌ها مسدود می‌کنند، حال آن که برخی دیگر از فیلترها بر مبنای لیست سیاهی که از [*نام دامنه*](/fa/glossary#Domain_name)های تشکیل شده است، عمل کرده و یا در مواردی در لابلای ارتباطات اینترنتی رمزگذاری نشده به دنبال لغات کلیدی معین می‌گردند و در صورت مشاهده آن، محتوا را مسدود می‌کنند. 

صرف نظر از نوع شیوه‌ی فیلترینگ، تقریباً همیشه می‌توان از طریق رایانه‌های واسط مستقر در خارج از کشور سانسور کننده، فیلترها را دور زده و به تارنما یا سرویس اینترنتی مسدود شده دست یافت. به طور کلی مجموعه مراحلی را که به کاربر کمک می‌کند تا از کمند فیلترهای اینترنت رهایی یابد *دور زدن سانسور* یا به طور خلاصه [*دور زدن*](/fa/glossary#Circumvention) می‌نامند و به رایانه‌های واسط [*پراکسی*](/fa/glossary#Proxy) می‌گویند. البته خود [*پراکسی*](/fa/glossary#Proxy)ها نیز انواع مختلفی دارند. در این فصل ابتدا به طور خلاصه در مورد شبکه‌های ناشناس‌مانی چند-پراکسی صحبت خواهد شد، سپس به طور مفصل در مورد پراکسی‌های اصلی ویژه‌ی دور زدن سانسور اینترنت و هم‌چنین نحوه‌ی کار با آن‌ها مطالبی ارائه می‌شود.

هر دو روش بالا از کارآیی لازم برای عبور از فیلترهای اینترنت برخوردارند، اما انتخاب روش مناسب کاملاً به شرایط و نوع نیاز کاربر بستگی دارد. به عنوان مثال اگر حاضر باشید که سرعت مرور اینترنت را قربانی امنیت ارتباطی و ناشناس ماندن بکنید، آن‌گاه روش اول گزینه‌ی مناسب‌تری برای شما خواهد بود. اما اگر با افراد یا تشکیلاتی که [*پراکسی*](/fa/glossary#Proxy) مورد استفاده شما را اداره می‌کنند آشنا بوده و به آن‌ها اعتماد دارید یا اگر کارآیی و سرعت اینترنت از موضوع ناشناس ماندن با اهمیت‌تر است، آن‌گاه یک فیلترشکن معمولی ممکن است چاره‌ساز باشد.



<div class="background" markdown="1">
منصور و مریم، خواهر و برادری هستند که در وب‌نوشت شخصی‌شان به طور ناشناس مطالبی در مورد تاریخ کهن و نوین ایران می‌نگارند. این دو گاهی در بین مطالبشان به مقایسه‌ی شرایط گذشته و فعلی جامعه ایران می‌پردازند، به همین خاطر برخی از مسئولان دستگاه‌های حکومتی واکنش‌ها و نگرانی‌هایی را نسبت به مطالب ارائه شده در وب‌نوشت آن‌ها نشان داده‌اند. تارنمای آن‌ها هنوز از طرف مقامات ایرانی مسدود نشده است و میزبانی آن را نیز شرکتی در خارج از ایران بر عهده دارد. آن‌ها حدس می‌زنند مقامات در تلاش برای شناسایی مدیران این وب‌نوشت باشند. منصور و مریم نگرانند که مبادا هویت آن‌ها از طریق به‌روز رسانی‌هایی که می‌کنند، شناسایی شود. به علاوه، آن‌ها می‌خواهند خود را برای زمانی که وب‌نوشتشان توسط دولت مسدود شود، آماده سازند. بدین ترتیب نه تنها خواهند توانست که مطالب خود را به‌روز کنند بلکه می‌توانند اطلاعاتی را در مورد ابزار دور زدن سانسور اینترنت به خوانندگان خود در داخل ایران ارائه دهند.
</div>


### آن‌چه در این فصل می‌آموزید: ###

- چگونه از داخل کشور محل اقامت خود به تارنمایی که فیلتر شده است دست‌رسی پیدا کنید. 
- چگونه می‌توان مانع از آن شد که تارنماهایی که به آن‌ها سر می‌زنید از جای شما آگاه شوند.
- چگونه می‌توان اطمینان حاصل کرد که [*ISP*](/fa/glossary#ISP) و تشکیلاتی که فعالیت‌های شما را زیر نظر دارد ، از این که به چه تارنماهایی سرزده و چه خدمات ایتنرنتی را مورد استفاده قرارداده‌اید، مطلع نخواهند شد. 
 
