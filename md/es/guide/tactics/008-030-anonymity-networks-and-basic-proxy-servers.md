

---

lang: es
community: guide
type: tactics
legacy: True
child: True
weight: 3
depth: 3
title: Anonymity networks and basic proxy servers

---

<h3 id="Redesanonimas">Redes anónimas<span class="anchor"> </span></h3>

<p>Las redes anónimas normalmente 'hacen rebotar' tu tráfico de Internet entre varios <a href="/es/glossary#Proxy" title="Proxy"><em>proxies</em></a> seguros con el fin de disfrazar de dónde vienes y a qué estas tratando de acceder. Esto puede reducir significativamente la velocidad a la cual eres capaz de descargar las páginas web y otros servicios de Internet. Sin embargo, en el caso de <em><a href="/es/glossary#Tor" title="Tor">Tor</a></em>, este también te proporciona un medio fiable, seguro y público de evasión que te ahorra el preocuparte si confías o no en las personas que operan tus proxies y los sitios web que visitas. Como siempre, debes garantizar que tienes una conexión cifrada, utilizando <a href="/es/glossary#HTTPS" title="HTTPS"><em>HTTPS</em></a> para un sitio web seguro antes de intercambiar información sensible, tal como contraseñas y correos electrónicos, a través de un navegador.</p>

<p>Tienes que instalar el software para utilizar <em><a href="/es/glossary#Tor" title="Tor">Tor</a></em>, pero el resultado es una herramienta que te proporciona anonimato así como evasión. Cada vez que te conectas a la red de Tor, seleccionas una ruta aleatoria a través de tres proxies seguros de Tor. Esto garantiza que ni tu <em><a href="/es/glossary#ISP" title="Proveedor de Servicio de Internet (ISP)">Proveedor de Servicio de Internet (ISP)</a></em> ni los mismos proxies conozcan tanto la <em><a href="/es/glossary#IP" title="Dirección de Protocolo de Internet (Dirección IP)">dirección IP</a></em> de tu computadora y como la ubicación de los servicios de Internet que solicitas. Puedes aprender más sobre esta herramienta en la Guía del Tor.</p>

<p>&nbsp;</p>

<table border="0" cellpadding="5" cellspacing="0">
	<tbody>
		<tr>
			<td><img align="middle" height="63" src="/sites/securitybkp.ngoinabox.org/files/u9/hand_web_trans.png" width="60" /> <strong>Parte Práctica: Empieza con la <a href="/es/tor_principal" title="Guía del Tor"><strong>Guía del Tor</strong></a> </strong></td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>Una de las fortalezas de <em><a href="/es/glossary#Tor" title="Tor">Tor</a></em> es que no sólo trabaja con navegadores sino que puede ser utilizado con varios tipos de software de Internet. Los programas de correo electrónico, entre ellos Mozilla <a href="/es/glossary#Thunderbird" title="Thunderbird"><em>Thunderbird</em></a>, y los programas de mensajería instantánea, incluyendo <a href="/es/glossary#Pidgin" title="Pidgin"><em>Pidgin</em></a>, pueden ser operados a través del Tor, ya sea para acceder a servicios filtrados o para esconder el uso que le das a dichos servicios.</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<h3 id="Proxiesbasicosevasion">Proxies básicos de evasión<span class="anchor"> </span></h3>

<p>Existen tres importantes características que debes considerar cuando seleccionas un <a href="/es/glossary#Proxy" title="Proxy"><em>proxy</em></a> básico de evasión. Primero, ¿es una herramienta basada en la web, o requiere que cambies las opciones o que instales software en tu computadora? Segundo, ¿es seguro? Tercero, ¿es público o privado?</p>

<h4 id="Proxiesbasadosweb">Proxies basados en la web y otros:</h4>

<p>Los <a href="/es/glossary#Proxy" title="Proxy"><em>proxies</em></a> basados en la web son probablemente los más fáciles de usar. Sólo requieren que apuntes tu navegador hacia una página web proxy, ingreses la dirección filtrada que deseas ver y pulses un botón. El proxy entonces mostrará el contenido solicitado dentro de su propia página web. Normalmente puedes acceder a los enlaces o ingresar una nueva dirección en el proxy si deseas ver una nueva página. No necesitas instalar ningún software o cambiar alguna opción de tu navegador, lo cual significa que los proxies basados en la web son:</p>

<ul>
	<li>Fáciles de usar</li>
	<li>Accesibles desde computadoras públicas, como aquellas en los Internet cafés, las cuales no permiten instalar programas o cambiar opciones</li>
	<li>Son potencialmente seguros si te preocupa ser 'sorprendido' con software de evasión en tu computadora.</li>
</ul>

