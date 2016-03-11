

---

lang: id
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: How to Install and Configure Eraser

---

Bagian-bagian dari halaman ini::

- [**2.0 Cara memasang Eraser**](#2.0)
- [**2.1 Cara mengatur Eraser**](#2.1)

-------

<a name="2.0"></a>
## 2.0 Cara memasang Eraser ##

Memasang **Eraser** adalah proses yang mudah dan cepat. Untuk memulai, ikut langkah berikut:

Seperti yang dijelaskan di 'Petunjuk bagaimana caranya' bagian [**6. Cara menghancurkan informasi rahasia**](https://securityinabox.org/id/chapter-6), **Eraser** menghapus data dari hard disk Anda dengan menimpanya dengan informasi acak. Semakin sering Anda menimpa data, semakin kecil kemungkinan data tersebut dapat ditemukan kembali.

**Langkah 1. Klik dua kali** ![](/sbox/screen/eraser-en/01.png); boks dialog O*Open File - Security Warning* mungkin akan muncul. Jika iya, klik ![](/sbox/screen/eraser-en/02.png) untuk mengaktifkan *InstallAware Wizard*; setelah beberapa saat, layar *Welcome to the InstallAware Wizard for Eraser* akan muncul.

**Langkah 2. Klik** ![](/sbox/screen/eraser-en/03.png) untuk mengaktifkan layar *License Agreement*, lalu **klik** checkbox untuk menyalakan pilihan *I accept the terms of the license agreement*, lalu **klik** ![](/sbox/screen/eraser-en/03.png) lagi untuk mengaktifkan jendela *Important Information*.

**Langkah 3.Klik** ![](/sbox/screen/eraser-en/03.png) setelah menbaca isi yang ditunjukkan di *scrolling window* untuk mengaktifkan jendela *Destination Folerd* dan **klik** ![](/sbox/screen/eraser-en/03.png) lagi.

**Langkah 4**. **Klik** ![](/sbox/screen/eraser-en/03.png) untuk menampilkan layar berikut:

![](/sbox/screen/eraser-en/04.png)

*Gambar 1: Jendela Pilih Folder Program (Select Program Folder)*

**Langkah 5. Centang** pilihan *Only for me (current user)* untuk memastikan hanya Andalah yang mempunyai izin untuk menggunakan **Eraser**, dan **klik** ![](/sbox/screen/eraser-en/03.png) untuk mengaktifkan jendela *Completing the InstallAware Wizard for Eraser*.

**Langkah 6**. **Klik** ![](/sbox/screen/eraser-en/03.png) lalu **klik** ![](/sbox/screen/eraser-en/05.png) untuk menyelesaikan proses instalasi, dan menjalankan **Eraser** seperti berikut: 

![](/sbox/screen/eraser-en/06.png)

*Gambar 2: Main user Interface dari Eraser*

<a name="2.1"></a>
## 2.1 Cara mengatur Eraser ##

**Catatan**: sangat dianjurkan agar Anda menimpa data paling sedikit tiga kali.

**Tips**: Setiap timpaan atau ***pass*** memakan waktu dan maka, semakin banyak ***pass***, proses penghapusan akan semakin lama. Ini akan terlihat terutama ketika menghapus file dengan ukuran besar, atau membersihkan ruang memori.

Jumlah pass dapat diatur dengan mengakses menu *Preferences: Erasing*.

**Langkah 1**. **Select > Edit > Preferences > Erasing...** seperti berikut: 

![](/sbox/screen/eraser-en/07.png)

*Gambar 3: Layar Eraser [On-Demand] menunjukkan Menu pilihan perubahan/edit*

*The Preferences: jendela Erasing terlihat sebagai berikut:*

![](/sbox/screen/eraser-en/08.png)

*Gambar 4: The Eraser Preferences: jendela Erasing*

Layar *Preferences: Erasing* menjelaskan bagaimana files akan ditimpa.

*Description*: Kolon ini menjabarkan nama dari prosedur-prosedur penimpaan.

*Passes*: Kolom ini menjabarkan berapa kali data akan ditimpa.

Di contoh ini, kami akan menimpa data kami menggunakan metode *Pseudorandom Data*. Seperti yang ditentukan, hanya satu pass yang dibuat ketika menggunakan pilihan ini. Akan tetapi, untuk keamanan ekstra kami akan menambah jumlah pass.

**Langkah 2**. **Pilih**  *#4 Pseudorandom Data* seperti yang terlihat di *Gambar 2*.

**Langkah 3**. **Klik** ![](/sbox/screen/eraser-en/09.png) untuk menampilkan layar *Passes* berikut:

![](/sbox/screen/eraser-en/10.png)

*Gambar 3: Layar Eraser Passes*

**Langkah 4. Aturlah** jumlah pass diantara tiga dan tujuh (ingat perbandingan waktu dan keamanan).

**Langkah 5**. **Klik** ![](/sbox/screen/eraser-en/11.png) untuk kembali ke layar *Passes*.

\# 4 Pseudorandom Data akan tampak seperti gambar di bawah:

![](/sbox/screen/eraser-en/12.png)

*Gambar 4: Layar Eraser Erase menunjukkan item 4 sedang dipilih*

**Tips**: Pastikan *check boxes* berlabel *Cluster Tip Area* dan *Alternate Data Streams* telah dicentang seperti gambar berikut (pilihan ini dicentang secara otomatis):

![](/sbox/screen/eraser-en/13.png)

*Gambar 5: Mode yang telah ditetapkan mencentang Eraser Cluster Tip Area dan Alternate Data Streams*

- *Cluster Tip Area*: Hard disk komputer dibagi menjadi segment-segment kecil yang disebut ‘cluster’. Biasanya, file memiliki beberapa clusters, dan file biasanya tidak mengisi secara penuh cluster yang terakhir, ruang yang tidak terisi di cluster terakhir ini disebut cluster tip area. Cluter tip area mungkin berisi informasi sensitive dari file lain yang ditulis di dalam cluster ini sebelumnya dan menempati lebih dari cluster nya. Informasi dari cluster tip mungkin dapat dibaca oleh spesialis proses mendapatkan data kembali. Jadi, **centanglah**  boks *Cluster Tip Area* untuk keamanan lebih.
- *Alternate Data Streams*: Ketika sebuah file disimpan di komputer Anda, ia bisa datang dengan berbagai bagian yang berbeda. Contohnya, teks ini berisi teks dan gambar-gambar. Ini akan disimpan di komputer Anda di lokasi atau ‘streams’ yang berbeda. Sehingga, **centanglah** boks *Alternate Data Streams* untuk memastikan semua data dihubungkan dengan file yang dihapus.

**Langkah 6**. **Klik** ![](/sbox/screen/eraser-en/11.png).

Anda sekarang telah mengatur metode penimpaan untuk **Eraser** menghapus file-file Anda. Anda juga harus mengatur pilihan yang sama untuk fitur *Unused Disk Space* yang muncul di tab berikutnya di layar *Preferences: Erasing*. Namun, Anda mungkin ingin mengatur jumlah passes ke angka yang dapat dicapai – perlu diingat bahwa penghapusan free-space akan memakan waktu dua jam per pass.

