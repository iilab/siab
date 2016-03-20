

---

lang: es
community: guide
type: tactics
legacy: True
child: True
weight: 1
depth: 3
title: Encrypting your information

---

<p>&nbsp;</p>

<table border="0" cellpadding="5" cellspacing="0">
	<tbody>
		<tr>
			<td>
			<p><em>Pablo: ¡Pero mi computadora ya está protegida por la contraseña de acceso de Windows! ¿No es eso lo suficientemente bueno? </em><br />
			<br />
			<em>Claudia: En realidad, las contraseñas de acceso de Windows son normalmente muy fáciles de descifrar. Además, cualquiera que ponga sus manos en tu computadora por el tiempo suficiente para reiniciar tu computadora con un LiveCD en la unidad lectora puede copiar tus datos sin siquiera tener que preocuparse sobre la contraseña. Si esta persona logra llevarse la computadora por un momento te encontrarás con peores problemas aún. Por ello no es sólo la contraseña de Windows de lo que necesitas preocuparte. Tampoco debes confiar en las contraseñas de Microsoft Word o de Adobe Acrobat.</em></p>
			</td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>El <em><a href="/es/glossary#Cifrado" title="Cifrado">cifrar</a> </em>tu información se parece un poco a mantenerla encerrada en una caja fuerte. Sólo aquellos que tengan la llave o conozcan la combinación de la cerradura pueden acceder a ella. La analogía es particularmente apropiada para <a href="/es/glossary#TrueCrypt" title="TrueCrypt"><em>TrueCrypt</em></a> y herramientas similares, las cuales crean contenedores seguros llamados 'volúmenes cifrados' en vez de simplemente proteger los archivos de uno en uno. Puedes poner un gran número de archivos dentro de un volumen cifrado, pero estas herramientas no protegerán los archivos que estén almacenados en otro lugar en tu computadora o en tu memoria extraíble USB.</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<table border="0" cellpadding="5" cellspacing="0">
	<tbody>
		<tr>
			<td><img align="middle" height="63" src="/sites/securitybkp.ngoinabox.org/files/u9/hand_web_trans.png" width="60" /> <strong>Parte Práctica: Empieza con la <a href="/es/truecrypt_principal" title="Guía del TrueCrypt"><strong>Guía del TrueCrypt</strong></a></strong></td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>Mientras que otros software puede proporcionarte un <em><a href="/es/glossary#Cifrado" title="Cifrado">cifrado</a> </em>que sea igualmente fuerte, <a href="/es/glossary#TrueCrypt" title="TrueCrypt"><em>TrueCrypt</em></a> contiene varias características importante que te permitirá diseñar tu estrategia de seguridad informática. Te da la posibilidad de encriptar permanentemente todo el disco de tu computadora incluyendo todos tus archivos, todos tus archivos temporales creados durante tu trabajo, todos los programas que hayas instalado y todos los archivos del sistema operativo Windows. Truecrypt proporciona respaldo para llevar volúmenes cifrados en dispositivos portátiles de almacenamiento. Y provee la opción de 'denegación' descrita en la sección <a href="/es/chapter_4_2" title="Ocultar tu información sensible"><strong>Ocultar tu información sensible</strong></a>. Adicionalmente TrueCrypt es un programa <em><a href="/es/glossary#FOSS" title="Cifrado">gratuito y de código abierto</a></em>.</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<table border="0" cellpadding="5" cellspacing="0">
	<tbody>
		<tr>
			<td>
			<p><em>Pablo: Está bien, ahora sí que me tienes preocupado. ¿Qué sucede con los otros usuarios de la misma computadora? ¿Esto significa que pueden leer documentos en la carpeta de 'Mis Documentos'? </em><br />
			<br />
			<em>Claudia: ¡Me gusta la manera en la que piensas! Si tu contraseña de Windows no te protege de los intrusos ¿cómo te podría proteger de otras personas con cuentas en la misma computadora?. </em></p>

			<p><em>De hecho, tu carpeta de Mis Documentos está normalmente visible para cualquiera, de modo que otros usuarios no tendrían siquiera que hacer algo inteligente para leer tus archivos no cifrados. Sin embargo, tienes razón, incluso si la carpeta se hace 'privada,' todavía no estás a salvo a menos que utilices algún tipo de cifrado. </em></p>
			</td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>

<p>&nbsp;</p>

<h3 id="Consejosutilizarcifradoarchivos">Consejos para utilizar el cifrado de archivos de manera segura</h3>

<p>&nbsp;</p>

