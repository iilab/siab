

---

lang: es
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: Advanced Configurations and Settings

---

<p><strong>Importante:</strong> Al momento de instalar el <strong>Comodo Firewall Pro</strong>, se te preguntará si tienes "algún otro cortafuegos (firewall) instalado por terceros." Sólo debes utilizar un cortafuegos en tu computadora. Si tienes otro cortafuegos activo en tu computadora este debe ser desinstalado antes de que puedas instalar el Comodo Firewall Pro.</p>

<p><strong>Nota: El Windows XP Edición Profesional (Paquete de Servicio dos (Service Pack Two) y versiones más avanzadas)</strong> tiene el <strong>Cortafuegos de Windows (Windows Firewall)</strong> activado automáticamente. Comodo Firewall Pro normalmente te pedirá desactivar el cortafuegos automáticamente. Si no lo hace puedes desactivarlo manualmente ejecutando los siguientes pasos:</p>

<p><strong>Paso 1. Selecciona: Inicio &gt; Configuración &gt; Panel de Control &gt; Firewall de Windows</strong> para activar la siguiente pantalla.</p>

<p><img alt="CPF/screenshots-es/43.png" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo-es/43.png" title="CPF/screenshots-es/43.png" /></p>

<p><em>Figura 1: Pantalla del Firewall de Windows</em></p>

<p><strong>Paso 2. Activa</strong> la opción <em>Desactivado (no se recomienda)</em>.</p>

<p><strong>Paso 3. Pulsa</strong> <img alt="CPF/screenshots-es/39.png" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo-es/39.png" title="CPF/screenshots-es/39.png" /> para desactivar el Firewall de Windows.</p>

<p>&nbsp;</p>

<h3 id="a2.1PermitiryDenegarAcceso">2.1 Permitir y Denegar Acceso</h3>

<p>Después de haber instalado el <strong>Comodo Firewall Pro</strong>, este te pedirá fijar los permisos o derechos de acceso que controlen la forma en que los distintos programas en tu computadora acceden a Internet. En general, las solicitudes válidas deben ser permitidas y las maliciosas denegadas. Sin embargo, ¡se necesita de un poco de experiencia para diferenciar unas de otras!</p>

<p>Cada vez que se realice un pedido, aparecerá una pantalla de <em>Alerta de Seguridad</em> similar a la que se muestra a continuación:</p>

<p><img alt="CPF/screenshots-es/01.png" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo-es/01.png" title="CPF/screenshots-es/01.png" /></p>

<p><em>Figura 2: Ejemplo de pantalla de Alerta de Seguridad del Comodo Firewall Pro</em></p>

<p><strong>Nota:</strong> Un cortafuegos (firewall) es un programa diseñado para proteger tu computadora de piratas informáticos (hackers) y de programas maliciosos. Ambos pueden invadir tu computadora directamente o tratar de enviar información de tu computadora a un tercero. Por tanto, un nuevo cortafuegos (firewall) debe saber que programas son 'buenos' y darles acceso, al tiempo de mantenerse cerrado a todo software y procesos 'malos' en tu computadora. Debes investigar todas las nuevas solicitudes de acceso y tomar la decisión de permitirles o denegarles acceso.</p>

<p><strong>Importante:</strong> <strong>Debes<em> </em></strong>leer la información presentada en <em>Aplicación</em> y <em>Padre</em> en la sección de <em>Detalles</em> de la pantalla de <em>Alerta de Seguridad</em>. Nota que:</p>

<ul>
	<li><em>Aplicación</em> busca acceso a Internet.</li>
</ul>

<ul>
	<li><em>Padre</em> es el programa que expide la solicitud para ejecutar la Aplicación.</li>
</ul>

<p>Normalmente, sólo algunos programas estarán en el campo de <em>Aplicación</em>. Estos pueden incluir tu navegador de Internet, tu cliente de correo electrónico, tu programa de mensajería instantánea, etc. Puedes reconocer muchas de estas Aplicaciones solo por sus nombres. La solicitud de Padre, sin embargo no siempre presente, podría venir de diferentes fuentes, algunas legítimas y otras maliciosas.</p>

