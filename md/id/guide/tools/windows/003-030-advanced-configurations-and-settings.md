

---

lang: id
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: Advanced Configurations and Settings

---

Bagian-bagian dari halaman ini:

- [**4.0 Cara mengakses jendela Firewall dan Defense+**](#4.0)
- [**4.1 Jendela pengaturan aktifitas Firewall**](#4.1)
- [**4.2 Jendela pengaturan Defense+**](#4.2)

-------

<a name="4.0"></a>
## 4.0 Cara mengakses jendela Firewall dan Defense+ ##

Main user interface dari **COMODO Firewall** dibagi menjadi dua jendela, jendela *Firewall* dan jendela *Defense+*. 

![](/sbox/screen/comodo-en/80.png)

*Gambar 1: Main user interface COMODO Firewall menunjukkan kedua jendela, Firewall dan Defense+*

Jendela  *Pengaturan aktifitas firewall* dan *Defense+* dapat diakses dengan meng-**klik** ![](/sbox/screen/comodo-en/43.png) di masing-masing jendela untuk mengatifkan jendela-jendela  yang diperlukan beserta tab-tabnya.

Atau, Anda juga dapat mengakses salah satu jendela  dengan melakukan langkah berikut:

**Langkah 1. Buka** Main User interface dari **COMODO Firewall**. 

**Langkah 2. Klik** salah satu untuk mendapatkan jendela

![](/sbox/screen/comodo-en/60.png) OR ![](/sbox/screen/comodo-en/81.png)

to activate the *Firewall Tasks* ATAU *Defense+  Tasks* panes respectively.

**Langkah 3. Klik** antara 

![](/sbox/screen/comodo-en/82.png) ATAU ![](/sbox/screen/comodo-en/83.png) 

untuk mengaktifkan tab dari *Firewall Behaviour Settings* atau *Defense+ Settings*. 

**Tips**: *Firewall Security Level, Defense+ Security Level* dan *Sandbox Security Level* yang akan dijelaskan di bagian berikut ini, dapat diatur dengan mudah menggunakan ikon konektifitas **COMODO Firewall** yang terdapat di *System Tray*.  **Klik kanan** pada ikon konektivitas untuk mendapatkan menu pop-up dan sub-menu seperti ini:

![](/sbox/screen/comodo-en/84.png)

*Gambar 2: Menu pop-up untuk ikon konektivitas dan sub-menu untuk Firewall Security Level* 

<a name="4.1"></a>
## 4.1 Jendela pengaturan aktifitas Firewall ##

Jendela  **Firewall Behaviour Settings** (Pengaturan aktifitas Firewall) membuat Anda dapat menyesuaikan keamanan *firewall* dengan menggunakan beramacam-macam fitur dan pilihan, termasuk tingkat keamanan *firewall*, jumlah dan tipe peringatan keamanan yang diterima dan paket analisis dan monitor.

![](/sbox/screen/comodo-en/44.png)

*Gambar 3: Jendela aktifitas firewall – tab pengaturan umum*

Di tab pengaturan umum (*General Settings*), Anda dapat menentukan tingkat keamanan yang Anda inginkan untuk **COMODO Firewall** Gunakan penggeser (*slider*) untuk mengatur tingkat keamanan dari beberapa pilihan berikut:

**Block All**: Mode  ini memberhentikan seluruh trafik  yang berhubungan dengan internet dan tidak mengindahkan konfiguras *firewall* apapun dan aturan yang telah Anda buat. Mode  ini tidak akan mengikuti aturan yang dibuat untuk aplikasi-aplikasi, maupun merekam atau ‘mempelajari’ aktifitas dari aplikasi-aplikasi.

**Custom Policy**: Mode  ini hanya menggunakan peraturan keamanan dan trafik jaringan yang Anda sudah pernah masukkan  di jendela *Firewall tasks > Network Security Policy dan Defense+ Tasks > Computer Security Policy*. 

**Safe Mode**: Mode ini merupakan pengaturan otomatis untuk **COMODO Firewall**, termasuk pemasangan *Optimum Proactive Defense* dan *Maximum Proactive Defense*.

**Tips: COMODO Firewall** mengatur sebuah daftar internal aplikasi yang sering digunakan dan file yang dinilai  aman, sehingga tidak mengeluarkan peringatan pop-up untuk mereka.  

**Peringatan**: *Training mode* dan *Disabled Mode* tidak disarankan karena mereka dapat mengancam tingkat efektifitas dari **COMODO Firewall** dan mengekspos sistem Anda terhadap ancaman infeksi. 

<a name="4.2"></a>
### 4.2 Jendela pengaturan Defense+ ###

**Catatan**: Fitur dan pilihan yang dijelaskan di bagian ini lebih diperuntukkan untuk *Pengguna yang sudah ahli* karena memerlukan pengetahuan yang cukup tentang firewall dan isu-isu mengenai keamanan.

**Penting**: Apabila Anda mencentang  pilihan *Firewall with Optimum Proactive Defense* atau *Firewall with Maximum Proactive Defense* selama proses instalasi  **COMODO Firewall**, sistem *host intrusion prevention* akan secara otomatis diaktifkan . Namun, apabila Anda memilih *Firewall Only*, sistem *Defense+* masih bisa untuk diaktifkan  secara manual. Pilihan *Defense+* harus diaktifkan  agar fitur-fitur yang diperlukan bisa  bekerja. 

**COMODO Firewall Defense+** adalah sistem pencegahan intruksi host. Komputer yang terhubung ke sebuah jaringan (network) bisa dikatakan sebagai komputer host. Sistem *Defense+* akan terus mengawasi aktifitas semua *executable file* yang ada di komputer Anda. *Executable file* adalah aplikasi atau program, atau bagian dari program, yang biasanya (namun tidak selalu), dilihat dari file ekstensinya adalah sebagai  berikut: .bat, .exe, .dll, .sys, dll.

*Defense+* mengeluarkan peringatan pop-up setiap *file executable* yang tidak diketahui mencoba untuk aktif , dan menanyakan Anda untuk membiarkan atau memblokir file tersebut. Hal ini bisa dikatakan penting ketika Anda berada di situasi dimana sebuah malware ingin memasang aplikasi atau program untuk merusak informasi pribadi Anda, menata  ulang hard disk atau membajak komputer Anda, dan menggunakan komputer Anda untuk menyebarkan malware atau *spam* – tanpa seizin Anda.

### 4.2.1 Pengaturan Defense+ - tab pengaturan umum ###

Untuk menyalakan sistem *Defense+* dan mengaktifkan window pengaturan *Defense+* secara manual, ikuti langkah berikut:

**Langkah 1. Klik** tab Defense+ di main user interface **COMODO Firewall** lalu **klik** ![](/sbox/screen/comodo-en/50.png) untuk mengaktifkan layar berikut:

![](/sbox/screen/comodo-en/51.png)

*Gambar 6: The Defense+ window displaying the default General Settings tab*

**Langkah 2**. **Pindahkan** the slider up the scale to *Safe Mode* lalu **klik** ![](/sbox/screen/comodo-en/06.png) untuk mengaktifkan  sistem *Defense+* seperti di *Gambar 6*.

Pilihan di *Defense+ Security Level* sangat mirip dengan *Firewall Behaviour Security Level*, dan Anda dapat menggunakan slider untuk memilih tingkat  yang optimal untuk proteksi sistem Anda. 

**Paranoid Mode**: Mode  ini memberikan tingkat keamanan yang paling tinggi dan mengawasi segala *executable file* selain dari file yang Anda kategorikan sebagai aman dan juga yang terdaftar di *Trusted Software Vendor.* Mode  ini mempunyai jumlah peringatan keamanan yang paling tinggi dan aktifitas sistem disaring melalui pengaturan konfigurasi Anda.  

**Safe Mode**: Mode  ini akan secara otomotis ‘mempelajari’ aktifitas dari berbagai aplikasi yang dapat dieksekusi bersamaan dengan mengawasi sistem aktifitas yang penting. Setiap aplikasi yang tidak memiliki sertifikat akan menimbulkan peringatan keamanan (*Security Alert*) ketika aplikasi ini berjalan. Mode  ini adalah mode  yang paling sering dianjurkan untuk mayoritas pengguna. 

- Pilihan *Block all unknown request if the application is closed* akan secara otomatis memblokir semua permintaan dari aplikasi dan program yang tidak diketahui, dan yang tidak Anda sebutkan di *Kebijakan keamanan komputer* (*Computer Security Policy*).

- Pilihan *Matikan Defense+ secara permanen (memerlukan restart sistem)* (*Deactivate the Defense+ permantently (Requires a system restart*) membolehkan Anda untuk secara manual mematikan sistem *Defense+ host intrusion prevention*. Pilihan ini tidak dianjurkan.

### 4.2.2 Pengaturan Defense+ - tab pengaturan ‘Execution Control’ ###

Tab pengaturan *Execution Control* membatasi seberapa jauh file yang mencurigakan dapat mengakses sistem sumber Anda, kemudian menyerahkan file tersebut untuk analisis

![](/sbox/screen/comodo-en/54.png)

*Gambar 7: Tab pengaturan Defense+ Execution Control*

**Tips**: **Pengguna yang sudah ahli** boleh membuat pengecualian untuk tindakan-tindakan yang telah dikatakan dengan meng-**klik** ![](/sbox/screen/comodo-en/55.png) untuk mengaktifkan jendela *Exclusions*, dan mencari atau memilih proses yang berbeda atau program untuk pengecualian.

**Catatan**: **Pengguna yang berpengalaman** serta ahli sangat disarankan untuk meng-**klik** ![](/sbox/screen/comodo-en/47.png) Untuk mengakses bantuan online **COMODO** tentang tab pengaturan *Execution Control, Sandbox Settings* dan *Monitoring Settings*. Selain itu, Anda juga dapat membuka  **http://help.comodo.com/topic-72-1-155-1074-Introduction-to-Comodo-Internet-Security.html** untuk memilih dari daftar topik bantuan online.




