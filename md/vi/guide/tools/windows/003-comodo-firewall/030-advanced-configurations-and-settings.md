

---

lang: vi
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: Advanced Configurations and Settings

---

Các mục trong trang này:

- [**4.0 Hướng dẫn Truy cập cửa sổ Firewall và Defense+**](#4.0)
- [**4.1 Cửa sổ Thiết đặt Hành vi Tường lửa**](#4.1)
- [**4.2 Cửa sổ Thiết đặt Defense+**](#4.2)

-------

<a name="4.0"></a>
## 4.0 Hướng dẫn Truy cập cửa sổ Firewall và Defense+ ##

Màn hình giao diện chính chương trình **COMODO Firewall** chia thành hai khung chính,  khung *Firewall* và *Defense+*. 

![](/sbox/screen/comodo-vi/80.png)

*Hình 1: Cửa sổ giao diện chính chương trình COMODO Firewall hiển thị hai khung Firewall và Defense+*

Cửa sổ *Firewall Behavior Settings* (Các Thiết đặt Hành vi Tường lửa) và *Defense+ Settings* (Các Thiết đặt Phòng vệ) có thể được mở bằng cách **nhấn** ![](/sbox/screen/comodo-vi/43.png) trong khung tương ứng.

Một cách khác, bạn có thể mở hai cửa sổ trên theo các bước sau:

**Bước 1**. **Mở** cửa sổ giao diện chính chương trình **COMODO Firewall**. 

**Bước 2**. **Nhấn** 

![](/sbox/screen/comodo-vi/60.png) hoặc ![](/sbox/screen/comodo-vi/81.png)

để mở các khung *Firewall Tasks* hay *Defense+  Tasks* tương ứng.

**Bước 3**. **Nhấn**  

![](/sbox/screen/comodo-vi/82.png) hoặc ![](/sbox/screen/comodo-vi/83.png) 

để mở khung *Firewall Behavior Settings* (Thiết đặt Hành vi Tường lửa) hay *Defense+ Settings* (Thiết đặt Phòng vệ) tương ứng.


**Gợi ý**: *Firewall Security Level* (Mức An ninh Tường lửa), *Defense+ Security Level* (Mức An ninh Phòng vệ) và *Sandbox Security Level* (Mức An ninh Cách ly) sẽ được đề cập cụ thể trong các phần tiếp theo,  có thể được thiết đặt dễ dàng nhanh chóng thông qua biểu tượng kết nối **COMODO Firewall** nằm trên *Khay Hệ thống*. **Nhấn chuột phải** vào biểu tượng kết nối để kích hoạt trình đơn điều khiển và các mục trình đơn con như sau:

![](/sbox/screen/comodo-vi/84.png)

*Hình 2: Trình đơn điều khiển với  mục trình đơn con Mức An ninh Tương lửa của biểu tượng kết nối* 


<a name="4.1"></a>
## 4.1 Cửa sổ Thiết đặt Hành vi Tường lửa ##

Cửa sổ *The Firewall Behavior Settings** cho phép bạn thay đổi an ninh tương lửa bằng thông qua các tùy chọn và tính năng khác nhau bao gồm mức an ninh tường lửa, số lượng cảnh báo an ninh tường lửa, phan tích và giám sát gói thông tin.

![](/sbox/screen/comodo-vi/44.png)

*Hình 3: Cửa sổ Thiết đặt Hành vi Tường lửa - Khung Thiết đặt Tổng quát*

Khung *Thiết đặt Tổng quát* cho phép bạn xác định mức độ an ninh phù hợp của **COMODO Firewall**. Thanh trượt cho phép bạn điều chỉnh mức độ an ninh trong các tùy chọn sau:

**Block All** (Cấm Tất cả): Ở chế độ này, tường lửa sẽ chặn toàn bộ các kết nối liên quan tới Internet và ghi đè toàn bộ các cấu hình và quy tắc đã xác định trước đó. Tường lửa sẽ không tạo ra các quy tắc kết nối cho ứng dụng hay ghi nhớ hoặc 'học' hành vi mới.

**Custom Policy** (Chính sách Tùy biến): Chế độ này áp dụng *riêng* các chính sách an ninh và lưu thông mạng của **COMODO Firewall** do người dùng định nghĩa trong cửa sổ *Firewall Tasks > Network Security Policy* và *Defense+ Tasks > Computer Security Policy*.

**Safe Mode** (Chế độ An toàn): Đây là chế độ mặc định của **COMODO Firewall**, gồm thành phần *Optimum Proactive Defense* và *Maximum Proactive Defense*.

**Gợi ý**: **COMODO Firewall** lưu danh sách các ứng dụng và tệp thường xuyên hoạt động trên hệ thống đã được kiểm tra an toàn và không đưa ra các cảnh báo an ninh với những ứng dụng này.

**Cảnh báo**: Cả hai chế độ *Training Mode* và *Disabled Mode* đều không được khuyên sử dụng bởi chúng có thể không đảm bảo hiệu quả của tường lửa **COMODO Firewall** khiến hệ thống gặp nguy hiểm.

<a name="4.2"></a>
### 4.2 Cửa sổ Thiết đặt Defense+ ###

**Lưu ý**: Để nắm rõ các tính năng và tùy chọn được giới thiệu trong phần này đòi hỏi kiến thức sâu về tường lửa cũng như các vấn đề an ninh liên quan do được thiết kế dành chủ yếu dành cho người dùng **Nâng cao**.

**Quan trọng**: Nếu bạn nhấn chọn tùy chọn *Firewall with Optimum Proactive Defense* hay *Firewall with Maximum Proactive Defense* trong lúc cài đặt **COMODO Firewall**, *Defense+* hệ thống phòng ngừa giả mạo kết nối sẽ tự động được kích hoạt. Tuy nhiên, nếu bạn chỉ chọn tùy chọn *Firewall Only* thì tính năng *Defense+* vẫn có thể được kích hoạt một cách thủ công khi cần thiết. Tính năng *Defense+* cần phải được kích hoạt để có thể sử dụng mọi tính năng giới thiệu dưới đây.
  

Thành phần *Defense+* của **COMODO Firewall** là hệ thống phòng ngừa giả mạo kết nối. Về mặt kỹ thuật, bất kỳ máy tính nào trong mạng đều được coi là một máy chủ. Thành phần *Defense+* liên tục theo dõi các hoạt động của các tệp thực thi trên hệ thống của bạn. Một tệp thực thi có thể là một hay một phần của ứng dụng hay chương trình và thường nhưng không nhất thiết có đuôi mở rộng dạng: *.bat*, *.exe*, *.dll*, *.sys*, và một số loại khác.

*Defense+* đưa ra các hộp thoại cảnh báo mỗi khi có một tệp thực thi không xác định chuẩn bị kích hoạt đồng thời đưa ra cho bạn các lựa chọn cho phép hay ngăn cấm tệp đó kích hoạt. Điều này rất hữu ích trong tình huống các chương trình độc hại tìm cách cài đặt lên hệ thống nhằm đánh cắp thông tin của bạn, xóa sạch ổ cứng hay xâm nhập điều khiển nhằm sử dụng máy tính của bạn để phát tán phần mềm độc hại hay quảng cáo mà bạn không hề hay biết.
 

### 4.2.1 Thiết đặt Defense+ - Khung Thiết đặt Tổng quát ###

Để tự kích hoạt thành phần *Defense+* và mở cửa sổ *Thiết đặt Defense+*, hãy theo các bước sau:

**Bước 1**. **Nhấn** khung *Defense+* trong màn hình giao diện chính chương trình **COMODO Firewall** sau đó **nhấn** ![](/sbox/screen/comodo-vi/50.png) để mở cửa sổ sau:

![](/sbox/screen/comodo-vi/51.png)

*Hình 4: Cửa sổ Defense+ với khung Thiết đặt Tổng quát mặc định*

**Bước 2**. **Kéo** thanh trượt lên mức *Safe Mode* và **nhấn** ![](/sbox/screen/comodo-vi/06.png) để kích hoạt thành phần *Defense+* như trong  *Hình 6*.

*Mức An ninh Defense+* giống với *Mức An ninh Tương lửa* (*Firewall Behavior Security Level*) với các tùy chọn tương tự, cho phép bạn sử dụng một thanh trượt để xác định mức tối ưu cho phòng ngừa giả mạo kết nối máy chủ cho máy tính của bạn.


**Paranoid Mode**(Chế độ Cảnh báo): Đây là mức an ninh cao nhất và sẽ theo dõi tất cả các tệp thực thi bất kỳ không thuộc danh sách các tệp đã được bạn xác nhận là an toàn, kể cả những tệp thuộc danh sách *Trusted Software Vendor* (Các Hãng Phần Mềm Tin cậy). Hệ thống sẽ đưa ra số lượng lớn cá cảnh báo an ninh, đồng thời các hoạt động hệ thống sẽ được kiểm tra thông qua các thiết đặt cấu hình.


**Safe Mode**(Chế độ An toàn): Ở chế độ này, hệ thống sẽ tự 'học' các hành vi tương ứng với các tệp thực thi khác nhau đồng thời giám sát các hoạt động quan trọng của máy tính. Mỗi khi một ứng dụng không được xác nhận tìm cách thực thi, hệ thống sẽ tạo ra một *Cảnh báo An ninh*. Chúng tôi khuyên dùng chế độ này cho hầu hết người dùng.

- Tùy chọn *Block all unknown requests if the application is closed* (Cấm tất cả các yêu cầu kết nối khi đóng ứng dụng) sẽ tự động khóa tất cả các yêu cầu của những ứng dụng và chương trình không rõ nguồn gốc cũng như không được khai báo trong *Chính sách An ninh Máy Tính* (*Computer Security Policy*).

- Tùy chọn *Deactivate the Defense+ permanently (Requires a system restart)* cho phép bạn tắt hẳn tính năng phòng ngừa giả mạo kết nối máy chủ *Defense+*. Chúng tôi khuyên *không* nên nhấn chọn chọn lựa này.

### 4.2.2 Thiết đặt Defense+ - Khung Thiết đặt Điều khiển Thực thi (Execution Control Settings tab) ###

Khung *Execution Control Settings* giới hạn khả năng truy cập tài nguyên máy tính đối với những tệp đáng ngờ hoặc không rõ nguồn gốc và đưa chúng vào phân tích.

![](/sbox/screen/comodo-vi/54.png)

*Hình 5: Khung Thiết đặt Điều khiển Thực thi Defense+*

**Gợi ý**: Người dùng **Nâng cao** có thể loại trừ các tiến trình không mong muốn kể trên bằng cách **nhấn** ![](/sbox/screen/comodo-vi/55.png) để mở khung *Exclusions* (Loại trừ) sau đó tìm và chọn các tiến trình hay ứng dụng cần loại bỏ.


**Lưu ý**: Người dùng **Có Kinh nghiệm** và **Nâng cao** hãy  **chọn** ![](/sbox/screen/comodo-vi/47.png) để truy cập trợ giúp mở rộng **COMODO** trực tuyến về  *Execution Control Settings*, *Sandbox Settings* và *Monitoring Settings*. Một cách khác, bạn có thể truy cập địa chỉ [**http://help.comodo.com/topic-72-1-155-1074-Introduction-to-Comodo-Internet-Security.html**](http://help.comodo.com/topic-72-1-155-1074-Introduction-to-Comodo-Internet-Security.html) để chọn danh sách các chủ đề cần trợ giúp

.