<p><img alt="CPF/screenshots-es/02.png" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo-es/02.png" title="CPF/screenshots-es/02.png" /></p>

<p><em>Figura 3. Pantalla de Alerta de Seguridad presentando una solicitud de un Generic Host Process for Win 32 Services</em></p>

<p><strong>Ejemplo:</strong> En la <em>Figura 3</em>, el programa de <em>Aplicación</em> es <em>svchost.exe</em> y el <em>Padre</em> es <em>services.exe</em>. En las <em>Consideraciones de Seguridad</em> se detalla que programa está solicitando acceso a través del <em>Padre</em> y de la <em>Aplicación</em>. En este caso un programa válido llamado <strong>Explorador de Windows</strong> está solicitando acceso a Internet. Esta es probablemente una de las primeras pantallas de <em>Alerta de Seguridad</em> que recibirás después de haber instalado el Comodo Firewall Pro y reiniciado tu computadora.</p>

<p><strong>Importante:</strong> Algunos virus engañosos pueden fingir hábilmente ser aplicaciones válidas de <strong>Windows</strong>. No existe una manera fácil de distinguir estos de solicitudes reales de acceso. Debes ser muy cuidadoso cuando descargues <em>algo</em> de Internet y escanear regularmente tu computadora en busca de virus y programas maliciosos (malware).</p>

<p><strong>Nota:</strong> Normalmente, todas las solicitudes válidas de acceso reflejaran alguna acción de tu parte. Por ejemplo, cuando ejecutas un nuevo programa por primera vez, el cortafuegos (firewall) te solicitará derechos o permisos de acceso. Esto también puede ocurrir cuando instalas o desinstalas programas. Puede tomar un poco de tiempo acostumbrarse a esto, pero pronto el cortafuegos (firewall) 'aprenderá' y aceptará tus decisiones, y estos mensajes dejarán de aparecer.</p>

<p><img alt="CPF/screenshots-es/23.png" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo-es/23.png" title="CPF/screenshots-es/23.png" /></p>

<p><em>Figura 4: Una típica pantalla de Alerta de Seguridad presentando la solicitud de acceso del KeePass</em></p>

<p>En otras ocasiones, <strong>Comodo Firewall Pro</strong> puede mostrarte un mensaje ligeramente diferente. El ejemplo que se muestra arriba nos indica que el programa <a href="/es/KeePass_principal" title="KeePass"><strong>KeePass Password Safe</strong></a> está intentando utilizar el navegador <strong>Firefox </strong>para tener acceso a Internet. Ya que sabemos que este es un programa legítimo previamente instalado en la computadora podemos permitir su solicitud de acceso.</p>

<p><strong>Consejo: Pulsa</strong> <img alt="CPF/screenshots-es/31.png" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo-es/31.png" title="CPF/screenshots-es/31.png" /> en la sección de <em>Detalles</em> de esta pantalla de <em>Alerta de Seguridad</em> para revelar información acerca de este proceso.</p>

<p><img alt="CPF/screenshots-es/24.png" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo-es/24.png" title="CPF/screenshots-es/24.png" /></p>

<p><em>Figura 5: Pantalla de Detalles de Aplicación</em></p>

<p><img alt="CPF/screenshots-es/25.png" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo-es/25.png" title="CPF/screenshots-es/25.png" /></p>

<p><em>Figura 6: Pantalla de Detalles de Aplicación del Modo Padre</em></p>

<p>Alternativamente, el investigar los nombres de estos procesos en Internet puede revelar alguna información sobre su propósito y acción.</p>

<ul>
	<li>Si tu indagación indica que puede ser un virus, o no puedes rastrear el significado u origen del mensaje, <strong>presiona</strong> <img alt="CPF/screenshots-es/35.png" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo-es/35.png" title="CPF/screenshots-es/35.png" /></li>
</ul>

