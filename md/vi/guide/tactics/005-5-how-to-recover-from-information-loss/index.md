

---

lang: vi
community: guide
type: tactics
legacy: True
child: False
weight: 005
title: 5. How to recover from information loss

---

Mỗi phương thức lưu trữ và truyền dữ liệu số đều có những đặc điểm khiến thông tin có khả năng bị xóa, lấy cắp hay phá hủy. Công sức hàng năm trời có thể bị phá hủy trong giây lát do bị lấy cắp, do một một giây bất cẩn, do bị tịch thu phần cứng hay đơn giản chỉ vì bản thân công nghệ lưu trữ kỹ thuật số tiềm ẩn nguy cơ. Có một câu nói phổ biến trong giới chuyên gia hỗ trợ máy tính là  &quot;Không có câu hỏi là có bao giờ dữ liệu của bạn bị mất không; chỉ có câu hỏi là điều đó xảy ra vào lúc nào&quot;. Vì vậy, khi điều này xảy đến với bạn, điều quan trọng nhất là bạn đã có trong tay bản dự phòng và một phương thức đã được thử nghiệm chắc chắn để thực hiện việc khôi phục. Ngày mà bạn được nhắc nhở về tầm quan trọng của bản sao lưu dữ liệu thì thường là ngày hôm sau bạn sẽ cần dùng đến nó.

Mặc dù là một trong những thành phần cơ bản nhất của bảo mật điện tử, việc xây dựng một chính sách sao lưu dự phòng có hiệu quả không phải đơn giản. Việc này có thể là một vấn đề phức tạp vì nhiều lý do: nhu cầu lưu trữ dữ liệu gốc và dữ liệu sao lưu tại những địa điểm khác nhau về mặt vật lý, tầm quan trọng của việc bảo đảm bí mật thông tin, và khó khăn trong việc quản lý việc chia sẻ dữ liệu giữa nhiều người dùng đang sử dụng những thiết bị lưu trữ lưu động của riêng họ. Ngoài những phương cách sao lưu và khôi phục dữ liệu, chương này cũng giới thiệu hai công cụ chuyên dùng, [*Cobian Backup*](/vi/glossary#Cobian_Backup) và [*Undelete Plus*](/vi/glossary#Undelete_Plus).


### Tình huống cơ bản ###

<div class="background" markdown="1">Elena là nhà hoạt động về môi trường tại một quốc gia nó tiếng Nga, ở đó cô bắt đầu xây dựng một trang web với những trình bày sáng tạo về hình ảnh, phim, bản đồ và những câu truyện để nhấn mạnh những đánh giá về sự tàn phá rừng bất hợp pháp trong khu vực. Cô đã và đang sưu tập những tại liệu, phim ảnh về việc khai thác gỗ trong nhiều năm, và phần lớn thông tin được lưu trong một máy tính cũ chạy hệ điều hành Windows trong văn phòng tại tổ chức Phi chính phủ nơi cô đang làm việc. Trong lúc thiết kế trang web về vấn đề này, cô chợt nhận ra tầm quan trọng của nó và quan tâm tới việc bảo vệ nó trong trường hợp máy tính gặp sự cố, đặc biệt là trong trường hợp điều đó xảy ra trước khi cô kịp tải mọi thông tin lên trên trang web của mình. Những đồng nghiệp khác đôi khi cũng sử dụng chung chiếc máy tính này, nên cô cũng muốn học cách khôi phục dữ liệu của mình trong trường hợp ai đó vô tình xóa các thư mục chứa dữ liệu của cô. Cô hỏi người cháu Nicolai giúp cô xây dựng kế hoạch sao lưu dự phòng.</div>

### Những điều bạn có thể học được từ chương này: ###

- Làm sao để tổ chức và sao lưu thông tin

- Bạn nên lưu trữ dữ liệu dự phòng ở đâu

- Làm sao để quản lý các dữ liệu sao lưu một cách an toàn

- Làm sao khôi phục những tệp vô tình bị xóa

