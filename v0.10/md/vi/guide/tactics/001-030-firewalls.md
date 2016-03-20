

---

lang: vi
community: guide
type: tactics
legacy: True
child: True
weight: 3
depth: 3
title: Firewalls

---

Tường lửa là chương trình đầu tiên tiếp nhận luồng dữ liệu từ Internet. Nó cũng là chương trình cuối cùng tiếp quản dữ liệu đi ra bên ngoài. Giống như một nhân viên an ninh, đứng ở cửa tòa nhà, xác định cho phép hay không việc đi vào và đi ra. Thông thường, có một điều quan trọng là bạn cần bảo vệ bản thân trước các kết nối không đáng tin cậy từ mạng Internet và mạng nội bộ, chúng đều đem đến nguy cơ Tin tặc hay virút xâm nhập máy tính của bạn. Giám sát các kết nối xuất phát từ máy tính của bạn cũng không kém phần quan trọng, tuy nhiên lý do có phần phức tạp hơn một chút.

Một tường lửa tốt cho phép bạn thiết đặt quyền truy cập cho từng chương trình trên máy của bạn. Khi một chương trình trong số này tìm cách thiết lập kết nối với thế giới bên ngoài, tường lửa sẽ phong tỏa nỗ lực kết nối này của chương trình và đưa ra cảnh báo cho bạn trừ khi nó nhận diện chương trình đã được xác nhận rằng bạn đã cấp phát quyền cho chương trình thực hiện những kết nối loại này. Điều này giúp ngăn chặn các [*phần mềm độc hại*](/vi/glossary#Malware) đang tồn tại tìm cách lan truyền virút hoặc kết nối với Tin tặc xâm nhập máy tính của bạn. Như vậy, tường lửa đóng vai trò vừa là lá chắn bảo vệ thứ hai đồng thời là hệ thống cảnh báo sớm giúp bạn nhận ra khi hệ thống an ninh của máy tính có vấn đề.

### Sử dụng tường lửa ###

Những phiên bản gần đây của Microsoft Windows được tích hợp sẵn một tường lửa, và được tự động bật. Thật không may, chương trình tường lửa của Windows này bị giới hạn nhiều mặt. Ví dụ, nó không kiểm soát các kết nối ra bên ngoài, và đôi lúc khá khó để sử dụng. Tuy nhiên, có một chương trình tường lửa cá nhân [*miễn phí*](/vi/glossary#Freeware) tuyệt vời là [*Comodo Firewall*](/vi/glossary#Comodo_Firewall), thực hiện tốt hơn việc đảm bảo an ninh cho máy tính của bạn.

<div class=getstarted markdown=1>Thực hành: Bắt đầu với Hướng dẫn [Comodo Firewall](/vi/comodo-main)
</div>

### Ngăn chặn những kết nối không đáng tin cậy ###

- Chỉ nên cài đặt những chương trình cần thiết lên máy tính cho các công việc thiết yếu, và đảm bảo rằng chúng được lấy từ những nguồn có danh tiếng tốt. Gỡ bỏ tất cả các phần mềm bạn không sử dụng.

- Ngắt kết nối với mạng Internet khi bạn không sử dụng và hãy tắt máy tính hoàn toàn khi không sử dụng qua đêm.

- Không chia sẻ mật khẩu máy tính của bạn cho người khác.

- Tắt các ‘dịch vụ’ trên máy nếu bạn không sử dụng đến. Để xem thêm trợ giúp, xem [*Hướng dẫn Đọc Thêm*](/vi/chuong_1_5).

- Chắc chắn rằng tất cả máy tính trong mạng văn phòng của bạn đều có cài đặt phần mềm tường lửa.

- Nếu bạn chưa có chương trình tường lửa, hãy cân nhắc việc cài đặt một tường lửa chung để bảo vệ toàn bộ hệ thống mạng cho văn phòng của bạn. Nhiều thiết bị [**gateways**](/vi/glossary#Router) Internet băng rộng có tích hợp sẵn một tường lửa, bật tường lửa này có thể tăng cường đáng kể mức an ninh cho hệ thống mạng của bạn. Nếu bạn không biết bắt đầu từ đâu, có thể tìm kiếm tư vấn từ nhân viên đã từng giúp bạn thiết kế hệ thống mạng.

<div class=background markdown=1>
 Asani: Vậy, giờ con muốn cha cài đặt chương trình diệt virút, chương trình chống phần mềm gián điệp và phần mềm tường lửa? Liệu máy tính của cha có tải nổi tất cả những thứ đó không?

Muhindo: Tất nhiên rồi, Thực tế cả ba công cụ trên là tối thiểu nếu cha muốn đảm bảo an ninh khi truy cập mạng Internet. Chúng được thiết kế để phối hợp với nhau, cho nên việc cài đặt chúng sẽ không gây nên bất cứ vấn đề gì. Tuy nhiên cần nhớ rằng cha không nên chạy hai chương trình diệt virút cũng như hai phần mềm tường lửa cùng lúc.
</div>

