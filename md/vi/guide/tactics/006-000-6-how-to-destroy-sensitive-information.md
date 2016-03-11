

---

lang: vi
community: guide
type: tactics
legacy: True
child: False
weight: 006
title: 6. How to destroy sensitive information

---

Những chương trước đã đề cập và thảo luận về một số công cụ và thói quen giúp bạn bảo vệ dữ liệu thông tin mật của mình, nhưng nếu bạn quyết định không muốn tiếp tục lưu giữ một số thông tin nữa thì sao? Nếu bạn xác định, lấy ví dụ, chỉ cần giữ lại những bản sao lại đã được mã hóa của một số tệp nào đó là đủ và muốn xóa bản chính đi, thì đâu là cách tốt nhất để xóa? Không may cho bạn là câu trả lời phức tạp hơn bạn nghĩ. Khi bạn xóa một tệp, ngay cả khi bạn đã chọn làm rỗng **Thùng Rác**, nội dung của tệp vẫn còn nằm đâu đó trên ổ đĩa cứng của hệ thống và có thể được khôi phục lại bởi kẻ nào đó có trong tay công cụ phù hợp và chút xíu may mắn.

Để đảm bảo rằng thông tin được xóa không rơi vào tay kẻ xấu, bạn cần sử dụng một công cụ phần mềm giúp xóa thông tin một cách triệt để và vĩnh viễn. [**Eraser**](/vi/glossary#Eraser) là một trong số đó, và sẽ được thảo luận bên dưới đây. Sử dụng [**Eraser**](/vi/glossary#Eraser) cũng giống như việc xé vụn tài liệu chứ không chỉ đơn giản là vò và ném vào thùng rác với hi vọng không ai tìm thấy. Và tất nhiên việc xóa tệp chỉ là một trường hợp của việc bạn muốn phá hủy những thông tin nhạy cảm. Nếu bạn quan tâm tới chi tiết rằng kẻ nào đó với công cụ phù hợp có động cơ chính trị thù địch có khả năng tìm hiểu về tổ chức và công việc của bạn bằng cách đọc được những thông tin mà bạn nghĩ là đã xóa bỏ, có thể bạn sẽ nghĩ tới thêm nhiều thông tin mà bạn muốn hủy một cách triệt để vĩnh viễn, ví dụ như xóa bỏ các bản sao lưu dữ liệu đã lỗi thời, [hủy toàn bộ dữ liệu](/vi/glossary#Wiping) của ổ cứng trước khi cho chúng đi, xóa bỏ các tài khoản cũ và xóa dấu vết các trang web bạn đã xem. [*CCleaner*](/vi/glossary#CCleaner), một công cụ khác được đề cập tại chương này có thể giúp bạn giải quyết vấn đề xóa bỏ những tệp tạm thời được tạo ra bởi hệ điều hành và các ứng dụng trong quá trình bạn sử dụng chúng. 	

### Tình huống cơ bản ###
<div class="background" markdown="1">
Elena là một nhà hoạt động môi trường ở một quốc gia nói tiếng Nga, nơi cô có duy trì một số trang web đang ngày càng được biết đến rộng rãi để phản ánh sự leo thang của hoạt động phá rừng bất hợp pháp tại khu vực. Cô đã tạo một bản sao lưu những thông tin dùng cho trang web, và cô cất giữ nó tại nhà, tại văn phòng nơi làm việc và trong máy tính xách tay của cô. Gần đây cô bắt đầu cất giữ các thông tin về nhật ký của máy chủ và cơ sở dữ liệu thông tin bài viết của những người tham gia diễn đàn. Elena sắp sửa đi ra nước ngoài tham dự một hội thảo lớn của các nhà hoạt động môi trường, một vài người trong số họ đã thông báo rằng máy tính của họ bị đem đi trong hơn một tiếng đồng hồ tại khu vực biên giới. Để đảm bảo thông tin mật của mình, và vì sự an toàn của những thành viên tham gia những diễn đàn mang tính chính trị, cô đã chuyển toàn hộ những bản sao lưu dự phòng ở nhà và văn phòng vào một vùng mã hóa TrueCrypt và xóa các bản sao khỏi máy tính xách tay của mình. Cô nhờ người cháu Nicolai khuyên xem liệu cô có cần làm gì nữa không hay chỉ cần xóa các tệp khỏi máy tính vì cô lo lắng về việc máy tính của cô có thể bị khám xét bởi các nhân viên tại vùng biên giới. </div>

### Những điều bạn có thể học được từ chương này: ###

- Làm sao để xóa vĩnh viễn những thông tin nhạy cảm khỏi máy tính của bạn

- Làm sao để phá hủy thông tin lưu trên các ổ đĩa lưu động như thẻ nhớ USB và đĩa CD

- Làm sao để ngăn chặn ai đó biết được những tài liệu mà bạn đã sử dụng gần đây

- Làm sao để thiết lập máy tính của bạn để những tài liệu đã được xóa không thể khôi phục lại trong tương lai


