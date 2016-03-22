

---

lang: vi
community: guide
type: tactics
legacy: True
child: True
weight: 3
depth: 3
title: Securing other Internet communication tools

---

Cũng giống như thư điện tử, phần mềm nhắn tin qua mạng và [*VoIP*](/vi/glossary#VoIP) có thể có tính bảo mật hoặc không, tùy thuộc vào công cụ bạn chọn và cách bạn sử dụng chúng.

**Bảo mật phần mềm nhắn tin qua mạng của bạn**

Nhắn tin qua mạng hay còn gọi là ‘chát’, thường không được bảo mật, và có thể dễ bị tấn công cũng như thư điện tử. Rất may mắn là có những chương trình có thể giúp bảo mật sự riêng tư của những phiên chát này. Cũng giống như việc trao đổi dùng thư điện tử, để đảm bảo một kênh thông tin bảo mật đòi hỏi cả hai phía, bạn và đối tác của bạn, sử dụng cùng một phần mềm và cùng có mức độ cảnh giác an ninh như nhau.

Có một chương trình chát tên là [*Pidgin*](/vi/pidgin-main) hỗ trợ rất nhiều giao thức nhắn tin qua mạng, nghĩa là bạn có thể sử dụng ngay chương trình mà không phải thay đổi thông tin tài khoản hay tạo lại danh sách liên lạc của bạn. Để đảm bảo bảo mật, bằng cách [*mã hóa*](/vi/glossary#Encryption) các hội thoại dùng [*Pidgin*](/vi/pidgin-main), bạn cần cài đặt và bật tính năng  [*Không lưu Dấu vết*](/vi/glossary#OTR). May mắn cho bạn vì quá trình này khá đơn giản.

<div class="getstarted" markdown="1">Thực hành: Hãy bắt đầu với [Hướng dẫn sử dụng Pidgin](/vi/pidgin-main)</div>

[**Skype**](/vi/glossary#Skype), một công cụ [*VoIP*](/vi/glossary#VoIP) phổ biến, cũng hỗ trợ nhắn tin qua mạng. Tuy [**Skype**](/vi/glossary#Skype) bảo mật khá hơn một số phần mềm khác không có tính năng  [*Không lưu Dấu vết*](/vi/glossary#OTR), nó lại có hai nhược điểm chính. Thứ nhất nó chỉ cho phép bạn liên lạc với những người dùng **Skype**](/vi/glossary#Skype) khác, trong khi [*Pidgin*](/vi/pidgin-main) có thể được sử dụng để liên lạc một cách an toàn với hầu hết các dịch vụ nhắn tin qua mạng khác. Thứ hai, vì đây là phần mềm có mã nguồn đóng, việc kiểm định tính năng [*mã hóa*](/vi/glossary#Encryption) của nó là không thể. [*Chương 1: Làm thế nào để bảo vệ máy tính của bạn khỏi phần mềm độc hại và hacker*](/vi/chuong-1) trong phần [*Giữ cho phần mềm luôn được cập nhật*](/vi/chuong_1_4) nêu ra những ưu điểm của [*Phần Mềm Nguồn Mở*](/vi/glossary#FOSS*). Nói tóm lại, bạn tốt hơn nên sử dụng  [*Pidgin*](/vi/pidgin-main), với tính năng  [*Không lưu Dấu vết*](/vi/glossary#OTR) (OTR) để đảm bảo bảo mật cho việc nhắn tin qua mạng.

<div class="background" markdown="1">
Pablo: Nếu dịch vụ thư điện tử của Yahoo là không bảo mật vậy điều đó có nghĩa là dịch vụ Chát của Yahoo cũng không an toàn, phải không?

Claudia: Có một điều cần ghi nhớ là, nếu chúng ta muốn sử dụng dịch vụ nhắn tin qua mạng để thảo luận về bản báo cáo này, chúng ta cần phải chắc chắn mọi người tham gia đều sử dụng Pidgin với tính năng OTR được cài đặt. Nếu làm được như vậy, chúng ta có thể sử dụng dịch vụ chát của Yahoo hay bất kỳ dịch vụ chát nào khác. </div>

**Bảo mật phần mềm truyền thoại qua mạng (VoIP) của bạn**

Các cuộc gọi dùng [*VoIP*](/vi/glossary#VoIP) tới những người dùng [*VoIP*](/vi/glossary#VoIP) khác thường là miễn phí. Một số chương trình còn cho phép bạn thực hiện những cuộc gọi tới các số máy điện thoại thông thường, bao gồm cả các cuộc gọi quốc tế, với chi phí rẻ. Không cần phải nói, những tính năng này thực sự rất hữu ích. Một số phần mềm [*VoIP*](/vi/glossary#VoIP) phổ biến nhất hiện nay bao gồm [Skype](http://www.skype.com), [Gizmo](http://www.gizmoproject.com/),  [Google Talk](http://www.google.com/talk) , [Yahoo! Voice](http://voice.yahoo.com/) , và [MSN Messenger](http://get.live.com/messenger).

Thông thường, truyền thoại qua Internet không có tính bảo mật cao hơn so với thư điện tử và nhắn tin qua mạng không được mã hóa. Chỉ có [Skype](http://www.skype.com) và [Gizmo](http://www.gizmoproject.com/) cung cấp sự mã hóa cho việc truyền thoại, nhưng chỉ trong trường hợp bạn thực hiện các cuộc gọi tới các người dùng [*VoIP*](/vi/glossary#VoIP) khác, chứ không phải cho những cuộc gọi tới máy di động hay máy để bàn. Thêm vào đó, không phần mềm nào trong hai phần mềm trên là có mã nguồn mở nên các chuyên gia độc lập không thể thực hiện việc kiểm tra và hoàn toàn chắc chắn rằng chúng được bảo mật.

