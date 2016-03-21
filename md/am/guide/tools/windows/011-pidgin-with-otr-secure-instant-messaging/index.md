

---

lang: am
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 011
title: Pidgin with OTR - Secure Instant Messaging

---

**ዋናው ገጽ (Homepage)**

- **ፒድጂን (Pidgin)**: [**www.pidgin.im**](http://www.pidgin.im)
- **ኦቲአር (OTR)**: [**www.cypherpunks.ca/otr**](http://www.cypherpunks.ca/otr/)

**ኮምፒውተራችን ምን ያስፈልገዋል?**
- የኢንተርኔት ግንኙነት
- ማንኛውም የዊንዶውስ አይነቴዎች

**በዚህ መመሪያ ጥቅም ላይ የዋሉት አይነቴዎች**
- Pidgin 2.7.11 
- OTR 3.2.0.1  

**ለመጠቀም የሚያስፈልግ ፈቃድ/ላይሰንስ**
ነጻ ሶፍትዌር (Freeware)

**አስፈላጊ ንባብ**፦
**የኢንተርኔት ደኅንነት መጽሐፍ** ምእራፍ [**7. የኢንተርኔት ግንኙነታችንን በምሥጢር መያዝ**] (/am/chapter-7)

**ይህን መሣሪያ መጠቀም ለመጀመር የሚፈጀው ጊዜ**
-	30 ደቂቃ

**ከዚህ መሣሪያ ምን ጥቅም እናገኛለን?**
- ብዙዎች የሚጠቀሙባቸውን የፈጣን መልእክት ልውውጥ አገልግሎቶች በአንድ ፕሮግራም ለማደራጀትና ለማስተዳደር ያስችላል
- ምሥጢራዊነቱ የተጠበቀ አስተማማኝ ቻት ማድረግ እንችላለን


**ከጂኤንዩ ሊኑክስ (GNU Linux)፣ ማክ (Mac OS) እና ከሌሎች የማይክሮሶፍት ዊንዶውስ ጋራ/ላይ በሚገባ የሚሠሩ ፕሮግራሞች**

**ፒድጂን (Pidgin)** እና **ኦቲአር (OTR)** **ከማይክሮሶፍት ዊንዶውስ** እና **ጂኤንዩ/ሊኑክስ** የሚሠሩ አይነቴዎች አሏዋቸው። ሌላው **ለማይክሮሶፍት ዊንዶውስ** የሚሠራው ባለብዙ አገልግሎት (multi-protocol) **የፈጣን መልእክት ልውውጥ** (**IM**) ፕሮግራም  [**Miranda IM (ሚራንዳ)**](http://www.miranda-im.org/) የሚባለው ነው። ይህ ፕሮግራም **ኦቲአር** አገልግሎትንም ጨምሮ ይሰጣል። **የማክ (Mac OS)** ተጠቃሚዎች [**Adium (አዲየም)**](http://adium.im/) የተባለው እንዲጠቀሙ ይመከራሉ። ይኽኛውም ፕሮግራም  **ኦቲአር** ለመጠቀም የሚያስችል ባለብዙ አገልግሎት የፈጣን መልእክት ልውውጥ ፕሮግራም ነው። 



### 1.1 ይህን መሣሪያ መጠቀም ከመጀመራችን በፊት ልናውቃቸው የሚገቡ ነገሮች ###

**ፒድጂን (Pidgin)** በተለያዩ **የፈጣን መልእክት ልውውጥ (Instant Messaging)** (**IM**) አገልግሎት መስጫዎች ያሉንን አድራሻዎች በቀላሉ በአንድ ፕሮግራም ለማደራጀትና ለመከታተል የሚረዳ፣ በነጻ የሚገኝ አገልግሎት ነው። **ፒድጂንን (Pidgin)** መጠቀም ከመጀመራችን በፊት **በፒጅን** የምናስመዘግበው **የፈጣን መልእክት ልውውጥ (Instant Messaging)** (**IM**) አድራሻ/አካውንት ሊኖረን ይገባል። ለምሳሌ የጂሜይል ተጠቃሚ የሆነ ሰው የጂሜይል **የፈጣን መልእክት ልውውጥ (Instant Messaging)** (**IM**) የሆነውን **GoogleTalk** **በፒድጂን** ሊጠቀምበት ይችላል። የፈጣን መልእክት አድራሻችንን የምንከፍትበትን መረጃ አድራሻውን **በፒድጂን** ለማስመዝገብ እንጠቀምበታለን። 

**ማስታወሻ**፦ ሁሉም ተጠቃሚዎች **የፈጣን መልእክት አገልግሎት ሰጪዎቻቸው (Instant Messaging Service Provider)** የሚተዳደሩበትን የደኅንነት ፖሊሲ በተቻለ መጠን በዝርዝር ለመረዳት እንዲሞክሩ ይመከራሉ። 


**ፒድጂንን (Pidgin)** የሚከተሉትን **የአይኤም (IM)** ማለትም**የፈጣን መልእክት ልውውጥ/ቻት (Instant Messaging)** አገልግሎቶች ያስተናግዳል፦ [**AIM**](http://dashboard.aim.com/aim) ፣ [**Bonjour**](http://www.apple.com/support/bonjour/) ፣ [**Gadu-Gadu**](http://komunikator.gadu-gadu.pl/) ፣  [**Google Talk**](http://www.google.com/talk/) ፣ **Groupwise** ፣ [**ICQ**](http://www.icq.com) ፣ **IRC** ፣  [**MIRC**](http://www.mirc.com/) ፣ [**MSN**](http://www.msn.com/)፣ 
[**MXit**](http://www.mxit.com/) ፣ [**MySpaceIM**](http://www.myspace.com/guide/im) ፣ [**QQ**](http://www.qq.com/) ፣  [**SILC**](http://silcnet.org/) ፣  **SIMPLE** ፣ [**Sametime**](http://www.ibm.com/developerworks/downloads/ls/lst/) ፣ [**Yahoo!**](http://messenger.yahoo.com/) ፣ **Zephyr**  እና  **XMPP** የተባለውን የመልእክት ስምምነት/አሠራር (messaging protocol)  የሚቀበል ማንኛውም **አይኤም (IM)** ።


**ፒድጂንን** በተለያዩ  **የፈጣን መልእክት** አገልግሎት ሰጪዎች መካከል መልእክት መለዋወጥን አይፈቅድም። ለምሳሌ **የጉግል ቶክ (Google Talk)** ተጠቃሚ የሆነ ሰው **ICQ** ወይም **Yahoo!**  በሚባለው አገልግሎት ሰጪ ካለ ሰው ጋራ ፈጥን መልእክት መለዋወጥ አይችልም። ተጠቃሚዎቹ እርስ በርስ ፈጣን መልእክት ለመለዋወጥ የግድ በተመሳሳይ አገልግሎት ሰጪዎች በሚከፍቷቸው አድራሻዎች መጠቀም አለባቸው፤ **በፒድጂን** ለመጠቀቀምም እንዲሁ። 


ይህን እንጂ **ፒድጂን** በተለያዩ አገልግሎት ሰጪዎች ዘንድ የከፈትናቸውን ብዙ አድራሻዎች/አካውንቶች በአንድ ላይ ለማደራጀት በሚያስችለን መልኩ ልንጠቀምበት እንችላለን። ይህ ማለት ለምሳሌ በተመሳሳይ ጊዜ **የጂሜይል** እና **የያሁ!** አድራሻዎቻችንን ከፍተን በሌላው ጫፍ የአንዱ ተጠቃሚ ከሆነ ሰው ጋራ ቻት ማድረግ ወይም ፈጣን መልእክት መለዋወጥ እንችላለን። (**በፒድጅን** የማይሠሩ አገልግሎቶች እንዳሉ ግን መርሳት የለብንም። የሚሠሩት ቀድም ሲል ተዘርዝረዋል።)


**ፒድጂን** ከሌሎች አገልግሎት ሰጪዎች በጣም የተሻለ አስተማማኝ የደኅንነት ጥበቃ የሚሰጥ በመሆኑ በፈጥን መልእክት ለውውጦች ወቅት እንድንጠቀምበት በጥብቅ እንመከራለን። ፒድጂን ምሥጢራዊነትን እና ደኅንነትን ለአደጋ ሊያጋልጡ ከሚችሉ የማያስፈልጉ አድዌሮች እና ስፓይዌዎች የጸዳ መሆኑ አገልግሎቱን የበለጠ ተመራጭ ያደርገዋል። 


**Off-the-Record (ኦፍ-ዘ-ሪከርድ)** (**ኦቲአር (OTR)**)፦ በተለይ **ለፒድጂን** ታስቦ የተዘጋጀ የአገልግሎት መጨመሪያ (plugin) ነው። የሚከተሉትን ከደኅንነት እና ምሥጢራዊነት ጋራ የተዛመዱ አገልግሎቶች ይሰጣል።

- **ማረጋገጥ(Authentication)**፦ በሌላው ወገን ሆኖ ቻት የሚያደርገን ሰው በእርግጥም እኛ የምናውቅውና የምንፈልገው ሰው መሆኑን ያረጋግጥልናል። 
- **የመልእክት ስወራ (Deniability)**፦ የፈጣን መልእክት ልውውጣችን ማለትም ቻታችን ከተጠናቀቀ በኋላ  የተለዋወጥናቸው መልእክቶች ከሁለታችን የመጡ መሆናቸው እንዳይታወቅ ይሆናል።
- **ኢንክሪፕሽን (Encryption)**፦ ፈጣን መልእክቶቻችንን/ቻታችንን ማንም ሰው ሊያገኘው እና ሊያነበው አይችልም።
- **Perfect Forward Security**፦ በሆነ አጋጣሚ የመግቢያ የይለፍ ቃላችን በሌላ ሰው እጅ ቢወድቅ እንኳን ከዚያ ቀደም ያደረግናቸውን ልውውጦች ሊያገኛቸው አይችልም። 


**ማስታወሻ**፦ **ከኦቲአር (OTR)** በፊት **ፒድጂንን** መጫን አለብን።
