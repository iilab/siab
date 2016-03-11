

---

lang: vi
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 008
title: Eraser - Secure File Removal

---

**Trang chủ**  
[**www.heidi.ie/eraser**](http://www.heidi.ie/eraser/) 

**Yêu cầu Cấu hình Máy tính**

- Tất cả các phiên bản Windows

**Phiên bản sử dụng trong hướng dẫn này**

- 5.86a 

***Lưu ý**: Có thể bạn thấy có phiên bản **Eraser** mới hơn trên trang chủ, chúng không được sử dụng ở đây vì các phiên bản này đòi hỏi phải có **.Net Framework** cài đặt trên hệ điều hành **Microsoft Windows**. Việc tải về **.Net Framework** có thể mất  nhiều thời gian đối với người dùng có tốc độ kết nối thấp*

**Bản quyền**

- Miễn phí và Nguồn mở

**Yêu cầu Đọc thêm**

- Hướng dẫn Sử dụng chương [**6. Làm thế nào để phá hủy thông tin nhạy cảm**](/chapter-6)

**Mức độ**: 1: Bắt đầu, **2: Trung bình**, 3: Trên trung bình, 4: Có kinh nghiệm, 5: Nâng cao


**Thời gian cần thiết để tìm hiểu công cụ này**: 20 phút

**Những điều bạn sẽ học được**:

- Khả năng xóa vĩnh viễn các tệp không mong muốn khỏi máy tính của mình
- Khả năng xóa các tệp có thể bị khôi phục lại hiện đang tồn tại nhưng không nhìn thấy trong máy tính của bạn


**Các Chương trình có Tính năng Tương tự trên GNU Linux, Mac OS và Microsoft Windows**:

Trong **GNU/Linux**, gói xóa bảo mật có thể được [**sử dụng từ cửa sổ giao diện dòng lệnh](http://www.ghacks.net/2010/08/26/securely-delete-files-with-secure-delete/) để vừa xóa tệp và thư mục một cách bảo mật đồng thời có thể dùng để quét sạch không gian trống trên ổ đĩa. Lệnh xóa bảo mật cũng có thể [**được tích hợp với một trình quản lý tệp có giao diện đồ họa**](http://techthrob.com/2010/07/07/adding-a-secure-delete-option-to-nautilus-file-manager-in-linux/).

Trên **Mac OS** bạn có thể sử dụng trình đơn **Finder** mục *Secure Empty Trash...* để vĩnh viễn xóa bỏ một số tệp và thư mục. Bạn cũng có thể sử dụng chương trình *Disk Utility* trên **Mac OS** để xóa an toàn toàn bộ ổ đĩa hoặc một không gian trống trên ổ đĩa trong hoặc cắm ngoài.

Trên **Microsoft Windows** bên cạnh **Eraser** được giới thiệu trong chương này, bạn cũng có thể sử dụng [**CCleaner**](/vi/ccleaner-main) để xóa tệp và thư mục khỏi **Recycle Bin**  một cách an toàn. **CCleaner** cũng có thể quét sạch không gian trống trên ổ đĩa. Một công cụ khác cũng có thể được sử dụng để xóa tệp bảo mật là  [**Freeraser**](http://www.freeraser.com/).

Chúng tôi cũng muốn giới thiệu một công cụ hoạt động trên nhiều nền tảng hệ điều hành khác nhau: [**DBAN - Darik's Boot And Nuke**](http://www.dban.org/). Đây là một gói bạn có thể ghi vào một đĩa CD và khởi động từ đĩa này. **DBAN** cho phép bạn xóa an toàn toàn bộ thông tin trên một ổ đĩa bất kỳ có thể nhận diện được, đây là công cụ rất *lý tưởng* để phá hủy thông tin trong trường hợp khẩn cấp.

## 1.1 Những điều bạn cần biết về công cụ này trước khi bắt đầu ##

**Eraser** được sử dụng để xóa triệt để hay *quét sạch* thông tin dữ liệu nhạy cảm trên máy tính của bạn.  Điều này được thực hiện bằng cách ghi đè lên thông tin dữ liệu cần xóa. Bạn có thể chọn các tệp và thư mục muốn xóa an toàn. **Eraser** cũng sẽ xóa các bản sao của dữ liệu đang tồn tại trên máy tính mà bạn không hề biết. Bao gồm những tệp bạn đã xóa trước đây sử dụng lệnh xóa thông thường của **Windows** cũng như những bản sao của các tài liệu bạn từng sử dụng trong quá khứ.

- Việc xóa tệp an toàn dùng **Eraser** có thể được thực hiện trực tiếp hoặc lên lịch thực hiện tại một số thời điểm xác định.
- Nếu bạn lên lịch **Eraser** thực hiện tại một thời điểm xác định, máy tính của bạn cần phải được bật tại thời điểm đó nếu không việc xóa bảo mật sẽ không được thực hiện. 
- Một khi đã xóa tệp sử dụng **Eraser**, tệp đó sẽ không thể khôi phục lại được bằng các chương trình khôi phục tệp đã xóa.
- Để tăng mức độ xóa an toàn, bạn nên thiết đặt **Eraser** ghi đè lên các dữ liệu đã chọn xóa từ 3 đến 7 lần.
- **Eraser** có thể được dùng để làm sạch không gian trống trên máy tính của bạn. Công cụ này cung cấp khả năng xóa an toàn vĩnh viễn các dấu vết làm việc trong quá khứ tồn tại trong máy tính của bạn do được xóa không triệt để và vì vậy có thể được khôi phục lại.

