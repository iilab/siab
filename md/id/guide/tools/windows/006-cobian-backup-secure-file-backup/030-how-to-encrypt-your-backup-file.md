

---

lang: id
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: How to Encrypt Your Backup File

---

Bagian-bagian dari halaman ini:

- [**4.0 Tentang *Encryption***](#4.0)
- [**4.1 Cara melakukan Enkripsi (*Encrypt*) pada salinan file Anda**](#4.1)
- [**4.2 Cara melakukan *Decrypt* pada salinan file Anda**](#4.2)

-------

<a name="4.0"></a>
## 4.0 Tentang Encryption ##

*Encryption* menjadi kebutuhan bagi mereka yang ingin menyimpan file salinan yang tidak dapat diakses tanpa izin.

*Encryption* adalah proses membuat sandi atau mengacak data untuk menyelubungi pesan yang sesungguhnya dari orang-orang yang tidak mempunyai kunci khusus untuk membaca pesan tersebut. Untuk informasi lebih lanjut tentang *encryption*, silakan baca 'Petunjuk bagaimana caranya' Bab [**4.Cara melindungi berkas penting di komputer**](https://securityinabox.org/id/chapter-4).

<a name="4.1"></a>
## 4.1 Cara melakukan Enkripsi (*Encrypt*) pada salinan file Anda ##

Jendela *Strong Encryption* digunakan untuk memilih metode *encryption* yang akan digunakan.

**Langkah 1. Klik** box *Encryption type* untuk mengaktifkan daftar dari metode encryption yang berbeda sebagai berikut:

![](/sbox/screen/cobian-en/30.png)

*Gambar 1: Daftar tipe Encryption*

Untuk memudahkan, kami menganjurkan Anda memilih metode *Blowfish* atau *Rijndael* (128 bits). Ini akan menyediakan keamanan yang baik untuk arsip Anda, dan Anda dapat mengakses data yang di-*encrypt* dengan password pilihan Anda.

**Langkah 2 Pilih** tipe *Encryption* yang Anda ingin gunakan.

**Catatan**: *Rijndael* dan *Blowfish* memiliki tingkat keamanan yang rata-rata sama. *DES* mempunya proses *encryption* yang lebih lemah namun lebih cepat.

**Langkah 3. Ketik** dan **ketik ulang** password ke dalam dua boks yang disediakan seperti berikut:

![](/sbox/screen/cobian-en/31.png)

*Gambar 2: Boks type Encryption dan Passphrase*

Kekuatan sebuah password ditunjukkan oleh bar bertuliskan ‘Passphrase quality’. Semakin jauh bar tersebut bergerak ke kanan, lebih kuat passphrase Anda. Silahkan baca 'Petunjuk bagaimana caranya' Bab [**3. Cara membuat dan mempertahankan kata sandi yang aman**](https://securityinabox.org/id/chapter-3)dan 'Petunjuk yang membantu' Bab [**KeePass**](https://securityinabox.org/id/keepass) untuk instruksi panduan cara membuat dan menyimpan *passphrases* (atau password) dengan aman.

**Langkah 4**. **Klik** ![](/sbox/screen/cobian-en/13.png).

<a name="4.2"></a>
## 4.2 Cara melakukan *Decrypt* pada salinan file Anda ##

Melakukan *decrypt* untuk file salinan Anda sangat mudah. Silahkan lakukan langkah ini untuk melakukan *decrypt*:

**Langkah 1. Pilih Select > Tools > Decrypter and Keys** seperti yang ditunjukkan di bawah:

![](/sbox/screen/cobian-en/32.png)

*Gambar 3: Menu Tools dengan Decrypter dan Keys dipilih*

*Ini akan mengaktifkan window Decrypter dan keys seperti berikut:*

![](/sbox/screen/cobian-en/33.png)

*Gambar 4: Jendela Cobian Backup 10 Decrypter dan Keys*

**Langkah 2. Klik** ![](/sbox/screen/cobian-en/34.png) untuk memilih arsip yang Anda ingin Anda *decrypt*.

**Langkah 3.Klik** ![](/sbox/screen/cobian-en/35.png) untuk memilih folder lokasi yang Anda inginkan untuk arsip Anda yang telah di-*decrypt*.

**Langkah 4. Pilih** tipe *encryption* yang sama dengan yang Anda pilih di bagian  [**4.1 Cara melakukan enkripsi (*encrypt*) pada salinan file Anda**](https://securityinabox.org/id/cobian_encryption#4.1), di daftar *Metode*.

![](/sbox/screen/cobian-en/36.png)

*Gambar 5. Daftar New Methods (metode-metode baru)*

**Langkah 4. Pilih** metode yang benar untuk *encryption* (yang Anda pilih untuk melakukan *encrypt* pada salinan file Anda).

**Langkah 5.Ketik** passphrase Anda ke dalam tempat yand disediakan.

**Langkah 6**. **Klik** ![](/sbox/screen/cobian-en/37.png).

File-file akan langsung ter-*decrypt* di lokasi yang telah Anda pilih. Apabila file-file juga telah Anda *compress*, Anda perlu melakukan *decompress* seperti yang telah dijelaskan pada bab [**3.1 Cara melakukan *decompress* pada salinan file Anda**](https://securityinabox.org/id/cobian_compress-decompress#3.1).

