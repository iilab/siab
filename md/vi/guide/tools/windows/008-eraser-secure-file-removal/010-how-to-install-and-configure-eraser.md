

---

lang: vi
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: How to Install and Configure Eraser

---

Các mục trong trang này:

- [**2.0 Hướng dẫn Cài đặt Eraser**](#2.0)
- [**2.1 Hướng dẫn Cấu hình Eraser**](#2.1)

-------

<a name="2.0"></a>
## 2.0 Hướng dẫn Cài đặt Eraser ##

**Lưu ý Cài đặt**: Trược khi bạn thực hiện việc cài đặt, hãy kiểm tra chắc chắn bạn có cài đặt phiên bản mới nhất của **Microsoft Windows Installer** và **Microsoft.NET Framework**. 

Việc cài đặt **Eraser** khá nhanh chóng và dễ dàng. Để bắt đầu cài đặt **Eraser**, hãy theo các bước sau:

Như đã hướng dẫn trong Sách Hướng dẫn chương [**6. Phá hủy Thông tin Nhạy cảm**](/vi/chapter-6), **Eraser** xóa triệt để thông tin trên ổ cứng của bạn bằng cách ghi đè lên các thông tin này bởi thông tin ngẫu nhiên. Việc ghi đè này càng được thực hiện nhiều lần, thì khả năng dữ liệu được khôi phục lại càng thấp.

**Bước 1**. **Nhấn đúp vào** ![](/sbox/screen/eraser-vi/01.png); cửa sổ cảnh báo mở tệp *Open File - Security Warning* có thể xuất hiện. Nếu vậy, **Nhấn vào** ![](/sbox/screen/eraser-vi/02.png) để mở thuật sỹ cài đặt *InstallAware Wizard*; sau vài giây, cửa sổ *Welcome to the InstallAware Wizard for Eraser* sẽ xuất hiện.

**Bước 2**. **Nhấn vào** ![](/sbox/screen/eraser-vi/03.png) để mở cửa sổ thông tin bản quyền *License Agreement*, sau đó **nhấn chọn** ô *I accept the terms of the license agreement*, và **nhấn vào** ![](/sbox/screen/eraser-vi/03.png), cửa sổ *Important Information* sẽ hiện lên.

**Bước 3**. **Nhấn vào** ![](/sbox/screen/eraser-vi/03.png) sau khi đã tìm hiểu kỹ thông tin trong cửa sổ để mở cửa sổ chọn thư mục cài đặt *Destination Folder* và **Nhấn vào** ![](/sbox/screen/eraser-vi/03.png).

**Bước 4**. **Nhấn vào** ![](/sbox/screen/eraser-vi/03.png) để mở cửa số sau:

![](/sbox/screen/eraser-vi/04.png)

*Hình 1: Cửa sổ Chọn Thư mục Chương trình*

**Bước 5**. **Nhấn chọn** ô *Only for me (current user)* để xác định rằng chỉ riêng bạn có quyền sử dụng **Eraser**, sau đó **Nhấn vào** ![](/sbox/screen/eraser-vi/03.png) để mở cửa sổ *Completing the InstallAware Wizard*.

**Bước 6**. **Nhấn vào** ![](/sbox/screen/eraser-vi/03.png) và tiếp tục **nhấn vào** ![](/sbox/screen/eraser-vi/05.png) để hoàn thành tiến trình cài đặt đồng thời khởi động **Eraser** như sau:

![](/sbox/screen/eraser-vi/06.png)

*Hình 2: Giao diện chính người dùng Eraser*

<a name="2.1"></a>
## 2.1 Hướng dẫn Cấu hình Eraser ##

**Lưu ý**: Bạn nên thiết đặt việc ghi đè lên dữ liệu xóa tổi thiểu ba lần.

**Gợi ý**: Mỗi lần ghi đè (hay *pass*) đều mất thời gian nên càng thực hiện nhiều lần việc ghi đè sẽ càng mất nhiều thời gian thực hiện quá trình xóa. Điều này sẽ đáng chú ý khi xóa một lượng lớn tệp hay quét sạch không gian trống trên ổ đĩa.

Số lần ghi đè có thể được thiết đặt tại trình đơn *Preferences: Erasing*.

**Bước 1**. **Chọn > Edit > Preferences > Erasing...** như sau: 

![](/sbox/screen/eraser-vi/07.png)

*Hình 3: Cửa sổ [On-Demand] hiển thị các tùy chọn trong trình đơn Edit*

*Cửa sổ Preferences: Erasing xuất hiện như sau:*

![](/sbox/screen/eraser-vi/08.png)

*Hình 4: Eraser Preferences: Erasing*

Khung *Preferences: Erasing* hiển thị phương thức ghi đè lên dữ liệu cần xóa.

Cột *Description*: Chứa danh sách tên các phương pháp xóa.

Cột *Passes*: Chứa số lần ghi đè lên dữ liệu xóa.

Trong ví dụ này chúng tôi sẽ sử dụng phương pháp ghi đè *Pseudorandom Data*. Mặc định, chỉ một lần ghi đè được thực hiện. Tuy nhiên, để tăng thêm mức độ an toàn, chúng ta sẽ tăng số lần ghi đè.

**Bước 2**. **Chọn** tùy chọn *# 4 Pseudorandom Data* như trong *Hình 2*.

**Bước 3**. **Nhấn vào** ![](/sbox/screen/eraser-vi/09.png) để mở cửa sổ  *Passes*:

![](/sbox/screen/eraser-vi/10.png)

*Hình 3: Cửa sổ Eraser Passes*

**Bước 4**. **Đặt* số lần ghi đè từ ba đến bảy lần (hãy ghi nhớ về sự cân bằng giữa thời gian/bảo mật).

**Bước 5**. **Nhấn vào** ![](/sbox/screen/eraser-vi/11.png) để quay về cửa sổ *Passes*.

\# 4 Pseudorandom Data sẽ thay đổi như dưới đây:

![](/sbox/screen/eraser-vi/12.png)

*Hình 4: Cửa sổ Eraser Erase với khung hiển thị mục thứ 4 được chọn*

**Gợi ý**: Hãy chắc chắn các ô *Cluster Tip Area* và *Alternate Data Streams* được nhấn chọn như sau (chúng được chọn theo mặc định):

![](/sbox/screen/eraser-vi/13.png)

*Hình 5: Ô Eraser Cluster Tip Area và Alternate Data Streams ở chế độ mặc định*


- *Cluster Tip Area*: Một ổ đĩa máy tính được chia thành các đoạn nhỏ gọi là các 'liên cung'. Thông thường một tệp sẽ chiếm một số liên cung, và thường thì một tệp sẽ không sử dụng hết liên cung cuối cùng. Vùng trống không sử dụng trong liên cung cuối cùng này được gọi là vùng đuôi liên cung (cluster tip). Vùng đuôi liên cung này có thể chứa các thông tin nhạy cảm là một phần của tệp đã từng sử dụng liên cung này và sử dụng nhiều liên cung khác. Thông tin nằm trong đuôi liên cung có thể được khôi phục bởi các chuyên gia khôi phục dữ liệu. Vì vậy hãy **nhấn chọn** ô  *Cluster Tip Area* để tăng cường an toàn.
- *Alternate Data Streams*: Khi một tệp được lưu trên máy tính, nó có thể gồm nhiều phần. Ví dụ một tệp văn bản gồm cả ký tự và hình ảnh. Những dữ liệu này sẽ được lưu trên máy tính ở nhiều vị trí khác nhau gọi là các 'streams'. Vì vậy hãy **nhấn chọn** ô *Alternate Data Streams* để đảm bảo rằng tất cả các dữ liệu thuộc về một tệp sẽ bị xóa.

**Bước 6**. **Nhấn vào** ![](/sbox/screen/eraser-vi/11.png).

Bạn vừa thiết đặt phương pháp ghi đè cho Eraser khi xóa tệp. Bạn cũng cần đặt các tùy chọn tương tự cho tính năng *Unused Disk Space* xuất hiện trong khung kế tiếp trong cửa sổ *Preferences: Erasing* . Tuy nhiên, bạn có thể đặt số lần ghi đè *hợp lý* -- do việc quét sạch vùng đĩa trống có thể mất khoảng hai giờ đồng hồ cho một lần ghi đè.

