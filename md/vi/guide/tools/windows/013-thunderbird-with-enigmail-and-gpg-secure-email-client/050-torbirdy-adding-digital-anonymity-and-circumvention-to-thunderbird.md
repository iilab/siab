

---

lang: vi
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 5
depth: 3
title: Torbirdy - adding digital anonymity and circumvention to Thunderbird

---

<a name="1.0"></a>
## 6.1 Hướng dẫn Cài đặt TorBirdy cho Thunderbird ##

Sau khi [tải về **TorBirdy**](https://addons.mozilla.org/en-us/thunderbird/addon/torbirdy/) về máy tính, bắt đầu thực hiện việc cài đặt **TorBirdy** theo các bước sau:

**Bước 1. Mở Thunderbird**, sau đó **nhấn vào** ![](/sbox/screen/thunderbird-TorBirdy-vi/03.png) để mở *Trình đơn Thunderbird* và **chọn Add-ons** và mở cửa sổ Add-ons Manager.

**Bước 2. Nhấn** ![](/sbox/screen/thunderbird-TorBirdy-vi/04.png) ở bên khung trình đơn phía bên trái

**Bước 3. Nhấn** ![](/sbox/screen/thunderbird-TorBirdy-vi/05.png) và **chọn** *Install Add-on from File* như bên dưới đây:
 
![](/sbox/screen/thunderbird-TorBirdy-vi/06.png)

*Hình 1: Trình đơn quản lý các Thành phần Mở rộng*

**Bước 4**. Chuyển tới thư mục bạn đã lưu TorBirdy (nhiều khả năng là thư mục *Download*) như trong hình dưới đây:

![](/sbox/screen/thunderbird-TorBirdy-vi/07.png)

*Hình 2: Chọn thành phần mở rộng để cài đặt*

**Bước 5 Nhấn** ![](/sbox/screen/thunderbird-TorBirdy-vi/08.png) để kích hoạt cửa sổ sau:

![](/sbox/screen/thunderbird-TorBirdy-vi/09.png)
*Hình 3: Cửa sổ cài đặt chương trình*

**Quan trọng:** Trước khi thực hiện bước tiếp theo bạn cần đảm bảo rằng tất cả các thư điện tử của bạn đã được gửi hoặc lưu lại.

**Bước 6. Nhấn** ![](/sbox/screen/thunderbird-TorBirdy-vi/10.png) sau đó **nhấn** ![](/sbox/screen/thunderbird-TorBirdy-vi/11.png) để khởi động lại Thunderbird và hoàn tất việc cài đặt thành phần mở rộng **TorBirdy**.

## 6.2 Hướng dẫn Sử dụng TorBirdy trong Thunderbird ##

Trước khi có thể sử dụng **TorBirdy** trong **Thunderbird**, bạn phải chắc chắn rằng **TorBrowser** đang chạy và kết nối thành công vào **mạng ẩn danh Tor**. Nếu bạn chưa thiết đặt **TorBrowser**, hãy tham khảo phần [Tor - Sự nặc danh và vượt rào chắn kiểm duyệt Internet
](vi/tor-main) trước khi tiếp tục.

## 6.2.1 Kích hoạt TorBirdy cho Thunderbird ===

Hãy theo các bước sau để khởi động *Tor Browser* và chạy Thunderbird qua mạng ẩn danh *Tor*

**Bước 1: Chuyển tới** thư mục *Tor Browser*, và **nhấn đúp chuột** vào  ![](/sbox/screen/thunderbird-TorBirdy-vi/18.png) để mở màn hình sau:

![](/sbox/screen/thunderbird-TorBirdy-vi/19.png)

*Hình 8: Cửa sổ Trạng thái Tor*

*Lưu ý*: Chúng tôi khuyến nghị bạn đóng các cửa sổ trình duyệt Firefox khác đang chạy trước khi khởi động *Tor Browser*

Sau một vài giây, **Tor Browser** sẽ mở một cửa sổ trình duyệt mới như sau:

![](/sbox/screen/thunderbird-TorBirdy-vi/20.png)

*Hình 9: Tor Browser; kết nối thành công vào mạng ẩn danh Tor*

Bạn đã kết nối vào *mạng ẩn danh Tor* qua *Tor Browser*.

**Bước 2: Khởi động** Thunderbird và nhập mật khẩu khi được yêu cầu. Trạng thái của TorBirdy sẽ được hiển thị ở góc bên phải cửa sổ Thunderbird như được đánh dấu dưới đây

 ![](/sbox/screen/thunderbird-TorBirdy-vi/30.png)  

*Hình 10: TorBirdy đựơc kích hoạt cho Tor*

## 6.2.2 Xác nhận TorBirdy đang kết nối sử dụng Tor ##

Hãy theo các bước sau để kiểm tra và xác nhận các thiết đặt cho TorBirdy

**Bước 1: Nhấn vào**  ![](/sbox/screen/thunderbird-TorBirdy-vi/21.png) để mở trình đơn sau:

![](/sbox/screen/thunderbird-TorBirdy-vi/22.png)

*Hình 11: Trình đơn Thiết đặt TorBirdy*

**Bước 2: Chọn** *Mở TorBirdy Preferences* để mở cửa sổ dưới đây. **Nhấn** ![](/sbox/screen/thunderbird-TorBirdy-vi/23.png) trên cửa sổ cảnh báo của *TorBirdy Advanced Settings*

![](/sbox/screen/thunderbird-TorBirdy-vi/25.png)

*Hình 12: Cửa sổ TorBirdy Preferences*

**Bước 3: Nhấn vào** ![](/sbox/screen/thunderbird-TorBirdy-vi/24.png). Nếu bạn đã kết nối thành công qua *mạng ẩn danh Tor*, bạn sẽ thấy một thông báo như dưới đây (*Địa chỉ IP sẽ khác*)

[](/sbox/screen/thunderbird-TorBirdy-vi/26.png)

*Hình 13: Cửa sổ Bạn có đang kết nối vào Tor?*

**Lưu ý** nếu bạn chưa khởi động Tor Browser hoặc Tor Browser không kết nối vào mạng ẩn danh Tor thể hiện trong phần 6.2.1 phía trên, bạn sẽ không thể kết nối tới máy chủ thư của mình và bạn có thể thấy thông báo dưới đây sau khi khởi động Thunderbird:

![](/sbox/screen/thunderbird-TorBirdy-vi/27.png)

*Hình 14: Cửa sổ kết nối bị từ chối*

Một điều đáng chú ý là một số nhà cung cấp dịch vụ thư điện tử như Google Mail có thể từ chối một kết nối tới máy chủ thư của họ từ *mạng ẩn danh Tor*.

## Vô hiệu TorBirdy trong Thunderbird ##

Bạn có thể vô hiệu hóa thành phần mở rộng TorBirdy nếu bạn muốn chạy Thunderbird không dùng TorBirdy bằng cách thực hiện các bước sau:

**Bước 1. Mở** chương trình **Thunderbird**, sau đó **nhấn vào** ![](/sbox/screen/thunderbird-TorBirdy-vi/03.png) để mở **Trình đơn Thunderbird* và **chọn Add-ons** để mở cửa sổ quản lý Add-ons

**Bước 2. Nhấn** ![](/sbox/screen/thunderbird-TorBirdy-vi/04.png) trên khung phía bên trái

**Bước 3. Nhấn** vào ![](/sbox/screen/thunderbird-TorBirdy-vi/29.png) để mở cửa sổ sau:

![](/sbox/screen/thunderbird-TorBirdy-vi/28.png)

*Hình 15: Vô hiệu hóa Thành phần mở rộng TorBirdy*

**Bước 4: Nhấn** ![](/sbox/screen/thunderbird-TorBirdy-vi/11.png) để khởi động Thunderbird và hoàn tất việc vô hiệu hóa TorBirdy.

