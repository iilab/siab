

---

lang: id
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: How to Install TrueCrypt and Create Standard Volumes

---

Bagian- bagian dari halaman ini:

- [**2.0 Cara memasang TrueCrypt**](#2.0)
- [**2.1 Tentang TrueCrypt**](#2.1)
- [**2.2 Cara membuat Standard Volume**](#2.2)
- [**2.3 Cara membuat Standard Volume di dalam USB/Flashdisk**](#2.3)
- [**2.4 Cara membuat Standard Volume (Lanjutan)**](#2.4)

-------

<a name="2.0"></a>
## 2.0 Cara memasang TrueCrypt ##

**Langkah 1. Klik dua kali** ![](/sbox/screen/truecrypt-en/01.png); dialog boks *Open File - Security Warning* mungkin akan muncul. Jika iya, klik ![](/sbox/screen/truecrypt-en/02.png) untuk mendapatkan layar **TrueCrypt** *License*.

**Langkah 2. Centang** pilihan *I accept and agree to be bound by the license terms* untuk mendapatkan tombol *Accept*; **klik** ![](/sbox/screen/truecrypt-en/03.png) untuk mendapatkan layar berikut:

![](/sbox/screen/truecrypt-en/04.png)

*Gambar 1: The Wizard Mode dalam mode instalasi yang sudah ditentukan*

- *Install* mode: Pilihan ini untuk pengguna yang tidak ingin menyembunyikan fakta bahawa mereka menggunakan **TrueCrypt** di komputer mereka. 

- *Extract* mode: Pilihan ini didesain untuk pengguna yang ingin menyimpan versi portable dari **TrueCrypt** di USB/flashdisk mereka dan tidak igin memasang **TrueCrypt** di komputer mereka.

**Catatan**: Beberapa dari pilihan yang ada (Contoh, entire partition and disk enkripsi) tidak dapat bekerja ketika **TrueCrypt** hanya berupa ekstrak saja.
 
**Catatan**: walaupun disarankan untuk memakai mode *Install* yang sudah ditetapkan, Anda masih dapat menggunakan **TrueCrypt** di modul portabel nantinya. Untuk mempelajari lebih jauh tentang menggunakan modul **TrueCrypt Traveller**, silahkan baca halaman [**TrueCrypt Portabel**](https://securityinabox.org/id/TrueCryptportabel).

**Langkah 3. Klik** ![](/sbox/screen/truecrypt-en/05.png) untuk mendapatkan layar berikut:

![](/sbox/screen/truecrypt-en/06.png)

*Gambar 2: Jendela Setup Options*

**Langkah 4. Klik** ![](/sbox/screen/truecrypt-en/07.png) untuk mengaktifkan layar *Installing* untuk memulai memasang **TrueCrypt** di sistem Anda.

**Langkah 5. Klik** ![](/sbox/screen/truecrypt-en/08.png) untuk mendapatkan layar berikut:

![](/sbox/screen/truecrypt-en/09.png)

*Gambar 3: Dialog boks konfirmasi TrueCrypt Setup*

**Langkah 6. Klik** ![](/sbox/screen/truecrypt-en/10.png) untuk meluncurkan website **TrueCrypt**, dan menyelesaikan pemasangan **TrueCrypt**, lalu **klik** ![](/sbox/screen/truecrypt-en/11.png).

**Catatan**: Semua pengguna sangat dianjurkan untuk melihat dokumentasi bantuan yang tersedia dari **TrueCrypt** setelah menyelesaikan tutorial ini.

<a name="2.1"></a>
## 2.1 Tentang TrueCrypt ##

**TrueCrypt** adalah program yang mengamankan file-file Anda dengan mencegah siapa saja mengakses tanpa password yang benar. Ia bekerja seperti brankas elektronik, agar Anda dapat mengunci file Anda sehingga hanya orang yang mempunyai password yang benar yang dapat membuka. **TrueCrypt** bekerja dengan membolehkan Anda membuat *volumes* atau bagian-bagian di komputer Anda dimana Anda dapat menyimpan file-file dengan aman. Ketika Anda menciptakan sebuah data, atau memindahkan data ke dalam volume-volume ini, **TrueCrypt** akan secara otomatis melakukan encrypt pada informasi tersebut. Ketika Anda membuka file atau mengeluarkan file tersebut, TrueCrypt akan secara otomatis mencopot encrypt agar dapat digunakan. Proses ini dinamakan *on-the-fly* enkripsi.

<a name="2.2"></a>
## 2.2 Cara membuat Standard Volume ##
 
Ada dua jenis volume yang dapat dibuat di **TrueCrypt**: *Hidden* dan *Standard*. Di bagian ini. Anda akan belajar cara membuat *Standard Volume* dimana Anda dapat menyimpan file Anda.
 
Untuk memulai menggunakan **TrueCrypt** untuk membuat *Standard Volume*, ikuti langkah berikut:

**Langkah 1. Klik dua kali** ![](/sbox/screen/truecrypt-en/52.png) atau **pilih Start > Programs > TrueCrypt > TrueCrypt** untuk membuka **TrueCrypt**.

**Langkah 2. Pilih** sebuah drive dari list di **TrueCrypt** seperti jendela di bawah ini:

![](/sbox/screen/truecrypt-en/12.png)

*Gambar 4: Konsol TrueCrypt*

**Langkah 3. Klik** ![](/sbox/screen/truecrypt-en/13.png) Volume untuk mengaktifkan *TrueCrypt Volume Creation Wizard* seperti berikut:

![](/sbox/screen/truecrypt-en/14.png)


*Gambar 5: Jendela TrueCrypt Volume Creation Wizard*

Ada tiga pilihan untuk melakukan encrypt pada *Standard Volume* di *Gambar 5*. Di bab ini, kami akan menggunakan pilihan *Create an encrypted file container*. Silahkan lihat [**TrueCrypt**](http://www.truecrypt.org/docs/) untuk deskripsi dari dua pilihan lain

**Langkah 4. Klik** ![](/sbox/screen/truecrypt-en/05.png) untuk menyalakan layar berikut:

![](/sbox/screen/truecrypt-en/15.png)

*Gambar 6: Jendela tipe Volume*
 
Dengan jendela *TrueCrypt Volume Creation Wizard Volume Type*, Anda dapat memilih apakah Anda menginginkan untuk membuat  volume *Standard* atau volume **TrueCrypt** yang *tersembunyi*.

**Penting**: Untuk informasi lebih lanjut mengenai *Cara membuat Hidden Volume*, silahkan baca halaman [**Hidden Volumes**](/id/truecrypt_hiddendisk).
 
**Langkah 5. Centanglah** pilihan *Standard TrueCrypt Volume*.

**Langkah 6. Klik** ![](/sbox/screen/truecrypt-en/05.png) untuk mendapatkan layar berikut:

![](/sbox/screen/truecrypt-en/16.png)

*Gambar 7: Jendela Volume Creation wizard-Volume Location*
 
Anda dapat menentukan di mana Anda ingin menyimpan *Standard Volume* Anda tersebut di layar *Volume Creation Wizard - Volume Location*. File ini dapat disimpan seperti file lain.

**Langkah 7**. Anda dapat **mengetik** nama file ke dalam kotak teks, atau **klik** ![](/sbox/screen/truecrypt-en/17.png) untuk mendapatkan layar berikut:

![](/sbox/screen/truecrypt-en/18.png)

*Gambar 8: Jendela navigasi Specify Path and File Name*
 
**Catatan**: Volume **TrueCrypt** berisi oleh file-file normal. Ini berarti Anda dapat memindahkan, mengopi, atau bahkan menghapusnya. Anda perlu mengingat lokasi dan nama dari file tersebut. Akan tetapi, Anda harus memilih nama baru untuk volume yang Anda buat (Baca juga bagian [**2.3 Cara membuat Standard Volume di dalam USB/Flashdisk**](https://securityinabox.org/id/truecrypt_instalasi#2.3) cara membuat Standar Volume di USB Memory Stick). Di tutorial ini, kami akan membuat StAndard Volume kami di folder **My Documents**, dengan nama file **My volume** seperti ditunjukkan di *Gambar 8* diatas.

**Tips**: Anda juga bebas menggunakan nama dan file extension apa saja. Contoh, Anda dapat memberi nama Standard volume Anda *recipes.doc*, sehingga ia akan terlihat seperti dokumen *Word*, atau *holiday.mpg*, sehingga akan terlihat seperti file film. Ini ada salah satu cara Anda untuk membantu Anda menyamarkan keberadaan Standard Volume Anda.

**Langkah 8. Klik** ![](/sbox/screen/truecrypt-en/19.png) untuk menutup jendela *Specify Path and File Name* and kembali ke jendela *Volume Creation Wizard* seperti berikut:

![](/sbox/screen/truecrypt-en/20.png)

*Gambar 9: TrueCrypt Volume Creation Wizard menunjukkan jendela volume location*
 
**Langkah 9. Klik** ![](/sbox/screen/truecrypt-en/05.png) untuk mengaktifkan *Gambar 10*.

<a name="2.3"></a>
## 2.3 Cara membuat Standard Volume di dalam USB/Flashdisk ##

Untuk membuat **TrueCrypt** Standard Volume di dalam USB Anda, lakukan langkah 1 sampai 7 di bagian [**2.2 Cara membuat Standard Volume**](https://securityinabox.org/id/truecrypt_instalasi#2.2), dimana Anda mengaktifkan layar *Select a TrueCrypt Volume*. Jangan pilih *My Documents* sebagai lokasi file Anda, piilh *navigate* to lalu **pilih** USB/flashdisk. Lalu, **masukkan** nama file dan buatlah *Standard Volume* disana.

<a name="2.4"></a>
## 2.4 Cara membuat Standard Volume (Lanjutan) ##

Di dalam tingkat ini, Anda sudah siap untuk memilih metode enkripsi yang spesifik (atau *algoritma* seperti yang ditunjukkan di layar) untuk meng-encode (memecahkan kode) data yang akan disimpan di *Standard Volume*.

![](/sbox/screen/truecrypt-en/21.png)

*Gambar 10: Jendela Volume Creation Wizard Encryption Options*

**Catatan**: Anda dapat membiarkan pilihan seperti yang ditetapkan. Semua algoritma yang ditunjukkan di kedua pilihan bisa dikatakan sebagai aman.

**Langkah 10. Klik** ![](/sbox/screen/truecrypt-en/05.png) untuk mengaktifkan layar *TrueCrypt Volume Creation Wizard* seperti berikut:

![](/sbox/screen/truecrypt-en/22.png)

*Gambar 11: Volume creation wizard menampilkan jendela ukuran volume*

Dengan Jendela *Volume Size* Anda dapat memilih size dari *Standard Volume*. Di contoh ini, volume telah diatur dengan ukuran 10 megabytes. Tetapi, Anda boleh memilih ukuran yang lain. Pertimbangkan ukuran dari dokumen-dokumen dan tipe file yang Anda akan simpan, lalu aturlah dengan ukuran yang cocok dengan file-file tersebut.

**Tips**: apabila Anda ingin membuat salinan dari Standard Volume Anda ke dalam CD nantinya, Anda lebih baik mengatur ukuran volume dengan tidak lebih dari 700MB

**Langkah 11. Ketik** ukuran volume yang specific di teks, lalu **klik** ![](/sbox/screen/truecrypt-en/05.png) untuk mengaktifkan layar berikut:

![](/sbox/screen/truecrypt-en/23.png)

*Gambar 12: TrueCrypt Volume Creation Wizard menunjukkan Volume Password*

**Penting**: Memilih password yang aman dan kuat adalah salah satu dari tugas yang paling penting yang akan Anda lakukan ketika menciptakan *Standard Volume*. Password yang baik akan melindungi volume yang mempunyai encrypt, dan akan lebih baik apabila password Anda kuat. Anda tidak perlu menciptakan password Anda ataupun mengingatnya apabila Anda menggunakan program pembuat password seperti KeePass. Silahkan baca [**KeePass**](https://securityinabox.org/id/keepass), untuk mengetahui lebih lanjut tentang pembuatan dan penyimpanan password.

**Langkah 12. Ketik** password Anda dan **ketik ulang** password Anda ke dalam teks field *Confirm*.

**Penting**: Tombol *Next* tidak akan bisa digunakan sampai kedua password yang Anda masukkan cocok. Apabila password Anda tidak dikategorikan sebagai aman, Anda akan diberi peringatan tentang ini. Pertimbangkanlah untuk merubahnya. Walaupun **TrueCrypt** tetap bekerja dengan password apa saja yang Anda pilih, data Anda mungkin tidak akan seaman ketika Anda memakai password yang kuat.

**Langkah 13. Klik** ![](/sbox/screen/truecrypt-en/05.png) untuk mendapatkan layar ini:

![](/sbox/screen/truecrypt-en/24.png)

*Gambar 13: TrueCrypt Volume Creation Wizard menunjukkan jendela Volume Format*

**TrueCrypt** sekarang telah siap untuk membuat *Standard Volume*. Gerakkan mouse Anda secara acak di dalam Window *TrueCrypt Volume Creation Wizard* untuk beberapa detik. Semakin lama Anda menggerakan mouse, semakin baik kualitas dari kunci enkripsinya.

**Langkah 14. Klik** ![](/sbox/screen/truecrypt-en/25.png) untuk memulai membuat Standard Volume Anda.
 
**TrueCrypt** sekarang telah disimpan dengan nama *My Volume* di dalam folder *My Documents* seperti yang telah tadi dikatakan. File ini akan berisi **TrueCrypt** *Standard Volume* dengan ukuran 10 Megabytes, sehingga Anda dapat menyimpan file-file Anda dengan aman.
 
Setelah *Standard Volume* berhasil dibuat, dialog box seperti berikut akan muncul:

![](/sbox/screen/truecrypt-en/26.png)

*Gambar 14: Layar TrueCrypt volume telah berhasil membuat pesan* 

**Langkah 15. Klik** ![](/sbox/screen/truecrypt-en/27.png) untuk menyelesaikan prosess pembuatan  *Standard Volume* Anda dan kembali ke konsol **TrueCrypt**.

**Langkah 16 Klik** ![](/sbox/screen/truecrypt-en/28.png) untuk menutup *TrueCrypt Volume Creation Wizard*.

