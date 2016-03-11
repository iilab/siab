

---

lang: vi
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: Jitsi - How to Install and Add Different Accounts in Jitsi

---

Các mục trong trang này:

- [**2.1 Hướng dẫn Cài đặt Jitsi**](#2.1)
- [**2.2 Hướng dẫn Thêm các Tài khoản vào Jitsi**](#2.2)
- [**2.2.1 Hướng dẫn Thêm một Tài khoản Gmail/Google**](#2.2.1)
- [**2.2.2 Đăng ký mới một tài khoản Jabber/XMPP hoặc SIP và thêm vào Jitsi**](#2.2.2)
- [**2.2.3 Hướng dẫn Thêm một Tài khoản Facebook**](#2.2.3)
- [**2.3 Hướng dẫn thay đổi mật khẩu cho một tài khoản Jitsi**](#2.3)
- [**2.4 Hướng dẫn cấu hình Jitsi để tăng cường bảo mật**](#2.4)
- [**2.4.1 Vô hiệu và gỡ bỏ lược sử các cuộc gọi và nhắn tin**](#2.4.1)
- [**2.4.2 Yêu cầu nhắn tin bảo mật khi sử dụng nhắn tin trực tuyến**](#2.4.2)
- [**2.4.3 Bảo vệ mật khẩu cho mọi tài khoản với mật khẩu chủ**](#2.4.3)

<a name="2.1"></a>
## 2.1 Hướng dẫn Cài đặt Jitsi ##

Để cài đặt **Jitsi**, hãy thực hiện các bước sau:

**Bước 1**. **Nhấn đúp chuột** vào ![](/sbox/screen/jitsi-en/02.png); hộp thoại *Open File - Security Warning* (*Mở Tệp - Cảnh báo Bảo mật*) có thể xuất hiện. Nếu vậy, **Nhấn** ![](/sbox/screen/jitsi-en/03.png) để mở cửa sổ *Windows Installer*, tiếp theo là cửa sổ *Welcome to the Jitsi Setup Wizard* (*Chào mừng tới Thuật sỹ Cài đặt Jitsi*).  

**Bước 2**. **Nhấn** ![](/sbox/screen/jitsi-en/04.png) để kích hoạt cửa sổ *End User License Agreement* (*Cam kết Bản quyền Người dùng cuối*); **chọn** ô *I accept the terms in the License Agreement* (*Tôi chấp nhận các điều khoản trong phần Cam kết Bản quyền*) để hiển thị nút *Next*, sau đó **nhấn**  ![](/sbox/screen/jitsi-en/04.png) để mở cửa sổ *Destination Folder* (*Thư mục Cài đặt*).

**Bước 3**. **Nhấn** ![](/sbox/screen/jitsi-en/04.png) để mở cửa sổ *Additional Tasks* và chấp nhận những thiết đặt mặc định như hiển thị.

**Lưu ý**: Chọn tùy chọn *Auto-start when computer restarts or reboots*  (*Tự động khởi động khi hệ thống khởi động*) có thể làm chậm máy tính của bạn, đặc biệt là khi bạn đã cài đặt nhiều ứng dụng khác tự động chạy mỗi khi máy tính khởi động.

**Bước 4**.  **Nhấn** ![](/sbox/screen/jitsi-en/04.png) để chuyển sang cửa sổ *Ready to Install Jitsi* (*Sẵn sàng Cài đặt Jitsi*), và **nhấn** ![](/sbox/screen/jitsi-en/05.png) để mở cửa sổ *Installing Jitsi* (*Cài đặt Jitsi*) hiển thị trạng thái tiến trình cài đặt.

**Bước 5**. **Nhấn** ![](/sbox/screen/jitsi-en/06.png) để hoàn thành tiến trình cài đặt và tự động khởi động cửa sổ *Đăng nhập* **Jitsi** như dưới đây:

![](/sbox/screen/jitsi-en/07.png)

*Hình 1: Cửa sổ đăng nhập Jitsi*

**Lưu ý**: Trong một số phiên bản, việc cài đặt và mở chương trình **Jitsi** lần đầu tiên sẽ khiến xuất hiện cảnh báo *Windows Security Alert* (*Cảnh báo Bảo mật Windows*)  (*Hình 2* bên dưới). Cảnh báo này là một hành động bình thường của hệ điều hành **MS Windows**, bạn có thể tiếp tục với ** Jitsi**. Ngay cả khi bạn không nhấn bất kỳ nút nào và chỉ đơn giản đóng cửa sổ cảnh báo vừa xuất hiện, **Jitsi** vẫn có thể kết nối thông qua các máy chủ công cộng như **Jabber/XMPP hoặc SIP**, **Google Chat** và **Facebook Chat**, hoặc **Yahoo Messenger**. Tuy nhiên, việc nhấn chọn nút *Allow access* (*Cho phép truy cập*) cho phép các tính năng nâng cao trong **Jitsi** là *Registrarless SIP Accounts* (*Các tài khoản SIP không đăng ký*). Để có thêm thông tin về loại tài khoản đặc biệt này, hãy tham khảo trang [**Registrarless SIP Accounts**](https://jitsi.org/Documentation/RegistrarlessSIPAccount).  

![](/sbox/screen/jitsi-en/08.png)

*Hình 2: Cửa sổ Cảnh báo Bảo mật Windows*

**Bước 6**. **Chọn** *cả hai* tùy chọn mạng **Private** và **Public**, sau đó **nhấn** **Allow access** để mở cửa sổ Đăng nhập **Jitsi** (như trong *Hình 1* phía trên) hoặc mở cửa sổ giao diện người dùng chính (như trong *Hình 4* bên dưới).


<a name="2.2"></a>
## 2.2 Hướng dẫn Thêm các Tài khoản vào Jitsi ##

Phần này hướng dẫn thêm hoặc thiết đặt các loại tài khoản khác nhau trong **Jitsi**. **Jitsi** hỗ trợ nhiều loại tài khoản khác nhau. Các tài khoản chúng tôi đề cập dưới đây dựa chủ yếu trên các giao thức truyền thông **Jabber/XMPP** và **SIP**. Trong số nhiều loại dịch vụ, **Jitsi** cho phép bạn sử dụng các tài khoản **Gmail** hoặc **Facebook** để liên lạc. Bởi vì các dịch vụ này là một trong những dịch vụ phổ biến nhất hiện nay sử dụng trên mạng Internet, hướng dẫn thêm các tài khoản này vào Jitsi được nêu bên dưới đây, cùng với chỉ dẫn cách tăng cường bảo mật khi bạn liên lạc sử dụng những tài khoản này, đem lại lợi ích từ sử dụng lớp mã hóa độc lập của **Jitsi** phía trên tầng bảo vệ được cung cấp bởi các nhà cung cấp dịch vụ của những tài khoản này. Tuy nhiên, xin hãy lưu ý rằng, ngay cả với lớp mã hóa riêng của **Jitsi**, các nhà cung cấp dịch vụ như **Google** hay **Facebook** đang giám sát những thông tin thực tế rằng bạn đang liên lạc (và có thể cả thông tin bạn đang liên lạc với ai), và có thể chia sẻ thông tin này với một bên thứ ba, như là một tổ chức hoặc chính phủ khác. Vì lý do đó, có lẽ tốt nhất nên tránh sử dụng những tài khoản này khi liên lạc những thông tin nhay cảm, thậm chí khi bạn sử dụng với lớp mã hóa của **Jitsi**. Chúng tôi cũng hướng dẫn trong phần này cách tạo các tài khoản (Jabber/XMPP or SIP) có tính bảo mật cao hơn và thêm những tài khoản này vào Jitsi, đồng thời chúng tôi khuyến nghị sử dụng những tài khoản này.

<a name="2.2.1"></a>
### 2.2.1 Hướng dẫn Thêm một Tài khoản Gmail/Google ###

**Lưu ý**: Ví dụ dưới đây sử dụng tài khoản **Google Talk**, tiến trình cài đặt cho các giao thức truyền thông khác đã liệt kê trong *Hình 1* phía trên cũng tương tự. Kết nối liên lạc hoặc một số tính năng khác (như lớp mã hóa độc lập cho nhắn tin văn bản và thoại - **OTR** và **ZRTP**) có thể không hoạt động giữa hay hay nhiều người dùng sử dụng các loại tài khoản khác nhau (như Facebook, Gmail, Yahoo, vv.). Tuy nhiên, những tính năng này thường sẽ hoạt động khi liên lạc giữa các tài khoản của cùng một nhà cung cấp dịch vụ.

**Bước 1**. **Chọn Start > Jitsi** hoặc **nhấn đúp chuột** vào biểu tượng **Jitsi** trên màn hình để mở **Jitsi**.

**Bước 2**. Trong cửa sổ *sign in* (đăng nhập), **nhập vào** tên người dùng và mật khẩu tài khoản **Gmail** bạn muốn sử dụng để liên lạc, khi đó cửa sổ sẽ giống như dưới đây:

![](/sbox/screen/jitsi-en/09.png)

*Hình 3: Cửa sổ "Đăng nhập" Jitsi (đã thay đổi kích thước)*

**Lưu ý**: Bạn có thể thêm nhiều tài khoản sử dụng các giao thức liên lạc khác nhau cùng lúc. 

**Bước 3**. **Nhấn** ![Sign in](/sbox/screen/jitsi-en/09s.png) để mở cửa sổ liên lạc dùng tài khoản của minh như dưới đây:

![](/sbox/screen/jitsi-en/10.png)

*Hình 4: Một ví dụ cửa sổ Jitsi sau khi thêm tài khoản Gmail*

**Lưu ý:** Nếu bạn đóng cửa sổ *Sign in* (*Đăng nhập*), hoặc bạn muốn thêm một tài khoản khác, bạn có thể thực hiện bằng cách **chọn *File* > *Add new account...***. Trong cửa sổ mới **chọn Network** là *Google Talk* và **nhập vào** tên người dùng cùng mật khẩu của tài khoản **Gmail** như hiển thị dưới đây:

![](/sbox/screen/jitsi-en/11.png)

*Hình 5: Cửa sổ "Add new account" („Thêm tài khoản mới“)*

Để kiểm tra bạn đã đã đăng ký tài khoản **Gmail** của mình với **Jitsi**, hãy theo các bước sau:

**Bước 1**. **Chọn *Tools* > *Options*** trong trình đơn để kích hoạt cửa sổ:

![](/sbox/screen/jitsi-en/12.png)

*Hình 6: Cửa sổ Options (Các tùy chọn) hiển thị tài khoản Gmail vừa đăng ký (đã thay đổi kích thước)*

**Lưu ý:** nếu bạn sử dụng [xác minh 2-bước](https://support.google.com/accounts/answer/180744?hl=vi) để bảo vệ truy cập vào tài khoản **Gmail** của mình, khi bạn đăng nhập từ **Jitsi** sử dụng mật khẩu thông thường của mình bạn có thể thấy thông báo như dưới đây xuất hiện. Để đăng nhập dùng **Jitsi**, bạn sẽ cần phải tạo một "mật khẩu ứng dụng". Hãy tham khảo [hướng dẫn thực hiện](https://support.google.com/accounts/answer/185833?hl=vi).

![](/sbox/screen/jitsi-en/13.png)

*Hình 7: Ví dụ về lỗi đăng nhập với Google Talk*

<a name="2.2.2"></a>
### 2.2.2 Đăng ký mới một tài khoản Jabber/XMPP hoặc SIP và thêm vào Jitsi ###

**Jabber/XMPP** và **SIP** là những chuẩn mở cho liên lạc tin nhắn văn bản và thoại. Có [nhiều máy chủ](https://xmpp.net/directory.php) cung cấp miễn phí các tài khoản cho phép bạn sử dụng với Jitsi. Dưới đây chúng tôi giới thiệu một số máy chủ bạn có thể sử dụng cho việc liên lạc những thông tin nhạy cảm. Lưu ý rằng bạn cũng có thể tải về [phần mềm máy chủ Jabber/XMPP](http://xmpp.org/xmpp-software/servers/) (như [ejabberd](http://www.process-one.net/en/ejabberd/) hoặc [Prosody IM](http://prosody.im/)), và cài đặt trên máy chủ riêng của bạn và thiết đặt để sử dụng cho liên lạc riêng bảo mật giữa những thành viên trong nhóm, cộng đồng hay tổ chức của mình.

* Tài khoản Jabber/XMPP **Riseup.net** 

Nếu bạn sử dụng một tài khoản [dịch vụ thư điện tử bảo mật Riseup.net](/vi/riseup-main) (được đặt tại Mỹ) bạn có thể [sử dụng tài khoản này để liên lạc qua mạng Jabber/XMPP](https://www.riseup.net/en/chat) băng cách thêm tài khoản này vào Jitsi – hãy xem phía dưới hướng dẫn thêm tài khoản Jabber/XMPP đã có.

* Tài khoản **Jabber.ccc.de** và các tài khoản Jabber/XMPP khác

Bạn có thể đăng ký một tài khoản trên máy chủ  Jabber.ccc.de (đặt tại Đức) bằng cách thực hiện các bước sau:

**Bước 1**.  Trong **Jitsi, chọn *File* > *Add new account...*** trên trình đơn. Trong cửa sổ mới hiện ra, **chọn *Network*: XMPP** và **nhấn chọn** tùy chọn *Create a new XMPP account***. Trong ô *Server*, **nhập** jabber.ccc.de, **nhập** vào tên người dùng XMPP bạn muốn tạo, và **điền vào** ô *Password* (*Mật khẩu*) và *Confirm password* (Xác nhận mật khẩu) giống như dưới đây:

![](/sbox/screen/jitsi-en/14.png)

*Hình 8: Ví dụ cửa sổ "Add new account" (Thêm tài khoản) với tùy chọn "Tạo một tài khoản XMPP" được lựa chọn*

**Bước 2**. **Nhấn *Add***. Sau khi đăng ký thành công bạn sẽ thấy màn hình giống như trong *Hình 4* phía trên.

Nếu tên người dùng bạn muốn tạo đã được sử dụng bởi ai đó, việc đăng ký sẽ thất bại với thông báo *We failed to create your account due to the following error: Could not confirm data.*  (*Chúng tôi đã thất bại trong việc tạo ra tài khoản mới cho bạn với lý do sau: Không thể xác nhận dữ liệu*). Bạn có thể thử lại tiến trình đăng ký với một tên người dùng khác.

**Lưu ý** rằng nếu bạn không đăng nhập vào jabber.ccc.de trong thời gian quá 12 tháng, tài khoản của bạn sẽ tự động bị xóa khỏi máy chủ và tên người dùng này sẽ có thể được đăng ký bởi một người khác.

Một máy chủ Jabber/XMPP xứng đáng được giới thiệu là **jit.si**. Máy chủ này được duy trì bở các nhà phát triển phần mềm Jitsi. Bạn có thể đăng ký tài khoản [**jit.si**](https://jit.si) và nhiều những máy chủ Jabber/XMPP công cộng khác cùng theo cách đã hướng dẫn phía trêncủa mục này. Dịch vụ Giám sát IM duy trì một [danh sách và thứ hạng các máy chủ Jabber/XMPP công cộng](https://xmpp.net/directory.php), và cũng cho phép bạn [kiểm tra bất kỳ máy chủ Jabber/XMPP về tính bảo mật](https://xmpp.net/index.php).

* Tài khoản SIP **ostel.co**

Các tài khoản **SIP** không thể được đăng ký từ chương trình **Jitsi**. Máy chủ **ostel.co** (đặt tại Mỹ) cho phép [đăng ký trên trang của họ](https://ostel.co/users/sign_up). **Chọn** một tên người dùng, mật khẩu và cung cấp địa chỉ thư điện tử của bạn sau đó **nhấn** nút *Sign up* (*Đăng nhập*) trên trang web. Sau khi đăng ký thành công, hãy quay lại chương trình Jitsi. **Chọn *File* > *Add new account...*** trên trình đơn, **chọn Network: SIP**, **nhập vào** tên người dùng (ví dụ terence.the.tester@ostel.co) và mật khẩu bạn đã tạo trong quá trình đăng ký trên trang web sau đó **nhấn *Add***. Hãy xem thêm thông tin trong các hình dưới đây:

![](/sbox/screen/jitsi-en/15.png)

*Hình 9: Ví dụ cửa sổ "Add new account" window cho tài khoản SIP*

* **Thêm một tài khoản Jabber/XMPP hoặc SIP đã đăng ký vào Jitsi**

Nếu bạn đã có một tài khoản Jabber/XMPP hoặc SIP bạn có thể thêm vào **Jitsi** bằng cách **chọn *File* > *Add new account...*** trên trình đơn và chọn **Network** tương ứng ( XMPP hoặc SIP tùy theo dạng tài khoản của bạn).

<a name="2.2.3"></a>
### 2.2.3 Hướng dẫn Thêm một Tài khoản Facebook ###

**Facebook** có hai thiết đặt bạn có thể cần thay đổi trước khi **Jitsi** có thể kết nối tới Facebook Chat.

 **Tên Người dùng Facebook**

**Facebook** yêu cầu một tên người dùng để **Jitsi** có thể kết nối vào Facebook chat. Nhiều người dùng **Facebook** đã có một tên người dùng. Để kiểm tra tên người dùng của bạn, hãy **đăng nhập** vào tài khoản **Facebook** của bạn: tên người dùng của bạn xuất hiện trên trang địa chỉ của trình duyệt phía sau *https://www.facebook.com/* khi bạn đang ở trang Timeline hoặc Page. Tên người dùng của bạn cũng chính là địa chỉ thư điện tử **Facebook** đối với tài khoản riêng (ví dụ: tênngườidùng@facebook.com). Bạn có thể thấy hoặc thay đổi tên người dùng hoặc tạo một tên tên người dùng bằng cách vào phần *Account Settings* > *General* hoặc truy cập [https://www.facebook.com/username](https://www.facebook.com/username). Để đặt thông tin tên người dùng, **Facebook** có thể yêu cầu việc xác minh thông tin tài khoản của bạn và điều này có thể đòi hỏi việc gửi một tin nhắn tới số điện thoại bạn cần cung cấp cho **Facebook** trong quá trình xác minh. Để tìm hiểu thêm hãy tham khảo [Giải thích của Facebookvề tên người dùng](https://www.facebook.com/help/329992603752372/).

* **Các thiết đặt Apps**

„Nền tảng ứng dụng“ trong **Facebook** cần được bật trước khi **Jitsi** có thể kết nối tới Facebook Chat. Hãy truy cập trang **Facebook** của bạn trong mục *Account Settings > Apps* và nhấn chọn thiết đặt *Apps you use* là *On*. Hành động này sẽ bật "nền tảng ứng dụng" cho tài khoản của bạn.

**Lưu ý** việc bật  "nền tảng ứng dụng" trong **Facebook** sẽ mở cửa cho nhiều dữ liệu *Facebook** của bạn cho các bên phát triển ứng dụng thứ ba. Những dữ liệu này sẽ có sẵn không chỉ cho các ứng dụng **Facebook** bạn sử dụng, mà còn cho các ứng dụng **Facebook** được sử dụng bởi những người trong danh sách bạn bè của bạn. Sau khi bật  "nền tảng ứng dụng" trong  **Facebook**, hãy chắc chắn kiểm tra các thiết đặt trong phần "Apps others use". thiết đặt này cho phép bạn ẩn một số thông tin cá nhân khỏi những ứng dụng sử dụng bởi bạn bè của bạn. 
Thật không may, **Facebook** không cung cấp các thiết đặt giúp ẩn toàn bộ thông tin cá nhân. Một số mục thông tin (như danh sách bạn bè của bạn, giới tính hoặc thông tin bạn đã chọn đăng công cộngl) đều sẵn có khi „bật“ "nền tảng ứng dụng" trong **Facebook**. Tùy thuộc vào bạn xác định có chấp nhận sự đánh đổi tính riêng tư của mình hay không.

Giờ bạn đã sẵn sàng để thêm tài khoản **Facebook** vào **Jitsi**. Để thực hiện, hãy theo các bước sau:

**Bước 1**.  Trong trình đơn chính **chọn *File > Add New Account...***

**Bước 2**.  Trong hộp thoại Add New Account, trình đôn **Network** hãy chọn *Facebook*, **nhập tên người dùng và mật khẩu của ban** và **nhấn "Add"**
 
![](/sbox/screen/jitsi-en/16.png)

*Hình 10: Ví dụ cửa sổ "Add new account..." thêm tài khoản Facebook*


<a name="2.3"></a>
## 2.3 Hướng dẫn thay đổi mật khẩu cho một tài khoản Jitsi ##

Một phần quan trọng trong bảo mật là biết cách thay đổi mật khẩu cho mỗi tài khoản mà một người sở hữu. Nhiều tài khoản bạn có thể sử dụng với Jitsi cho phép thay đổi mật khẩu trong quá trình thiết đặt, thường có thể được thực hiện qua giao diện web. Tuy nhiên một số tài khoản abber/XMPP và SIP sẽ không có bất kỳ giao diện web nào để quản lý chúng. Bạn cần thay đổi mật khẩu cho những tài khoản này sử dụng Jitsi theo các bước sau:


**Bước 1**. **chọn *Tools* > *Options*** trên trình đơn, **chọn** khung ***Accounts*** 

![](/sbox/screen/jitsi-en/17.png)

*Hình 11: Cửa sổ Các tùy chọn với một tài khoản được chọn*

**Bước 2**. **Nhấn vào nút *Edit*** ở phía dưới để mở cửa sổ sau:

![](/sbox/screen/jitsi-en/18.png)

*Hình 12: cửa sổ Thuật sỹ Đăng ký Tài khoản với nút Đổi mật khẩu tài khoản ở phía dưới*

**Bước 3**. **Nhấn vào *Change account password*** (*Thay đổi mật khẩu*) để mở cửa sổ *Change account password*:

![](/sbox/screen/jitsi-en/19.png)

*Hình 13: Cửa sổ thay đổi mật khẩu*

**Bước 4**. ***Nhập mật khẩu mới* và *Nhập lại mật khẩu*** sau đó **Nhấn nút *OK*** để đóng cửa sổ.

**Bước 5**. Đóng Thuật sỹ Đăng ký Tài khoản.

<a name="2.4"></a>
## 2.4 Hướng dẫn cấu hình Jitsi để tăng cường bảo mật ##

<a name="2.4.1"></a>
### 2.4.1 Vô hiệu và gỡ bỏ lược sử các cuộc gọi và nhắn tin ###

**Jitsi** mặc định lưu trữ các thông tin về các cuộc gọi thoại/video đến và đi cũng như lược sử các tin nhắn văn bản – tất cả các tin nhắn bạn gửi và nhận. Bạn có thể truy cập các cuộc gọi thoại/video calls bằng cách **nhấn** vào biểu tượng đồng hộ trong cửa sổ chính Jitsi:

![](/sbox/screen/jitsi-en/20.png)

*Hình 14: Phần trên cửa sổ chính Jitsi với nút lịch sử cuộc gọi được chọn*

Bạn có thể thấy lịch sử các tin nhắn văn bản bằng cách **nhấn** vào biểu tượng có hình đồng hồ quả trứng trong cửa sổ nhắn tin văn bản khi liên lạc với một đối tác:

![](/sbox/screen/jitsi-en/21.png)

*Hình 15: Cửa sổ Nhắn tin với nút lịch sử tin nhắn được chọn*

Dữ liệu được thu thập và lưu trữ trên ổ đĩa máy tính của bạn. **Thậm chí khi bạn mã hóa tin nhắn văn bản với OTR mọi tinh nhắn gửi và nhận được lưu trữ trên máy tính của bạn dưới dạng văn bản mở.** Dữ liệu tương tự như vậy cũng được thu thập và lưu trữ trên ổ đĩa máy tính của những đối tác bạn liên lạc.

Để ngăn không cho phép Jitsi thu thập những dữ liệu này (và xóa bỏ những dữ liệu đã thu thập), **bạn và đối tác liên lạc cần thực hiện các bước sau**.

#### Để vô hiệu Jitsi trong việc thu thập dữ liệu: ####

**Bước 1**.  **chọn *Tools* > *Options*** trên trình đơn, **chọn** khung ***General*** và **hủy chọn** tùy chọn ***Log chat history*** (*Ghi lại lịch sử nhắn tin*) như trong hình dưới đây:

![](/sbox/screen/jitsi-en/22.png)

*Hình 16: Cửa sổ "Options", khung "General" với tùy chọn "Log chat history" được hủy chọn*

**Bước 2**. trong của sổ *Options* window, trước tiên **chọn khung *Advanced***, sau đó **chọn mục *Logging***, và **hủy chọn tùy chọn *Enable packet logging*** như trong hình dưới đây: 

![](/sbox/screen/jitsi-en/23.png)

*Hình 17: Cửa sổ "Options", khung "Advanced", mục "Logging" với tùy chọn "Enable packet logging" được hủy chọn*

Những thay đổi sẽ có hiệu lực khi bạn **khởi động lại Jitsi**.

#### Để gỡ bỏ những dữ liệu đã được thu thập về các cuộc gọi và tin nhắn văn bản: ####

**Bước 1**. **Thoát khỏi** Jitsi.

**Bước 2**. Xóa toàn bộ thư mục ghi lại lịch sử *history_ver1.0* trong thư mục **Jitsi** *user profile*. Bạn có thể xóa một thư mục con của *history_ver1.0* nếu bạn chỉ muốn hủy bỏ một phần của thông tin lịch sử lưu trữ. Vị trí thư mục *user profile* và *log history* tùy thuộc vào hệ điều hành:

* Trong Windows XP và các phiên bản trươc đó, các thu mục này nằm trong *C:\Documents and Settings\&lt;Windows login/user name&gt;\Application Data\Jitsi\history_ver1.0*
* Trong Windows Vista, 7, 8, đó là thư mục *C:\Users\&lt;Windows login/user name&gt;\AppData\Roaming\Jitsi\history_ver1.0* (**lưu ý** rằng thư mục "AppData" có thể bị ẩn. Hãy tham khảo [làm thế nào để hiện tệp ẩn](http://windows.microsoft.com/en-us/windows/show-hidden-files)).
* Trong Mac OS X: từ thư mục người dùng *~/Library/Application Support/Jitsi/history_ver1.0*
* Linux: từ thư mục người dùng *~/.jitsi/history_ver1.0* (**Lưu ý** rằng thưu mục ".jitsi" có thể bị ẩn. Hãy tham khảo [làm thế nào xem tệp ẩn trong Ubuntu](http://itsfoss.com/hide-folders-and-show-hidden-files-in-ubuntu-beginner-trick/))

Tham khảo [Làm thế nào để phá hủy thông tin nhạy cảm](/vi/chuong-6) để biết cách hủy bỏ thông tin một cách bảo mật.


<a name="2.4.2"></a>
### 2.4.2 Yêu cầu nhắn tin bảo mật khi sử dụng nhắn tin trực tuyến ###

Bạn được khuyến nghị thiết đặt **Jitsi** để yêu cầu tính riêng tư và mã hóa tin nhắn văn bản dùng [*mã hóa*](/vi/glossary#encryption) [*OTR*](/vi/glossary#OTR) bất kỳ lúc nào có thể. Để thực hiện, **chọn *Tools* > *Options*** trên trình đơn, **chọn khung *Security*** , **chọn khung con *Chat*** và **nhấn chọn *Require private messaging*** phía dưới mạn hình như dưới đây:

![](/sbox/screen/jitsi-en/24.png)

*Hình 18: Cửa sổ "Options", khung "Security", khugn con "Chat" với tùy chọn "Require private messaging" được chọn*

<a name="2.4.3"></a>
### 2.4.3 Bảo vệ mật khẩu cho mọi tài khoản với mật khẩu chủ ###

Tốt nhất không nên để Jitsi ghi nhớ mật khẩu các tài khoản của bạn. Nếu bạn chọn cách ngược lại vì lý do thuận tiện sử dụng, bất kỳ ai có thể truy cập máy tính của bạn đều có thể đăng nhập vào các tài khoản đơn giản bằng cách khởi động Jitsi. Cũng có thể xem các mật khẩu đăng nhập tài khoản trong cửa sổ *Options*. Chính vì vậy chúng tôi **hết sức khuyến nghị** bảo vệ mật khẩu của bạn bằng một **mật khẩu chủ** mạnh. Khi bạn thiết đặt mật khẩu chủ, Jitsi sẽ yêu cầu bạn nhập mật khẩu chủ này mỗi khi chương trình khởi động.


**Bước 1**. **Mở** cửa sổ *Options* bằn cách **chọn *Tools* > *Options*** trên trình đơn, **chọn khung *Security*** và khung con ***Passwords***, và **chọn *Use a master password*** để mở cửa sổ ***Master Password***.

**Bước 2**. Trong cửa sổ mới **nhập vào mật khẩu** như trong hình bên dưới. Để tìm hiểu thêm về cách tạo một mật khẩu mạnh, hãy tham khảo [***Làm thế nào để tạo và duy trì mật khẩu bảo mật***](/vi/chuong-3).

![](/sbox/screen/jitsi-en/25.png)

*Hình 19: Cửa sổ "Master Password"*

**Bước 3**. **Nhấn *OK*** để xác nhận mật khẩu và mở cửa sổ mới với thông báo ***Master Password successfully set up*** (*Mật khẩu chủ đã được thiết đặt thành công*). **Nhấn "OK"** để đóng cửa sổ và quay lại màn hình *Options* như dưới đây:

![](/sbox/screen/jitsi-en/26.png)

*Hình 20: Cửa sổ "Options", khung "Security", khung con "Passwords" với tùy chọn "Use a master password" được chọn*	

**Lưu ý**: Nút ***Change Master Password*** (*Thay đổi Mật khẩu Chủ*) cho phép bạn thay đổi mật khẩu chủ và nút ***Saved Passwords...*** (*Lưu các Mật khẩu*) cho phép bạn truy cập danh sách các mật khẩu được ghi nhớ bởi Jitsi và xóa chúng nếu cần.