<p>Almacenar datos confidenciales puede ser un riesgo para ti y para aquellos con quien trabajas. El <a href="/es/glossary#Cifrado" title="Cifrado"><em>cifrado</em></a> reduce el riesgo pero no lo elimina. El primer paso para proteger información sensible es el reducir la cantidad de la misma que almacenas. A menos que tengas una buena razón para almacenar un archivo en particular, o una categoría particular de información dentro de un archivo, simplemente deberías borrarla (dirígete al capítulo <a href="/es/chapter-6" title="6. Destruir información sensible"><strong>6. Destruir información sensible</strong></a> para obtener más información de como hacerlo de manera segura.) El segundo paso es utilizar una buena herramienta de cifrado de archivos, tal como <a href="/es/glossary#TrueCrypt" title="TrueCrypt"><em>TrueCrypt</em></a>.</p>

<p>&nbsp;</p>

<table border="0" cellpadding="5" cellspacing="0">
	<tbody>
		<tr>
			<td><em>Claudia: Bien, tal vez no necesitamos en realidad almacenar información que podría identificar a las personas que nos dieron sus testimonios. ¿Qué opinas? </em><br />
			<br />
			<em>Pablo: De acuerdo. Probablemente deberíamos escribir lo menos posible sobre ello. Además, deberíamos pensar en un código simple que podamos utilizar para proteger los nombres y las ubicaciones que tenemos que registrar de todas maneras. </em></td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>Regresando a la analogía de la caja fuerte cerrada, hay algunas cosas que debes tener en cuenta cuando utilices <a href="/es/glossary#TrueCrypt" title="TrueCrypt"><em>TrueCrypt</em></a> u otras herramientas similares. No importa cuán robusta sea caja fuerte, no te hará mucho bien si dejas la puerta abierta. Cuando tu volumen TrueCrypt está 'montado' (el momento en que puedes acceder a su contenido), tus datos pueden ser vulnerables, de modo que debe mantenerse cerrado excepto cuando estás, ciertamente, leyendo o modificando los archivos dentro de este.</p>

<p>&nbsp;</p>

<p>Existen algunas situaciones en las que es especialmente importante que recuerdes no dejar montado tu volumen <a href="/es/glossary#Cifrado" title="Cifrado"><em>cifrado</em></a>:</p>

<ul>
	<li>Desconéctalo cuando debas alejarte de tu computadora por cualquier lapso de tiempo. Incluso si normalmente dejas tu computadora funcionando toda la noche, debes asegurarte de no dejar tus archivos sensibles accesibles a intrusos físicos o remotos mientras estás ausente.</li>
	<li>Desconéctalo antes de poner tu computadora a dormir. Esto se aplica a las opciones de 'suspendido' e 'hibernación', las cuales son comúnmente usadas en computadoras portátiles pero que pueden estar presentes también en las computadoras de escritorio.</li>
	<li>Desconéctalo antes de permitir a alguien usar tu computadora. Cuando pases tu computadora portátil a través de un control de seguridad o frontera, es importante que desconectes todos los volúmenes <a href="/glossary#Cifrado" title="Cifrado"><em>cifrados</em></a> y que apagues completamente tu computadora.</li>
	<li>Desconéctalo antes de insertar una memoria extraíble USB no confiable u otro dispositivo de almacenamiento externo, incluyendo aquellos que pertenezcan a tus amigos y colegas.</li>
	<li>Si mantienes un volumen <a href="/es/glossary#Cifrado" title="Cifrado"><em>cifrado</em></a> en una memoria extraíble USB, recuerda que el solo hecho de extraer el dispositivo puede no desconectar inmediatamente el volumen. Incluso si necesitas proteger tus archivos con urgencia, necesitas desmontar el volumen de forma apropiada, luego desconectar la unidad externa o la memoria extraíble, y luego retirar el dispositivo. Puedes practicar varias veces hasta que halles la forma más rápida de hacer todas estas cosas.</li>
</ul>

<p>Si decides mantener tu volumen <a href="/es/glossary#TrueCrypt" title="TrueCrypt"><em>TrueCrypt</em></a> en una memoria extraíble USB, también puedes mantener una copia del programa TrueCrypt en ella. Esto te permitirá tener acceso a tus datos en las computadoras de otras personas. Sin embargo, las reglas normales todavía se aplican: si no confías en que la máquina esté libre de <a href="/es/glossary#Malware" title="Software malicioso (malware)"><em>software malicioso (malware)</em></a>, probablemente no deberías ingresar tus contraseñas o acceder a datos sensibles.</p>

<p>&nbsp;</p>