<p><strong>Importante:</strong> Es mejor mantenerse en el lado seguro y rechazar las solicitudes que no puedas identificar. Si ello causa que un programa deje de funcionar adecuadamente, puedes permitir el proceso la próxima vez que el cortafuegos (firewall) te lo consulte. El ser estricto en los procesos de restricción es un enfoque adecuado de seguridad informática.</p>

<ul>
	<li>Si estás convencido que es una solicitud legítima, <strong>presiona</strong> <img alt="CPF/screenshots-es/32.png" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo-es/32.png" title="CPF/screenshots-es/32.png" /></li>
</ul>

<p><strong>Nota<em>:</em></strong> A veces un programa puede desear de diferentes maneras acceder a Internet, algunas anteriormente invisibles para ti. No te desesperes si se te consulta repetidamente sobre el otorgamiento de acceso a un mismo programa. Después de una semana o algo más de trabajo con el <strong>Comodo Firewall Pro</strong>, la mayoría de los mensajes de <em>Alerta de Seguridad</em> dejarán de aparecer.</p>

<p>A continuación se muestra un ejemplo de herramienta maliciosa solicitando tener acceso a la Internet a través del <strong>Internet Explorer</strong>:</p>

<p><img alt="CPF/screenshots-es/26.png" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo-es/26.png" title="CPF/screenshots-es/26.png" /></p>

<p><em>Figura 7: Pantalla de Alerta de Seguridad presentando una solicitud maliciosa de WallBreaker.exe</em></p>

<p><strong>Paso 1. Presiona</strong> <img alt="CPF/screenshots-es/31.png" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo-es/31.png" title="CPF/screenshots-es/31.png" /> si el nombre de <em>Padre</em> se muestra muy dudoso y parece no estar relacionado con algún programa instalado en la computadora.</p>

<p><em>Al ejecutar el paso 1 se revelará su verdadero origen además de información sobre este, como se muestra a continuación:</em></p>

<p><img alt="CPF/screenshots-es/27.png" src="/sites/securitybkp.ngoinabox.org/files/u5/comodo-es/27.png" title="CPF/screenshots-es/27.png" /></p>

<p><em>Figura 8: Pantalla de Detalles de la Aplicación en el Modo Padre del WallBreaker.exe</em></p>

<p>A pesar de que se conoce poco sobre esta aplicación, una búsqueda en <strong>Google </strong>de <em>wallbreaker.exe</em> puede revelar su verdadero propósito.</p>

<p><strong>Paso 2. Pulsa</strong> el botón de <em>Denegar</em>, luego escanea tu computadora utilizando un programa que combata los virus y los programas espía (spyware) como el <a href="/es/spybot_principal" title="Spybot"><strong>Spybot</strong></a>.</p>

<p><strong>Consejo:</strong> Habilita la casilla de la opción <em>Recordar mi respuesta para esta aplicación</em> de modo que el <strong>Comodo Firerwall Pro</strong> 'recuerde' esta decisión, y que este mensaje de advertencia no vuelva a aparecer en el futuro.</p>

<p>A veces tal vez no reconozcas el nombre de algún programa. A menudo, puede haber programas en la computadora que habías olvidado que estaban ahí, o que no fuiste tú quien los instaló. Quizás alguien más que usaba tu computadora instaló el programa y éste podría ser válido, o quizás se trate de un programa malicioso (malware). Éstos son los que tenemos que examinar. Después de haber efectuado el proceso de revisar qué programas son válidos y cuáles no, no será necesario repetirlo. Después de unos cuantos días, recibirás cada vez menos mensajes de este tipo.</p>

<p><strong>Consejo:</strong> El rechazar la solicitud de un programa para acceder a Internet implica que lo consideras un virus o programa malicioso (malware). Además, debes mantener actualizados tus programas <a href="/es/avast_principal" title="Avast"><strong>antivirus</strong></a> y de <a href="/es/spybot_principal" title="Spybot"><strong>eliminación de programas maliciosos</strong></a>, y escanear frecuentemente tu sistema, <em>especialmente</em> después de haber recibido solicitudes sospechosas del cortafuegos (firewall).</p>

<p>&nbsp;</p>


