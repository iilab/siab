

---

lang: id
community: guide
type: tactics
legacy: True
child: True
weight: 1
depth: 3
title: Encrypting your information

---

<div class="background" markdown="1">
Pablo: Komputer saya kan sudah dilindungi dengan kata sandi masuk ke Windows! Apakah itu tidak cukup?

Claudia: Sebenarnya kata sandi masuk Windows itu mudah sekali dibongkar. Siapa saja yang menggunakan komputermu, bisa menyalakannya kembali dan dengan menggunakan LiveCD bisa mengkopi semua data tanpa harus menembus kata sandimu. Jika mereka mengambil semua datamu, bahkan untuk waktu sebentar saja, masalahmu akan sangat besar. Selain kata sandi Windows, sebaiknya kamu juga jangan terlalu tergantung pada kata sandi Microsoft Word dan Adobe Acrobat.
</div>

Mengenkripsi ([*Encrypting*](/id/glossary#Encryption)) informasi kurang lebih sama seperti menyimpannya di brankas yang terkunci. Hanya orang yang punya kuncinya atau tahu kombinasi nomor (dalam hal ini kunci atau sandi [*encryption*](/id/glossary#Encryption)) yang bisa mengaksesnya. Analogi tersebut sesuai untuk [*TrueCrypt*](/id/glossary#TrueCrypt) dan alat sejenisnya yang dapat membuat wadah pengaman yang disebut 'encrypted volumes', sehingga anda tidak harus selalu melindungi setiap berkas setiap waktu. Anda dapat menyimpan banyak berkas dalam satu '[*encrypted*](/id/glossary#Encryption) volume', tetapi berkas atau file program yang ditempatkan diluar program ini tidak akan terlindungi demikian juga dengan stik memori USB anda.

<div class="getstarted" markdown="1">
**Hands-on: Petunjuk Memulai Penggunaan** [***TrueCrypt***](/truecrypt_main)
</div>

Perangkat lunak (software) lain mungkin saja menyediakan enkripsi (*[encryption](/id/glossary#Encryption)*) yang sama kuatnya, tetapi [*TrueCrypt*](/id/glossary#TrueCrypt) dibuat khusus agar sistem penyimpanan berkas tersebut mudah digunakan. Selain itu, program ini juga dilengkapi dengan kemampuan untuk membawa *[encrypted](/id/glossary#Encryption)* volumes dalam media penyimpanan portabel, faktanya ini adalah perangkat [*FOSS*](/id/glossary#FOSS) dan fitur penyangkalan (deniability) yang akan dijelaskan dalam bagian [***Menyembunyikan informasi rahasia anda***](/id/chapter_4_2) dibawah ini, [*TrueCrypt*](/id/glossary#TrueCrypt) memiliki keunggulan yang berbeda dibandingkan dengan alat-alat enkripsi berhak paten ([*proprietary*](/id/glossary#Proprietary_software) [*encryption*](/id/glossary#Encryption)) seperti ‘bitlocker’ dari Windows XP.

<div class="background" markdown="1">
Pablo: Nah, sekarang aku jadi khawatir. Bagaimana dengan pengguna (users) lain yang memakai komputerku? Apa mereka juga bisa membaca berkas yang ada di folder ‘My Documents’?

Claudia: Aku suka cara berpikirmu! Kalau kata sandi Windows saja tidak dapat melindungi komputermu dari penyusup yang ada diluar, bagaimana mungkin kata sandi itu melindungi komputermu dari orang (user) lain yang punya akun di komputermu? Jadi folder My Documents-mu memang bisa dilihat oleh siapa saja, bahkan orang lain bisa dengan mudah membaca berkasmu yang tidak dienkripsi. Kamu benar, walaupun folder sudah di buat menjadi 'private' tetap saja tidak aman kecuali kamu meng-enkripsi-nya.
</i>
</div>

### Petunjuk untuk menggunakan enkripsi dengan aman ###

Menyimpan data rahasia bisa beresiko bagi anda dan orang lain yang bekerja dengan anda. Enkripsi (*[Encryption](/id/glossary#Encryption)*) memperkecil resiko tersebut tetapi tidak menghilangkannya. Langkah pertama untuk melindungi informasi sensitif adalah dengan mengurangi jumlahnya. Jika tidak ada alasan tertentu untuk menyimpan suatu berkas atau kategori informasi tertentu dalam suatu berkas, sebaiknya anda menghapusnya (lihat [***Bab 6: Cara menghancurkan informasi rahasia***](/id/chapter-6)) untuk mengetahui cara melakukannya dengan aman. Langkah kedua adalah dengan cara menggunakan alat enkripsi ([*encryption*](/id/glossary#Encryption)) yang baik, seperti [*TrueCrypt*](/id/glossary#TrueCrypt). 
  
<div class="background" markdown="1">
Claudia:Mungkin kita tidak perlu menyimpan informasi yang dapat mengidentifikasi orang-orang yang memberi kesaksian pada kita. Menurutmu bagaimana?

Pablo:Setuju! Mungkin sebaiknya kita menuliskannya sesedikit mungkin. Selain itu, kita harus memikirkan kode sederhana yang bisa kita gunakan untuk melindungi nama dan lokasi yang memang harus kita catat 			
</div>

Kembali ke analogi brankas sebelumnya, ada beberapa hal yang harus anda perhatikan saat menggunakan [*TrueCrypt*](/id/glossary#TrueCrypt) dan alat sejenisnya. Sebagaimanapun kokohnya brankas anda, akan menjadi tidak berguna jika anda membiarkan pintunya terbuka. Saat [*TrueCrypt*](/id/glossary#TrueCrypt) volume anda sudah terpasang (saat anda bisa mengakses isinya), data anda menjadi rentan, maka anda harus selalu menutupnya, kecuali saat anda sedang membaca atau memodifikasi berkas yang ada di dalamnya.

Ada beberapa situasi dimana anda harus ingat untuk tidak meninggalkan [*encrypted*](/id/glossary#Encryption) volumes anda 'terpasang (mounted)':

* Putuskan sambungan saat anda hendak meninggalkan komputer anda. Tapi jika anda terbiasa membiarkan komputer anda menyala semalaman, anda harus memastikan bahwa anda tidak membiarkan berkas rahasia anda dapat diakses oleh penyusup, baik secara fisik atau jarak jauh.
* Putuskan sambungan ke komputer anda sebelum anda memasangnya dalam posisi "sleep". Hal ini juga berlaku jika anda hendak memasang komputer anda dalam posisi 'suspend' atau 'hibernation' yang biasanya hanya ada di laptop tapi juga tidak menutup kemungkinan terjadi di komputer anda.
* Putuskan sambungan sebelum orang lain menggunakan komputer anda. Saat anda membawa laptop dan melewati petugas pemeriksa atau perbatasan, sangatlah penting untuk memutuskan semua [*encrypted*](/id/glossary#Encryption) volume dan mematikan komputer anda secara sempurna.
* Putuskan sambungan sebelum memasukkan stik memori USB atau perangkat penyimpan eksternal lain yang tidak terpercaya, termasuk perangkat milik teman atau kolega anda.
* Jika anda menyimpan  [*encrypted*](/id/glossary#Encryption) volume  di dalam stik memori USB, ingatlah bahwa mencabut perangkat tersebut tidak secara langsung memutuskan enkripsi volume tersebut. Bahkan saat anda terburu-buru, anda harus tetap mematikan 'enkripsi volume' secara sempurna, lalu memutuskan sambungan 'external drive atau stik memory, baru anda dapat mencabutnya dari komputer anda. Sebaiknya anda berlatih sampai anda menemukan cara terbaik untuk melakukannya dengan cepat.

Jika anda memutuskan untuk menyimpan [*TrueCrypt*](/id/glossary#TrueCrypt) volume  dalam stik memori USB, anda juga dapat menyimpan salinan program [*TrueCrypt*](/id/glossary#TrueCrypt) di dalamnya. Dengan demikian anda dapat mengakses data anda melalui komputer lain. Tetapi, aturan main yang sama tetap berlaku: jika anda tidak yakin komputer tersebut bebas [*malware*](/id/glossary#Malware), anda sebaiknya tidak mengetikkan kata sandi atau mengakses data rahasia anda.  
 


