

---

lang: th
community: guide
type: tactics
legacy: True
child: False
weight: 004
title: 4. How to protect the sensitive files on your computer

---

การเข้าถึงข้อมูลในคอมพิวเตอร์ของคุณหรืออุปกรณ์เก็บข้อมูลที่พกพาจากระยะไกลได้โดยไม่ได้รับอนุญาตเกิดขึ้นได้ หากว่า “ผู้บุกรุก” อ่านหรือเปลี่ยนแปลงแก้ไขข้อมูลของคุณทางอินเทอร์เน็ต หรือในกรณีที่เขาเข้าถึงฮาร์ดแวร์ของคุณได้ คุณปกป้องตัวเองจากภัยคุกคามไม่ประเภทใดก็ประเภทหนึ่งนี้โดยการปรับปรุงความปลอดภัยทางกายภาพและระบบเครือข่ายให้กับข้อมูลของคุณ อย่างที่ได้อธิบายไปแล้วใน[***บทที่ 1: ปกป้องคอมพิวเตอร์ของคุณจากโปรแกรมประสงค์ร้ายและนักเจาะระบบ***](/th/chapter-1) และ[***บทที่ 2: ปกป้องข้อมูลของคุณจากภัยคุกคามทางกายภาพ***](/th/chapter-2) อย่างไรก็ตาม วิธีที่ดีที่สุดคือ มีแนวป้องกันไว้หลายชั้น ซึ่งเป็นเหตุผลว่าคุณควรปกป้องไฟล์ด้วย  แม้ความพยายามในการตั้งระบบความปลอดภัยอื่นๆ ของคุณจะไม่พอ ก็ยังมีแนวโน้มว่าข้อมูลที่อ่อนไหวของคุณจะปลอดภัยอยู่

โดยทั่วไปแล้ว วิธีป้องกันภัยคุกคามความปลอดภัยของข้อมูลลักษณะนี้มี 2 วิธี คุณสามารถ[*เข้ารหัส(encrypt)*](/th/glossary#Encryption)ไฟล์ของคุณ เพื่อทำให้บุคคลอื่นๆ ไม่สามารถอ่านไฟล์ต่างๆ เหล่านั้นได้ หรือ **คุณสามารถซ่อนไฟล์เหล่านั้น** โดยหวังว่าผู้บุกรุกจะหาข้อมูลอ่อนไหวของคุณไม่เจอ มีเครื่องมือที่จะช่วยให้คุณสามารถดำเนินการวิธีดังกล่าว รวมถึง[*ซอฟต์แวร์เสรีและโอเพนซอร์ส(FOSS)*](/th/glossary#FOSS) ชื่อว่า [*ทรูคริปต์(TrueCrypt)*](/th/glossary#TrueCrypt) ซึ่งสามารถเข้ารหัสและซ่อนไฟล์ของคุณได้

### สถานการณ์ภูมิหลัง ###
<div class="background" markdown="1">
คลาวเดียและปาโบลทำงานในองค์กรพัฒนาเอกชนด้านสิทธิมนุษยชนที่ประเทศหนึ่งในอเมริกาใต้ ทั้งคู่ได้ใช้เวลาหลายเดือนเก็บคำให้การจากพยานต่างๆ เกี่ยวกับการละเมิดสิทธิมนุษยชนที่กระทำโดยทหารในภูมิภาคที่พวกเขาอยู่ ถ้าข้อมูลเกี่ยวกับตัวผู้ให้คำให้การเหล่านี้ถูกเปิดเผยจะทำให้ทั้งผู้กล้าหาญที่ให้คำเบิกความและสมาชิกขององค์กรที่อยู่ในภูมิภาคนั้นตกอยู่ในอันตราย ตอนนี้ข้อมูลเหล่านี้ถูกเก็บไว้ในไฟล์เอกสารสเปรดชีต (spreadsheet) ในคอมพิวเตอร์ขององค์กรซึ่งใช้ระบบปฏิบัติการวินโดวส์เอ็กซ์พี ซึ่งเชื่อมต่อกับอินเทอร์เน็ต คลาวเดียตระหนักถึงเรื่องความปลอดภัยเป็นอย่างดี จึงได้ทำการสำรองข้อมูลทั้งหมดไว้ในแผ่นซีดีซึ่งเธอเก็บไว้นอกสำนักงาน 
</div>

### สิ่งที่คุณจะได้เรียนรู้จากบทนี้ ### 

- รู้วิธี[*เข้ารหัส*](/th/glossary#Encryption) ข้อมูลในคอมพิวเตอร์ของคุณ
- รู้ว่ามีความเสี่ยงอะไรบ้างที่คุณต้องเผชิญจากการเก็บข้อมูลซึ่งเข้ารหัสไว้
- รู้วิธีปกป้องข้อมูลที่อยู่ในแฟลชไดรฟ์ ในกรณีที่มันสูญหายหรือถูกขโมย
- รู้ขั้นตอนซ่อนข้อมูลจากผู้บุกรุกทางกายภาพหรือผู้บุกรุกจากระยะไกล

