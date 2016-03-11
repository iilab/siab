

---

lang: vi
community: guide
type: tactics
legacy: True
child: True
weight: 3
depth: 3
title: Anonymity networks and basic proxy servers

---

### Mạng ẩn danh ###

Mạng ẩn danh thường ‘đưa’ luồng thông tin của bạn đi qua nhiều hệ thống [*máy ủy quyền*](/vi/glossary#Proxy) bảo mật nhằm che dấu vị trí hiện tại của bạn và những địa chỉ bạn muốn truy cập. Điều này có thể làm giảm đáng kể tốc độ tải trang web cũng như các dịch vụ Internet khác. Tuy nhiên, với công cụ [*Tor*](/vi/glossary#Tor) là một phương tiện công cộng đáng tin cậy được bảo mật để vượt rào chắn, điều này giúp bạn không phải lo lắng về việc phải đặt lòng tin vào những cá nhân điều hành các [*máy ủy quyền*](/vi/glossary#Proxy) cũng như những trang web bạn truy cập. Và như thường lệ, hãy chắc chắn sử dụng kết nối được mã hóa sử dụng [HTTPS](/vi/glossary#SSL) tới một trang web bảo mật mỗi khi bạn muốn trao đổi những thông tin bí mật như mật khẩu, thư điện tử dùng trình duyệt.

Bạn sẽ phải cài đặt phần mềm để có thể sử dụng [*Tor*](/vi/glossary#Tor), đổi lại bạn sẽ có trong tay một công cụ cho phép vừa ẩn danh vừa có thể giúp vượt rào chắn. Mỗi khi bạn kết nối vào mạng lưới Tor, bạn lựa chọn một tuyến đường ngẫu nhiên qua ba [*máy ủy quyền*](/vi/glossary#Proxy) bảo mật [*Tor*](/vi/glossary#Tor). Điều này đảm bảo rằng cả [*ISP*](/vi/glossary#ISP) của bạn lẫn bản thân các [*máy ủy quyền*](/vi/glossary#Proxy) đều không biết về [*địa chỉ IP*](/vi/glossary#IP_address) của bạn hay địa chỉ dịch vụ Internet bạn yêu cầu. Bạn có thể tìm hiểu thêm nhiều thông tin về công cụ này từ Hướng dẫn sử dụng Tor.

<div class="getstarted" markdown="1">Thực hành: Hãy bắt đầu với [Hướng dẫn sử dụng Tor](/vi/tor-main)</div>

Một trong những điểm mạnh của [*Tor*](/vi/glossary#Tor) là nó không chỉ làm việc với trình duyệt mà có thể sử dụng với nhiều ứng dụng Internet khác. Các chương trình quản lý thư điện tử, bao gồm Mozilla [*Thunderbird*](/vi/glossary#Thunderbird), những công cụ nhắn tin qua mạng như [*Pidgin*](/vi/glossary#Pidgin) đều có thể sử dụng [*Tor*](/vi/glossary#Tor) để sử dụng những dịch vụ bị chặn hay để ẩn danh việc sử dụng những dịch vụ này.

## Những máy ủy quyền cơ bản ###

Có ba câu hỏi quan trọng cần được đặt ra khi bạn lựa chọn một [*máy ủy quyền*](/vi/glossary#Proxy) vượt rào chặn cơ bản. Thứ nhất, đây là một công cụ web hay nó đòi hỏi bạn phải thay đổi các thiết đặt trên máy tính hoặc yêu cầu phải cài đặt phần mềm trên máy của bạn? Thứ hai là nó có bảo mật không? Thứ ba, nó thuộc về tư nhân hay công cộng?

### Những máy ủy quyền dựa sử dụng trình duyệt và các loại khác ###

Những [*máy ủy quyền*](/vi/glossary#Proxy) sử dụng trình duyệt có lẽ là dễ sử dụng nhất. Chúng chỉ yêu cầu bạn dùng trình duyệt mở trang web của [*máy ủy quyền*](/vi/glossary#Proxy), nhập địa chỉ bị chặn mà bạn muốn truy cập và nhấn một nút trên màn hình. Khi đó, [*máy ủy quyền*](/vi/glossary#Proxy) sẽ hiển thị những nội dung được yêu cầu lên chính trang của nó. Bạn có thể mở tiếp những liên kết một cách bình thường hoặc nhập một địa chỉ mới và trang của [*máy ủy quyền*](/vi/glossary#Proxy) nếu bạn muốn xem một trang khác. Bạn không cần phải cài đặt bất cứ phần mềm hay thay đổi bất kỳ thiết đặt nào của trình duyệt, điều đó khiến cho những [*máy ủy quyền*](/vi/glossary#Proxy) sử dụng trình duyệt:

- Dễ sử dụng

- Có thể truy cập từ những máy tính công cộng, như những quán Internet, nơi bạn không được phép cài đặt thêm chương trình hay thay đổi những thiết đặt

- Sẽ an toàn hơn nếu bạn lo ngại bị ‘bắt giữ’ do có phần mềm vượt rào chắn cài đặt trên máy tính của bạn

Những [*máy chủ  ủy quyền*](/vi/glossary#Proxy) dựa trên trình duyệt cũng có nhiều nhược điểm. Không phải lúc nào chúng cũng hiển thị nội dung yều cầu một cách chính xác, nhiều trang của [*máy ủy quyền*](/vi/glossary#Proxy) web thường không hiển thị được nội dung những trang web phức tạp có chứa tính năng tạo luồng âm thanh và phim ảnh. Thêm nữa, cũng như mọi [*máy chủ ủy quyền*](/vi/glossary#Proxy) khác sẽ bị chậm lại khi lượng người sử dụng nó tăng lên, đây sẽ là một vấn đề đối với những [*máy chủ ủy quyền*](/vi/glossary#Proxy) dựa trên trình duyệt công cộng. Và tất nhiên loại [*máy chủ ủy quyền*](/vi/glossary#Proxy) này chỉ làm việc với trình duyệt. Bạn không thể sử dụng những chương trình kiểu như phần mềm nhắn tin qua mạng, hay chương trình quản lý thư điện tử phía người dùng để truy cập những dịch vụ bị chặn thông qua một máy chủ ủy quyền loại này. Cuối cùng, tính bảo mật của những máy chủ ủy quyền dùng trình duyệt được bảo mật bị giới hạn do bản thân chúng phải sử dụng và sửa đổi những thông tin trả về cho bạn từ trang web bạn yêu cầu truy cập. Nếu không làm như vậy, mỗi khi sử dụng, các liên kết sẽ tự kết nối trực tiếp tới địa chỉ đích thay vì qua trang của [*máy chủ ủy quyền*](/vi/glossary#Proxy). Điều này sẽ được thảo luận thêm ở phần tiếp theo.

Các dạng [*máy chủ ủy quyền*](/vi/glossary#Proxy) khác thường yêu cầu bạn cài đặt một chương trình hoặc thay đổi thiết đặt của trình duyệt hoặc hệ điều hành của bạn với một địa chỉ của [*máy chủ ủy quyền*](/vi/glossary#Proxy) bên ngoài. Khi đó, với trường hợp đầu tiên, chương trình được cài đặt sẽ cung cấp các lựa chọn bật và tắt công cụ để thông báo cho trình duyệt của bạn biết là có hay không sử dụng các [*máy ủy quyền*](/vi/glossary#Proxy). Những chương trình này cho phép thay đổi [*máy ủy quyền*](/vi/glossary#Proxy) một cách tự động trong trường hợp một máy bị chặn, như đã đề cập ở phía trên. Với trường hợp bạn phải tự nhập vào địa chỉ riêng của [*máy ủy quyền*](/vi/glossary#Proxy) vào trình duyệt hay hệ điều hành, bạn sẽ cần học cách thay đổi chúng trong trường hợp địa chỉ này cũng bị chặn hoặc trở nên quá chậm.

Mặc dù sẽ phức tạp hơn đôi chút so với việc sử dụng những [*máy  chủ ủy quyền*](/vi/glossary#Proxy) sử dụng trình duyệt, công cụ vượt rào cản này có thể hiển thị các trang có nội dung phức tạp một cách tốt hơn và thường dùng được lâu hơn trước khi chúng trở nên quá chậm do nhiều người dùng chung. Hơn nữa, các loại [*máy chủ ủy quyền*](/vi/glossary#Proxy) phù hợp sẽ được sử dụng cho nhiều loại ứng dụng Internet. Ví dụ [*máy chủ ủy quyền*](/vi/glossary#Proxy) HTTP dùng cho trình duyệt, Máy chủ SOCKS dùng cho ứng dụng thư điện tử và chát, và [*máy chủ ủy quyền*](/vi/glossary#Proxy) VPN có thể định tuyến lưu thông Internet của bạn để tránh bị chặn.

### Các máy chủ ủy quyền bảo mật và không bảo mật ###

Khái niệm [*máy chủ ủy quyền*](/vi/glossary#Proxy) bảo mật dùng trong chương này để chỉ những [*máy chủ ủy quyền*](/vi/glossary#Proxy) hỗ trợ những kết nối được [*mã hóa*](/vi/glossary#Encryption) tới nguời sử dụng chúng. Một [*máy ủy quyền*](/vi/glossary#Proxy) không bảo mật vẫn cho phép bạn vượt qua nhiều loại rào chắn nhưng sẽ không dùng được nếu kết nối Internet của bạn bị kiểm soát và quét chặn những từ khóa hay địa chỉ trang web đặc biệt. Không nên sử dụng một máy chủ ủy quyền không bảo mật để truy cập một trang web bảo mật như trang chủ thư điện tử hay trang giao dịch ngân hàng. Nếu làm như vậy, bạn có thể để lộ những thông tin bí mật mà thường luôn được bảo vệ. Và như đã nêu ở phần trước, những [*máy chủ ủy quyền*](/vi/glossary#Proxy) không bảo mật thường dễ dàng bị phát hiện và chặn bởi nhóm người bảo trì các phần mềm và chính sách lọc chặn. Và trong thực tế có nhiều máy chủ bảo mật nhanh và miễn phí đang hoạt động, nghĩa là càng có ít lý do chính đáng để sử dụng một hệ thống không bảo mật.

Bạn biết rằng một [*máy chủ ủy quyền*](/vi/glossary#Proxy) dựa trên trình duyệt có thể là an toàn nếu bạn truy cập nó sử dụng giao thức [*HTTPS*](/vi/glossary#HTTPS). Cũng giống như các dịch vụ máy chủ thư điện tử, những kết nối mã hóa hay không mã hóa sẽ được hỗ trợ, nên bạn cần đảm bảo sử dụng những loại được mã hóa. Và thường thì trong trường hợp này bạn sẽ nhận được những ‘cảnh báo xác thực bảo mật’ của trình duyệt trước khi tiếp tục. Điều này xảy ra với cả  [*máy chủ ủy quyền*](/vi/glossary#Proxy) [*Psiphon*](/vi/glossary#Psiphon) và [*Peacefire*](/vi/glossary#Peacefire) sẽ được đề cập dưới đây. Những cảnh báo dạng này lưu ý rằng ai đó, có thể là ISP của bạn hay hacker, có thể đang kiểm soát kết nối của bạn tới máy chủ ủy quyền. Cho dù vậy, sử dụng những [*máy ủy quyền*](/vi/glossary#Proxy) bảo mật bất kỳ khi nào có thể vẫn là việc nên làm. Tuy nhiên sử dụng những hệ thống vượt rào chặn kiểu này, bạn nên tránh truy cập những trang web bảo mật, nhập thông tin mật khẩu và trao đổi các thông tin mật trừ khi bạn xác thực được mã nhận dạng [*SSL*](/vi/glossary#SSL)(figureprint) của hệ thống này. Để thực hiện việc này, bạn cần có cách trao đổi với người quản trị [*máy chủ ủy quyền*](/vi/glossary#Proxy) này.

*Phụ lục C* của [*Hướng dẫn sử dụng Psithon*](https://sesawe.net/Using-psiphon-2.html) hướng dẫn từng bước cụ thể để bạn và người quản trị [*máy chủ ủy quyền*](/vi/glossary#Proxy) cần thực hiện để có thể xác thực mã nhận dạng của [*máy chủ ủy quyền*](/vi/glossary#Proxy).
	
Bạn cũng nên tránh truy cập những thông tin mật qua [*máy chủ ủy quyền*](/vi/glossary#Proxy) dựa trên web trừ khi bạn tin tưởng người vận hành nó. Ngay cả khi bạn có nhận được những cảnh báo xác thực hay không khi sử dụng những máy đó. Khi bạn dựa vào một [*máy ủy quyền*](/vi/glossary#Proxy cho mục đích vượt qua kiểm duyệt, người quản trị máy đó sẽ biết được [*địa chỉ IP*](/vi/glossary#IP_address)  của bạn và trang web mà bạn đang truy cập. Quan trọng hơn là đây là một [*máy chủ ủy quyền*](/vi/glossary#Proxy) dựa trên trình duyệt, một kẻ vận hành có ác ý có thể kiểm soát được toàn bộ thông tin truyền giữa bạn và trang web bạn đang truy cập, bao gồm cả nội dung trao đổi thư từ và mật khẩu.
	
Với những [*máy chủ ủy quyền*](/vi/glossary#Proxy) không thuộc dạng dựa trên trình duyệt, có thể bạn nên tìm hiểu xem chúng có hỗ trợ kết nối bảo mật hay không. Tất cả những [*máy ủy quyền*](/vi/glossary#Proxy) và mạng lưới ẩn danh được khuyên dùng trong chương này đều được bảo mật.

## Các máy chủ ủy quyền riêng và công cộng ##

Những [*máy chủ ủy quyền*](/vi/glossary#Proxy) công cộng chấp nhận các kết nối từ bất kỳ người dùng nào, trong khi những [*máy ủy quyền*](/vi/glossary#Proxy) dùng riêng thường yêu cầu nhập tên người dùng và mật khẩu. Dù những máy công cộng có ưu điểm rõ ràng là luôn có sẵn miễn phí, giả sử rằng chúng có thể còn sử dụng được, chúng thường dễ bị quá tải rất nhanh chóng. Và kết quả là dù những hệ thống ủy quyền công cộng có thể có tính năng kỹ thuật và được duy trì không thua kém gì những hệ thống riêng, chúng thường tương đối chậm. Các hệ thống [*máy chủ ủy quyền*](/vi/glossary#Proxy) riêng thường dùng cho các mục đích kinh doanh hoặc do những người quản trị tạo riêng những tài khoản cho những người dùng mà họ có mối quan hệ, cá nhân hay xã hội. Vì lý do đó, rất dễ dàng xác định động cơ của nhưng người vận hành các hệ thống ủy quyền riêng. Tuy nhiên, bạn không nên cho rằng [*máy chủ ủy quyền*](/vi/glossary#Proxy) dùng riêng về cơ bản là đáng tin cậy hơn. Trong quá khứ, những động cơ lợi nhuận đã khiến nhiều dịch vụ trực tuyến đã tiết lộ thông tin người dùng của họ.

Những hệ thống [*máy chủ ủy quyền*](/vi/glossary#Proxy) đơn giản, không được bảo mật thường dễ dàng được tìm thấy bằng công cụ tìm kiếm với những từ khóa như ‘public proxy’, nhưng bạn không nên tin cậy những hệ thống được tìm ra kiểu này. Nếu có thể, tốt hơn hãy chọn một hệ thống[*máy chủ ủy quyền*](/vi/glossary#Proxy) dùng riêng, có bảo mật được vận hành bởi những người mà bạn tin tưởng, về cá nhân hay qua danh tiếng của họ, và những người có trình độ kỹ thuật để đảm bảo bảo mật cho hệ thống của họ. Việc có nên dùng [*máy chủ ủy quyền*](/vi/glossary#Proxy) dựa trên trình duyệt hay không tùy thuộc vào nhu cầu và sự ưu tiên của bạn. Bất kỳ khi nào bạn sử dụng một [*máy chủ ủy quyền*](/vi/glossary#Proxy) với mục đích vượt qua rào chặn, tốt nhất nên dùng trình duyệt [*Firefox*](/vi/glossary#Firefox) có cài đặt thành phần mở rộng [*Noscript*](/vi/glossary#NoScript), được đề cập tại [*Hướng dẫn sử dụng Firefox*](/vi/firefox-main). Làm như vậy có thể giúp bảo vệ bạn khỏi những [*máy ủy quyền*](/vi/glossary#Proxy) giả mạo hay những trang web cố tìm cách xác định [*địa chỉ IP*](/vi/glossary#IP_address) thực của bạn. Cuối cùng, nên ghi nhớ rằng ngay cả những [*máy ủy quyền*](/vi/glossary#Proxy) có [*mã hóa*](/vi/glossary#Encryption)  cũng không giúp bảo mật những trang web không có bảo mật. Bạn phải đảm bảo rằng mình sử dụng một kết nối [*HTTPS*](/vi/glossary#HTTPS) trước khi gửi hoặc nhận những thông tin bí mật.

Nếu bạn không thể tìm được một công ty, tổ chức hay cá nhân nào có dịch vụ máy chủ ủy quyền đáng tin, giá thành tốt và có thể truy cập được từ nước bạn, bạn nên xem xét sử dụng mạng lưới ẩn danh Tor, đã được trình bày ở phía trên ở mục [*Mạng ẩn danh Tor*](#Mạng_ẩn_danh_Tor).

