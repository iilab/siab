

---

lang: km
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 4
depth: 3
title: More Useful Firefox Add-Ons

---

បញ្ជីផ្នែកដែលមាននៅក្នុងទំព័រនេះ ៖ 

- [**៥.០ អំពី Add-ons (មុខងារបន្ថែម)**](#5.0)
- [**៥.១ របៀបប្រើ HTTPS ឱ្យបានគ្រប់កន្លែង**](#5.1)
- [**៥.២ របៀបប្រើ Adblock Plus**](#5.2)
- [**៥.៣ របៀបប្រើ Beef Taco (Targeted Advertising Cookies Opt-Out)**](#5.3)
- [**៥.៤ របៀបប្រើ Better Privacy (ភាពឯកជនដែលប្រសើរជាងមុន)**](#5.4) 
- [**៥.៥ Add-ons (មុខងារបន្ថែម) ផ្សេងទៀតដែលមានប្រយោជន៍**](#5.5)

-------

<a name="5.0"></a>
## ៥.០ អំពី Add-ons (មុខងារបន្ថែម) ##
**Mozilla Firefox Add-ons** (**មុខងារបន្ថែមសម្រាប់ Mozilla Firefox**) ដែលលើកមកបង្ហាញនៅក្នុងផ្នែកនេះ ត្រូវបានបង្កើតឡើងដើម្បីលើកកម្ពស់ ឬការពារអនាមិកភាព ភាពឯកជន និងសុវត្ថិភាពនៃវគ្គបើកទំព័រអ៊ីនធើរណែត(browsing sessions)របស់លោកអ្នក។ ដើម្បីដោនឡូតមុខងារបន្ថែមទាំងនេះ សូមមើលផ្នែក [**របៀបដោនឡូតកម្មវិធី Firefox**](/km/firefox_main)។

<a name="5.1"></a>
## ៥.១ របៀបប្រើ HTTPS ឱ្យបានគ្រប់កន្លែង ##

![](/sbox/screen/firefox-en-1/httpseverywherelogo.png)

**HTTPS Everywhere** គឺជាមុខងារបន្ថែម(extension)មួយសម្រាប់ **Mozilla Firefox** ដែលធានាថា លោកអ្នកប្រាស្រ័យទាក់ទងជាមួយបញ្ជីគេហទំព័រជាក់លាក់មួយ នៅលើបណ្តាញមានទម្រង់សម្ងាត់(*https*)មួយជានិច្ច។ ទោះបីគេហទំព័រជាច្រើនផ្តល់វិធីបម្លែងជាទម្រង់សម្ងាត់ក៏ដោយ ជាស្វ័យប្រវត្តដំបូង ពួកគេទំនងជាផ្តល់អាសយដ្ឋាន http ដែលមិនមានទម្រង់សម្ងាត់។ មុខងារបន្ថែម **HTTPS Everywhere** ដោះស្រាយបញ្ហាទាំងនេះ ដោយសរសេរឡើងវិញនូវរាល់សំណើទាំងអស់របស់លោកអ្នកដែលមានចំពោះគេហទំព័រទាំងនេះឱ្យទៅជាពិធីការ **HTTPS**។ វាដំណើរការយ៉ាងស្ងៀមស្ងាត់នៅក្នុងផ្ទៃខាងក្រោយ និងធានាថា វគ្គបើកអ៊ីនធើរណែត(Internet sessions)ជាមួយគេហទំព័រជ្រើសរើសទាំងនោះ គឺមានសុវត្ថិភាព។ ប៉ុន្តែ វាធ្វើការ*តែ*នៅពេលគេហទំព័រទាំងនោះកំពុងប្រើពិធីការ **HTTPS** ដោយខ្លួនឯងប៉ុណ្ណោះ។

បន្ទាប់ពីមុខងារបន្ថែម **HTTPS Everywhere** ត្រូវបានបញ្ចូលដោយជោគជ័យរួចហើយ ផ្ទាំងខាងក្រោមនេះនឹងលេចចេញមក៖ 

![](/sbox/screen/firefox-en-1/75.png)

*រូបភាព ១ ៖ ផ្ទាំងសំណួរ Should HTTPS Everywhere Use the SSL Observatory? (តើ HTTPS Everywhere គួរប្រើ SSL Observatoryដែរឬទេ?)* 

**ជំហានទី ១**. **ចុច**លើ ![](/sbox/screen/firefox-en-1/76.png) ដើម្បីបើកផ្ទាំងខាងក្រោមនេះ៖ 

![](/sbox/screen/firefox-en-1/77.png)

*រូបភាព ២ ៖ ផ្ទាំងSSL Observatory Preferences* 

**កំណត់សម្គាល់** ៖ ប្រសិនបើធ្លាប់មានការបញ្ចូលមុខងារ **HTTPS Everywhere** ពីលើកមុន នៅក្នុងកម្មវិធី**Firefox**របស់លោកអ្នក  ត្រូវ**ជ្រើសយក Tools > HTTPS Everywhere > SSL Observatory Preferences** និងពិនិត្យផ្ទៀងផ្ទាត់ថា ជម្រើស *Use the Observatory* (*ប្រើកន្លែងសង្កេត*) និងជម្រើស *When you see a new certificate, tell the Observatory which ISP you are connected to* (*នៅពេលលោកអ្នកឃើញមានវិញ្ញាបនបត្រថ្មីមួយ ត្រូវប្រាប់កន្លែងសង្កេតថា តើក្រុមហ៊ុនផ្តល់សេវា        អ៊ីនធើរណែតណាដែលលោកអ្នកកំពុងភ្ជាប់សេវាជាមួយ*) ត្រូវបានគូសយក។ ប្រសិនបើលោកអ្នកមិនកំពុងប្រើ **Tor** ទេនោះ ត្រូវ**ជ្រើសយក** ជម្រើស *Check certificates even if Tor is not available* (*ពិនិត្យផ្ទៀងផ្ទាត់វិញ្ញាបនបត្រ ទោះបីមិនមាន Tor ក៏ដោយ*) ផងដែរ។  

<a name="5.2"></a>
## ៥.២ របៀបប្រើ Adblock Plus ##

![](/sbox/screen/firefox-en-1/adblockpluslogo.png)

**Adblock Plus** គឺជាមុខងារបន្ថែមប្រើសម្រាប់ច្រោះខ្លឹមសារមួយ (a content filtering extension) ដែលបង្កើតឡើង ដើម្បីកំណត់និងដាក់កម្រិតសមត្ថភាពរបស់ផ្ទាំងផ្សាយពាណិជ្ជកម្មក្នុងការបង្ហាញខ្លួនដោយខ្លួនឯង។ 

បន្ទាប់ពី **Adblock Plus** ត្រូវបានបញ្ចូលដោយជោគជ័យរួចហើយ ទំព័រខាងក្រោមនេះនឹងត្រូវបានបើក៖
[**chrome://adblockplus/content/ui/firstRun.html**](chrome://adblockplus/content/ui/firstRun.html)
 
![](/sbox/screen/firefox-en-1/60.png)

*រូបភាព ៣ ៖ ទំព័រ Adblock Plus chrome content page*

**ជំហានទី ១**. **ចុច**លើ ![](/sbox/screen/firefox-en-1/61.png) ដើម្បីឱ្យវាប្តូរទៅជា ![](/sbox/screen/firefox-en-1/62.png) សម្រាប់ជម្រើស *Malware Blocking* (*បំបិទម៉ាលវែរ*), *Remove Social Media Buttons* (*ប៊ូតុងលុបចោលបណ្តាញទំនាក់ទំនងសង្គម*) និង *Disable Tracking* (*បិទចោលការតាមដាន*) (ដូចដែលបង្ហាញនៅក្នុង *រូបភាព ១* ខាងលើ)។

**ជំហានទី ២**. **ជ្រើសយក Tools > Adblock Plus > Filter preferences...** ដើម្បីបើកផ្ទាំងខាងក្រោមនេះ៖

![](/sbox/screen/firefox-en-1/63.png)

*រូបភាព ៤ ៖ ផ្ទាំង Add Adblock Plus Filter Preferences ដែលបង្ហាញជម្រើសជាវតម្រង (filter subscriptions) ចំនួនបី*

**ជំហានទី ៣**. **ចុច**លើប្រអប់គូសជាវតម្រង (filter subscription) នីមួយៗ ដើម្បីជ្រើសយកវា (ដូចដែលបង្ហាញនៅក្នុង *រូបភាព ២* ខាងលើ) បន្ទាប់មក **លែងជ្រើសយក**ជម្រើស ![](/sbox/screen/firefox-en-1/64.png) ដើម្បីរារាំង*គ្រប់*ការផ្សាយពាណិជ្ជកម្មដែលត្រូវបានបរិយាយ ឬរាយឈ្មោះនៅក្នុងតម្រងទាំងនេះមិនឱ្យបង្ហាញខ្លួនបាន។

**ជំហានទី ៤**. ប្រសិនបើលោកអ្នកធ្វើការដោយប្រើភាសាច្រើន ត្រូវ**ចុច**លើ ![](/sbox/screen/firefox-en-1/65.png) ដើម្បីមើលការជាវតម្រង(filter subscription)ផ្សេងៗ បន្ទាប់មក **ចុច**លើ ![](/sbox/screen/firefox-en-1/66.png) ដើម្បីបើកបញ្ជីទម្លាក់មួយដែលមានតម្រងសម្រាប់ជាវផ្សេងៗ  រួច **ជ្រើសយក**ជម្រើសដែលសមស្រប បន្ទាប់មក **ចុច**លើ  ![](/sbox/screen/firefox-en-1/67.png)។

**ជំហានទី ៥**. ដើម្បីធ្វើបច្ចុប្បន្នភាពការជាវតម្រង(filter subscriptions)របស់លោកអ្នក ត្រូវ**ចុច**លើ ![](/sbox/screen/firefox-en-1/68.png) បន្ទាប់មក **ជ្រើសយក** ជម្រើស *Update filters* (*ធ្វើបច្ចុប្បន្នភាពតម្រង*) ពីម៉ឺនុយPop-up (pop-up menu)។

<a name="5.3"></a>
## ៥.៣ របៀបប្រើ Beef Taco (Targeted Advertising Cookies Opt-Out) ##

![](/sbox/screen/firefox-en/beeftacologo.png)

**Beef Taco** គឺជាមុខងារបន្ថែមមួយសម្រាប់ **Mozilla Firefox** ដែលអាចឱ្យលោកអ្នកគ្រប់គ្រងឃុកឃី(Cookies)ដែលទាក់ទងការផ្សាយពាណិជ្ជកម្មពីក្រុមហ៊ុនផ្សេងៗជាច្រើន ដែលក្នុងចំណោមនោះមានក្រុមហ៊ុន **Google**, **Microsoft** និង**Yahoo**។ លោកអ្នកអាចកំណត់មុខងារឱ្យវាលុបចោលដោយស្វ័យប្រវត្ត នូវឃុកឃី(Cookies)ដែលត្រូវបានស្គាល់ថាជា **Targeted Advertising Cookies Opt-Out**។ ប៉ុន្តែ វាក៏អនុញ្ញាតឱ្យអ្នកប្រើប្រាស់ដែលមាន **កម្រិតមានបទពិសោធន៍** និង **កម្រិតខ្ពស់** អាចកំណត់បានច្បាស់លាស់ក្នុងរបៀបលម្អិតជាងមុនថា តើឃុកឃី(Cookies)ណាខ្លះដែលអនុញ្ញាតឱ្យស្ថិតនៅក្នុងប្រព័ន្ធកុំព្យូទ័ររបស់លោកអ្នក និងឃុកឃី(Cookies)ណាខ្លះដែលត្រូវលុបចោល។

<a name="5.4"></a>
## ៥.៤ របៀបប្រើ Better Privacy (ភាពឯកជនដែលប្រសើរជាងមុន) ##

![](/sbox/screen/firefox-en-1/betterprivacylogo.png)

**Better Privacy** គឺជាមុខងារបន្ថែមមួយសម្រាប់ **Mozilla Firefox**។ មុខងារបន្ថែមនេះ ជួយការពារប្រព័ន្ធកុំព្យូទ័ររបស់លោកអ្នកពីឃុកឃី(Cookies)ពិសេសមួយមានឈ្មោះថា **LSO** (**Local Shared Objects**) ដែលគេអាចដាក់ទៅក្នុងកុំព្យូទ័ររបស់លោកអ្នកបានដោយសំណេរកម្មវិធី **Flash** មួយ។ ឃុកឃី(Cookies)ទាំងនេះ មិនត្រូវបានលុបចោលដោយនីតិវិធី សម្អាតឃុកឃី(Cookies)ស្តង់ដាររបស់កម្មវិធី **Firefox** ទេ។

<a name="5.5"></a>
## ៥.៥ Add-ons (មុខងារបន្ថែម) ផ្សេងទៀតដែលមានប្រយោជន៍ ##
ផ្នែកនេះ បរិយាយអំពីមុខងារបន្ថែម(add-ons, extensions)មានប្រយោជន៍មួយចំនួន ដែលមានលក្ខណៈសេរីនិងបើកចំហ (ឬដែលកំពុងស្ថិត នៅក្នុងដំណើរការក្លាយជាមានលក្ខណៈសេរី និងបើកចំហ) ដែលអាចលើកកម្ពស់ និងពង្រីកសមត្ថភាពរបស់លោកអ្នក ក្នុងការបើកប្រើអ៊ីនធើរណែតបានក្នុងលក្ខណៈឯកជន និងមានសុវត្ថិភាព។

### ៥.៥.១ Cryptocat ###

[![](/sbox/screen/firefox-en-1/cryptocatlogo.png)](https://addons.mozilla.org/en-us/firefox/addon/cryptocat/)

**Cryptocat** គឺជាមុខងារបន្ថែមផ្នែកសេវាផ្ញើសាររហ័សក្នុងលក្ខណៈឯកជន និងមានទម្រង់សម្ងាត់បើកចំហមួយ ដែលធ្វើការនៅក្នុងកម្មវិធីបើកអ៊ីនធើរណែតរបស់លោកអ្នក។ ដោយហេតុនេះហើយ នៅក្នុងស្ថានភាពមួយចំនួន វាអាចងាយស្រួលប្រើប្រាស់ជាងកម្មវិធីសន្ទនាជាអក្សរដែលអាចប្រៀបធៀបគ្នាបានផ្សេងទៀត។ **Cryptocat** អាចឱ្យលោកអ្នកបង្កើតបន្ទប់សន្ទនាជាក់ស្តែងមួយ ដែលនៅក្នុងនោះលោកអ្នកអាចសន្ទនាជាមួយគ្រប់សមាជិកទាំងអស់ ឬអាចមានការសន្ទនាឯកជនមួយទល់មួយ ជាមួយអ្នកចូលរួមនីមួយៗ។ គ្រប់ការសន្ទនាទាំងអស់ ត្រូវបានបម្លែងជាទម្រង់សម្ងាត់ និងស្រាយទម្រង់សម្ងាត់នៅក្នុងកម្មវិធីបើកអ៊ីនធើរណែតរបស់អ្នកប្រើប្រាស់ មុននឹងផ្ញើចេញ និងបន្ទាប់ពីបានទទួល។ **Cryptocat** មានជាមុខងារបន្ថែម(extension)សម្រាប់កម្មវិធីបើកអ៊ីនធើរណែត **Mozilla Firefox**, **Google Chrome** និង **Apple Safari** និងមានជា **Mac OS X** app ផងដែរ។ [**សូមអានបន្ថែម…**](https://crypto.cat/)

### ៥.៥.២ Disconnect ###

[![](/sbox/screen/firefox-en-1/disconnectmelogo.png)](https://addons.mozilla.org/en-us/firefox/user/disconnect/)

**Disconnect** ត្រូវបានបង្កើតឡើង ដើម្បីរក្សាទិន្នន័យរបស់លោកអ្នកឱ្យមានសុវត្ថិភាពពីកម្មវិធីតាមដានអ៊ីនធើរណែតភាគីទីបី ហើយស្របពេលជាមួយគ្នានោះ ធ្វើការវិភាគលើកម្មវិធីតាមដានអ៊ីនធើរណែត និងបែងចែកកម្មវិធីទាំងនោះជាក្រុម ឧទា.ដូចជា កម្មវិធីផ្សាយពាណិជ្ជកម្ម កម្មវិធីវិភាគ និងកម្មវិធីសង្គម ជាដើម។ [**សូមអានបន្ថែម…**](https://www.disconnect.me/)

### ៥.៥.៣ DuckDuckGo ###

[![](/sbox/screen/firefox-en-1/duckduckgologo.png)](https://addons.mozilla.org/en-US/firefox/addon/duckduckgo-ssl/)

**DuckDuckGo** ត្រូវបានបង្កើតឡើង ដើម្បីផ្តល់ជាជម្រើសផ្សេងមួយដែលមានលក្ខណៈឯកជន និងមានសុវត្ថិភាព ក្រៅពីម៉ាស៊ីនស្វែងរករបស់អ៊ីនធើរណែត(Internet search engine)ដែលមានដូចជា **Google** ឬ **Bing**ជាដើម។ **DuckDuckGo** មិនកត់ត្រាទុកនិងចែករំលែកព័ត៌មានរបស់អ្នកប្រើប្រាស់ទេ ហើយអ្នកប្រើប្រាស់ទាំងអស់មានសិទ្ធិប្រើប្រាស់ព័ត៌មានដូចៗគ្នា។ លោកអ្នកអាចបើកចូលគេហទំព័រ [**DuckDuckGo**](https://duckduckgo.com/) បានដោយផ្ទាល់ ឬ **ចុច**លើរូបសញ្ញា **DuckDuckGo** ដើម្បីតម្លើងវាជាម៉ាស៊ីនស្វែងរកដែលមានជាស្វ័យប្រវត្តនៅក្នុងរបាស្វែងរក។

### ៥.៥.៤ vtzilla ###

[![](/sbox/screen/firefox-en-1/vtzillalogo.png)](https://addons.mozilla.org/en-us/firefox/addon/vtzilla/)

**vtzilla** គឺជាមុខងារបន្ថែម(extension)មួយសម្រាប់ **Mozilla Firefox** ដែលបង្កើតឡើងដើម្បីស្គែនការដោនឡូត និងគេហទំព័ររកម៉ាលវែរនិងមេរោគ។ បន្ទាប់ពីមុខងារបន្ថែម **vtzilla** ត្រូវបានបញ្ចូលដោយជោគជ័យរួចហើយ របាឧបករណ៍(toolbar)របស់ **vtzilla** (ដែលអាចចុចបើកនិងបិទបាន) លេចមកនៅខាងក្រោមរបាឧបករណ៍ Navigation Toolbar របស់ **Firefox**។ ដោយគ្រាន់តែថតចម្លងទៅដាក់ឬវាយបញ្ចូលនូវអាសយដ្ឋានអ៊ីនធើរណែតមួយ ចូលទៅក្នុងប្រអប់ស្វែងរករបស់ **vtzilla** ប៉ុណ្ណោះ    សំណើស្វែងរករបស់លោកអ្នកនឹងត្រូវបាននាំទៅកាន់គេហទំព័រ **Virus Total** ដែលជាគេហទំព័រមួយនាំកម្មវិធីស្គែនរកម៉ាលវែរឬមេរោគផ្សេងៗចំនួនជាងសែសិបមកកាន់តំណភ្ជាប់ ដឬគេហទំព័រជាក់លាក់។ ជាងនេះទៅទៀត **vtzilla**កាត់បន្ថយហានិភ័យនៃការឆ្លង ដោយការបន្ថែមនូវកម្រិតការពារមួយទៀតទៅឱ្យកម្មវិធីប្រឆាំងមេរោគដែលមានស្រាប់ (ឧទា. កម្មវិធី [**avast!**](https://securityinabox.org/km/avast_main)) និងដោយការស្គែនឯកសារដែលអាចដោនឡូតបានរបស់លោកអ្នក។ [**សូមអានបន្ថែម…**](https://www.virustotal.com/km/documentation/browser-extensions/)។

### ៥.៥.៥ ShareMeNot ###

[![](/sbox/screen/firefox-en-1/sharemenotlogo.png)](https://addons.mozilla.org/en-us/firefox/addon/sharemenot/)

**ShareMeNot** ត្រូវបានបង្កើតឡើង ដើម្បីរារាំងប៊ូតុងភាគីទីបី (ដូចជា ប៊ូតុង “Like” របស់ Facebook ឬ ប៊ូតុង “tweet” របស់ Twitter ជាដើម) ដែលត្រូវបានបង្កប់ដោយគេហទំព័រអ៊ីនធើរណែត មិនឱ្យតាមដានលោកអ្នកបាន លុះត្រាតែលោកអ្នកចុចលើពួកវាដោយពិតប្រាកដ។ [**សូមអានបន្ថែម …**](http://sharemenot.cs.washington.edu/)


### 5.5.6 Click&Clean ###

[![](/sbox/screen/firefox-en-1/clickcleanlogo.png)](https://addons.mozilla.org/en-US/firefox/addon/clickclean/) 

**Click&Clean** ត្រូវបានបង្កើតឡើង ដើម្បីលុបចោលទិន្នន័យឯកជនដោយស្វ័យប្រវត្ត បន្ទាប់ពីបិទកម្មវិធី **Firefox**។ កិច្ចការនេះរួមមាន ការសម្អាតប្រវត្តិដោនឡូតឯកសាររបស់លោកអ្នក ការលុបចោលប្រវត្តិបើកទំព័រអ៊ីនធើរណែត និងការលុបចោលឃុកឃី(Cookies) រួមទាំង **Flash Local Shared Objects** (**LSO**)។ វាលុបចោលឯកសារបណ្តោះអាសន្ន និងសម្អាតកន្លែងលាក់ ទុកមូលដ្ឋាន(Local Cache)របស់លោកអ្នកផងដែរ។

**កំណត់សម្គាល់** ៖ តាមរបៀបផ្សេងពីនេះ អ្នកប្រើប្រាស់ក៏អាចគិតគូរប្រើប្រាស់កម្មវិធីក្រៅផងដែរ ដូចជាកម្មវិធី [**CCleaner**](https://securityinabox.org/km/ccleaner_main), **Wise Disk Cleaner** ជាដើម សម្រាប់ប្រព័ន្ធប្រតិបត្តិការ **Windows** ឬ កម្មវិធី **Janitor** ឬ **BleachBit** សម្រាប់ប្រព័ន្ធប្រតិបត្តិការ **Linux**។

