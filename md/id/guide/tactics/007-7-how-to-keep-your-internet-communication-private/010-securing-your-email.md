

---

lang: id
community: guide
type: tactics
legacy: True
child: True
weight: 1
depth: 3
title: Securing your email

---

Ada beberapa langkah penting yang dapat anda ambil untuk meningkatkan keamanan komunikasi email anda. Pertama, anda harus memastikan bahwa hanya orang yang anda kirimi email lah yang bisa membaca pesan tersebut. Hal ini dibahas di bagian [*Menjaga webmail anda tetap private*](/id/chapter_7_1#Menjaga_webmail_anda_tetap_private) dan [*Beralih ke akun email yang lebih aman*](/id/chapter_7_1#Beralih_ke_akun_email_yang_lebih_aman). Terkadang penting bagi penerima email untuk dapat memverifikasi bahwa pesan yang di terima benar-benar berasal dari anda, bukannya orang lain yang menyamar sebagai anda. Salah satu cara melakukannya dijelaskan dalam [*Keamanan Email Tingkat lanjut*](/id/chapter_7_4) di bagian [*Enkripsi dan otentikasi pesan email individu*](/id/chapter_7_4#Encrypting_and_authenticating_individual_email_messages)

Anda juga harus mengetahui apa yang harus dilakukan jika anda kerahasiaan email anda terbongkar. Bagian [*Tips merespon email yang diduga email surveillance*](/id/chapter_7_2) akan menjawab pertanyaan ini

Ingat juga bahwa email yang aman tidak akan berguna jika apa yang anda ketik terekam oleh spyware dan secara berkala dikirim ke pihak ketiga melalui Internet. [*Bab 1:  Cara melindungi komputer dari malware dan hacker/peretas*](/id/chapter-1) menyediakan beberapa cara untuk mencegah hal tersebut, dan [*Bab 3: Cara membuat dan merawat password yang aman*](/id/chapter-3) untuk melindungi akun email dan pesan instan anda, seperti dijelaskan di bawah ini 

### Membuat webmail anda tetap privat ###

Internet adalah jaringan terbuka dimana informasi dapat terkirim dalam bentuk yang dapat dibaca. Jika sebuah pesan email dibajak sebelum sampai ke sang penerima, isinya dapat dengan mudah dibaca. Dan karena Internet merupakan satu jaringan yang mendunia yang bergantung pada banyak komputer perantara sebagai pengarah lalu lintasnya, maka banyak sekali orang yang berkesempatan untuk membajak pesan anda dengan cara ini. Penyedia Jasa Internet (*Internet Service Provider [*ISP*](/id/glossary#ISP)*) anda adalah penerima pertama dari sebuah pesan email yang anda kirimkan, dalam perjalanannya sampai ke si penerima. Begitu juga dengan email yang dikirmkan untuk anda, [*ISP*](/id/glossary#ISP)  adalah perhentian terakhir sebelum pesan tersebut sampai ke tangan anda. Jika anda tidak melakukan langkah tertentu, pesan anda dapat dibaca atau diganggu pada kedua titik tersebut, atau diantaranya

<div class="background" markdown="1">
Pablo: Aku baru saja berbicara dengan salah satu mitra kita tentang hal ini. Katanya, dia dan koleganya kadang hanya menyimpan pesan-pesan penting di folder 'Draft' webmailnya, yang kata sandinya mereka ketahui bersama. Kedengarannya aneh, tapi apakah efektif? Maksudku, bukankah itu bisa mencegah pihak yang tidak dikehendaki membaca pesannya, karena pesan itu sebenarnya tidak pernah dikirimkan?

Claudia: Setiap saat kita membaca email di komputer, walaupun hanya 'draft', isinya terkirim kepada kita melalui internet. Kalau tidak, mana mungkin muncul di layar, kan? Masalahnya, jika ada orang yang mengintai kita, mereka tidak hanya memonitor email kita saja, tapi juga segala bentuk informasi yang masuk dan keluar dari komputer kita. Dengan kata lain, trik itu tidak akan berhasil kalau yang mebuka email tidak terhubung dengan jaringan Internet aman. Jika terhubung, tidak ada salahnya membuat akun terpisah dan mereka bisa saling berkirim email.
</div>

Sudah lama kita bisa mengamankan koneksi Internet antara komputer kita dengan situs web yang kita kunjungi. Biasanya ini dijumpai saat kita harus memasukkan password atau informasi kartu kredit ke dalam situs web. Teknologi yang digunakan disebut dengan [*enkripsi*](/glossary#Encryption) Secure Socket Layer/ [*SSL*](/id/glossary#SSL). Kita dapat mengetahui saat kita menggunakan [*SSL*](/id/glossary#SSL) atau tidak dengan melihat ke **address bar** dari browser yang kita gunakan.

Semua alamat web biasanya diawali dengan huruf **HTTP**, seperti terlihat pada contoh dibawah:

![](/sites/securitybkp.ngoinabox.org/files/u7/01.png)

Saat anda mengunjungi situs yang aman, alamatnya akan diawali dengan **HTTPS**.
 
![](/sites/securitybkp.ngoinabox.org/files/u7/02.png)

Tambahan huruf **S** di akhir menunjukkan bahwa komputer anda telah membuka koneksi aman (secure) ke situs web tersebut. Ada dapat juga melihat symbol 'kunci/gembok', di **address bar** atau di **status bar**  yang ada di sisi bawah jendela browser anda. Ini merupakan tanda bahwa siapapun yang mungkin ingin memonitor koneksi internet anda tidak akan bisa 'menguping' komunikasi anda dengan situs web tersebut

Selain melindungi kata sandi dan transaksi keuangan anda, [*enkripsi*](/id/discussion#Encryption) jenis ini juga dapat melindungi webmail anda dengan sempurna. Namun, banyak penyedia webmail yang tidak menawarkan akses yang aman, beberapa yang lain mengharuskan anda untuk mengaktifkannya secara ekplisit, dengan cara memilihnya di bagian pengaturan atau dengan mengetikkan **HTTPS** secara manual. Anda harus selalu memastikan bahwa koneksi anda aman sebelum masuk, membaca email atau mengirimkan pesan. 

Perhatikanlah saat browser anda mengeluhkan [*sertifikat keamanan*](/id/glossary#Security_certificate) yang cacat saat anda mencoba mengakses akun webmail yang aman. Ini dapat berarti bahwa seseorang merusak komunikasi antara komputer anda dan server dengan tujuan membajak pesan anda. Lalu, jika anda mengandalkan webmail untuk bertukar informasi rahasia, penting untuk memastikan bahwa anda menggunakan browser yang handal. Pertimbangkan untuk meng-install Mozilla [*Firefox*](/id/glossary#Firefox) dan tambahan-tambahannya yang berkaitan dengan keamanan. 

<div class="getstarted" markdown="1">
Hands-on: Memulai Penggunaan [*Panduan Firefox*](/firefox_main)
</div>			

<div class="background" markdown="1">
Pablo: Salah satu orang yang akan mengerjakan laporan ini sering menggunakan akun Yahoo-nya saat ia di luar kantor. Ada satu lagi yang menggunakan Hotmail. Apa orang lain bisa membacanya kalau aku kirim email ke mereka?

Claudia: Mungkin saja. Yahoo, Hotmail dan banyak penyedia webmail lainnya menggunakan situs web yang tidak melindungi kerahasiaan pesan penggunanya. Kita harus merubah kebiasaan orang-orang agar kita bisa membahas kesaksian ini dengan aman. 
</div>		

### Beralih ke akun email yang lebih aman ###

Hanya sedikit penyedia webmail yang menawarkan akses [*SSL*](/id/glossary#SSL) untuk email anda. Misalnya Yahoo dan Hotmail, keduanya memberikan koneksi yang aman untuk melindungi password saat anda masuk, tetapi pesan-pesan anda tidak dikirim dan diterima dengan aman. Selain itu Yahoo, Hotmail dan beberapa penyedia layanan webmail gratis mengikutkan [*IP address*](/id/glossary#IP_address) komputer yang anda gunakan di semua pesan yang anda kirim

Sebaliknya, akun Gmail dapat digunakan sepenuhnya melalu koneksi yang aman, selama anda masuk ke akun melalui [*https://mail.google.com*](https://mail.google.com)(menggunakan **HTTPS**), dibandingkan dengan  [*http://mail.google.com*](http://mail.google.com). Bahkan, anda sekarang bisa mengatur pilihan agar Gmail selalu menggunakan koneksi yang aman. Tidak seperti Yahoo atau Hotmail , Gmail tidak memberitahukan [*IP address*](/id/glossary#IP_address) anda kepada si penerima email. Namun, anda tidak disarankan untuk mengandalkan Google sepenuhnya untuk menjaga kerahasiaan komunikasi email anda. Google men-scan dan merekam isi pesan-pesan penggunanya untuk berbagai keperluan, dan di masa lalu mereka sudah pernah memberikannya sesuai permintaan pemerintah negara yang membatasi kebebasan digital. Untuk informasi lebih lanjut mengenai kebijakan privasi Google, lihat bagian [***Bacaan lanjutan***](/id/chapter_7_5)

Jika memungkinkan buatlah akun email baru di [*RiseUp*](/id/glossary#RiseUp) dengan mengunjungi [*https://mail.riseup.net*](https://mail.riseup.net). [*RiseUp*](/id/glossary#RiseUp) menawarkan email gratis untuk para aktivis di seluruh dunia dan sebaik mungkin melindungi informasi yang tertampung dalam server mereka. RiseUp sudah dipercaya sejak dahulu sebagai sumberdaya bagi mereka yang membutuhkan solusi email yang aman. Tidak seperti Google, RiseUp memiliki kebijakan yang sangat ketat berkenaan dengan privasi penggunanya dan tidak memiliki ketertarikan komersil yang suatu hari dapat bertentangan dengan kebijakan tersebut. Untuk membuat akun [*RiseUp*](/id/glossary#RiseUp) baru anda membutuhkan dua 'kode undangan'. Kode ini dapat diberikan oleh seseorang yang sudah mempunyai akun RiseUp. Jika anda mempunyai versi cetak dari buklet ini berarti anda sudah menerima 'kode undangan' tersebut bersama dengan buku ini. Jika tidak, anda harus mencari dua pengguna [*RiseUp*](/id/glossary#RiseUp) dan memintanya untuk mengirimkan kode tersebut untuk anda. 

<div class="getstarted" markdown="1">
Hands-on: Memulai Penggunaan[* Panduan RiseUp*](/riseup_main)
</div>	

Gmail maupun [*RiseUp*](/id/glossary#RiseUp) lebih dari sekerdar penyedia webmail. Keduanya dapat digunakan dengan email client seperti Mozilla [*Thunderbird*](/id/glossary#Thunderbird) yang mendukung teknik-teknik yang dibahas dalam [***Keamanan email tingkat lanjut***](/id/chapter_7_4). Memastikan klien email anda membuat koneksi ter[*enkripsi*](/id/glossary#Encryption) ke penyedia email sama pentingnya dengan mengakses email anda melalui **HTTPS**. Jika anda menggunakan email client, lihat [***Panduan Thunderbird***](/thunderbird_main) untuk informasi tambahan. Namun setidaknya anda harus selalu mengaktifkan [*SSL*](/id/glossary#SSL) atau [*enkripsi*](/id/glossary#Encryption) untuk server email baik yang masuk maupun keluar.

<div class="background" markdown="1">
Pablo: Jadi, haruskah aku beralih menggunakan RiseUp, atau tetap bisa menggunakan Gmail dengan alamat 'https'-nya?

Claudia: Terserah padamu. Tetapi ada beberapa hal yang harus kamu pertimbangkan saat memilih penyedia email. Yang pertama, apakah mereka menyediakan koneksi yang aman untuk akun mu? Gmail menyediakannya, jadi OK saja. Kedua, apakah kau mempercayai administrator akan tetap menjaga kerahasiaan email mu dan tidak akan membacanya atau memperlihatkannya kepada orang lain? Itu semua tergantung padamu. Lalu, yang terakhir, kamu juga perlu memikirkan apa kamu boleh diidentifikasikan dengan penyedia email tersebut. Dengan kata lain, apakah kamu akan mendapat masalah karena menggunakan 'riseup.net' yang popular di kalangan aktivis, atau kamu perlu alamat 'gmail.com' yang lebih umum?
</div>

Apapun alat email aman yang akan anda gunakan, ingatlah bahwa setiap email memiliki seorang pengirim dan seorang atau lebih penerima. Anda hanyalah bagian dari gambaran yang ada. Walaupun anda mengakses dengan cara yang aman, pertimbangkan juga cara apa yang kontak anda lakukan untuk menjaga keamanan saat mengirim, membaca dan membalas pesan. Pelajarilah juga dimana lokasi penyedia email kontak anda. Beberapa negara mungkin lebih agresif dibandingkan dengan yang lain, berkenaan dengan surveilans email. Untuk memastikan komunikasi anda bersifat personal, sebaiknya anda dan kontak anda menggunakan layanan email yang aman yang host-nya berada di negara yang aman. Jika anda ingin lebih yakin bahwa pesan anda tidak tertangkap dalam perjalanannya dari server email anda ke server kontak anda, ada baiknya anda dan kontak anda menggunakan akun dari penyedia email yang sama.  [*RiseUp*](/id/glossary#RiseUp) adalah salah satu pilihan yang baik. 
 
### Tip tambahan untuk meningkatkan keamanan email anda  ### 

* Berhati-hatilah saat membuka lampiran email yang tidak anda harapkan, yang datang dari orang yang tidak dikenal atau memiliki judul yang mencurigakan. Saat membuka email seperti ini, anda harus memastikan software anti-virus anda up-to-date dan perhatikanlah peringatan yang muncul di browser atau program email anda. 

* Menggunakan software anonimitas seperti  [*Tor*](/id/glossary#Tor), yang dijelaskan di [***Bab 8: Cara untuk tetap anonim dan menembus sensor di Internet***], dapat membantu anda menyembunyikan layanan email pilihan anda dari siapapun yang mungkin memonitor koneksi Internet anda. Tergantung sejauh mana pemfilteran Internet di negara anda, anda mungkin perlu menggunakan [*Tor*](/id/glossary#Tor) atau alat [*circumvention*](/id/glossary#Circumvention)yang dijelaskan di bab 8 untuk mengakses penyedia email aman seperti [*RiseUp*](/id/glossary#RiseUp) atau Gmail.

* Saat membuat akun yang akan anda gunakan secara anonym dari penerima email anda, atau dari forum publik dimana anda akan mengirim pesan lewat email, anda harus berhati-hati untuk tidak mendaftarkan nama pengguna/username  atau 'Full Name'/Nama Lengkap yang berkaitan dengan kehidupan pribadi maupun professional anda. Dalam hal ini, sebaiknya hindari penggunaan Hotmail, Yahoo atau penyedia webmail lain yang menampilkan[*IP address*](/id/glossary#IP_address) di dalam pesan yang anda kirim.

* Tergantung juga pada siapa yang dapat mengakses komputer anda secara fisik, membersihkan jejak-jejak yang berkaitan dengan email dalam berkas sementara anda, sama pentingnya dengan melindungi pesan anda saat sedang terkirim melalui internet. Lihat [***Bab 6:  Cara menghancurkan informasi rahasia***](/id/chapter-6) dan [***Panduan CCleaner***](/ccleaner_main) untuk keterangan lebih lanjut. 

