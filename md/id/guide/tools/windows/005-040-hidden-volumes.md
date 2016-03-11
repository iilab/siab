

---

lang: id
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 4
depth: 3
title: Hidden Volumes

---

Topi bahasan dari halaman ini:

- [**5.0 Tentang Hidden Volumes**](#5.0)
- [**5.1 Cara membuat Hidden Volume**](#5.1)
- [**5.2 Cara melakukan Mount pada Hidden Volume**](#5.2)
- [**5.3 Tips cara menggunakan fitur Hidden Disk dengan aman**](#5.3)

-------

<a name="5.0"></a>
## 5.0 Tentang Hidden Volumes ##
 
Di **TrueCrypt**, *Hidden Volume*  disimpan di dalam *Standard Volume* yang telah di encrypt, tetapi keberadaannya diselubungkan. Walaupun Anda melakukan *mount* atau membuka standard volume Anda, tidak mungkin Anda dapat menemukan atau membuktikan keberadaan dari Hidden Volume. Apabila Anda dipaksa untuk menunjukkan password dan lokasi dari stAndard volume, isi dari standard volume akan terlihat, namun *tidak* dengan keberadaan hidden volume di dalam volume tersebut.

Anda dapat bayangkan komper dengan kompartemen tersembunyi. Anda dapat menyimpan file-file yang Anda tidak keberatan apabila disita atau hilang di dalam bagian normal dari koper Anda, namun Anda menyimpan file yang penting dan pribadi di dalam kompartemen rahasia. Tujuan dari dari kompartemen rahasia (terutama yang didesain khusus), adalah untuk menyembunyikan keberadaannya dan tentunya, dokumen di dalamnya.

<a name="5.1"></a>
## 5.1 Cara membuat Hidden Volume ##

Proses pembuatan Hidden Volume **TrueCrypt** mirip dengan pembuatan *Standard Volume* **TrueCrypt**: Beberapa panel, layar dan jendela bahkan sama persis.

**Langkah 1**. **Buka** **TrueCrypt**.

**Langkah 2**. **Klik** ![](/sbox/screen/truecrypt-en/13.png) untuk mengaktifkan *TrueCrypt Volume Creation Wizard*. 

**Langkah 3**. **Klik** ![](/sbox/screen/truecrypt-en/05.png) untuk menerima pilihan  *Create an encrypted file container* yang sudah ditentukan.

**Langkah 4**. **Centang** pilihan *Hidden TrueCrypt volume* sebagai berikut: 

![](/sbox/screen/truecrypt-en/37.png)

*Gambar 1: TrueCrypt Volume Creation Wizard dengan pilihan volume Hidden TrueCrypt menyala*

**Langkah 5**. **Klik** ![](/sbox/screen/truecrypt-en/05.png) untuk menampilkan layar berikut:

![](/sbox/screen/truecrypt-en/38.png)

*Gambar 2: Jendela mode TrueCrypt Volume Creation Wizard*

- *Direct mode*: Pilihan ini membolehkan Anda membuat *Hidden Volume* di dalam *Standard Volume* yang sudah ada.

- *Normal mode*: Pilihan ini membolehkan Anda membuat *Standard Volume* yang benar-benar baru untuk menyimpan *Hidden Volume*. 

Dalam contoh ini, kita akan menggunakan *Direct mode*. 

**Catatan**: Jika Anda memilih untuk membuat *Standard Volume* yang baru, ulangi langkah-langkah yang dijabarkan dalam [**2.2 Cara membuat Standard Volume**](https://securityinabox.org/id/truecrypt_instalasi#2.2).

**Langkah6**. **Check** pilihan *Direct Mode*, kemudian **click** ![](/sbox/screen/truecrypt-en/05.png) untuk mengaktifkan jendela *TrueCrypt Volume Creation - Volume Location*.

**Catatan**: Pastikan *Standard Volume* tidak di-*mount* sebelumnya memilihnya.

**Langkah 7**. **Klik** ![](/sbox/screen/truecrypt-en/17.png) untuk menampilkan layar berikut:

![](/sbox/screen/truecrypt-en/29.png)

*Gambar 3: Jendela TrueCrypt Volume Creation Wizard - Select TrueCrypt Volume*

**Langkah 8**. **Letakkan** file volume menggunakan jendela *Select a TrueCrypt Volume* seperti yang ditunjukkan pada *Gambar 3*. 

**Langkah 9**. **Klik** ![](/sbox/screen/truecrypt-en/30.png) untuk kembali ke *TrueCrypt Volume Creation Wizard*.

**Langkah 10**. **Klik** ![](/sbox/screen/truecrypt-en/05.png) untuk mengaktifkan layar *Enter password*.

**Langkah 11**. **Ketik** password yang Anda gunakan ketika membuat *Standard Volume* ke dalam kotak *Password* untuk menampilkan layar di bawah ini:

![](/sbox/screen/truecrypt-en/46.png)

*Gambar 4: Panel Pesan Hidden Volume - TrueCrypt Volume Creation Wizard*

**Langkah 12**. **Klik** ![](/sbox/screen/truecrypt-en/05.png) setelah Anda membaca pesan untuk mengaktifkan layar *Hidden Volume Encryptions Options*.

**Catatan**: Biarkan pilihan untuk *Enkripsi Algoritma* dan *Hash Algoritma* untuk *Hidden Volume* dengan pilihan yang telah ditetapkan.

**Langkah 13**. **Klik** ![](/sbox/screen/truecrypt-en/05.png) untuk mengaktifkan layar berikut:

![](/sbox/screen/truecrypt-en/41.png)

*Gambar 5: Jendela Hidden Volume Size - TrueCrypt Volume Creation Wizard*

Anda akan diminta untuk menetapkan ukuran *Hidden Volume*. 

**Catatan**: Pertimbangkanlah jenis dokumen, jumlahnya dan ukuran yang harus disimpan. Sisakan tempat untuk *Standard Volume*. Apabila Anda memilih ukuran maksimum yang tersedia untuk *Hidden Volume*, Anda tidak akan dapat menyimpan file lain ke dalam *Standard Volume* yang original.
 
Apabila *Standard Volume* Anda berukuran 10 Megabytes (MB) dan Anda memilih *Hidden Volume* Anda dengan ukuran 5MB (seperti yang ditunjukkan di *Gambar 6* di atas), Anda akan mempunyai dua volumes (satu yang tersembunyi dan satu normal) dengan ukuran masing-masing 5MB.

Pastikan informasi yang Anda berikan di *Standard Volume* tidak melebihi 5MB yang telah Anda tentukan. Ini disebabkan karena program **TrueCrypt** tidak secara otomatis menyadari kehadiran dari *Hidden Volume*, dan dapat menimpa file di hidden volume dengan tidak sengaja. Anda dapat kehilangan semua file yang Anda simpan di hidden volume apabila Anda melebihi ukuran yang telah Anda tetapkan.

**Langkah 14**. **Ketik** ukuran hidden volume yang Anda inginkan ke dalam boks teks yang ditunjukkan oleh *Gambar 6*. 

**Langkah 15**. **Klik** ![](/sbox/screen/truecrypt-en/05.png) untuk menampilkan jendela *Hidden Volume Password*.

Anda sekarang harus membuat password yang *berbeda* dari yang Anda pasang untuk standard volume.Pilihlan password yang kuat. Silahkan baca [**KeePass**](https://securityinabox.org/id/keepass) untuk informasi lebih lanjut tentang cara membuat password yang kuat.

**Tips**: Apabila Anda mengantisipasi untuk menunjukkan isi dari volume **TrueCrypt**, letakkanlah password untuk standard volume Anda di **KeePass**, dan buatlah password yang kuat yang harus Anda ingat untuk hidden volume. Ini akan membantu Anda untuk menyelubungkan hidden volume Anda, karena Anda tidak akan meninggalkan jejak akan kehadiran hidden volume Anda.

**Langkah 16**. **Buatlah** sebuah password, dan **ketik** dua kali, kemudian **klik** ![](/sbox/screen/truecrypt-en/05.png) untuk menampilkan layar berikut:

![](/sbox/screen/truecrypt-en/42.png)

*Gambar 6. Jendela untuk Wizard TrueCrypt Volume Creation – Hidden Volume Format*
 
Biarkanlah pilihan *File System* dan *Cluster* seperti yang telah ditetapkan.

**Langkah 17. Pindahkan** kursor Anda memutari layar untuk menambahkan kekuatan *cryptographic* dari enkripsi lalu **klik** ![](/sbox/screen/truecrypt-en/25.png) untuk membuat format hidden volume.

*Setelah hidden volume telah terformat, layar berikut ini akan muncul:* 

![](/sbox/screen/truecrypt-en/43.png)

*Gambar 7: Layar pesan Wizard TrueCrypt Volume Creation*

**Catatan**: *Gambar 8* mengkonfirmasi bahwa hidden volume telah sukses dibentuk dan juga mengingatkan Anda akan resiko menimpa file yang terletak di hidden volume ketika menyimpan file di standard volume.
 
**Langkah 18. Klik** ![](/sbox/screen/truecrypt-en/27.png)  untuk mengaktifkan window Hidden Volume Created, lalu **klik** ![](/sbox/screen/truecrypt-en/28.png) dan kembali ke **TrueCrypt** console.

Hidden volume sekarang telah terbuat di dalam stAndard volume Anda. Anda sekarang dapat menyimpan dokumen di dalamnya yang tidak akan terlihat oleh siapapun bahkan oleh pengguna yang mengetahui password untuk standard volume tersebut.

<a name="5.2"></a>
## 5.2 Cara melakukan Mount pada Hidden Volume ##

Metode untuk melakukan mount atau membuat *Hidden Volume* dapat di akses adalah sama dengan yang Anda lakukan dengan *Standard Volume*; hanya saja Anda akan menggunakan password yang Anda baru saja buat untuk *Hidden Volume*.

Untuk *melakukan* mount atau membuka *Hidden Volume*, silahkan lakukan langkah ini:


**Langkah 1. Pilih** sebuah drive dari list (Seperti di contoh, drive *K*):

![](/sbox/screen/truecrypt-en/44.png)

*Gambar 8: Layar Drive yang terpilih untuk mount di TrueCrypt Volume*
 
**Langkah 2. Klik** ![](/sbox/screen/truecrypt-en/17.png) untuk mengaktifkan jendela *Select a TrueCrypt Volume*.

**Langkah 3. Pilih Navigate** lalu **pilih** file volume **TrueCrypt** (file yang sama dengan standard volume).

**Langkah 4**. **Klik** ![](/sbox/screen/truecrypt-en/30.png) untuk kembali ke  **TrueCrypt** console.

**Langkah 5**. **Klik** ![](/sbox/screen/truecrypt-en/31.png) untuk menampilkan layar *Enter Password for* seperti berikut:

![](/sbox/screen/truecrypt-en/32.png)

*Gambar 9: Layar Enter Password (Masukkan password)*

**Langkah 6**. **Ketik** password yang Anda gunakan untuk membuat hidden volume, kemudian **Klik** ![](/sbox/screen/truecrypt-en/33.png). 

Hidden volume Anda kini telah di-*mount* (atau dibuka) seperti gambar berikut:

![](/sbox/screen/truecrypt-en/45.png)

*Gambar 10: Layar utama TrueCrypt menampilkan Hidden Volume yang sudah di-mount* 

**Langkah 7**. **Klik dua kali** pada entri di atas atau masuk melalui jendela *My Computer*. 

<a name="5.3"></a>
## 5.3 Tips cara menggunakan fitur Hidden Disk dengan aman ##

Tujuan dari fitur hidden disk adalah untuk menghindari situasi yang berpotensi bahaya dengan *terlihat seolah-olah* Anda menyerahkan file Anda yang Anda encrypt ketika seseorang dengan posisi yang kuat menuntut untuk melihat file tersebutt, tanpa harus memberitahu informasi Anda yang paling sensitif. Sebagai tambahan dari melindungi data Anda, ini akan membantu Anda untuk menghindari resiko keselamatan Anda atau mendedahkan kolega dan partner Anda di masa yang akan datang. Agar teknik ini efektif, Anda harus menciptakan situasi dimana seseorang yang menuntut untuk melihat file Anda akan puas dengan apa yang mereka lihat dan melepaskan Anda.
 
Untuk melakukan ini, sebaiknya Anda melaksanakan saran-saran berikut:

- Letakkanlah dokumen rahasia Anda yang Anda tidak keberatan untuk dilihat di stAndard volume. Informasi ini harus cukup sensitive sehingga tidak terlihat janggal apabila Anda menyimpannya di volume yang ter-encrypt.

- Hati-hati bahwa orang yang menuntut untuk melihat file Anda mungkin mengetahui tentang hidden volume Anda. Apabila Anda menggunakan **TrueCrypt** dengan benar, orang tersebut tidak akan bisa membuktikan bahwa hidden volume Anda ada, yang akan membuat pengelakkan Anda dapat dipercaya.

- Update file-file Anda di standard volume seminggu sekali. Ini akan memberikan kesan bahwa Anda betul-betul menggunakan file tersebut.
 
Ketika Anda melakukan *mount* pada volume **TrueCrypt**, Anda dapat memilih fitur *Protect hidden volume against damage caused by writing to outer volume*. Ini adalah fitur yang sangat penting yang membolehkan Anda untuk menambah file ‘samaran’ untuk standard volume tanpa resiko Anda menghapus atau menimpa isi yang ter encrypt di hidden volume Anda secara tidak sengaja.

Seperti yang telah disebut sebelumnya, dengan melebihi batas penyimpanan di stAndard volume Anda, Anda dapat merusak file tersembunyi Anda. Jangan menyalakan fitur *Protect hidden volume* ketika melakukan *mount* pada volume **TrueCrypt**, karena melakukan ini akan memaksa Anda untuk memasukkan password rahasia ke dalam hidden volume Anda dan akan menunjukkan dengan jelas keberadaan volume tersebut. Namun, ketika Anda meng-*update* file samaran Anda sewaktu sendiri, Anda harus selalu menyalakan pilihan ini.

Untuk menggunakan fitur *Protect hidden volume*, silahkan lakukan langkah dibawah:

**Langkah 1**. **Klik** ![](/sbox/screen/truecrypt-en/47.png) pada layar  *Enter Password* yang muncul seperti terlihat pada *Gambar 10* diatas. Ini akan mengaktifkan jendela *Mount Options* sebagai berikut:

![](/sbox/screen/truecrypt-en/48.png)

*Gambar 11: Jendela Mount Options (Pilihan mount)*

**Langkah 2**. **Centang** pilihan *Protect hidden volume against damage caused by writing to outer volume*.

**Langkah 3**. **Ketik** password Hidden Volume Anda, kemudian **click** ![](/sbox/screen/truecrypt-en/33.png).

**Langkah 4**. **Klik** ![](/sbox/screen/truecrypt-en/31.png) untuk melakukan *mount* pada Standar Volume Anda. Setelah proses *mount* berhasil, Anda akan dapat menambah file samaran tanpa membahayakan Hidden Volume Anda. 

**Langkah 5**. **Klik** ![](/sbox/screen/truecrypt-en/51.png) untuk *dismount*, atau membuat Standar Volume Anda tidak dapat digunakan ketika Anda selesai memodifikasi isinya. 

**Ingat**: Anda hanya perlu melakukan ini ketika Anda meng-*update* file-file yang ada di stAndard volume Anda. Apabila Anda terpaksa harus menunjukkan standard volume Anda kepada orang lain, janganlah Anda menggunakan fitur *Protect hidden volume*.

