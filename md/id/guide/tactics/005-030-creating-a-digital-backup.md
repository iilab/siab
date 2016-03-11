

---

lang: id
community: guide
type: tactics
legacy: True
child: True
weight: 3
depth: 3
title: Creating a digital backup

---

Dari semua tipe data yang telah kita bahas, 'dokumen elektronik' adalah jenis yang paling menjadi perhatian saat kita membuat kebijakan backup. Istilah tersebut memang agak ambigu, tetapi biasanya mengacu pada berkas-berkas yang anda pantau sendiri dan anda buka secara manual, baik dengan men-dobel-klik atau dengan menggunakan menu File pada aplikasi tertentu. Secara spesifik, yang termasuk tipe data ini adalah text files word processing documents, presentations (presentasi), PDFs and spreadsheets(lembar kerja). Lain halnya dengan email, dokumen elektronik biasanya tidak tersinkronisasi dengan salinan jarak jauh melalui Internet
 
Saat mem-backup dokumen elektronik anda, ingatlah juga untuk mem-backup database program anda. Jika anda menggunakan aplikasi kalender atau buku alamat elektronik, anda juga perlu mencari folder dimana program tersebut menyimpan datanya. Mudah-mudahan database tersebut tersimpan di tempat yang sama dengan dokumen elektronik anda, karena biasanya akan tersimpan di folder **My Documents** di komputer Windows. Jika tidak, anda perlu menambahkan folder yang sesuai untuk backup rutin anda

