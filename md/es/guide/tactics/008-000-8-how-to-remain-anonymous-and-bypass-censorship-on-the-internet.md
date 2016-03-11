

---

lang: es
community: guide
type: tactics
legacy: True
child: False
weight: 008
title:  8. How to remain anonymous and bypass censorship on the Internet

---

<p>Muchos países alrededor del mundo han instalado software que evita que los usuarios dentro de ese país puedan acceder a ciertos sitios web y servicios de Internet. Las compañías, colegios y bibliotecas públicas a menudo utilizan un software similar para proteger a sus empleados, estudiantes y clientes de material que consideran molesto o dañino. Este tipo de tecnología de filtrado viene en diferentes formas. Algunos filtros bloquean sitios de acuerdo a su <a href="/es/glossary#IP" title="Dirección de Protocolo de Internet (Dirección IP)"><em>dirección IP</em></a>, mientras otros ponen en su lista negra ciertos <a href="/es/glossary#Nombre_dominio" title="Nombre de dominio"><em>nombres de dominio</em></a> o buscan a través de todas las comunicaciones no cifradas en Internet palabras claves específicas.</p>

<p>Sin importar que métodos de filtrado se hallen presentes, casi siempre es posible evadirlos confiando en computadoras intermediarias, fuera del país, para acceder a servicios bloqueados para ti. Este proceso a menudo se llama <em>evasión de la censura</em>, o simplemente <a href="/es/glossary#Evasion" title="Evasión"><em>evasión</em></a>, y las computadoras intermedias se llaman <a href="/es/glossary#Proxy" title="Proxy"><em>proxies</em></a>. También existen proxies de diferentes formas. Este capitulo incluye un breve tratamiento de redes de anonimato multiproxy, seguido de una descripción más al detalle de proxies de evasión básica y de cuál es su forma de funcionamiento.</p>

<p>Ambos métodos son maneras efectivas de evadir los filtros de Internet, aunque el primero es más apropiado si estás dispuesto a sacrificar velocidad con el fin de mantener tus actividades en Internet lo más anónimas posibles. Si conoces y confías en la persona o en la organización que opera tu <a href="/es/glossary#Proxy" title="Proxy"><em>proxy</em></a>, o si el desempeño es más importante para ti que el anonimato, entonces un proxy de <a href="/es/glossary#Evasion" title="Evasión"><em>evasión</em></a> básica te será más útil.</p>

<p>&nbsp;</p>

<h3 id="Contexto">Contexto</h3>

<table border="0" cellpadding="5" cellspacing="0">
	<tbody>
		<tr>
			<td><em>Mansour y Magda son hermanos, en un país de habla árabe, que mantienen blog en la cual anónimamente hacen público abusos de derechos humanos y hacen campaña por un cambio político. Las autoridades en su país no han sido capaces de cerrar su sito web, debido a que está alojado en otro país, pero a menudo han intentado conocer la identidad de los administradores del blog a través de otros activistas. A Mansour y Magda les preocupa que las autoridades sean capaces de vigilar sus actualizaciones y saber quiénes son. Además, desean prepararse por si finalmente el gobierno filtra su sitio web, para no sólo continuar actualizándolo, sino también poder proporcionar un buen consejo de evasión para sus lectores dentro de su propio país, quienes de otro modo perderían acceso al blog.</em></td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>

<h3 id="Quepuesdesaprender">¿Qué puedes aprender de esta capítulo?</h3>

<ul>
	<li>Acceder a un sitio web que esté bloqueado dentro de tu país</li>
	<li>Evitar que los sitios web que visitas sepan tu ubicación</li>
	<li>Garantizar que ni tu <a href="/es/glossary#ISP" title="Proveedor de Servicios de Internet (ISP)"><em>Proveedor de Servicios de Internet (ISP</em></a><em><a href="/es/glossary#ISP" title="Proveedor de Servicios de Internet (ISP)">)</a> </em>ni una organización de vigilancia en tu país puedan determinar qué sitios web o servicios de Internet visitas</li>
</ul>

<p>&nbsp;</p>


