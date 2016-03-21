

---

lang: am
community: guide
type: tactics
legacy: True
child: True
weight: 2
depth: 3
title: Wiping information with secure deletion tools

---

በዚህ ምእራፍ የተጠቆሙትንም ይሁን መሰል አስተማማኝ የመደምሰሻ (secure deletion) መሣሪያዎች ተጠቀምን ማለት እንደተለመደው “ዴሊት አደርግን” ማለት ብቻ አይደለም፤ የተደመሰሱትን ስሱ መረጃዎች በሌላ ተካናቸው፣ ወይም በላያቸው ላይ ሌላ ነገር ጻፍንባቸው  ('overwriting') ማለት ነው። ቀድሞ ባነሳነው የፋይል-ካቢኔት ምሳሌያችን ብንቀጥል፤ የመዝገቦቹ ስሞች ቢቀየሩም በውስጣቸው ያለው መረጃ ግን እንዳለ ባለበት ሊቆይ እንደሚችል ጠቅሰናል። እነዚህ መረጃዎች በእርሳስ እንደተጻፉ እናስብ። አስተማማኝ የማጥፊያ መሣሪያዎችን ተጠቀምን ማለት፣ እነዚህን በእርሳስ የተጻፉ መረጃዎች በላፒስ ማጥፋት ብቻ ሳይሆን፤ ከዚያ በኋላ በጠፋው በእያንዳንዱ ቃል የቀረ ደብዛዛ ምስል ላይ ሌላ ቃል ጻፍንበት እንደማለት ነው። መጀመሪያ በላፒስ አጥፍቶ ከዚያ በላዩ ላይ አዲስ ነገር መጻፍ። በላፒስ የጠፋ ጽሑፍ በደብዛዛውም ቢሆን የመታየት እድል እንዳለው ሁሉ ዴሊት የተደረገ ዲጂታል መረጃም መልሶ ሊገኝና ሊነበብ ይችላል። በዚህ ላይ አዲስ ነገር ተመልሶ ሲጻፍበት ግን የቀድሞው ጽሑፍ የመታየት እድሉ እያነሰ ይሔዳል።   ይህ አሠራር [*ማንጻት/ዋይፒንግ (wiping)*](/am/glossary#Wiping) ይባላል። በመጀመሪያው ጽሑፍ ላይ ተደጋግሞ በተጻፈበት መጠንም ፈጽሞ ሊታይ/ሊገኝ ወደማይችልበት ደረጃ ይደርሳል፤ የመጀመሪያውን መረጃ ለማንበብ ለሚሞክርም እጅግ አስቸጋሪ ይሆንበታል። የመስኩ ባለሞያዎች በአብዛኛው ሦስት እና ከዚያም በላይ ጊዜ ደራርቦ መጻፍን (overwriting) ይመክራሉ፤ አንዳንዶቹ ደግሞ እንደ መረጃው ስሱነት ለሰባት እና ከዚያም ለሚበልጥ ጊዜ ደራርቦ መጻፍን ያሳስባሉ። [*የማንጻት/ዋይፒንግ (wiping)*](/am/glossary#Wiping)  ሶፍትዌር በቀጥታ በቂ ሊባል ለሚችል ጊዜ ደጋግሞ አጥፍቶ-የመጻፍ ሥራ ይሠራል፤ ይህ የማይበቃ መስሎ ከታየን ደግሞ የድግግሞሹን መጠን ልንጨምረው እንችላለን።


### ፋይሎችን ማንጻት/ዋይፒንግ ### 

ስሱ መረጃዎችን ከሐርድ ድራይቮችም ይሁን ከሌሎች የማከማቻ ማህደሮች/ቋቶች [*ለማንጻት/ዋይፒንግ (wiping)*](/am/glossary#Wiping)  ሁለት የተለመዱ መንገዶች አሉ። አንድን ነጠላ ፋይል [*ማንጻት/ዋይፕ (wipe)*](/am/glossary#Wiping) ይቻላል፤ ወይም በሐርድ ድራይቩ ውስጥ አገልግሎት ላይ ያልዋሉ ቦታዎችን ('unallocated' space) በጅምላ [*ማንጻት/ዋይፕ (wipe)*](/am/glossary#Wiping) እንችላለን። በዚህ ላይ ውሳኔ ስንሰጥ አስቀድመን ያነሳነውን የረጅም ሪፖርት ዝግጅት ሒደት ምሳሌያችንን መላልሶ ማስተወስ ይጠቅማል። በሪፖርት ዝግጅቱ መጨረሻ የምናገኘው የሚታይ ፋይል አንድ ብቻ ቢሆንም፣ በዝግጅቱ ሒደት ሴቭ የተደረጉ በሐርድ ድራይቫችን ላይ የተበታተኑ ያለተጨረሱ ቅጂዎች መኖራቸው አይቀርም። አንድን ፋይል ለይተን [*ብናነጻ/ዋይፕ (wipe)*](/am/glossary#Wiping) የዚህ ፋይል የመጨረሻ እትም/አይነቴ (ቨርዥን) ፈጽሞ ይጠፋል፤ የተበታተኑት የቀደሙ እትሞቹ/አይነቴዎቹ ግን ባሉበት ይተዋሉ። ለነገሩ እነዚህን በየቦታው የተዘሩ የቀደሙ እትሞቹን ልዩ ሶፍትዌር ካልተጠቀምን በቀር እንኳን ልናነጻቸው ያሉበትንም ቦታ ማግኘት አንችልም። ነገር ግን ባዶ ቦታዎችን (blank space) በጅምላ [*በማንጻት/ዋይፒንግ (wiping)*](/am/glossary#Wiping) ከዚህ ቀደም የተደመሰሱ (deleted) መረጃዎች በሙሉ በያሉበት እስከወዲያኛው እንዲነጹ ማድረግ እንችላለን። ይህንን በፋይል-ካቢኔው ምሳሌ ያየነው እንደሆነ ስማቸው ቢጠፋም መረጃዎችን የያዙ ዶክመንቶችን አንድ በአንድ እየፈለጉ መረጃውን እያጠፉ በላዩ ላይ ሌላ መረጃ እንደመጻፍ ነው።

    
[*ኢሬዘር (Eraser)*](/am/glossary#Eraser)  በኢንተርኔት በነጻ የሚገኝ፣ ለአጠቃቀም ቀላል የሆነ አስተማማኝ የማጥፊያ/መደምሰሻ መሣሪያ ነው። [*ኢሬዘርን (Eraser)*](/am/glossary#Eraser) በመጠቀም ፋይሎችን በሦስት መንገዶች  [*ማንጻት/ዋይፕ (wipe)*](/am/glossary#Wiping) ይቻላል። አንድ ነጠላ ፋይልን ለይተን ማንጻት፣ **በሪሳይክል ቢን (Recycle Bin)**   የተጠራቀሙትን ፋይሎች አንድ ላይ ማንጻት፣ ወይም በድራይቩ ውስጥ የሚገኙትን አገልግሎት ላይ ያልዋሉ ቦታዎችን (unallocated space) በጅምላ [*ማንጻት/ዋይፒንግ (wiping)*](/am/glossary#Wiping) እንችላለን።  [*ኢሬዘር (Eraser)*](/am/glossary#Eraser) በዊንዶውስ የሚፈጠሩ  [*ስዋፕ ፋይል (swap file)*](/am/glossary#Swap_file) የሚባሉትንም [*ለማንጻት/ዋይፕ (wipe)*](/am/glossary#Wiping)  ይችላል፤ ዝርዝሩን ወደፊት እናገኘዋለን።


<div class="getstarted" markdown="1">

አጠቃቀም! [*ኢሬዘር - አስተማማኝ የፋይል አወጋገድ መመሪያ (Eraser - Secure File Removal Guide)*](/en/eraser_main)

</div>


አስተማማኝ የመደምሰሻ መሣሪያዎች እኛ ራሳችን ካላዘዝናቸው በቀር የሚታዩ ፋይሎችን [*የማንጻት/ዋይፕ (wipe)*](/am/glossary#Wiping)  ሥራ  አያከናውኑም። ነገር ግን ይህን መሰል መሣሪያዎችን ስንጠቀም ከፍተኛ ጥንቃቄ ማድረግ እንዳለብን ለአፍታም ቢሆን መዘንጋት የለብንም። መቼም ስሕተት አያጋጥምም አይባልም፤  ለዚህም ነው ተጠቃሚዎች  **ሪሳይክል ቢንን (Recycle Bins)**   እና የመረጃ መልሶ ማግኛ መሣሪያዎችን (data recovery tools) እጅግ ጠቃሚ ሆነው የሚያገኙዋቸው። አንድ ፋይል ዴሊት ባደረግን (በደመሰስን) ቁጥር ወዲያውኑ [*የማንጻት/ዋይፒንግ (wiping)*](/am/glossary#Wiping) ልምድ ካለን በስሕተት ያጠፋነውን ፋይል መልሶ ማግኘት የምንችልበትን እድል ሁሉ እያጠበብነው እንሔዳለን። ስለዚህ ብዙ መረጃዎችን ከኮምፒውተራችን [*ከማንጻታችን/ዋይፒንግ (wiping)*](/am/glossary#Wiping) በፊት አስተማማኝ የመጠባበቂያ ክምችት መያዛችንን  ማረጋገጥ አለብን።


<div class="background" markdown="1">

**ዘሐራ**፦ ማይክሮሶፍትን እና ኦፕን ኦፊስን የመሳሰሉ ፕሮግራሞች የፋይሎችን ጊዜያዊ ቅጂዎች የሚያስቀምጡበት ጊዜ እንዳለ አውቃለሁ። ሌሎችም ፕሮግራሞች እንዲሁ ሳናውቀው የፋይሎችን የተለያዩ ቅጂዎች ያስቀምጣሉ? መጨነቅ ያለብኝ ራሴ ስለምፈጥራቸውና ስለምደመስሳቸው (ዴሊት) ፋይሎች ብቻ አይደለም ማለት ነው?

**ኦላና**፦  በእርግጥ የተለያዩ ፕሮግራሞች ግላዊ መረጃዎችሽን እና የኢንተርኔት እንቅስቃሴሽን ሊያመላክቱ የሚችሉ መረጃዎችን በኮምፒውተርሽ ላይ የሚተዉበት ብዙ ቦታዎች አሉ። ለምሳሌ የጎበኘሻቸውን ድረ ገጾች፣ በቅርቡ ያዘጋጀሽው የኢሜይል ረቂቆች (ድራፍቶች)  ወይም ሌላ ነገር ሊሆን ይችላል። ኮምፒውተርሽን እንደምትጠቀሚበት መጠን እነዚህ ነገሮች አሳሳቢ ሊሆኑ ይችላሉ።
</div>


### ጊዜያዊ ዳታዎችን ማንጻት ###

[*ኢሬዘር (Eraser)*](/am/glossary#Eraser)  በድራይቭ ውስጥ አገልግሎት ላይ ያልዋሉ ቦታዎችን (unallocated space) እየመረጠ [*ለማንጻት/ዋይፕ (wipe)*](/am/glossary#Wiping) የሚችልበት አሠራር አስቀድሞ የተደመሰሱ (previously-deleted) ይዘቶችን/መረጃዎችን ብቻ እየመረጠ [*የሚያነጻ/ዋይፕስ (wipes)*](/am/glossary#Wiping) በመሆኑ ብዙ የሚየሰጋ አይደለም። የተለመዱ የሚታዩ ፋይሎች አንዳችም የሚሆኑት ነገር የለም፤ አይነኩም። በሌላ በኩል ግን፣ ይህ እውነታ ራሱ ሌላ ቁም ነገር በትኩረት እንድንመለከት ይጋብዘናል፤ ይኸውም [*ኢሬዘር (Eraser)*](/am/glossary#Eraser) ያልተደመሰሱ ስሱ መረጃዎችን እንደማያጠፋልን ማወቅ ነው፤ ርቀው የተደበቁ ፋይሎችንም እንዲሁ። ስሱ መረጃዎችን የያዙ ፋይሎች በማይታዩ ፎልደሮች ውስጥ ተቀምጠው ይሆናል፤ ሆን ተብሎ በተሳሳተ ወይም ትርጉም በማይሰጥ የፋይል ስም ተቀምጠውም ሊሆን ይችላል። ይህ ጉዳይ ኤሌክትሮኒክ ዶክመንቶችን በተመለከተ ብዙ የሚያሳስብ አይደለም፤ ነገር ግን ኮምፒውተራችንን እየተጠቀምን እያለ ለምንሰበስባቸው/ለምናገኛቸው (ጊዜያዊ) መረጃዎች ደኅንነት ግን በጣም አስፈላጊ ነው። ለዚህ ጥቂት ምሳሌዎች እንጥቀስ፤    
 
 - የኢንተርኔት ማሰሻችን (browser) የሚመዘግባቸው ጊዜያዊ መረጃዎች/ዳታ ይኖራሉ። ይህም የጎበኘናቸውን ድረ ገጾች፣ የተጠቃሚ መግቢያ መረጃዎች (account information)፣ ኦንላይን ቅጾችን ለመሙላት የተጠቀምንባቸውን ግላዊ መረጃዎች፣ በድረ ገጾች ያየናቸውን ምስሎችና ጽሑፎች፣  [*ኩኪስ (cookies)*](/am/glossary#Cookie)  ሁሉ ይጨምራል። 
 
 - በኮምፒውተራችን ላይ የምንሠራውን ነገር እንዲቀመጥ ከማዘዛችን (ሴቭ ከማድረጋችን) በፊት ኮምፒውተራችን ሥራ ቢያቆም፣ ይህን ፋይል  መልሰን እንድናገኘው የሚረዱን፣ ፋይሉን በጊዜያዊነት የሚያስቀምጡልን አፕሊኬሽኖች አሉ። እነዚህ በጊዜያዊነት የተቀመጡ ፋይሎች ጽሑፎች፣ ምስሎች፣ የሌሎች ፋይሎች ስም፣ ወይም ሌሎች ስሱ መረጃዎችን የያዙ ሊሆኑ ይችላሉ።

 - ዊንዶውስ ለተጠቃሚዎቹ ሥራ ለማቅለል ሲል ብዙ ጊዜ የምንጠቀምባቸውን ፋይሎች እና ሊንኮች (መተላለፊያ) ያጠራቅማል፤ ለምሳሌ በቅርቡ የተጠቀምንበትን/የከፈትነውን አፕሊኬሽን አቋራጭ መክፈቻ (shortcuts)፣  የፎልደር መክፈቻ መተላለፊያዎችን (ፎልደሩ ምናልባት እንዲታይ አንፈልግ ይሆናል)፣ እና ሳናነጻ የረሳነውን <b>ሪሳይክል ቢን (Recycle Bin)</b> ሁሉ ዊንዶውስ ያጠራቅመዋል።

 - የዊንዶውስ [*ስዋፕ ፋይል (swap file)*](/am/glossary#Swap_file)። የኮምፒውተራችን መረጃ ማጠራቀሚያ (computer's memory) ሲሞላ፣ ለምሳሌ በአሮጌ ኮምፒውተር ብዙ ፕሮግራሞችን በአንድ ጊዜ ስንከፍትበት፣ ዊንዶውስ እየተጠቀምንበት ያለውን መረጃ/ዳታ ቀድቶ ወደ አንድ ትልቅ ፋይል የሚገለብጥበት ጊዜ አለ። ይህ በዚህ አይነቱ ወቅት የሚፈጠረው ትልቅ ፋይል የዊንዶውስ [*ስዋፕ ፋይል(swap file)*](/am/glossary#Swap_file)  ይባላል። ይህ ፋይል የተጠቀምንበትን ማንኛውንም መረጃ በሙሉ ይዞ ሊገኝ ይችላል፤ ለምሳሌ ድረ ገጾችን፣ የዶክመንቶቻችንን ይዘት፣ የይለፍ ቃሎችን፣ የኢንክሪፕሽን ቁልፎችን…። ኮምፒውተራችንን ስንዘጋም ቢሆን [*ስዋፕ ፋይል(swap file)*](/am/glossary#Swap_file) አይጠፋም፤ ስለዚህም ራሳችን ማንጻት (wipe) አለብን። 


እነዚህን የመሳሰሉ ጊዜያዊ ፋይሎችን ከኮምፒውተራችን ላይ ጠራርጎ ለማጥፋት [*ሲክሊነር (CCleaner)*](/ am/glossary#CCleaner)  የተባለውን በነጻ የሚገኝ መሣሪያ/ሶፍትዌር መጠቀም ይኖርብናል። ሲክሊነር ስሱ መረጃዎችን አጋልጠው ሊሰጡብን የሚችሉትን ኢንተርኔት ኤክስፕሎረር፣ ሞዚላ  [*ፋየርፎክስ (Firefox)*](/am/glossary#Firefox) እና ማይክሮሶፍት ኦፊስን የመሳሰሉ አፕሊኬሽኖችን እና ዊንዶውስን ራሱን ለማጻዳት ተብሎ የተሠራ ሶፍትዌር ነው። ኮምፒውተራችንን ተጠቅመን በጨረስን ቁጥር [*ኢሬዘርን (/Eraser)*](/am/glossary#Eraser) በመጠቀም አገልግሎት ላይ ያልዋሉ ቦታዎችን አድኖ  [*ከማንጻት/ዋይፕ (wipe)*](/am/glossary#Wiping) ይልቅ [*ሲክሊነር (CCleaner)*](/am/glossary#CCleaner)  ፋይሎችን በአስተማማኝ መንገድ የማጽዳት ብቃት አለው።


<div class="getstarted" markdown="1">

አጠቃቀም! [*ሲክሊነር - አስተማማኝ የፋይል አጠፋፍ እና የጊዜያዊ መረጃዎች አነጻጽ መመሪያ (CCleaner  - Secure File Deletion and Work Session Wiping Guide)*](/en/ccleaner_main)

</div>
