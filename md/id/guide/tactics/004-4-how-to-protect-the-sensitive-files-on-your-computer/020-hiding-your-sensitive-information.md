

---

lang: id
community: guide
type: tactics
legacy: True
child: True
weight: 2
depth: 3
title: Hiding your sensitive information

---

Menjaga keamanan adalah hal yang sangat mutlak, baik saat anda menyimpan sesuatu di rumah maupun dikantor, bahkan saat anda membawa sesuatu di kantong anda. Banyak orang memiliki kekhawatiran bahwa dengan menggunakan enkripsi ([*encryption*](/id/glossary#Encryption)) akan menyusahkan diri mereka. Walaupun izin resmi untuk meng-enkripsi ([*encrypt*](/id/glossary#Encryption)) data lebih banyak daripada tidaknya, tapi tetap saja orang jarang menggunakannya. Pada dasarnya terdapat dua alasan mengapa anda mungkin mengurungkan diri dari menggunakan  [*TrueCrypt*](/id/glossary#TrueCrypt): resiko menjadi "tertuduh" dan resiko terbongkarnya lokasi informasi rahasia anda

### **Mempertimbangkan resiko menjadi 'tertuduh'** ###

Di beberapa negara enkripsi ([*Encryption*](/id/glossary#Encryption)) dianggap ilegal. Hal ini berarti mengunduh, menginstal dan menggunakan software enkripsi dianggap sebagai tindak kriminal. Dan jika informasi yang anda miliki harus dilindungi dari kelompok-kelompok tertentu atau misalnya dari polisi, militer, atau badan intelijen, maka melanggar peraturan tersebut dapat memberikan alasan bagi mereka untuk menginvestigasi atau mengintimidasi kegiatan organisasi anda. Kenyataannya, ancaman ini bisa saja tidak berhubungan dengan keabsahan dari alat yang digunakan. Apapun yang berkaitan dengan perangkat lunak (software) enkripsi ([*encryption*](/id/glossary#Encryption)) bisa saja digunakan untuk menuduh anda telah melakukan tindak kriminal atau spionase (tanpa memperhatikan apa sebenarnya yang ada dalam [*encrypted*](/id/glossary#Encryption) volume anda), karena itu sebaiknya anda juga mempertimbangkan dengan cermat apakah penggunaan alat tersebut sesuai dengan keadaan anda.  

Jika hal itu yang terjadi, anda memiliki beberapa pilihan:

* Anda dapat menghindari penggunaan perangkat lunak (software) perlindungan data, itu berarti anda hanya dapat menyimpan informasi yang bersifat umum atau anda harus menciptakan sebuah sistem kode yang terdiri dari kata-kata untuk melindungi elemen-elemen kunci dari berkas rahasia anda.
* Anda dapat mengandalkan sebuah teknik yang disebut [*steganography*](/id/glossary#Steganography) untuk menyembunyikan informasi rahasia anda, daripada mengenkripsinya. Ada alat-alat yang dapat membantu anda dengan teknik ini, tetapi menggunakannya membutuhkan persiapan yang matang, selain itu anda juga akan tetap beresiko menjadi "tertuduh" saat ada orang yang mengetahui "alat" yang anda gunakan.
* Anda dapat mencoba menyimpan informasi rahasia anda di akun webmail yang aman, tetapi ini membutuhkan sambungan jaringan yang terpercaya dan pengetahuan komputer serta layanan internet tingkat tinggi. Tehnik ini mengasumsikan bahwa melakukan enkripsi ([*encryption*](/id/glossary#Encryption)) di jaringan lebih meringankan dibandingkan dengan melakukan enkripsi ([*encryption*](/id/glossary#Encryption)) berkas sehingga anda juga dapat menghindari ketidak sengajaan tertinggal salinan data di harddrive komputer tersebut.
* Anda dapat menyimpan informasi rahasia di luar komputer dengan menyimpannya di stik memori USB atau portabel hard drive. Namun perangkat jenis itu biasanya lebih rentan terhadap pencurian dan perampasan, jadi sebaiknya hindari membawa perangkat tersebut dengan data yang tidak terenkripsi.

Jika perlu, anda dapat menggunakan beberapa taktik tersebut secara bersamaan. Meskipun anda takut dianggap melakukan tindakan kriminal, menggunakan [*TrueCrypt*](/id/glossary#TrueCrypt) tetap merupakan cara yang paling aman, sambil menyamarkan [*encrypted*](/id/glossary#Encryption) volume anda sebaik mungkin. 

Jika anda ingin membuat encryted volume anda tidak terlalu mencolok, anda dapat mengubah namanya agar terlihat seperti berkas lain. Salah satu caranya adalah dengan mengubah jenis file ekstensinya menjadi '.iso' sehingga terlihat seperti sebuah file CD, cara ini sangat dianjurkan untuk file berukuran besar hingga kisaran 700MB. Jenis file ekstensi lainnya dapat digunakan untuk volume data yang lebih kecil. Hal ini seperti menyembunyikan brankas dibalik salah satu lukisan di dinding kantor anda. Walaupun ada kemungkinan brangkas tersebut ditemukan jika di cari dengan teliti, namun setidaknya cara ini dapat memberikan perlindungan yang lebih aman. Anda juga dapat mengganti nama program [*TrueCrypt*](/id/glossary#TrueCrypt), asumsikan saja anda menyimpannya sama seperti anda menyimpan berkas biasa di hard drive atau stik memori USB, bukan menginstalnya sebagai program. [***Panduan TrueCrypt***](/truecrypt_main) menjelaskan lebih lanjut tentang cara ini.    
	
### **Mempertimbangkan resiko teridentifikasinya informasi rahasia anda** ###

Seringkali, anda mungkin tidak terlalu kuatir ketika anda "tertangkap" karena anda memiliki perangkat lunak (software) [*encryption*](/id/glossary#Encryption) dikomputer atau usb anda namun kekuatiran terbesar akan timbul karena encryted volume anda akan dengan sangat jelas menginformasikan dimana anda menyimpan data/informasi rahasia yang anda lindungi tersebut. Walapun mungkin tidak ada yang dapat membacanya, namun mereka akan mengetahui bahwa data tersebut ada disana dan anda telah melakukan sesuatu untuk melindungi data tersebut. Hal ini dapat berakibat pada intimidasi, pemerasan, interogasi dan penyiksaan dari mereka yang menginginkan akses ke informasi tersebut. Pada saat seperti ini fitur penyangkalan (deniability) [*TrueCrypt's*](/id/glossary#TrueCrypt) sangat memainkan peranan penting, pembahasan selengkapnya ada dibawah ini.

Fitur penyangkalan [*TrueCrypt's*](/id/glossary#TrueCrypt) adalah salah satu fitur yang tidak ditawarkan oleh alat enkripsi ([*encryption*](/id/glossary#Encryption)) lainnya. Fitur ini dapat dianggap sebagai bentuk khusus dari steganografi ([*steganography*](/id/glossary#Steganography)) yang dapat menyamarkan informasi rahasia anda sehingga terlihat seperti data lain yang tidak sensitif dan tersembunyi. Hal ini analoginya sama seperti saat anda memasang 'ruang tipuan' pada brankas kantor anda. Jika seseorang mencuri kunci atau memaksa anda memberikan kombinasi angka kuncinya, ia akan menemukan umpan yang telah anda buat berada dalam 'ruang tipuan' brankas tersebut, tetapi tidak dapat menemukan informasi yang sebenarnya.

Hanya anda yang mengetahui adanya bagian tersembunyi di dalam brankas anda. Dengan demikian anda bisa meyakinkan mereka bahwa anda sudah memberitahukan semua informasi yang anda punya dan menyangkal bahwa masih ada rahasia yang anda lindungi, hal ini juga dapat membantu anda di saat anda terpaksa harus memberitahukan kata sandinya dengan alasan apapun. Beberapa alasan yang mengharuskan anda memberikan kata sandi misalnya ancaman hukuman atau fisik terhadap anda, kolega, teman, dan anggota keluarga. Tujuan dari penyangkalan ini adalah untuk memberikan kesempatan bagi anda untuk menyelamatkan diri dari bahaya yang mungkin timbul saat anda memilih untuk tetap melindungi data anda. Seperti yang dibahas dalam bagian [***Mempertimbangkan resiko menjadi 'tertuduh'***](#Mempertimbangkan_resiko_menjadi_'tertuduh'), biar bagaimanapun,  fitur ini 
sedikit banyak bermanfaat saat brangkas anda tertangkap karena konsekuensi dari fitur ini sungguh tidak terduga.

Fitur penyangkalan [*TrueCrypt's*](/id/glossary#TrueCrypt) bekerja dengan cara menyimpan 'hidden volume' di dalam  [*encrypted*](/id/glossary#Encryption) volume biasa. Anda dapat membuka 'hidden volume' ini dengan cara memasukkan kata sandi lainnya, berbeda dari kata sandi yang biasa anda gunakan. Bahkan jika penyusup yang canggih pun berhasil mengakses standar volume anda, ia tidak akan dapat membuktikan ada 'hidden volume' didalamnya. Sangat mungkin orang tersebut mengetahui bahwa [*TrueCrypt*](/id/glossary#TrueCrypt) dapat menyembunyikan informasi dengan cara ini, dan tidak ada jaminan ancaman tersebut akan berhenti walaupun anda sudah memberikan kata sandi perangkap anda. Banyak orang menggunakan [*TrueCrypt*](/id/glossary#TrueCrypt) tanpa mengaktifkan fitur penyangkalannya, dan biasanya tidak mungkin memastikan, bahkan setelah dianalisa,  apakah ([*encrypted*](/id/glossary#Encryption)) volume memiliki 'ruang tipuan' tersebut. Maka, anda harus memastikan agar anda tidak mengungkap hidden volume karena hal-hal non tehnis,  seperti membiarkannya terbuka atau mengijinkan salah satu aplikasi membuat jalan pintas (shortcut)ke salah satu file yang berada di volume tersebut. Bagian [***Bacaan lanjutan***](/id/chapter_4_3) di bawah ini mengarahkan anda ke berbagai informasi yang lebih lengkap mengenai hal ini. 

<div class="background" markdown="1">
Claudia: Baiklah, kalau begitu kita simpan saja berkas-berkas tidak penting di standard volume dan kita pindahkan semua berkas kesaksian ke hidden volume. Kamu punya berkas PDF atau file lama yang bisa kita gunakan?

Pablo: Wah, pikiran kita sama. Maksudku, kita harus memberikan kata sandi perangkap kalau tidak ada pilihan lain. Tapi supaya meyakinkan, kita harus membuat berkas-berkas itu terlihat penting, betul kan? Kalau tidak, percuma saja kan mengenkripsinya? Mungkin kita bisa masukkan dokumen-dokumen keuangan atau daftar situs-situs web kata sandi. 
</div>

