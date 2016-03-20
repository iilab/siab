

---

lang: vi
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 003
title: Comodo Firewall

---

**Trang chủ**

[**www.personalfirewall.comodo.com**](http://www.personalfirewall.comodo.com)


**Yêu cầu cấu hình máy tính**

- Windows 2000/XP/2003/Vista
- Yêu cầu quyền quản trị hệ thống khi tiến hành cài đặt phần mềm

**Phiên bản sử dụng trong tài liệu này**

- 5.0.16 

**Bản quyền**

- Phần mềm miễn phí

**Yêu cầu đọc thêm**

- Sách Hướng dẫn chương [**1. Làm thế nào để bảo vệ máy tính của bạn khỏi phần mềm độc hại và tin tặc**](/vi/chuong-1).

**Mức độ**: 1: Người mới bắt đầu, 2: Trung bình, 3: **Trên trung bình, 4: Có kinh nghiệm**, 5: Nâng cao

**Thời gian cần thiết để có thể sử dụng công cụ**: 60 phút

**Những lợi ích bạn sẽ có được:**

- Khả năng bảo vệ một cách nhanh chóng và hiệu quả máy tính và hệ thống mạng của bạn khỏi những đối tượng thù địch, tin tặc từ mạng Internet, phần mềm gián điệp, vi rút, và các nguy cơ khác.

- Khả năng kiểm soát mọi yêu cầu kết nối từ các chương trình cài đặt trên máy tính khi truy cập Internet, thông qua một giao diện phần mềm dễ sử dụng và cấu hình.

**Các Chương trình có Tính năng Tương tự trong GNU Linux, Mac OS và Microsoft Windows:**

**GNU/Linux** được tích hợp sẵn phần mềm tường lửa ([**netfilter/iptables**](http://www.netfilter.org/)) với cài đặt an ninh mạng rất cao. Có nhiều giao diện người dùng dễ sử dụng để điều khiển tường lửa tích hợp này, chúng tôi đặc biệt khuyên dùng [**GUFW**](https://help.ubuntu.com/community/Gufw) (**Graphical Uncomplicated Firewall**) (hãy xem [**thông tin thêm**](http://blog.bodhizazen.net/linux/firewall-ubuntu-gufw/)).

**Mac OS** có tích hợp một tường lửa mạnh mẽ đáng tin cậy có thể được điều khiển bởi các thành phần mở rộng giao diện người dùng đa dạng giúp tăng cường khả năng của tường lửa này. Trong số đó có: [**NoobProof**](http://www.hanynet.com/noobproof/) hoặc [**IPSecuritas**](http://www.lobotomo.com/products/IPSecuritas/). Với người dùng muốn tiết kiệm chi phí, chúng tôi khuyên dùng [**Little Snitch**](http://www.obdev.at/products/littlesnitch/index.html), để nâng cao tính bảo mật Internet và bảo vệ thông tin riêng tư của mình.

Bên cạnh **COMODO Firewall**,có rất nhiều các lựa chọn tốt khác cho môi trường **Microsoft Windows**. Bạn có thể thấy [**ZoneAlarm Free Firewall**](http://www.zonealarm.com/security/en-us/zonealarm-pc-security-free-firewall.htm) hay [**Outpost Firewall Free**](http://free.agnitum.com/) là những giải pháp thay thế hiệu quả.

### 1.1 Những điều cần biết về công cụ này trước khi bạn bắt đầu ###

Một tường lửa giống như một người gác cửa, hay người bảo vệ cho máy tính của bạn. Nó có một tập chính sách quy định việc cho phép thông tin đi vào và đi ra khỏi máy tính. Tường lửa là chương trình đầu tiên tiếp nhận và xử lý thông tin nhận được từ Internet và là chương trình cuối cùng quét thông tin đi ra khỏi máy tính vào mạng Internet.

Để ngăn chặn tin tặc và những kẻ xâm nhập khác tìm cách truy cập thông tin cá nhân lưu trữ trong máy tính của bạn. Đồng thời ngăn chặn các chương trình gián điệp tìm cách gửi thông tin ra Internet mà bạn không hay biết. Comodo Firewall Pro là một phần mềm tương lửa nổi tiếng. Nó được cấp phát miễn phí, nghĩa là bạn có thể sử dụng mà không phải trả tiền bản quyền. Trong những thử nghiệm gần đây, phần mềm luôn tỏ ra vượt trội so với những phần mềm yêu cầu đăng ký khác.

Sẽ cần một chút thời gian để làm quen. Để cấu hình một chương trình tường lửa đòi hỏi phải đầu tư một khoảng thời gian và công sức đáng kể nhằm đảm bảo mọi thiết đặt đều đúng đắn và phù hợp với mục đích sử dụng máy tính của bạn. Sau giai đoạn tìm hiểu ban đầu, phần mềm tường lửa sẽ hoạt động trơn tru, ít đòi hỏi sự can thiệp của bạn.

**Cảnh báo!:** Không nên truy cập Internet bằng những máy tính không có tường lửa bảo vệ. Ngay cả khi modem kết nối Internet hay các bộ định tuyến có tích hợp những tường lửa, vẫn nên có một phần mềm tường lửa được cài đặt trên máy tính của bạn.

