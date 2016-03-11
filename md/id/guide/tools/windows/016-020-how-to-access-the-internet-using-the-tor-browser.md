

---

lang: id
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to access the Internet using the Tor Browser

---

Daftar isi laman ini:

- [**3.0 Mengenai Penggunaan Jaringan Tor**](#3.0)
- [**3.1 Cara Terhubung dengan Jaringan Tor**](#3.1)
- [**3.2 Cara Manual Melakukan Verifikasi Koneksi terhadap Tor**](#3.2)
- [**3.3 Cara Merambah Internet Menggunakan Tor**](#3.3)
- [**3.3.1 Cara Konfigurasi Mozilla Firefox untuk penggunaan dengan Tor**](#3.3.1)
- [**3.3.2 Cara Konfigurasi Internet Explorer untuk penggunaan dengan Tor**](#3.3.2)

-------

<a name="3.0"></a>
## 3.0 Mengenai Penggunaan Jaringan Tor ##

Untuk memulai menjelajah Internet tanpa dikenali, Anda harus mengaktifkan program **Tor Browser**. Pertama, hal tersebut akan menghubungkan sistem Anda dengan jaringan **Tor**. Setelah komputer Anda berhasil terhubung dengan jaringan **Tor**, **Tor Browser** akan menjalankan secara terpisah **Firefox Portable** yang dimuat dalam **Tor Browser Bundle** secara otomatis.

**Catatan**: Akan ada perbandingan terbalik antara anonimitas dengan kecepatan. Menggunakan penghilangan identitas akan mengakibatkan berkurangnya kecepatan perambah dibandingkan Anda menggunakan perambah biasa. **Tor** memantulkan trafik Anda kepada komputer sukarelawan di berbagai penjuru dunia untuk menjaga keamanan dan privasi Anda.


<a name="3.1"></a>
## 3.1 Cara Terhubung dengan Jaringan Tor ##

Untuk bisa terhubung dengan jaringan **Tor**, lakukan langkah-langkah ini:

**Langkah 1**. **Cari Tor Browser** di folder tempat Anda menyimpannya, kemudian **klik dua kali** ![](/sbox/screen/tor-en/30.png) untuk mengaktifkan tampilan di bawah ini:

![](/sbox/screen/tor-id/10.png)

*Gambar 1: Vidalia Control Panel sedang mecoba terhubung dengan jaringan Tor*


Sementara *Vidalia Control Panel* berusaha terhubung dengan jaringan **Tor**, lambang bawang kuning akan muncul pada *tray system* Anda sperti ini: ![](/sbox/screen/tor-id/11.png). Saat koneksi Anda telah berhasil didirikan dengan jaringan **Tor**, maka warna bawang tersebut berubah menjadi hijau: ![](/sbox/screen/tor-id/11b.png)

**Catatan**: untuk belajar menggunakan *Vidalia Control Panel* secara efektif, silahkan merujuk pada halaman [**Cara Menggunakan Panel Kontrol Vidalia**](/id/Tor_panel_kontrol_vidalia).

Beberapa saat kemudian, **Tor Browser** akan mengaktifkan **Mozilla Firefox**, menunjukan tampilan seperti di bawah ini:

![](/sbox/screen/tor-id/12.png)

*Gambar 2: Mozilla Firefox menampilkan “Are you using Tor?”*

Setiap kali Anda menjalankan program **Tor Browser**, hal itu akan mengaktifkan *Vidalia Control Panel* secara bersamaan (*gambar 1*) dan [**https://check.torproject.org/**](https://check.torproject.org/) (*gambar 2*).  Pengaya **Torbutton** akan muncul pada bagian pojok bawah kanan seperti ini: ![](/sbox/screen/tor-id/13.png) 

**Catatan**: Jika Anda sudah menjalankan **Mozilla Firefox** saat menjalankan **Tor Browser**, **Torbutton** akan dinonaktifkan dengan tampilan seperti berikut: ![](/sbox/screen/tor-id/14.png)
 
**Torbutton** digunakan untuk mengatur **Firefox** agar terhubung dengan benar pada jaringan **Tor**. Cukup **klik** **Torbutton** untuk mengubah statusnya menjadi aktif atau non-aktif.

Bagaimanapun juga, jika Anda *tidak* terhubung pada jaringan **Tor**, **Torbutton** akan dengan sendirinya non-aktif, dan tampilan seperti di bawah akan muncul:

![](/sbox/screen/tor-id/15.png)

*Gambar 3: Mozilla Firefox menampilkan “Sorry. You are not using Tor tab*

Jika Anda melihat pada *Gambar 3*, **Torbutton** yang non-aktif, atau halaman web yang kosong, silahkan merujuk pada [**4.0 Cara Mengatasi Masalah Umum Pada Tor**](/id/Tor_Troubleshooting)

<a name="3.2"></a>
## 3.2 Cara Manual Melakukan Verifikasi Koneksi terhadap Tor ##

Untuk secara manual memastikan koneksi terhadap jaringan **Tor**, lakukan langkah di bawah ini:

**Langkah 1**. **Buka** laman [**https://check.torproject.org/**](https://check.torproject.org/) untuk memastikan apakah Anda terhubung dengan jaringan **Tor** atau tidak.

Jika browser Anda terhubung dengan Internet menggunakan jaringan **Tor**, situs yang diblokir di Negara Anda sangat mungkin untuk diakses sekarang, dan kegiatan online Anda tetap terjaga privasi dan keamanannya. Anda juga akan menemukan situs seperti **www.google.com** menganggap Anda berada di Negara yang berbeda. Hal tersebut wajar jika Anda menggunakan **Tor**.


<a name="3.3"></a>
## 3.3 Cara Merambah Internet Menggunakan Tor ##

Walaupun Anda dapat memulai menjelajah situs web langsung menggunakan **Firefox** dengan jaringan **Tor**, kami sarankan Anda membaca sesi berikut mengenai pengaturan **Firefox** untuk mengoptimalkan keamanan dan privasi online Anda

<a name="3.3.1"></a>
### 3.3.1 Cara Konfigurasi Mozilla Firefox untuk penggunaan dengan Tor ###

**Torbutton** adalah pengaya atau ekstensi untuk **Mozilla Firefox**, sebuah program kecil yang dirancang untuk melindungi identitas Anda dan keamanan kegiatan online Anda dengan memblokir beberapa kelemahan yang ada pada **Mozilla Firefox**.

**Penting**: Situs berbahaya atau bahkan server **Tor** *masih* dapat membocorkan informasi mengenai lokasi dan aktifitas online Anda, bahkan saat Anda sedang menggunakan **Tor**. Untungnya, konfigurasi asal dari **Torbutton** relative aman; bagaimanapun juga, kami sarankan Anda untuk mengubah pengaturan berikut untuk mengoptimalkan privasi dan keamanan kegiatan online Anda. 

**Catatan**: Pengguna **Ahli** dengan pemahaman yang baik tentang keamanan browser dapat menyempurnakan pengaturan ini.

Jendela *Torbutton Preferences* mempunyai 3 tabs yang memungkinkan Anda menspesifiksi pilihan berbeda:

- Tab **Proxy Settings**  
- Tab **Security Settings**
- Tab **Display Settings** 

Jendela *Torbutton Preferences* dapat diakses terlepas apakah **Torbutton** aktif atau tidak. Untuk memunculkannya, lakukan langkah-langkah di bawah ini:

**Langkah 1**. **Klik-Kanan** untuk mengaktifkan menu **Torbutton** seperti berikut:

![](/sbox/screen/tor-id/16.png)

*Gambar 4: Menu Torbutton*

**Langkah 2**. **Pilih** item *Preferences...* untuk mengaktifkan layar berikut: 

![](/sbox/screen/tor-id/17.png)

*Gambar 5: Jendela Torbutton Preferences - tab Proxy Setting*

- Tab **Proxy Settings**
 
Tab *Proxy Setting* mengatur bagaimana **Firefox** mengakses Internet saat **Torbutton** menyala. Anda tidak perlu mengubah apapun pada tab ini. 

- Tab **Security Settings** 

Tab *Security Setting* dirancang untuk pengguna **berpengalaman** atau **ahli** dengan pengetahuan mendalam tentang keamanan browser dan Internet. Pengaturan awal pada tab ini menawarkan tingkat keamanan dan privasi yang cukup tinggi untuk pengguna pada umumnya. *Security Setting* ini memungkinkan Anda mengkonfigurasi **Torbutton** mengatur riwayat perambah, *cache*, kukis dan fitur lain pada **Firefox**.

![](/sbox/screen/tor-id/18.png)

*Gambar 6: Tab Security Settings*

Opsi *Disable plugins during Tor usage* merupakan hal yang harus Anda aktifkan diantara pengaturan keamanan, tapi hanya *sementara*. Untuk menampilkan konten video saat menggunakan **Tor** – termasuk [**Dailymotion**](http://www.dailymotion.com/), [**The Hub**](http://hub.witness.org/) dan [**YouTube**](http://www.youtube.com)-  Anda harus **mematikan** opsi *Disable plugins during Tor usage*.

**Catatan**: Anda hanya dianjurkan mengaktifkan plugin dari situs terpercaya, dan Anda harus mengembalikan tab *Security Setting* untuk **mengaktifkan** opsi *Disable plugins during Tor usage* setelah Anda selesai mengunjungi situs tersebut.

Untuk informasi lebih lanjut mengenai fungsi yang spesifik untuk tiap opsi dalam tab *Security Setting*, silahkan merujuk pada [**Torbutton**](https://www.torproject.org/torbutton/).

- Tab **Display Settings** tab

Tab *Display Setting* memungkinkan Anda untuk menampilkan bar status **Torbutton** pada **Firefox**, sebagaimanan ![](/sbox/screen/tor-id/19.png) atau ![](/sbox/screen/tor-id/20.png), atau ![](/sbox/screen/tor-id/21.png) atau ![](/sbox/screen/tor-id/22.png). Semua akan berfungsi apapun pilihan Anda.

![](/sbox/screen/tor-id/23.png)

*Gambar 7: Tab Display Settings*

**Tip**: Saat Anda telah selesai browsing, yakinkan bahwa data sementara, *cache* dan kukis Internet telah dihapus. Hal ini dapat dilakukan pada **Firefox** dengan **memilih *Alat > Bersihkan Riwayat Terakhir...*, centang semua opsi** yang ada pada layar dan **tekan** tombol *Bersihkan sekarang*. Untuk informasi lebih lanjut, silahkan merujuk pada **Petunjuk yang membantu** bab [**Mozilla Firefox**](/id/firefox_instal).

Untuk informasi lebih lanjut mengenai **Torbutton**, silahkan merujuk pada [**Torbutton FAQ**](https://www.torproject.org/torbutton/torbutton-faq.html.en).

<a name="3.3.2"></a>
### 3.3.2 Cara Konfigurasi Internet Explorer untuk penggunaan dengan Tor ###

**Catatan**: Walaupun **Tor** dirancang untuk digunakan dengan semua browser, **Firefox** dan **Tor** adalah kombinasi ideal untuk menghindari deteksi atau ditemukan oleh pihak yang berbahaya. **Internet Explorer** sebaiknya dijadikan pilihan terakhir. 

Bagaimana pun juga, jika Anda dalam keadaan yang mengharuskan Anda menggunakan **Internet Explorer**, lakukan langkah-langkah berikut:

**Langkah 1**. **Buka** perambah **Internet Explorer**. 

**Langkah 2**. **Pilih Tools > Internet Options** untuk mengaktifkan layar *Internet Options*. 

**Langkah 3**. **Klik** tab *Connections* untuk mengaktifkan layar yang ditampilkan pada *Gambar 8* di bawah ini: 

![](/sbox/screen/tor-id/24.png)

*Gambar 8: Tab Connection pada layar Internet Option*

**Langkah 4**. **Klik** ![](/sbox/screen/tor-id/25.png) untuk mengaktifkan layar *Local Area Network (LAN) Settings* seperti berikut: 

![](/sbox/screen/tor-id/26.png)

*Gambar 9: Pengaturan Local Area Network (LAN).*

**Langkah 5**. **Centang** pilihan *Use a proxy server...* seperti yang ditunjukan *Gambar 9*, dan kemudian **klik** ![](/sbox/screen/tor-id/27.png) untuk mengaktifkan layar *Proxy Settings*. 

**Langkah 6**. **Lengkapi** kolom pada *proxy settings* seperti yang ditunjukan di bawah ini: 

![](/sbox/screen/tor-id/28.png)

*Gambar 10: Contoh Proxy Settings yang telah diisi*

**Langkah 7**. **Klik** ![](/sbox/screen/tor-id/ok.png) pada setiap tampilan pengaturan untuk keluar dari jendela **Internet Option** dan kembali pada **Internet Explorer**.

**Catatan**: Anda perlu mengulang **langkah 1 sampai 4** untuk mematikan Tor. Pada **langkah 5**, Anda harus **mematikan** opsi *Use Proxy server...*  

**Tip**: Anda harus menghapus data sementara, cache, kukis dan riwayat dari browser atau perambah Anda setelah menyelesaikan kegiatan online Anda dengan langkah berikut:

**Langkah 1**. **Pilih Tools > Internet Options** untuk menampilkan Tab *General* seperti:

![](/sbox/screen/tor-id/29.png)

*Gambar 11: Tab Internet Explorer General*

**Langkah 2**. **Klik** ![](/sbox/screen/tor-id/30.png) pada bagian *Temporary Internet files*, konfirmasi *Delete Cookies* akan muncul seperti dibawah ini:

![](/sbox/screen/tor-id/31.png)

*Gambar 12: Konfirmasi Delete Cookies*

**Langkah 3**. **Klik** ![](/sbox/screen/tor-id/ok.png) untuk menghapus kukis internet sementara.

**Langkah 4**. **Klik** ![](/sbox/screen/tor-id/32.png) untuk memunculkan kotak konfirmasi *Delete Files*, dan kemudian **klik** ![](/sbox/screen/tor-id/ok.png)untuk menghapus data sementara. 

**Langkah 5**. **Klik** ![](/sbox/screen/tor-id/33.png), kotak konfirmasi *Internet Options* akan muncul, **klik** ![](/sbox/screen/tor-id/34.png) dan kemudian **klik** ![](/sbox/screen/tor-id/ok.png). 

**Catatan:** Untuk mengakses jaringan **Tor** menggunakan **Internet Explorer** Anda perlu memastikan **Tor Browser** tetap berjalan dengan **Vidalia** yang terhubung pada jaringan **Tor**.

