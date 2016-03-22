

---

lang: id
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 005
title: TrueCrypt - Secure File Storage

---

**Situs Resmi**

[**www.truecrypt.org**](http://www.truecrypt.org/)

**Sistem operasi yang diperlukan**

- Windows 2000/XP/2003/Vista/7
- Administrator rights required for installation or to create volumes but not to access existing volumes 

**Versi yang digunakan dalam panduan ini**

- 7.0a

**Lisensi**

- Piranti lunak gratis dan bisa diakses siapa saja (Free and Open-Source Software)

**Petunjuk yang perlu dibaca**: 

- Petunjuk bagaimana caranya [**4. Cara melindungi berkas penting di komputer**](https://securityinabox.org/id/chapter-4)
	
**Level** 

- (Volume Standard): 1: Pemula, 2: Umum, **3: Menengah**, 4: Berpengalaman, 5: Ahli

- (Volume Tersembunyi): 1: Pemula, 2: Umum, 3: Menengah, **4: Berpengalaman**, 5: Ahli


**Waktu yang diperlukan untuk menggunakan alat ini** 

- (Volume Standard): 30 menit 
- (Volume Tersembunyi): 30 menit 

**Apa yang akan Anda dapatkan**:

- Pengetahuan untuk melindungi file Anda dari penyusup secara efektif
- Pengetahuan untuk menyimpan salinan dari file-file penting secara aman dan mudah


**GNU Linux, Mac OS dan Program Microsoft Windows lainnya yang kompatibel:**

**Catatan**: Kami sangat merekomendasikan penggunaan **TrueCrypt** untuk **GNU Linux** dan **Mac OS**. 

Kebanyakan dari distribusi **GNU Linux**, seperti [**Ubuntu**](http://www.ubuntu.com/), mempunyai fitur standard dimana sistem ini mendukung *on-the-fly encryption-decryption* untuk seluruh disk. Anda dapat memilih untuk menggunakannya ketika Anda memasang sistem tersebut. Anda juga dapat menambahkan fungsi encryption ke dalam sistem **Linux** Anda dengan menggunakan integrasi dari [**dm-crypt**](http://www.saout.de/misc/dm-crypt/) dan [**cryptsetup and LUKS**](http://code.google.com/p/cryptsetup/) dan [**cryptsetup and LUKS**](http://code.google.com/p/cryptsetup/). Cara lainnya adalah dengan menggunakan [**ScramDisk for Linux SD4L**](http://sd4l.sourceforge.net/),yang merupakan program gratis dan open source untuk melakukan on-the-fly encryption-decryption.

Untuk **Mac OS** Anda dapat menggunakan **FileVault**, yang merupakan bagian dari sistem operasi, untuk menyediakan *on-the-fly* enkripsi dan dekripsi untuk isi dari folder utama Anda, dan semua sub-folder. Anda juga akan merasakan kegunaan dari program gratis dan opern source bernama [**Encrypt This**](http://www.nathansheldon.com/files/) yang dapat melakukan enkrip pada file pilihan menjadi .DMG disk image.

Terdapat banyak program enkripsi untuk **Microsoft Windows**. Berikut adalah beberapa rekomendasi kami:

* [**FreeOTFE**](http://www.freeotfe.org/) adalah program enkripsi yang gratis dan bisa diakses siapa saja (*free and open source*), serupa dengan **TrueCrypt**.
* [**The FREE CompuSec**](http://www.ce-infosys.com/english/free_compusec/free_compusec.aspx) adalah program on-the-fly enkripsi/dekripsi gratis dengan hak kepemilikan. Ia dapat melakukan enkripsi separuh maupun seluruh disk komputer, USB drives ataupun CD. Modul **DataCrypt** dari **CompuSec** juga dapat digunakan untuk melakukan enkripsi secara individual.
* [**CryptoExpert 2009 Lite**](http://www.cryptoexpert.com/lite/) 
adalah program on-the-fly encryption-decryption yang gratis dengan hak kepemilikan yang dapat membuat file container encryption seperti **TrueCrypt**.
* [**AxCrypt**](http://www.axantum.com/AxCrypt/) adalah program gratis dan open source yang dapat melakukan enkripsi pada file-file yang terpisah.
* [**Steganos LockNote**](https://www.steganos.com/us/products/for-free/locknote/overview/) adalah program gratis dan open source. Anda dapat menggunakannya untuk melakukan encrypt atau decrypt teks apapun. Teks akan disimpan di aplikasi **LockNote**: Mekanisme untuk melakukan encrypt atau decrypt pada sebuah catatan adalah bagian dari itu. **LockNote** dapat dipindahkan, dan tidak memerlukan pemasangan.

### 1.1	Hal-hal yang perlu Anda ketahui sebelum menggunakan alat ini ###

**TrueCrypt** dengan password yang Anda buat. Apabila Anda lupa password Anda, Anda akan kehilangan akses terhadap data Anda! **TrueCrypt** menggunakan proses yang disebut enkripsi untuk melindungi file Anda. Jangan lupa bahwa menggunakan enkripsi adalah illegal di sebagian Negara. **TrueCrypt** tidak melakukan encrypting kepada beberapa file, namun ia membuat area yang terlindungi, yang disebut *Volume*, di komputer Anda. Anda juga dapat menyimpan file Anda dengan aman di dalam volume yang di-enkripsi.

**TrueCrypt** mempunyai kemampuan untuk membuat volume standard yang di-encrypt atau hidden volume. Keduanya akan menyimpan file-file Anda secara rahasia, tetapi hidden volume menyembunyikan informasi penting Anda dibalik data yang tidak terlalu sensitif untuk melindunginya, walaupun ketika Anda terpaksa untuk menunjukkan volume **TrueCrypt** Anda. Panduan ini akan menjelaskan kedua jenis volume secara detil.

