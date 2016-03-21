

---

lang: id
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Use OTR to Initiate a Secure Messaging Session in Pidgin

---

Bagian-bagian dari halaman ini:

- [**3.0 Tentang Pidgin dan OTR**](#3.0)
- [**3.1 Cara konfigurasi Pidgin-OTR Plugin**](#3.1)
- [**3.2 Langkah pertama - Cara mendapatkan *Private Key* (Kunci rahasia) dan menampilkan *Fingerprint*-nya**](#3.2)
- [**3.3 Langkah kedua - Cara mengesahkan sesi percakapan**](#3.3)
- [**3.4 Langkah ketiga - Cara mengesahkan identifikasi koresponden/teman *chat* Anda**](#3.4)

-------

<a name="3.0"></a>
## 3.0 Tentang Pidgin dan OTR ##

Lawan bicara Anda dan juga Anda harus mengkonfigurasi **OTR** plugin sebelum bisa melakukan sesi percakapan yang aman dan rahasia. Karena **OTR** plugin ini didesain khusus untuk **Pidgin**, ia akan secara otomatis mengidentifikasi ketika kedua pihak telah memasang dan mengkonfigurasi **OTR** plugin dengan benar.

**Catatan**: Apabila Anda meminta percakapan rahasia dengan teman Anda yang belum memasang atau mengkonfirgurasi **OTR**, **OTR** akan secara otomatis mengirim pesan bagaimana caran mendapatkan **OTR** Plugin.

<a name="3.1"></a>
## 3.1 Cara konfigurasi Pidgin-OTR Plugin ##

Untuk menjalankan **OTR**  plugin, lakukan langkah berikut:

**Langkah 1. Klik dua kali** ![](/sbox/screen/pidgin-en/13.png) atau **pilih** **Start > Programs > Pidgin** untuk meluncurkan **Pidgin** dan mengaktifkan jendela *Buddy List* (silahkan lihat *Gambar 1*).

**Langkah 2. Buka** menu *tools*, lalu **pilih** item *Plugins* seperti berikut:

![](/sbox/screen/pidgin-en/40.png)

*Gambar 1: Jendela Buddy List dengan item Plugins yang dipilih dari menu Tools*

Ini akan mengaktifkan jendela *Pugins* seperti berikut:

**Langkah 2. Geser ke bawah** ke pilihan *Off-the-Record Messaging*, lalu **klik** *cek box* nya untuk mengaktifkannya.

![](/sbox/screen/pidgin-en/41.png)

*Gambar 2: Jendela Pidgin Plugins dengan Off-the-Record Messaging terpilih*

**Langkah 3. Klik** ![](/sbox/screen/pidgin-en/42.png) untuk memulai mengatur jendela *Off-the-Record Messaging*.

Pada dasarnya, terdapat 3 langkah yang harus dilakukan ketika mengatur **OTR** secara benar agar dapat bekerja secara efektif dan ketiganya dijelaskan dibawah:

- **Langkah pertama**: Langkah ini melibatkan pembuatan kunci rahasia yang unik yang berhubungan dengan akun Anda, dan menunjukkan *fingerprint*. 

Dua langkah selanjutnya melibatkan sesi **IM** dan pengesahan *buddy* Anda.

- **Langkah kedua**: Dimana salah satu pihak meminta mengatur sesi yang aman dan rahasia dengan pihak yang juga *on-line*.

- **Langkah ketiga** adalah pengesahan atau meyakinkan idetitas dari buddy **Pidgin** Anda. (**Catatan**: di **Pidgin**, **buddy** adalah seseorang yang berkomunikasi dengan Anda melalui sesi percakapan. Proses ini dikenal dengan nama *authentication (pengesahan)* di **Pidgin** dan ini meyakinkan bahwa identitas *buddy* diketahui. Ini berarti mengkonfirmasi bahwa *buddy* Anda adalah orang yang *benar* seperti yang dia akui.

<a name="3.2"></a>
## 3.2 Langkah pertama - Cara mendapatkan *Private Key* (Kunci rahasia) dan menampilkan *Fingerprint*-nya ##

Sesi percakapan yang aman di **Pidgin** dinyalakan dengan membuat sebuah *kunci rahasia* dari akun yang relevan. Jendela konfigurasi *Off-the-Record* dibagi menjadi tab *Config* dan *Known fingerprints*. Tab *Config* digunakan untuk mendapatkan *kunci* untuk setiap akun Anda dan untuk mengatur pilihan **OTR** yang spesifik. Tab *Known fingerprints* mengandung kunci rahasia dari teman-teman Anda. Anda juga harus memiliki sebuah kunci untuk setiap *buddy* yang dengannya Anda ingin bicara secara pribadi.

![](/sbox/screen/pidgin-en/43.png)

*Gambar 3: Layar Off-the-Record Messaging menunjukkan tab Config*

**Langkah 1**. Untuk mengoptimalkan privasi Anda, centang *Enable private messaging (Nyalakan percakapan pribadi)*, *Automaticall intiate privat message (Lakukan percakapan pribadi secara otomatis)* dan *Don’t log OTR conversations (Jangan masuk dalam percakapan OTR)* di tab *Config* seperti yang ditunjukkan di *Gambar 3* diatas.

**Langkah 2. Klik** ![](/sbox/screen/pidgin-en/44.png) untuk memulai pembuatan kunci rahasia Anda; sebuah layar akan muncul, memberitahu Anda bahwa kunci rahasia sedang dibuat:

![](/sbox/screen/pidgin-en/45.png)

*Gambar 4: Boks konfirmasi Generating private key*

**Catatan**: *Buddy* Anda harus melakukan hal yang sama dengan akunnya sendiri.
 
**Langkah 3. Klik** ![](/sbox/screen/pidgin-en/37.png) setelah kunci rahasia (yang terlihat seperti ini), telah didapatkan:

![](/sbox/screen/pidgin-en/46.png)

*Gambar 5: contoh dari fingerprint sebuah kunci yang dihasilkan oleh program OTR*
 
**Penting**: Anda telah menciptakan kunci rahasia untuk akun Anda. Ini akan digunakan untuk meng-*encrypt* percakapan Anda sehingga tidak ada orang lain yang dapat membacanya, walaupun mereka berhasil mengawasi sesi percakapan Anda. *Fingerprint* adalah sebuah kumpulan huruf dan angka yang panjang, yang digunakan untuk mengidentifikasi kunci sebuah akun tertentu, yang terlihat seperti *Gambar 5* diatas.

**Pidgin** akan secara otomatis menyimpan dan mengesahkan *fingerprint* Anda, dan milik *buddy* Anda, agar Anda tidak harus mengingatnya.

<a name="3.3"></a>
## 3.3 Langkah kedua - Cara mengesahkan sesi percakapan ##

**Langkah 1. Klik dua kali** akun *buddy* Anda yang sedang online untuk memulai sesi percakapan baru. Apabila Anda berdua mempunyai **OTR** plugin terpasang dengan benar, Anda akan menyadari bahwa tombol **OTR** baru akan muncul di pojok kanan bawah dari window percakapan Anda.

![](/sbox/screen/pidgin-en/47.png)

*Gambar 6: Jendela pesan Pidgin menunjukkan ikon OTR dilingkari garis hitam*

**Langkah 2. Klik** ![](/sbox/screen/pidgin-en/48.png) untuk mengaktifkan menu pop-up, lalu **pilih** item *Start private conversation (memulai percakapan pribadi)* seperti berikut:

![](/sbox/screen/pidgin-en/49.png)

*Gambar 7: Menu pop-up dengan item Start Private conversation terpilih*

*Jendela **Pidgin IM** Anda akan terlihat seperti ini:*

![](/sbox/screen/pidgin-en/50.png)

*Gambar 8: Jendela Pidgin IM menunjukkan tombol Unverified (belum terverifikasi)*
 
**Catatan**: **Pidgin** akan secara otomatis memulai komunikasi dengan program **IM** *buddy* Anda dan mengambil pesan ketika Anda mencoba untuk menyalakan sesi percakapan yang aman dan rahasia. Hasilnya, tombol ![](/sbox/screen/pidgin-en/48.png) **OTR** berubah menjadi ![](/sbox/screen/pidgin-en/51.png),  menandakan bahwa Anda sekarang dapat meng-encrypt percakapan Anda dengan *buddy* Anda.

**Peringatan!** Walaupun percakapan ini aman, identitas dari *buddy* Anda belum disahkan. Hati-hati: *Buddy* Anda bisa jadi seseorang yang *berpura-pura* menjadi teman Anda.

<a name="3.4"></a>
## 3.4 Langkah ketiga - Cara mengesahkan identifikasi koresponden/teman *chat* Anda ##

Anda dapat menggunakan tiga metode idetifikasi untuk mengesahkan *buddy* **Pidgin** Anda; Anda dapat menggunakan 1). Kode kata atau kalimat rahasia yang sudah dirancang sebelumnya, 2). Membuat pertanyaan yang jawabannya hanya diketahui Anda berdua atau 3) Secara manual mem-verifikasi *fingerprints* kunci rahasia Anda menggunakan metode komunikasi yang lain.

### Metode Kode Kata atau Kalimat Rahasia ###

Anda dapat mengatur kode berupa kalimat atau kata sebelumnya, dengan bertemu dengan buddy Anda atau menggunakan media komunikasi lain (seperti telepon atau **Skype** atau SMS). Ketika Anda telah mengetik kode yang sama, sesi Anda akan disahkan.

**Catatan**: Fitur yang mengenali kode rahasia **OTR** sangatlah sensitif. Ini berarti, fitur ini dapat mengenali perbedaan antara huruf kapital (A,B,C) dan huruf kecil. Ingatlah hal ini ketika sedang menciptakan kode rahasia!

**Langkah 1. Klik** tombol *OTR* di di jendela *chat*, lalu **pilih** item *Authenticate Buddy* seperti berikut:

![](/sbox/screen/pidgin-en/52.png)

*Gambar 9: Menu Unverified muncul dengan item Authenticate buddy terpilih*

Ini akan mengaktifkan jendela *Authenticate Buddy*, meminta Anda untuk memilih metode pengesahan.

**Langkah 2. Klik** ![](/sbox/screen/pidgin-en/53.png lalu **pilih** *Shared Secret* seperti berikut:

![](/sbox/screen/pidgin-en/54.png)

*Gambar 10: Layar Autheticate Buddy dengan daftar drop-down ditunjukkan*

**Langkah 3. Masukkan** kode rahasia seperti berikut:

![](/sbox/screen/pidgin-en/55.png)

Gambar 11: Layar Shared Secret*

**Langkah 4. Klik** ![](/sbox/screen/pidgin-en/56.png) untuk mengaktifkan layar berikut:

![](/sbox/screen/pidgin-en/58.png)

*Gambar 12: Jendela Authenticate Buddy untuk koresponden fiksi*

**Catatan**: *Pada tahap ini, buddy Anda akan melihat jendela yang sama seperti Gambar 13 dan harus memasukkan kode yang sama. Apabila cocok, sesi Anda akan disahkan*.

![](/sbox/screen/pidgin-en/57.png)

*Gambar 13: Jendela Authenticate Buddy untuk koresponden fiksi*

Setelah sesi disahkan, tombol *OTR* akan berubah menjadi ![](/sbox/screen/pidgin-en/51.png). Sesi Anda sekarang aman dan Anda dapat yakin bahwa Anda berbicara dengan *buddy* Anda.

### Metode Pertanyaan dan Jawaban ###

Satu lagi metode pengesahan satu sama lain ialah metode pertanyaan dan jawaban. Ciptakan sebuah pertanyaan dan jawaban. Setelah membaca pertanyaan, *buddy* Anda harus menjawab pertanyaan dengan *persis*, apabila jawabannya cocok dengan jawaban Anda, identitas Anda berdua akan langsung disahkan.

**Langkah 1. Klik** menu *OTR* di jendela pesan aktif untuk mengaktifkan menu pop-up yang berhubungan, lalu **pilih** item *Authenticate Buddy* (silahkan merujuk pada *Gambar 9*).

![](/sbox/screen/pidgin-en/59.png)

*Gambar 14: Jendela Pidgin Chat menunjukkan ikon OTR*

Jendela *Authenticate Buddy* akan muncul, meminta Anda memilih metode pengesahan.
  
**Langkah 2. Klik** menu lalu **pilih** item *Question and Answer* seperti berikut:

![](/sbox/screen/pidgin-en/60.png)

*Gambar 15: Layar Authenticate Buddy*

**Langkah 3. Masukkan** pertanyaan dan jawabannya. Pertanyaan ini akan dikirim ke *buddy* Anda.

![](/sbox/screen/pidgin-en/61.png)

*Gambar 16: Layar Questions and Answer*

Apabila jawaban *buddy* cocok dengan jawaban Anda, berarti Anda dan *buddy* Anda telah saling melakukan verifikasi, dan identitas kedua pihak adalah benar-benar seperti yang mereka akui!

Ketika sesi percakapan telah disahkan, tombol **OTR** akan berubah menjadi ![](/sbox/screen/pidgin-en/51.png). Sesi Anda sekarang aman dan Anda dapat yakin dengan identitas teman *chat* Anda.

Perhatikan, ketika Anda melakukan **Select > Buddy List > Tools > Plugins > Off the Record Messaging > configure Plugin**, tab **Known fingerpints (fingerprints/sidik jari dikenali)* sekarang ditunjukkan di akun *buddy* Anda, dan sebuah pesan bahwa identitas mereka sudah diverifikasi.

![](/sbox/screen/pidgin-en/62.png)

*Gambar 17: Layar Off-the Record menunjukkan tab Known Fingerprints*

Selamat! Anda sekarang dapat melakukan percakapan secara rahasia. Ketika Anda dan buddy Anda akan melakukan percakapan lagi (dengan komputer yang sama), Anda dapat melewati langkah kesatu dan kedua, diatas. Anda hanya harus melakukan permintaan untuk koneksi yang aman dan buddy Anda hanya harus menerimanya/menyetujuinya.

