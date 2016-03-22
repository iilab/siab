

---

lang: id
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: How to Encrypt and Decrypt Text and Files

---

Daftar dari bab di halaman ini:

- [**4.0 Cara Mengenkripsi Pesan Teks Menggunakan gpg4usb**](#4.0)
- [**4.1 Cara Mendekripsi Pesan Teks Menggunakan gpg4usb**](#4.1)
- [**4.2 Cara Mengenkripsi File Menggunakan gpg4usb**](#4.2)
- [**4.3 Cara Mendekripsi File Menggunakan gpg4usb**](#4.3)

-------

<a name="4.0"></a>
## 4.0 Cara Mengenkripsi Pesan Teks menggunakan gpg4usb ##

Proses untuk mengenkripsi pesan teks mudah dan cepat; seperti contoh berikut ini, Terence akan mengenkripsi email untuk Salima temannya, menggunakan langkah berikut:

**Langkah 1**. **Klik dua kali** ![](/sbox/screen/gpg4usb-en/03.png) untuk membuka konsol **gpg4usb**.

**Langkah 2**. **Menyusun** pesan anda seperti yang terlihat pada contoh di bawah ini:

![](/sbox/screen/gpg4usb-en/19.png)

*Gambar 1: Konsol gpg4usb menunjukkan sebuah contoh dari sebuah pesan*

**Langkah 3**. **Check** kotak cek yang terkait dengan penerima yang dimaksud email Anda sebagai berikut:

![](/sbox/screen/gpg4usb-en/20.png)

*Gambar 2: Konsol gpg4usb menampilkan penerima yang dimaksud, diuraikan dalam warna hitam*

**Catatan:** Anda dapat mengenkripsi pesan ke lebih dari satu penerima dengan hanya memeriksa *check boxes* yang sesuai dalam panel *Encrypt for:*. Juga, mungkin akan berguna untuk catatan pribadi Anda untuk mengenkripsi pesan itu untuk diri sendiri, sehingga Anda dapat membaca apa yang Anda kirim kemudian. 

**Langkah 4**. Baik **klik** ![](/sbox/screen/gpg4usb-en/21.png)atau **select Encrypt** dari menu **Crypt** untuk enkrip pesan Anda seperti berikut:

![](/sbox/screen/gpg4usb-en/22.png)

*Gambar 3: Konsol gpg4usb menampilkan contoh pesan yang di enkripsi*

**Langkah 5**. **Klik** ![](/sbox/screen/gpg4usb-en/23.png) Klik untuk memilih seluruh pesan terenkripsi, kemudian **klik** ![](/sbox/screen/gpg4usb-en/24.png) untuk menyalin pesan ke clipboard.

**Catatan**: Atau, Anda dapat menggunakan tombol *short-cut* yang terkait dengan setiap item dalam menu, dalam hal ini **Ctrl + E**.

**Langkah 6**. **Open** akun email Anda dan kemudian **open** pesan halaman kosong, dan kemudian **paste** pesan ini sehingga menyerupai berikut:

![](/sbox/screen/gpg4usb-en/25.png)

*Gambar 4: Sebuah contoh dari pesan enkripsi pada gpg4usb disisipkan ke dalam akun email Gmail*

**Catatandapat**: **Rich Text Formats** (**RTF**)dapat merusak format pesan terenkripsi, maka, lebih baik anda menyusun pesan anda dalam *plaintext*. Untuk mengkonversi **RTF** dalam *plain text* in **Gmail** secara mudah **klik** ![](/sbox/screen/gpg4usb-en/26.png) menampilkan dalam format toolbar di atas panel pesan.

<a name="4.1"></a>
## 4.1 Cara Mendekripsi Pesan Teks menggunakan gpg4usb ##

untuk mendekripsi sebuah email enkripsi, lakukan langkah berikut:

**Langkah 1**. **Klik dua kali** ![](/sbox/screen/gpg4usb-en/03.png) untuk membuka program **gpg4usb**.

**Langkah 2**. **Open** akun email Anda, kemudian **open** pesan.

**Langkah 3**. **Select**, **copy** kemudian **paste** pesan enkripsi kedalam konsol **gpg4usb** tab *untitled1.txt* seperti berikut:

![](/sbox/screen/gpg4usb-en/27.png)

*Gambar 5: Konsol gpg4usb menampilkan pesan dari dekripsi*

**Catatan**: Jika teks terenkripsi muncul dengan jeda baris ganda seperti yang ditunjukkan pada *Gambar 6* di bawah ini, *gpg4usb* mungkin tidak dapat secara otomatis mendekripsi. Untuk menghapus jeda baris ganda, **select** *Remove double Linebreaks* dari menu **Edit** untuk menghapus mereka dan kemudian melanjutkan proses dekripsi pada **Langkah 4**.

![](/sbox/screen/gpg4usb-en/28.png)

*Gambar 6: Konsol gpg4usb menampilkan pesan dari dekripsi dengan double linebreaks*
 
**Langkah 4**. **Klik** ![](/sbox/screen/gpg4usb-en/29.png) dan masukkan password yang Anda buat ketika men-*generate* sepasang kunci, seperti yang terlihat di layar berikut ini:

![](/sbox/screen/gpg4usb-en/30.png)

*Gambar 7: Jendela Enter Password prompt window*

**Langkah 5**. **Klik** ![](/sbox/screen/gpg4usb-en/09.png) untuk mengaktifkan konsol **gpg4usb** yang menyerupai *Gambar 2* di atas.

<a name="4.2"></a>
## 4.2 Cara Mengenkripsi File menggunakan gpg4usb ##

Proses untuk mengenkripsi file mirip dengan mengenkripsi pesan teks; dalam contoh berikut ini, Salima akan mengenkripsi file untuk Terence, menggunakan langkah-langkah berikut:

**Langkah 1**. **klik dua kali** ![](/sbox/screen/gpg4usb-en/03.png) untuk membuka program **gpg4usb**.

**Langkah 2**. **Klik** ![](/sbox/screen/gpg4usb-en/31.png) untuk mengaktifkan layar berikut:

![](/sbox/screen/gpg4usb-en/32.png)

*Gambar 8: Jendela file Enkrip / Dekrip, dengan pilihan default diaktifkan*

Jendela *Encrypt / Decrypt File* scroll list (digariskan dengan hitam) memungkinkan Anda memilih akun email dan kunci yang sesuai yang akan Anda gunakan untuk enkrip sebuah pesan.

**Langkah 3**. **Check** tombol radio *Encrypt* kemudian **klik** ![](/sbox/screen/gpg4usb-en/33.png) untuk mengaktifkan layar berikut:

![](/sbox/screen/gpg4usb-en/34.png)

*Gambar 9: Jendela Open File browser window*

**Langkah 4**. **Klik** ![](/sbox/screen/gpg4usb-en/35.png) untuk melampirkan file untuk di enkrip dan kembali untuk *Encrypt / Decrypt* window seperti:

![](/sbox/screen/gpg4usb-en/36.png)

*Gambar 10: Jendela Encrypt / Decrypt File menampilkan file yang didesign untuk enkripsi*

**langkah 5**. **Klik** ![](/sbox/screen/gpg4usb-en/09.png) untuk mengaktifkan layar berikut:

![](/sbox/screen/gpg4usb-en/38.png)

*Gambar 11:Kotak dialog konfirmasi done*

Kotak dialog konfirmasi *Done* menunjukkan dimana file enkripsi berada. sebuah file enkripsi juga dapat di identifikasi melalui *.asc* file extension, contohnya, *Technical White Paper.doc.asc*. 

**Langkah 6**. **Klik** ![](/sbox/screen/gpg4usb-en/09.png) untuk menyelesaikan proses enkripsi file.

**Catatan**: Anda dapat enkripsi pesan teks yang Anda kirim bersama dengan pesan enkripsi secara terpisah. 

**Langkah 7**. Menggunakan akun email Anda, **arahkan** pada spesifik lokasi dalam kotak dialog konfirmasi *Done* (*Gambar 11*), kemudian lampirkan file enkripsi ke email Anda seperti yang Anda lakukan pada file yang lain.

**PENTING**: Perhatikan bahwa nama file tersebut **tidak dienkripsi**.Pastikan bahwa nama ini tidak mengungkapkan informasi penting! Jangan lupa bahwa versi terenkripsi dari file terus berada dalam disk.

<a name="4.3"></a>
## 4.3 Cara Mendekripsi File menggunakan gpg4usb ##

Pada contoh berikut ini, Terence akan mendekripsi file yang telah Salima kirim, menggunakan langkah berikut:

**Langkah 1**. **Klik dua kali** ![](/sbox/screen/gpg4usb-en/03.png) untuk membuka program **gpg4usb**.

**Langkah 2**. **Open** akun email Anda, **open** pesan dan **download** file terlampir.

**Catatan**: Jika koresponden Anda telah mengirimkan pesan yang disertai dengan file yang dienkripsi, Anda dapat mendekripsi pesan dengan menggunakan metode yang dijelaskan dalam  [**4.1 Cara Dekrip Pesan Teks dengan  gpg4usb**](https://securityinabox.org/id/Cara%20mengenkripsi%20dan%20mendekripsi%20teks%20dan%20files)


**Langkah 3**. Pada konsol **gpg4usb** (seperti terlihat pada *Gambar 1* di atas), **klik** ![](/sbox/screen/gpg4usb-en/31.png) untuk mengaktifkan jendela **Encrypt / Decrypt File**  (seperti pada *Gambar 12* di bawah ini). 

**Langkah 4**. **Klik** ![](/sbox/screen/gpg4usb-en/33.png) untuk mencari lokasi file enkripsi yang di *download* seperti berikut:

![](/sbox/screen/gpg4usb-en/37.png) 

*Gambar 12: Jendela Encrypt / Decrypt, menampilkan jalan menuju file yang di enkripsi*

**Langkah 5**. **Klik** ![](/sbox/screen/gpg4usb-en/09.png) untuk mengaktifkan layar berikut:

![](/sbox/screen/gpg4usb-en/39.png) 

*Gambar 13: kotak dialog konfirmasi *Done* menampilkan lokasi file yang di enkripsi*

**Penting**: Jika Anda bekerja dari warnet atau di workstation di mana orang lain memiliki akses, Lebih baik Anda menyalin file *.asc* ke *USB atau Portable drive* Anda, dan bawa bersama Anda sehingga Anda dapat dekripsi file Anda dengan privasi dirumah Anda sendiri.

