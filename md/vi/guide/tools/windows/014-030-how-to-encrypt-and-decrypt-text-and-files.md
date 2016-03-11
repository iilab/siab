

---

lang: vi
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: How to Encrypt and Decrypt Text and Files

---

Các mục trong trang này


- [**4.0 Hướng dẫn Mã hóa Tin nhắn Văn bản với gpg4usb**](#4.0)
- [**4.1 Hướng dẫn Giải mã hóa Tin nhắn Văn bản với gpg4usb**](#4.1)
- [**4.2 Hướng dẫn Mã hóa Tệp với gpg4usb**](#4.2)
- [**4.3 Hướng dẫn Giải mã Tệp với gpg4usb**](#4.3)

-------

<a name="4.0"></a>
## 4.0 Hướng dẫn Mã hóa Tin nhắn Văn bản với gpg4usb ##

Trong ví dụ dưới đây, Terrence sẽ mã hóa một thư điện tử gửi cho người bạn là Salima theo các bước sau đây:

**Bước 1**. **Nhấn đúp chuột vào** ![](/sbox/screen/gpg4usb-vi/03.png) để mở giao diện chính chương trình **gpg4usb**.

**Bước 2**. **Soạn thảo** tin nhắn như trong ví dụ dưới đây:

![](/sbox/screen/gpg4usb-vi/19.png)

*Hình 1: Cửa sổ giao diện gpg4usb hiển thị một ví dụ về tin nhắn*

**Bước 3**. **Chọn** hộp chọn tương ứng với địa chỉ thư điện tử của người nhận như sau:

![](/sbox/screen/gpg4usb-vi/20.png)

*Hình 2: Giao diện gpg4usb hiển thị người nhận được chọn, được tô đậm*

**Lưu ý:** Bạn có thể mã hóa một tin nhắn cho nhiều hơn một người nhận với một thao tác đơn giản là chọn các hộp chọn tương ứng trong khung *Mã hóa cho:*. Đồng thời, cũng rất hữu ích khi bạn mã hóa tin nhắn cho bản thân mình để lưu giữ những tin nhắn đã gửi đi để có thể tham khảo sau này. 

**Bước 4**. **Nhấn chuột vào** ![](/sbox/screen/gpg4usb-vi/21.png) hoặc **chọn Mã hóa** từ trình đơn **Mã hóa** để mã hóa tin nhắn như trong hình dưới đây:

![](/sbox/screen/gpg4usb-vi/22.png)

*Hình 3: Cửa sổ giao diện gpg4usb hiển thị một ví dụ tin nhắn được mã hóa*

**Bước 5**. **Nhấn chuột vào** ![](/sbox/screen/gpg4usb-vi/23.png) để chọn toàn bộ tin nhắn được mã hóa, sau đó **nhấn chuột vào** ![](/sbox/screen/gpg4usb-vi/24.png) để chép đoạn mã vào bộ nhớ.

**Lưu ý**: Một cách khác bạn có thể sử dụng tổ hợp phím tắt cho từng lệnh trên trình đơn, trong trường hợp này là **Ctrl + E** sẽ mã hóa tin nhắn, **Ctri + A** sẽ chọn toàn bộ tin nhắn được mã hóa, và **Ctrl + C** sẽ chép toàn bộ tin nhắn vào bộ nhớ. 


**Bước 6**. **Mở** hộp thư của bạn và **tạo** một thư mới, sau đó **chép** tin nhắn từ bộ nhớ vào như dưới đây:

![](/sbox/screen/gpg4usb-vi/25.png)

*Hình 4: Ví dụ một tin nhắn được mã hóa trong gpg4usb được chép vào trình soạn thảo trong tài khoản Gmail*

**Lưu ý**: **Văn bản có định dạng** **RTF** có thể gây lỗi định dạng của tin nhắn mã hóa; do đó, tốt nhất nên soạn thảo tin nhắn của bạn dưới dạng văn bản thuần. Để chuyển đổi định dạng **RTF** sang dạng thuần văn bản trong **Gmail** đơn giản chỉ cần **Nhấn chuột vào** biểu tượng *More Options* và **chọn** *Plain Text Mode* nằm trên trình đơn định dạng phía trên khung soạn thảo như dưới đây:

![](/sbox/screen/gpg4usb-vi/26.png)

*Hình 5: Tùy chọn More Options của Gmail*


<a name="4.1"></a>
## 4.1 Hướng dẫn Giải Mã hóa Tin nhắn Văn bản với gpg4usb ##

Để giải mã tin nhắn được mã hóa, hãy thực hiện các bước sau:

**Bước 1**. **Nhấn đúp chuột vào** ![](/sbox/screen/gpg4usb-vi/03.png) để mở chương trình **gpg4usb**.

**Bước 2**. **Mở** hộp thư điện tử của bạn, sau đó **mở** tin nhắn.

**Bước 3**. **Chọn**, **sao** sau đó **chép** tin nhắn đã được mã hóa vào khung *untitled1.txt* của giao diện **gpg4usb** như sau:

![](/sbox/screen/gpg4usb-vi/27.png)

*Hình 6: Giao diện gpg4usb hiển thị tin nhắn cần giải mã*

**Lưu ý**: Nếu tin nhắn được mã hóa chứa cách dòng kép như trong *Hình 6* bên dưới, **gpg4usb** có thể không tự động giải mã được. Để loại bỏ, **chọn** ![](/sbox/screen/gpg4usb-vi/27b.png) từ trình đơn **Soạn thảo** và sau đó tiếp tục tiến trình giải mã tin nhắn trong **Bước 4**.

![](/sbox/screen/gpg4usb-vi/28.png)

*Hình 7: Giao diện gpg4usb hiển thị một tin nhắn cần giải mã có chứa các cách dòng kép*
 
**Bước 4**. **Nhấn chuột vào** ![](/sbox/screen/gpg4usb-vi/29.png) và nhập mật khẩu bạn đã tạo khi tạo cặp khóa, như trong hình sau:

![](/sbox/screen/gpg4usb-vi/30.png)

*Hình 8: Cửa sổ Nhập Mật khẩu*

**Bước 5**. **Nhấn chuột vào** OK để kích hoạt giao diện **gpg4usb** như trong *Hình 2* phía trên.

<a name="4.2"></a>
## 4.2 Hướng dẫn Mã hóa Tệp với gpg4usb ##

Tiến trình mã hóa một tệp cũng tương tự như việc mã hóa một tin nhắn văn bản; trong ví dụ dưới đây, Salima sẽ mã hóa một tệp gửi cho Terence, theo các bước sau:

**Bước 1**. **Nhấn đúp chuột vào** ![](/sbox/screen/gpg4usb-vi/03.png) để mở chương trình **gpg4usb**.

**Bước 2**. **Nhấn chuột vào** ![](/sbox/screen/gpg4usb-vi/31.png) để mở cửa sổ sau:

![](/sbox/screen/gpg4usb-vi/32.png)

*Hình 9: Cửa sổ Mã hóa / Giải mã Tệp, với tùy chọn Giải mã mặc định được bật*

Cửa sổ *Mã hóa / Giải mã Tệp* với thanh cuộn (được tô đậm) cho phép bạn chọn tài khoản thư và khóa mã hóa tương ứng sử dụng để mã hóa tin nhắn.

**Bước 3**. **Chọn** nút *Mã hóa* và sau đó **nhấn chuột vào** ![](/sbox/screen/gpg4usb-vi/33.png) để mở cửa sổ sau:

![](/sbox/screen/gpg4usb-vi/34.png)

*Hình 10: Cửa sổ Duyệt Thư mục*

**Bước 4**. **Nhấn chuột vào** ![](/sbox/screen/gpg4usb-vi/35.png) để chọn tệp cần mã hóa và quay trở lại cửa sổ *Mã hóa / Giải mã* như sau:

![](/sbox/screen/gpg4usb-vi/36.png)

*Hình 11: Cửa sổ Mã hóa / Giải mã Tệp hiển thị tệp được chọn để mã hóa*

**Bước 5**. **Nhấn chuột vào** OK để mở cửa sổ sau:

![](/sbox/screen/gpg4usb-vi/38.png)

*Hình 12: Hộp thoại thông báo hoàn thành*

Hộp thoại thông báo *Hoàn thành* cho bạn biết nơi lưu tệp vừa mã hóa. Một tệp được mã hóa có thể được xác định bằng đuôi *.asc*, ví dụ, *Meeting Minute.odt.asc*. 

**Bước 6**. **Nhấn chuột vào** OK để hoàn tất quá tình mã hóa tệp.

**Lưu ý**: Bạn có thể mã hóa một tin nhắn văn bản và gửi kèm với một tệp mã hóa một cách riêng biệt. 

**Bước 7**. Sử dụng hộp thư của bạn, **chuyển tới** thư mục được xác định trong hộp thoại xác nhận *Hoàn thành* (*Hình 12*), sau đó đính kèm tệp mã hóa vào thư điện tử bạn muốn gửi đi giống như một tệp bình thường. 

**Quan trọng**: Hãy lưu ý rằng tên của tệp sẽ **không được mã hóa**. Hãy đảm bảo rằng tên tệp không tiết lộ bất cứ thông tin quan trọng nào! Đừng quên rằng tệp nguyên bản chưa được mã hóa vắn còn nằm trên ổ đĩa.

<a name="4.3"></a>
## 4.3 Hướng dẫn Giải mã Tệp với gpg4usb ##

Trong ví dụ dưới đây, Terence sẽ giải mã tệp nhận được từ Salima, theo các bước sau:

**Bước 1**. **Nhấn đúp chuột vào** ![](/sbox/screen/gpg4usb-vi/03.png) để kích hoạt chương trình **gpg4usb**.

**Bước 2**. **Mở** hộp thư của bạn, và **mở** tin nhắn và **tải về** tệp đính kèm.

**Lưu ý**: Nếu đối tác liên lạc của bạn có gửi tin nhắn được mã hóa có đính kèm theo tệp mã hóa, bạn có thể giải mã tin nhắn này theo phương pháp đã hướng dẫn tại mục [**4.1 Hướng dẫn Giải Mã hóa Tin nhắn Văn bản với gpg4usb**](https://securityinabox.org/vi/gpg4usb_mahoatep#4.1)

**Bước 3**. Trong giao diện **gpg4usb**  (như trong *Hình 1* phía trên), **Nhấn chuột vào** ![](/sbox/screen/gpg4usb-vi/31.png) để kích hoạt cửa sổ **Mã hóa / Giải mã tệp**  (như trong *Hình 13* phía trên). 

**Bước 4**. **Nhấn chuột vào** ![](/sbox/screen/gpg4usb-vi/33.png) để mở thư mục chứa tệp mã hóa vừa tải về như dưới đây:

![](/sbox/screen/gpg4usb-vi/37.png) 

*Hình 13: Cửa sổ Mã hóa / Giải mã hiển thị đường dẫn tới tệp mã hóa*

**Bước 5**. **Nhấn chuột vào** OK để kích hoạt cửa sổ sau:

![](/sbox/screen/gpg4usb-vi/39.png) 

*Hình 14: Hộp thoại Xác nhận Hoàn thành hiển thị đường dẫn tới tệp được giải mã*

**Quan trọng**: Nếu bạn làm việc từ một quán café Internet hoặc sử dụng chung một máy tính có nhiều người sử dụng, tốt nhất hãy chép tệp *.asc* vào thẻ nhớ USB hoặc ổ nhớ di động và giải nén tại nhà trong điện kiện đảm bảo tính riêng tư.

