

---

lang: id
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: How to Scan for and Deal with Viruses Using avast!

---

Daftar isi laman ini:  

- [**4.0 Sebelum memulai**](#4.0)
- [**4.1 Panduan singkat cara untuk menanggulangi penyebaran virus**](#4.1)
- [**4.2 Ringkasan Main User Interface avast!**](#4.2)
- [**4.3 Cara mencari Malware dan virus-virus**](#4.3)
- [**4.4 Cara melakukan pencarian di seluruh sistem**](#4.4)
- [**4.5 Cara melakukan pencarian di dalam folder**](#4.5)
- [**4.6 Cara melakukan pencarian secara Boot-time**](#4.6)
- [**4.7 Cara menghadapi virus-virus**](#4.7)
- [**4.8 Cara menggunakan Virus Chest**](#4.8)
- [**4.9 Metode menghapus virus lebih lanjut**](#4.9)

----
<a name="4.0"></a>
### 4.0 Sebelum memulai ###

Ada dua cara untuk menghadapi malware dan berbagai macam virus ketika menggunakan **avast!**. Pertama adalah dengan melakukan pencarian di dalam komputer untuk mengidentifikasi ancaman-ancaman tersebut. Cara kedua adalah menghapus atau memindahkan ancaman-ancama tersebut ke dalam *Virus Chest* **avast!**. Menghapus dan/atau memindahkan malware dan virus-virus ke dalam *Virus Chest* merupakan cara efektif untuk mencegah ancaman tersebut berinteraksi dengan sistem komputer, sistem file, ataupun program email.

Walaupun terlihat janggal untuk menyimpan malware atau virus, tetapi apabila informasi penting maupun sensitif telah terjangkit, Anda tentunya ingin menyelamatkan informasi tersebut. **avast!** terkadang, walaupun jarang sekali, salah dalam mengidentifikasi kode sah atau program sebagai malware ataupun virus. Kode ataupun program tersebut, yang biasa disebut *“fales positives”*, mungkin sangat penting untuk sistem Anda, dan Anda tentunya tidak ingin kehilangannya.

*Virus Chest* **avast!** adalah *'dead zone'* atau karantina dalam bentuk elektronik dimana Anda bisa meneliti virus dan mengetahui bentuk ancamannya dengan melakukan riset di Internet, atau menyerahkan virus tersebut ke dalam laboratorium virus - pilihan tersebut terdapat di **avast!**  ketika Anda meng-klik kanan virus yang terdaftar di *Virus Chest*. Dengan meng-klik dua kali virus di dalam *Virus Chest*,  *tidak* akan mengaktifkan malware atau virus karena *Virus Chest* mengisolasi virus tersebut dari sistem Anda.

**Tips**: Sebagai alternatif, Anda dapat mentransfer informasi penting dan sensitif ke dalam *Virus Chest* **avast!** untuk melindungi informasi tersebut dari serangan virus.

Di dalam bab ini, anda akan: 

* Diperkenalkan dengan cara-cara terbaik untuk melindungi jaringan dan sistem PC Anda
* Diperkenalkan dengan main user interface, dengan fokus ke dalam tab *SCAN COMPUTER* dan *MAINTENANCE*
* Belajar melakukan macam-macam pencarian, dan
* Belajcar cara menggunakan *Virus Chest* **avast!**

<a name="4.1"></a>
### 4.1 Panduan singkat cara menanggulangi penyebaran virus ###

Terdapat beberapa tindakan pencegahan yang dapat dilakukan untuk membatasi ancaman-ancaman terhadap sistem komputer Anda; contohnya, dengan menghindari website-webiste yang meragukan maupun bermasalah, atau rajin menggunakan program anti-virus atau anti-spyware, seperti **avast!** atau **Spybot**. Tetapi, terkadang kita juga harus membagi koneksi Local-area network (LAN) atau internet. Poin-poin berikut dapat diambil sebagai pertimbangan ketika menghadapi serangan virus di dalam pengaturan komunitas ataupun ketika Anda di kantor:

* Putuskan sambungan fisik komputer Anda dari internet ataupun jaringan/network lokal. Apabila Anda mempunyai koneksi *wireless*, putuskan komputer Anda dari jaringan *wireless*. Matikan atau cabut kartu *wireless* apabila memungkinkan.

* Apabila komputer Anda berada dalam suatu jaringan, segera putuskan sambungan internet dari semua komputer di jaringan tersebut dari Internet, lalu putuskan komputer-komputer dari jaringan lokal. Semua pengguna harus berhenti menggunakan jaringan dan mulai menyalakan **avast!** atau anti-virus yang dapat dipercaya untuk mengindentifikasi dan menghapus virus. Walaupun terlihat seperti proses yang melelahkan, namun langkah ini sangat penting untuk mempertahankan integritas sistem individual dan jaringan.

* Lakukan pencarian secara *boot-time* untuk semua komputer di dalam  jaringan. Catatlah nama-nama virus yang Anda temukan, agar Anda bisa meneliti - lalu menghapus virus-virust tersebut, atau memindahkannya ke dalam **avast!** *Virus Chest*. Untuk mempelajari cara melakukan pencarian secara *boot-time*, silahkan lihat bab [**4.6 Cara melakukan pencarian secara *Boot-time***](/id/avast_menghadapivirus#4.6).

* Walaupun virus sudah dihapus, lakukan langkah sebelumnya, dan lakukan pencarian secara *boot-time* di dalam *semua* komputer, sampai **avast!** berhenti menunjukkan pesan peringatan. Anda mungkin harus melakukan pencarian secara *boot-time* lebih dari sekali, namun ini tergantung dari seberapa parah serangan malware atau virus yang terjadi.

Untuk informasi lebih lanjut tentang cara menghadapi penyebaran malware atau virus, anda dapat membaca bab [**4.9 Metode menghapus virus lebih lanjut**](/id/avast_menghadapivirus#4.9).

<a name="4.2"></a>
### 4.2 Ringkasan Main User Interface avast! ###

*Main User Interface* **avast!** terdiri dari empat tab yang tertera pada sebelah kiri window: *SUMMARY, SCAN COMPUTER, REAL-TIME SHIELDS* dan *MAINTENANCE*. Masing-masing tab dibagi menjadi sub-tab yang mengaktifkan jendela/panel yang saling berhubungan.

**Langkah 1**. **Klik** ![](/sbox/screen/avast-en/60.png) untuk mengaktifkan tampilan berikut:

![](/sbox/screen/avast-en/61.png)

*Gambar 1: Tab SUMMARY menunjukkan status saat ini sebagai SECURED* 

Berikut penjelasan singkat mengenai fungsi masing-masing tab: 

**SUMMARY**: Tab ini memperlihatkan *Current Status* dan sub-tabs *Statistik*. Sub-tab *Current Status* memperlihatkan status pekerjaan dari komponen kunci dari **avast!** yang digunakan untuk melindungi komputer Anda dari seringan malware atau virus. Jendela *STATISTICS* menunjukkan kegiatan operasional dari setiap komponen **avast!** selama seminggu, sebulan, atau setahun.  

**SCAN COMPUTER**: Tab ini menunjukkan sub-tab *Scan Now*, *Boot-time Scan* dan *Scan Logs*. *SCAN NOW* meperlihatkan pilihan-pilihan berbeda untuk melakukan pencarian manual. *BOOT-TIME SCAN* memungkinkan Anda untuk melakukan pencarian secara *boot-time* di waktu berikutnya Anda menyalakan komputer, dan *SCAN LOGS* memperlihatkan rekaman pencarian manual yang dilakukan dalam bentuk tabel.

**REAL-TIME SHIELDS**: Tab ini berfungsi untuk memonitor semua 'tameng' yang melindungi setiap aspek dari fungsi komputer Anda, dimulai dari *FILE SYSTEM SHIELD*. Tab ini menyediakan akses ke pengaturan *real-time shield*, termasuk menghentikan dan memulai perlindungan.

**MAINTENANCE**: tab ini mempunyai sub-tabs *Update*, *Registration*, *Virus Chest*, dan *About avast!*. Jendela *UPDATE* memungkinkan Anda melakukan *update* secara manual program dan definisi virus, sedangkan jendela *REGISTRATION*  memungkinkan Anda mendaftarkan *avast!* Anda. *VIRUS CHEST* bisa memperlihatkan macam-macam malware atau virus yang **avast!** temukan selama pencarian, dan memungkinkan Anda untuk melakukan macam-macam tindakan termasuk, menghapus, mencari lebih lanjut, ataupun menyerahkan virus ke dalam laboratorium virus. Tab *ABOUT AVAST!* menunjukkan informasi tentang versi terbaru dari **avast!** di dalam komputer Anda.

**Catatan**: Jendela *SCAN COMPUTER* dan *MAINTENANCE* sangat berguna ketika menghadapi malware dan virus. 

<a name="4.3"></a>
### 4.3 Cara mencari Malware dan Virus-virus ###

Di dalam bagian ini, Anda akan belajar tentang pilihan pencarian/*scan* yang tersedia, dan cara menggunakannya. Anda juga akan belajar cara melakukan pencarian sistem secara menyeluruh dan pencarian di dalam folder, dan juga pencarian secara *boot-time*.

Jendela *SCAN COMPUTER > SCAN NOW* menunjukkan empat pilihan scan yang tersedia di **avast!**, untuk melihatnya, lakukan langkah berikut:

**Langkah 1**. **Klik** ![](/sbox/screen/avast-en/62.png) untuk mengaktifkan layar berikut

![](/sbox/screen/avast-en/63.png)

*Gambar 2: Tab SCAN COMPUTER menunjukkan SCAN NOW*

Penjelasan singkat dibawah ini akan membantu Anda memilih cara pencarian yang tepat:

**Quick scan**: Pilihan ini disarankan untuk para pengguna yang tidak mempunyai banyak waktu untuk melakukan pencarian virus atau malware.

**Full sytem scan**: Pilihan ini direkomendasikan untuk pengguna yang memiliki cukup waktu untuk melakukan pencarian secara menyeluruh di dalam sistem Anda. Pencarian ini juga di rekomendasikan ketika pengguna pertama kali menggunakan software anti-virus di dalam komputernya. Durasi pencarian ini tergantung dari jumlah dokumen, *file*, ataupun *folder* dan *hard drives* di komputer Anda, dan juga kecepatan komputer. Silahkan baca bab [**4.4 Cara melakukan pencarian di seluruh sistem**](/id/avast_menghadapivirus#4.4).

**Removable media scan**: Pilihan ini direkomendasikan untuk melakukan pencarian di external *hard drives, USB flash drives*, dan media lainnya, terutama yang bukan milik Anda. Aktivitas ini akan melakukan pencarian terhadap program yang mencurigakan ketika peralatan portable ini dihubungkan ke komputer Anda.

**Select folder to scan**: pilihan ini digunakan untuk melakukan pencarian di suatu folder maupun beberapa folder yang spesifik, terutama folder yang Anda curigai telah terkena virus. Silahkan baca bab [**4.5 Cara melakukan pencarian di dalam folder**](/id/avast_menghadapivirus#4.5).

**Tips**: Setiap pilihan pemindaian membolehkan anda untuk melihat detil pencarian, contohnya, area yang sedang dipindai/*scan*. **Klik** ![](/sbox/screen/avast-en/84.png) untuk melihat. Apabila Anda memiliki keahlian lebih dalam bidang komputer, **klik** ![](/sbox/screen/avast-en/85.png) untuk memperbaiki parameter pencarian virus untuk setiap pilihan pencarian.

<a name="4.4"></a>
### 4.4 Cara melakukan pencarian di seluruh sistem ###

Untuk melakukan pencarian di seluruh sistem, ikuti langkah-langkah berikut:

**Langkah 1**. **Klik** ![](/sbox/screen/avast-en/64.png) pada pilihan *Full System Scan*, layar berikut akan muncul:

![](/sbox/screen/avast-en/65.png)

*Gambar 3: Jendela SCAN NOW menunjukkan scan ke seluruh sistem sedang dilaksanakan...* 

Setelah pencarian selesai, dan apabila ancaman terhadap komputer Anda ditemukan, jendela *Full system scan* akan terlihat seperti layar di bawah:

![](/sbox/screen/avast-en/66.png)

*Gambar 4: Proses Scan selesai, tampilan yang menunjukkan peringatan THREAT DETECTED!/ANCAMAN TERDETEKSI*

Pencarian seluruh sistem telah menunjukkan dua ancaman; untuk mengetahui cara untuk menanggulanginya, silahkan baca bagian [**4.7 Cara menghadapi virus-virus**](/id/avast_menghadapivirus#4.7).

**Avast!** *Virus Chest* adalah suatu folder yang muncul ketika pemasangan **avast!**  sedang dalam proses, yang merupakan *'dead zone'* atau karantina elektronik dimana malware atau virus dicegah supaya tidak berinteraksi dengan proses sistem lainnya

<a name="4.5"></a>
### 4.5 Cara melakukan pemindaian di dalam folder ###

Untuk melakukan pencarian di dalam, ikuti langkah berikut:

**Langkah 1**. **Klik** ![](/sbox/screen/avast-en/64.png) di *Select folder to scan*, layar berikut akan muncul:

![](/sbox/screen/avast-en/86.png)

*Gambar 5: Dialog box Select the areas*

Dialog box *Select the area* membolehkan Anda untuk memilih folder yang ingin Anda pindai. Anda dapat memilih lebih dari satu folder untuk melakukan pemindaian. Ketika Anda mencek box di samping setiap folder, folder path akan ditunjukkan di dalam kotak teks *Selected path*.

**Langkah 2**. **Klik** ![](/sbox/screen/avast-en/87.png) untuk memulai pencarian dan mengaktifkan layar berikut :

![](/sbox/screen/avast-en/88.png)

*Gambar 6: Pencarian di dalam folder sedang berlangsung.* 

**Tips**: **avast!** membolehkan Anda untuk melakukan pencarian folder individual melalui standard menu *pop-up* **Windows** yang muncul apabila Anda meng-klik kanan sebuah folder. Klik **Select** ![](/sbox/screen/avast-en/13.png) yang muncul di samping nama folder yang ingin Anda pindai. 

<a name="4.6"></a>
### 4.6 Cara melakukan pencarian secara Boot-time ###

Pencarian secara *boot-time* membolehkan Anda melakukan pencarian secara menyeluruh di *hard drive* Anda sebelum  **Microsoft Windows Operating System** mulai berjalan. Ketika pencarian secara *boot-time* dilakukan, mayoritas dari program malware dan virus sedang tidak dalam keadaan aktif, sehingga mereka belum berkesempatan untuk mengaktifkan diri mereka, atau berinteraksi dengan proses sistem yang lain. Maka dari itu, mereka lebih mudah untuk ditemukan dan dihapus.

Pencarian secara *boot-time* juga bisa mengakses langsung disk dan melewati *drivers* untuk sistem file **Windows**, yang merupakan target favorit dari sebagian besar ancaman komputer. Proses ini akan memunculkan *'rootkits'* – nama dari bentuk malware yang paling merugikan dan paling kuat sekalipun. **Sangat disarankan** bagi Anda untuk melakukan *scan boot-time* apabila Anda mencurigai bahwa sistem komputer Anda mungkin telah terinfeksi.

Pencarian *boot-time* disarankan untuk memperoleh hasil pencarian yang menyeluruh dan komplit. Bergantung pada kecepatan komputer dan jumlah data serta jumlah hard drives yang Anda miliki, pencarian secara *boot-time* mungkin akan membutuhkan waktu yang cukup lama. Pencarian secara *boot-time* sebaiknya dijadwalkan saat Anda menyalakan komputer Anda.

Untuk melakukan pencarian secara *boot time*, Anda perlu mengikuti langkah- langkah ini:

**Langkah 1**. **Klik** ![](/sbox/screen/avast-en/67.png) untuk mengaktifkan jendela  *BOOT-TIME SCAN*.

**Langkah 2**. **Klik** ![](/sbox/screen/avast-en/68.png) untuk menjadwalkan *boot-time scan* saat Anda menyalakan komputer. 

**Langkah 3**. **Klik** ![](/sbox/screen/avast-en/69.png) untuk memulai *boot-time scan* secepatnya.

**Catatan**: Pemindaian secara *boot-time* dimulai sebelum *Operating System* dan *interface* dimulai, sehingga hanya layar biru seperti dibawah ini yang akan muncul untuk menunjukkan kemajuan dari pencarian:

![](/sites/securitybkp.ngoinabox.org/files/u5/Avast_3_2_6.png)

*Gambar 7: Pencarian boot time avast! terjadwal*

**avast!** akan memberikan respon setiap kali mendeteksi adanya virus dan juga untuk melakukan *Menghapus/Delete*, *Mengabaikan/Ignore*, *Pindahkan/Move* atau *Perbaiki/Repair* satu atau semua virus yang terdeteksi, sangat disarankan agar Anda *tidak* mengabaikan hal ini dalam kondisi apapun. Daftar perintah ini hanya akan keluar jika ada virus yang terdeteksi di sistem Anda.

<a name="4.7"></a>
### 4.7 Cara menghadapi virus-virus ###

Selama proses pemasangan **avast!**, *Virus Chest* **avast!** akan diciptakan di *hard drive* Anda. *Virus chest* adalah sebuah folder yang terisolasi dari sistem komputer Anda, dan digunakan untuk menyimpan virus atau malware yang terdeteksi ketika pencarian dilakukan,  dan juga dokumen-dokumen, file, dan folder yang terkena virus.

Apabila Anda sudah pernah meng-*update* program dan definisi virus, Anda akan terbiasa dengan tab *MAINTENANCE* – yang juga merupakan akses Anda untuk masuk ke dalam **avast!** *Virus Chest*.
 
Untuk menghadapi malware atau virus yang terdeteksi ketika pencarian, lakukan langkah-langkah berikut:

**Langkah 1**. **Klik** ![](/sbox/screen/avast-en/70.png) untuk mengaktifkan layar berikut:

![](/sbox/screen/avast-en/71.png)

*Gambar 8: Jendela SCAN RESULTS/HASIL PENCARIAN menunjukkan peringatan THREAT DETECTED!/ANCAMAN TERDETEKSI* 

**Langkah 2**. **Klik** ![](/sbox/screen/avast-en/72.png) untuk menunjukkan daftar pilihan tindakan yang dapat dilakukan terhadap ancaman yang terdeteksi seperti yang ditunjukkan di *Gambar 8* di atas. 

**Catatan**: Disini, kami cenderung untuk memindahkan file yang terinfeksi ke dalam *Virus Chest*. Namun, daftar dari pilihan tindakan di atas menunjukkan tiga pilihan lain dan dibawah ini adalah deskripsi dari masing-masing pilihan:

**Repair**: tindakan ini mencoba untuk memperbaiki file yang terserang. 

**Delete**: Tindakan ini akan menghapus secara permanen file yang terserang.

**Do nothing**: pilihan ini tidak melakukan tindakan apa-apa, dan *sangat tidak direkomendasikan* sebagai cara menanggulangi malware atau virus yang berpotensi merusak.

**Langkah 3**. **Pilih** *Move to Chest*, lalu **klik** ![](/sbox/screen/avast-en/74.png) untuk mengaktifkan layar berikut: 

![](/sbox/screen/avast-en/75.png)

*Gambar 9: Virus telah berhasil dipindahkan ke dalam Virus Chest*

<a name="4.8"></a>
### 4.8 Cara menggunakan *Virus Chest* ###

Sekarang Anda bebas untuk memutuskan bagaimana cara untuk menanggulangi virus ketika virus tersebut telah berhasil dipindahkan ke *Virus Chest* **avast!**.

**Langkah 1**. **Klik** ![](/sbox/screen/avast-en/80.png) and **Klik** ![](/sbox/screen/avast-en/81.png) untuk mengaktifkan layar berikut:

![](/sbox/screen/avast-en/82.png)

*Gambar 10: Virus Chest menunjukkan dua virus*

**Langkah 2**: **Klik kanan**  virus yang manapun, untuk memperlihatkan menu tindakan yang dapat dilakukan terhadap virus yang telah dipilih. Tindakan itu adalah sebagai berikut

![](/sbox/screen/avast-en/83.png)

*Gambar 11: Pop up menu tindakan untuk virus di dalam Virus Chest*

**Catatan**: Meng-klik dua kali sebuah virus di dalam *Virus Chest* tidak akan mengaktifkan atau membuka virus tersebut. Hal itu hanya akan menunjukkan properti virus, atau informasi yang sama yang dapat Anda dapatkan apabila Anda memilih *Properties* dari pop-up menu.

Dibawah ini adalah daftar deskripsi dari tindakan di pop-up menu  yang dapat digunakan untuk menanggulangi virus:

**Delete**: Item ini akan menghapus virus secara permanen.

**Restore**: Item ini akan mengembalikan virus ke lokasi aslinya.

**Extract**: item ini akan menduplikat file atau virus ke dalam folder yang Anda pilih. 

**Scan**: Item ini akan memasukkan virus ke dalam pencarian berikutnya. 

**Submit to virus lab...**: Item ini akan menyerahkan virus untuk dianalisa lebih lanjut di database virus-virus yang telah diketahui. Memilih item ini akan memunculkan formulir penyerahan virus untuk diisi oleh Anda dan disubmit.

**Properties**: Item ini akan memunculkan detail lebih banyak tentang virus yang dipilih. 
 
**Add...**: Item ini akan memungkinkan Anda mencari file di sistem Anda untuk dimasukkan ke dalam *Virus Chest*. Hal ini sangat berguna apabila Anda mempunya file yang ingin Anda lindungi ketika terjadi penyebaran virus.

**Refresh all files**: Item ini akan meng-update file Anda, agar Anda dapat melihat file yang terakhir.
 
<a name="4.9"></a>
### 4.9 Metode menghapus virus lebih lanjut ###

Terkadang proteksi yang disediakan oleh **avast!**, **Comodo Firewall**, dan **Spybot** tidaklah cukup walaupun kita sudah berusaha dengan maksimal, sistem kerja maupun pribadi kita tetap *akan* terinfeski oleh malware dan virus lainnya. Di dalam bagian **4.1 Panduan singkat cara untuk menanggulangi penyebaran virus**, beberapa metode telah disampaikan untuk menanggulangi virus yang membandel. Tetapi, terdapat *cara* lain yang bisa dilakukan untuk menghapus ancaman-ancaman dari komputer Anda.

**Metode A: Mengunakan Anti-malware Rescue CDs/DVDs**

Beberapa perusahaan piranti lunak anti-malware juga menawarkan anti-virus CD/DVD 'penyelamat' secara cuma-cuma. Ini dapat di unduh dengan format ISO image (format yang dapat dimasukkan kedalam CD atau DVD).

Untuk memulai menggunakan Cds/DVDs ini, lakukan langkah berikut ini:

1. Unduh dan masukan program anti-malware kedalam CD. 
   *Anda dapat menggunakan program gratis seperti [**ImgBurn**](http://www.imgburn.com/)  untuk memasukkan gambar ke dalam disk.*

2. Masukan disk ke dalam komputer yang terserang, CD/DVD player  lalu restart lah komputer anda dari CD/DVD ini. 
   *Biasanya, Anda dapat melakukan ini dengan memencet tombol F10 atau F12 di keyboard Anda sesaat setelah menyalakan komputer. Perhatikan instruksi di layar komputer ketika sedang dinyalakan untuk mempelajari cara melakukan ini di komputer Anda.*
 
3. Hubungkan kembali sistem Anda ke Internet agar program anti-malware dengan sendirinya meng-*update* definisi virus apabila diperlukan, dimana setelah itu, sistem Anda akan kembali melakukan pencarian ke *hard drives* komputer Anda untuk menghapus software yang terinfeksi.

Berikut dafar dari rescue CDs images:

- [**AVG Rescue CD**](http://www.avg.com/us-en/avg-rescue-cd)
- [**Kaspersky Rescue CD**](http://support.kaspersky.com/viruses/rescuedisk/)
- [**F-Secure Rescue CD**](http://www.f-secure.com/linux-weblog/files/f-secure-rescue-cd-release-3.00.zip)
- [**BitDefender Rescue CD**](http://download.bitdefender.com/rescue_cd/)

Anda juga dapat melakukan scan virus di komputer Anda dengan menggunakan alat dibawah ini yang bekerja ketika **Windows OS** dinyalakan; akan tetapi, alat ini hanya akan bekerja apabila virus yang menyerang komputer Anda tidak menghalangi alat tersebut untuk bekerja:

* [**HijackThis**](http://free.antivirus.com/hijackthis/) dan alat gratis lainnya dari [Clean-up Tools](http://free.antivirus.com/clean-up-tools/) dari perusahaan **Trend Micro**.
* [**RootkitRevealer**](http://technet.microsoft.com/en-us/sysinternals/bb897445.aspx) dari [Sysinternals](http://technet.microsoft.com/en-us/sysinternals)dari **Microsoft**.

**Catatan**: Anda dapat menggunakan masing-masing alat di atas secara terpisah untuk memaksimalkan pembersihan komputer Anda.

**Metode B: Memasang ulang/*Re-installing* sistem Microsoft Windows Operating System**

***Catatan**:  Sebelum Anda mulai, pastikan Anda mempunyai lisensi atau nomer serial yang benar, dan salinan pemasangan dari **Windows OS** dan program lain yang Anda perlukan. Prosedur ini akan memakan waktu akan tetapi menghasilkan hasil yang maksimal apabila Anda tidak dapat menghapus malware dan virus dengan cara lain.*

Dalam beberapa kasus, infeksi virus bisa *sangat* merusak dimana software yang direkomendasikan sebelumnya di atas bisa dikatakan tidak berguna. Di dalam situasi seperti ini, kami rekomendasikan Anda untuk melakukan langkah dibawah ini:

1. Buatlah salinan dari semua data personal Anda di komputer.

2. Instal ulang sistem operasi **Microsoft Windows** dengan meng-format seluruh disk. 

3. Update sistem operasi **Microsoft Windows** setelah pemasangan selesai.

4. Pasang **avast!** (atau program anti-virus pilihan anda) lalu update.

5. Pasang program yang Anda perlukan dan ingatlah untuk mengunduh versi terbaru dan juga update dari setiap program.
   
    **Catatan**: Jangan sekalipun menghubungkan disk cadangan Anda ke komputer *sebelum* Anda melakukan langkah di atas karena komputer Anda beresiko untuk terkena serangan lagi.

6. Hubungkan disk cadangan Anda ke dalam komputer dan lakukan pencarian untuk mendeteksi dan menghapus masalah yang ada.

7. Setelah Anda mendeteksi dan menghapus masalah yang Anda temui, Anda boleh mengkopi file Anda dari disk cadangan ke hard drive komputer Anda.

