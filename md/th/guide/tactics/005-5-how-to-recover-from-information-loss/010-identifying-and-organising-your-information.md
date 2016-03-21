

---

lang: th
community: guide
type: tactics
legacy: True
child: True
weight: 1
depth: 3
title: Identifying and organising your information

---

ในขณะที่เป็นสิ่งสำคัญที่คุณต้องดำเนินการป้องกันหายนะที่อาจเกิดขึ้นด้วยการทำให้มั่นใจว่าข้อมูลของคุณนั้นมีความปลอดภัยทางกายภาพ ปราศจาก[*มัลแวร์*](glossary#Malware) และได้รับการปกป้องอย่างดีด้วย[*ไฟร์วอลล์*](glossary#Firewall) มีรหัสผ่านที่แข็งแกร่ง แต่เท่านั้นก็ยังไม่เพียงพอ มีอีกหลายอย่างที่อาจก่อให้เกิดความผิดพลาดได้ รวมถึงการโจมตีของไวรัส[*นักเจาะระบบ (hackers)*](/th/glossary#Hacker)ไฟฟ้าลัดวงจร ไฟฟ้ากระชาก น้ำหกใส่ การโจรกรรม การที่เครื่องคอมพิวเตอร์ถูกยึด ปัญหาสภาพความเป็นแม่เหล็กหายไป(demagnetization) ปัญหาระบบปฏิบัติการเสียหาย หรือฮาร์ดแวร์มีปัญหา ซึ่งสิ่งเหล่านี้เป็นเพียงปัญหาตัวอย่างเท่านั้น การเตรียมพร้อมรับมือหายนะก็เป็นสิ่งสำคัญมากเท่ากับการป้องกันเช่นกัน 

<div class="background" markdown="1">
เอลีนา: ฉันรู้ว่าการสำรองข้อมูลนั้นสำคัญนะนิโคไล แต่นั่นไม่ได้หมายความว่า จะมีใครที่สำรองข้อมูลให้ฉันหรือ? หมายความว่า ตัวฉันเองจะมีเวลา ทรัพยากรและความเชี่ยวชาญในการที่จะทำการสำรองข้อมูลด้วยตัวเองจริงๆ หรือ?


นิโคไล: น้าไม่ต้องกังวลครับ การวางแผนสำรองข้อมูลให้ดีนั้นต้องใช้ความคิดมากสักหน่อย แต่ไม่ต้องใช้เวลาหรือเงินมากมายอะไร และเมื่อเปรียบเทียบกับการที่ข้อมูลทั้งหมดของน้าหายไป ก็ยากที่จะบอกว่ามันไม่สะดวกใช่ไหม? นอกจากนี้ แน่นอนว่าการสำรองข้อมูลเป็นเรื่องที่น้าควรทำด้วยตัวเอง เว้นแต่ว่าจะมีคนที่ช่วยเหลือน้าเป็นประจำทางเทคนิคและเชื่อใจได้ที่สุด และรู้ดีที่สุดว่าน้าเก็บข้อมูลดิจิทัลไว้ที่ไหนบ้าง แต่ถ้าน้าจัดการสิ่งเหล่านี้ได้ด้วยตัวเองจะดีที่สุด
</div>

ขั้นแรกของการกำหนด *นโยบายการสำรองข้อมูล* คือการนึกภาพให้ออกว่าคุณเก็บข้อมูลส่วนตัวและข้อมูลงานไว้ที่ไหนบ้าง ตัวอย่างเช่น อีเมลของคุณอาจถูกเก็บอยู่บนเซิร์ฟเวอร์ของผู้ให้บริการเมล อยู่ในคอมพิวเตอร์ของคุณ หรือทั้งสองที่ในคราวเดียวกัน และแน่นอนว่าคุณอาจมีบัญชีอีเมลหลายบัญชี แล้วคุณอาจมีเอกสารที่สำคัญหลายฉบับเก็บอยู่ในคอมพิวเตอร์ที่คุณใช้ ซึ่งอาจอยู่ที่สำนักงานหรือที่บ้าน อาจมีสมุดบันทึกที่อยู่ บันทึกการสนทนา หรือ การตั้งค่าโปรแกรมส่วนตัวไว้ และก็เป็นไปได้ที่ข้อมูลบางอย่างอาจถูกเก็บไว้ในสื่อที่เคลื่อนย้ายได้เช่นกัน แฟลชไดรฟ์ ฮาร์ดไดรฟ์ที่เคลื่อนย้ายได้ ซีดี ดีวีดี หรือ ฟล็อปปี้ดิสก์รุ่นเก่า โทรศัพท์มือถือที่มีรายชื่อ ข้อความสั้นที่สำคัญเก็บไว้ด้วย ถ้าคุณมีเว็บไซต์ เว็บไซต์นั้นอาจมีบทความจำนวนมากที่คุณสะสมมาหลายปี และท้ายสุด อย่าลืมว่าคุณก็มีข้อมูลที่ไม่อยู่ในรูปแบบดิจิทัลด้วย เช่น กระดาษสมุดบันทึก ไดอารี่ และจดหมาย

ขั้นต่อไป คุณต้องกำหนดว่าไฟล์ใดเป็น “เอกสารต้นฉบับ(master copies)” และไฟล์ใดเป็นสำเนาสำรองข้อมูล โดยปกติแล้วเอกสารต้นฉบับจะเป็นเอกสารที่มีการอัปเดดล่าสุดเฉพาะไฟล์หรือ ชุดไฟล์รวมกัน และเกี่ยวเนื่องกับเอกสารที่คุณได้แก้ไขเมื่อต้องการอัปเดดเนื้อหา ที่เห็นได้ชัดคือ จะไม่ใช้การแยกประเภทในกรณีที่คุณมีไฟล์เดียว แต่สำหรับข้อมูลบางประเภทแล้วสำคัญมาก เพราะเหตุการณ์เลวร้ายที่มักเกิดขึ้นบ่อยๆ คือ ในกรณีที่แม้จะสำรองข้อมูลเอกสารสำคัญไว้แล้ว แต่เอกสารต้นฉบับหายไป หรือถูกทำลายก่อนที่จะได้มีการอัปเดดสำเนาสำรองข้อมูลนั้น ตัวอย่างเช่น ลองจินตนาการว่าคุณเดินทางเป็นเวลาสัปดาห์ และการอัปเดดไฟล์สเปรดชีทที่เก็บไว้ในแฟลชไดรฟ์ของคุณด้วยระหว่างนั้น ลักษณะนี้คุณควรเริ่มมองว่าไฟล์นั้นเป็นเอกสารต้นฉบับ เพราะว่าไฟล์เก่าที่มีการทำสำเนาอัตโนมัติตามระยะเวลาที่เก็บอยู่ในคอมพิวเตอร์ที่สำนักงาน ตอนนี้กลายเป็นไฟล์ที่ไร้ประโยชน์ไปแล้ว


ลองเขียนว่าคุณเก็บเอกสารต้นฉบับและสำเนาสำรองข้อมูลดังกล่าวไว้ที่ไหนบ้าง มันจะช่วยแจกแจงความต้องการของคุณและเริ่มที่จะกำหนดนโยบายการสำรองข้อมูลได้ ตารางด้านล่างเป็นตัวอย่างพื้นฐาน แน่นอนว่ารายการของคุณอาจจะยาวกว่านี้และ มี “อุปกรณ์บันทึกข้อมูล” ซึ่งมี “ประเภทของข้อมูล” มากกว่าหนึ่งประเภท และข้อมูลบางประเภทอาจแสดงอยู่ในหลายอุปกรณ์บันทึกข้อมูลก็ได้


<table border="1">
<tbody>
<tr>
<th>ประเภทข้อมูล</th>
<th>เอกสารต้นฉบับ/สำเนาสำรองข้อมูล</th>
<th>อุปกรณ์บันทึกข้อมูล</th>
<th>สถานที่</th>
</tr>
<tr>
<td>เอกสารอิเล็กทรอนิกส์</td>
<td>เอกสารต้นฉบับ</td>
<td>ฮาร์ดดิสก์ในคอมพิวเตอร์</td>
<td>สำนักงาน</td>
</tr>
<tr>
<td>เอกสารอิเล็กทรอนิกส์ที่สำคัญจำนวนเล็กน้อย</td>
<td>เอกสารสำเนา</td>
<td>แฟลชไดรฟ์</td>
<td>ตัวเอง</td>
</tr>
<tr>
<td>ฐานข้อมูลโปรแกรม (ภาพถ่าย,สมุดบันทึกที่อยู่, ปฏิทิน,ฯลฯ)</td>
<td>เอกสารต้นฉบับ</td>
<td>ฮาร์ดดิสก์ในคอมพิวเตอร์</td>
<td>สำนักงาน</td>
</tr>
<tr>
<td>เอกสารอิเล็กทรอนิกส์จำนวนเล็กน้อย</td>
<td>เอกสารสำเนา</td>
<td>ซีดี</td>
<td>บ้าน</td>
</tr>
<tr>
<td>อีเมลและรายชื่อติดต่อทางอีเมล</td>
<td>เอกสารต้นฉบับ</td>
<td>บัญชีจีเมล </td>
<td>อินเทอร์เน็ต
</td>
</tr>
<tr>
<td>ข้อความสั้น และรายชื่อติดต่อทางโทรศัพท์</td>
<td>เอกสารต้นฉบับ</td>
<td>โทรศัพท์มือถือ</td>
<td>ตัวเอง</td>
</tr>
<tr>
<td>เอกสารกระดาษ (สัญญา,ใบเรียกเก็บเงิน, ฯลฯ)</td>
<td>เอกสารต้นฉบับ</td>
<td>ลิ้นชักโต๊ะทำงาน</td>
<td>สำนักงาน</td>
</tr>
</tbody>
</table>


จากตารางด้านบน คุณจะเห็นว่า

- เอกสารที่จะหลงเหลืออยู่ถ้าฮาร์ดดิสก์คอมพิวเตอร์ที่สำนักงานคุณเสียหาย คือ เอกสารสำเนาที่อยู่ใน แฟลชไดรฟ์และแผ่นซีดีที่บ้านคุณ
- คุณไม่มีสำเนาแบบออฟไลน์ของข้อความหรือบันทึกที่อยู่จากอีเมลเลย ดังนั้นหากคุณลืมรหัสผ่าน (หรือมีใครที่ประสงค์ร้ายเปลี่ยนรหัสผ่านของคุณ) คุณจะเข้าถึงอีเมลไม่ได้อีกต่อไป
- คุณไม่มีสำเนาข้อมูลใดๆ ไว้ในโทรศัพท์มือถือเลย
- คุณไม่มีสำเนาข้อมูลใดๆ ไม่ว่าในรูปแบบดิจิทัล หรือเอกสารแบบกระดาษเช่น สัญญา หรือใบเรียกเก็บเงินเลย
