

---

lang: es
community: guide
type: tactics
legacy: True
child: False
weight: 007
title: 7. How to keep your Internet communication private

---

<p>La conveniencia, la relación costo-beneficio y la flexibilidad del correo electrónico y de la mensajería instantánea los hace extremadamente valiosos para las personas y las organizaciones, incluso para aquellas con el acceso más limitado a la Internet. Para aquellos con conexiones más rápidas y más confiables, programas como Jitsi, <a href="/es/glossary#Skype" title="Skype"><em>Skype</em></a> y otras herramientas de <a href="/es/glossary#VoIP" title="Voz sobre Protocolo de Internet (VoIP)"><em>Voz sobre Protocolo de Internet (VoIP)</em></a> también comparten estas características. Lamentablemente, estas alternativas digitales a los medios tradicionales de comunicación no siempre pueden ser confiables para mantener privada información sensible. Por supuesto, esto no es nada nuevo. El correo postal, las llamadas telefónicas y los mensajes de texto también son vulnerables, particularmente cuando se utilizan por quienes son objeto de vigilancia por parte de las autoridades.</p>

<p>Una diferencia importante entre las comunicaciones digitales, métodos de comunicación basados en Internet y métodos más tradicionales, es que la primera a menudo te permite elegir tu propio nivel de seguridad. Si envías correos electrónicos, mensajes instantáneos y conversaciones en <a href="/es/glossary#VoIP" title="Voz sobre Protocolo de Internet (VoIP)"><em>Voz sobre Protocolo de Internet (VoIP)</em></a> utilizando métodos inseguros, éstos son casi con certeza menos privados que las cartas físicas o las llamadas telefónicas. Esto ocurre, en parte, debido a que algunas muy poderosas computadoras pueden automáticamente buscar a través de grandes cantidades de información digital para identificar a los remitentes, los destinatarios y palabras claves específicas. Se requieren de grandes recursos para llevar a cabo el mismo nivel de vigilancia para canales de comunicación tradicionales. Sin embargo, si tomas ciertas precauciones, puedes hacer realidad lo opuesto. La flexibilidad de las herramientas de comunicación de Internet y la fortaleza del <em><a href="/glossary#Cifrado" title="/es/glossary#Cifrado">cifrado</a><strong> </strong></em> moderno pueden ahora proporcionarnos un nivel de privacidad que alguna vez sólo estuvo al alcance de los ejércitos nacionales y de las organizaciones de inteligencia.</p>

<p>Siguiendo las guías y explorando el software que se trata en este capítulo, puedes mejorar enormemente la seguridad de tus comunicaciones. El servicio de correo electrónico <a href="/es/glossary#RiseUp" title="RiseUp"><em>Riseup</em></a>, el complemento <a href="/es/glossary#OTR" title="Fuera de Registro (OTR)"><em>OTR</em></a> para el programa de mensajería instantánea de <a href="/es/glossary#Pidgin" title="Pidgin"><em>Pidgin</em></a>, el Mozilla <a href="/es/glossary#Firefox" title="Firefox"><em>Firefox</em></a> y el complemento <a href="/es/glossary#Enigmail" title="Enigmail"><em>Enigmail</em></a> para el cliente de correo electrónico Mozilla <a href="/es/glossary#Thunderbird" title="Thunderbird"><em>Thunderbird</em></a> son todas excelentes herramientas. Sin embargo, cuando las utilices debes tener en cuenta que la privacidad de una conversación nunca estará cien por ciento garantizada. Siempre existe alguna amenaza que no has considerado, ya sea un <a href="/es/glossary#Keylogger" title="Registrador de teclas (keylogger)"><em>registrador de teclas (keylogger)</em></a> en tu computadora, una persona escuchando tras la puerta, un corresponsal de correo electrónico descuidado o algo completamente diferente. El objetivo de este capítulo es ayudarte a reducir incluso las amenazas que no se te ocurran, mientras evitamos la posición extrema, favorecida por algunos, de que no debes enviar nada por Internet que no estés dispuesto/a a comunicar públicamente.</p>

<p>&nbsp;</p>

<h3 id="Contexto">Contexto</h3>

<p>&nbsp;</p>

<table border="0" cellpadding="5" cellspacing="0">
	<tbody>
		<tr>
			<td><em>Claudia y Pablo trabajan con una ONG de derechos humanos en un país sudamericano. Después de pasar varios meses recolectando testimonios de testigos de violaciones de derechos humanos que fueron cometidos por miembros del ejército en su región, Claudia y Pablo han empezado a dar pasos para proteger los datos resultantes. Ellos mantienen sólo la información que necesitan, la cual almacenan en una partición TrueCrypt que está respaldada en varias ubicaciones físicas. Mientras se preparan para publicar ciertos aspectos de estos testimonios en un próximo informe, ellos se han percatado que deben debatir información sensible con unos cuantos de sus colegas en otro país. Aunque han acordado no mencionar nombres ni ubicaciones, aún así quieren garantizar que sus correos electrónicos y conversaciones a través de mensajería instantánea sobre este tema se mantengan privadas. Después de convocar una reunión para ocuparse de la importancia de la seguridad en la comunicación, Claudia pregunta si alguien en la oficina tiene alguna inquietud.</em></td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>

<p>&nbsp;</p>

<h3 id="Quepuedesaprender">¿Qué puedes aprender de este capítulo?</h3>

<ul>
	<li>Porqué la mayoría de los correos con interfaz web y servicios de mensajería instantánea no son seguros.</li>
	<li>Cómo crear una nueva y más segura cuenta de correo electrónico.</li>
	<li>Cómo mejorar la seguridad en tu actual cuenta de correo electrónico.</li>
	<li>Cómo utilizar un servicio seguro de mensajería instantánea.</li>
	<li>Qué hacer en caso que sospeches que alguien podría estar accediendo a tu correo electrónico.</li>
	<li>Cómo verificar la identidad de un remitente de correo electrónico.</li>
</ul>

<p>&nbsp;</p>


