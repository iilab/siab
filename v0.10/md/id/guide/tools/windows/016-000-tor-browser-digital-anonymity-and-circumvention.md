

---

lang: id
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 016
title: Tor Browser - Digital Anonymity and Circumvention

---

**Situs Resmi**
			
[**www.torproject.org**](https://www.torproject.org/)
			
**Sistem operasi yang di perlukan**

- Semua Versi **Windows**
- Koneksi Internet
- Cocok dengan perambah mayoritas terutama **Mozilla Firefox**.		

**Versi yang digunakan dalam panduan ini**

- Tor Browser: 2.2.35-8

**Lisensi** 

- Gratis dan bisa digunakan siapa saja

**Petunjuk yang perlu dibaca** 

- How-to Booklet Chapter [**8. Bagaimana Cara menjadi tetap anonimus dan melewati sensor Internet**](/id/chapter-8) 

**Level**: 1: Pemula, 2: Umum, **3: Menengah, 4: Berpengalaman**, 5: Ahli

**Waktu yang diperlukan untuk menggunakan alat ini**: 20 - 30 Menit

**Apa yang akan Anda dapatkan**: 

- Kemampuan untuk menyembunyikan identitas digital Anda dari situs yang dikunjungi
- Kemampuan untuk menyembunyikan tujuan online Anda dari **Penyedia jasa koneksi Internet (ISPs)** dan sistem pemantauan lain
- Kemampuan untuk melewati sensor Internet dan aturan penyaringan


**GNU Linux, Mac OS dan Program Microsoft Windows lainnya yang kompatibel**:

**Tor** *anonymity network client* juga tersedia untuk GNU Linux, Sistem Operasi Mac, Microsoft Windows dan sistem operasi lain. **Tor** merupakan alat yang paling direkomendasikan dan diujicoba dengan ketat untuk menjaga kegiatan Internet Anda tetap rahasia dan aman. Tapi kami juga mencoba menawarkan beberapa solusi lain:

* [**Hotspot Shield**](http://hotspotshield.com/) merupakan **Virtual Private Network** (**VPN**) yang gratis untuk **Microsoft Windows**.
* [**Dynaweb FreeGate**](http://www.dit-inc.us/freegate) merupakan alat proxy untuk **Microsoft Windows**.
* [**UltraReach UltraSurf**](http://www.ultrareach.com/) merupakan alat proxy untuk **Microsoft Windows**.
* [**Your Freedom**](http://www.your-freedom.net/) proxy komersil yang juga menawarkan layanan gratis (walaupun lebih lambat) . Tersedia untuk **Linux**, **Mac OS** dan **Microsoft Windows**.
* [**Psiphon**](http://psiphon.ca/) merupakan proxy web, karena itu dapat berjalan pada semua system operasi.

Kami sangat menyarankan Anda membaca dokumentasi yang dibuat oleh [**Sesawe**](http://sesawe.net/), organisasi global yang mengabdi demi keuntungan akses bebas sensor pada informasi bagi seluruh pengguna Internet di dunia.

## 1.1 Hal-hal yang perlu Anda ketahui sebelum menggunakan alat ini ##

Piranti **Tor** dirancang untuk meningkatkan privasi Anda dan keamanan dalam aktifitas dan kebiasaan Internet Anda; membuat identitas Anda terselubung dalam kegiatan online Anda; menghindari dari pengawasan Internet. Terlepas dari anonimitas itu penting atau tidak untuk Anda, **Tor** juga sangat berguna dalam menjaga keamanan kebebasan berInternet dan menipu sensor dan pembatasan alektronik sehingga Anda dapat mengakses blog dan berita atau membuatnya.

**Tor** melindungi anonimitas Anda dengan cara mengatur jalur komunikasi Anda melalui jaringan yang dikerjakan oleh sukarelawan dari seluruh dunia. Hal ini mencegah siapapun yang mungkin memantau Anda mempelajari situs apa yang Anda kunjungi, dan mencegah situs tersebut untuk melacak lokasi keberadaan Anda. Sebagai administrator dari **Tor**, mereka mengetahui jika Anda menggunakan **Tor**, atau sebagian lagi mengetahui *seseorang* mengakses situs yang Anda kunjungi, tapi tidak ada yang mengetahui keduanya.

**Tor** dapat menyamarkan akses Anda terhadap beberapa situs web, tetapi tidak dirancang untuk menyembunyikan konten dari komunikasi online Anda. Oleh karenanya, **Tor** memberi tambahan perlindungan jika digunakan dengan layanan internet seperti **Gmail** dan **RiseUp**, tetapi sebaiknya tidak digunakan untuk mengakses penyedia jasa email yang tidak aman, seperti **Hotmail** dan **Yahoo**, atau konten pengiriman dan penerimaan yang sensitive melalui koneksi *http* yang tidak aman.


**Definisi**: 

- **Port**: pada bab ini, port merupakan pin akses dimana piranti lunak berkomunikasi dengan layanan yang sedang bekerja pada komputer di jaringan lain. Jika sebuah URL, seperti **www.google.com** , memberikan 'alamat jalan' sebuah layanan, maka port akan memberitahu Anda 'pintu' mana yang harus Anda gunakan untuk mencapai tujuan yang benar. Saat merambah web, Anda pada umumnya menggunakan port 80 untuk situs yang tidak aman (**http://mail.google.com**) dan port 443 untuk situs yang aman (**https://mail.google.com**).

- **Proxy**: proxy merupakan penengah piranti lunak yang bekerja pada komputer, jaringan local atau tempat lain di Internet, yang membantu Anda mencapai tujuan akhir dari komunikasi Anda.

- **Route**: merupakan jalur komunikasi pada Internet antara computer Anda dan tujuannya.

- **Bridge Relay**: merupakan server **Tor** yang menyediakan langkah pertama Anda pada **Tor** anonymity network. Bridge merupakan pilihan, dan dirancang khususnya untuk pengguna di Negara yang memblokir akses kepada **Tor**


