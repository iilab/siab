

---

lang: es
community: guide
type: tactics
legacy: True
child: True
weight: 3
depth: 3
title: Securing other Internet communication tools

---

<p>De manera similar que en el caso del correo electrónico, el software de mensajería instantánea y de <a href="/es/glossary#VoIP" title="Voz sobre Protocolo de Internet (VoIP)"><em>Voz sobre Protocolo de Internet (VoIP)</em></a> pueden o no ser seguros, dependiendo de las herramientas que escojas y de cómo las uses.</p>

<p>&nbsp;</p>

<h3>Asegurar tu software de mensajería instantánea</h3>

<p>La mensajería instantánea, también llamada 'chat,' normalmente no es segura, y puede ser tan vulnerable a la vigilancia como lo es el correo electrónico. Por suerte, existen programas que pueden ayudarte a asegurar la privacidad de tus sesiones de conversación o chat. Sin embargo - del mismo modo que con el correo electrónico - un canal de comunicación seguro requiere que tanto tú como tus contactos de mensajería instantánea utilicen el mismo software y tomen las mismas precauciones de seguridad.</p>

<p>Existe un programa de chat llamado <a href="/es/glossary#Pidgin" title="Pidgin"><em>Pidgin </em></a> que admite muchos de los protocolos existentes de mensajería instantánea, lo que significa que puedes utilizarlo fácilmente sin tener que cambiar el nombre de tu cuenta o recrear tu lista de contactos. Con el fin de tener conversaciones privadas <strong>cifradas</strong> a través del Pidgin, necesitarás instalar y activar el complemento <a href="/es/glossary#OTR" title="Fuera de Registro (OTR)"><em>Fuera de Registro (OTR)</em></a>. Afortunadamente, este es un proceso muy simple.</p>

<p>&nbsp;</p>

<table border="0" cellpadding="5" cellspacing="0">
	<tbody>
		<tr>
			<td><img align="middle" height="63" src="/sites/securitybkp.ngoinabox.org/files/u9/hand_web_trans.png" width="60" /> <strong>Parte Práctica: Empieza con la <a href="/es/pidgin_principal"><strong>Guía del Pidgin</strong></a></strong></td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<table border="0" cellpadding="5" cellspacing="0">
	<tbody>
		<tr>
			<td>
			<p><em>Pablo: Si el correo con interfaz de Yahoo es inseguro, eso significa que el ¿Yahoo Chat es inseguro, también? </em></p>

			<p><em>Claudia: Lo que tienes que recordar es que, si queremos utilizar mensajería instantánea para ocuparnos de este informe, necesitamos asegurarnos que todas las personas involucradas tengan instalados el Pidgin y el complemento Fuera de Registro (OTR). Si es así, podemos utilizar el Yahoo Chat o cualquier otro servicio de conversación (Chat).</em></p>
			</td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>

<p>&nbsp;</p>

<h3>Asegurar tu software de Voz sobre Protocolo de Internet (VoIP)</h3>

<p>Las llamadas utilizando <em><a href="/es/glossary#VoIP" title="Voz sobre Protocolo de Internet (VoIP)"><em>Voz sobre Protocolo de Internet (VoIP)</em></a></em> hacia otros usuarios de <strong> </strong>Voz sobre Protocolo de Internet (VoIP) son generalmente gratuitas. Algunos programas te permiten también hacer llamadas baratas a teléfonos normales, incluyendo números internacionales. No es necesario decir que estas características pueden ser extremadamente útiles. Algunos de los programas más populares de <strong> </strong>Voz sobre Protocolo de Internet (VoIP) incluyen al <a href="/es/glossary#Skype" title="Skype"><em>Skype</em></a>, <a href="https://jitsi.org">Jitsi</a>, <a href="http://www.google.com/hangouts" title="Google Hangouts">Google Talk</a> [2], y el <a href="https://messenger.yahoo.com/features/voice/" title="Yahoo! Messenger">Yahoo! Messenger</a> [3].</p>

<p>Normalmente, la comunicación por voz en Internet no es más segura que el correo electrónico no protegido y la mensajería instantánea. Cuando utilices conversaciones por voz para el intercambio de información sensible es importante escoger una herramienta que cifre la llamada durante todo el proceso, desde tu computadora hasta la computadora del destinatario. También es mejor utilizar software libre y de código abierto, preferiblemente aquellos que han sido revisados, probados y recomendados por una comunidad confiable. Tomando en cuenta los criterios expuestos anteriormente, recomendamos que pruebes Jitsi como tu elección para VoIP.</p>

<p>&nbsp;</p>

