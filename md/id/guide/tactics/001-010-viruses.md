

---

lang: id
community: guide
type: tactics
legacy: True
child: True
weight: 1
depth: 3
title: Viruses

---

Ada banyak cara untuk mengklasifikasikan virus, dan setiap metode tersebut menghasilkan nama kategori yang berbeda-beda. Worm, macrovirus, trojan dan backdoor adalah beberapa contoh virus yang banyak dikenal. Banyak dari virus tersebut tersebar di Internet, melalui email, situs web berbahaya, atau berbagai cara lain yang ditujukan untuk menginfeksi komputer yang tidak terlindungi. Virus lain tersebar melalui media yang bisa dipindahkan, seperti stik memori/USB dan eksternal hard drives yang memungkinkan pengguna untuk menulis dan membaca informasi. Virus dapat menghancurkan, merusak, atau menginfeksi informasi dalam komputer anda, termasuk data yang berada dalam drive eksternal. Virus juga dapat mengkontrol komputer anda dan menggunakannya untuk menyerang komputer lain. Untungnya banyak perangkat anti-virus yang dapat anda gunakan untuk melindungi komputer anda serta mereka yang sering bertukar informasi digital dengan anda. 

### Perangkat Lunak (Software) Anti-virus ###

Ada sebuah program [*freeware*](/id/glossary#Freeware) anti-virus hebat untuk Windows disebut [*Avast*](/id/glossary#Avast),program ini mudah digunakan, di-update (perbarui) secara rutin, dan diakui oleh para ahli anti-virus. Program ini mengharuskan anda mendaftar setiap 14 bulan sekali, proses  pendaftaran, up dates dan program ini diberikan secara gratis.

<div class=getstarted markdown=1>
Hands-on: Petunjuk penggunaan [*Avast Guide*](/avast_main)
</div>

[*Clam Win*](/id/glossary#Clam_Win) adalah sebuah alternatif [*FOSS*](/id/glossary#FOSS) untuk *[Avast](/id/glossary#Avast)* dan berbagai program anti-virus ternama yang banyak dijual di pasaran. Walaupun terbatas dalam beberapa fitur utama yang penting dalam program anti-virus, [*Clam Win*](/id/glossary#Clam_Win) memiliki kelebihan, yaitu dapat dijalankan melalui USB untuk memindai komputer yang diprotect dimana anda tidak dapat meg-install software kedalamnya. Program ini sangat berguna saat anda harus menggunakan komputer umum atau warnet untuk pekerjaan yang penting. 

### Tips penggunaan software anti-virus secara efektif ###

* Jangan menjalankan dua program anti-virus pada saat yang bersamaan karena dapat memperlambat kerja komputer anda atau dapat juga menyebabkan crash. Hapuslah program anti-virus yang ada sebelum anda menginstal program anti-virus yang baru
* Pastikan program anti-virus anda memungkinkan untuk menerima update. Banyak dari anti-virus komersil atau yang sudah diinstal dalam komputer baru harus didaftarkan (dan harus membayar) terlebih dahulu untuk item-item tertentu atau antivirus tersebut akan berhenti menerima up date.  Semua software yang direkomendasikan disini dapat di-update secara gratis. 
* Pastikan software anti-virus anda di-update secara teratur. Virus baru dibuat dan disebarkan setiap hari dan komputer anda bisa menjadi rentan jika anti-virus anda tidak terus menerus di-update. [*Avast*](/id/glossary#Avast) akan secara otomatis meng-update saat komputer anda terhubung dengan Internet. 
* Upayakan agar fitur Virus Detection pada Anti Virus anda selalu dalam posisi ‘always on’ (selalu menyala). Setiap software memiliki nama yang berbeda untuk fitur tersebut, tetapi kebanyakan memiliki fitur yang serupa. Ada yang menyebutnya ‘Realtime Protection’ , ‘Resident Protection’, atau sejenisnya. Perhatikan [***Section 3.2.1***](/howtouseavast#Section_3.2.1) pada [***Panduan Avast***](/avast_main) untuk mempelajari lebih lanjut tentang fitur ‘Resident Scanner’ pada perangkat tersebut.
* Scan (pindai) semua berkas yang ada dalam komputer anda secara rutin. Anda tidak harus melakukannya setiap hari (terutama jika Anti Virus anda memiliki fitur ‘always on’ seperti dijelaskan di atas), tetapi anda tetap harus melakukannya secara berkala. Seberapa seringnya tergantung pada keadaan masing-masing. Apakah baru-baru ini anda menghubungkan komputer anda ke jaringan yang tidak dikenal? Dengan siapa saja anda sudah berbagi stik memori/USB? Apakah anda sering menerima lampiran aneh dalam email anda? Apakah komputer yang ada di rumah atau kantor anda mengalami gangguan virus? Untuk informasi lebih lanjut mengenai cara men-scanning file, lihat [***Panduan Avast***](/avast_main). 

### Mencegah infeksi virus ###

* Berhati-hatilah saat membuka attachment (lampiran email). Sebaiknya hindari membuka attachment dari sumber tidak dikenal. Jika anda harus membukanya, pertama anda harus menyimpan lampiran tersebut ke dalam folder di komputer anda, lalu bukalah aplikasi yang sesuai (seperti Microsoft Word atau Adobe Acrobat). Jika anda menggunakan menu ‘File’ dalam program untuk membuka lampiran secara manual dan tidak meng-klik dua kali lampiran tersebut atau membiarkan email anda membukanya secara otomatis, kemungkinan anda untuk terkena virus lebih kecil.
* Pertimbangkan resikonya sebelum memasukkan media seperti CD, DVD, dan stik memori/USB ke komputer anda. Anda harus memastikan anti-virus anda sudah ter-update dan virus scan berjalan. Ada baiknya juga untuk mematikan fitur ‘AutoPlay’ pada komputer anda, fitur ini sering digunakan virus untuk menginfeksi komputer. Dalam Windows XP, ini dapat dilakukan dengan cara masuk ke **My Computer**, klik-kanan pada penggerak CD atau DVD, pilih **Properties** dan klik pada tab **AutoPlay**. Pilih **Take no action** atau **Prompt me each time to choose an action** untuk setiap tipe berkas, lalu klik **OK**.
* Anda juga dapat mencegah infeksi virus dengan beralih ke software open source yang dapat diperoleh secara gratis, biasanya lebih aman dan jarang diincar oleh para pembuat virus..  

<div class=background markdown=1>
Assani: Saya punya pembersih virus dan secara rutin saya membersihkan komputer saya, berarti komputer saya amankan?? 

Salima: Sebenarnya, punya software anti-virus saja tidak cukup. Kamujuga harus melindungi komputermu dari spyware dan hackes/peretas, jadi kamu harus menginstal dan menggunakan perangkat yang lebih lengkap. 
</div>

