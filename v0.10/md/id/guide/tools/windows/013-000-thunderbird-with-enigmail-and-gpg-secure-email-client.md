

---

lang: id
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 013
title: Thunderbird with Enigmail and GPG - Secure Email Client

---

**Situs Resmi**

- [**www.mozilla.com/thunderbird**](http://www.mozilla.com/thunderbird/)
- [**www.enigmail.mozdev.org**](http://enigmail.mozdev.org/home/index.php)
- [**www.gnupg.org**](http://www.gnupg.org/)

**Sistem operasi yang diperlukan**

- Semua versi Windows

**Versi yang digunakan dalam panduan ini**

- Thunderbird 11.0.1
- Enigmail 1.4.1
- GNU Privacy Guard (GnuPG) 1.4.9 

**Lisensi**

- Gratis dan bisa diakses siapa saja (*Free and Open-Source*)

**Petunjuk yang perlu dibaca:**

- Petunjuk bagaimana caranya Bab [**7. Cara agar komunikasi internet Anda tetap rahasia**](https://securityinabox.org/id/chapter-7)

Level: 1: Pemula, ***2: Umum, 3: Menengah***, 4: Berpengalaman, 5: Ahli

**Waktu yang diperlukan untuk menggunakan alat ini**: 40 menit

**Apa yang akan Anda dapatkan**: 

- Pengetahuan untuk mengatur beberapa akun email melalui satu program
- Pengetahuan untuk membaca dan membuat pesan setelah tidak terhubung lagi ke Internet
- Pengetahuan untuk menggunakan kunci enkripsi umum untuk menjaga privasi email Anda 

**GNU Linux, Mac OS dan Program Microsoft Windows lainnya yang kompatibel**:

Klien email **Mozilla Thunderbird** tersedia untuk **GNU Linux**, **Mac OS**, **Microsoft Windows** dan sistem operasi lainnya. Mengatur beberapa akun email adalah tugas yang rumit dilihat dari kacamata keamanan digital; karenanya, kami *sangat menyarankan* agar Anda menggunakan **Mozilla Thunderbird** untuk ini. Tingkat keamanan yang diberikan **Thunderbird**, program *cross-platform* yang *gratis* dan *open source*, lebih penting dibandingkan dengan saingan komersilnya seperti **Microsoft Outlook**. Akan tetapi, jika Anda ingin menggunakan program selain **Mozilla Thunderbird**, sebagai alternatif, kami merekomendasikan beberapa program yang juga gratis di bawah ini:

* [**Claws  Mail**](http://www.claws-mail.org/) dapat digunakan untuk **GNU Linux** dan **Microsoft Windows**;
* [**Sylpheed**](http://sylpheed.sraoss.jp/en/) dapat digunakan pada **GNU Linux**, **Mac OS** dan **Microsoft Windows**;
* [**Alpine**](http://www.washington.edu/alpine/) dapat digunakan pada **GNU Linux**, **Mac OS** dan **Microsoft Windows**.

### 1.1 Hal-hal yang perlu Anda ketahui sebelum menggunakan alat ini ###

**Mozilla Thunderbird** ialah klien email *cross-platfom* yang gratis untuk menerima, mengirim, dan menyimpan email. Klien email adalah aplikasi komputer yang dapat Anda gunakan untuk mengunduh dan mengatur pesan email tanpa koneksi Internet. Anda dapat mengatur beberapa akun email menggunakan satu program. Anda harus memiliki alamat email yang sudah ada sebelum menggunakan **Thunderbird**. Anda juga dapat membuat akun email [**Gmail**](https://www.google.com/accounts/NewAccount?service=mail) atau [**RiseUp**](http://securityinabox.org/id/riseup_caramembuatakun) apabila diinginkan.

**Enigmail** adalah tambahan yang dikembangkan untuk **Thunderbird**. Dengan **Enigmail**, pengguna dapat mengakses otentifikasi dan fitur *encryption* yang digunakan **GNU Privacy Guard (GnuPG)**.

**GnuPG** adalah program yang menyediakan kunci enkripsi umum yang digunakan untuk mendapatkan dan mengatur kunci berpasangan untuk digunakan dalam proses enkripsi dan dekripsi pesan-pesan, dan untuk menjaga komunikasi Anda rahasia dan aman. **GnuPG** harus dipasang agar **Enigmail** dapat bekerja, seperti yang nanti dijelaskan di bab ini.

