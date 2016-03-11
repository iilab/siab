

---

lang: fa
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 007
title: Recuva - File Recovery

---

**صفحه‌ی اصلی تارنما**

[**www.piriform.com/recuva**](http://www.piriform.com/recuva)
			
**نیازهای رایانه ای**

- قابل اجرا در تمامی نسخه های ویندوز (به جز نسخه ویندوز 98)

**روایت استفاده شده در این راهنما**

- 1.3 

**مجوز**

- رایگان افزار

**منابع لازم برای مطالعه**

- کتابچه راهنما [**فصل پنجم: چگونگی بازیابی اطلاعات از دست رفته**](chapter-5)

- **سطح**: ۱. مبتدی، **۲. متوسط**، ۳. میانه، ۴. باتجربه، ۵. پیشرفته

- زمان مورد نیاز برای شروع به استفاده از این ابزار: ۲۰ دقیقه




**آنچه در این راهنما خواهید آموخت**:

- توانایی اجرای روش‌های مختلف اسکن کردن فایل و اطلاعات مختلف
- توانایی بازیافت فایل‌های پاک شده از رایانه
- توانایی پاک‌سازی مطمئن اطلاعات شخصی یا محرمانه

**گنو لینوکس، مک، و سایر برنامه‌های هم سازگار با ویندوز**:

برای کاربران **گنو لینوکس** برنامه [**R-Linux**](http://www.r-tt.com/data_recovery_linux/) را توصیه می‌کنیم.

کاربران **مک** می‌توانند از [**TestDisk** و **PhotoRec**](http://www.cgsecurity.org/) که با **ویندوز** و **گنولینوکس** نیز سازگاری دارد، استفاده کنند.

علاوه بر برنامه **Recuva** برنامه‌های رایگان دیگر سازگار با ویندوز نیز وجود دارند که استفاده از آن‌ها توصیه می‌شود. برخی از این برنامه‌ها عبارتند از:

- [**NTFS Undelete**](http://ntfsundelete.com/)
- [**Disk Digger**](http://diskdigger.org/)
- [**PCInspector File Recovery**](http://www.pcinspector.de/Default.htm?language=1)
- [**FileRestorePlus**](http://undeleteplus.com/)

### ۱.۱ نکاتی که پیش از استفاده از این ابزار باید از آن‌ها آگاه باشید ###

در مواردی که فایل‌های شخصی یا محرمانه به اشتباه پاک شده باشند، برنامه **Recuva** می‌تواند به شما در اسکن کردن و بازیافت آن‌ها کمک کند. همان‌گونه که در [**فصل ششم: چگونگی از بین بردن اطلاعات محرمانه**](Chapter-6) بدان اشاره شد، فایلی که از طریق ویژگی *Delete* برنامه ویندوز پاک شده باشد، حتی پس از تخلیه سطل زباله ممکن است هنوز بر روی رایانه شما باقی‌مانده باشد.

اما موقعیت‌هایی وجود دارد که در آن‌ها **Recuva** قادر به بازیابی اطلاعات از دست رفته نخواهد بود. مثلاً اگر فایل‌های موقتی را با استفاده از نرم‌افزار **CCleaner** در حالتی که گزینه‌ی *Secure file deletion (Slower)* فعال بوده است پاک‌سازی کامل و دائم نموده باشید، فایل‌های مزبور عملاً غیر قابل بازیابی خواهند بود. **Recuva** نمی‌تواند فایل‌ها را پس از آنکه از برنامه‌هایی چون **CCleaner** و **Eraser** برای پاک‌سازی فضای خالی دیسک استفاده شده است، یا ویندوز بر روی فضایی که قبلاً توسط آن فایل آشغال شده بود، رونویسی کرده باشد، بازیابی کند. **Recuva** همچنین قادر به احیای اسناد یا فایل‌های آسیب دیده نیست.

از **Recuva** همچنین می‌توان برای رونویسی مطمئن داده‌های شخصی و محرمانه استفاده کرد.

