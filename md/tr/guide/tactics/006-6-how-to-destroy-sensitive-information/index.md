

---

lang: tr
community: guide
type: tactics
legacy: True
child: False
weight: 006
title: 6. How to destroy sensitive information

---

Önceki bölümler hassas bilgilerinizi korumanıza yardım edebilecek bir dizi aracı ve alışkanlığı ele aldı; ancak bir bilgiyi saklamanız gerekmediğine karar verdiğinizde ne olur? Örneğin belirli bir dosyanın şifrelenmiş yedek kopyalarının yeterli olduğuna karar verdiğinizde ve esas kopyayı silmek istediğinizde bunu yapmanın en iyi yolu nedir? Ne yazık ki, yanıt sandığınızdan daha karmaşık olabilir. Bir dosyayı sildiğinizde, **Geri Dönüşüm Kutusu**’nu boşalttıktan sonra bile, belgenin içeriği sabit diskinizde kalır ve uygun araçlara ve biraz da şansa sahip olan herhangi biri tarafından kurtarılabilir. 

Silinmiş bilgilerin yanlış ellere geçmemesini güvence altına almak için verileri güvenli ve kalıcı olarak ortadan kaldıran özel yazılımlar kullanmanız gerekir.[*Eraser*](/tr/glossary#Eraser) aşağıda ele alınan bu araçlardan biridir. [*Eraser*](/tr/glossary#Eraser)’ı kullanmak, kağıt belgeleri kimsenin bulmayacağını umut ederek basitçe çöp sepetine atmak yerine onları küçük parçalara ayırmaya benzer. Ve elbette dosyaları silmek, hassas bilgileri ortadan kaldırmanızı gerektiren durumların sadece bir örneğidir.. Birinin, özellikle güçlü ve siyasî olarak motive olmuş bir rakibinizin, sildiğinizi düşündüğünüz belirli dosyaları okuyarak siz ve kuruluşunuz hakkında bir şeyler öğrenebileceğinin ayrıntılarını göz önünde bulundurduğunuzda, muhtemelen kalıcı olarak silmek isteyebileceğiniz başka veri örnekleri de aklınıza gelecektir. Örneğin, günü geçmiş yedeklemeleri imha etmek, elden çıkarmadan önce eski sabit disklerinize [*kalıcı silme işlemi*](/tr/glossary#Wiping) uygulamak, internet tarayıcınızın geçmişini temizlemek... [*CCleaner*](/tr/glossary#CCleaner), bu bölümde ele alınan ve işletim sisteminizin ve uygulamalarınızın her kullandığınızda oluşturduğu geçici dosyaları silerken karşılaşacağınız zorluklar konusunda size yardımcı olabilecek bir başka araçtır.

### Arka plan senaryosu ### 
<div class="background" markdown="1">
Elena, Rusça konuşulan bir ülkede, bölgedeki yasa dışı ağaç kesiminin hangi boyutlara ulaştığını göstermek için fotoğrafların, videoların, haritaların ve öykülerin sunumuna dayanan bir web sitesi oluşturmaya başlamış bir çevrecidir. Web sitesini yaparken kullandığı bilgilerin bir yedeğini oluşturmuştur ve kopyalarını evinde, iş yerinde ve yeni dizüstü bilgisayarında saklamaktadır. Kısa bir süre önce web sunucusunun ziyaretçi kayıtlarını ve kullanıcıların forum gönderilerini içeren veritabanının da bir kopyasını depolamaya başlamıştır. Elena yakın zamanda çevreci aktivistlerin uluslararası bir konferansına katılmak için yurt dışına seyahat edecektir. Sınırı geçerken aktivistlerden bazılarının dizüstü bilgisayarlarına bir saati aşkın bir süreliğine el konulduğu haberi verilmişti. Hassas bilgilerini ve daha siyasî olan forum katılımcılarının güvenliğini korumak için, evindeki ve iş yerindeki yedekleri bir TrueCrypt bölümüne taşıdı ve dizüstü bilgisayarındaki kopyayı da sildi. Tavsiyede bulunması için yeğeni Nikolai’e danıştı ve o da, sınır görevlileri tarafından bilgisayarına el konulmasından endişe ediyorsa eski yedeklerini sadece silmekten daha fazlasını yapması gerektiği konusunda onu uyardı.
</div>

### Bu bölümden ne öğrenebilirsiniz ###

- Hassas bilgilerinizi bilgisayarınızdan kalıcı olarak nasıl silebilirsiniz 
- CD’ler ve USB bellekler gibi taşınabilir depolama aygıtlarındaki bilgilerinizi nasıl ortadan kaldırabilirsiniz
- Bilgisayarınızda yakın zamanda hangi belgelere göz attığınızı başkalarının öğrenmesini nasıl önlersiniz
- Silinmiş dosyalarınız gelecekte kurtarılamayacak şekilde bilgisayarınızı nasıl muhafaza edersiniz

