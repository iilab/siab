

---

lang: vi
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 001
title: Spybot - Anti-Spyware

---

		
**Trang chủ**

[**www.safer-networking.org/en**](http://www.safer-networking.org/en)



**Yêu cầu cấu hình máy tính**

- Mọi phiên bản Windows

**Phiên bản sử dụng trong tài liệu này**

- 1.6.2

**Bản quyền**

- Phần mềm miễn phí

**Yêu cầu đọc thêm**

- Sách hướng dẫn [**chương 1. Làm thế nào để bảo vệ máy tính của bạn khỏi phần mềm độc hại và hacker**](/vi/chuong-1)

**Mức độ**: 1: Người mới bắt đầu, **2: Trung bình**, 3: Trên trung bình, 4: Có kinh nghiệm, 5: Nâng cao

**Thời gian cần thiết để có thể sử dụng công cụ: 20 phút**

**Những lợi ích bạn sẽ có được:**

- Khả năng **tìm và diệt** nhiều loại phần mềm độc hại/ hay phần mềm gián điệp 

- Khả năng **tạo hệ miễn dịch** bảo vệ máy tính chống lại nguy cơ lây nhiễm phần mềm độc hại

**Các Chương trình có Tính năng tương tự trên GNU Linux, Mac OS và Microsoft Windows**:

Các hệ điều hành như **GNU Linux** và **Mac OS**, ở thời điểm hiện tại, về lý thuyết là không bị lây nhiễm các phần mềm độc hại (phần mềm gián điệp, vi rút...). Để tự bảo vệ bản thân, chúng tôi khuyên bạn: **1)** hãy thường xuyên cập nhật chương trình hệ điều hành và các phần mềm được cài đặt trên máy tính; **2)** sử dụng một chương trình diệt vi rút được đề cập trong chương về [*Avast*](/vi/avast-main);  **3)** sử dụng một phần mềm tường lửa được giới thiệu trong [*Comodo*](/vi/comodo-main); **4)** sử dụng trình duyệt bảo mật [*Firefox*](/vi/firefox-main) với thành phần mở rộng [*NoScript*](/vi/firefox_noscript) giúp ngăn chặn các mã độc trên các trang web tải về máy trong quá trình duyệt trang. Những biện pháp phòng ngừa trên giúp bảo vệ tôt hơn hệ thống **GNU Linux** hoặc **Mac OS** của bạn.

Vấn đề an ninh cho các máy tính chạy hệ điều hành **Microsoft Windows** sẽ rất khác biệt. Có hàng ngàn chương trình độc hại được tạo ra hàng ngày. Các phương thức tấn công ngày càng trở nên tinh vi. Các biện pháp phòng ngừa được nêu phía trên là **bắt buộc** với các máy sử dụng hệ điều hành **Microsoft Windows**. Hơn thế nữa, chúng tôi đặc biệt khuyên dùng thêm **Spybot** được giới thiệu trong chương này. 

Tuy nhiên, nếu máy tính của bạn vẫn bị lây nhiễm dù đã sử dụng các biện pháp đề phòng trên, bạn có thể cần tới những cộng cụ khác, chúng tôi giới thiệu một số dưới đây:

1. Cài đặt [**SuperAntiSpyware**](http://superantispyware.com), cập nhật cơ sở dữ liệu phần mềm gián điệp sau đó quét máy tính của bạn.
2. Cài đặt  [**Malwarebytes Anti-Malware**](http://www.malwarebytes.org/mbam.php), thực hiện quét  *Quick Scan* sau đó *Quét kỹ* (*Scan*), gỡ bỏ các phần mềm độc hại phát hiện được trong phần  *Show Results*
3. Sử dụng các chương trình diệt phần mềm gián điệp miễn phí (free anti-spyware) như:  [**Microsoft Windows Defender**](http://www.microsoft.com/windows/products/winfamily/defender), [**Ad-Aware Internet Security**](http://www.lavasoft.com/) or [**SpywareBlaster**](http://www.javacoolsoftware.com/spywareblaster.html).


###1.1 Những điều cần biết về công cụ này trước khi bạn bắt đầu###

**Spybot S&D** là một chương trình miễn phí rất phổ biến được sử dụng để phát hiện và xóa bỏ nhiều loại phần mềm độc hại, mã quảng cáo, và phần mềm gián điệp khỏi máy tính của bạn. Nó cũng tạo hệ miễn dịch cho hệ thống của bạn chống lại các loại phần mềm độc hại đó, ngăn không cho chúng lây nhiễm lên máy tính của bạn một khi **Spybot** đã được cài đặt.

*Phần mềm quảng cáo* (adware) là những dạng chương trình hiển thị những nội dung quảng cáo trên máy tính của bạn. Một số loại nhất định trong nhóm mã quảng cáo này hoạt động giống như phần mềm gián điệp và có thể xâm hại sự bảo mật và an ninh của bạn.

Phần mềm độc hại: (ví dụ như ‘trojans’ và sâu máy tính) là những chương trình được thiết kế với mục đích gây hại hoặc tấn công đột nhập máy tính của bạn một cách âm thầm mà bạn không hề hay biết.

Phần mềm gián điệp gồm những chương trình tìm cách thu thập thông tin dữ liệu của bạn, nhòm ngó và ghi lại những thông tin cá nhân cũng như những hoạt động truy cập Internet của bạn. Giống như các phần mềm độc hại khác, chúng thường chạy ẩn trên máy tính. Do vậy, việc cài đặt **Spybot** giúp bảo vệ máy tính và chính bản thân bạn.

**Spybot** có một thành phần mở rộng là Tea Timer. Thành phần này bảo vệ máy tính của bạn khỏi những phần mềm độc hại mới.

***Lưu ý***:
 
**Windows Vista** có cài đặt sẵn chương trình chống phần mềm gián điệp **Windows Defender**. Tuy nhiên, Windows Vista cho phép **Spybot** được cài đặt và hoạt động mà không bị xung đột.

