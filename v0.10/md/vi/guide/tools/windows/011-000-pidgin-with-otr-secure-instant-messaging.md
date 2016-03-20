

---

lang: vi
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 011
title: Pidgin with OTR - Secure Instant Messaging

---

**Trang chủ**

- **Pidgin**: [**www.pidgin.im**](http://www.pidgin.im)
- **OTR**: [**www.cypherpunks.ca/otr**](http://www.cypherpunks.ca/otr/)

**Yêu cầu cấu hình máy tính**

- Kết nối Internet
- Mọi phiên bản Windows

**Phiên bản sử dụng trong tài liệu này**

- Pidgin 2.7.11 
- OTR 3.2.0.1 

**Bản quyền**

- Phần mềm Nguồn mở và Miễn phí

**Yêu cầu đọc thêm**

- Sách hướng dẫn [chương 7. Đảm bảo bảo mật truyền thông trên Internet](/vi/chuong-7)

Mức độ: 1: Người mới bắt đầu, **2: Trung bình**, 3: Trên trung bình, 4: Có kinh nghiệm, 5: Nâng cao

**Thời gian cần thiết để có thể sử dụng công cụ:** 30 phút

**Những lợi ích bạn sẽ có được:**

- Khả năng sử dụng hầu hết các dịch vụ tin nhắn trực tuyến trên một chương trình
- Khả năng tạo các phiên liên lạc bảo mật và có xác thực

**Các Chương trình có Tính năng Tương tự trên GNU Linux, Mac OS và Microsoft Windows:**

Cả **Pidgin** và **OTR** để có phiên bản cho **Microsoft Windows** và cho **GNU/Linux**. Một chương trình **Nhắn tin Trực tuyến**(**IM**) hỗ trợ đa giao thức hoạt động trên **Microsoft Windows** có hỗ trợ **OTR** là [**Miranda IM**](http://www.miranda-im.org/). Với hệ điều hành **Mac OS** chúng tôi giới thiệu [**Adium**](http://adium.im/), một chương trình  **IM** đa giao thức và hỗ trợ tiện ích **OTR**.

## 1.1 Things you should know about this tool before you start ##

**Pidgin** là một chương trình nguồn mở cho phép bạn sử dụng và quản lý nhiều tài khoản của các dịch vụ **Nhắn tin Trực tuyến** (**IM**) khác nhau sử dụng chung một giao diện duy nhất. Trước khi bắt đầu sử dụng **Pidgin**, bạn cần phải có một tài khoản **IM**. Lấy ví dụ, nếu bạn có một tài khoản thư điện tử **Gmail** hoặc **Yahoo**, bạn có thể sử dụng dịch vụ **IM** cung cấp bởi các công ty này với phần mềm **Pidgin**. Sử dụng thông tin đăng nhập để truy cập tài khoản nhắn tin (**IM**) bằng **Pidgin**.

**Lưu ý‎:** Tất cả người sử dụng nên tìm hiểu kỹ càng về chính sách an ninh bảo mật của **Nhà Cung cấp Dịch vụ Tin nhắn Trực tuyến**.

**Pidgin** hỗ trợ các dịch vụ **Nhắn tin Trực tuyến** (**IM**) sau: [**AIM**](http://dashboard.aim.com/aim), [**Bonjour**](http://www.apple.com/support/bonjour/), [**Gadu-Gadu**](http://komunikator.gadu-gadu.pl/), [**Google Talk**](http://www.google.com/talk/), **Groupwise**, [**ICQ**](http://www.icq.com), **IRC**, [**MIRC**](http://www.mirc.com/), [**MSN**](http://www.msn.com/), 
[**MXit**](http://www.mxit.com/), [**MySpaceIM**](http://www.myspace.com/guide/im), [**QQ**](http://www.qq.com/), [**SILC**](http://silcnet.org/), **SIMPLE**, [**Sametime**](http://www.ibm.com/developerworks/downloads/ls/lst/), [**Yahoo!**](http://messenger.yahoo.com/), **Zephyr** và các dịch vụ **Nhắn tin Trực tuyến** (**IM**) khác sử dụng giao thức nhắn tin **XMPP**.

**Pidgin** không cho phép liên lạc giữa hai dịch vụ **Nhắn tin Trực tuyến**  khác nhau. Ví dụ: Nếu bạn sử dụng dịch vụ **Google Talk** với **Pidgin**, bạn không thể chát với một một người khác đang sử dụng **Pidgin** với tài khoản nhắn tin của **ICQ**. Tuy nhiên, nếu bạn sử dụng **Pidgin** để kết nối với nhiều tài khoản, khi đó bạn có thể liên lạc với bạn bè sử dụng các dịch vụ tương ứng. Đúng vậy, bạn có thể cùng lức sử dụng các tài khoản **Gmail** và **ICQ** để chát , và có thể liên lạc với các đối tac sử dụng các dịch vụ nêu trên (được hỗ trợ bởi **Pidgin**).


**OTR (Off-the-Record) Messaging** là thành phần mở rộng được xây dựng riêng cho pidgin. Nó cho phép việc liên lạc được bảo mật và có các tính năng sau:
**Pidgin** được hết sức khuyên dùng trong các phiên làm việc **Nhắn tin Trực tuyến** (**IM**), vì nó cung cấp tính năng bảo mật cao hơn so với các phần mềm có chức năng tương tự, đồng thời phần mềm này không đi kèm các thành phần quảng cáo hay gián điệp có thể gây nguy cơ mất tính riêng tư và bảo mật.

**OTR (Off-the-Record)** là tiện ích được xây dựng riêng cho **Pidgin**. Nó cho phép việc liên lạc được bảo mật và có các tính năng sau:


	
- Xác thực (Authentication): Bạn có thể đảm bảo người liên lạc với bạn chính là người bạn muốn liên lạc.
- Chối bỏ  (Deniability): Sau cuộc hội thoại, các tin nhắn sẽ không thể được xác định có nguồn gốc từ bạn cũng như người bạn liên lạc.
- Mã hóa (Encryption): Không ai có thể đọc được các tin nhắn qua mạng của bạn.
- Đảm bảo bảo mật tuyệt đối: Nếu bạn mất mật khẩu, các tin nhắn liên lạc trong quá khứ không bị lộ.

**Chú ý:** Trước hết bạn cần cài đặt phần mềm **Pidgin**, sau đó cài đặt tiện ích **OTR**. 



