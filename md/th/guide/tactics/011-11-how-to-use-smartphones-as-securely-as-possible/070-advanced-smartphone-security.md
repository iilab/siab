

---

lang: th
community: guide
type: tactics
legacy: True
child: True
weight: 7
depth: 3
title: Advanced Smartphone Security

---

## เข้าถึงสมาร์ตโฟนของคุณเต็มรูปแบบ ##

สมาร์ตโฟนส่วนใหญ่มีความสามารถมากกว่าที่ระบบปฏิบัติการที่ติดตั้งอยู่ ซอฟต์แวร์ที่ติดตั้งมาจากโีรงงาน (เฟิร์มแวร์) หรือโปรแกรมที่ผู้ให้บริการโทรศัพท์อนุญาตให้ใช้ ในทางกลับกัน คำสั่งการทำงานบางอย่างถูก “ล็อค (locked in)” ทำให้ผู้ใช้ไม่สามารถควบคุมหรือเปลี่ยนแปลงคำสั่งเหล่านั้นได้ และเข้าถึงไม่ได้ ส่วนใหญ่แล้วคำสั่งการทำงานนั้นไม่มีจำเป็นต่อผู้ใช้สมาร์ตโฟน อย่างไรก็ตาม มีแอปพลิเคชั่นหรือคำสั่งการทำงานบางตัวที่เพิ่มความปลอดภัยให้กับข้อมูลและการสื่อสารบนสมาร์ตโฟนได้ ขณะเดียวกันมีคำสั่งการทำงานบางตัวที่มีอยู่แต่ลบออกไปเพื่อหลีกเลี่ยงความเสี่ยงเรื่องความปลอดภัยได้


ด้วยเหตุผลนี้และเหตุผลอื่นๆ ผู้ใช้สมาร์ตโฟนบางคนเลือกที่จะควบคุมซอฟต์แวร์และโปรแกรมต่างๆ ที่ทำงานในสมาร์ตโฟน เพื่อที่จะได้สิทธิที่ทำให้ติดตั้งโปรแกรม เพิ่มความสามารถ ลบมันออก หรือลดคำสั่งการทำงานบางอย่างได้

กระบวนการเอาชนะข้อจำกัดที่ผู้ให้บริการโทรศัพท์มือถือหรือผู้ผลิตระบบปฏิบัติการตั้งขึ้นเรียกว่ารูทติ้ง (rooting) (ในกรณีของเครื่องที่ใช้ระบบแอนดรอยด์) หรือ เจลเบรก (ในกรณีของเครื่องที่ใช้ระบบไอโอเอส เช่น ไอโฟน ไอแพด) โดยปกติแล้วหากรูทติ้งหรือเจลเบรกสำเร็จ คุณจะมีสิทธิติดตั้งและใช้แอปพลิเคชั่นเพิ่มเติม ดัดแปลง หรือ ล็อคการปรับแต่งค่า และมีอำนาจควบคุมพื้นที่เก็บข้อมูลและหน่วยความจำของสมาร์ทโฟนได้ทั้งหมด

**คำเตือน**: รูทติ้งหรือเจลเบรกอาจจะเป็นกระบวนการที่เมื่อดำเนินการแล้ว จะไม่สามารถกลับมาสู่จุดเดิมได้อีก และต้องอาศัยประสบการณ์ในการติดตั้งและปรับแต่งค่าของซอฟต์แวร์ ควรพิจารณาเงื่อนไขต่างๆ ต่อไปนี้:

- มีความเสี่ยงที่ทำให้สมาร์ตโฟนของคุณไม่สามารถกลับมาทำงานอย่างถาวร หรือทำให้มันเป็น “ก้อนอิฐ” ที่ไร้ค่า (bricking)
- ทำให้การรับประกันที่มีกับผู้ผลิตหรือผู้ให้บริการโทรศัพท์มือถือเป็นโมฆะ
- ในบางที่ กระบวนการดังกล่าวอาจผิดกฎหมาย

แต่ถ้าคุณระมัดระวังแล้ว อุปกรณ์ที่รูทติ้งแล้วเป็นหนทางมุ่งตรงไปสู่การไปควบคุมสมาร์ตโฟนให้ปลอดภัยยิ่งขึ้น

### เฟิร์มแวร์ทางเลือก ###

เฟิร์มแวร์หมายถึงโปรแกรมที่เกี่ยวข้องใกล้ชิดกับอุปกรณ์ที่เฉพาะเจาะจง มันอาจทำงานร่วมกับระบบปฏิบัติการของอุปกรณ์นั้น และรับผิดชอบการทำงานขั้นพื้นฐานของฮาร์ดแวร์ในสมาร์ตโฟนของคุณ เช่น ลำโพง ไมโครโฟน กล้อง หน้าจอสัมผัส หน่วยความจำ กุญแจ เสาอากาศ ฯลฯ


ถ้าคุณมีอุปกรณ์แอนดรอยด์ คุณอาจพิจารณาติดตั้งเฟิร์มแวร์ทางเลือกเพื่อควบคุมโทรศัพท์ของคุณได้มากขึ้น มีข้อสังเกตว่า การติดตั้งเฟิร์มแวร์ทางเลือก คุณต้องรูทโทรศัพท์ของคุณ

