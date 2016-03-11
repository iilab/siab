

---

lang: vi
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: How to Encrypt Your Backup File

---

Các mục trong trang này:

- [**4.0 Giới thiệu về Mã hóa**](#4.0)
- [**4.1 Hướng dẫn Mã hóa Tệp Sao lưu**](#4.1)
- [**4.2 Hướng dẫn Giải mã Tệp Sao lưu**](#4.2)

-------

<a name="4.0"></a>
## 4.0 Giới thiệu về Mã hóa ##

Việc mã hóa là rất cần thiết cho những ai muốn bảo mật các bản sao lưu của mình chống lại những truy cập trái phép.

*Mã hóa* là quá trình tạo mã hay xáo trộn dữ liệu theo một phương pháp khiến dữ liệu trở nên không thể xử lý được đối với những ai không có chìa khóa giải mã. Để có thêm thông tin về việc mã hóa, hãy tham khảo **Hướng dẫn Sử dụng** Chương [**4. Làm thế nào để bảo vệ thông tin mật trên máy tính của bạn**](http://securityinabox.org//vi/chuong-4)


<a name="4.1"></a>
## 4.1 Hướng dẫn Mã hóa Bản sao lưu ##

Cửa sổ *Strong encryption* xác định phương pháp mã hóa được sử dụng.


**Bước 1**: **Chọn** danh sách xổ xuống *Encryption type* để xem danh sách các phương pháp mã hóa khác nhau như sau:

![](/sbox/screen/cobian-vi/30.png)

*Hình 1:  Danh sách các phương pháp Mã hóa*

Để cho quá trình được đơn giản, chúng tôi khuyên bạn nên chọn một trong hai lựa chọn: *Blowfish* hoặc *Rijndael* (128 bits). Những lựa chọn này cung cấp tính bảo mật cao cho tệp nén của bạn và cho phép bạn sử dụng một mật khẩu tùy chọn.

**Bước 2**. **Chọn** Phương pháp *Mã hóa* bạn muốn sử dụng.

**Lưu ý**: *Rijndael* và *Blowfish* đề có mức bảo mật tương đương. *DES* có mức độ bảo mật thấp hơn tuy nhiên tiến trình mã hóa sẽ nhanh hơn.

**Bước 3**: **Nhập** và **xác nhận mật khẩu** vào hai ô tương ứng như bên dưới.

![](/sbox/screen/cobian-vi/31.png)

*Hình 2: Các dạng mã hóa và các trường nhập mật khẩu*

Độ phức tạp của mật khẩu được thể hiện ở thanh trạng thái có tên ‘Passphrase quality’. Thanh trạng thái này càng chạy nhiều về phía bên phải thể hiện mật khẩu càng mạnh. Hãy tham khảo Sách Hướng dẫn chương [**3. Làm thế nào để tạo và duy trì mật khẩu bảo mật**](/vi/chuong-3) và [**Hướng dẫn Thực hành KeePass**](/vi/keepass-main) để có thêm hướng dẫn về cách tạo và lưu trữ mật khẩu bảo mật.

**Bước 4**. **Nhấn vào** ![](/sbox/screen/cobian-vi/13.png).

<a name="4.2"></a>
## 4.2 Hướng dẫn Giải mã Tệp Sao lưu ##

Việc giải mã tệp sao lưu khá dễ dàng và nhanh chóng. Để giải mã tệp sao lưu mã hóa, hãy theo các bước sau:

**Bước 1**. **chọn > Tools > Decrypter and Keys** như dưới đây:

![](/sbox/screen/cobian-vi/32.png)

*Hình 3: Trình đơn Tools với chọn lựa Decrypter and Keys*

*Cửa sổ Decrypter and Keys sẽ xuất hiện như sau:*

![](/sbox/screen/cobian-vi/33.png)

*Hình 4: Cửa sổ Cobian Backup 10 Decrypter and Keys*

**Bước 2**. **Nhấn vào** ![](/sbox/screen/cobian-vi/34.png) để chọn tệp sao lưu mã hóa bạn muons giải mã.

**Bước 3**. **Nhấn vào** ![](/sbox/screen/cobian-vi/35.png) để chọn thư mục lưu kết quả giải mã.

**Bước 4**. **Chọn** dạng mã hóa bạn đã lựa chọn trong mục [4.0 Hướng dẫn Mã hóa Tệp sao lưu](/vi/cobianbackup_mahoatepsaoluu#4.1), trong danh sách *New Methods*

![](/sbox/screen/cobian-vi/36.png)

*Hình 5: Danh sách New Methods*

**Bước 4**.  **Chọn** một một phương pháp giải mã thích hợp (chính là phương pháp mã hóa bạn đã dùng để mã hóa tệp nén của mình ).

**Bước 5**. **Nhập** mật khẩu vào trường *Passphrase*.

**Bước 6**. **Nhấn vào** ![](/sbox/screen/cobian-vi/37.png).

Các tệp được giải mã sẽ nằm trong thư mục bạn đã chọn. Nếu đó là các tệp nén, bạn sẽ cần giải nén chúng như đã đề cập tại mục [**3.1 Hướng dẫn giải nén**](/vi/cobianbackup_huongdannen#3.1).

