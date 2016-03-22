

---

lang: fa
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 4
depth: 3
title: Portable Thunderbird with GPG and Enigmail

---

## ۱- تفاوت‌های بین نسخه‌ی نصب شده و نسخه‌ی قابل حمل Thunderbird ##

مزیت اصلی استفاده از **نسخه‌ی قابل حمل Thunderbird** آن است که شما می‌توانید نسخه‌ای از رایانامه‌های (ایمیل‌) خود روی درایوهای جانبی یا حافظه‌ی USB ذخیره کنید. علاوه بر این، می‌توان **نسخه‌ی قابل حمل Thunderbird** به همراه رایانامه‌های شما در داخل یک بایگانی رمزگذاری شده **TrueCrypt** پنهان نمود. به این ترتیب، شما میزان امنیت رایانامه‌های خود را بهبود بخشیده، شناسه‌های رایانه‌ی (ایمیل) خود و آدرس‌هایی را که استفاده می‌کنید را مخفی می‌نمایید. با وجود این به خاطر داشته باشید که حافظه‌ی جانبی یا حافظه‌ی USB شما و ابزارهای قابل حمل درون آن تا زمانی محفوظ هستند که رایانه‌ی شما نیز سالم و عاری از آلودگی باشد. این برنامه‌ها نیز ممکن است در معرض خطر ناشی از حمله تبلیغ‌افزارها، بدافزارها، جاسوس‌افزارها و ویروس‌ها قرار گیرند.

**توجه**: برای حفظ حریم شخصی و امنیت ارتباطات رایانامه‌ای (ایمیلی) خود، قویاً توصیه می‌کنیم که **نسخه‌ی قابل حمل GnuPG** بر اساس آن‌چه که انتهای این صفحه آمده است دریافت کنید.


## ۲- چگونه می‌توان نسخه‌ی قابل حمل Thunderbird را دریافت و اجرا کرد ##

