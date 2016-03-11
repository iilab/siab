

---

lang: vi
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Configure Important Thunderbird Settings

---

Các mục trong trang này:


- [**3.0 Các Tùy chọn Bảo mật trong Thunderbird**](#3.0)
- [**3.1 Hướng dẫn Tắt Tính năng Khung Đọc thư trong Thunderbird**](#3.1)
- [**3.2 Hướng dẫn Tắt Tính năng HTML trong Thunderbird**](#3.2)
- [**3.3 Hướng dẫn Thiết đặt Khung Bảo mật trong Thunderbird**](#3.3)
- [**3.4 Hướng dẫn Bật Bộ lọc Thư rác trong Thiết đặt Tài khoản**](#3.4)

-------

<a name="3.0"></a>
## 3.0 Các Tùy chọn Bảo mật trong Thunderbird ##

Bảo mật trong **Mozilla Thunderbird** liên quan tới việc bảo vệ máy tính của bạn khỏi các tin nhắn thư điện tử độc hại. Một số thư loại này có thể chỉ là những thư rác, số khác có thể chứa vi rút hoặc phần mềm gián điệp. Có một số thiết đặt cần được sử dụng và cấu hình trong **Mozilla Thunderbird** để tăng cường bảo mật cho chương trình. Một điều cũng *rất quan trọng* là máy tính của bạn có cài đặt các chương trình diệt phần mềm gián điệp và tường lửa. 

Để có thêm thông tin liên quan tới phòng chống các xâm nhập độc hại, hãy tham khảo sách **Hướng dẫn** chương [**1. Bảo vệ máy tính khỏi Vi rút, Phần mềm độc hại và Hacker**](/vi/chuong-1) để có thêm thông tin về các công cụ như  [**Avast**](/vi/avast-main), [**Comodo Firewall**](/vi/comodo-main), [**Spybot**](/vi/spybot-main).


<a name="3.1"></a>
## 3.1 Hướng dẫn Tắt Tính năng Khung Đọc thư trong Thunderbird ##

Cửa sổ chính của **Thunderbird** được chia thành ba vùng: Vùng bên trái hiển thị các thư mục trong các tài khoản thư điện tử của bạn, vùng bên phải hiển thị danh sách các tin nhắn đã nhận, và khung bên dưới hiển thị *xem trước nội dung* (preview) của một tin nhắn được chọn. Việc hiển thị xem trước nội dung sẽ tự động được thực hiện mỗi khi một tin nhắn được chọn.

**Lưu ý**: Nếu tin nhắn đó có chứa mã độc hại, thị nó sẽ được kích hoạt bởi cửa sổ xem trước này. Để tránh điều này xảy ra, bạn nên tắt tính năng xem trước này.


![](/sbox/screen/thunderbird-vi-1/23.png)

*Hình 1: Cửa sổ giao diện chính Thunderbird*

Để tắt tính năng khung xem trước, hãy thực hiện các bước sau:

**Bước 1. Nhấn vào** ![](/sbox/screen/thunderbird-vi-1/24a.png). **Chọn Options > Bố cục chương trình**, và **chọn** the *Khung Đọc thư F8* để tắt: 

![](/sbox/screen/thunderbird-vi-1/24.png)

*Hình 2: Trình đơn Hiển thị với khung Bố cụng chương trình và lựa chọn Khung Đọc thư* 

*Khung Đọc thư* sẽ biến mất, và bạn phải **nhấn đúp chuột** vào một tin nhắn để đọc nó. Nếu một tin nhắn có vẻ đáng ngờ (có thể vì nó có một tiêu đề đáng ngờ hay người gửi không rõ ràng) thì bạn có thể xóa tin nhắn đó mà không mở tin nhắn này.

<a name="3.2"></a>
## 3.2 Hướng dẫn Tắt tính năng HTML trong Thunderbird ##

**Thunderbird** có khả năng tạo và hiển thị các thư điện tử sử dụng ngôn ngữ giống như trong các trang web là **HyperText Markup Language** (HTML). Tính năng này cho phép bạn gửi và nhận các tin nhắn kèm theo ảnh, phông chữ, màu sắc và các định dạng khác. Tuy nhiên nếu bạn bật tính năng định dạng **HTML** trong **Thunderbird**, các thư điện tử độc hại có thể khai thác các lỗ hổng bảo mật giống như đối với một trang web. 
 
Để tắt tính năng định dạng **HTML**, hãy thực hiện các bước sau: 

**Bước 1. Nhấn vào** ![](/sbox/screen/thunderbird-vi-1/24a.png). **Chọn Hiển thị > Nội dung thư dưới dạng > Văn bản Thuần** như sau: 

![](/sbox/screen/thunderbird-vi-1/25.png)

*Hình 3: T Trình đơn Hiển thị với khung Bố cụng chương trình và lựa chọn Văn bản Thuần*

<a name="3.3"></a>
### 3.3 Hướng dẫn thiết đặt chọn lựa Bảo mật ###

**Thunderbird** được tích hợp hai bộ lọc *thư rác* có thể giúp xác định thư rác trong các thư bạn nhận được. Mặc định, các bộ lọc này bị tắt, nên bạn cần phải thay đổi một số thiết đặt nếu bạn muốn sử dụng chúng. Ngay cả khi chúng được bật, bạn vẫn tiếp tục nhận được các thư rác nhưng **Thunderbird** sẽ tự động đưa chúng vào thư mục *Thư rác*.

Những thư đánh lừa hay các *thư giả mạo*, thường tìm cách khiến bạn nhấn chuột vào một đường dẫn gửi kèm theo tin nhắn. Thông thường các đường dẫn này sẽ dẫn tới các trang web có chứa vi rút có thể lây nhiễm lên máy tính của bạn. Một số trường hợp khác, các đường dẫn này mở ra các trang có vẻ hợp lệ nhằm đánh lừa bạn nhập vào tên đăng nhập và mật khẩu của bạn, để lấy các thông tin này phục vụ lợi ích bất chính của những kẻ tạo ra các trang web giả này. 

**Thunderbird** có thể giúp nhận dạng và cảnh báo bạn đối với các dạng thư điện tử nói trên. Các công cụ bổ sung giúp phòng chống lây nhiễm từ các trang web độc hại được đề cập tại phần [**Các Thành phần mở rộng hữu ích khác của Mozilla**](/vi/firefox_cacthanhphanmorongkhac) trong chương giới thiệu về **Firefox**.

Nhóm lựa chọn thiết đặt liên quan tới thư rác và an ninh được đặt tại cửa sổ *Tùy chọn – An ninh*, nơi bạn có thể thiết đặt các lựa chọn quan trọng về an ninh và bảo mật. Để mở cửa sổ này, hãy theo các bước sau:

**Bước 1**. **Chọn Công cụ > Options** để vào cửa sổ *Tùy chọn*.

**Bước 2**. **Nhấn** ![](/sbox/screen/thunderbird-vi-1/26.png) để kích hoạt cửa sổ sau:

![](/sbox/screen/thunderbird-vi-1/27.png)

*Hình 4: Cửa sổ An ninh với các khung liên quan*

### Khung Thư rác ###

**Bước 1**. **Chọn** các lựa chọn tương ứng trong khung *Thư rác* như trong *Hình 4* nếu bạn muốn **Thunderbird** xóa những tin nhắn được bạn xác định là các *thư rác*. Các thiết đặt liên quan tới thư rác sẽ được đề cập sau trong phần này

### Khung Lừa đảo email ###

**Bước 1**. **Nhấn chọn**  *Báo tôi biết nếu thư tôi đang đọc bị nghi ngờ là thư xấu* để yêu cầu **Thunderbird** phân tích các tin nhắn tìm thư lừa đảo như dưới đây: 

![](/sbox/screen/thunderbird-vi-1/28.png)

*Hình 5: Khung Lừa đảo email* 

### Khung Diệt Virút ###

**Bước 1**. **Nhấn** khung *Diệt Virút* để mở cửa sổ sau: 

![](/sbox/screen/thunderbird-vi-1/29.png)

*Hình 6: Khung diệt virút* 

Lựa chọn này cho phép chương trình diệt vi rút trên máy có thể quét kiểm tra từng tin nhắn khi chúng được tải về. Nếu lựa chọn này không được bật, có khả năng toàn bộ thư mục *Hộp thư* của bạn sẽ bị ‘phong tỏa’ nếu bạn nhận được một tin nhắn bị nhiễm virút. 

**Lưu ý** Điều này giả sử rằng máy tính của bạn có cài đặt một chương trình diệt vi rút. Hãy xem phần hướng dẫn sử dụng [**Avast**](/vi/avast-main) để biết các cài đặt và cấu hình chương trình diệt vi rút.

### Khung Mật khẩu ###

**Bước 2**. **Nhấn** khung *Mật khẩu* để mở cửa sổ sau: 

![](/sbox/screen/thunderbird-vi-1/30.png)

*Hình 7: Khung Mật khẩu*

**Quan trọng:** Chúng tôi khuyên bạn nên lưu trữ mật khẩu bảo mật của mình sử dụng chương trình được thiết kế riêng cho mục đích này; hãy xem chương [**KeyPass**](/vi/keepass-main) để tìm hiểu thêm. 

**Lưu ý**: Các tùy chọn trong khung *Mật khẩu* chỉ có tác dụng khi bạn nhấn chọn ô *Ghi nhớ mật khẩu* tại màn hình *Thiết đặt Tài khoản Thư* trong quá trình đăng ký các tài khoản thư điện tử với **Thunderbird**. 

**Bước 1**. **Nhấn** ![](/sbox/screen/thunderbird-vi-1/31.png) để mở cửa sổ sau:

![](/sbox/screen/thunderbird-vi-1/32.png)

*Hình 8: Cửa sổ Lưu Mật khẩu*

Cửa sổ *Mật khẩu được Lưu* cho phép bạn xóa bỏ hoặc xem tất cả các mật khẩu tương ứng với các tài khoản thư. Tuy nhiên, để đảm bảo tối đa an ninh và bảo mật riêng tư của bạn, bạn có thể chọn một *Mật khẩu Chính* để ngăn chặn những kẻ thông thạo **Thunderbird** tìm thấy các mật khẩu của mình.

**Bước 3**. **Nhấn chọn** ô *Dùng một mật khẩu chính* như trong *Hình 7* để kích hoạt nút *Thay đổi Mật khẩu Chính ...*.

**Bước 4**. **Nhấn** ![](/sbox/screen/thunderbird-vi-1/33.png) để mở cửa sổ sau:

![](/sbox/screen/thunderbird-vi-1/34.png)

*Hình 9: Cửa sổ Thay đổi Mật khẩu Chính*

**Bước 5**. **Hãy nhập** một mật khẩu đủ mạnh và chỉ có thể mình bạn ghi nhớ được, và **Nhấn** ![](/sbox/screen/thunderbird-vi-1/35.png) để xác nhận *Mật khẩu Chính*.

### Khung Nội dung Trang Web ###

Cookie là một tệp văn bản được các trình duyệt sử dụng trong quá trình xác thực hay xác định một trang web. Khung *Nội dung Trang Web* cho phép bạn xác định các trang nhật ký cá nhân (blog), nguồn tin tức (news feed) hay nhóm tin tức (newsgroup) nào là đáng tin và an toàn.

**Bước 1**. **Nhấn** ![](/sbox/screen/thunderbird-vi-1/36.png) để hiển thị *Nội dung Trang Web*:

![](/sbox/screen/thunderbird-vi-1/37.png)

*Hình 11: Khung Nội dung Trang Web*

**Bước 2**. **Chọn** mục *I close Thunderbird* trong tùy chọn *Lưu đến khi:* để xóa các cookies mỗi khi bạn tắt chương trình **Thunderbird** nhằm tăng cường bảo mật.

<a name="3.4"></a>
### 3.4 Hướng dẫn bật tính năng Lọc thư Rác ###

Dạng lọc thư rác thứ hai của **Thunderbird** nằm trong cửa sổ *Thiết lập tài khoản - Thiết đặt Thư rác*. Mặc định, các bộ lọc này bị tắt, vì vậy cần bật chúng lên nếu bạn muốn sử dụng. Mỗi khi nhận được thư rác, **Thunderbird** sẽ tự động đưa chúng vào thư mục *Junk* tương ứng của từng tài khoản thư khác nhau.

**Bước 1**. **Chọn Công cụ > Account Settings** để mở cửa sổ *Thiết lập Tài khoản*.

**Bước 2**. **Chọn** tùy chọn *Thiết lập Thư rác* tương ứng với tài khoản **Gmail**  hoặc **RiseUp** trên khung bên trái. 

**Bước 3**. **Bật** tùy chọn *Thiết đặt Thư rác* để hiển thị màn hình *Thiết đặt Tài khoản - Thiết đặt Thư rác* tương tự như dưới đây: 

![](/sbox/screen/thunderbird-vi-1/38.png)

*Hình 12: Cửa sổ Thiết lập Tài khoản - Thiết lập Thư rác*

**Bước 4**. **Nhấn** ![](/sbox/screen/thunderbird-vi-1/35.png) để hoàn thành việc thiết đặt trong cửa sổ *Thiết lập Tài khoản*.

**Lưu ý**: Các tùy chọn *Thiết đặt Thư rác* cần được thiết đặt riêng rẽ cho từng tài khoản thư. Khi đó, thư rác cho tài khoản **Gmail** hay **RiseUp** sẽ được đưa vào các thư mục *Xóa* tương ứng của từng tài khoản. Một cách khác,  bạn có thể tạo một thư mục *Local Folder* để chứa thư rác của tất cả các tài khoản. 

![](/sbox/screen/thunderbird-vi-1/39.png)

*Hình 13: Cửa sổ Thiết đặt Tài khoản - Thiết đặt Thư rác, với các thiết đặt để tạo một thư mục chung chứa thư rác*

**Bước 1**. **Chọn** tùy chọn *Thiết đặt Thư rác* bên dưới *Thư mục Nội bộ* ở cửa sổ bên trái.

**Bước 2**. **Chọn** mục *Thư mục nội bộ* *ở thư mục "Thư rác" trong:* danh sách xổ xuống như trong *Hình 13*.

**Bước 3**. **Nhấn** ![](/sbox/screen/thunderbird-vi-1/35.png) để hoàn thành thiết đặt trong cửa sổ *Thiết đặt Tài khoản*.

Bạn vừa thiết đặt thành công các tùy chọn an ninh và lọc thư rác trong **Thunderbird**, hãy tìm hiểu tiếp chương sau  [**Hướng dẫn Sử dụng Enigmail với GnuPG trong Thunderbird**](/vi/thunderbird_enigmail_GNUPG). 