<table border="0" cellpadding="5" cellspacing="0">
	<tbody>
		<tr>
			<td><img align="middle" height="63" src="/sites/securitybkp.ngoinabox.org/files/u9/hand_web_trans.png" width="60" /> <strong>Parte Práctica: Empieza con la <a href="/en/Jitsi"><strong>Guía del Jitsi</strong></a></strong></td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<h3>Nota sobre la seguridad de Skype</h3>

<p>El <a href="/es/glossary#Skype" title="Skype"><em>Skype</em></a> es una herramienta común de mensajería instantánea y de VoIP que también soporta llamadas a líneas fijas y teléfonos móviles. A pesar de su popularidad, varios temas hacen de esta aplicación un elección insegura. Algunos de estos temas se describen a continuación.</p>

<p>Según indica Skype, encriptan tanto los mensajes comos las llamadas de voz, esto sólo sucedería cuando ambos lados de la comunicación se encuentren utilizando el programa Skype. Skype no cifra las llamadas a teléfonos o textos enviados por mensajes SMS.</p>

<p>Si ambos lados de la comunicación se encuentran utilizando el programa (genuino) Skype, su cifrado podrá hacer un poco más segura la llamada que aquellas realizadas de forma común por teléfono. Pero debido a que Skype es una programa de código cerrado, es imposible realizar una auditoría independiente y una evaluación de sus afirmaciones sobre cifrado, así mismo es imposible verificar que tan bien protege Skype a sus usuarios/as y su información y comunicación. El capitulo <a href="/es/chapter-1" title="1. Proteger tu computadora de software malicioso (malware) y piratas informáticos (hackers)"><strong>1. Proteger tu computadora de software malicioso (malware) y piratas informáticos (hackers)</strong></a> se ocupa de las virtudes del <a href="/es/glossary#FOSS" title="Software Libre y de Código Abierto (FLOSS)"><em>Software Libre y de Código Abierto (FOSS)</em></a> en su sección <strong>mantener actualizado tu software</strong>.</p>

<p>Como mencionamos anteriormente, no podemos recomendar Skype como herramienta segura de comunicación, es importante tomar algunas precauciones si uno/a decide utilizarlo para comunicar información sensible:</p>

<ul>
	<li>Descargue e instale Skype sólo de su sitio oficial www.skype.com para evitar un programa skype infectado con spyware. Siempre es importante que revises dos veces el URL para asegurarte de que estas conectado al sitio oficial. En algunos países el sitio de Skype está bloqueado y/o algunos sitios falsos anunciando que son el sitio oficial de Skype están funcionando. En estos casos, la versión disponible de Skype seguramente está infectado con malware diseñado para espiar cualqueir comunicación. Utiliza herramientas de evasión como se describe en el Capítulo 8 para conectarse al sitio de Skype y descargar una versión genuina del programa Skype y cuando quieras actualizar la última versión del programa.</li>
	<li>Es importante que cambies tu contraseña de Skype regularmente. Skype permite múltiples accesos a sesiones desde diferentes ubicaciones y no te informa de estas múltiples sesiones simultáneas. Esto es un gran riesgo si tu contraseña se encuentra comprometida, porque cualqueira con esa contraseña puede abrir su sesión. Todas las sesiones abiertas reciben todas las comunicaciones de texto y tienen acceso al historial de llamadas. Cambiar la contraseña es la única forma de deshabilitar las sesiones 'ilegales' (obligando a un reinicio de sesión).</li>
	<li>También es recomendable activar las configuraciones de privacidad del Skype para que no guarde el historial de los chat.</li>
	<li>También es recomendable deshabilitar la configuración del Skype que permite aceptar automáticamente los archivos enviados, ya que esto ha sido utilizado para introducir malware/spyware en las computadoras.</li>
	<li>Siempre verifica de forma independiente la identidad de la persona con quien te estás comunicando. Es más sencillo hacerlo cuando realizas chat con voz ya que sabes con quién estás hablando.</li>
	<li>Decide si quieres que tu nombre de usuario te identifica o relaciona con tu nombre verdadero o el nombre de tu organización.</li>
	<li>Es importante siempre buscar otras alternativas de comunicación. Skype podría no estar disponible en todo momento.</li>
	<li>Ten cuidado con lo que dices, desarrolla un sistema de código para conversar sobre temas sensibles sin utilizar una terminología específica.</li>
</ul>

<p>A pesar de la popularidad de Skype, las preocupaciones anteriormente expuestas cuestionan su uso seguro, por lo tanto recomendamos que inicies el uso de herramientas como Jitsi para VoIP y Pidgin, con el complemento Fuera de Registro (OTR), para mensajería instantánea segura.</p>


