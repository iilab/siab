

---

lang: vi
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Mount the Standard Volume

---

Các mục trong trang này:

- [**3.0 Hướng dẫn Gắn Vùng Mã hóa Chuẩn**](#3.0)
- [**3.1 Hướng dẫn Gỡ Vùng Mã hóa Chuẩn**](#3.1)

-------

<a name="3.0"></a>
## 3.0 Hướng dẫn Gắn Vùng Mã hóa Chuẩn ##

Trong **TrueCrypt**, ‘gắn’ là quá trình làm cho vùng mã hóa sẵn sàng được sử dụng. Trong phần này bạn sẽ học cách ‘gắn’ một Vùng mã hóa mới tạo. 

Để thực hiện việc gắn một Vùng mã hóa Chuẩn, thực hiện các bước sau: 

**Bước 1**. **Nhấn đúp chuột** vào ![](/sbox/screen/truecrypt-vi/52.png) hoặc **Chọn Start > Programs > TrueCrypt > TrueCrypt** để mở **TrueCrypt**.

**Bước 2**: **Chọn** một ổ đĩa trong danh sách như bên dưới: 

![](/sbox/screen/truecrypt-vi/12.png)

*Hình 1: Giao diện chương trình TrueCrypt*

*Vùng mã hóa Chuẩn sẽ được gắn vào ổ đĩa M.* 

**Chú ý**: Trong *Hình 1*, ký tự ổ đĩa *M* được chọn, nhưng bạn cũng có thể chọn bất kỳ ký tự ổ đĩa sẵn có nào khác. 

**Bước 3**. **Nhấn**: ![](/sbox/screen/truecrypt-vi/17.png)

Màn hình *Chọn một tập đĩa TrueCrypt* sẽ xuất hiện như sau:

![](/sbox/screen/truecrypt-vi/29.png)

*Hình 2: Cửa sổ Chọn một Vùng Mã hóa TrueCrypt*

**Bước 4**. **Chọn** một tệp Vùng mã hóa bạn đã tạo, và **nhấn** ![](/sbox/screen/truecrypt-vi/30.png)  để đóng *Hình 2* và chuyển sang cửa sổ chính của **TrueCrypt**.

**Bước 5**: **Nhấn**: ![](/sbox/screen/truecrypt-vi/31.png)  kích hoạt cửa sổ *Nhập mật mã* như sau:


![](/sbox/screen/truecrypt-vi/32.png)

*Hình 3: Cửa sổ Nhập Mật khẩu* 

**Bước 6**: **Nhập** mật khẩu vào trường *Mật khẩu*. 

**Bước 7**: **Nhấn**:  ![](/sbox/screen/truecrypt-vi/33.png)

*TrueCrypt sẽ thực hiện việc gắn Vùng mã hóa.* 

**Chú ý**: Nếu mật khẩu nhập vào không đúng, **TrueCrypt** sẽ thông báo và bạn cần nhập lại mật khẩu và **nhấn**: ![](/sbox/screen/truecrypt-vi/00.png). Nếu mật khẩu thích hợp, *Vùng mã hóa Chuẩn* sẽ được gắn vào hệ thống như sau:

![](/sbox/screen/truecrypt-vi/34.png)

*Hình 4: Màn hình chính của TrueCrypt hiển thị Vùng mã hóa Chuẩn vừa được gắn vào hệ thống* 

**Bước 8**. **Nhấn đúp chuột** vào mục đánh dấu trong cửa sổ TrueCrypt hoặc **nhấn đúp chuột** vào ký tự ổ đĩa tương ứng trong **My Computer** để mở *Vùng mã hóa* đã được gắn vào ổ đĩa *M:* trên máy tính của bạn. 

![](/sbox/screen/truecrypt-vi/35.png)

*Hình 5: Truy cập Vùng mã hóa Chuẩn qua cửa sổ My Computer* 

**Lưu ý**: Chúng ta vừa gắn thành công *Vùng mã hóa* *My Volume* thành ổ đĩa ảo *M:*. Ổ đĩa ảo này hoạt động giống như một ổ đĩa hệ thống bình thường, ngoại trừ một điều là nó được mã hóa toàn bộ. Một tệp bất kỳ sẽ được mã hóa mỗi khi bạn sao chép, di chuyển hoặc lưu nó vào trong ổ đĩa ảo này (tiến trình này gọi là sự mã hóa tức thời). 

Bạn cũng có thể chép tệp ra từ Vùng nhớ mã hóa này như cách bạn làm với một ổ đĩa thông thường bất kỳ (ví dụ kéo-và-thả chúng). Khi bạn di chuyển một tệp ra khỏi *Vùng mã hóa*, nó sẽ tự động được giải mã hóa. Ngược lại, nếu bạn chuyển một tệp vào trong *Vùng mã hóa*, **TrueCrypt** sẽ tự động mã hóa nó. Nếu máy tính của bạn bị treo hay tự nhiên bị tắt, **TrueCrypt** sẽ ngay lập tức đóng *Vùng mã hóa* lại. 

**Quan trọng:** Sau khi chuyển các tệp vào trong vùng mã hóa **TrueCrypt**, hãy đảm bảo những dấu vết của tệp sẽ không bị lưu lại trên máy tính hay thẻ nhớ USB. Hãy xem thêm chương [**6. Làm thế nào để phá hủy thông tin mật**](/vi/chuong-6).

<a name="3.1"></a>
## 3.1 Hướng dẫn Gỡ một Vùng mã hóa Chuẩn ##


Trong **TrueCrypt**, ‘gỡ’ một *Vùng mã hóa Chuẩn* đơn giản là làm cho ổ nhớ này không sử dụng được. 

Để đóng hay gỡ một *Vùng mã hóa Chuẩn* và làm cho những tệp trong đó chỉ truy cập được đối với những người có mật khẩu thích hợp, hãy thực hiện các bước sau: 

**Bước 1**. **Chọn** ổ muốn gỡ từ danh sách các ổ được gắn vào hệ thống trong cửa sổ **TrueCrypt**. 

![](/sbox/screen/truecrypt-vi/34.png)

*Hình 6: Chọn một Vùng mã hóa Chuẩn để gỡ khỏi hệ thống* 

**Bước 2**. **Nhấn**: ![](/sbox/screen/truecrypt-vi/49.png)  để gỡ (hay đóng) một Vùng mã hóa **TrueCrypt**

**Quan trọng!** Bạn nên gỡ ổ mã hóa **TrueCrypt** trước khi chuyển máy tính về trạng thái *Standby* hay **Hibernate*. Tốt hơn hết, hãy tắt máy tính của bạn mỗi khi bạn không sử dụng. Việc đó sẽ ngăn không cho ai đó tìm cách lấy trộm mật khẩu vùng mã hóa của bạn.  

Để sử dụng các tệp trong *Vùng mã hóa* sau khi đã gỡ hay đóng nó lại, bạn sẽ phải gắn nó lại vào hệ thống.

