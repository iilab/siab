

---

lang: ru
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Use OTR to Initiate a Secure Messaging Session in Pidgin

---

<ul>
	<li>Дважды щелкаем левой кнопкой мыши по нужному контакту. Как обычно, откроется окно сообщений. Обратите внимание на кнопку "Не защищено".</li>
</ul>

<p><img border="0" height="26" src="/sites/securitybkp.ngoinabox.org/files/u17/pidgin-notprotected.png" width="96" /></p>

<ul>
	<li>Нажимаем на эту кнопку и в появившемся меню выбираем "Начать защищенный разговор". Кнопка изменяется на "Не идентиф."</li>
</ul>

<p><img border="0" height="26" src="/sites/securitybkp.ngoinabox.org/files/u17/pidgin-notauth.png" width="96" /></p>

<ul>
	<li>В окне сообщений появляется информация о том, что начался защищенный диалог.</li>
</ul>

<p><img border="0" height="92" src="/sites/securitybkp.ngoinabox.org/files/u17/pidgin-started.png" width="377" /></p>

<p>Осталось подтвердить личность собеседника. Щелкаем правой кнопкой мыши по кнопке "Не идентиф.". В появившемся меню выбираем "Идентифицированный контакт". Pidgin и OTR предлагают на выбор три способа:</p>

<ul>
	<li><b>Вопрос-ответ.</b> Вы задаете вопрос, ответ на который, вы уверены, знает лишь ваш собеседник. Вы оба вводите ответы. Система проверяет, совпадают ли эти ответы. Если да, то все в порядке – контакт подтвержден.</li>
	<li><b>Секретное слово.</b> Вы вводите слово (число), о котором вы заранее условились со своим собеседником, и которое известно только вам двоим. Система осуществляет проверку.</li>
	<li><b>Отпечаток ключа.</b> Каким-либо иным способом (не с помощью Pidgin, а, скажем, по телефону) вы получаете от своего собеседника отпечаток его ключа, сравниваете с тем, что отображает Pidgin, и таким образом подтверждаете личность собеседника.</li>
</ul>

<p>Возьмем для примера первую ситуацию.</p>

<ul>
	<li>В первом списке выбираем "Question and answer" ("Вопрос и ответ").</li>
	<li>В поле "Enter question here" вводим придуманный вопрос.</li>
	<li>В поле "Enter secret answer here" вводим вариант ответа.</li>
</ul>

<p>Тот же вопрос возникает на экране компьютера вашего друга. Pidgin предлагает ему ввести ответ. Если ваши ответы не совпадут, вы увидите следующее сообщение:</p>

<p><img border="0" height="161" src="/sites/securitybkp.ngoinabox.org/files/u17/pidgin-error.png" width="255" /></p>

<p>А если совпадут – такое:</p>

<p><img border="0" height="160" src="/sites/securitybkp.ngoinabox.org/files/u17/pidgin-success.png" width="255" /></p>

<p>Теперь кнопка в окне диалога заменится на следующую:</p>

<p><img border="0" height="26" src="/sites/securitybkp.ngoinabox.org/files/u17/pidgin-protected.png" width="84" /></p>

<p>В настройках модуля OTR (вкладка "Известные отпечатки") вы сможете увидеть отпечаток ключа вашего друга. Чтобы и он получил отпечаток вашего ключа, ему тоже нужно проделать все шаги, описанные в этом пункте.</p>

