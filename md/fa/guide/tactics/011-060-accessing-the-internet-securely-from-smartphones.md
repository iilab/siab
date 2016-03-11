

---

lang: fa
community: guide
type: tactics
legacy: True
child: True
weight: 6
depth: 3
title: Accessing the Internet Securely from Smartphones

---

همانطور که در [***فصل ۷: چگونه می توان از حریم شخصی ارتباطات اینترنتی محافظت کرد***](chapter-7) و [***فصل ۸: چگونگی ناشناس ماندن و دورزدن سانسور انترنت***](chapter-8) شرح داده شده است دسترسی به محتویات اینترنتی، یا انتشار آیتم های آنلاین از قبیل عکس ها یا ویدئو ها، رد پاهای فراوانی از اینکه شما چه کسی هستید، در کجا بوده و مشغول چه کاری هستید، بر جای می گزارد.  به این ترتیب ممکن است موقعیت شما به خطر بیافتد.  استفاده از تلفن هوشمند برای ارتباط با اینترنت میزان ان خطر را افزایش می دهد.  

### دسترسی به اینترنت از طریق WiFi یا داده های تلفن همراه ###

تلفن های هوشمند به شما امکان می دهند تا نوع دسترسی به اینترنت را انتخاب کنید: از طریق ارتباط بیسیم با استفاده از نقطه دسترسی (مثلا یک کافه اینترنتی)، یا از طریق داده های تلفن همراه مانند GPRS، EDGE یا UMTS که از جانب اپراتور شبکه تلفن همراه فراهم می شود.  

استفاده از ارتباط WiFi از میزان ردپاهای داده هایی که ممکن است شما برای سرویس دهنده خدمات تلفن همراه باقی بگزارید می کاهد (بدلیل آنکه در این شرایط شما از امکان اینترنتی تلفن همراه خود که اشتراک آن به نام شماست استفاده نمی کنید).  با وجود این، گاهی اوقات تنها راه ارتباط برقرار کردن با اینترنت از طریق تلفن همراه میسر است.  متاسفانه، پروتکل های ارتباط از طریق داده های تلفن همراه ( مانند EDGE یا UMTS ) دارای استاندارد باز نیستند.  بنابراین، برنامه نویسان مستقل یا متخصصین امنیت اینترنتی نمی توانند این پروتکل ها را از بابت اینکه آنها چگونه توسط سرویس دهنده های داده تلفن همراه اجرا می شوند، مورد آزمایش قرار دهند.

در برخی کشورها، سرویس دهندگان خدمات اینترنت تلفن همراه از قواعد و قوانینی متفاوت از سرویس دهندگان خدمات اینترنتی پیروی می کنند، که ممکن است نتیجه آن اعمال شنودهای مستقیم توسط دولت ها و شبکه های خدمات دهنده شود.

صرف نظر از اینکه، چه روشی را برای ارتباطات دیجیتال خود از طریق تلفن هوشمند انتخاب می کنید، با استفاده از ابزارهای ناشناس سازی و رمزنگاری می توانید از میزان ریسک افشا شدن داده هایتان بکاهید.

### ناشناس سازی ###

برای آنکه بتوانید بطور ناشناس به محتویات آنلاین دسترسی پیدا کنید، می توانید از برنامه  [**Orbot**](https://www.torproject.org/docs/android.html.en) که منطبق با سیستم عامل اندروید می باشد استفاده کنید.  Orbot ارتباطات اینترنتی شما را درون کانال های شبکه ناشناس سازی Tor عبور می دهد.

<div class=getstarted markdown=1>
Hands-on: Get started with the [*Orbot Guide*](/en/Orbot_main)
</div>

یک برنامه کاربردی دیگر، برنامه Orweb است که در واقع نوعی مرورگر اینترنتی است که ویژگیهای امنیتی آن مانند استفاده ازپراکسی ها و عدم نگهداری سوابق بازدیدهای اینترنتی در آن ارتقاء یافته است.  برنامه های Orbot و Orweb با کمک یکدیگر فیلترهای وبی و دیوارهای آتش را دور زده، و امکان مرور اینترنت بصورت ناشناس را برای شما فراهم می آورند.

<div class=getstarted markdown=1>
Hands-on: Get started with the [*Orweb Guide*](/en/Orweb_main)
</div>

### پراکسی ها ###

نسخه [*Firefox*](glossary#Firefox) مخصوص تلفن همراه با نام  [**Firefox mobile**](http://f-droid.org/repository/browse/?fdid=org.mozilla.firefox)  را می توان به افزونه های پراکسی مجهز نمود، در اینصورت ترافیک داده های شما به یک سرور پراکسی انتقال داده شده و از آنجا به سایتی که مایل به بازدید آن هستید ارجاع داده می شود.  این امر در مواقعی که قصد عبور از سانسور را دارید مفید است، اما ممکن هنوز هم نوع درخواست شما را افشا کند مگر آنکه ارتباط برنامه مدیریت کننده اتصال اینترنتی شما به پراکسی رمزنگاری شده باشد.  ما افزونه [**Proxy Mobile**](https://guardianproject.info/apps/proxymob-firefox-add-on/) (که از محصولات  [پروژه Guardian ](https://guardianproject.info/) بوده و اتصال به پراکسی از طریق Firefox را آسان می کند) پیشنهاد می کنیم.  این روش همچنین تنها راه انتقال داده هایی که با استفاده از نسخه تلفن همراه Firefox رد و بدل می شوند به Orbot و استفاده از شبکه  [*Tor*](/en/glossary#Tor) می باشد. 
