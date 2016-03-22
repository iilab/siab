

---

lang: vi
community: guide
type: tactics
legacy: True
child: True
weight: 2
depth: 3
title: Understanding censorship circumvention

---

Nếu bạn không thể truy cập trực tiếp một trang web do nó bị chặn bởi một trong những phương thức thảo luận phía trên, bạn sẽ cần tìm một cách đi vòng qua rào cản này. Một [*máy chủ ủy quyền*](/vi/glossary#Proxy) được bảo mật, đặt tại một quốc gia không bị kiểm duyệt Internet có thể cung cấp tuyến đường vòng này bằng cách lấy nội dung các trang web mà bạn yêu cầu và chuyển chúng về cho bạn. Đứng ở góc độ [*ISP*](/vi/glossary#ISP) của bạn, bạn đơn giản là chỉ thể hiện là có kết nối bảo mật với một máy tính không xác định (chính là [*máy chủ ủy quyền*](/vi/glossary#Proxy)) ở đâu đó trên Internet.

![](/sites/securitybkp.ngoinabox.org/security/files/img/2-en.png)

Tất nhiên, cơ quan chính quyền chuyên trách kiểm duyệt Internet tại quốc gia bạn (hoặc công ty cung cấp cập nhật cho các phần mềm lọc chặn do họ phân phối) có thể biết rằng ‘máy tính không xác định’ kia chính là một [*máy ủy quyền*](/vi/glossary#Proxy) giúp vượt rào chặn. Nếu điều này xảy ra, [*địa chỉ IP*](/vi/glossary#IP_address) của nó cũng sẽ bị đưa vào [*danh sách đen*](/vi/glossary#Blacklist) và không thể dùng được nữa. Tuy nhiên thường mất một thời gian trước khi các [*máy ủy quyền*](/vi/glossary#Proxy) này bị phát hiện và bị chặn, đồng thời những người xây dựng và cập nhật các công cụ vượt rào cản này cũng nhận thức rất rõ vấn đề này. Họ thường chống lại bằng các sử dụng một hay cả hai phương thức sau:

1. **Các máy ủy quyền ẩn** thường khá khó bị phát hiện. Đây là một trong những lý do quan trọng để sử dụng các [*máy ủy quyền*](/vi/glossary#Proxy) bảo mật vì ít có nguy cơ bị lộ. Tuy nhiên [*mã hóa*](/vi/glossary#Encryption)  chỉ là một phần của giải pháp. Những người điều hành hệ thống máy ủy quyền cần phải cẩn thận khi tiết lộ thông tin vị trí cho những người dùng mới nếu họ muốn duy trì ẩn.

2. **Các máy ủy quyền dùng một lần** có thể được thay thế rất nhanh ngay khi chúng bị chặn. Trong trường hợp này, tiến trình thông báo tới người dùng cách tìm các [*máy ủy quyền*](/vi/glossary#Proxy) thay thế có thể không thực sự được bảo mật. Thay vào đó, các công cụ vượt rào chặn loại này thường đơn giản là phân bố các [*máy ủy quyền*](/vi/glossary#Proxy) mới trước khi bị chặn.

Kết quả là, khi bạn có thể sử dụng một [*máy ủy quyền*](/vi/glossary#Proxy) đáng tin cậy để truy cập dịch vụ mà bạn yêu cầu, tất cả những gì bạn phải làm là gửi các yêu cầu của bạn cho nó và hiển thị những gì mà nó trả lại bằng các ứng dụng Internet thích hợp. Thông thường, chi tiết của tiến trình này sẽ được điều khiển một cách tự động bởi phần mềm vượt rào chặn cài trên hệ thống của bạn, hay bằng cách thay đổi các thiết đặt trên trình duyệt hoặc trỏ trình duyệt của bạn tới một trang web của [*máy ủy quyền*](/vi/glossary#Proxy). Mạng ẩn danh [*Tor*](/vi/glossary#Tor), sẽ được trình bày dưới đây,  sử dụng phương thức thứ nhất. Tiếp đó là phần thảo luận về các công cụ vượt rào chặn đơn lẻ và đơn giản, hai loại này có cách làm việc hơi khác nhau.

