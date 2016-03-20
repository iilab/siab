

---

lang: vi
community: guide
type: tactics
legacy: True
child: False
weight: 007
title: 7. How to keep your Internet communication private

---

Sự tiện lợi, giá thành rẻ với tính linh hoạt cao của thư điện tử và việc nhắn tin qua mạng khiến chúng trở nên thực sự hữu ích cho các cá nhân và tổ chức ngay cả khi việc kết nối vào Internet rất bị hạn chế. Với những đối tượng có kết nối nhanh và đáng tin cậy hơn, thì phần mềm [*Skype*](/vi/glossary#Skype) và những phần mềm sử dụng công nghệ [*Truyền thoại qua giao thức Internet*](/vi/glossary#VoIP)  cũng tận dụng được ưu điểm kể trên. Không may rằng những giải pháp thay thế các phương tiện liên lạc truyền thống này không phải lúc nào cũng đáng tin cậy để có thể giữ bí mật thông tin nhạy cảm.

Tất nhiên đây không phải là điều gì mới mẻ. Thư tín, các cuộc gọi điện hay tin nhắn điện thoại đều không an toàn, đặc biệt đối với những người sử dụng đang bị theo dõi bởi các cơ quan chức năng.

Một điểm khác biệt quan trọng giữa công nghệ truyền thông số, dựa trên nền tảng Internet với các phương tiện liên lạc truyền thống là nó cho phép người dùng tự xác lập mức độ bảo mật của mình.

Nếu bạn gửi thư điện tử, tin nhắn, hay [*đàm thoại qua mạng*](/vi/glossary#VoIP) sử dụng các phương thức không đảm bảo an ninh, thì một điều chắc chắn rằng chúng có tính bảo mật còn kém hơn cả việc gửi thư tín hay gọi điện thoại thông thường. Điều này một phần do một số hệ thống máy tính mạnh có thể tự động dò tìm một lượng thông tin số khổng lồ để xác định danh tính người nhận và người gửi hay những từ khóa đặc biệt. Việc giám sát ở mức độ tương tự đối với các kênh liên lạc truyền thống thường đòi hỏi một nguồn lực lớn hơn nhiều. Tuy nhiên, nếu bạn có sự đề phòng nhất định, điều ngược lại có thể đúng. Sự đa dạng của các công cụ liên lạc trên Internet và sức mạnh của những phương pháp **mã hóa** tiên tiến có thể đem lại cho bạn mức độ bảo mật từng chỉ có trong quân đội và các lực lượng đặc biệt.

Bằng cách thực hiện theo những hướng dẫn và tìm hiểu những phần mềm được thảo luận trong chương này, bạn sẽ gia tăng khả năng bảo mật cho việc truyền thông của mình. Dịch vụ thư điện tử [*Riseup*](/vi/glossary#RiseUp), mô-dul [Không lưu Dấu vết](/vi/glossary#OTR) (OTR) cho chương trình chát qua mạng [**Pidgin**](/vi/pidgin-main), [**Mozilla Firefox**](/vi/firefox-main), và môdul bổ sung [*Enigmail*](/vi/glossary#Enigmail) cho chương trình quản lý thư điện tử phía người dùng [**Mozilla Thunderbird**](/vi/thunderbird-main) đều là những công cụ hữu hiệu. Tuy nhiên, trong khi sử dụng chúng, bạn nên luôn biết rằng mức độ riêng tư của những cuộc liên lạc không bao giờ được đảm bảo trăm phần trăm. Luôn có những mối nguy cơ mà bạn không lường trước, có thể là một [*chương trình ghi lại những phím được gõ*](/vi/glossary#Keylogger) nằm trên máy của bạn, một kẻ nghe lén ngoài cửa sồ, một thư điện tử phúc đáp bất cẩn hay những điều đại loại như vậy.

Mục đích của chương này là giúp bạn giảm thiểu ngay cả những nguy cơ có thể không xảy ra với bạn, trong khi tránh được phương án cực đoan – mà nhiều người lựa chọn – là không gửi bất cứ thứ gì qua mạng Internet nếu bạn không muốn bị lộ.

### Tình huống cơ bản ###

<div class="background" markdown="1">
Claudia và Pablo làm việc với một Tổ chức Phi chính phủ về nhân quyền ở một quốc gia Nam Mỹ.  Sau vài tháng thu thập thông tin bằng chứng từ các nhân chứng về một loạt hành vi vi phạm nhân quyền của quân đội trong khu vực, Claudia và Pablo bắt đầu tiến hành các bước để bảo vệ kết quả thu thập được. Họ chỉ giữ lại những thông tin cần thiết, và lưu chúng vào một vùng mã hóa TrueCrypt đồng thời sao lưu tại nhiều địa điểm khác nhau.Trong khi chuẩn bị công bố một số phần của những bằng chứng này trong một bản báo cáo, họ nhận ra rằng họ cần phải trao đổi thảo luận những thông tin mật này với các đồng nghiệp ở một nước khác. Mặc dù đã nhất trí không nhắc tới bất kỳ tên hay địa điểm nào, họ vẫn muốn đảm bảo rằng thư điện tử và các tin nhắn qua mạng của họ về chủ đề này được đảm bảo bí mật. Sau khi yêu cầu tổ chức một cuộc họp để thảo luận về tầm quan trọng của việc bảo mật thông tin truyền thông, Claudia hỏi mọi người trong tổ chức xem có ai có câu hỏi nào không. </div>

### Những điều bạn có thể học được từ chương này ###

- Tại sao đa phần các dịch vụ thư điện tử và nhắn tin qua mạng không bảo đảm an toàn

- Làm thế nào để tạo một tài khoản thư điện tử mới bảo mật tốt hơn

- Làm sao để tăng cường bảo mật cho các tài khoản thư điện tử hiện tại

- Làm sao để sử dụng dịch vụ chát qua mạng một cách an toàn

- Phải làm gì khi bạn nghĩ ai đó đang xem trộm hộp thư của mình

- Làm sao để xác thực một phúc đáp thư điện tử

