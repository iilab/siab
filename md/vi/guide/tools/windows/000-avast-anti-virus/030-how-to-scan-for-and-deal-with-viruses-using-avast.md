

---

lang: vi
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: How to Scan for and Deal with Viruses Using avast!

---

Những mục trong trang này:

- [**4.0 Trước khi Bắt đầu**](#4.0)
- [**4.1 Hướng dẫn cơ bản để Đối phó với Sự bùng phát Vi rút**](#4.1)
- [**4.2 Giới thiệu chung về Cửa sổ Giao diện Chính avast!**](#4.2)
- [**4.3 Hướng dẫn Quét tìm Phần mềm độc hại (Malware) và Virút**](#4.3)
- [**4.4 Hướng dẫn Thực hiện tác vụ Quét Tổng thể**](#4.4)
- [**4.5 Hướng dẫn Thực hiện tác vụ Quét Thư mục**](#4.5)
- [**4.6 Hướng dẫn Thực hiện Quét tại Thời điểm Khởi động**](#4.6)
- [**4.7 Đối phó với Vi rút**](#4.7)
- [**4.8 Hướng dẫn Sử dụng Virus Chest (Vùng Cách ly Vi rút)**](#4.8)
- [**4.9 Các Phương pháp Diệt Vi rút Nâng cao**](#4.9)
- [**4.10 Quét Thông minh**](#4.9)

----

<a name="4.0"></a>

### 4.0 Trước khi Bắt đầu ###

Có hai phần cơ bản khi đối phó với phần mềm độc hại và các loại vi rút máy tính khác trong **avast!**. Thứ nhất là quét tìm để xác định các mối đe dọa đó. Phần tiếp theo là xóa hoặc di chuyển các chương trình độc hại đó vào *Vùng Cách ly Vi rút* (*Virus Chest*) của **avast!**. Việc Xóa hoặc/và di chuyển các mã độc hại và virút vào *Vùng Cách ly Vi rút* giúp ngăn ngừa một cách có hiệu quả ảnh hưởng của chúng đối với hệ thống, ví dụ như lây nhiễm tệp hệ thống hoặc các chương trình thư điện tử.

Việc lưu giữ mã độc hại hay virút trong *Vùng Cách ly* có vẻ là hành động bất bình thường. Tuy nhiên, nếu các mã độc đó lây nhiễm các thông tệp tin quan trọng, nhạy cảm thì có thể bạn sẽ muốn khôi phục các tệp và tài liệu bị lây nhiễm này càng nhiều càng tốt. Ví dụ trong một số trường hợp hiếm gặp, **avast!** có thể xác định nhầm các đoạn mã và chương trình hợp lệ là mã độc hay virút. Những đoạn mã hay chương trình này có thể quan trọng trong hệ thống và bạn muốn khôi phục chúng.

**Vùng Cách ly Vi rút** (**Virus Chest**) của **avast!** là một 'vùng nhớ quân sự ' hay 'bị phong tỏa', nơi bạn có thể nghiên cứu một vi rút và xác định tính chất phá hoại của nó bằng cách tìm hiều thông tin trên Internet hoặc gửi mẫu virút đó cho một trung tâm nghiên cứu virút - lựa chọn này có sẵn trong **avast!** khi bạn nhấn chuột phải vào một vi rút nằm trong danh sách ở *Vùng Cách ly Virút*. Nhấn đúp chuột vào một virút trong *Vùng Cách ly Virút*  sẽ không kích hoạt hoặc thực thi mã độc hay vi rút đó bởi vì *Vùng Cách ly Virút* đã được cách ly với phần còn lại của hệ thống. 

**Gợi ý**: Bạn có thể chuyển những dữ liệu quan trọng, nhạy cảm vào **Vùng Cách ly Vi rút** của **avast!** để bảo vệ thông tin đó khỏi bị nhiễm virút.

<a name="4.1"></a>

### 4.1. Hướng dẫn cơ bản để Đối phó với Sự bùng phát Vi rút ##
 
Có một số đề phòng cần thực hiện để giảm nguy cơ lây nhiễm mã độc vào máy tính của bạn; ví dụ như  thường xuyên sử dụng các chương trình diệt virút hay chống phần mềm gián điệp như **avast!** hoặc **Spybot** được cập nhật, tránh truy cập các trang web không rõ nguồn gốc hoặc đáng ngờ, hoặc hết sức chấp hành việc cảnh giác khi cắm các thiết bị lưu trữ di động vào máy tính của bạn. Hãy tham khảo các bước trong phần [**Phòng chống lây nhiễm vi rút**](/vi/chuong_1_1) của chương 1. [**Làm thế nào để bảo vệ máy tính của bạn khỏi phần mềm độc hại và tin tặc**](/vi/chuong-1). Tuy nhiên, dù cẩn thận, chúng ta đôi khi vẫn thấy máy tính của mình bị nhiễm vi rút. Những điểm lưu ý dưới đây giúp bạn đối phó với sự tấn công của vi rút:

- Ngắt kết nối - vật l‎ý - khỏi Internet hay mạng nội bộ. Nếu bạn kết nối không dây, ngắt kết nối mạng không dây. Nếu có thể, hãy tắt hoặc tháo card mạng không dây ra khỏi máy. Bạn nên ngắt kết nối khỏi mạng Internet cho tất cả các máy trong mạng nội bộ chia sẻ với máy tính của bạn.

- Thực hiện việc quét vi rút tại thời điểm khởi động đối với tất cả các máy trong mạng. Ghi lại tên tất cả vi rút tìm thấy, để có thể tìm hiểu thêm về chúng - sau đó xóa, hoặc di chuyển chúng vào *Vùng Cách ly Vi rút* của **avast!**. Để tìm hiểu cách quét vi rút tại thời điểm khởi động, xem phần [**4.6 Hướng dẫn thực hiện tác vụ Quét tại Thời điểm Khởi động**](/vi/avast_doiphovirut#4.6).

- Ngay cả khi đã chọn xóa hoặc sửa tệp nhiễm virút, hãy thực hiện lại các bước trên, và quét vi rút tại thời điểm khởi động cho **tất cả** các máy tính, cho đến khi **avast!** không còn hiển thị các cảnh báo. Tùy thuộc vào mức độ nghiêm trọng của cuộc tấn công của virút bạn có thể cần thực hiện việc quét virút tại thời điểm khởi động hơn một lần.  

Để tìm hiểu thêm về việc đối phó với sự lây lan mã độc hoặc virút, hãy xem phần [**4.9 Các Phương pháp Diệt Virút Nâng cao**]/vi/avast_doiphovirut#4.9).

<a name="4.2"></a>

### 4.2 Giới thiệu chung về Cửa sổ Giao diện Chính avast! ###

Cửa sổ giao diện chính của **avast!** gồm một số khung nằm bên trái: SUMMARY (TỔNG KẾT), SCAN COMPUTER (QUÉT MÁY TÍNH), REAL-TIME SHIELDS (CÁC BỘ BẢO VỆ THỜI GIAN THỰC) và MAINTENANCE (BẢO TRÌ). Các khung *Scan*, *Tools* và *Settings* gồm các trình đơn các lệnh được thảo luận bên dưới đây.

Để mở Cửa sổ giao diện chính người dùng **avast!** **Nhấn** ![](/sbox/screen/avast-vi-1/22.png) từ khay hệ thống (thường nằm ở góc dưới bên phải màn hình).

![](/sbox/screen/avast-vi-1/56.png)

*Hình 1:  Cửa sổ chính giao diện người dùng* 

Dưới đây là mô tả ngắn gọn các tính năng của các khung và trình đơn con:

**Overview:** (Tổng quan): Trang giao diện người dùng hiển thị trạng thái làm việc của **avast!**

**Scan:**  Khung này có thể được sử dụng để thực hiện các tùy chọn quét khác nhau bao gồm:

- *Smart scan* có thể thực hiện việc quét bên dưới từng lệnh một;
- *Các phương pháp quét vi rút như:* *Quick scan* (Quét nhanh), *Full System scan* (Quét toàn bộ hệ thống), *Removable Media scan* (Quét các thiết bị lưu trữ lưu động), *Select folder* (Quét thư mục chọn) và *Boot-time scan* (Quét tại thời điểm khởi động) – được hướng dẫn chi tiết phía bên dưới.

- *Scan for outdated software*; Quét kiểm tra các phần mềm không cập nhật.

- *Scan for network threats* - (Quét các mối đe dọa trong mạng) có thể kiểm tra các cấu hình an ninh trên thiết bị định tuyến của bạn và đưa ra các khuyến nghị thiết đặt bạn có thể cần cập nhật.

- *Scan for performance issues* – (Quét các vấn đề về hiệu năng hoạt động hệ thống) – tính năng này chỉ hoạt động đầy đủ cho phiên bản thương mại của avast!;

**Tools** (Công cụ): Khung này chứa các tính năng công cụ bao gồm *Software Update* (Cập nhật phần mềm), *Browser Cleanup* (Dọn sạch trình duyệt), và *Rescue Disk* (Tạo đĩa khẩn cấp) như đã hướng dẫn trong Mục 3.2 [**Các cộng cụ Mở rộng avast!**](/avast_huongdantucapnhat#3.2)

**Settings:** Khung này chứa các tính năng bao gồm *General* (Tổng quát), *Active Protection* (Bảo vệ Chủ động), *Antivirus* (Diệt vi rút), *Update* (Cập nhật) như mô tả dưới đây:

- **General** bao gồm một mục về 'Bảo trì' là nơi bạn có thể thực hiện việc cấu hình *Logs* (ghi nhật ký chương trình), *Virus Chest size* (Kích thước Vùng cách ly vi rút) và history (lược sử hoạt động chương trình).

- **Active Protection** là tính năng cho phép bạn cấu hình việc quét các *File System* (Tệp Hệ thống), *Mail* (Thư điện tử), *Web*. **Hãy lưu ý** rằng chúng tôi khuyến nghị không thay đổi các thiết đặt mặc định trừ khi bạn hiểu rõ các tác động của việc thay đổi tắt/bật các tùy chọn đặc biệt này.

- **Antivirus** cho phép bạn cấu hình tổng quá về tác vụ quét bao gồm *Exclusions* (Ngoại lệ quét), và *Alert* (Cảnh báo).

- **Update** hiển thị  các *Chương trình* và *Cơ sở dữ liệu vi rút* đã được cài đặt và cho phép việc cập nhật thủ công cho cả hai thành phần này như mô tả trong Mục 3.1 [**Hướng dẫn Tự Cập nhật Avast!**](/avast_huongdantucapnhat#3.1)


<a name="4.3"></a>

### 4.3 Hướng dẫn Quét tìm Mã độc và Virút ###

Trong phần này bạn sẽ tìm hiểu các phương pháp quét tìm. Bạn cũng sẽ học các thực hiện một tác vụ quét tổng thể hệ thống hay quét từng thư mục hoặc quét ngay khi khởi động hệ thống.

Khung *Scan*  có năm lựa chọn quét tìm của **avast!**; để mở cửa sổ này, hãy thực hiện:

**Bước 1**. **Nhấn** ![](/sbox/screen/avast-vi-1/57.png) 

**Bước 2**. **Nhấn** ![](/sbox/screen/avast-vi-1/95.png) để mở cửa sổ sau:

![](/sbox/screen/avast-vi-1/96.png)

*Hình 2: Khung Scan hiển thị tùy chọn mặc đinh Quét nhanh*

Phần hướng dẫn dưới đây giúp bạn chọn tùy chọn quét phù hợp:

**Quick scan** (**Quét nhanh**): Lựa chọn này được khuyên dùng với những người dùng có ít thời gian để quét tìm các chương trình có hại trong hệ thống.

**Full system scan** (**Quét toàn bộ hệ thống**): Nên dùng lựa chọn này nếu bạn có thời gian để thực hiện việc quét toàn bộ hệ thống hoặc trong lần đầu quét tìm vi rút cho máy tính. Thời gian để hoàn tất quá trình quét này sẽ phụ thuộc vào số lượng tài liệu, tệp tin, và dung lượng ổ cứng cũng như tốc độ của máy tính. Hãy tham khảo phần [**4.4 Hướng dẫn Thực hiện Quét Toàn bộ Hệ thống**](/avast_doiphovirut#4.4).

**Removable media scan** (**Quét các ổ đĩa ngoài**): Lựa chọn này dùng để quét các ổ đĩa ngoài, thẻ nhớ USB, và các thiết bị lưu trữ khác, nhất là các ổ đĩa không phải của bạn. Tính năng này cho phép quét tìm các chương trình độc hại có khả năng tự động chạy khi ổ đĩa được cắm vào máy tính.

**Select folder to scan** (**Chọn thư mục quét**): Sử dụng lựa chon này khi bạn muốn quét tìm một thư mục riêng hoặc một nhóm các thư mục đặc biệt khi bạn biết rõ hoặc nghi ngờ rằng các thư mục hoặc tệp nào đó đã bị nhiễm virút. Hãy xem phần [**4.5 Hướng dẫn quét Thư mục**](/avast_doiphovirut#4.5).

**Boot-time scan** (*Quét vào thời điểm khởi động*): Quét tị thời điểm khởi động cho phép bạn thực hiện việc quét toàn bộ ổ đĩa trước khi hệ điều hành **Microsoft Windows** chạy. Tùy chọn này được khuyên dùng để quét toàn bộ máy tính của bạn và thực hiện việc quét này cần khá nhiều thời gian. Hãy tham khảo mục [**4.6 Hướng dẫn Thực hiện việc Quét tại Thời điểm Khởi động**](/vi/avast_doiphovirut#4.6)

**Gợi ý**: **Nhấn** ![](/sbox/screen/avast-vi-1/59.png) cho phép bạn tìm hiểu cụ thông tin cụ thể về các phương pháp quét, ví dụ như các vùng nhớ nào sẽ được quét.

<a name="4.4"></a>
### 4.4 Hướng dẫn Thực hiện Quét Toàn bộ Hệ thống ###

**Bước 1**. **Chọn** tùy chọn quét *Full system scan* trong trình đơn (xem hình 2 phía trên).

**Bước 2**. Nhấn ![](/sbox/screen/avast-vi-1/60.png) để mở cửa sổ sau:

![](/sbox/screen/avast-vi-1/61.png)

*Hình 3: Khung Quét hiển thị Quét toàn bộ hệ thống/ đang thực hiện quét...* 

Sau khi quá trình quét toàn bộ hệ thống hoàn thành, và nếu phát hiện có nguy cơ, khung *Full system scan* (quét toàn bộ hệ thống) có thể xuất hiện như sau:

![](/sbox/screen/avast-vi-1/62.png)

*Hình 4: Khung Quét hoàn thành  hiển thị các tệp bị lây nhiễm được phát hiện* 

Nếu quá trình quét toàn bộ hệ thống phát hiện ra các mối nguy cơ,  **nhấn vào** ![](/sbox/screen/avast-vi-1/69.png) để mở cửa sổ kết quả quét. Hãy tham khảo mục [**4.7 Hướng dẫn Đối phó với Vi rút**](/avast_doiphovirut#4.7) để tìm hiểu thêm:

<a name="4.5"></a>
### 4.5 Hướng dẫn Thực hiện Quét Thư mục ###


**Bước 1**. **Chọn** *Select folder to scan* từ trình đơn (Xem hình 2 phía trên).

**Bước 2**. **Nhấn** ![](/sbox/screen/avast-vi-1/60.png) để mở cửa sổ sau:

![](/sbox/screen/avast-vi-1/63.png)

*Hình 5: Hộp thoại hướng dẫn chọn vùng quét*


Hộp thoại *Select the areas* hướng dẫn bạn chọn thư mục muốn quét. Bạn có thể chọn nhiều hơn một thư mục để quét. Khi bạn nhấn chọn các ô chọn bên cạnh mỗi thư mục, đường dẫn của thư mục đó sẽ được hiển thị trong trường *Selected paths*.

**Bước 3**. **Nhấn** ![](/sbox/screen/avast-vi-1/64.png) để bắt đầu quét các thư mục đã chọn, khung tiến trình sẽ hiện lên như sau:

![](/sbox/screen/avast-vi-1/64.png)

*Hình 6: Tiến trình quét thư mục* 

**Gợi ý**: **avast!** cho phép bạn chọn từng thư mục riêng rẽ theo trình đơn cảm ngữ cảnh của **Windows** xuất hiện khi nhấn phải chuột vào một thư mục. **Chọn** ![](/sbox/screen/avast-vi-1/66.png)  ở gần tên thư mục nếu bạn muốn thực hiện quét tìm vi rút cho thư mục này.

Nếu việc quét thư mục tìm thấy bất kỳ nguy cơ nào, hãy **nhấn vào** ![](/sbox/screen/avast-vi-1/69.png) để mở trang kết quả. Hãy tham khảo mục [**4.7 Hướng dẫn Đối phó với Vi rút**](/avast_doiphovirut#4.7) để thực hiện các hành động tiếp theo.

<a name="4.6"></a>
### 4.6 Hướng dẫn Quét tại Thời điểm Khởi động ###

Tính năng quét tại thời điểm khởi động của **avast!** cho phép bạn quét kiểm tra toàn bộ ổ cứng hệ thống trước khi **Hệ điều hành Microsoft Windows** bắt đầu chạy. Tại thời điểm đó, hầu hết các mã độc và các chương trình phá hoại cũng như vi rút vẫn chưa hoạt động, đúng vậy, chúng chưa có cơ hội để tự kích hoạt hay tương tác với các tiến trình khác. Vì lý do đó, chúng dẽ dàng bị phát hiện và xóa bỏ.
Tiến trình quét tại thời điểm khởi động truy cập trực tiếp vào hệ thống ổ đĩa không qua các trình điều khiển của hệ điều hành **Windows** nơi mà thường bị tấn công bởi các chương trình độc hại. Do đó sẽ phát hiện các 'rootkit' gan lỳ nhất - rootkit là tên gán cho một số chương trình phá hoại nguy hiểm. 

Chúng tôi **hết sức khuyến nghị** thực hiện quét tại-thời-điểm-khởi-động ngay cả khi có nghi ngờ nhỏ rằng máy tính của bạn bị tấn công hay lây nhiễm.  *Boot-time Scan* (*Quét tại thời điểm khởi động*)  và đĩa cứu hộ khẩn cấp (được đề cập trong mục 3.2.3 Đĩa Khẩn cấp) là các tùy chọn quét đầy đủ  và toàn diện nhất của avast! cho máy tính của bạn. Quét tại thời điểm khởi động có thể cần thời gian, tùy thuộc vào tốc độ máy tính và lượng dữ liệu cũng như số ổ đĩa trên hệ thống của bạn. 

Để quét máy tính tại thời điểm khởi động, hãy theo các bước sau:

**Bước 1**. **Nhấn** ![](/sbox/screen/avast-vi-1/57.png) để mở khung *Scan*.

**Bước 2**. **Nhấn** ![](/sbox/screen/avast-vi-1/67.png) từ trình đơn xổ xuống.

**Bước 3**. **Nhấn** ![](/sbox/screen/avast-vi-1/60.png) để chọn thực hiện việc quét trong lần máy tính khởi động lần tới.

**Bước 4**. **Khởi động máy tính của bạn** để bắt đầu thực hiện việc quét.

**Chú ý**: Tiến trình quét tại thời điểm khởi động sẽ được thực hiện trước khi hệ điều hành và giao diện đồ họa hoạt động; vì vậy, giao diện chương trình sẽ là màn hình ký tự màu xanh như sau:
 
![](/sbox/screen/avast-vi-1/68.png) 

*Hình 7: Tiến trình quét tại thời điểm khởi động của avast!*

**avast!** sẽ thông báo mỗi khi phát hiện một vi rút. Bạn chọn các hành động phù hợp bằng cách ấn các phím số tương ứng trên bàn phím. Chúng tôi khuyên bạn ấn phím số 2 *Fix all automatically* (Sửa tự động mọi lỗi) và để cho avast!  xử các vi rút tìm thấy.

 Hãy lưu ý rằng việc di chuyển các tệp nhiễm vi rút vào vùng cách ly hoặc xóa tệp có thể gây ra việc một số tính năng thông tin của hệ thống không thực hiện được, khi một tệp hệ thống quan trọng bị lây nhiễm vi rút, việc di chuyển tệp vào vùng cách ly có thể khiến máy tính của bạn không thể khởi động được nữa.
 
<a name="4.7"></a>
## 4.7 Hướng dẫn Đối phó với Vi rút ###

Mục 4.5 và 4.6 phía trên hướng dẫn cách sử dụng avast! để quét vi rút. Khi tìm thấy vi rút với những phương pháp quét trên, avast! sẽ thông báo cho bạn như trong *hình 8*. Để bắt đầu việc xử lý các vi rút hay mã độc tìm thấy trong quá trình quét, hãy thực hiện các bước sau:

![](/sbox/screen/avast-vi-1/100.png)

*Hình 8: Quá trình Quét hoàn thành – phát hiện nguy cơ*

**Bước 1**. **Nhấn** ![](/sbox/screen/avast-vi-1/69.png) để mở cửa sổ:

![](/sbox/screen/avast-vi-1/70.png)

*Hình 9: Cảnh báo PHÁT HIỆN NGUY CƠ! trong cửa sổ SCAN RESULTS*

**Bước 2**. Để mở danh sách xổ-xuống chứa các hành động tương ứng, **nhấn** vào mũi tên bên dưới *Actions* như sau:

![](/sbox/screen/avast-vi-1/72.png)

*Hình 10: Actions – Di chuyển vào vùng cách ly*


**Chú ý**: Trong ví dụ này, chúng ta sẽ di chuyển các tệp tin bị nhiễm vào *Vùng Cách ly Virút*. Tuy nhiên, danh sách các lệnh gồm ba lựa chọn khác như sau:

**Repair** (**Sửa**): Lệnh này sẽ cố khôi phục tệp bị nhiễm.

**Delete** (**Xóa**): Lệnh này sẽ xóa - vĩnh viễn - tệp tin bị nhiễm.

**Do nothing** (**Bỏ qua**): Đúng như tên gọi, lệnh này không thực hiện gì cả, và lệnh này *không được khuyên dùng* để đối phó các nguy hiểm tiềm tàng hoặc vi rút.

**Bước 3**. **Chọn** mục *Move to Chest* (*Chuyển đên Vùng Cách ly*) sau đó **chọn** ![](/sbox/screen/avast-vi-1/71.png)

![](/sbox/screen/avast-vi-1/73.png)

*Hình 11: Tệp lây nhiễm đã được chuyển vào Vùng Cách ly Vi rút*

**avast!** theo dõi liên tục máy tính ở chế độ nền để tìm vi rút và mã độc trong khi bạn vẫn tiếp tục làm việc. Khi avast! phát hiện mã độc hoặc một tệp khả nghi, chương trình sẽ cảnh báo bạn bằng một thông báo tương tự như hình dưới đây.

![](/sbox/screen/avast-vi-1/81.png)

*Hình 12: Phát hiện Vi rút*

Hành động mặc định sẽ là di chuyển tệp bị nhiễm vào *Quarantine* (Vùng cách ly Vi rút). Mục tiếp theo sẽ hướng dẫn cách xử lý các mã độc và vi rút phát hiện trong quá tình quét và được di chuyển vào vùng Cách ly Vi rút.

<a name="4.8"></a>
### 4.8 Hướng dẫn Sử dụng Vùng Cách ly Virút ###

Trong quá trình cài đặt **avast!**, *Vùng Cách ly Vi rút* được tạo ra trên ổ cứng của bạn. *Vùng Cách ly Vi rút* là một thư mục đặc biệt được cách ly khỏi phần còn lại của hệ thống, và được sử dụng để lưu trữ mã độc hoặc vi rút phát hiện trong quá trình quét, cũng như những tài liệu bị lây nhiễm, tệp hoặc thư mục.

Giờ bạn truy cập nội dung của *Vùng Cách ly Vi rút* và quyết định sẽ xử lý các tệp được lưu trong vùng này như thế nào**. 

**Bước 1**. **Nhấn** ![](/sbox/screen/avast-vi-1/57.png) và **chọn** ![](/sbox/screen/avast-vi-1/74.png) để kích hoạt cửa sổ:

![](/sbox/screen/avast-vi-1/75.png)

*Hình 13: Vùng Cách ly Vi rút hiển thị thông tin của một virút*

**Bước 2**: **Nhấn phải chuột** lên một trong hai virút để hiển thị các hành động xử lý:

![](/sbox/screen/avast-vi-1/76.png)

*Hình 14: Các lệnh xử lý một vi rút trong Vùng Cách ly*

**Lưu ý**: Nhấn đúp chuột vào một vi rút trong *Vùng Cách ly* sẽ không kích hoạt hoặc khởi động vi rút đó. Việc đó sẽ hiển thị các thông tin thuộc tính của vi rút, cũng nhu khi bạn chọn *Properties* từ trình đơn cảm ngữ cảnh tương ứng.

Các hành động xử lý vi rút trong trình đơn cảm ngữ cảnh như sau:


**Delete** (**Xóa**): Lệnh này sẽ xóa triệt để virút. 

**Restore** (**Khôi phục**): Lệnh này sẽ phục hồi virút về thư mục cũ nơi nó được tìm thấy.

**Extract** (**Chép**): Lệnh này sẽ sao tệp hoặc vi rút vào một thư mục do bạn chọn.

**Scan** (**Quét**): Lệnh này sẽ thực hiện một tác vụ quét khác đối với tệp nhiễm virút này.

**Submit to virus lab...** (**Gửi mẫu tới trung tâm nghiên cứu vi rút...**): Lệnh này cho phép bản gửi mẫu vi rút tới trung tâm nghiên cứu để phân tích thêm. Một mẫu đăng ký sẽ xuất hiện yêu cầu bạn điền thông tin và gửi đi.

**Properties** (**Thuộc tính**): Lệnh này hiển thị các thông tin chi tiết về vi rút.

**Add...** (**Thêm vào**): Lệnh này cho phép bạn chọn thư mục hay tệp để chuyển vào *Vùng Cách  ly*. Tính năng này rất hữu ích khi bạn muốn bảo vệ dữ liệu khi bị vi rút tấn công.

**Refresh all files** (**Duyệt lại danh sách tệp**): Lệnh này sẽ cập nhật lại danh sách tệp để hiển thị các tệp hiện tại.

<a name="4.9"></a>
### 4.9 Các Phương pháp Diệt Vi rút Nâng cao ###

Trong một số trường hợp, sự bảo vệ của **avast!**, **Comodo Firewall** và **Spybot** là không đủ; dù chúng ta đã nỗ lực hết sức, máy tính cá nhân hay hệ thống các máy tính tại nơi làm việc *vẫn* có thể bị nhiễm mã độc hay vi rút. Trong phần [**4.1  Hướng dẫn cơ bản để Đối phó với Sự bùng phát Vi rút**](/avast_doiphovirut#4.1) có nêu một số phương pháp đối phó với các loại mã độc và vi rút xảo quyệt. Tuy nhiên, *còn có* những phương pháp khác nữa để đối phó với các loại nguy cơ này.

**Phương pháp A: Sử dụng Đĩa CD/DVD hoặc USB khẩn cấp diệt virút**

Một số công ty phát triển phần mềm diệt vi rút cung cấp đĩa CD/DVD diệt vi rút 'khẩn cấp'. Bạn có thể tải về các tệp ảnh ISO của chương trình (định dạng này để ghi thành đĩa CD hoặc DVD).

Để sử dụng các đía CD/DVD này, hãy làm theo các bước sau:

1. Tải về tệp ISO đĩa khẩn cấp (hãy xem danh sách bên dưới) và ghi chương trình diệt virút vào đĩa CD /DVD hoặc USB. 
*Bạn có thể sử dụng chương trình miễn phí như [*ImgBurn*](http://www.imgburn.com) để ghi tệp lên đĩa. Hoặc bạn có thể sử dụng chương trình như [*Universal USB*](http://www.pendrivelinux.com/universal-usb-installer-easy-as-1-2-3/) để ghi tệp lên đĩa USB*. 

**Lưu ý:** Tốt nhất bạn nên thực hiện bước này trên một máy tính khác không bị lây nhiễm nếu có thể.

2. Cho đĩa vừa tạo vào ổ đĩa CD/DVD hoặc cắm ổ USB vào máy tính bị nhiễm vi rút và khởi động lại máy tính với chọn lựa khởi động từ đía CD/DVD. 

*Thường thì bạn có thể nhấn phím F10 hoặc F12 ngay sau khi bật máy. Hãy chú ý cẩn thận các thông tin chỉ dẫn trên màn hình sau khi khởi động để thực hiện. Hãy tìm hiểu thêm trên mạng Internet các hướng dẫn về khởi động (boot) máy tính từ USB hoặc CD/DVD. Các hướng dẫn cho các máy khác nhau có thể khác nhau.*

3. Khi máy tính bị nhiễm đã khởi động từ ổ USB/CD/DVD, hãy kết nối máy tính với mạng Internet để chương trình diệt virút có thể tự động cập nhật cơ sở dữ liệu vi rút nếu cần, sau đó chương trình sẽ thực hiện quét toàn bộ các ổ đĩa để tìm và diệt các loại phần mềm độc hại.
*Có thể sẽ tốt hơn khi sử dụng kết nối Internet tốc độ cao nếu sẵn có*

4. Bắt đầu việc quét các ổ đĩa trên hệ thống để gỡ bỏ các lây nhiễm và các mối nguy hại từ mã độc.

Danh sách các chương trình diệt vi rút trên CD:

- [**Avira AntiVir Rescue CD**](https://www.avira.com/en/download/product/avira-rescue-system)
- [**AVG Rescue CD**](http://www.avg.com/us-en/avg-rescue-cd)
- [**BitDefender Rescue CD**](http://www.bitdefender.com/support/How-to-create-a-BitDefender-Rescue-CD-627.html)
- [**F-Secure Rescue CD**](http://www.f-secure.com/en/web/labs_global/rescue-cd)
- [**Kaspersky Rescue CD**](http://support.kaspersky.com/viruses/rescuedisk/)
- [**Dr.Web Live Rescue CD**](http://www.freedrweb.com/livecd/)


Bạn cũng có thể thấy các thông tin và các công cụ sau có thể thú vị và hữu ích:

- [**Hướng dẫn làm sạch máy tính bị nhiễm mã độc một cách đơn giản (Hướng dẫn Gở bỏ Mã độc hại)**](http://malwaretips.com/blogs/malware-removal-guide-for-windows/)

- [**Hướng dẫn Gỡ bỏ Mã độc hại trên Windows**](http://www.selectrealsecurity.com/malware-removal-guide).

**Lưu ý:** Bạn có thể sử dụng lần lượt từng công cụ nêu trên để tăng tối đa hiệu quả.

**Phương pháp B: Cài đặt lại Hệ điều hành Microsoft Windows**

Trong một số trường hợp hiếm thấy,  một lây nhiễm vi rút có thể gây tổn hại nặng nề đến mức những công cụ giới thiệu phía trên có thể không sử dụng được. Trong tình huống như vạy, chúng tôi khuyên bạn nên thực hiện các hành động sau:

***Lưu ý**: Trước khi bạn thực hiện, hãy chắc chắn rằng bạn có lưu mọi thông tin liên quan tới bản quyền phần mềm hay mã số đăng ký phần mềm và bản cài đặt **Hệ điều hành Windows** cũng như các chương trình phần mềm khác. Việc này đòi hỏi phải mất thời gian chuẩn bị nhưng sẽ là giải pháp tốt trong trường hợp không thể tiêu diệt triệt để các chương trình độc hại hay vi rút bằng các phương pháp khác.* 

1. Sao lưụ tất cả các tệp trên máy tính.

2. Cài lại **Hệ điêu hành Microsoft Windows** với lựa chọn định dạng lại toàn bộ ổ đĩa.

3. Cập nhật hệ điều hành **Microft Windows** sau khi hoàn thành cài đặt.

4. Cài đặt **avast!** (hoặc một chương trình diệt virút bạn tin tưởng) và cập nhật chương trình đó.

5. Cài đặt các chương trình cần thiết và hãy sử dụng phiên bản mới nhất cũng như cập nhật từng chương trình.

  **Lưu ý**: Trong bất cứ trường hợp nào cũng không được kết nối ổ đĩa sao lưu vào máy tính *trước khi* đã hoàn tất các bước phía trên. Bạn có thể sẽ khiến hệ thống bị lây nhiễm lại.
6. Connect your backup disk to your computer and scan it thoroughly to detect and eliminate any existing problems. 

6. Nối ổ đĩa sao lưu vào máy tính và quét toàn bộ ổ đĩa đó để tiêu diệt các chương trình độc hại.

7. Sau khi đã phát hiện và xóa các tệp nhiễm, bạn có thể sao chép dữ liệu từ ổ đĩa dự phòng vào ổ cứng máy tính.


<a name="4.10"></a>
## 4.10 Quét Thông minh ###

*Quét Thông minh* có thể thực hiện cùng một lúc một số loại quét như đề cập phía trên. Đây là một cách thuận tiện để thực hiện một 'kiểm tra sức khỏe' về nhiễm mã độc hại, cập nhật các phần mềm và bảo mật mạng. Trong ví dụ dưới đây, Smart Scan phát hiện một số phần mềm chưa được cập nhật và yêu cầu cập nhật chúng.

**Bước 1. Nhấn** ![](/sbox/screen/avast-vi-1/57.png) và ![](/sbox/screen/avast-vi-1/36.png) để kích hoạt cửa sổ sau:

![](/sbox/screen/avast-vi-1/84.png)

*Hình 19: Quét thông minh* 

Khi việc *Quét Thông minh* hoàn thành, trạng thái của từng phương pháp quét sẽ được hiển thị như bên dưới đây.

![](/sbox/screen/avast-vi-1/85.png)

*Hình 20: Quét thông minh – Phát hiện nguy cơ* 

**Bước 2. Nhấn** ![](/sbox/screen/avast-vi-1/86.png) để bắt đầu tìm hiểu các nguy cơ được phát hiện. Lưu ý *GrimeFighter* không được tích hợp trong phiên bản miễn phí của avast!.

![](/sbox/screen/avast-vi-1/39.png)

*Hình 21: Quét thông minh – Cửa sổ Cập nhật phần mềm* 

**Bước 3.** Nhấn ![](/sbox/screen/avast-vi-1/40.png) để bắt đầu cập nhật từng ứng dụng cần cập nhật.

![](/sbox/screen/avast-vi-1/38.png)

*Hình 22: Phần mềm được cập nhật* 

**Bước 4.** Hãy thực hiện các bước từ 1 đến 3 phía trên để đánh giá lại tình trạng máy tính của bạn sau khi quét.


