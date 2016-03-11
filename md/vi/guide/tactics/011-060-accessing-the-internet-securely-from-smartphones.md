

---

lang: vi
community: guide
type: tactics
legacy: True
child: True
weight: 6
depth: 3
title: Accessing the Internet Securely from Smartphones

---

Như đã thảo luận trong [***Chuong 7: Làm thế nào để bảo mật truyền thông Internet của bạn***](/vi/chuong-7) và [***Chương 8: Làm thế nào để đảm bảo nặc danh và vượt qua sự kiểm duyệt trên mạng Internet***](/vi/chuong-8), truy cập nội dung trên Internet, hoặc đăng tải các thông tin trực tuyến như hình ảnh hoặc các đoạn phim, sẽ để lại những dấu vết tiết lộ bạn là ai và bạn đang làm gì. Điều này có thể khiến bạn gặp nguy hiểm. Việc sử dụng điện thoại thông minh để truy cập Internet sẽ khiến những nguy cơ trên ở mức độ lớn hơn.

### Truy cập qua kết nối WiFi hoặc Mạng Di động ###

Điện thoại thông minh cho phép bạn lựa chọn cách bạn kết nối vào Internet: có thể qua kết nối không dây từ một thiết bị phát không dây (như trong một quán café Internet), hoặc qua kết nối dữ liệu mạng di động, như GPRS, EDGE, hay UMTS được cung cấp bởi nhà cung cấp dịch vụ mạng di động.

Sử dụng kết nối không dây sẽ giảm các dấu vết dữ liệu bạn có thể để lại trong mạng của nhà cung cấp dịch vụ di động (bởi không kết nối sử dụng các thông tin đăng ký dịch vụ di động). Tuy nhiên, trong nhiều trường hợp, kết nối qua mạng thông tin di động là cách duy nhất. Rất không may là các giao thức kết nối dữ liệu cho mạng điện thoại di động ( như EDGE hay UMTS) đều không phải là các chuẩn mở. Các nhà phát triển độc lập và các kỹ sư bảo mật không thể tìm hiểu và kiểm tra các giao thức này để hiểu rõ về cách các giao thức này được cài đặt như thế nào bởi các nhà cung cấp dịch vụ di động.

Ở một số quốc gia các đơn vị cung cấp dịch vụ điện thoại di động hoạt động trong điều kiện pháp lý khác biệt so với các đơn vị cung cấp dịch vụ kết nối Internet, điều này cho phép việc giám sát và theo dõi sẽ chặt chẽ hơn bởi các nhà cung cấp và chính quyền các nước này.

Dù bạn phải sử dụng phương thức kết nối dữ liệu nào qua điện thoại thông minh, bạn luôn có thể giảm thiểu các nguy cơ để lộ dữ liệu bằng các sử dụng các công cụ năng danh và mã hóa.

### Sự nặc danh ###

Để truy cập các thông tin một cách nặc danh, bạn có thể sử dụng ứng dụng Android là [**Orbot**](https://www.torproject.org/docs/android.html.en). Orbot định tuyến luồng thông tin liên lạc của bạn qua mạng ẩn danh Tor.

<div class=getstarted markdown=1>
Thực hành: Hãy bắt đầu với [*Hướng dẫn Orbot*](/vi/Orbot_main)
</div>

Một tiện ích khác, Orweb, là một trình duyệt web có các tính năng bảo mật tăng cường giống như sử dụng các máy chủ trung chuyển và không lưu lại lược sử truy cập. Orbot và Orweb kết hợp vượt qua các bộ lọc chặn và tường lửa và cho phép truy cập trực tuyến nặc danh.

<div class=getstarted markdown=1>
Thực hành: Hãy bắt đầu với [*Hướng dẫn Orweb*](/vi/Orweb_main)
</div>

### Máy chủ trung chuyển ###

Phiên bản dành cho di động của [*Firefox*](/vi/glossary#Firefox) - [**Firefox mobile**](http://f-droid.org/repository/browse/?fdid=org.mozilla.firefox) có thể được tích hợp các tiện ích mở rộng máy chủ trung chuyển giúp định tuyến dữ liệu kết nối của bạn tới một máy chủ trung chuyển. Từ máy chủ trung gian này dữ liệu của bạn được chuyển tới trang web bạn truy cập. Giải pháp này hữu ích trong trường hợp mạng bị kiểm duyệt, nhưng sẽ vẫn để lộ yêu cầu truy cập của bạn trừ khi kết nối từ trình duyệt của bạn tới máy chủ trung chuyển được mã hóa. Chúng tôi khuyên dùng tiện ích mở rộng [**Proxy Mobile**](https://guardianproject.info/apps/proxymob-firefox-add-on/)  (cũng được phát triển bởi [**Guardian Project**](https://guardianproject.info/), cho phép tạo kết nối máy chủ trung chuyển dễ dàng với Firefox. Đây cũng là cách duy nhất để định tuyến kết nối từ trình duyệt Firefox mobile tới Orbot và sử dụng mạng nặc danh [*Tor*](/vi/glossary#Tor).


