

---

lang: vi
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: How to Use Enigmail with GnuPG in Thunderbird

---

Các mục trong trang này

- [**4.0 Giới thiệu Tổng quát về Enigmail, GnuPG và Mã hóa với Khóa Riêng-Công khai**](#4.0)
- [**4.1 Hướng dẫn Cài đặt Enigmail và GnuPG**](#4.1)
- [**4.2 Hướng dẫn Tạo Cặp Khóa và Cấu hình Enigmail cho các Tài khoản Thư Của bạn**](#4.2)
- [**4.3 Hướng dẫn Trao đổi Khóa Công khai**](#4.3)
- [**4.4 Hướng dẫn Cập nhật và Ký một Cặp Khóa**](#4.4)
- [**4.5 Hướng dẫn Mã hóa và Giải Mã hóa một Tin nhắn**](#4.5)

-------

<a name="4.0"></a>
## 4.0 Giới thiệu Tổng quát về Enigmail, GnuPG và Mã hóa với Khóa Riêng-Công khai ##

**Enigmail** là một thành phần mở rộng của **Mozilla Thunderbird** cho phép bạn bảo mật truyền thông thư điện tử. **Enigmail** đơn giản chỉ là một giao diện giúp bạn sử dụng chương trình mã hóa **GnuPG** trong **Thunderbird**.  Giao diện **Engimail** được hiển thị là *OpenPGP* trên thanh trình đơn điều khiển **Thunderbird**. 

**Engimail** hoạt động dựa trên [**public-key cryptography**](http://en.wikipedia.org/wiki/Public-key_cryptography). (Mã hóa với mã công khai)
Trong phương pháp này, mỗi cá nhân tham gia quá trình liên lạc cần tạo một cặp khóa riêng cho bản thân mình. Khóa đầu tiên gọi là *khóa riêng* (private key). Nó được bảo vệ bởi một mật khẩu và cần được bảo vệ bí mật đồng thời *không bao giờ* để lộ khóa này cho *bất kỳ ai*.

Khóa thứ hai trong cặp khóa là *khóa công khai* (public key). Bạn có thể chia sẻ khóa này với bất kỳ ai muốn liên lạc. Khi bạn có *khóa công khai* của một ai đó, bạn có thể tiến hành gửi tin nhắn được mã hóa cho người đó. Chỉ bản thân người này có thể giải mã và đọc được thư mã hóa do bạn gửi , bởi vì chỉ có mình họ có thể sử dụng *khóa riêng* tương ứng.

Tương tự như vậy, nếu bạn gửi *khóa công khai* của mình cho những người cần liên lạc và giữ bí mật *khóa riêng* của mình, chỉ mình bạn có thể đọc các thư được mã hóa bởi các đối tác liên lạc này.

**Enigmail** cũng cho phép bạn *ký số* lên các tin nhắn của mình. Những người nhận tin nhắn đã có khóa công khai chính xác của bạn có thể xác nhận rằng thư điện tử được gửi từ bạn, và nội dụng của thư này không bị thay đổi trong quá trình truyền tin. Một cách tương tự, nếu bạn có khóa công khai của một đối tác liên lạc, bạn có thể xác minh chữ ký số trên tin nhắn của người này.

<a name="4.1"></a>
## 4.1 Hướng dẫn Cài đặt Enigmail và GnuPG ##

Hãy xem phần [**Tải về**](http://securityinabox.org/vi/thunderbird-main) để xem hướng dẫn tải về **Enigmail** và **GnuPG**.

### 4.1.1 Hướng dẫn Cài đặt GnuPG ###

Việc cài đặt **GnuPG** khá dễ dàng, và tương tự như cách cài đặt các phần mềm khác.

Để bắt đầu cài đặt **GnuPG** hãy thực hiện các bước sau:

**Bước 1**. **Nhấn đúp chuột vào** ![](/sbox/screen/thunderbird-vi-1/40.png) để khởi động tiến trình cài đặt. Hộp thoại *Mở Tệp - Cảnh báo An ninh* (Open File - Security Warning) có thể xuất hiện. Nếu vậy, **Nhấn** ![](/sbox/screen/thunderbird-vi-1/02.png) để mở cửa sổ sau để mở cửa sổ sau:

![](/sbox/screen/thunderbird-vi-1/41.png)

*Hình 1: Thuật sỹ Cài đặt GNU Privacy Guard*

**Bước 2**. **Nhấn** ![](/sbox/screen/thunderbird-vi-1/04a.png) để mở cửa sổ thông tin bản quyền *GNU Privacy Guard Setup - License Agreement*; sau khi đọc kỹ thông tin , **Nhấn** ![](/sbox/screen/thunderbird-vi-1/04.png) để mở cửa sổ chọn các thành phần cài đặt *GNU Privacy Guard Setup - Choose Components* .

**Bước 3**. **Nhấn** ![](/sbox/screen/thunderbird-vi-1/04a.png) để chấp nhận các thiết đặt mặc định và mở cửa sổ *Các Tùy Chọn cài đặt - Lựa chọn Ngôn ngữ* (GNU Privacy Guard Setup - Install Options - GnuPG Language Chọnion). 

**Bước 4**. **Nhấn** ![](/sbox/screen/thunderbird-vi-1/04a.png) để chọn ngôn ngữ Tiếng Anh *en-English* là ngôn ngữ mặc định, cửa sổ *Chọn Thư mục Cài đặt* (Choose Install Location) sẽ xuất hiện.

**Bước 5**. **Nhấn** ![](/sbox/screen/thunderbird-vi-1/06a.png) để xác nhận đường dẫn cài đặt mặc định và kích hoạt màn hình  *Chọn Thư mục Trình đơn Khởi động* (Choose Start Menu Folder*).

**Bước 6**. **Nhấn** ![](/sbox/screen/thunderbird-vi-1/06a.png) để giải nén và cài đặt các gói **GnuPG**. Khi tiến trình này hoàn thành, cửa sổ *Hoàn thành Cài đặt* (Installation Complete)  sẽ xuất hiện.

**Bước 7**. **Nhấn** ![](/sbox/screen/thunderbird-vi-1/04a.png) sau đó nhấn ![](/sbox/screen/thunderbird-vi-1/08a.png) để hoàn thành việc cài đặt chương trình **GnuPG**.

### 4.1.2 Hướng dẫn Cài đặt Thành phần Mở rộng Enigmail  ###

Sau khi cài đặt thành công chương trình **GnuPG**, bạn đã sẵn sàng cài đặt thành phần mở rộng **Enigmail**. 

Để bắt đầu cài đặt **Enigmail**, hãy theo các bước sau: 

**Bước 1**. **Mở Thunderbird**, và **Nhấn** ![](/sbox/screen/thunderbird-vi-1/24a.png) **Chọn Công cụ > Tiện ích** để kích hoạt cửa sổ *Quản lý Tiện ích*; cửa sổ *Quản lý Tiện ích* sẽ xuất hiện với khung *Phần mở rộng* được mở.

**Bước 2**. **Nhấn** ![](/sbox/screen/thunderbird-vi-1/44.png) ở khung bên trái, nếu Tiện ích Enigmail chưa được cài đặt, bạn sẽ thấy một thông báo: *bạn không có tiện ích nào thuộc kiểu này được cài đặt* 

**Bước 3**. Nếu Tiện ích Enigmail xuất hiện trong cửa sổ chính Tiện ích, **Nhấn** ![](/sbox/screen/thunderbird-vi-1/46.png), nếu không thì hãy **Nhấn** ![](/sbox/screen/thunderbird-vi-1/45a.png) và **chọn** *cài đặt Tiện ích từ tập tin* như sau:

![](/sbox/screen/thunderbird-vi-1/46a.png)

*Hình 3: Chọn một Thành phần mở rộng để cài đặt*

**Bước 4**. Tìm đến thư mục bạn lưu **Enigmail** như trong cửa sổ sau:

![](/sbox/screen/thunderbird-vi-1/49.png)

*Hình 4: Chọn Tiện ích Cài đặt*

**Bước 5**. **Nhấn** ![](/sbox/screen/thunderbird-vi-1/50.png), sau đó **Nhấn** ![](/sbox/screen/thunderbird-vi-1/51.png) để hoàn thành việc cài đặt thành phần mở rộng **Enigmail**. 

Để kiểm trai việc cài đặt **Enigmail** thành công, hãy quay về cửa sổ giao diện chính **Thunderbird**, **nhấn vào** ![](/sbox/screen/thunderbird-vi-1/24a.png) để xem *Enigmail* có xuất hiện trên trình đơn không, như sau đây: 

![](/sbox/screen/thunderbird-vi-1/52.png)

*Hình 6: Trình đơn hệ thống Thunderbird với Enigmail*

### 4.1.3 Hướng dẫn Khẳng định Enigmail và GnuPG đang Hoạt động ###

Trước khi sử dụng **Enigmail** và **GnuPG** để xác thực và mã hóa các thư điện tử, bạn cần chắc chắn rằng chúng đang hoạt động với nhau.

**Bước 1**. **Chọn OpenPGP > Preferences** để mở màn hình *OpenPGP Preferences* như sau: 

![](/sbox/screen/thunderbird-vi-1/53.png)

*Hình 7: Màn hình Tùy thích của Enigmail*

Nếu **GnuPG** đã được cài đặt thành công, ![](/sbox/screen/thunderbird-vi-1/54.png) sẽ xuất hiện trong mục *Files and Directories*; trái lại, bạn sẽ nhận được một thông báo như sau:

![](/sbox/screen/thunderbird-vi-1/55.png)

*Hình 8: Thông báo lổi không thấy OpenPGP*

**Gợi ý**: Nếu bạn nhận được thông báo lỗi trên, có thể do bạn cài đặt tệp vào nhầm đường dẫn thư mục. **Chọn** ô *Override with* để hiện nút *Browse...*, và **Nhấn** ![](/sbox/screen/thunderbird-vi-1/69.png) để mở *Locate GnuPG program* và tự tìm đến tệp *gpg.exe* trên máy tính.

**Bước 2**. **Nhấn** ![](/sbox/screen/thunderbird-vi-1/35.png) để quay lại màn hình  **Thunderbird**.

<a name="4.2"></a>
## 4.2 Hướng dẫn Tạo Cặp khóa và Thiết đặt Enigmail Làm việc với Các Tài khoản Thư của Bạn ##

Sau khi chắc chắn **Enigmail** và **GnuPG** đã làm việc đúng đắn, bạn cần thiết đặt một hoặc nhiều tài khoản thư sử dụng **Enigmail** để tạo một hay nhiều cặp khóa mã hóa.

### 4.2.1 Hướng dẫn Trợ lý Thiết lập để Tạo một Cặp Khóa Mã hóa ###

**Engimail** cung cấp hai cách sinh cặp khóa mã hóa riêng-công khai; cách đầu sử dụng  *Trợ lý Thiết lập* và cách thứ hai thông qua màn hình *Quản lý Khóa* (Key Management). 

Để tạo một cặp khóa mã hóa cho lần đầu với  *Trợ lý Thiết lập*, hãy theo các bước sau:

**Bước 1**. Nếu cửa sổ **Trợ lý Thiết lập** chưa được kích hoạt, **chọn Enigmail > Trợ lý Thiết lập** để mở cửa sổ *Trợ lý Thiết lập cho Enigmail* như sau: 

![](/sbox/screen/thunderbird-vi-1/56.png)

*Hình 9: Cửa sổ Chào mừng - Welcome to the OpenPGP Setup Wizard*

**Bước 2**. **Nhấn** ![](/sbox/screen/thunderbird-vi-1/04c.png) để mở cửa sổ sau:

![](/sbox/screen/thunderbird-vi-1/61.png)

*Hình 10: Mã hóa – Màn hình Mã hóa Các Thư Gửi đi*

**Bước 3**. **Nhấn** ![](/sbox/screen/thunderbird-vi-1/04c.png) để mở cửa sổ sau:

![](/sbox/screen/thunderbird-vi-1/60.png)

*Hình 12: Cửa sổ Mã hóa - Mã hóa Các Thư Gửi đi*

**Bước 4**. **Nhấn** ![](/sbox/screen/thunderbird-vi-1/04.png) để mở cửa sổ sau:

![](/sbox/screen/thunderbird-vi-1/61.png)

*Hình 12: Màn hình Ký Số Các Thư gửi đi*

**Bước 5**. **Nhấn** ![](/sbox/screen/thunderbird-vi-1/04c.png) để mở cửa sổ sau:

![](/sbox/screen/thunderbird-vi-1/62.png)

*Hình 13: Cửa sổ Preferences - Thay đổi Thiết đặt Thư để Enigmail Hoạt động Hiệu quả Hơn*

**Bước 6**. **Nhấn** ![](/sbox/screen/thunderbird-vi-1/04c.png) để mở cửa sổ *Taoj Khóa – Tạo một cặp khóa cho việc Ký tên và Mã hóa Thư điện tử*

**Lưu ý**: Trong lần đầu bạn thực hiện việc tạo cặp khóa cho một tài khoản, cửa sổ No Open PGP Key Found sẽ xuất hiện.

**Bước 7**. **Chọn** *Tôi muốn tạo mới một cặp khóa để ký tên và mã hóa thư điện tử của tôi* 
**Bước 8**. **Nhập** đoạn mật khẩu mạnh vào cả hai ô nhập *Mật khẩu* (*Password*)

![](/sbox/screen/thunderbird-vi-1/65.png)

*Hình 15: Tạo Khóa Mã hóa - Tạo một Khóa Mã hóa để Ký số và Mã hóa Thư điện tử*

**Bước 9**. **Nhấn** ![](/sbox/screen/thunderbird-vi-1/04c.png) mở cửa sổ *Tóm tắt*, trình bày các thiết đặt được sử dụng cho việc tạo cặp khóa.

**Bước 10**. **Nhấn** ![](/sbox/screen/thunderbird-vi-1/04c.png) để bắt đầu việc sinh cặp khóa như trong hình sau:

![](/sbox/screen/thunderbird-vi-1/67.png)

*Hình 16: Tài khoản/ Mã Người dùng Vừa được tạo*

**Lưu ý**: Bất kỳ cặp khóa mã hóa nào được tạo ra bởi *Trợ lý Thiết lập Enigmail* sẽ mặc định sử dụng chuẩn 4096-bit, và có thời gian hết hạn là 5 năm. 

**Bước 11** Sau khi cặp khóa được sinh ra, bạn sẽ được hướng dẫn để tạo chứng chỉ thu hồi. **Nhấn vào** ![](/sbox/screen/thunderbird-vi-1/76.png) như trong hình dưới đây:

![](/sbox/screen/thunderbird-vi-1/8.png)

*Hình 17: Cửa sổ xác nhận Enigmail*

**Lưu ý:** Nếu bạn biết rằng một đối tượng thù địch hay phá hoại đã chiếm được quyền kiểm soát bất hợp pháp đối với khóa của bạn và bạn mất quyền truy cập những khóa này, bạn có thể gửi chứng nhận thu hồi khóa tới các đối tác liên lạc của mình để thông báo cho họ biết rằng họ không nên sử dụng khóa công khai của bạn nữa. Hãy luôn ghi nhớ rằng bạn có thể cần thực hiện điều này trong trường hợp máy tính của bạn bị mất, mất cắp hoặc bị tịch thu. Chúng tôi cũng hết sức khuyến nghị nên sao lưu và bảo vệ khóa thu hồi này.

**Bước 12** Bạn sẽ được yêu cầu **nhập vào** mật khẩu tương ứng với cặp khóa vừa tạo ra. Sau đó chuyển tới thư mục để cất giữ chứng nhận thu hồi một cách an toàn và **Nhấn vào** ![](/sbox/screen/thunderbird-vi-1/76.png) như trong hình dưới đây:

![](/sbox/screen/thunderbird-vi-1/70.png)

*Hình 18: Tạo và Lưu Chứng nhận Thu hồi*

**Bước 13. Nhấn** ![](/sbox/screen/thunderbird-vi-1/04c.png) để hoàn thành cả hai tác vụ tạo cặp khóa và chứng nhận thu hồi.

### 4.2.2 Hướng dẫn Tạo Thêm Cặp Khóa (Additional Key Pairs) và Chứng chỉ Thu hồi (Revocation Certificates) cho một Tài khoản Thư khác ###

Việc tạo một cặp khóa mã hóa riêng biệt cho mỗi tài khoản thư là thường gặp. Sử dụng chung cặp khóa cho nhiều tài khoản thư điện tử là có thể, tuy nhiên điều này dễ gây nhầm lẫn cho các đối tách sử dụng.  Có thể thêm một hoặc nhiều hơn các tài khoản thư vào một cặp khóa (Chúng tôi sẽ không thảo luận chi tiết trong chương này) và có thể mang lại một số tiện ích khi sử dụng nhưng cũng đồng thời liên kết tất cả các tài khoản thư tới một cá nhân và đây có thể là điều không mong muốn. 

Hãy theo các bước sau nếu bạn muốn tạo thêm một cặp khóa cho các tài khoản thư khác:

**Bước 1**. **Chọn Enigmail > Quản lý Khóa** để mở cửa sổ sau:

![](/sbox/screen/thunderbird-vi-1/71.png)

*Hình 19: Trình đơn Enigmail Quản lý Khóa với mục Tạo khóa được chọn*

**Lưu ý**: **Chọn** ô *Hiển thị tất cả khóa theo mặc định* để xem các cặp khóa mã hóa được tạo bởi  *Trợ lý thiết lập Enigmail* cho tài khoản thư đầu tiên, như trong *Hình 19* phía trên và hình bên dưới đây.

**Bước 2**. **Chọn Tạo ra > Cặp khóa mới** trong *Quản lý khóa* như trong *Hình 19* phía trên để mở cửa sổ sau: 

![](/sbox/screen/thunderbird-vi-1/72.png)

*Hình 20: Cửa sổ Tạo Khóa mã hóa Open PGP*

**Bước 3**. **Chọn** một tài khoản thư điện tử trong danh sách xổ xuống *Tài khoản /Tên người dùng*, **chọn** ô *Sử dụng khóa được tạo ra cho danh tính được chọn*. và tạo một đoạn mật khẩu bảo vệ khóa riêng này.

**Lưu ý**: Như tên gọi, một đoạn mật khẩu thường là một mật khẩu dài. **Enigmail** sẽ yêu cầu bạn nhập một mật khẩu dài và bảo mật hơn các mật khẩu đơn giản.

**Quan trọng**: Hãy luôn tạo các cặp khóa mã hóa với một đoạn mật khẩu và *không bao giờ* chọn lựa chọn "không có cụm từ mật khẩu".

![](/sbox/screen/thunderbird-vi-1/73.png)

*Hình 21: Cửa sổ Tạo Khóa Mã hóa OpenPGP hiển thị khung Khóa hết hạn (Key Expiry)*

**Lưu ý**: Thời gian một cặp khóa có hiệu lực phụ thuộc vào nhu cầu bảo mật và an ninh của bạn; việc thay đổi khóa định kỳ thường xuyên sẽ khiến việc xâm nhập các cặp khóa mới sẽ càng khó khăn. Tuy nhiên, mỗi lần thay đổi cặp khóa mã hóa, bạn sẽ phải gửi lại khóa công khai cho các đối tác liên lạc và xác nhận với từng người.

**Bước 4**. **Nhập vào** thời gian tương ứng và **chọn** đơn vị thời gian (*ngày* (days), *tháng* (months) hoặc *năm* (years)) để khóa có hiệu lực. 

**Bước 5**. **Nhấn** ![](/sbox/screen/thunderbird-vi-1/74.png) để mở cửa sổ Xác nhận Enigmail.

**Bước 6**. Bạn sẽ được yêu cầu tạo một chứng nhận như trong *hình 17*.

**Bước 7**. **Nhấn** ![](/sbox/screen/thunderbird-vi-1/76.png) để mở cửa sổ *Tạo và Lưu Chứng chỉ Thu hồi* (Create & Save Revocation Certificate).

**Lưu ý**: Nếu bạn biết một đối tượng thù địch hoặc một kẻ phá hoại đã chiếm được khóa riêng của bạn bạn mất quyền kiểm soát khóa riêng này, bạn cần gửi chứng chỉ thu hồi cho các đối tác liên lạc để họ biết và không sử dụng khóa công khai tương ứng. Hãy nhớ thực hiện điều này khi máy tính của bạn bị mất, hay bị tịch thu. Hãy sao lưu dự phòng chứng chỉ thu hồi này.

**Bước 8**. Chuyển tới một thư mục an toàn để lưu chứng nhận như trong màn hình bên dưới và **nhấn** ![](/sbox/screen/thunderbird-vi-1/78.png). Bạn sẽ được yêu cầu nhập mật khẩu tương ứng của cặp khóa vừa tạo.

![](/sbox/screen/thunderbird-vi-1/77.png)

*Hình 22: Cửa sổ Tạo và Lưu Chứng nhận Thu hồi*

**Bước 9**. **Nhấn** ![](/sbox/screen/thunderbird-vi-1/35.png) để hoàn thành việc tạo cặp khóa và chứng nhận thu hồi, và quay về màn hình sau:

![](/sbox/screen/thunderbird-vi-1/79.png) 

*Hình 23: Cửa sổ Quản lý Khóa của Enigmail hiển thị các cập khóa*



**Lưu ý**: **Nhấn chọn** ô *Hiển thị tất cả các khóa theo mặc định* để hiển thị tất cả các khóa tương ứng của các tài khoản thư, hãy đảm bảo rằng bạn đang xem ở một nơi an toàn và riêng tư.

Sau khi tạo thành công khóa mã hóa và chứng chỉ thu hồi tương ứng, bạn đã sẵn sàng trao đổi khóa mã hóa với các đối tác liên lạc tin cậy

### 4.2.3 Hướng dẫn Thiết đặt Enigmail để Sử dụng với Các Tài khoản Thư ###

Để chọn bật **Enigmail** đối với một tài khoản thư nào đó, hãy theo các bước sau:

**Bước 1**.  **Nhấn** ![](/sbox/screen/thunderbird-vi-1/24a.png) để hiển thị *Trình đơn Thunderbird* và **Chọn Công cụ > Account Settings**.

**Bước 2**. **Chọn** mục *OpenPGP Security* trên khung quản lý bên trái như sau: 

![](/sbox/screen/thunderbird-vi-1/80.png)

*Hình 24: Cửa sổ Thiết lập Tài khoản - OpenPGP Security*

**Bước 3**. **Chọn** lựa chọn *Bật hỗ trợ của OpenPGP support* và **chọn** ô *Sử dụng địa chỉ thư điện tử của danh tính này để nhận diện khóa OpenPGP*.

**Bước 4**. **Nhấn** ![](/sbox/screen/thunderbird-vi-1/35.png) để quay về màn hình **Thunderbird**. 

<a name="4.3"></a>
## 4.3 Hướng dẫn Trao đổi Khóa Công khai ##

Trước khi có thể gửi một thư mã hóa cho nhau, bạn và đối tác liên lạc cần trao đổi khóa công khai. Bạn cũng cần xác nhận hiệu lực khóa nhận được bằng việc xác minh rằng khóa đó thực sự thuộc về người đã gửi khóa đó cho bạn. 

### 4.3.1 Hướng dẫn Gửi một Khóa Công khai sử dụng Enigmail ###

Để gửi một khóa công khai dùng **Enigmail**/**OPenPGP**, cả hai phía, bạn và đối tác liên lạc cần thực hiện các bước sau:

**Bước 1**. **Mở Thunderbird** và **nhấn** ![](/sbox/screen/thunderbird-vi-1/81.png) để tạo một tin nhắn mới.

**Bước 2**. Chọn tùy chọn trên trình đơn **Enigmail > Đính kèm Khóa công của tôi**.

Lưu ý: Theo cách này, khung **Phần đính kèm:** sẽ không xuất hiện ngay; khung này chỉ xuất hiện khi tin nhắn được gửi đi.

Nếu bạn muốn gửi một khóa công khác hãy chọn tùy chọn trên trình đơn
**Enigmail > Đính kèm Khóa công của tôi...** và chọn khóa bạn muốn gửi.

![](/sbox/screen/thunderbird-vi-1/82.png)

*Hình 25: Cửa sổ Viết Tin nhắn hiển thị khóa công khai được đính kèm trong cửa sổ Đính kèm*

**Bước 3**. **Nhấn** ![](/sbox/screen/thunderbird-vi-1/83.png) để gửi tin nhắn có đính kèm khóa công khai.

### 4.3.2 Hướng dẫn Nhập một Khóa Công khai sử dụng Enigmail ###

Cả bạn và đối tác liên lạc cân thực hiện giống nhau các bước sau để nhập khóa công khai của nhau.

**Bước 1**. **Chọn** và **mở** tin nhắn có chứa khóa công khai nhận được. Phần đính kèm sẽ xuất hiện giống như sau: ![](/sbox/screen/thunderbird-vi-1/87.png) 

**Bước 2**. **Nhấn** vào tệp đính kèm phía trên ![](/sbox/screen/thunderbird-vi-1/87a.png). Enigmail phát hiện dữ liệu chứa khóa công khai, nó sẽ yêu cầu bạn nhập khóa công khai như sau:

![](/sbox/screen/thunderbird-vi-1/88.png)

*Hình 26: Enigmail xác nhận việc Nhập khóa công khai* 

**Bước 3**. **Nhấn** ![](/sbox/screen/thunderbird-vi-1/89.png) để nhập khóa công khai của đối tác liên lạc.

Nếu việc nhập khóa công khai thành công, một thông báo giống dưới đây sẽ xuất hiện:

![](/sbox/screen/thunderbird-vi-1/90.png)

*Hình 27: Màn hình OpenPGP hiển thị khóa công khai của đối tác liên lạc vừa nhập*

Để xác nhận bạn đã nhận được khóa công khai của đối tác liên lạc, hãy theo các bước:

**Bước 1**. **Chọn Enigmail > Quản lý khóa** để hiển thị cửa sổ *Quản lý Khóa Enigmail* như sau:

![](/sbox/screen/thunderbird-vi-1/91.png)

*Hình 33: Enigmail – Quản lý khóa hiển thị các khóa công khai nhập gần đây* 

**Lưu ý** rằng tùy chọn *Hiển thị Tất cả Khóa theo Mặc định* cần được chọn để có thể thấy tất cả các khóa.

<a name="4.4"></a>
## 4.4 Hướng dẫn Xác minh và Ký cặp Khóa Mã hóa ##

Bước cuối cùng, bạn phải xác minh một khóa nhận được thực sự của đối tác liên lạc gửi cho bạn và xác nhận tính hiệu lực cho khóa này. Đây là một bước rất quan trọng mà cả hai phía liên lạc cần thực hiện đối với các khóa công khai của nhau. 

### 4.4.1 Hướng dẫn Xác minh Cặp Khóa Mã hóa ###

**Bước 1**. **Liên lạc** với đối tác liên lạc của bạn thông qua một phương tiện trao đổi khác với gửi thư điện tử. Bạn có thể sử dụng điện thoại, tin nhắn hoặc phần mềm sử dụng **Giao thức Thoại trên Internet** (**VoIP**) hay các phương thức khác nhưng **phải** chắc chắn rằng mình thực sự đang nói chuyện với đúng người. Vì lý do đó, việc điện thoại hay gặp trực tiếp là cách tốt nhất, nếu thuận tiện và an toàn.

**Bước 2**. Bạn và đối tác liên lạc sẽ xác nhận 'dấu vân tay' ('fingerprints') của các khóa công khai vừa trao đổi. Một 'dấu vân tay' (fingerprint) là một chuỗi số, chữ duy nhất để xác định một khóa mã hóa. Bạn có thể vào cửa sổ**Enigmail** *Quản lý khóa* để xem dấu vân tay của cặp khóa mã hóa bạn đã tạo và của khóa công khai bạn vừa nhập.

Để xem dấu vân tay (fingerprint) của một cặp khóa mã hóa, hãy thực hiện các bước sau:

**Bước 1**. **Chọn > Enigmail > Quản lý khóa** và **nhấn chuột phải** vào một khóa để kích hoạt trình đơn: 

![](/sbox/screen/thunderbird-vi-1/92.png) 

*Hình 29: Trình đơn Quản lý Khóa Enigmail với mục Thuộc tính khóa được chọn*

**Bước 2**. **Chọn** mục *Thuộc tính khóa* để mở cửa sổ sau: 

![](/sbox/screen/thunderbird-vi-1/93.png)

*Hình 30: Cửa sổ Thuộc tính khóa*

Đối tác của bạn cũng phải thực hiện tất cả các bước trên. Xác nhận dấu vân tay cho các khóa đã trao đổi với nhau đảm bảo chúng trùng với dấu vân tay gốc phía người gửi. Nếu chúng không trùng nhau, hãy trao đổi lại khóa công khai và thực hiện lại quá trình xác minh. 

**Lưu ý**: Dấu vân tay (fingerprint) không phải là thông tin cần giữ bí mật và có thể được ghi lại để  xác minh trong lần sau.

### 4.4.2 Hướng dẫn Ký một Khóa Công khai Có hiệu lực ###

Sau khi bạn đã xác nhận một khóa công khai của đối tác là chính xác, bạn có thể *ký số* vào khóa này để xác nhận bạn đã xác minh khóa này có hiệu lực. Việc ký khóa có thể làm lộ mối liên hệ giữa bạn và đối tác liên lạc khi bạn gửi một khóa có ký số tới một ai đó hoặc gửi khóa này lên máy chủ khóa. Để ngăn chặn điều này, hãy luôn chọn tùy chọn *Local signature* dưới đây.

Để ký số vào một khóa công khai, hãy theo các bước sau:

**Bước 1**. **Nhấn Enigmail > Quản lý khóa** để trở về cửa sổ *Quản lý khóa*.

**Bước 2**. **Nhấn chuột phải** vào khóa công khai của đối tác trong cửa sổ *Quản lý khóa* (xem hình 29 phía trên) và  **chọn** lệnh *Ký tên khóa* trong trình đơn để mở cửa sổ sau:

![](/sbox/screen/thunderbird-vi-1/94.png)

*Hình 31: Cửa sổ Enigmail - Sign Key*

**Bước 3**. **Chọn** lựa chọn *Tôi có kiểm soát rất cẩn thận*, **chọn** *Chữ ký cục bộ (không thể xuất ra được)* và **nhấn** ![](/sbox/screen/thunderbird-vi-1/35.png) để ký số vào khóa công khai của đối tác. Bạn có thể được yêu cầu nhập mật khẩu cho khóa riêng của mình. 


#### 4.4.3 Hướng dẫn Quản lý Các Cặp Khóa Mã hóa ####

Cửa sổ *Quản lý khóa Enigmail* được sử dụng để tạo ra, xác minh hiệu lực và ký số vào các cặp khóa mã hóa khác nhau. Tuy nhiên, bạn cũng có thể thực hiện các thao tác khác liên quan tới việc quản lý khóa (xem hình 29 phía trên):


- **Manage User Ids** (Quản lý Mã Người dùng): lệnh này cho phép bạn liên kết nhiều hơn một tài khoản thư điện tử với một cặp khóa mã hóa.
- **Change Expiration Date** (Thay đổi Thời hạn Hết hiệu lực): cho phép bạn thay đổi thời gian hết hạn của cặp khóa mã hóa.
- **Change Passphrase** (Thay đổi Mật khẩu): Lệnh này cho phép bạn thay đổi mật khẩu bảo vệ cặp khóa mã hóa.
- **Generate & Save Revocation Certificate** (Tạo và Lưu Chứng chỉ Thu hồi): Lệnh này cho phép bạn tạo một chứng chỉ thu hồi mới, nếu bạn bị mất hoặc thất lạc chứng chỉ tạo trước đó.

<a name="4.5"></a>
## 4.5 Hướng dẫn Mã hóa và Ký số Tin nhắn ##

**Quan trọng**: Tiêu đề của bất kỳ tin nhắn nào - đúng vậy, phần *Subject* và danh sách các người nhận (bao gồm thông tin trong các trường *To*, *CC* and *BCC*) - *không thể* được mã hóa và sẽ được gửi dưới dạng văn bản thuần. Để đảm bảo bảo mật và an ninh trong liên lạc bằng thư điện tử, tiêu đề thư cần được lưu ý để không mô tả hay chứa bất kỳ thông tin nhạy cảm nào. Thêm vào đó, chúng tôi khuyên bạn nên cho tất cả các địa chỉ nhận vào trường *BCC* khi gửi thư tới một nhóm người nhận.

Khi mã hóa tin nhắn thư điện tử với tệp đính kèm, hãy sử dụng tùy chọn **PGP/MIME**, điều này sẽ mở rộng việc mã hóa cho tất cả các tệp đính kèm vào tin  nhắn của bạn.

Lưu ý rằng bất kỳ thư mã hóa nào bạn gửi với Thunderbird/Enigmail/GnuPG sẽ được tự động mã hóa với  khóa của bạn và khóa của những người trong danh sách nhận thư này, vì vậy bạn có thể giải mã các thư trong thư mục đã gửi.

### 4.5.1 Hướng dẫn Giải mã hóa Tin nhắn ###

Khi cả hai phía trao đổi thông tin đã nhập, xác nhận và ký số vào các khóa công khai của nhau, bạn đã sẵn sàng gửi các tin nhắn mã hóa và giải mã các tin mã hóa nhận được.

Để mã hóa nội dung tin nhắn gửi đi, hãy theo các bước sau:

**Bước 1**. **Mở** tài khoản thư và **Nhấn** 
![](/sbox/screen/thunderbird-vi-1/81.png) để soạn tin nhắn.

**Bước 2**. Để Mã hóa một tin nhắn, **nhấn** *Enigmail > Message sẽ không được mã hóa* và **chọn** *Force Encryption* như trong hình sau:

![](/sbox/screen/thunderbird-vi-1/84.png)

*Hình 33: Tùy chọn Force Encryption*



**Bước 3**. Để Ký số tin nhắn **nhấn** *Enigmail → Message will not be signed* và **chọn** *Force Sign*

**Lưu ý**: Để kiểm tra tin nhắn đã được mã hóa và ký số, hãy kiểm tra hai biểu tượng xuất hiện **được tô đậm**  phía bên góc phải bên dưới của của sổ tin nhắn như sau:

![](/sbox/screen/thunderbird-vi-1/85.png)

*Hình 34: Xác nhận Ký số và Mã hóa Tin nhắn được chọn*

**Bước 4**. **Nhấn** ![](/sbox/screen/thunderbird-vi-1/83.png) để gửi tin nhắn. Bạn sẽ được yêu cầu nhập mật khẩu để sử dụng khóa riêng của mình cho việc ký số tin nhắn.

**Tùy chọn Bước 5.** Nếu bạn đính kèm một tệp tin vào tin nhắn gửi đi, bạn có thể cần **chọn** tùy chọn *Encrypt/sign message as a whole and...* và **nhấn** nút OK, như trong hình sau:

![](/sbox/screen/thunderbird-vi-1/86.png)

*Hình 35: Cửa sổ thông báo Enigmail xuất hiện*

**Lưu ý: Khi bạn mã hóa từng tệp đính kèm một cách riêng biệt (tùy chọn thứ hai trong hình 35 phía trên), các tên của các tệp đính kèm này sẽ không được mã hóa và sẽ được gửi đi dưới dạng văn bản thuần! Điều này có thể dẫn tới việc lộ các thông tin nhạy cảm! Sử dụng PGP/MIME đảm bảo rằng toàn bộ tin nhắn, các tệp đính kèm cùng với tên của các tệp này được mã hóa và ẩn**

### 4.5.2 Hướng dẫn Giải mã hóa Tin nhắn ###

Khi nhận được và mở một tin nhắn mã hóa, **Enigmail/OpenPGP** sẽ tự động tìm cách giải mã tin nhắn. Nếu không, hãy chọn nút *Decrypt*. Cửa sổ sau sẽ xuất hiện:

![](/sbox/screen/thunderbird-vi-1/96.png)

*Hình 36:  Thông báo Enigmail - Yêu cầu nhập mật khẩu OpenPGP hoặc số SmartCard PIN*

**Bước 1**. **Nhập vào** mật khẩu như trong hình phía trên.

Sau khi nhập mật khẩu cho khóa riêng, tin nhắn sẽ được giải mã và hiển thị như sau:

![](/sbox/screen/thunderbird-vi-1/97.png)

*Hình 37: Tin nhắn vừa được giải mã trong cửa sổ tin nhắn.*

Bạn đã thực hiện thành công việc giải mã hóa tin nhắn. Bằng cách thực hiện các bước trong mục **4.5 Hướng dẫn Mã hóa và Giải mã hóa Tin nhắn** trong mỗi lần trao đổi thư điện tử với đối tác, bạn có thể đảm bảo một kênh liên lạc bảo mật và có xác thực cho dù có kẻ tìm cách theo dõi thông tin trao đổi.

### 4.5.2 Hướng dẫn Giải mã hóa Tin nhắn ###

Khi sử dụng *Enigmail* và *GnuPG* để bảo mật tính riêng tư có một điều hết sức quan trọng là chắc chắn rằng toàn bộ thư của bạn gửi đi đều được mã hóa. Điều này đặc biệt bao gồm cả các thư trả lời cho các thư mã hóa, bản nháp của thư bạn muốn mã hóa và các trích dẫn từ các thư trước đây có mã hóa.

**Luôn bật tính năng mã hóa (như hướng dẫn trong phần 4.5.1. Hướng dẫn Mã hóa 
Tin nhắn phía trên) trước khi bạn bắt đầu viết tin nhắn.** Bằng cách này bạn đảm bảo rằng các tin nháp của thư chỉ có thể được ghi lên máy chủ thư ở dạng mã hóa.

Chúng tôi hết sức khuyến nghị **Cấu hình Enigmail để cảnh báo bạn trước khi gửi một thư không được mã hóa**. Các bước sau đây hướng dẫn cách thực hiện:

**Bước 1. Nhấn** *Enigmail > Tùy chỉnh* và **chọn** khung *Sending*.

**Bước 2. Chọn** *Confirm...* và nhấn OK.

![](/sbox/screen/thunderbird-vi-1/97.png)

*Hình 38: Tùy chỉnh Enigmail – Xác nhận trước khi gửi.*

Với mọi tin nhắn không mã hóa bạn gửi giờ sẽ xuất hiện cảnh báo rằng thư sẽ không được mã hóa như hình dưới đây. Nếu bạn muốn gửi một thư mã hóa, **nhấn**  *Cancel* và thực hiện các bước trong mục 4.5.1 phía trên.

![](/sbox/screen/thunderbird-vi-1/98.png)

*Hình 38: Xác nhận Enigmail.*

**Hãy một lần nữa lưu ý rằng** các trường *Tiêu đề*, *Gửi tới*, *CC và BCC* **không bao giờ** được mã hóa.

