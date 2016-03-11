

---

lang: ru
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Mount the Standard Volume

---

Теперь нужно, чтобы созданный нами файл-контейнер mult.avi появился в системе в виде диска. Эту операцию TrueCrypt называет &quot;монтированием&quot;.

- В основном окне TrueCrypt выбираем букву для нашего виртуального диска (какая вам больше нравится), например, T (TrueCrypt не предложит буквы, которые уже  заняты дисками). 

![](/sbox/screen/truecrypt-ru/13.png)

- Нажимаем на кнопку &quot;Файл&quot;, находим и выбираем файл mult.avi.


![](/sbox/screen/truecrypt-ru/14.png)

- Первая кнопка в нижнем ряду — &quot;Смонтировать&quot;. Нажимаем на нее.

![](/sbox/screen/truecrypt-ru/15.png)

- Запрос пароля к mult.avi. Вводим пароль и нажимаем &quot;ОК&quot;.

![](/sbox/screen/truecrypt-ru/16.png)

- В основном окне появляется информация, что диск подключен. Мы видим его букву, путь к файлу, размер (мы указывали 640 Мб, но в реальности получили чуть меньше, потому что TrueCrypt использует часть диска для хранения служебной информации) и тип тома — &quot;Обычный&quot;.

![](/sbox/screen/truecrypt-ru/17.png)

Теперь в системе появился диск T. Мы можем работать с ним как с любым
другим диском: открывать, сохранять, копировать, перемещать, удалять
файлы. TrueCrypt будет &quot;на лету&quot; шифровать наши данные.

Если мы закончили работать с диском и хотим отключить его, нужно убедиться, что все файлы на диске закрыты, ничего не читается и не
записывается, том не открыт ни в каких программах (вроде &quot;Проводника&quot; Windows). Выбираем из списка диск и нажимаем на кнопку &quot;Размонтировать&quot;.

![](/sbox/screen/truecrypt-ru/18.png)

Файл mult.avi исчезнет из окна TrueCrypt (конечно, он останется на компьютере), а диск T: — из системы.

&quot;Зачем размонтировать том, отключать диск? — спросите вы. — Разве нельзя постоянно держать его включенным?&quot;

Когда надобность в материалах на диске TrueCrypt отпала, в целях безопасности лучше отключить этот диск. Ведь если том смонтирован, существует потенциальная возможность получения доступа к нему в системе или по сети. Поэтому не следует оставлять компьютер со смонтированным томом без присмотра. Если вы работаете со смонтированным томом TrueCrypt на ноутбуке и намереваетесь временно отключить ноутбук (погрузить в &quot;спящий режим&quot;), не забудьте сначала размонтировать том. А если собираетесь сделать долгий перерыв в работе, лучше вообще выключить компьютер. Помня этот совет, вы убережете свои данные от чужих глаз.

Время от времени рекомендуется делать резервные копии томов TrueCrypt — переписывать файлы (в нашем случае mult.avi) на внешние носители, например, на CD или DVD.
