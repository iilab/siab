

---

lang: vi
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 013
title: Thunderbird with Enigmail and GPG - Secure Email Client

---

**Trang chủ**

- [**www.mozilla.com/thunderbird**](http://www.mozilla.com/thunderbird/)
- [**www.enigmail.mozdev.org**](http://enigmail.mozdev.org/home/index.php)
- [**www.gnupg.org**](http://www.gnupg.org/)
- [**www.trac.torproject.org/projects/tor/wiki/torbirdy**](http://www.trac.torproject.org/projects/tor/wiki/torbirdy/)


**Yêu cầu cấu hình máy tính**

- *Mọi phiên bản Windows*

**Phiên bản sử dụng trong tài liệu này**

- Thunderbird 31.0 
- Enigmail 1.7
- GNU Privacy Guard (GnuPG) 1.4.18
-Torbirdy 0.1.2 

**Lần cập nhật cuối**

- Tháng 9 năm 2014

**Bản quyền**

- *Phần mềm Miễn phí và Nguồn mở*

**Yêu cầu đọc thêm**

- Sách Hướng dẫn [**Chương 7. Đảm bảo bảo mật truyền thông trên Internet**](/vi/chuong-7)


**Những lợi ích bạn sẽ có được**: 

- *Khả năng quản lý nhiều tài khoản thư điện tử sử dụng một chương trình duy nhất*

- *Khả năng đọc và soạn tin nhắn sau khi đã ngắt kết nối Internet*

- *Khả năng bảo mật thư điện tử bằng mã hóa với khóa công khai*


**GNU Linux, Mac OS và các Chương trình khác Tương thích với Microsoft Windows**:

Chương trình quản lý thư điện tử phía người dùng **Mozilla Thunderbird** có phiên bản cho **GNU Linux**, **Mac OS**, **Microsoft Windows** và các hệ điều hành khác. Quản lý nhiều tài khoản thư điện tử là một việc phức tạp đứng trên quan điểm bảo mật số; do đó, chúng tôi **hết sức khuyến nghị** bạn sử dụng **Mozilla Thunderbird** cho công việc này. Các tính năng bảo mật nâng cao của  **Thunderbird**, vốn là một chương trình nguồn mở, miễn phí và hoạt động trên các hệ điều hành khác nhau thậm chí còn quan trọng hơn khi đem so sánh với các phần mềm thương mại có cùng chức năng như **Microsoft Outlook**. Tuy nhiên, nếu bạn vẫn muốn sử dụng một chương trình khác  **Mozilla Thunderbird**, chúng tôi xin giới thiệu một số các chương trình miễn phí nguồn mở có tính năng tương tự:

* [**Claws  Mail**](http://www.claws-mail.org/) có phiên bản cho **GNU Linux** và **Microsoft Windows**;
* [**Sylpheed**](http://sylpheed.sraoss.jp/en/) có phiên bản cho **GNU Linux**, **Mac OS** và **Microsoft Windows**;
* [**Alpine**](http://www.washington.edu/alpine/)  có phiên bản cho **GNU Linux**, **Mac OS** và **Microsoft Windows**.

**Lưu ý**: Mặc dù chúng tôi khuyên dùng **Enigmail/GnuPG** bởi vì sự tiện dụng của các công cụ này khi kết hợp với **Thunderbird**, bạn vẫn có thể sử dụng các công cụ mã hóa độc lập như gpg4usb cùng với Thunderbird. Hãy đọc chương hướng dẫn [**gpg4usb**](/vi/gpg4usb_main) để tìm hiểu một cách khác để mã hóa thư điện tử với phương pháp mã hóa sử dụng khóa công khai. 


###Những điều cần biết về công cụ này trước khi bạn bắt đầu###

**Mozilla Thunderbird** là chương trình miễn phí, nguồn mở hoạt động trên mọi nền tảng hệ điều hành giúp quản lý việc nhận, gửi và lưu trữ thư điện tử. Một phần mềm quản lý thư điện tử phía người dùng là một chương trình giúp bạn tải về và quản lý thư điện tử mà không cần sử dụng trình duyệt Internet. Bạn có thể quản lý nhiều tài khoản thư điện tử khác nhau sử dụng chương trình này. Tài khoản của bạn phải được tạo ra trước khi dùng với **Thunderbird**. Bạn có thể tạo các tài khoản [**Gmail**](https://www.google.com/accounts/NewAccount?service=mail) hoặc [**RiseUp**](http://securityinabox.org/en/riseup_createaccount) nếu muốn.

**Enigmail** là một thành phần mở rộng (add-on) do **Thunderbird** phát triển. Nó cho phép người dùng sử dụng tính năng xác thực và mã hóa của **GNU Privacy Guard (GnuPG)**. 

**GnuPG** là một chương trình dùng để tạo và quản lý các cặp khóa mã hóa sử dụng phương pháp mã hóa với khóa công khai để đảm bảo bảo mật truyền thông. Để sử dụng **Enigmail**, bạn phải cài đặt **GnuPG** theo hướng dẫn ở phần sau của chương này. 




