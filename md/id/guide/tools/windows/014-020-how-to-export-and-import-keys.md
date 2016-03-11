

---

lang: id
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Export and Import Keys

---

daftar seksi pada halaman ini:

- [**3.1 Cara Eksport Kunci Publik Anda dengan gpg4usb**](#3.1)
- [**3.2 Cara Import Kunci Publik koresponden dengan gpg4usb**](#3.2)
- [**3.3 Cara untuk memverifikasi kunci publik menggunakan gpg4usb**](#3.3)

-------

<a name="3.1"></a>
## 3.1 Cara eksport kunci publik anda dengan gpg4usb ##

Anda harus mengirimkan kunci publik Anda kepada koresponden Anda sebelum ia akan dapat mengirim pesan terenkripsi kepada Anda.

Untuk eksport kunci publik Anda menggunakan **gpg4usb**, ikuti langkah-langkah berikut:

**Langkah 1**. **Klik dua kali** ![](/sbox/screen/gpg4usb-en/02.png) untuk membuka program **gpg4usb** .

**Langkah 2**. **Klik** ![](/sbox/screen/gpg4usb-en/03.png) untuk mengaktifkan layar berikut:

![](/sbox/screen/gpg4usb-en/10.png)

*Gambar 1: Jendela Keymanagement menunjukan semua kunci*

**Langkah 3**. **Check** kunci Anda sendiri, seperti yang terlihat pada *Gambar 1* di atas.

**Langkah 4**. **Select** item *Export To File* dari menu **Key** seperti yang terlihat pada gambar dibawah ini:

![](/sbox/screen/gpg4usb-en/11.png)

*Gambar 2: Jendela Keymanagement dengan Export untuk item file yang dipilih*

ini akan mengaktifkan layar berikut:

![](/sbox/screen/gpg4usb-en/12.png)

*Gambar 3: Jendela Export To Folder browse*

**Langkah 5**. **Klik** ![](/sbox/screen/gpg4usb-en/13.png) untuk menyimpan sepasang kunci Anda ke folder program **gpg4usb** .

**Catatan**: Jika Anda ingin menyimpan kunci publik di tempat lain, Anda dapat menavigasi ke jendela yang diinginkan dengan menggunakan *Export To Folder* di jendela browse.

**Langkah 6**: **Send** file yang dieksport dengan kunci publik sebagai lampiran ke koresponden Anda.

<a name="3.2"></a>
## 3.2 Cara Import Kunci Publik koresponden dengan gpg4usb ##

Sebelum Anda akan dapat mengenkripsi informasi dan mengirimkannya ke koresponden Anda, Anda perlu untuk  harus menerima, dan mengambil kunci publik-nya.  Untuk mengimpor kunci publik koresponden dengan menggunakan **gpg4usb**, lakukan langkah-langkah berikut:


**Langkah 1**. **Klik dua kali** ![](/sbox/screen/gpg4usb-en/03.png) untuk membuka program **gpg4usb**.

**Langkah 2**. **Klik** ![](/sbox/screen/gpg4usb-en/14.png) untuk mengaktifkan layar berikut:

![](/sbox/screen/gpg4usb-en/15.png)

*Gambar 4: Import Key kotak dialog*

**Langkah 3**. **Choose** sumber kunci dan **klik** ![](/sbox/screen/gpg4usb-en/09.png) untuk mengaktifkan layar berikut:

![](/sbox/screen/gpg4usb-en/16.png)

*Gambar 5: Konsol gpg4usb menampilkan kunci publik yang baru diimpor terkait dengan akun Salima yang digariskan dalam hitam*

Sekarang Anda telah berhasil impor kunci publik koresponden Anda, Anda sekarang harus memverifikasi dan menandai kunci yang telah diimpor itu.

<a name="3.3"></a>
## 3.3 Cara verifikasi sepasang kunci menggunakan gpg4usb ##

Anda harus memverifikasi bahwa kunci yang diimpor benar-benar milik orang yang konon  mengirimkannya dan kemudian memverifikasinya sebagai pesan asli. Ini merupakan langkah penting bahwa Anda dan kontak email Anda harus mengikuti setiap kunci publik yang Anda terima.

Untuk memverifikasi sepasang kunci, lakukan langkah berikut:

**Langkah 1**. **Contact** koresponden Anda melalui beberapa alat komunikasi lain selain email.

**Catatan**: Anda dapat menggunakan telepon, pesan teks, **Voice over Internet Protocol** (**VoIP**) atau metode lainnya, tetapi hanya jika Anda yakin bahwa Anda benar-benar berbicara dengan orang yang tepat. Akibatnya hasilnya, percakapan telepon dan pertemuan tatap muka pertemuan memberikan jaminan terbesar atas keaslian identitas seseorang, jika atau ketika mereka dapat diatur dengan aman.

**Langkah 2**. Keduanya Anda dan koresponden Anda harus verifikasi 'fingerprints' dari kunci publik yang sudah Anda tukar .  

**Catatan**: Sidik jari adalah serangkaian unik angka dan huruf yang mengidentifikasi setiap tombol kunci. Sidik jari sendiri adalah bukan rahasia, dan dapat dicatat dan digunakan untuk verifikasi jika atau ketika diperlukan.

Untuk melihat sidik jari dari pasangan kunci yang telah Anda buat dan kunci publik yang Anda telah anda impor, lakukan langkah-langkah berikut:

**Langkah 1**. **Select** kunci, kemudian **klik-kanan** untuk mengaktifkan menu pop-up  terkait.

**Langkah 2**. **Select** item *Show Keydetails* seperti yang terlihat di bawah *Gambar 6*. 

![](/sbox/screen/gpg4usb-en/17.png)

*Gambar 6: Menu pop-up terkait dengan pasangan kunci koresponden*

*ini akan mengaktifkan layar berikut:*

![](/sbox/screen/gpg4usb-en/18.png)

*Gambar 7: Menu pop-up terkait dengan koresponden Terence, pasangan kunci Salima, dengan sidik jari yang digariskan dalam hitam*

**Langkah 3**. **Bandingkan** sidik jari ini dengan satu koresponden Anda lihat dalam program **gpg4usb**.

Koresponden Anda harus mengulangi langkah-langkah ini. Konfirmasikan  satu sama lain bahwa sidik jari untuk kunci Anda masing-masing telah bertukar cocok pengirim adalah asli. Jika mereka tidak cocok, tukar kunci publik Anda lagi dan ulangi proses verifikasinya.


Jika sidik jari cocok satu sama lain dengan *tepat*, maka Anda siap untuk mengirim pesan terenkripsi dan file antara satu sama lain dengan aman.

