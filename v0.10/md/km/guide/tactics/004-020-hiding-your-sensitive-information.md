

---

lang: km
community: guide
type: tactics
legacy: True
child: True
weight: 2
depth: 3
title: Hiding your sensitive information

---

បញ្ហាមួយនៃការទុកទូដែកមួយនៅក្នុងផ្ទះ ឬក្នុងការិយាល័យរបស់លោកអ្នកគឺថា វាត្រូវបានគេមើលឃើញយ៉ាងច្បាស់។ មនុស្សជាច្រើនមានក្តីបារម្ភសមហេតុផល អំពីការធ្វើពិរុទ្ធកម្មខ្លួនឯង តាមរយៈការប្រើវិធីសាស្ត្រ [*កូដនីយកម្ម*](/km/glossary#Encryption)។ ទោះបីជាហេតុផលស្របច្បាប់ដើម្បីធ្វើ[*កូដនីយកម្ម*](/km/glossary#Encryption) មានចំនួនច្រើនជាងហេតុផលមិនស្របច្បាប់ក៏ដោយ ក៏វាមិនអាចធ្វើឲ្យការគំរាមកំហែងនេះថយចុះដែរ។ ជាសំខាន់ មានហេតុផលពីរដែលលោកអ្នកប្រហែលជាលែងចង់ប្រើកម្មវិធីដូចជា [*TrueCrypt*](/km/glossary#TrueCrypt) នេះទៀត៖ គឺហានិភ័យនៃការធ្វើពិរុទ្ធកម្មខ្លួនឯង និងហានិភ័យនៃការឲ្យគេរកឃើញទីតាំងយ៉ាងច្បាស់នៃព័ត៌មានរសើបបំផុតរបស់លោកអ្នក។

### ការពិចារណាអំពីហានិភ័យនៃការធ្វើពីរិទ្ធកម្មខ្លួនឯង ###
[*កូដនីយកម្ម*](/km/glossary#Encryption) គឺខុសច្បាប់នៅក្នុងប្រទេសមួយចំនួន ដែលមានន័យថា ការដោនឡូត ការបញ្ចូល ឬការប្រើកម្មវិធីកុំព្យូទ័រប្រភេទនេះ អាចជាបទឧក្រិដ្ឋមួយ។ ហើយ ប្រសិនបើអង្គភាពនគរបាល អង្គភាពយោធា ឬអង្គភាពស៊ើបការណ៍បានបន្លំខ្លួននៅក្នុងចំណោមក្រុមមនុស្សដែលលោកអ្នកកំពុងសុំឲ្យជួយការពារព័ត៌មានរបស់លោកអ្នកនោះ នោះការរំលោភច្បាប់ទាំងនេះអាចផ្តល់ជាលេសមួយ ដែលសកម្មភាពរបស់លោកអ្នកអាចនឹងត្រូវបានស៊ើបអង្កេត ឬអង្គការរបស់លោកអ្នកអាចនឹងត្រូវបានធ្វើទុក្ខបុកម្នេញ។ ប៉ុន្តែ តាមពិត ការគំរាមកំហែងដូចនេះ អាចនឹងមិនមានពាក់ព័ន្ធអ្វី ជាមួយនីត្យានុកូលភាពរបស់កម្មវិធីនេះឡើយ។ ការដែលជាប់ទាក់ទងជាមួយកម្មវិធី [*កូដនីយកម្ម*](/km/glossary#Encryption) អាចជាលេសគ្រប់គ្រាន់ដើម្បីចោទប្រកាន់អ្នកអំពីសកកម្មភាពឧក្រិដ្ឋ ឬចារកម្មមួយ(ដោយមិនគិតពីអ្វីដែលមានជាក់ស្តែងនៅក្នុងប្រអប់ [*កូដនីយកម្ម*](/km/glossary#Encryption)របស់លោកអ្នកឡើយ)រួចទៅហើយ  ដូច្នេះអ្នកត្រូវតែគិតឲ្យបានច្បាស់លាស់ថា តើកម្មវិធីបែបនេះសមស្របសម្រាប់ស្ថានភាពរបស់លោកអ្នកដែរឬទេ។

ប្រសិនបើមានករណីនោះមែន លោកអ្នកមានជម្រើសមួយចំនួនដូចខាងក្រោម៖

- លោកអ្នកអាចជៀសវាងប្រើប្រាស់ទាំងស្រុង នូវកម្មវិធីរក្សាសុវត្ថិភាពទិន្នន័យ ដែលប្រហែលនឹងតម្រូវឲ្យលោកអ្នករក្សាទុកតែព័ត៌មានមិនសម្ងាត់ ឬ ច្នៃបង្កើតប្រព័ន្ធពាក្យកូដមួយដើម្បីការពារធាតុគន្លឹះនៃឯកសាររសើបរបស់លោកអ្នក។
- លោកអ្នកអាចពឹងផ្អែកទៅលើបច្ចេកទេសមួយដែលមានឈ្មោះថា [*Steganography (ស្តែហ្គាណូហ្គ្រាហ្វី)*](/km/glossary#Steganography) ដើម្បីលាក់ព័ត៌មានរសើបរបស់លោកអ្នក ជាជាងធ្វើកូដនីយកម្មវា។ មានកម្មវិធីជាច្រើនដែលអាចជួយធ្វើការនេះបាន ប៉ុន្តែការប្រើកម្មវិធីទាំងនេះឲ្យបានត្រឹមត្រូវ តម្រូវឲ្យមានការរៀបចំដោយប្រុងប្រយ័ត្នបំផុតជាមុន ប៉ុន្តែលោកអ្នកនៅតែមានហានិភ័យធ្វើពិរុទ្ធកម្មខ្លួនឯងនៅក្នុងភ្នែករបស់អ្នកដែលស្គាល់កម្មវិធីដែលលោកអ្នកបានប្រើដដែល។
- លោកអ្នកអាចសាកល្បងរក្សាទុកព័ត៌មានរសើបទាំងអស់របស់លោកអ្នក នៅក្នុងគណនីវែបមែលមានសុវត្ថិភាពមួយ ប៉ុន្តែការនេះតម្រូវឲ្យមានការភ្ជាប់បណ្តាញមួយដែលអាចទុកចិត្តបាន និងការយល់ដឹងលម្អិតគួរសមមួយអំពីកុំព្យូទ័រ និងសេវាអ៊ីនធើរណែត។ បច្ចេកទេសនេះសន្មតផងដែរថា [*កូដនីយកម្ម*](/km/glossary#Encryption) កម្រិតបណ្តាញកុំព្យូទ័រ បង្ករពិរុទ្ធកម្មតិចជាង [*កូដនីយកម្ម*](/km/glossary#Encryption)កម្រិតឯកសារ ហើយលោកអ្នកអាចជៀសវាងបាននូវការចម្លងទិន្នន័យរសើបដោយចៃដន្យទៅក្នុង Hard Drive និងទុកទិន្នន័យចោលនៅទីនោះផងដែរ។
- លោកអ្នកអាចរក្សាព័ត៌មានរសើបនៅក្រៅកុំព្យូទ័រ ដោយទុកវានៅក្នុងអង្គចងចាំUSB ឬ Hard Driveចល័ត។ ប៉ុន្តែ ឧបករណ៍បែបនេះ ជាទូទៅមានហានិភ័យជាងកុំព្យូទ័រក្នុងការបាត់បង់ និងការរឹបអូស។ ដូច្នេះ យកតាមខ្លួននូវព័ត៌មានរសើប និងការមិនធ្វើកូដនីយកម្មពួកវារបៀបនេះ ជាទូទៅមិនមែនជាយោបល់ល្អឡើយ។

	
ប្រសិនបើចាំបាច់ លោកអ្នកអាចប្រើស្នៀតយុទ្ធសាស្ត្រទាំងនេះបាន។ ប៉ុន្តែ បើទោះជានៅក្នុងកាលៈទេសៈដែលលោកអ្នកបារម្ភអំពីការធ្វើពិរុទ្ធកម្មខ្លួនឯងក៏ដោយ ការប្រើកម្មវិធី [*TrueCrypt*](/km/glossary#TrueCrypt) អាចនឹងមានសុវត្ថិភាពបំផុតផងដែរ បើសិនជាលោកអ្នកអាចលាក់បាំងប្រអប់ [*កូដនីយកម្ម*](/km/glossary#Encryption) របស់លោកអ្នកបានល្អបំផុតនោះ។

ប្រសិនបើចង់ធ្វើឲ្យប្រអប់កូដនីយកម្មរបស់លោកអ្នកមិនសូវមានភាពសង្ស័យ លោកអ្នកអាចកែឈ្មោះវាឲ្យមើលទៅដូចជាប្រភេទឯកសារផ្សេងទៀតបាន។ ការប្រើកន្ទុយពាក្យសម្គាល់ប្រភេទឯកសារ'.iso' ដើម្បីបន្លំវាជារូបភាពCDមួយ គឺជាជម្រើសដែលល្អសម្រាប់ទំហំប្រអប់ទិន្នន័យប្រមាណ៧០០មេហ្គាបៃផងដែរ។ កន្ទុយពាក្យសម្គាល់ប្រភេទឯកសារផ្សេងៗទៀត អាចនឹងប្រើបានសមរម្យសម្រាប់ប្រអប់ទិន្នន័យដែលទំហំតូចជាងនេះ។ ការធ្វើដូចនេះ គឺមានប្រៀបដូចជាការលាក់ទូដែក នៅខាងក្រោយផ្ទាំងគំនូរដែលព្យួរនៅលើជញ្ជាំងការិយាល័យរបស់អ្នក។ វាប្រហែលជាមិនអាចលាក់បានពីការត្រួតពិនិត្យល្អិតល្អន់នោះទេ ប៉ុន្តែវាអាចផ្តល់នូវការការពារបានខ្លះ។ ដូចគ្នានេះផងដែរ លោកអ្នកអាចផ្លាស់ប្តូរឈ្មោះកម្មវិធី [*TrueCrypt*](/km/glossary#TrueCrypt) ហើយរក្សាវាទុកដូចជាឯកសារធម្មតាមួយ នៅក្នុង Hard Drive ឬអង្គចងចាំUSBរបស់លោកអ្នក ជាជាងបញ្ចូលវាក្នុងលក្ខណៈជាកម្មវិធីមួយ។ [***មគ្គុទ្ទេសក៍ណែនាំអំពី កម្មវិធីTrueCrypt***](/km/truecrypt_main) មានពន្យល់អំពីរបៀបធ្វើការនេះ។


### ការពិចារណាអំពីហានិភ័យ នៃការរកឃើញព័ត៌មានរសើបរបស់លោកអ្នក ###
ជាញឹកញាប់ លោកអ្នកប្រហែលជាមិនសូវបារម្ភច្រើន អំពីផលវិបាកនៃ'ការដែលត្រូវបានចាប់ខ្លួន' ដោយសារកម្មវិធី [*កូដនីយកម្ម*](/km/glossary#Encryption) នៅក្នុងកុំព្យូទ័រ ឬអង្គចងចាំUSB របស់លោកអ្នក ច្រើនដូចការព្រួយបារម្ភអំពីការបង្ហាញពីទីកន្លែងដែលលោកអ្នករក្សាទុកព័ត៌មានដែលលោកអ្នកចង់ការពារបំផុតនោះឡើយ។ វាអាចជាការពិតដែលថាមិនមាននរណាម្នាក់ផ្សេងទៀតអាចអានវាបាននោះទេ ប៉ុន្តែជនឈ្លានពាននឹងដឹងថាវានៅកន្លែងណា នឹងដឹងថាលោកអ្នកបានចាត់វិធានការដើម្បីការពារវា។ ចំណុចនេះធ្វើឲ្យលោកអ្នកប្រឈមទៅនឹងហានិភ័យមួយចំនួន ដែលក្នុងនោះ ជនឈ្លាមពានអាចនឹងព្យាយាមចូលយកឲ្យព័ត៌មានឲ្យបានតាមមធ្យោបាយដូចជាការបំភិតបំភ័យ ការគំរាមហែកកេរ្តិ៍ ការសួរចម្លើយ និងការធ្វើទារុណកម្មជាដើម។ នៅក្នុងបរិបទនេះហើយ ដែលមុខងារ‘Deniability’របស់កម្មវិធី [*TrueCrypt*](/km/glossary#TrueCrypt) ដែលនឹងយកពិភាក្សាលម្អិតបន្ថែមនៅខាងក្រោមនេះ នឹងត្រូវដើរតួសំខាន់។ 


មុខងារ ‘Deniability’ របស់កម្មវិធី [*TrueCrypt's*](/km/glossary#TrueCrypt) គឺជាវិធីសាស្ត្រមួយក្នុងចំណោមវិធីសាស្ត្រទាំងឡាយ ដែលលើសពីអ្វីដែលកម្មវិធី [*កូដនីយកម្ម*](/km/glossary#Encryption) ទូទៅអាចផ្តល់ឲ្យ។ មុខងារនេះ អាចត្រូវបានគិតថា ជាទម្រង់ពិសេសមួយរបស់ [*Steganography*](/km/glossary#Steganography) ដែលបន្លំព័ត៌មានរសើបបំផុតរបស់លោកអ្នក ទៅជាទិន្នន័យដែលមានលក្ខណៈរសើបតិច និងលាក់កំបាំង។ វាស្រដៀងគ្នាទៅនឹងការបញ្ឆោត'បាតក្លែងក្លាយ'នៅក្នុងទូដែកនៃការិយាល័យរបស់អ្នកយ៉ាងដូច្នោះដែរ។ ប្រសិនបើជនអាក្រក់លួចយកកូនសោររបស់លោកអ្នក ឬសម្លុតលោកអ្នកឲ្យផ្តល់លេខសម្ងាត់ទូដែក ជននោះនឹងរកឃើញតែសម្ភារៈ'បញ្ឆោត'តែប៉ុណ្ណោះ ប៉ុន្តែមិនអាចឃើញព័ត៌មានដែលលោកអ្នកកំពុងព្យាយាមការពារពិតប្រាកដនោះទេ។

មានតែលោកអ្នកប៉ុណ្ណោះដែលដឹងថា ក្នុងទូដែករបស់ខ្លួនមានថតសម្ងាត់មួយនៅខាងក្រោយ។ ចំណុចនេះ អាចឲ្យលោកអ្នក'បដិសេធ'បានថា លោកអ្នកមិនមានរក្សាការសម្ងាត់លើសពីអ្វីដែលលោកអ្នកបានបង្ហាញនោះទេ ហើយប្រហែលជាអាចជួយការពារលោកអ្នក នៅក្នុងស្ថានភាពដែលលោកអ្នកត្រូវបានបង្ខំឲ្យផ្តល់ពាក្យសម្ងាត់សម្រាប់ហេតុផលណាមួយផងដែរ។ ហេតុផលទាំងនោះ អាចរួមមានដូចជាការគំរាមកំហែងផ្នែកច្បាប់ ឬរូបវន្ត ចំពោះសុវត្ថិភាពផ្ទាល់របស់លោកអ្នក ឬសុវត្ថិភាពរបស់សហសេវិក សហការី មិត្តភក្តិ និងសមាជិកគ្រួសាររបស់លោកអ្នកជាដើម។ គោលបំណងរបស់មុខងារ'Deniability' គឺផ្តល់ឲ្យលោកអ្នកនូវឱកាសគេចផុតពីស្ថានភាពគ្រោះថ្នាក់ខ្លាំងខ្លាមួយ ទោះបីលោកអ្នកជ្រើសរើសបន្តការពារទិន្នន័យរបស់ខ្លួនក៏ដោយ។ ប៉ុន្តែ ដូចដែលត្រូវបានពិភាក្សានៅក្នុងផ្នែក [***ការពិចារណាអំពីហានិភ័យធ្វើពិរុទ្ធកម្មខ្លួនឯង***](#Considering_the_risk_of_self-incrimination) មុខងារពិសេសនេះមិនសូវជាមានប្រយោជន៍នោះទេ ប្រសិនបើការគ្រាន់តែមានទូដែកមួយក្នុងការិយាល័យរបស់លោកអ្នក គ្រប់គ្រាន់នឹងនាំផលវិបាកដែលមិនអាចទទួលយកបានមួយដល់អ្នកហើយនោះ។


មុខងារ'Deniability'របស់កម្មវិធី [*TrueCrypt's*](/km/glossary#TrueCrypt) ធ្វើការ ដោយរក្សាទុក'ប្រអប់កំបាំង'មួយនៅខាងក្នុងប្រអប់ [*កូដនីយកម្ម*](/km/glossary#Encryption) ធម្មតារបស់លោកអ្នក។ លោកអ្នកបើកប្រអប់កំបាំងនេះ ដោយប្រើនូវពាក្យសម្ងាត់មួយផ្សេងពីពាក្យសម្ងាត់ដែលលោកអ្នកប្រើប្រាស់តាមធម្មតា។ ទោះបីជនអាក្រក់ដែលមានភាពល្អិតល្អន់ខាងបច្ចេកទេសណាម្នាក់ អាចចូលទៅក្នុងប្រអប់ស្តង់ដារបានក៏ដោយ ក៏ជននោះនឹងមិនអាចរកឃើញថា មានប្រអប់សម្ងាត់លាក់កំបាំងមួយនៅក្នុងនោះដែរ។ ពិតណាស់ ជននោះអាចដឹងយ៉ាងច្បាស់ថា  កម្មវិធី [*TrueCrypt*](/km/glossary#TrueCrypt) មានសមត្ថភាពអាចលាក់ព័ត៌មានតាមមធ្យោបាយនេះ ដែលដោយហេតុនេះហើយ ការគំរាមកំហែងនេះមិនធានាថា ត្រូវបានបញ្ចប់ភ្លាមៗ បន្ទាប់ពីលោកអ្នកបើកបង្ហាញពាក្យសម្ងាត់បញ្ឆោតរបស់លោកអ្នកឡើយ។ ប៉ុន្តែ មនុស្សជាច្រើនប្រើកម្មវិធី [*TrueCrypt*](/km/glossary#TrueCrypt)  ដោយមិនបើកដំណើរការមុខងារ'Deniability'នេះឡើយ ហើយជាទូទៅ  គេក៏មិនអាចកំណត់ ឬវិភាគបានថា តើប្រអប់ [*កូដនីយកម្ម*](/km/glossary#Encryption) មួយមាន'បាតបញ្ឆោត'ប្រភេទនេះដែរឬអត់នោះឡើយ។ វាគឺជាការងាររបស់លោកអ្នក ដែលត្រូវប្រាកដថា លោកអ្នកមិនលាតត្រដាងប្រអប់កំបាំងរបស់លោក អ្នកតាមរយៈមធ្យោបាយមិនសូវមានបច្ចេកទេសឡើយ ដូចជាការទុកឲ្យវាបើកចំហចោល ឬអនុញ្ញាតឲ្យកម្មវិធីផ្សេងទៀតបង្កើត Shortcut (ស្ហតខាត់) សម្រាប់ឯកសារដែលមាននៅក្នុងវាជាដើម។ ផ្នែក [***សេចក្តីសម្រាប់អានបន្ថែម***](/km/chapter_4_3)ខាងក្រោមនេះ អាចចង្អុលបង្ហាញលោកអ្នកនូវព័ត៌មានបន្ថែមអំពីបញ្ហានេះ។

<div class="background" markdown="1">
ក្លូដ្យា៖ ត្រូវហើយ ដូច្នេះតោះយើងដាក់ឯកសារមិនបានការខ្លះទៅក្នុងប្រអប់ស្តង់ដារ ហើយបន្ទាប់មក យើងអាចយកឯកសារសក្ខីភាពទាំងអស់របស់យើងទៅដាក់ក្នុងប្រអប់កំបាំង។ តើឯងមានឯកសារPDFsចាស់ៗខ្លះ ឬអ្វីមួយដែលយើងអាចប្រើបានឬទេ?

ប៉ាប្លូ៖ ល្អ ខ្ញុំកំពុងតែគិតអំពីរឿងនេះដែរ។ ខ្ញុំមានន័យថា គំនិតសម្រាប់យើងគឺ លះបង់ពាក្យសម្ងាត់បញ្ឆោត     ប្រសិនបើយើងគ្មានជម្រើសផ្សេង តើត្រូវទេ? ប៉ុន្តែ ដើម្បីធ្វើឲ្យគេជឿជាក់លើរឿងនេះ យើងចាំបាច់ត្រូវធ្វើឲ្យឯកសារទាំងនោះមើលទៅដូចជាឯកសារសំខាន់អញ្ចឹង តើឯងគិតអញ្ចឹងទេ? បើមិនអញ្ចឹងទេ ហេតុអ្វីយើងចាំបាច់ខ្វល់ខ្វាយអំពីការធ្វើកូដនីយកម្មពួកវា? ប្រហែលយើងគួរប្រើឯកសារហិរញ្ញវត្ថុមិនសំខាន់មួយចំនួន ឬបញ្ជីពាក្យសម្ងាត់គេហទំព័រមួយ ឬអ្វីមួយហើយ។
</div>

