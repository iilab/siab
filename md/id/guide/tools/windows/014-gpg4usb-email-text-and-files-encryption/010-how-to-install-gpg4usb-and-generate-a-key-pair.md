

---

lang: id
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: How to Install gpg4usb and Generate a Key Pair

---

Daftar isi dari halaman ini:

- [**2.0 Cara Install gpg4usb**](#2.0)
- [**2.1 Cara *Generate* sepasang kunci dengan gpg4usb**](#2.1)

-------

<a name="2.0"></a>
## 2.0 Cara Install gpg4usb ##

Instalasi **gpg4usb** adalah proses yang cukup mudah dan sederhana, untuk memulai proses instalasi lakukan langkah-langkah berikut:

**Langkah 1**. **Tempatkan** file arsip **gpg4usb** zipped, kemudian **extract** semua file ke perangkat removable USB atau folder pada komputer Anda :

![](/sbox/screen/gpg4usb-en/01.png)

*Gambar 1:  Lokasi tujuan program gpg4usb*

**Langkah 2**. untuk menjalankan program **gpg4usb** , **klik dua kali** ![](/sbox/screen/gpg4usb-en/02.png) untuk membuka folder **gpg4usb** dan kemudian **klik dua kali** ![](/sbox/screen/gpg4usb-en/03.png) untuk mengaktifkan jendela *Open File - Security Warning*.  

**Langkah 3**. **Klik** ![](/sbox/screen/gpg4usb-en/04.png) untuk meluncurkan program **gpg4usb** seperti:

![](/sbox/screen/gpg4usb-en/05.png)

*Gambar 2: konsol utama gpg4usb*

<a name="2.1"></a>
## 2.1 Cara *Generate* sepasang kunci gpg4usb ##
 
Sebelum Anda dapat mulai mendekripsi dan mengenkripsi dokumen, file dan pesan teks, anda harus terlebih dahulu *Generate* sepasang kunci. Namun, sebelum Anda dapat mengenkripsi informasi yang akan dikirim ke orang lain, mereka harus terlebih dahulu mengirimkan kunci publik mereka.Bagaimana men-*share* kunci publik di jelaskan pada halaman berikutnya. Untuk mulai *Generate* sepasang kunci Anda, lakukan langkah-langkah berikut:

**Langkah 1**. **Klik** ![](/sbox/screen/gpg4usb-en/06.png) untuk mengaktifkan layar berikut:

![](/sbox/screen/gpg4usb-en/07.png)

*Gambar 3: Jendela Keymanagement dengan item Generate Key yang dipilih* 

**Langkah 2**. **Select** item *Generate Key* dari menu *Key* muntuk mengaktifkan jendela *Generate Key* .

**Langkah 3**. **Enter** data yang tepat kedalam kotak teks yang sesuai, jadi Anda mempunyai jendela anda sendiri yang menyerupai seperti berikut:

![](/sbox/screen/gpg4usb-en/08.png)

*Gambar 4: sebuah contoh dari format Generate Key yang selesai*

**Penting:** Menyetel kata sandi yang aman untuk melindungi kunci pribadi Anda (silahkan lihat bab 3 [**3. Cara membuat dan menjaga keamanan kata sandi**](/id/chapter-3)).

**Catatan**: Sebelum Anda dapat mengatur tanggal kadaluwarsa untuk sepasang kunci, Anda harus **disable** kotak *Never Expire* untuk mengaktifkan fitur calendering.

**Catatan:** daftar gulir *KeySize in Bit* digunakan untuk menyetel ukuran dari kunci Anda perlu diingat bahwa kunci yang ukurannya lebih besar lebih aman, tapi juga membutuhkan waktu lebih untuk membuatnya, enkrip dan dekrip teks. 

**Langkah4**. **Klik** ![](/sbox/screen/gpg4usb-en/09.png) untuk *generate* sepasang kunci. setelah sepasang kunci sudah sukses di *generate*, layar yang menyerupai seperti berikut akan muncul:


![](/sbox/screen/gpg4usb-en/10.png)

*Gambar 5: Jendela Keymanagement, menampilkan sepasang kunci yang baru dibuat* 

Sekarang Anda telah berhasil membuat sepasang kunci, Anda harus belajar bagaimana cara mengekspor kunci publik anda untuk berbagi dengan orang lain, dan bagaimana untuk mengimpor kunci publik koresponden Anda.

