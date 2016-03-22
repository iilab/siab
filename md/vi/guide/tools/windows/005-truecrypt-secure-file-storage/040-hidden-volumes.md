

---

lang: vi
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 4
depth: 3
title: Hidden Volumes

---

Các mục trong trang này:

- [**5.0 Giới thiệu Vùng Mã hóa Ẩn**](#5.0)
- [**5.1 Hướng dẫn Tạo Vùng Mã hóa Ẩn**](#5.1)
- [**5.2 Hướng dẫn Gắn Vùng Mã hóa Ẩn**](#5.2)
- [**5.3 Những Gợi ý Hướng dẫn Sử dụng Tính năng Ẩn một cách bảo mật**](#5.3)

-------

<a name="5.0"></a>
## 5.0 Giới thiệu Vùng Mã hóa Ẩn ##

Trong **TrueCrypt**, một *Vùng mã hóa Ẩn* được tạo ngay bên trong *Vùng mã hóa Chuẩn*, nhưng sự tồn tại của nó được ẩn đi. Ngay cả khi bạn gắn hoặc mở *Vùng mã hóa Chuẩn*, bạn cũng không thể biết được sự tồn tại của vùng mã hóa ẩn này. Nếu bạn bị cưỡng bức phải tiết lộ mật khẩu và tệp *Vùng mã hóa Chuẩn*, dữ liệu trong vùng này sẽ bị lộ nhưng sự tồn tại của *Vùng mã hóa ẩn* vẫn **không** bị phát hiện. 

Hãy tưởng tượng một cái vali có một đáy ẩn. Bạn lưu những tài liệu không thực sự quan trọng nếu bị mất hoặc bị sung công vào ngăn bình thường trong chiếc vali này, và cấp giữ những tài liệu tuyệt mật khác vào cái đáy ẩn. Mục đích của cái đáy bí mật (đặc biệt với những đáy được thiết kế khéo léo) là để che dấu sự tồn tại của nó cũng như những tài liệu chứa bên trong đó. *Vùng mã hóa Ẩn* **TrueCrypt** được thiết kế dựa trên ý tưởng đó. 

<a name="5.1"></a>
## 5.1 Hướng dẫn Tạo Vùng mã hóa Ẩn ##


Việc tạo một *Vùng mã hóa Ẩn* **TrueCrypt** cũng tương tự như tạo *Vùng mã hóa Chuẩn*: Một số khung thoại, màn hình và cửa sổ hướng dẫn giống nhau. 

**Bước 1**. **Khởi động** chương trình **TrueCrypt**

**Bước 2**. **Nhấn**: ![](/sbox/screen/truecrypt-vi/13.png) để mở *Thuật sỹ Tạo Vùng Mã hóa* **TrueCrypt**.

**Bước 3**. **Nhấn**: ![](/sbox/screen/truecrypt-vi/05.png)  để chọn lựa chọn mặc định *Cấu tạo bộ chứa tập tin được mã hóa*.

**Bước 4**. **Chọn** lựa chọn *Tập đĩa TrueCrypt được ẩn* như sau: 

![](/sbox/screen/truecrypt-vi/37.png)

*Hình 1: Lựa chọn tạo Vùng mã hóa Ẩn* 

**Bước 5**. **Nhấn**: ![](/sbox/screen/truecrypt-vi/05.png) để mở cửa sổ sau:

![](/sbox/screen/truecrypt-vi/38.png)

*Hình 2: Thuật sỹ Tạo Vùng Mã hóa TrueCrypt - cửa sổ Chế độ*

Bạn sẽ được hướng dẫn để chọn một trong hai chế độ:

- *Direct Mode* - *Chế độ Trực tiếp*: tạo *Vùng mã hóa Ẩn* bên trong một *Vùng mã hóa Chuẩn* đã tồn tại.

- *Normal Mode* - *Chế độ Thường*: tạo một *Vùng mã hóa Chuẩn* mới để chứa *Vùng mã hóa Ẩn*. Trong ví dụ này chúng ta sử dụng *Chế độ Trực tiếp*. 

**Lưu ý**: Nếu bạn muốn tạo một *Vùng mã hóa Chuẩn* mới, hãy theo các bước trong [**Phần 2.2 Hướng dẫn tạo một Vùng mã hóa Chuẩn**](/vi/truecrypt_huongdancaidatvataovungmahoachuan#2.2). 

**Bước 6**. **Chọn** lựa chọn *Direct Mode* và **nhấn** ![](/sbox/screen/truecrypt-vi/05.png) để mở cửa sổ *TrueCrypt Volume Creation - Volume Location*.

**Lưu ý**: Cần gỡ (đóng) Vùng mã hóa Chuẩn trước khi lựa chọn nó cho ví dụ này. 

**Bước 7**. **Nhấn** ![](/sbox/screen/truecrypt-vi/17.png) để mở cửa sổ:

![](/sbox/screen/truecrypt-vi/29.png)

*Hình 3: Thuật sỹ Tạo Vùng Mã hóa TrueCrypt - khung Chọn Ổ đĩa*


**Bước 8**. **Chọn** tệp mã hóa thông qua cửa sổ *Chọn Ổ đĩa TrueCrypt* như trong *Hình 3*.

**Bước  9**. **Nhấn**:  ![](/sbox/screen/truecrypt-vi/30.png) để quay về cửa sổ *Thuật sỹ Tạo Vùng Mã hóa TrueCrypt*.

**Bước 10**. **Nhấn** ![](/sbox/screen/truecrypt-vi/33.png) để mở cửa sổ *Nhập mật khẩu*.

**Bước 11**. **Nhập** mật khẩu dùng để mở **Vùng mã hóa Chuẩn** vào trường *Mật khẩu*để kích hoạt cửa sổ sau:

![](/sbox/screen/truecrypt-vi/46.png)

*Hình 4: Thuật sỹ Tạo Vùng Mã hóa TrueCrypt - khung Thông báo Vùng Mã hóa Ẩn*

**Bước 12**. **Nhấn** ![](/sbox/screen/truecrypt-vi/05.png) sau khi đọc thông báo để mở cửa sổ  *Các Tùy chọn Mã hóa Vùng Mã hóa Ẩn*.

Một cửa sổ xuất hiện sau khi bạn nhập thành công mật khẩu, thông báo rằng chương trình **TrueCrypt** sẽ bắt đầu kiểm tra *Vùng mã hóa Chuẩn* để xác định dung lượng có thể sử dụng để tạo một Vùng mã hóa Ẩn.

**Lưu ý**: Nên giữ nguyên các tùy chọn mặc định cho *Encryption Algorithm* (Thuật toán Mã hóa) và *Hàm Băm* cho việc mã hóa *Vùng Mã hóa Ẩn*.

**Bước 13**. **Nhấn** ![](/sbox/screen/truecrypt-vi/05.png) để kích hoạt cửa sổ:

![](/sbox/screen/truecrypt-vi/41.png)

*Hình 5: Thuật sỹ Tạo Vùng Mã hóa TrueCrypt - cửa sổ Kích thức Vùng mã hóa Ẩn* 

Bạn sẽ được hướng dẫn xác định kích thước *Vùng mã hóa Ẩn*.

**Lưu ý**: Hãy cân nhắc loại tài liệu, số lượng cũng như dung lượng cần lưu trữ. Nên nhớ rằng bạn cần để lại một phần cho Vùng mã hóa Chuẩn sử dụng. Nếu bạn chọn toàn bộ dung lượng trống trên vùng mã hóa Chuẩn để tạo Vùng mã hóa Ẩn, bạn sẽ không thể tải thêm tệp vào Vùng mã hóa Chuẩn. 

*Nếu Vùng mã hóa Chuẩn có dung lượng là 10MB, và bạn muốn sử dụng 5MB cho  vùng mã hóa ẩn, kết quả là bạn sẽ có hai vùng mã hóa (một Chuẩn và một Ẩn) mỗi vùng có dung lượng là 5MB.*

Bạn phải đảm bảo rằng thông tin lưu trữ trong Vùng mã hóa Chuẩn không quá 5MB. Lý do vì chương trình TrueCrypt không tự phát hiện sự tồn tại của Vùng mã hóa Ẩn, và nó có thể vô tình ghi đè lên vùng nhớ đó. Bạn có nguy cơ mất toàn bộ dữ liệu lưu trên Vùng mã hóa Ẩn nếu bạn sử dụng quá dung lượng đã thiết lập. 

**Bước 14**. **Nhập** dung lượng vùng mã hóa ẩn bạn lựa chọn vào trường tương ứng như trong *Hình 6*. . 

**Bước 15**. **Nhấn**:  ![](/sbox/screen/truecrypt-vi/05.png) để mở cửa sổ *Định dạng Vùng mã hóa Ẩn*.

Bây giờ bạn có thể tạo một mật khẩu dùng cho *Vùng mã hóa Ẩn*. Xin nhấn mạnh rằng bạn nên chọn một mật khẩu đủ mạnh. Hãy xem chương hướng dẫn sử dụng [**KeePass**](/vi/keepass-main)  để tìm hiểu cách tạo mật khẩu bảo mật. Hơn thế nữa, mật khẩu này phải khác mật khẩu dùng cho *Vùng mã hóa Chuẩn*.

**Gợi ý**: Nếu bạn dự liệu tình huống bạn có thể bị buộc phải tiết lộ nôi dung *Vùng mã hóa TrueCrypt*, thì hãy tạo một mật khẩu bảo mật cất giữ trong **KeePass** cho *Vùng mã hóa Chuẩn* và một mật khẩu riêng cho *Vùng Mã hóa Ẩn* để ghi nhớ và chỉ mình bạn biết. Điều này giúp che giấu sự tồn tại của *Vùng mã hóa Ẩn* và không để lại dấu vết nào về vùng mã hóa ẩn này. 

**Bước 16**. Tạo mật khẩu và nhập mật khẩu 2 lần và **nhấn**: ![](/sbox/screen/truecrypt-vi/05.png) để mở:

![](/sbox/screen/truecrypt-vi/42.png)

*Hình 6: Cửa sổ Định dạng vùng Mã hóa Ẩn* 

Sử dụng lựa chọn *Hệ thống* và *Cụm* mặc định 

**Bước 17**. **Di chuyển** the con trỏ chuột quanh màn hình để sinh dữ liệu ngẫu nhiên và **nhấn**: ![](/sbox/screen/truecrypt-vi/25.png) để định dạng vùng mã hóa ẩn.

*Sau khi một Vùng mã hóa Ẩn được định dạng, thông báo sau sẽ xuất hiện:*

![](/sbox/screen/truecrypt-vi/43.png)

*Hình 7: Thông báo Vùng mã hóa Ẩn được tạo thành công* 

**Lưu ý**: *Hình 7* xác nhận việc tạo thành công vùng nhớ ẩn đồng thời cảnh báo nguy cơ ghi đè lên các tệp trong *Vùng mã hóa Ẩn* nằm trong *Vùng mã hóa Chuẩn*.

**Bước 18**. **Nhấn** ![](/sbox/screen/truecrypt-vi/27.png) để mở cửa sổ *Trợ lý cấu tạo tập đĩa TrueCrypt*, sau đó **nhấn** ![](/sbox/screen/truecrypt-vi/28.png) để quay về giao diện chính **TrueCrypt**. 

*Môt Vùng mã hóa Ẩn* đã được tạo bên trong *Vùng mã hóa Chuẩn*. Bây giờ bạn có thể lưu tài liệu ẩn bên trong một *Vùng mã hóa Ẩn* được bảo vệ bởi mật khẩu của riêng nó. 

<a name="5.2"></a>
## Hướng dẫn Gắn một Vùng mã hóa Ẩn ##

Cách gắn một *Vùng Mã hóa Ẩn* vào hệ thống để truy cập cũng giống như đối vơí một *Vùng mã hóa Chuẩn*; chỉ khác là bạn cần phải sử dụng mật khẩu vừa được tạo ra cho *Vùng mã hóa Ẩn*. 

Để *gắn* hay *mở* một *Vùng mã hóa Ẩn*, thực hiện các bước sau: 

**Bước 1**. **Chọn:** Một ký tự ổ đĩa, ví dụ ‘K:’ 

![](/sbox/screen/truecrypt-vi/44.png)

*Hình 8: Chọn một ký tự ổ đĩa để gắn Vùng mã hóa vào hệ thống*


**Bước 2**. **Nhấn**: ![](/sbox/screen/truecrypt-vi/17.png). Màn hình *Chọn một Ổ đĩa TrueCrypt* sẽ xuất hiện.

**Bước 3**. **Xác định** tệp vùng mã hóa TrueCrypt của bạn (chính là tệp dùng cho Vùng mã hóa Chuẩn). 

**Bước 4**. **Nhấn**: ![](/sbox/screen/truecrypt-vi/30.png) để về cửa sổ chính chương trình **TrueCrypt**.

**Bước 5**. **Nhấn**: ![](/sbox/screen/truecrypt-vi/31.png) cửa sổ yêu cầu *Nhập Mật khẩu* sẽ hiện lên như sau:

![](/sbox/screen/truecrypt-vi/32.png)

*Hình 9: Màn hình nhập mật khẩu* 


**Bước 6**. **Nhập** mật khẩu bạn sử dụng khi tạo Vùng mã hóa Ẩn và **nhấn** ![](/sbox/screen/truecrypt-vi/33.png). 

*Vùng mã hóa Ẩn được gắn (mở) như sau*:

![](/sbox/screen/truecrypt-vi/45.png) 

*Hình 10:  Cửa sổ chính của TrueCrypt hiển thị Vùng mã hóa Ẩn mới được gắn vào hệ thống*

**Bước 7**. **Nhấn đúp chuột** vào mục tương ứng trên cửa sổ **TrueCrypt** hoặc mở cửa sổ **My Computer** và chọn ổ đĩa tương ứng (ở ví dụ này là ổ *K*). 

<a name="5.3"></a>
## 5.3 Gợi ý Hướng dẫn sử dụng Tính năng Vùng mã hóa Ẩn một cách bảo mật ##

Mục đích của tính năng ổ đĩa ẩn là để tránh những tình huống nguy hiểm có thể xảy ra bằng cách *chấp nhận* tiết lộ những tệp được mã hóa, khi ở trong tình thế bắt buộc, mà không thực sự phải tiết lộ những thông tin tuyệt mật quan trong hơn. Ngoài việc bảo vệ dữ liệu của bạn, điều này còn cho phép bạn tránh gặp thêm những nguy hiểm đối với bản thân hay với các đồng nghiệp và đối tác. Để đảm bảo điều này, bạn phải tạo được tình huống nếu bị yêu cầu trình báo các tệp dữ liệu, chúng đủ đảm bảo có giá trị nào đó để thỏa mãn yêu cầu của những kẻ yêu cầu xem thông tin và để bạn đi.

Những gợi ý sau đây có thể giúp bạn: 

- Lưu một số tài liệu mật mà bạn có thể chấp nhận bị lộ vào *Vùng mã hóa Chuẩn*. Thông tin loại này cần có mức độ nhạy cảm đủ để cần được lưu trữ dưới dạng mã hóa.

- *Hãy cảnh giác trường hợp những kẻ yêu cầu kiểm tra dữ liệu của bạn cũng biết về tính năng tạo *Vùng mã hóa Ẩn* của **TrueCrypt**. Tuy nhiên, nếu bạn sử dụng **TrueCrypt** đúng cách, kẻ đó sẽ không thể chứng minh rằng có tồn tại một **Vùng mã hóa Ẩn**, điều đó giúp bạn có thể chối bỏ.*

- *Hãy sử dụng *Vùng nhớ Chuẩn* hàng tuần. Điều đó tạo ấn tượng rằng bạn thực sự sử dụng những dữ liệu này*

Bất kỳ khi nào bạn gắn một vùng mã hóa **TrueCrypt** vào hệ thống, bạn có thể sử dụng tính năng *Bảo vệ vùng mã hóa Ẩn khỏi nguy cơ bị ghi đè*. Đây là một lựa chọn *rất* quan trọng cho phép bạn thêm nhiều tệp ‘mồi’ vào *Vùng mã hóa Chuẩn* mà không lo bị ghi đè lên nội dung trong *Vùng mã hóa Ẩn*. Như đã đề cập ở phía trên, việc sử dụng quá kích thước giới hạn của Vùng nhớ Chuẩn có thể phá hủy toàn bộ những tệp thông tin ẩn.  Bạn không bao giờ sử dụng lựa chọn Bảo vệ vùng mã hóa Ẩn khỏi nguy cơ bị ghi đè trong trường hợp bị cưỡng bức mở Vùng mã hóa TrueCrypt, nếu làm như vậy chương trình sẽ yêu cầu bạn nhập mật khẩu cho Vùng mã hóa Ẩn và rõ ràng sẽ để lộ sự tồn tại của vùng nhớ này. Khi bạn cập nhật các thông tin ‘mồi’ trong điều kiện riêng tư, bạn nên sử dụng chọn lựa này.

Để sử dụng tính năng *Bảo vệ Vùng mã hóa Ẩn*, thực hiện các bước sau.

**Bước 1**. **Nhấn** ![](/sbox/screen/truecrypt-vi/47.png) trên cửa sổ *Nhập Mật khẩu* như trên *Hình 10* phía trên. Cửa sổ *Tùy chọn Gắn* sẽ xuất hiện như sau:

![](/sbox/screen/truecrypt-vi/48.pngng)

*Hình 11: Cửa sổ Các lựa chọn Gắn vùng Mã hóa*

**Bước 2**. **Lựa chọn**  *Bảo vệ tập đĩa khỏi bị tổn hại gây ra bởi viết vào tập đĩa bên ngoài*.

**Bước 3**. **Nhập** mật khẩu của Vùng mã hóa Ẩn và nhấn (/sbox/screen/truecrypt-vi/33.png)

**Bước 4**. **Nhấn** ![](/sbox/screen/truecrypt-vi/31.png) để  gắn *Vùng mã hóa Chuẩn*. Sau khi việc gắn thành công bạn có thể thêm các ‘tệp mồi’ mà không lo làm hỏng Vùng mã hóa Ẩn

**Bước 5**. **Nhấn** ![](/sbox/screen/truecrypt-vi/51.png) để đóng vùng mã hóa chuẩn, sau khi bạn thực hiện xong việc thay đổi nội dung bên trong đó.

**Hãy ghi nhớ** chỉ thực hiện điều này khi bạn cập nhật các tệp bên trong *Vùng mã hóa Chuẩn*. Còn khi bị bắt buộc phải mở *Vùng mã hóa Chuẩn* cho ai đó, bạn không nên sử dụng tính năng *Bảo vệ Vùng mã hóa Ẩn này*.


