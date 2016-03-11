

---

lang: vi
community: guide
type: tactics
legacy: True
child: True
weight: 2
depth: 3
title: Communicating (Voice and Messages) via Smartphone

---

## Hội thoại An toàn ##

### Cơ bản về điện thoại ###

Trong chương [[***9.2.2  sự ẩn danh***](/vi/chuong_9_2_2) chúng tôi đã thảo luận các phương pháp khác nhau bạn nên cân nhắc để giảm nguy cơ bị chặn nghe lén khi sử dụng mạng hạ tầng điện thoại di động của nhà cung cấp dịch vụ để đàm thoại.

Sử dụng Điện thoại thông minh kết nối Internet hay WiFi có thể cung cấp các cách liên lạc bảo mật hơn có thể kể đến như sử dụng thoại qua giao thức IP [*VoIP*](/en/Glossary#VoIP) và áp dụng các phương thức bảo mật kênh truyền liên lạc này. Một số công cụ cho điện thoại thông minh còn có thể mở rộng cách thức bảo mật cho không chỉ VoIP, mà cả cho các cuộc gọi điện thoại di động. (Xem **Redphone** bên dưới).

Dưới đây là danh sách các công cụ với các điểm mạnh và yếu:

### Skype ###

Là ứng dụng VoIP thương mại phổ biến nhất, [*Skype*](/vi/glossary#skype), có phiên bản cho mọi nền tảng điện thoại thông minh và hoạt động hiệu quả khi kết nối không dây của bạn ổn định. Kết nối qua đường mạng điện thoại di động kém ổn định hơn.

Trong [***Phần 3***](/vi/chuong_7_3) của [***Chương 7: Làm thế nào để bảo mật truyền thông Internet***](/vi/chuong_7_3), chúng tôi đã đề cập tới nguy cơ khi sử dụng Skype cùng với nguyên nhân tại sao nếu có thể thì nên tránh sử dụng. Nhìn chung, Skype là một phần mềm không phải Nguồn Mở và rất khó để có thể xác nhận một cách độc lập mức độ bảo mật của phần mềm này. Hơn thế nữa, Skype đã bị sở hữu bởi Microsoft, họ có lợi ích thương mại để quan tâm tới việc tìm hiểu bạn sử dụng Skype khi nào và ở đâu. Skype cũng có thể cho phép các cơ quan thực thi luật pháp truy xuất mọi thông tin lịch sử liên lạc của bạn. 

### Các ứng dụng VoIP khác ###

Liên lạc sử dụng ứng dụng VoIP thường là miễn phí (hoặc giảm chi phí đáng kể so với các cuộc gọi di động thông thường) và để lại it dấu vết liên lạc. Trên thực tế một phiên liên lạc VoIP bảo mật là cách an toàn nhất để đàm thoại.

 [**CSipSimple**](http://f-droid.org/repository/browse/?fdid=com.csipsimple&fdpage=4) là phần mềm VoIP mạnh mẽ cho các điện thoại Android được phát triển và duy trì tốt cùng với nhiều tính năng trợ giúp thiết đặt cho các dịch vụ VoIp khác nhau.

 [**Mạng Thoại Bảo mật Kiến trúc Mở (OSTN)**](https://guardianproject.info/wiki/OSTN) và máy chủ cung cấp bởi dự án Guardian, [**ostel.me**](https://ostel.me), gần đây đưa ra một trong những phương thức kết nối thoại bảo mật nhất. Hiểu rõ và tin tưởng đơn vị vận hành máy chủ VoIP bạn sử dụng để kết nối là một sự cân nhắc quan trọng. Nhà cung cấp máy chủ cho dịch vụ này - [**Guardian Project**](https://guardianproject.info) – nổi tiếng và có uy tín trong cộng đồng.

Khi sử dụng CsipSimple, bạn không bao giờ kến nối trực tiếp với đối tác liên lạc, thay vào đó luồng dữ liệu sẽ được định tuyến qua máy chủ Ostel. Điều này khiến cho việc theo dõi dữ liệu và tìm ra đối tác liên lạc của bạn. Hơn nữa, Ostel không lưu trữ bất kỳ thông tin dữ liệu nào ngoài thông tin tài khoản cần để đăng nhập. Tất cả dữ liệu thoại được mã hóa bảo mật và ngay cả siêu dữ liệu, thường đã rất khó để khai thác, cũng sẽ trở nên khó khăn hơn khi thông tin được định tuyến qua máy chủ ostel.me. Nếu bạn tải về CsipSimple từ ostel.me, chương trình sẽ được cấu hình trước để sử dụng máy chủ ostel.me khiến cho việc cài đặt và sử dụng rất dễ dàng.

 [**RedPhone**](https://play.google.com/store/apps/details?id=org.thoughtcrime.redphone) là ứng dụng Miễn phí và Nguồn Mở thực hiện việc mã hóa dữ liệu liên lạc thoại giữa hai thiết bị sử dụng phần mềm này. Chương trình rất dễ cài đặt và sử dụng với giao diện quay số và liên lạc truyền thống. Đối tác liên lạc của bạn cần cài đặt và sử dụng RedPhone để đàm thoại với bạn. Để thuận tiện, RedPhone sử dụng số điện thoại của bạn làm thông tin xác nhận (giống như tên người dùng tron các ứng dụng VoIP khác). Tuy nhiên điều này sẽ kiến việc phân tích dữ liệu và truy tìm ngược ra bạn dễ dàng hơn, qua số điện thoại của bạn. RedPhone sử dụng một máy chủ trung tâm, là điểm tập trung dữ liệu và do đó cho phép RedPhone ở vị trí quan trọng (về kiểm soát một số thông tin trên).
Hướng dẫn Thực hành CsipSimple, Ostel.me và Redphone sẽ được giới thiệu tới đây. Bạn có thể tìm hiểu thêm thông tin theo các đường dẫn cung cấp phía trên.

## Gửi Tin nhắn An toàn ##

Bạn nên lưu ý khi gửi tin nhắn SMS và khi nhắn tin trực tuyến trên điện thoại thông minh.

### SMS ###

Như đã mô tả trong [***Chương 9.2.3 Liên lạc qua Tin nhắn – SMS / Tin nhắn***](/vi/chuong_9_2_3), Trao đổi SMS ở mặc định là rất không an toàn. Bất kỳ ai có thể truy cập hạ tầng mạng viễn thông di động đều có khả năng chặn nghe lén các tin nhắn này dễ dàng và đây là điều xảy ra thường xuyên trong nhiều trường hợp. Không tin tưởng sử dụng việc nhắn tin trong các tình huống nghiêm trọng cần bảo mật. Không có cách nào xác thực tin nhắn SMS, do đó sẽ không thể xác định được nội dung tin nhắn có bị thay đổi trong quá trình truyền hay liệu người gửi tin nhắn có thực sự là ai đó mà họ tự nhận không.

### Bảo mật SMS ###

[**TextSecure**](https://play.google.com/store/apps/details?id=org.thoughtcrime.securesms) là công cụ Nguồn Mở Miễn phí [*FOSS*](/en/glossary#FOSS) cho phép gửi và nhận SMS bảo mật trên điện thoại Android. Chương trình cho phép gửi tin nhắn mã hóa và không mã hóa nên bạn có thể sử dụng làm ứng dụng SMS mặc định. Để trao đổi tin nhắn mã hóa, ứng dụng này cần được cài đặt trên cả máy điện thoại của người nhận và người gửi, do đó bạn sẽ cần yêu cầu đối tác liên lạc cài đặt ứng dụng này lên điện thoại của họ. Textsecure tự động xác định khi một tin nhắn mã hóa được gửi đến từ một người dùng Textsecure khác. Chương trình cho phép bạn gửi tin nhắn mã hóa tới nhiều hơn một người nhận. Các tin nhắn sẽ được tự động ký số cho phép việc thay đổi nội dung tin nhắn trên đường truyền là gần như không thể. Trong phần hướng dẫn thực hành Textsecure chung tôi sẽ giải thích chi tiết các tính năng của công cụ này cũng như cách sử dụng.

<div class=getstarted markdown=1>
Thực hành: Hãy bắt đầu với [*Hướng dẫn Textsecure*](/vi/textsecure_main)
</div>

### Nhắn tin trực tuyến An toàn ###

Tin nhắn và trò chuyện trực tuyến sử dụng điện thoại có thể tạo ra nhiều thông tin có nguy cơ bị chặn nghe lén. Những cuộc hội thoại như vậy có thể được sử dụng chống lại bạn bởi các thế lực thù địch về sau này. Chính vì vậy bạn nên hết sức cảnh giác về những gì sẽ trao đổi qua tin nhắn trên điện thoại khi nhắn tin trực tuyến. 
Có một số cách nhắn tin trực tuyến an toàn. Cách tối ưu là dùng phương pháp mã hóa từ gửi tới nhận, bằng cách này bạn có thể chắc chắn rằng người ở đầu kia chính là người bạn muốn trao đổi tin tức.

Chúng tôi khuyến nghị sử dụng [**Gibberbot**](https://guardianproject.info/apps/gibber/) là ứng dụng nhắn tin trực tuyến cho điện thoại Android. Gibberbot cung cấp tính năng mã hóa mạnh và dễ sử dụng để nhắn tin với giao thức Nhắn tin [*Off-the-Record*](/vi/glossary#OTR). Việc mã hóa này cung cấp khả năng xác thực (bạn có thể xác thực rằng bạn đang trao đổi với đúng người) và khả năng bảo mật độc lập cho từng phiên liên lạc đảm bảo nếu việc mã hóa của một phiên liên lạc bị lộ, các phiên liên lạc trong quá khứ và tương lai sẽ vẫn đảm bảo an toàn.
Gibberbot được thiết kế để làm việc với Orbot nên tin nhắn trực tuyến của bạn sẽ được định tuyến qua mạng ẩn danh [*Tor*](/vi/glossary#Tor). Điều này khiến cho việc truy dấu vết hoặc thậm chí việc phát hiện có liên lạc sẽ rất khó khăn.

<div class=getstarted markdown=1>
Thực hành: Hãy bắt đầu với [*Gibberbot Guide*](/vi/gibberbot_main)
</div>

Với điện thoại iPhone, tiện ích [**ChatSecure**](https://chatsecure.org) cung cấp tính năng tương tự, tuy nhiên sẽ không dễ dàng để thiết đặt tiện ích sử dụng với mạng ẩn danh [*Tor*](/vi/glossary#Tor).
Phần Hướng dẫn Thực hành ChatSecure sẽ sớm được giới thiệu. Bạn có thể xem thêm thông tin tại [trang chủ](https://chatsecure.org). 
Với bất kỳ ứng dụng nào bạn sẽ sử dụng, hãy luôn cân nhắc xem tài khoản nào bạn sẽ sử dụng cho việc nhắn tin trực tuyến. Ví dụ khi bạn sử dụng tài khoản Google Talk, Google sẽ biết thông tin đăng nhập và thời gian truy cập của bạn. Đồng thời hãy đồng ý với đối tác liên lạc về việc không lưu lại lịch sử trao đổi đặc biệt là khi những hội thoại này không được mã hóa.


