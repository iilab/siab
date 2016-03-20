

---

lang: id
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 014
title: gpg4usb - email text and files encryption

---

**Situs Resmi**

- [**http://gpg4usb.cpunk.de/**](http://gpg4usb.cpunk.de/)

**Sistem operasi yang diperlukan**

- Semua versi windows

**Versi yang digunakan dalam panduan ini**

- 0.3.1

**Lisensi**

- Piranti lunak gratis dan bisa diakses dimana saja *(Free and Open-Source Software)*

**Petunjuk yang perlu dibaca**

- How-to Booklet chapter [**7. Cara agar komunikasi Anda tetap rahasia**](/id/chapter-7)

- [**Digital Security and Privacy for Human Rights Defenders**](https://www.frontlinedefenders.org/esecman), chapter **2.4 Cryptology - Public Key Encryption (page 38)**

**Level**: 1: Pemula, **2: Umum** 3: Menengah, 4: Berpengalaman, 5: Ahli

**Waktu yang diperlukan untuk menggunakan alat ini**: 20 menit

**Apa yang akan Anda dapatkan**:

- Kemampuan untuk mengenkripsi file dan pesan teks dari mana pun Anda berada (misalnya, sebuah kafe internet atau di tempat kerja)
- Kemampuan untuk mengenkripsi pesan *off-line* atau ketika akses internet tidak tersedia, dan kemudian mengirimkannya dari komputer yang terhubung ke Internet kemudian.

## 1.1 Hal-hal yang perlu Anda ketahui sebelum menggunakan alat ini ##

**gpg4usb** adalah program yang sederhana, ringan dan portabel yang memungkinkan Anda mengenkripsi dan mendekripsi pesan teks dan file. **gpg4usb** di dasarkan pada kriptografi kunci publik. Dalam metode ini, setiap individu harus menghasilkan sepasang kuncinya masing-masing. Yang pertama dikenal dengan sebutan kunci pribadi/private. Ini di lindungi oleh password atau passphrase, di jaga dan jangan pernah berbagi dengan siapa pun. 

Kunci kedua dikenal dengan kunci publik. Kunci ini dapat dibagi dengan salah satu koresponden Anda - dan koresponden Anda dapat berbagi kunci mereka kepada Anda. Setelah Anda memiliki kunci umum koresponden Anda, Anda dapat mulai mengirimkan email enkripsi kepada orang itu. Hanya dia yang dapat mendekrip dan membaca email Anda, karena dia hanya seorang yang mempunyai akses ke kunci pribadi.

Demikian pula, jika Anda mengirim salinan kunci publik Anda sendiri ke kontak email Anda dan menjaga kerahasiaan kunci pencocokan pribadi Anda, hanya Anda yang dapat membaca pesan enkripsi dari kontak-kontak itu.

Anda juga dapat melampirkan tanda tangan digital untuk pesan Anda. Penerima pesan Anda yang memiliki salinan asli dari kunci publik Anda akan dapat memverifikasi bahwa email tersebut berasal dari Anda, dan isinya tidak dirusak di dalam perjalanan.Demikian pula, jika Anda memiliki kunci publik koresponden, Anda dapat memverifikasi tanda tangan digital pada pesan-pesannya.

**gpg4usb** memungkinkan Anda *generate* sepasang kunci enkripsi, mengekspor kunci publik untuk dibagikan dengan orang lain, menulis pesan teks, dan mengenkripsi itu. Anda bisa cukup copy dan paste kunci publik dan / atau pesan terenkripsi dari *gpg4usb* untuk tubuh email Anda, atau menyimpannya sebagai file teks yang akan dikirim kemudian. Dokumen dan file dapat dienkripsi juga.

**Catatan**: ingatlah bahwa versi yang asli, versi yang tidak terenkripsi  dari dokumen dan file Anda mungkin masih berada di komputer Anda, sehingga koresponden Anda dan diri Anda sendiri harus ingat untuk menghapusnya dari komputer bila diperlukan.

**gpg4usb** memungkinkan Anda menukar kunci dan pesan yang terenkripsi serupa dengan program **GPG** atau **PGP**.

