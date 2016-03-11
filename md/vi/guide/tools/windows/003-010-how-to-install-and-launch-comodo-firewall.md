

---

lang: vi
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: How to Install and Launch COMODO Firewall 

---

Các mục trong trang này:

- [**2.0 Tổng quát về Cài đặt COMODO Firewall**](#2.0)
- [**2.1 Hướng dẫn Tắt Windows Firewall**](#2.1)
- [**2.2 Hướng dẫn Cài đặt COMODO Firewall**](#2.2)

-------

<a name="2.0"></a>
## 2.0 Tổng quát về Cài đặt COMODO Firewall ##

Cài đặt **COMODO Firewall** khá dễ dàng và nhanh chóng, bao gồm hai bước: trước hết cần phải tắt **Windows Firewall** (tường lửa tích hợp trong Windows), và tiếp theo là thực hiện cài đặt phần mềm **COMODO Firewall**.

Tốt nhất bạn chỉ nên sử dụng một chương trình tường lửa trên máy tại một thời điểm. Nếu bạn đang sử dụng một chương trình tường lửa khác trên máy, bạn cần gỡ bỏ chương trình này trước khi cài đặt **COMODO Firewall**, như vậy sẽ giúp loại bỏ khả năng xung đột chương trình.

<a name="2.1"></a>
## 2.1 Hướng dẫn Tắt Windows Firewall ##

Để  tắt Windows Firewall hãy thực hiện các bước sau:

**Bước 1**: **Chọn Start > Control Panel > Windows Firewall** để mở cửa sổ **Windows Firewall**. 

**Bước 2**. **Chọn** lựa chọn *Off (not recommended)* để tắt  **Windows Firewall** như trong  *Hình 1* dưới đây: 

![](/sbox/screen/comodo-vi/01.png)

*Hình 1: Màn hình Windows Firewall với lựa chọn OFF (Tắt) được nhấn chọn*

**Bước 3. Nhấn**: ![](/sbox/screen/comodo-vi/02.png) để tắt tường lửa của Windows.

<a name="2.2"></a>
## 2.2 Hướng dẫn cài đặt COMODO Firewall ##

**Lưu ý**: **COMODO Firewall** không tự động gỡ bỏ phiên bản cũ hay một phiên bản chương trình đã cài đặt trước đó. Bạn cần gỡ bỏ chương trình cũ trước khi cài đặt phiên bản mới hơn.

Để cài đặt **COMODO Firewall**, hãy theo các bước sau:

**Bước 1**. **Nhấn đúp chuột** vào ![](/sbox/screen/comodo-vi/03.png) để bắt đầu tiến trình cài đặt. Hộp thoại *Open File - Security Warning* (Cảnh báo An ninh - Mở Tệp) có thể xuất hiện. Nếu vậy, hãy **nhấn** ![](/sbox/screen/comodo-vi/04.png) để mở hộp thoại xác nhận sau:

![](/sbox/screen/comodo-vi/05.png)

*Hình 2: Hộp thoại Lựa chọn ngôn ngữ*

**Bước 2**. **Nhấn** ![](/sbox/screen/comodo-vi/06.png) để mở cửa sổ thông tin bản quyền *End User License Agreement*. Hãy đọc kỹ *End User License Agreement* trước khi tiến hành các bước cài đặt tiếp theo, sau đó **nhấn** ![](/sbox/screen/comodo-vi/07.png) để mở cửa sổ *Free Registration*. 

**Bước 3**:  **Không** nhập địa chỉ thư điện tử của bạn vào trường *Enter your email address (optional)*; chỉ **nhấn** ![](/sbox/screen/comodo-vi/09.png) để mở cửa sổ *Extracting the Packages* (Giải nén các Gói cài đặt).

Sau khi việc giải nén hoàn thành, khung *Firewall Setup Destination Folder* (*Thư mục Cài đặt Tường lửa*) sẽ xuất hiện.

**Bước 4**. **Nhấn** ![](/sbox/screen/comodo-vi/09.png) để chấp nhận đường dẫn thư mục cài đặt mặc định và kích hoạt màn hình *Firewall security level selection* (Lựa chọn mức an ninh Tường lửa), sau đó chọn lựa chọn *Firewall Only* (Chỉ Tường lửa) như sau: 

![](/sbox/screen/comodo-vi/11.png)

*Hình 3: Màn hình lựa chọn mức An ninh Tường lửa*

**Definition of Firewall Security Level Options**
**Định nghĩa các Lựa chọn Mức An ninh Tường lửa**

Mỗi lựa chọn mức an ninh tường lửa thích hợp cho các mức độ người dùng khác nhau. Mỗi lựa chọn có mức độ phức tạp sử dụng và độ bảo mật tương ứng, cũng như số lượng cảnh báo tới người dùng. Sau đây là một số mô tả sơ lược về các mức độ an ninh:

Chế độ **Firewall Only** (Chỉ có Tường lửa):  Lựa chọn này cho phép bạn chạy chương trình **COMODO Firewall** không có tính năng *Defense +*. Chương trình đã được xác định trước một số ứng dụng phổ biến được coi là khá an toàn (như các trình duyệt web và trình quản lý thư điện tử phía người dùng), nhằm giảm đáng kể số lượng cảnh báo an ninh tới người dùng. Chương trình đưa ra những thông tin hướng dẫn khi một màn hình cảnh báo xuất hiện. Thêm vào đó, các hành động cần thao tác cũng khá đơn giản.

Chế độ **Firewall with Optimum Proactive Defense** (Tường lửa với tính năng Chủ động Phòng vệ Tối ưu): Lựa chọn này bao gồm tính năng bảo vệ của chế độ *Firewall Only* cộng với tính năng *Defense+* được kích hoạt. *Defense+* đưa ra sự phòng ngừa tích cực chống lại các chương trình độc hại được thiết kế để phong tỏa các loại tường lửa khác nhau. *COMODO Firewall Alerts* đưa ra các thông tin giải thích chi tiết hơn về lý do một ứng dụng hay một yêu cầu bị khóa, và bạn được cung cấp lựa chọn riêng để cô lập hoặc 'cách ly' một tệp hay chương trình đáng ngờ.

Chế độ **Firewall with Maximum Proactive Defense** (Tường lửa với tính năng Chủ động Phòng vệ Tối đa): Lựa chọn này bao gồm tính năng an ninh của *Firewall with Optimum Proactive Defense*  kết hợp tính năng bảo vệ  'anti-leak' (chống dò rỉ ) để ngăn ngừa các nguy cơ an ninh 'thụ động', ví dụ như chi tiết về các cổng được mở trên máy tính bị gửi qua mạng Internet. Tính năng cách ly chương trình được thực hiện hoàn toàn tự động.  

**Bước 6**. **Nhấn** ![](/sbox/screen/comodo-vi/09.png) để kích hoạt cửa sổ *COMODO Secure DNS Configuration*, với lựa chọn  *I would like to use COMODO Secure DNS Servers* (Tôi muốn sử dụng Máy chủ DNS bảo mật COMODO) được kích hoạt như sau:

![](/sbox/screen/comodo-vi/12.png)

*Hình 4: Cửa sổ Cấu hình COMODO Secure DNS*

**Quan trọng**: Cho dù không tồn tại máy chủ **Hệ thống Tên miền** (**Domain Name System** - **DNS**) bảo mật hoàn toàn, các lợi ích của việc sử dụng Các Máy chủ Bảo mật DNS  COMODO (**COMODO Secure DNS Servers**) là rất rõ ràng. Điều này cung cấp thêm sự bảo vệ chống lại các tấn công dạng *pharming* (địa chỉ ma) và *phishing* (lừa đảo) vốn là hai dạng tấn công phổ biến bởi  những kẻ có ác tâm nhằm 'xâm nhập' hoặc hướng máy tính của bạn tới các trang web độc hại. **COMODO Secure DNS Servers** cũng có thể giúp bảo vệ bạn khỏi sự can thiệp của chính quyền, với những thiết đặt đơn giản trong quá trình cài đặt, cũng như việc giúp truy cập dễ dàng những trang web đã được đăng ký với  **COMODO**. Ví dụ, nếu bạn vô tình gõ nhầm một địa chỉ trang web, một thông báo cảnh bảo từ **COMODO Secure DNS Servers** sẽ xuất hiện như sau:

![](/sbox/screen/comodo-vi/126.png)

*Hình 5: Một ví dụ điển hình về thông báo của COMODO Secure DNS Server*


**Bước 7**. **Nhấn** vào ![](/sbox/screen/comodo-vi/09.png) để mở cửa sổ *Ready to Install COMODO Firewall* (Sẵn sàng Cài đặt COMODO Firewall), sau đó **nhấn** ![](/sbox/screen/comodo-vi/13.png) để bắt đầu tiến trình cài đặt, và mở cửa sổ *Cài đặt COMODO Firewall*. Sau khi quá trình cài đặt hoàn thành, cửa sổ *Completed the COMODO Firewall Setup Wizard* sẽ xuất hiện.

**Bước 8**. **Nhấn** ![](/sbox/screen/comodo-vi/14.png) để mở hộp thoại xác nhận *Hoàn thành*, và  **nhấn** ![](/sbox/screen/comodo-vi/14.png) để mở hộp thoại xác nhận sau:

![](/sbox/screen/comodo-vi/15.png)

*Hình 6: Hộp thoại xác nhận Firewall Installer*

**Bước 9**. **Nhấn** ![](/sbox/screen/comodo-vi/16.png) để khởi động lại máy tính, và hoàn thành quá trình cài đặt **COMODO Firewall**.

After your computer restarts itself, the The *New Private Network Detected!* screen appears as follows: 

Sau khi khởi động, cửa sổ *New Private Network Detected!* (Phát hiện Mạng riêng Mới) xuất hiện như sau:

![](/sbox/screen/comodo-vi/17.png)

*Hình 7: Cửa sổ COMODO Firewall New Private Network Detected!*

**Gợi ý**: Nếu máy tính của bạn thuộc một mạng nội bộ (LAN), hãy nhấn chọn *I would like to be fully accessible to other PCs in this network* để bật tính năng chia sẻ tệp/thư mục/máy in và/hoặc kết nối Internet.

**Bước 10**. Hãy **nhập** tên vào trường *Give a name to this network for your network* hoặc sử dụng tên mặc định như trong *Hình 7* phía trên. Hãy để lựa chọn phía dưới mục *Bước 2 - Decide if you want to trust the other PCs in this network* không được chọn và **nhấn** ![](/sbox/screen/comodo-vi/06.png) để hoàn thành quá trình cài đặt.

Biểu tượng màn hình **COMODO Firewall** và biểu tượng kết nối **COMODO Firewall** cùng xuất hiện với *Hình 7*. Trước khi kết nối vào Internet, biểu tượng kết nối xuất hiện trên *Khay Hệ thống* như sau:

![](/sbox/screen/comodo-vi/18.png)

*Hình 8: Biểu tượng kết nối của COMODO Firewall xuất hiện trên Khay Hệ thống*

Khi bạn kết nối mạng và kích hoạt các chương trình có yêu cầu kết nối (như các trình duyệt) thì ngay lập tức xuất hiện các mũi tên chỉ xuống màu vàng nhạt và/hoặc các mũi tên chỉ xuống màu xanh nhạt thể hiện các yêu cầu kết nối Internet đến hay đi như dưới đây: 

![](/sbox/screen/comodo-vi/19.png)

*Hình 9: Biểu tượng kết nối COMODO Firewall đang hoạt động*

Sau khi **COMODO Firewall** được kích hoạt, *Cửa sổ Thông báo* (*COMODO Message Center*) sẽ xuất hiện:

![](/sbox/screen/comodo-vi/20.png)

*Hình 10: Cửa sổ Thông báo COMODO Message Center*


**Lưu ý**: **Nhấn** vào đường dẫn *Learn more* để truy cập diễn đàn cộng đồng trợ giúp của  **COMODO**.

**Gợi ý**: **Nhấn phải chuột** vào biểu tượng kết nối **COMODO Firewall** trên *Khay Hệ thống* (như trong *Hình 10*) để kích hoạt trình đơn chính cũng như các trình đơn con của nó như sau:
![](/sbox/screen/comodo-vi/127.png)

*Hình 11: Trình đơn Cấu hình với các trình đơn con của biểu tượng kết nối*

Trình đơn của biểu tượng kết nối cho phép bạn lựa chọn sử dụng các thành phần của **COMODO Firewall**. **Lựa chọn **Cấu hình** sẽ kích hoạt trình đơn *Manage My Configurations* (Quản lý Cấu hình) cho phép bạn *lựa chọn* sử dụng *COMODO - Proactive Security* hay *COMODO - Internet Security* để bật tính năng cách ly chương trình/ tệp.

Hơn thế nữa, mỗi thành phần sẽ có các mức an ninh riêng có thể được điều chỉnh trong các trình đơn con của biểu tượng kết nối như bên dưới; các mức an ninh này sẽ được thảo luận cụ thể hơn ở phần **4.1 Cửa sổ Thiết đặt Hành vi Tường lửa** và mục **4.2 Cửa sổ Thiết đặt Defense+**

![](/sbox/screen/comodo-vi/128.png)

*Hình 12: Mục Trình đơn Mức An ninh Tường lửa của biểu tượng kết nối*


 



