

---

lang: vi
community: guide
type: tactics
legacy: True
child: False
weight: 004
title: 4. How to protect the sensitive files on your computer

---

Một ‘kẻ xâm nhập’ có thể truy cập dữ liệu trên máy tính hay các thiết bị lưu trữ lưu động của bạn từ xa qua mạng Internet; hay hắn có thể xâm nhập trực tiếp phần cứng hệ thống của bạn. Bạn có thể tự bảo vệ mình chống lại các nguy cơ trên bằng cách tăng cường bảo mật hệ thống phần cứng và mạng cho dữ liệu của bạn, như đã được đề cập ở [***Chương 1: Làm thế nào để bảo vệ máy tính của bạn khỏi phần mềm độc hại và tin tặc***](/vi-chuong1)) và [***Chương 2: Làm sao để bảo vệ thông tin của bạn khỏi những nguy cơ vật lý trực tiếp***](/vi/chuong-2). Luôn là tốt nhất khi có một vài tầng bảo vệ, chính vì vậy bạn cũng cần có tầng bảo vệ chính các tệp dữ liệu. Bằng cách đó, dữ liệu tối mật của bạn có khả năng được an toàn ngay cả khi các các nỗ lực bảo mật khác không được đáp ứng.

Có hai cách tiếp cận chung cho các vấn đề về bảo mật dữ liệu theo hướng này. Bạn có thể [*mã hóa*](/vi/glossary#Encryption) các tệp dữ liệu, khiến cho chúng không thể đọc được bởi bất kỳ ai khác ngoài bạn, hoặc có thể giấu chúng với hi vọng kẻ xâm nhập không thể tìm thấy các thông tin nhạy cảm. Có một số công cụ giúp bạn theo cả hai hướng tiếp cận, trong đó có [*Phần Mềm Nguồn Mở*](/vi/glossary#FOSS) là [*TrueCrypt*](/vi/glossary#TrueCrypt), là công cụ có thể [*mã hóa*](/vi/glossary#Encryption) và ẩn giấu các tệp dữ liệu của bạn.

### Tình huống cơ bản ###
<div class="background" markdown="1">
Claudia và Pablo làm việc với một tổ chức Phi Chính phủ về nhân quyền ở một nước Nam Mỹ. Họ mất vài tháng để thu thập các bằng chứng từ các nhân chứng về các vi phạm nhân quyền của quân đội tại khu vực họ sinh sống. Nếu những thông tin chi tiết về những nhân chứng này bị tiết lộ, sẽ rất nguy hiểm cho những người đã dũng cảm đưa ra chứng cứ và các thành viên của tổ chức tại khu vực này. Thông tin này hiện được lưu trong một bảng tính tại một máy tính chạy hệ điều hành Windows Xp đặt tại văn phòng và có kết nối với Internet. Claudia nhận thức rất rõ về vấn đề bảo mật, vì vậy cô đã tạo một bản dự phòng dữ liệu trên đĩa CD, và được cất giữ bên ngoài văn phòng.
</div>

### Những điều bạn có thể học được từ chương này ###

- Cách mã hóa thông tin trên máy tính của bạn

- Những vấn đề bạn có thể gặp khi lưu trữ dữ liệu dưới dạng mã hóa

- Làm sao để bảo vệ dữ liệu trên thẻ nhớ USB phòng trường hợp bị mất hay bị đánh cắp

- Những bước cần thực hiện để ẩn giấu dữ liệu khỏi những xâm nhập trực tiếp hay từ xa


