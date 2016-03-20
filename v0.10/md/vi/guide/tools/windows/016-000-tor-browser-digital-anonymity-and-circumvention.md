

---

lang: vi
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 016
title: Tor Browser - Digital Anonymity and Circumvention

---

**Trang chủ**
			
[**https://www.torproject.org**](https://www.torproject.org/)
			
**Yêu cầu cấu hình máy tính**

- *Mọi phiên bản Windows*

- *Kết nối Internet*

- *Hoạt động tốt nhất với **Mozilla Firefox***		

**Phiên bản sử dụng trong tài liệu này**

- Tor Browser: 1.3.24

**Bản quyền** 

- Phần mềm Miễn phí và Nguồn mở 

**Yêu cầu Đọc thêm** 

- Sách Hướng dẫn [**Chương 8. Làm thế nào để vượt qua sự kiểm duyệt và xuất bản thông tin trên Internet một cách nặc danh**](/vi/chuong-8)) 

**Mức độ**: 1: Người mới bắt đầu, 2: Trung bình, **3: Trên trung bình** và **4: Có kinh nghiệm**, 5: Nâng cao

**Thời gian cần thiết để có thể sử dụng công cụ**: 20 - 30 minutes 

**Những lợi ích bạn sẽ có được**: 

- *Khả năng ẩn giấu danh tính và dấu vết truy cập các trang web*

- *Khả năng che dấu địa chỉ các trang web truy cập khỏi nhà cung cấp dịch vụ Internet hay các bộ máy kiểm duyệt tại quốc gia bạn*

- *Khả năng vượt qua các bộ máy kiểm duyệt thông tin và lọc chặn trên Internet*


**Môi trường hệ điều hành GNU Linux, Mac OS và các Chương trình có Tính năng Tương tự trên Microsoft Windows**:

Chương trình cài đặt phía máy khách của mạng lưới **Tor** có các phiên bản cho **GNU Linux**, **Mac OS** và **Microsoft Windows**. **Tor** là công cụ bảo mật an ninh trực tuyến được kiểm tra kỹ càng và được khuyên dùng. Tuy nhiên, nếu nếu bạn muốn tìm hiểu một số giải pháp tương đương:

* [**Hotspot Shield**](http://hotspotshield.com/) là một giải pháp **Mạng Riêng Ảo** thương mại miễn phí **Virtual Private Network** (**VPN**) cho hệ điều hành **Microsoft Windows**.
* [**Dynaweb FreeGate**](http://www.dit-inc.us/freegate) là một công cụ máy chủ ủy quyền miễn phí cho **Microsoft Windows**.
* [**UltraReach UltraSurf**](http://www.ultrareach.com/) là một công cụ máy chủ ủy quyền miễn phí cho **Microsoft Windows**.
* [**Your Freedom**](http://www.your-freedom.net/) là một dịch vụ máy ủy quyền thương mại có cung cấp dịch vụ miễn phí (tuy nhiên với tốc độ thấp hơn) . Nó hoạt động cả trên **Linux**, **Mac OS** và **Microsoft Windows**.
* [**Psiphon**](http://psiphon.ca/) là máy chủ ủy quyền web, vì vậy hoạt động trên mọi hệ điều hành.

Chúng tôi đặc biệt khuyến nghị bạn tham khảo tài liệu được soạn thảo bởi [**Sesawe**](http://sesawe.net/), đây là một liên hiệp cam vì mục tiêu quyền truy cập thông tin tự do của người dùng Internet trên toàn thế giới.

## 1.1 Những điều cần biết về công cụ này trước khi bạn bắt đầu ##


**Tor** được thiết kế để nâng cao tính nặc danh cho các hoạt động của bạn trên Internet. Chương trình giúp bạn ngụy trang tránh sự theo dõi hoạt động trên mạng. Không chỉ đảm bảo tính nặc danh, **Tor**  còn là công cụ bảo mật hữu ích được sử dụng để vượt qua các bộ lọc chặn Internet nhằm truy cập các trang blog công cộng và tin tức quốc tế. 

**Tor** thực hiện việc đảm bảo nặc danh bằng cách định tuyến kết nối của bạn qua nhiều mạng máy chủ tình nguyện phân tán khắp nơi trên thế giới. Điều này giúp ngăn cản những kẻ muốn theo dõi kết nối Internet của bản để giám sát các trang web bạn truy cập, cũng như tránh việc các trang web bạn truy cập biết được vị trí của bạn. Đối với các máy chủ **Tor**, một số có thể biết bạn đang sử dụng **Tor**, một số khác có thể biết địa chỉ trang web được truy cập, nhưng không máy chủ nào biết được cả hai thông tin trên. 

**Tor** có thể giúp ngụy trang những kết nối của bạn tới các trang web phổ biến, nhưng nó không giúp bảo vệ nội dung thông tin liên lạc. Do vậy, đây là một lớp bảo vệ thêm để sử dụng cùng với những dịch vụ liên lạc bảo mật khác, ví dụ như **RiseUp** và **Gmail**, nhưng không nên sử dụng công cụ này khi truy cập các máy chủ thư điện tử không bảo mật như **Hotmail** hay **Yahoo**, hay những trang web có kết nối không bảo mật *http* khi phải nhập thông tin mật khẩu. 

**Một số định nghĩa:** 

- ***Port**: (cổng kết nối) Trong chương này, cổng kết nối được định nghĩa là điểm giao tiếp được phần mềm sử dụng để liên lạc với các dịch vụ chạy trên các máy chủ mạng. Ví dụ một địa chỉ, như [http://www.google.com](http://www.google.com),giống như tên phố của một dịch vụ đó, thì cổng chính là cửa bạn cần tìm đến đích. Khi truy cập một trang web, bạn thường dùng cổng 80 đối với các liên kết không bảo mật [http://mail.google.com](http://mail.google.com) và cổng 443 cho các liên kết bảo mật [https://mail.google.com](https://mail.google.com)*

- ***Proxy**: Trong chương này, một proxy là một phần mềm trung gian chạy trên máy tính của bạn, trên mạng nội bộ hoặc đâu đó trên Internet, giúp trung chuyển kết nối của bạn tới đích cuối cùng.*

- ***Route**: (tuyến) Trong chương này, route là một tuyến liên lạc trên Internet được thiết lập giữa máy tính của bạn và máy chủ đích.*

- ***Bridge Relay**: (Máy trung chuyển) Một máy trung chuyển là một máy chủ **Tor** giúp bạn kết nối vào mạng ẩn danh Tor. Các máy trung chuyển này là lựa chọn được thiết kết cho người sử dụng Internet ở các quốc gia khóa các truy cập tới **Tor**.*

