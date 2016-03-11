

---

lang: vi
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: How to Install TrueCrypt and Create Standard Volumes

---

Các mục trong trang này: 

- [**2.0 Hướng dẫn Cài đặt TrueCrypt**](#2.0)
- [**2.1 Thông tin TrueCrypt**](#2.1)
- [**2.2 Hướng dẫn Tạo một Vùng Mã hóa Chuẩn**](#2.2)
- [**2.3 Hướng dẫn Tạo một Vùng Mã hóa Chuẩn trên thẻ nhớ USB**](#2.3)
- [**2.4 Hướng dẫn Tạo một Vùng Mã hóa Chuẩn (tiếp)**](#2.4)

-------

<a name="2.0"></a>
## 2.0 Hướng dẫn Cài đặt TrueCrypt ##

**Bước 1**. **Nhấn đúp vào** ![](/sbox/screen/truecrypt-vi/01.png); hộp thoại *Open File - Security Warning* có thể xuất hiện. Nếu vậy, hãy **nhấn** ![](/sbox/screen/truecrypt-vi/02.png) (chọn *Yes* trong cửa sổ User Control đối với MS Windows 7 hoặc 8 ) để mở cửa sổ *Thông tin Bản quyền*  **TrueCrypt**.

**Bước 2**. **Chọn** ô *I accept and agree to be bound by the license terms* để hiện nút *Accept*; **nhấn** ![](/sbox/screen/truecrypt-vi/03.png) để kích hoạt cửa sổ sau:

![](/sbox/screen/truecrypt-vi/04.png)

*Hình 1: Thuật sỹ Cài đặt ở chế độ mặc định*

- Chế độ *Install* - Cài đặt: Lựa chọn này dành cho những người dùng không cần che dấu việc sử dụng chương trình **TrueCrypt** trên máy tính.

- Chế độ *Extract* - Giải nén: Lựa chọn này dành cho người dùng muốn lưu phiên bản chạy không cần cài đặt của **TrueCrypt** trên một thẻ nhớ USB và không muốn cài đặt **TrueCrypt** vào máy tính.

**Lưu ý**: Một số tùy chọn (ví dụ, mã hóa toàn bộ phân vùng và ổ đĩa) sẽ không thể thực hiện khi sử dụng **TrueCrypt** ở chế độ *extracted* (giải nén).


**Chú ý**: Cho dù chế độ mặc định *Install* (Cài đặt) được khuyên dùng, bạn vẫn có thể sử dụng  **TrueCrypt** ở chế độ chạy không cần cài đặt bất cứ khi nào. Để tìm hiểu cách sử dụng chế độ **TrueCrypt Traveller**, hãy thao khảo [**TrueCrypt chạy không cần cài đặt**](http://securityinabox.org/vi/truecrypt_portable). 

**Bước 3**. **Nhấn** ![](/sbox/screen/truecrypt-vi/05b.png) để mở cửa sổ sau:

![](/sbox/screen/truecrypt-vi/06.png)

*Hình 2: Cửa sổ Lựa chọn Cài đặt*


**Bước 4**. **Nhấn** ![](/sbox/screen/truecrypt-vi/07.png) để mở cửa sổ *Installing* (Cài đặt) bắt đầu quá trình cài đặt **TrueCrypt** lên máy tính của bạn.

**Bước 5**. **Nhấn** ![](/sbox/screen/truecrypt-vi/08.png) để mở cửa sổ sau:

![](/sbox/screen/truecrypt-vi/09.png)

*Hình 3: Hộp thoại Xác nhận Cài đặt TrueCrypt*

**Bước 6**. **Nhấn** ![](/sbox/screen/truecrypt-vi/10.png) để truy cập trang chủ **TrueCrypt** và hoàn thành quá trình cài đặt **TrueCrypt**, sau đó **nhấn** ![](/sbox/screen/truecrypt-vi/11.png).

**Quan trọng**: Sau khi hoàn thành việc cài đặt, hãy làm theo hướng dẫn tại [*trang 1*](/vi/keepass-main) để lưu tệp ngôn ngữ tiếng việt vào thư mục cài đặt.
  
**Lưu ý**: Mọi người dùng nên tham khảo tài liệu hướng dẫn của **TrueCrypt** sau khi làm theo bản hướng dẫn này.

<a name="2.1"></a>
## 2.1 Thông tin TrueCrypt ##

**TrueCrypt** là chương trình giúp bảo mật các tệp của bạn bằng các ngăn cản các truy cập nếu không có mật khẩu hợp lệ. Nó có chức năng như một *chiếc két* điện tử, cho phép bạn cất giữ những tệp và chỉ cho phép những ai có mật khẩu hợp lệ có thể truy cập được. **TrueCrypt** giúp bạn tạo ra những *vùng mã hóa* trên máy tính nơi bạn có thể lưu trữ các tệp một cách an toàn. Khi bạn tạo hoặc lưu dữ liệu trong các vùng mã hóa này, **TrueCrypt** sẽ tự động mã hóa mọi thông tin trong vùng đó. Khi bạn mở hoặc lấy thông tin ra, chương trình sẽ tự động giải mã. Quy trình này gọi là tiến trình *mã hóa-tức thời*. 

<a name="2.2"></a>
## 2.2 Hướng dẫn Tạo một Vùng Mã hóa Chuẩn ##

**TrueCrypt** cho phép tạo hai loại vùng mã hóa: *Vùng mã hóa Ẩn* và *Vùng mã hóa Chuẩn*. Trong phần này chúng ta sẽ học cách tạo một *Vùng Mã hóa Chuẩn* để chứa tệp. 

Để bắt đầu **TrueCrypt** và tạo một *Vùng Mã hóa Chuẩn*, hãy theo các bước sau:

**Bước 1**. **Nhấn đúp vào** ![](/sbox/screen/truecrypt-vi/52.png) hoặc  **Chọn Start > Programs > TrueCrypt > TrueCrypt** để mở **TrueCrypt**.

**Quan trọng**: **Chọn: Settings &gt; Language** để mở cửa sổ lựa chọn ngôn ngữ cho giao diện chương trình như hình dưới:

![](/sbox/screen/truecrypt-vi/02a.png)

*Hình 3a: Chuyển đổi Giao diện chương trình TrueCrypt sang Tiếng Việt*


**Chọn** **Tiếng Việt** để chuyển giao diện chương trình sang Tiếng Việt:

![](/sbox/screen/truecrypt-vi/3d.png)

*Hình 3b: Chuyển đổi Giao diện chương trình TrueCrypt sang Tiếng Việt*

**Bước 2**. **Chọn** một ổ đĩa trong danh sách tại cửa sổ **TrueCrypt** như sau:

![](/sbox/screen/truecrypt-vi/12.png)

*Hình 4: Màn hình TrueCrypt*

**Bước 3**. **Nhấn** ![](/sbox/screen/truecrypt-vi/13.png)  để kích hoạt *Thuật sỹ Tạo Vùng Mã hóa* như  sau:

!![](/sbox/screen/truecrypt-vi/14.png)

*Hình 5: Cửa sổ  Thuật sỹ Tạo Vùng mã hóa TrueCrypt* 

Có ba lựa chọn mã hóa một *Vùng Mã hóa Chuẩn* trong cửa sổ *Thuật sỹ Tạo Vùng mã hóa* như *Hình 5*. Trong phần này, chúng tôi sẽ hướng dẫn cách tạo một *encrypted file container* (vùng mã hóa dạng tệp). Hãy tham khảo tài liệu [**TrueCrypt**](http://www.truecrypt.org/docs/) để biết thêm hướng dẫn về hai lựa chọn còn lại.

**Bước 4**. **Nhấn** ![](/sbox/screen/truecrypt-vi/05.png) để mở cửa sổ:

![](/sbox/screen/truecrypt-vi/15.png)

*Hình 6: Cửa sổ Loại Vùng Mã hóa*

Cửa sổ  *TrueCrypt Volume Creation Wizard Volume Type* cung cấp hai lựa chọn tạo *Vùng Mã hóa Ẩn* và * Vùng mã hóa Chuẩn*.

**Quan trọng**: Để xem *Hướng dẫn tạo Vùng mã hóa Ẩn*, xin xem phần:[**Vùng mã hóa Ẩn**](/vi/truecrypt_vungmahoaan)

**Bước 5**. **Chọn**: lựa chọn *Tập đĩa TrueCrypt Chuẩn* 

**Bước 6**. **Nhấn**: ![](/sbox/screen/truecrypt-vi/05.png) để mở cửa sổ sau:

![](/sbox/screen/truecrypt-vi/16.png)

*Hình 7: Thuật sỹ Tạo Vùng Mã hóa - Vị trí Vùng Mã hóa*

Bạn có thể xác định nơi lưu trữ Vùng nhớ Chuẩn trong quá trình thực hiện *TrueCrypt Volume Creation Wizard - Thuật sỹ Tạo Vùng Mã hóa*. Tệp này có thể được lưu trữ như những tệp bình thường khác. 

**Bước 7**. **nhập** tên tệp vào trường tên hoặc **nhấn** ![](/sbox/screen/truecrypt-vi/17.png) để mở cửa sổ sau:

![](/sbox/screen/truecrypt-vi/18.png)

*Hình 8: Cửa sổ Xác định Đường dẫn và Tên tệp*

**Lưu ý:** Một Vùng Mã hóa Chuẩn là một vùng chứa bên trong một tệp bình thường. Nghĩa là bạn có thể di chuyển, sao chép hay thậm chí xóa nó! Cần ghi nhớ tên tệp và nơi bạn lưu trữ nó. Tuy nhiên, bạn cần chọn tên tệp mới cho vùng mã hóa được tạo (xem mục [**2.3 Hướng dẫn tạo Vùng Mã hóa Chuẩn trên thẻ nhớ USB](#2.3). Trong ví dụ này, chúng ta tạo một *Vùng Mã hóa Chuẩn* tại thư mục **My Documents**, và đặt tên tệp là *My Volume* như trong *Hình 8*.

**Gợi ý**: Bạn có thể chọn tên tệp và phần mở rộng tùy ý. Ví dụ, bạn có thể đặt tên cho Vùng Mã hóa là *recipes.doc*, khiến nó trông giống như một tài liệu *Word*, hoặc *holidays.mpg* giống như một tệp phim. Đây là một cách giúp bạn che giấu *Vùng Mã hóa Chuẩn* này.

**Bước 8**. **Nhấn** ![](/sbox/screen/truecrypt-vi/19.png) để đóng cửa sổ *Xác định Đường dẫn và Tên tệp* và quay trở lại cửa sổ *Thuật sỹ Tạo Vùng Mã hóa*:

![](/sbox/screen/truecrypt-vi/20.png)

*Hình 9: Thuật sỹ Tạo Vùng Mã hóa hiển thị khung Vị trí Vùng Mã hóa*

**Bước 9**. **Nhấn** ![](/sbox/screen/truecrypt-vi/05.png) để mở *Hình 10*.

<a name="2.3"></a>
## 2.3 Hướng dẫn Tạo Vùng Mã hóa Chuẩn trên thẻ nhớ USB ##

Để tạo một *Vùng Mã hóa Chuẩn* **TrueCrypt** trên thẻ nhớ USB, hãy thực hiện từ bước 1 đến bước 3 trong phần [**2.2 Hướng dẫn Tạo Vùng Mã hóa Chuẩn**](#2.2), khi bạn mở cửa sổ *Chọn một Vùng mã hóa TrueCrypt*. Thay vì chọn thư mục **My Documents** để lưu tệp, hãy **tìm** **chọn** thẻ nhớ USB của bạn. Sau đó, **nhập** tên tệp và tạo *Vùng Mã hóa Chuẩn* ở đó. 

<a name="2.4"></a>
## 2.4 Hướng dẫn Tạo một Vùng Mã hóa Chuẩn (Tiếp) ##

Lúc này bạn đã sẵn sàng chọn một phương pháp mã hóa (hay *thuật toán* như hiển thị trên màn hình) cho *Vùng Mã hóa Chuẩn*. Phương pháp này sẽ được sử dụng để mã hóa dữ liệu lưu trữ trong Vùng Mã hóa này.

![](/sbox/screen/truecrypt-vi/21.png)

*Hình 10: Cửa sổ Thuật sỹ Tạo Vùng Mã hóa TrueCrypt  với các Tùy chọn Mã hóa*

**Lưu ý**: Bạn có thể để nguyên các lựa chọn mặc định. Những thuật toán mặc định đều có tính bảo mật cao.

**Bước 10**. **Nhấn** ![](/sbox/screen/truecrypt-vi/05.png)
 để mở cửa sổ *Thuật sỹ Tạo Vùng Mã hóa TrueCrypt* như sau:

![](/sbox/screen/truecrypt-vi/22.png)

*Hình 11: Cửa sổ Thuật sỹ Tạo Vùng Mã hóa hiển thị khung Kích thước Vùng Mã hóa*

Cửa sổ *Kích thước Vùng mã hóa* cho phép bạn xác định kích thước Vùng mã hóa. Trong ví dụ này, kích thước được chọn là 10 megabytes. Hãy cân nhắc về tài liệu và dạng tệp bạn muốn lưu trữ, cũng như kích thước của chúng, và lựa chọn một kích thước phù hợp. 

**Gợi ý**: Nếu sau này bạn muốn sao lưu Vùng mã hóa này vào một đĩa CD, nên chọn kích thước cỡ 700MB. 

**Bước 11**. **Nhập** kích thước cho vùng mã hóa vào trường tương ứng và **Nhấn** ![](/sbox/screen/truecrypt-vi/05.png) to activate the following screen:

![](/sbox/screen/truecrypt-vi/23.png)

*Hình 12: Cửa sổ Tạo Vùng Mã hóa TrueCrypt hiển thị khung Mật khẩu Mã hóa*



**Quan trọng**: : Việc chọn lựa một mật khẩu mạnh là một trong những bước quan trọng trong quá trình tạo *Vùng mã hóa Chuẩn*. Một mật khẩu mạnh sẽ bảo vệ vùng mã hóa, và cần lựa chọn mật khẩu càng mạnh càng tốt. Bạn không cần phải tự tạo mật khẩu và ghi nhớ chúng, nếu bạn sử dụng chương trình tạo mật khẩu như **KeePass**. Hãy xem [Hướng dẫn sử dụng KeePass](/vi/keepass-main) để tìm hiểu về việc tạo và lưu trữ mật khẩu bảo mật.

**Bước 12**. **Nhập** và **xác nhận** mật khẩu trong trường *Xác nhận*.

**Quan trọng**: Nút **Next** sẽ không có tác dụng chừng nào mật khẩu ở hai trường chưa khớp nhau. Nếu mật khẩu bạn chọn không đủ độ an toàn và bảo mật, bạn sẽ thấy một cảnh báo. Hãy cân nhắc thay đổi mật khẩu! Cho dù TrueCrypt vẫn hoạt động với bất kỳ mật khẩu nào do bạn chọn, dữ liệu của bạn có thể sẽ không được bảo mật. 

**Bước 13**. **Nhấn** ![](/sbox/screen/truecrypt-vi/05.png) để mở cửa sổ sau:

![](/sbox/screen/truecrypt-vi/24.png)

*Hình 13: Cửa sổ TrueCrypt Volume Creation Wizard hướng dẫn tạo Định dạng cho Vùng Mã hóa*

Trong cửa sổ tiếp theo, **TrueCrypt** sẽ tiến hành tạo *Vùng mã hóa Chuẩn*. Di chuyển con trỏ chuột một cách ngẫu nhiên trong cửa sổ *TrueCrypt Volume Creation Wizard* trong khoảng it nhất 30 giây. Bạn càng di chuyển chuột càng lâu càng tốt. Việc này giúp tăng độ phức tạp của khóa mã hóa. 


**Bước 14**. **Nhấn** ![](/sbox/screen/truecrypt-vi/25.png) để bắt đầu tiến trình tạo vùng mã hóa chuẩn.

**TrueCrypt** tiến hành tạo *Vùng Mã hóa Chuẩn*. Với những chọn lựa ở trên, một **TrueCrypt** tạo một tệp có tên là **My Volume** trong thư mục **My Documents**. Tệp này chính là một *Vùng Mã hóa Chuẩn* của **TrueCrypt**, có dung lượng 10MB, nơi bạn có thể lưu trữ các tệp dữ liệu một cách an toàn.

Sau khi một *Vùng Mã hóa Chuẩn* đã được tạo ra, một hộp thoại sẽ xuất hiện như sau: 

![](/sbox/screen/truecrypt-vi/26.png)

*Hình 14: Màn hình thông báo Vùng mã hóa TrueCrypt đã được tạo thành công*

**Bước 15**. **Nhấn** ![](/sbox/screen/truecrypt-vi/27.png) để hoàn thành việc tạo một *Vùng Mã hóa Chuẩn* **TrueCrypt** và quay về màn hình giao diện chính.

**Bước 16**. **Nhấn** ![](/sbox/screen/truecrypt-vi/28.png) để đóng *Thuật sỹ Tạo Vùng Mã hóa Chuẩn TrueCrypt*.

