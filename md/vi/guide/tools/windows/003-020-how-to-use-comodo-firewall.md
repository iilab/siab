

---

lang: vi
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Use COMODO Firewall

---

Các mục trong trang này:

- [**3.0 Hướng dẫn Cho phép và Khoá các Truy cập Sử dụng COMODO Firewall**](#3.0)
- [**3.1 Hướng dẫn Mở Giao diện Chính Chương trình COMODO Firewall**](#3.1)
- [**3.2 Tổng quan về Giao diện Chính Chương trình COMODO Firewall**](#3.2)

-------

<a name="3.0"></a>
## 3.0 Hướng dẫn Cho phép và Khoá các Truy cập Sử dụng COMODO Firewall ##


Tường lửa được thiết kế để bảo vệ máy tính chống lại tin tặc và các phần mềm độc hại. Cả hai đối tượng này đều tìm cách truy cập trực tiếp máy tính của bạn hoặc gửi thông tin từ máy tính của bạn cho kẻ nào đó. **Comodo Firewall** cần phải được thiết đặt để ‘nhận biết’ những chương trình nào 'đáng tin cậy' và cho phép truy cập, và khóa tất cả những phần mềm và tiến trình bất hợp lệ trên máy tính của bạn. Có thể sẽ cần chút kinh nghiệm sau một thời gian sử dụng để phân biệt các yêu cầu hợp lệ với những yêu cầu kết nối nguy hiểm.

Mỗi khi có yêu cầu kết nối, màn hình *Cảnh bảo An ninh* sẽ xuất hiện cho phép bạn chọn *Cho phép* (Allow) hoặc *Khóa* (Block) truy cập vào hoặc ra từ máy tính của bạn tới Internet. Ví dụ dưới đây với một chương trình an toàn như *Firefox* sẽ giúp bạn làm quen với các cảnh báo của tường lửa và cách sử dụng chúng. Mặc dù đôi khi có các ngoại lệ đối với các yêu cầu truy cập xuất phát từ các trình duyệt và trình quản lý thư điện tử được sử dụng rộng rãi, mỗi lần có một yêu cầu kết nối sẽ kích hoạt một *Cảnh báo An ninh* như dưới đây:

![](/sbox/screen/comodo-en/21.png)

*Hình 1: Một ví dụ Cảnh báo An ninh của COMODO Firewall*

Một tường lửa đơn giản chỉ là tập hợp các quy tắc giám sát luồng thông tin vào và ra khỏi máy tính. Mỗi khi bạn nhấn chọn *Cho phép* (Allow) hay *Ngăn cấm* (Block) một tiến trình, **COMODO Firewall** tạo ra một quy tắc cho tiến trình hay chương trình yêu cầu kết nối. **COMODO Firewall** thực hiện tác vụ này đối với những tiến trình, chương trình mới, không nhận diện được cũng như những chương trình đã được liệt vào danh sách *Các Hãng Phần mềm Đáng tin cậy* (Trusted Software Vendors) nằm trong cửa sổ *Defense+ - Tasks > Computer Security Policy*.

**Remember my answer** (Ghi nhớ Lệnh thực hiện): Lựa chọn này được sử dụng để ghi lại lựa chọn  của bạn là cho phép hay ngăn cấm một chương trình nào đó truy cập **COMODO Firewall**.  Chương trình sẽ tự động cho phép hoặc ngăn cấm các kết nối của ứng dụng này trong các lần yêu cầu sau đó dựa trên lựa chọn hiện tại của bạn.

**Quan trọng**: Chúng tôi khuyến nghị việc tắt chọn lựa *Remember my answer option* (Ghi nhớ lệnh thực hiện) khi mới sử dụng **COMODO Firewall**. Hãy quyết định cho phép hay ngăn cấm các yêu cầu kết nối khác nhau, và tìm hiểu, quan sát ảnh hưởng của các quyết định này tới hệ thống.  Bật chọn lựa *Remember my answer* (Ghi nhớ lệnh thực hiện) khi và *chỉ* khi bạn hoàn toàn chắc chắn và hiểu rõ quyết định của mình.


**Gợi ý**: Việc giới hạn truy cập hệ thống của bạn là phương pháp tốt nhất đảm bảo an toàn cho máy tính. Đừng ngần ngại ngăn cấm bất kỳ các yêu cầu kết nối đáng ngờ hay không xác định được. Nếu việc này khiến một chương trình bình thường hoạt động không ổn định, bạn có thể cho phép kết nối được thực hiện trong lần cảnh báo tiếp theo.

**Bước 1**. **Nhấn** ![](/sbox/screen/comodo-en/26.png) để mở cửa sổ *Properties* để tìm hiểu thêm về tiến trình gốc hoặc chương trình yêu cầu truy cập, trong ví dụ này là **Firefox**:

![](/sbox/screen/comodo-en/27.png)

*Hình 2: Thông tin tiến trình firefox.exe Properties*

**Bước 2**: **Nhấn** ![](/sbox/screen/comodo-en/02.png) để đóng cửa sổ thông tin chương trình.

**Bước 3**: Nếu bạn xác định rằng một yêu cầu nào đó là không an toàn hoặc đơn giản là không chắc chắn về yêu cầu đó, dựa vào thông tin hiển thị trong cửa sổ thông tin (*Properties*), **nhấn** ![](/sbox/screen/comodo-en/29.png) để yêu cầu **COMODO Firewall** để từ chối truy cập vào hệ thống của bạn.

HOẶC:

Nếu bạn xác định một chương trình hợp lệ yêu cầu tạo kết nối không có hại dựa trên thông tin tại bảng thông tin chương trình (*Properties*), hãy **nhấn** ![](/sbox/screen/comodo-en/28.png) để cho phép chương trình đó truy cập hệ thống.


**Bước 4**. **Nhấn** ![](/sbox/screen/comodo-en/28.png) để cho phép **Firefox** truy cập hệ thống qua **COMODO Firewall**. 

**Bước 5**. Vì **Firefox** là một ứng dụng an toàn, hãy **chọn** the ![](/sbox/screen/comodo-en/30.png) để **COMODO Firewall** tự động cho phép **Firefox** truy cập hệ thống của bạn trong các lần tiếp theo.

**Lưu ý**: Nút *Allow* (Cho phép) cho phép bạn cấp quyền truy cập cho các tiến trình hay ứng dụng trong từng trường hợp cụ thể.

**Gợi ý**: **Nhấn** ![](/sbox/screen/comodo-en/31.png) để truy cập thông tin trợ giúp mở rộng trực tuyến của **COMODO Firewall**.

Khả năng đưa ra quyết định cho phép hay ngăn cấm kết nối của bạn sẽ được nâng cao khi bạn tự tin và có nhiều kinh nghiệm hơn trong quá trình sử dụng **COMODO Firewall**. 

<a name="3.1"></a>
## 3.1 Hướng dẫn Mở Giao diện Chính Chương trình COMODO Firewall ##


**COMODO Firewall** sẽ tự động khởi động sau khi quá trình cài đặt hoàn tất và khởi động lại hệ thống. Chương trình gồm một khung điều khiển với một loại tính năng và thiết đặt tùy chọn. **Người dùng Mới Bắt đầu** có thể tìm hiểu nhanh về các cảnh báo an ninh của **COMODO Firewall** security alerts, trong khi người dùng **Có kinh nghiệm** và **Nâng cao** có thể tìm hiểu sâu hơn về các cấu hình phức tạp và quản lý tường lửa.

**Lưu ý**: Tất cả các ví dụ trình bày trong phần này dựa trên chế độ **Phòng vệ Tối ưu** của **COMODO Firewall**. Có nghĩa là tính năng *Defense+* phòng chống giả mạo địa chỉ kết nối được kích hoạt. Nếu trong quá trình cài đặt **COMODO Firewall** bạn chọn lựa *Firewall only* (Chỉ riêng Firewall), tính năng *Defense+* sẽ không được kích hoạt.

Để mở cửa sổ giao diện chính  **COMODO Firewall**, hãy theo các bước sau:

**Bước 1**. **Chọn Start > Programs > Comodo > Firewall > Comodo Firewall**. 

**Lưu ý**: Một cách khác, bạn có thể **nhấn đúp chuột** vào biểu tượng chương trình trên màn hình hoặc **nhấn đúp chuột** vào biểu tượng **COMODO Firewall** trên *Khay Hệ thống* để mở cửa sổ giao diện chính chương trình. Ngoài ra, bạn có thể **nhấn chuột phải** vào biểu tượng  **COMODO Firewall** để mở trình đơn cảm ngữ cảnh sau đó chọn *Open* như sau:

![](/sbox/screen/comodo-en/35.png)

*Hình 3: Trình đơn cảm ngữ cảnh của biểu tượng kết nối COMODO Firewall*

![](/sbox/screen/comodo-en/36.png)

*Hình: Cửa sổ giao diện chính Comodo Firewall ở chế độ Tổng hợp* 

  <a name="3.2"></a>
## 3.2 Tổng quan về Giao diện Chính Chương trình COMODO Firewall ##

Cửa sổ *Firewall* hiển thị rõ ràng, chính xác thông tin chung về các yêu cầu kết nối vào và ra của các tiến trình và ứng dụng qua **COMODO Firewall**. Nhìn chung, sẽ có nhiều yêu cầu kết nối ra hơn số lượng yêu cầu kết nối tới hệ thống. Chế độ hoạt động mặc định là *Safe Mode* (An toàn), các chế độ hoạt động khác nhau sẽ được đề cập tiếp theo trong phần này. Khung *Traffic* hiển thị các tiến trình và ứng dụng đang hoạt động cũng như số lượng yêu cầu kết nối chúng tạo ra tính theo phần trăm. 

**Nhấn**![](/sbox/screen/comodo-en/37.png) để xem thông tin tổng kết tương ứng của các yêu cầu kết nối ra *tại thời điểm yêu cầu* như sau:

![](/sbox/screen/comodo-en/38.png)

*Hình 5: Cửa sổ Active Connections hiển thị chi tiết thông tin lưu lượng Internet*

**Nhấn** ![](/sbox/screen/comodo-en/39.png) xem cửa sổ *Active Connections* của các yêu cầu kết nối tới hệ thống *tại thời điểm xem*.

**Gợi ý**: **Nhấn** ![](/sbox/screen/comodo-en/40.png) để chặn tất cả các kết nối đến và ra khỏi máy tính nếu kết nối Internet của bạn tự nhiên chậm hay bị nghẽn đồng thời bạn có lý do để nghi ngờ một tiến trình hay một ứng dụng đang tự thực hiện việc tải về tự kích hoạt. Thao tác này sẽ tự động thiết đặt chế độ hoạt động của *Tường lửa * về ![](/sbox/screen/comodo-en/41.png).
Kiểm tra thông tin tổng hợp chi tiết trong cửa sổ *Active Connections* để xác định tiến trình gây ra vấn đề kết nối.

Sau khi đã giải quyết vấn đề thành công, hãy **nhấn** ![](/sbox/screen/comodo-en/42.png) để thực hiện các yêu cầu kết nối vào và ra qua **COMODO Firewall** và trở về ![](/sbox/screen/comodo-en/43.png) như bình thường.

### 3.2.1 Biểu tượng Trạng thái của COMODO Firewall  ###

**COMODO Firewall** và **Defense+** hoạt động đồng thời; nếu cả hai chương trình cùng hoạt động, chỉ thị phía trái màn hình giao diện chính sẽ xuất hiện như sau:

![](/sbox/screen/comodo-en/69.png)

*Hình 6: Biểu tượng trạng thái COMODO Firewall màu xanh*

Nếu một trong hai chương trình bị tắt, biểu tượng trạng thái sẽ chỉ rõ rằng tường lửa hoặc thành phần phòng vệ chủ động bị tắt như sau:

![](/sbox/screen/comodo-en/70.png)

*Hình 7: Biểu tượng trạng thái màu vàng COMODO Firewall bị tắt*

Tuy nhiên nếu cả hai chương trình bị tắt, biểu tượng trạng thái sẽ xuất hiện như sau:

![](/sbox/screen/comodo-en/71.png)

*Hình 8: biểu tượng trạng thái COMODO Firewall khi các thành phần bảo vệ đều bị tắt*

Trong cả hai trường hợp, hãy **nhấn** ![](/sbox/screen/comodo-en/72.png) để kích hoạt các thành phần bảo vệ tương ứng.

