

---

lang: th
community: guide
type: tactics
legacy: True
child: True
weight: 1
depth: 3
title: Selecting and maintaining secure passwords

---

โดยทั่วไป เมื่อคุณต้องการปกป้องอะไรบางอย่าง คุณก็จะล็อกมันไว้ด้วยกุญแจ บ้าน รถยนต์ หรือจักรยานล้วนมีกุญแจที่มีลักษณะกายภาพจับต้องได้ ในขณะที่ไฟล์จะมีกุญแจที่[*เข้ารหัส*](/th/glossary#Encryption) บัตรธนาคารจะมีหมายเลขพิน (PIN number) และบัญชีอีเมล์ก็จะมีรหัสผ่าน กุญแจเหล่านี้ทั้งที่เป็นรูปแบบกายภาพจับต้องได้หรือที่เป็นอิเล็กทรอนิกส์มีสิ่งที่เหมือนกันอยู่ประการหนึ่งคือ ถ้าพวกมันตกอยู่ในมือของบุคคลอื่น มันก็ใช้เปิดล็อกต่างๆตามนั้นได้เช่นกัน คุณติดตั้งไฟร์วอลล์รุ่นที่มีความก้าวหน้าสูง รักษาความปลอดภัยบัญชีอีเมล และ[*เข้ารหัส*](/th/glossary#Encryption)แผ่นดิสก์ไว้ แต่ถ้ารหัสผ่านของคุณอ่อนแอเกินไป หรือคุณยอมให้รหัสผ่านนั้นตกอยู่ในมือที่ผิด การใส่กุญแจต่างๆ ที่กล่าวมาก็ไม่ได้ให้ประโยชน์อะไรกับคุณมากนัก

### องค์ประกอบของรหัสผ่านที่แข็งแรง ###

รหัสผ่านจะต้องยากเกินกว่าที่โปรแกรมคอมพิวเตอร์ที่จะคาดเดาได้

- **สร้างรหัสผ่านให้ยาว:** รหัสผ่านยิ่งยาวมากแค่ไหน ก็ยิ่งเป็นไปได้น้อยที่โปรแกรมคอมพิวเตอร์จะคาดเดาได้ในเวลาอันจำกัด คุณควรพยายามสร้างรหัสผ่านที่รวมตัวอักษรสิบตัวหรือมากกว่านั้น บางคนใช้รหัสผ่านที่มีคำมากกว่าหนึ่งคำ มีหรือไม่มีช่องว่างระหว่างคำเหล่านั้น ซึ่งโดยปกติจะเรียกว่า วลีรหัสผ่าน(passphrase) ซึ่งถือเป็นความคิดที่ดีมาก ตราบเท่าที่โปรแกรม หรือบริการที่คุณใช้งานอยู่ยินยอมให้เลือกรหัสผ่านยาวๆ ได้

- **สร้างรหัสผ่านให้ซับซ้อน:** นอกจากเรื่องความยาวของรหัสผ่านแล้ว ความซับซ้อนของรหัสผ่านก็ช่วยป้องกันไม่ให้ ***ซอฟท์แวร์ถอดรหัสผ่านอัตโนมัติ*** คาดเดาการรวมตัวอักษรอย่างถูกต้องได้ หากเป็นไปได้ คุณควรใช้ตัวอักษรภาษาอังกฤษตัวใหญ่ (upper case) ตัวอักษรภาษาอังกฤษตัวเล็ก(lower case) ตัวเลข และสัญลักษณ์ เช่น เครื่องหมายวรรคตอน ในรหัสผ่านของคุณด้วย

รหัสผ่านจะต้องยากเกินกว่าที่บุคคลอื่นจะคิดออก

- **ปฏิบัติได้จริง:** ถ้าคุณต้องจดรหัสผ่านลงไปเพราะว่าคุณจำรหัสผ่านไม่ได้ คุณอาจจะประสบปัญหาภัยคุกคามทุกประเภททั้งหมด ซึ่งทำให้คุณอ่อนไหวต่อผู้คนที่เห็นโต๊ะทำงานของคุณได้อย่างชัดเจน หรือในบางครั้งเขาอาจเข้าไปในบ้านของคุณ เข้าดูกระเป๋าเงินของคุณ หรือแม้กระทั่งเข้าดูถังขยะที่อยู่นอกสำนักงานของคุณ ถ้าคุณไม่สามารถคิดรหัสผ่านที่ยาวซับซ้อนโดยที่คุณจำได้ หัวข้อ[***การจำรหัสผ่านอย่างปลอดภัย***](/th/chapter_3_2) ด้านล่างอาจจะช่วยคุณได้ หรือถ้ามันไม่ช่วย คุณยังสามารถเลือกใช้รหัสผ่านที่มีความปลอดภัยแต่อาจต้องบันทึกลงไปใน[*ฐานข้อมูลรหัสผ่านอย่างปลอดภัย*](/th/glossary#Secure_password_database) เช่น[*คีพาส (KeePass)*](/th/glossary#KeePass) ไฟล์ที่มีระบบป้องกันด้วยรหัสผ่านประเภทอื่นๆ รวมถึงของไมโครซอฟท์เวิร์ดนั้นไม่น่าเชื่อถือเพียงพอสำหรับกรณีการปกป้องข้อมูลนี้ เนื่องจากว่าไฟล์เหล่านี้สามารถถูกถอดรหัสได้ในไม่กี่วินาทีโดยเครื่องมือที่สามารถหาได้ง่ายๆ บนอินเทอร์เน็ต

- **อย่าใช้รหัสผ่านที่เกี่ยวกับเรื่องส่วนตัว:** รหัสผ่านไม่ควรที่จะเกี่ยวข้องกับเรื่องส่วนตัวของคุณ อย่าเลือกใช้คำหรือวลีที่อยู่บนฐานของข้อมูลชื่อคุณ หมายเลขประกันสังคม หมายเลขโทรศัพท์ ชื่อลูก ชื่อสัตว์เลี้ยง วันเกิด หรืออะไรก็ตามที่บุคคลสามารถรู้ได้ง่ายๆ โดยเพียงแค่ทำการค้นหาข้อมูลเพียงเล็กน้อยเกี่ยวกับคุณ

- **เก็บรหัสผ่านเป็นความลับ:** อย่าใช้รหัสผ่านร่วมกันกับใครทั้งสิ้นเว้นแต่กรณีมีความจำเป็นอย่างยิ่งยวด และถ้าที่คุณจำต้องร่วมใช้รหัสผ่านกับเพื่อน สมาชิกครอบครัว หรือเพื่อนร่วมงาน คุณจะต้องเปลี่ยนรหัสผ่านนั้นเป็นรหัสผ่านชั่วคราว คือ ให้คนอื่นใช้รหัสผ่านชั่วคราวนั้นร่วมกันครั้งหนึ่ง เมื่อพวกเขาใช้งานรหัสผ่านชั่วคราวนั้นเสร็จ ให้คุณเปลี่ยนรหัสผ่านชั่วคราวกลับมาเป็นรหัสผ่านเดิม บ่อยครั้งมีอีกหลายวิธีที่ทำให้สามารถใช้รหัสผ่านร่วมกัน เช่น การสร้างบัญชีแยกต่างหากสำหรับรายบุคคลที่ต้องการเข้าถึง รักษารหัสผ่านของคุณให้เป็นความลับยังหมายถึงการให้ความใส่ใจในกรณีที่อาจมีใครบางคนแอบมองข้ามบ่าคุณระหว่างที่คุณกำลังพิมพ์รหัสผ่าน หรือกำลังดูรหัสผ่านใน [*ฐานข้อมูลรหัสผ่านอย่างปลอดภัย*](/th/glossary#Secure_password_database)

จะต้องเลือกรหัสผ่านเพื่อที่จะลดความเสียหายหากว่ามีใครบางคนรู้รหัสผ่านนั้น

- **ทำให้รหัสผ่านมีความเฉพาะตัว:** หลีกเลี่ยงการใช้รหัสผ่านเดียวกับหลายๆ บัญชี ไม่อย่างนั้นแล้วใครก็ตามที่รู้รหัสผ่านก็จะเข้าถึงข้อมูลของคุณได้ลึกกว่า แม้กระทั่งข้อมูลที่อ่อนไหวของคุณ เพราะมีบริการบางอย่างที่ช่วยให้การถอดรหัสทำได้ง่ายดาย ตัวอย่างเช่น ถ้าคุณใช้รหัสผ่านอันเดียวเพื่อเข้าไปใช้งานวินโดว์สและใช้เข้าบัญชีจีเมลของคุณ ผู้ที่สามารถเข้าถึงคอมพิวเตอร์ของคุณทางกายภาพจะถอดรหัสผ่านสำหรับการใช้งานวินโดว์สและใช้รหัสที่ได้มานั้นเข้าถึงบัญชีจีเมลของคุณได้ ด้วยเหตุผลที่คล้ายกันนี้ การเวียนรหัสผ่านโดยแลกเปลี่ยนรหัสผ่านสำหรับเข้าถึงระหว่างบัญชีที่ต่างกันก็ไม่ใช่ความคิดที่ดีนัก

- **รักษาให้รหัสผ่านใหม่เสมอ:** คุณควรเปลี่ยนรหัสผ่านเป็นประจำ จะให้ดีควรจะเปลี่ยนหนึ่งครั้งทุกสามเดือน บางคนค่อนข้างยึดติดกับรหัสผ่านบางอันและไม่เคยเปลี่ยนมันเลย ซึ่งนี่ก็ไม่ใช่ความคิดที่ดีนัก ยิ่งคุณเก็บรหัสผ่านเดิมไว้นานเท่าใด คนอื่นก็ยิ่งมีโอกาสที่จะล่วงรู้รหัสผ่านของคุณได้มากขึ้นเท่านั้น นอกจากนี้ หากมีใครใช้รหัสผ่านที่ขโมยมาจากคุณเพื่อใช้เข้าถึงข้อมูลหรือบริการของคุณโดยที่คุณไม่รู้ คนเหล่านั้นจะทำเช่นนั้นต่อไปเรื่อยๆจนกว่าคุณจะเปลี่ยนรหัสผ่าน

<div class="background" markdown="1">
แมนซัวร์: จะเป็นอะไรถ้าฉันเชื่อใจบางคน มันจะเหมาะสมไหมถ้าฉันจะบอกรหัสผ่านของฉันให้เธอรู้

แม็กดา: อืม ก่อนอื่นขอบอกว่า การที่เธอบอกรหัสผ่านให้กับคนที่เธอไว้ใจไม่ได้หมายความว่าเธอเชื่อใจว่าบุคคลนั้นจะดูแลรหัสผ่านของเธออย่างดี จริงหรือไม่ ถึงแม้ว่าฉันจะไม่ทำอะไรที่ไม่ดีกับรหัสผ่านของเธอ แต่ฉันอาจจะเขียนมันลงไปแล้วทำมันหายไป ในกรณีนี้นั้นเป็นการทำให้ฉันตกอยู่ในสถานการณ์ยุ่งยากเข้าไปอีก นอกจากนี้เรื่องรหัสผ่านไม่ใช่เรื่องของความเชื่อใจ ถ้าเธอเป็นคนเดียวที่รู้รหัสผ่านของเธอ เธอก็ไม่ต้องเสียเวลาที่ต้องมากังวลโทษว่าเป็นความผิดของใครหากมีการใช้รหัสผ่านนั้นเข้าไปในบัญชี เช่น ตอนนี้ฉันค่อนข้างมั่นใจว่ามีใครที่พยายามคาดเดา หรือ “ถอด” รหัสผ่านของฉันอยู่ เพราะฉันไม่เคยเขียนหรือใช้รหัสผ่านร่วมกับใคร
</div>

