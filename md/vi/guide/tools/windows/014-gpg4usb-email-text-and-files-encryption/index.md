

---

lang: vi
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 014
title: gpg4usb - email text and files encryption

---

**Trang chủ**

- [**http://gpg4usb.org/**](http://gpg4usb.org/)

**Yêu cầu cấu hình máy tính**

- Mọi phiên bản Windows

**Phiên bản  sử dụng trong tài liệu này**

-0.3.3

**Lần cuối kiểm tra chương này**

-Tháng 7 năm 2014

**Bản quyền**

- Phần mềm Miễn phí và Mã  nguồn Mở

**Yêu cầu đọc thêm**

- Sách Hướng dẫn Sử dụng  chương [**7. Bảo  mật Truyền thông Internet**](/vi/chuong-7)

- [**An ninh Số và Sự Riêng tư cho Những nhà Bảo vệ Nhân quyền**](https://www.frontlinedefenders.org/esecman), chương **2.4 Cryptology - Public Key Encryption (trang 38)**

**Những điều bạn sẽ đạt được**:

- Khả năng mã hóa tệp và các tin nhắn văn bản khi bạn ở bất kỳ địa điểm nào (ví dụ, ttrong quán café  Internet hay tại nơi làm việc) 
- Khả năng mã hóa tin nhắn *ngoại tuyến* (khi không kết nối với Internet) hay khi không thể  truy cập Internet, sau đó sẽ gửi tin  nhắn đi sau khi kết nối máy tính với Internet sau đó.

## 1.1 Những điều Bạn nên Biết về Công cụ này Trước Khi Bắt đầu ##

**gpg4usb** là một chương trình gọn nhẹ, đơn giản và không cần cài đặt cho phép bạn mã hóa và giải mã hóa các tin nhắn văn bản cũng như các tệp. **gpg4usb** dựa trên thuật toán mã  hóa với khóa công khai. Trong phương pháp này, mỗi bên tham gia liên lạc phải tạo một cặp khóa cho riêng mình. Khóa đầu tiên là khóa riêng. Khóa này được bảo vệ bởi một mật khẩu và được cất giữ và *không bao giờ* được tiết lộ cho bất kỳ ai .

Khóa thứ hai là khóa công khai. Khóa này cần được chia sẻ với bất kỳ ai bạn muốn liên lạc – và các đối tác liên lạc của  bạn có thể trao đổi khóa công khai của họ cho bạn. Một khi có khóa công khai của đối tác liên lạc, bạn có thể thực hiện việc gửi thư điện tử được mã hóa cho người này. Chỉ  mình đối tác này có thể  mở được tin nhắn đã mã hóa do bạn gửi bởi chỉ  mình người  này có khóa riêng tương  ứng để giải mã tin nhắn.

Tương tự như vậy, nếu bạn đính kèm một bản sao khóa công khai của bạn cho các đối tác liên lạc qua thư điện tử và cất giữ khóa riêng tương ứng của mình một cách bí mật, chỉ mình bạn có thể đọc các tin nhắn được mã hóa từ các đối tác này.

Bạn cũng có thể ký số lên các tin nhắn của mình. Người nhận tin nhắn của bạn có bản sao y hệt của khóa công khai của bạn sẽ có thể xác minh một thư  điện tử được gửi đến từ bạn, và rằng nội dung của thư điện tử  này không bị giả mạo trong  quá  trình  truyền đến  người nhận. Một cách tương  tự, nếu bạn có  khóa  công khai của một đối tác liên lạc, bạn có thể xác minh chữ  ký số của người đó trên tin nhắn gửi từ người này.


**gpg4usb** cho phép bạn tạo và mã hóa cặp khóa mã hóa, xuất các khóa công khai  để chia sẻ với các đối  tác liên lạc, soạn tin  nhắn và mã hóa tin nhắn  này. Bạn có thể đơn giản thực hiện việc sao chép và  dán khóa công khai và/hoặc tin nhắn đã được mã hóa từ **gpg4usb** vào thư điện tử của mình hoặc lưu  vào thành một tệp văn  bản để gửi đi sau đó. Các tài liệu và các  tệp cũng  có thể được mã hóa.

**Lưu ý**: Hãy để ý tới các tài liệu hoặc tệp nguyên bản không được mã hóa có thể vẫn tồn tại trên máy tính của bạn, vì vậy cả bạn và các đối tác liên lạc cần phải nhớ xóa chúng đi khi cần thiết

**gpg4usb** cho phép bạn trao đổi khóa và các tin nhắn đã mã hóa với các chương trình **GPG** hoặc **PGP** tương tự.

