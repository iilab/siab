

---

lang: vi
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to access the Internet using the Tor Browser

---

List of sections on this page:

- [**3.0 Giới thiệu Sử dụng Mạng Ẩn danh Tor**](#3.0)
- [**3.1 Hướng dẫn Kết nối vào Mạng Ẩn danh Tor**](#3.1)
- [**3.2 Hướng dẫn Kiểm tra Kết nối Tor**](#3.2)
- [**3.3 Hướng dẫn truy cập Internet sử dụng Tor**](#3.3)
- [**3.3.1 Hướng dẫn Cấu hình Mozilla Firefox Làm việc với Tor**](#3.3.1)
- [**3.3.2 Hướng dẫn Cấu hình Internet Explorer Làm việc với Tor**](#3.3.2)

-------

<a name="3.0"></a>
## 3.0 Giới thiệu Sử dụng Mạng Ẩn danh Tor ##
Để có thể truy cập Internet một cách ẩn danh, bạn phải khởi động chương trình **Tor Browser**. Trước hết, chương trình sẽ kết nối máy tính của bạn vào mạng lưới **Tor**. Sau khi đã thiết đặt thành công kết nối vào mạng **Tor**, **Tor Browser** sẽ tự động khởi động trình duyệt chạy không cần cài đặt **Firefox Portable** được tích hợp trong chương trình **Tor Browser Bundle**. 

**Lưu ý**: Có một sự đánh đổi giữa sự ẩn danh và tốc độ. Do **Tor** đảm bảo việc truy cập ẩn danh, tốc độ của nó chắc chắn sẽ chậm hơn so với các trình duyệt khác trên máy của bạn. **Tor** phân luồng dữ liệu truy cập của bạn qua các máy tính tình nguyện ở các khu vực khác nhau trên thế giới nhằm đảm bảo bảo mật riêng tư và an ninh của bạn.

<a name="3.1"></a>
## 3.1 Hướng dẫn Kết nối vào Mạng Ẩn danh Tor ##

Để kết nối vào mạng ẩn danh **Tor** hãy theo các bước:

**Bước 1**. **Chuyển tới** thư mục *Tor Browser*, và **nhấn đúp chuột** vào ![](/sbox/screen/tor-vi/30.png) để mở cửa sổ sau:

![](/sbox/screen/tor-vi/24.png)

*Hình 1: Khung điều khiển Vidalia Control Panel đang tạo kết nối vào mạng ẩn danh Tor*

Khi *Vidalia Control Panel* khởi tạo một kết nối vào mạng ẩn danh **Tor**, một biểu tượng  hình củ hành màu vàng xuất hiện trên *Khay Hệ thống* như thế này: ![](/sbox/screen/tor-vi/31.png). Khi kết nối giữa máy tính của bạn và mạng **Tor** được thiết lập thành công, biển tượng này sẽ chuyển thành màu xanh: ![](/sbox/screen/tor-vi/32.png)

**Lưu ý**: Để sử dụng hiệu quả *Vidalia Control Panel*, hãy tìm hiểu phần [**Hướng dẫn Cấu hình Vidalia Control Panel**](/vi/tor_huongdankhungdieukhien). 

Sau vài giây, **Tor Browser** sẽ khởi động trình duyệt **Mozilla Firefox** như trong hình:

![](/sbox/screen/tor-vi/33.png)

*Hình 2: Mozilla Firefox hiển thị thông báo Bạn đang sử dụng Tor?*

Mỗi lần bạn khởi động chương trình **Tor Browser**, nó sẽ tự động kích hoạt *Vidalia Control Panel* (*Hình 1*) và trang [**https://check.torproject.org/**](https://check.torproject.org/)  (*Hình 2*). Thành phần mở rộng **Torbutton** sẽ xuất hiện phía góc dưới bên phải trình duyệt như trong hình sau: ![](/sbox/screen/tor-vi/34.png) 

**Lưu ý**: Nếu bạn đang mở một trình duyệt **Mozilla Firefox** khi khởi đọng **Tor Browser**, thành phần mở rộng **Torbutton** sẽ xuất hiện ở chế độ tắt trong cửa sổ trình duyệt đang mở như trong hình sau: ![](/sbox/screen/tor-vi/35.png)

Thành phần mở rộng **Torbutton** được sử dụng để thiết đặt cách **Firefox** kết nối đúng đắn vào mạng ẩn danh **Tor**. Chỉ cần **nhấn** biểu tượng **Torbutton** để chuyển đổi trạng thái bật và tắt.  

Tuy nhiên, nếu bạn *không* kết nối vào mạng **Tor**, **Torbutton** sẽ ở trạng thái tắt và cửa sổ thông báo sau sẽ xuất hiện:

![](/sbox/screen/tor-vi/36.png)

*Hình 3: Mozilla Firefox hiển thị thông báo: Xin lỗi. Bạn không sử dụng Tor*

Nếu bạn gặp *Hình 3*, nút **Torbutton** ở trạng thái tắt (cho dù bạn cố gắng bật lên), hoặc trang web trống rỗng không có nội dung gì, hãy tham khảo phần [**4.0 Gỡ rối Sử dụng Tor**](/vi/tor_khacphucloiketnoi). 

<a name="3.2"></a>
## 3.2 Hướng dẫn Kiểm tra Kết nối Tor ##

Để tự xác minh bạn đã kết nối thành công vào mạng ẩn danh **Tor** hay chưa, hãy theo các bước sau:

**Bước 1**. **Mở** trang [**https://check.torproject.org/**](https://check.torproject.org/). Nó sẽ xác nhận bạn đã kết nối vào mạng **Tor** hay chưa.

Nếu trình duyệt của bạn đã kết nối vào Internet thông qua mạng ẩn danh **Tor** network, các trang web bị chặn lọc hay cấm tại quốc gia bạn sẽ có thể truy cập được, và các hoạt động trực tuyến của bạn sẽ được bảo mật và an toàn. Bạn có thể nhận thấy một số trang như **www.google.com** sẽ thể hiện như bạn truy cập từ các nước khác nhau. Điều này là bình thường khi sử dụng **Tor**. 

<a name="3.3"></a>
## 3.3 Hướng dẫn truy cập Internet sử dụng Tor ##

Dù bạn có thể ngay lập tức sử dụng **Firefox** với mạng **Tor**, chúng tôi khuyến nghị bạn đọc kỹ phần dưới đây liên quan tới việc thiết đặt **Firefox** để tối đa việc bảo mật riêng tư và an ninh cho bản thân bạn.

<a name="3.3.1"></a>
### 3.3.1 Hướng dẫn Cấu hình Mozilla Firefox Làm việc với Tor ###

**Torbutton** là một thành phần mở rộng hay tiện ích dành cho **Mozilla Firefox**, được thiết kế để bảo vệ tính nặc danh và bảo mật của các hoạt động trực tuyến bằng cách khóa các tính năng dễ bị khai thác trong **Mozilla Firefox**. 

**Quan trọng**: Các trang web độc hại hoặc thậm chí một máy chủ **Tor** có thể *vẫn* để lộ thông tin về địa điểm truy cập Internet và các thông tin trực tuyến của bạn, *thậm chí* khi bạn đang sử dụng **Tor**. Rất may là cấu hình mặc định của **Torbutton** cũng khá an toan; tuy nhiên, chúng tôi khuyến nghị bạn thay đổi một số thiết lập an ninh sau để tối ưu bảo mật riêng tư và an ninh trực tuyến cho bản thân. 

**Lưu ý**: Người dùng **nâng cao** am hiểu về các vấn đề liên quan tới trình duyện có thể chọn lọc các thiết đặt này.

Cửa sổ thiết đặ *Torbutton Preferences* có ba khung thiết đặt cho phép bạn xác định các tùy chọn khác nhau: 

- Khung **Proxy Settings** 
- Khung **Security Settings**
- Khung **Display Settings**  

Cửa sổ *Torbutton Preferences* có thể được mở cho dù **Torbutton** được tắt hay bật. Để mở *Torbutton Preferences* hãy theo các bước sau: 

**Bước 1**. **Nhấn chuột phải** vào **Torbutton** để mở trình đơn chương trình: 

![](/sbox/screen/tor-vi/37.png)

*Hình 4: Trình đơn Torbutton*

**Bước 2**. **Chọn** mục *Preferences...* để mở cửa sổ sau: 

![](/sbox/screen/tor-vi/38.png)

*Hình 5: Cửa sổ Torbutton Preferences hiển thị khung Proxy Settings*

- Khung **Proxy Settings** 
 
Khung *Proxy Settings* điều khiển cách thức **Firefox** truy cập Internet khi **Torbutton** trạng thái bật. Bạn không cần thay đổi gì trong khung này. 

- Khung **Security Settings**  

Khung *Security Settings* được dành cho những người dùng **Có kinh nghiệm** và **Nâng cao** có kiến thức sâu về bảo mật Internet và các trình duyệt. Các thiết đặt mặc định cung cấp một mức bảo mật cao cho những người dùng bình thường. Khung *Security Settings* cho phép bạn thiết đặt cách thức **Torbutton** quản lý lược sử, bộ nhớ đệm, và các tính năng khác trong **Firefox**. 

![](/sbox/screen/tor-vi/39.png)

*Hình 6: Khung Thiết đặt An ninh*

Lựa chọn *Tắt các Thành phần Mở rộng khi sử dụng Tor* (*Disable plugins during Tor usage*) là một trong vài thiết đặt an ninh bạn cần chọn, nhưng cũng chỉ chọn *tạm thời*. Để có thể hiển thị nội dung trang có chứa video qua **Tor** - bao gồm các trang như  [**DailyMotion**](http://www.dailymotion.com/), [**The Hub**](http://hub.witness.org/) và [**YouTube**](http://www.youtube.com) - bạn phải **hủy chọn** tính năng *Disable plugins during Tor usage*. 

**Lưu ý**: Bạn chỉ nên cho phép các thành phần mở rộng hoạt động đối với các trang web tin tưởng, và phải vào khung *Security Settings* để **nhấn chọn** ô *Disable plugins during Tor usage* một lần nữa sau khi đã truy cập xong những trang web này 

Để có thêm thông tin về các tùy chọn thiết đặt trong khung *Security Settings* hãy tham khảo [**Torbutton**](https://www.torproject.org/torbutton/).

- Khung **Display Settings**

Khung Thiết đặt Hiển thị (*Display Settings*) cho phép bạn chọn cách hiển thị
**Torbutton** trên thanh trạng thái **Firefox** như ![](/sbox/screen/tor-vi/34.png) or ![](/sbox/screen/tor-vi/40.png), hoặc ![](/sbox/screen/tor-vi/35.png) hay ![](/sbox/screen/tor-vi/41.png). Đây là các cách hiển thị được thiết kế cố định.

![](/sbox/screen/tor-vi/42.png)

*Hình 7: Khung Thiết đặt Hiển thị*

**Gợi ý**: Sau khi kết thúc phiên truy cập Internet, hãy xóa các tệp đệm và cookies Internet. Việc này có thể được thực hiện trong  **Firefox** bằng cách **chọn Tools > Clear Recent History...**, kiểm tra tất cả các lựa chọn có sẵn trong màn hình hiện lên và **nhấn** vào nút *Clear Now*. Để tìm hiểu thêm, hãy xem chương **Hướng dẫn Thực hành** [**Mozilla Firefox**](/vi/firefox-main).

Để tìm hiểu them về **Torbutton**, hãy xem [**Torbutton FAQ**](https://www.torproject.org/torbutton/torbutton-faq.html.en).

<a name="3.3.2"></a>
### 3.3.2 Hướng dẫn Cấu hình Internet Explorer Làm việc với Tor ###

**Lưu ý**: Mặc dù **Tor** được thiết kế để làm việc với bất kỳ trình duyệt web nào,  **Firefox** và **Tor** là sự kết hợp tuyệt vời để tránh sự pháp hiện hay do thám của các đối tượng thù địch hay phá hoại. **Internet Explorer** nên là lựa chọn cuối cùng! 

Tuy  nhiên, nếu bạn ở tình huống phải sử dụng **Internet Explorer** hãy theo các bước sau:

**Bước 1**. **Mở** trình duyệt **Internet Explorer**. 

**Bước 2**. **Chọn Tools > Internet Options** để mở cửa sổ *Internet Options*.

**Bước 3**. **Nhấn** vào khung *Connections* để mở cửa sổ như trong *Hình 8* bên dưới: 

![](/sbox/screen/tor-vi/43.png)

*Hình 8: Khung Kết nối (Connections) của cửa sổ Internet Options*

**Bước 4**. **Nhấn** ![](/sbox/screen/tor-vi/44.png) để mở *Local Area Network (LAN) Settings* : 

![](/sbox/screen/tor-vi/45.png)

*Hình 9: Thiết đặt Mạng Nội bộ (LAN)*

**Bước 5**. **Nhấn chọn** ô *Use a proxy server...* như trong *Hình 9*, sau đó **Nhấn** ![](/sbox/screen/tor-vi/46.png) để kích hoạt màn hình *Proxy Settings*. 

**Bước 6**. **Điền vào** các trường thông tin thiết đặt máy chủ ủy quyền như dưới đây: 

![](/sbox/screen/tor-vi/47.png)

*Hình 10: Ví dụ một màn hình Proxy Settings được nhập thông tin đầy đủ*

**Bước 7**. **Nhấn** ![](/sbox/screen/tor-vi/07.png) trong các cửa sổ cấu hình tiếp theo để thoát khỏi **Internet Options** và quay lại trình duyệt **Internet Explorer**.

**Lưu ý**: Bạn cần lặp lại các bước **từ 1 đến 4** để dừng sử dụng **Tor**. Trong **Bước 5**, bạn cần **hủy chọn** ô *Use a proxy server...*. 

**Gợi ý**: Bạn cần xóa các tệp đẹm Internet, cookies và lược sử truy cập sau phiên truy cập theo các bước sau:

**Bước 1**. **Chọn Tools > Internet Options** để mở khung mặc định *General*:

![](/sbox/screen/tor-vi/48.png)

*Hình 11: Khung Thiết đặt Tổng quát của Internet Explorer*

**Bước 2**. **Nhấn** ![](/sbox/screen/tor-vi/49.png) trong mục *Temporary Internet files*, cửa sổ xác nhận *Xóa Cookies* xuất hiện như sau:

![](/sbox/screen/tor-vi/50.png)

Hình 12: Hộp thoiạ xác nhận Xóa Cookies

**Bước 3**. **Nhấn** ![](/sbox/screen/tor-vi/07.png) để xóa vĩnh viễn Internet cookies.

**Bước 4**. **Nhấn** ![](/sbox/screen/tor-vi/51.png) để mở hộp thoại xác nhận *Xóa Tệp*sau đó **nhấn** ![](/sbox/screen/tor-vi/07.png) để xóa các tệp đệm Internet. 

**Bước 5**. **Nhấn** ![](/sbox/screen/tor-vi/52.png) để mở hộp thoại xác nhận *Internet Options*  **nhấn** ![](/sbox/screen/tor-vi/53.png) và **nhấn** ![](/sbox/screen/tor-vi/07.png). 

**Lưu ý:** Để truy cập mạng ẩn danh **Tor** sử dụng **Internet Explorer** bạn phải giữ chương trình **Tor Browser** với **Vidalia** kết nối vào mạng Tor.

