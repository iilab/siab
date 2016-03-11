

---

lang: fa
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Configure Important Thunderbird Settings

---

فهرست عناوین این بخش عبارتند از:

- [**۳.۰ در باره گزینه امنیت در برنامه  Thunderbird**](#3.0)
- [**۳.۱ چگونه می‌توان کادر بازبینی صفحه را در برنامه  Thunderbird غیرفعال کرد**](#3.1)
- [**۳.۲ چگونه می‌توان ویژگی HTML را در برنامه  Thunderbird غیرفعال کرد**](#3.2)
- [**۳.۳ چگونه می‌توان تنظیمات برگه های امنیت را در برنامه  Thunderbird انجام داد**](#3.3)
- [**۳.۴ چگونه می‌توان تنظیمات مربوط به فیلترکردن پیامهای زائد را انجام داد**](#3.4)

-------

<a name="3.0"></a>
## ۳.۰ درباره گزینه امنیت در برنامه  Thunderbird ##

در برنامه **Mozilla Thunderbird**، امنیت یعنی حفاظت از رایانه تان در برابر پیامهای ایمیل مضر و مخرب. برخی پیامهای ایمیل ممکن است اسپم باشند، و برخی دیگر ممکن است حاوی جاسوس افزار و ویروس باشند. تنظیمات متعددی در برنامه **Mozilla Thunderbird** وجود دارند که برای تقویت توانایی آن در برابر حملاتی که از طریق ایمیل‌ها به سیستم شما می‌شود می باید آن‌ها را تغییر داد، غیرفعال و یا فعال کرد. اما این امر که رایانه شما مجهز به نرم افزارهای ضد بدافزار و دیوار آتش )فایروال( باشد نیز از اهمیت بسیاری برخوردار است. 

برای کسب اطلاعات بیشتر در باره حملات مضر و مخرب از جانب پیامهای ایمیل با استفاده از برنامه‌هایی چون [**Avast**](avast), [**Comodo Firewall**](comodo) و [**Spybot**](spybot_main) لطفاً به کتابچه راهنما فصل [**۱. چگونه از رایانه تان در برابر ویروس ها، بدافزارها، و هکرها محافظت کنید**](chapter-1) مراجعه کنید.


<a name="3.1"></a>
## ۳.۱ چگونه می‌توان کادر پیش نمایش را در برنامه  Thunderbird غیرفعال کرد ##

صفحه برنامه **Thunderbird** به سه قسمت تقسیم می شود: بخش سمت چپ شاخه‌های اکانت های ایمیل شما را نشان می دهد. در بخش سمت راست فهرستی از پیامها دیده می شود، و در همان قسمت سمت راست در کادر پایین، پیش نمایش محتوای ایمیل انتخاب شده به نمایش در می آید. به محض اینکه یکی از پیامهای ایمیل انتخاب می‌شود پیش نمایش آن بصورت خودکار مشاهده می گردد. 

**توجه**: چنانچه پیام ایمیلی که برای شما فرستاده می‌شود حاوی کد برنامه مخرب باشد، پیش نمایش آن، کد مزبور را فعال می کند. بنابراین بهتر است که ویژگی پیش نمایش ایمیل از حالت فعال خارج شود. 

![](/sbox/screen/thunderbird-en/23.png)

*تصویر ۱: رابط کاربری اصلی برنامه Thunderbird*


برای غیرفعال کردن پیش نمایش، مراحل زیر را انجام دهید:

**مرحله ۱**. زیرمنوی **View > Layout** **انتخاب** کرده و گزینه *Message Pane* را **انتخاب** کنید تا همانطور که در تصویر زیر دیده می شود، پیش نمایش از حالت فعال درآید:

![](/sbox/screen/thunderbird-en/24.png)

*تصویر ۲: منوی View که در آن زیرمنوی Layout که گزینه Message Pane در آن انتخاب شده است دیده می شود*


بدینترتیب کادر پیام (Message Pane) ناپدید می‌شود، و از این پس برای آنکه بتوانید محتوای یک پیام را مشاهده کنید باید بر روی آن **دوبار کلیک** کنید. اگر یک پیام ایمیل مظنون به نظر آید (مثلا موضوع آن غیرمنتظره یا نامربوط بوده، یا از طرف شخصی ناشناس فرستاده شده باشد) آن وقت می‌توانید بدون پیش نمایش شدن آن در مورد حذف پیام مزبور تصمیم بگیرید. 


<a name="3.2"></a>
## ۳.۲ چگونه می‌توان ویژگی HTML را در برنامه  Thunderbird غیرفعال کرد ##

برنامه **Thunderbird** به شما امکان میدهد تا برای نوشتن پیام و خواندن آن از زبان **HTML** استفاده کنید. این ویژگی شما را قادر می‌سازد تا  پیامهای حاوی رنگ‌های گوناگون، قلم های متفاوت، تصویر و سایر توانمندی‌های قالب بندی راارسال کرده یا دریافت دارید. اما **HTML** همان زبانی است که برای طراحی صفحات وب نیز بکار می رود بنابراین مشاهده پیامها با قالب **HTML** ممکن است شما در برابر خطرات ناشی از حملاتی که صفحات وب را نیز تهدید می‌کنند، آسیب‌پذیر کند. 

برای غیرفعال کردن ویژگی قالب بندی **HTML**، مراحل زیر را انجام دهید:

**مرحله ۱.** **View > Message Body As > Plain Text** را **انتخاب** کنید:

![](/sbox/screen/thunderbird-en/25.png)

*تصویر ۳: در منوی View زیرمنوی Message Body که در آن گزینه Plain Text انتخاب شده است، دیده می شود*


<a name="3.3"></a>
### ۳.۳ چگونه می‌توان تنظیمات برگه های امنیت را در برنامه  Thunderbird انجام داد ###

برنامه **Thunderbird** دارای دو فیلتر درونی برای ایمیل‌های ناخواسته (Junk Mail) است که می‌تواند به شما در تعیین اینکه کدامیک از ایمیل‌های دریافتی تان  اسپم می‌باشد کمک کند. بصورت پیش فرض، این فیلترها در حالت غیر فعال قرار دارند، بنابراین بایستی آن‌ها را فعال کنید. حتی پس از آنکه آن‌ها فعال شدند، شما همچنان ایمیل‌های ناخواسته دریافت خواهید کرد، اما برنامه  **Thunderbird** آن‌ها را در شاخه ایمیل‌های ناخواسته قرار می دهد. 

کلاهبرداری از طریق ایمیل – که معمولاً به آن‌ها ایمیل‌های pishing نیز گفته می‌شود – وضعیتی است که از وسوسه کردن شما برای کلیک کردن روی لینک های درون ایمیل ها استفاده می کند. در غالب اوقات این لینک ها مرورگر شما را به وبسایتی هدایت می‌کنند که رایانه شما را به ویروس آلوده می نماید. در برخی دیگر از موارد، لینک شما را به وبسایتی منتقل می‌کند که در ظاهر موجه به نظر می‌رسد اما در عمل شما را فریب می دهد که نام کاربری و رمز عبور یکی از شناسه‌های خود را وارد کنید. در این وضعیت اطلاعات شما دزدیده شده، مورد سوء استفاده قرار گرفته یا به مؤسسات و افراد دیگر با اهداف تجاری یا مخرب فروخته می‌شود. 

برنامه **Thunderbird** می‌تواند به شما کمک کند تا اینگونه ایمیل‌ها را شناسایی کنید و همچنین به شما در مورد وجود چنین خطراتی هشدار می‌دهد. ابزارهای اضافی دیگری که در جلوگیری از آلوده شدن به وبسایتهای مخرب می‌توانند به کاربران کمک کنند راهنمای دستی **Firefox** و در بخش [**Other Useful Mozilla Add-Ons**](firefox_addons) معرفی می شوند.

اولین مجموعه گزینه های مربوط به مرتب کردن امور ایمیل‌های ناخواسته و تحکیم وضعیت امنیتی در پنجره *Options - Security* قابل دسترس هستند و در همینجا می‌توان تنظیمات مربوط به هریک را انجام داد. برای دسترسی به آن‌ها لطفا مراحل زیر را انجام دهید:

**مرحله ۱**. برای فعال کردن پنجره گزینه ها **Tools > Options** را **انتخاب** کنید.

**مرحله ۲**. بر روی نمایه ![](/sbox/screen/thunderbird-en/26.png) **کلیک** کنید تا پنجره زیر فعال شود:

![](/sbox/screen/thunderbird-en/27.png)

*تصویر ۴: پنجره امنیت که برگه های مربوطه در آن مشاهده می شوند*


### برگه ایمیل‌های ناخواسته (Junk) ###

**مرحله ۱**. گزینه های مربوط به برگه Junk را همانکونه که در *تصویر ۴* در بالا دیده می‌شود علامت بزنید تا برنامه **Thunderbird** را قادر سازد که ایمیل‌هایی را که از نظر شما به عنوان Junk تعیین شده اند، پاک کند. تنظیمات دیگر مربوط به ایمیل‌های ناخواسته در بخش‌های بعدی این فصل شرح داده خواهند شد.


### برگه کلاهبرداری های ایمیلی (Email Scams)###

**مرحله ۱**. گزینه *Tell me if the message I'm reading is a suspected email scam* را علامت بزنید تا برنامه **Thunderbird** را قادر سازد که پیامهای مشکوک به کلاهبرداری را مورد تجزیه و تحلیل قرار دهد:

![](/sbox/screen/thunderbird-en/28.png)

*تصویر ۵: برگه Email Scams*


### برگه آنتی ویروس ###

**مرحله ۱**. بر روی برگه آنتی ویروس **کلیک** کنید تا پنجره زیر فعال شود:

![](/sbox/screen/thunderbird-en/29.png)

*تصویر ۶: برگه آنتی ویروس*

با استفاده از این گزینه به برنامه آنتی ویروس موجود در رایانه شما اجازه داده می‌شود تا ایمیل‌ها را در هنگام ورود اسکن و از سایر ایمیل‌ها جدا کند. اگر این گزینه غیرفعال باشد، ممکن است در صورت دریافت یک پیام آلوده، کل شاخه Inbox شما تحت قرنطینه قرار گیرد. 

**توجه**: فرض برآنست که یک برنامه آنتی ویروس خوب و فعال در رایانه شما نصب شده است. برای کسب اطلاعات بیشتر در مورد چگونگی نصب و تنظیم نرم‌افزار آنتی ویروس لطفاً به راهنمای  [**Avast**](avast) مراجعه کنید.


### برگه رمز عبور (Password) ###

**مرحله ۲**. بر روی برگه  Password **کلیک** کنید تا پنجره زیر درحالت فعال قرار گیرد:

![](/sbox/screen/thunderbird-en/30.png)

*تصویر ۷: برگه Password*

**نکته مهم**: قویا توصیه می‌کنیم که با استفاده از نرم افزارهای مخصوص از رمزهای عبور خود نهایت محافظت را به عمل بیاورید؛ لطفاً برای کسب اطلاعات بیشتر به راهنمای برنامه [**KeyPass**](keepass) مراجعه کنید.


**توجه**: گزینه های برگه  Password فقط در صورتی کار می‌کنند که گزینه *Remember password* را در صفحه *Mail Account Setup* در هنگام ثبت کردن اکانت های ایمیل خود در برنامه **Thunderbird** علامت زده باشید.


**مرحله ۱**. بر روی  ![](/sbox/screen/thunderbird-en/31.png) **کلیک** کنید تا پنجره زیر فعال شود:  

![](/sbox/screen/thunderbird-en/32.png)

*تصویر ۸: پنجره رمز عبورهای ذخیره شده*


پنجره رمز عبورهای ذخیره شده (Saved Passwords) به شما امکان می‌دهد تا تمامی رمزعبورهای مربوط به هر یک از اکانت های ایمیل خود را مشاهده یا حذف نمایید. برای اینکار و برای بالابردن میزان امنیت و حراست از حریم شخصی می‌توانید یک رمز عبور ارشد (Master Password) بوجود بیاورید و بدینترتیب تمامی رمزهای عبور اکانت های شما برای فرد یا افرادی که از گزینه های مربوط به رمز عبور برنامه  **Thunderbird** اطلاعی ندارند، غیرقابل دسترس می شود.

**مرحله ۳**. گزینه *Use a master password* را همانطور که در تصویر 7 مشاهده می‌کنید **علامت** بزنید تا دکمه *Change Master Password...* فعال شود.


**مرحله ۴**. بر روی ![](/sbox/screen/thunderbird-en/33.png) **کلیک** کنید تا پنجره زیر فعال شود:

![](/sbox/screen/thunderbird-en/34.png)

*تصویر ۹: پنجره تغییر رمز عبور ارشد*


**مرحله ۵**. یک رمز عبور نسبتا دشوار که فقط شما قادر به یاد آوردن باشید در کادر مربوطه **تایپ** کرده و بر روی ![](/sbox/screen/thunderbird-en/35.png) **کلیک** کنید تا آن را به عنوان رمز عبور ارشد خود تأیید کنید. بار بعدی که بر روی ![](/sbox/screen/thunderbird-en/33.png) **کلیک** می‌کنید صفحه زیر ظاهر می‌شود که از شما می‌خواهد تا رمز عبور ارشد خود را وارد کنید:

![](/sbox/screen/thunderbird-en/36.png)

تصویر ۱۰: صفحه وارد کردن رمز عبور


### برگه محتوای وب ###

کوکی متن بسیار کوچکی است که مرورگر وب از آن استفاده می‌کند تا وبسایت خاصی را شناسایی کرده و به رسمیت بشناسد. برگه محتوای وب (Web Content) به شما امکان می‌دهد تا مشخص نمایید که کوکی های مربوط به کدام وبلاگ، دریافت خبر، یا گروه خبری، قابل اعتماد و مطمئن هستند. 

**مرحله ۱**. بر روی برگه *Web Content* **کلیک** کنید تا پنجره زیر فعال شود:

![](/sbox/screen/thunderbird-en/37.png)

*تصویر ۱۱: برگه محتوای وب*

**مرحله ۲**  *I close Thunderbird* را در گزینه *:Keep until* **انتخاب** کنید تا تا هر بار که از برنامه **Thunderbird** خارج می شوید، کوکی های مزبور بسته شوند. 


<a name="3.4"></a>
### ۳.۴ چگونه می‌توان تنظیمات مربوط به فیلترکردن پیامهای زائد را انجام داد ###

نوع دوم فیلتر ایمیل‌های ناخواسته از طریق پنجره *Account Settings - Junks Settings* در دسترس قرار دارد. بصورت پیش فرض، این فیلترها در حالت غیرفعال قرار دارند، بنابراین در صورتی که می‌خواهید از آن‌ها استفاده کنید باید آن‌ها را بصورت فعال در آورید. هر بار که ایمیل‌های ناخواسته وارد شوند برنامه **Thunderbird** بصورت خودکار آن‌ها را در شاخه Junk مربوط به اکانت های مختلف قرار می دهد.

**مرحله ۱**. **Tools > Account Settings** را **انتخاب** کنید تا پنجره *Account Settings* (تنظیمات اکانت) فعال شود.

**مرحله ۲**. گزینه *Junk Settings* مربوط به یک اکانت **Gmail** یا **RiseUp** را که در کادر کناری صفحه دیده می‌شود **انتخاب** کنید.

**مرحله ۳**. گزینه های *Junk Settings* را **فعال** کنید، بدینترتیب صفحه *Account Settings - Junk Settings* شما مشابه تصویر زیر خواهد شد:

![](/sbox/screen/thunderbird-en/38.png)

*تصویر ۱۲: پنجره تنظیمات اکانت – تنظیمات ایمیل‌های ناخواسته*


**مرحله ۴**. بر روی ![](/sbox/screen/thunderbird-en/35.png) **کلیک** کنید تا تنطیمات پنجره *Account Settings* تکمیل شود.


**نکته**: تنظیمات گزینه های *Junk Settings* برای هر اکانت باید بصورت جداگانه انجام گیرد. بدینترتیب، ایمیل‌های ناخواسته مربوط به اکانت **Gmail** یا **RiseUp** در شاخه *Deleted* مربوط به هریک قرار داده می شوند. راه دیگر آنست که می‌توان یک … (شاخه محلی) را برای دریافت ایمیل‌های ناخواسته تمامی اکانت های ایمیل تعیین کرد.

![](/sbox/screen/thunderbird-en/39.png)
*تصویر ۱۳: پنجره Account Settings - Junk Settings  که تنظیمات یک  junk folder مرکزی در آن مشاهده می شود*

**مرحله ۱**. گزینه *Junk Settings* را که مستقیماً در زیر *Local Folders* در کادر کناری قرار دارد **انتخاب** کنید.

**مرحله ۲**. *Local Folders* را از فهرست کرکره ای *"Junk" folder on:*همانطور که در *تصویر 13* دیده می‌شود **انتخاب** کنید.

**مرحله ۳**. بر روی ![](/sbox/screen/thunderbird-en/35.png) **کلیک** کنید تا تنظیمات پنجره *Account Settings* کامل شود.

اکنون که گزینه های امنیتی و تنطیمات ایمیل‌های ناخواسته را در **Thunderbird** با موفقیت پیکربندی نمودید، لطفاً به بخش بعدی  [**چگونه می‌توان Enigmail را همراه با GnuPG در Thunderbird**](thuderbird_encryption) استفاده کرد مراجعه کنید.
