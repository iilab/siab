

---

lang: vi
community: guide
type: tactics
legacy: True
child: True
weight: 4
depth: 3
title: Advanced Email Security

---

Những công cụ và khái niệm được thảo luận dưới đây được khuyên dùng đối với những người dùng máy tính có kinh nghiệm.

### Sử dụng việc mã hóa với khóa công khai trong thư điện tử ###

Việc đạt được mức độ bảo mật ở mức cao hơn là hoàn toàn có thể, ngay cả với những tài khoản thư điện tử không bảo mật. Để đạt được điều này, bạn cần tìm hiểu về việc [*mã hóa*](/vi/glossary#Encryption) với khóa công khai. Kỹ thuật này cho phép bạn [*mã hóa*](/vi/glossary#Encryption)  từng bức thư điện tử, khiến chúng không thể bị đọc bởi bất kỳ ai ngoài những người thực sự được gửi tới. Điều tuyệt vời của việc [*mã hóa*](/vi/glossary#Encryption)  với khóa công khai ở chỗ bạn không cần trao đổi bất kỳ thông tin bí mật nào với đối tác liên lạc về việc làm sao để có thể mã hóa mọi thông tin trong tương lai.

<div class="background" markdown="1">
Pablo: Nhưng tất cả những điều này hoạt động thế nào?

Claudia: Thuật toán thông minh! anh mã hóa những bức thư điện tử gửi cho ai đó sử dụng ‘khóa công khai’ của người đó, khóa này được cung cấp một cách công khai. Sau đó, Người nhận này sẽ sử dụng ‘khóa riêng’ của họ, những khóa riêng này được họ giữ cẩn thận và được dùng để đọc những bức thư được mã hóa. Về phía mình, các đối tác của anh cũng sẽ sử dụng khóa công khai của anh để mã hóa nội dung thư mà họ gửi cho anh. Vậy nên kết quả là, hai bên vẫn phải phải trao đổi khóa công khai, nhưng việc này có thể thực hiện một cách công khai, không phải lo lắng bởi vì ai muốn có khóa công khai của anh đều có thể có được nó. </div>

Kỹ thuật này có thể được sử dụng với bất kỳ dịch vụ thư điện tử nào, ngay cả những dịch vụ thiếu tính bảo mật cho đường truyền, vì nội dung từng bức thư đều đã được [*mã hóa*](/vi/glossary#Encryption)  trước khi chúng rời khỏi máy tính của bạn.

Cần ghi nhớ rằng, với việc sử dụng [*mã hóa*](/vi/glossary#Encryption) , bạn có thể gây sự chú ý về bản thân mình. Loại mã hóa được sử dụng khi bạn truy cập các trang web, bao gồm cả các tài khoản thư điện tử, thường được coi là it đáng ngờ hơn là những loại [*mã hóa*](/vi/glossary#Encryption)  dùng khóa công khai được bàn luận ở đây. Trong một số trường hợp, nếu một thông tin được mã hóa bị kiểm duyệt, hay được tải lên trên một diễn đàn công cộng, nó có thể gây trách nhiệm cho người gửi thông tin đó mà không cần biết đến nội dung của thông tin là gì. Nhiều khi bạn sẽ phải chọn lựa giữa mức độ bảo mật thông tin với việc tránh bị nghi ngờ.

### Việc mã hóa và xác thực cho từng thư điện tử ###

[*Mã hóa*](/vi/glossary#Encryption) dùng khóa công khai ban đầu có vẻ phức tạp, nhưng nó khá dễ hiểu sau khi bạn nắm vững những kiến thức cơ bản, đồng thời các công cụ thực hiện nó khá dễ để sử dụng. Chương trình quản lý thư điện tử [*Thunderbird*](/vi/glossary#Thunderbird)  có thể được sử dụng kết hợp với một thành phần mở rộng là [*Enigmail*](/vi/glossary#Enigmail) để mã hóa và giải mã hóa thư một cách rất dễ dàng.

<div class="getstarted" markdown="1">**Thực hành: Hãy bắt đầu với [***Hướng dẫn sử dụng Thunderbird***](/vi/thunderbird-main)**</div>|

[*VaultletSuite 2 Go*](/vi/glossary#VaultletSuite), một chương trình quản lý thư điện tử có mã hóa miễn phí thậm chí còn dễ sử dụng hơn cả Thunderbird nếu bạn sẵn sàng tin cậy công ty cung cấp công cụ này và cho phép họ thực hiện nhiều phần việc giúp bạn.

<div class="getstarted" markdown="1">Thực hành: Hãy bắt đầu với [Hướng dẫn sử dụng VaultletSuit2Go](/vi/vaultletmail-main)</div>

Việc xác thực cho thư điện tử của bạn là một phần quan trọng trong quá trình bảo mật truyền thông của bạn. Bất kỳ ai có truy cập Internet và những công cụ thích hợp đều có thể giả mạo bạn bằng cách gửi thư từ những tài khoản thư giả mạo có những thông tin xác định cá nhân bạn. Mối nguy hiểm càng rõ ràng hơn khi cân nhắc vấn đề này trong vai trò là người nhận thư. Lấy ví dụ, Hãy tưởng tượng, một mối nguy cơ có thể gây ra do một bức thư điện tử được cho là gửi từ một đối tác tin cậy nhưng thực tế là bởi một kẻ nào đó có mục đích phá hoại các hoạt động của bạn và tìm cách lấy những thông tin bí mật của tổ chức bạn.

Do chúng ta không thể nhìn hay nghe thấy đối tác của mình qua thư điện tử, chúng ta thường dựa vào địa chỉ của người gửi để xác định đối tác, điều này rất dễ khiến chúng ta bị lừa gạt bởi những bức thư bị giả mạo. [*Chữ ký điện tử*](/vi/glossary#Digital_signature), một kỹ thuật cũng sử dụng [*mã hóa*](/vi/glossary#Encryption) với khóa công khai, cung cấp phương thức xác thực danh tính của một người khi gửi thư điện tử. Mục *Sử dụng Enigmail với Thunderbird như thế nào* trong [*Hướng dẫn sử dụng Thunderbird*](/vi/thunderbird-main) giải thích vấn đề này được thực hiện ra sao.

<div class="background" markdown="1">
Pablo: Tôi có một đồng nghiệp từng nhận được một thư điện tử từ tôi mà tôi thực tế chưa bao giờ gửi. Chúng tôi đã cho rằng đó chỉ là một thư rác, nhưng bây giờ tôi có thể tưởng tượng một bức thư giả mạo có thể gây nguy hại biết chừng nào khi nó xuất hiện trong hòm thư của không đúng người không đúng thời điểm. Tôi đã nghe chị nói rằng việc này có thể được ngăn chặn bằng cách sử dụng chữ ký điện tử, nhưng đó là gì vậy*

Một chữ ký điện tử giống như một nhãn sáp dán trên mép một phong bì đựng thư. Chỉ có điều là nó không thể bị giả mạo. Nó chứng thực rằng anh thực sự là người gửi đi bức thư và bức thư không bị thay đổi trong suốt đường truyền đến đích.</div>


