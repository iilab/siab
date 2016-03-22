

---

lang: id
community: guide
type: tactics
legacy: True
child: True
weight: 4
depth: 3
title: Advanced Email Security

---

Alat-alat dan konsep yang dibahas berikut ini direkomendasikan bagi pengguna komputer yang berpengalaman. 

### Menggunakan kunci enkripsi publik pada email ###
 
Anda bisa mendapatkan tingkat kerahasiaan email yang lebih tinggi, bahkan pada akun email yang tidak aman. Untuk melakukannya, anda perlu mempelajari tentang kunci [*enkripsi*](/id/glossary#Encryption) publik. Teknik ini memungkinkan anda untuk menyandi pesan individu, membuatnya tidak dapat terbaca oleh siapapun kecuali si penerima yang dituju. Aspek pintar dari kunci [*enkripsi*](/id/glossary#Encryption) publik adalah anda tidak perlu bertukar informasi rahasia dengan kontak tentang cara menyandi pesan-pesan anda di masa mendatang.

<div class="background" markdown="1">
Pablo: Tapi bagaimana cara kerjanya? 

Claudia: Matematika yang pintar! Kita menyandi pesan-pesan ke kontak email menggunakan 'kunci publik' khusus yang dapat ia sebarkan secara bebas. Lalu dia menggunakan 'kunci persobal' rahasia, yang harus ia jaga dengan hati-hati, untuk dapat membaca pesan tersebut. Demikian juga sebaliknya, kontakmu menggunakan kunci publik untuk mengenkripsi pesan-pesan yang ia tulis untukmu. Jadi pada akhirnya kamu harus bertukar kunci publik. Kamu bisa membagikan dengan terbuka tanpa harus khawatir jika orang yang menginginkan kunci tersebut bisa mengetahuinya. 
</div>

Teknik ini dapat digunakan dengan layanan email apa saja. Bahkan untuk layanan yang tidak memiliki kanal komunikasi yang aman. Ini karena pesan-pesan di [*enkripsi*](/id/glossary#Encryption) sebelum pesan tersebut meninggalkan komputer anda.

Ingatlah bahwa menggunakan [*enkripsi*](/id/glossary#Encryption) ada dapat mengundang perhatian ke diri anda sendiri. Jenis [*enkripsi*](/id/glossary#Encryption) yang digunakan saat anda mengakses situs web aman, termasuk akun webmail, sering kali tidak terlalu dicurigai, lain halnya dengan kunci [*enkripsi*](/id/glossary#Encryption) publik yang dibahas disini. Dalam beberapa situasi, jika sebuah email berisi data yang  di[*enkripsi*](/id/glossary#Encryption) ditampilkan di forum publik, email tersebut dapat memberatkan orang yang mengirimkannya, apapun isi pesan tersebut. Anda terkadang harus memilih antara kerahasiaan pesan anda atau menjaga agar tidak terlalu menarik perhatian. 

### Mengenkripsi dan mengotentikasi pesan-pesan individu ###
 
Kunci [*enkripsi*](/id/glossary#Encryption) publik mungkin terlihat rumit, tetapi akan mudah digunakan setelah anda mengerti dasar-dasarnya, serta alat-alat yang mudah digunakan. Program email Mozilla [*Thunderbird*](/id/glossary#Thunderbird) dapat digunakan dengan ekstensi [*Enigmail*](/id/glossary#Enigmail)untuk mengenkripsi dan mendekripsi pesan email dengan mudah. 

<div class="getstarted" markdown="1">
**Hands-on: Memulai Penggunaan**  [***Panduan Thunderbird***](/thunderbird_main)
</div>

[*VaultletSuite 2 Go*](/id/glossary#VautletSuite), sebuah program freeware email terenkripsi lebih mudah digunakan dari Thunderbird jika anda mau mempercayakan penyedia layanannya untuk mengerjakannya untuk anda. 

<div class="getstarted" markdown="1">
**Hands-on: Get started with the** [***VaultletSuite 2 Go Guide***](/vaultletsuite_main)
</div>

Otentisitas/keaslian email anda adalah aspek penting lain dari keamanan komunikasi. Siapapun yang memiliki akses internet dan alat yang tepat dapat menyamar sebagai anda dengan mengirim email dari alamat-alamat palsu yang identik dengan alamat anda. Bahanyanya disini lebih dirasakan oleh si penerima email. Bayangkan adanya ancaman yang datang melalui email, yang sepertinya datang dari kontak terpercaya, padahal berasal dari seseorang yang ingin mengganggu aktivitas anda, atau ingin mengetahui informasi tentang organisasi anda. 

Karena kita tidak dapat melihat ataupun mendengar koresponden kita melalui email, kita biasa mengandalkan alamat si pengirim untuk memastikan identitasnya, inilah sebabnya kita mudah tertipu oleh email palsu. [*Tanda tangan digital*](/id/glossary#Digital_signature) yang juga mengandalkan kunci [*enkripsi*](/id/glossary#Encryption) publik, memberikan cara yang aman untuk membuktikan identitas seseorang saat mengirim email. Bagian [***Cara menggunakan Enigmail pada Thunderbird***](thunderbird_main) dalam [***Panduan Thunderbird***](thunderbird_main) menjelaskan lebih rinci tentang cara kerjanya.

<div class="background" markdown="1">
Pablo:Ada seorang kolegaku yang pernah menerima email yang tidak aku kirim. Lalu kami berkesimpulan kalau itu adalah spam. Tapi aku jadi berpikir, apa jadinya kalau ada email palsu itu diterima oleh orang yang salah pada saat yang salah pula. Aku dengar kita bisa mencegahnya dengan tanda tangan digital. Apa sih tanda tangan digital itu?
			
Claudia:Tanda tangan digital itu seperti cap lilin yang ditempelkan di tutup amplop yang berisi surat di dalamnya. Tapi tanda tangan itu tidak bisa dipalsukan. Itu bukti bahwa kamu adalah pengirim asli dari pesan itu dan bahwa pesan itu belum dirusak saat dikirim. 
</div>

