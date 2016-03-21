

---

lang: my
community: guide
type: tactics
legacy: True
child: False
weight: 005
title: 5. How to recover from information loss

---

ဒစ္ဂ်စ္တယ္ သတင္း အခ်က္အလက္ေတြကို သိုေလွာင္ႏုိင္ (သို႔) လႊဲေျပာင္းႏုိင္တဲ့ နည္းလမ္းသစ္ တခုစီေၾကာင့္ စဥ္းစားစရာ ျဖစ္လာေနတဲ့ သတင္း အခ်က္အလက္ေတြ ေပ်ာက္ဆံုးသြားတာ၊ အခုိးခံရတာ (သို႔) အဖ်က္ဆီးခံရတာေတြ ျဖစ္ေပၚလာႏိုင္တယ္။ ႏွစ္နဲ႔ခ်ီျပီး လုပ္ေဆာင္လာခဲ့တဲ့ အရေတြကုိ အခိုးခံရတာ၊ နေမာ္နမက္ႏိုင္မႈေၾကာင့္ ပ်က္စီးသြားတာ၊ ကြန္ပ်ဴတာ hardware အသိမ္းခံရတာ၊ (သို႔) ဒီဂ်စ္တယ္ သိုေလွာင္ေရး နည္းပညာရဲ႕ သေဘာ သဘာဝအရ အၾကမ္းမခံတာေတြေၾကာင့္ တခဏ အတြင္းမွာ ေပ်ာက္ဆုံးသြားႏိုင္တယ္။ ကြန္ပ်ဴတာနဲ႔ ဆုိင္တဲ့ ကူညီပံ့ပိုးမႈေပးတဲ့ ကၽြမ္းက်င္သူေတြၾကားမွာ ေျပာဆိုသုံးႏႈန္းေလ့ရွိတဲ့ ဆို႐ိုးစကား တခုကေတာ့ - "အကယ္လုိ႔ ေဒတာ ေပ်ာက္ဆံုးသြားတယ္ဆုိရင္ ဆိုတာ ေမးရမဲ့ ေမးခြန္း မဟုတ္ဘူး၊ ဘယ္အခ်ိန္မွာ ေပ်ာက္သြားသလဲ ဆိုတာ သိဖို႔ပဲ အေရးႀကီးတယ္" ဆုိတဲ့အခ်က္ ျဖစ္တယ္။ ဒါေၾကာင့္ ဒီလို အေျခအေနမ်ိဳးနဲ႔ ႀကံဳေတြ႔လာရင္၊ ေနာက္ဆံုး Backup တခုကို ျပန္ဆယ္တင္ႏိုင္ဖို႔ စနစ္တက် စမ္းသပ္ထားတဲ့ ကိရိယာ တခုခုကုိ အသုံးျပဳဖုိ႔ အလြန္ အေရးႀကီးတယ္။ Backup နည္းစနစ္ရဲ႕ အေရးႀကီးပံုကို သတိျပဳလာတဲ့ အခ်ိန္ဟာ Backup တခုကို စနစ္တက် ထားရွိဖို႔ လိုအပ္လာတဲ့ေန႔ကေန စတင္လာတယ္။

