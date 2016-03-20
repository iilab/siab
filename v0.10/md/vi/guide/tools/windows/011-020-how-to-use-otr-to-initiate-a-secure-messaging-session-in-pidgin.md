

---

lang: vi
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Use OTR to Initiate a Secure Messaging Session in Pidgin

---

Các mục trong trang này:

- [**3.0 Giới thiệu Pidgin và OTR**](#3.0)
- [**3.1 Hướng dẫn Cấu hình Tiện ích Pidgin-OTR**](#3.1)
- [**3.2 Bước Đầu tiên – Hướng dẫn Tạo Khóa riêng và Hiển thị Dấu tay của khóa này**](#3.2)
- [**3.3 Bước Thứ hai – Hướng dẫn Xác thực một Phiên Nhắn tin**](#3.3)
- [**3.4 Bước Thứ ba – Hướng dẫn Xác thực Danh tính của Đối tác liên lạc**](#3.4)

-------

<a name="3.0"></a>
## 3.0 Giới thiệu Pidgin và OTR ##

Both your correspondent and yourself must configure the **OTR** plugin before you can enable private and secure **Internet Messaging** (**IM**) sessions. Given that this **OTR** plugin was designed especially for **Pidgin**, it will automatically detect when both parties have installed and properly configured the **OTR** plugin.

Cả hai phía thực hiện phiên liên lạc đều cần cài đặt và cấu hình thành phần **OTR** trước khi có thể thực hiện một phiên liên lạc **Nhắn tin Trực tuyến** riêng tư và bảo mật. Do **OTR** là tiện ích được thiết kế đặc biệt cho **Pidgin**, nó sẽ tự động phát hiện khi cả hai phía đều cài đặt và cấu hình đúng thành phần mở rộng này.

Nếu bạn yêu cầu thực hiện một phiên liên lạc bảo mật với một người bạn và người đó chưa cài đặt thành phần **OTR** trong **Pidgin**, một thông báo sẽ được gửi tới người đó hướng dẫn họ cài đặt thành phần này.

**Lưu ý**: Nếu bạn yêu cầu thực hiện một phiên liên lạc bảo mật với một người bạn và người đó chưa cài đặt thành phần **OTR** trong **Pidgin**, một thông báo sẽ được gửi tới người đó hướng dẫn họ cài đặt tiện ích này.

<a name="3.1"></a>
## 3.1 Hướng dẫn Cấu hình Tiện ích Pidgin-OTR ##

Để kích hoạt tiện ích **OTR**, hãy theo các bước sau: 

**Bước 1**. **Nhấn đúp chuột** vào ![](/sbox/screen/pidgin-vi/13.png) hoặc **chọn** **Start > Programs > Pidgin** để khởi động **Pidgin** và mở cửa sổ *Buddy List* (hãy xem *Hình 1*).

**Bước 2**. **Mở** trình đơn *Tools* và **chọn** mục *Plugins* như sau: 

![](/sbox/screen/pidgin-vi/40.png)

*Hình 1: Cửa sổ Buddy List với mục Plugins được trọn trong trình đơn Tools*

*Cửa sổ *Plugins* sẽ hiện ra như sau:* 

**Bước 2**. **Cuộn** xuống tới lựa chọn *Off-the-Record Messaging*, và **nhấn vào** ô chọn tương ứng để kích hoạt tiện ích này. 

![](/sbox/screen/pidgin-vi/41.png)

*Hình 2: Cửa sổ Tiện ích OTR với mục Off-the-Record Messaging được chọn*

**Bước 3**. **Nhấn vào** ![](/sbox/screen/pidgin-vi/42.png) để bắt đầu thiết đặt cửa sổ *Off-the-Record Messaging*.

Về cơ bản, có 3 bước cần thực hiện khi thiết đặt đúng đắn **OTR** để thiết lập một phiên **IM** riêng tư và bảo mật, các bước này được giải thích cụ thể dưới đây: 

- **Bước Đầu tiên**: Tạo ra một khóa riêng duy nhất liên quan tới tài khoản của bạn và hiển thị thông tin dấu tay của khóa riêng này.

Hai bước tiếp theo liên quan tới việc bảo mật phiên **IM** và xác thực đối tác liên lạc.

- **Bước Thứ hai**: Một bên tham gia liên lạc sẽ yêu cầu một khởi tạo một phiên nhắn tin riêng tư và bảo mật với bên kia khi đang kết nối trực tuyến. 

- **Bước Thứ ba** thực hiện việc *xác thực* hoặc kiểm tra danh tính của đối tác liên lạc bằng  **Pidgin**. (**Lưu ý**: Trong **Pidgin**, một đối tác liên lạc (buddy) là bất kỳ ai bạn đang chát cùng trong phiên **IM**. Tiến trình này sẽ xác minh danh tính của một bạn chát đã được *xác thực*  trong **Pidgin**. Điều này sẽ xác định rằng một bạn chát *đúng* là người mà họ tự nhận.   

<a name="3.2"></a>
## 3.2 Bước Đầu tiên – Hướng dẫn Tạo Khóa riêng và Hiển thị Dấu tay của khóa này ##

Việc bảo mật một phiên liên lạc trong **Pidgin** được thực hiện bằng cách tạo một *khóa riêng* (private key) cho các tài khoản tương ứng. Cửa sổ cấu hình tính năng *Off-the-Record* được chia thành hai phần *Config* và *Known fingerprints*.  Khung *Config* được sử dụng để tạo khóa cho từng tài khoản của bạn và chứa các thiết đặt các lựa chọn riêng trong **OTR**. Phần khung *Known fingerprints* chứa khóa của các đối tác liên lạc. Bạn cần có khóa của người bạn muốn thiết lập một phiên liên lạc bảo mật.

![](/sbox/screen/pidgin-vi/43.png)

*Hình 3: Khung Config trong cửa sổ Off-the-Record Messaging*

**Bước 1**. Để tăng cường bảo mật, **nhấn chọn** các tùy chọn *Enable private messaging*, *Automatically initiate private messaging* và *Don't log OTR conversations* trong *khung Config* như trong *Hình 3* phía trên. 

**Bước 2**. **Nhấn vào** ![](/sbox/screen/pidgin-vi/44.png) để thực hiện việc tạo khóa bảo mật của bạn; một màn hình thông báo rằng khóa riêng đang được tạo sẽ xuất hiện như sau:

![](/sbox/screen/pidgin-vi/45.png)

*Hình 4: Hộp thoại xác nhận Tạo khóa riêng*

**Lưu ý**: Đối tác liên lạc của bạn cũng phải thực hiện các bước như trên đối với tài khoản của họ. 

**Bước 3**. **Nhấn vào** ![](/sbox/screen/pidgin-vi/37.png) sau khi khóa riêng (giống như dưới đây), đã được tạo ra: 

![](/sbox/screen/pidgin-vi/46.png)

*Hình 5: Ví dụ về dấu tay của một khóa riêng được tạo bởi OTR*

**Quan trọng:** Bạn vừa tạo một khóa riêng cho một tài khoản của mình. Khóa này sẽ được sử dụng để mã hóa thông tin liên lạc của bạn và không ai có thể đọc được, ngay cả khi họ có thể ‘nghe trộm’ ở giữa kênh truyền giữa bạn và các đối tác. Fingerprint là một chuỗi dài các ký tự và số dùng để xác nhận một khóa mã hóa của một tài khoản nào đó, như trong  *Hình 5* phía trên. 

**Pidgin** tự động lưu và kiểm tra fingerprints của bạn cũng như các đối tác, do đó bạn không cần phải ghi nhớ thông tin này.

<a name="3.3"></a>
## 3.3 Bước Thứ hai – Hướng dẫn Xác thực một Phiên Nhắn tin ##

**Bước 1. Nhấn đúp chuột** vào tài khoản của đối tác đang trực tuyến để bắt đầu một phiên trao đổi tin nhắn trực tuyến. Nếu cả hai phía đều có cài đặt thành phần **OTR** với thiết đặt đúng đắn thì bạn sẽ thấy một nút **OTR** xuất hiện phía bên góc dưới cửa sổ chát.

![](/sbox/screen/pidgin-vi/47.png)

*Hình 6: Một cửa sổ chát hiển thị biểu tượng OTR*

**Bước 2**. **Nhấn vào** ![](/sbox/screen/pidgin-vi/48.png) để mở trình đơn tương ứng và **chọn** mục *Start private conversation* như sau: 

![](/sbox/screen/pidgin-vi/49.png)

*Hình 7: Trình đơn với mục Khởi tạo hội thoại bảo mật được chọn*

*Cửa sổ **Pidgin IM** của bạn sẽ xuất hiện như sau:*

![](/sbox/screen/pidgin-vi/50.png)

*Hình 8: Cửa sổ Pidgin IM hiển thị khung Unverified (Chưa Kiểm tra)*

**Lưu ý**: **Pidgin** tự động kết nối với chương trình **IM** của đối tác liên lạc và tạo ra các thông báo khi bạn muốn thực hiện một phiên nhắn tin riêng tư và bảo mật. Kết quả là nút ![](/sbox/screen/pidgin-vi/48.png) **OTR** chuyển thành ![](/sbox/screen/pidgin-vi/51.png), xác đinh rằng bạn đã tạo được một kênh trao đổi mã hóa với đối tác liên lạc.

**Cảnh báo**! Mặc dù kênh trao đổi này giờ đã bảo mật, Tuy nhiên đối tác này chưa được *xác thực*. Hãy cảnh giác, người này tế có thể là một ai đó sử dụng máy tính ở phía bên kia hoặc ai đó *giả danh* là đối tác bạn cần trao đổi. 

<a name="3.4"></a>
## 3.4 Bước Thứ ba – Hướng dẫn Xác thực Danh tính của Đối tác liên lạc ##

Bạn có thể sử dụng một trong ba phương thức xác nhận danh tính để xác thực một đối tác liên lạc  **Pidgin**; bạn có thể sử dụng 1). một đoạn mật khẩu bí mật trao đổi từ trước 2). đưa ra một câu hỏi, câu trả lời chỉ có bạn và đối tác thực sự biết hoặc 3) tự kiểm tra dấu tay của khóa bằng các phương thức liên lạc khác.

### Phương thức Mật khẩu Bí mật ###

Bạn có thể trao đổi một đoạn hay từ mật khẩu bí mật từ trước với đối tác liên lạc bằng cách gặp mặt trực tiếp hay các phương tiện trao đổi khác (như điện thoại, hội thoại qua mạng bằng **Skype** hoặc sử dụng tin nhắn điện thoại di động). Khi cả hai phía cùng nhập đúng đoạn mã bí mật, phiên nhắn tin của bạn sẽ được xác thực. 

**Lưu ý**: Tính năng nhận dạng đoạn mã bí mật của **OTR** có phân biệt chữ hoa chữ thường, đúng vậy, nó có thể phân biệt các chữ viết hoa (A,B,C) và các chữ viết thường (a,b,c). Hãy ghi nhớ điều này khi bạn muốn tạo ra một đoạn mã hay từ bí mật!

**Bước 1** . **Nhấn vào** nút *OTR* trên cửa sổ chát sau đó  **chọn** mục *Authenticate Buddy* như sau: 

![](/sbox/screen/pidgin-vi/52.png)

*Hình 9: Trình đơn Unverified với mục Authenticate buddy được chọn*

Cửa sổ *Authenticate Buddy* sẽ xuất hiện, yêu cầu bạn chọn phương thức xác thực. 

**Bước 2**. **Nhấn vào** ![](/sbox/screen/pidgin-vi/53.png) và **chọn** *Shared Secret* như sau: 

![](/sbox/screen/pidgin-vi/54.png)

*Hình 10: Cửa sổ Authenticate buddy với danh sách các mục chọn* 

**Bước 3**. **Nhập** đoạn mã hoặc từ bí mật như dưới đây:

![](/sbox/screen/pidgin-vi/55.png)

*Hình 11: Cửa sổ Shared Secret* 

**Bước 4**. **Nhấn vào** ![](/sbox/screen/pidgin-vi/56.png) để mở cửa sổ sau:

![](/sbox/screen/pidgin-vi/57.png)

*Hình 12: Cửa sổ Authenticate Buddy cho một đối tác tưởng tượng*

**Bước 5**. **Nhấn tiếp vào** ![](/sbox/screen/pidgin-vi/56.png) để mở thanh trạng thái xác thực *Authenticating Buddy*; cửa sổ sau sẽ hiện ra sau một lúc:

![](/sbox/screen/pidgin-vi/58.png)

*Hình 13: Cửa sổ Authenticate Buddy cho một đối tác tưởng tượng*

**Lưu ý**: *Đối tác của bạn cũng sẽ thấy một cửa sổ y hệt ở phía họ và sẽ phải nhập đúng đoạn mã bí mật. Nếu chúng khớp nhau, phiên nhắn tin của bạn sẽ được xác thực.*

Khi phiên làm việc được xác thực, nút *OTR* sẽ chuyển thành ![](/sbox/screen/pidgin-vi/51.png). Phiên nhắn tin trực tuyến của bạn giờ đã được bảo mật và bạn có thể chắc chắn rằng mình đang trao đổi với đúng đối tác.

### Phương thức Câu hỏi và Trả lời ###

Một phương thức khác để xác thực lẫn nhau là sử dụng câu hỏi và trả lời. Hãy tạo một câu hỏi và câu trả lời. Sau khi đọc câu hỏi, đối tác của bạn sẽ phải nhập câu trả lời *chính xác*, và nếu câu trả lời khớp với của bạn, danh tính của bạn tự động được xác thực. 

**Bước 1**. **Nhấn vào** trình đơn *OTR* trên cửa sổ chát đang hoạt động để mở danh sách lệnh và  **chọn** *Authenticate Buddy* window (please refer to *Hình 9*).

![](/sbox/screen/pidgin-vi/59.png)

*Hình 14: Cửa sổ chát Pidgin hiển thị biểu tưởng OTR*

cửa sổ *Authenticate Buddy* sẽ yêu cầu bạn chọn phương thức xác thực. 

**Bước 2**. **Nhấn vào** danh sách xổ xuống và **chọn** mục *Question and Answer* như sau:  

![](/sbox/screen/pidgin-vi/60.png)

*Hình 15: Cửa sổ Authenticate buddy*

**Bước 3**. **Nhập** câu hỏi và câu trả lời tương ứng. Câu hỏi này sẽ được gửi tới phía đối tác liên lạc. 

![](/sbox/screen/pidgin-vi/61.png)

*Hình 16:Cửa sổ Questions and Answer*

Nếu câu trả lời phía bên kia khớp với của bạn, danh tính hai bên sẽ được xác thực và kiểm tra và hai phía tham gia liên lạc đều là những người họ tự nhận!

Sau khi xác thực thành cộng, nút *OTR* sẽ chuyển thành ![](/sbox/screen/pidgin-vi/51.png). Phiên làm việc của bạn sẽ được bảo mật và bạn có thể chắc chắn về danh tính của đối tác liên lạc.

Hãy lưu ý khi bạn **Chọn > Buddy List > Tools > Plugins > Off The Record Messaging > Configure Plugin**, khung *Known fingerprints* giờ sẽ hiển thị dấu tay của tài khoản đối tác liên lạc và thông báo rằng danh tính của họ đã được xác thực. 

![](/sbox/screen/pidgin-vi/62.png)

*Hình 17: Cửa sổ Off-the-Record Messaging hiển thị khung Known Fingerprints*

Xin chúc mừng! Giờ bạn có thể nhắn tin trực tuyến một cách riêng tư. Trong lần chát tiếp theo giữa bạn và đối tác liên lạc (vẫn sử dụng những máy tính này), bạn có thể bỏ qua bước một và ba phía trên. Bạn chỉ cần yêu cầu một kết nối bảo mật và phía đối tác chấp nhận. 

