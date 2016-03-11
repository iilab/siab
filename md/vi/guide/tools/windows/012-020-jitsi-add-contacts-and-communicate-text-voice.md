

---

lang: vi
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: Jitsi - Add contacts and communicate text & voice

---

Các mục trong trang này:

- [**3.1 Thêm đối tác liên lạc (buddies) vào Jitsi**](#3.1)
- [**3.2 Nhắn tin văn bản (Nhắn tin trực tuyến) với mã hóa OTR**](#3.2)
- [**3.3 Liên lạc thoại và video với mã hóa ZRTP**](#3.3)


<a name="3.1"></a>
## 3.1 Thêm đối tác liên lạc (buddies) vào Jitsi ##

Sau khi thêm ít nhất một tài khoản vào Jitsi và đăng nhập, bạn đã sẵn sàng để thêm các đối tác liên lạc để trao đổi với họ.

To add a contact to Jitsi follow steps below:
Để thêm một đối tác vào Jitsi, hãy thêo các bước sau:

**Bước 0**. Mở cửa sổ chính Jitsi bằng cách **chọn Start > Jitsi** hoặc **nhấn đúp chuột** vào biểu tượng **Jitsi** trên màn hình.

**Bước 1**. **chọn *File* > *Add contact...*** vaà cửa sổ sau sẽ xuất hiện:

![](/sbox/screen/jitsi-en/30.png)

*Hình 1: Cửa sổ thêm đối tác liên lạc*

**Bước 2**. **Chọn** những tài khoản bạn muốn thêm đối tác liên lạc này vào (ví dụ *terance.the.tester@jit.si*). 

**Tùy chọn**: Bạn cũng có thể thêm tài khoản liên lạc vào một *nhóm* (*group*) trong các tài khoản liên lạc khác của bạn. Tuy nhiên trước hết bạn cần tạo một nhóm. Điều này được thực hiện bằng cách chọn ***File* > *Create group...*** từ trình đơn). 

**Nhập vào** tên người dùng hoặc địa chỉ thư điện tử của đối tác liên lạc vào ô ***ID or Number*** (ví dụ, *sally.the.doer@jit.si*). 

You can choose the name or nickname for the contact, which will be visible in your contacts list in the **Jitsi** main window; **type it into the *Display name*** field. 

Bạn có thể chọn tên hoặc bí danh đặt cho đối tác liên lạc, thông tin này sẽ hiển thị trong danh sách các đối tác liên lạc trong cửa sổ chính của **Jitsi**; **nhập thông tin này trong ô *Display name* - (Hiển thị tên).

**Bước 3**. **Nhấn vào** nút *Add* để đóng của sổ *Add contact* và quay trở lại của sổ chính Jitsi. Trong danh sách các đối tác liên lạc của bạn giờ xuất hiện đối tác liên lạc mới thêm vào với lưu ý "Waiting for authorisation" („Đang chờ việc xác thực") như hình bên dưới:



![](/sbox/screen/jitsi-en/31.png)

*Hình 2: Cửa sổ chính Jitsi với đối tác liên lạc mới thêm vào đang chờ xác thực*
 
**Bước 4**. Khi đối tác liên lạc của bạn đăng nhập vào tài khoản của họ (sally.the.doer@jit.si), một cửa sổ pop-up sẽ hiện lên thông báo cho cô ấy biết rằng bạn đã yêu cầu thêm cô ấy vào danh sách liên lạc của bạn:

![](/sbox/screen/jitsi-en/32.png)

*Hình 3: Cửa sổ yêu cầu xác thực một đối tác liên lạc mới*

Đối tác liên lạc của bạn có các lựa chọn: *Ignore* (*Lờ đi*), trong trường hợp này yêu cầu thêm liên lạc của bạn sẽ tiếp tục ở trạng thái chờ xác thực; *Deny* (*Từ chối*), khi đó bạn sẽ nhận được một thông tin rằng yêu cầu của bạn đã bị từ chối; và *Authorise* (*Xác nhận*), trong trường hợp này bạn sẽ nhận được thông tin rằng đối tác liên lạc đã chấp nhận yêu cầu xác nhận của bạn, và mục tài khoản đối tác liên lạc mới thêm vào này sẽ chuyển sang trạng thái hoạt động:

![](/sbox/screen/jitsi-en/33.png)

*Hình 4: Cửa sổ chính Jitsi với đối tác liên lạc mới đã xác nhận*

<a name="3.2"></a>
## 3.2  Nhắn tin văn bản (Nhắn tin trực tuyến) với mã hóa OTR

Now that you added and authorised your contact, you can Nhấn vào on their name in the contact list and initiate text conversation, voice or video calls, and desktop sharing, by choosing the relevant icon under their name:
Giờ bạn đã thêm và xác nhận một đối tác liên lạc, bạn có thể nhấn vào tên của đối tác này trong danh sách liên lạc và khởi tạo một hội thoại qua nhắn tin, thoại hay video, và chia sẻ màn hình, bằng cách chọn các biểu tượng tương ứng phía dưới tên tài khoản của họ.

![](/sbox/screen/jitsi-en/34.png)

*Hình 5: Đối tác được chọn trong cửa sổ chính Jitsi với các biểu tượng IM, thoại hay video và chia sẻ màn hình*

**Bước 1**. Bây giờ chúng ta sẽ khám phá một trong những tính năng quan trọng nhất của Jitsi: khả năng nhắn tin văn bản một cách bảo mật, mã hóa tin nhắn trao đổi với [*OTR*](/vi/glossary#OTR). OTR hoạt động tương tư như [*GPG/PGP*](/vi/glossary#PGP) được hướng dẫn trong các chương khác của bộ công cụ này. Cũng như với PGP, trước khi bạn và đối tác liên lạc có thể mã hóa phiên liên lạc của mình, cả hai phía đề cần cấu hình **Jitsi** để tạo các khóa mã hóa. Bạn có thể thực hiện điều này bằng cách trình đơn **chọn *Tools* > *Options*** và ** chọn khung *Security*** và khung con ***Chat***. Bạn sẽ thấy cửa sổ tương tự như dưới dây xuất hiện:

![](/sbox/screen/jitsi-en/35.png)

*Hình 6: Phần cửa sổ „chat“ (Nhắn tin văn bản) nơi bạn có thể sinh các khóa mã hóa cho việc nhắn tin bằng văn bản*

**Bước 2**. Tiếp theo, **nhấn vào** nút ***Generate***. Kết quả là bạn sẽ thấy hiển thị vân tay số (fingerprint) của khóa vừa sinh ra:

![](/sbox/screen/jitsi-en/36.png)

*Hình 7: Cửa sổ tùy chọn chat hiển thị vân tay số của khóa cho mã hóa OTR nhắn tin văn bản*

Một khóa sẽ được sinh ra cho mỗi tài khoản. Bạn chỉ phải thực hiện lại bước này nếu bạn thêm một tài khoản mới hoặc cài đặt Jitsi trên một máy khác mà không chuyển các khóa hiện tại sang máy đó.

Giờ bạn đã sẵn sàng để liên lạc:

**Bước 3**. **Chọn một đối tác liên lạc** trong cửa sổ chính Jitsi và **nhấn vào** biểu tượng *send message* -(*Gửi tin*)-  (biểu tượng đầu tiên từ bên trái qua, bên dưới tên đối tác liên lạc) để mở cửa sổ nhắn tin văn bản:

![](/sbox/screen/jitsi-en/37.png)

*Hình 8: Cửa sổ nhắn tin văn bản với mã hóa OTR được xác định nhưng **không** được sử dụng*

Chú ý biểu tượng *Encrypt chat with OTR* (*Mã hóa nhắn tin với OTR*), ổ khóa mở phía góc trên bên phải của cửa sổ. Biểu tượng khó nhận diện này cho bạn biết phiên nhắn tin có được mã hóa hay không. Hiện tại ổ khóa đang ở trạng thái mở (có một khoảng cách nhỏ giữa phần móc khóa và phần thân khóa!). 


**Bước 4**. **Nhấn vào biểu tượng *Encrypt chat with OTR***. Chú ý tới sự thay đổi trong cửa sổ:

![](/sbox/screen/jitsi-en/38.png)

*Hình 9: Cửa sổ nhắn tin văn bản sau khi nhấn vào biểu tượng Encrypt chat with OTR*

Hãy quan sát ổ khóa giờ đã ở trạng thái đóng. Điều này có nghĩa là bất kỳ tin nhắn nào được trao đổi giữa bạn và đối tác liên lạc đều được mã hóa. Hãy chú ý tới thông báo thể hiện rằng đây là *hội thoại riêng tư chưa được kiểm tra* và bạn nên *xác thực*  sally.the.doer@jit.si.

**Bước 5**. **Nhấn vào đường dẫn *xác thực sally.the.doer@jit.si*** để mở cửa sổ *Authenticate Buddy* (*Xác thực Đối tác liên lạc*):

![](/sbox/screen/jitsi-en/39.png)

*Hình 10: Cửa sổ Xác thực Đối tác liên lạc với các vân tay số cho bạn và đối tác liên lạc*

Lưu ý thông báo khuyến khích bạn so sánh vân tay số giữa khóa mã hóa của bạn với khóa của của đối tác liên lạc thông qua một kênh liên lạc khác (không phải kênh nhắn tin văn bản này). Khi thực hiện việc xác thực này, bạn có thể chắc chắn hơn rằng bạn đang liên lạc với chính đối tác liên lạc của mình chứ không phải với ai khác. Một lựa chọn tốt cho việc so sánh khóa mã hóa là gặp trực tiếp đối tác, hoặc thông qua gọi điện hoặc hội thoại video vì các phương thức liên lạc này cho phép xác định danh tính đối tác liên lạc một cách dễ dàng. Sau khi đã so sánh vân tay số, **chọn** tùy chọn ***Tôi đã* xác thực** vân tay số trong trình đơn xổ xuống và **Nhấn chọn *Authenticate Buddy***.


![](/sbox/screen/jitsi-en/40.png)

*Hình 11: Phần Xác thực Đối tác liên lạc (Authenticate Buddy) sau khi chọn "I have" („Tôi đã“ xác thực vân tay số) cho đối tác liên lạc của bạn*

Đóng cửa sổ *Authenticate Buddy* sẽ đưa bạn quay trở lại cửa sổ nhắn tin văn bản:

![](/sbox/screen/jitsi-en/41.png)

*Hình 12: Cửa sổ nhắn tin văn bản  với mã hóa OTR*

Hãy chú ý biểu tượng ổ khóa sẽ không còn chứa một hình tam giác nhỏ màu vàng cam với một dấu chấm than màu trắng. Điều này có nghĩa là bạn đã xác thực đối tác liên lạc của minh. **Việc xác thực này chỉ cần được thực hiện một lần đối với mỗi đối tác liên lạc.** Nếu hình tam giác với dấu chấm than màu trắng xuất hiện, điều này có nghĩa là bạn đang nhắn tin văn bản với một ai đó bạn chưa xác minh. Điều này có thể xảy ra khi đối tác của bạn chuyển sang sử dụng một thiết bị khác với một khóa mã hóa khác (một bản cài đặt Jitsi mới, hay một chương trình khác sử dụng OTR...). Trong trường hợp này bạn và đối tác liên lạc sẽ cần phải xác minh lại lẫn nhau để chắc chắn danh tính của đối tác mình liên lạc.

**Jitsi** cho phép bạn nhắn tin với nhiều hơn một đối tác cùng lúc. Mã hóa OTR sẽ chỉ hoạt động khi bạn nhắn tin với một đối tác.


<a name="3.3"></a>
## 3.3 Liên lạc thoại và video với mã hóa ZRTP ##

**Jitsi** cung cấp khả năng thoại và hội thoại với hình ảnh video được mã hóa độc lập sử dụng chuẩn mã hóa mở tên là ZRTP. Để khởi tạo phiên liên lạc bạn cần:

**Bước 1**. **Nhấn vào** tên đối tác liên lạc trong danh sách đối tác trong **Jitsi** và **nhấn vào** biểu tượng thoại (biểu tượng thứ hai từ bên trái sang, bên dưới tên tài khoản đối tác liên lạc) hoặc biểu tượng video (thứ ba)- hãy xem hình 5 phía trên. Một cửa sổ mới sẽ xuất hiện thể hiện rằng **Jitsi** đang thiết lập kết nối:

![](/sbox/screen/jitsi-en/42.png)

*Hình 13: Cửa sổ Gọi với trang thái Đổ chuông*

Đối tác của bạn sẽ thấy thông báo cuộc gọi đến:

![](/sbox/screen/jitsi-en/43.png)

*Hình 14: Thông báo Cuộc gọi đến*

**Bước 2.** Nếu đối tác của bạn **chấp nhận cuộc gọi** bạn sẽ nhận được thông báo bạn đã được kết nối:

![](/sbox/screen/jitsi-en/44.png)

*Hình 15: Cửa sổ kết nối cuộc gọi không có mã hóa ZRTP*

**Lưu ý** ổ khóa mở màu đỏ. Điều này có nghĩa là cuộc gọi của bạn chưa được mã hóa với ZRTP.

**Bước 3.** **Hãy đợi...** Chương trình của bạn và đối tác liên lạc đang thiết lập một kết nối mã hóa, điều này có thể mất một chút thời gian. Nếu thành công bạn sẽ thấy các ký tự*zrtp* xuất hiện trên nền màu vàng cam với ổ khóa ở trạng thái đóng như bên dưới. Nếu việc thiết lập kết nối mã hóa không thành công, bạn vẫn có thể nói chuyện với đối tác nhưng thông tin không được mã hóa. Bạn có thể dừng kết nối, khởi động lại **Jitsi** và thử kết nối lại để xem chương trình có thể kết nối mã hóa hay không.  ZRTP có thể không hoạt động đối với những cuộc gọi giữa các loại tài khoản của các nhà cung cấp dịch vụ khác nhau (ví dụ như giữa Google và Jit.si).

![](/sbox/screen/jitsi-en/45.png)

*Hình 16: Phần cửa sổ Cuộc gọi với mã hóa ZRTP được thiết lập nhưng chưa được xác thực*

**Bước 4**. **Quan sát** phần bên dưới các ký tự *zrtp* và ổ khóa với thông báo "So sánh với đối tác liên lạc" tiếp theo là 4 ký tự. **Hãy đọc** những ký tự này cho đối tác liên lạc của bạn và hỏi xem liệu họ có thấy đúng những ký tự này xuất hiện trên màn hình phía họ hay không. Nếu đúng vậy, có nghĩa là kết nối đã được mã hóa và không ai có thể nghe lén được. Bạn có thể **nhấn vào *Confirm***. Ô *zrtp* màu vàng cam sẽ chuyển sang màu xanh lá cây:

![](/sbox/screen/jitsi-en/46.png)

*Hình 17: Phần cửa sổ Cuộc gọi với mã hóa ZRTP được thiết lập và xác nhận*

**Bước 5**. Bạn có thể đóng phần cửa sổ xác nhận màu đen bằng cách nhấn vào dấu x màu trắng ở phía trên bên phải của ô màu đen:

![](/sbox/screen/jitsi-en/47.png)

*Hình 18: Phần cửa sổ cuộc gọi với mã hóa ZRTP được thiết lập*

**Jitsi** cho phép bạn kết nối thoại và hình ảnh video với nhiều hơn một đối tác cùng lúc. **Lưu ý** rằng với kết nối như vậy, mã hóa ZRTP có thể được thiết lập giữa phía khởi tạo cuộc gọi và các đối tác liên lạc, nhưng không phải giữa các đối tác liên lạc với nhau.

