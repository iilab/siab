

---

lang: id
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: How to Use Enigmail with GnuPG in Thunderbird

---

Daftar isi laman ini:

- [**4.0 Sekilas tentang tentang Enigmail, GnuPG dan Enkripsi Kunci Pribadi-Publik (*Private-Public Key Encryption*)**](#4.0)
- [**4.1 Cara memasang Enigmail dan GnuPG**](#4.1)
- [**4.2 Cara mendapatkan Kunci Pasangan (*Key Pairs*) dan mengkonfigurasi Enigmail untuk bekerja dengan akun email Anda**](#4.2)
- [**4.3 Cara saling bertukar Kunci Publik (*Public Keys*)**](#4.3)
- [**4.4 Cara memvalidasi dan mendaftarkan Kunci Pasangan (*Key Pair*)**](#4.4)
- [**4.5 Cara melakukan Enkripsi (*Encrypt*) dan Dekripsi (*Decrypt*) sebuah pesan**](#4.5)

-------

<a name="4.0"></a>
## 4.0 Sekilas tentang tentang Enigmail, GnuPG dan Enkripsi Kunci Pribadi-Publik (*Private-Public Key Encryption*) ##
 
**Enigmail** adalah Program Pengaya (*Add-on*) dari **Mozilla Thunderbird** yang dapat  melindungi privasi komunikasi email Anda. **Enigmail** adalah sebuah *interface* yang memungkinkan Anda menggunakan program enkripsi **GnuPG** dari dalam **Thunderbird**. *Interface* **Enigmail** direpresentasikan sebagai *OpenPGP* di konsol **Thunderbird**.

Enigmail berbasiskan [**kunci publik kriptografi (public-key cryptography)**](http://id.wikipedia.org/wiki/Kriptografi). Di metode ini, setiap individu harus mendapatkan kunci pasangan pribadi (*personal key pair*) mereka. Kunci pertama disebut *kunci pribadi (private key)*. Kunci ini dilindungi oleh kata sandi atau kalimat rahasia, terjaga dan *tidak pernah* diberitahukan kepada *siapapun*. 

Kunci kedua dikenal sebagai *kunci publik (public key)*. Kunci ini dapat dibagi dengan koresponden/teman chat Anda. Ketika Anda telah memiliki *kunci publik* koresponden Anda, maka Anda mulai dapat mengirimkan email yang ter-enkripsi kepadanya. Hanya koresponden Anda yang dapat men-dekripsi dan membaca email Anda, karena hanya dia yang memiliki akses dengan *kunci pribadi* yang cocok. 

Begitu pula sebaliknya, Anda dapat mengirim salinan dari *kunci publik* Anda kepada kontak email Anda dan tetap merahasiakan *kunci pribadi* yang cocok, hanya Anda yang dapat membaca email yang ter-enkripsi dari kontak Anda. 

Dengan **Enigmail**, Anda juga dapat melampirkan tanda tangan digital dalam pesan Anda. Penerima pesan Anda yang memiliki salinan kopi asli dari *kunci publik* Anda akan dapat memverifikasi bahwa email tersebut datang dari Anda, dan isi dari email tersebut belum diketahui oleh siapapun. Juga, apabila Anda mempunyai *kunci publik* milik koresponden Anda, Anda dapat memverifikasi tanda tangan digital milik koresponden Anda dalam pesannya.

<a name="4.1"></a>
## 4.1 Cara memasang Enigmail dan GnuPG ##

Untuk instruksi cara mengunduh **Enigmail** dan **GnuPG**, Anda dapat membaca [**Bagian Mengunduh**](https://securityinabox.org/id/thunderbird) .

### 4.1.1 Cara Mengunduh GnuPG ###

Memasang GnuPG tidak rumit dan mirip dengan instalasi piranti lunak lainnya yang mungkin pernah Anda lakukan. 

Ikut langkah berikut untuk memulai pemasangan **GnuPG**:

**Langkah 1. Klik dua kali** ![](/sbox/screen/thunderbird-id/36.png) untuk memulai proses instalasi. Dialog boks *Open File - Security Warning* mungkin akan muncul. Apabila iya, **klik** ![](/sbox/screen/thunderbird-en/02.png) untuk mengaktifkan layar berikut:

![](/sbox/screen/thunderbird-id/37.png)

*Gambar 1: GNU Privacy Guard Setup Wizard*

**Langkah 2. Klik** ![](/sbox/screen/thunderbird-en/04.png) untuk mengaktifkan jendela *GNU Privacy Guard Setup - License Agreement*; setelah Anda selesai membacanya, **klik** ![](/sbox/screen/thunderbird-en/04.png) untuk mengaktifkan jendela *GNU Privacy Guard Setup - Choose Components*.
 
**Langkah 3. Klik** ![](/sbox/screen/thunderbird-en/04.png) untuk menerima pengaturan yang telah ditetapkan dan mengaktifkan jendela *GNU Privacy Guard Setup - Install Options - GnuPG Language Selection*. Pilih bahasa Indonesia seperti gambar di bawah ini:

![](/sbox/screen/thunderbird-id/38.png)

**Langkah 4. Klik** ![](/sbox/screen/thunderbird-en/04.png) untuk menetapkan bahasa yang dipilih, jendela *Choose Install Location* akan muncul.

**Langkah 5. Klik** ![](/sbox/screen/thunderbird-en/06.png) untuk menerima jalur pemasangan yang ditetapkan dan mengaktifkan layar *Choose Start Menu Folder*.

**Langkah 6. Klik** ![](/sbox/screen/thunderbird-en/06.png) untuk memulai instalasi paket **GnuPG**. Setelah proses ini selesai, layar *Installation Complete* akan muncul.

**Langkah 7. Klik** ![](/sbox/screen/thunderbird-en/04.png), lalu ![](/sbox/screen/thunderbird-en/08.png) untuk menyelesaikan instalasi program **GnuPG**.

### 4.1.2 Cara memasang Program Pengaya Enigmail ###

Setelah Anda berhasil memasang piranti lunak **GnuPG**, sekarang Anda telah siap untuk memasang program pengaya **Enigmail**.

Untuk memulai memasang **Enigmail**, lakukan langkah beriktu:

**Langkah 1. Buka Thunderbird**, lalu **pilih Alat > Pengaya** untuk mengaktifkan jendela *Pengaya*; jendela *Pengaya* akan muncul dengan jendela *Unduh Pengaya* yang telah menyala. 

**Langkah 2. Klik** ![](/sbox/screen/thunderbird-id/39.png) untuk mengaktifkan layar berikut:

![](/sbox/screen/thunderbird-id/40.png)

*Gambar 3. Jendela Pengaya dengan Panel Ekstensi* 

**Langkah 3. Klik** ![](/sbox/screen/thunderbird-en/46.png) untuk mengaktifkan layar berikut:

![](/sbox/screen/thunderbird-id/41.png)

*Gambar 4: Masukkan nama berkas untuk disimpan*

**Langkah 4**. Masuklah ke folder tempat Anda menyimpan **Enigmail** lalu **klik** ![](/sbox/screen/thunderbird-id/42.png) untuk mengaktifkan layar berikut:

![](/sbox/screen/thunderbird-id/43.png)

*Gambar 5: Jendela Pemasangan Perangkat Lunak*

**Penting**: Sebelum Anda melakukan langkah ini, pastikan bahwa semua pekerjaan online Anda telah disimpan!

**Langkah 7. Klik** ![](/sbox/screen/thunderbird-id/44.png) untuk kembali ke *Gambar 5*, lalu **klik** ![](/sbox/screen/thunderbird-id/45.png) untuk menyelesaikan pemasangan **Enigmail**.

Untuk memverifikasi pemasangan **Enigmail** Anda telah berhasil, kembali ke interface pengguna utama **Thunderbird**, dan periksa apakah **OpenPGP** muncul di toolbar **Thunderbird**.

![](/sbox/screen/thunderbird-id/46.png)

*Gambar 6: Toolbar Thunderbird dengan openPGP dipilih*

### 4.1.3 Cara untuk mengetahui apakah Enigmail dan GnuPG berfungsi ###

Sebelum Anda memulai menggunakan **Enigmail** dan **GnuPG** untuk mengotentikasi dan meng-enkripsi alamat email Anda, Anda harus pertama-tama memastikan bahwa kedua program ini telah berkomunikasi satu sama lain.

**Langkah 1. PIlih OpenPGP > Preferences** untuk menampilkan layar *OpenPGP Preferences* seperti berikut:

![](/sbox/screen/thunderbird-id/47.png)

*Gambar 7: Layar OpenPGP Preferences*

Apabila **GnuPG** telah berhasil dipasang, ![](/sbox/screen/thunderbird-en/54.png) akan muncul di bagian *Files and Directories*; jika tidak, akan muncul peringatan yang terlihat seperti berikut:

![](/sbox/screen/thunderbird-en/55.png)

*Gambar 8: Pesan OpenPGP Alert*

**Tips**: Apabila Anda menerima pesan ini, ia menandakan bahwa Anda telah memasang file di tempat yang salah. **Centang** pilihan *Override with* untuk menyalakan tombol *Browse...*, lalu **klik** ![](/sbox/screen/thunderbird-en/69.png) untuk mengaktifkan *Locate GnuPG program* dan secara manual pergi ke lokasi file *gpg.exe* di komputer Anda.

**Langkah 2. Klik** ![](/sbox/screen/thunderbird-en/56.png) untuk kembali ke konsol **Thunderbird**.

<a name="4.2"></a>
## 4.2 Cara mendapatkan Kunci Pasangan (*Key Pairs*) dan mengkonfigurasi Enigmail untuk bekerja dengan akun email Anda ##

Setelah Anda yakin **Enigmail** dan **GnuPG** bekerja dengan benar, Anda dapat mengkonfigurasi akun-akun email Anda menggunakan **Enigmail** untuk mendapatkan lebih dari satu pasangan kunci pribadi/kunci publik. 

### 4.2.1 Cara menggunakan *OpenPGP Wizard* untuk mendapatkan Kunci Pasangan ###

**Enigmail** menyediakan dua cara untuk mendapatkan pasangan kunci pribadi-publik; cara pertama adalah dengan menggunakan *OpenPGP Setup Wizard* dan cara kedua adalah dengan menggunakan layar *Key Management*. 

Untuk mendapatkan kunci pasangan dengan menggunakan *OpenPGP Setup Wizard*, lakukan langkah-langkah berikut:

**Langkah 1**. **Pilih OpenPGP > Setup Wizard** untuk membuka layar *OpenPGP Setup Wizard* seperti gambar berikut: 

![](/sbox/screen/thunderbird-id/48.png)

*Gambar 9: Layar Selamat datang di OpenPGP Setup Wizard*

**Langkah 2**. **Klik** ![](/sbox/screen/thunderbird-id/lanjut.png) untuk mengaktifkan layar berikut: 

![](/sbox/screen/thunderbird-id/49.png)

*Gambar 10: Layar Select Identities*

**Langkah 3**. **Klik** ![](/sbox/screen/thunderbird-en/04.png) untuk mengaktifkan layar berikut: 

![](/sbox/screen/thunderbird-en/60.png)

*Gambar 11: Layar Signing - Digitally Sign Your Outgoing Emails*

**Langkah 4**. **Klik** ![](/sbox/screen/thunderbird-en/04.png) untuk mengaktifkan layar berikut: 

![](/sbox/screen/thunderbird-en/61.png)

*Gambar 12: Layar Encryption - Encrypt Your Outgoing Emails*

**Langkah 5**. **Klik** ![](/sbox/screen/thunderbird-en/04.png) untuk mengaktifkan layar berikut: 

![](/sbox/screen/thunderbird-en/62.png)

*Gambar 13: Layar Preferences - Change Your Email Settings to Make OpenPGP Work More Reliably.png*

**Langkah 6**. **Klik** ![](/sbox/screen/thunderbird-en/63.png) untuk mengaktifkan layar berikut: 

![](/sbox/screen/thunderbird-en/64.png)

*Gambar 14: Layar Preferences*

**Catatan**: Pada bagian [**3.2 Cara mematikan fitur HTML di Thunderbird**](/id/thunderbird_pengaturankeamanan#3.2) kami sudah sedikit membahas bagaimana pesan yang dengan format HTML menempatkan Anda dalam resiko terserang oleh berbagai virus. Pilihan *Lihat Pesan sebagai teks polos* dan pilihan *Jangan membuat pesan HTML* ditujukan untuk menghadapi permasalahan tersebut. 

**Langkah 7**. **Klik** ![](/sbox/screen/thunderbird-en/56.png) untuk kembali ke *OpenPGP Setup Wizard*, kemudian **klik** ![](/sbox/screen/thunderbird-en/04.png) untuk mengaktifkan jendela *Create Key - Create A Key To Sign and Encrypt Email*. 

**Catatan**: Ketika pertama kali Anda mencoba membuat kunci untuk akun email, akun email Anda belum ada yang muncul di daftar *drop-down*.

**Langkah 8. Ketik** kata sandi yang terdiri dari 8 karakter alfanumerik ke dalam kedua kolom *Password* 

![](/sbox/screen/thunderbird-en/65.png)

*Gambar 15. Jendela Create Key – Create a key to sign and encrypt email*

**Langkah 9. Klik** ![](/sbox/screen/thunderbird-en/04.png) untuk menyetujui pengaturan ini lalu **klik** ![](/sbox/screen/thunderbird-en/66.png) untuk kembali ke layar *Create a Key*; nama akun email pertama Anda akan muncul, dan terlihat seperti berikut:

![](/sbox/screen/thunderbird-en/67.png)

*Gambar 16: Akun / USER ID yang baru terbuat*

**Langkah 10**. **Klik** ![](/sbox/screen/thunderbird-en/04.png) untuk mengaktifkan layar summary, yang pada dasarnya mencerminkan pengaturan yang digunakan ketika mendapatkan kunci pasangan.

**Catatan**: Kunci Pasangan yang didapatkan menggunakan *OpenPGP Setup Wizard* akan secara otomatis berdasarkan pada struktur 2048-bit, dan memiliki *masa hidup* 5 tahun. Dua karakteristik ini tidak dapat diganti setelah kunci pasangan dibuat menggunakan metode ini.

### 4.2.2 Cara mendapatkan kunci pasangan tambahan dan mencabut sertifikat untuk akun email lain ###

Mempunyai kunci pasangan yang terpisah untuk setiap akun email adalah hal yang biasa. Ikuti langkah di bawah ini apabila Anda ingin mendapatkan kunci pasangan tambahan untuk akun email Anda. Mendapatkan kunci pasangan berarti mendapatkan sertifikat pencabutan untuk kunci pasangan tersebut. Kirim sertifikat ini ke kontak Anda untuk mematikan fungsi kunci publik Anda, jika kunci pribadi Anda diketahui atau Anda kehilangan akses untuk masuk.

**Langkah 1. Pilih OpenPGP > Key Management** untuk mengaktifkan layar berikut:

![](/sbox/screen/thunderbird-en/70.png)

*Gambar 17: Menu OpenPGP Key Management dengan item New Key Pair terpilih*

**Catatan**: **Centang** *Display All Keys by Default* untuk melihat key pair yang dihasilkan dengan menggunakan *OPenPGP Setup Wizard* untuk akun email pertama Anda, seperti yang terlihat pada *Gambar 17* di atas.

**Langkah 2. Pilih Generate > New Key Pair** dari *Key Management* seperti yang ditunjukkan pada Gambar 17 di atas untuk mendapatkan layar berikut:

![](/sbox/screen/thunderbird-en/71.png)

*Gambar 18: Layar Generate OpenPgP Key (Pembuatan Kunci OpenPgp)*

**Langkah 3. Pilih** akun email dari menu drop-down *Account / User ID*, **centang** pilihan *Use generated key for the selected identity* . Lalu ciptakan frase rahasia untuk melindungi kunci pribadi Anda.

**Catatan**: Seperti namanya, frase rahasia ialah password yang lebih panjang. **Enigmail** akan meminta Anda untuk memasukkan password yang lebih panjang dan aman dibanding password pada umumnya.

**Penting**: Buatlah kunci pasangan dengan menggunakan frase rahasia, dan *jangan pernah* menyalakan pilihan 'No passpharase'.

![](/sbox/screen/thunderbird-en/72.png)

*Gambar 19: Tab Generate OpenPGP Key menampilkan the Key Expiry (masa kadaluarsa kunci)*

**Catatan**: Panjangnya *masa hidup* kunci pasangan bergantung pada kebutuhan privasi dan keamanan Anda; semakin sering Anda mengganti kunci pasangan, semakin rumit untuk sebuah kunci pasanga baru diketahui. Namun, setiap Anda mengganti kunci pasangan, Anda akan harus mengirimnya kepada koresponden Anda, dan melakukan verifikasi dengan setiap orang.

**Langkah 5. Ketik** nomor yang benar, dan **pilih** unit waktu yang Anda inginkan (*hari, bulan*, atau *tahun*) untuk masa aktif kunci pasangan Anda.

**Langkah 6. Klik** ![](/sbox/screen/thunderbird-en/73.png) untuk mengaktifkan layar berikut:

![](/sbox/screen/thunderbird-en/74.png)

*Gambar 20: Dialog box OpenPGP Confirm*

**Langkah 7**. **Klik** ![](/sbox/screen/thunderbird-en/73.png) untuk mengaktifkan layar berikut:

![](/sbox/screen/thunderbird-en/75.png)

*Gambar 21: Dialog box Open PGP meminta konfirmasi*

**Langkah 8**. **Klik** ![](/sbox/screen/thunderbird-en/76.png) untuk menampilkan jendela *Create & Save Revocation Certificate*.

**Catatan**: Apabila Anda mengetahui ada pihak jahat yang memiliki akses tanpa izin terhadap kunci publik Anda atau Anda kehilangan akses terhadap kunci ini, Anda dapat mengirim sertifikat pencabutan terhadap kontak Anda dan memberitahu mereka agar jangan menggunakan kunci publik Anda. Perlu diingat Anda mungkin harus melakukan ini apabila komputer Anda hilang, dicuri, atau disita. Anda juga sangat disarankan untuk membuat salinan dan melindungi sertifikat pencabutan Anda.

![](/sbox/screen/thunderbird-en/77.png)

*Gambar 22: Layar konfirmasi OpenPGP*

**Langkah 9. Klik** ![](/sbox/screen/thunderbird-en/78.png) untuk mengaktifkan layar berikut; lalu **ketik** kata sandi/frase rahasia untuk akun ini seperti berikut:

![](/sbox/screen/thunderbird-en/79.png) 

*Gambar 23: Silahkan ketik kata sandi OpenPGP Anda untuk melanjutkan mendapatkan kunci pasangan*

**Langkah 10. Klik** ![](/sbox/screen/thunderbird-en/56.png) untuk menyelesaikan proses pembuatan kunci pasangan dan sertifikat pencabutan, dan kembali ke layar berikut:

![](/sbox/screen/thunderbird-en/80.png) 

*Gambar 24: The OpenPGP Key Management window with the key pair displayed*

**Catatan: centang** pilihan *Display All Keys by Default* untuk menunjukkan semua kunci pasangan dan dan akun asosiasinya, apabila sedang sendirian berada di lingkungan yang aman.

Setelah Anda selesai mendapatkan kunci pasangan dan sertifikat pencabutannya, Anda sekarang telah siap untuk bertukar kunci publik dengan koresponden terpercaya Anda.

### 4.2.3 Cara mengkonfigurasi Enigmail untuk penggunaan akun email Anda ###

Untuk menyalakan **Enigmail** dengan akun email yang spesifik, lakukan langkah berikut:  

**Langkah 1**. **Pilih Alat > Pengaturan Akun**.

**Langkah 2**. **Pilih** item *OpenPGP Security* pada sidebar seperti berikut: 

![](/sbox/screen/thunderbird-id/55.png)

*Gambar 25: Layar Pengaturan Akun - OpenPGP Security screen*

**Langkah 3**. **Check** opsi *Enable OpenPGP support* dan **pilih** opsi *Use email address of this identity to identify OpenPGP key* seperti terlihat di *Gambar*.

**Langkah 4**. **Klik** ![](/sbox/screen/thunderbird-en/56.png) untuk kembali ke konsol **Thunderbird** . 

<a name="4.3"></a>
## 4.3 Cara saling bertukar Kunci Publik (*Public Keys*) ##

Sebelum Anda dapat memulai mengirimkan email yang di enkripsi satu sama lain, Anda dan koresponden Anda harus saling bertukar kunci publik (*Public Keys*). Anda juga harus mengkonfirmasi validitas dari kunci yang Anda terima dengan mengkonfirmasi bahwa itu benar-benar milik pemiliknya yang diakui. 

### 4.3.1 Cara mengirim kunci publik melalui Enigmail ###

Untuk mengirimkan Public Key menggunakan **Enigmail**/**OPenPGP**, baik koresponden Anda dan Anda akan melakukan langkah-langkah berikut:

**Langkah 1**. **Buka Thunderbird** dan kemudian **Klik** ![](/sbox/screen/thunderbird-id/57.png) untuk menulis pesan baru.

**Langkah 2**. Pilih menu option **OpenPGP > Attach My Public Key**.

Catatan: Dalam metode ini panel **Lampiran:** tidak ditampilkan segera; ini akan muncul segera seperti Anda mengirim pesan.

Jika Anda ingin mengirimkan kunci Publik yang berbeda pilih opsi menu **OpenPGP > Attach Public Key...** dan pilih kunci yang ingin Anda kirimkan.

![](/sbox/screen/thunderbird-id/59.png) 

*Gambar 26: Panel Tulis Pesan menampilkan kunci publik pada panel lampiran.*

**Langkah 3**. **Klik** ![](/sbox/screen/thunderbird-id/58.png) untuk mengirim email Anda dengan Kunci publik yang terlampir. Gambar seperti ini akan ditampilkan:

![](/sbox/screen/thunderbird-en/104.png)

*Gambar 28: Layar OpenPGP Prompt muncul untuk pengaturan enkripsi dan penandaan standar.* 

**Langkah 4**. **Centang** pilihan *Encrypt/sign message as a whole*, dan kemudian **klik** ![](/sbox/screen/thunderbird-en/56.png) untuk mengaktifkan *Gambar 23*.

**Langkah 5**. **Enter** passphrase Anda, dan kemudian **klik** ![](/sbox/screen/thunderbird-en/56.png) untuk mengaktifkan layar berikut:

![](/sbox/screen/thunderbird-en/105.png)

*Gambar 29: Boks OpenPGP Muncul - menanyakan Do you want to encrypt the message before saving?* 

**Langkah 6**. **Klik** ![](/sbox/screen/thunderbird-en/106.png) untuk enkrip, tandai dan kirim pesan Anda.

### 4.3.2 Cara Mengirim Kunci Publik menggunakan Enigmail ###

Baik Anda maupun koresponden Anda akan melakukan langkah-langkah berikut untuk saling menukarkan kunci publik. 

**Langkah 1**. **Pilih** dan **Buka** email yang berisi kunci publik milik koresponsedn Anda. 

Jika kunci publik milik korensponden Anda 'menyatu' dengan email, Anda dapat meng-**klik** tombol *Decrypt* untuk menampilkan *heading* berikut: 

![](/sbox/screen/thunderbird-en/84.png) 

*Gambar 30: **Klik** Decrypt untuk mengimpor kunci publik dalam pesan* 

**Langkah 2**. **Klik** ![](/sbox/screen/thunderbird-en/85.png) untuk memulai proses pemindaian secara otomatis, untuk memindai isi email yang berisi data terenkripsi. 

![](/sbox/screen/thunderbird-en/86.png)

*Gambar 31: Layar OpenPGP Confirm Import public key(s) embedded in message?* 

**Langkah 3**. **Klik** ![](/sbox/screen/thunderbird-en/87.png) untuk mengirimkan kunci publik korensponden Anda. 

Ketika Anda telah berhasil mengimpor kunci publik, pesan berikut akan muncul: 

![](/sbox/screen/thunderbird-en/108.png)

*Gambar 32: Layar OpenPGP Alert menampilkan kunci publik milik korensponden.* 

Lakukan langkah-langkah berikut sebagai konfirmasi bahwa Anda telah menerima kunci publik dari koresponden Anda:

**Langkah 1**. **Select OpenPGP > Key Management** agar layar *OpenPGP Key Management* berikut muncul:

![](/sbox/screen/thunderbird-en/107.png)

*Gambar 33: Layar OpenPGP - Key Management menampilkan kunci publik yang baru diimpor* 

<a name="4.4"></a>
## 4.4 Cara memvalidasi dan mendaftarkan Kunci Pasangan (*Key Pair*) ##

Terakhir, Anda harus melakukan verifikasi bahwa kunci yang baru diimpor adalah memang milik orang yang 'seharusnya' mengirimkan hal ini, setelah itu validitas kunci impor tersebut dikonfirmasi. Ini adalah langkah yang penting, dimana Anda dan teman Anda terlambat untuk saling mengikuti kunci publik yang Anda terima. 

### 4.4.1 Cara Melakukan Validasi Kunci Pasangan ###

**Langkah 1**. **Hubungi** koresponden Anda melalui jalur komunikasi selain email. Anda dapat menghubuginya melalui telepon, SMS, **Voice over Internet Protocol** (**VoIP**) atau cara lainnya, tapi Anda **harus** benar-benar yakin bahwa Anda berbicara dengan orang-orang yang benar. Untuk hasil yang baik, Anda dapat menggunakan jalur telepon atau berhadapan langsung. 

**Langkah 2**. Anda dan koresponden Anda harus melakukan verifikasi *sidik jari (fingerprint)* dari kunci publik yang sudah Anda ganti. *Sidik jari* adalah sebuah  serial yang unik (terdiri dari angka dan huruf) yang dapat mengidentifikasi tiap kunci. Anda dapat melihat sidik jari kunci pasangan yang telah Anda buat dan kunci publik yang Anda impor melalui layar **OpenPGP** *Key Management*. 

Untuk melihat sidik jari kunci pasangan tertentu, berikut langkah-langkahnya:

**Langkah 1**. **Pilih > OpenPGP > Key Management**, kemudian **klik-kanan** pada sebuah kunci yang terpilih untuk menampilkan layar berikut: 

![](/sbox/screen/thunderbird-en/90.png) 

*Gambar 34: Menu OpenPGP Key Management dengan item Key Properties terpilih* 

**Langkah 2**. **Pilih** *Key Properties* untuk mengaktifkan layar berikut: 

![](/sbox/screen/thunderbird-en/91.png)

*Gambar 35: Layar Key Properties*

Koresponden Anda harus juga melakukan langkah-langkah yang sama. Lakukan konfirmasi antara satu dengan yang lainnya. Jika ada satu saja yang tidak cocok, maka lakukan pertukaran kunci publik lagi dan ulang proses validasi di atas. 

**Catatan**: Sidik jari itu sendiri bukanlah sesuatu yang rahasia dan masih bisa disimpan untuk keperluan verifikasi nantinya. 

### 4.4.2 Cara Memberi Tanda pada Kunci Publik yang Valid ###

Setelah memastikan kunci koresponden yang diberikan adalah kunci yang benar, maka Anda harus *menandai*nya, untuk konfirmasi bahwa kunci ini adalah kunci yang valid. 

Cara menandai kunci publik yang sudah divalidasi adalah sebagai berikut: 

**Langkah 1**. **Klik** ![](/sbox/screen/thunderbird-en/56.png) untuk kembali ke layar *Key Management*.

**Langkah 2**. **Klik kanan** kunci publik koresponden Anda dan **pilih** item *Sign Key* dari menu. Layar berikut akan muncul: 

![](/sbox/screen/thunderbird-en/92.png)

*Gambar 36: Layar OpenPGP - Sign Key*

**Langkah 3**. **Centang** pilihan *I have done very careful checking*, kemudian **klik** ![](/sbox/screen/thunderbird-en/56.png) untuk menyelesaikan proses penandaan kunci publik milik koresponden Anda. Setelah proses validasi selesai, kembali ke jendela *OpenPGP Key Management* seperti berikut: 

![](/sbox/screen/thunderbird-en/93.png)

*Gambar 37: Jendela OpenPGP Key Management menampilkan kunci pasangan yang sudh divalidasi* 

#### 4.4.3 Cara Mengatur Kunci Pasangan Anda ####

Jendela *OpenPGP Key Management* digunakan untuk mendapatkan, memvalidasi dan menandatangi kunci pasangan yang berbeda-beda. Bagaimanapun juga, Anda dapat saja melakukan task lain yang berhubungan dengan *key management*: 

- **Change Passphrase**: Item ini memungkinkan Anda untuk mengubah kalimat yang melindungi kunci pasangan Anda. 
- **Manage User IDs**: Item ini mengijinkan Anda untuk berhubungan dengan lebih dari satu alamat email menggunakan satu kunci pasangan. 
- **Generate & Save Revocation Certificate**: Item ini memungkinkan Anda mendapatkan sertifikat pembatalan yang baru, jika Anda menghilangkan kunci pasangan yang sebelumnya. 

<a name="4.5"></a>
## 4.5 Cara melakukan Enkripsi (*Encrypt*) dan Dekripsi (*Decrypt*) sebuah pesan ##

**Penting**: Bagian kepala setiap pesan email - umumnya terdiri dari *Subject* dan penerima yang dimaksud (termasuk di dalamnya: *To*, *CC* dan *BCC*)- *tidak dapat* di-enkripsi dan akan dikirim sebagai pesan terbuka. Untuk memastikan privasi dan keamanan surat menyurat Anda,  bagian subjek dan penerima email sebaiknya dibiarkan *non-descriptive* dengan tujuan tidak *mengumbar* informasi sensitif. Selain itu, Anda disarankan untuk meletakkan semua alamat email pada kolom *BCC* ketika mengirimkan email pada orang banyak. 

Untuk melakukan enkripsi email dengan attachment, sangat disarankan untuk menggunakan pilihan **PGP/MIME**. Pilihan ini akan memperluas enkripsi sehingga mengikutsertakan semua file yang terlampir dalam email Anda. 

### 4.5.1 Cara Melakukan Enkripsi ###

Begitu Anda dan koresponden Anda berhasil mengirim, mem-validasi dan menandatangani kunci publik masing-masing, Anda selalu siap untuk mengirim dan menerima email yang memerlukan proses enkripsi dan dekripsi.

Untuk enkripsi isi email Anda, lakukan hal berikut: 

**Langkah 1**. **Buka** akun email Anda dan **klik** 
![](/sbox/screen/thunderbird-id/57.png) untuk menulis email.

**Langkah 2**. **Klik** ![](/sbox/screen/thunderbird-en/94.png) untuk menampilkan layar berikut:

![](/sbox/screen/thunderbird-en/95.png)

*Gambar 38: Jendela pop-up OpenPGP Encryption*

**Catatan**: Jika Anda memilih pilihan *Encrypt/sign message as a whole* dan mengirimnya menggunakan **PGP**/**MIME** seperti terlihat pada *gambar 28*, maka *gambar 35* tidak akan muncul. 

**Langkah 3**. **Centang** kedua pilihan *Sign Message* dan *Encrypt Message* seperti terlihat pada *gambar 32*, kemudian **klik** ![](/sbox/screen/thunderbird-en/56.png) untuk melengkapi penandaan dan proses enkripsi konten email Anda. 

**Catatan**: Untuk mem-verifikasi bahwa email Anda akan selalu di enkripsi dan ditandatangani, Anda dapat mencari dua ikon di pojok kanan bawah panel pesan seperti contoh berikut: 

![](/sbox/screen/thunderbird-en/97.png)

*Gambar 39: Ikon Message Signing and Encryption Confirmation icons*

**Langkah 4**. **Klik** ![](/sbox/screen/thunderbird-id/58.png) untuk mengirim pesan. Anda akan dimintai kata sandi sebelum menggunakan kunci pribadi Anda. 

### 4.5.2 Cara Melakukan Dekripsi ###

Ketika Anda menerima dan membuka pesan ter-enkripsi, **Enigmail/OpenPGP** secara otomatis akan mencoba untuk melakukan dekripsi pada pesan yang ter-enkripsi ketika Anda menerimanya dan membukanya. Ini akan mengaktifkan layar berikut:

![](/sbox/screen/thunderbird-en/79.png)

*Gambar 40: Layar OpenPGP Prompt - Please type in your OpenPGP passphrase or your SmartCard PIN*

**Langkah 1**. **Masukan** *passphrase*.

Setelah Anda memasukkan kunci *passphrase*, pesan tersebut didekripi dan ditampilkan sebagai berikut:  

![](/sbox/screen/thunderbird-en/109.png)

*Gambar 41: Pesan yang baru saja didekripi di panel pesan.* 

Anda telah berhasil mendekripsi dengan sukses. Dengan terus mengulang penjelasan di bagian [**4.5 Cara melakukan Enkripsi (*Encrypt*) dan Dekripsi (*Decrypt*) sebuah pesan**](/id/thunderbird_enigmaildangnupg#4.5), setiap saat Anda dan koresponden Anda bertukar pesan, Anda dapat menjaganya tetap rahasia dan privat, terlepas dari siapa pun yang mencoba untuk mengawasi pertukaran pesan Anda. 

