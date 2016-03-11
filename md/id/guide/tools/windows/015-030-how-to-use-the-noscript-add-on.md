

---

lang: id
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: How to Use the NoScript Add On

---

Daftar isi laman ini:

- [**4.0 Mengenai NoScript**](#4.0)
- [**4.1 Cara Menggunakan NoScript**](#4.1)
- [**4.2 Mengenai Serangan Clickjacking dan Script Cross-site (XXS)**](#4.2)

-------

<a name="4.0"></a>
## 4.0 Mengenai NoScript ##

![](/sites/securitybkp.ngoinabox.org/files/u9/noscript.png)

**NoScript** merupakan pengaya khusus pada **Mozilla Firefox** yang dapat membantu Anda melindungi komputer Anda dari situs web berbahaya. **NoScript** menggunakan daftar putih sebagai panduan menentukan situs yang dapat diterima, aman dan terpercaya (seperti Internet perbankan atau jurnal online). Situs lainnya dianggap berpotensi bahaya dan dibatasi kerja fungsinya, sampai Anda menentukan bahwa isi dari situs tersebut tidak membahayakan; pada titik ini, Anda dapat memasukkannya ke dalam daftar putih.

**NoScript** akan secara otomatis memblokir munculnya *banner*, iklan yang timbul pada jendela baru, **Script Java** dan kode **Java** yang terkait, begitu juga dengan atribut sebuah situs yang dinilai berpotensi membahayakan. **NoScript** pada dasarnya tidak dapat membedakan antara konten yang berbahaya dan konten yang dibutuhkan untuk menampilkan sebuah situs sebagaimana mestinya. Keputusan ada di tangan Anda sebagai penggunauntuk membuat pengecualian terhadap konten yang Anda anggap aman.

<a name="4.1"></a>
## 4.1 Cara Menggunakan NoScript ##

Sebelum menggunakan **NoScript**,  **Penting** untuk memastikan bahwa **NoScript** telah terpasang dengan benar dengan cara **memilih Alat > Pengaya** untuk memunculkan jendela *pengaya* guna memastikan bahwa pemasangan telah dilakukan.

**Tip**: Walau pada awalnya **NoScript** seakan membuat frustasi dalam pemakaiannya, (karena situs yang biasa Anda kunjungi tidak menampilkan laman sebagaimana mestinya), Anda akan merasa diuntungkan dengan segera karena fitur pemblokiran objek secara otomatis. Fitur ini akan membatasi iklan yang menjengkelkan, pesan *pop-up* dan kode berbahaya yang ada atau disusupkan dalam halaman web.

**NoScript** akan berjalan tanpa Anda sadari sampai ia mendeteksi kehadiran **Script Java**, **Adobe Flash** atau konten lain yang menyerupai *script*. Pada saat itu **NoScript** akan memblokir konten dan akan muncul status bar pada dasar jendela **Firefox** seperti di bawah ini:

![](/sbox/screen/firefox-id/31.png)

*Gambar 1: Status bar NoScript*

Status Bar **NoScript** menampilkan informasi mengenai objek (contohnya, iklan dan pesan *pop-up*) dan script yang sedang dicegah untuk berjalan dalam sistem Anda. Gambar berikut ini adalah contoh utama saat **NoScript** bekerja: Pada *Gambar 2*, **NoScript** telah berhasil memblokir iklan yang ditampilkan dengan **Adobe Flash** pada situs komersil.

![](/sbox/screen/firefox-id/32.png)

*Gambar 2: Contoh Noscript yang memblokir iklan pada situs komersil*

Pada *Gambar 3*, situs Twitter memperingatkan Anda bahwa Anda harus menghidupkan **JavaScript** (setidaknya sementara) untuk melihat laman situs tersebut.

![](/sbox/screen/firefox-id/33.png)

*Gambar 3: Situs Twitter yang meminta Script Java dihidupkan*

Dikarenakan **NoScript** tidak dapat membedakan antara kode berbahaya dan yang benar, fitur dan fungsi kunci tertentu (seperti toolbar) dapat saja hilang. Beberapa halaman web menampilkan konten, termasuk konten yang menyerupai *script*, dari beberapa halaman web. Contohnya seperti situs **www.youtube.com** yang memiliki tiga sumber script:

![](/sbox/screen/firefox-id/34.png)

*Gambar 4: Opsi Statusbar Noscript*

Untuk menghentikan pemblokiran pada situasi ini, mulai dengan **memilih** opsi *Ijinkan Sementara [alamat situs]* (pada contoh ini, opsi tersebut akan menjadi *Ijinkan sementara youtube.com*). Bagaimanapun juga, jika cara ini tidak membuat Anda dapat melihat konten halaman web, Anda perlu menentukan, melalui beberapa kali proses mencoba, beberapa situs web yang Anda akan izinkan dalam rangka memungkinkan Anda untuk melihat dan membuka konten pilihan Anda. Untuk **YouTube**, Anda hanya perlu **memilih** *Ijinkan Sementara Youtube.com* dan *Ijinkan sementara ytimg.com*, agar **Youtube** dapat bekerja.

**Peringatan!**: Dalam situasi seperti apapun Anda tidak disarankan melakukan opsi ini: *Ijinkan Semua Naskah (berbahaya)*. Sebisa mungkin, hindari untuk memilih opsi *Bolehkan semua laman ini*. Pada suatu waktu, Anda perlu mengizinkan semua script; pada situasi ini, pastikan Anda hanya melakukan hal ini pada situs yang Anda percayai dan aman dan hanya bersifat sementara – sampai akhir sesi online Anda. Hanya *satu* injeksi kode saja yang dibutuhkan untuk menembus keamanan dan privasi Internet Anda.

<a name="4.2"></a>
## 4.2 Mengenai Serangan Clickjacking dan Script Cross-site (XXS) ##

**NoScript** dapat diatur untuk melindungi sistem Anda melawan *script Crsoss-site* dan serangan *ClickJacking*. *Script cross-site* merupakan kelemahan dari komputer dimana memungkinkan peretas atau penyelundup lainnya melakukan injeksi kode berbahaya ke dalam situs web yang ada. Singkatnya, serangan *ClickJacking* seperti pada saat kita menekan tombol yang muncul karena aksi tertentu, kode tertentu yang diikutkan dalam tombol tersebut ikut tereksekusi. Kedua serangan tersebut dapat terjadi tanpa Anda ketahui kecuali Anda menggunakan **NoScript**.

Setiap kali serangan *clickjacking* sedang dilakukan, jendela seperti di bawah akan muncul:

![](/sbox/screen/firefox-en/41.png)

*Gambar 5: Contoh jendela Potential Clickjacking / UI Redressing Attempt*

Ikuti instruksi yang ditampilkan pada jendela tersebut untuk menetralisir serangan *clickjacking* dan **klik** ![](/sbox/screen/firefox-en/15.png).

