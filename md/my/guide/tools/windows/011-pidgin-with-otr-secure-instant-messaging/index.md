

---

lang: my
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 011
title: Pidgin with OTR - Secure Instant Messaging

---

**ပင္မ စာမ်က္ႏွာ**

- **OTR**: [**www.cypherpunks.ca/otr**](http://www.cypherpunks.ca/otr/)

**ကြန္ပ်ဴတာ လုိအပ္ခ်က္မ်ား**

- အင္တာနက္လုိင္း တခု
- ၀င္းဒုိး ဗားရွင္း အားလုံး

**ဒီလမ္းညႊန္ခ်က္ထဲမွာ သုံးစြဲထားတဲ့ ဗားရွင္း**

- Pidgin 2.7.11
- OTR 3.2.0.1

**ခြင့္ျပဳခ်က္ လုိင္စင္ -**

- အခမဲ့ျပီး ပြင့္လင္းတဲ့ အရင္းအျမစ္ ေဆာ့ဗ္၀ဲ

**ဖတ္႐ႈရမဲ့ အေၾကာင္းအရာမ်ား -**

သုံးစြဲနည္း စာအုပ္ငယ္ အခန္း [**၇။ အင္တာနက္ ဆက္သြယ္မႈ လမ္းေၾကာင္းကုိ လ်ွိဳ႕၀ွက္ထားနည္း**](/my/chapter-7)

**အဆင့္ -** ၁။ လက္သင္၊ **၂။ ပ်မ္းမွ်**၊ ၃။ အလယ္အလတ္၊ ၄။ အေတြ႔အၾကံဳရွိေသာ၊ ၅။ အဆင့္ျမင့္

**ဒီေဆာ့ဗ္၀ဲကို စတင္ သံုးစြဲဖို႔ လိုအပ္တဲ့ အခ်ိန္ -** ၃၀ မိနစ္

**ျပန္လည္ရရွိမဲ့ အက်ိဳးေက်းဇူးမ်ား -**

- အလြန္ ေရပမ္းစားတဲ့ လက္ငင္း စာတုိပုိ႔ေရး ၀န္ေဆာင္မႈ တခ်ိဳ႕ကုိ ပရုိဂရမ္ တခုထဲမွာ စုစည္းထားၿပီး စီစဥ္ႏုိင္၊ စီမံခန္႔ခြဲႏုိင္တယ္
- သီးသန္႔ျဖစ္ၿပီး စစ္မွန္တဲ့ chat စကားေျပာဆုိမႈေတြကုိ ေဆာင္ရြတ္ႏုိင္တယ္

**GNU Linux, Mac OS နဲ႔ တျခား Microsoft Windows ေတြနဲ႔ လိုက္ဖက္တဲ့ ပ႐ိုဂရမ္မ်ား -**

**Pidgin** နဲ႔ **OTR** ႏွစ္မ်ိဳးစလုံးကုိ **Microsoft Windows** နဲ႔ **GNU/Linux** တုိ႔အတြက္ ရရွိႏိုင္တယ္။ **OTR** ကုိ ပံ့ပုိးမႈေပးတဲ့ **Microsoft Windows** ရဲ႕ တျခား multi-protocol **IM** ပရုိဂရမ္ကေတာ့ [**Miranda IM**](http://www.miranda-im.org/) ျဖစ္တယ္။ **Mac OS** မွာေတာ့ **OTR** plugin ကုိ ပံ့ပုိးမႈေပးတဲ့ multi-protocol IM ပရုိဂရမ္ တခု ျဖစ္တဲ့ [**Adium**](http://adium.im/) ကုိ အသုံးျပဳ ႏုိင္ပါတယ္။

##၁.၁ ဒီပ႐ိုဂရမ္ကို စတင္ အသံုးမျပဳခင္ သိထားသင္႔တဲ့ အခ်က္မ်ား##

**Pidgin** ဟာ အခမဲ့ျပီး ပြင့္လင္းတဲ့ အရင္းအျမစ္ **Instant Messaging** (**IM**) ဂလုိင္း ျဖစ္တယ္၊ **IM** အေကာင့္အမ်ိဳးမ်ိဳးကုိ interface တခုထဲမွာ စုစည္းၿပီး စီစဥ္ႏုိင္၊ စီမံခန္႔ခြဲႏုိင္တယ္။ **Pidgin** ကုိ စတင္ မသုံးစြဲခင္၊ ေလာေလာဆယ္ သင္ အသုံးျပဳေနတဲ့ **IM** အေကာင့္ တခုခု ရွိထားရမယ္၊ အဲဒီ အေကာင့္ကုိ **Pidgin** မွာ မွတ္ပုံတင္ထားရမယ္။ ဥပမာ အားျဖင့္၊ အကယ္လုိ႔ သင့္ဆီမွာ **Gmail** အီးေမးလ္ အေကာင့္တခု ရွိတယ္ ဆုိရင္၊ **IM** ၀န္ေဆာင္မႈ တခု ျဖစ္တဲ့ **GoogleTalk** ကုိ **Pidgin** ထဲမွာ အသုံးျပဳႏုိင္တယ္။ လက္ရွိ **IM** အေကာင့္ log-in အခ်က္အလက္ကုိ အသုံးျပဳျပီး **Pidgin** ထဲမွာ မွတ္ပုံတင္ႏုိင္၊ ၀င္ေရာက္ အသုံးျပဳႏုိင္ပါတယ္။

**မွတ္ခ်က္** - သုံးစြဲသူ အားလုံးက သူတုိ႔ရဲ႕ **Instant Messaging Service Provider** ေတြရဲ႕  privacy နဲ႔ လုံျခဳံေရး မူ၀ါဒေတြကုိ အတတ္ႏုိင္ဆုံး ေလ့လာ သိရွိထားဖုိ႔ လုိအပ္ပါတယ္။

**Pidgin** က ေအာက္ပါ **IM** ၀န္ေဆာင္မႈေတြကုိ ပံ့ပုိးထားတယ္ - [**AIM**](http://dashboard.aim.com/aim), [**Bonjour**](http://www.apple.com/support/bonjour/), [**Gadu-Gadu**](http://komunikator.gadu-gadu.pl/), [**Google Talk**](http://www.google.com/talk/), **Groupwise**, [**ICQ**](http://www.icq.com), **IRC**, [**MIRC**](http://www.mirc.com/), [**MSN**](http://www.msn.com/), 
[**MXit**](http://www.mxit.com/), [**MySpaceIM**](http://www.myspace.com/guide/im), [**QQ**](http://www.qq.com/), [**SILC**](http://silcnet.org/), **SIMPLE**, [**Sametime**](http://www.ibm.com/developerworks/downloads/ls/lst/), [**Yahoo!**](http://messenger.yahoo.com/), **Zephyr** နဲ႔  **XMPP** messaging protocol ကုိ အသုံးျပတဲ့ **IM** clients အားလုံး။

**Pidgin** ကုိ သူနဲ႔ အမ်ိဳးမတူတဲ့ **IM** services ေတြနဲ႔ ဆက္သြယ္ စကားေျပာလုိ႔ မရဘူး။ ဥပမာ အားျဖင့္၊ အကယ္လုိ႔ **Pidgin** ကုိ အသုံးျပဳၿပီး **Google Talk** အေကာင့္ထဲ ၀င္မယ္ ဆုိရင္၊ ICQ အေကာင့္ကုိ အသုံးျပဳေနတဲ့ မိတ္ေဆြ တေယာက္ေယာက္ကုိ chat လုပ္လုိ႔ ရမွာ မဟုတ္ပါဘူး။

ဒါေပမဲ့၊ **Pidgin** ကုိ ပံ့ပုိးမႈေပးတဲ့ messaging protocols ေတြကုိ အေျခခံျပီး multiple accounts ေတြကုိ configure လုပ္ႏုိင္၊ စီမံခန္႔ခြဲႏုိင္တယ္။ ဆုိလုိတာက **Gmail** နဲ႔ **ICQ** အေကာင့္ေတြကုိ တျပိဳင္တည္း အသုံးျပဳျပီး (**Pidgin** က ေထာက္ပံ့ထားတဲ့) services တခုခုနဲ႔ အဆက္အသြယ္ လုပ္တဲ့သူေတြကုိ chat စကားေျပာႏုိင္ပါတယ္။

**Pidgin** ဟာ **IM** sessions အတြက္ အထူး သင့္ေတာ္တယ္၊ တျခား messaging clients ေတြထက္ ပုိေကာင္းတဲ့ လုံျခဳံေရးကုိ ပံ့ပုိးထားျပီး သင့္ရဲ႕ privacy နဲ႔ လုံျခဳံေရးကုိ အႏၱရာယ္ ျဖစ္ႏိုင္တဲ့ မလုိအပ္တဲ့ adware (သုိ႔) spyware ေတြလည္း မပါဘူး။

**Off-the-Record** (**OTR**) စာတုိေပးပုိ႔ေရးစနစ္ဟာ **Pidgin** အတြက္ စီစဥ္ ေရးသားထားတဲ့ plugin တခု ျဖစ္တယ္။ ေအာက္ပါ privacy နဲ႔ လုံျခဳံေရး features ေတြကုိ ပံ့ပုိးထားတယ္ -

- **Authentication** - သင္နဲ႔ ဆက္သြယ္ စကားေျပာေနသူဟာ သင္ ရည္ရြယ္ထားတဲ့သူ ျဖစ္ေၾကာင္း အတည္ျပဳလုိ႔ ရတယ္။
- **Deniability** - စကားေျပာဆုိမႈ chat session ျပီးဆုံးသြားတဲ့အခါ၊ စာတုိေပးပုိ႔ခ်က္ေတြကုိ ဘယ္ေနရာကေန လုပ္တယ္၊ ဘယ္သူနဲ႔ စကားေျပာတယ္ စတာေတြကုိ ခြဲျခား ေဖၚထုတ္လုိ႔ ရမွာ မဟုတ္ပါဘူး။
- **Encryption** - လက္ငင္း စာတုိေပးပို႔ခ်က္ေတြကုိ ဘယ္သူမွ ရယူ ဖတ္ရႈလုိ႔ ရမွာ မဟုတ္ပါဘူး။
- **Perfect Forward Security** - အကယ္လုိ႔ တေယာက္ေယာက္က သင့္ရဲ႕ private keys ေတြကုိ ရရွိသြားတယ္ ဆုိရင္၊ အရင္က စကားေျပာဆုိခ်က္ေတြကုိ သိႏုိင္မွာ မဟုတ္ဘူး။

**မွတ္ခ်က္** - **Pidgin** ကုိ **OTR** plugin မတုိင္ခင္ install လုပ္ထားရပါ့မယ္။
