

---

lang: fa
community: guide
type: tactics
legacy: True
child: False
weight: 006
title: 6. How to destroy sensitive information

---

در فصل‌های گذشته راجع به روش‌ها و تکنیک‌هایی که با کمک آن‌ها می‌توان از داده‌ها و اطلاعات محرمانه مراقبت کرد، صحبت به میان آمد. اما اگر بخشی از آن اطلاعات، دیگر مورد نیاز شما نباشند با آن‌ها چه می‌کنید؟ به عنوان مثال اگر به این نتیجه برسید که نسخه‌ی کپی از اطلاعات اصلی که رمزگذاری نیز شده است، نیاز شما را برطرف کرده و دیگر احتیاجی به نسخه‌ی اصلی ندارید، بهترین روش برای پاک کردن آن‌ها چیست؟ متأسفانه پاسخ به این سؤال پیچیده‌تر از آن است که تصور می‌کنید. زمانی که یک فایل را پاک می‌کنید، حتا پس از خالی کردن **Recycle bin**، محتویات آن فایل هنوز در جایی روی دیسک سخت رایانه‌ی شما وجود دارد و با استفاده از نرم‌افزارهای مناسب و داشتن کمی شانس می‌توان آن را به طور تمام و کمال بازیابی کرد. 

برای اطمینان از این که افراد غیر مجاز نخواهند توانست اطلاعات پاک شده توسط شما را بازیابی کنند، به نرم‌افزارهای ویژه‌ای نیاز دارید که می‌توانند اطلاعات شما به طور کامل و غیر قابل بازیابی از بین ببرند. نرم‌افزار [*Eraser*](/fa/glossary#Eraser) از جمله این ابزارها است که در ادامه راجع به آن صحبت می‌شود. در‌ واقع استفاده از [*Eraser*](/fa/glossary#Eraser) مانند این است که به جای دور ریختن کاغذهای باطله در سطل زباله، از کاغذ خردکن استفاده کنید. البته پاک کردن دائمی فایل‌ها تنها یکی از موضوعاتی است که در مبحث حذف اطلاعات حساس، به آن پرد اخته می‌شود. حال اگر اهمیت اطلاعات محرمانه‌ای که قرار است پاک شوند به قدری باشد که اگر آن اطلاعات به دست افراد غیر مجاز یا گروه‌های قدرتمند رقیب و مخالف شما بیافتد، اطلاعات ارزشمندی را در رابطه با شما و تشکیلات شما در در اختیار آن‌ها قرار دهد، آن‌گاه لازم است که نه تنها راجع به پاک کردن دائمی آن‌ها چاره‌ای بیاندیشید، بلکه اقدام‌های دیگری از قبیل از بین بردن نسخه‌های پشتیبان قدیمی، [*پاک‌سازی کامل*](/fa/glossary#Wiping) سخت‌دیسک‌های کهنه‌ای که می‌خواهید به دیگران بدهید، حذف شناسه‌های کابری قدیمی و پاک کردن حافظه‌ی موقت مرورگر اینترنتی‌تان، را نیز مد نظر قرار دهید.

نرم‌افزار [*CCleaner*](/fa/glossary#CCleaner) یکی دیگر از برنامه‌هایی است که در این فصل راجع به آن صحبت می‌کنیم. این نرم‌افزار در پاک کردن فایل‌های موقتی که در هر باز استفاده از سیستم‌عمل و نرم‌افزارهای کاربردی مختلف روی رایانه ذخیره می‌شوند، بسیار مؤثر عمل می‌کند. 



<div class="background" markdown="1">
الینا یکی از متخصصین محیط زیست در یکی از استان‌های شرقی است. او تارنمایی را اداره می‌کند که در آن به مسائل و مشکلات مربوط به قطع غیر قانونی درختان و جنگل‌زدایی‌های بی‌رویه در منطقه می‌پردازد. تارنمای وی از شهرت روزافزونی برخوردار شده و عده‌ی زیادی بازدید کننده دارد. او نسخه‌ی پشتیان از اطلاعات موجود در تارنمای خود تهیه کرده و یک کپی از آن را در خانه و کپی دیگر را در محل کار و بالاخره یک کپی نیز در لپ‌تاپ جدیدش نگهداری می‌کند. هم‌چنین به تازگی شروع به تهیه کپی از شمار بازدیدکنندگان و هم‌چنین مطالبی که در تالار گفتگوی تارنمایش از طرف خوانندگانش فرستاده شده، کرده است. الینا به زودی به خارج از کشور سفر خواهد کرد تا در یک کنفرانس بین‌المللی طرفداران محیط زیست شرکت کند. او گزارش‌هایی دریافت کرده است مبنی بر این که لپ‌تاپ برخی شرکت کنندگان این کنفرانس در هنگام خروج از کشور برای مدت بیش از یک ساعت توقیف بوده است. الینا برای حفاظات از اطلاعات محرمانه‌اش، نسخه‌های پشتیبان خود را در خانه و محل کار به صندوقچه‌های رمزگذاری شده‌ی TrueCrypt انتقال داده و نسخه‌ای را که روی لپ‌تاپ خود نگهداری می‌کرد، پاک کرده است. برادرزاده وی، نیکزاد به او هشدار داده است اگر او نگران است که لپ‌تاپش را در هنگام خروج از مرز توقیف کنند، بهتر است فقط به پاک کردن ساده‌ی نسخه پشتیبان اکتفا نکند.
</div>

### آن‌چه در این فصل می‌آموزید: ###

- چگونه اطلاعات حساس را برای همیشه از روی رایانه خود پاک کنید
- چگونه اطلاعات حساس ذخیره شده روی ابزارهای قایل حمل لوح‌های فشرده و حافظه‌های USB را حذف کنید
- چگونه از آگاه شدن افراد غیرمجاز نسبت به اسنادی که اخیرا با آن‌ها کار کرده‌اید، جلوگیری کنید
- چگونگی نگهداری از رایانه نگهداری کنید به گونه‌ای که اطلاعات حذف شده از روی آن هرگز قابل بازیابی نباشند

