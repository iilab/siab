

---

lang: vi
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: How to Use the NoScript Add On

---

Các mục trong trang này:

- [**4.0 Giới thiệu NoScript**](#4.0)
- [**4.1 Hướng dẫn Sử dụng NoScript**](#4.1)

-------

<a name="4.0"></a>
## 4.0 Giới thiệu NoScript ##

![](/sites/securitybkp.ngoinabox.org/files/u9/noscript.png)

**NoScript** là một thành phần mở rộng rất hữu ích của **Mozilla** giúp bảo vệ máy tính khỏi các trang web độc hại trên Internet. Nó hoạt động bằng cách tạo ‘danh sách trắng’ các trang web bạn đã kiểm tra và chấp nhận, an toàn hoặc đáng tin cậy (như trang giao dịch tài chính ngân hàng hoặc trang tin trực tuyến). Mọi trang khác sẽ được coi là có nguy cơ gây hại và bị hạn chế chức năng, cho đến khi bạn quyết định nội dung của các trang này không gây hại và đưa chúng vào danh sách trắng. 

**NoScript** sẽ tự động khóa các cửa sổ quảng cáo, khung quảng cáo, các mã **Java** và **JavaScript** cũng như những thuộc tính có thể gây hại khác trên các trang web. **NoScript** sẽ không thể phân biệt được các nội dung có hại với các nội dung cần thiết được hiển thị trên một trang web. Nên bạn sẽ phải chọn cho phép các trang mà bạn biết rằng chúng an toàn.

<a name="4.1"></a>
## 4.1 Hướng dẫn Sử dụng NoScript ##

Trước khi bắt đầu sử dụng **NoScript** hãy chắc chắn rằng tiện ích này đã được cài đặt thành công bằng cách **chọn Công cụ > Tiện ích** để mở cửa sổ *Quản lý Tiện ích* và kiểm tra xác nhận *thành phần mở rộng* này đã được cài đặt.

**Gợi ý**: Mặc dù sử dụng **NoScript** ban đầu khá khó chịu, (vì các trang web bạn thường hay truy cập không được hiển thị đúng đắn), bạn sẽ thấy hữu ích từ tính năng chặn các đối tượng động trên trang web. Tính năng này sẽ giúp chặn các quảng cáo quấy rối, các cửa sổ thông báo, và các mã độc nằm trên các trang web. 

**NoScript** sẽ chạy ở chế độ nền cho đến khi nó phát hiện thấy các nội dung chứa mã **JavaScript**, **Adobe Flash** hay các loại mã tương tự. Khi đó **NoScript** sẽ khóa các nội dung này và thanh trạng thái sẽ xuất hiện tại phía dưới cửa sổ **Firefox** như sau: 

![](/sbox/screen/firefox-vi-1/50.png)

*Hình 1: Thanh trạng thái NoScript*

Thanh trạng thái **NoScript** hiển thị các thông tin về các *đối tượng* (ví dụ, quảng cáo và hộp thoại tin nhắn) *các đoạn mã* đang bị chặn trên hệ thống của bạn. Hai hình dưới đây là những ví dụ về cách hoạt động của **NoScript**: Trong *Hình 2*, **NoScript** đã khóa thành công một quảng cáo trên **Adobe Flash Player** của một trang web thương mại. 

![](/sbox/screen/firefox-vi-1/51.png)

*Hình 2: Ví dụ việc NoScript khóa một hộp thoại quảng cáo trên một trang web thương mại*

Trong *Hình 3*, trang mạng **Twitter** cảnh báo rằng mã **JavaScript** cần được bật (ít nhất là tạm thời) để xem nội dung trang này.

![](/sbox/screen/firefox-vi-1/52.png)

*Hình 3: Trang mạng Twitter yêu cầu bật JavaScript*

Vì **NoScript** không thể phân biệt giữa các mã độc hại và mã được sử dụng thông thường, bạn có thể thấy một số tính năng hay chức năng (ví dụ: thanh trình đơn) không hiển thị. Một số trang web chứa nội dung bao gồm các dạng mã kịch bản (script) từ nhiều hơn một trang. Ví dụ trang **www.twitter.com** có ba nguồn mã kịch bản:

![](/sbox/screen/firefox-vi-1/53.png)

*Hình 4: Ví dụ về thanh trạng thái NoScript với mục Tùy chọn*

Để bỏ việc chăn các đoạn mã trong những trường hợp này, hãy **chọn** tùy chọn *Tạm thời Cho phép [tên trang web]* (trong ví dụ này là *Tạm thời cho phép twitter.com*). Tuy nhiên, nếu bạn vẫn không thể xem nội dung trang, có thể bạn cần kiểm tra xác minh qua việc thử và kiểm tra lỗi để cho phép một số trang web tối thiểu để có thể hiển thị nội dung của trang cần xem. Ví dụ với **Twitter**, bạn phải **chọn** tùy chọn *Tạm thời cho phép twitter.com* và *Tạm thời cho phép twimg.com*, để trang **Twitter** có thể hoạt động.

**Cảnh báo!**: Trong bất kỳ tình huống nào, bạn **không** bao giờ nên chọn lựa chọn sau: *Cho phép Script trên mọi trang (nguy hiểm)*. Tránh càng xa càng tốt lựa chọn *Cho phép tất cả trên trang này* . Đôi khi bạn có thể sẽ phải cho phép tất cả các script, tuy nhiên trong trường hợp đó hãy đảm bảo rằng bạn chỉ thực hiện điều này trên các trang bạn thực sự tin tưởng và đây chỉ là sự cho phép tạm thời.- đúng vậy, chỉ cho phép tạm thời đến hết phiên làm việc trực tuyến này. Chỉ cần một xâm nhập *duy nhất* của một đoạn mã độc có thể gây nguy cơ xâm phạm tính riêng tư và an toàn trực tuyến của bạn.

Đối với những trang web bạn đã tin tưởng và viếng thăm thường xuyên, **hãy chọn** tùy chọn *Cho phép [tên trang web]. (Trong ví dụ phía trên, tùy chọn *Cho phép twitter.com* và *Cho phép twimg.com* đã được chọn). Việc chọ các tùy chọn này cho phép **NoScript** ghi nhớ các trang web đã tin tưởng. 

