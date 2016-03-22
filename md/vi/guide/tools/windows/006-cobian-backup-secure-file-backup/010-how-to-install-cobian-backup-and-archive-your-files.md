

---

lang: vi
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: How to Install Cobian Backup and Archive Your Files

---

Các mục trong trang này:

- [**2.0 Hướng dẫn Cài đặt Cobian Backup**](#2.0)
- [**2.1 Hướng dẫn Sao lưu Tệp và Thư mục**](#2.1)
- [**2.2 Hướng dẫn tạo một Tệp Sao lưu**](#2.2)
- [**2.3 Hướng dẫn Lên lịch một Tác vụ Sao lưu**](#2.3)

-------

<a name="2.0"></a>
## 2.0 Hướng dẫn Cài đặt Cobian Backup ##

**Lưu ý Cài đặt**: Trước khi tiến hành việc cài đặt, hãy kiểm tra chắc chắn bạn có cài đặt bản mới nhất **Microsoft Windows Installer** và **Microsoft.NET Framework**. 

Việc cài đặt **Cobian Backup** khá dễ dàng và nhanh chóng. Để bắt đầu việc cài đặt, hãy theo các bước sau:

**Bước 1**. **Nhấn đúp chuột vào** ![](/sbox/screen/cobian-vi/01.png); hộp thoại *Open File - Security Warning* có thể xuất hiện. Nếu vậy, **nhấn vào** ![](/sbox/screen/cobian-vi/02.png) để kích hoạt thanh tiến trình trạng thái *Extracting the resource*, tiếp đó cửa sổ sau sẽ mở ra:

![](/sbox/screen/cobian-vi/03.png)

*Hình 1: Cửa sổ chọn Ngôn ngữ*

**Bước 2**. **Nhấn vào** ![](/sbox/screen/cobian-vi/04.png) để mở cửa sổ thông tin bản quyền *Please read and accept the license agreement*; **Nhấn chọn** ô *I accept*, sau đó **nhấn vào** ![](/sbox/screen/cobian-vi/04.png), cửa sổ sau sẽ xuất hiện:

![](/sbox/screen/cobian-vi/05.png)

*Hình 2: Cửa sổ chọn thư mục cài đặt*

**Bước 3**. **Nhấn vào** ![](/sbox/screen/cobian-vi/04.png) để mở cửa sổ sau:

![](/sbox/screen/cobian-vi/06.png)

*Hình 3: Cửa sổ Loại Cài đặt và Tùy chọn Dịch vụ*

**Bước 4**. **Chọn** ô *Use Local System account* trong khung *Service options*, màn hình của bạn có dạng như trong *Hình 3* phía trên. 

**Quan trọng**: Tùy chọn này đảm bảo rằng **Cobian Backup** sẽ luôn hoạt động ở chế độ nền,  việc sao lưu sẽ được thực hiện như đã lên lịch.

**Bước 5**. **Nhấn vào** ![](/sbox/screen/cobian-vi/04.png), thông báo sau sẽ xuất hiện:

![](/sbox/screen/cobian-vi/07.png)

*Hình 4: Thông báo Cobian Backup 10 xuất hiện* 

**Bước 6**. **Nhấn vào** ![](/sbox/screen/cobian-vi/08.png) để mở cửa sổ cài đặt tiếp theo và **nhấn vào** ![](/sbox/screen/cobian-vi/04.png) để tiếp tục tiến trình cài đặt.

**Bước 7**. **Nhấn vào** ![](/sbox/screen/cobian-vi/09.png) để hoàn thành quá trình cài đặt. Sau khi hoàn thành, biêu tượng **Cobian Backup** sẽ xuất hiện trên **Khay Hệ thống** như sau: ![](/sbox/screen/cobian-vi/10.png)

<a name="2.1"></a>
## 2.1 Hướng dẫn Sao lưu Tệp và Thư mục ##

Trong phần này bạn sẽ tìm hiểu cách thực hiện việc sao lưu đơn giản các tệp hay thư mục. **Cobian Backup** sử dụng một *tác vụ sao lưu* được thiết đặt để gồm một nhóm các tệp hay thư mục. Một tác vụ sao lưu có thể được thiết đặt để tự kích hoạt vào một giờ hay ngày định trước.

Để tạo một tác vụ sao lưu mới, hãy thực hiện theo các bước sau:

**Bước 1**. **Nhấn vào** ![](/sbox/screen/cobian-vi/11.png) để tạo một tác vụ sao lưu mới, và kích hoạt cửa sổ *New task* như sau:

![](/sbox/screen/cobian-vi/12.png)

*Hình 2: Khung New task*

Phần bên trái chứa các khung để thiết đặt các tùy chọn và thông số sao lưu khác nhau được hiển thị trong khung bên phải. Tất cả các tùy chọn trong khung **General** được liệt kê dưới đây:

### 2.1.1 Mô tả các Tùy chọn ###


*Task Name*: Đặt tên cho tác vụ sao lưu mới. Hãy chọn một tên giúp xác định tiến trình sao lưu. Ví dụ, nếu đây là quá trình sao lưu các tệp video, bạn có thể đặt tên là *Sao lưu Video*.

*Diabled*: Hãy *để trống* hộp chọn này. 

**Cảnh báo**: nếu bạn chọn hộp chọn này, nó sẽ vô hiệu các tùy chọn còn lại và nó sẽ dừng tác vụ sao lưu.

*Include Subdirectories*: Tùy chọn này cho phép bạn bao gồm cả  những thư mục con của thư mục được chọn để sao lưu. Lựa chọn này đem lại hiệu quả cho việc sao lưu một lượng lớn các tệp. Ví dụ: Nếu bạn chọn thư mục *My Documents* và chọn hộp chọn này, thì tất cả các tệp và thư mục con bên trong thư mục *My Documents* sẽ được thực hiện sao lưu.

*Create separated backups using timestamps*: Với lựa chọn này, sau khi quá trình sao lưu hoàn thành, giờ và ngày tháng sẽ được sử dụng để tạo tên của tệp sao lưu. Điều này có thể giúp bạn dễ dàng xác định được thời điểm tệp được sao lưu.

*Use file attribute logic*: Lựa chọn này chỉ có tác dụng khi bạn thực hiện việc sao lưu thêm hoặc sao lưu những thay đổi (xem phần dưới). Thuộc tính tệp sẽ chứa các thông tin về tệp đó.

**Lưu ý**: Các tùy chọn sao chỉ có trong phiên bản dành cho hệ điều hành **Windows OS**  từ **Windows XP** trở đi.

*Use Volume Shadow Copy*: Tùy chọn này cho phép bạn sao lưu những tệp bị khóa.

**Cobian Backup** kiểm tra thông tin trên để xác định xem có sự thay đổi nào ở tệp nguồn kể từ lần sao lưu gần đây nhất không. Nếu bạn sử dụng phương pháp sao lưu thêm (Incremental) hay sao lưu những thay đổi (Differential) thì tệp này sẽ được cập nhật.

**Lưu ý** ‎: Bạn chỉ có thể thực hiện việc sao lưu toàn bộ hay ‘dummy backup’ nếu bạn *bỏ lựa chọn* này (lựa chọn sao lưu ‘dummy backup’ sẽ đước giải thích bên dưới).


### 2.1.2 Backup type Descriptions ###

*Full*: *Mọi tệp* ở trong địa chỉ nguồn được chọn để sao lưu sẽ được sao chép vào thư mục sao lưu. Nếu bạn chọn *Create separated backups using timestamp*, bạn sẽ có một số bản sao của cùng một nguồn (được xác định bằng ngày và giờ thực hiện việc sao lưu ghi trên tên thư mục). Còn không thì **Cobian Backup** sẽ ghi đè lên tệp cũ (nếu có).

*Incremental*: Chương trình sẽ kiểu tra xem các tệp nguồn có sự thay đổi gì so với lần sao lưu trước đó không. Nếu không có sự thay đổi, tệp đó sẽ được bỏ qua giúp giảm thời gian thực hiện việc sao lưu. Ô *Use file attributes logic* cần được chọn để thực hiện phương pháp sao lưu này.

*Archive Bit*: Đây là thông tin về kích thước, ngày tạo và thay đổi của tệp. Nó cho phép **Cobian Backup** xác định xem tệp này có bị thay đổi hay không từ lần sao lưu trước đó.

*Differential*: Chương trình sẽ kiểm tra xem tệp nguồn có thay đổi gì không từ lần sao lưu *toàn bộ* trước đó. Nếu không cần phải sao chép tệp, nó sẽ bỏ qua nhằm tiết kiệm thời gian. Nếu bạn đã thực hiện việc sao lưu toàn bộ với một tập hợp các tệp nhất định, thì bạn có thể tiếp tục thực hiện sao lưu những tệp đó, sử dụng phương pháp sao lưu Differential.

*Dummy task*: Bạn có thể sử dụng phương pháp này để kích hoạt hay tắt các chương trình tại những thời điểm nhất định. Đây là một tùy chọn nâng cao và không có liên quan tới những phương pháp sao lưu cơ bản.

**Bước 2**. **Nhấn vào** ![](/sbox/screen/cobian-vi/13.png) để xác nhận tùy chọn tìm kiếm và thông số thiết đặt cho tác vụ sao lưu.

<a name="2.2"></a>
## 2.2 Hướng dẫn tạo một Tệp Sao lưu ##

Để tạo một tệp sao lưu, hãy thực hiện các bước sau:

**Bước 1**. **Nhấn vào** ![](/sbox/screen/cobian-vi/14.png) ở phía khung bên trái cửa sổ *New task* để mở cửa sổ *trống* dưới đây:

![](/sbox/screen/cobian-vi/15.png)

*Hình 3: Cửa sổ New task (MyBackup) hiển thị các khung Source và Destination*

**Bước 2**. **Chọn** các tệp bạn muốn sao lưu. (trong *Hình 3* phía trên, thư mục *My Documents* được chọn.)

**Bước 3**. **Nhấn vào** ![](/sbox/screen/cobian-vi/16.png) trong khung *Source* để mở trình đơn sau:

![](/sbox/screen/cobian-vi/17.png)

*Hình 4: Khung Source - nút Add (Thêm)*

**Bước 4**. **Chọn** *Directory* nếu bạn muốn sao lưu toàn bộ thư mục và chọn *Files* đẻ sao lưu từng tệp riêng lẻ. Để tự xác định các tệp hay thư mục cần sao lưu, hãy chọn *Manually*, và nhập vào đường dẫn tệp hay thư mục để tiến hành sao lưu. 

**Lưu ý**: Bạn có thể thêm số lượng tệp hay thư mục tùy ý. Nếu bạn muốn sao lưu các tệp trên *máy chủ FTP*, hãy chọn *FTP site* (bạn sẽ cần có thông tin đăng nhập vào máy chủ).

Sau khi đã chọn xong tệp và các thư mục, chúng sẽ xuất hiện trong cửa sổ *Source*. Bạn có thể xem trong *Hình 3*, thư mục *My Documents* nằm trong cửa sổ này nghĩa là nó sẽ được sao lưu.

Cửa sổ Đích (Destination pane) xác định nơi bản sao lưu sẽ được lưu trữ.

**Bước 5**. **Nhấn vào** ![](/sbox/screen/cobian-vi/16.png) trong *khung Destination* để mở trình đơn sau:

![](/sbox/screen/cobian-vi/18.png)

*Hình 5: Khung Destination – Lựa chọn thêm tài liệu*

**Bước 6**. **Chọn** *Directory* để mở cửa sổ quản lý thư mục nơi bạn chọn thư mục đích để lưu tệp sao lưu.

**Chú ý**: Nếu bạn muốn tạo nhiều bản sao lưu, bạn có thể xác định một số thư mục ở đây. Nếu bạn chọn *Manual*, bạn phải nhập đường dẫn đầy đủ đến thư mục bạn muốn lưu bản sao lưu. Để lưu bản sao lưu trên máy chủ Internet, **chọn** *FTP site* (bạn sẽ cần thông tin đăng nhập máy chủ).

Màn hình của bạn giờ có đầy đủ thông tin giống như trong ví dụ với các tệp và/hoặc thư mục trong vùng nguồn và đích. Tuy nhiên, chưa nhấn nút  *OK* vội! Bạn cần đặt lịch cho tác vụ sao lưu này.

<a name="2.3"></a>
## 2.3 Hướng dẫn Lập lịch cho Tác vụ Sao lưu ##

Để thực hiện việc sao lưu tự động, bạn cần điền thông tin trong mục *Schedule*. Mục này cho phép bạn xác định thời điểm bạn muốn hệ thống thực hiện việc sao lưu.

Để thiết đặt những lựa chọn này, thực hiện các bước sau:

**Bước 1**. **Chọn** ![](/sbox/screen/cobian-vi/19.png) cửa sổ trình đơn bên trái, mở màn hình như sau:

![](/sbox/screen/cobian-vi/20.png)

*Hình 6: Cửa sổ Thuộc tính của myBackup hiển thị khung Đặt lịch*

Lựa chọn các kiểu đặt lịch (*Schedule type*) được liệt kê trong trình đơn xổ xuống, được mô tả như sau:

*Once*: Việc sao lưu sẽ được thực hiện một lần duy nhất tại thời điểm xác định tại ô *Date/Time*.

*Daily*: Việc sao lưu sẽ được thực hiện hàng ngày tại thời điểm xác định tại ô Date/Time.

*Weekly*: Việc sao lưu sẽ được thực hiện vào ngày được chọn trong tuần. Trong ví dụ trên là ngày thứ Sáu. Bạn có thể chọn một ngày bất kỳ. Việc sao lưu sẽ thực hiện vào ngày được chọn hàng tuần, vào thời điểm được xác định tại ô *Date/Time*.

*Yearly*: Việc sao lưu được thực hiện vào những ngày được nhập trong ổ *day of the month* (ngày trong tháng), trong tháng được chọn và vào thời điểm được xác định tại ô *Date/Time*.

*Timer*:  Việc sao lưu sẽ được lặp lại sau khoảng thời gian xác định trong ô *Timer* tại ô *Date/Time*.

*Manually*: Bạn có thể tự kích hoạt việc sao lưu từ cửa sổ chương trình.

**Bước 2**. **Nhấn vào** ![](/sbox/screen/cobian-vi/13.png) để xác nhận các lựa chọn và thiết đặt cho việc đặt lịch như sau:

![](/sbox/screen/cobian-vi/21.png)

*Hình 7: Cửa sổ New task hiển thị khung Thiết đặt Đặt lịch*

Đặt lịch sao lưu chính là bước cuối cùng. Bây giờ chương trình sẽ sao lưu các thư mục được chọn lựa theo lịch mà bạn thiết đặt.

