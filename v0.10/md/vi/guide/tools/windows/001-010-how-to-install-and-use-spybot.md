

---

lang: vi
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: How to Install and Use Spybot

---

Các mục trong chương này:

- [**2.0 Hướng dẫn Cài đặt Spybot**](#2.0)
- [**2.1 Thông tin Spybot**](#2.1)
- [**2.2 Hướng dẫn khởi động Spybot Lần đầu**](#2.2)
- [**2.3 Hướng dẫn Cập nhật Luật Dò tìm và Cơ sở dữ liệu phòng ngừa của Spybot**](#2.3)
- [**2.4 Hướng dẫn tạo hệ miễn dịch cho hệ thống**](#2.4)
- [**2.5 Hướng dẫn Kiểm tra Lỗi**](#2.5)
- [**2.6 Trình thường trú TeaTimer**](#2.6)
- [**2.7 Hướng dẫn sử dụng Công cụ Phục hồi (Recovery Tool)**](#2.7)

-------
<a name="2.0"></a>
## 2.0 Hướng dẫn Cài đặt Spybot ##

**Bước 1**. **Nhấn đúp chuột** vào ![](/sbox/screen/spybot-vi/01.png); hộp thoại *Open File - Security Warning* có thể xuất hiện. Nếu vậy, **nhấn** ![](/sbox/screen/spybot-vi/02.png) để mở cửa sổ sau:

![](/sbox/screen/spybot-vi/03.png)

*Hình 1: Cửa sổ chọn ngôn ngữ cài đặt*

**Bước 2**. **Nhấn** ![](/sbox/screen/spybot-vi/04.png) để mở cửa sổ Thuật sỹ trợ giúp cài đặt *Setup - Spybot Password Safe – Welcome to the Spybot - Search & Destroy Setup Wizard*.

**Bước 3**. **Nhấn** ![](/sbox/screen/spybot-vi/05.png) để mở cửa sổ thông tin bản quyền  *License Agreement*. Hãy đọc kỹ  *Thông tin bản quyền*  trước khi tiếp tục quá trình cài đặt.

**Bước 4**. **Nhấn chọn** ô *I accept the agreement* để hiện nút *Next*, sau đó **nhấn** ![](/sbox/screen/spybot-vi/05.png) để mở cửa sổ *Select Destination Location* (Chọn Vị trí Cài đặt).

**Bước 5**. **Nhấn** ![](/sbox/screen/spybot-vi/05.png) để kích hoạt cửa sổ:

![](/sbox/screen/spybot-vi/06.png)

*Hình 2: Cửa sổ Chọn các Thành phần Cài đặt*


**Bước 6**. **Chọn** các thành phần cài đặt phù hợp như trong *Hình 2* phía trên, và **nhấn** ![](/sbox/screen/spybot-vi/05.png) để mở *Select Start Menu Folder* 

**Bước 7**. **Nhấn** ![](/sbox/screen/spybot-vi/05.png) để chọn đường dẫn thư mục mặc định, và mở cửa sổ *Select Additional Tasks*.

**Bước 8**. **Nhấn** ![](/sbox/screen/spybot-vi/05.png) để mở khung *Ready to Install*và **nhấn** ![](/sbox/screen/spybot-vi/07.png) để kích hoạt cửa sổ *Installing*.

**Bước 9**. **Nhấn** ![](/sbox/screen/spybot-vi/08.png) để hoàn thành quá trình cài đặt và khởi động chương trình **Spybot - Search & Destroy**. 

<a name="2.1"></a>
## 2.1 Thông tin Spybot ##

Có hai bước cần tiến hành để sử dụng **Spybot** hiệu quả:

- Cập nhật thường xuyên các **Chính sách Dò tìm** và **Cơ sở Dữ liệu Phòng ngừa** từ **Spybot**.

- Kích hoạt **Spybot**. Việc này bao gồm quá trình tạo *hệ miễn dịch* cho hệ thống sử dụng các chính sách dò tìm và cơ sở dữ liệu phòng ngừa cũng như những gói cập nhật mới tải về, sau đó quét kiểm tra hệ thống để tìm những phần mềm độc hại và xóa chúng.

**Lưu ý**: Để tham khảo nhanh những lựa chọn nâng cao quan trọng, xin xem phần [**3.0 Những lựa chọn Nâng cao**](/vi/spybot_chedonangcao)

## 2.1 Hướng dẫn khởi động Spybot lần đầu ##

*Sau khi bạn hoàn thành việc cài đặt, **Spybot** *sẽ tự khởi động và hiển thị cửa sổ ‘Thông tin Lưu ý’* như sau*: 

![](/sbox/screen/spybot-vi/09.png)

*Hình 3: Hộp thoại thông tin cảnh báo hợp lệ* 

**Lưu ý**: Để kích hoạt **Spybot** trong lần tiếp theo, có thể **nhấn đúp chuột** vào biểu tượng ![](/sbox/screen/spybot-vi/10.png) trên màn hình hoặc **chọn Start > All Programs > Spybot - Search & Destroy > Spybot - Search & Destroy.**

**Bước 1**. **Nhấn** ![](/sbox/screen/spybot-vi/11.png) để kích hoạt màn hình *Trợ giúp cài đặt Spybot* và *Tạo sao lưu registry* như sau:

![](/sbox/screen/spybot-vi/12.png)

*Hình 4: Cửa sổ Trợ giúp tạo sao lưu registry Spybot-S&D*

**Lưu ý**: Chúng tôi khuyên bạn nên tạo bản sao của registry. **Windows Registry** được trình bày tại [**Hướng dẫn sử dụng Ccleaner**](//securityinabox.org/vi/ccleaner_windowsregistry#4.0).

**Bước 2**. **Nhấn** ![](/sbox/screen//spybot-vi/14.png) trong *Hình 4* để tạo và sao lưu cơ sở dữ liệu hệ thống Windows của bạn.

**Bước 3**. **Nhấn** ![](/sbox/screen/spybot-vi/15.png) để mở cửa sổ *Cập nhật Spybot* *Spybot - Search for Updates*. Nếu bạn đang kết nối Internet, hãy thực hiện bước sau:

**Bước 4**. **Nhấn** ![](/sbox/screen/spybot-vi/16.png) để mở cửa sổ *Search for Updates*, và chuyển tới mục [**2.3 Hướng dẫn Cập nhật Luật Dò tìm và Cơ sở dữ liệu phòng ngừa của Spybot**](#2.3). 

- Nếu *không* có kết nối Internet, hãy theo bước sau.

**Bước 5**. **Nhấn** ![](/sbox/screen/spybot-vi/17.png) để mở cửa sổ *Immunize this system*, và  thực hiện phòng ngừa cho hệ thống như sau: 

![](/sbox/screen/spybot-vi/18.png) 

*Hình 5: Thanh trạng thái tiến trình tạo sự phòng ngừa* 

**Lưu ý**: Nếu vì lý do gì đó bạn đang mở một trình duyệt, cửa sổ sau sẽ xuất hiện trước khi tiến trình phòng ngừa bắt đầu: 

![](/sbox/screen/spybot-vi/19.png)

*Hình 6: Cửa sổ Phát hiện Trình duyệt đang Hoạt động* 

**Bước 6**. **Đóng** tất cả các trình duyệt đang mở và **nhấn** ![](/sbox/screen/spybot-vi/04.png) để thực hiện quá trình tạo sự phòng ngừa cho hệ thống.

**Bước 7**. **Nhấn** ![](/sbox/screen/spybot-vi/15.png) sau đó **nhấn** ![](/sbox/screen/spybot-vi/22.png) để trở về cửa sổ chính *Spybot - Search & Destroy* trong chế độ *Immunize*. 

![](/sbox/screen/spybot-vi/13.png)

*Hình 8: Giao diện chính của Spybot - Search & Destroy*

<a name="2.3"></a>

## 2.3. Hướng dẫn Cập nhật Chính sách tìm diệt và Cơ sở dữ liệu Phòng ngừa của Spybot ##

**Quan trọng:** Việc đảm bảo **Spybot** luôn cập nhật là hết sức quan trọng.

**Bước 1: Nhấn** ![](/sbox/screen/spybot-vi/23.png) ở phía tay trái trên trình đơn để mở cửa sổ *Spybot-S&D Updater* chứa danh sách các trang web có chứa các bản cập nhật.

**Bước 2: Nhấn chọn** máy chủ gần bạn nhất và **nhấn chuột phải** vào đó và **chọn** **Set this server as the preferred download location* như trong *Hình 9*.

- Nếu bạn mới cập nhật chương trình, một cửa sổ thông báo **Không có cập nhật mới nào** sẽ xuất hiện.

- Nếu chương trình của bạn chưa được cập nhật, màn hình *Cập nhật Spybot-S&D* sẽ liệt kê danh sách các máy chủ cung cấp những gói cập nhật cần thiết như bên dưới đây:

![](/sbox/screen/spybot-vi/24.png)

*Hình 9: Cửa sổ Cập nhật Spybot-S&D*

**Bước 3**. **Nhấn** ![](/sbox/screen/spybot-vi/25.png) để mở *Spybot-S&D Updater - Please select the updates to download here*.

**Bước 4**. **Chọn** toàn bộ những lựa chọn được hiển thị, và **nhấn** ![](/sites/securitybkp.ngoinabox.org/security/vi/spybot/12.png) để thực hiện việc cập nhật.

![](/sbox/screen/spybot-vi/27.png)

*Hình 10: Cửa sổ Spybot-S&D Updater hiển thị các luật dò tìm, tệp trợ giúp và cơ sở dữ liệu phòng chống*

**Lưu ý**: Nếu có lỗi xuất hiện trong quá trình cập nhật, **Spybot** sẽ cho phép bạn thực hiện lại. Sau khi quá trình cập nhật hoàn thành, bạn sẽ được yêu cầu tạo hệ miễn dịch cho hệ thống và kiểm tra hệ thống để tìm những phần mềm độc hại như sau:

![](/sbox/screen/spybot-vi/28.png)

*Hình 11: Cửa sổ Thông tin*

**Bước 6**. **Nhấn** ![](/sbox/screen/spybot-vi/04.png), sau đó **nhấn** ![](/sbox/screen/spybot-vi/29.png).

*Bạn sẽ quay trở lại màn hình chính Spybot – Search & Destroy*

**Lưu ý**: Bạn có thể thực hiện việc cập nhật **Spybot** bất kỳ lúc nào bằng cách **chọn: Start &gt; All Programs &gt; Spybot-Search&Destroy &gt; Update Spybot-S&D**.

<a name="2.4"></a>
## 2.4 Hướng dẫn tạo hệ miễn dịch cho hệ thống ##

**Spybot** giúp bảo vệ máy tính của bạn khỏi những chương trình gián điệp đã được nhận dạng bằng cách tạo **hệ miễn dịch**. Quá trình này cũng tương tự việc tiêm phòng vắc xin phòng chống những bệnh dịch mới.

Để tạo hệ miễn dịch cho máy tính của bạn, hãy thực hiện những bước sau:

**Bước 1. Nhấn** ![](/sbox/screen/spybot-vi/30.png) trên trình đơn Spybot-S&D hoặc or ![](/sbox/screen/spybot-vi/31.png) để tự động quá trình tạo hệ miễn dịch như trong *Hình 6* bên trên.

You may need to maximise your window to view all the different protections applied in the *Immunize* pane. 

Có thể bạn cần mở rộng toàn màn hình để có thể hiển thị toàn bộ lựa chọn trong khung *Immunize*.

**Bước 2. Nhấn** ![](/sites/securitybkp.ngoinabox.org/security/vi/spybot/16.png) và đợi đến khi tiến trình hoàn thành.
Hệ thống của bạn đã được miễn dịch khỏi những phần mềm độc hại đã được nhận dạng.

**Lưu ý**: Bạn có thể hủy bỏ quá trình tạo hệ miễn dịch hệ thống nếu bạn cho rằng quá trình này ảnh hưởng đến tốc độ máy tính của bạn. Bạn có thể nhấn ![](/sbox/screen/spybot-vi/32.png) để hủy bỏ tiến trình tạo hệ miễn dịch và khôi phục hệ thống về trạng thái trước đó.

<a name="2.5"></a>
## 2.5 Hướng dẫn Kiểm tra tìm diệt phần mềm độc hại ##

**Lưu ý** Trước khi tiến hành quá trình tìm diệt, hãy cập nhật *chính sách tìm diệt* và *cơ sở dữ liệu phòng ngừa* của **Spybot**.

Để kiểm tra tìm diệt những phần mềm độc hại, hãy thực hiện các bước sau:

**Bước 1**. **Nhấn** ![](/sbox/screen/spybot-vi/33.png) để mở khung  **Spybot** *Search and Destroy*.

**Bước 2**. **Nhấn** ![](/sbox/screen/spybot-vi/34.png) để thực hiện việc tìm diệt (nếu bạn có một lượng lớn dữ liệu, tệp, chương trình… quá trình này có thể mất 20 phút tới một giờ). Cửa sổ chương trình **Spybot** sẽ xuất hiện như dưới đây: 

![](/sbox/screen/spybot-vi/35.png)

*Hình 12: Chương trình Spybot - Search & Destroy đang phát hiện các nguy cơ* 

**Bước 3**. **Nhấn** ![](/sbox/screen/spybot-vi/36.png) để bắt đầu việc kiểm tra lỗi trong hệ thống như sau:

![](/sbox/screen/spybot-vi/37.png)

*Hình 13: Chương trình Spybot - Search & Destroy đang phát hiện các nguy cơ* 

*Sau khi quá trình tìm diệt hoàn thành, danh sách các nguy cơ được liệt kê trong cửa sổ như dưới đây*:

![](/sbox/screen/spybot-vi/38.png)

*Hình 14: Màn hình Spybot - Search & Destroyhiển thị những nguy cơ tìm thấy* 

**Bước 4**. Chỉ **chọn** những mục bạn dự định sẽ xóa. Có một số mục liệt kê ở đây là những chương trình quảng cáo bạn có thể muốn giữ lại (vì bất kỳ lý‎ do gì).

**Gợi ý**: Những mục được hiện thị bằng màu đỏ thường được cho là những nguy cơ. Những mục màu xanh thực hiện theo dõi việc sử dụng Internet của bạn. Để giữ lại một mục nào đó, hãy nhấn bỏ hộp chọn lựa tương ứng và nó sẽ không bị xóa.

**Quan trọng:** Trước khi bạn xóa hay bỏ qua một mối nguy cơ được tìm thấy bởi Spybot, chúng tôi khuyên bạn nên tìm hiểu về hành vi và xuất xứ của nó.

**Bước 5. Nhấn:** ![](/sbox/screen/spybot-vi/39.png) bên phía tay phải màn hình kết quả tìm kiếm để tìm hiểu thêm về mục được lựa chọn. Nếu không có thông tin nào được hiển thị, bạn có thể tìm kiếm trên Internet. Tìm hiểu cách thức hoạt động và ảnh hưởng của nguy cơ đó tới sự toàn vẹn và an ninh của hệ thống. Hiểu rõ về các mối nguy cơ sẽ giúp tăng cường bảo mật cho bạn.

![](/sbox/screen/spybot-vi/40.png)

*Hình 15: Cửa sổ hiển thị thông tin về nguy cơ của Spybot-S&D*

**Bước 6 . Nhấn** ![](/sbox/screen/spybot-vi/41.png) để thực hiện xóa.

*Một hộp thoại xác nhận xuất hiện để chắc chắn bạn muốn xóa toàn bộ những nguy cơ tìm thấy.*

**Bước 7. Nhấn** nút *Yes* nếu bạn muốn xóa chúng.

***Lưu ý***: Bạn nên thực hiện kiểm tra tìm diệt hàng tuần.

<a name="2.6"></
## 2.5 Chương trình thường trú Teatimer ##

Chương trình thường trú **Teatimer** là thành phần **Spybot** liên tục hoạt động ở chế độ nền (ngay cả khi bạn không mở cửa sổ **Spybot**). Nó liên tục giám sát những tiến trình hệ thống quan trọng để đảm bảo rằng không có những nguy cơ thay đổi những thiết đặt quan trọng trong hệ thống. **TeaTimer** cảnh báo người dùng mỗi khi nó phát hiện những tiến trình lạ có hành động đáng nghi ngờ, và đưa ra lựa chọn *Cho phép* (*Allow*) hay *Từ chối* (*Deny*) thực hiện tiến trình đó (nếu tiến trình đó được xác nhận là độc hại). Ví dụ màn hình cảnh bảo như sau:

![](/sbox/screen/spybot-vi/42.png)

*Hình 16: Màn hình cảnh báo của Spybot-S&D TeaTimer, hiển thị lựa chọn Cho phép/Từ chối*

Trường hợp có nhiều chương trình (cả những chương trình thiết yếu lẫn những chương trình độc hại) yêu cầu truy cập những tiến trình hệ thống, **TeaTimer** sẽ liên tục hỏi bạn *Đồng ý* hay *Từ chối*. Lấy ví dụ chương trình **Skype** được gỡ khỏi trình đơn **Khởi động Windows**. Việc này xảy ra mỗi khi một chương trình được gỡ bỏ khỏi hệ thống (và thông báo này không nhất thiết chỉ xuất hiện tại thời điểm hệ thống khởi động). Trong trường hợp này, đây là một yêu cầu thực tế cần thay đổi một thiết đặt hệ thống và bạn có thể chọn đồng ý.

**Gợi ý**: Nếu bạn không chắc chắn phải làm gì với cửa sổ xác nhận của **TeaTimer**, *Nhấn** nút ![](/sbox/screen/spybot-vi/43.png) để tìm hiểu thêm.

![](/sbox/screen/spybot-vi/44.png)

*Hình 17: Cửa sổ thông tin của Trình thường trú của Spybot-S&D*

Sẽ an toàn hơn nếu bạn từ chối yêu cầu khi bạn không chắc chắn về ảnh hưởng của nó. Trong trường hợp đây là một yêu cầu hợp lệ, hãy chọn hộp chọn **Ghi nhớ lựa chọn này** và Spybot sẽ không hiển thị thông báo đối với yêu cầu này nữa.

**Lưu ý**: Bạn sẽ thấy trình thường trú **TeaTimer** được kích hoạt ngay khi bạn cài đặt thêm một chương trình mới và tự thêm vào danh sách các chương trình được kích hoạt tại thời điểm khởi động của Windows. Cũng tương tự như vậy mỗi khi bạn gỡ bỏ một chương trình khỏi hệ thống.

**Gợi ý**: Chúng tôi khuyên bạn nên cập nhật **TeaTimer** mỗi khi có phiên bản mới.

<a name="2.7"></a>
## 2.7 Hướng dẫn sử dụng công cụ Khôi phục ##

Công cụ *khôi phục* cho phép bạn phục hồi lại những thành phần vừa bị xóa hoặc thay đổi. Điều này có thể thực hiện được là nhờ **Spybot** luôn tạo bản sao cho mọi thành phần mà nó xóa. Nếu xóa một chương trình lạ khiến hệ thống của bạn hoạt động bất bình thường, bạn có thể khôi phục nó sử dụng công cụ Khôi phục.

Để khôi phục một thành phần bị xóa bởi Spybot, hãy thực hiện nhưng bước sau:

**Bước 1**. **Nhấn** ![](/sbox/screen/spybot-vi/45.png) để mở cửa sổ *Khôi phục* (*Recovery*)  như dưới đây:

![](/sbox/screen/spybot-vi/46.png)

*Hình 18: Màn hình Khôi phục – Spybot Search & Destroy*
 
**Bước 2**. Từ danh sách những thành phần đã bị xóa, **chọn** những thành phần bạn muốn khôi phục và **nhấn**: ![](/sbox/screen/spybot-vi/47.png).

*Một hộp thoại xác nhận sẽ xuất hiện như sau:*

![](/sbox/screen/spybot-vi/48.png)

*Hình 19: The Confirmation dialog box*

**Bước 3**. **Nhấn** ![](/sbox/screen/spybot-vi/49.png) để khôi phục những thành phần được chọn. 

**Bước 4.** Một cách khác, nhấn  ![](/sbox/screen/spybot-vi/50.png)  để xóa những tệp được chọn một cách vĩnh viễn. Các thành phần được xóa triệt để sẽ không thể khôi phục được nữa.

