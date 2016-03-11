

---

lang: vi
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 012
title: Jitsi - Secure Audio, Video and Instant Text Messaging 

---

**Trang chủ**

- [**https://jitsi.org/**](https://jitsi.org/)

**Yêu cầu Cấu hình Máy tính**

- Tất cả các phiên bản Windows

**Phiên bản sử dụng trong hướng dẫn này**

- 2.4

**Lần kiểm tra gần nhất**

- Tháng Một 2014

**Bản quyền**

- Phần mềm Miễn phí Mã nguồn Mở

**Những điều bạn sẽ đạt được**: 
 
- Khả năng có được một hệ thống liên lạc tích hợp có bảo mật và riêng tư, bao gồm cả khả năng tạo các phiên liên lạc bằng hình ảnh video.
- Khả năng mã hóa phiên liên lạc độc lập với các nhà cung cấp tài khoản.
- Khả năng đăng ký và sử dụng các tài khoản khác nhau cùng lúc(ví dụ **Facebook**, **Google Talk**, **Yahoo Messenger**).
-

**GNU Linux, Mac OS và các Chương trình Tương tự trên Microsoft Windows**:

**Jitsi** có các phiên bản cho **GNU Linux**, **Mac OS**, cũng như **MS Windows** (và sắp tới là cho **Android OS**). Những chương trình khác mà **Jitsi**  có thể kết nối được sử dụng lớp mã hóa **OTR** hoặc **ZRTP** được khuyến nghị bên dưới đây:

- Với **tin nhắn văn bản**: [**Pidgin**](/vi/pidgin-main) (**MS Windows** và **GNU Linux**), [**Miranda**](http://www.miranda-im.org/) (**MS Windows**), [**Adium**](https://adium.im/) (**Mac OS X**), [**ChatSecure**](https://guardianproject.info/apps/chatsecure/) (**Android OS** và **iOS** từng được biết tới với cái tên [**Gibberbot**](/vi/Gibberbot_main)) 

- Với **những phiên liên lạc thoại**: **CSipSimple** (**Android OS**), [**Linphone**](http://www.linphone.org/) (**GNU Linux**, **MS Windows**, **Mac OS X**, **Android OS**, **iOS**, và một số hệ điều hành khác.)

**1.1 Những điều bạn cần biết trước khi bắt đầu**

**Jitsi** hỗ trợ nhiều loại tài khoản và giao thức liên lạc khác nhau và do đó cho phép liên lạc với các đối tác sử dụng một chương trình liên lạc khác. Một số chương trình trong số này cung cấp các tính năng tương tự để nâng cao bảo mật phiên liên lạc (như những chương trình đã đề cập trong phần trên), bằng việc hỗ trợ mã hóa riêng về liên lạc thoại và văn bản dùng (**OTR** và **ZRTP**).  Các chương trình khác, đặc biệt là các phần mềm có bản quyền sở hữu (ví dụ tính năng nhắn tin **Facebook** hay **Google Talk** ), có thể không cài đặt những tính năng này. Tuy nhiên bạn vẫn có thể liên lạc với đối tác sử dụng những chương trình có bản quyền sở hữu với sự hỗ trợ của **Jitsi** mà không có thêm lớp bảo mật thêm vào được cung cấp bởi **Jitsi*.

Bất kể dù bạn liện lạc qua tin nhắn văn bản, thoại hay hình ảnh video, các nhà cung cấp các dịch vụ như **Facebook Chat**, **Google Talk**, **Yahoo! Messanger**, **Skype** và **Viber** đều có truy cập vào các phiên liên lạc của bạn và có thể cung cấp khả năng truy cập này cho các bên thứ ba, ví dụ như các tập đoàn hay chính phủ. **Jitsi** cho phép bạn liên lạc theo cách thức an toàn và riêng tư với các tài khoản dịch vụ sẵn có với việc hỗ trợ cung cấp thêm một lớp mã hóa bảo mật riêng. Điều này cho phép nội dung của phiên liên lạc không thể truy cập được bởi nhà cung cấp dịch vụ cũng như một bên thứ ba khác. Để bảo vệ các phiên liên lạc và nội dung đàm thoại, **Jitsi** sử dụng các phương pháp mã hóa bao gồm **Off-the-Record** ([**OTR**](/vi/glossary#OTR)) cho nhắn tin văn bản, và **ZRTP/SRTP** cho các cuộc gọi thoại.

Một sự khác biệt đáng chú ý giữa **Jitsi** và các phần mềm như **Skype** là công cụ này cho phép người dùng sử dụng các tài khoản sẵn có từ các nhà cung cấp dịch vụ khác nhau, không phụ thuộc vào các nhà phát triển phần mềm.  Điều này cũng có nghĩa là bạn cần phải đăng ký thiết đặt một tài khoản trước khi có thể sử dụng với **Jitsi**.

**Lưu ý**: **Jitsi** sử dụng ngôn ngữ lập trình **Java**. Do vậy, môi trường Java cần được cài đặt trên máy tính của bạn để phần mềm có thể hoạt động được. **Oracle Java** được biết có chứa nhiều lỗi bảo mật và có thể khiến máy tính của bạn bị chiếm quyền điều khiển từ xa và cài đặt các phần mềm gián điệp nhằm giám sát các phiên liên lạc và dữ liệu của bạn. Chúng tôi **hết sức** khuyến cáo bạn nên hạn chế tối đa số lượng các chương trình có thể sử dụng Java trên máy tính của mình. Hãy thao khảo [**Vô hiệu thành phần mở rộng liên quan tới Java trong Firefox**](/vi/firefox_caidatthanhphanmorong#3.2) và xem phần [**các bước để vô hiệu Java cho tất cả các trình duyệt trên máy tính của bạn**](https://www.java.com/en/download/help/disable_browser.xml). Tuy nhiên, như bạn sẽ thấy trong phần sau của chương này, mặc dù sử dụng **Java**, có một số những ưu điểm về bảo mật khi sử dụng **Jitsi**.

