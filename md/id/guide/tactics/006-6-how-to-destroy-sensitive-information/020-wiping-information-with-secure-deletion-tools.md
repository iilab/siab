

---

lang: id
community: guide
type: tactics
legacy: True
child: True
weight: 2
depth: 3
title: Wiping information with secure deletion tools

---

Ketika anda menggunakan alat penghapus yang aman seperti yang direkomendasikan di bab ini, dapat dikatakan bahwa sebenarnya anda mengganti, atau ‘menimpa’ informasi rahasia anda, bukan hanya menghapusnya. Jika anda membayangkan dokumen yang disimpan di lemari file, yang telah kita bahas sebelumnya, ditulis menggunakan pensil, maka software penghapus yang aman bukan hanya akan menghapus isinya, tetapi juga akan menghapus setiap kata yang dituliskan diatasnya. Seperti goresan pensil, informasi digital masih dapat sedikit terbaca walaupun sudah dihapus dan diatasnya sudah dibuat tulisan baru. Karena itu, alat-alat yang direkomendasikan di bab ini akan menimpa berkas dengan data acak beberapa kali. Proses ini disebut dengan [*wiping*](/id/glossary#Wiping) dan semakin banyak informasi ditimpa maka konten aslinya akan semakin sulit untuk dipulihkan. Para ahli berpendapat bahwa sebaiknya penimpaan dilakukan sebanyak tiga kali atau lebih; bahkan beberapa standar menyarankan untuk menimpa sebanyak tujuh kali atau lebih. Software [*wiping*](/id/glossary#Wiping)  secara otomatis melakukan beberapa tahap penimpaan, tetapi anda bisa mengubah jumlah tahap tersebut jika dibutuhkan

### Wiping file-file ### 

Terdapat dua cara umum untuk me-[*wipe*](/id/glossary#Wiping)/membersihkan data rahasia dari hard drive atau storage device anda. Anda dapat me-[*wipe*](/id/glossary#Wiping)/membersihkan satu file saja atau dapat juga me-[*wipe*](/glossary#Wiping) semua ruang yang ’tidak teralokasikan’ di drive anda. Saat membuat keputusan ini, ada baiknya anda mengingat contoh hipotetis yang telah disebutkan sebelumnya, yaitu file laporan panjang yang telah anda tulis dan meninggalkan potongan-potongan salinan yang tersebar di dalam hard drive anda walaupun yang terlihat hanya satu file saja. Jika anda me-[*wipe*](/glossary#Wiping)/menghapus file tersebut, sudah pasti file tersebut akan terhapus, namun anda masih akan meninggalkan salinan lainnya. Kenyataannya, sangat sulit untuk menghapus salinan-salinan tersebut secara langsung karena salinan tersebut tidak dapat dilihat tanpa menggunakan software khusus. Dengan [*wiping*](/glossary#Wiping)/membersihkan semua ruang kosong yang ada di storage device anda, anda sedang memastikan bahwa semua informasi yang sudah dihapus sebelumnya akan dihancurkan. Kembali ke metafora tentang lemari file yang berlabel buruk, prosedur ini sama seperti menelusuri lemari, lalu menghapus dan berulang kali mencoreti dokumen yang sudah diambil labelnya

[*Eraser*](/id/glossary#Eraser) adalah sebuah alat penghapus gratis dan open-source yang sangat mudah digunakan. Anda dapat me-[*wipe*](/glossary#Wiping)/membersihkan file dengan [*Eraser*](/id/glossary#Eraser) melalui tiga cara yang berbeda: dengan memilih satu file saja, dengan memilih konten dari **Recycle Bin** atau dengan me- [*wiping*](/id/glossary#Wiping) semua ruang yang tidak teralokasi di drive anda. [*Eraser*](/id/glossary#Eraser) juga dapat membersihkan konten dari Windows [*swap file*](/id/glossary#Swap_file), yang akan dibahas lebih lanjut. 

<div class="getstarted" markdown="1">
Hands-on: Menggunakan [*Panduan Eraser*](/eraser_main)
</div>
Walaupun alat penghapus aman tidak akan merusak berkas yang terlihat, kecuali anda dengan sengaja me-[*wiping*](/id/glossary#Wiping)nya, anda tetap harus berhati-hati menggunakan software seperti ini. Kemalangan bisa terjadi kapan saja, karena itulah banyak orang yang merasakan manfaat **Recycle Bins** dan alat pemulihan data. Jika anda sudah terbiasa  me-[*wiping*](/id/glossary#Wiping) data setiap kali anda menghapus sesuatu ada kemungkinan anda tidak dapat memulihkan data jika anda membuat kesalahan. Pastikan anda sudah mempunyai backup yang aman sebelum menyeka data dalam jumlah besar.

<div class="background" markdown="1">
Elena: Aku tahu program pengolah kata seperti Microsoft Word dan Open Office biasanya membuat salinan sementara dari berkas yang kita tulis. Apakah program lain juga melakukan hal yang sama? Apa aku hanya cukup memperhatikan berkas yang aku buat dan kuhapus sendiri?

Nikolai: Sebenarnya ada banyak ruang di komputer kita, dimana program-program meninggalkan jejak informasi pribadi dan tentang aktivitas online kita. Yang aku maksud adalah situs web yang kita kunjungi, draf email dan lain-lain. Informasi tersebut bisa saja rahasia, tergantung seberapa sering komputer tersebut digunakan
</div>

### Wiping Data Sementara ### 

Fitur yang memungkinkan [*Eraser*](/id/glossary#Eraser) untuk me-[*wipe*](/id/glossary#Wiping) semua ruang yang tidak teralokasi di drive resikonya tidak seberat yang anda bayangkan, karena fitur tersebut hanya me-[*wipes*](/glossary#Wiping) konten yang sudah dihapus sebelumnya. Biasanya, file biasayang terlihat tidak akan terkena dampaknya. Namun hal ini justru menimbulkan masalah lain: [*Eraser*](/id/glossary#Eraser) tidak dapat membersihkan informasi rahasia tersembunyi yang belum dihapus. File yang berisi data seperti itu dapat saja terletak di folder terpencil, atau tersimpan dengan nama yang tidak ada artinya. Ini tidak menjadi masalah untuk dokumen elektronik, tetapi penting untuk informasi yang terkumpul secara otomatis setiap kali anda menggunakan komputer. Contohnya adalah:  

* Data sementara yang terekam dalam browser saat menampilkan laman web, termasuk teks, gambar, [*cookies*](/id/glossary#Cookie), informasi akun, data personal yang digunakan dalam formulir online dan riwayat situs web yang telah anda kunjungi. 

* File sementara yang disimpan oleh berbagai aplikasi untuk membantu pemulihan saat terjadi tabrakan data sebelum anda sempat menyimpan pekerjaan anda. File ini mungkin berisi teks, gambar, data lembar kerja dan nama-nama berkas lain termasuk informasi lain yang mungkin adalah rahasia. 

* File-file dan tautan yang disimpan oleh Windows yang sifatnya memudahkan, seperti shortcut/jalan pintas ke aplikasi yang baru saja anda gunakan, tautan ke folder yang sebenarnya anda rahasiakan, dan juga isi <b>Recycle Bin</b> anda jika anda lupa mengosongkannya. 

* Windows  [*swap file*](/id/glossary#Swap_file). Saat memori komputer anda penuh, contohnya saat anda sedang menjalankan beberapa program pada saat yang bersamaan di komputer tua anda, Windows biasanya akan menyalin data yang anda gunakan ke sebuah file ukuran besar yang disebut [*swap file*](/id/glossary#Swap_file). Akibatnya, file ini mungkin menampung apa saja, termasuk laman web, konten dokumen, kata sandi ataupun kunci enkripsi. [*Swap file*](/id/glossary#Swap_file) tidak terhapus bahkan setelah anda mematikan komputer anda. Maka anda harus menghapusnya secara manual.

Untuk menghilangkan file sementara dari komputer, anda dapat menggunakan sebuah alat bernama [*CCleaner*](/id/glossary#CCleaner), yang dirancang untuk membersihkan software seperti Internet Explorer, Mozilla [*Firefox*](/id/glossary#Firefox) dan aplikasi Microsoft Office (semua software yang sering membongkar informasi yang mungkin rahasia), serta membersihkan Windows itu sendiri. [*CCleaner*](/id/glossary#CCleaner) memiliki kemampuan untuk menghapus berkas dengan aman, sehingga anda tidak perlu me-[*wipe*](/glossary#Wiping) ruangan di drive yang tidak teralokasi menggunakan [*Eraser*](/id/glossary#Eraser) setiap anda selesai menggunakannya

<div class="getstarted" markdown="1">
Hands-on: Get started with the [*CCleaner Guide*](/ccleaner_main)
</div>