ตัวอย่างของเฟิร์มแวร์ทางเลือกสำหรับโทรศัพท์ระบบแอนดรอยด์ คือ[**ซายเอนจินมอด (Cyanogenmod)**](http://www.cyanogenmod.com) ซึ่งทำให้คุณสามารถถอนการติดตั้งแอปพลิเคชั่นได้จากโทรศัพท์ของคุณ (กล่าวคือ แอปพลิเคชั่นที่ติดตั้งโดยผู้ผลิตโทรศัพท์ หรือผู้ให้บริการโทรศัพท์ของคุณ) การกระทำเช่นนี้ ลดวิธีที่อุปกรณ์ของคุณจะถูกจับตาดูได้ เช่น เห็นข้อมูลที่ถูกส่งไปยังผู้ให้บริการของคุณโดยที่คุณไม่รู้ตัว 

นอกจากนี้ ซายเอนจินมอดมาพร้อมกับแอปพลิเคชั่น OpenVPN ซึ่งการติดตั้งอาจน่าเบื่อ VPN (เครือข่ายส่วนตัวเสมือน - Virtual Private Network) เป็นหนึ่งในการใช้พร็อกซี่กับการสื่อสารทางอินเทอร์เน็ตของคุณ (ดูด้านล่าง) 

ซายเอนจินมอด ยังมีโหมดการท่องเว็บแบบไม่ระบุนาม (Incognito) ซึ่งจะไม่บันทึกประวัติการท่องเว็บไว้ในสมาร์ตโฟนของคุณ

ซายเอนจินมอดยังมีคุณสมบัติอื่นๆ อีกมากมาย อย่างไรก็ตามอาจจะใช้ไม่ได้กับโทรศัพท์ระบบแอนดรอยด์ทั้งหมด ดังนั้นก่อนจะเริ่มดำเนินการ ให้ตรวจสอบ [รายชื่อของอุปกรณ์ที่รองรับ](http://www.cyanogenmod.com/devices).
 
### การเข้ารหัสกลุ่่มข้อมูลทั้งหมด ###

ถ้าโทรศัพท์ของคุณผ่านการรูทแล้ว คุณอาจพิจารณาเข้ารหัสพื้นที่เก็บข้อมูลทั้งหมด หรือ สร้างกลุ่มข้อมูลในสมาร์ตโฟนเพื่อปกป้องข้อมูลบางอย่างในโทรศัพท์

[**ลุคซ์ เมเนเจอร์ (Luks Manager)**](https://play.google.com/store/apps/details?id=com.nemesis2.luksmanager&hl=en) มีระบบเข้ารหัสกลุ่มข้อมูลที่ง่าย แข็งแรง และได้รับการออกแบบให้ง่ายต่อผู้ใช้งาน เราแนะนำให้คุณติดตั้งเครื่องมือนี้ก่อนจะเก็บข้อมูลสำคัญลงในอุปกรณ์ระบบแอนดรอยด์และให้ใช้เอนคริปต์ โวลลุ่ม (Encrypted Volumes)ที่ ลุคซ์ เมเนเจอร์จัดให้เพื่อเก็บข้อมูลทั้งหมดของคุณ

### เครือข่ายส่วนตัวเสมือน (Virtual Private Network - VPN) ###

VPN มีท่อที่เข้ารหัสตลอดการเชื่อมต่ออินเทอร์เน็ตระหว่างอุปกรณ์ของคุณและเซิร์ฟเวอร์ VPN ช่องทางนี้เรียกว่าท่อ เพราะมันไม่เหมือนการจราจรข้อมูลอื่นๆ ที่มีการเข้ารหัสไว้อย่าง https VPN จะซ่อนบริการ โปรโตคอล และเนื้อหาทั้งหมด เมื่อติดตั้ง VPN แล้วจะหยุดการทำงานเมื่อใดก็ได้

มีข้อสังเกตว่า เพราะการจราจรข้อมูลทั้งหมดของคุณเดินทางผ่านพร็อกซี่หรือเซิร์ฟเวอร์ VPN  สิ่งที่ตัวกลางต้องทำคือ เข้าถึงพร็อกซี่เพื่อที่จะวิเคราะห์กิจกรรมของคุณ ดังนั้นจึงเป็นเรื่องสำคัญที่คุณต้องเลือกบริการพร็อกซี่หรือ VPN อย่างระมัดระวัง ขอแนะนำให้คุณใช้พร็อกซี่ และ/หรือ VPN ที่แตกต่างกันไป เพราะกระจายการส่งข้อมูลของคุณจะช่วยลดผลกระทบจากบริการที่มีการพยายามเข้าถึงได้

เราแนะนำให้ให้ใช้เซิร์ฟเวอร์ [**ไรซ์อัพ VPN (RiseUp VPN)**](https://help.riseup.net/en/vpn) คุณอาจใช้ ไรซ์อัพ VPN บนอุปกรณ์ระบบแอนดรอยด์ได้หลังจากที่ทำการติดตั้ง ซายเอนจินมอด (ดูด้านบน) การตั้งค่าให้เชื่อมต่อกับ ไรซ์อัพ VPN ในกรณีของไอโฟนก็เป็นเรื่องที่ง่ายเช่นกัน – รายละเอียดดู[ที่นี่](https://support.apple.com/kb/HT1424).
