

---

lang: vi
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: How to Install gpg4usb and Generate a Key Pair

---

Các mục trong trang này:


- [**2.0 Hướng dẫn cài đặt gpg4usb**](#2.0)
- [**2.1 Hướng dẫn Tạo một Cặp Khóa với gpg4usb**](#2.1)

-------

<a name="2.0"></a>
## 2.0 Hướng dẫn cài đặt gpg4usb ##

**gpg4usb** là một công cụ không yêu cầu phải cài đặt lên máy tính của bạn. Phần mềm này được phân phối dưới dạng tệp nén zip và có thể được giải nén trực tiếp lên một ổ nhớ USB hoặc vào một thư mục trên máy tính của bạn; để bắt đầu tiến trình cài đặt hãy theo các bước sau:

**Bước 1**. **Xác định** thư mục chứa tệp nén **gpg4usb**, và **giải nén** tất cả các tệp vào một thẻ nhớ USB hoặc lên một thư mục trên máy tính của bạn:

![](/sbox/screen/gpg4usb-vi/01.png)

*Hình 1: Xác định thư mục chứa chương trình gpg4usb*

<a name="2.1"></a>
## 2.1 Hướng dẫn Tạo một Cặp Khóa với gpg4usb ##

Trước khi bạn bắt đầu mã hóa và giải mã thư điện tử, các tài liệu, tệp hay các tin nhắn văn bản, bạn phải thực hiện hai bước chuẩn bị: trước tiên bạn cần tạo ra hoặc nhập cặp khóa mã hóa của bạn và tiếp theo bạn cần gửi khóa công khai của mình cho các đối tác liên lạc đồng thời nhận khóa công khai của họ và nhập vào keyring (xâu chìa khóa, quản lý các khóa mã hóa trong hệ thống của bạn) của mình. Chúng tôi sẽ hướng dẫn cách chia sẻ khóa công khai trong trang kế tiếp. **gpg4usb** trợ giúp bạn việc sinh cặp khóa của mình ngay khi khởi động chương trình lần đầu. Lưu ý rằng bạn luôn có thể quay trở lại trang trợ giúp *Getting Started* này từ trình đơn *Trợ Giúp → Open Wizard*.

**Bước 1**. Để kích hoạt chương trình **gpg4usb** lần đầu tiên,  ** tìm tới thư mục và nhấn đúp chuột** vào ![](/sbox/screen/gpg4usb-vi/02.png) để mở thư mục **gpg4usb** sau đó **nhấn đúp chuột** vào ![](/sbox/screen/gpg4usb-vi/03.png). Cửa sổ Getting Started sẽ mở. Hãy chọn ngôn ngữ **Tiếng Việt** và nhấn Next.

**Bước 2**. Trong cửa sổ *Choose your Action*, nhấn vào đường dẫn *Create a new key pair*.

![](/sbox/screen/gpg4usb-vi/04.png)

*Hình 2: Cửa số Chọn một hành động*

Hãy lưu ý các tùy chọn khác để nhập các khóa đã sẵn có trong cửa sổ First Start Winzard. Nếu bạn nâng cấp phần mềm từ phiên bản cũ của gpg4usb, bạn có thể chọn hành động *import settings and/or keys from gpg4usb* (*nhập các thiết đặt và/hoặc khóa từ gpg4usb*). Nếu bạn sử dụng [Thunderbird with Enigmail](https://securityinabox.org/vi/thunderbird-main), bạn có thể chọn hành động *import keys from GnuPG* (*nhập khóa từ GnuPG*). Bạn cũng có thể chọn nhập các khóa sau bằng cách mở cửa sổ hỗ trợ tử trình đơn *Trợ Giúp -> Open Winzard*.

**Bước 3.** Tại khung *Create a keypair* **nhấn vào** *Create New Key* 

![](/sbox/screen/gpg4usb-vi/05.png)

*Hình 3: Tạo Khóa Mới*

**Bước 4**. **Điền** thông tin tương ứng vào các trường yêu cầu, cửa sổ có  dạng như dưới đây :

![](/sbox/screen/gpg4usb-vi/06.png)

*Hình 4: Ví dụ một khung Tạo Khóa được điền đầy đủ*

**Quan trọng:**:
- Hãy đặt  một mật khẩu mạnh để  bảo vệ khóa riêng của mình (hãy xem thêm tại chương [**3. Làm thế nào để tạo và duy trì mật khẩu bảo mật**](/vi/chuong-3).
- Chúng tôi khuyên bạn sử dụng ngày hết hạn cho khóa sinh ra và đặt thời gian hết hạn ít hơn 5 năm.
- Chúng tôi hết sức khuyến cáo nên tạo khóa có độ mạnh tối thiểu 2048 bít. Khóa có độ mạnh lớn hơn sẽ bảo mật hơn tuy nhiên sẽ cần nhiều thời gian hơn để sinh ra, mã hóa và giải mã

**Lưu ý:** Bạn không cần phải sử dụng tên thật hay địa chỉ thư điện tử thật của mình khi tạo ra cặp khóa. Tuy nhiên, sử dụng địa chỉ thư điện tử bạn sử dụng trong liên lạc sẽ giúp đối tác của bạn thuận lợi trong việc thêm và quản lý khóa của bạn tương ứng với tài khoản liên lạc.

**Bước 5**. Nhấn OK để tạo cặp khóa. 

![](/sbox/screen/gpg4usb-vi/07.png)

*Hình 5: Tạo ra khóa...* 

![](/sbox/screen/gpg4usb-vi/08.png)

*Hình 6: Khóa được tạo ra*

**Bước 6**.  **Nhấn** OK để quay trở về cửa sổ **gpg4usb**. Sau khi cặp khóa đã được tạo ra thành công, bạn có thể thấy thông tin trên cửa sổ giống như sau: 

![](/sbox/screen/gpg4usb-vi/09.png)

*Hình 7: Khóa được tạo ra*

Bạn vừa tạo thành công một cặp khóa mã hóa, giờ bạn sẽ tìm hiểu cách xuất khóa công khai để chía sẻ  với các đối tác liên lạc, và cách nhập khóa công khai của các đối tác này.

