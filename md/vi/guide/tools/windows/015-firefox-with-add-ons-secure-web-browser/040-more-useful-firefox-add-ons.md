

---

lang: vi
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 4
depth: 3
title: More Useful Firefox Add-Ons

---

Các mục trong chương này:

- [**5.0 Giới thiệu các Tiện ích**](#5.0)
- [**5.1 Hướng dẫn Sử dụng  HTTPS Everywhere**](#5.1) 
- [**5.2 Hướng dẫn Sử dụng Adblock Plus**](#5.2)
- [**5.3 Hướng dẫn Sử dụng Beef Taco** (Đối phó với các cookies quảng cáo Opt-Out)](#5.3)
- [**5.4 Hướng dẫn Sử dụng Better Privacy**](#5.4)
- [**5.5 Hướng dẫn Một số Thành phần Mở rộng hữu ích khác**](#5.5) 

----

<a name="5.0"></a>
## 5.0 Giới thiệu các Tiện ích ##
Trong phần này bạn sẽ tìm hiểu về một số thành phần mở rộng hữu ích khác của **Mozilla**. Chúng giúp tăng cường và cải thiện mức an toàn và an ninh Internet khi bạn truy cập các trang web khác nhau hay khi thực hiện các phiên làm việc trực tuyến. Để tải về các tiện ích này hãy xem phần [**Tải về Firefox**](/vi/firefox-main).



<a name="5.1"></a>
## 5.1 Hướng dẫn HTTPS Everywhere ##

[![](/sbox/screen/firefox-en/httpseverywherelogo.jpg)](https://www.eff.org/https-everywhere)

**HTTPS Everywhere** là phần mở rộng **Mozilla Firefox** đảm bảo rằng bạn luôn truy cập các trang web nằm trong danh sách đặc biệt qua một kênh mã hóa (sử dụng giao thức https). Mác dù nhiều trang web có hỗ trợ mã hóa, họ thường sử dụng địa chỉ mặc định không mã hóa http. Tiện ích **HTTPS Everywhere** khắc phục vấn đề này bằng cách sửa lại tất cả các yêu cầu truy cập của bạn sử dụng giao thức **HTTPS**. Nó hoạt động ở chế độ nền để đảm bảo các phiên truy cập Internet của bạn tới các trang web trong danh sách được an toàn và bảo mật.

Sau khi thành phần mở rộng **HTTPS Everywhere** được cài đặt thành công, cửa sổ sau sẽ xuất hiện: 

![](/sbox/screen/firefox-vi-1/75.png)

*Hình 1: Cửa sổ xác nhận HTTPS Everywhere có nên sử dụng SSL Observatory*

**Bước 1**: **Nhấn** ![](/sbox/screen/firefox-vi-1/76.png) để mở cửa sổ sau:

![](/sbox/screen/firefox-vi-1/77.png)

*Hình 2: Cửa sổ SSL Observatory Preferences*

**Lưu ý**: Nếu đã có một phiên bản cài đặt trước đó của **HTTPS Everywhere** trên máy tính của bạn, **hãy chọn Công cụ > HTTPS Everywhere > SSL Observatory Preferences** và kiểm tra rằng tùy chọn *Use the Observatory* và *When you see a new certificate, tell the Observatory which ISP you are connected to* đã được chọn. Nếu bạn không sử dụng **Tor**, **hãy chọn** cả tùy chọn *Check certificates even if Tor is not available*. 


<a name="5.2"></a>
## 5.1 Hướng dẫn Adblock Plus ##

[![](/sbox/screen/firefox-en/httpseverywherelogo.jpg)](https://www.eff.org/https-everywhere)

**Adblock Plus** là tiện ích lọc nội dung được thiết kế để giới hạn hoặc ngăn chăn khả năng hiển thị của cách loại quảng cáo. 

Sau khi hoàn tất quá trình cài đặt **Adblock Plus**, trang web sau sẽ xuất hiện: [chrome://adblockplus/content/ui/firstRun.html](chrome://adblockplus/content/ui/firstRun.html)

![](/sbox/screen/firefox-vi-1/60.png)

*Hình 3: Nội dung trang Adblock Plus chrome* 

**Bước 1**. **Nhấn** ![](/sbox/screen/firefox-vi-1/61.png) để thay đổi thành ![](/sbox/screen/firefox-vi-1/62.png) cho nút *Chặn Phần mềm Độc hại, Loại bỏ các Nút bấm Phương tiện Mạng Xã hội* và tùy chọn *Vô hiệu hóa Theo dõi*  (như trong *Hình 1* phía trên).

**Bước 2**. **Chọn Công cụ > Adblock Plus > Tùy chỉnh Bộ lọc**... để mở cửa sổ sau:

![](/sbox/screen/firefox-vi-1/63.png)

*Hình 4: Cửa sổ Thêm bộ lọc cho  Add Adblock hiển thị các bộ lọc đăng ký*

**Bước 3**. **Nhấn chọn** từng hộp chọn của các đăng ký bộ lọc để kích hoạt (như trong *Hình 2* phía trên), sau đó bỏ chọn ô *Cho phép một số quảng cáo không gây hại*, để ngăn *tất cả* các quảng cáo được liệt kê trong danh các bộ lọc này khỏi hiển thị. 

**Bước 4**. Nếu bạn sử dụng đa ngôn ngữ, **nhấn** ![](/sbox/screen/firefox-vi-1/65.png) để xem các đăng ký bộ lọc khác nhau, sau đó **nhấn** ![](/sbox/screen/firefox-vi-1/66.png) để mở danh sách xổ xuống các bộ lọc khác nhau, **hãy chọn** bộ lọc phù hợp và **nhấn** ![](/sbox/screen/firefox-vi-1/67.png). 

**Bước 4**. Để cập nhật đăng ký bộ lọc, **nhấn** ![](/sbox/screen/firefox-vi-1/65.png), và **chọn** mục *Cập nhật Bộ lọc* trong trình đơn. 


<a name="5.3"></a>
## 5.3 Hướng dẫn Sử dụng Beef Taco (Đối phó các Cookies quảng cáo Opt-Out) ##

[![](/sbox/screen/firefox-en/beeftacologo.png)](https://addons.mozilla.org/en-US/firefox/addon/beef-taco-targeted-advertising/)

**Beef Taco** là một tiện ích **Mozilla Firefox** cho phép bạn quản lý các cookie liên quan tới việc quảng cáo từ các công ty khác nhau gồm cả **Google**, **Microsoft** và **Yahoo**. Chương trình có thể được thiết đặt để xóa các cookie đã được nhận biết là **Các Cookie với Mục đích Quảng cáo** một cách tự động. Tuy nhiên, nó cũng cho phép người dùng **Có kinh nghiệm** và **Nâng cao** xác định cụ thể những cookie nào được cho phép tồn tại trên máy tính của mình và những cookie nào sẽ bị loại bỏ.


<a name="5.4"></a>
## 5.4 Hướng dẫn Sử dụng Better Privacy ##

[![](/sbox/screen/firefox-en/betterprivacylogo.jpg)](https://addons.mozilla.org/en-US/firefox/addon/betterprivacy/)

**Better Privacy** là một tiện ích **Mozilla Firefox** giúp bảo vệ hệ thống của bạn khỏi một loại  cookie đặc biệt được nhận dạng là một **LSO** (**Local Shared Objects** ) có thể được tải về trên máy của bạn bởi một đoạn mã **Flash**. Những cookie này sẽ không bị xóa bởi chức năng xóa cookie thông thường của **Firefox**.



<a name="5.5"></a>
## 5.5 Hướng dẫn Một số Thành phần Mở rộng hữu ích khác ##

Phần này giới thiệu một số các thành phần bổ sung và mở rộng hữu ích miễn phí, mã nguồn mở (hoặc đang trong quá trình trở thành nguồn mở), giúp tăng cường hoặc mở rộng khả năng lướt web một cách riêng tư và bảo mật.


### 5.5.1 Cryptocat ###

[![](/sbox/screen/firefox-vi-1/cryptocatlogo.png)](https://addons.mozilla.org/en-us/firefox/addon/cryptocat/)

Cryptocat là thành phần bổ sung về Nhắn tin Trực tuyến riêng tư, nguồn mở có mã hóa hoạt động trực tiếp trên trình duyệt. Nhờ đó việc sử dụng có thể dễ dàng hơn so với việc sử dụng các phần mềm nhắn tin khác. **Cryptocat** cho phép bạn tạo ra các phòng chát ảo để trò truyện với tất cả các thành viên hoặc hội thoại riêng tư môt-một với từng thành viên riêng rẽ. Tất cả các hội thoại đều được mã hóa và giải mã trên trình duyệt của người sử dụng trước khi gửi và sau khi nhận về. **Cryptocat** sẵn có dưới dạng thành phần bổ sung cho **Mozilla Firefox, Google Chrome và Apple Safari** và cũng có dưới dạng ứng dụng cho **Mac OS X**. [Hãy tìm hiểu thêm...](https://crypto.cat/)

----

### 5.5.2 Disconnect ###

[![](/sbox/screen/firefox-vi-1/disconnectmelogo.png)](https://addons.mozilla.org/en-us/firefox/user/disconnect/)

**Disconnect** được thiết kế để giữ an toàn cho dữ liệu của bạn khỏi sự theo dõi của các trang web bên thứ ba, đồng thời phân tích các bên theo dõi và phân loại họ theo các nhóm khác nhau, ví dụ, quảng cáo, phân tích và xã hộ. [Hãy tìm hiểu thêm...](https://www.disconnect.me/)
 
### 5.5.3 DuckDuckGo ###

[![](/sbox/screen/firefox-vi-1/duckduckgologo.png)](https://addons.mozilla.org/en-US/firefox/addon/duckduckgo-ssl/)

**DuckDuckGo** được thiết kế để cung cấp công cụ tìm kiếm trên bảo mật và riêng tư trên Internet thay cho các công cụ như **Google** hoặc **Bing**. **DuckDuckGo** không ghi lại hay chia sẻ thông tin người dùng, và mọi người dùng đề có truy cập tới thông tin như nhau. Bạn có thể truy cập trực tiếp trang [DuckDuckGo](https://duckduckgo.com/), hoặc **nhấn** vào biểu tượng **DuckDuckGo** để cài đặt thành phần này là bộ tìm kiếm mặc định trên thanh tìm kiếm.

### 5.5.4 vtzilla ###

[![](/sbox/screen/firefox-vi-1/vtzillalogo)](https://addons.mozilla.org/en-us/firefox/addon/vtzilla/)

vtzilla là thành phần mở rông của Mozilla Firefox được thiết kế để quét các tải về và các trang web kiểm tra mã độc hại và virút. Sau khi **vtzilla** được cài đặt thành công, thanh **vtzilla** (có thể chọn hiện lên hay ẩn đi) sẽ xuất hiện bên dưới thanh duyệt của **Firefox**. Chỉ đơn giản copy và chép hoặc nhập vào địa chỉ cần duyệt vào ô tìm kiếm **vtzlla**, là yêu cầu tìm kiếm của bạn sẽ được chuyển thẳng tới **Virus Total** (*Cổng quét Virut*), một trang sẽ sử dụng hơn 40 bộ quét khác nhau tìm mã độc và virút của các đường dẫn riêng hoặc trang web. Hơn nữa, **vtzilla** giúp giảm nguy cơ nhiễm mã độc bằng cách tăng cường thêm một lớp bảo vệ cho các chương trình diệt virút bạn đang sử dụng (ví dụ như [avast!](https://securityinabox.org/vi/avast-main)), bằng việc quét các tệp tải về. [Hãy tìm hiểu thêm...](https://www.virustotal.com/en/documentation/browser-extensions/).

### 5.5.5 ShareMeNot ###

[![](/sbox/screen/firefox-vi-1/sharemenotlogo.png)](https://addons.mozilla.org/en-us/firefox/addon/sharemenot/)

**ShareMeNot** được thiết kế để tránh các nút bấm do bên thứ ba (như nút “Like” của Facebook hay nút “tweet” của Tweeter) nhúng vào trong các trang web trên mạng Internet theo dõi bạn, chừng nào bạn chưa bấm vào chúng. [Hãy tìm hiểu thêm...](http://sharemenot.cs.washington.edu/)

----

### 5.5.6 Click&Clean ###

[![](/sbox/screen/firefox-vi-1/clickcleanlogo.png)](https://addons.mozilla.org/en-US/firefox/addon/clickclean/)


**Click&Clean** được thiết kế giúp xóa tự động dữ liệu riêng tư khi đóng chương trình **Firefox**; việc xóa này bao gồm dọn sạch các bản ghi từ lược sử tải về, xóa lược sử truy cập web, và gỡ bỏ các cookies, bao gồm cả **Flash Local Shared Objects (LSO)**. Tiện ích cũng xóa các tệp tạm và làm sạch bộ nhớ đệm cục bộ trên hệ thống của bạn.

**Lưu ý**: Một cách khác, người dùng có thể cân nhắc sử dụng các ứng dụng riêng, như [**Ccleaner**](https://securityinabox.org/vi/ccleaner-main), **Wise Disk Cleaner**, vv cho hệ điều hành **MS Windows**, hoặc **Janior** hoặc **BleachBit** cho **Linux**.







