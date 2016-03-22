

---

lang: vi
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 006
title: Cobian Backup - Secure File Backup

---

**Trang chủ**

[**www.educ.umu.se/~cobian /cobianbackup.htm**](http://www.educ.umu.se/~cobian/cobianbackup.htm)

**Yêu cầu cấu hình máy tính**

- XP, 2003, Vista, 2008, Windows 7 
- Windows 95, 98 và ME tương thích với Cobian [**phiên bản 7**](/sites/securitybkp.ngoinabox.org/security/files/cobian/Cb7Setup.exe)

**Phiên bản sử dụng trong tài liệu này**

- 10

**Bản quyền**

- Phần mềm miễn phí

**Yêu cầu đọc thêm**

- Sách hướng dẫn chương [5. Làm thế nào để khôi phục thông tin bị xóa](/vi/chuong-5)

**Mức độ**: 1: Người mới bắt đầu, 2: Trung bình, **3: Trên trung bình**, 4: Có kinh nghiệm, 5: Nâng cao

**Thời gian cần thiết để có thể sử dụng công cụ**: 30 phút




**Những lợi ích bạn sẽ có được:**

- Khả năng sao lưu toàn bộ tệp, thư mục tài liệu
- Khả năng nén và giải nén các tệp sao lưu
- Khả năng mã hóa và giải mã những tệp sao lưu

**Các Chương trình Tương tự Trên GNU Linux, Mac OS và Microsoft Windows:**

Việc cất giữ hay thực hiện sao lưu tài liệu, tệp hay thư mục của bạn có thể đơn giản là sao chép tệp từ vị trí này sang vị trí khác an toàn hơn; để thực hiện điều này các công cụ đặc biệt không thực sự cần thiết. Tuy nhiên, khi cần sao lưu một lượng lớn tài liệu và tệp bạn có thể thấy rất hữu ích khi sử dụng một chương trình sao lưu đặc biệt (như **Cobian Backup**) hoặc một công cụ *đồng bộ tệp*, các chương trình này đảm bảo rằng các tệp gốc hay 'nguồn' và các tệp sao lưu ở đích có cùng nội dung. Ngoài **Cobian Backup**, còn có nhiều công cụ khác giúp bạn thực hiện việc sao lưu cất giữ tài liệu; sau đây chúng tôi xin giới thiệu một số:

- [**Freebyte Backup**](http://www.freebyte.com/fbbackup/) là chương trình sao lưu miễn phí thiết kế cho **Microsoft Windows**;
- [**Unison File Synchronizer**](http://www.cis.upenn.edu/~bcpierce/unison/) chương trình nguồn mở, miễn phí cho  **Microsoft Windows, Mac OS, và GNU/Linux**;
- [**Allway Sync**](http://allwaysync.com/) là công cụ đồng bộ hóa tệp cho **Microsoft Windows** ;
- [**FreeFileSync**](http://freefilesync.sourceforge.net/) là công cụ đồng bộ hóa tệp miễn phí và nguồn mở hoạt động trên **GNU/Linux** và **Microsoft Windows**;
- [**Time Machine**](https://secure.wikimedia.org/wikipedia/en/wiki/Time_Machine_%28Mac_OS%29) là tiện ích sao lưu được phát triển bởi **Apple**, kèm theo hệ điều hành **Mac OS** (phiên bản 10.5 trở lên); và
- Người dùng **Ubuntu GNU/Linux** hãy tham khảo hướng dẫn [**Backup Your System**](https://help.ubuntu.com/community/BackupYourSystem)..

## 1.1 Những điều bạn cần biết trước khi bắt đầu ##

**Cobian Backup** được sử dụng để lưu trữ (hoặc tạo một bản sao lưu) các tệp và thư mục của bạn. Các bản sao lưu có thể được lưu ở các thư mục hay ổ đĩa khác trên máy tính của bạn, trên các máy tính khác, hay trên các máy tính trong mạng văn phòng, trên các ổ đĩa cắm ngoài như CD, DVD và USB.

**Cobian Backup** cho phép bạn thường xuyên sao lưu thư mục, tệp. Chương trình chạy ở chế độ nền trên hệ thống của bạn, kiểm tra lịch thiết đặt và thực hiện tiến trình sao lưu khi cần thiết. **Cobian Backup** cũng có thể nén và mã hóa tệp trong quá trình sao lưu.

