

---

lang: es
community: guide
type: tactics
legacy: True
child: True
weight: 2
depth: 3
title: Hiding your sensitive information

---

<p>Un problema con el hecho de mantener una caja fuerte en tu casa u oficina, ni que decir de llevarla contigo, es que tiende a ser muy obvio. Muchas personas tienen preocupaciones razonables sobre autoincriminarse por medio del uso del <a href="/es/glossary#Cifrado" title="Cifrado"><em>cifrado</em></a>. Sólo porque las razones legítimas para cifrar<em> </em>datos exceden en número aquellas ilegítimas no hace esta amenaza menos real. Existen dos razones fundamentales por las que querrías evitar utilizar una herramienta como el <em><a href="/es/truecrypt_principal">TrueCrypt</a></em>: el riesgo de autoincriminación y el riesgo de identificar claramente la ubicación de tu información más sensible.</p>

<p>&nbsp;</p>

<h3 id="Considerarriesgoautoincriminacion">Considerar el riesgo de autoincriminación</h3>

<p>El <a href="/es/glossary#Cifrado" title="Cifrado"><em>cifrado</em></a> es ilegal en algunos países, lo que significa que descargar, instalar o utilizar software de este tipo podría ser un crimen en si. Y, si la policía, el ejército o los servicios de inteligencia se hallan entre los grupos de quienes estás buscando proteger tu información, entonces el violar estas leyes puede proporcionarles un pretexto ideal bajo el cual tus actividades pueden ser investigadas o tu organización perseguida. En realidad, amenazas como esta pueden no tener nada que ver con la legalidad de las herramientas en cuestión. En cualquier momento, el mero hecho de estar asociado con software de cifrado sería suficiente para exponerte a acusaciones de actividad criminal o espionaje—sin importar lo que realmente está dentro de los volúmenes cifrados-- por tanto debes pensar cuidadosamente respecto a si dichas herramientas son apropiadas o no para tu situación.</p>

<p>Si ese es el caso, tienes unas cuantas opciones:</p>

<ul>
	<li>Puedes evitar completamente el utilizar software de seguridad de datos, lo que requerirá que almacenes únicamente información no confidencial o que inventes un sistema de palabras en código para proteger elementos clave de tus archivos sensibles.</li>
	<li>Puedes confiar en una técnica llamada <a href="/es/glossary#Esteganografia" title="Esteganografía"><em>esteganografía</em></a> para esconder tu información sensible, en vez de cifrarla. Existen herramientas que pueden ayudarte con ello, pero el utilizarlas adecuadamente requiere una preparación muy cuidadosa, y todavía corres el riesgo de incriminarte a los ojos de cualquiera que descubra que estás usando esta herramienta.</li>
	<li>Puedes intentar almacenar toda tu información sensible en una cuenta de correo electrónico segura, pero ello requiere de una conexión de red confiable y un relativamente sofisticado nivel de conocimiento de computadoras y de servicios de Internet. Esta técnica también da por hecho que el <a href="/es/glossary#Cifrado" title="Cifrado"><em>cifrado</em></a> de red es menos incriminatorio que el cifrado de archivos y que puedes evitar copiar accidentalmente datos sensibles en tu disco duro y dejarlos ahí.</li>
	<li>Puedes mantener la información sensible lejos de tu computadora almacenándola en una memoria extraíble USB o en una disco duro portátil. Sin embargo, tales dispositivos son normalmente incluso más vulnerables que las computadoras a la perdida y a su confiscación, de modo que estar portando información sensible y no cifrada en uno de estos tipos de dispositivos es normalmente una mala idea.</li>
</ul>

<p>Si es necesario, puedes emplear varias de estas tácticas. Sin embargo, incluso en circunstancias en las que estás preocupado sobre la autoincriminación, lo más seguro será utilizar <a href="/es/glossary#TrueCrypt" title="TrueCrypt"><em>TrueCrypt</em></a>, mientras que a la vez tratas de camuflar tu volumen <a href="/es/glossary#Cifrado" title="Cifrado"><em>cifrado</em></a> de la mejor manera posible.</p>

<p>Si deseas que tu volumen cifrado sea menos llamativo, puedes renombrarlo para que se parezca a un tipo diferente de archivo. Utiliza la extensión '.iso', para camuflarlo como una imagen de CD, es una opción que funciona bien para grandes volúmenes de alrededor de 700 MB. Otras extensiones serían más realistas para pequeños volúmenes. Esto se asemeja a esconder tu caja fuerte detrás de una pintura en la pared de tu oficina. Este no será útil bajo una inspección detallada, pero ofrecerá alguna protección. También puedes renombrar el mismo programa <a href="/es/glossary#TrueCrypt" title="TrueCrypt"><em>TrueCrypt</em></a>, asumiendo que lo has guardado como harías con un archivo normal en tu disco duro o memoria extraíble USB, en vez de instalarlo como programa. La <a href="/es/truecrypt_principal" title="Guía del TrueCrypt"><strong>guía del TrueCrypt</strong></a> te explica cómo hacerlo.</p>

<p>&nbsp;</p>