<p>Los <a href="/es/glossary#Proxy" title="Proxy"><em>proxies</em></a> basados en la web también tienen ciertas desventajas. No siempre muestran correctamente las páginas, y muchos proxies basados en la web no lograrán descargar sitios web complejos, entre ellos los que presentan archivos de audio o contenidos de video. Además, mientras que todo proxy se volverá más lento cuantos más usuarios lo estén utilizando, esto puede ser especialmente problemático con los proxies públicos basados en la web. Y, obviamente, los proxies basados en la web sólo funcionan para páginas web. No puedes, por ejemplo, utilizar un programa de mensajería instantánea o un cliente de correo electrónico para acceder a servicios bloqueados a través de un proxy basado en la web. Finalmente, los proxies seguros basados en la web ofrecen una confidencialidad limitada debido a que ellos mismos deben acceder y modificar la información de retorno hacia ti proveniente de los sitios web que visitas. Si no lo hicieran, serías incapaz de pulsar en un enlace sin dejar el proxy, realizando una conexión directa con la página web objetivo. Esto se trata más adelante en la sección siguiente.</p>

<p>Otros tipos de <a href="/es/glossary#Proxy" title="Proxy"><em>proxies</em></a> generalmente requieren que instales un programa o configures una dirección externa de un proxy en tu navegador o sistema operativo. En el primer caso, tu programa de evasión normalmente proporcionará alguna forma de activar y desactivar la herramienta, para indicarle a tu navegador si debe o no utilizar el proxy. El software de este tipo a menudo te permite cambiar automáticamente de proxies si uno de ellos es bloqueado, como se trató anteriormente. En el segundo caso, necesitarás saber la dirección correcta del proxy, la cual cambiará si dicho proxy es bloqueado o se vuelve tan lento que deja se der útil.</p>

<p>Aunque esto puede ser ligeramente más difícil de utilizar que un <a href="/es/glossary#Proxy" title="Proxy"><em>proxy</em></a> basado en la web, este método de evasión está mejor dotado para mostrar páginas complejas de manera correcta y tomará mucho más tiempo en ralentizarse. Además, pueden encontrarse proxies para varias aplicaciones diferentes de Internet. Los ejemplos incluyen proxies HTTP para navegadores, SOCKS para programas de correo electrónico y mensajería (chat) y VPN, que pueden redireccionar todo tu tráfico de Internet para evitar el filtrado.</p>

<h4>Proxies seguros e inseguros:</h4>

<p>Un <a href="/es/glossary#Proxy" title="Proxy"><em>proxy</em></a> seguro, en este capitulo, se refiere a cualquier proxy que permita conexiones <em><a href="/es/glossary#Cifrado" title="Cifrado">cifradas</a></em> de sus usuarios. Un proxy inseguro te permitirá evadir muchos tipos de filtro pero fracasará si tu conexión de Internet está siendo escaneada en busca de palabras claves o de direcciones de páginas web. Es especialmente malo utilizar un proxy inseguro para acceder a sitios web que normalmente están cifrados, tales como aquellos de cuentas de correo electrónico con interfaz web y páginas web bancarias. Al hacerlo, podrías estar exponiendo información sensible que normalmente estaría escondida. Y, como se mencionó anteriormente, los proxies inseguros a menudo son más fáciles de descubrir y bloquear por parte de aquellos que actualizan el software y la políticas de filtrado de Internet. En definitiva, el hecho de que existan proxies libres, rápidos y seguros supone que existen muy pocas razones para decidirse por uno inseguro.</p>

<p>Sabrás si un <a href="/es/glossary#Proxy" title="Proxy"><em>proxy</em></a> basado en la web es seguro o inseguro si puedes acceder a las mismas páginas web del proxy utilizando direcciones <a href="/es/glossary#HTTPS" title="HTTPS"><em>HTTPS</em></a>. Del mismo modo que con los servicios de correo con interfaz web, las conexiones seguras e inseguras pueden ser admitidas, de modo que debes estar seguro de utilizar una dirección segura. Puede pasar que, en dichos casos, se te pedirá aceptar una 'advertencia de certificado de seguridad' de tu navegador con el fin de continuar. Este es el caso para el proxy <a href="/es/glossary#Peacefire" title="Peacefire"><em>Peacefire</em></a>, que se trata a continuación. Advertencias como estas te indican que alguien, como tu <a href="/es/glossary#ISP" title="Proveedor de Servicio de Internet (ISP)"><em>Proveedor de Servicio de Internet (ISP)</em></a> o un <a href="/es/glossary#Hacker" title="Pirata informático (hacker)"><em>pirata informático (hacker)</em></a>, podría estar vigilando tu conexión al proxy. A pesar de estas advertencias, podría ser una buena idea utilizar proxies seguros en la medida de lo posible. Sin embargo, cuando confíes en tales proxies para evasión, debes evitar visitar sitios web seguros, a menos que verifiques la huella digital <a href="/es/glossary#SSL" title="Capa de Conexión Segura (SSL)"><em>Capa de Conexión Segura (SSL)</em></a> del proxy. Con el fin de hacer esto, necesitarás una manera de comunicarte con el administrador del proxy. <strong>En general, es mejor evitar ingresar contraseñas o intercambiar información sensible cuando utilices un proxy web</strong>.</p>

