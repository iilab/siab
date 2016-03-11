

---

lang: am
community: guide
type: tactics
legacy: True
child: False
weight: 005
title: 5. How to recover from information loss

---

ዲጂታል መረጃዎችን ለማከማቸት እና ለማስተላለፍ የሚፈጠሩ አዳዲስ ዘዴዎች የመረጃ አያያዝን የሚያሻሽሉትን ያህል መረጃዎች የሚጠፉበት እና የሚበላሹበት እድልም ተያይዞ ሊጨምር ይችላል።  በአንድ ስሕተት ወይም በቸልተኝነት፣ ምናልባትም ኮምፒውተራችን አለዚያ ሌላ የመረጃ ቋታችን ከእጃችን በውጣቱ ለዓመታት የተጠራቀመ መረጃ ሊሰረቅ፣ ሊበላሽ እና ከነጭራሹም ሊጠፋ ይችላል። የዚህ አደጋ ምንጩ ራሱ የዲጂታል የመረጃ ማጠራቀሚያ ቴክኖሎጂ ተፈጥሯዊ ድክመትም ሊሆን ይችላል። በኮምፒውተር ባለሞያዎች ዘንድ አንድ የተለመደ አባባል አለ፤ &quot; ጥያቄው “*ምናልባት ከሆነ* ሳይሆን *ሆኖ ሲገኝ*” የሚል ነው።&quot; በሌላ አነጋገር ጥያቄው “ምናልባት ወደፊት መረጃዎቻችን ቢጠፉብንስ” የሚል ሳይሆን “መረጃዎቻችን መቼ ይጠፋሉ” ነው። መረጃዎቻችንን በድንገት ማግኘት ሲያቅተን፣ ከዚያ አስቀድመን ወዳስቀመጥነው የመጠባበቂያ ክምችት (up-to-date backup) እና የጠፉ መረጃዎችን መልሶ ወደሚያገኝልን (restoring) አሠራር መሔድ ይኖርብናል። በአብዛኛው ስለመጠባበቂያ ክምችት (backup system) አስፈላጊነት የምናስታውስበት ቀን የሚመጣው ዘግይቶ የሚሆንበት አጋጣሚ ሞልቷል፤ “በኖረን ኖሮ” ብለው ከተጸጸቱ በኋላ በአስፈላጊነቱ የሚያምኑ ሰዎች አሉ።

ደኅንነቱ የተጠበቀ የኮምፒውተር አሠራር እንዲኖረን የመጠባበቂያ ክምችት ፖሊሲ (backup policy) እጅግ አስፈላጊ ነው፤ ነገር ግን ይህን ፖሊሲ መቅረጽ ከውጭ ሲያዩት እንደሚመስለው በጣም ቀላል ሥራ አይደለም።  በብዙ ምክንያቶች ይህን እቅድ ማስፈጸም አስቸጋሪ ሊሆን ይችላል፤ የመረጃዎችን የመጀመሪያ/እናት ምንጭ/ቅጂ ሌሎች ቅጂዎች ከተቀመጡበት በተለየ ቦታ ማኖር፣ መጠባበቂያ ክምችቶችን በምሥጢር የማስቀመጥ አስፈላጊነት፣ በየራሳቸው ተንቀሳቃሽ የመረጃ ቋቶች መረጃዎቹን የሚዋዋሱ ሰዎች ካሉ ይህን ማስተባበር ሁሉ የዚሁ አካል ነው። በዚህ ምእራፍ ከመጠባበቂያ ክምችት  የጠፉ ፋይሎችን መልሶ ስለማግኛ ዘዴዎች እናነሣለን። በተጨማሪ  [*ኮቢያን ባክአፕ/Cobian Backup*](/am/glossary#Cobian_Backup) እና  [*አንዴሊት ፕላስ/Undelete Plus*](/am/glossary#Undelete_Plus) የተባሉትን መሣሪዎች በዝርዝር እንተዋወቃለን።


### አስረጅ አጋጣሚ ###


<div class="background" markdown="1">
ሕሊና የአካባቢ ጥበቃ ተቆርቋሪ ናት። በኢትዮጵያ የተለያዩ ቦታዎች የሚገኙ ከአካባቢ ጥበቃ ጋራ የተያያዙ እንቅስቃሴዎችን በፎቶ፣ በቪዲዮ እና በካርታ በታገዘ ሪፖርት ለሕዝቡ ማቅረብ ትፈልጋለች። ከዚሁ ጋይ የተያያዙ ሰነዶችን፣ የሚዲያ ሪፖርቶችን፣ የመልክአ ምድር አመላካች መረጃዎችን ለረጅም ጊዜ ስታሰባስብ ቆይታለች። እነዚህን መረጃዎችም በምትሰራበት ድርጅት ቢሮ ውስጥ በምትጠቀምበት አሮጌ ዊንዶውስ ኮምፒውተር አጠራቅማቸዋለች። በቅርቡ የራሷን መካነ ድር (website) መክፈት ትፈልጋለች፤ ይህን ስታስብ ግን የሰበሰባቻቸውን መረጃዎች ወደ ድረ ገጽ ሳትገለብጥ ኮምፒውተሯ ችግር ቢገጥመው መረጃዎቿ ሊጠፉ እንደሚችሉ አስተውላለች። አንዳንድ ጊዜ ሌሎች የሥራ ባልደረቦቿ የእርሷን ኮምፒውተር የሚጠቀሙ በመሆኑ ፋይሎቿ በስሕተት ቢጠፉባት እንዴት መልሳ ልታገኛቸው እንደምትችል ማወቅ ትፈልጋለች። አሸናፊ የተባለው የቀድሞ የሥራ ባልደረባዋ የመጠባበቂያ ክምችት (ባክአፕ) ስትራቴጂ በማዘጋጀት እንዲረዳት ጠይቃዋለች።            
</div>



### የምእራፉ ዋና ዋና ጭብጦች ###

- መረጃዎችን ማደራጀት እና መጠባበቂያ ቅጂ ማስቀመጥ የሚቻለው እንዴት ነው?
- መጠባበቂያ ቅጂዎቻችንን (ባክአፕስ) ማስቀመጥ የሚገባን የት ነው?
- መጠባበቂያ ቅጂዎቻችንን (ባክአፕስ) ደኅንነታቸው በተጠበቀ ሁኔታ መያዝ ያለብን እንዴት ነው?
-	በስሕተት የተሰረዘ (ዴሊት የተደረገ) መረጃን መልሶ ማግኘት የሚቻለው እንዴት ነው?
