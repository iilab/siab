

---

lang: vi
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 005
title: TrueCrypt - Secure File Storage

---

**Vào ngày 28 tháng 5 năm 2014 trang web phát triển của TrueCrypt đăng thông báo tới người dùng rằng TrueCrypt sẽ ngừng tiếp tục nâng cấp kể từ thời điểm này. Những nguyên nhân phía sau quyết định này vẫn chưa rõ ràng. Trang phát triển này cũng cung cấp phiên bản mới 7.2 của TrueCrypt với một số tính năng bị gỡ bỏ. Cho dù phiên bản mới này được xuất bản, chúng tôi vẫn khuyến nghị bạn tiếp tục sử dụng phiên bản 7.1a (Hãy tham khảo hướng dẫn Tải về), cho tới khi chúng tôi biết thêm thông tin về điều gì đang diễn ra và các kế hoạc cho sự phát triển trong tương lai của TrueCrypt. Những công cụ thay thế TrueCrypt có thể được tìm thấy trong mục "**Các Chương trình có Tính năng Tương tự trên GNU Linux, Mac OS và Microsoft Windows**" bên dưới.**

**Trang chủ**
[**www.truecrypt.org**](http://www.truecrypt.org/)

**Yêu cầu cấu hình máy tính**

- Windows 2000/XP/2003/Vista/7

- Yêu cầu quyền quản trị hệ thống khi tiến hành cài đặt phần mềm và tạo vùng mã hóa, nhưng không cần thiết khi truy cập. 

**Phiên bản sử dụng trong tài liệu này**

- 7.0a

**Bản quyền** 

- Phần mềm miễn phí Mã nguồn mở 
			
**Yêu cầu đọc thêm** 

- *Sách hướng dẫn [chương 4. Làm sao để bảo vệ các tệp dữ liệu tối mật trên máy tính của bạn](/vi/chuong-4)*

**Mức độ khó** 

- (Standard Volumes) - Vùng Mã hóa Chuẩn: 1: Người mới bắt đầu, 2: Trung bình, **3: Trên trung bình**, 4: Có kinh nghiệm, 5: Nâng cao 

- (Hidden Volumes) - Vùng Mã hóa Ẩn: 1: Người mới bắt đầu, 2: Trung bình, 3: Trên trung bình, **4: Có kinh nghiệm**, 5: Nâng cao

**Thời gian cần thiết để có thể sử dụng công cụ**: 

- (Standard Volumes): 30 phút 

- (Hidden Volumes): 30 phút 

**Những lợi ích bạn sẽ có được**: 

- Khả năng bảo vệ một cách có hiệu quả các tệp thông tin của mình khỏi sự truy cập trái phép 

- Khả năng sao lưu dễ dàng và bảo mật những tệp quan trọng 

**Các Chương trình có Tính năng Tương tự trên GNU Linux, Mac OS và Microsoft Windows:**

**Lưu ý**: Chúng tôi khuyên bạn sử dụng **TrueCrypt**  phiên bản cho **GNU Linux** và **Mac OS**. 

Nhiều phiên bản của **GNU Linux** như  [**Ubuntu**](http://www.ubuntu.com/) tích hợp tính năng hỗ trợ việc  mã hóa - giải mã hóa tức thời cho toàn bộ ổ đĩa. Bạn có thể sử dụng tính năng này khi cài đặt hệ thống. Bạn cũng có thể thêm chức năng mã hóa vào hệ thống **Linux** của mình bằng việc sử dụng [**dm-crypt**](http://www.saout.de/misc/dm-crypt/) và [**cryptsetup and LUKS**](http://code.google.com/p/cryptsetup/). Một cách khác là sử dụng [**ScramDisk for Linux SD4L**](http://sd4l.sourceforge.net/), đây là một chương trình miễn phí mã nguồn mở hỗ trợ việc mã hóa-giải mã hóa tức thời.

Trong **Mac OS** bạn có thể sử dụng **FileVault**, được tích hợp sẵn trong hệ điều hành này cung cấp tính năng mã hóa và giải mã hóa *tức thời* nội  dung các thư mục thuộc thư mục người dùng và các thư mục con trong đó.

Có nhiều chương trình mã hóa cho hệ điều hành **Microsoft Windows**. Chúng tôi xin giới thiệu một số chương trình sau:

* [DiskCryptor](https://diskcryptor.net/wiki/Main_Page) là giải pháp mã hóa miễn phí, nguồn mở cho phép mã hóa toàn bộ ổ đĩa bao gồm cả phân khu chứa hệ điều hành.
* [AxCrypt](http://www.axantum.com/AxCrypt/) là chương trình miễn phí nguồn mở có thể mã hóa các tệp riêng rẽ. 

Trên MS Windows 7 Utimate và Enterprise hoặc  MS Windows 8 Pro và  phiên bản Enterprise bạn có thể tìm thấy công cụ [BitLocker](http://windows.microsoft.com/en-us/windows7/products/features/bitlocker) cho phép mã hóa toàn bộ ổ đĩa. Lưu ý rằng BitLocker là phần mềm thuộc sở hữu của Microsoft, nguồn đóng, có bản quyền nên không được kiểm tra một cách độc lập để xác định mức độ bảo vệ và tính riêng tư phần mềm đảm bảo cho thông tin của bạn.

### 1.1 Những điều cần biết về công cụ này trước khi bạn bắt đầu ###

**TrueCrypt** sẽ bảo vệ dữ liệu của bạn khỏi những truy cập không mong muốn bằng cách khóa chúng bằng một mật khẩu do bạn tạo ra. Nếu bạn quên mật khẩu bạn sẽ mất khả năng truy cập những dữ liệu đó! **TrueCrypt** sử dụng việc mã hóa để bảo vệ thông tin của bạn. Nên biết rằng việc sử dụng mã hóa là bất hợp pháp ở một số quốc gia. Không chỉ mã hóa một số tệp riêng biệt, **TrueCrypt** tạo ra một vùng bảo vệ, gọi là *vùng mã hóa*, trên máy tính của bạn. Bạn có thể lưu trữ các tệp của mình một cách an toàn bên trong vùng mã hóa này. 

**TrueCrypt** cung cấp tính năng tạo vùng mã hóa chuẩn và vùng mã hóa ẩn. Cả hai loại này đều có khả năng bảo vệ thông tin mật của bạn, tuy nhiên vùng mã hóa ẩn cho phép bạn ẩn dấu những thông tin tuyệt mật đằng sau những thông tin kém phần quan trọng hơn để bảo vệ chúng trong trường hợp bạn bị bắt buộc phải mở vùng mã hóa **TrueCrypt**. Phần này sẽ hướng dẫn cụ thể các phương pháp. 


