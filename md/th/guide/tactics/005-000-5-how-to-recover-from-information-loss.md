

---

lang: th
community: guide
type: tactics
legacy: True
child: False
weight: 005
title: 5. How to recover from information loss

---

วิธีการใหม่ๆ ในการเก็บรักษาหรือถ่ายโอนข้อมูลดิจิทัลมีแนวโน้มที่จะทำให้ข้อมูลเหล่านั้นสูญหาย ถูกหยิบฉวย หรือถูกทำลาย งานที่ใช้เวลาทำมานานหลายปีอาจสูญหายในพริบตาด้วยสาเหตุต่างๆ เช่น การโจรกรรม ความประมาทเพียงเสี้ยววินาที การยึดฮาร์ดแวร์คอมพิวเตอร์ หรือเพียงแค่ความไม่เสถียรของเทคโนโลยีเก็บรักษาข้อมูลดิจิทัลในตัวมันเอง มักมีคำกล่าวโดยทั่วไปจากเหล่าผู้ให้บริการช่วยเหลือทางคอมพิวเตอร์มืออาชีพว่า &quot;คำถามไม่ใช่ว่าข้อมูลของคุณจะสูญหาย*หรือไม่* แต่เป็นคำถามที่ว่าข้อมูลเหล่านั้นจะสูญหายไป*เมื่อใด*&quot; ดังนั้น *เมื่อ*มันเกิดขึ้น การที่คุณจะมีข้อมูลที่ทันสมัยที่สุดสำรองไว้และมีเครื่องมือกู้ข้อมูลที่ผ่านการทดสอบอย่างดีไว้อยู่แล้วจึงเป็นสิ่งสำคัญมาก ปกติแล้ววันที่คุณจะนึกถึงความสำคัญของการสำรองข้อมูลก็มักจะเป็นวันที่คุณต้องการที่จะมีสำรองข้อมูลไว้ใช้เสมอ

ถึงแม้ว่าการสำรองข้อมูลจะเป็นองค์ประกอบพื้นฐานที่สุดของการรักษาความปลอดภัยทางคอมพิวเตอร์ การกำหนดนโยบายการสำรองข้อมูลนั้นไม่ได้เรียบง่ายอย่างที่คิด อาจจะมีอุปสรรคที่สำคัญในการวางแผนสำรองข้อมูลด้วยเหตุผลหลายประการ ได่แก่ ความต้องการเก็บรักษาข้อมูลต้นฉบับและข้อมูลสำรองไว้ในที่ตั้งทางกายภาพที่ต่างกัน ความสำคัญในการเก็บข้อมูลสำรองให้เป็นความลับ อุปสรรคในการประสานงานระหว่างผู้คนต่างๆ ซึ่งใช้ข้อมูลร่วมกันผ่านอุปกรณ์เก็บข้อมูลแบบพกพาของตนเอง นอกจากกลวิธีสำรองข้อมูล และการกู้ข้อมูล บทนี้จะได้กล่าวถึงเครื่องมือสองเครื่องมือ คือ[*โคเบียน แบ็คอัป (Cobian Backup)*](/th/glossary#Cobian_Backup) และ[*รีคิววา (Recuva)*](/th/glossary#Recuva)

### สถานการณ์ภูมิหลัง ###
<div class="background" markdown="1">
เอลีนาเป็นนักรณรงค์ด้านสิ่งแวดล้อมในประเทศที่พูดภาษารัสเซีย เธอได้ก่อตั้งเว็บไซต์ซึ่งต้องใช้ภาพจากวีดีโอ แผนที่ และเรื่องราวต่างๆ เพื่อสะท้อนให้เห็นถึงปัญหาการตัดไม้ทำลายป่าอย่างผิดกฎหมายในภูมิภาคนั้น เธอได้เก็บรวบรวมเอกสารต่างๆ ไฟล์สื่อต่างๆ  และข้อมูลทางภูมิศาสตร์เกี่ยวกับการตัดไม้มานานหลายปี และข้อมูลส่วนใหญ่ถูกเก็บไว้ในคอมพิวเตอร์ที่มีระบบปฏิบัติการวินโดวส์เครื่องเก่าๆ ที่อยู่ในสำนักงานที่เธอทำงานอยู่ ในขณะที่เธอออกแบบเว็บไซต์เพื่อเก็บข้อมูลเหล่านี้ เอลีนาคิดถึงความสำคัญของการเก็บรักษาข้อมูลต่างๆ และเริ่มกังวลในกรณีที่เครื่องคอมพิวเตอร์ของเธอได้รับความเสียหาย โดยเฉพาะอย่างยิ่งถ้าเหตุการณ์เหล่านี้เกิดขึ้นก่อนที่เธอจะทำสำเนาใส่ลงไปในเว็บไซต์ได้หมด บางครั้งเพื่อนร่วมงานคนอื่นๆ ในองค์กรก็มาใช้คอมพิวเตอร์ของเธอ ดังนั้นเธอต้องการที่จะเรียนรู้วิธีกู้ไฟล์คืนมา ถ้าเกิดว่ามีใครบังเอิญลบแฟ้มข้อมูลที่เก็บงานของเธอไว้ เธอจึงได้ขอให้นิโคไลซึ่งเป็นหลานของเธอช่วยสอนวิธีสำรองข้อมูล
</div>

### สิ่งที่คุณจะได้เรียนรู้ในบทนี้ ###
- วิธีจัดระเบียบและสำรองข้อมูลของคุณ
- ควรเก็บรักษาข้อมูลสำรองไว้ที่ไหน
- วิธีจัดการข้อมูลสำรองคุณอย่างปลอดภัย
- วิธีกู้ไฟล์ที่ถูกลบโดยบังเอิญกลับคืนมา 
	
