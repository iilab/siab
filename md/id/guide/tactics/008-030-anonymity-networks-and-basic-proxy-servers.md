

---

lang: id
community: guide
type: tactics
legacy: True
child: True
weight: 3
depth: 3
title: Anonymity networks and basic proxy servers

---

### Jaringan anonimitas ###

Jaringan anonimitas biasanya 'memantulkan' lalu lintas internet anda dari [*proxies*](/id/glossary#Proxy) aman satu ke yang lain guna menyamarkan lokasi asal anda dan apa yang sedang anda akses. Hal ini dapat menurunkan kecepatan internet anda dalam menampilkan situs web dan layanan lainnya. Namun, jika anda menggunakan  [*Tor*](/id/glossary#Tor), program ini juga menyediakan cara menembus sensor yang handal, aman dan umum, sehingga anda tidak perlu khawatir tentang orang yang mengoperasikan [proxies](/id/glossary#Proxy) anda dan juga situs web yang anda kunjungi. Seperti biasa, anda tetap harus memastikan bahwa koneksi anda terenkripsi melalui [HTTPS](/id/glossary#SSL), sebelum anda bertukar informasi rahasia, seperti password dan email, melalui browser. 

Anda harus menginstal software untuk dapat menggunakan [*Tor*](/id/glossary#Tor), dan kombinasi keduanya akan menghasilkan sebuah alat yang memberikan anonimitas dan juga circumvention ke sensor internet. Setiap kali anda terhubung ke jaringan [*Tor*](/id/glossary#Tor) anda memilih jalur acak melalui tiga [*proxies*](/id/glossary#Proxy) [*Tor*](/id/glossary#Tor) yang aman. Ini menjamin bahwa baik [*ISP*](/id/glossary#ISP) maupun [*proxies*](/id/glossary#Proxy) anda akan mengetahui [*IP address*](/id/glossary#IP_address) komputer serta lokasi layanan internet yang anda minta. Anda dapat mempelajarinya lebih lanjut di Panduan Tor.

<div class="getstarted" markdown="1">
Hands-on: Get started with the [*Tor Guide*](/tor_main)
</div>

Salah satu kelebihan Tor adalah bahwa ia tidak hanya bisa digunakan dengan browser, tetapi juga dengan berbagai software internet. Tor dapat digunakan dengan berbagai program berikut untuk mengakses layanan yang disaring ataupun menyembunyikan penggunaannya: program email, termasuk Mozilla [*Thunderbird*](/id/glossary#Thunderbird), dan program pesan instan seperti [*Pidgin*](/id/glossary#Pidgin).

### circumvention proxies dasar ###

Terdapat tiga pertanyaan penting saat anda memilih circumvention [*proxy*](/id/glossary#Proxy) dasar. Pertama, apakah tersebut berbasis web, atau mengharuskan anda mengubah pengaturan atau menginstal software tertentu di komputer anda? Yang ke dua, apakah proksi tersebut aman? Dan yang ke tiga, apakah privat atau publik?

#### Proksi berbasis-web dan proksi lainnya::####

[*Proxies*](/id/glossary#Proxy) berbasis web adalah proksi yang paling mudah digunakan. Proksi jenis ini hanya mengharuskan anda untuk mengunjungi laman web [*proxy*](/id/glossary#Proxy) dan memasukkan alamat terpilih yang akan anda kunjungi dan klik tombol yang ada. [*Proxy*](/id/glossary#Proxy) tersebut akan menampilkan konten yang anda minta di dalam laman webnya sendiri. Anda dapat mengikuti tautan yang ada seperti biasa, atau memasukkan alamat baru ke [*Proxy*](/id/glossary#Proxy) saat anda ingin mengunjungi laman lainnya. Anda tidak harus menginstal software apapun atau mengubah pengaturan browser. Ini berarti [*proxies*](/id/glossary#Proxy) berbasis web anda:

* Mudah digunakan.
* Dapat dijangkau dari komputer umum seperti di warnet, yang biasanya tidak membolehkan anda untuk menginstal program atau mengubah pengaturannya.
* Bisa lebih aman, terutama jika anda takut ketahuan memiliki circumvention software  di komputer anda. 

Web berbasis [*proxies*](/id/glossary#Proxy)  biasanya memiliki kelemahan tersendiri. Webtidak selalu menampilkan laman dengan benar, dan banyak web berbasis  [*proxies*](/id/glossary#Proxy) yang tidak bisa menampilkan situs web yang rumit, seperti yang memiliki fitur streaming suara dan video. Dan masalah yang sering ditemukan dalam web berbasis [*proxy*](/id/glossary#Proxy) publik  adalah bahwa [*proxy*](/id/glossary#Proxy) akan berjalan lebih lambat saat digunakan banyak orang.  Selain itu, web berbasis [*proxy*](/id/glossary#Proxy) terbatas dalam kerahasiaannya karena [*proxy*](/id/glossary#Proxy) tersebut juga harus mengakses dan memodifikasi informasi yang didapat dari situs yang anda kunjungi sebelum menampilkannya untuk anda. Jika tidak, anda tidak akan bisa mengklik tautan yang ada tanpa meninggalkan proksi. Hal ini dibahas lebih jauh di bagian berikutnya. 
 
[*Proxies*](/id/glossary#Proxy) jenis lain biasanya mengharuskan anda untuk menginstal program atau mengkonfigurasi alamat [*proxy*](/id/glossary#Proxy) eksternal di browser atau operating system anda. Untuk yang pertama, program  circumvention anda biasanya akan menyediakan cara untuk menyalakan dan mematikan alatnya, yang memberitahukan browser anda kapan harus menggunakan [*proxy*](/id/glossary#Proxy). Software seperti ini biasanya memungkinkan anda untuk mengganti [*proxy*](/id/glossary#Proxy) secara otomatis jika ada proksi yang di blokir. Jika anda harus mengkonfigurasi alamat [*proxy*](/id/glossary#Proxy) eksternal di browser atau sistem operasi anda, anda harus mengetahui alamat [*proxy*](/id/glossary#Proxy) yang benar, yang mungkin harus diganti jika [*proxy*](/id/glossary#Proxy)tersebut diblokir atau bekerja dengan lambat. 

Walaupun sedikit lebih susah digunakan daripada web berbasis [*proxy*](/id/glossary#Proxy), metode circumvention ini lebih bisa menampilkan laman yang rumit dengan akurat dan membutuhkan waktu yang lebih lama untuk menjadi lambat walaupun banyak orang yang menggunakannya. Lebih lanjut lagi, [*proxy*](/id/glossary#Proxy) dapat ditemukan di berbagai aplikasi internet. Contohnya [*proxy*](/id/glossary#Proxy) HTTP untuk browser, [*proxy*](/id/glossary#Proxy) SOCKS untuk program email dan chat, dan [*proxy*](/id/glossary#Proxy) VPN yang dapat mengalihkan seluruh lalu lintas internet anda untuk menghindari penyensoran. 

#### proxy yang aman dan tidak aman: ####
 

[*Proxy*](/id/glossary#Proxy)yang aman dalam bab ini mengacu pada [*proxy*](/glossary#Proxy) yang mendukung koneksi ter[*enkripsi*](/id/glossary#Encryption) dari penggunanya. [*Proxy*](/id/glossary#Proxy) tidak aman tetap memungkinkan anda untuk menembus berbagai jenis penyensoran, tetapi tidak akan bekerja jika koneksi internet anda dipindah ke kata kunci atau alamat situs web tertentu. Sebaiknya anda tidak menggunakan [*Proxy*](/id/glossary#Proxy) tidak aman saat mengakses situs web ter[*enkripsi*](/glossary#Encryption) seperti akun webmail dan situs web perbankan. Jika tidak, anda akan mengekspos informasi rahasia yang seharusnya tersembunyi. Dan seperti yang dikatakan sebelumnya, [*Proxy*](/id/glossary#Proxy) tidak aman mudah diketahui dan diblokir oleh mereka yang bertugas mengupdate software penyensoran internet. Untuk apa menggunakan yang tidak aman jika sudah banyak tersedia proksi yang aman, cepat dan gratis?

Anda akan mengetahui apakah sebuah web berbasis [*Proxy*](/id/glossary#Proxy) aman atau tidak dengan mengakses situs [*Proxy*](/id/glossary#Proxy) webnya melalui alamat [*HTTPS*](/id/glossary#HTTPS). Seperti layanan webmail, proksi juga mendukung koneksi aman dan tidak aman, jadi anda harus yakin bahwa anda menggunakan alamat yang aman. Dalam banyak kasus, anda harus meng-'accept' ‘peringatan sertifikat keamanan’ (security certificate warning) dari browser anda. Hal ini berlaku untuk [*proxies*](/id/glossary#Proxy) [*Psiphon*](/id/glossary#Psiphon) dan [*Peacefire*](/id/glossary#Peacefire), seperti yang dibahas di bawah ini. Peringatan seperti ini mengisyaratkan bahwa seseorang, seperti ISP anda atau seorang hackers/peretas, mungkin memonitor koneksi anda ke [*proxies*](/id/glossary#Proxy) tersebut. Walaupun ada peringatan tersebut, sebisa mungkin anda tetap menggunakan  [*proxies*](/id/glossary#Proxy) aman. Namun, saat menggunakan [*proxies*](/id/glossary#Proxy) untuk circumvention, sebaiknya hindari kunjungan ke situs web aman, memasukkan pasword atau bertukar informasi rahasia, kecuali anda bisa memverifikasi cap jari dari [*SSL*](/id/glossary#SSL) [*proxy's*](/id/glossary#Proxy) tersebut. Untuk dapat melakukannya anda harus berkomunikasi dengan administrator [*proxy's*](/id/glossary#Proxy) tersebut. 

*Lampiran C* dari [*Psiphon User's Guide*](https://sesawe.net/Using-psiphon-2.html)/Panduan Pengguna Psiphon menjelaskan langkah-langkah yang harus diambil baik oleh anda sendiri maupun administrator [*proxy*](/id/glossary#Proxy)  untuk dapat memverifikasi cap jadi  [*proxy's*](/id/glossary#Proxy) tersebut.  

Sebaiknya hindari juga mengakses informasi rahasia melalui web berbasis [*proxy*](/id/glossary#Proxy) kecuali anda mempercayai orang yang menjalankannya. Ini berlaku baik saat anda melihat peringatan sertifikat keamanan maupun tidak, sewaktu anda mengunjungi [*proxy*](/id/glossary#Proxy). Ini juga berlaku walaupun anda mengenal operator [*proxy*](/id/glossary#Proxy) dan dapat memverifikasi *cap sidik jari* dari servernya sebelum anda mengabulkan peringatan tersebut. Juka anda mengandalkan server proksi tunggal untuk penembusan, sang administrator akan mengetahui [*IP address*](/id/glossary#IP_address) anda serta situs web yang anda akses. Yang lebih penting, jika [*proxy*](/id/glossary#Proxy) tersebut berbasis web, operator yang nakal akan dapat mengakses semua informasi yang lewat antara browser dan situs web yang anda kunjungi, termasuk konten webmail dan passwordnya. 

Untuk [*proxies*](/id/glossary#Proxy) yang tidak berbasis web, anda mungkin harus meneliti terlebih dahulu untuk mengetahui apakah proksi tersebut mendukung koneksi yang aman. Semua [*proxies*](/glossary#Proxy) dan jaringan anonimitas yang direkomendasikan di bab ini tergolong aman. 

#### Proksi publik dan privat: ####

[*Proxies*](/id/glossary#Proxy) publik menerima koneksi dari siapa saja, sedangkan [*proxies*](/id/glossary#Proxy) privat biasanya memerlukan nama pengguna dan kata sandi. Walaupun [*proxies*](/id/glossary#Proxy) publik memiliki kelebihan dapat diakses siapa saja, biasanya proksi publik cepat dipenuhi pengunjung. Akibatnya, walaupun [*proxies*](/glossary#Proxy) publik sama canggihnya dan sama terawatnya dengan yang privat, biasanya mereka berjalan lambat. [*Proxies*](/id/glossary#Proxy) privat biasanya dijalankan oleh perusahaan atau oleh administrator yang membuat akun untuk pengguna yang mereka kenal secara pribadi. Karena itu biasanya lebih mudah mengetahui motivasi dari operator proksi privat. Anda sebaiknya tidak berasumsi bahwa, karena alasan di atas, [*proxies*](/id/glossary#Proxy) privat lebih terpercaya. Lagipula, sudah banyak layanan online yang mengekspos penggunanya karena motif mencari keuntungan. 

[*Proxies*](/id/glossary#Proxy) publik sederhana biasanya dapat ditemukan dengan mencari istilah ‘proksi publik’ (public proxy), tetapi sebaiknya anda tidak mengandalkan [*proxies*](/id/glossary#Proxy) yang ditemukan dengan cara seperti ini. Karena itu, masih tetap lebih baik menggunakan [*proxies*](/id/glossary#Proxy) privat yang aman yang dijalankan oleh orang yang anda kenal dan percayai, baik secara pribadi ataupun berdasarkan reputasinya, dan oleh mereka yang mempunyai kecakapan teknis untuk mengaja keamannya. Apakah anda harus menggunakan [*proxy*](/id/glossary#Proxy) berbasis web atau tidak itu semua tergantung dari kebutuhan dan preferensi anda sendiri. Kapanpun anda menggunakan [*proxy*](/id/glossary#Proxy) untuk menembus sensor, sebaiknya anda juga menggunakan browser[*Firefox*](/id/glossary#Firefox) yang sudah terinstal ektensi browser [*NoScript*](/id/glossary#NoScript), seperti yang dibahas dalam  [*Panduan Firefox*](/firefox_main). Dengan melakukannya anda akan terlindungi dari  [*proxies*](/id/glossary#Proxy) jahat dan dari situs web yang mungkin ingin mengetahui [*IP address*](/id/glossary#IP_address) anda yang sebenarnya. Perlu diingat bahwa, [*proxy*](/id/glossary#Proxy) ter[*enkripsi*](/id/glossary#Encrypted) tidak akan membuat situs web yang tidak aman menjadi aman. Anda tetap harus memastikan bahwa anda memiliki koneksi [*HTTPS*](/id/glossary#SSL) sebelum mengirim atau menerima informasi rahasia.

Jika anda tidak bisa menemukan orang, organisasi atau perusahaan yang layanan  [*proxy*](/id/glossary#Proxy)nya bisa anda percaya, terjangkau dan mudah diakses dari negara anda, sebaiknya anda mencoba menggunakan jaringan anonimitas Tor, yang telah dibahas sebelumya, dalam [*Jaringan anonimitas*](#Anonymity_networks). 