<h3 id="Considerarriesgoidentificarinformacionsensible">Considerar el riesgo de identificar tu información sensible</h3>

<p>A menudo, debes preocuparte menos de las consecuencias de ser 'capturado' con software de <a href="/es/glossary#Cifrado" title="Cifrado"><em>cifrado</em></a> en tu computadora o en tu memoria extraíble USB y hacerlo más porque tu volumen cifrado indique específicamente donde almacenas la información que deseas proteger más. Aunque pueda ser cierto que nadie más pueda leerla, un intruso sabrá que está ahí, y que has dado pasos para protegerla. Ello te expone a varios métodos no técnicos a través de los cuales dicho intruso podría intentar tener acceso, como puede ser la intimidación, chantaje, interrogatorios o tortura. Es en este contexto que la opción o característica de denegación del <a href="/es/glossary#TrueCrypt" title="TrueCrypt"><em>TrueCrypt</em></a>, que se trata detalladamente más adelante, entra en juego.</p>

<p>La opción de denegación del <a href="/es/glossary#TrueCrypt" title="TrueCrypt"><em>TrueCrypt</em></a> es una de las maneras en las cuales este va más allá de lo ofrecido por otras herramientas de <a href="/es/glossary#Cifrado" title="Cifrado"><em>cifrado</em></a> de archivos. Esta opción puede interpretarse como una forma peculiar de <a href="/es/glossary#Esteganografia" title="Esteganografía"><em>esteganografía</em></a> que disfraza tu información más sensible como otra información oculta, menos sensible. Es análogo a instalar un astuto 'falso fondo' dentro de una no tan sútil caja fuerte. Si un intruso roba tus llaves, o te intimida para que le des la combinación de la caja fuerte, este encontrará algún material de 'señuelo' convincente, pero no la información que realmente te importa proteger.</p>

<p>Sólo tú sabes que tu caja fuerte contiene un compartimiento oculto en su parte trasera. Esto te permite 'negar' que estás manteniendo algún secreto más allá de lo que ya le has dado al intruso, y podría ayudar a protegerte en situaciones en las cuales por alguna razón debes reveler una contraseña. Tales razones podrían incluir amenazas legales o físicas a tu propia seguridad, o la de tus colegas, asociados, amigos y familiares. El propósito de la denegación es el de darte una oportunidad de escapar de una situación potencialmente peligrosa incluso si decides continuar protegiendo tus datos. Sin embargo, como se trata en la sección de <a href="#Considerarriesgoautoincriminacion" title="Considerar el riesgo de la autoincriminación"><strong>Considerar el riesgo de la autoincriminación</strong></a>, esta opción es mucho menos útil si el mero hecho de ser capturado con una caja fuerte en tu oficina es suficiente para provocar consecuencias inaceptables.</p>

<p>La opción de denegación del TrueCrypt funciona por medio del almacenamiento de un 'volumen oculto' dentro de un volumen común <a href="/es/glossary#Cifrado" title="Cifrado"><em>cifrado</em></a>. Este volumen oculto se abre mediante una contraseña diferente a la que normalmente utilizarías. Incluso si un intruso técnicamente sofisticado logra acceder a tu volumen común, él será incapaz de probar que existe uno oculto. Por supuesto, él puede saber perfectamente que <a href="/es/glossary#TrueCrypt" title="TrueCrypt"><em>TrueCrypt</em></a> es capaz de ocultar información de esta forma, de modo que no hay garantía de que la amenaza desaparezca tan pronto como reveles tu contraseña señuelo. Muchas personas utilizan el TrueCrypt sin habilitar su opción de denegación. Sin embargo, se considera en general que es imposible determinar, a través de un análisis, si un volumen cifrado contiene esta clase de 'falso fondo'. No obstante, es tu trabajo asegurarte de no revelar tu volumen oculto por medio de medios menos técnicos, tales como dejarlo abierto o permitir que otras aplicaciones creen accesos directos a los archivos que contiene. La sección de <a href="/es/chapter_4_3" title="Lecturas Adicionales"><strong>Lecturas Adicionales</strong></a>, que viene a continuación, te puede indicar cómo obtener información adicional al respecto.</p>

<p>&nbsp;</p>

<table border="0" cellpadding="5" cellspacing="0">
	<tbody>
		<tr>
			<td><em>Claudia: Bien, entonces vamos a arrojar algo de basura dentro del volumen común, y luego, podemos desplazar todos nuestros testimonios dentro del volumen oculto. ¿Tienes algunos viejos PDFs o algo que podamos utilizar? </em><br />
			<br />
			<em>Pablo: Justamente estuve pensando en ello, es decir, la idea es revelar la contraseña señuelo si no tenemos otra opción, ¿cierto? Pero para que ello sea convincente, necesitamos asegurarnos que dichos archivos se vean importantes, ¿no crees? De otro modo, ¿Por qué nos molestaríamos en cifrarlos? Tal vez deberíamos utilizar algunos documentos financieros no relacionados o una lista de contraseñas de sitios web o algo parecido.</em></td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>

<p>&nbsp;</p>


