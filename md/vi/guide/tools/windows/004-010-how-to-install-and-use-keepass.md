

---

lang: vi
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: How to Install and Use KeePass

---

Các mục trong chương này:

- [**2.0 Hướng dẫn cài đặt KeePass**](#2.0)
- [**2.1 Hướng dẫn Tạo Một Cơ sở dữ liệu Mật khẩu mới**](#2.1)
- [**2.2 Hướng dẫn Tạo một Mục vào**](#2.2)
- [**2.3 Hướng dẫn Chỉnh sửa Mục vào**](#2.3)
- [**2.4 Hướng dẫn Tạo Mật khẩu Ngẫu nhiên**](#2.4)
- [**2.5 Hướng dẫn Thoát, Thu nhỏ, Hiển thị KeePass**](#2.5)
- [**2.6 Hướng dẫn Sao lưu tệp Cơ sở dữ liệu Mật khẩu**](#2.6)
- [**2.7 Hướng dẫn khởi tạo lại Mật khẩu chủ**](#2.7)

-------

<a name="2.0"></a>
## 2.0 Hướng dẫn cài đặt KeePass ##

**Bước  1**. **Nhấn đúp chuột** vào ![](/sbox/screen/keepass-vi-1/01.png); hộp thoại cảnh báo mở tệp *Open File - Security Warning* có thể xuất hiện. Nếu vậy, **Nhấn** ![](/sbox/screen/keepass-vi-1/02.png) để mở cửa sổ sau:

![](/sbox/screen/keepass-vi-1/03.png)

*Hình 1: Lựa chọn Ngôn ngữ Cài đặt*

**Bước 2**. **Nhấn** ![](/sbox/screen/keepass-vi-1/04.png) để kích hoạt cửa sổ Thuật sỹ Hướng dẫn  Cài đặt KeePass (*Setup - KeePass Password Safe – Welcome to the KeePass Password Safe Setup Wizard*).

**Bước  3**. **Nhấn** ![](/sbox/screen/keepass-vi-1/05.png) để mở cửa sổ thông tin bản quyền *License Agreement*. Hãy đọc kỹ thông tin bản quyền *License Agreement* trước khi tiến hành các bước cài đặt tiếp theo. 

**Bước  4**. **Nhấn chọn** ô *I accept the agreement* để hiện nút *Next*, sau đó  **Nhấn** ![](/sbox/screen/keepass-vi-1/05.png) để mở cửa sổ lựa chọn Thư mục Cài đặt *Select Destination Location*.

**Bước  5**. **Nhấn** ![](/sbox/screen/keepass-vi-1/05.png) to để chấp nhận đường dẫn thư mục cài đặt mặc định, cửa sổ Lựa chọn Thư mục trong Trình đơn Khởi động *Select Start Menu Folder* xuất hiện, hãy **Nhấn** ![](/sbox/screen/keepass-vi-1/05.png) để chấp nhận thư mục mặc định.

**Bước  6**. **Nhấn** ![](/sbox/screen/keepass-vi-1/05.png) để kích hoạt cửa sổ sau:

![](/sbox/screen/keepass-vi-1/06.png)

*Hình 2: Cửa sổ Lựa chọn Tác vụ Khác* 

**Bước 7**. **Chọn** hộp chọn ![](/sbox/screen/keepass-vi-1/07.png) như trong *Hình 2*. 

**Lưu ý**: Nếu bạn không chọn hộp chọn *Don't create a Start Menu folder*, *Thuật sỹ Cài đặt KeePass Password Safe* sẽ tự động tạo một biểu tượng khởi động nhanh của **KeePass** *Quick Launch* trên trình đơn *Start* của hệ thống. 

**Bước  8**. **Nhấn** ![](/sbox/screen/keepass-vi-1/05.png) để mở cửa sổ thông tin chung về thiết đặt cài đặt  (*Ready to Install*), sau đó **Nhấn** ![](/sbox/screen/keepass-vi-1/08.png) để mở cửa sổ  **Cài đặt** (**Installing**) và thanh trạng thái tiến trình cài đặt.

Sau vài giây, cửa sổ thông báo *Hoàn thành Thuật sỹ Hướng dẫn Cài đặt KeePass Password Safe* (*Completing the KeePass Password Safe Setup Wizard*) sẽ xuất hiện.

**Bước  9**. **Nhấn chọn** ô *Launch KeePass* và **Nhấn** ![](/sbox/screen/keepass-vi-1/09.png) để khởi động **KeePass**, bạn sẽ được dẫn vào trang web **KeePass** giới thiệu các *Thành phần Mở rộng* (*Plugins and Extensions*) nếu bạn đang kết nối vào Internet.

**Lưu ý:** Sau khi cài đặt xong, để sử dụng giao diện Tiếng Việt hãy thực hiện các bước sau:

**Bước 1.** Tải về tệp ngôn ngữ **Vietnamese.lng** tại

**Bước 2.** Khởi động chương trình KeePass (Xem Bước 1 Phần 2.1) và chọn **View &gt; Change Language** như trong hình sau:

![](/sbox/screen/keepass-vi-1/2a.png)

*Hình 2a: Chuyển đổi Giao diện chương trình KeePass sang Tiếng Việt*

Cửa sổ liệt kê các ngôn ngữ đã cài đặt sẽ xuất hiện:

![](/sbox/screen/keepass-vi-1/2b.png)

*Hình 2b: Lựa chọn giao diện Tiếng Việt*

**Bước 3.** Chọn dòng *Vietnamse* sau đó **khởi động lại** chương trình **KeePass**.


<a name="2.1"></a>
## 2.1 Hướng dẫn tạo một Cơ sở dữ liệu mật khẩu mới ##

Trong các phần tiếp theo, bạn sẽ học cách tạo một mật khẩu chủ, lưu tệp cơ sở dữ liệu mới tạo,  tạo một mật khẩu ngẫu nhiên cho một chương trình, sao lưu cơ sở dữ liệu **KeePass** và sử dụng mật khẩu lưu trong **KeePass** mỗi khi cần.

Để khởi động **KeePass**, thực hiện những bước sau:  

**Bước 1**. **Chọn: Start &gt; Programs &gt; KeePass Password Safe &gt; KeePass** hoặc **nhấn** biểu tượng  ![](/sbox/screen/keepass-vi-1/36.png) trên màn hình để mở giao diện chính của chương trình **KeePass** như dưới đây:

![](/sbox/screen/keepass-vi-1/10.png)

*Hình 3: Giao diện chương trình KeePass Password Safe*

Để tạo một cơ sở dữ liệu mật khẩu mới cần thực hiện hai bước:

Bạn cần nghĩ ra một mật khẩu chủ riêng đủ mạnh dùng để khóa và mở cơ sở dữ liệu mật khẩu. Sau đó lưu cơ sở dữ liệu mật khẩu vừa tạo vào đâu đó.

Để tạo một cơ sở dữ liệu mật khẩu, tiến hành các bước sau:

**Bước 1**. **Chọn: Tệp tin &gt; Tạo mới..**:

![](/sbox/screen/keepass-vi-1/11.png)

*Hình 4: Cửa sổ KeePass khi chọn Tệp tin &gt;Tạo mới* 

*Cửa sổ **Tạo Cơ sở dữ liệu mới** sẽ hiện ra như sau:*

![](/sbox/screen/keepass-vi-1/12.png)  

*Hình 5: Cửa sổ Tạo một cơ sở dữ liệu mật khẩu*

**Bước 2**. **Nhập** mật khẩu chủ bạn muốn sử dụng vào trường **Mật khẩu**.

![](/sbox/screen/keepass-vi-1/13.png)

*Hình 6: Màn hình thiết đặt mật khẩu chủ*

Bạn để ý thanh trạng thái màu xanh-cam ngay bên dưới ô nhập mật khẩu chủ. Khi bạn nhập vào mật khẩu chủ, màu xanh sẽ tăng lên thể hiện độ phức tạp hay độ mạnh của mật khẩu dựa vào số lượng số và ký tự trong mật khẩu. 

**Gợi ý**: Bạn nên cố gắng tạo những mật khẩu có tối thiểu một nửa thanh trạng thái là mầu xanh. 

**Bước 3**. **Nhấn** ![](/sbox/screen/keepass-vi-1/14.png) để mở cửa sổ *Nhập lại Mật khẩu* và  xác nhận mật khẩu như sau:

![](/sbox/screen/keepass-vi-1/15.png)

*Hình 7: Cửa sổ Nhập lại Mật khẩu KeePass*

**Bước 4**. **Nhập lại** mật khẩu một lần nữa vào ổ * Nhập lại mật khẩu* và **nhấn** ![](/sbox/screen/keepass-vi-1/14.png).

**Bước 5**. **Nhấn**: ![](/sbox/screen/keepass-vi-1/16.png) để chắc chắn mật khẩu nhập lại là chính xác.

**Cảnh báo**: Việc hiển thị mật khẩu là không nên nếu bạn lo ngại có ai đó có thể quan sát từ phía sau. 

*Sau khi đã hoàn tất việc nhập và xác nhận mật khẩu chủ, giao diện chương trình KeePass sẽ được kích hoạt như sau:*

![](/sbox/screen/keepass-vi-1/17.png)  

*Hình 8: Cấu hình Cơ sở dữ liệu KeePass*

Sau khi đã tạo cơ sở dữ liệu mật khẩu, bạn cần lưu nó vào đâu đó. Để lưu cơ sở dữ liệu mật khẩu, thực hiện các bước sau:

**Bước 1**. **Chọn: Tệp tin &gt; Lưu thành**

![](/sbox/screen/keepass-vi-1/18.png)  

*Hình 9: Giao diện chương trình KeePass Password Safe*

*Cửa sổ Lưu Cơ sở dữ liệu sẽ hiện ra như sau*:

![](/sbox/screen/keepass-vi-1/19.png)

*Hình 10: Màn hình Lưu Cơ sở dữ liệu*


**Bước 2**. **Nhập** tên cho tệp cơ sở dữ liệu mật khẩu mới.


**Bước 3**. **Nhấn**: ![](/sbox/screen/keepass-vi-1/20.png) để lưu tệp cơ sở dữ liệu.


**Gợi ý**: Hãy ghi nhớ nơi bạn lưu tệp cơ sở dữ liệu mật khẩu cũng như tên của tệp! Điều này sẽ giúp việc sao lưu tệp dễ dàng hơn. 

**Xin chúc mừng!** Bạn đã hoàn thành việc tạo và lưu một cơ sở dữ liệu mật khẩu bảo mật. Bây giờ bạn có thể bắt đầu sử dụng nó để quản lý tất cả mật khẩu hiện có cũng như trong tương lai.


<a name="2.2"></a>
## 2.2. Hướng dẫn Thêm Mục ##

Tính năng *Thêm Mục* cho phép bạn nhập thông tin tài khoản, mật khẩu và các thông tin quan trọng khác vào cơ sở dữ liệu vừa tạo ra. Ở ví dụ bên dưới, bạn sẽ tạo ra các mục quản lý mật khẩu và tên người dùng cho các tài khoản trang web hay thư điện tử .

**Bước 1**. **Chọn: Hiệu chỉnh &gt; Thêm Mục** tại cửa sổ **KeePass Password Safe** để mở hộp thoại **Thêm Mục** như sau::


![](/sbox/screen/keepass-vi-1/21.png)

*Hình 11: Giao diện KeePass Password Safe khi chọn Hiệu chỉnh &gt; Thêm Mục*  

![](/sbox/screen/keepass-vi-1/22.png)

*Hình 12: Cửa sổ Thêm Mục*

**Chú ý**: Cửa sổ *Thêm Mục *gồm nhiều trường nhập thông tin. Không có trường nào là bắt buộc; những thông tin nhập ở đây nhằm tạo sự thuận lợi cho bạn. Nó sẽ giúp ích khi bạn tìm một mục thông tin cụ thể.

Sau đây là giải thích tóm tắt những trường thông tin:

- **Nhóm**: KeePass cho phép bạn quản l‎ý mật khẩu theo các nhóm được tạo trước. Ví dụ: *Internet* là nơi thích hợp để lưu các mật khẩu cho các tài khoản trang web.

- **Tiêu đề**: Một tên miêu tả một mục lưu mật khẩu: Ví dụ: mật khẩu Gmail

- **Tài khoản**: tên người dùng tương ứng với mật khẩu lưu trong mục này. Ví dụ: securitybox@gmail.com

- **Địa chỉ URL**: Địa chỉ Internet tương ứng với mật khẩu lưu trong mục này. Ví dụ : https://mail.google.com

- **Mật khẩu**: Tính năng này tự động tạo một mật khẩu ngẫu nhiên khi cửa sổ *Thêm Mục* được kích hoạt. Nếu bạn tạo mới một tài khoản thư điện tử, bạn có thể sử dụng mật khẩu ‘tạo sẵn’ trong trường này. Bạn cũng có thể sử dụng tính năng này để tạo mật khẩu mới thay thế một mật khẩu hiện có của bạn. KeePass sẽ luôn ghi nhớ mật khẩu này cho bạn nên bạn thậm chí không cần phải xem mật khẩu này như thế nào. Một mật khẩu được tạo ra ngẫu nhiên bởi KeePass rất mạnh (rất khó đoán hay phá bởi kẻ lạ).

Cách yêu cầu chương trình tạo ra một mật khẩu ngẫu nhiên sẽ được hướng dẫn ở phần tiếp theo. Bạn có thể thay thế mật khẩu ‘tạo sẵn’ bằng mật khẩu của riêng bạn. Ví dụ bạn tạo một mục lưu thông tin tài khoản hiện có, thì bạn sẽ nhập mật khẩu tương ương của tài khoản đó vào mục này.

- **Xác nhận lại**: Xác nhận mật khẩu.

- **Chất lượng**: Thanh trạng thái thể hiện độ phức tạp của mật khẩu dựa trên độ dài và tính ngẫu nhiên. Màu xanh trên thanh trạng thái này càng nhiều, độ phức tạp của mật khẩu tương ứng càng cao.

- **Ghi chú**: Đây là nơi bạn nhập các thông tin mô tả chung về tài khoản hoặc trang web liên quan tới mục quản lý thông tin này. Ví dụ: ‘Mail server settings: POP3 SSL, pop.gmail.com, Port 995; SMTP TLS, smtp.gmail.com, Port: 465’

**Lưu ý**: Việc tạo và thay đổi một mục quản l‎ý mật khẩu trong KeePass sẽ không làm thay đổi mật khẩu thực tế của bạn! Hãy coi **KeePass** như là một sổ liên lạc điện tử bảo mật để lưu mật khẩu. Nó không làm gi hơn việc chỉ lưu trữ những thông tin bạn ghi vào.

Nếu bạn chọn  *Internet* từ danh sách *Nhóm*, mục quản lý mật khẩu có thể giống dưới đây:


![](/sbox/screen/keepass-vi-1/24.png)


*Hình 13: Cửa sổ Thêm Mục của KeePass –  hoàn thành*


**Bước 2**. **Nhấn**: ![](/sbox/screen/keepass-vi-1/14.png) để lưu mục này.


*Mục thông tin này xuất hiện trong nhóm *Internet*.

![](/sbox/screen/keepass-vi-1/25.png)

*Hình 14: Cửa sổ KeePass Password Safe*  


**Lưu ý**: Khung bên dưới cửa sổ này hiển thị thông tin về một mục được chọn. Bao gồm thời điểm tạo, thay đổi và hết hạn cũng như những ghi chú của bạn. Nó không hiển thị mật mật khẩu.

- **Hiệu lực**: Chọn ô chọn này để kích hoạt trường ngày tháng hết hạn. Với lựa chọn này bạn có thể tạo một lịch thông báo thay đổi mật khẩu sau một khoảng thời gian nhất định (ví dụ: sau 3 tháng). Khi một mật khẩu bị hết hạn, nó sẽ xuất hiện trên màn hình với dấu gạch chéo đỏ bên cạnh tên của mục quản lý mật khẩu như hình dưới đây :

![](/sbox/screen/keepass-vi-1/23.png)

*Hình 15: Cửa sổ hiển thị tệp Cơ sở dữ liệu mới.kdb của KeePass Password Safe*

<a name="2.3"></a>
## 2.3 Hướng dẫn Hiệu chỉnh Mục ##


Bất kỳ lúc nào bạn cũng có thể thay đổi một mục thông tin trong **KeePass**. Bạn có thể thay đổi mật khẩu (Một thói quen bảo mật tốt là thay đổi mật khẩu định kỳ ba hay sáu tháng), hoặc chỉnh sửa những thông tin lưu trong mục quản l‎ý thông tin. 

Để chỉnh sửa một mục thông tin, thực hiện các bước sau:


**Bước 1**. **Chọn** *Nhóm* thích hợp ở phía bên tay trái để hiển thị các mục thông tin tương ứng.


**Bước 2**. **Chọn** Chọn mục thông tin cần chỉnh sửa, **nhấn chuột phải** vào mục đó như sau: 


![](/sbox/screen/keepass-vi-1/26.png)

*Hình 16: Cửa sổ KeePass Password Safe với trình đơn Hiệu chỉnh*

**Bước 3.** **Nhấn**: ![](/sbox/screen/keepass-vi-1/14.png) để lưu những thay đổi.


Để thay đổi một mật khẩu hiện tại (do bạn tạo trước đó) bằng một mật khẩu được tạo ra bởi chương trình KeePass, hãy xem phần tiếp theo.

<a name="2.4"></a>
## 2.4 Hướng dẫn Tạo Mật khẩu Ngẫu nhiên ##

Những mật khẩu dài, có tính ngẫu nhiên được coi là có tính bảo mật cao. Tính ngẫu nhiên được tạo ra dựa trên những thuật toán và không dễ dàng bị ‘đoán’ bởi những kẻ muốn tấn công tài khoản của bạn. **KeePass** cung cấp tính năng *Password Generator* để thực hiện công việc này. Như bạn thấy ở hình bên dưới, một mật khẩu ngẫu nhiên được tự động sinh ra mỗi khi bạn tạo một mục thông tin mới. Phần này sẽ hướng dẫn bạn cách tự tạo một mật khẩu.


**Lưu ý**: Cửa sổ **Tạo Mật khẩu** có thể được kích hoạt trong các màn hình *Thêm Mục* và *Soạn thảo/Xem mục* hoặc **Công cụ\Tạo Mật khẩu**.


**Bước 1**. **Nhấn**: ![](/sbox/screen/keepass-vi-1/27.png)  trong cửa sổ *Thêm Mục* hoặc *Hiệu chỉnh/Kiểm tra Mục*, để kích hoạt cửa sổ *Tạo Mật khẩu* như sau:

![](/sbox/screen/keepass-vi-1/28.png)

*Hình 17: Màn hình Tạo Mật khẩu trong KeePass*

Màn hình *Tạo Mật khẩu* cung cấp một số chọn lựa tạo mật khẩu. Bạn có thể xác định độ dài, tập hợp ký tự sử dụng để tạo mật khẩu và nhiều lựa chọn khác. Ở ví dụ này, chúng ta sử dụng lựa chọn mặc định của chương trình. Với độ dài mật khẩu là 20 ký tự và bao gồm cả ký tự thường lẫn chữ hoa và số.

**Bước 2**. **Nhấn**: ![](/sbox/screen/keepass-vi-1/29.png)  để thực hiện. Sau khi hoàn thành, **KeePass** sẽ hiển thị mật khẩu vừa tạo ra.

![](/sbox/screen/keepass-vi-1/30.png)

*Hình 18: Khung Tạo Mật khẩu KeePass*

**Lưu ý**: Bạn có thể xem mật khẩu vừa tạo ra bằng cách **nhấn vào**: ![](/sbox/screen/keepass-vi-1/16.png)

Tuy nhiên việc này có thể không bảo mật như đã thảo luận ở trên. Trong thực tế, bạn không cần thiết phải xem mật khẩu vừa tạo ra. Chung tôi sẽ giải thích chi tiết ở mục [**3.0 Sử dụng Mật khẩu KeePass**](/vi/keepass_quanlymatkhau).


**Bước 3**. **Nhấn**: ![](/sbox/screen/keepass-vi-1/31.png) để chấp nhận mật khẩu vừa tạo và quay trở về cửa sổ *Thêm Mục* như bên dưới:

![](/sbox/screen/keepass-vi-1/24.png)

*Hình 19: Cửa sổ Thêm Mục của KeePass*


**Bước 4**. **Nhấn**:  ![](/sbox/screen/keepass-vi-1/14.png) để lưu mục thông tin này.

**Bước 5**. **Chọn: Tệp tin &gt; Lưu** to để lưu cập nhật cơ sở dữ liệu mật khẩu.

<a name="2.5"></a>
## 2.5 Hướng dẫn Thoát, Thu nhỏ, Hiển thị KeePass ##


Bạn có thể thu nhỏ hoặc thoát khỏi chương trình **KeePass** bất kỳ lúc nào. Khi bạn mở hoặc hiển thị lại chương trình, nó sẽ yêu cầu bạn nhập *Mật khẩu chủ*. 


**KeePass** sẽ tự thu nhỏ, nằm trên khay hệ thống (phía góc phải bên dưới màn hình) với biểu tượng: ![](/sbox/screen/keepass-vi-1/39.png).

**KeePass** cũng cho phép bạn khóa truy cập chương trình bằng cách thực hiện các bước sau:

**Bước  1**. **Chọn Tệp > Khóa Chương trình** để mở cửa sổ:

![](/sbox/screen/keepass-vi-1/40.png)

*Hình 20: KeePass - khung xác nhận An toàn Trước khi Đóng/Khóa*


**Bước  2**. **Nhấn** ![](/sbox/screen/keepass-vi-1/41.png) để lưu thông tin và đóng giao diện  **KeePass** như trong *Hình 2*, biểu tượng chương trình sẽ xuất hiện trong *Khay Hệ thống* như sau:
![](/sbox/screen/keepass-vi-1/42.png)

**Bước 1**. **Nhấn đúp chuột ** vào biểu tượng này để hiển thị cửa sổ KeePass ở kích thước thực, cửa sổ sau xuất hiện:

![](/sbox/screen/keepass-vi-1/33.png)

*Hình 21: Nhập Mật khẩu Chủ để mở Cơ sở Dữ liệu KeePass – NetSecureDb.kdb*

**Bước  2**. **Nhập** your *Mật khẩu Chủ* để mở **KeePass**

Để đóng chương trình **KeePass** hãy thực hiện bước sau :

**Bước 1**. **Chọn: Tệp tin &gt; Thoát** để thoát khỏi chương trình. 

Nếu bạn có những thay đổi chưa được lưu vào cơ sở dữ liệu, **KeePass** sẽ yêu cầu bạn lưu vào.

<a name="2.6"></a>
## 2.6 Hướng dẫn Sao lưu tệp Cơ sở dữ liệu mật khẩu ##

Tệp cơ sở dữ liệu của **KeePass** nằm trên máy tính của bạn có đuôi mở rộng là .kdb. Bạn có thể sao tệp này vào thẻ nhớ USB. Không ai có thể mở được tệp này nếu không có mật khẩu chủ.

**Bước 1**. **Chọn: Tệp tin &gt; Lưu mot ban khac** từ cửa sổ chính của chương trình, và lưu một bản sao của cơ sở dữ liệu vào một địa điểm khác.


Bạn có thể chạy chương trình **KeePass** từ một thẻ nhớ USB. Hãy xem hướng dẫn [KeePass chạy không cần cài đặt](https://securityinabox.org/vi/keepass-botui) .


<a name="2.7"></a>
## 2.7 Hướng dẫn khởi tạo lại Mật khẩu chủ ##

Bạn có thể thay đổi *Mật khẩu Chủ* bất kỳ lúc nào bạn muốn. Việc này có thể được thực hiện sau khi bạn mở cơ sở dữ liệu mật khẩu.

**Bước 1**. **Chọn: Tệp tin &gt; Đổi Mã khóa chính**

![](/sbox/screen/keepass-vi-1/34.png)

*Hình 22: Thay đổi Mật khẩu Chủ*

Bạn sẽ được yêu cầu nhập *Mật khẩu Chủ* hai lần.

![](/sbox/screen/keepass-vi-1/35.png)

*Hình 23: Cửa sổ thay đổi Mật khẩu Chủ trong KeePass*

