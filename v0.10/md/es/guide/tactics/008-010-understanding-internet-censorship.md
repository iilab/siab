

---

lang: es
community: guide
type: tactics
legacy: True
child: True
weight: 1
depth: 3
title: Understanding Internet censorship

---

<p>Las investigaciones llevadas a cabo por organizaciones como <a href="http://opennet.net/" title="OpenNet Initiative">OpenNet Initiative (ONI)</a> [1] y <a href="http://www.rsf.org/" title="Reporteros Sin Fronteras">Reporteros Sin Fronteras (RSF)</a> [2] indican que muchos países filtran una amplia variedad de contenido social, político y de 'seguridad nacional', aunque raramente publican listas precisas de lo que ha sido bloqueado. Naturalmente, aquellos que desean controlar el acceso de sus ciudadanos a la Internet también hacen un esfuerzo especial para bloquear <a href="/es/glossary#Proxy" title="Proxy"><em>proxies</em></a> y sitios web conocidos que ofrecen herramientas e instrucciones para ayudar a las personas a evadir estos filtros.</p>

<p>A pesar de la garantía de libre acceso a la información consagrada en el Artículo 19 de la Declaración Universal de los Derechos Humanos, el número de países involucrados en la censura de Internet se ha incrementado espectacularmente en los últimos años. Sin embargo, a medida que la práctica de filtrado de Internet se disemina en el mundo, de igual manera lo hace el acceso a las herramientas de evasión que han sido creadas, utilizadas y publicitadas por activistas, programadores y voluntarios.</p>

<p>Antes de explorar las distintas maneras de evadir la censura en Internet, primero debes desarrollar un entendimiento básico de cómo funcionan estos filtros. Para hacerlo, es muy útil considerar un modelo altamente simplificado de tu conexión a Internet.</p>

<p>&nbsp;</p>

<h3 id="Tuconexioninternet">Tu conexión a Internet</h3>

<p><img border="0" src="/sites/securitybkp.ngoinabox.org/security/files/img/1-es.png" /></p>

<p>El primer paso de tu conexión a la Internet se hace típicamente a través del <a href="/es/glossary#ISP" title="Proveedor de Servicio de Internet (ISP)"><em>Proveedor de Servicio de Internet (ISP)</em></a> en tu casa, oficina, colegio, biblioteca o Internet café. El Proveedor de Servicio de Internet (ISP) le asigna a tu computadora una <a href="/es/glossary#IP" title="Dirección de Protocolo de Internet (Dirección IP)"><em>dirección IP</em></a>, la cual puede ser utilizada por varios servicios de Internet para identificarte y enviarte información, tales como correos electrónicos y páginas web que solicites. Cualquiera que conozca tu dirección IP puede saber más o menos en que ciudad te hallas. Sin embargo, algunas organizaciones bien conectadas en tu país pueden utilizar esta información para determinar tu ubicación precisa.</p>

<ul>
	<li><strong>Tu Proveedor de Servicio de Internet (ISP)</strong> sabrá en que edificio estás o que línea telefónica estás utilizando si accedes a Internet a través de un módem.</li>
	<li><strong>Tu Internet café, biblioteca o negocio</strong> sabrá qué computadora estuviste utilizando en un momento determinado, así como a qué puerto o a qué punto de acceso inalámbrico estuviste conectado.</li>
	<li><strong>Las agencias gubernamentales</strong> pueden conocer todos estos detalles, como resultado de su influencia sobre las organizaciones arriba mencionadas.</li>
</ul>

<p>Actualmente, tu <em><a href="/es/glossary#ISP" title="Proveedor de Servicio de Internet (ISP)"><em>Proveedor de Servicio de Internet (ISP)</em></a></em> descansa en la infraestructura de la red en tu país para conectar a sus usuarios, incluyéndote a ti, con el resto del mundo. En el otro extremo de tu conexión, el sitio web o el servicio de Internet al cual estás accediendo pasa a través de un proceso similar, habiendo recibido su propia dirección IP de su Proveedor de Servicio de Internet (ISP) en su propio país. Incluso sin todos los detalles técnicos, un modelo básico como este puede ser útil cuando piensas en las varias herramientas que te permiten evitar los filtros y mantenerte anónimo en la Internet.</p>

<p>&nbsp;</p>

<h3>Cómo son bloqueados los sitios web</h3>

