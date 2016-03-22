

---

lang: id
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 011
title: Pidgin with OTR - Secure Instant Messaging

---

**Situs Resmi**

- **Pidgin**: [**www.pidgin.im**](http://www.pidgin.im)
- **OTR**: [**www.cypherpunks.ca/otr**](http://www.cypherpunks.ca/otr/)

**Sistem operasi yang diperlukan**

- Semua koneksi internet
- Semua versi Windows

**Versi yang digunakan dalam panduan ini**

- Pidgin 2.7.11 
- OTR 3.2.0.1 

**Lisensi** 

- Gratis dan bisa didapat siapa saja (*Free and Open-Source Software*)

**Petunjuk yang perlu dibaca**: 

'Petunjuk bagaimana caranya' Bab [**7. Cara agar komunikasi internet Anda tetap rahasia**](https://securityinabox.org/id/chapter-7)

**Level:** 1: Pemula, **2: Umum**, 3: Menengah, 4: Berpengalaman, 5: Ahli 

**Waktu yang diperlukan untuk menggunakan alat ini**: 30 menit 

**Apa yang akan Anda dapatkan**: 

- Pengetahuan untuk mengatur dan merapikan beberapa dari pelayanan *IM* yang populer  melalui satu program
- Pengetahuan untuk untuk melakukan sesi percakapan yang pribadi dan aman.

**GNU Linux, Mac OS dan Program Microsoft Windows lainnya yang kompatibel:**

Baik **Pidgin** dan **OTR** tersedia untuk **Microsoft Windows** dan **GNU/Linux**. Program multi-protokol **IM** lainnya untuk **Microsoft Windows** yang bisa menjalankan **OTR** adalah [**Miranda IM**](http://www.miranda-im.org/). Pengguna **Mac OS** disarankan untuk menggunakan [**Adium**](http://adium.im/), program multi-protokol **IM** yang dapat menjalankan **OTR** plugin.

## 1.1	Hal-hal yang perlu Anda ketahui sebelum menggunakan alat ini ##

**Pidgin** adalah perangkat lunak **IM** yang gratis dan open source yang dapat Anda gunakan untuk mengatur dan merapikan berbagai akun **IM** Anda memalui satu interface. Sebelum Anda memulai **Pidgin** Anda harus mempunyai akun pesan instan, yang akan Anda daftarkan untuk akun **Pidgin** Anda. Contohnya, apabila Anda memiliki akun email Gmail, Anda dapat menggunakan layanan pesan instan GoogleTalk dengan **Pidgin**. Detil log-in dari akun pesan instan Anda digunakan untuk mendaftar dan mengakses akun Anda melalui **Pidgin**.

**Catatan**: Semua pengguna disarankan untuk belajar sebanyak mungkin tentang peraturan keamanan dan privasi dari **penyedia layanan pesan instan (*Instant Messaging Service Provider*)**.

**Pidgin** menunjang layanan **IM** berikut: [**AIM**](http://dashboard.aim.com/aim), [**Bonjour**](http://www.apple.com/support/bonjour/), [**Gadu-Gadu**](http://komunikator.gadu-gadu.pl/), [**Google Talk**](http://www.google.com/talk/), **Groupwise**, [**ICQ**](http://www.icq.com), **IRC**, [**MIRC**](http://www.mirc.com/), [**MSN**](http://www.msn.com/), 
[**MXit**](http://www.mxit.com/), [**MySpaceIM**](http://www.myspace.com/guide/im), [**QQ**](http://www.qq.com/), [**SILC**](http://silcnet.org/), **SIMPLE**, [**Sametime**](http://www.ibm.com/developerworks/downloads/ls/lst/), [**Yahoo!**](http://messenger.yahoo.com/), **Zephyr** dan semua **IM** yang menjalankan **XMPP** *messaging protocol*.

**Pidgin** tidak mengizinkan komunikasi antar layanan **IM** yang berbeda. Contoh, apabila Anda menggunakan **Pidgin** untuk mengakses **Google Talk** Anda, Anda tidak akan bisa berkomunikasi dengan teman yang menggunakan akun **ICQ**.

Namun, **Pidgin** dapat diatur untuk menjalanakan beberapa akun tergantung dari protocol pesan. Maka, Anda dapat menggunakan **Gmail** dan **ICQ** dalam waktu yang sama, dan bercakap menggunakan salah satu dari layanan tersebut (yang dijalankan oleh **Pidgin**).

**Pidgin** sangat dianjurkan untuk sesi-sesi **IM**, karena ia menawarkan tingkat keamanan yang lebih tinggi dibanding klien pesan yang lain, dan juga tidak dipenuhi dengan iklan yang tidak bermanfaat atau *spyware* yang dapat membahayakan privasi dan keamanan Anda.

Pesan **Off-the-Record (OTR)** adalah plugin yang dikembangkan khusus untuk **Pidgin**. Ia menawarkan fitur  privasi dan keamanan berikut:

- **Authentication**: Jaminan bahwa koresponden/teman bicara Anda adalah orang yang benar.
- **Deniability**: setelah sesi percakapan selesai, pesan yang bersal dari Anda atau koresponden Anda tidak dapat diidentifikasi 
- **Encryption**: tidak ada orang lain yang dapat mengakses dan membaca pesan instan Anda.
- **Perfect Forward Security**: apabila pihak ketiga mengambil kunci rahasia Anda, tidak ada percakapan sebelumnya yang dapat dibaca.

**Catatan**: **Pidgin** harus diinstal sebelum **OTR** plugin.

