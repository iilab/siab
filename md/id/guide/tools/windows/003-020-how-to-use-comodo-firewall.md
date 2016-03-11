

---

lang: id
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Use COMODO Firewall

---

Bagian-bagian dari halaman ini:

- [**3.0 Cara mengizinkan atau memblokir akses menggunakan COMODO Firewall**](#3.0)
- [**3.1 Cara membuka Main User Interface COMODO Firewall**](#3.1)
- [**3.2 Sekilas tentang Main User Interface COMODO Firewall**](#3.2)

-------

<a name="3.0"></a>
## 3.0 Cara mengizinkan atau memblokir akses menggunakan COMODO Firewall ##

Firewall adalah program yang didesain untuk melindungi komputer Anda dari pembajak ataupun malware. Keduanya ingin mempunyai akses langsung ke dalam komputer Anda, atau mengirim informasi dari komputer ke pihak ketiga. **COMODO Firewall** harus di konfigurasi untuk ‘belajar’ atau merekam applikasi yang ‘aman’ dan memberikan akses kepada aplikasi tersebut, ketika memblokir permintaan dari program / aplikasi  yang tidak aman dan proses yang mencurigakan terhadap sistem Anda. Mungkin proses ini akan memerlukan  beberapa waktu untuk memutuskan mana permintaan yang sah dan yang berupa ancaman.

Setiap kali **COMODO Firewall** menerima permintaan koneksi, ia akan mengaktifasi *Firewall Alert* (Peringatan Firewall) untuk memberitahu Anda untuk “allow” (mengizinkan) atau “block” (memblokir)  akses terhadap sistem Anda dari dan ke internet. Beberapa kali latihan yang melibatkan program aman seperti **Firefox** akan membantu Anda untuk menjadi lebih memahami peringatan firewall dan cara menggunakannya. Walaupun terkadang pengecualian akan dibutuhkan untuk permintaan dari browser yang diterima secara universal dan program email, setiap permintaan koneksi akan memunculkan *Firewall Alert* seperti yang ditunjukkan dibawah ini

![](/sbox/screen/comodo-en/21.png)

*Gambar 1: Contoh dari COMODO Firewall Allert (Peringatan firewall COMODO)*

Firewall bisa dikatakan sebagai peraturan yang mengawasi lalu lintas program atau file. Setiap kali Anda klik  *Allow* atau *Block*, **COMODO Firewall** akan membuat peraturan untuk permintaan untuk proses atau jaringan koneksi program. **COMODO Firewall** melakukan ini untuk program atau proses yang baru atau program yang tidak dikenal , serta yang terdaftar di daftar *Trusted Software Vendors* yang berada di jendela *Defense+ - Tasks > Computer Security Policy*

**Remember my answer**: Pilihan ini digunakan untuk mengingat jawaban Anda untuk program tertentu yang mengakses **COMODO Firewall**. Pililhan ini akan secara otomatis mengizinkan  atau memblokir permintaan koneksi dari program ketika kali berikutnya program tersebut meminta koneksi ke dalam komputer Anda, tergantung dengan pilihan yang Anda pilih disini. 

**Penting!**: kami sangat menyarankan Anda untuk **tidak memilih** *Remember my answer* (Ingat jawaban saya) ketika pertama kali menggunakan **COMODO Firewall**. Pilihlah mengizinkan  atau memblokir permintaan-permintaan koneksi, lalu awasi apakah pilihan Anda memperngaruhi operasi dari sistem Anda. Pilih *Remember my answer* hanya jika  Anda yakin dengan pilihan Anda.

**Tips**: Teliti dalam membatasi akses ke dalam sistem Anda adalah cara terbaik untuk memastikan keamanan komputer. Jangan ragu untuk memblokir permintaan yang mencurigakan. Apabila hal ini menghentikan  program yang normal  sehingga tidak berfungsi, Anda dapat mengizinkan  proses tersebut untuk bekerja ketika Anda menerima peringatan *firewall* berikutnya. 

**Langkah 1. Klik** ![](/sbox/screen/comodo-en/26.png) akan memunculkan jendela *Properties* sehingga Anda bisa mempelajari lebih jauh tentang proses atau program yang meminta akses, dalam hal ini, **Firefox**:

![](/sbox/screen/comodo-en/27.png)

*Gambar 2: Layar Firefox.exe Properties*

**Langkah 2: Klik** ![](/sbox/screen/comodo-en/02.png) untuk menutup layar *Properties*.

**Langkah 3**: Apabila Anda melihat suatu permintaan yang tidak aman atau tidak meyakinkan, berdasarkan informasi yang ditunjukkan layar program *Properties*, **klik** ![](/sbox/screen/comodo-en/29.png) untuk mengarahkan **COMODO Firewall** untuk menolak memberikan akses ke sistem Anda.

ATAU:

Apabila Anda melihat program yang sah yang tidak terlihat untuk meminta akses yang tidak mencurigakan, berdasarkan informasi yang ditunjukkan layar program *Properties*, **klik** ![](/sbox/screen/comodo-en/28.png) untuk memberikan akses ke sistem Anda.

**Langkah 4. Klik** ![](/sbox/screen/comodo-en/28.png) untuk membolehkan **Firefox** mengakses sistem Anda melalui **COMODO Firewall**.

**Langkah 5**. Karena **Firefox** adalah program yang aman, **centang**  pilihan ![](/sbox/screen/comodo-en/30.png) agar **COMODO Firewall** akan memberikan izin pada **Firefox** secara otomatis untuk kali berikutnya.

**Catatan**: Tombol *Allow* mengizinkan  Anda untuk memberikan akses kepada proses atau program setiap dijalankan. 

**Tips: Klik** ![](/sbox/screen/comodo-en/31.png) untuk mengakses file bantuan online **COMODO Firewall** yang lengkap.

Kemampuan Anda untuk memberikan keputusan akses atau blokir dengan benar akan bertambah baik seiiring dengan bertambahnya rasa percaya diri Anda dan pengalaman Anda menggunakan **COMODO Firewall**. 

<a name="3.1"></a>
## 3.1 Cara membuka Main User Interface COMODO Firewall ##

**COMODO Firewall** akan secara otomatis bekerja ketika Anda telah memasangnya dan telah merestart sistem Anda. Perangkat lunak  ini mempunyai panel kontrol yang lengkap dengan fitur dan pilihan yang dapat Anda sesuaikan. **Pengguna pemula (*Beginner*)** akan belajar cepat cara berhadapan dengan peringatan keamanan dari **COMODO Firewall**, sedangkan **Pengguna yang berpengalaman (*Experienced*)** dan **Ahli (*Advanced*)** akan belajar lebih tentang manajemen dan konfigurasi *firewall* yang lebih sulit. 

**Catatan**: Semua contoh di bawah ini berbasis pada **COMODO Firewall** berada dalam mode  **Optimum Defense**. Ini berarti sistem  *Defense+ host intrusion prevention* sedang dijalankan . Apabila Anda telah memasang **COMODO Firewall** menggunakan pilihan *Firewall only*, *Defense+* tidak akan menyala.

Untuk membuka  *Main User Interface **COMODO Firewall***, silahkan lakukan langkah berikut:

**Langkah 1. Pilih Start > Programs > COMODO > Firewall > COMODO Firewall**.

**Catatan**: Selain ini, Anda juga bisa meng-**klik dua kali** ikon desktop atau **klik dua kali** ikon **COMODO Firewall** di dalam *System Tray* untuk membuka *main user interface*. Sebagai tambahan, Anda juga boleh **klik kanan** pada ikon **COMODO Firewall** untuk mengaktifkan menu pop-up, lalu **pilih** *Open* seperti berikut:

![](/sbox/screen/comodo-en/35.png)

*Gambar 3: ikon menu pop-up konektivitas COMODO Firewall*

![](/sbox/screen/comodo-en/36.png)

*Gambar 4: User interface COMODO Firewall dalam mode default summary* 

<a name="3.2"></a>
## 3.2 Sekilas tentang Main User Interface ‘COMODO Firewal’l ##

Jendela *Firewall* menunjukkan ringkasan yang singkat dan jelas dari permintaan masuk dan keluar dari proses dan program yang ingin melewati **COMODO Firewall**. Seperti biasanya, lebih banyak permintaan keluar  daripada permintaan masuk. Mode operasi  yang sudah teratur adalah *Safe Mode*, dan mode operasi yang lain akan disebutkan nanti di bagian ini.  *Traffic*  menunjukkan bermacam proses dan program yang sedang dalam operasi, dan persentase jumlah dari permintaan yang dibuat.

**Klik** ![](/sbox/screen/comodo-en/37.png) untuk mengaktifkan ringkasan dari permintaan keluar *at a given moment* (saat ini juga) yang detil seperti berikut:
 
![](/sbox/screen/comodo-en/38.png)

*Gambar 5: Contoh dari jendela Active connections menunjukkan detail lalu lintas internet*

**Klik** ![](/sbox/screen/comodo-en/39.png) untuk mengaktifkan jendela *Active connections* untuk permintaan masuk *at a given moment*.

**Tips: Klik** ![](/sbox/screen/comodo-en/40.png) untuk memberhentikan semua permintaan masuk dan keluar, apabila layanan  internet Anda tiba-tiba melambat, Anda boleh mencurigai adanya proses atau program merusak yang sedang mengunduh dirinya sendiri ke dalam sistem Anda. Dengan melakukan ini, mode  operasi *Firewall* akan berubah menjadi ![](/sbox/screen/comodo-en/41.png). Silahkan lihat kembali detail ringkasan dari jendela *Active Connection* untuk mengidentifikasi potensi sumber masalah. 

Setelah Anda yakin bahwa semua masalah telah teratasi, **klik** ![](/sbox/screen/comodo-en/42.png) untuk memulai proses permintaan masuk dan keluar ke **COMODO Firewall** dan kembali ke ![](/sbox/screen/comodo-en/43.png) seperti biasanya.

### 3.2.1 Ikon Status COMODO Firewall dan Defense+ ###

Ketika **COMODO Firewall** dan **Defense+** sedang berjalan bersamaan,  indikasi pada sebelah kiri main user interface akan muncul seperti berikut:

![](/sbox/screen/comodo-en/69.png)

*Gambar 6: Ikon status COMODO Firewall*

Apabila salah satu program tidak dijalankan, ikon status akan mengindikasikan apakah *firewall* atau komponen proteksi proaktif tidak dijalankan seperti berikut:

![](/sbox/screen/comodo-en/70.png)

*Gambar 7: Ikon status COMODO Firewall tidak dijalankan yang berwarna kuning*

Akan tetapi, apabila kedua program tidak dijalankan, ikon status akan muncul seperti ini:

![](/sbox/screen/comodo-en/71.png)

*Gambar 8: Ikon status proteksi ganda COMODO Firewall tidak dijalankan yang berwarna kuning*
 
Dalam situasi yang mana pun, **klik** ![](/sbox/screen/comodo-en/72.png) untuk menjalankan proteksi yang berhubungan.


