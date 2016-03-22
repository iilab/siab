

---

lang: id
community: guide
type: tactics
legacy: True
child: True
weight: 2
depth: 3
title: Remembering and recording secure passwords

---

Setelah melihat sederet petunjuk di atas, anda mungkin berpikir bagaimana seorang tanpa ingatan fotografik dapat mengingat kata sandi yang panjang, rumit dan tidak ada artinya, tanpa menuliskannya. Pentingnya menggunakan kata sandi yang berbeda pada setiap akun membuatnya semakin sulit. Namun, ada beberapa trik yang dapat membantu anda membuat kata sandi yang mudah diingat namun sangat sulit ditebak, bahkan oleh seorang pandai yang menggunakan perangkat lunak (software) pemecah kata sandi tingkat tinggi. Anda juga dapat  mencatat kata sandi anda menggunakan perangkat seperti [*KeePass*](/glossary#KeePass) yang dibuat khusus untuk tujuan ini

### Mengingat kata sandi yang aman ###

Penting untuk menggunakan jenis karakter yang berbeda-beda dalam memilih kata sandi. Hal ini dapat dilakukan dengan berbagai cara:

* Variasi penggunaan huruf kapital, seperti: ‘Nama saYA bukan TuaN MarSter’ / **'My naME is Not MR. MarSter'**
* Menggunakan angka dan huruf, seperti: 'k3rj4 teRu5 p4nTan6 5aN7a1' / **'a11 w0Rk 4nD N0 p14Y'**
* Menggunakan symbol tertentu, seperti: 'c@t(heR1nthery3' 
* Menggunakan beberapa bahasa, seperti: 'Let Them Eat 1e roTi at4u c()kelaT' 

Metode ini dapat membantu meningkatkan kerumitan kata sandi yang sederhana, yang memungkinkan anda untuk memilih kata sandi yang aman namun tetap dapat diingat. Beberapa penggantian yang sering digunakan (contoh : menggunakan angka nol untuk mengganti huruf 'o' atau menggunakan symbol '@' untuk mengganti huruf 'a') sudah lama dimasukkan ke dalam perangkat pemecah kata sandi, tapi masih bisa juga digunakan. Penggantian tersebut dapat memperlambat perangkat pemecah kata sandi tersebut untuk memecahkan kata sandi anda, dan saat perangkat tersebut tidak dapat digunakan, hal ini dapat mencegah orang menebak kata sandi anda.

Kata sandi juga dapat memanfaatkan Perangkat mnemonik ([*mnemonik devices*](/id/glossary#Mnemonic_device)) tradisional, seperti penggunaan singkatan. Ini dapat mengubah frase-frase yang penjang menjadi kata yang rumit dan terlihat acak:

* 'Iya atau tidak? Itu pertanyaannya' menjadi '1yatwTdk?Iptny4nY' / **'To be or not to be? That is the question' becomes '2Bon2B?TitQ'** 
* 'Kebenaran itu terbukti dengan sendirinya: semua manusia diciptakan sama' menjadi 'Kitds:sMdc=' / **'We hold these truths to be self-evident: that all men are created equal' becomes 'WhtT2bs-e:taMac='**
* 'Apa kamu senang hari ini?' menjadi 'apKm:-)H@riIn1?' / **'Are you happy today?' becomes 'rU:-)2d@y?**

Itu hanyalah beberapa conton untuk membantu anda menggunakan metode pengkodean kata dan frase and sendiri untuk membuatnya rumit dan mudah diingat

### Mencatat kata sandi dengan aman ###

Dengan sedikit kreativitas, anda dapat mengingat semua kata sandi anda, tetapi keharusan mengganti kata sandi secara teratur dapat menyebabkan anda kehabisan ide. Sebagai alternatif, anda dapat membuat kata sandi acak dan aman untuk semua akun anda, dan tidak perlu mengingat semua kata sandi anda. Anda dapat mencatatnya dalam sebuah secure password database portabel yang ter-enkripsi ([*secure password database*](/id/glossary#Secure_password_database)) seperti [*KeePass*](/id/glossary#KeePass). 

<div class="getstarted" markdown="1">
***Hands-on: Petunjuk memulai dengan*** [***KeePass Guide***](/en/keepass_main)
</div>

Jika anda menggunakan metode ini, sangat penting untuk membuat dan mengingat satu kata kunci yang sangat aman untuk [*KeePass*](/id/glossary#KeePass), atau perangkat apapun yang anda pilih. Setiap kali anda perlu memasukkan kata sandi untuk sebuah akun, anda dapat mencarinya menggunakan kata sandi utama tersebut, yang akan memudahkan anda untuk mengikuti semua saran diatas. <i>*[KeePass](/id/glossary#KeePass)* bersifat portable, yang berarti anda bisa meletakkan database tersebut dalam batang memori USB, jika anda perlu mencari kata sandi saat anda berada jauh dari komputer utama anda.

Walaupun ini mungkin adalah pilihan yang terbaik bagi siapa saja yang harus mengurus banyak akun, namun terdapat beberapa kelemahan dari metode ini. Pertama, jika anda kehilangan atau secara tidak sengaja menghapus  database kata sandi anda, maka anda juga akan kehilangan akses ke akun-akun yang kata sandinya disimpan dalam database tersebut. Sangatlah penting untuk membuat rekam cadangan (backup) database [*KeePass*](/id/glossary#KeePass) anda. Lihat [***Bab 5: Cara memulihkan informasi yang hilang***](/chapter-5) untuk berbagai informasi strategi membuat rekam cadangan. Untungnya, karena database anda terenkripsi, anda tidak perlu khawatir saat anda kehilangan batang memori USB atau piringan rekam cadangan yang mengandung salinan database tersebut

Kekurangan kedua mungkin lebih penting lagi. Jika anda lupa kata kunci utama untuk  [*KeePass*](/id/glossary#KeePass) anda, tidak ada cara untuk mengembalikannya bahkan untuk isi dari database tersebut. Maka, pastikan anda memilih kata sandi yang aman sekaligus mudah diingat!

<div class="background" markdown="1">
Mansour: Tunggu dulu. Jika KeePass menggunakan satu kata sandi utama untuk melindungi kata sandi kita yang lain, apa bedanya dengan menggunakan satu kata sandi yang sama untuk semua akun kita? Maksudnya, kalau ada orang jahat yang mengetahui kata sandi utama kita, dia bisa mengakses semuanya, kan? 

Magda: Pertanyaan bagus! Dan kamu benar, menjaga kata sandi utama sangat penting, tetapi ada beberapa perbedaannya. Pertama, si 'orang jahat' ini bukan hanya butuh kata sandimu, dia juga butuh database KeePass-mu. Kalau kamu menggunakan kata sandi yang sama untuk semua akunmu, dia hanya perlu kata sandinya saja. Selain itu, kita tahu bahwa KeePass ini sangat aman, kan? Program dan situs-situs lain bisa saja berbeda. Beberapa program lebih tidak aman dibanding yang lain, dan kamu tidak mau kan ada orang yang menerobos masuk ke situs yang lemah untuk mengakses akun lain yang lebih aman? Selain itu ada lagi. KeePass memudahkan kita mengganti kata sandi kalau memang perlu. Untung saya hari ini sudah memperbarui semua kata sandi saya!
</div>


