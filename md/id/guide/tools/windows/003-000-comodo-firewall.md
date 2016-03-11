

---

lang: id
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 003
title: Comodo Firewall

---

**Situs Resmi**

[**www.personalfirewall.comodo.com**](http://www.personalfirewall.comodo.com)

**Sistem operasi yang diperlukan**

- Windows 2000/XP/2003/Vista
- Hak administrator untuk instalasi

**Versi yang digunakan dalam panduan ini**

- 5.0.16

**Lisensi** 

- Gratis

**Petunjuk yang perlu dibaca**: 

- Petunjuk bagaimana caranya [**1. Cara melindungi komputer dari malware dan peretas (hacker)**](https://securityinabox.org/id/chapter-1)

**Level:** 1: Pemula, 2: Umum, **3: Menengah, 4: Berpengalaman**, 5: Ahli

**Waktu yang diperlukan untuk menggunakan alat ini**: 60 menit 

**Apa yang akan Anda dapatkan**: 
 
- Pengetahuan  untuk melindungi komputer Anda dan keamanan jaringan dari pihak jahat, penyusup internet, malware, virus dan ancaman lainnya secara efektif  dan efisien 
- Pengetahuan  untuk mengatur permintaan dari program yang ada di komputer ketika mengakses Internet, dengan antarmuka *(interface)* perangkat  lunak yang mudah di konfigurasi


**GNU Linux, Mac OS dan program Microsoft Windows yang kompatibel:**

**GNU/Linux** mempunyai *firewall* di dalamnya ([**netfilter/iptables**](http://www.netfilter.org/)) dan pengaturan keamanan jaringan yang sangat baik. Di dalam *firewall linux*, terdapat berbagai interface yang mudah digunakan, kami merekomendasikan [**GUFW**](https://help.ubuntu.com/community/Gufw) (**Graphical Uncomplicated Firewall**) (see [**more information**](http://blog.bodhizazen.net/linux/firewall-ubuntu-gufw/)).

**Mac OS** juga mempunyai *firewall* internal yang kuat dan dapat diandalkan, yang bisa digabungkan dengan tambahan interface lainnya, seperti: [**NoobProof**](http://www.hanynet.com/noobproof/) or [**IPSecuritas**](http://www.lobotomo.com/products/IPSecuritas/), yang dapat memberikan kapasitas yang lebih. Untuk pengguna dengan keterbatasan finansial, kami menyarankan [**Little Snitch**](http://www.obdev.at/products/littlesnitch/index.html), untuk memberikan privasi dan kemanan serta perlindungan informasi pribadi yang lebih.

Selain **COMODO Firewall**, terdapat alternatif lainnya untuk **Microsoft Windows**. Pengguna dapat menggunakan [**ZoneAlarm Free Firewall**](http://www.zonealarm.com/security/en-us/zonealarm-pc-security-free-firewall.htm) atau [**Outpost Firewall Free**](http://free.agnitum.com/) sebagai pengganti yang sama efektifnya.

### 1.1	Hal-hal yang perlu Anda ketahui sebelum menggunakan alat ini ### 

*Firewall* bertugas sebagai penjaga atau pengaman  bagi komputer Anda. Ia mempunyai peraturan yang menentukan informasi mana yang boleh masuk dan keluar dari komputer Anda. *Firewall* adalah program pertama yang menerima dan menganalisa informasi yang masuk dari Internet dan program terakhir yang memperhatikan informasi yg keluar ke internet.

*Firewall* mencegah pembajak atau penyusup  mengakses informasi pribadi yang disimpan di komputer Anda, serta mencegah program malware mengirimkan informasi ke internet tanpa izin dari Anda. **COMODO Firewall** adalah *firewall* yang sudah dikenal luas yang merupakan perangkat lunak  gratis, artinya  Anda tidak perlu membeli lisensi untuk menggunakannya.  

Menggunakan program *firewall* yang dimodifikasi akan memerlukan waktu dan usaha untuk memastikan semua pengaturan sudah benar dan cocok untuk digunakan di komputer Anda. Setelah periode belajar, *firewall* akan bekerja dengan sendirinya dan hanya memerlukan sedikit kontrol dari Anda. 

**Peringatan!**: Jangan pernah mengakses Internet tanpa memasang *firewall* yang berfungsi di komputer Anda. Walaupun modem internet atau *router* mempunyai *firewall* sendiri, sangat disarankan Anda mempunyai *firewall* sendiri di komputer Anda.

