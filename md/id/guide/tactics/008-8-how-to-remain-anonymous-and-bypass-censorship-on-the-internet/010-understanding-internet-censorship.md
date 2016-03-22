

---

lang: id
community: guide
type: tactics
legacy: True
child: True
weight: 1
depth: 3
title: Understanding Internet censorship

---

Penelitian yang dilakukan oleh [OpenNet Initiative (ONI)](http://opennet.net/) dan [Reporters Without Borders (RSF)](http://www.rsf.org/) menunjukkan bahwa banyak negara yang menyaring berbagai jenis konten sosial, politik dan 'keamanan nasional', tetapi jarang mempublikasikan daftar yang pasti tentang apa saja yang sudah diblokir. Biasanya, negara yang mengontrol akses penduduknya ke Internet juga berusaha untuk memblokir proksi dan situs web yang menyediakan alat dan instruksi untuk menembus pengawasan tersebut.

Walaupun ada jaminan akses bebas untuk mendapatkan informasi, seperti yang tertulis di Ayat 19 Deklarasi Universal Hak Asasi Manusia, jumlah negara yang memberlakukan sensor Internet terus bertambah dalam beberapa tahun terakhir. Namun, seiring bertambahnya pemfilteran internet, semakin banyak pula alat-alat penembus yang berhasil dikembangkan dan digunakan oleh banyak aktivis, programmer, dan sukarelawan.

Sebelum menelusuri berbagai cara untuk menembus sensor internet, hal pertama yang harus anda lakukan adalah mengerti cara kerja penyaring tersebut. Untuk melakukannya, mari kita tinjau sebuah model sederhana dari koneksi internet anda.

### Koneksi Internet anda  ###

![](/sites/securitybkp.ngoinabox.org/security/files/img/1-en.png)

Langkah pertama koneksi anda ke Internet biasanya dibuat melalui sebuah <i>Internet Service Provider ([*ISP*](/id/glossary#ISP))/Penyedia Jasa Internet di rumah, kantor, sekolah, perpustakaan atau warnet. [*ISP*](/id/glossary#ISP) memberikan [*IP address*](/id/glossary#IP_address), yang digunakan oleh berbagai layanan internet untuk mengidentifikasi anda dan mengirimkan informasi kepada anda, seperti email dan situs web yang anda kunjungi. Siapapun yang tahu [*IP address*](/id/glossary#IP_address) anda dapat mengetahui di kota apa anda tinggal. Organisasi tertentu di negara anda dapat menggunakan informasi ini untuk mengetahui lokasi anda secara akurat.

* **ISP anda** akan mengetahui gedung tempat anda berada atau saluran telepon yang anda gunakan, jika anda mengakses internet dengan modem.
* **Warnet, perpustakaan atau perusahaan anda** akan mengetahui komputer mana yang anda gunakan saat itu, serta port atau titik akses nirkabel mana yang anda gunakan	
* **Badan pemerintah** mungkin mengetahui semua rincian ini karena pengaruh mereka terhadap organisasi di atas.	

Pada tahap ini, [*ISP*](/id/glossary#ISP) anda mengandalkan infrastruktur jaringan di negara anda untuk menghubungkan penggunanya, termasuk anda, dengan dunia luar. Di titik lain koneksi anda, situs web atau layanan Internet yang anda akses juga telah melalui proses yang sama, karena mereka memiliki alamat IP yang diberikan oleh [*ISP*](/id/glossary#ISP) di negaranya masing-masing. Walaupun tanpa detil teknis, model dasar seperti ini sangat membantu dalam mempertimbangkan berbagai alat yang memungkinkan anda untuk menghindari penyaring dan untuk tetap anonim di internet. 

### Bagaimana situs web diblokir  ###

Pada dasarnya saat anda sedang melihat sebuah laman web, anda menunjukkan [*IP address*](/id/glossary#IP_address) dari situs tersebut kepada [*ISP*](/id/glossary#ISP) anda dan memintanya untuk menguhubungkan anda ke [*ISP*](/id/glossary#ISP) milik webserver. Dan jika anda menggunakan koneksi internet tanpa penyensor, itulah yang akan dilakukan oleh ISP anda. Jika anda berada di negara yang menyensor internet, maka langkah pertama yang akan dilakukan ISP anda adalah melihat [*blacklist*](/id/glossary#Blacklist)/daftar hitam  yang berisi situs web terlarang dan memutuskan apakah ia akan menuruti permintaan anda. 

Dalam beberapa kasus, ada sebuah organisasi pusat yang menangani penyensoran [*ISPs*](/glossary#ISP). Sering kali, [*blacklist*](/id/glossary#Blacklist)/daftar hitam berisi [*domain names*](/id/glossary#Domain_names), seperti www.blogger.com, bukan [*IP addresses*](/id/glossary#IP_address). Dan di beberapa negara software penyensor tidak memblokir alamat internet tertentu, tetapi hanya memonitor koneksi anda. Software seperti ini memindai permintaan anda dan laman web yang kembali ke anda sambil mencari kata-kata kunci tertentu, lalu memutuskan apakah anda boleh melihat hasilnya atau tidak.

Dan, Yang lebih memperburuk suasana, saat sebuah laman web diblokir anda mungkin tidak mengetahuinya. Beberapa penyensor menyediakan sebuah 'halaman blokir' yang menjelaskan mengapa laman tertentu disensor, penyensor lain hanya menampilkan pesan eror yang menyesatkan. Pesan ini mungkin hanya mengatakan bahwa laman yang dicari tidak ditemukan atau alamat yang dituju salah. 

Umumnya, lebih mudah untuk memikirkan yang terburuk tentang sensor internet, daripada meneliti kekuatan atau kelemahan teknologi penyensoran yang digunakan di negara anda. Dengan kata lain anda dapat menggunakan asumsi:

* Lalu lintas internet anda dimonitor untuk kata kunci tertentu
* Penyaringan diterapkan secara langsung pada tingkat [*ISP*](/id/glossary#ISP)
* Situs yang di blokir/[*blacklisted*](/id/glossary#Blacklist) di masukkan ke daftar hitam baik  [*IP addresses*](/id/glossary#IP_address) maupun [*domain names *](/id/glossary#Domain_name).
* Anda mungkin mendapatkan alasan yang tidak jelas atau menyesatkan tentang mengapa situs yang diblokir tidak bisa dibuka.

Meskipun alat-alat penembus yang paling efektif dapat digunakan melawan metode penyensoran yang ada, tidak ada salahnya asumsi diatas kita terapkan. 
	
<div class="background" markdown="1">
Mansour:Jadi, jika suatu saat aku tidak bisa mengakses blog, tetapi ada teman di negara lain yang masih bisa mengunjunginya, apa itu berarti pemerintah sudah memblokir blog kita?
 
Magda:Belum tentu. Bisa saja masalah itu hanya dialami oleh orang-orang yang mengakses blog dari sini. Bisa juga karena ada masalah di komputermu yang hanya tampil di situs tertentu. Tapi kamu sudah benar. Kamu bisa coba mengunjunginya dengan menggunakan alat penembus. Lagipula, sebagian besar alat ini mengandalkan server proksi eksternal, jadi seperti minta tolong teman kita di negara lain untuk mengetes situs web untuk kita, bedanya, kita melakukan ini sendiri. 
</div>


