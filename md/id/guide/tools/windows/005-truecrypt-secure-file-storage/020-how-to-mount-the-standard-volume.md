

---

lang: id
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Mount the Standard Volume

---

Bagian-bagian dari halaman ini

- [**3.0 Cara melakukan *Mount* pada Standard Volume**](#3.0)
- [**3.1 Cara melakukan *Dismount* pada Standard Volume**](#3.1)

-------

<a name="3.0"></a>
## 3.0 Cara melakukan *Mount* pada Standard Volume ##

Di dalam **TrueCrypt**, melakukan *mount* terhadap *Standard Volume* berarti membuat standard volume menjadi siap digunakan. Di dalam bagian ini, Anda akan belajar cara melakukannya terhadap standard volume yang baru Anda buat.

Untuk memulai, silahkan lakukan langkah berikut:

**Langkah 1. Klik dua kali** ![](/sbox/screen/truecrypt-en/52.png) atau **pilih Start > Program > TrueCrypt > TrueCrypt** untuk memulai **TrueCrypt**.

**Langkah 2. Pilih salah satu** dari drive yang ada di daftar berikut:

![](/sbox/screen/truecrypt-en/12.png)

*Gambar 1: TrueCrypt Console*

*Di contoh ini Standard Volume akan di mount sebagai drive M.*:

**Catatan**: Di *Gambar 1*, drive *M* : telah dipilih untuk melakukan mount pada *standard  volume*, namun Anda boleh memilih drive lain yang terdaftar.

**Langkah 3. Klik** ![](/sbox/screen/truecrypt-en/17.png)

*Layar Select a TrueCrypt Volume akan muncul sebagai berikut:*

![](/sbox/screen/truecrypt-en/29.png)

*Gambar 2: Layar Select a TrueCrypt Volume*

**Langkah 4. Pilih** standard volume yang Anda telah buat, lalu **klik** ![](/sbox/screen/truecrypt-en/30.png) untuk menutup *Gambar 2* dan kembali ke konsol **TrueCrypt**.

**Langkah 5. Klik** ![](/sbox/screen/truecrypt-en/31.png) untuk mengaktifkan layar *Enter Password* seperti berikut:

![](/sbox/screen/truecrypt-en/32.png)

*Gambar 3: Layar Masukkan Password (Enter Password)*
 
**Langkah 6:  Ketik** password di tempat untuk mengetikkan *Password*

**Langkah 7. Klik** ![](/sbox/screen/truecrypt-en/33.png) untuk memulai *mount* pada *Standard Volume*.

**Catatan**: Apabila password yang Anda masukkan salah, **TrueCrypt** akan meminta Anda mengetik ulang dan **klik** ![](/sbox/screen/truecrypt-en/33.png). Apabila password Anda benar, *Standard Volume* akan menjadi *mount* sebagai berikut:

![](/sbox/screen/truecrypt-en/34.png)

*Gambar 4. TrueCrypt console menunjukkan Standard Volume yang baru di-mount*
 
**Langkah 8. Klik dua kali** entri berwarna di **TrueCrypt** atau **klik dua kali** huruf drive di layar *My Computer* untuk mengakses Standard Volume (yang sekarang di-*mount* di drive *M* : di komputer Anda).

![](/sbox/screen/truecrypt-en/35.png)

*Gambar 5: Layar memasuki Standard Volume melalui My Computer*
 
**Catatan**: Kita baru saja berhasil melakukan *mount* kepada standard volume *My Volume* di dalam disk virtual *M*:. Disk virtual ini beraktifitas seperti disk sungguhan, namun ia adalah drive encrypt seluruhnya.  Semua file akan selalu ter-encrypt secara otomatis ketika Anda mengopi, memindahkan, atau menyimpan mereka di disk virtual (prosesnya bernama *on-the-fly* enkripsi).

Anda dapat mengkopi file ke dan dari *Standard Volume* seperti Anda mengkopi mereka ke disk yang biasa (Contoh, dengan cara tarik dan letakkan (*dragging-and-dropping*) file-file tersebut). Ketika Anda mengeluarkan file dari *Standard Volume*, file akan secara otomatis mencopot encrypt yang ada. Sebaliknya, apabila Anda memasukkan file ke *Standard Volume*, **TrueCrypt** akan secara otomatis memasangkan encrypts pada file tersebut. Apabila komputer Anda tiba-tiba mati, **TrueCrypt** akan langsung menutup *Standard Volume* secepatnya.

**Penting**: Setelah menmindahkan file ke dalam volume **TrueCrypt**, pastikan tidak ada sisa dari file yang tertinggal di komputer atau USB memory stick. Silahkan baca bab [**6. Cara menghancurkan informasi rahasia**](https://securityinabox.org/id/chapter-6).

<a name="3.1"></a>
## 3.1 How to Dismount the Standard Volume ##
 
Di dalam **TrueCrypt**, melakukan *dismount* pada *Standard Volume* berarti membuat suatu volume menjadi tidak dapat digunakan.

Untuk menutup atau melakukan dismount pada *Standard Volume* dan membuatnya dapat diakses hanya oleh pengguna yang mempunyai password, lakukan langkah berikut:

**Langkah 1. Pilih** volume dari daftar volume yang ter-*mount* di jendela **TrueCrypt** seperti berikut:

![](/sbox/screen/truecrypt-en/34.png)

*Gambar 17: Memilih Standad Volume untuk melakukan dismount*

**Langkah 2. Klik** ![](/sbox/screen/truecrypt-en/49.png) untuk melakukan dismount atau menutup standard volume **TrueCrypt** Anda.

**Penting**: Pastikan untuk meng-*dismount*-kan volume **TrueCrypt** sebelum komputer Anda diubah ke  *Standby* atau *Hibernate* mode. Akan lebih baik  lagi jika Anda selalu mematikan komputer atau laptop jika Anda berencana untuk meninggalkannya tanpa pengawasan. Ini akan mencegah orang mendapatkan kata sandi volume Anda

Untuk mendapatkan kembali file yang Anda simpan di standard volume setelah Anda menutup atau melakukan *dismount* pada volume, Anda harus melakukan *mount* kembali.

