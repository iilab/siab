

---

lang: ru
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: Advanced Configurations and Settings

---

Comodo Firewall относится к программам, которые обладают достаточной простотой для невзыскательных пользователей и новичков, но способны предложить много полезных настроек продвинутым пользователям и тем, кто хочет сделать защиту компьютера максимально гибкой и эффективной. В рамках этого руководства мы не станем подробно разбирать все тонкости настройки Comodo Firewall и ограничимся общим обзором.

Вторая вкладка в основном окне называется &quot;Фаервол&quot;.

![](/sbox/screen/comodo-ru/23.png)

- **Журнал событий Фаервола.** Это &quot;регистрационная книга&quot; (компьютерщики часто говорят &quot;лог&quot;) всех случаев, когда Comodo Firewall реагировал на сетевую активность разных программ. Здесь можно увидеть, какая программа и когда пыталась выполнить то или иное действие, а также что предпринял межсетевой экран (например, заблокировал или задал пользователю вопрос).
- **Добавить доверенное приложение.** Удобно, если вы полностью уверены в безопасности некоей программы и хотите, чтобы Comodo Firewall больше не обращал на нее внимание.
- **Добавить заблокированное приложение.** Наоборот, сделать какую-либо программу &quot;персоной нон грата&quot;.
- **Политики сетевой безопасности.** Инструмент для гибкого создания правил. Можно выбрать одну из предустановленных политик или сформулировать свою.
- **Активные сетевые подключения.** Список программ, которые в данный момент осуществляют сетевую активность (с подробностями).
- **Мастер скрытых портов.** Эта группа настроек влияет на &quot;видимость&quot; вашего компьютера в интернете. Например, можно сделать компьютер видимым только в определенных сетях.
- **Настройки Фаервола.** Окно выбора режима (с ползунком), с которым мы познакомились ранее.

Следующая вкладка называется &quot;Защита&quot; (в других окнах Comodo Firewall то же самое называется &quot;Проактивная защита&quot;.

![](/sbox/screen/comodo-ru/24.png)

Что это такое?

Вопрос о том, включать ли &quot;проактивную защиту&quot;, программа задает еще на этапе установки. Но даже если мы тогда выбрали только межсетевой экран, позднее можно включить &quot;проактивную защиту&quot; в основных настройках программы (вкладка &quot;Сводка&quot;) подробно тому, как мы включали или изменяли режим межсетевого экрана.

&quot;Проактивная защита&quot; — своего рода &quot;усиленный контроль&quot; за поведением компьютерных программ. Этот модуль отслеживает все действия приложений, запускаемых на компьютере. Если Comodo Firewall &quot;не узнаёт&quot; программу, появляется предупреждение. Вы можете заблокировать программу, если считаете необходимым. &quot;Проактивная защита&quot; может быть полезной для защиты от разнообразного вредоносного кода — например, если программа-&quot;злоумышленник&quot; пытается получить доступ к вашим персональным данным, разослать спам, отформатировать жесткий диск или иным способом вторгнуться &quot;туда, куда не надо&quot;.

Окно богато разными опциями, которые в целом повторяют таковые для межсетевого экрана. Выделяется, пожалуй, лишь опция &quot;Запустить программу в Sandbox&quot;. *Sandbox* в переводе с английского — &quot;песочница&quot;. Это специальная защищенная область, создаваемая Comodo Firewall. Если программу запустить в &quot;песочнице&quot;, она (даже если захочет) не сможет навредить другим программам и данным на вашем компьютере.

Пункт &quot;Настройки Проактивной Защиты&quot; открывают окно с ползунком, похожим на тот, с помощью которого мы переключали режимы межсетевого экрана.

![](/sbox/screen/comodo-ru/25.png)

Режимы:

- **Параноидальный.** Программа ориентируется на пользовательские политики. Всякая иная активность будет вызывать тревогу и вопросы. Рекомендуется продвинутым пользователям.
- **Безопасный режим.** Применяются пользовательские политики. Кроме того, Comodo Firewall будет разрешать активность тем программам, которые считает безопасными (а об остальных предупреждать пользователя).
- **Режим: Чистый ПК.** В этом случае Comodo Firewall условно делит ваше рабочее пространство на две зоны: &quot;чистую&quot; (всем программам на жестких дисках можно доверять) и &quot;грязную&quot; (все появляющиеся на компьютере новые файлы, например, с USB-флэшки, по умолчанию считаются подозрительными).
- **Режим обучения.** Мониторинг без вмешательства, как и для межсетевого экрана.
- **Защита отключена.**

Остается рассмотреть окно вкладки &quot;Разное&quot;.

![](/sbox/screen/comodo-ru/26.png)

- **Настройки.** Общие настройки Comodo Firewall (выбор языка, защита программы паролем, опции ведения журнала и т.д.).
- **Управление моими конфигурациями.** Настроив Comodo Firewall по своему вкусу, вы можете экспортировать эти настройки в файл, а затем импортировать их в Comodo Firewall на другом компьютере.
- **Диагностика.** Функция &quot;самопроверки&quot; Comodo Firewall.
- **Проверить наличие обновлений.** Обычно Comodo Firewall делает это автоматически, но здесь вы можете выполнить такую проверку вручную.
- **Посетить форумы поддержки.**
- **Справка.**
- **О программе.**
