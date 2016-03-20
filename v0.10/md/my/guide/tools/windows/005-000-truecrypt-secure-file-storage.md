

---

lang: my
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 005
title: TrueCrypt - Secure File Storage

---

**ပင္မ စာမ်က္ႏွာ**

[**www.truecrypt.org**](http://www.truecrypt.org/)

**ကြန္ပ်ဴတာ လိုအပ္ခ်က္မ်ား**

- Windows 2000/XP/2003/Vista/7
- Install လုပ္ဖို႔ (သုိ႔) volumes ေတြကို (လက္ရွိ volumes အထဲကို ဝင္ေရာက္ဖုိ႔ မဟုတ္ပဲ) ဖန္တီးဖို႔ Administrator လုပ္ပိုင္ခြင့္ ရွိထားရမယ္။

**ဒီလမ္းၫႊန္ထဲမွာ အသံုးျပဳတဲ့ ဗားရွင္းမ်ား**

- ၇.ဝa

**လုိင္စင္ ခြင့္ျပဳခ်က္**

- အခမဲ့ၿပီး ပြင့္လင္းတဲ့ အရင္းအျမစ္ ေဆာ့ဗ္ဝဲ

**ဖတ္ရႈရမည့္ အေၾကာင္းအရာမ်ား -**

- သံုးစြဲနည္း စာအုပ္ငယ္ အခန္း [**၄။ ကြန္ပ်ဴတာထဲက အထိခိုက္မခံတဲ့ ဖိုင္မ်ားကို ကာကြယ္နည္း**](/my/chapter-4)

**အဆင့္**

- (Standard Volumes) - ၁။ လက္သင္၊ ၂။ ပ်မ္းမွ်၊ **၃။ အလယ္အလတ္**၊ ၄။ အေတြ႔အၾကံဳရွိေသာ၊ ၅။ အဆင့္ျမင့္ 
- (Hidden Volumes) - ၁။ လက္သင္၊ ၂။ ပ်မ္းမွ်၊ ၃။ အလယ္အလတ္၊ **၄။ အေတြ႔အၾကံဳရွိေသာ**၊ ၅။ အဆင့္ျမင့္

**ဒီေဆာ့ဗ္၀ဲကို စတင္ သံုးစြဲဖို႔ လိုအပ္တဲ့ အခ်ိန္ -**

- (Standard Volumes) - ၃၀ မိနစ္
- (Hidden Volumes) - ၃၀ မိနစ္

**ျပန္လည္ရရွိမဲ့ အက်ိဳးေက်းဇူးမ်ား -**

- ဖိုင္ေတြကို က်ဴးေက်ာ္ ဝင္ေရာက္လာသူေတြ (သုိ႔) ခြင့္ျပဳခ်က္ မရွိပဲ ဝင္ေရာက္မႈေတြရဲ႕ အႏၱရာယ္ကေန ထိထိေရာက္ေရာက္ ကာကြယ္ေပးႏုိင္ပါတယ္
- အေရးႀကီးတဲ့ ဖိုင္ေတြကို အလြယ္တကူနဲ႔ လံုလံုျခံဳျခံဳ သိမ္းဆည္းေပးႏုိင္ပါတယ္

**GNU Linux, Mac OS နဲ႔ တျခား Microsoft Windows နဲ႔ လိုက္ဖက္တဲ့ ပ႐ိုဂရမ္မ်ား -**

**မွတ္ခ်က္** - **TrueCrypt** ကို **GNU Linux** နဲ႔ **Mac OS** တုိ႔မွာ အသံုးျပဳဖို႔ ကၽြန္ေတာ္တို႔ အထူး အၾကံျပဳလိုပါတယ္။

ဥပမာ [**Ubuntu**](http://www.ubuntu.com/) လို၊ **GNU Linux** ထုတ္လုပ္ျဖန္႔ခ်ီေရးအဖြဲ႔ အေတာ္မ်ားမ်ားက standard feature အရ disk တခုလံုးအတြက္ on-the-fly စာဝွက္ - စာျဖည္စနစ္ကို ပံ့ပိုးထားၾကတယ္။ system ကို Install လုပ္ၿပီးတဲ့အခါ အဲဒါကို စတင္ အသံုးျပဳႏုိင္တယ္။ စာဝွက္စနစ္ကို Linux system ထဲမွာ [**dm-crypt**](http://www.saout.de/misc/dm-crypt/), [**cryptsetup နဲ႔ LUKS**](http://code.google.com/p/cryptsetup/) စုစည္းမႈ တခုကို အသံုးျပဳၿပီး ထည့္သြင္းႏိုင္တယ္။ ေနာက္တမ်ဳိးအေနနဲ႔ အခမဲ့ ျဖစ္ၿပီး ပြင့္လင္းတဲ့ အရင္းအျမစ္ on-the-fly စာဝွက္-စာျဖည္တဲ့ ပ႐ိုဂရမ္တခု ျဖစ္တဲ့[**ScramDisk for Linux SD4L**](http://sd4l.sourceforge.net/) ကုိ အသံုးျပဳႏုိင္ပါတယ္။

**Mac OS** မွာေတာ့ **FileVault** ကို အသံုးျပဳႏိုင္တယ္၊ သူဟာ operating system ရဲ႕ အစိတ္အပိုင္းတခုျဖစ္ၿပီး၊ ပင္မ ဖိုင္တြဲထဲက အေၾကာင္းအရာနဲ႔ ဖိုင္တြဲငယ္ အားလံုးကို on-the-fly နည္းနဲ႔ စာဝွက္-စာျဖည္ေပးႏိုင္တယ္။ အခမဲ့ျဖစ္ၿပီး ပြင္းလင္းတဲ့ အရင္းအျမစ္ ပ႐ိုဂရမ္ ျဖစ္တဲ့ [**Encrypt This**](http://www.nathansheldon.com/files/) ကိုလည္း အသံုးျပဳႏိုင္တယ္။ ေရြးထားတဲ့ ဖိုင္ေတြကို သူက .DMG disk image အျဖစ္ စာဝွက္ေပးပါတယ္။

**Microsoft Windows** အတြက္ စာဝွက္ေပးတဲ့ ပရုိဂရမ္ေတြ အမ်ားႀကီးရွိပါတယ္။ ကၽြန္ေတာ္တို႔ အၾကံျပဳထားတဲ့ ေဖာ္ျပခ်က္တခ်ဳိ႕ကုိ ေအာက္မွာ ၾကည့္ရႈပါ -

- [**The FREE CompuSec**](http:/ခwww.ce-infosys.com/english/free_compusec/free_compusec.aspx) ဟာ အခမဲ့ျပီး၊ တဦးတည္းပုိင္၊ on-the-fly စာဝွက္/စာျဖည္ ပ႐ိုဂရမ္တခု ျဖစ္တယ္။ သူဟာ ကြန္ပ်ဴတာ disk တစိတ္တပိုင္းကုိပဲ ျဖစ္ျဖစ္၊ တခုလံုးကုိပဲ ျဖစ္ျဖစ္၊ USB drives (သုိ႔) CD ကိုပဲ ျဖစ္ျဖစ္ စာဝွက္ေပးႏိုင္တယ္။ CompuSec ရဲ႕ **DataCrypt** module ကို သီးျခား ဖိုင္ေတြကုိ စာဝွက္တဲ့ ေနရာမွာ အသံုးျပဳပါတယ္။
- *[**CryptoExpert 2009 Lite**](http://www.cryptoexpert.com/lite/) ဟာ အခမဲ့ျပီး၊ တဦးတည္းပုိင္၊ on-the-fly စာဝွက္စာျဖည္ ပ႐ိုဂရမ္တခု ျဖစ္တယ္။ သူဟာ **TrueCrypt** လိုပဲ ဝွက္ထားတဲ့ ဖိုင္ေတြကုိ ထားရွိႏုိင္တဲ့ container ကို ဖန္တီးေပးပါတယ္။*
- *[**AxCrypt**](http://www.axantum.com/AxCrypt/) ဟာ အခမဲ့ၿပီး သီးျခား ဖိုင္ေတြကို စာဝွက္ေပးႏိုင္တဲ့ ပြင့္လင္းတဲ့ အရင္းအျမစ္ ပ႐ိုဂရမ္တခု ျဖစ္ပါတယ္။* 
- *[**Steganos LockNote**](https://www.steganos.com/us/products/for-free/locknote/overview/) ဟာ အခမဲ့ၿပီး ပြင့္လင္းတဲ့ အရင္းအျမစ္ ပ႐ိုဂရမ္ တခု ျဖစ္တယ္။ သူ႔ကို အသံုးျပဳၿပီး ဘယ္လုိ စာမ်ိဳးကိုမဆို စာဝွက္ႏိုင္၊ စာျဖည္ေပးႏိုင္တယ္။ အဲဒီ စာကို **LockNote** application ထဲမွာ သိမ္းဆည္းထားမွာ ျဖစ္တယ္။ မွတ္ခ်က္တခုကို စာဝွက္/စာျဖည္ေပးႏုိင္တဲ့ ယႏၱရားဟာ သူရဲ႕ အစိတ္အပိုင္းတခု ျဖစ္တယ္။ **LockNote** ကုိ သယ္ေဆာင္ရတာ လြယ္ကူၿပီး Installation လုပ္ဖုိ႔လည္း မလိုပါဘူး။*

###၁.၁ ဒီပ႐ိုဂရမ္ကို စတင္ အသံုးမျပဳခင္ သိထားသင္႔တဲ့အခ်က္မ်ား###

**TrueCrypt** ဟာ ဖန္တီးလုိက္မဲ့ စကားဝွက္နဲ႔ ေဒတာေတြကို ေသာ့ခတ္ေပးျခင္းျဖင့္ ကာကြယ္မႈ ေပးမွာ ျဖစ္တယ္။ အကယ္လို႔ အဲဒီ စကားဝွက္ကို ေမ့သြားရင္ေတာ့၊ ေဒတာတခုလုံးကို ဆံုးရံႈးသြားမွာ ျဖစ္တယ္။ **TrueCrypt** ဟာ ဖိုင္ေတြကို ကာကြယ္ေပးႏုိင္ဖို႔ encryption (စာဝွက္စနစ္)လို႔ ေခၚတဲ့ လုပ္ငန္းစဥ္တခုကို အသံုးျပဳထားတယ္။ စာဝွက္စနစ္ အသံုးျပဳမႈကုိ တခ်ဳိ႕ႏိုင္ငံေတြမွာ တရားဝင္ ခြင့္ျပဳမထားဘူး။ ဖိုင္တခုခ်င္းကို စာဝွက္တာထက္၊ ကြန္ပ်ဴတာထဲမွာ **volume** လို႔ေခၚတဲ့ ကန္႔သတ္ထားတဲ့ ေနရာတခုကို **TrueCrypt** က ဖန္တီးေပးႏုိင္တယ္။ အဲဒီ စာဝွက္ထားတဲ့ volume ထဲမွာ ဖိုင္ေတြကို လံုလံုျခံဳျခံဳ သိမ္းထားႏိုင္ပါတယ္။

**TrueCrypt** က standard encrypted volume (သုိ႔) hidden volume တခုခုကို ဖန္တီးေပးႏိုင္တယ္။ အဲဒီ ေနရာတခုခုမွာ ဖိုင္ေတြကို လံုလံုျခံဳျခံဳ သိမ္းထားေပးမွာ ျဖစ္တယ္၊ ဒါေပမဲ့ hidden volume ဟာ အေရးႀကီးတဲ့ အခ်က္အလက္ေတြကို သိပ္ အေရးမႀကီးတဲ့ ဖိုင္ေတြရဲ႕ ေနာက္ကြယ္မွာ ဝွက္ထားျခင္းျဖင့္၊ **TrueCrypt** volume ကို ဖြင့္ဖို႔ ဖိအားေပးလာတဲ့ အခ်ိန္မ်ိဳးမွာ သင့္ကို အကာအကြယ္ ေပးႏိုင္မွာ ျဖစ္တယ္။ ဒီလမ္းၫႊန္ခ်က္ထဲမွာ volumes နွစ္ခုစလံုးရဲ႕ အေသးစိတ္ အေၾကာင္းအရာကို ရွင္းလင္းေဖၚျပေပးထားပါတယ္။
