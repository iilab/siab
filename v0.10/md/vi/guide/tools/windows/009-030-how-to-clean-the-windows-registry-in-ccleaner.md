

---

lang: vi
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: How to Clean the Windows Registry in CCleaner

---

Các mục trong trang này:  

- [**4.0 Trước khi Bắt đầu**](#4.0)
- [**4.1 Hướng dẫn sử dụng CCleaner để dọn dẹp Windows Registry**](#4.1)
- [**4.2 Hướng dẫn Phục hồi Thông tin Sao lưu Registry**](#4.2)


<a name="4.0"></a>
### 4.0 Trước khi Bắt đầu ###

**CCleaner** cũng cho phép bạn dọn dẹp **Windows  Registry**, đây là một cơ sở dữ liệu lưu trữ thông tin, các thiết đặt cho phần cứng, phần mềm trên máy tính. Bất kỳ lúc nào bạn thay đổi một thiết đặt trên máy tính, cài thêm một ứng dụng hay thực hiện bất kỳ một tác vụ nào khác, những thay đổi đó sẽ được thể hiện và ghi lại trên **Windows Registry**.

Tuy nhiên sau một thời gian hoạt động, **Windows Registry** lưu chứa nhiều thông tin cấu hình, thiết đặt lỗi thời liên quan tới những ứng dụng từng được cài đặt. Tính năng **CCleaner** *Registry*  cho phép bạn tìm và xóa bỏ những loại thông tin trên giúp cải thiện hoạt động của máy tính cũng như tăng cường bảo mật tính riêng tư và an toàn thông tin số của bạn.

**Gợi ý**: Bạn nên chạy chức năng quét **Windows Registry** hàng tháng.

<a name="4.1"></a>
### 4.1 Hướng dẫn Dọn dẹp Windows Registry ###

**Bước 1**. **Nhấn** ![](/sbox/screen/ccleaner-vi-1/30.png) để mở cửa sổ sau:

![](/sbox/screen/ccleaner-vi-1/31.png)

*Hình 1: Màn hình giao diện CCleaner hiển thị khung Registry*

Khung **CCleaner** *Registry* được chia thành hai cột hiển thị danh sách các mục **Dọn dẹp Registry** và cột các thông tin về những lỗi tìm thấy.

**Bước 2**. **Chọn** tất cả các mục trong danh sách **Dọn dẹp Registry** và **nhấn** ![](/sbox/screen/ccleaner-vi-1/32.png) để bắt đầu quá trình quét tìm các lỗi liên quan đến registry; sau khi hoàn thành, thông tin kết quả thực hiện được hiển thị có dạng như sau:

![](/sbox/screen/ccleaner-vi-1/33.png)

*Hình 2: Báo cáo kiểm tra Windows Registry liệt kê các lỗi cần sửa* 

Trước khi sửa **Windows Registry**, bạn sẽ được hướng dẫn sao lưu tệp thông tin registry. Nếu có xảy ra lỗi sau khi dọn dẹp **Windows Registry**, bạn có thể khôi phục **Windows Registry** lại trạng thái trước đó từ bản sao lưu này.

**Bước 3**. **Nhấn** ![](/sbox/screen/ccleaner-vi-1/34.png) để mở hộp thoại xác nhận:

![](/sbox/screen/ccleaner-vi-1/35.png)

*Hình 3: Hộp thoại xác nhận sao lưu registry*

**Gợi ý**: Nếu bạn quên nơi lưu tệp sao lưu registry này, có thể dùng chức năng tìm kiếm tệp để tìm  tệp có phần mở rộng *.reg*. 

**Bước 4**. **Nhấn** ![](/sbox/screen/ccleaner-vi-1/36.png) để tạo tệp sao lưu registry và hiển thị cửa sổ sau:

![](/sbox/screen/ccleaner-vi-1/37.png)

*Hình 4: Chọn nơi lưu tệp sao lưu*

**Bước 5**. **Nhấn** ![](/sbox/screen/ccleaner-vi-1/38.png) sau khi đã chọn xong đường dẫn lưu tệp sao lưu, hộp thoại sau sẽ xuất hiện:

![](/sbox/screen/ccleaner-vi-1/39.png)

*Hình 5: Khung Sửa lỗi trong Registry*

**Lưu ý** Người dùng có kinh nghiệm và các chuyên gia sẽ thấy tính năng chọn lựa các lỗi cần sửa rất hữu ích tùy theo yêu cầu riêng. Với đa số người dùng bình thường và mới bắt đầu nên chọn sửa tất cả các vấn đề được tìm thấy.

**Bước 6**. **Nhấn** ![](/sbox/screen/ccleaner-vi-1/40.png) hoặc ![](/sbox/screen/ccleaner-vi-1/41.png) để tìm hiểu từng vấn đề, sau đó **nhấn** ![](/sbox/screen/ccleaner-vi-1/42.png) để sửa những lỗi bạn mong muốn.

**Bước 7**. **Nhấn** ![](/sbox/screen/ccleaner-vi-1/43.png) để sửa tất cả các vấn đề đã chọn, sau đó **nhấn** ![](/sbox/screen/ccleaner-vi-1/44.png)

**Gợi ý**: lặp lại **các bước 3** đến **6** cho đến khi không còn thấy vấn đề nào cần sửa.

Quá trình dọn dẹp **Windows Registry** đã hoàn thành.

<a name="4.2"></a>
### 4.2 Hướng dẫn Phục hồi Thông tin Sao lưu Registry ###

Nếu bạn cho rằng quá trình dọn dẹp **Windows Registry** đã gây ra lỗi đối với hệ thống, tệp sao lưu registry được tạo trong **bước 3** đến **5** của mục **4.1** có thể được sử dụng để khôi phục bản registry cũ và giảm thiểu những can thiệp vào hệ thống của bạn.

Để khôi phục lại registry, hãy theo các bước sau:

**Bước 1**. **Chọn Start > Run** để mở hộp thoại *Run* và **gõ vào** *regedit* như sau:

![](/sbox/screen/ccleaner-vi-1/45.png)

*Hình 6: Hộp thoại Run*

**Bước 2**. **Nhấn** ![](/sbox/screen/ccleaner-vi-1/22.png) để kích hoạt cửa sổ:

![](/sbox/screen/ccleaner-vi-1/46.png)

*Hình 7: Trình Soạn thảo Registry*

**Bước 3**. **Chọn File > Import** từ trình đơn của trình duyệt để mở cửa sổ *Import Registry File* sau đó **chọn** ![](/sbox/screen/ccleaner-vi-1/47.png).

**Bước 4**. **Nhấn** ![](/sbox/screen/ccleaner-vi-1/48.png) để mở hộp thoại xác nhận:

![](/sbox/screen/ccleaner-vi-1/49.png)

*Hình 8: Hộp thoại Trình soạn thảo Registry Editor xác nhận tệp registry đã được khôi phục*

**Bước 5**. **Nhấn** ![](/sbox/screen/ccleaner-vi-1/22.png) để hoàn thành việc khôi phục registry từ tệp sao lưu.

