

---

lang: vi
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 009
title: CCleaner - Secure File Deletion and Work Session Wiping

---

**Trang chủ**

[**www.ccleaner.com**](http://www.ccleaner.com)		

**Yêu cầu cấu hình máy tính**

- Mọi  phiên bản Windows

**Phiên bản sử dụng trong tài liệu này**

- 4.03

**Bản quyền**

- Phần  mềm miễn phí

**Yêu cầu đọc thêm**

**Sách hướng dẫn** [**chương 6. Làm sao để phá hủy thông tin mật**](/vi/chuong-6)

**Mức độ:** 1: bắt đầu, **2: Trung bình**, 3: Trên trung bình, 4: Có kinh nghiệm, 5: Nâng cao

**Thời gian cần thiết để có thể sử dụng công cụ:** 15 phút

**Những lợi ích bạn sẽ có được:**

- Khả năng xóa vĩnh viễn những dấu vết sử dụng và những dữ liệu đệm tạm thời trên  máy tính của bạn
- Khả năng **quét sạch không gian trống trên các ổ đĩa** được gắn trên máy tính của bạn

- Khả năng dọn dẹp **Windows Registry** (Cơ sở dữ liệu quản lý thông tin hoạt động của Windows)

- Khả năng kiểm soát những chương trình được kích hoạt vào thời điểm máy tính khởi động

**GNU Linux, Mac OS và Các chương trình Tương thích với Microsoft Windows**

Một công cụ tuyệt vời khác giúp xoá bỏ triệt để tệp tạm tương thích với **GNU Linux** và **Microsoft Windows** là  [**BleachBit**](http://bleachbit.sourceforge.net/). **BleachBit** cho phép bạn xoá các tệp đệm của 70 ứng dụng phổ biến nhất cũng như  thông tin đệm hệ thống và làm giải phóng không gian đĩa. Là một phần mềm nguồn-mở có phiên bản chạy không cần cài đặt, **BleachBit** hỗ trợ tới 32 ngôn ngữ. Người dùng **Ubuntu Linux** có thể xem thêm hướng dẫn [Dọn sạch những tệp thông tin rác…](http://ubuntuforums.org/showthread.php?t=140920) để tìm hiểu thêm việc làm sạch hệ thống. 

Người dùng **Mac OS** sẽ thấy công cụ miễn phí [Titanium’s Software: **OnyX** and **Maintenance**](http://www.titanium.free.fr/) hữu ích trong việc xoá dấu vết phiên làm việc của mình. Để xoá an toàn *Thùng rác* hãy vào ứng dụng *Finder* và chọn trình đơn: *Finder > Secure Empty Trash..*. Bạn có thể thiết đặt chọn mặc định việc xóa an toàn *Thùng rác* bằng cách vào phần thiết đặt Finder tại mục *Advance* và nhấn chọn *Empty Trash securely*. Để xóa sạch không gian trống trên một ổ đĩa hãy chạy chương trình hệ thống *Disk Utility*, chọn phân vùng ổ đĩa cần làm sạch, chọn khung *Erase* và nhấn nút *Erase Free Space..*. 

### 1.1 Những điều cần biết về công cụ này trước khi bạn  bắt đầu ###

Các thiết đặt mặc định trên máy tính của bạn hay một trình duyệt Internet tự động lưu giữ và tạo thông tin dấu vết về quá trình sử dụng mà một đối tượng thù địch có thể lợi dụng - không khác  một kẻ đi săn lần theo dấu vết con mồi. Mỗi khi bạn sử dụng một trình duyệt, một chương trình xử lý văn bản hay một chương trình, các tệp và dữ liệu tạm thời sẽ được tạo ra và lưu trong hệ thống. Một chương trình có thể tạo và lưu danh sách  những tài liệu văn bản hay các trang web bạn sử dụng gần đây. Ví dụ khi bạn nhập  địa chỉ một trang web vào trình duyệt, bạn có thể thấy xuất hiện một danh sách  các địa chỉ bắt đầu bằng những k‎ý tự bạn vừa nhập vào như dưới đây:

![](/sbox/screen/ccleaner-vi-1/00.png)

*Hình 1: Thanh địa chỉ trên trình duyệt web hiển thị nhiều đường dẫn khác nhau.*

Mặc dù việc hiển thị danh sách này có thể thuận tiện, giúp bạn  tiết kiệm công sức và thời gian nhập đầy đủ địa chỉ của trang web; tuy nhiên,  nó cũng có thể khiến người khác biết được những trang web bạn viếng thăm gần đây. Hơn thế nữa, các hoạt động trên máy tính gần đây của bạn có thể bị lộ bởi những dữ liệu tạm thời được lưu lại trên máy tính từ những hình ảnh trên trang web, gồm cả thư điện tử và những thông tin nhập vào trên trang web. 

Để xóa dữ liệu tạm được tạo ra sau mỗi lần bạn sử dụng một chương trình, bạn sẽ phải mở từng thư mục chương trình, chọn và xóa thủ công các tệp tạm của chương trình đó. **CCleaner** giúp cho việc này trở nên dễ dàng bằng cách hiển thị danh sách những chương trình và cho phép bạn chọn (những) chương trình có chứa tệp đệm tạm thời cần xóa.

**Quan trọng:**  Mặc dù CCleaner thường chỉ xóa những tệp tạm thời chứ  không xóa những tệp thực sự được lưu trên máy tính.  Chúng tôi **hết sức khuyến cáo** bạn  nên giữ một bản sao lưu tài liệu được cập nhật. (Hãy xem **Sách Hướng dẫn** chương [**5. Hướng dẫn khôi phục  dữ liệu bị xóa**](/vi/chuong-5) để có thêm thông tin về sao lưu dữ liệu). 

Sau khi chạy **Ccleaner** bạn có thể mất mọi thông  tin lịch sử truy cập trên các trình duyệt và thông tin lược sử các tài liệu sử dụng gần đây cũng như những mật khẩu được lưu trên hệ thống – nhưng đó chính là mục đích của công cụ này này – để giảm thiểu những nguy cơ nhiễm mã độc và bị theo dõi máy tính của bạn.

