

---

lang: vi
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: Using the Tor Browser

---

- [**4.0 Giới thiệu Cửa sổ Điều khiển Vidalia**](#4.0)
- [**4.1 Hướng dẫn Xem Kết nối Tor**](#4.1)
- [**4.2 Hướng dẫn Xem và Cấu hình Cửa sổ Thiết đặt Vidalia**](#4.2)
- [**4.3 Hướng dẫn Dừng và Chạy Chương trình Tor**](#4.3)

-------

<a name="4.0"></a>
## 4.0 Giới thiệu Cửa sổ Điều khiển Vidalia ##

*Cửa sổ Điều khiển Vidalia* - giờ chắc bạn đã khá quen thuộc - chính là cửa sổ giao diện chính của chương trình **Tor**. *Cửa sổ Điều khiển Vidalia* cho phép bạn thiết đặt các tùy chọn quan trọng của **Tor**, kiểm tra các thông số kết nối. Để mở **Cửa sổ Điều khiển Vidalia** hãy theo hướng dẫn sau:

**Nếu bạn đang bật Tor Browser** **nhấn đúp chuột** vào ![](/sbox/screen/tor-vi/32.png) để mở *Cửa sổ Điều khiển Vidalia*.

**Gợi ý**: Nếu bạn nhấn phải chuột vào biểu tượng hình củ hành, *Cửa sổ Điều khiển Vidalia*  sẽ xuất hiện dưới dạng trình đơn cảm ngữ cảnh như sau:

![](/sbox/screen/tor-vi/73.png)

*Hình 1: Trình đơn cảm ngử cảnh Cửa sổ Điều khiển Vidalia*


**Nếu bạn không bật Tor Browser** **hãy chuyển đến** thư mục **Tor Browser**, và **nhấn đúp chuột** vào ![](/sbox/screen/tor-vi/60.png) để mở *Cửa sổ Điều khiển Vidalia* và tự động kết nối vào mạng ẩn danh **Tor** như sau:

![](/sbox/screen/tor-vi/61.png)

*Hình 2: Cửa sổ Điều khiển Vidalia hiển thị một kết nối thành công vào mạng Tor*

<a name="4.1"></a>
## 4.1 Hướng dẫn Kiểm tra Kết nối Tor ##

**Bước 1**. **Nhấn** ![](/sbox/screen/tor-vi/62.png) để mở cửa sổ sau:

![](/sbox/screen/tor-vi/63.png)

*Hình 3: Bản đồ Mạng lưới Tor*
*Bản đồ Mạng lưới Tor* hiển thị danh sách tất cả những máy chủ trung gian *Tor* tạo nên mạng ẩn danh *Tor*. Khung bên trái sẽ liệt kê các máy chủ này theo mức độ băng thông sắn có và theo vị trí địa lý.

 
- **Nhấn** ![](/sbox/screen/tor-vi/64.png) để thay đổi danh sách các máy chủ này theo thứ tự tăng hoặc giảm băng thông sẵn có, hoặc theo trình tự chữ cái quốc qia nơi các máy chủ này được đặt.

Bên dưới bản đồ thế giới là hai khung, khung *Kết nối* (Connections) và khung chi tiết chuyển tiếp (relay details). Khung *Kết nối* hiển thị tên các máy chủ **Tor** được chọn ngẫu nhiên khi thiết đặt kết nối ẩn danh cho bạn. 

- **Chọn** một máy chủ trong danh sách *Kết nối* để xem định tuyến cụ thể trong mạng **Tor** được hiển thị bởi các đường kết nối màu xanh trên bản đồ. 

Khung liền kề hiển thị thông tin kết nối chi tiết của một máy chủ trong danh sách *Trung chuyển* (Relay) ở trong khung bên trái; trong *Hình 3*, thông tin chi tiết két nối của một máy chủ trung chuyển tại Canada *setting Orange* được hiển thị.

**Lưu ý**: *Bản đồ Mạng lưới Tor* giúp diễn đạt cách thức **Tor** hoạt động một cách trực quan.

<a name="4.2"></a>
## 4.2 Hướng dẫn Xem và Cấu hình Cửa sổ Thiết đặt Vidalia ##

**Bước 1**. **Nhấn** ![](/sbox/screen/tor-vi/65.png) để mở cửa sổ sau:

![](/sbox/screen/tor-vi/66.png)

*Hình 4: Màn hình Thiết đặt trong Khung Điều khiển Vidalia*

Khung *General* (Tổng quát) cho phép bạn xác định **Vidalia** sẽ tự động khởi động trong quá trình khởi động **Windows**, và sau đó tự khởi động chương trình **Tor**. 

Nếu bạn muốn tự tay khởi động chương trình **Vidalia**, hãy **bỏ chọn** tùy chọn  *Start Vidalia when my system starts*.

**Lưu ý**: Người dùng ở trình độ **Bắt đầu** hoặc **Trung bình** nên chấp nhận các lựa chọn mặc định như trong *Hình 4*.

**Bước 2**. **Nhấn** ![](/sbox/screen/tor-vi/67.png) để xác nhận thiết đặt.


Cho dù ngôn ngữ mặc định của **Tor** là Tiếng Anh, khung *Appearance* (Hiển thị) cho phép bạn chọn một ngôn ngữ khác cho *Khung Điều khiển Vidalia*. Nó cũng cho phép bạn thay đổi cách hiển thị. 

![](/sbox/screen/tor-vi/68.png)

*Hình 5: Màn hình Appearance trong Cửa sổ Vidalia*

<a name="4.3"></a>
## 4.3 Hướng dẫn Dừng Chương trình Tor ##

**Bước 1**. **Nhấn** ![](/sbox/screen/tor-vi/69.png) trong cửa sổ *Vidalia Shortcuts* để dừng chương trình **Tor** program; Mục *Status* (Trạng thái) của *Khung Điều khiển Vidalia* sẽ xuất hiện như sau:

![](/sbox/screen/tor-vi/70.png)

*Hình 6: Mục Trạng thái Tor - Thông báo Tor đang ngừng hoạt động*

**Bước 2**. **Nhấn** ![](/sbox/screen/tor-vi/71.png) để khởi động **Tor**; Mục *Status* (Trạng thái) của *Khung Điều khiển Vidalia* sẽ xuất hiện sau vài giây như sau:

![](/sbox/screen/tor-vi/72.png)

*Hình 7: Mục Trạng thái Tor - Thông báo Kết nối Thành công vào Mạng lưới!*

