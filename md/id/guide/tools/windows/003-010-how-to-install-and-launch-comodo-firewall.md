

---

lang: id
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: How to Install and Launch COMODO Firewall 

---

Bagian-bagian dari halaman ini:

- [**2.0 Selintas tentang pemasangan COMODO Firewall**](#2.0)
- [**2.1 Cara mematikan Firewall Windows**](#2.1)
- [**2.2 Cara menginstal  COMODO Firewall**](#2.2)

-------

<a name="2.0"></a>
## 2.0 Selintas tentang pemasangan COMODO Firewall ##

Memasang **COMODO Firewall** relatif mudah dan cepat, dan terbagi dalam dua langkah: pertama dengan mematikan ***firewall Windows*** secara manual, dan yang kedua dengan menginstal  **COMODO Firewall**.

Idealnya, Anda hanya menggunakan satu program *firewall* untuk sistem komputer Anda.  Apabila Anda menggunakan *firewall*  lain di komputer Anda, matikanlah dulu sebelum Anda memasang **COMODO Firewall**  untuk menghidari kemungkinan adanya konflik antar perangkat lunak yang sejenis .


<a name="2.1"></a>
## 2.1 Cara mematikan Firewall Windows ##

Untuk mematikan ***Firewall Windows***, silahkan ikuti langkah ini:
 
**Langkah 1. Pilih start > Control Panel > Windows Firewall** untuk memunculkan layar **Windows Firewall**.

**Langkah 2.  Centang** pilihan *Off (not recommended)* untuk mematikan **Windows Firewall** seperti yang ditunjukkan *Gambar 1* di bawah ini:

![](/sbox/screen/comodo-en/01.png)

*Gambar 1. Windows Firewall yang sudah dimatikan*

**Langkah 3:  Klik** ![](/sbox/screen/comodo-en/02.png) untuk mematikan *firewall Windows*. 

<a name="2.2"></a>
## 2.2 Cara menginstal  COMODO Firewall ##

**Catatan: COMODO Firewall**  tidak dengan otomatis mematikan versi lama dari softwarenya. Anda harus mematikannya secara manual sebelum menginstal  versi yang terbaru.

Lakukan langkah-langkah berikut untuk memulai instalasi  **COMODO Firewall** :

**Langkah 1. Klik dua kali *(double click)*** ![](/sbox/screen/comodo-en/03.png) untuk memulai proses instalasi. Box dialog *Open File – Security Warning* akan muncul. Selanjutnya , **klik** ![](/sbox/screen/comodo-en/04.png) untuk memunculkan box dialog  konfirmasi seperti ini:

![](/sbox/screen/comodo-en/05.png)

*Gambar 2: Dialog box konfirmasi bahasa yang dipilih*

**Langkah 2. Klik** ![](/sbox/screen/comodo-en/06.png) untuk mengaktifkan *End User License Agreement*. Silahkan baca *End User License Agreement* sebelum melanjutkan proses instalasi, lalu **klik** ![](/sbox/screen/comodo-en/07.png) untuk mendapatkan layar *Free registration*.

**Langkah 3: Jangan** masukkan alamat email Anda ke dalam kotak teks *Enter your email address (optional)*; **klik** saja ![](/sbox/screen/comodo-en/09.png) untuk mengaktifkan layar *Extracting the Packages*.
  
Setelah proses ekstrak telah selesai, *Firewall Setup Destination Folder* akan muncul.

**Langkah 4: Klik** ![](/sbox/screen/comodo-en/09.png) untuk menerima tujuan folder yang telah ditentukan dan menyalakan layar *Firewall security level selection*, lalu centang  pilihan *Firewall Only* seperti berikut:

![](/sbox/screen/comodo-en/11.png)

*Gambar 3: Layar Firewall Security level selection*

**Definisi dari pilihan tingkat keamanan *firewall (Firewall Security level)***

Setiap pilihan tingkat keamanan *firewall* memberikan pelayanan dengan tingkat yang berbeda. Setiap pilihan mempunyai jenis proteksi dengan tingkat kerumitan penggunaan yang berbeda, serta jumlah peringatan keamanan yang akan diterima. Berikut adalah deskripsi singkat dari masing-masing tingkat: 

**Firewall Only**: Pilihan ini akan menjalankan **COMODO Firewall** tanpa fitur Defense+. Ia akan mengidentifikasi aplikasi populer  yang realtif aman seperti web browser dan email klien, mengurangi jumlah peringatan yang akan Anda terima. Mode ini juga memberikan penjelasan umum kenapa layar peringatan tersebut muncul. Tindakan-tindakan yang harus dilakukan tergolong mudah. 

**Firewall with Optimum Proactive Defense**: pilihan ini menggabungkan proteksi solid dari modul *Firewall Only* dengan fitur *Defense+*. *Defense+* melakukan proteksi aktif terhadap *malware* yang didesain untuk menghindari *firewall-firewall* yang berbeda. *COMODO Firewall Alerts* memberikan penjelasan lebih dalam kenapa *firewall* memblokir sebuah aplikasi atau perintah dan Anda mempunyai pilihan untuk setengah mengisolasi  atau memasukkan program atau file yang mencurigakan ke dalam *‘sandbox’*.

**Firewall with Maximum Proactive Defense**: pilihan ini menggabungkan keamanan *Firewall with Optimum Proactive Defense* dengan proteksi ‘anti-bocor’ melawan ancaman keamanan yang lebih ‘pasif’, contohnya detail tentang port terbuka di komputer Anda yang dikirim ke internet. Fitur  *sandbox* bekerja dengan otomatis sepenuhnya di pilihan ini. 

**Langkah 6. Klik** ![](/sbox/screen/comodo-en/09.png) untuk mengaktifkan layar *COMODO Secure DNS Configuration*, dan memberikan pilihan *I would like to use COMODO Secure DNS Servers* seperti berikut:

![](/sbox/screen/comodo-en/12.png)

*Gambar 4: layar COMODO Secure DNS Configuration*

**Penting**: walaupun tidak ada server ***Domain Name Systems (DNS)*** yang betul-betul aman, kelebihan menggunakan server **COMODO Secure DNS** melebihi kekurangannya. Ia menawarkan proteksi tambahan dari *pharming* dan *phishing*, yang merupakan metode populer  untuk membajak atau menghubungkan komputer Anda ke website yang berbahaya. Server **COMODO Secure DNS** juga melindungi Anda dari interfensi pemerintah, yang sangat mudah untuk diatur ketika proses instalasi, dan juga memfasilitasi akses yang lebih aman ke websites yang terdaftar di **COMODO**. Contohnya, kesalahan mengetik URL akan mengaktifkan pesan dari server **COMODO Secure DNS** seperti dibawah ini:

![](/sbox/screen/comodo-en/126.png)

*Gambar 5: Contoh notifikasi dari server COMODO Secure DNS*

**Langkah 7. Klik**  ![](/sbox/screen/comodo-en/09.png) untuk mengaktifkan layar *Ready to Install COMODO Firewall* lalu **klik**  ![](/sbox/screen/comodo-en/13.png) untuk memulai proses penginstalan , dan mendapatkan layar *Installing COMODO Firewall*. Setelah proses pemasangan berhasi, layar *Completed the COMODO Firewall Setup Wizard* akan muncul.

**Langkah 8. Klik**![](/sbox/screen/comodo-en/14.png) untuk mengaktifkan layar konfirmasi *Done*, lalu **klik** ![](/sbox/screen/comodo-en/14.png) untuk mengaktifasi dialog box konfirmasi seperti berikut:

![](/sbox/screen/comodo-en/15.png)

*Gambar 6: dialog box konfirmasi Firewall Installer*

**Langkah 9. Klik** ![](/sbox/screen/comodo-en/16.png) untuk *restart* komputer Anda dan menyelesaikan instalasi  **COMODO Firewall**.

Setelah computer menyala kembali, layar *New Private Network Detected!* akan muncul seperti berikut: 

![](/sbox/screen/comodo-en/17.png)

*Gambar 7: layar COMODO Firewall New Private Network Detected!*

**Tips**: apabila Anda bekerja di lingkungan LAN (*Local Area Network*), silahkan centang  pilihan  *I would like to be fully accessible to other PCs in this network* (saya ingin memiliki akses penuh dengan komputer lain dalam jaringan ini) untuk membolehkan file/folder/printer dan/atau koneksi berbagi Internet.

**Langkah 10. Ketik** sebuah nama di teks field *Give a name to this network for your network* (beri nama pada jaringan Anda) atau silahkan terima nama yang telah diatur seperti di *Gambar 7* diatas. Jangan pilih pilihan yang terdaftar di langkah  2 – *Decide if your want to trust the other PCs in this network* (Tentukan jika Anda ingin mempercayai komputer lain dalam jaringan ini), lalu **klik** ![](/sbox/screen/comodo-en/06.png) untuk menyelesaikan instalasi. 

Ikon desktop **COMODO Firewall**  dan ikon konektivitas **COMODO Firewall** akan muncul bersama  dengan *Gambar 7*. Sebelum menghubungkan komputer Anda ke internet, ikon konektivitas akan muncul di *System Tray* seperti ini:

![](/sbox/screen/comodo-en/18.png)

*Gambar 8: Ikon konektivitas COMODO Firewall dikelilingi garis hitam  di System Tray*

Tersambung ke internet (*online*) atau membuka  program yang terhubung dengan internet  (contoh: web browser) akan memunculkan beberapa panah oranye yang menghadap ke bawah dan/atau panah hijau yang menghadap keatas, yang mengindikasikan permintaan koneksi internet ke dalam maupun keluar, seperti gambar di bawah: 

![](/sbox/screen/comodo-en/19.png)

*Gambar 9:Ikon konektivitas COMODO Firewall aktif*

Setelah **COMODO Firewall** telah berjalan beberapa waktu, pesan pop-up akan muncul dari *COMODO Message Center* seperti gambar berikut:

![](/sbox/screen/comodo-en/20.png)

*Gambar 10: Layar pop-up COMODO Message Center*

**Catatan: klik** *hyperlink Learn More* untuk diarahkan ke forum ***COMODO** community-based help*.

**Tips: klik-kanan** ikon konektivitas **COMODO Firewall** di *System Tray* (seperti *Gambar 8*) untuk mengaktifkan menu pop-up berikut, dan juga sub-menu yang berhubungan:

![](/sbox/screen/comodo-en/127.png)

*Gambar 11: Ikon konfigurasi menu dan sub-menu konektivitas*

Ikon konektivitas membolehkan Anda mengganti produk **COMODO Firewall** yang Anda gunakan. **Memilih** item *Configuration* akan mengaktifkan sub-menu ‘*Manage My Configurations*’ dimana Anda bisa memilih *COMODO Proactive Security* atau *COMODO – Internet Security* untuk mengaktifkan  fitur *sandbox*. 

Sebagai tambahan, tiap produk mempunyai tingkat keamanan yang disesuaikan dari menu pop-up ikon konektivitas sebagai berikut; tingakat keamanan ini dijelaskan lebih jauh di bagian **4.1 Jendela pengaturan aktifitas Firewall** dan 4.2 Jedela pengaturan Defense+**.

![](/sbox/screen/comodo-en/128.png)

*Gambar 12: ikon sub-menu konektivitas tingkat keamanan (Firewall Security Level)*