အဲဒါဟာ လံုၿခံဳမႈ ရွိတဲ့ တြက္ခ်က္မႈထဲမွာ အေျခခံအက်ဆံုး အစိတ္အပိုင္းေတြထဲက တခု ျဖစ္ေပမဲ့၊ ထိေရာက္တဲ့ Backup မူဝါဒကို ဖန္းတီးဖို႔ ဆုိတာ ထင္ထားသလို သာမန္ ကိစၥေတာ့ မဟုတ္ဘူး။ မူရင္း ေဒတာနဲ႔ Backup ေတြကို ျပင္ပ ေနရာအမ်ဳိးမ်ဳိးမွာ သိမ္းဆည္းဖို႔ လိုအပ္လာမႈ၊ Backup ေတြကို စိတ္ခ်လက္ခ် သိမ္းဆည္းရန္ အေရးႀကီးပံု၊ ကိုယ္ပိုင္ အိတ္ေဆာင္ သိမ္းဆည္းေရး ကိရိယာ (storage devices) ေတြကို အသံုးျပဳၿပီး တေယာက္နဲ႔ တေယာက္အၾကား သတင္း အခ်က္အလက္ေတြ ေဝမွ်ေနၾကတဲ့ လူအမ်ဳိးမ်ဳိးကို ညွိႏိႈင္းရတဲ့ အခက္အခဲ အမ်ဳိးမ်ဳိးေၾကာင့္ ထြက္ေပၚလာတဲ့ စီမံခန္႔ခြဲပုိင္းမွာ အခက္အခဲ တခု ျဖစ္လာႏိုင္တယ္။ Backup နဲ႔ ဖိုင္ဆယ္တင္မႈ (file-recovery) နည္းနာေတြအျပင္၊ [*Cobian Backup*](/my/glossary#Cobian_Backup) နဲ႔ [*Undelete Plus*](/my/glossary#Undelete_Plus) ကိရိယာ ႏွစ္မ်ဳိး အေၾကာင္းကို ဒီအခန္းမွာ တင္ဆက္ ေပးထားတယ္။

### ေနာက္ခံ ဇာတ္လမ္း - ###

<div class="background" markdown="1">အယ္လင္နာဟာ ႐ုရွား စကားေျပာတဲ့ ႏိုင္ငံတခုမွာ သဘာဝ ထိန္းသိမ္းေရး အဖြဲ႔ဝင္ တဦးျဖစ္ၿပီး၊ အဲဒီေဒသက တရားမဝင္ သစ္ပင္ ခုတ္ထြင္မႈ အေျခအေနကို အသားေပးတဲ့ ႐ုပ္ပံုေတြ၊ ဗြီဒီယိုေတြ၊ ေျမပံုေတြနဲ႔ အျဖစ္အပ်က္ေတြကို ဆန္းဆန္းျပားျပား ဖန္တီးထားတဲ့ တင္ဆက္မႈကို အေျခခံျပီး ကြန္ရက္ စာမ်က္ႏွာ တခုကုိ စတင္ တည္ေဆာက္ခဲ့တယ္။ သူမဟာ သစ္ထုတ္လုပ္မႈနဲ႔ ပါတ္သက္တဲ့ စာတမ္းေတြ၊ မီဒီယာ ဖိုင္ေတြနဲ႔ ပထဝီ အေနအထားနဲ႔ဆုိင္တဲ့ အခ်က္အလက္ကို ႏွစ္ေပါင္းမ်ားစြာ စုေဆာင္းခဲ့ၿပီး အဲဒါေတြကို သူမ အလုပ္လုပ္ေနတဲ့ NGO ႐ံုးတြင္းက ဝင္းဒိုး ကြန္ပ်ဴတာ အေဟာင္း တလံုးထဲမွာ အမ်ားစုကို သိမ္းဆည္းထားခဲ့တယ္။ အဲဒီသတင္း အခ်က္အလက္ေတြ အေၾကာင္းကုိ တင္ထားတဲ့ ကြန္ရက္ စာမ်က္ႏွာ တခုကို တည္ေဆာက္ေနတဲ့ အခ်ိန္မွာ၊ ဖိုင္ေတြရဲ႕ အေရးပါပံုကို သတိျပဳမိလာတယ္၊ အထူးသျဖင့္ ဖိုင္အားလံုးကို ကြန္ရက္ စာမ်က္ႏွာေပၚ မတင္မီ အကယ္လုိ႔ သူမရဲ႕ ကြန္ပ်ဴတာ ပ်က္စီးသြားခဲ့ရင္၊ ဖိုင္ေတြကို ထိန္းသိမ္းရမဲ့ ကိစၥအတြက္ စိတ္ပူလာမိတယ္။ သူမ အလုပ္လုပ္ေနတဲ့ အဖြဲ႔အစည္းမွာ တျခား အဖြဲ႔ဝင္ေတြကလည္း အဲဒီကြန္ပ်ဴတာကို တခါတေလ အသံုးျပဳတတ္ၾကတဲ့ အတြက္၊ သူမရဲ႕ လုပ္ေဆာင္ခ်က္ေတြကို သိမ္းဆည္းထားတဲ့ ဖိုင္တြဲကို တေယာက္ေယာက္က အမွတ္တမဲ့ ပယ္ဖ်က္မိရင္ ျပန္ဆယ္တင္ႏိုင္တဲ့ နည္းလမ္းကို သူမ သိခ်င္လာတယ္။ သူမရဲ႕ တူေလး နီကိုလိုင္းကို ေခၚၿပီး Backup လုပ္တဲ့ နည္းတခုကို လုပ္ေပးဖို႔ အကူအညီ ေတာင္းလိုက္တယ္။
</div>

### ဒီသင္ခန္းစာကေန ေလ့လာသင္ယူႏိုင္တဲ့ အခ်က္မ်ား ###

- သတင္း အခ်က္အလက္ေတြကို စီမံၿပီး Backup လုပ္နည္း
- Backup ေတြကို သိမ္းဆည္းထားသင့္တဲ့ ေနရာ
- Backup ေတြကို လံုလံုၿခံဳၿခံဳ စီမံႏိုင္တဲ့ နည္းလမ္း
- မေတာ္တဆ ဖ်က္လိုက္မိတဲ့ ဖိုင္ေတြကို ဆယ္တင္နည္း
	
