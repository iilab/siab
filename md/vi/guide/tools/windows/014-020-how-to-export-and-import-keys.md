

---

lang: vi
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Export and Import Keys

---

Các mục trong trang này:

- [**3.1 Hướng dẫn Xuất Khóa Công khai của Bạn với gpg4usb**](#3.1)
- [**3.2 Hướng dẫn Nhập Khóa Công khai của Đối tác liên lạc với gpg4usb**](#3.2)
- [**3.3 Hướng dẫn Xác Minh một Khóa Công khai sử dụng gpg4usb**](#3.3)

-------

<a name="3.1"></a>
## 3.1 Hướng dẫn Xuất Khóa Công khai của Bạn với gpg4usb ##

Bạn phải gửi khóa công khai của mình cho đối tác liên lạc trước khi anh ta có thể gửi các tin nhắn mã hóa cho bạn.

Để xuất khóa công khai của mình với **gpg4usb**, hãy theo các bước sau:

**Bước 1**. **Nhấn đúp vào** ![](/sbox/screen/gpg4usb-vi/02.png) để mở thư mục **gpg4usb**

**Bước 2**. **Nhấn vào** ![](/sbox/screen/gpg4usb-vi/03.png) để kích hoạt chương trình **gpg4usb** 

**Bước 3**. **Nhấn vào biểu tượng** ![](/sbox/screen/gpg4usb-vi/10a.png) để mở cửa sổ sau:

![](/sbox/screen/gpg4usb-vi/10.png)

*Hình 2: Cửa sổ Quản lý Khóa hiển thị tất cả các khóa*

**Bước 4**. Chọn khóa tương ứng của bạn, như trong *Hình 2*

**Bước 5**. **Chọn** lệnh *Xuất ra Tệp* trong trình đơn **Khóa** như dưới đây:

![](/sbox/screen/gpg4usb-vi/11.png)

*Hình 3: Cửa sổ Quản lý Khóa với lệnh Xuất ra Tệp được chọn*

Cửa sổ sau sẽ được kích hoạt:

![](/sbox/screen/gpg4usb-vi/12.png)

*Hình 3: Cửa sổ Chọn Thư Mục để xuất tệp*

**Bước 6**. **Nhấn vào** ![](/sbox/screen/gpg4usb-vi/13.png) để lưu cặp khóa vào thư mục chương trình **gpg4usb**.

**Bước 7**: **Gửi** tệp được xuất ra gồm khóa công khai của bạn cho đối tác liên lạc bằng cách đính kèm tệp.

<a name="3.2"></a>
## 3.2 Hướng dẫn Nhập Khóa Công khai của Đối tác liên lạc với gpg4usb ##

Trước khi có thể mã hóa thông tin và gửi tới đối tác liên lạc, bạn cần nhận và nhập khóa công khai của họ. Để nhập Khóa công khai của một đối tác bằng **gpg4usb**, hãy thực hiện các bước sau:

**Bước 1**. **Nhấn đúp chuột vào** ![](/sbox/screen/gpg4usb-vi/03.png) để khởi động **gpg4usb**.

**Bước 2**. **Nhấn vào** ![](/sbox/screen/gpg4usb-vi/14.png) để kích hoạt cửa sổ sau:

![](/sbox/screen/gpg4usb-vi/15.png)

*Hình 4: Hộp thoại Nhập Khóa*

**Bước 3**. **Tìm tới** và chọn tệp chứa khóa bạn muốn nhập.

![](/sbox/screen/gpg4usb-vi/16g.png)

*Hình 5: Mở một tệp chứa Khóa*

**Bước 4**. Nhấn Open để mở cửa sổ sau:

![](/sbox/screen/gpg4usb-vi/16a.png)

*Hình 6: Thông tin chi tiết Khóa*

**Bước 5**. Nhấn OK để đóng cửa sổ này lại và quay trở lại màn hình chính của **gpg4usb**. Cửa sổ này hiển thị thông tin khóa công khai vừa nhập vào như dưới đây. 

![](/sbox/screen/gpg4usb-vi/16b.png)

*Hình 7: Giao diện gpg4usb hiển thị khóa công khai vừa được nhập vào liên quan tới tài khoản của  đối tác liên lạc*

Bạn đã nhập thành công khóa công khai của một đối tác liên lạc, bạn cần phải kiểm tra và ký số khóa vừa nhập vào này.

<a name="3.3"></a>
## 3.3 Hướng dẫn Xác Minh một Khóa Công khai sử dụng gpg4usb ##

Bạn phải kiểm tra một khóa được nhập về thực sự thuộc về đối tác liên lạc đã gửi nó cho bạn sau đó xác minh khóa này chưa hề bị sửa đổi. Đây là một bước hết sức quan trọng mà bạn và đối tác liên lạc nên thực hiện cho từng khóa công khai nhận được.

Để kiểm tra một cặp khóa, hãy thực hiện các bước sau:

**Bước 1**. **Liên lạc** với đối tác liên lạc qua một cách khác ngoài thư điện tử. 

**Lưu ý**: Bạn có thể gọi điện, nhắn tin hoặc, **Gọi điện qua Internet** (**VoIP**) hay một phương thức liên lạc bất kỳ nào khác, nhưng luôn phải chắc chắn rằng mình đang nói chuyện với đúng đối tác liên lạc cần xác minh về khóa. Vì lý do này, gọi điện hoặc gặp mặt trực tiếp tại thời gian và địa điểm phù hợp đảm bảo an toàn cho phép chắc chắn rằng người bạn nói chuyện được xác định về danh tính.

**Bước 2**. Cả bạn lẫn đối tác liên lạc cần kiểm tra 'dấu tay số' của khóa công khai của cả hai đã trao đổi.  

**Lưu ý**: Một dấu vân tay số là dãy duy nhất các số và chữ cái xác định một khóa. Dấu vân tay số không phải giữ bí mật và có thể ghi lại để sử dụng với mục đích kiểm tra sau này khi cần.

Để kiểm tra vân tay số của một khóa mã hóa bạn vừa tạo và của khóa công khai của đối tác bạn vừa nhập, hãy theo các bước sau:

**Bước 1**. **Chọn** một khóa, **nhấn phải chuột** để mở trình đơn cảm ngữ cảnh tương ứng.

**Bước 2**. **Chọn** lệnh *Hiển thị thông tin Khóa* như trong *Hình 8*. 

![](/sbox/screen/gpg4usb-vi/17.png)

*Hình 8: Trình đơn tương ứng với khóa của đối tác liên lạc*

*Cửa sổ sau sẽ xuất hiện:*

![](/sbox/screen/gpg4usb-vi/18.png)

*Hình 9: Chi tiết Khóa với dấu vân tay ở phần cuối*

**Bước 3**. **So sánh** dấu vân tay số này với dấu vân tay số hiển thị trong chương trình **gpg4usb** của đối tác liên lạc.

Đối tác liên lạc của bạn cũng cần thực hiện các bước trên. Xác minh vân tay số cho từng khóa hai bên trao đổi để đảm bảo chúng giống như của người gửi. Nếu chúng không trùng nhau, hãy trao đổi lại khóa công khai và thực hiện lại các bước xác minh trên.

Nếu các dấu vân tay số trùng nhau *hoàn toàn*, bạn và đối tác liên lạc đã sẵn sàng để gửi các tin nhắn và tệp mã hóa cho nhau.

