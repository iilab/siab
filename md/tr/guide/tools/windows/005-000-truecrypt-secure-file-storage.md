

---

lang: tr
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 005
title: TrueCrypt - Secure File Storage

---

**28 Mayıs 2014 tarihinde TrueCrypt geliştirici web sitesi, kullanıcılarına TrueCrypt gelişiminin şimdilik durduğunu haber verdi. Bu durumun arkasında yatan nedenler hala belli değil. Geliştirici web sitesi, TrueCrypt'in daha yeni ama bazı işlevleri kaldırılmış 7.2 sürümünü sunuyor. Bu yeni sürümün varlığına rağmen, gelişiminin durdurulmasının arkasındaki nedenleri ve TrueCrypt  gelişimi ile ilgili gelecekte bizleri neler beklediğini öğrenene kadar, eski sürüm 7.1a’yı kullanmanızı öneririz (Kurulum Talimatlarına bakınız). TrueCrypt’e alternatif programlar için aşağıdaki “GNU Linux, Mac OS ve diğer Microsoft Windows ile Uyumlu Programlar” bölümüne bakınız.**

**Ana Sayfa**

**www.truecrypt.org**

**Bilgisayar Gereksinimleri**

- Windows 2000/XP/2003/Vista/7
- Var olan birimlere erişmek için değil ama programın kurulumu ve yeni birim yaratmak için yönetici hakları gerekmektedir.

**VBu kılavuzda kullanılan sürüm**

- 7.1a

**Bu bölümün son güncellenme tarihi**

- Mayıs 2014

**Lisans**

- Özgür ve Açık Kaynak Yazılım 

**Taşınabilir Sürüm**

- [**Taşınabilir TrueCrypt için Uygulamalı Rehberler**](https://securityinabox.org/tr/truecrypt_portable)

**Gerekli Okumalar**

- Nasıl Yapmalı Kitapçığı [**4. Bilgisayarınızdaki hassas dosyaları nasıl korursunuz**](/chapter-4) bölümü

**Buradan sağlıyacağınız faydalar**: 

- Dosyalarınızı kötü amaçlı kimselerden ve izinsiz erişimlerden etkin bir şekilde koruyabilmek 
- Önemli dosyalarınızın kopyalarını kolay ve güvenli bir şekilde muhafaza edebilmek


**GNU Linux, Mac OS ve Microsoft Windows ile Uyumlu Diğer Programlar:**

**Not**: **TrueCrypt**, **GNU Linux** ve **Mac OS** için de uygundur.

[**Ubuntu**](http://www.ubuntu.com/) gibi birçok **GNU Linux** dağıtımı, standart bir özellik olarak, tüm sürücü için anında oluşturulan şifreleme ve şifre çözme özelliklerini destekler. Sistemi kurduğunuz zaman bu özelliği kullanıp kullanmayacağınıza karar verebilirsiniz. Ayrıca, kurulum esnasında ana klasör için şifreleme özelliğini açmanızı öneririz. **Linux** sisteminize , [**dm-crypt**](http://www.saout.de/misc/dm-crypt/) ve [**cryptsetup and LUKS**](http://code.google.com/p/cryptsetup/) kullanarak da şifreleme özelliği ekleyebilirsiniz. Bir başka olasılık da, özgür ve açık yazılım olan ve anında şifreleme-şifre çözme özelliğini kullanan [**SD4L (ScramDisk için Linux)**](http://sd4l.sourceforge.net/) programını kullanmaktır. 

**Mac OS** için **FileVault** kullanabilirsiniz. Bu işletim sisteminin bir parçasıdır ve tüm sürücünüz ve/veya ana klasörünüz ve alt klasörleriniz için *anında* şifreleme ve şifre çözme özelliği vardır. 

**Microsoft Windows** için alternatif olarak şunları öneririz:

* [DiskCryptor](https://diskcryptor.net/wiki/Main_Page) sistem bölmesi dahil tüm sürücü bölmeleriniz için şifreleme sağlayan özgür, açık kaynak şifreleme programıdır. 
* [**AxCrypt**](http://www.axantum.com/AxCrypt/) farklı dosyaları şifreleyebilen özgür ve açık kaynak bir programdır.

MS Windows 7 Ultimate veya Enterprise sürümlerine veya MS Windows 8 Pro ve Enterprise sürümlerinde, tüm sürücünüzü şifrelemek için [**BitLocker'ı**](http://windows.microsoft.com/en-us/windows7/products/features/bitlocker) bulabilirsiniz. Fakat unutmayın ki, BitLocker, bilgilerinizi koruma ve güvenlik sağlama amacını nasıl yerine getirdiği bağımsız olarak denetlenmemiş, kapalı ve tescilli bir Microsoft ürünüdür. 

### 1.1 Başlamadan once bu araçla ilgili bilmeniz gerekenler ###

**TrueCrypt** verilerinizi sizin oluşturacağınız bir şifre ile korumaya yardımcı olur. Bu şifreyi unutursanız, verilerinize erişiminizi kaybedersiniz! **TrueCrypt**, dosyalarınızı korumak için şifreleme denen bir işlem kullanır. Lütfen aklınızda tutun ki bazı ülkelerde şifreleme yasal değildir. **TrueCrypt**, belli başlı dosyaları şifrelemek yerine, bilgisayarınızda birim denilen, korunmuş bir alan yaratır. Bu şifrelenmiş birim içerisinde dosyalarınızı güvenli bir şekilde muhafaza edebilirsiniz.

**TrueCrypt**, şifrelenmiş bir standart birim veya bir gizli birim oluşturmanıza olanak verir. İkisi de dosyalarınızı gizli tutacaktır, fakat gizli birim, önemli bilgilerinizi daha az hassas olan verilerinizin arkasına saklayarak korur. **TrueCrypt** biriminiz ortaya çıksa bile bu bilgiler korunaklı kalır. Bu kılavuz her iki tür birim hakkında da detaylı bilgi vermektedir. 



