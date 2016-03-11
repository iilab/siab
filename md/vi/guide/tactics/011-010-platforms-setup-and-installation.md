

---

lang: vi
community: guide
type: tactics
legacy: True
child: True
weight: 1
depth: 3
title: Platforms, Setup and Installation

---

### Các nền tảng và Hệ điều hành ###

Tại thời điểm bài viết, những điện thoại thông minh được sử dụng rộng rãi nhất là iPhone của Apple và Android của Google, theo sau đó là sản phẩm sử dụng Blackberry và Windows. Sự khác biệt quan trọng nhất giữa Android và các hệ điều hành khác là Android, hầu hết mọi trường hợp, là hệ thống Nguồn Mở ([*FOSS*](/vi/Glossary#FOSS)), cho phép hệ điều hành này được kiểm tra một cách độc lập để xác nhận khả năng bảo vệ thông tin người dùng và phương thức liên lạc an toàn. Điều này cũng cho phép tăng cường phát triển các ứng dụng bảo mật cho nền tảng nguồn mở này. Nhiều nhà phát triển phần mềm có ý thức về bảo mật phát triển các ứng dụng cho Android với sự chú trọng về an toàn và bảo mật cho người dùng. Một số ứng dụng này sẽ được đề cập rõ trong phần sau của chương này.

Cho dù bạn đang dùng loại điện thoại thông minh nào, có những vấn đề bạn luôn cần chú ý khi sử dụng điện thoại có kết nối Internet và có các tính năng như [*GPS*](/vi/glossary#GPS) hay khả năng kết nối không dây. Trong chương này chúng tôi chú  trọng tới các thiết bị sử dụng nền tảng Android với lý do đã đề cập phía trên đây là cách dễ dàng hơn để bảo mật dữ liệu và các kết nối liên lạc. Tuy nhiên, hướng dẫn thiết đặt cơ bản cho một số ứng dụng trên các thiết bị chạy hệ điều hành khác Android cũng sẽ được cung cấp.
Điện thoại Blackberry thường được giới thiệu là thiết bị nhắn tin và gửi thư điện tử ‘an toàn’. Điều này là bởi các tin nhắn và email được truyền trên kênh bảo mật qua các máy chủ của Blackberry, nằm ngoài phạm vi kiểm soát của những đối tượng nghe lén. Thật không may là ngày càng nhiều các chính quyền yêu cầu truy cập các kênh kết nối này với lý do nhu cầu chống lại nguy cơ khủng bố và tội phạm có tổ chức. Ấn độ, Liên hiệp các vương quốc Ả rập, Ả rap xê ut, Inddoonexxia và Liban là các ví dụ về chính quyền kiểm soát việc sử dụng các thiết bị Blackberry và yêu cầu truy cập dữ liệu người dùng tại các quốc gia này.

### Feature Phones ###

Một dòng điện thoại di động được gọi với những tính năng cao cấp hơn điện thoại di động cơ bản nhưng chưa phải là điện thoại thông minh gọi là 'feature phones' (ví dụ  Nokia 7705 Twist hay Samsung Rogue). Gần đây, ‘feature phones’ đã được tăng cường các tính năng có ở điện thoại thông minh. Nhưng nhìn chung, hệ điều hành của dòng ‘feature phones' thường ít khả năng truy cập do đó cơ hội xây dựng ứng dụng và cải thiệt bảo mật là rất hạn chế. Chung tôi không đề cập riêng tới dòng điện thoại ‘feature phones’ dù nhiều vấn đề đề cập trong chương này có thể cũng hữu ích cho cả dòng điện thại feature phones.

### Điện thoại thông minh gắn nhãn hãng và khóa mạng ###

Điện thoại thông minh thường được bán sau khi đã được gắn nhãn bởi nhà cung cấp dịch vụ hoặc khóa mạng. Khóa mạng điện thoại thông minh nghĩa là thiết bị này chỉ có thể hoạt động với một mạng của chính nhà cung cấp với thẻ SIM được cấp là thẻ duy nhất hoạt động với thiết bị này. Các nhà cung cấp dịch vụ di động thường thương hiệu hóa điện thoại họ bán ra bằng cách cài đặt phần mềm lớp giữa (firmware) hoặc phần mềm riêng của họ lên điện thoại. Họ cũng có thể thêm hoặc bớt một số tính năng của chiếc điện thoại này. Việc thương hiệu hóa là một cách để các công ty tăng cường doanh thu bằng cách định hướng việc sử dụng điện thoại thông minh, thông thường bao gồm cả việc thu thập thông tin bạn sử dụng điện thoại hay cho phép việc truy cập từ xa vào điện thoại của bạn.

Với những lý do trên, chúng tôi khuyên bạn nên mua một điện thoại không bị thương hiệu hóa bởi nhà cung cấp nếu bạn có lựa chọn. Một điện thoại bị khóa mạng có nguy cơ cao hơn vì dữ liệu của bạn sẽ được định tuyến qua một nhà mạng nơi tập trung mọi luồng dữ liệu kết nối của bạn và bạn không thể thay đổi SIM card của nhà cung cấp dịch vụ khác để phân tán dữ liệu trên các mạng khác nhau. Nếu điện thoại của bạn bị khóa mạng, hãy nhờ ai đó tin tưởng được giúp bạn mở khóa.

### Thiết đặt chung ###

Điện thoại thông minh có nhiều thiết đặt cho phép kiểm soát bảo mật của thiết bị. Một điều rất quan trọng là chú ý cách điện thoại thông minh của bạn được thiết đặt như thế nào. Trong Hướng dẫn Thực hành bên dưới chúng tôi sẽ cảnh báo bạn về các thiết đặt bảo mật điện thoại nhất định có thể được sử dụng nhưng không được kích hoạt theo mặc định cũng như những thiết đặt mặc định khiến điện thoại của bạn không an toàn.

<div class=getstarted markdown=1>
Thực hành: Hãy bắt đầu với [*Hướng dẫn Cài đặt cơ bản Android*](/vi/android_basic)
</div>

<div class=getstarted markdown=1>
Thực hành: Hãy bắt đầu với [*Hướng dẫn Cài đặt Cơ bản iPhone*](/vi/iphone_basic)
</div>

### Cài đặt và cập nhật các ứng dụng ###

Cách thông dụng để cài đặt phần mềm mới lên điện thoại thông minh của bạn là sử dụng Gian hàng Ứng dụng iPhone (iPhone Appstore) hoặc gian hàng Google Play, đăng nhập với thông tin đăng nhập người dùng sau đó tải về và cài đặt ứng dụng mong muốn. Với việc đăng nhập bạn liên kết việc sử dụng gian hàng trực tuyến với tài khoản người dùng đăng nhập. Chủ gian hàng trực tuyến lưu trữ thông tin lược sử trình duyệt và lựa chọn ứng dụng của người dùng.

Các ứng dụng được chào bán trên các gian hàng trực tuyến chính thức được chứng nhận bởi chủ gian hàng (Google hay Apple), tuy nhiên trên thưc tế điều này cung cấp sự bảo vệ ít ỏi về các hoạt động của ứng dụng sau khi được cài đặt trên điện thoại của bạn. Ví dụ, một số ứng dụng có thể sao lưu và gửi danh sách địa chỉ liên lạc của bạn sau khi được cài lên máy điện thoại. Trên các máy Android mỗi ứng dụng cần yêu cầu, trong quá trình cài đặt những hành động gì được cho phép khi ứng dụng chạy. Bạn cần để ý cẩn thận tới việc cho phép yêu cầu nào, và liệu những sự chấp thuận này có phù hợp với tính năng tương ứng của ứng dụng đang cài đặt hay không.

Các ứng dụng Android cũng có sẵn từ những nguồn bên ngoài các kênh cung cấp chính thức của Google. Bạn cần nhấn chọn tùy chọn *Unknown sources* trong *Application settings* để có thể sử dụng những trang cung cấp ứng dụng này.

Rất hữu ích khi bạn sử dụng các trang thay thế nếu bạn muốn giảm thiểu liên lạc trực tuyến với Google. Chúng tôi giới thiệu [**F-Droid**](http://f-droid.org) ('Free Droid'), chuyên cung cấp các ứng dụng Nguồn Mở [*FOSS*](/vi/glossary#FOSS). Trong hướng dẫn này, F-Droid là địa chỉ nguồn chính cho các ứng dụng chúng tôi giới thiệu, và chúng tôi sẽ chỉ liên kết bạn tới Google Play cho ứng dụng không có sẵn trên F-Droid.

Nếu bạn không muôn (hoặc không thể) kết nối trực tuyến để truy cập các ứng dụng, bạn có thể truyền các ứng dụng từ điện thoại của người khác bằng cách copy các tệp [*.apk*](/en/glossary#apk) (viết tắt của cụm từ 'android application package' – gói ứng dụng android) qua kết nối bluetooth. Một các khác là tải các tệp .apk vào thẻ nhớ Micro SD cho điện thoại của bạn hay sử dụng cáp kết nối để tải các tệp về từ một máy tính PC. Sau khi đã lưu các tệp vào điện thoại, bước đơn giản tiếp theo là ấn vào tên tệp và bạn sẽ được hướng dẫn để cài đặt ứng dụng. (**Lưu ý**: hãy hết sức chú ý khi sử dụng kết nối bluetooth – hãy tìm hiểu [***Chương 9.2.4: Các tính năng khác ngoài thoại và nhắn tin***](/vi/chuong_9_2_4)).


