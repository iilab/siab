

---

lang: vi
community: guide
type: tactics
legacy: True
child: False
weight: 008
title:  8. How to remain anonymous and bypass censorship on the Internet

---

Nhiều nước trên thế giới đã cài đặt những chương trình ngăn chặn những người dùng Internet trong nước không được truy cập một số trang web và dịch vụ trên Internet. Các công ty, trường học và thư viện công cộng thường sử dụng những phần mềm tương tự để bảo vệ nhân viên, học sinh và độc giả của họ khỏi những nguy cơ mà họ cho là có ảnh hưởng xấu. Các kỹ thuật chặn thông tin kiểu này tồn tại dưới nhiều dạng. Một số chặn một trang web dựa trên [*địa chỉ IP*](/vi/glossary#IP_address) của trang web đó, một số khác đưa vào danh sách đen những [*tên miền*](/vi/glossary#Domain_name)  nhất định hoặc tìm kiếm trên toàn bộ những kết nối không được mã hóa để kiểm tra những từ khóa đặc biệt.

Cho dù là kỹ thuật lọc chặn nào được sử dụng, gần như là luôn có cách tránh được chúng dựa vào những hệ thống trung gian, phía bên ngoài quốc gia bạn, để sử dụng những dịch vụ bị chặn. Việc này được gọi là sự vượt qua *sự kiểm duyệt*, hay đơn giản là [*vượt rào cản*](/vi/glossary#Circumvention), và những máy tính trung gian gọi là các [*máy ủy quyền*](/vi/glossary#Proxy)(proxy). Những [*máy ủy quyền*](/vi/glossary#Proxy) này cũng có rất nhiều loại. Chương này bao gồm một phần thảo luận ngắn gọn về mạng lưới hệ thống [*máy ủy quyền*](/vi/glossary#Proxy) nặc danh và tiếp đó là những miêu tả chi tiết hơn về các máy ủy quyền [*vượt rào cản*](/vi/glossary#Circumvention) và cách thức chúng hoạt động.

Cả hai phương pháp này đều là những cách hiệu quả để vượt qua những bộ lọc chặn Internet, dù phương pháp đầu sẽ thích hợp hơn nếu bạn sẵn sàng hi sinh chút tốc độ để đổi lại sự nặc danh cho các hoạt động trên Internet của mình. Trong trường hợp bạn biết và tin tưởng những cá nhân hay tổ chức vận hành hệ thống [*máy ủy quyền*](/vi/glossary#Proxy) mà bạn lựa chọn, hoặc tốc độ truy cập cần thiết hơn là sự nặc danh, thì những  [*máy ủy quyền*](/vi/glossary#Proxy) [*vượt rào cản*](/vi/glossary#Circumvention) sẽ tốt hơn cho bạn.

### Tình huống cơ bản ###

<div class="background" markdown="1">
Mansour và Magda là hai anh em ở một đất nước nói tiếng Ả rập. Họ có một trang web cá nhân nơi họ công bố một cách nặc danh những xâm phạm và các chiến dịch về nhân quyền nhằm tác động thay đổi chính trị. Chính quyền sở tại không thể đóng cửa trang web của họ bởi vì nó được đăng ký tại một quốc gia khác, nhưng họ luôn tìm cách xác định danh tính của những người quản trị trang web thông qua các nhà hoạt động chính trị khác. Mansour và magda rất lo ngại rằng chính quyền có thể theo dõi các hoạt động cập nhật của họ và tìm ra họ là ai. Thêm nữa, họ muốn chuẩn bị cho tình huống chính quyền thực tế sẽ chặn trang web của họ, để không những vẫn có thể tiếp tục cập nhật trang web đồng thời cung cấp một hướng dẫn vượt rào cản hiệu quả cho người đọc trong nước có nguy cơ bị chặn truy cập vào trang web. </div>

### Những điều bạn có thể học được từ chương này ###

- Làm sao để truy cập một trang web bị chặn truy cập trong nước

- Làm sao để tránh một trang web bạn viếng thăm có thể biết được địa điểm của bạn

- Làm sao để chắc chắn rằng cả Nhà cung cấp dịch vụ Internet (ISP) và cơ quan kiểm duyệt ở nước bạn không thể xác định được địa chỉ trang web hay dịch vụ Internet mà bạn viếng thăm

