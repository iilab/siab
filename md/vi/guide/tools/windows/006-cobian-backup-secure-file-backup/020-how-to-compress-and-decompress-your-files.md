

---

lang: vi
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Compress and Decompress Your Files

---

Các mục trong trang này:

- [**3.0 Hướng dẫn Nén các Tệp Sao lưu**](#3.0)
- [**3.1 Hướng dẫn Giải nén Tệp Sao lưu**](#3.1)

-------

<a name="3.0"></a>
## 3.0 Hướng dẫn Nén các Tệp Sao lưu ##

**Bước 1**. **Tạo một tác vụ sao lưu** như hướng dẫn tại phần [**2.2 Hướng dẫn tạo một Tệp Sao lưu**](/vi/cobianbackup_huongdancaidat#2.2) gồm những tệp bạn muốn sao lưu.

**Bước 2**. **Chọn** ![](/sbox/screen/cobian-vi/22.png) từ cửa sổ trình đơn bên trái để mở cửa sổ *New task* như sau:

![](/sbox/screen/cobian-vi/23.png)

*Hình 1: Cửa sổ Tác vụ Mới hiển thị khung Compression and Strong Encryption*

Khung **Compression** xác định phương pháp nén cho tệp sao lưu của bạn.

**Lưu ý**: Việc nén tệp được sử dụng để làm giảm dung lượng những tệp lớn. Giả sử bạn có một khối lượng lớn các tệp cũ mà bạn chỉ thỉnh thoảng mới sử dụng, nhưng bạn vẫn muốn giữ chúng. Sẽ tốt hơn nếu có thể lưu chúng ở một định dạng nào đó càng chiếm ít không gian càng tốt. Việc nén giúp loại bỏ những phần mã không cần thiết khỏi dữ liệu của bạn, trong khi không làm ảnh hưởng tới nội dung tài liệu. Quá trình nén không làm tổn hại đến dữ liệu của bạn. Tệp nén sẽ không thể đọc trực tiếp được, cần thực hiện quá trình giải nếu bạn muốn xem những tệp đó.

Có ba lựa chọn trong danh sách *các phương pháp Nén* (*Compression type*) như sau:



*No Compression*: Như bạn thấy, lựa chọn này không thực hiện việc nén.

*Zip Compression*: Đây là kỹ thuật nén chuẩn cho hệ thống **Windows**. Các tệp nén dạng này có thể được mở bằng các công cụ chuẩn của Windows (hoặc bạn có thể tải về chương trình [*ZipGenius*](http://www.zipgenius.it/) để mở chúng). Đây là lựa chọn thuận tiện nhất.

*SQX Compression*: *SQX* compression is slower than *Zip* compression. It does however give a better data recovery rate, should the archive become corrupted.


*SQX Compression*: *nén SQX*  thường chậm hơn so với nén theo chuẩn nén *Zip*. 
Tuy nhiên nó cho phép khôi phục dữ liệu tốt hơn trong trường hợp quá trình nén bị lỗi.




Việc chọn một phương pháp nén kể trên sẽ tự động kích hoạt mục *Split options*, cũng như danh sách các tùy chọn trong mục này.

*Split Options*  là một lựa chọn thường dùng cho các thiết bị lưu trữ ngoài như đĩa CD, DVD, đĩa mềm hay thẻ nhớ USB. Tùy chọn này cho phép chia các tệp nén thành các phần có dung lượng phù hợp với thiết bị lưu trữ bạn chọn lựa.

Ví dụ: 
Giả sử bạn sao lưu một lượng lớn dữ liệu và bạn muốn lưu chúng trên đĩa CD. Tuy nhiên, sau khi kiểm tra kích thước nén, bạn thấy nó lớn hơn 700MB (dung lượng của một đĩa CD). Chức năng cắt tệp nén cho phép chia tệp đó thành nhiều phần nhỏ hơn hoặc bằng 700MB giúp bạn có thể lưu chúng lên các đĩa CD. Nếu bạn dự định lưu trữ trên ổ đĩa cứng của máy tính hoặc nếu tệp bạn muốn sao lưu nhỏ hơn dung lượng của thiết bị lưu trữ thì bạn có thể bỏ qua phần này.

Những lựa chọn dưới đây xuất hiện khi bạn nhấn chuột vào danh sách *Split Options*. Lựa chọn của bạn sẽ tùy theo loại thiết bị lưu trữ ngoài bạn sử dụng.


![](/sbox/screen/cobian-vi/24.png)

*Hình 2: Danh sách Split Options*

- 3,5" - Floppy disk. This option is big enough to perform backup of a small number of documents
- Zip - Zip Disk (check the capacity of the one you are using). You will need a special Zip Drive in your computer and the custom-made disks
- CD-R - CD disk (check the capacity of the one you are using). You will need a CD Writer in your computer and a CD writing program (see [**DeepBurner Free** version](http://www.deepburner.com/) or [other **disk burning tools**](http://www.thefreecountry.com/utilities/dvdcdburning.shtml)).
- DVD - DVD disk (check the capacity of the one you are using). You will need a DVD Writer in your computer and a DVD writing program (see [**DeepBurner Free** version](http://www.deepburner.com/) or [other **disk burning tools**](http://www.thefreecountry.com/utilities/dvdcdburning.shtml)). 

- 3,5” – Đĩa mềm. Tùy chọn này đủ để sao lưu một lượng nhỏ tài liệu
- Zip - Ổ đĩa nén – (hãy kiểm tra dung lượng thiết bị bạn đang sử dụng). Bạn sẽ cần một ổ đĩa Nén cài đặt trên máy cũng như những đĩa nén đặc chủng.
- CD-R – Đĩa CD (hãy kiểm tra dung lượng đĩa CD của  bạn). Bạn sẽ cần một ổ đĩa ghi CD cài đặt trên máy cũng như chương trình điều khiển quá trình ghi (xem [**DeepBurner Free**](http://www.deepburner.com/) hoặc [các **công cụ ghi đĩa khác**](http://www.thefreecountry.com/utilities/dvdcdburning.shtml)).).
- DVD - Đĩa DVD (hãy kiểm tra dụng lượng đĩa DVD của bạn). Bạn sẽ cần có một ổ ghi đĩa DVD và một chương trình điều khiển ghi đĩa (xem [**DeepBurner Free** version](http://www.deepburner.com/) hay [các **công cụ ghi đĩa** khác](http://www.thefreecountry.com/utilities/dvdcdburning.shtml)).

Nếu bạn dự định sử dụng thẻ nhớ để lưu bản sao lưu, có thể bạn nên dùng lựa chọn *custom size*.

Để tự chọn dung lượng, hãy theo các bước sau:

**Bước 1**. **Chọn** mục *Custom size* (bytes), sau đó **nhập** kích thước của tệp sao lưu theo đơn vị bytes vào trường văn bản như sau:

![](/sbox/screen/cobian-vi/25.png)

*Hình 10: Trường Custom size*

To give you an idea of sizes

Để giúp bạn hình dung về dung lượng:

- 1KB(kilobyte)=1024 bytes – một trang tài liệu của Open Office có kích cỡ khoảng 20KB
- 1MB(megabyte)=1024 KB – một ảnh chụp bằng máy ảnh kỹ thuật số thường có kích cỡ từ 1-3MB
- 1GB(gigabyte)=1024 MB – xấp xỉ một tiếng phìm DVD chất lượng cao

**Lưu ý**: Khi bạn tự chọn kích cỡ để cắt tệp trước khi lưu vào đĩa CD hoặc DVD, **Cobian Backup** sẽ không lưu tệp lưu trữ vào thiết bị lưu trữ ngoài của bạn một các tự động mà sẽ lưu trên máy tính và bạn cần tự thực hiện việc ghi chúng vào đĩa CD hoặc DVD.


*Password Protection*: Lựa chọn này cho phép bạn nhập mật khẩu để bảo vệ tệp nén. Chỉ cần nhập mật khẩu, nhập lại một lần nữa để xác nhận mật khẩu vào trường tương ứng. Khi bạn giải nén tệp, chương trình sẽ yêu cầu bạn nhập mật khẩu trước khi bắt đầu thực hiện lệnh.

**Lưu ý**: Nếu bạn muốn bảo mật tệp nén của mình, bạn nên nghĩ tới một phương pháp khác hơn là chỉ dùng mật khẩu. **Cobian Backup** cho phép bạn mã hóa tệp nén. Vấn đề này được đề cập tại phần [**4. Mã hóa tệp sao lưu**](/vi/cobianbackup_mahoatepsaoluu). Một cách khác nữa xem [**Hướng dẫn thực hành TrueCrypt**](/vi/truecrypt-main) để tìm hiểu về việc tạo các vùng mã hóa trên máy tính hoặc các thiết bị lưu trữ ngoài.

*Nhận xét*: Tùy chọn này cho phép bạn đưa vào những nhận xét miêu tả về tệp nén, tùy chọn này không bắt buộc.


<a name="3.1"></a>
## 3.1 Hướng dẫn Giải nén Tệp Sao lưu ##

Để giải nén tệp sao lưu, hãy thực hiện các bước sau

**Bước 1**. **Chọn > Tools > Decompressor** như dưới đây;

![](/sbox/screen/cobian-vi/26.png)

*Hình 3: Trình đơn Tools với lựa chọn Decompressor*

Cửa sổ Decompressor xuất hiện như sau:

![](/sbox/screen/cobian-vi/27.png)

*Hình 4: Cobian 10 Backup – cửa sổ Decompressor*

**Bước 2**. **Nhấn vào** ![](/sbox/screen/cobian-vi/28.png)

Một cửa sổ mở ra cho phép bạn chọn tệp nén bạn muốn giải nén.

**Bước 3**. **Chọn** tệp nén (*.zip* or *.sqx* file)

**Bước 4**. **Nhấn vào** ![](/sbox/screen/cobian-vi/13.png).

**Bước 5**. **Chọn** một thư mục chứa kết quả của quá trình giải nén.

**Bước 6**. **Nhấn vào** ![](/sbox/screen/cobian-vi/29.png) để mở cửa cửa sổ cho phép bạn chọn thư mục để lưu kết quả giải nén.

**Bước 7**. **Chọn** một thư mục, sau đó **nhấn vào** ![](/sbox/screen/cobian-vi/13.png).

Mở **Windows Explorer** để xem các tệp trong thư mục này.

