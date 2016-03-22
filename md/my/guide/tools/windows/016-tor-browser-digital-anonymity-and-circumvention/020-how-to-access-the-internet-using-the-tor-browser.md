

---

lang: my
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to access the Internet using the Tor Browser

---

ဒီစာမ်က္ႏွာမွာ ပါဝင္တဲ့ အပိုင္းမ်ား -

- [**၃.၀ Tor Network သုံးစြဲျခင္း အေၾကာင္း**](#3.0)
- [**၃.၁ Tor Network ကို ဆက္သြယ္နည္း**](#3.1)
- [**၃.၂ Tor ကုိ ဆက္သြယ္တဲ့လုိင္းကုိ ကုိယ္တုိင္ စစ္ေဆး အတည္ျပဳနည္း**](#3.2)
- [**၃.၃ Tor ကုိ သုံးၿပီး Internet ကုိ ေလွာ္လွန္နည္း**](#3.3)
- [**၃.၃.၁ Mozilla Firefox ကုိ Tor နဲ႔ အသုံးျပဳဖုိ႔ Configure လုပ္နည္း**](#3.3.1)
- [**၃.၃.၂ Internet Explorer ကုိ Tor နဲ႔ အသုံးျပဳဖုိ႔ Configure လုပ္နည္း**](#3.3.2)

-------

<a name="3.0"></a>
## ၃.၀ Tor Network သုံးစြဲျခင္း အေၾကာင္း ##

အင္တာနက္ကုိ အမည္၀ွက္ျပီး စသုံးဖုိ႔၊ **Tor Browser** ကုိ ဖြင့္ဖုိ႔ လုိတယ္။ ပထမဆုံးအေနနဲ႔ ကြန္ပ်ဴတာနဲ႔ **Tor** network ကုိ ဆက္သြယ္ရမွာ ျဖစ္တယ္။ ကြန္ပ်ဴတာက **Tor** network ကုိ ေအာင္ေအာင္ျမင္ျမင္ ဆက္သြယ္ျပီးတဲ့အခါ၊ **Tor Browser** ဟာ **Tor Browser Bundle** ပါတဲ့ **အိတ္ေဆာင္ Firefox** ကုိ အလုိအေလ်ာက္ သီးသန္႔ ဖြင့္ေပးမွာ ျဖစ္ပါတယ္။

**မွတ္ခ်က္** - အမည္၀ွက္တည္ရွိမႈနဲ႔ အင္တာနက္ အျမန္ႏႈန္းတုိ႔ၾကား အေပးအယူ တခု ရွိေနတယ္။ **Tor** က အမည္၀ွက္ အင္တာနက္ သုံးစြဲမႈကုိ လုပ္ေဆာင္ေပးတဲ့အတြက္၊ ကြန္ပ်ဴတာဟာ တျခား web browser ကုိ အသုံးျပဳတာထက္ ပုိျပီး ေႏွးေကြးသြားလိမ့္မယ္။ **Tor** ဟာ သင့္ရဲ႕ privacy နဲ႔ လုံျခဳံေရးကို အကာအကြယ္ေပးဖုိ႔ သင္သြားတဲ့ လမ္းေၾကာင္းကုိ ေစတနာျဖစ္ အသုံးခံေနၾကတဲ့ ကြန္ပ်ဴတာေတြကဆင့္ ကမၻာအႏွံ႔ကုိ ျဖန္႔က်က္သြားပါတယ္။

<a name="3.1"></a>
## ၃.၁ Tor Network ကို ဆက္သြယ္နည္း ##

**Tor** network ကုိ ခ်ိတ္ဆက္ဖုိ႔၊ ေအာက္ပါ အဆင့္ေတြကုိ လုပ္ေဆာင္ပါ -

**အဆင့္ ၁**။ *Tor Browser* ပါတဲ့ ဖုိင္တြဲကုိ **ေနရာခ်**ပါ၊ အဲဒီေနာက္ ေအာက္ပါ မ်က္ႏွာျပင္ကုိ သက္၀င္ေစဖုိ႔ ![](/sbox/screen/tor-my/30.png) ကုိ **ႏွစ္ခ်က္ ႏွိပ္**ပါ -

![](/sbox/screen/tor-my/24.png)

*ပုံ ၁ - Tor network ကုိ ဆက္သြယ္ေနတဲ့ Vidalia Control Panel ျပပံု*

*Vidalia Control Panel* က **Tor** network ကုိ ခ်ိတ္ဆက္ဖုိ႔ စတင္တဲ့အခါ၊ ေအာက္က *System Tray* ထဲမွာ အ၀ါေရာင္ ၾကက္သြန္ပုံနဲ႔ တူတဲ့ ![](/sbox/screen/tor-en/31.png) icon ေပၚလာလိမ့္မယ္။ ကြန္ပ်ဴတာနဲ႔ **Tor** network တုိ႔ ေအာင္ေအာင္ျမင္ျမင္ ခ်ိတ္ဆက္ျပီးတာနဲ႔ icon ေလးဟာ အစိ္မ္းေရာင္ ![](/sbox/screen/tor-en/32.png) ေျပာင္းသြားပါလိမ့္မယ္။

**မွတ္ခ်က္** - *Vidalia Control Panel* ကုိ ထိထိေရာက္ေရာက္ အသုံးျပဳနည္းကုိ ေလ့လာဖုိ႔ [**Vidalia Control Panel ကုိ သုံးစြဲနည္း**](/my/tor_vidaliacontrol) စာမ်က္ႏွာကုိ သြားပါ။ 

ခဏအၾကာမွာ၊ **Tor Browser** က ေအာက္မွာ ျပထားတဲ့အတုိင္း **Mozilla Firefox** browser ကုိ သက္၀င္လာေစမွာ ျဖစ္ပါတယ္ -

![](/sbox/screen/tor-my/33.png)

*ပုံ ၂ - Are you using Tor? tab ကုိ ျပသေနတဲ့ Mozilla Firefox ျပပုံ*
 
**Tor Browser** ပရုိဂရမ္ကုိ ဖြင့္တဲ့အခါတုိင္း၊ *Vidalia Control Panel* (*ပုံ ၁*) နဲ႔ [**https://check.torproject.org/**](https://check.torproject.org/) (*ပုံ ၂*) မ်က္ႏွာျပင္ေတြကုိ အလိုအေလ်ာက္ ဖြင့္လာမွာ ျဖစ္တယ္။ **Torbutton** add-on ![](/sbox/screen/tor-my/34.png) ဟာ မ်က္ႏွာျပင္ရဲ႕ ေအာက္ေျခ ညာဖက္ေထာင့္မွာ ေပၚလာမွာ ျဖစ္ပါတယ္ 

**မွတ္ခ်က္** - ဒါေပမဲ့၊ အကယ္လုိ႔ **Tor Browser** ကုိ ဖြင့္တဲ့အခါ **Mozilla Firefox** browser ကုိ ဖြင့္ထားႏွင့္ၿပီ ဆုိရင္၊ **Torbutton** ![](/sbox/screen/tor-my/35.png) ဟာbrowser ၀င္းဒုိးရဲ႕ တေနရာမွာ disabled mode အတုိင္း ေပၚေနမွာ ျဖစ္ပါတယ္။

**Torbutton** ဟာ **Tor** network ကို စနစ္တက် ဆက္သြယ္ႏုိင္ဖို႔ **Firefox** ကုိ configure လုပ္ထားေလ့ ရွိတယ္။ enabled နဲ႔ disabled အေနအထားေတြကုိ ေျပာင္းဖုိ႔ **Torbutton** ကုိ **ႏွိပ္**လုိက္ပါ။  

ဒါေပမဲ့၊ အကယ္လုိ႔ သင္ဟာ **Tor** network ကုိ ခ်ိတ္ဆက္မထားဘူး ဆုိရင္၊ **Torbutton** ဟာ disabled ျဖစ္သြားမွာ ျဖစ္ျပီး၊ ေအာက္ပါ မ်က္ႏွာျပင္ေပၚလာလိမ့္မယ္ -

![](/sbox/screen/tor-my/36.png)

*ပုံ ၃ - Sorry. You are not using Tor tab ကုိ ျပသေနတဲ့ Mozilla Firefox ျပပုံ*

အကယ္လုိ႔ သင္ဟာ *ပုံ ၃*ထဲမွာ disable လုပ္ထားတဲ့ **Torbutton** (despite your efforts to enable it)၊ (သုိ႔) ကြန္ရက္စာမ်က္ႏွာ အလြတ္ကုိ ေတြ႔ရတယ္ ဆုိရင္၊ အခန္း [**၄.၀ Tor ထဲမွ ၾကဳံေတြ႔ေလ့ရွိတဲ့ ျပႆနာမ်ားကုိ ေျဖရွင္းနည္း**](/my/tor_vidaliacontrol) ကုိ ဖတ္ရႈပါ။ 

<a name="3.2"></a>
## ၃.၂ Tor ကုိ ဆက္သြယ္တဲ့လုိင္းကုိ ကုိယ္တုိင္ စစ္ေဆး အတည္ျပဳနည္း ##

**Tor** network ကုိ ခ်ိတ္ဆက္ေနတယ္ မခ်ိတ္ဆက္ထားဘူး ဆုိတာ စစ္ေဆးႏုိင္ဖုိ႔၊ ေအာက္ပါ အဆင့္ကုိ လုပ္ေဆာင္ပါ -

**အဆင့္ ၁**။ [**https://check.torproject.org/**](https://check.torproject.org/) ကြန္ရက္ စာမ်က္ႏွာကုိ **ဖြင့္**ပါ။ သူက သင္ဟာ **Tor** network ကုိ ခ်ိတ္ဆက္ေနတယ္ မခ်ိတ္ဆက္ထားဘူး ဆုိတာကုိ အတည္ျပဳေပးလိမ့္မယ္။

အကယ္လုိ႔ web browser ဟာ အင္တာနက္ကတဆင့္ **Tor** network ကုိ ဆက္သြယ္ထားတယ္ ဆုိရင္၊ သင္ေနထုိင္တဲ့ ႏုိင္ငံမွာ ပိတ္ဆုိ႔ (သိ႔ု) တားျမစ္ထားတဲ့ ကြန္ရက္ စာမ်က္ႏွာေတြကုိ ၾကည့္ရႈလုိ႔ ရမွာ ျဖစ္ျပီး၊ သင့္ရဲ႕ အြန္လုိင္း လုပ္ေဆာင္မႈေတြလည္း သီးသန္႔ရွိၿပီး လုံျခဳံမႈ ရွိေနမွာ ျဖစ္တယ္။ **www.google.com** လုိ ကြန္ရက္ စာမ်က္ႏွာေတြကုိလည္း တျခားႏုိင္ငံကေန အသုံးျပဳေနသလုိ ျပဳမႈေနမွာ ျဖစ္တယ္။ ဒါဟာ **Tor** ရဲ႕ သာမန္ လုပ္ေဆာင္ခ်က္ ျဖစ္ပါတယ္။

<a name="3.3"></a>
## ၃.၃ Tor ကုိ သုံးၿပီး Internet ကုိ ေလွာ္လွန္နည္း ##

**Tor** network ကတဆင့္ **Firefox** ကုိ အသုံးျပဳၿပီး ကြန္ရက္ စာမ်က္ႏွာေတြကုိ ခ်က္ျခင္း ၾကည့္ရႈႏုိင္ေပမဲ့၊ အြန္လုိင္း Privacy နဲ႔ လုံၿခံဳေရး ပုိေကာင္းေအာင္ **Firefox** ကုိ configure လုပ္တဲ့နည္းနဲ႔ ပါတ္သက္တဲ့ ေအာက္ပါ အခန္းကုိ ဖတ္ရႈဖုိ႔ အႀကံျပဳလုိပါတယ္။

<a name="3.3.1"></a>
## ၃.၃.၁ Mozilla Firefox ကုိ Tor နဲ႔ အသုံးျပဳဖုိ႔ Configure လုပ္နည္း ##

**Torbutton** ဟာ **Mozilla Firefox** ရဲ႕ add-on (သုိ႔) extension တခု ျဖစ္တယ္၊ ေသးငယ္တဲ့ ပရုိဂရမ္ တခုျဖစ္ၿပီး **Mozilla Firefox** မွာ ရွိတဲ့ အားနည္းခ်က္ တခ်ိဳ႕ကုိ ပိတ္ဆုိ႔ျခင္းျဖင့္ အြန္လုိင္း လုပ္ေဆာင္မႈေတြကုိ အမည္၀ွက္ၿပီး လုံၿခံဳေစဖုိ႔ စီစဥ္ထုတ္လုပ္ထားပါတယ္။

**အေရးႀကီးခ်က္** - အႏၱရာယ္ ရွိတဲ့ ကြန္ရက္ စာမ်က္ႏွာေတြ (သုိ႔) **Tor** ဆာဗာတခုက သင့္အေနနဲ႔ **Tor** ကုိ အသုံးျပဳေနတဲ့အခ်ိန္မွာေတာင္ သင္ အသုံးျပဳေနတဲ့ အင္တာနက္ တည္ေနရာနဲ႔ အြန္လုိင္း လုပ္ေဆာင္မႈေတြနဲ႔ ပါတ္သက္တဲ့ အခ်က္အလက္ေတြကုိ ထုတ္ေဖၚႏုိင္တယ္။ ကံအားေလွ်ာ္စြာပဲ၊ **Torbutton** ရဲ႕ default configuration ဟာ အေတာ္ေလး လုံၿခံဳတယ္။ ဒါေပမဲ့၊ အြန္လုိင္း Privacy နဲ႔ လုံၿခံဳေရးကုိ သင့္ျမတ္ေအာင္ လုပ္ေဆာင္ဖုိ႔ ေအာက္မွာ ေဖၚျပထားတဲ့ settings ကုိ ျပင္ဆင္ဖို႔ အႀကံျပဳလုိပါတယ္။

**မွတ္ခ်က္** - Browser နဲ႔ ပါတ္သက္တဲ့ လုံၿခံဳေရး ျပႆနာေတြကုိ နက္နက္နဲနဲ နားလည္ထားတဲ့ **အဆင့္ျမင့္** သုံးစြဲသူေတြက အဲဒီ settings ေတြကုိ ေကာင္းမြန္ေအာင္ ျပန္ျပင္ႏုိင္ပါတယ္။

*Torbutton Preferences* ၀င္းဒုိးမွာ options အမ်ိဳးမ်ိဳးကုိ သတ္မွတ္ေပးႏုိင္တ့ဲ tabs သုံးမ်ိဳးရွိတယ္ -

- The **Proxy Settings** tab
- The **Security Settings** tab
- The **Display Settings** tab

**Torbutton** ကုိ disable လုပ္ထားတယ္ ျဖစ္ျဖစ္၊ (သုိ႔) enable လုပ္ထားတယ္ ျဖစ္ျဖစ္၊ *Torbutton Preferences*  ၀င္းဒုိးထဲ ၀င္ေရာက္ႏုိင္တယ္။ *Torbutton Preferences* ၀င္းဒုိးကုိ သက္၀င္ေစဖုိ႔၊ ေအာက္ပါ အဆင့္ေတြကုိ လုပ္ေဆာင္ပါ -

**အဆင့္ ၁**။ **Torbutton** ရဲ႕ menu ကုိ သက္၀င္ေစဖုိ႔ ေအာက္ပါအတုိင္း သူ႔ကုိ **ညာဖက္ ႏွိပ္**ပါ -

![](/sbox/screen/tor-my/37.png)

*ပုံ ၄ - Torbutton menu ျပပုံ*

**အဆင့္ ၂**။ ေအာက္ပါ မ်က္ႏွာျပင္ကုိ သက္၀င္ေစဖုိ႔ *Preferences...* item ကုိ **Select** လုပ္ပါ -

![](/sbox/screen/tor-my/38.png)

*ပုံ ၅ - Proxy Settings tab ကုိ ျပသေနတဲ့ Torbutton Preferences ၀င္းဒုိး ျပပုံ*

- The **Proxy Settings** tab

*Proxy Settings* tab ဟာ **Torbutton** ကုိ enable လုပ္ထားတဲ့အခ်ိန္မွာ **Firefox** က အင္တာနက္ကုိ ဘယ္လုိ ပုံစံနဲ႔ ဆက္သြယ္ရမယ္ ဆုိတာကုိ ထိန္းခ်ဳပ္ေပးတယ္။ ဒီ tab မွာ ဘယ္ကုိမွ် ေျပာင္းလဲစရာ မလုိပါဘူး။

- The **Security Settings** tab

Security Settings tab ဟာ အင္တာနက္ လုံၿခံဳေရးနဲ႔ web browsers ေတြ အေၾကာင္း နက္နက္နဲနဲ သိကၽြမ္းထားတဲ့ **အေတြ႔အႀကံဳ**ရွိၿပီး **အဆင့္ျမင့္**တဲ့ သုံးစြဲသူေတြအတြက္ စီစဥ္ထုတ္လုပ္ထားတာ ျဖစ္တယ္။ သူ႔ရဲ႕ default settings ဟာ ပ်မ္းမွ် သုံးစြဲသူအတြက္ အဆင့္ျမင့္တဲ့ လုံၿခံဳေရးကုိ ပ့ံပုိးေပးတယ္။ *လုံၿခံဳေရး Settings* ေတြကုိ အသုံးျပဳၿပီး **Torbutton** က browser history, cache memory, cookies နဲ႔ **Firefox** မွာ ရွိတဲ့ တျခား features ေတြကုိ စီမံခန္႔ခြဲမဲ့ ပုံစံေတြကုိ configure လုပ္ေပးပါတယ္။

![](/sbox/screen/tor-my/39.png)

*ပုံ ၆ - လုံၿခံဳေရး Settings tab ပုံ*

*Disable plugins during Tor usage* option ဟာ *ခဏတျဖဳတ္* enable လုပ္ဖုိ႔ လုိအပ္လာႏုိင္တဲ့ လုံၿခံဳေရး settings အနည္းစုထဲမွာ ပါ၀င္တယ္။ [**DailyMotion**](http://www.dailymotion.com/), [**The Hub**](http://hub.witness.org/) နဲ႔ [**YouTube**](http://www.youtube.com/) အပါအ၀င္ အြန္လုိင္း ဗြီဒီယုိေတြကုိ **Tor** ကတဆင့္ ၾကည့္ရႈဖုိ႔၊ *Disable plugins during Tor usage* option ကုိ **disable** လုပ္ထားဖုိ႔ လုိပါတယ္။

**မွတ္ခ်က္** - ယုံၾကည္ စိတ္ခ်ရတဲ့ ကြန္ရက္စာမ်က္ႏွာေတြရဲ႕ plugins ေတြကုိပဲ enable လုပ္ထားဖုိ႔ လုိတယ္။ အဲဒီ ကြန္ရက္စာမ်က္ႏွာေတြကုိ ၾကည့္ရႈၿပီးတဲ့အခါ၊ Security Settings tab ကုိ ျပန္သြားၿပီး၊ *Disable plugins during Tor usage* option ကုိ ေနာက္တခါ **enable** လုပ္ပါ။

*Security Settings* tab မွာ ရွိတဲ့ option တခုစီရဲ႕ တိက်တဲ့ လုပ္ေဆာင္ခ်က္နဲ႔ ပါတ္သက္တဲ့ အေသးစိတ္ အခ်က္အလက္ကုိ ေလ့လာဖုိ႔၊ [**Torbutton**](https://www.torproject.org/torbutton/) ကုိ သြားေရာက္ ဖတ္ရႈပါ။

- The **Display Settings** tab

*Display Settings* tab ကုိ အသုံးျပဳၿပီး **Firefox** ရဲ႕ status bar မွာ **Torbutton** ေပၚလာမဲ့ ![](/sbox/screen/tor-my/34.png) (သုိ႔) ![](/sbox/screen/tor-en/40.png) (သုိ႔) ![](/sbox/screen/tor-my/35.png) (သုိ႔) ![](/sbox/screen/tor-en/41.png) ပုံစံတခုခုကုိ ေရြးခ်ယ္ႏုိင္တယ္။ ဘယ္လုိ ေရြးခ်ယ္မႈမ်ိဳးကုိပဲ လုပ္လုပ္၊ ဒီဇုိင္းဖန္တီးထားတဲ့အတုိင္း အလုပ္လုပ္လာမွာ ျဖစ္ပါတယ္။

![](/sbox/screen/tor-my/42.png)

*ပုံ ၇ - Display Settings tab ျပပုံ*

**သိေကာင္းစရာ** - အင္တာနက္ အသုံးျပဳၿပီးတဲ့အခါ၊ ယာယီ အင္တာနက္ cache နဲ႔ cookies ေတြကုိ ေသေသခ်ာခ်ာ ပယ္ဖ်က္လုိက္ပါ။  **Firefox** ကုိ ဖြင့္ၿပီး **Tools > Clear Recent History...** ကုိ သြား၊ ေပၚလာတဲ့ မ်က္ႏွာျပင္မွာ ျမင္ေတြရတဲ့ options ေတြ အားလုံးကုိ **ေရြး**လုိက္ၿပီး *Clear Now* ခလုတ္ကုိ **ႏွိပ္**ပါ။ အေသးစိတ္ အခ်က္အလက္ကုိ [**Mozilla Firefox**](/my/firefox_privacy_and_security) နဲ႔ပါတ္သက္တဲ့ **လက္စြဲ လမ္းညႊန္** အခန္းမွာ သြားေရာက္ ဖတ္ရႈပါ။

**Torbutton** နဲ႔ပါတ္သက္ၿပီး အေသးစိတ္ အခ်က္အလက္ကုိ၊ [**Torbutton ရဲ႕ မၾကာခဏ ေမးေလ့ရွိတဲ့ ေမးခြန္းမ်ား**](https://www.torproject.org/torbutton/torbutton-faq.html.en) မွာ သြားေရာက္ ဖတ္ရႈပါ။

<a name="3.3.2"></a>
## ၃.၃.၂ Internet Explorer ကုိ Tor နဲ႔ အသုံးျပဳဖုိ႔ Configure လုပ္နည္း ##

**မွတ္ခ်က္** - **Tor** ကုိ ဘယ္ web browser မွာ မဆုိ အသုံးျပဳႏုိင္ဖုိ႔ စီစဥ္ထုတ္လုပ္ထားေပမဲ့၊ **Firefox** နဲ႔ **Tor** တုိ႔ဟာ ရန္လုိၿပီး အႏၱရာယ္ ျပဳတတ္တဲ့ အုပ္စုေတြက မေတြ႔ႏုိင္ေအာင္ ကာကြယ္ေပးႏုိင္တဲ့ အေကာင္းဆုံး ကိရိယာေတြ ျဖစ္ၾကတယ္။ **Internet Explorer** ဟာ ေနာက္ဆုံးအဆင့္မွာ အသုံးျပဳရမဲ့ browser တခု ျဖစ္ဖုိ႔ လုိပါတယ္။

ဒါေပမဲ့၊ **Internet Explorer** ကုိ လုံး၀ မလြဲသာ၊ မေရွာင္သာ အသုံးျပဳရမဲ့ အေျခအေနမ်ိဳးမွာ ေရာက္ေနတယ္ ဆုိရင္၊ ေအာက္ပါ အဆင့္ေတြကုိ လုပ္ေဆာင္ပါ -

**အဆင့္ ၁**။ **Internet Explorer** web browser ကုိ **ဖြင့္**ပါ။

**အဆင့္ ၂**။ *Internet Options* မ်က္ႏွာျပင္ကုိ သက္၀င္ေစဖုိ႔ **Tools > Internet Options** ကုိ **Select** လုပ္ပါ။

**အဆင့္ ၃**။ ေအာက္က *ပုံ ၈* မွာ ျပထားတဲ့ မ်က္ႏွာျပင္ကုိ သက္၀င္ေစဖုိ႔ *Connections* tab ကုိ **ႏွိပ္**ပါ -

![](/sbox/screen/tor-en/43.png)

*ပုံ ၈ - Internet Options မွာ ေတြ႔ရတဲ့ Connections tab မ်က္ႏွာျပင္ ျပပုံ*

**အဆင့္ ၄**။ ေအာက္မွာ ျပထားတဲ့အတုိင္း *Local Area Network (LAN) Settings* မ်က္ႏွာျပင္ကုိ သက္၀င္ေစဖုိ႔ ![](/sbox/screen/tor-my/44.png) ကုိ **ႏွိပ္**ပါ -

![](/sbox/screen/tor-en/45.png)

*ပုံ ၉ - Local Area Network (LAN) Settings ျပပုံ*

**အဆင့္ ၅**။ *ပုံ ၉* မွာ ျပထားတဲ့အတုိင္း *Use a proxy server...* option ကုိ *Check* လုပ္ပါ။ အဲဒီေနာက္ *Proxy Settings* မ်က္ႏွာျပင္ကုိ သက္၀င္ေစဖုိ႔ ![](/sbox/screen/tor-my/46.png) **ႏွိပ္**ပါ။

**အဆင့္ ၆**။ ေအာက္မွာ ျပထားတဲ့အတုိင္း proxy settings အတြက္ ကြက္လပ္ေတြကုိ **ျဖည့္**ေပးပါ -

![](/sbox/screen/tor-my/47.png)

*ပုံ ၁၀ - အၿပီး ျဖည့္စြတ္ထားတဲ့ Proxy Settings မ်က္ႏွာျပင္ ဥပမာ ျပပုံ*

**အဆင့္ ၇**။ **Internet Options** ၀င္းဒုိးကုိ ပိတ္ၿပီး **Internet Explorer** browser ကုိ ျပန္သြားဖုိ႔၊ အလ်င္ေပၚလာတဲ့ configuration မ်က္ႏွာျပင္ေတြကုိ တခုခ်င္းကုိ ![](/sbox/screen/tor-my/07.png) **ႏွိပ္**လုိက္ပါ။

**မွတ္ခ်က္** - **Tor** ကုိ အသုံးမျပဳေတာ့ဘူး ဆုိရင္ **အဆင့္ ၁ ကေန ၄** အထိ ထပ္ခါတလဲလဲ လုပ္ပါ။ **အဆင့္ ၅** ေနရာမွာ၊ *Use a proxy server...* option ကုိ **disable** လုပ္ပါ။

**သိေကာင္းစရာ** - အင္တာနက္ကုိ အသုံးျပဳၿပီးတဲ့အခါ၊ ေအာက္ပါ အဆင့္ေတြကုိ လုပ္ၿပီး ယာယီ Internet cache, cookies နဲ႔ browser history ေတြကုိ ပယ္ဖ်က္ရမွာ ျဖစ္တယ္ -

**အဆင့္ ၁**။ ေအာက္ပါအတုိင္း *default General* tab ကုိ ေဖၚျပဖုိ႔ **Tools > Internet Options** ကုိ **Select** လုပ္ပါ -

![](/sbox/screen/tor-my/48.png)

*ပုံ ၁၁ - Internet Explorer General tab ျပပုံ*

**အဆင့္ ၂**။ *Delete Cookies* အတည္ျပဳ dialog box ကုိ ေအာက္ပါအတုိင္း သက္၀င္ေစဖုိ႔ *Temporary Internet files* အခန္းမွာ ![](/sbox/screen/tor-my/49.png) ကုိ **ႏွိပ္**ပါ၊ 

![](/sbox/screen/tor-my/50.png)

*ပုံ ၁၂ - Cookies ေတြကုိ ပယ္ဖ်က္ဖုိ႔ အတည္ျပဳခ်က္ေပးတဲ့ dialog box ျပပုံ*

**အဆင့္ ၃**။ ယာယီ အင္တာနက္ cookies ကုိ ပယ္ဖ်က္ဖုိ႔ ![](/sbox/screen/tor-my/07.png) ကုိ **ႏွိပ္**ပါ။

**အဆင့္ ၄**။ Delete Files အတည္ျပဳခ်က္ေပးတဲ့ dialog box ကုိ သက္၀င္ေစဖုိ႔ ![](/sbox/screen/tor-my/51.png) ကုိ **ႏွိပ္**ပါ။ အဲဒီေနာက္ ယာယီ အင္တာနက္ ဖုိင္ေတြကုိ ပယ္ဖ်က္ဖုိ႔ ![](/sbox/screen/tor-my/07.png) ကုိ **ႏွိပ္**ပါ။

**အဆင့္ ၅**။ Internet Options အတည္ျပဳခ်က္ ေပးတဲ့ dialog box ကုိ သက္၀င္ေစဖုိ႔ ![](/sbox/screen/tor-my/51.png) ကုိ **ႏွိပ္**ပါ၊ ![](/sbox/screen/tor-my/53.png) ကုိ **ႏွိပ္**ၿပီးတဲ့ေနာက္၊ ![](/sbox/screen/tor-my/07.png) ကုိ **ႏွိပ္**ပါ။

**မွတ္ခ်က္** - **Internet Explorer** ကုိ အသုံးျပဳၿပီး **Tor** network ထဲကုိ ၀င္ေရာက္ဖုိ႔၊ **Tor Browser** ဟာ **Vidalia** နဲ႔ ခ်ိတ္ဆက္ထားရမွာ ျဖစ္ၿပီး Tor network ထဲကုိ ၀င္ေရာက္ရမွာ ျဖစ္ပါတယ္။