<p>También debes evitar acceder a información sensible a través de un <a href="/es/glossary#Proxy" title="Proxy"><em>proxy</em></a> basado en la web a menos que confíes en la persona que lo dirige. Esto se aplica sin importar si ves o no una advertencia de certificado de seguridad cuando visitas el proxy. Incluso se aplica si conoces lo suficiente al operador del proxy para verificar la huella digital del servidor antes de dirigir tu navegador a aceptar la advertencia. Cuando confías en un único proxy para la evasión, su administrador conocerá en todo momento tu <em><a href="/es/glossary#IP" title="Dirección de Protocolo de Internet (Dirección IP)">dirección IP</a></em> y el sitio web al que estás accediendo. Sin embargo, es mucho más importante considerar que si ese proxy está basado en la web, un operador malicioso podría tener acceso a toda la información que pasa entre tu navegador y los sitios web que visitas, incluyendo el contenido de tu correo con interfaz web y tus contraseñas.</p>

<p>Para los <a href="/es/glossary#Proxy" title="Proxy"><em>proxies</em></a> que no están basados en la web, debes investigar un poco para determinar si admiten conexiones seguras o inseguras. Todas los proxies y las redes anónimas recomendadas en este capitulo son seguros.</p>

<h4>Proxies privados y públicos:</h4>

<p>Los <a href="/es/glossary#Proxy" title="Proxy"><em>proxies</em></a> públicos aceptan conexiones de cualquiera, mientras que los privados normalmente requieren un nombre de usuario y una contraseña. Mientras que los proxies públicos tienen la obvia ventaja de estar disponibles libremente, asumiendo que puedan ser hallados, estos tienden a saturarse rápidamente. Como resultado de ello, aunque los proxies públicos sean técnicamente tan sofisticados y bien mantenidos como los privados, estos son a menudo relativamente lentos. Finalmente, los proxies privados tienden a ser dirigidos ya sea por lucro o por administradores que crean cuentas para sus usuarios a quienes conocen personal o socialmente. Debido a esto, es generalmente muy fácil determinar qué motiva a un operador de un proxy privado. Sin embargo, no debes asumir que los proxies privados son por tanto básicamente más fiables. Después de todo, algunos de estos servicios han llegado a exponer a sus usuarios en el pasado para lucrarse.</p>

<p><a href="/es/glossary#Proxy" title="Proxy"><em>Proxies</em></a> simples, inseguros y públicos pueden a menudo encontrarse ingresando términos como 'proxy público' en un buscador, pero no debes confiar en proxies descubiertos de esta manera. Dada la oportunidad, es mejor utilizar un proxy seguro y privado conducido por personas que conoces y en las que confías, ya sea personalmente o por su reputación, y quienes tienen las habilidades técnicas para mantener su servidor seguro. Ya sea que utilices o no un proxy basado en la web dependerá de tus particulares necesidades y preferencias. En cualquier momento en que utilices un proxy para evasión, es una buena idea utilizar también el navegador <a href="/es/glossary#Firefox" title="Firefox"><em>Firefox</em></a> e instalar el complemento <a href="/es/glossary#NoScript" title="NoScript"><em>NoScript</em></a>, como se trata en la <a href="/es/firefox_principal" title="Guía del Firefox"><strong>Guía del Firefox</strong></a>. El hacerlo puede ayudarte a protegerte tanto de proxies maliciosos como de sitios web que pueden tratar de descubrir tu verdadera <em><a href="/es/glossary#IP" title="Dirección de Protocolo de Internet (Dirección IP)">dirección IP</a></em>. Finalmente, ten en cuenta que incluso un proxy <a href="/es/glossary#Cifrado" title="Cifrado"><em>cifrado</em></a> no tornará un sitio web inseguro en uno seguro. Debes garantizar que tienes una conexión <a href="/es/glossary#HTTPS" title="HTTPS"><em>HTTPS</em></a> antes de enviar o recibir información sensible.</p>

<p>Si eres incapaz de encontrar en tu país una persona, una organización o una compañía cuyo servicio <a href="/es/glossary#Proxy" title="Proxy"><em>proxy</em></a> consideres fiable, asequible y accesible, debes pensar en utilizar la red anónima de <em><a href="/es/glossary#Tor" title="Tor">Tor</a></em>, de la cual nos ocupamos anteriormente en la parte de <a href="/es/chapter_8_3#Redesanonimas" title="Redes anónimas"><strong>Redes anónimas</strong></a>.</p>

<p>&nbsp;</p>


