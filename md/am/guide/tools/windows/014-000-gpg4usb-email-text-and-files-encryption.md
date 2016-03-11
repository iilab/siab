

---

lang: am
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 014
title: gpg4usb - email text and files encryption

---

**ዋናው ገጽ (Homepage)**

- [**http://gpg4usb.cpunk.de/**](http://gpg4usb.cpunk.de/)


**ኮምፒውተራችን ምን ያስፈልገዋል?**

- ሁሉም የዊንዶው ዓይነቴዎች ሊሠሩ ይችላሉ።


**ለዚህ መመሪያ የተወሰደው ዓይነቴ**

- 0.3.1


**ፈቃድ/ላይሰንስ**

- ነጻ ሶፍትዌር


**አስፈላጊ ንባብ**

- የኢንተርኔት ደኅንነት መጽሐፍ [**7. የኢንተርኔት ግንኙነታችንን በምስጢር መያዝ ይቻላል? እንዴት?**](chapter-7)

- [**Digital Security and Privacy for Human Rights Defenders (የዲጂታል ደኅንነት ለሰብዓዊ መብት ተሟጋቾች**](https://www.frontlinedefenders.org/esecman) ፤ ምዕራፍ **2.4 Cryptology - Public Key Encryption (ገጽ 38)** 

**ይህን መሣርያ መጠቀም ለመጀመር የሚያስፈልገው ጊዜ**፦ 20 ደቂቃ


**ከጂፒጂ4ዩኤስቢ ምን ጥቅም እናገኛለን?**

- ከየትኛውም ቦታ (ለምሳሌ በኢንተርኔት ካፌ ወይም በሥራ ቦታ) ሆነን የኢሜል መልእክቶችን እና ፋይሎችን ኢንክሪፕት ማድረግ እንችላለን። 
- *ከኢንተርኔት ግንኙነት መስመር ውጪ (off-line)* በመሆን ኢንክሪፕት ማድረግ እና ከዚያም ኢንክሪፕት ያደረግናቸውን መልእክቶች የኢንተርኔት ግንኙነት ካለው ኮምፒውተር ላይ መላክ እንችላለን።

## 1.1 ይህንን መሣሪያ መጠቀም ከመጀመራችን በፊት ማወቅ ያለብን ጉዳዮች ##

**ጂፒጂ4ዩኤስቢ** ፋይሎችን እና የኢሜይል መልእክቶችን ኢንክሪፕት ወይም ዲክሪፕት ለማድረግ የምንጠቀምበት እና በተንቀሳቃሽ የመረጃ ማስቀመጫ ቋቶች በቀላሉ የሚያዝ ፕሮግራም ነው። **ጂፒጂ4ዩኤስቢ** በአደባባይ ቁልፍ ኢንክሪፕት የማድረግ ስልት (public-key cryptography) ላይ የተመሠረተ ነው። በዚህ አሠራር መሠረት እያንዳንዱ ተጠቃሚ የግሉን መንትያ ቆልፎች መፍጠር ይኖርበታል። አንደኛው መንትያ የግል ቁልፍ (private key) ተብሎ የሚጠራ ሲሆን ለሌላ ማንኛውም አካል   *በፍጹም* አሳልፈን የማንሰጠው በይለፍ ቃል የተጠበቀ ቁልፍ ነው ነው። 

ሁለተኛው መንትያ በአንጻሩ የአደባባይ ቁልፍ (public key) ተብሎ የሚጠራ ሲሆን መልእክት ተለዋዋጮቹ የሚቀባበሉትና የሚጠቀሙበት ነው። መረጃ የምንለዋወጠውን ሰው የአደባባይ ቁልፍ ካገኘን፣ እርሱም የእኛ የአደባባይ ቁልፍ እንዲደርሰው ካደረግን፣ ከእርሱ ጋራ ኢንክሪፕት የተደረጉ ፋይሎችን መላላክ እንችላለን። በሌላ አገላለጽ የአደባባይ ቁልፍ የተለዋወጡ ተጠቃሚዎች ብቻ ኢንክሪፕት ተደርገው የተላኩ ትን መረጃዎች ዲክሪፕት ማድረግ ይችላሉ ማለት ነው። 
የአደባባይ ቁልፋችንን መረጃ ለምንለዋወጣቸው ባልጀሮቻችን ከላክን እንዲሁ መንትያውን እና የግል ቁልፋችንን በጥንቃቄ መያዝ ከቻልን የሚላኩልንን ኢንክሪፕትድ ኢሜይሎች ማንበብ እንችላለን። 
 
በተጨማሪም የመልእክቶቻችንን ምሥጢራዊነትና ደኅንነት የበለጠ ለማረጋገጥ ዲጂታል ፊርማ መጠቀም እንችላለን። ትክክለኛው የአደባባይ ቁልፋችን ያለው ሰው የደረሰው የኢሜይል መልእክት በትክክል ከእኛ መላኩን፣ እንዲሁም መልእክቱ በመንገድ ላይ በሦስተኛ ወገን ተጠልፎ አለመነካካቱን ማረጋገጥ ይችላል። እኛም በተመሳሳይም የደረሰን የኢሜይል መልእክት በትክክልም ከምንፈልገው ሰው መምጣቱን በዲጂታል ፊርማው ማረጋገጥ እንችላለን።  

**በጂፒጂ4ዩኤስቢ** ፕሮግራም ስውር መንትያ ቁልፎችን ለመፍጠር፣ መረጃ ከምንለዋወጣቸው ሰዎች ጋራ የምንቀባበለውን የአደባባይ ቁልፍ (public keys)  ለማስተላለፍ (export)፣ መልእክቶችን ለመጻፍ እና ኢንክሪፕት ለማድረግ ያስችለናል። የአደባባይ ቁልፋችንን እና/ወይም ኢንክሪፕት የተደረገውን መልእክት **ከጂፒጂ4ዩኤስቢ** መገልበጥና (copy) በኢሜይላችን የመልእክት መጻፊያ ገበታ ላይ መለጠፍ (paste) እንችላለን። አለበለዚያም የአደባባይ ቁልፋችንን እና/ወይም ኢንክሪፕት የተደረገውን መልእክት እንደሌላ ፋይል በኮምፒውተራችን ላይ ማኖርና በአባሪነት አያይዘን መላክ እንችላለን። ሰነዶች እና ፋይሎችም ኢንክሪፕ ሊደረጉ እንደሚችሉ ማስታወስ ያሻል።  

**ማስታወሻ**፦ ኢንክሪፕትድ ያልሆኑት የመጀመሪያ (ኦርጅናል) ፋይሎችና ሰነዶች ቅጂ በኮምፒውተራችን ላይ ሊቀር ስለሚችል እነዚህን ቅጂዎች ከራሳችንም ሆነ ከመልእክት ተቀባያችን ኮምፒውተር ማስወገድ አስፈላጊ እና ጠቃሚ መሆኑን ማስታወስ ጠቃሚ ነው።

**ጂፒጂ4ዩኤስቢ** ከተመሳሳይ **ጂፒጂ** ወይም **ፒጂፒ** ፕሮግራሞች ጋር ቁልፎችን እና ኢንክሪፕት የተደረጉ መልእክቶችን ለመለዋወጥ ያስችላል። 

