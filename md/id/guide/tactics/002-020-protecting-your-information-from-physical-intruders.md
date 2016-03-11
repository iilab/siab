

---

lang: id
community: guide
type: tactics
legacy: True
child: True
weight: 2
depth: 3
title: Protecting your information from physical intruders

---

Penjahat atau penyusup yang berniat mengakses informasi/data rahasia anda merupakan salah satu contoh dari ancaman utama dalam ancaman fisik ([*physical threat*](/id/glossary#Physical_threat)).Merupakan suatu kesalahan jika anda berpikir bahwa ini adalah satu-satunya ancaman terhadap keamanan informasi/data anda, akan lebih fatal lagi jika anda mengabaikannya. Ada beberapa langkah yang bisa anda ambil untuk mengurangi resiko dari penyelundupan ini. Kategori dan saran-saran di bawah berlaku baik untuk rumah maupun kantor dan dapat digunakan sebagai dasar untuk membuat pedoman keamanan disesuaikan dengan kondisi lingkungan dimana anda berada. 

### Lingkungan kantor###

* Kenalilah tetangga anda. Perhatikan situasi keamanan di negara maupun lingkungan anda, ada dua kemungkinan berikut bisa terjadi. Anda bisa mengikutsertakan mereka untuk membantu menjaga kantor anda atau memasukkan mereka ke daftar potensi ancaman yang harus diatasi didalam buku pedoman  keamanan anda.

* Periksa kembali cara anda melindungi semua pintu, jendela, dan jalan masuk lainnya ke kantor anda. 

* Pertimbangkan untuk memasang kamera pengintai  atau alarm dengan sensor gerakan.

* Buatlah ruang penerima tamu, dimana anda bisa menemui tamu anda sebelum mereka masuk ke kantor anda; dan ruang pertemuan yang terpisah dari ruang kerja anda.

### Didalam kantor ###

* Lindungi kabel jaringan dengan memasangnya di dalam kantor.

* Kuncilah perangkat jaringan seperti  [*servers*](/id/glossary#Server), perute ([*routers*](/id/glossary#Router)), sakelar([*switches*](/id/glossary#Router)), [hubs](/id/glossary#Router), dan modem di dalam ruangan atau lemari yang aman. Seorang penyusup dapat saja memiliki akses ke peralatan tersebut lalu menginstal [*malware*](/id/glossary#Malware) yang dapat mencuri data yang sedang masuk/keluar jaringan atau menyerang komputer lain di jaringan anda, bahkan setelah orang itu pergi. 

* Jika anda memiliki jaringan nirkabel, sangat penting bagi anda untuk mengamankan titik akses ([*access point*](/id/glossary#Router)) sehingga penyusup tersebut tidak dapat masuk ke jaringan ataupun memonitor lalu lintas jaringan anda. Jika anda menggunakan jaringan nirkabel yang tidak aman, siapapun yang mempunyai laptop di lingkungan anda berpotensi menjadi penyusup. Definisi fisik disini memang sedikit berbeda, tapi dengan pertimbangan bahwa penjahat yang menyusup memonitor jaringan nirkabel anda memiliki akses yang sama dengan penjahat yang menyelinap ke kantor anda dan melakukan penyambungan ilegal ke kabel Ethernet anda. Langkah-langkah yang diperlukan untuk mengamankan jaringan nirkabel dapat berbeda satu sama lain, tergantung dari titik akses ([*access point*](/glossary#Router)) hardware dan software anda, tetapi biasanya mudah untuk dilakukan

### Diruang kerja ###

* Perhatikan posisi layar komputer anda dengan cermat, baik saat anda sedang bekerja maupun saat anda sedang tidak berada di meja anda, ini untuk mencegah orang lain membaca apa yang tertampang di layar. selain itu anda juga harus mempertimbangkan lokasi jendela, posisi pintu saat terbuka, dan ruang tunggu tamu, jika ada. 

* Sebagian penutup komputer desktop memiliki lubang dimana anda bisa meletakkan gembok, untuk menghindari orang lain membukanya. Jika anda memiliki penutup seperti ini, sebaiknya anda menguncinya supaya tidak ada penyusup yang mengacaukan hardware di dalamnya. Anda juga dapat mempertimbangkan fitur ini saat anda membeli komputer baru.

* Jika memungkinkan, gunakan kabel pengaman ([*security cable*](/id/glossary#Security_cable)) untuk menghindari penyusup mencuri komputer anda. Kabel ini terutama penting untuk laptop dan  desktop kecil yang bisa disembunyikan di dalam tas atau jas. 

### Perangkat lunak (software) dan pengaturannya terkait keamanan fisik ###

* Saat anda menyalakan kembali komputer anda ( me-restart), pastikan komputer meminta anda untuk memasukkan kata sandi sebelum perangkat lunaknya bekerja dan mengakses berkas. Jika tidak, anda bisa menyalakan fitur ini di Windows dengan cara mengklik menu *Start*, pilihlah Control Panel, dan klik dua kali di User Accounts. Di User Accounts pilih lah akun anda dan klik Create a Password. Pilihlah kata sandi yang aman, seperti yang di bahas di [***Bab 3: Cara membuat dan menjaga kata sandi yang aman***](/chapter-3), masukkan kata sandi anda, konfirmasikan, lalu klik Create Password dan klik Yes, Make Private.
* Ada beberapa pengaturan dalam  [*BIOS*](/id/glossary#BIOS) komputer anda yang relevan dengan keamanan fisik. Pertama, anda harus mengkonfigurasi komputer anda sehingga komputer tidak akan mem-*[boot](/id/glossary#Booting)* dari penggerak flopi, CD-ROM ataupun DVD. Ke dua, anda harus menset kata sandi pada [*BIOS*](/id/glossary#BIOS) itu sendiri, sehingga penyusup tidak bisa dengan mudah mengganti pengaturan. Pilihlah kata sandi yang aman.
* Jika anda hanya mengandalkan database kata sandi, seperti yang dibahas di  [***Bab 3***](/chapter_3), untuk menyimpan kata sandi Windows atau SKMD ([*BIOS*](/id/glossary#BIOS)) anda di komputer, pastikan anda tidak menyimpan satu-satunya salinan database di komputer tersebut. 
* Biasakanlah mengunci akun anda setiap kali anda akan meninggalkan komputer. Dalam Windows, anda dapat melakukannya dengan menekan logo Windows dan huruf L pada saat bersamaan. Tetapi ini hanya berlaku jika anda sudah membuat kata sandi untuk akun anda, seperti di jelaskan diatas.
* Enkripsikan ([*Encrypt*](/id/glossary#Encryption)) informasi senstitif yang ada di komputer dan perangkat penyimpanan di kantor anda. Lihat [***Bab 4: Cara mengamankan berkas sensitive di komputer anda***](chapter-4) untuk penjelasan yang lebih mendetil dan referensi ke Panduan Hands-on.# 

<div class=background markdown=1>
Rudo: Saya agak khawatir mengutak-atik BIOS. Apakah komputer saya akan rusak kalau saya melakukan kesalahan?  

Otto: Tentu saja, paling tidak untuk sementara. Pengaturan yang ingin kamu ganti sebenarnya sederhana, tapi karena tampilan layar BIOS bisa terlihat sangat rumit dan sedikit mengintimidasi, maka saat kita melakukan kesalahan komputernya untuk sementara tidak akan bisa dinyalakan. Tapi secara umum, jika tidak biasa mengatur BIOS, sebaiknya kamu minta tolong kepada orang yang lebih mengerti.
</div>

### Piranti Portable ### 

* Pastikan laptop, telepon genggam dan piranti portable lain yang memiliki informasi/data penting selalu anda bawa, terutama saat anda sedang berpergian atau menginap di hotel. Membawa kabel pengaman ([*security cable*](/glossary#Security_cable)) laptop saat anda berpergian akan sangat bermanfaat, walaupun kadang ada kesulitan dalam menemukan benda yang bisa digunakan untuk menyangkutkan kabel tersebut. Waktu makan sering kali dimanfaatkan oleh pencuri untuk menyelinap masuk ke kamar hotel dan mencuri laptop anda.
* Jika anda memiliki laptop atau piranti komputasi genggam seperti Personal Digital Assistant (PDA), sebaiknya anda tidak memamerkannya. Tidak ada gunanya menunjukkan bahwa tas anda berisi perangkat berharga tersebut kepada pencuri atau orang lain yang ingin mengakses data anda. Sebaiknya hindari penggunaan piranti portable di tempat umum dan bawalah laptop anda di dalam tas yang tidak terlihat seperti tas laptop
 