<p>Esencialmente, cuando vas a visualizar una página web, le estás mostrando la <a href="/es/glossary#IP" title="Dirección de Protocolo de Internet (Dirección IP)"><em>dirección IP</em></a> del sitio a tu <em><a href="/es/glossary#ISP" title="Proveedor de Servicio de Internet (ISP)"><em>Proveedor de Servicio de Internet (ISP)</em></a></em> y solicitándole conectarte con el Proveedor de Servicio de Internet (ISP) del servidor web. Y - si tienes una conexión de Internet no filtrada - hará justamente eso. Sin embargo, si te encuentras en un país que censura Internet, este consultará primero la <em><a href="/es/glossary#Lista_negra" title="Lista negra">lista negra</a></em> de sitios web prohibidos y luego decidirá si accede o no a tu solicitud.</p>

<p>En algunos casos, puede haber una organización central que maneja el filtrado en lugar de los mismos <em><a href="/es/glossary#ISP" title="Proveedor de Servicio de Internet (ISP)"><em>Proveedor de Servicio de Internet (ISP)</em></a></em>. A menudo, una <em><a href="/es/glossary#Lista_negra" title="Lista negra">lista negra</a></em> contendrá <em><a href="/es/glossary#Nombre_dominio" title="Nombre de dominio">nombres de dominio</a></em>, tales como www.blogger.com, en vez de <em><a href="/es/glossary#IP" title="Dirección de Protocolo de Internet (Dirección IP)"><em>direcciones IP</em></a></em>. Y, en algunos países, el software de filtrado controla tu conexión, en vez de intentar bloquear direcciones específicas en Internet. Este tipo de software escanea las solicitudes que hiciste y las páginas que regresan a ti, buscando palabras claves sensibles para luego decidir si te permite o no ver los resultados.</p>

<p>Y, para empeorar las cosas, cuando una página web es bloqueada, podrías ni siquiera saberlo. Aunque algunos filtros proporcionan una 'página de bloqueo' que explica porque una página en particular ha sido censurada, otras muestran mensajes de error engañosos. Estos mensajes pueden decir que la página no puede ser encontrada, por ejemplo, o que la dirección fue mal ingresada.</p>

<p>En general, lo más fácil es asumir el peor de los casos en cuanto a la censura de Internet, en vez de intentar investigar todas las fortalezas y debilidades de las tecnologías de filtrado utilizadas en tu país. En otras palabras, puedes asumir que:</p>

<ul>
	<li>Tu tráfico en Internet está controlado por palabras claves.</li>
	<li>El filtrado está implementado directamente al nivel del <em><em><a href="/es/glossary#ISP" title="Proveedor de Servicio de Internet (ISP)"><em>Proveedor de Servicio de Internet (ISP)</em></a><em>.</em></em></em></li>
	<li>Los sitios bloqueados son considerados en <em><a href="/es/glossary#Lista_negra" title="Lista negra">listas negras</a></em> tanto por las <em><a href="/es/glossary#IP" title="Dirección de Protocolo de Internet (Dirección IP)"><em>direcciones IP</em></a></em> como por <em><a href="/es/glossary#Nombre_dominio" title="Nombre de dominio">nombres de dominio</a>.</em></li>
	<li>Se te pueden dar razones engañosas o desorientadoras para explicar porque un sitio bloqueado no se descarga.</li>
</ul>

<p>Debido a que las herramientas de evasión más efectivas pueden ser utilizadas sin importar que métodos de filtrado están en funcionamiento, generalmente no hace daño hacer esta asunción pesimista.</p>

<p>&nbsp;</p>

<table border="0" cellpadding="5" cellspacing="0">
	<tbody>
		<tr>
			<td><em>Mansour: Entonces, si un día me encuentro con que no puedo acceder al blog, pero un amigo en otro país puede verlo sin problemas, ¿eso significa que el gobierno lo ha bloqueado? </em><br />
			<br />
			<em>Magda: No necesariamente. Podría ser algún problema que sólo afecta a las personas que están tratando de acceder al sitio web desde aquí. O, podría ser algún problema con tu computadora que sólo se muestra con ciertos tipos de páginas web. Sin embargo estás en la ruta correcta. Podrías también intentar visitarla mientras utilizas una herramienta de evasión. Después de todo, la mayoría de estas herramientas descansan en servidores proxy externos, cuyo funcionamiento se parece al hecho de pedirle a un amigo en otro país que pruebe un sitio web para ti, excepto que puedes hacerlo por ti mismo</em></td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>

<p>&nbsp;</p>


