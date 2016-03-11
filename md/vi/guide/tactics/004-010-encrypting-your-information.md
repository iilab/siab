

---

lang: vi
community: guide
type: tactics
legacy: True
child: True
weight: 1
depth: 3
title: Encrypting your information

---

<div class="background" markdown="1">
Pablo: Nhưng máy tính của tôi đã được bảo vệ bởi mật khẩu đăng nhập của Windows! Điều đó đã đủ chưa?

Clauda: Thực tế, mật khẩu đăng nhập của Windows rất dễ dàng bị phá. Thêm nữa là bất kỳ ai có thể sử dụng máy tính của anh đủ lâu để khởi động hệ thống từ một đĩa CD đều có thể sao chép toàn bộ dữ liệu trên máy của anh mà không cần đến bất kỳ một mật khẩu nào. Trong trường hợp họ có thể mang máy tính đi một khoảng thời gian nhất định, anh còn có thể gặp nhiều rắc rối hơn nữa. Không chỉ mỗi mật khẩu đăng nhập của Windows có thể bị phá, anh cũng không thể tin cậy các mật khẩu của Trình soạn thảo Microsoft Word hay Adobe Acrobat.
</div>

[*Mã hóa*](/vi/glossary#Encryption) thông tin của bạn giống như việc cất chúng trong các két an toàn được khóa lại. Chỉ những ai có chìa khóa hoặc biết tổ hợp khóa (một chìa khóa mật mã hay một mật khẩu, trong trường hợp này) mới có thể mở được. Đặc điểm chung trên đặc biệt phù hợp cho [*TrueCrypt*](/vi/glossary#TrueCrypt) và các công cụ tương tự, tạo ra các không gian chứa được [*mã hóa*](/vi/glossary#Encryption) gọi là các ‘vùng được mã hóa’ hơn là chỉ bảo vệ từng tệp một. Bạn có thể đưa một số lượng lớn các tệp vào trong một vùng được mã hóa, nhưng những công cụ này sẽ không bảo vệ những dữ liệu được lưu trữ ở những nơi khác trên máy tính hay thẻ nhớ USB của bạn.

<div class="getstarted" markdown="1">
**Thực hành: Bắt đầu với [***Hướng dẫn sử dụng TrueCrypt***](/vi/truecrypt-main)**
</div>

Trong khi các phần mềm mã hóa khác có thể cung cấp khả năng [*mã hóa*](/vi/glossary#Encryption) tương đương, [*TrueCrypt*](/vi/glossary#TrueCrypt) được thiết kế đặc biệt cho dạng bảo mật lưu trữ tệp này một cách tương đối đơn giản nhất. Thêm nữa, phần mềm này hỗ trợ các vùng [*mã hóa*](/vi/glossary#Encryption) có thể được di chuyển trên các thiết bị lưu trữ lưu động. Thực tế đây là một công cụ phần mềm [*Mã nguồn Mở*](/vi/glossary#FOSS), với tính năng ‘có thể chối bỏ’ được nêu kỹ tại phần [***Ẩn giấu thông tin mật***](/vi/chuong_4_2) ở bên dưới mang lại cho [*TrueCrypt*](/vi/glossary#TrueCrypt) một ưu thế vượt trội so với rất nhiều các công cụ mã hóa [*bản quyền*](/vi/glossary#Proprietary_software) được cài đặt sẵn, ví dụ như ‘bitlocker’ của Windows XP.

<div class="background" markdown="1">
Pablo: Được rồi, bây giờ em làm anh lo lắng. Thế còn những người dùng khác trên cùng máy tính thì sao? Liệu họ có thể xem các tập tin trong thư mục ‘My Documents’ không?

Claudia: Em thích cách suy nghĩ của anh! Nếu mật khẩu của Windows không bảo vệ anh khỏi những kẻ xâm nhập, làm sao nó có thể bảo vệ anh khỏi những người dùng chung máy tính với anh? Thực tế, thư mục My Documents thường được thấy bởi tất cả mọi người dùng trên máy vì vậy những người khác không cần phải làm gì phức tạp vẫn có thể đọc các tệp không được mã hóa của anh. Anh cũng đúng ngay cả khi một thư mục được thiết đặt là ‘cá nhân’, nó vẫn không an toàn trừ khi sử dụng một dạng mã hóa nào đó.
</div>

### Một số mẹo sử dụng mã hóa tệp một cách an toàn ###

Lưu trữ các thông tin mật có thể nguy hại đối với bạn và cho những người liên quan. Việc [*mã hóa*](/vi/glossary#Encryption) giúp giảm thiểu nguy cơ này nhưng không hoàn toàn loại bỏ được. Bước đầu tiên để bảo vệ những dữ liệu mật này là giảm tối đa việc phải lưu trữ nó ở đâu đấy. Trừ khi bạn có lý do để lưu một tệp đặc biệt hay cất giữ một mảng thông tin quan trọng trong một tệp, bạn nên đơn giản là xóa nó đi (xem [*Chương 6: Làm sao để xóa thông tin nhạy cảm khỏi máy tính*](/vi/chuong-6) để biết thêm cách thực hiện điều đó một cách an toàn). Bược tiếp theo lẳ dụng một công cụ mã hóa tiên tiến, như [*TrueCrypt*](/vi/glossary#TrueCrypt).

<div class="background" markdown="1">
Claudia: Có khi chúng ta không nhất thiết phải lưu trữ các thông tin mà có thể xác định những người đã đưa cho chúng ta những bằng cứ. Anh nghĩ sao?

Pablo: Đồng ý, chúng ta có lẽ chỉ nên ghi lại càng ít càng tốt. Hơn nữa, chúng ta cần tìm cách mã hóa để bảo vệ các tên người và địa điểm mà chúng ta bắt buộc phải ghi lại.
</div>

Quay trở lại với việc sử dụng két an toàn được khóa, có một vài điều bạn luôn ghi nhớ trong đầu khi sử dụng  [*TrueCrypt*](/vi/glossary#TrueCrypt). và các công cụ tương tự. Bất kể két an toàn của bạn chắc chắn thế nào, sẽ chẳng giúp ích gì nếu bạn để cửa két mở toang. Khi vùng mã hóa của  [*TrueCrypt*](/vi/glossary#TrueCrypt). được ‘gắn’ vào hệ thống (bất kể khi nào bạn có thể tự truy cập dữ liệu), dữ liệu của bạn có nguy cơ bị lộ, vì vậy bạn nên giữ nó luôn đóng trừ trường hợp bạn đang đọc hay thay đổi các tệp bên trong nó.

Một số tình huống quan trọng bạn tuyệt đối không nên để ‘vùng [*mã hóa*](/vi/glossary#Encryption) ’ ở trạng thái mở (được gắn vào hệ thống):

- Đóng ngay vùng mã hóa khi bạn rời khỏi máy tính, trong bất kỳ khoảng thời gian nào. Ngay cả khi bạn thường để máy tính của bạn chay qua đêm, bạn cần chắc rằng bạn không để dữ liệu nhạy cảm của mình có thể bị xâm nhập trực tiếp hay từ xa khi bạn không có ở đó.

- Đóng ngay vùng mã hóa trước khi chuyển máy tính sang trạng thái nghỉ. Điều này áp dụng với cả hai trạng thái nghỉ là tạm nghỉ (suspend) hay ngủ đông (hibernation) hay được sử dụng cho máy xách tay nhưng cũng có thể có cả trên máy để bàn.

- Đóng ngay vùng mã hóa trước khi cho phép ai đó sử dụng máy tính của bạn. Khi mang máy xách tay qua các điểm kiểm tra an ninh hay qua biên giới, rất cần thiết phải đóng tất cả các vùng [*mã hóa*](/vi/glossary#Encryption) và tắt hẳn máy tính đi.

- Đóng ngay vùng mã hóa trước khi cắm bất kỳ ổ đĩa USB hay thiết bị lưu trữ ngoại vi không đáng tin cậy, bao gồm cả các thiết bị của bạn bè hay đồng nghiệp.

- Nếu bạn lưu trữ một ‘vùng [*mã hóa*](/vi/glossary#Encryption)’ trên một thẻ nhớ USB, nhớ rằng việc rút thiết bị ra không có nghĩa ngay lập tức đóng ‘vùng mã hóa’ đó. Ngay cả khi bạn cần bảo mật các tệp tin một cách nhanh chóng, bạn cũng cần tuân theo trình tự đóng kết nối (gắn) vùng mã hóa, sau đó ngắt kết nối của thiết bị với máy tính thông qua phần mềm và rút thiết bị ra khỏi máy tính. Bạn có thể cần thực hành các thao tác này để tìm ra cách nhanh nhất thực hiện chúng.

Nếu bạn quyết định lưu vùng mã hóa [*TrueCrypt*](/vi/glossary#TrueCrypt) trên thẻ nhớ USB, bạn cũng có thể lưu chương trình *TrueCrypt*](/vi/glossary#TrueCrypt) trên đó. Điều này cho phép bạn truy cập dữ liệu trên những máy tính khác nhau. Những quy định trên vẫn được áp dụng, tuy nhiên nếu bạn không tin cậy một máy tính lạ không nhiễm [*phần mềm độc hại*](/vi/glossary#Malware), bạn không nên nhập mật khẩu hay truy cập thông tin nhạy cảm của mình.

