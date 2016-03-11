

---

lang: fa
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 006
title: Cobian Backup - Secure File Backup

---

**صفحه اصلی وبسایت**

[**www.educ.umu.se/~cobian /cobianbackup.htm**](http://www.educ.umu.se/~cobian/cobianbackup.htm)


**نیازهای رایانه‌ای:**

XP, 2003, Vista, 2008, Windows 7
ویندوزهای ۹۵، ۹۸ و ME با نسخه‌ی Cobian [**version 7**](/sites/securitybkp.ngoinabox.org/security/files/cobian/Cb7Setup.exe) سازگار اند


**نسخه‌ی به کار رفته در این راهنما**:

- ۱۰

**مجوز**:

- نرم افزار آزاد 

**منابع مورد نیاز برای مطالعه**:

کتابچه‌ی راهنما: فصل [**۵. چگونه اطلاعات از دست رفته را بازیابی کنیم**](/chapter-5)


**سطح یادگیری**:  ۱:مبتدی، ۲:متوسط، **۳: نیمه حرفه‌ای**، ۴: باتجربه، ۵- پیشرفته


**زمان یادگيری و شروع استفاده از این ابزار**: ۳۰ دقیقه


**آنچه با مطالعه این راهنما خواهید آموخت**:

- توانایی پشتیبان گرفتن از تمام اسناد، فایل‌ها و پوشه‌ها
- توانایی فشرده و غیرفشرده کردن فایل‌های پشتیبان خود
- توانایی رمزگذاری و رمز زدایی از فایل‌های بایگانی خود


**گنو لینوکس، مک او اس و دیگر برنامه‌های سازگار مایکروسافت ویندوز:**

بایگانی کردن یا پشتیبان گرفتن از اسناد، فایل‌ها و پوشه‌های شما می‌تواند به سادگی کپی کردن فایل‌ها از یک مکان به مکان امن دیگری باشد، برای این به ابزارهای ویژه احتیاج نیست. هرچند هنگامی که تعداد بیشتری سند و فایل را بایگانی می‌کنید شما از یک برنامه‌ی ویژه برای پشتیبان گرفتن از فایل‌ها (مانند **Cobian Backup**) یا یک ابزار *همسان سازی فایل*، برنامه‌هایی که اطمینان حاصل می‌کنند که هر دو مکان ابتدایی یا «مبدأ» و مکان جدید دقیقا محتوای یکسانی دارند، سود می‌برید. به غیر از  **Cobian Backup** ابزارهای بسیاری برای کمک کردن به شما در بایگانی کردن یا پشتیبان گرفتن از اسناد شما وجود دارند. فهرست پیشنهادی ما از این قرار است: 

-  [**Freebyte Backup**](http://www.freebyte.com/fbbackup/) نرم‌افزار آزاد پشتیبان گیرنده ای است که برای مایکروسافت ویندوز طراحی شده است
- [**Unison File Synchronizer**](http://www.cis.upenn.edu/~bcpierce/unison/) برنامه ای آزاد و کد باز برای **مایکروسافت ویندوز**، **مک او اس** و **گنولینوکس** است
-  [**Allway Sync**](http://allwaysync.com/) is a freeware ابزار آزاد همسان سازی فایل‌ها برای **مایکروسافت ویندوز** است
-  [**FreeFileSync**](http://freefilesync.sourceforge.net/) برنامه ای آزاد و کد باز برای **مایکروسافت ویندوز**، **مک او اس** و **گنولینوکس** است
- [**Time Machine**](https://secure.wikimedia.org/wikipedia/en/wiki/Time_Machine_%28Mac_OS%29) ابزار پشتیبان گیرنده‌ی توسعه یافته توسط **اپل** است که در **سيستم عامل مک** وجود دارد (نسخه‌ی ۱۰/۵ به بعد) و
- کاربران گنولینوکس لطفا راهنمای [**Backup Your System**](https://help.ubuntu.com/community/از سیستم خود پشتیبان بگیرید) را برای توضیح دادن ابزارهایی که شما می‌توانید استفاده کنید بخوانید


## ۱.۱ چیزهایی که درباره‌ی این ابزار پیش از شروع باید بدانید ##

**Cobian Backup** برای بایگانی کردن (یا نسخه‌ی پشتیبان گرفتن) از فایل‌ها و پوشه‌های شما استفاده می‌شود. پشتیبان‌ها می‌توانند در مسیرها یا درایوهای دیگر بر روی کامپیوتر شما، کامپیوترهای دیگر در شبکه‌ی محل کار یا وسایل قابل حمل (سی‌دی‌ها، دی‌وی‌دی‌ها و حافظه‌های یو‌اس‌بی) ذخیره شوند. **Cobian Backup** به شما اجازه می‌دهد که به طور مداوم از فایل‌ها و مسیرهایتان  پشتیبان بگیرید. **Cobian Backup** در پس‌زمینه‌ی سیستم شما (یعنی در سینی سیستم) کار می‌کند، زمان‌بندی شما را چک کرده و روند پشتیبانی لازم را زمانی که لازم است اجرا می‌کند.  **Cobian Backup**  هم‌چنین می‌تواند فایل‌ها را هم‌زمان با تولید فایل پشتیبان فشرده و رمز‌گذاری کند.
