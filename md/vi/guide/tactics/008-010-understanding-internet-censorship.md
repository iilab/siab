

---

lang: vi
community: guide
type: tactics
legacy: True
child: True
weight: 1
depth: 3
title: Understanding Internet censorship

---

Nghiên cứu được thực hiện bởi những tổ chức như [*OpenNet Initiative*](http://opennet.net/) và [Reporters Without Borders (RSF)](http://www.rsf.org/) chỉ ra rằng rất nhiều quốc gia thực hiện chặn lọc nội dung thông tin trên một lĩnh vực rộng về xã hội, chính trị và ‘an ninh quốc gia’, trong khi ít có bản danh sách cụ thể về nội dung nào bị lọc chặn được công bố. Một lẽ đương nhiên là những người tìm cách kiểm soát sự truy cập Internet của công dân nước họ sẽ tìm mọi cách để khóa những hệ thống máy ủy quyền và các trang web mà họ cho rằng cho phép và hướng dẫn mọi người vượt qua các rào chắn trên.

Cho dù sự đảm bảo về tự do truy cập thông tin được ghi nhận tại Mục 19, Bản Tuyên Ngôn về Nhân Quyền, số lượng các quốc gia áp dụng kiểm duyệt thông tin Internet ngày càng tăng nhanh trong vài năm trở lại đây. Do sự hiện diện của việc lọc chặn Internet mở rộng khắp nơi trên thế giới, các công cụ vượt rào chặn cũng được xây dựng, triển khai và phổ biến và được sử dụng rộng rãi bởi các nhà hoạt động chính trị, những lập trình viên và các tình nguyện viên.

Trước khi khám phá các cách vượt qua sự kiểm duyệt Internet, trước hết bạn cần tìm hiểu căn bản cách hoạt động của những hệ thống lọc chặn này. Để làm điều đó, sẽ có ích khi chúng ta xem xét một mô hình đơn giản hóa sơ đồ kết nối tới Internet của bạn.

### Kết nối Internet của bạn ###


![](/sites/securitybkp.ngoinabox.org/security/files/img/1-en.png)

Đoạn đầu của kết nối tới Internet của bạn thường đi qua một Nhà cung cấp dịch vụ Internet [*ISP*](/vi/glossary#ISP) từ nhà bạn, văn phòng, trường học, thư viện hay quán café Internet. Nhà cung cấp dịch vụ này tiếp đó gán cho máy tính của bạn một [*địa chỉ IP*](/vi/glossary#IP_address) , địa chỉ này sẽ được các dịch vụ Internet khác nhau sử dụng để xác định địa chỉ của bạn và truyền thông tin như thư điện tử hay các trang web mà bạn yêu cầu. Bất kỳ ai biết [*địa chỉ IP*](/vi/glossary#IP_address)  của bạn đều có thể dò ra thành phố nơi bạn đang ở. Một số cơ quan chức năng thậm chí có thể xác định chính xác vị trí của bạn từ những thông tin này.

- **Nhà cung cấp dịch vụ Internet** của bạn sẽ biết tòa nhà nơi bạn đang truy cập Internet hoặc đường dây điện thoại nào bạn đang sử dụng để truy cập Internet qua một modem.

- **Quán Internet café, thư viện hay cơ quan** sẽ biết bạn đã sử dụng máy tính nào trong một khoảng thời gian xác định cũng như bạn đã được kết nối qua cổng hay thiết bị không dây nào.

- **Các cơ quan chính quyền** có thể biết những thông tin trên, sử dụng ảnh hưởng của họ tới những đơn vị trên.

Tiếp theo, [*Nhà cung cấp dịch vụ*](/vi/glossary#ISP) của bạn sẽ dựa vào cơ sở hạ tầng mạng tại quốc gia để kết nối người sử dụng trong nước, trong đó có bạn, với phần còn lại của thế giới. Ở phía đầu bên kia của kết nối, trang web hay dịch vụ Internet mà bạn truy cập cũng có một tiến trình tương tự, nhận [*địa chỉ IP*](/vi/glossary#IP_address) của riêng mình từ Nhà cung cấp dịch vụ [*ISP*](/vi/glossary#ISP) tại quốc gia nó được lưu trữ. Thậm chí không cần những chi tiết kỹ thuật cụ thể, mô hình đơn giản hóa này sẽ có ích cho việc cân nhắc những công cụ khác nhau cho phép bạn vượt qua những bộ lọc chặn và duy trì tính nặc danh của mình trên Internet.

### Các trang web bị chặn như thế nào ###

Để truy cập một trang web bạn phải gửi [*địa chỉ IP*](/vi/glossary#IP_address)  của trang web đó cho [*ISP*](/vi/glossary#ISP) của bạn và yêu cầu họ kết nối bạn với [*ISP*](/vi/glossary#ISP) của máy chủ cung cấp dịch vụ web đó. Và nếu bạn sử dụng một kết nối Internet không bị lọc chặn, việc kết nối sẽ được thực hiện chính xác như vậy. Tuy nhiên, nếu bạn ở một quốc gia có thực hiện việc kiểm duyệt Internet, thì đầu tiên nó sẽ đối chiếu **danh sách đen** chứa các trang web bị cấm để quyết định có thực hiện yêu cầu của bạn hay không.
Trong nhiều trường hợp, chính các [*ISP*](/vi/glossary#ISP) đóng vai trò là trung tâm của cơ quan kiểm duyệt. Và thường các danh sách đen chứa các [*tên miền*](/vi/glossary#Domain_name) , dạng www.blogger.com thay vì các [*địa chỉ IP*](/vi/glossary#IP_address). Ở nhiều quốc gia các phần mềm lọc chặn sẽ theo dõi những kết nối của bạn thay vì chỉ khóa chặn một số địa chỉ Internet nhất định. Các phần mềm này sẽ quét toàn bộ những yêu cầu mà bạn gửi và nội dung những trang gửi ngược lại cho bạn, để dò tìm những từ khóa nhạy cảm và đưa ra quyết định xem có để bạn nhận được kết quả yêu cầu hay không.

Và để làm cho vấn đề thêm tồi tệ, một trang web bị chặn mà bạn có thể không hề hay biết. Trong khi một số hệ thống chặn một ‘trang web bị cấm’ chúng có đưa ra lý do tại sao trang web đó bị kiểm duyệt, số còn lại chỉ hiện thị những thông báo lỗi không chính xác, ví dụ như không thể tìm thấy trang web hay địa chỉ trang web không chính xác.

Nhìn chung, sẽ là đơn giản nhất khi nghiên cứu một một tình huống xấu nhất liên quan đến sự kiểm duyệt Internet hơn là việc tìm hiểu chi tiết điểm mạnh, yếu của từng kỹ thuật lọc chặn được sử dụng ở quốc gia bạn. Nói cách khác, chúng ta sẽ giả sử rằng:

- Lưu thông Internet của bạn bị kiểm duyệt theo từ khóa

- Việc lọc chặn được thực hiện trực tiếp tại các [*ISP*](/vi/glossary#ISP)

- Các trang web bị liệt vào **danh sách đen** gồm cả [*địa chỉ IP*](/vi/glossary#IP_address)một số địa chỉ Internet nhất định. Các phần mềm này sẽ quét toàn bộ những yêu cầu mà bạn gửi và nộ và [*tên miền*](/vi/glossary#Domain_name) của chúng

- Bạn có thể nhận được những thông báo không rõ ràng hay không chính xác về lý do trang web bị chặn không được thể hiện

Do những công cụ vượt rào cản hiệu quả nhất có thể được sử dụng cho mọi phương pháp chặn lọc đang sử dụng, sẽ không nguy hại gì khi đưa ra những giả sử bi quan như trên.

<div class="background" markdown="1">
Mansour: vậy nếu một ngày đẹp trời nào đó anh không thể truy cập được vào trang web cá nhân của mình, nhưng bạn của anh ở nước ngoài vẫn có thể vào được bình thường, thì liệu có phải là do chính quyền đã chặn nó rồi không?

Magda: Chưa hẳn là như vậy. Có một số vấn đề chỉ ảnh hưởng tới những người truy cập trang web từ ở trong nước. Cũng có thế do máy tính của anh có trục trặc gì đó chỉ hiển thị một số trang web nhất định. Tuy nhiên anh đang đi đúng hướng đấy. Anh cũng có thể thử truy cập trang web đó sử dụng một số công cụ vượt rào cản. Hầu hết những công cụ này sử dụng những máy chủ ủy quyền nằm ở nước ngoài nên việc này cũng giống như là nhờ bạn anh ở nước ngoài vào thử trang web cho anh vậy, chỉ khác một điều là anh tự thực hiện lấy việc này. </div>

