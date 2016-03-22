

---

lang: id
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: How to Install Cobian Backup and Archive Your Files

---

bagian-bagian dari halaman ini:

- [**2.0 Cara memasang Cobian Backup**](#2.0)
- [**2.1 Cara menyalin direktori dan file Anda**](#2.1)
- [**2.2 Cara membuat salinan file**](#2.2)
- [**2.3 Cara membuat jadwal untuk pembuatan salinan file**](#2.3)

-------

<a name="2.0"></a>
## 2.0 Cara memasang Cobian Backup ##
 
**Catatan pemasangan**: Sebelum Anda memulai proses pemasangan, pastikan bahwa Anda mempunyai versi terbaru dair **Microsoft Windows Installer** dan juga **Microsoft.NET Framework**.

Memasang **Cobian Backup** termasuk mudah dan cepat. Untuk memasang **Cobian Backup**, ikuti langkah berikut:

**Langkah 1. Klik dua kali** ![](/sbox/screen/cobian-en/01.png); dialog boks *Open File - Security Warning* akan muncul. Jika sudah muncul, **klik** ![](/sbox/screen/cobian-en/02.png) untuk mengaktifkan status bar *Extracting the resource*, dan layar dibawah ini akan muncul beberapa saat kemudian:

![](/sbox/screen/cobian-en/03.png)

*Gambar 1: Jendela Cobian Setup - Please slect a language (Pilih bahasa)*

**Langkah 2. Klik** ![](/sbox/screen/cobian-en/04.png) untuk mengaktifkan layar *Please read the license agreement*; centang pilihan *I accept (Saya menerima)*, lalu **klik** ![](/sbox/screen/cobian-en/04.png) sekali lagi untuk mengaktifkan layar berikut:

![](/sbox/screen/cobian-en/05.png)

*Gambar 2: Jendela Select an installation directory (Pilih direktori instalasi)*

**Langkah 3. Klik** ![](/sbox/screen/cobian-en/04.png) untuk mengaktifkan layar berikut:

![](/sbox/screen/cobian-en/06.png)

*Gambar 3: Jendela Installation type dan service options (Tipe instalasi dan pilihan layanan)*
 
**Langkah 4. Centang** pilihan *Use Local System account* di jendela *Service options*, agar jendela Anda persis dengan yang ditunjukkan *Gambar 3* diatas.

**Penting**: Pilihan ini memastikan **Cobian Backup** untuk terus berjalan diam-diam di belakang, sehingga salinan file Anda akan muncul seperti yang telah dijadwalkan.

**Langkah 5. Klik** ![](/sbox/screen/cobian-en/04.png) untuk mengaktifkan pesan berikut:

![](/sbox/screen/cobian-en/07.png)

*Gambar 4: Cobian Backup 10 message prompt*

**Langkah 6. Klik** ![](/sbox/screen/cobian-en/08.png) untuk mengaktifkan layar pemasangan berikutnya, lalu **klik** ![](/sbox/screen/cobian-en/04.png) untuk melanjutkan proses pemasangan.

**Langkah 7. Klik** ![](/sbox/screen/cobian-en/09.png) untuk menyempurnakan proses instalasi. Lalu setelah proses pemasangan telah dilakukan, ikon **Cobian Backup** akan muncul di **Windows System Tray** seperti berikut: ![](/sbox/screen/cobian-en/10.png) 

<a name="2.1"></a>
## 2.1 Cara menyalin direktori dan file Anda ##

Di dalam topik ini Anda akan belajar cara membuat salinan atau arsip dari file atau folder yang Anda pilih. **Cobian Backup** menggunakan *backup task* yang dapat diatur untuk memasukkan kumpulan file spesifik dan/atau folder. *Backup task* dapat diatur untuk bekerja pada hari dan waktu yang telah ditentukan.

Untuk membuat *backup task*, Ikuti langkah berikut:

**Langkah 1. Klik** ![](/sbox/screen/cobian-en/11.png) untuk menciptakan *backup task* yang baru, dan mengaktifkan jendela *New task* seperti berikut:

![](/sbox/screen/cobian-en/12.png)

*Gambar 2: Jendela New task*

*Sidebar* sebelah kiri menjabarkan beberapa tab dan layar-layarnya - yang digunakan untuk mengatur pilihan dan parameter *backup* yang berbeda- ditunjukkan di jendela di sebelah kanan. Semua pilihan di dalam tab General dijelaskan dibawah ini:

### 2.1.1 Definisi pilihan ###

***Task Name***: di Kotak teks *Task Name* ini, Anda memasukkan sebuah nama untuk *backup task*. Gunakan nama yang mengidentifikasi sifat dari backup tersebut. Contoh, apabila salinan akan berisi file video, Anda dapat memberi nama *Video Backup*.

***Disabled***: *Jangan* pilih pilihan ini.

**Peringatan**: Dengan menyalakan pilihan *Disabled*, pilihan lain akan tertutupi dan ini menghalangi backup task dari bekerja dengan benar.

***Include Subdirectories***: Pilihan ini memungkinkan Anda memasukkan semua *subdirektori* atau folder di dalam sebuah direktori atau folder untuk *backup task*. Ini adalah metode yang efisien untuk menyalin folder dengan jumlah yang banyak. Sebagai contoh, apabila Anda memilih folder *My Documents*, semua file dan folder di *My Documents* akan termasuk di *backup task*.

***Create separated backups using timestamps***: Dengan pilihan ini, Anda dapat memilih tanggal dan waktu dari *backup task* tersebut untuk secara otomatis termasuk di dalam nama folder yang berisi file salinan Anda. Hal ini mempermudah Anda untuk mengetahui kapan salinan tersebut dibuat.

***Use file attribute logic***: Pilihan ini akan relevant ketika Anda memilih untuk melakukan salinan *incremental* atau *differential* (lihat bawah). Atribut dari file mengandung informasi tentang file.

**Catatan**: Berikut ialah pilihan yang hanya tersedia untuk versi **Windows OS** yang lebih baru daripada *dan* termasuk **Windows XP**.

***Use Volume Shadow Copy***: Pilihan ini memungkinkan Anda membuat salinan file yang terkunci 

**Cobian Backup** mengecek ulang informasi ini untuk memperkiraan apakah ada perubahan di file sumber/utama dibandingkan dengan ketika file tersebut baru disalin. Apabila Anda menyalakan *Differential* or *Incremental*, file akan langsung terbarukan (*update*).

**Catatan**: Anda hanya dapat menjalankan sepenuhnya atau *“dummy backup”* apabila Anda *tidak memilih* pilihan ini (*dummy backup* option dijelaskan di bawah).

### 2.1.2 Deskripsi jenis-jenis penyalinan ###

***Full***: Dengan pilihan ini, itu berarti bahwa *setiap* file di lokasi sumber akan dikopi ke dalam direkori salinan Anda. Apabila Anda membolehkan pilihan *Create separated backups using timestamp*, Anda akan mempunyai beberapa kopi dari sumber yang sama (teridentifikasi dengan waktu dan tanggal dari backcup yang ada di folder). Kalau tidak, **Cobian Backup** akan menimpa versi yang lama (kalau ada).

***Incremental***: Pilihan ini berarti program akan mengkonfirmasi  apabila file yang dipilih untuk disalin mengalami perubahan sejak proses penyalinan terakhir. Apabila tidak ada perubahan, maka ia akan dilewati ketika disalin untuk menghemat waktu penyalinan. Pilihan *Use File attribut logic* perlu dicentang untuk melakukan prosess penyalinan ini.

***Differential***: Program akan memeriksa apakah file sumber telah berubah sejak ***full** backup* yang terakhir. Apabila tidak perlu untuk menyalin file tersebut, file tersebut akan dilewati, untuk menghemat waktu penyalinan. Apabila Anda telah menyalin file yang sama sebelumnya, maka Anda bisa meneruskan untuk menyalinnya dengan menggunakan metode *Differential*.

***Dummy task***: Anda dapat menggunakan pilihan ini untuk membuat komputer Anda untuk menjalankan atau mematikan program pada waktu tertentu. Ini adalah pilihan yang lebih rumit yang tidak relevan dengan prosedur penyalinan dasar.

**Langkah 2.Klik** ![](/sbox/screen/cobian-en/13.png) untuk mengkonfirmasi pilihan pencarian Anda dan parameter untuk tugas penyalinan Anda.

<a name="2.2"></a>
## 2.2 Cara membuat salinan file ##

Untuk memulai penyalinan file, lakukan langkah berikut:

**Langkah 1. Klik** ![](/sbox/screen/cobian-en/14.png) di *sidebar* kiri dari jendela *New task* untuk memunculkan versi *Blank* dari layar berikut:

![](/sbox/screen/cobian-en/15.png)

*Gambar 3: Jendela The New task (MyBackup) memunculkan jendela Source and Destination (Lokasi sumber/awal dan lokasi tujuan)*

**Langkah 2.Pilih** file yang Anda ingin salin. (*Gambar 3* diatas, folder *My documents* dipilih).

**Langkah 3. Klik** ![](/sbox/screen/cobian-en/16.png) di jendela *Source* untuk mengaktifkan menu berikut:

![](/sbox/screen/cobian-en/17.png)

*Gambar 4: Panel Source - Add button menu*

**Langkah 4**. **Pilih** *Directory* apabila Anda ingin menyalin seluruh direktori, dan *Files* untuk menyalin file secara individual/satu per satu. Untuk memilih spesifik file individual ataupun direktori untuk disalin, pilih *Manually*, lalu ketik lokasi tujuan file atau direktori untuk salinan Anda.

**Catatan**: Anda dapat menambah file atau direktori sebanyak yang Anda suka. Apabila Anda ingin menyalin file yang sedang berada di server **FTP** Anda, pilihlah *FTP site* (Anda harus memiliki detil server login yang benar).

Ketika Anda sudah memilih file atau folder, mereka akan muncul di area *Source*. Seperti yang Anda lihat di *Gambar 3* diatas, terdapat folder *My Documents*, yang berarti folder ini akan termasuk di tugas penyalinan.

Jendela *Destination* menunjukkan dimana salinan akan disimpan.

**Langkah 5. Klik** ![](/sbox/screen/cobian-en/16.png) di jendela *Destination* untuk mengaktifkan menu berikut:

![](/sbox/screen/cobian-en/18.png)

*Gambar 5: Panel Destination – menu Add button*

**Langkah 6.Pilih** *Directory* untuk membuka jendela browser dimana Anda dapat memilih folder tujuan untuk file salinan Anda.

**Catatan**: Apabila Anda ingin membuat beberapa versi file salinan, Anda dapat menentukan beberapa folder disini.Apabila Anda memilih pilihan *Manually*, Anda harus mengetik sepenuhnya jalur ke folder yang Anda inginkan untuk menyimpan salinan.Untuk menggunakan Internet server yang jauh untuk menyimpan arsip Anda, **pilih** pilihan *FTP site* (Anda harus memasukkan  detil server login yang benar).

Sekarang layar Anda seharusnya mirip dengan contoh yang di atas dengan file dan folder di area source dan folder di area destinasi. Tetapi, janganlah dulu meng klik *OK* Anda masih harus mengatur jadwal penyalinan Anda.

<a name="2.3"></a>
## 2.3 Cara membuat jadwal untuk pembuatan salinan file ##

Agar penyalinan otomatis Anda bekerja, Anda perlu mengisi bagian *Schedule (Jadwal)*. Di bagian ini Anda dapat memilih waktu untuk melakukan penyalinan.

Untuk mengatur pilihan jadwal, lakukan langkah-langkah ini:

**Langkah 1. Pilih** ![](/sbox/screen/cobian-en/19.png) dari sidebar kiri, untuk mengaktifkan jendela berikut:

![](/sbox/screen/cobian-en/20.png)

*Gambar 6: Properties for myBackup menunjukkan panel tipe-tipe penjadwalan (Schedule)*

Pilihan *Schedule type (tipe penjadwalan)* terdapat di menu drop-down, dan dijelaskan dibawah ini:

***Once***: Penyalinan akan dilakukan sekali di tanggal dan waktu yang dipilih di area *Date/Time*.

***Daily***: Penyalinan akan dilakukan setiap hari pada waktu yang dipilih di area *Date/Time*.

***Weekly***: Penyalinan akan dilakukan pada hari yang dipilih pada setiap minggu. Pada contoh di atas, penyalinan akan dilakukan setiap hari Jum’at. Anda dapat memilih hari lain juga. Penyalinan akan dilakukan sekali pada hari yang dipilih dan waktu yang dipilih di area *Date/Time*.

***Monthly***: Penyalinan akan dilakukan pada hari yang dimasukan ke boks *'days of the month'* pada waktu yang telah dipilih di area *Date/Time*.

***Yearly***: Penyalinan akan dilakukan pada hari yang telah diketik di boks *'days of the month'*, pada bulan yang dipilih, dan pada waktu yang dipilih di area *Date/Time*.

***Timer***: Penyalinan akan dilakukan secara berulang dengan interval/jarak waktu yang telah ditentukan pada boks *Timer* di area *Date/Time*.

***Manually***: Anda harus melakukan penyalinan sendiri dari jendela *main program*.

**Langkah 2. Klik** ![](/sbox/screen/cobian-en/13.png) untuk mengkonfirmasikan pilihan dan pengaturan untuk jadwal penyalinan seperti berikut:

![](/sbox/screen/cobian-en/21.png)

*Gambar 7: Jendela New task menunjukkan panel penjadwalan yang telah ditentukan*

Ketika Anda sudah memilih jadwal penyalinan, Anda telah melakukan langkah terakhir. Penyalinan sekarang akan berjalan di folder yang telah Anda pilih sesuai dengan jadwal yang Anda tentukan.