Email yang disimpan oleh aplikasi seperti [*Thunderbird*](/id/glossary#Thunderbird) adalah salah satu contoh dari database program. Jika anda menggunakan program email, ada saat anda tidak bisa atau malas menyimpan salinan pesan-pesan anda di server, maka anda harus memastikan database email ini masuk dalam backup rutin anda. Anda juga bisa menganggap file gambar atau video sebagai dokumen elektronik atau item dalam database program, tergantung cara anda berinteraksi dengannya. Aplikasi seperti Windows Media Player dan iTunes bekerja seperti database. Jika anda menggunakan program seperti ini anda mungkin harus mencari di hard drive anda untuk mengetahui dimana program tersebut menyimpan berkas yang mereka kelola.  

### Storage devices ###

Sebelum anda mem-backup dokumen elektronik anda, anda harus menetapkan jenis storage device (tempat penyimpanan) apa yang akan anda gunakan

**Compact Discs (CDs)** CD dapat menyimpan data sampai 700 Megabita (MB). Anda akan memerlukan [*CD burner*](/id/glossary#CD_burner) dan CD kosong untuk membuat CD Backup. Jika anda ingin menghapus CD dan memperbarui file yang ada di dalamnya, anda memerlukan CD-RW burner dan rewritable CD. Semua Operating System besar, termasuk Windows XP, sekarang sudah memuat built in software yang dapat menulis CD dan CD-RW. Ingatlah bahwa informasi yang tertulis didalamnya dapat rusak setelah lima atau sepuluh tahun. Jika anda perlu menyimpan backup untuk jangka waktu yang lebih lama anda harus sesekali membuat ulang CD tersebut, membeli CD 'tahan lama', atau gunakan metode backup lain

**Digital Video Discs (DVDs)** – DVD dapat menyimpan data sampai dengan ukuran 4.7 Gigabita (GB). Cara kerjanya sama seperti CD tetapi membutuhkan alat yang lebih mahal untuk membuatnya. Anda memerlukan DVD atau [*DVD-RW burner*](/id/glossary#CD_burner) dan disc yang sesuai. Sama seperti CD, data yang dituliskan di dalam DVD normal akhirnya akan rusak

**USB** – USB dapat menyimpan informasi sebanyak kemampuan stik tersebut. USB tergolong tidak terlalu mahal, bahkan untuk stik yang kapasitasnya sama atau lebih banyak dari CD atau DVD. Stik ini juga mudah digunakan, data dapat dihapus dan ditulis ulang berulang kali. Seperti CD dan DVD, stik memori USB punya usia yang terbatas, yaitu sekitar 10 tahun

**Remote Server** – Server backup jaringan yang dikelola dengan baik kapasitasnya hampir tidak terbatas, namun kecepatan dan stabilitas sambungan Internet anda lah yang akan menentukan apakah ini merupakan pilihan yang realistis. Namun perlu diingat bahwa dengan menggunakan backup server di kantor anda berarti anda menyalahi aturan tentang meletakkan salinan data penting anda di lokasi yang terpisah; walaupun cara ini lebih cepat dari menyalin informasi melalui Internet. Terdapat berbagai layanan penyimpanan gratis di Internet, tetapi anda tetap harus mengenkripsi backup anda sebelum meng-unggahnya ke server yang dikelola oleh organisasi atau orang yang tidak anda kenal dan percaya. Lihat bagian [***Bacaan Lanjutan***](/id/chapter_5_5) untuk beberapa contohnya.

### Backup Software ###

Cobian Backup adalah sebuah alat ramah guna yang dapat diatur untuk bekerja secara otomatis dan rutin di waktu-waktu yang sudah dijadwalkan, dan juga untuk mengikut sertakan file-file yang telah anda ubah sejak backup terakhir. Alat ini juga dapat mengkompres backup dan membuat ukurannya menjadi lebih kecil

<div class="getstarted" markdown="1">
Hands-on: Get started with the [*Cobian Backup Guide*](/cobian_main)
</div>

Seperti biasa, ada baiknya anda mengenkripsi berkas backup anda menggunakan alat seperti TrueCrypt. Informasi lebih lanjut tentang enkripsi data dapat ditemukan di [***Bab 4:Cara melindungi berkas rahasia di komputer anda***](/id/chapter-4).
<div class="getstarted" markdown="1">

Hands-on: Memulai penggunaan [*Panduan TrueCrypt*](/truecrypt_main)
</div>
<p>

Saat menggunakan alat-alat backup ini, ada beberapa hal yang dapat anda lakukan untuk memperlancar kinerja sistem backup anda: 

* Aturlah file-file dalam komputer anda. Pindahkan semua folder yang berisi dokumen elektronik yang ingin anda backup ke dalam satu tempat, seperti ke dalam folder **My Documents**
* Jika anda menggunakan software yang menyimpan datanya dalam database aplikasi, anda harus terlebih dahulu menentukan lokasi database tersebut. Jika tempatnya tidak mudah dijangkau, coba lihat apakah anda dapat memilih lokasi baru untuk database program tersebut. Jika bisa, anda dapat meletakkannya di folder yang sama dengan dokumen elektronik anda.
* Buatlah jadwal rutin untuk melakukan backup
* Buatlah prosedur bagi seluruh staf di kantor anda yang belum memiliki kebijakan backup yang aman dan bisa diandalkan. Bantulah rekan kerja anda untuk lebih mengerti pentingnya hal ini
* Ujilah proses recovering data dari backup anda. Ingatlah bahwa pada akhirnya yang harus anda perhatikan adalah prosedur re-store, bukan prosedur backup-nya

<div class="background" markdown="1">
Elena: Baiklah, aku sudah membuat backup terenkripsi di kantor, dan aku menyimpannya di CD. Cobian dijadwalkan untuk memperbarui backupku dalam beberapa hari ini. Meja kerjaku di kantor mempunyai laci yang bisa dikunci dan aku berencana menaruh CD backup ini disana supaya tidak hilang atau rusak

<i>Nikolai:Lalu bagaimana jika kantor kebakaran? Komputer, meja, CD backup dan semua ikut terbakar! Atau, bagaimana jika forum di situs web digunakan untuk merencanakan demonstrasi lingkungan hidup, lalu pihak yang berwenang bertindak, lalu keadaan menjadi kacau dan kantor bibi digrebek? Aku tidak yakin kunci di laci bibi bisa mencegah polisi dari merampas CD-CD itu. Bagaimana kalau bibi menyimpannya di rumah, atau meminta tolong teman bibi untuk menyimpannya?
</div>


