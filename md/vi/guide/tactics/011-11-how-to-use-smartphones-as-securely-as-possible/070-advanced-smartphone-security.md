

---

lang: vi
community: guide
type: tactics
legacy: True
child: True
weight: 7
depth: 3
title: Advanced Smartphone Security

---

## Tạo quyền truy cập đầy đủ vào điện thoại thông minh của bạn ##

Hầu hết các điện thoại thông minh có nhiều tính năng hơn những gì hệ điều hành cài đặt sẵn, các phần mềm của nhà sản xuất (phần mềm lớp giữa), hay các chương trình của nhà cung cấp dịch vụ điện thoại cho phép. Nhiều chức năng bị ‘khóa’ một cách nghịch lý khiến người dùng không thể sử dụng hoặc thay thế các tính năng này, và chúng tồn tại ngoài tầm kiểm soát của người dùng. Trong hấu hết các trường hợp, những tính năng này không thực sự cận thiết cho người dùng điện thoại thông minh. Tuy nhiên có những tính năng và ứng dụng có thể nâng cao tính bảo mật cho dữ liệu và kết nối trên điện thoại thông minh. Đồng thời có những tính năng cài đặt sẵn cần được gỡ bỏ để tránh các nguy cơ bảo mật.

Vì điều này và những lý do khác, nhiều người dùng điện thoại thông minh chọn cách can thiệp và cài đặt các phần mềm và chương trình lên điện thoại thông minh của họ để đạt được quyền truy cập đầy đủ cho phép họ cài đặt một số chức năng nâng cao hay gỡ bỏ hoặc giảm bớt những tính năng khác.

Tiến trình thực hiện việc vượt qua các hạn chế của hệ điều hành cài đặt bởi các nhà cung cấp dịch vụ mạng hay nhà sản xuất trên điện thoại thông minh được gọi là ‘mở khóa’ ‘rooting’ (đối với các thiết bị Android) và jailbreaking ( trong thường hợp các thiết bị dùng iOS, như iPhone hay iPad). Thông thường, việc mở khóa thành công sẽ cho bạn toàn quyền truy cập để có thể cài đặt và sử dụng các ứng dụng bổ sung, cho phép thay đổi các cấu hình trước khi mở khóa không thể thực hiện được, và toàn quyền kiểm soát việc lưu trữ dữ liệu và thẻ nhớ của điện thoại thông minh.

**CẢNH BÁO**: Việc mở khóa (Rooting hay jailbreaking) có thể là quá trình không khôi phục lại trạng thái cũ được, và thường yêu cầu kinh nghiệm về cài đặt và cấu hình phần mềm. Hãy cân nhắc kỹ các điều sau trước khi tiến hành ‘mở khóa’:

- Sẽ có rủi ro khiến điệnt thoại của bạn không thể hoạt động được nữa, hay ‘mất hết chức năng’.

- Bảo hành của nhà sản xuất hay nhà cung cấp dịch vụ di động có thể bị từ chối.

- Ở một số nơi, việc mở khóa phần mềm là phạm pháp.

Tuy nhiên, nếu bạn thực hiện cẩn thận, việc mở khóa thiết bị là cách trực tiếp để có quyền kiểm soát chiếc điện thoại thông minh của bạn và khiến nó trở nên an toàn hơn. 

### Phần mềm Lớp giữa Thay thế ###

Nếu bạn sở hữu điện thoại Android, bạn có thể cân nhắc cài đặt thay thế phần mềm lớp giữa để tăng cường thêm khả năng kiểm soát chiếc điện thoại của mình. Hãy lưu ý rằng đề có thể cài đặt phần mềm lớp giữa thay thế, bạn cần trước hết phải có quyền truy cập tối đa bằng việc ‘mở khóa’ điện thoại của mình.

