

---

lang: id
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 008
title: Eraser - Secure File Removal

---

**Situs Resmi**
  
[**www.heidi.ie/eraser**](http://www.heidi.ie/eraser/) 

**Sistem operasi yang diperlukan**

- Semua versi Windows

**Versi yang digunakan dalam panduan ini**

- 5.86a <br>
Walaupun anda mungkin dapat menemukan versi **Eraser** yang lebih baru di website pengembangnya, versi-versi tersebut tidak dimasukkan di sini, karena mereka memerlukan pemasanganan **.Net Framework** di **Microsoft Windows**. Mengunduh **.Net Framework** mungkin akan memerlukan waktu yang sangat lama bagi pengguna yang menggunakan *bandwidth* kecil.

**Lisensi**

- Piranti lunak gratis dan bisa diakses siapa saja (*Free and open-source software*)

**Petunjuk yang perlu dibaca**

- Petunjuk bagaimana caranya bagian [**6. Cara menghancurkan informasi rahasia**](https://securityinabox.org/id/chapter-6)

**Level**: 1: Pemula, **2: Umum**, 3: Menengah, 4: Berpengalaman, 5: Ahli


**Waktu yang diperlukan untuk menggunakan alat ini**: 20 menit

**Apa yang akan Anda dapatkan**:

- Pengetahuan untuk menghapus semua file yang tidak dinginkan dari komputer Anda secara permanen.
- Pengetahuan untuk menghapus file yang dapat di dapatkan kembali yang tidak terlihat di komputer	

**GNU Linux, Mac OS dan Program Microsoft Windows yang kompatibel**:

Di **GNU/Linux**, paket *secure-delete* dapat [**digunakan dari terminal**](http://www.ghacks.net/2010/08/26/securely-delete-files-with-secure-delete/) untuk menghapus file dan folder secara aman, atau menghapus ruang di dalam disk. *Secure-delete* dapat juga [**digabungkan dengan *graphical file manager***](http://techthrob.com/2010/07/07/adding-a-secure-delete-option-to-nautilus-file-manager-in-linux/).

Di **Mac OS** Anda dapat menggunakan menu **Finder** item **Finder** untuk secara permanen menghapus file dan folder. Anda juga dapat menggunakan program generic **Mac OS** *Disk Utility* untuk menghapus dengan aman seluruh disk atau 'ruang kosong (*free space*)' di dalam disk internal atau eksternal.

Di **Microsoft Windows** selain dari **Eraser** yang dijelaskan di bab ini, penguna juga dapat menggunakan [**CCleaner**](/id/ccleaner) untuk secara aman menghapus file dan folder dari **Recycle Bin**. **CCleaner** juga dapat memebersihkan ruang di dalam disk. Alat lain yang dapat direkomendasikan yang dapat digunakan untuk menghapus file secara aman ialah [**Freeraser**](http://www.freeraser.com/).

Kami juga ingin menyarankan alat multiplatform berikut: [**DBAN - Darik's Boot And Nuke**](http://www.dban.org/). Ini adalah sebuah paket yang Anda masukkan ke sebuah CD dan memulai komputer Anda. **DBAN** membolehkan Anda menghapus secara aman seluruh isi dari hard disk yang dapat ditemukan, menjadikannya alat yang *ideal* untuk penghancuran data yang banyak dan darurat.

## 1.1 Hal-hal yang perlu Anda ketahui sebelum menggunakan Alat ini ##

**Eraser** digunakan untuk *menghapus* data yang sensitive secara permanen dari komputer Anda. Ia melakukan ini dengan menimpa data yang Anda ingin hapus. Anda dapat memilih file atau folder yang Anda ingin hapus dengan cara ini. **Eraser** juga akan menghapus salinan dari file yang mungkin masih terdapat di komputer Anda tanpa sepengetahuan Anda. Ini termasuk file-file yang sebelumnya dihapus dengan metoder standar penghapusan **Windows**, dan salinan dari kopi yang Anda pernah kerjakan sebelumnya.

- Menghapus file dengan **Eraser** dapat dilakukan pada waktu yang ditentukan.
- Apabila Anda menjadwalkan untuk menjalankan program **Eraser** pada waktu tertentu, maka nyalakan komputer Anda pada waktu tersebut atau penghapusan tidak dapat dilakukan 
- Ketika Anda menghapus sebuah file menggunakan **Eraser**, file tersebut tidak bisa didapatkan kembali menggunakan program pendapatan file kembali (*file recovery program*).
- Untuk keamanan yang lebih, Anda harus mengatur **Eraser** untuk menimpa file yang Anda pilih untuk dihapis sebanyak 3 sampai 7 kali.
- **Eraser** dapat digunakan untuk membersihkan komputer Anda yang berarti secara permanen menghapus semua jejak-jejak pekerjaan yang mungkin sebelumnya belum dihapus secara benar, dan secara, bisa didapatkan kembali.


