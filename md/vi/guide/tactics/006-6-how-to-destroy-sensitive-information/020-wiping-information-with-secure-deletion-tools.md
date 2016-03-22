

---

lang: vi
community: guide
type: tactics
legacy: True
child: True
weight: 2
depth: 3
title: Wiping information with secure deletion tools

---

Khi bạn sử dụng một công cụ xóa an toàn, như những công cụ được giới thiệu trong chương này, sẽ chính xác hơn để nói rằng bạn thay thế, ‘ghi đè’ lên những thông tin nhạy cảm chứ không chỉ đơn thuần là xóa chúng. Nếu bạn tưởng tượng rằng những tài liệu được lưu tại chiếc tủ tài liệu tưởng tượng ban nãy được viết bằng bút chì, thì việc [*xóa chúng một cách an toàn*](/vi/glossary#Wiping) không chỉ đơn thuần là tẩy đi nội dung các tài liệu mà còn gạch loằng ngoằng đè lên từng chữ một. Cũng giống như đầu bút chì, thông tin số có thể bị đọc cho dù là trong tình trạng rất kém ngay cả khi nó đã bị xóa hoặc thậm chí bị ghi đè lên. Bởi lý do này, những công cụ được giới thiệu dưới đây ghi đè lên các tệp cần xóa một vài lần bằng những dữ liệu ngẫu nhiên. Quá trình này gọi là [*hủy thông tin*](/vi/glossary#Wiping), và thông tin càng được ghi đè nhiền lần, nó càng khó bị khôi phục bởi ai đó để lấy dữ liệu gốc. Các chuyên gia thường đồng ý rằng cần thực hiện việc ghi đè ba lần hoặc nhiều hơn; một số tiêu chuẩn khác yêu cầu tối thiểu bảy lần. Phần mềm hủy dữ liệu tự động đưa ra số lần ghi đè phù hợp, nhưng bạn có thể thay đổi các thiết đặt đó nếu bạn muốn.

### Hủy tài liệu ###

Có hai cách chung để [*hủy những tài liệu bí mật*](/vi/glossary#Wiping) của bạn khỏi ổ cứng hay các thiết bị lưu trữ. Bạn có thể chỉ xóa những tệp đó hoặc có thể [*xóa sạch*](/vi/glossary#Wiping) toàn bộ không gian ‘chưa được cấp phát’ trên ổ cứng. Trong khi đưa ra sự lựa chọn, có thể hữu ích nếu bạn suy nghĩ về trường hợp tủ đựng tài liệu trong ví dụ phía trên – những báo cáo dài có thể có những bản sao không hoàn chỉnh nằm rải rác ở đâu đó trong ổ cứng của bạn ngay cả khi chỉ có một tệp chính là được nhìn thấy. Nếu bạn chỉ hủy bỏ một tệp, bạn có thể chắc chắn rằng tệp đó đã được [xóa vĩnh viễn](/vi/glossary#Wiping), nhưng bạn vẫn để những bản sao khác tồn tại. Thực tế, không có cách nào để truy cập những tệp đó một cách trực tiếp, bởi chúng không được thấy nếu không có những phần mềm đặc biệt. Bằng cách [*xóa sạch toàn bộ*](/vi/glossary#Wiping) không gian trống trên ổ cứng của mình, bạn đảm bảo rằng mọi thông tin đã được xóa trước đây sẽ được hủy hoàn toàn. Quay trở lại trường hợp tủ tài liệu được gắn nhãn trong ví dụ, quá trình trên tương ứng với việc tìm toàn bộ tài liệu trong tủ, tẩy hết thông tin và ghi đè nhiều lần lên toàn bộ mọi tài liệu nằm trong các ngăn đã bị bóc nhãn.

[**Eraser**](/vi/glossary#Eraser) là một phần mềm xóa an toàn miễn phí mã nguồn mở, và rất dễ sử dụng. Bạn có thể [xóa triệt để](/vi/glossary#Wiping) các tệp sử dụng [**Eraser**](/vi/glossary#Eraserr)er với ba cách sau: chọn xóa từng tệp, xóa nội dung của Thùng Rác, hay chọn tẩy xóa toàn bộ không gian chưa sử dụng trên ổ cứng. [**Eraser**](/vi/glossary#Eraser) có thể xóa nội dung của [*tệp nhớ đệm*](/vi/glossary#Swap_file) của Windows, sẽ được thảo luận bên dưới.

<div class="getstarted" markdown="1">
Thực hành: Hãy bắt đầu với [Hướng dẫn sử dụng Eraser](/vi/eraser-main)
</div>

Cho dù các công cụ xóa an toàn không làm tổn hại đến những tệp khác đang tồn tại trong hệ thống trừ khi bạn muốn làm điều đó, bạn cũng cần hết sức chú ý khi sử dụng chúng. Suy cho cùng, sự cố vẫn luôn xảy ra và đó là lý do tại sao mà mọi người lại thấy rằng **Thùng Rác** và các công cụ phục hồi dữ liệu khác rất là hữu ích. Nếu bạn có thói quen luôn xóa vĩnh viễn dữ liệu, bạn sẽ không thể khôi phục lại dữ liệu khi vô tình xóa nhầm. Cần luôn chắc chắn rằng bạn có một bản sao lưu an toàn trước khi bạn xóa một lượng lớn dữ liệu khỏi máy tính.

<div class="background" markdown="1">
Elena: Cô biết rằng những chương trình xử lý văn bản như MicroSoft Words hay Open Office đôi khi tạo những bản sao tạm thời cho một tệp trong lúc người dùng đang làm việc với tệp đó. Liệu những chương trình khác có cũng làm như vậy không, hay cô chỉ nên quan tâm tới những tệp mà bản thân cô tạo và xóa thôi?’

Nicolai: Thực tế là máy tính để lại rất nhiều dấu vết về thông tin cá nhân và thông tin các hoạt động trực tuyến của cô khắp nơi trong máy. Cháu đang nói về các trang web mà cô viếng thăm, bản nháp của thư điện tử mà cô mới tạo gần đây và những thứ tương tự như thế. Tất cả những thông tin này có thể là thông tin nhạy cảm và phụ thuộc vào mức độ thường xuyên cô sử dụng máy tính.</div>

### Hủy bỏ thông tin đệm tạm thời ###

Tính năng cho phép [*Eraser*](/vi/glossary#Eraser) có thể [*xóa triệt để*](/vi/glossary#Wiping)  toàn bộ không gian chưa được cấp phát trên ổ đĩa có thể không nguy hiểm như ta nghĩ, bởi nó chỉ xóa sạch những nội dung đã được xóa trước đó. Thông thường thì một tệp chưa bị xóa sẽ không bị ảnh hưởng. Mặt khác, điều hiển nhiên này lại chỉ ra một vấn đề: [*Eraser*](/vi/glossary#Eraser) không thể giúp bạn xóa sạch những thông tin mà chưa từng bị xóa mà có thể được ẩn rất kỹ ở đâu đó. Những tệp chứa dữ liệu này có thể nằm trong những thư mục ẩn, hay có những cái tên không được để ý. Điều này có thể không phải thực sự là quan trọng với các loại tệp tài liệu nhưng lại có thể vô cùng quan trọng đối với các thông tin được thu thập tự động bất cứ khi nào bạn sử dụng máy tính. Có thể kể ra và ví dụ:
 Những thông tin tạm thời được ghi lại bởi trình duyệt khi bạn hiển thị các trang web, bao gồm văn bản, hình ảnh,**cookies**, thông tin tài khoản, thông tin cá nhân được sử dụng khi điền các biểu mẫu trực tuyến, và lịch sử các trang web bạn hay truy cập.

- Các tệp tạm thời được lưu bởi nhiều ứng dụng với mục đích giúp bạn khôi phục dữ liệu trong trường hợp máy tính xảy ra sự cố trước khi bạn kịp lưu lại công việc đang làm. Những tệp này có thể bao gồm văn bản, hình ảnh, dữ liệu bảng tính và tên của các tệp khác cùng với các thông tin nhạy cảm khác.
-  Những tệp tạm và những liên kết được lưu bởi Windows nhằm tạo sự thuận tiện, như các đường dẫn tắt đến ứng dụng mà bạn hay sử dụng gần đây, đường dẫn rõ ràng tới các thư mục mà bạn muốn ẩn giấu và tất nhiên là dữ liệu trong Thùng Rác mà bạn quên không xóa.

- [*Tệp nhớ đệm*](/vi/glossary#Swap_file) của Windows. Khi bộ nhớ của máy tính bị đầy, ví dụ khi bạn chạy một số chương trình cùng một lúc trên chiếc máy tính cũ, Windows đôi lúc sẽ sao chép dữ liệu bạn đang thao tác vào một tệp có dung lượng lớn gọi là tệp nhớ đệm. Và kết quả là tệp này có khả năng chứa hầu hết mọi thứ, bao gồm các trang web, nội dung tài liệu, mật khẩu và các chìa khóa mã hóa. Ngay cả khi bạn tắt hoặc khởi động lại máy, những [*tệp đệm này*](/vi/glossary#Swap_file) cũng không bị xóa đi do vậy bạn cần thực hiện việc này một cách thủ công.

Để có thể xóa những tệp tạm thời trên máy tính của bạn, bạn có thể sử dụng một công cụ miễn phí có tên là [*CCleaner*](/vi/glossary#Ccleaner), được thiết kế để xóa triệt để thông tin sau khi sử dụng Internet Explorer, Mozilla Firefox, Microsoft Office (được biết đến với nguy cơ để lộ thông tin dữ liệu)... cũng như làm sạch bản thân hệ điều hành. CCleaner có khả năng xóa các tệp một cách triệt để an toàn, nhờ đó giúp bạn không phải xóa sạch các vùng nhớ chưa cấp phát sử dụng [*Eraser*](/vi/glossary#Eraser) sau mỗi lần bạn sử dụng nó.

<div class="getstarted" markdown="1">Thực hành: Hãy bắt đầu với [Hướng dẫn sử dụng CCleaner](/vi/ccleaner-main)</div>


