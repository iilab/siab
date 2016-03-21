

---

lang: vi
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Use Eraser

---

Các mục trong trang này:

- [**3.0 Hướng dẫn Sử dụng Eraser với Windows Explorer**](#3.0)
- [**3.1 Hướng dẫn Quét sạch Vùng Đĩa Không Sử dụng**](#3.1)
- [**3.2 Hướng dẫn Sử dụng Tính năng Tác vụ Tức thời**](#3.2)
- [**3.3 Hướng dẫn Sử dụng Tính năng Tác vụ  Đặt lịch**](#3.3)
- [**3.4 Hướng dẫn Hủy Tác vụ**](#3.4)
- [**3.5 Hướng dẫn Xóa sạch Thùng rác Windows**](#3.5)

-------

<a name="3.0"></a>
## 3.0 Hướng dẫn Sử dụng Eraser với Windows Explorer ##

Người dùng thường sử dụng **Eraser** qua cửa số chương trình **My Computer Windows Explorer** hơn là qua việc mở chương trình **Eraser**. 

**Bước 1**. **Mở** thư mục chứa tệp bạn muốn xóa an toàn.

**Bước 2**. **Nhấn chuột phải** vào tệp cần xóa. Hai tính năng mới nằm trong danh sách các lệnh là *Erase* và *Eraser Secure Move* như sau:

![](/sbox/screen/eraser-vi/14.png)

*Hình 1: Lệnh Erase và Eraser Secure Move*

Chúng ta sẽ sử dụng lệnh *Erase* để xóa tệp này một cách triệt để.

**Bước 3**. **Chọn** lệnh **Erase** từ trình đơn như trong *Hình 1* phía trên.

*Hộp thoại Erasing xuất hiện*:

![](/sbox/screen/eraser-vi/15.png)

*Hình 2: Xác nhận Xóa*

Nếu tệp xuất hiện trong hộp thoại xác nhận chính là tệp bạn muốn xóa, hãy theo các bước sau:

**Bước 4**. **Nhấn vào** ![](/sbox/screen/eraser-vi/16.png) để xóa *vĩnh viễn* hay xóa an toàn tệp đã chọn khỏi máy tính của bạn.

**Cảnh báo**: Bất kỳ tệp này được xóa theo phương pháp này sẽ *không thể khôi phục lại* và bị xóa vính viễn. Vì vậy bạn phải hoàn toàn chắc chắn về môt hay một nhóm tệp mình định xóa.

Để di chuyển một cách an toàn một hay nhiều tệp từ vị trí này sang vị trí khác (ví dụ, từ máy tính của bạn sang thẻ nhớ USB):

**Bước 5**. **Chọn** ![](/sbox/screen/eraser-vi/17.png)

Bạn sẽ cần trả lời một số thông báo cảnh báo như phía trên để tiếp tục.

<a name="3.1"></a>
## 3.1 Hướng dẫn Quét sạch Vùng Đĩa Không Sử dụng ##

Việc quét sạch vùng đĩa không sử dụng gồm việc xóa an toàn các dấu vết của các tệp trước đó khỏi các 'vùng trống' trên ổ đĩa cứng hay ổ đĩa di động. Vùng nhớ trống này thường chứa các tệp không được xóa triệt để ( hãy tham khảo phần **Hướng dẫn Thực hành** [**Recuva**](/vi/recuva-main) và **Sách Hướng dẫn** [**Chương 6**](chuong-6) để có tham khảo thêm).

**Bước 1**. **Chọn Start > Programs > Eraser > Eraser**

**Gợi ý**: Bạn có thể thực hiện tác vụ quét triệt để trực tiếp hoặc có thể đặt lịch thực hiện vào một thời gian xác định. 

**Quan trọng**: Tiến trình này có thể kéo dài từ 2 đến 5 giờ để hoàn thành và sẽ làm chậm hệ thống của bạn khi chương trình hoạt động. Có thể là ý hay nếu bạn thực hiện hoặc đặt lịch thực  hiện tiến trình quét triệt để vùng nhớ trống của ổ đĩa khi không sử dụng máy tính (hoặc khi bạn đi đi về đẻ máy hoạt động qua đêm). 

<a name="3.2"></a>
## 3.2 Hướng dẫn Sử dụng Tính năng Tác vụ Tức thời (On-Demand) ##

Để tạo một tác vụ *On-Demand* (tức thời) để xóa an toàn *vùng không gian trống trên ổ đĩa*, hãy theo các bước sau:

**Bước 1**. **Nhấn vào** ![](/sbox/screen/eraser-vi/18.png)

**Bước 2**. **Chọn File > New Task** như sau: 

![](/sbox/screen/eraser-vi/19.png)

*Hình 3: Chọn Tác vụ Mới trên trình đơn File*

Tùy chọn *Unused space on drive* phải được chọn. 

**Bước 3**. **Chọn** ổ đĩa bạn muốn quét triệt để vùng nhớ trống (Trong ví dụ này *Local Disk (C:)* được chọn. Đây thường là ổ đĩa hệ thống trên hầu hết các máy tính.) 

![](/sbox/screen/eraser-vi/20.png)

*Hình 4: Màn hình Thuộc tính Tác vụ Eraser*

**Bước 4**. **Nhấn vào** ![](/sbox/screen/eraser-vi/21.png) để tạo và thực hiện tác vụ, cửa sổ giao diện **Eraser** sẽ hiển thị thông tin.

**Bước 5**. **Nhấn chuột phải** vào tác vụ để mở trình đơn sau:

![](/sbox/screen/eraser-vi/22.png)

*Hình 5: Lệnh Run được chọn trên màn hình Eraser*

**Bước 6**. **Chọn Run** để mở hộp thoại **Eraser**:

![](/sbox/screen/eraser-vi/23.png)

*Hình 6: Hộp thoại Eraser*

**Bước 7**. **Nhấn vào** ![](/sbox/screen/eraser-vi/16.png).

*Thanh trạng thái tiến trình **Eraser** sẽ hiển thị quá trình xóa triệt để vùng nhớ không sử dụng như sau:*

![](/sbox/screen/eraser-vi/24.png)

*Hình 7: Cửa sổ Eraser với tiến trình xóa an toàn không gian trống của ổ đĩa*

<a name="3.3"></a>
## 3.3 Hướng dẫn Sử dụng Tính năng Tác vụ  Đặt lịch ##

Do chúng ta thường hay quên việc 'dọn dẹp' máy tính này,  **Eraser** có một tùy chọn cho phép bạn đặt lịch thực thi tác vụ vào một thời điểm xác định hàng ngày, hoặc vào một ngày nào đó trong tuần.

**Bước 1**. **Nhấn vào** ![](/sbox/screen/eraser-vi/25.png) trên cửa sổ chính **Eraser**.

**Bước 2**. **Chọn File > New Task** như sau:

![](/sbox/screen/eraser-vi/26.png)

*Hình 8: Chọn mục New Task trên trình đơn File*

Cửa sổ giống như trong *Hình 4* sẽ xuất hiện (như khi bạn tạo một tác vụ tức thì). 

**Bước 3**. **Đặt** các tùy chọn như đã hướng dẫn trong phần [**3.2 How to Use the on-Demand Tasks Option**](/vi/eraser_huongdansudung#3.2).

![](/sbox/screen/eraser-vi/27.png)

*Hình 9: Thuộc tính Tác vụ Eraser với khung Schedule*

**Bước 4**. **Nhấn vào** khung *Schedule* để mở khung cấu hình đặt lịch: 

![](/sbox/screen/eraser-vi/28.png)

*Hình 10: Khung Đặt lịch Eraser*

**Bước 5**. **Chọn** ngày hoặc một mục thời điểm phù hợp với bạn trong trường *Every*.

**Bước 6**. **Nhập** thời gian phù hợp trong mục *At* với định dạng 24 giờ.

**Bước 7**. Sau khi đã đặt xong ngày, giờ hãy **nhấn vào** ![](/sbox/screen/eraser-vi/21.png).

*Tác vụ được lên lịch sẽ hiển thị như sau*:

![](/sbox/screen/eraser-vi/29.png)

*Hình 11: Danh sách các tác vụ  Eraser được lên lịch*

**Lưu ý**: Máy tính của bạn phải hoạt động tại thời điểm đặt lịch thực hiện tác vụ.

<a name="3.4"></a>
## 3.4 Hướng dẫn Hủy Tác vụ ##

Sau khi bạn đã chạy tác vụ tức thời hoặc tác vụ được lên lịch, bạn có thể muốn hủy tác vụ đó khỏi danh sách tác vụ

Để loại bỏ một tác vụ tức thời hãy thực hiện các bước sau:

**Bước 1**. **Nhấn vào** ![](/sbox/screen/eraser-vi/18.png) để hiển thị danh sách các tác vụ tương ứng như sau:

![](/sbox/screen/eraser-vi/30.png)

*Hình 12: Danh sách tác vụ Eraser*

**Bước 2**. **Chọn** tác vụ bạn muốn hủy bỏ như trong *Hình 12* phía trên. 

**Bước 3**. **Nhấn phải chuột** để mở cửa sổ trình đơn và **chọn** lệnh *Delete* để hủy một tác vụ khỏi danh sách tác vụ. (Một cách khác, bạn cũng có thể **nhấn vào** ![](/sbox/screen/eraser-vi/31.png) nằm bên dưới thanh trình đơn **Eraser**.

Các bước thực hiện việc hủy bỏ một *Tác vụ được Lên lịch* gần như tương tự. Để hủy bỏ một tác vụ được lên lịch, hãy thực hiện các bước sau:

**Bước 1**. **Nhấn vào** ![](/sbox/screen/eraser-vi/25.png), sau đó **lặp lại** **bước** 2 và 3, như hướng dẫn phía trên.

<a name="3.5"></a>
## 3.5 Hướng dẫn Xóa sạch Thùng rác Windows ##

**Eraser** cũng cho phép bạn xóa dấu vết các tài liệu bạn đã từng xóa khỏi **Thùng Rác Windows trên Màn hình**. 

Để thực hiện tính năng này hãy theo các bước sau:

**Bước 1**. **Nhấn phải chuột** vào biểu tượng **Recycle Bin** để mở trình đơn **Eraser** như sau:

![](/sbox/screen/eraser-vi/32.png)

*Hình 13: Trình đơn Eraser cho Recycle Bin*

**Bước 2**. **Chọn** mục thích hợp trên trình đơn để thực hiện việc xóa triệt để dữ liệu trong **Thùng Rác**.

