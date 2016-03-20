

---

lang: id
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Perform Different Scans Using Recuva

---

Bagian-bagian dari halaman ini:  

- [**3.0 Sebelum Anda memulai**](#3.0)
- [**3.1 Cara melakukan pencarian menggunakan Recuva Wizard**](#3.1)
- [**3.2 Cara melakukan pencarian tanpa menggunakan Recuva Wizard**](#3.2)
- [**3.3 Cara melakukan pencarian menyeluruh (*Deep Scan*) menggunakan Recuva**](#3.3)
- [**3.4 Pengenalan layar pilihan (*Options Screen*)**](#3.4)

----

<a name="3.0"></a>
### 3.0 Sebelum Anda memulai ###

Di bagian ini, Anda akan belajar cara melakukan tipe-tipe pencarian yang berbeda, dan dikenalkan pada tab-tab *General* dan *Actions* di layar *Options*.

**Catatan**: Pencarian akan mendapatkan dan menunjukkan file yang masih mungkin untuk didapatkan kembali. Prosedur pendapatkan kembali dibahas di bagian [**4.0 Cara mendapatkan file kembali dan menimpanya dengan aman menggunakan Recuva**](https://securityinabox.org/id/recuva_mendapatkanfilekembali).

<a name="3.1"></a>
### 3.1 Cara melakukan pencarian menggunakan Recuva Wizard ###
 
**Recuva** *Wizard* sangat disarankan untuk situasi dimana Anda mengetahui nama lengkap atau sebagian dari file yang Anda ingin dapatkan kembali. Perangkat ini juga direkomendasikan apabila ini adalah kali pertama Anda menggunakan **Recuva**. Dengan **Recuva** *Wizard*, Anda dapat mencari parameter dengan memasukkan tipe file dan dimana file tersebut dihapus.

Untuk memulai mencari file yang terhapus, lakukan langkah-langkah dibawah ini:

**Langkah 1. Click** ![](/sbox/screen/recuva-en/15.png) atau **pilih Start > Programs > Recuva > Recuva** untuk meluncurkan program, dan mengaktfikan layar berikut:

![](/sbox/screen/recuva-en/16.png)

*Gambar 1: Layar Welcome to the Recuva Wizard*

**Tips**: Jika Anda mengetahui nama file ataupun sebagian nama file yang Anda ingin cari, **klik** ![](/sbox/screen/recuva-en/17.png) untuk pergi ke *Piriform Recuva main user interface*, lalu ikuti langkah-langkah **3.2 Cara melakukan pencarian tanpa menggunakan Recuva Wizard**. 

**Step 2**. **Click** ![](/sbox/screen/recuva-en/18.png) to activate the following screen:
**Langkah 2. Klik** ![](/sbox/screen/recuva-en/18.png) untuk mendapatkan layar berikut:

![](/sbox/screen/recuva-en/19.png)

*Gambar 2: Layar Recuva Wizard File type*

*Tipe file Recuva Wizard* menunjukkan tipe-tipe file, dan menjelaskan file apa yang Anda bisa dapatkan ketika setiap pilihan dinyalakan.

**Langkah 3. Centang** pilihan *Other* seperti yang ditunjukkan di *Gambar 2*, lalu **klik** ![](/sbox/screen/recuva-en/18.png) untuk mengaktifkan layar berikut:

![](/sbox/screen/recuva-en/20.png)

*Gambar 3: Layar Recuva Wizard File Location*

**Catatan**: Pengaturan yang ditetapkan untuk layar *Recuva Wizard File Location* adalah pilihan *I’m not sure (Saya tidak yakin)*. Pilihan ini akan meminta pencarian ke seua drive dan juga media portable, kecuali CDs, DVDs, dan media optikal. Sehingga, mungkin, akan membutuhkan waktu yang lebih lama untuk mendapatkan hasil.

File-file  lebih sering di hapus dari *Recycle Bin*  di sistem operasi **Windows**, untuk meminimalisir kesempatan Anda untuk menghapus informasi pribadi dan sensitive.

**Langkah 4. Centang** pilihan *In the Recycle Bin* seperti yang ditunjukkan *Gambar 3* diatas, lalu klik ![](/sbox/screen/recuva-en/18.png) untuk mendapatkan layar berikut:

![](/sbox/screen/recuva-en/21.png)

*Gambar 4: Thank you, Recuva is now ready to search for your files*
 
**Catatan**: Untuk pelatihan ini, jangan nyalakan pilihan *Deep Scan*. Teknik pencarian ini akan dibahas di bagian **3.3 Cara melakukan pencarian menyeluruh (*Deep Scan*) menggunakan Recuva**.
 
**Langkah 5. Klik** ![](/sbox/screen/recuva-en/22.png) untuk memulai proses mendapatkan kembali file yang terhapus.

Selama proses, dua *progress status bar* akan muncul. Progress bar bernama *Scanning the drive for deleted files* menjabarkan file-file yang terhapus. Progress bar bernama *Analyzing the file contents* mengumpulkan dan mensortir file-file yang terhapus ke dalam tiep-tipe file dan tingkat sejauh mana file dapat didapatkan kembali. Dua progress bar ini juga menunjukkan durasi dari pencarian dan proses analisis. Main user interface dari *Piriform Recuva* Anda mungkin akan mirip seperti layar berikut:

![](/sbox/screen/recuva-en/23.png)

*Gambar 5: The piriform recuva main user interface dengan file-file yang telah dihapus*

Main user interface dari *Piriform Recuva* mendaftarkan informasi tentang setiap file yang terhapus dan mengaturnya ke dalam enam kolom. Setiap kolom di jelaskan seperti berikut:

**Filename**: Ini menunjukkan nama dan extension file dari file yang terhapus. **Klik** judul *Filename* untuk mengatur file yang terhapus ke dalam urutan alfabet.

**Path**: ini menunjukkan dimana file yang terhapus ditemukan. Karena pilihan *In the Recycle Bin* dinyalakan di contoh ini, maka jalur file adalah *C:RECYCLER* untuk semua file yang terhapus. **Klik** judul *Path* untuk melihat semua file yang terdaftar dibawah jalur file atau direktori.

**Last modified**: Ini menunjukkan waktu terakhir ketika file dirubah sebelum file tersebut dihapus, dan dapat berguna untuk membantu untuk mengindentifikasi file yang Anda ingin dapatkan kembali. **Klik** *Last modified* untuk menjabarkan file yang terhapus menurut waktu terhapusnya.

**Size**: Ini menunjukkan ukuran dari file. **Klik** *Size* untuk menjabarkan file yang terhapus dari ukurang yang terbesar sampai yang terkecil.

**Status**: Kolom ini menunjukkan sejauh mana kemungkinan file tersebut untuk didapatkan kembali, dan *Gambar 6* menunjukkan cara menjawab ikon pada file status. **Klik** *Status* untuk memilah file yang terhapus ke dalam tiga kategori dasar, dan menjabarkan status mereka dari *Excellent* sampai *Unrecoverable*.

**Comment**: Kolom ini menjelaskan mengapa file yang diminta tidak dapat diperoleh kembaliini dan sejauh mana file yang dihapus telah ditimpa dalam **Windows Master File Table**. **Klik** *Komentar* untuk melihat sejauh mana sebuah file atau grup file telah ditimpa.

Setiap file mempunyai status ikon yang berwarna yang memberitahu sejauh mana untuk sebuah file dapat didapatkan kembali.

![](/sbox/screen/recuva-en/24.png)

*Gambar 6: Ikon file status*

Dibawah ini adalah penjelasan dari setiap ikon status:

-  **Hijau**: Kemungkinan untuk file didapatkan kembali sepenuhnya sangat baik.
- **Oranye**: Masih ada kemungkinan untuk mendapatkan file kembali.
-  **Merah**: Hampir tidak ada kemungkinan untuk mendapatkan file kembali.

<a name="3.2"></a>
### 3.2 Cara melakukan pencarian tanpa menggunakan Recuva Wizard ###

Untuk mengakses main user interface **Recuva** langsung, (tanpa menggunakana *Recuva Wizard*), ikut langkah berikut:

**Langkah 1. Klik** ![](/sbox/screen/recuva-en/15.png) atau **pilih Start > Programs > Recuva > Recuva** untuk mengaktifkan *Gambar 1*.

**Langkah 2. Centang** pilihan *Do not Show this Wizard on statup*, lalu klik (/sbox/screen/recuva-en/50.png) untuk mengaktifkan layar berikut:

![](/sbox/screen/recuva-en/51.png)

*Gambar 7: The Recuva main user interface*

Main user interface dari *Piriform Recuva* dibagi menjadi jendela hasil di sebelah kiri dan tab *Preview*, *Info* and *Header* yang digunakan untuk menyortir dan melihat informasi spesifik tentang file yang terhapus. Dengan ini, Anda dapat mengatur beberapa pilihan pencarian, mirip dengan pilihan yang ada di *Recuwa Wizred*.

**Langkah 3. Klik** untuk mengaktifkan dafatar drop-down and **pilih** drive yang ingin dicari, Local Disk (C:)* merupakan pilihan yang telah diatur dan akan digunakan di contoh ini:

![](/sbox/screen/recuva-en/52.png)

*Gambar 8: Daftar drop-down dari hard-drive*

Daftar drop-down dari *Filename atau jalur* membolehkan Anda untuk memberitahu file seperti apa yang Anda cari, dan sedikit bekerja sama dengan layar tipe *Recuva Wizard File* seperti yang ditunjukkan *Gambar 2*.

![](/sbox/screen/recuva-en/53.png)

*Gambar 9: Daftar drop-down File name atau Path*

Fitur *Filename atau path* adalah gabungan dari text box dan daftar drop-down. Ia mempunyai dua kegunaan: untuk membolehkan Anda mencari file yang spesifik, dan/atau mensorti seluruh daftar dari file yang terhapus, tergantung dari tipe file.

Atau, fitur *Filename atau path* dapat digunakan untuk mencari tipe file yang spesifik, atau untuk memilah-milah dari daftar umum dari file yang terhapus di jendela results.

Untuk memulai pencarian untuk file yang namanya diketahui sebagian atau seluruhnya, ikuti langkah berikut:

**Langkah 1. Ketik** nama atau sebagian nama dari file yang Anda ingin dapatkan kembali seperti berikut (di contoh ini, file *triangle.png* akan dicari):

![](/sbox/screen/recuva-en/54.png)

*Gambar 10: Daftar drop-down dari file name atau path sedang menunjukkan triangle.png*

**Tips: Klik** ![](/sbox/screen/recuva-en/55.png) untuk memunculkan kembali nama *File dan path* (tampilan berwarna keabu-abuan).

**Langkah 2. Klik** ![](/sbox/screen/recuva-en/56.png) untuk memulai pencarian; sesaat setelah itu, sebuah layar akan muncul yang mirip seperti ini:

![](/sbox/screen/recuva-en/57.png)

*Gambar 11: Recuva user interface menunjukkan triangle.png file di tab preview*

<a name="3.3"></a>
#### 3.3 Cara melakukan pencarian menyeluruh (Deep Scan) menggunakan Recuva ####

Dengan menyalakan pilihan *Enable Deep Scan* Anda dapat melakukan pencarian yang lebih dalam; tentunya, deep scan akan lebih banyak memakan waktu, bergantung pada kecepatan komputer Anda dan jumlah file yang Anda punya. Pilihan ini mungkin terbukti berguna apabila pencarian Anda sebelumnya tidak menunjukkan file yang Anda ingin dapatkan kembali. Walaupun *Deep Scan* mungkin dapat memakan waktu berjam-jam tergantung dengan jumlah data yang ada di komputer, ia mungkin memiliki kesempatan yang lebih tinggi untuk mendapatkan file yang diperlukan.
 
Pilihan **Recuva** *Deep Scan* dapat dinyalakan dengan cara **mencentang** pilihan **Enable Deep Scan** di *Recuva Wizard* (lihat *Gambar 4*).

**Langkah 1. Klik** ![](/sbox/screen/recuva-en/70.png) untuk mengaktifkan layar *Options*, lalu **klik** tab *Actions* berikut:

![](/sbox/screen/recuva-en/73.png)

*Gambar 12: Layar Options menunjukkan tab Actions*

**Langkah 2. Centang** pilihan *Deep Scan* *(menambah waktu pencarian)*, **klik** [](/sbox/screen/recuva-en/72.png).

**Langkah 3. Klik** ![](/sbox/screen/recuva-en/74.png) untuk memulai pencarian file yang sudah terhapus dengan memilih *Deep Scan*. Seperti yang disebutkan sebelumnya, deep scan mungkin akan memakan waktu berjam-jam, tergantung dari ukuran hard disk dan keceptan komputer:

![](/sbox/screen/recuva-en/78.png)

*Gambar 13: The Scan menunjukkan perkiraan waktu yang diperlukan untuk melakukan pencarian secara menyeluruh*

<a name="3.4"></a>
### 3.4 Pengenalan layar pilihan (*Option Screen*) ###

Di bagian ini, Anda akan belajar untuk melihat berbagai pengaturan untuk mendapatkan kembali dan menimpa informasi sensitif Anda di layar *Options*. Untuk mendapatkan pengaturan ini, ikut langkah berikut:

**Langkah 1: Klik** ![](/sbox/screen/recuva-en/70.png) untuk mengaktifkan layar berikut:

![](/sbox/screen/recuva-en/71.png)

*Gambar 14: Layar Options menunjukkan tab General di mode yang sudah ditetapkan*
 
Layar *Options(Pilihan)* terbagi menjadi tab *General (Umum)*, *Actions (Tindakan)* dan *About (Tentang)*

Tab *General* membolehkan Anda untuk memilih pengaturan yang penting, termasuk *Bahasa* (**Recuva** tersedia dalah 37 bahasa), *View mode* dan juga pilihan menyalakan atau mematikan *Recuva Wizard*.

![](/sbox/screen/recuva-en/76.png)

*Gambar 15: Daftar drop-down mode View*
 
*Modul view* membolehkan Anda untuk memilih bagaimana Anda ingin melihat file-file yang terhapus, dan dapat dinyalakan ketika Anda meng-**klik kanan** sebuah file di *Piriform Recuva*.

- **List** : pilihan ini membolehkan Anda melihat file-file yang terhapus per barisan seperti yang ditunjukkan *Gambar 5*

- ***Tree**: Pada pilihan ini, Anda dapat melihat jalur direktori dari file yang dihapus dalam bentuk bercabang-cabang.

- **Thumbnails**: Pilihan ini membolehkan Anda untuk melihat file dalam bentuk grafik atau foto (apabila bisa).

Mungkin yang terpenting adalah, bagian *Advanced* dari tab *Genereal* yang membolehkan Anda untuk mengatur berapa kali data Anda dapat ditimpa dengan data acak untuk melindunginya dari pihak jahat. 

Daftar drop-down *Secure overwriting* menunjukkan empat pilihan untuk menimpa informasi pribadi Anda. Modul yang diatur pengaturannya adalah *Simple Overwrite* (*1 
Pass)* seperti yang ditunjukkan *Gambar 14*. Pass adalah berapa kali dokumen, file, atau folder Anda akan ditimpa dengan data acak untuk membuatnya tidak dapat dibaca.

**Langkah 2: Pilihlah** *DOD 5220.22-M (3 passes)* seperti berikut:

![](/sbox/screen/recuva-en/77.png) 

*Gambar 16: Secure overwriting drop-down list dengan DOD 5220.22-M (3 passes)*

Sebuah pass akan terlhiat efektif ketika menimpa dokumen, file atau folder; namun, ada beberapa pihak yang mempunyai kemampuan dan narasumber untuk mendapatkan kembali data yang hanya ditimpa dengan ringan. Tiga pass adalah batas yang solid di antara waktu yang diperlukan untuk melakukan penimpaan data yang aman, dan kesempatan untuk mendapatkan kembali dokumen, file atau folder.

**Langkah 3. Klik** ![](/sbox/screen/recuva-en/72.png) untuk menyimpan pilihan konfigurasi tab *General* Anda.*

![](/sbox/screen/recuva-en/75.png)

*Gambar 17: Layar options menunukkan tab Actions*

- **Show files found in hidden system directories: Pilihan ini membolehkan Anda menunjukkan file yang terletak di sistem directori yang tersembunyi.

- **Show zero-byte files**: Dengan pilihan ini, Anda dapat menunjukkan file yang mempunyai isi yang sangat sedikit atau nyaris tidak ada sama sekali, yang pada dasarnya tidak dapat ditemukan kembali.

- **Show securely deleted files**: Pilihan ini membolehkan Anda menunjukkan file yang sudah dihapus secara aman di jendela hasil.

**Catatan**: apabila Anda sudah menggunakana **CCleaner** atau program lainnya yang mirip, program tersebut akan mengganti nama file menjadi *ZZZZZZ.ZZZ* demi alasan keamanan, ketika ia menghapus file secara aman.

- **Deep Scan**: Pilihan ini membolehkan Anda melakukan pencarian kepada seluruh drive untuk dokmuen atau file yang dihapus; apabila pencarian sebelumnya tidak menemukan file Anda, Deep Scan mungkin akan berguna. Tetapi, akan lebih memakan waktu. Silahkan baca bagian **3.3 Cara melakukan pencarian menyeluruh (*Deep Scan*) menggunakan Recuva**.

- **Scan for non-deleted files (untuk mendapatkan file dari disk yang rusak)**: pilihan ini membolehkan Anda untuk mencoba mendapatkan kembali files dari disks yang mungkin telah tidak sengaja rusak.
 
Tab *About* menunjukkan informasi versi, dan juga link ke website Piriform.

Sekarang Anda lebih merasa percaya diri dengan melakukan bermacam-macam pencarian dan lebih terbiasa dengan pengaturan di tab *General* dan *Actions* di layar *Options*, Anda telah siap untuk belajar cara mendapatkan kembali dan/atau dengan aman menimpa informasi pribadi dan sensitive di [**4.0 Cara mendapatkan file kembali dan menimpanya dengan aman menggunakan Recuva**](https://securityinabox.org/id/recuva_mendapatkanfilekembali).

