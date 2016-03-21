

---

lang: vi
community: guide
type: tactics
legacy: True
child: True
weight: 1
depth: 3
title: Securing your email

---

Có một số bước quan trọng bạn cần tuân thủ để tăng cường mức độ bảo mật trong liên lạc bằng thư điện tử. Bước đầu tiên là đảm bảo rằng chỉ duy nhất người mà bạn gửi thư cho có thể đọc được nó. Điều này được bàn luận tại mục [*Bảo mật hộp thư của bạn*](/vi/chuonng_7_1#Bảo_mật_hộp_thư_của_bạn) và [*Chuyển sang một tài khoản thư điện tử có độ bảo mật cao hơn*](/vi/chuong_7_1#Chuyển_sang_một_tài_khoản_thư_điện_tử_có_độ_bảo_mật_cao_hơn) ở bên dưới. Ngoài những tính năng cơ bản, đôi khi rất cần thiết rằng đối tác của bạn có khả năng kiểm tra một cách chắc chắn rằng một bức thư điện tử thực sự được gửi tới từ bạn chứ không phải từ một kẻ giả mạo nào khác. Một cách để thực hiện điều này sẽ được thảo luận trong phần [*Tăng cường bảo mật thư điện tử*](/vi/chuong_7_4) thuộc  mục [*Mã hóa và xác thực thư điện tử cá nhân*](/vi/chuong_7_4#Mã_hóa_và_xác_thực_thư_điện_tử_cá_nhân).

Bạn cũng nên biết phải làm gì trong trường hợp tính riêng tư của các tài khoản thư điện tử của mình bị xâm hại. Mục [*Mẹo giúp đối phó trong trường hợp nghi ngờ hòm thư bị theo dõi*](/vi/chuong_7_2) sẽ giải quyết vấn đề này.

Cũng cần nhớ rằng việc bảo mật thư điện tử sẽ không có tác dụng nếu mọi điều bạn gõ xuống đều bị ghi lại bởi một phần mềm gián điệp và định kỳ sẽ gửi đi qua Internet cho một kẻ thứ ba. [*Chương 1: Làm thế nào để bảo vệ máy tính của bạn khỏi phần mềm độc hại và hacker*](/vi/chuong-1) đưa ra một sỗ hướng dẫn để ngăn chặn nguy cơ này, và [*Chương 3: Làm thế nào để tạo và duy trì mật khẩu bảo mật*](/vi/chuong-3) sẽ giúp bạn bảo vệ tài khoản thư điện tử và tin nhắn qua mạng với các công cụ được hướng dẫn dưới đây.

### Bảo mật hộp thư của bạn ###

Mạng Internet là một mạng lưới mở qua đó thông tin thường được truyền dưới dạng có thể đọc được. Nếu một tin nhắn thư điện tử thông thường bị chặn lấy trên đường tới tay người nhận, nội dung của nó có thể dễ dàng bị đọc. Đồng thời vì Internet là một mạng lưới rộng toàn cầu dựa vào các hệ thống máy tính trung gian để định tuyến, nhiều người khác có khả năng chặn thông tin của bạn trên đường truyền. [*Nhà cung cấp dịch vụ Internet*](/vi/glossary#ISP) là nơi đầu tiên thông tin của bạn đi qua trong chặng đường đi tới địa chỉ người nhận. Tương tự như vậy, [*ISP*](/vi/glossary#ISP) của người nhận là điểm cuối cùng tin nhắn đi qua trước khi được chuyển tới đích. Trừ khi bạn có sự đề phòng tốt, thông tin của bạn có thể bị đọc hay thay đổi tại hai điểm đầu cuối hay bất kỳ điểm nào trên đường truyền.

<div class="background" markdown="1">
Pablo: Tôi đã nói chuyện với một trong những đối tác của tôi về vấn đề này, và cô ấy cho biết cô ấy và đồng nghiệp đôi khi chỉ lưu các thư điện tử quan trọng trong thư mục *Nháp* trên một hòm thư mà hai người dùng chung cùng một mật khẩu. Việc này có vẻ hơi lạ, nhưng như thế có được không? Ý của tôi là liệu làm như vậy có tránh được việc ai đó đọc được thư không, vì thực tế chúng không được gửi đi?

Claudia: Bất kỳ lúc nào anh đọc một thư điện tử từ máy tính của mình, ngay cả khi nó chỉ là một ‘bản nháp’ thì nội dung của nó sẽ được gửi xuống máy tính của anh qua mạng Internet. Nếu không thì làm sao nó hiển thị được trên màn hình máy tính của anh, đúng không nào? Vấn đề là, nếu ai đó đang theo dõi anh, họ không chỉ theo dõi các thư điện tử của anh mà họ có thể kiểm soát toàn bộ thông tin có thể đọc được đi ra và đi vào từ máy tính của anh. Nói cách khác, cái mẹo trên sẽ không dùng được trừ khi tất cả mọi người đều kết nối một cách bảo mật tới hòm thư chung đó. Và nếu họ làm như vậy thì chẳng tội gì mà không tạo hai tài khoản riêng biệt và gửi thư cho nhau.</div>

Từ lâu việc bảo mật kết nối Internet từ máy tính của bạn với trang web mà bạn truy cập đã có thể thực hiện. Bạn thường gặp loại bảo mật này khi đăng nhập mật khẩu hoặc các thông tin tài khoản thanh toán vào các trang web. Kỹ thuật thực hiện điều này gọi là kỹ thuật [*mã hóa*](/vi/glossary#Encryption) đường truyền [*SSL*](/glossary#SSL). Bạn có thể xác định liệu bạn có đang sử dụng [*SSL*](/glossary#SSL) hay không bằng cách nhìn kỹ vào thanh địa chỉ của trình duyệt Web của bạn.

Mọi địa chỉ trang web thường bắt đầu bằng các ký tự **HTTP**, như ở ví dụ dưới đây:

![](/sites/securitybkp.ngoinabox.org/files/u7/01.png)

Khi bạn truy cập một trang web bảo mật, địa chỉ của  nó bắt đầu bằng **HTTPS**.

![](/sites/securitybkp.ngoinabox.org/files/u7/02.png)

Ký tự **S** cuối cùng xác định rằng máy tính đã mở một kết nối bảo mật tới trang web. Bạn cũng có thể để ý biểu tượng ‘ổ khóa’ hoặc nằm trên **thanh địa chỉ** hay trên **thanh trạng thái** phía dưới cửa sổ trình duyệt của bạn. Đó là những dấu hiệu cho bạn biết rằng nếu có kẻ nào đó đang theo dõi kết nối Internet của bạn sẽ không thể xem trộm kết nối giữa bạn và trang web bảo mật.

Ngoài việc tăng cường bảo vệ mật khẩu và các giao dịch tài chính, dạng [*mã hóa*](/vi/discussion#Encryption) này cũng lý tưởng cho việc bảo mật thư điện tử. Tuy nhiên, rất nhiều nhà cung cấp dịch vụ thư điện tử không cung cấp tính năng truy cập bảo mật, một số khác yêu cầu bạn phải tự chọn tính năng này, có thể bằng cách thay đổi thiết lập hoặc gõ **HTTPS** một cách thủ công. Bạn cần phải kiểm tra kỹ để đảm bảo rằng kết nối của bạn được mã hóa trước khi đăng nhập, đọc thư hay gửi tin.

Bạn cũng cần hết sức chú ý nếu trình duyệt của bạn tự nhiên cảnh báo về một [*xác thực bảo mật*](/vi/glossary#Security_certificate) không hợp lệ trong lúc truy cập một địa chỉ thư điện tử bảo mật. Điều này có khả năng do ai đó đang can thiệp vào kết nối giữa máy tính của bạn và máy chủ hòng xem trộm thông tin của bạn. Cuối cùng, nếu bạn dựa vào thư điện tử để trao đổi thông tin bí mật, thì một điều quan trọng là trình duyệt của bạn cũng phải hết sức đáng tin cậy. Bạn có thể cân nhắc việc cài đặt [*Mozilla Firefox*](/vi/glossary#Firefox) và các thành phần mở rộng bảo mật của nó. 

<div class="getstarted" markdown="1">Thực hành: Hãy bắt đầu với [Hướng dẫn sử dụng Firefox](/vi/firefox-main)</div>

<div class="background" markdown="1">
Pablo: Một trong những đối tác sẽ làm việc với chúng tôi về bản bảo cáo này thường sử dụng hòm thư điện tử Yahoo khi anh ta không ở trong văn phòng. Và tôi nhớ là có ai đó thì sử dụng Hotmail. Nếu tôi gửi một tin nhắn tới họ, liệu có ai khác có thể đọc được không?*

Claudia: Hoàn toàn có khả năng. Yahoo, Hotmail và rất nhiều các nhà cung cấp dịch vụ thư điện tử khác có những trang web không an toàn và không bảo vệ tính bảo mật cho thư điện tử của người dùng. Chúng ta sẽ cần phải thay đổi thói quen sử dụng của một vài người nếu chúng ta muốn thảo luận về các chứng cứ này một cách an toàn.* </div>

### Chuyển sang một tài khoản thư điện tử bảo mật hơn ###

Một số nhà cung cấp dịch vụ thư điện tử cho phép truy cập với [*đường truyền mã hóa*](/vi/glossary#SSL) tới hộp thư của bạn. Yahoo và Hotmail là những ví dụ cung cấp kết nối mã hóa trong khi bạn đăng nhập vào hộp thư để bảo vệ mật khẩu của bạn, nhưng thư của bạn lại được gửi và nhận mà không được bảo mật. Hơn nữa, Yahoo, Hotmail và một số nhà cung cấp dịch vụ thư điện tử khác gắn thêm thông tin về [*Địa chỉ IP*](/vi/glossary#IP_address) của máy tính bạn đang dùng vào trong thư bạn gửi đi.

Các tài khoản Gmail, trái lại, có thể được sử dụng hoàn toàn trên một kết nối được mã hóa, ngay khi bạn sử đăng nhập từ địa chỉ [*https://mail.google.com*](https://mail.google.com) (với **HTTPS**), thay vì [*http://mail.google.com*](http://mail.google.com). Thực tế là hiện tại bạn có thể thiết lập để Gmail luôn sử dụng kết nối mã hóa. Hơn nữa, không giống như Yahoo hay Hotmail, Gmail tránh việc để lộ thông tin **Địa chỉ IP** của bạn với người nhận. Tuy nhiên cũng không nên hoàn toàn tin cậy vào Google về sự bảo mật cho các liên lạc thư điện tử bí mật của bạn. Google sao chép và ghi lại thông tin của người dùng cho nhiều mục đích khác nhau và đã từng, trong quá khứ, nhượng bộ trước yêu cầu của chính phủ về sự hạn chế tự do thông tin số. Xem thêm tại phần [*Đọc thêm*](/vi/chuong_7_5) thông tin về các chính sách bảo mật của Google.

Nếu có thể, bạn nên tạo một tài khoản thư điện tử [*RiseUp*](/vi/glossary#RiseUp) bằng cách truy cập [*https://mail.riseup.net*](https://mail.riseup.net). [*RiseUp*](/vi/glossary#RiseUp) cung cấp dịch vụ thư điện tử miễn phí cho các nhà hoạt động xã hội trên thế giới và rất quan tâm tới việc bảo vệ những thông tin được lưu trữ trên các máy chủ của họ. Họ từ lâu đã trở thành một địa chỉ tin cậy cho những ai cần các giải pháp bảo mật thư điện tử. Và không giống như Google, họ có những chính sách rất khắt khe bảo quyền bảo mật của người dùng và không có mục đích thương mại nào sẽ ảnh hưởng tới các chính sách này. Tuy vậy, để tạo một tài khoản [*RiseUp*](/vi/glossary#RiseUp), bạn sẽ cần hai ‘mã giới thiệu’. Chúng được gửi cho bạn bởi hai người dùng [*RiseUp*](/vi/glossary#RiseUp) bất kỳ. Nếu bạn có trong tay cuốn sách hướng dẫn này, bạn sẽ nhận được ‘mã giới thiệu’ đi kèm với nó. Nếu không, bạn có thể tìm hai người sử dụng Riseup và yêu cầu mối người gửi cho bạn một mã.

<div class="getstarted" markdown="1">Thực hành: Hãy bắt đầu với [Hướng dẫn sử dụng Riseup.net](/vi/riseup-main)</div>

Cả Gmail và [*RiseUp*](/vi/glossary#RiseUp) đều hơn là những nhà cung cấp dịch vụ thư điện tử thông thường. Họ cho phép sử dụng các chương trình quản lý thư điện tử phía người dùng như Mozilla [*Thunderbird*](/vi/glossary#Thunderbird) có hỗ trợ những kỹ thuật được mô tả trong mục [*Tăng cường bảo mật thư điện tử*](/vi/chuong_7_4). Việc đảm bảo chắc chắn rằng phần mềm này của bạn luôn luôn khởi tạo các kết nối được [*mã hóa*](/vi/glossary#Encryption) tới máy chủ cung cấp dịch vụ cũng quan trọng như việc truy cập các trang web sử dụng **HTTPS**. Nếu bạn sử dụng một trình quản lý thư điện tử, xem [*Hướng dẫn Sử dụng Thunderbird*](/vi/thunderbird-main) để có thêm thông tin. Và cuối cùng, bạn nên chọn sử dụng [*SSL*](/vi/glossary#SSL) hoặc mã hóa cả hai đường thông tin đi và đến máy chủ dịch vụ thư điện tử của bạn.

<div class="background" markdown="1">
Pablo: Vậy thì, tôi có nên chuyển sang sử dụng Riseup hay tôi nên tiếp tục sử dụng Gmail và chỉ chuyển sang dùng địa chỉ bảo mật ‘https’?

Claudia: Điều đó là do anh quyết định, nhưng có những điều anh cần cân nhắc khi chọn lựa một nhà cung cấp dịch vụ thư điện tử. Trước hết, họ có cung cấp một kết nối an toàn tới hộp thư của anh không? Gmail có cung cấp, nên anh có thể chấp nhận điểm này. Thứ hai, liệu anh có tin tưởng những người quản trị hệ thống sẽ giữ bí mật, không xem hay để lộ thông tin của anh cho ai khác không? Điều này hoàn toàn phụ thuộc thuộc vào anh. Và cuối cùng, anh cũng cần suy nghĩ xem liệu anh có chấp nhận việc anh có thể bị xác định khi sử dụng nhà cung cấp dịch vụ nào đó không. Nói cách khác, liệu có gây phiền phức gì cho anh khi sử dụng một hộp thư có địa chỉ là ‘riseup.net’ hay không, khi mà nó khá phổ biến cho các nhà hoạt động chính trị, hay anh cần một địa chỉ ‘gmail.com’ bình thường? </div>

Cho dù bạn sẽ dùng công cụ bảo mật thư điện tử nào, cần luôn nhớ rằng mọi thư điện tử đều gồm thông tin người gửi và một hay nhiều người nhận. Bản thân bạn chỉ là một phần của bức tranh. Ngay cả khi bạn thực hiện truy cập hộp thư một các bảo mật, cân nhắc kỹ những cảnh báo trong trường hợp đối tác của bạn có thể hoặc không thực hiện khi gửi, đọc và trả lời các thư điện tử. Nên cố gắng tìm hiều xem nhà cung cấp dịch vụ Internet cho đối tác của bạn nằm ở đâu. Thường thì mỗi quốc gia sẽ có mức độ kiểm duyệt khác nhau đối với thư điện tử. Để đảm bảo bảo mật cho truyền thông tin, cả bạn lẫn đối tác của bạn đều cần sử dụng các dịch vụ thư điện tử bảo mật tại những quốc gia an toàn. Và nếu bạn muốn chắc chắn rằng thông tin của bạn không bị can thiệp giữa máy chủ phía bạn hay phía đối tác, cả hai bên đều nên cùng sử dụng các tài khoản từ cùng  một nhà cung cấp dịch vụ thư điện tử. [*RiseUp*](/vi/glossary#RiseUp) là một lựa chọn tốt.

### Thêm một số mẹo giúp tăng cường bảo mật thư điện tử của bạn ###

- Luôn luôn chú ý cảnh giác khi mở các tệp đính kèm theo thư mà bạn không mong đợi, đến từ những người mà bạn không biết hoặc có chứa những tiêu đề đáng ngờ. Khi mở những tệp như vậy, bạn cần chắc chắn rằng phần mềm diệt virut của bạn được cập nhật và hết sức để ý tới những thông báo cảnh báo của trình duyệt hay chương trình quản lý thư điện tử.

- Sử dụng phần mềm ẩn danh như [*TOR*](/vi/glossary#Tor), được trình bày trong [*Chương 8: Làm sao để đảm bảo nặc danh và vượt qua sự kiểm duyệt trên mạng Internet*](/vi/chuong-8), có thể giúp bạn ẩn dịch vụ thư điện tử mà bạn chọn dùng khỏi những kẻ muốn kiểm soát kết nối Internet của bạn. Và, tùy thuộc vào mức độ kiểm duyệt Internet tại quốc gia bạn, bạn có thể cần sử dụng [*TOR*](/vi/glossary#Tor), hay một công cụ vượt rào chặn khác được mô tả trong chương 8, chỉ để truy cập thư điện tử bảo mật như [*RiseUp*](/vi/glossary#RiseUp hay Gmail.

- Khi  tạo một tài khoản thư điện tử mà bạn định dùng nặc danh với mọi người bao gồm cả những người nhận, hay với những diễn đàn công cộng mà bạn cần gửi bài qua thư điện tử, bạn cần chú ý không đăng ký tên người dùng hay ‘Họ và Tên’ có liên quan tới thông tin cá nhân hay công việc ngoài đời của bạn. Trong trường hợp này, cũng nên tránh sử dụng dịch vụ của Yahoo, Hotmail hay các nhà cung cấp khác có đính kèm thông tin [*Địa chỉ IP*](/vi/glossary#IP_address) của bạn theo tin nhắn bạn gửi đi.

- Tùy thuộc vào thực tế những ai có thể truy cập máy tính của bạn, xóa bỏ mọi dấu vết liên quan tới thư điện tử khỏi các tệp tạm thời trên máy cũng quan trọng không kém việc bảo mật thư điện tử của bạn khi truyền qua mạng Internet vậy. Xem [*Chương 6: Làm sao để phá hủy những thông tin nhạy cảm*](/vi/chuong-6) và [*Hướng dẫn sử dụng CCleaner*](/vi/ccleaner-main) để biết thêm chi tiết.

