

---

lang: vi
community: guide
type: tactics
legacy: True
child: True
weight: 2
depth: 3
title: Hiding your sensitive information

---

Một vấn đề của việc cất giữ một chiếc két an toàn trong nhà hay ở văn phòng, không nói đến việc mang theo một cái trong túi áo, là nó thường khá dễ nhận thấy. Nhiều người có quan ngại chính đáng về việc tự thu hút sự chú ý do sử dụng việc [*mã hóa*](/vi/glossary#Encryption). Việc có nhiều l‎ý do chính đáng cho việc sử dụng hơn là không sử dụng [*mã hóa*](/vi/glossary#Encryption) không làm cho nguy cơ này bớt phần thực tế. Hai l‎ý do thiết thực tại sao bạn nên tránh sử dụng các công cụ như [*TrueCrypt*](/vi/glossary#TrueCrypt): nguy cơ của việc tự thu hút sự chú ý và nguy cơ để lộ vị trí cất giữ thông tin mật.

### Cân nhắc nguy cơ tự thu hút sự chú ý ###

Việc [*mã hóa*](/vi/glossary#Encryption) là trái pháp luật ở một số quốc gia, có nghĩa là việc tải về và cài đặt hay sử dụng các phần mềm loại này có thể bị coi là phạm pháp. Đồng thời, nếu cảnh sát, quân đội hay các lực lượng đặc nhiệm là nhóm đối tượng bạn muốn bảo vệ thông tin khỏi bị lọt rơi vào, thì việc vi phạm luật này có thể là cái cớ để qua đó các hoạt động của bạn bị điều tra hoặc cơ quan của bạn có thể bị làm phiền. Tuy nhiên trong thực tế, mối nguy cơ này chẳng hề liên quan gì tới tính hợp pháp của các công cụ. Bất kỳ khi nào, nếu chỉ cần có dính líu một chút xíu tới việc sử dụng  các phần mềm [*mã hóa*](/vi/glossary#Encryption) cũng đủ để quy kết bạn hoạt động phạm pháp hay gián điệp (không quan tâm tới dữ liệu thực tế bạn lưu trữ trong vùng [*mã hóa*](/vi/glossary#Encryption)) thì bạn sẽ phải suy nghĩ cẩn thận việc dùng các công cụ này có phù hợp trong hoàn cảnh thực tế của bạn không.

Nếu đây là thực tế, bạn có một số lựa chọn sau:

- Bạn hoàn toàn tránh sử dụng các phần mềm bảo mật dữ liệu, có nghĩa là bạn chỉ lưu trữ nhưng dữ liệu không bí mật hay phát minh ra môt hệ thống mã hóa từ ngữ để bảo vệ các thành phần quan trọng của các tệp tin mật.

- Bạn có thể dựa trên một kỹ thuật gọi là [*kỹ thuật ẩn giấu ngữ nghĩa*](/vi/glossary#Steganography) để giấu thông tin mật, thay vì mã hóa nó. Có những công cụ giúp bạn thực hiện việc này, nhưng để sử dụng chúng một cách đúng đắn đòi hỏi sự chuẩn bị hết sức kỹ càng, và bạn vẫn đối diện với nguy cơ thu hút sự chú ý của những kẻ biết rõ công cụ bạn đã sử dụng.

- Bạn cũng có thể thử lưu trữ dữ liệu mật của mình trên các tài khoản tại những trang web được bảo mật, nhưng điều này đòi hỏi một kết nối mạng đáng tin cậy và sự am hiểu tốt về máy tính và các dịch vụ Internet. Kỹ thuật này cũng giả định rằng việc [*mã hóa*](/vi/glossary#Encryption) đường truyền mạng không thu hút sự chú ý (như mã hóa tệp tin) cũng như bạn không sao chép nhầm dữ liệu nhạy cảm lên trên máy tính của mình và quên ở đó.

- Bạn có thể lưu các thông tin mật trên các thẻ nhớ USB hay thiết bị nhớ lưu động. Tuy nhiên những thiết bị này thậm chí dễ dàng bị mất hay bị tước đoạt hơn là máy tính, vì vậy việc mang những thông tin mật không được [*mã hóa*](/vi/glossary#Encryption) trong những thiết bị này là một điều không nên làm.

- Nếu cần thiết bạn có thể sử dụng một loạt những phương cách trên. Tuy nhiên, thậm chí trong trường hợp bạn quan ngại về việc tự gây sự chú ý, có lẽ vẫn là an toàn nhất khi sử dụng [*TrueCrypt*](/vi/glossary#TrueCrypt) với sự cố gắng ngụy trang vùng mã hóa một cách tốt nhất có thể được.

- Nếu muốn tạo một vùng [*mã hóa*](/vi/glossary#Encryption) ít gây sự chú ý nhất, bạn có thể thay đổi tên để nó trông giống như bất kỳ một loại tệp nào khác. Sử dụng tệp dạng ‘.iso’ để ngụy trang là tệp hình ảnh của đĩa CD, đây là một lựa chọn phù hợp cho các vùng lưu trữ lớn cỡ khoảng 700MB. Các dạng mở rộng khác của tệp thường phù hợp cho những vùng nhớ nhỏ hơn. Việc làm này giống như giấu chiếc két an toàn sau bức tranh trong tường văn phòng. Nó có thể không che được những rà xoát kỹ lưỡng nhưng cũng đem lại mức độ bảo vệ nào đó. Bạn có thể thay đổi tên của chương trình [*TrueCrypt*](/vi/glossary#TrueCrypt), giả định rằng bạn sẽ lưu nó như các tệp khác trên ổ cứng máy tính hay thẻ nhớ USB chứ không cài đặt lên máy tính. Phần 

[***Hướng dẫn Sử dụng TrueCrypt***](/vi/truecrypt-main) sẽ giải thích cách thực hiện.

### **Cân nhắc nguy cơ để lộ thông tin mật** ###

Thường thì bạn ít để tâm tới hậu quả của việc ‘bị bắt’ với phần mềm [*mã hóa*](/vi/glossary#Encryption) lưu trữ trong máy hay thẻ nhớ USB mà thường quan tâm rằng các vùng mã hóa sẽ chỉ ra chính xác nơi bạn cất giấu những dữ liệu bí mật mà bạn muốn bảo vệ. Có thể đúng khi cho rằng không ai khác có thể đọc được chúng, kẻ xâm nhập có thể biết rằng dữ liệu nằm ở đó, và rằng bạn đang tìm mọi cách để bảo vệ nó. Điều này dẫn bạn tới những phương cách phi điện toán mà kẻ thù có thể sử dụng để lấy được quyền truy cập dữ liệu như: đe dọa, tống tiền, khủng bố và tra tấn. Trong trường hợp này, tính năng ‘có thể chối bỏ’ của [*TrueCrypt*](/vi/glossary#TrueCrypt), sẽ được trình bày chi tiết dưới đây, sẽ đem lại sự hữu ích.

Tính năng ‘có thể chối bỏ’ của [*TrueCrypt*](/vi/glossary#TrueCrypt) là một tính năng vượt trội so với các các công cụ [*mã hóa*](/vi/glossary#Encryption) tệp khác. Tính năng này có thể được coi là một dạng riêng của [*kỹ thuật ẩn giấu nội dung*](/vi/glossary#Steganography) giúp ẩn giấu dữ liệu nhạy cảm nhất của bạn so với các thông tin được ẩn giấu khác, ít nhạy cảm hơn. Nó tương tự như việc làm một cái đáy giả mỏng bên trong một cái đáy giả không quá mỏng cho cái két an toàn tại văn phòng bạn.  Nếu một kẻ xâm nhập lấy trộm được chìa khóa két an toàn, hoặc đe dọa bạn phải đưa cho hắn thông tin mở khóa, hắn sẽ tìm thấy những thông tin ‘ngụy trang’, chứ không phải những thông tin mà bạn thực sự muốn bảo vệ.

Chỉ có mình bạn biết rằng két an toàn của bạn có chứa một ngăn ẩn phía sau. Điều này cho phép bạn ‘chối bỏ’ rằng bạn còn giữ thêm bất cứ thông tin nào ngoài những thông tin bạn đã đưa cho kẻ thù, và có thể giúp bạn trong tình huống bạn phải tiết lộ mật khẩu vì lý do nào đó. Những lý do này có thể bao gồm những đe dọa về pháp lý hay thể chất đối với bạn, hay đối với tới đồng nghiệp, đồng minh hoặc bạn bè, người thân trong gia đình. Mục đích của việc có thể chối bỏ cho bạn cơ hội để thoát khỏi nguy cơ rơi vào tình huống nguy hiểm cho dù bạn chọn cách cố gắng bảo vệ dữ liệu của mình. Tuy nhiên như đã đề cập tại phần ***Cân nhắc nguy cơ tự thu hút sự chú ý***, tính năng này không có tác dụng nếu chỉ đơn thuần bị bắt với chiếc két an toàn trong văn phòng cũng đủ đưa bạn tới những hậu quả không chấp nhận được.

Tính năng có thể chối bỏ của [*TrueCrypt*](/vi/glossary#TrueCrypt) được thực hiện bằng cách tạo một ‘vùng [*mã hóa*](/vi/glossary#Encryption) ẩn’ bên trong ‘vùng [*mã hóa*](/vi/glossary#Encryption)’ thông thường của bạn. Bạn mở vùng dữ liệu ẩn này bằng cách nhập một mật khẩu khác với mật khẩu thông thường bạn dùng. Ngay cả khi một kẻ xâm nhập với kỹ thuật tinh vi có được mật khẩu truy cập vùng mã hóa thông thường, hắn cũng không thể chứng minh rằng vùng mã hóa ẩn thực sự tồn tại. 

Tất nhiên, có khả năng hắn cũng biết rõ rằng [*TrueCrypt*](/vi/glossary#TrueCrypt) có khả năng che giấu thông tin theo cách này, không có gì đảm bảo rằng các mối đe dọa sẽ không còn một khi bạn tiết lộ cho hắn thông tin mật khẩu ‘mồi’. Rất nhiều người sử dụng [*TrueCrypt*](/vi/glossary#TrueCrypt) không bật tính năng có thể chối bỏ, tuy nhiên điều này được coi là không thể xác định được, theo cách phân tích, liệu vùng mã hóa này có chứa ‘đáy giả’ hay không. Với điều này, việc của bạn là đảm bảo rằng bạn không để lộ vùng mã hóa ẩn do các lỗi phi kỹ thuật như để nó ở tình trạng mở hoặc để lại các đường dẫn tới tệp nằm trong vùng này. Mục [*Đọc thêm*](/vi/chuong_4_3) bên dưới có thể chỉ dẫn bạn tới thêm thông tin về vấn đề này

<div class="background" markdown="1">
Claudia: Được thôi, vậy hãy bỏ một chút dữ liệu vớ vẩn vào vùng mã hóa chuẩn, và sau đó có thể lưu toàn bộ thông tin chứng cứ vào vùng ẩn. Anh có ít tài liệu PDF cũ hay cái gì đại loại như vậy không?

Pablo: Ừ, anh cũng đã nghĩ về điều đó. Ý anh là ý tưởng đưa ra mật khẩu mồi chỉ trong trường hợp chúng ta không có lựa chọn nào khác, phải không? Nhưng để điều đó có tính thuyết phục, chúng ta cần làm sao để những tệp này trông có vẻ như quan trọng, em có nghĩ như vậy không? Nếu không phải vậy thì tại sao chúng ta phải mất công mã hóa chúng? Có lẽ chúng ta sử dụng những tài liệu tài chính không có liên quan hoặc một danh sách các mật khẩu trang web hay cái gì đó tương tự.
</div>

