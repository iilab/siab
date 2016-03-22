

---

lang: vi
community: guide
type: tools
legacy: True
child: True
os: android
weight: 1
depth: 3
title: KeePassDroid - Basic Usage

---

### 2. Hướng dẫn Cài đặt và Sử dụng KeePassDroid

Danh sách các phần:

[**2.0 Hướng dẫn Cài đặt KeePassDroid**](#2.0)

[**2.1 Hướng dẫn Taok một Cơ sở Dữ liệu Mật khẩu Mới**](#2.1)

[**2.2 Hướng dẫn Thêm một Nhóm và một Mục vào**](#2.2)

[**2.3 Hướng dẫn Sửa đổi một Mục vào**](#2.3)

[**2.4 Hướng dẫn Sinh Mật khẩu Ngẫu nhiên**](#2.4)

[**2.5 Hướng dẫn Khóa cơ sở dữ liệu KeePassDroid**](#2.5)

[**2.6 Hướng dẫn Tạo một tệp Sao lưu Cơ sở dữ liệu Mật khẩu**](#2.6)

[**2.7 Hướng dẫn Khởi tạo lại Mật khẩu Chủ**](#2.7)

-------

<a name="2.0"></a>
## 2.0 Hướng dẫn Cài đặt KeePassDroid ##

**Bước 1**. Tải về ứng dụng từ kho ứng dụng [**F-Droid**](http://f-droid.org/)

![](/sbox/screen/keepassdroid-vi/01.png)

*Hình 1: Các phiên bản KeyPassDroid.*

**Bước 2**. Sau khi tải về, nhấn vào **Package installer** (Gói Cài đặt) và chọn  **Install** (Cài đặt)

![](/sbox/screen/keepassdroid-vi/02.png)

*Hình 2: Quyền truy cập cần thiết cho KeyPassDroid.*

**Bước 3**. Nhấn **Open** (Mở) như trong hình bên dưới để kích hoạt **KeePassDroid**

![](/sbox/screen/keepassdroid-vi/03.png)

*Hình 3: Màn hình ứng dụng được cài đặt.*

### Để sử dụng ứng dụng:

<a name="2.1"></a>
## 2.1 Hướng dẫn Tạo một Cơ sở Dữ liệu Mật khẩu Mới ##

Trong các phần tiếp theo bạn sẽ được hướng dẫn cách tạo một mật khẩu chủ, lưu cơ sở dữ liệu mật khẩu vừa tạo, sinh một mật khẩu ngẫu nhiên cho một chương trình riêng và tạo bản sao lưu cho cơ sở dữ liệu mật khẩu.
Để mở **KeePassDroid** bạn cần nhấn chạm vào biểu tượng ứng dụng.

![](/sites/securityinabox.org/files/u12/keepass.gif)

Tạo một cơ sở dữ liệu mật khẩu bảo mật mới yêu cầu hai bước:

Bạn phải nghĩ ra một mật khẩu chủ riêng, mạnh sử dụng để khóa và mở khóa cơ sở dữ liệu mật khẩu này. Sau đó bạn cần lưu cơ sở mật khẩu vừa tạo ra.

Để tạo một cơ sở dữ liệu mật khẩu mới hãy theo các bước sau:

**Bước 1**. Nhấn chọn **Create** (Tạo mới)

![](/sbox/screen/keepassdroid-vi/04.png)

*Hình 4: Cửa sổ mở/tạo cơ sở dữ liệu mật khẩu.* 

Cửa sổ *Enter database password* (Nhập mật khẩu cơ sở dữ liệu) sẽ xuất hiện như sau:

![](/sbox/screen/keepassdroid-vi/05.png)

*Hình 5: Cửa sổ nhập mật khẩu cho cơ sở dữ liệu.*

**Bước 2**. **Nhập** vào mật khẩu chủ bạn đã chuẩn bị trước đó vào trường *password* (mật khẩu) và trường *confirm password* (xác nhận mật khẩu) như trong hình dưới đây:

![](/sbox/screen/keepassdroid-vi/06.png)

*Hình 6: Nhập mật khẩu.*

**Gợi ý**: Hãy chắc chắn bạn tạo một mật khẩu chủ đủ mạnh, hãy tham khảo chương [**3. Hướng dẫn tạo và duy trì mật khẩu bảo mật**](/vi/chuong_3_1) để có thêm hướng dẫn.

**Bước 3**. Nhấn **OK** để kích hoạt cửa sổ sau

![](/sbox/screen/keepassdroid-vi/07.png)

*Hình 7: Cửa sổ chính KeePassDroid.*

Xin chúc mừng! Bạn đã tạo thành công một cơ sở dữ liệu mật khẩu bảo mật. Giờ bạn có thể bắt đầu sử dụng cơ sở dữ liệu này để lưu trữ các mật khẩu hiện có cũng như trong tương lai.

**Lưu ý**: Bạn cũng có thể chép tệp cơ sở dữ liệu KeePass từ máy tính vào thiết bị Android và mở tệp này với **KeePassDroid**.

<a name="2.2"></a>
## 2.2. Hướng dẫn Thêm một Nhóm và một Đề mục ##

**KeePassDroid** lưu trữ các đề mục mật khẩu trong các nhóm để đảm bảo thông tin được tổ chức. Các nhóm mặc định được tạo sẵn gồm **Email** và **Internet** tuy nhiên bạn cũng có thể tạo các nhóm riêng theo ý mình bằng cách nhấn vào **Add group** (Thêm nhóm) và nhập tên nhóm sau đó ấn **OK** để kích hoạt cửa sổ sau: 

![](/sbox/screen/keepassdroid-vi/09.png) ![](/sbox/screen/keepassdroid-vi/10.png)

*Hình 8 và 9: Thêm một nhóm mới.*

Cửa sổ **Add entry** (Thêm đề mục) cho phép bạn thêm thông tin về tài khoản, mật khẩu và các thông tin quan trọng khác vào cơ sở dữ liệu vừa tạo. Trong ví dụ dưới đây, bạn sẽ thêm các đề mục để lưu trữ các mật khẩu và tên truy cập cho các tài khoản của các trang web và hòm thư điện tử khác nhau. 
**Bước 1**. Nhấn vào **Add entry** (Thêm đề mục) để kích hoạt cửa sổ **Add entry** như dưới đây:

![](/sbox/screen/keepassdroid-vi/11.png) ![](/sbox/screen/keepassdroid-vi/12.png)

*Hình 10 và 11: Thêm một đề mục mật khẩu mới.*

**Lưu ý**: Cửa sổ Add Entry hiển thị những trường thông tin lưu trữ. Không có trường nào là bắt buộc; thông tin lưu ở đây chủ yếu giúp tạo thuận lợi cho bạn. Trong nhiều trường hợp, các thông tin này rất hữu ích khi bạn cần tìm một đề mục cụ thể.

Dưới đây là giải thích ngắn gọn cho các trường thông tin khác nhau : 

**Name** (Tên): Một tên dùng để miêu tả một đề mục mật khẩu. Ví dụ: Mật khẩu Gmail

**Username** (tên đăng nhập): Là tên đăng nhập liên quan cho đề mục mật khẩu này. Ví dụ: securitybox@gmail.com

**URL**: Địa chỉ đường dẫn Internet liên quan đề mục mật khẩu này. Ví dụ: https://mail.google.com

**Password** (Mật khẩu): Tính năng này sinh ra một mật khẩu ngẫu nhiên khi cửa sổ Add Entry được kích hoạt. Bạn có thể sử dụng tính năng này khi bạn muốn thay đổi mật khẩu hiện tại bằng một mật khẩu sinh ra bởi KeePass. Vì KeePass sẽ luôn ghi nhớ các mật khẩu này cho bạn, bạn sẽ thậm chí không cần phải ghi nhớ các mật khẩu này. Một mật khẩu được sinh một cahs ngẫu nhiên được coi là mật khẩu mạnh (đúng vậy, sẽ khó để cho một kẻ xâm nhập tìm cách đoán hay phá mật khẩu).

Việc sinh một mật khẩu ngẫu nhiên theo yêu cầu sẽ được hướng dẫn trong phần tiếp theo. Tât nhiên bạn có thể thay mật khẩu mặc định bằng mật khẩu của bạn. Ví dụ, nếu bạn tạo một đề mục cho tài khoản đã tồn tại bạn có thể nhập mật khẩu đã có này vào trường mật khẩu này.

**Confirm passwords** (Xác nhận mật khẩu): Bạn nhập lại mật khẩu để xác nhận.

**Comments** (Chú thích): Trường này là nơi bạn có thể nhập vào các thông tin miêu tả hay thông tin chung về tài khoản hoặc trang web đề mục này chứa thông tin. Ví dụ: Thiết lập Máy chủ Thư: *POP3 SSL, pop.gmail.com, Port 995; SMTP TLS, smtp.gmail.com, Port: 465*

**Lưu ý**: Việc tạo hay sửa đổi các đề mục mật khẩu sẽ không làm thay đổi mật khẩu thực tế của bạn! Hãy tưởng tượng KeePass như là một cuốn sổ liên lạc điện tử ghi các mật khẩu của bạn. Chương trình chỉ lưu những gì bạn ghi vào đó, không có gì hơn.

**Bước 2**. Nhấn vào **save** (lưu) để lưu những thay đổi của cửa sổ Add entry.

Đề mục mới sẽ xuất hiện trong nhóm.

![](/sbox/screen/keepassdroid-vi/13.png)

*Hình 12: Một đề mục mới được thêm vào trong một nhóm vừa tạo.*

<a name="2.3"></a>
## 2.3 Hướng dẫn Sửa đổi một Đề mục ##

Bạn có thể sửa đổi một đề mục đã tồn tại trong **KeePass** bất cứ khi nào bạn muốn. Bạn có thể đổi mật khẩu (một thói quen bảo mật tốt khi thay đổi mật khẩu mỗi ba hoặc sáu tháng), hoặc các thông tin khác lưu trong đề mục mật khẩu
Để sửa đổi một đề mục, hãy thực hiện các bước sau:

**Bước 1**. **Chọn** *Group* tương ứng để kích hoạt các đề mục trong đó.

![](/sbox/screen/keepassdroid-vi/14.png)

*Hình 13: Danh sách các nhóm.*

**Bước 2**. **Chọn** đề mục tương ứng, sau đó **nhấn** chọn đề mục xác định để kích hoạt cửa sổ sau: 

![](/sbox/screen/keepassdroid-vi/15.png)

*Hình 14: Xem một đề mục.*

**Bước 3**. **Nhấn** vào **Edit** (Sửa đổi), Giờ bạn có thể bắt đầu sửa đổi các thông tin trong cửa sổ này. Khi bạn hoàn thành **Nhấn** vào **save** (lưu) để lưu các thay đổi, bao gồm cả mật khẩu.

![](/sbox/screen/keepassdroid-vi/16.png)

*Hình 15: Chỉnh sửa thông tin.*

Để thay đổi một mật khẩu hiện tại (được bạn tạo ra trước đó) bằng một mật khẩu tạo ra và được chúng tôi khuyến nghị dùng, bởi **KeePassDroid**, hãy xem phần tiếp theo.

<a name="2.4"></a>
## 2.4 Hướng dẫn Sinh Mật khẩu Ngẫu nhiên ##

Các mật khẩu dài, ngẫu nhiên được coi là mật khẩu mạnh trong lĩnh vực an ninh bảo mật số. Sự ngẫu nhiên dựa trên các thuật toán và không dễ dàng bị ‘đoán’ bởi những đối tượng tìm cách tấn công tài khoản của bạn. KeePass cung cấp Cơ chế Sinh Mật khẩu để giúp bạn thực hiện công việc này. Như bạn đã thấy ở phía trên, một mật khẩu ngẫu nhiên được tự động sinh ra khi bạn tạo một đề mục mới. Phần này sẽ hướng dẫn bạn tự sinh một mật khẩu theo yêu cầu của mình.
**Lưu ý**: *Cơ chế Sinh Mật khẩu* có thể được kích hoạt trong cửa sổ *Add Entry* (Thêm đề mục) và *Edit Entry* (Sửa Đề mục).

![](/sbox/screen/keepassdroid-vi/17.png)

*Hình 16: Thông tin đề mục mật khẩu.*

**Bước 1**. **Nhấn** nút ![](/sbox/screen/keepassdroid-vi/18.png) trên cửa sổ Add Entry hoặc Edit Entry, để kích hoạt cửa sổ Sinh Mật khẩu như sau:

![](/sbox/screen/keepassdroid-vi/19.png)

*Hình 17: Các tùy chọn sinh mật khẩu.*

Cửa sổ Password Generator (Sinh Mật khẩu) hiển thị một số tùy chọn để tạo mật khẩu. Bạn có thể xác định độ dài mong muốn cho mật khẩu, tập hợp các ký tự sử dụng và nhiều tùy chọn khác. Với mục đích của chúng tôi, chúng tôi sẽ chọn những tùy chọn sau làm ví dụ: 

- **Length** (Độ dài) là 16 ký tự
- **Chọn** Upper-case Letter (Chữ hoa)
- **Chọn** Lower-case Letter (Chữ thường)
- **Chọn** Digits (Số)
- **Chọn** Minus (Dấu)
- **Chọn** Ngoặc móc
- **Chọn** Gạch chân 

![](/sbox/screen/keepassdroid-vi/19.png)

*Hình 18: Các tùy chọn sinh mật khẩu.*

**Bước 2**. **Nhấn** ![](/sbox/screen/keepassdroid-vi/20.png) để bắt đầu tiến trình. Khi hoàn thành, **KeePassDroid** sẽ hiển thị mật khẩu đã sinh cho bạn.

![](/sbox/screen/keepassdroid-vi/21.png)

*Hình 19: Một mật khẩu ngẫu nhiên được tạo ra.*

**Bước 3**. **Nhấn** **Accept** (Chấp nhận) để kích hoạt màn hình sau:

![](/sbox/screen/keepassdroid-vi/22.png)

*Hình 20: Thông tin đề mục.*

**Lưu ý**: Bạn có thể xem mật khẩu vừa được tạo bằng cách nhấn vào (Screenshot) từ trình đơn. Tuy nhiên, điều này có thể gây ra nguy cơ bảo mật như đã thảo luận phía trên. Trong thực tế, bạn sẽ không cần thiết phải xem mật khẩu được tạo ra. Chúng tôi sẽ giải thích rõ hơn về điều này trong phần [**3.0 Sử dụng KeePass Passwords**](/vi/keepass_passwords).

**Bước 4**. **Nhấn** vào **Save** (Lưu) để chấp nhận mật khẩu và quay trở lại cửa sổ *Entry* (Đề mục) như trong hình sau:

![](/sbox/screen/keepassdroid-vi/23.png)

*Hình 21: Cửa sổ Đề mục.*

<a name="2.5"></a>
## 2.5 Hướng dẫn Khóa cơ sở dữ liệu KeePassDroid ##

**Bước 1**. **Nhấn** vào nút **Trình đơn** để khích hoạt cửa sổ sau:

![](/sbox/screen/keepassdroid-vi/24.png)

*Hình 22: Trình đơn các tùy chọn.*

**Bước 2**. **Nhấn** chọn **Lock Database** (Khóa Cơ sở Dữ liệu) để đóng cửa sổ giao diện KeePassDroid như dưới đây:

![](/sbox/screen/keepassdroid-vi/25.png)

*Hình 23: Cơ sở dữ liệu bị khóa.*

Bạn sẽ cần nhập lại mật khẩu để truy cập cơ sở dữ liệu **KeePassDroid**.

<a name="2.6"></a>
## 2.6 Hướng dẫn Tạo Sao lưu tệp Cơ sở Dữ liệu Mật khẩu ##

Tệp cơ sở dữ liệu **KeePassDroid** trên điện thoại Android sẽ được xác định với thành phần mở rộng .kdb. Bạn có thể sao chép tệp này sang máy tính của bạn hoặc vào thẻ nhớ USB. Không ai có thể mở được cơ sở dữ liệu này nếu không có mật khẩu chủ.

**Lưu ý**: Để mở cơ sở dữ liệu **KeePassDroid** được chép vào từ thiết bị Android sang máy tính, bạn cần chắc chắn rằng chương trình KeePass được cài đặt trên máy tính hoặc có phiên bản chạy không cần cài đặt trên thẻ nhớ USB.

Xin hãy tham khảo chương sau để có thêm thông tin [**Portable KeePass**](https://securityinabox.org/vi/keepass_portable)

<a name="2.7"></a>
## 2.7 Hướng dẫn Thay đổi Mật khẩu Chủ ##

Bạn có thể thay đổi Mật khẩu Chủ bất kỳ khi nào. Việc này có thể được thực hiện khi bạn mở cơ sở dữ liệu mật khẩu.

**Bước 1**. **Chọn cở sở dữ liệu > Chọn Menu (Trình đơn)** để kích hoạt cửa sổ sau:

![](/sbox/screen/keepassdroid-vi/26.png)

*Hình 24: Trình đơn các tùy chọn.*

**Bước 2**. **Nhấn** vào **Change Master key** (Thay đổi Mật khẩu chủ) để khích hoạt cửa sổ sau:

![](/sbox/screen/keepassdroid-vi/27.png)

*Hình 25: Nhập một mật khẩu mới.*

**Bước 3**. Nhập mật khẩu vào trường **Password** (Mật khẩu) và trường **Confirm Password** (Xác nhận Mật khẩu), sau đó **Nhấn** OK.

![](/sbox/screen/keepassdroid-vi/28.png)

*Hình 26: Nhập một mật khẩu mới.*

## 3.0 Sử dụng KeePassDroid Passwords ##

**Xóa Bộ nhớ Đệm Bàn phím khi quá hạn**

Với thực tế là một mật khẩu bảo mật rất khó ghi nhớ, **KeePassDroid**
cho phép bạn chép mật khẩu từ cơ sở dữ liệu và dán mật khẩu này vào tài khoản hay trang web cần nhập.
. 
Để đảm bảo bảo mật tốt hơn, bạn có tùy chọn lưu mật khẩu sao chép trong bộ nhớ bàn phím trong khoảng thời gian **30 giây**, **1 phút**, **5 phút**, vì vậy sẽ tiết kiệm thời gian khi mở tài khoản hay trang web sẵn sàng để bạn có thể dán mật khẩu vào theo yêu cầu
. 

**Lưu ý**: bạn cũng có tùy chọn để không bao giờ lưu mật khẩu sao chép vào bộ nhớ bàn phím. 

Bạn có thể thấy các tùy chọn này trong cửa sổ dưới đây bằng cách:

**Menu** (Trình đơn) > **Settings** (Thiết đặt) > **Application** (Ứng dụng)> **Clipboard timeout (Giới hạn thời gian Bộ nhớ bàn phím**

![](/sbox/screen/keepassdroid-vi/29.png)

*Hình 27: Các tùy chọn giới hạn thời gian lưu trữ bộ nhớ bàn phím.*

**Sử dụng KeePassDroid**

**Bước 1**. Nhấn vào **Menu** (Trình đơn) trong đề mục mật khẩu yêu cầu để kích hoạt cửa sổ:

![](/sbox/screen/keepassdroid-vi/30.png)

*Hình 28: Các tùy chọn mật khẩu.*

**Bước 2**. **Select Copy Password** (Chọn Chép Mật khẩu) như sau:

![](/sbox/screen/keepassdroid-vi/31.png)



**Bước 3**. Chuyển tới tài khoản hoặc trang web tương ứng và **dán** mật khẩu vào trường tương ứng bằng cách nhấn chạm và giữ tại trường tương ứng và chọn **Paste** (Dán) để dán thông tin:

![](/sbox/screen/keepassdroid-vi/32.png)

*Hình 29: Các tùy chọn thao tác ký tự.*

**Lưu ý**: Bằng việc sử dụng **KeePassDroid** trong mọi trường hợp, bạn sẽ thực tế không bao giờ cần xem hoặc biết mật khẩu của mình như thế nào. Tính năng copy/paste (chép/dán) sẽ đảm nhận việc sao chép mật khẩu từ cơ sở dữ liệu vào cửa sổ nhập mật khẩu tương ứng. Nếu bạn sử dụng tính năng *Random Generator* (Cơ chế Sinh Ngẫu nhiên) sau đó dùng mật khẩu này cho quá trình đăng ký một tài khoản thư điện tử mới, bạn sẽ sử dụng một mật khẩu mà bạn sẽ không bao giờ cần biết về mật khẩu này. Và điều này hoạt động tốt !

**Khóa cơ sở dữ liệu khi quá thời gian**

Bạn cũng có một tùy chọn khóa cơ sở dữ liệu mật khẩu khi ứng dụng không có hoạt động trong một khoảng thời gian nhất định. Bạn có thể thực hiện điều này bằng cách:

**Menu** (Trình đơn)> **Settings**(Thiết đặt) > **Application**(Ứng dụng) **Nhấn** vào **Application timeout** (Ứng dụng quá hạn thời gian) để mở cửa sổ sau:


![](/sbox/screen/keepassdroid-vi/33.png)

*Hình 30: Các tùy chọn giới hạn thời gian ứng dụng.*

**Chọn** khoảng thời gian bạn muốn đóng cơ sở dữ liệu.


