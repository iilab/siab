

---

lang: id
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Compress and Decompress Your Files

---

Bagian-bagian dari halaman ini:

- [**3.0 Cara meng*compress* salinan file Anda**](#3.0)
- [**3.1 Cara me-*decompress (melepas compress)* salinan file Anda**](#3.1)

-------

<a name="3.0"></a>
## 3.0 Cara meng*compress* salinan file Anda ##

**Langkah 1. Buatlah** tugas salinan (*backup task*) seperti yang dijelaskan di [**2.2 Cara membuat salinan file**](https://securityinabox.org/id/cobian_install#2.2) yang berisi file salinan yang ingin Anda arsip.

**Langkah 2. Pilih** ![](/sbox/screen/cobian-en/22.png) dari sidebar kiri untuk mengaktifkan layar *New Task* sebagai berikut:

![](/sbox/screen/cobian-en/23.png)

*Gambar 1: Layar New task menunjukkan jendela compression dan Strong Encryption*

Jendela **Compression** digunakan untuk memilih metode untuk melakukan *compress* pada salinan Anda. 

**Catatan**: Peng-*compress*-an digunakan untuk mengurangi ruangan yang terpakai untuk menyimpan file. Apabila Anda mempunyai setumpuk file-file lama yang hanya Anda gunakan sekali-sekali, namun Anda masih ingin menyimpannya, akan lebih nyaman menyimpannya di dalam sebuah format dimana mereka hanya menggunakan sedikit memori/kapasitas disk Anda. Peng-*compress*-an  bekerja dengan membuang kode-kode yang tidak terlalu penting dari dokumen Anda dengan membiarkan informasi yang penting di dalamnya. Peng-*compress*-an tidak akan merusak data asli Anda. File-file tersebut tidak dapat dilihat ketika mereka sedang di-*compress*. Proses ini harus dikembalikan dan peng-*compress*-an file harus dicopot (*decompress*) ketika Anda ingin melihat file-file itu kembali.

Tiga sub-pilihan yang ada di daftar drop-down *Compression type* adalah:

***No Compression***: Pilihan ini tidak melakukan peng-*compress*-an, seperti yang Anda mungkin duga.

***Zip Compression***: Pilihan ini adalah teknik standar dari pengompresan di dalam sistem **Windows**, dan yang paling mudah. Arsip yang telah terbentuk, dapat dibuka melalui alat standar dari **Windows** (atau Anda dapat mengunduh program [**ZipGenius**](http://www.zipgenius.it/) untuk mengaksesnya).

Memilih type peng-*compress*-an yang terdaftar akan secara otomatis menyalakan bagian *Split options*, dan juga menu drop-down di dalamnya.

The ***Split options*** dapat digunakan untuk penyimpanan di media yang dapat dipindahkan, seperti CDs, DVDs, *Floppy disks* dan juga USB/Flashdisk. Pilihan *split* yang bermacam-macam akan terus membagi arsip ke dalam ukuran yang nantinya akan muat untuk disimpan ke dalam media penyimpanan yang dipilih.

Contoh: 
Misalnya Anda mengarsip file dalam jumlah besar, dan Anda ingin menaruh file itu ke dalam CD. NAmun, ternyata ukuran arsip Anda lebih besar dari 700MB (Ukuran sebuah CD). Fungsi membagi akan membagi arsip Anda berkeping-koping sehingga kurang dari atau sama dengan 700MB, yang Anda akan dapat masukkan ke CD. Apabila Anda berencana untuk menyalinnya ke *hard disk* komputer Anda, atau file yang akan Anda salin lebih kecil dari alat di mana file tersebut akan ditaruh, Anda tidak perlu melakukan hal ini.

Pilihan-pilihan berikut akan tersedia untuk Anda ketika Anda meng-klik daftar *Split options*. Pilihan Anda akan bergantung pada tipe dari media penyimpanan Anda.

![](/sbox/screen/cobian-en/24.png)

*Figure 2: The Split Options drop-down list*
*Gambar 2: Daftar drop-down Split Options*

- 3,5" - Floppy disk. Pilihan ini cukup besar untuk melakukan sebuah salinan dari jumlah dokumen yang sedikit

- Zip - Zip Disk (periksa kapasitas dari yang akan Anda gunakan). Anda akan memerlukan *Zip Drive* khusus di komputer Anda dan disk yang dibuat dengan penyesuaian.

- CD-R - CD disk (periksa kapasitasnya). Anda akan memerlukan CD Writer di komputer Anda dan juga program CD writing (Lihat versi [**DeepBurner Free** ](http://www.deepburner.com/) atau [**disk burning tools**](http://www.thefreecountry.com/utilities/dvdcdburning.shtml)).

- DVD - DVD disk (periksa kapasitasnya). Anda akan perlu sebuah DVD Writer di komputer Anda dan juga program DVD writing (Lihat versi [**DeepBurner Free** ](http://www.deepburner.com/)  [**disk burning tools**](http://www.thefreecountry.com/utilities/dvdcdburning.shtml)).

Apabila Anda menyalin ke dalam beberapa USB/Flashdisk, Anda mungkin ingin ukurannya disesuaikan

Untuk melakukannya, ikuti langkah-langkah ini:

**Langkah 1. Pilih** *Custom size* (bytes), lalu ketik ukuran dari arsip dalam bentuk bytes di tempat teks seperti berikut:

![](/sbox/screen/cobian-en/25.png)

*Gambar 10: Field text untuk Custom size*

Sebagai gambaran:

- 1KB (kilobyte) = 1024 bytes - satu halaman dokumen teks yang di buat di Open Office biasanya sekitar 20kb

- 1MB (megabyte) = 1024 KB - sebuah foto yang diambil di kamera digital biasanya berkisar di 1-3MB

- 1GB (gigabyte) = 1024 MB - kira-kira setengah jam dari film yang berkualitas DVD

**Catatan**: Ketika memilih ukuran yg disesuaikan  untuk memecah salinan Anda untuk dimasukkan ke CD atau DVD, **Cobian Backup** tidak akan menyalin file Anda ke dalam alat-alat portable tersebut secara otomatis. Tetapi, ia akan menciptaan arsip dari file tersebut di komputer dan Anda perlu memasukkannya ke dalam kepingan CD atau DVD  secara manual.

***Password Protect***: Dengan pilihan ini Anda dapat memasukkan password untuk melindungi arsip Anda. Ketik password Anda, lalu ketik ulang password di kotak yang disediakan. Ketika Anda ingin mencoba untuk melakukan *decompress* dari arsip Anda, Anda akan diminta untuk memasukkan password Anda sebelum melakukan tugas Anda.

**Catatan**: Apabila Anda ingin mengamankan arsip Anda, Anda harus mempertimbangkan tentang menggunakan metode lain selain menggunakan password. Dengan **Cobian Backup** Anda dapat melakukan *encrypt* pada arsip Anda. Ini akan dibahas di bagian [**4. Cara melalukan enkripsi (*encrypt*) pada salinan file Anda**](https://securityinabox.org/id/cobian_encryption). Selain itu, Anda juga dapat membaca [**Petunjuk yang membantu - TrueCrypt**](https://securityinabox.org/id/truecrypt) untuk mengetahui cara menciptakan ruang simpan yang ter*encrypt* di komputer Anda atau di alat yang dapat dipindahkan.

*Tambahan*: Pilihan ini memungkinkan Anda untuk menulis sesuatu yang deskriptif tentang arsip Anda, tetapi ini bukanlah suat keharusan.

<a name="3.1"></a>
## 3.1 Cara me-*decompress (melepas compress)* salinan file Anda ##

Untuk melakukan *decompress*, silahkan lakukan langkah berikut:

**Langkah 1. Select > Tools > Decompressor** seperti berikut;

![](/sbox/screen/cobian-en/26.png)

*Gambar 3: Menu Tools menunjukkan pilihan Decompressor*

Jendela **Decompressor** akan muncul seperti ini:

![](/sbox/screen/cobian-en/27.png)

*Gambar 4: Jendela Cobian 10 Backup - Decompressor*

**Langkah 2. Klik** ![](/sbox/screen/cobian-en/28.png) untuk membuka jendela pencarian  agar Anda dapat memilih arsip yang Anda ingin *decompress*.

**Langkah 3.Pilih** arsip (*.zip* or *.7x* file) llu **klik** ![](/sbox/screen/cobian-en/13.png).

**Langkah 4. Pilih** direktori tempat Anda akan membuka arsip file Anda. 

**Langkah 5. Klik** ![](/sbox/screen/cobian-en/29.png) untuk membuka jendela lain agar Anda dapat memilih folder dimana Anda dapat membuka arsip.

**Langkah 6.Pilih** sebuah folder, lalu **klik** ![](/sbox/screen/cobian-en/13.png).

Gunakan **Windows Explorer** untuk melihat file yang akan terkirim ke folder tersebut.