Một ví dụ về phần mềm lớp giữa thay thế cho điện thoại Android là [**Cyanogenmod**](http://www.cyanogenmod.com) cho phép bạn, lấy một ví dụ, gỡ bỏ các ứng dụng ở mức hệ thống trên điện thoại của bạn (ví dụ các ứng dụng được cài bởi nhà sản xuất hoặc nhà cung cấp dịch vụ di động). Bằng cách đó, bạn có thể giảm bớt nguy cơ thiết bị của mình bị theo dõi, như khả năng tự động gửi dữ liệu tới nhà cung cấp dịch vụ mà bạn không hề hay biết. 

Hơn thế nữa, Cyanogenmod mặc định có cài đặt săn ứng dụng OpenVPN, ứng dụng này có thể khá khó để tự cài đặt. VPN ( mạng riêng ảo) là một trong các cách bảo mật định tuyến kết nối Internet của bạn (hãy xem bên dưới). 

Cyanogenmod đồng thời cung cấp chế độ truy cập Incognito, với chế độ này lịch sử liên lạc của bạn không được lưu lại trên điện thoại.

Cyanogenmod bao gồm nhiều tính năng khác. Tuy nhiên phần mềm lớp giữa này không được hỗ trợ bởi mọi thiết bị Android, vì vậy trước khi thực hiện cài đặt, hãy kiểm tra [**danh sách các thiết bị hỗ trợ**](http://www.cyanogenmod.com/devices).

### Mã hóa toàn bộ các ổ đĩa ###

Nếu điện thoại của bạn đã được ‘mở khóa’, bạn có thể cân nhắc việc mã hóa toàn bộ thiết bị lưu trữ dữ liệu hoặc tạo một vùng nhớ trên điện thoại để bảo vệ một số thông tin trên đó.
 [**Luks Manager**](http://www.whispersys.com/) cho phép việc mã hóa tức thời đơn giản các vùng nhớ với giao diện người dùng rất thân thiện. Chúng tôi hết sức khuyến nghị bạn sử dụng công cụ này trước khi lưu trữ dữ liệu trên chiếc điện thoại Android của mình và sử dụng Ổ đĩa Mã hóa được tạo bởi Luks Manager để lưu trữ dữ liệu của mình.

Dự án Whisper Systems đang phát triển ứng dụng [**WhisperCore**](http://www.whispersys.com/whispercore.html) cho phép mã hóa toàn bộ thiết bị Android của bạn.

### Mạng Riêng Ảo (VPN) ###

Một kết nối VPN cung cấp một kênh mã hóa qua mạng Internet giữa thiết bị của bạn và máy chủ VPN. Kênh này được gọi là đường hầm, vì không giống như các kênh truyền mã hóa khác, như https, kênh này ẩn toàn bộ ccs dịch vụ, giao thức và nội dung. Một đường hầm VPN được thiết lập một lần và tồn tại đến khi bạn quyết định tắt kết nối đó.

Hãy lưu ý, do luồng dữ liệu của bạn sẽ đi qua máy chủ trung chuyển hay máy chủ VPN, bên thứ ba chỉ cần truy cập được vào máy chủ này để phân tích theo dõi các hoạt động liên lạc của bạn. Vì vậy một điều quan trọng là phải chọn cẩn thận nhà cung cấp dịch vụ máy chủ trung chuyển và VPN. Một điều nên thực hiện là sử dụng các máy chủ trung gian và/hoặc máy chủ VPN vì việc phân tán luồng dữ liệu sẽ giúp giảm nguy cơ bị ảnh hưởng bởi một dịch vụ đã bị kiểm duyệt.

Chúng tôi giới thiệu sử dụng máy chủ [**RiseUp VPN**](https://help.riseup.net/en/vpn). Bạn có thể sử dụng máy chủ VPN RiseUp trên thiết bị Android sau khi cài đặt Cyanogenmod (xem phía trên). Việc thiết lập kết nối tới máy chủ RiseUp VPN cho điện thoại iPhone cũng khá dễ dàng – hãy xem thêm [tại đây](https://support.apple.com/kb/HT1424).