**مرحله‌ی ۱**. روی [**http://portableapps.com/apps/internet/Thunderbird_portable**](http://portableapps.com/apps/internet/Thunderbird_portable) کلیک کنید. 

**مرحله‌ی ۲**. روی  ![](/sbox/screen/thunderbirdportable-en/01.png) کلیک کنید تا صفحه‌ی دریافت برنامه در تارنمای **Source Forge** باز شود.


**مرحله‌ی ۳**. روی  ![](/sbox/screen/thunderbirdportable-en/02.png) کلیک کنید تا فایل نصب ![](/sbox/screen/thunderbirdportable-en/03.png) در رایانه‌ی شما ذخیره شود. 

**مرحله‌ی ۴**. روی ![](/sbox/screen/thunderbirdportable-en/03.png) دو بار کلیک کنید تا جعبه‌ی گفتگوی *Open File - Security Warning* باز شود، سپس روی ![](/sbox/screen/thunderbirdportable-en/04.png) کلیک کنید تا صفحه‌ای شبیه به صفحه‌ی زیر باز شود:

![](/sbox/screen/thunderbirdportable-en/05.png)

*تصویر ۱: پنجره‌ی Mozilla Thunderbird, Portable Edition | Portableapps.com Installer*

**مرحله‌ی ۵**. روی  ![](/sbox/screen/thunderbirdportable-en/06.png) کلیک کنید تا پنجره‌ای شبیه به پنجره‌ی زیر باز شود. 

![](/sbox/screen/thunderbirdportable-en/07.png)

*تصویر ۲: پنجره‌ی انتخاب محل نصب*

**مرحله‌ی ۶**. روی  ![](/sbox/screen/thunderbirdportable-en/08.png) کلیک کنید تا پنجره‌ی *Browse for Folders* باز شود. 

![](/sbox/screen/thunderbirdportable-en/09.png)

*تصویر ۳: پنجره‌ی جست‌وجو برای شاخه‌ی محل ذخیره شدن برنامه*

**مرحله‌ی ۷**. همان طور در *تصویر ۳* دیده می‌شود در حافظه‌ی جانبی یا حافظه‌ی USB روی  ![](/sbox/screen/thunderbirdportable-en/10.png) کلیک کنید تا محل نصب **نسخه‌ی قابل حمل Mozilla Thunderbird** تایید شده و به پنجره‌ی *Choose Install Location* بازگردید. 

**توجه**: انتخاب یک نام متفاوت برای شاخه‌ی حاوی **نسخه‌ی قابل حمل Thunderbird** فهمیدن این که از چنین برنامه‌ای استفاده می‌شود را سخت‌تر می‌کند.

**مرحله‌ی ۸**. روی  ![](/sbox/screen/thunderbirdportable-en/11.png) کلیک کنید تا پنجره‌ی *Installing* باز شده و مراحل غیر فشرده‌سازی فایل **نسخه‌ی قابل حمل Mozilla Thunderbird** آغاز شود. در ادامه روی ![](/sbox/screen/thunderbirdportable-en/12.png) کلیک کنید تا فرآیند غیر فشرده‌سازی به پایان برسد. 

**مرحله‌ی ۹**: درایو جانبی یا حافظه‌ای USB، **نسخه‌ی قابل حمل Mozilla Thunderbird** را پیدا کنید. 

**مرحله‌ی ۱۰**. دو بار کلیک کنید تا درایو جانبی یا حافظه‌ی USB باز شود. باید تصویری مشابه با تصویر زیر ظاهر شود:

![](/sbox/screen/thunderbirdportable-en/13.png)

*تصویر ۴: نسخه‌ی قابل حمل تازه نصب شده‌ی Mozilla Thunderbird که شاخه‌ی Thunderbird Portable در آن دیده می‌شود. 


## ۳- چگونه می‌توان نسخه‌ی قابل حمل GPG را برای Thunderbird دریافت و اجرا کرد ##


**مرحله‌ی ۱**. روی [**http://portableapps.com/support/thunderbird_portable#encryption**](http://portableapps.com/support/thunderbird_portable#encryption) کلیک کنید.

**مرحله‌ی ۲**. روی ![](/sbox/screen/thunderbirdportable-en/18.png) **کلیک کنید تا پنجره‌ی دریافت *GPG_for_Thunderbird_Portable_1.4.11.paf.exe* باز شود، و در ادامه روی ![](/sbox/screen/thunderbirdportable-en/02.png) کلیک کنید تا فایل نصب ![](/sbox/screen/thunderbirdportable-en/18.png) در رایانه شما ذخیره شود. 

**مرحله‌ی ۳**. روی ![](/sbox/screen/spybotportable-en/04.png) دو بار کلیک کنید تا جعبه‌ی گفتگوی *Open File - Security Warning* ظاهر شود، سپس روی ![](/sbox/screen/thunderbirdportable-en/04.png) کلیک کنید تا صفحه‌ای شبیه به صفحه‌ی زیر باز شود:

![](/sbox/screen/thunderbirdportable-en/19.png)

*تصویر ۶: پنجره‌ی زبان نصب*

**مرحله‌ی ۴**. روی ![](/sbox/screen/thunderbirdportable-en/10.png) دو بار کلیک کنید تا پنجره‌ی **GPG for Thunderbird | Portable Apps Installer** باز شود، سپس روی  ![](/sbox/screen/thunderbirdportable-en/06.png) کلیک کنید تا پنجره‌ای شبیه به پنجره‌ی زیر باز شود. 

**توجه**: انتخاب یک نام متفاوت برای شاخه‌ی حاوی **نسخه‌ی قابل حمل GPG** فهمیدن این که از چنین برنامه‌ای استفاده می‌شود را سخت‌تر می‌کند.

![](/sbox/screen/thunderbirdportable-en/20.png)

*تصویر ۷: پنجره‌ی انتخاب محل نصب*

**مرحله‌ی ۵: روی ![](/sbox/screen/thunderbirdportable-en/08.png) کلیک کنید تا پنجره‌ی *Browse for Folder* باز شود:

![](/sbox/screen/thunderbirdportable-en/21.png)

*تصویر ۸: پنجره‌ی جست‌وجو برای شاخه‌ی محل ذخیره شدن برنامه*

**مرحله‌ی ۶**. روی ![](/sbox/screen/thunderbirdportable-en/10.png) کلیک کنید تا به پنجره‌ی *Choose Install Location* باز شود (*تصویر ۷*). سپس با کلیک کردن روی ![](/sbox/screen/thunderbirdportable-en/11.png) غیر فشرده شدن 
**نسخه‌ی قابل حمل GnuPG** آغاز می‌شود. پس از آن که مراحل غیر فشرده‌سازی به پایان رسید، روی  ![](/sbox/screen/thunderbirdportable-en/12.png) کلیک کنید. 

**مرحله‌ی ۷**. در حافظه‌ی جانبی یا حافظه‌ی USB *E:\ThunderbirdPortable\App* را انتخاب کنید تا **نسخه‌ی قابل حمل GPG برای Thunderbird** با موفقیت باز شود. 

![](/sbox/screen/thunderbirdportable-en/23.png)

*تصویر ۹: در درایو جانبی نسخه‌ی قابل حمل برنامه‌ی GPG برای Thunderbird دیده می‌شود*


## ۴- چگونه می‌توان Enigmail را دریافت و اجرا کرد ##

**Enigmail** یک افزونه برای برنامه‌ی **Mozilla Thunderbird** است که با کمک آن می‌توانید از حریم شخصی ارتباطات رایانامه‌ای (ایمیلی) خود حفاظت کنید. **Enigmail** به طور ساده یک رابط کاربردی است که به شما امکان می‌دهد تا از برنامه رمزگذاری **GnuPG** در برنامه‌ی **Thunderbird** استفاده کنید. رابط کاربردی **Enigmail** به صورت *OpenPGP* در کادر ابزارهای برنامه‌ی **Thunderbird** مشاهده می‌شود.

**مرحله‌ی ۱**. روی [**http://enigmail.mozdev.org/home/index.php.html**](http://enigmail.mozdev.org/home/index.php.html) کلیک کنید تا به تارنمای دریافت فایل هدایت شوید.

**مرحله‌ی ۲**. روی ![](/sbox/screen/thunderbirdportable-en/24.png) در زیر دکمه‌ی *Download* در گوشه بالا و سمت چپ صفحه کلیک کنید تا پنجره‌ی دانلود *enigmail-1.1.2-tb-win.xpi* باز شود، سپس روی  ![](/sbox/screen/thunderbirdportable-en/25.png) کلیک کنید تا فایل نصب ![](/sbox/screen/thunderbirdportable-en/26.png) در رایانه شما ذخیره شود. 

**مرحله‌ی ۳**. شاخه‌ی **Thunderbird Portable** را باز کنید و روی ![](/sbox/screen/thunderbirdportable-en/14.png) دو بار کلیک کنید تا **Thunderbird Portable** باز شود.

**مرحله‌ی ۴**. **Tools > Add-ons** را از فهرست (منو) بالای **نسخه‌ی قابل حمل Thunderbird** انتخاب کنید:

![](/sbox/screen/thunderbirdportable-en/27.png)

*تصویر ۱۰: فهرست بالای نسخه‌ی قابل حمل Thunderbird که گزینه‌ی Add-ons در آن در حالت انتخاب شده*

*این کار باعث باز شدن پنجره‌ی زیر خواهد شد*:

![](/sbox/screen/thunderbirdportable-en/28.png)

*تصویر ۱۱:‌ پنجره‌ی افزونه‌ها در نسخه‌ی قابل حمل Thunderbird*

**مرحله‌ی ۵**. روی ![](/sbox/screen/thunderbirdportable-en/29.png) کلیک کنید تا نصب **Enigmail** به پایان برسد و **نسخه‌ی قابل حمل Thunderbird** باز شروع شود. 

<div class=getstarted markdown=1>
اگر برای کار با **نسخه‌ی قابل حمل Thunderbird** و **GPG برای Thunderbird** نیاز به راهنمایی دارید، لطفاً به فصل [**Thunderbird – برنامه‌ای امن برای مدیریت رایانامه (ایمیل)**](/fa/thunderbird) در **راهنماهای دستی** سری بزنید تا شیوه‌ی کار با آن را بیاموزید.
</div>

