

---

lang: es
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: Jitsi - Add contacts and communicate text & voice

---

Listado de las secciones en esta página:

- [**3.1 Añadir contactos a Jitsi**](#3.1)
- [**3.2 Chat de texto (mensajería instantánea) con cifrado OTR**](#3.2)
- [**3.3 Chat de texto y video con cifrado ZRTP**](#3.3)


<a name="3.1."></a>
##3.1 Añadir contactos a Jitsi##

Después de añadir por lo menos una cuenta a Jitsi e iniciar sesión, puede añadir contactos y comunicarse con ellos.

Para añadir contactos a Jitsi siga los pasos:

**Paso 0**. Abra la ventana principal de Jitsi **seleccionando Inicio > Jitsi** o **haciendo doble clic** en el icono del escritorio de **Jitsi**.

**Paso 1**. **Seleccione *Archivo* > *Añadir contacto...***, lo que abrirá la siguiente ventana:

![](/sbox/screen/jitsi-es/30.png)

*Figura 1: ventana “Añadir contacto”*

**Paso 2**. **Seleccione** a cuáles de sus cuentas desea añadir el contacto (por ejemplo, *terance@jit.si*). 

**Opcional**: puede también añadir el contacto a un *grupo* de contactos. Sin embargo, primero debe crear el grupo. Puede hacerlo al seleccionar ***Archivo* > *Crear grupo...*** en el menú). 

**Introduzca** el nombre de usuario o dirección del contacto en el campo ***ID o Número*** (por ejemplo, *sally@jit.si*). 

Puede elegir el nombre o apodo del contacto, que se verá en la lista de contactos de la ventana principal de **Jitsi**, **escríbalo en el campo *Mostrar nombre***. 

**Paso 3**. **Haga clic** en *Añadir* para cerrar la ventana *Añadir contacto* y regrese a la ventana principal de Jitsi. En su lista de contactos verá al nuevo contacto añadido con la nota “Esperando autorización” como se muestra a continuación:

![](/sbox/screen/jitsi-es/31.png)

*Figura 2: Ventana principal de Jitsi con el contacto añadido esperando autorización*
 
**Paso 4**. Cuando el contacto (sally@jit.si) inicie sesión en su cuenta, una ventana emergente le informará que usted solicitó añadirlo a su lista de contactos:

![](/sbox/screen/jitsi-es/32.png)

*Figura 3: Ventana solicitando autorización para contacto nuevo*

Su contacto tiene la opción de seleccionar *Ignorar*, en cuyo caso la solicitud permanecerá en espera; *Denegar*, en cuyo caso recibirá un aviso de que la solicitud fue rechazada; o *Autorizar*, en cuyo caso recibirá un aviso de que el contacto aceptó la solicitud, y se activará la entrada del contacto en su lista de contactos.

![](/sbox/screen/jitsi-es/33.png)

*Figura 4: Ventana de Jitsi con el contacto nuevo autorizado*

<a name="3.2."></a>
##3.2 Chat de texto (mensajería instantánea) con cifrado OTR##

Ahora que añadió el contacto y está autorizado, puede hacer clic en el nombre en la lista de contactos e iniciar una conversación de texto, o una llamada de voz o video, o puede compartir pantalla, seleccionando el icono correspondiente debajo del nombre:

![](/sbox/screen/jitsi-es/34.png)

*Figura 5: Contacto seleccionado en la ventana principal de Jitsi con iconos para IM, llamadas de voz o video y compartir el escritorio*

**Paso 1**. Ahora se explicará una de las funciones más importantes de Jitsi: la capacidad de tener conversaciones de texto seguras, cifrando los mensajes con [*OTR*](/en/glossary#OTR). OTR funciona de manera similar a [*GPG/PGP*](/en/glossary#PGP), que se describe en otros capítulos de este grupo de guías. Tal y como con PGP, antes de que usted y su contacto puedan cifrar la comunicación, ambos necesitan configurar **Jitsi** para que genere una clave de cifrado. Puede hacer esto **seleccionando el menú *Herramientas* > *Opciones*** y **seleccionando la pestaña *Seguridad*** y luego la pestaña ***Charla***. Entonces verá una ventana parecida a la que se muestra en la imagen siguiente:

![](/sbox/screen/jitsi-es/35.png)

*Figura 6: Parte de la ventana de opciones de chat en la que puede generar claves de cifrado para sus conversaciones de texto*

**Paso 2**. Después, **haga clic** en el botón ***Generar***. Como resultado, verá la huella digital de la clave que se generó.

![](/sbox/screen/jitsi-es/36.png)

*Figura 7: Parte de la ventana de opciones de chat mostrando la huella digital del chat de texto cifrado con OTR que se generó*

Se genera una clave por cuenta. Sólo necesita hacer esto de nuevo si añade una cuenta nueva o si instala Jitsi en otro dispositivo y no transfiere las claves existentes a él.

Ahora está listo para iniciar conversaciones:

**Paso 3**. **Seleccione un contacto** desde la ventana principal de Jitsi y **haga clic** en el icono *enviar mensaje* (el primero de la izquierda debajo del nombre del contacto) para abrir la ventana de la conversación de texto:

![](/sbox/screen/jitsi-es/37.png)

*Figura 8: Ventana de conversación de texto con el cifrado OTR marcado pero **no** activado*

Observe el icono *Cifrar conversación con OTR*, el candado abierto en la parte superior derecha de la ventana. Este símbolo discreto le informa si la conversación está cifrada o no. Ahora el candado está abierto (hay un pequeño espacio entre la manija y el cuerpo del candado). 

**Paso 4**. **Haga clic en el icono *Cifrar conversación con OTR***. Observe los cambios en la ventana:

![](/sbox/screen/jitsi-es/38.png)

*Figura 9: Ventana de la conversación de texto después de hacer clic en el icono “Cifrar conversación con OTR”*

Observe que ahora el candado está cerrado. Esto significa que los mensajes que su contacto y usted se envíen estarán cifrados. Observe el mensaje que dice que esta es una *conversación privada sin verificar* y que debería *autenticar* sally@jit.si.

**Paso 5**. **Haga clic en el enlace *autenticar sally@jit.si*** para abrir la ventana *Autenticar contacto*:

![](/sbox/screen/jitsi-es/39.png)

*Figura 10: Ventana “Autenticar contacto” con la huella digital para usted y su contacto*

Observe que el mensaje le recomienda comparar las huellas digitales de sus claves con las del contacto mediante otro canal (no esta conversación de texto). Al hacerlo, puede estar más seguro de que se está comunicando con su contacto, y no con otra persona. Una buena opción para comparar claves es hacerlo cara a cara, o mediante comunicación por vídeo o voz, ya que estas proporcionan medios más sencillos de validar la identidad de la otra persona. Una vez que haya comparado huellas digitales, **seleccione** la opción **Tengo** la huella digital en el menú desplegable y **haga clic en *Validar compañero***.

![](/sbox/screen/jitsi-es/40.png)

*Figura 11: Parte de la ventana “Autenticar contacto” después de seleccionar “Tengo” la huella digital del contacto*

Al cerrar la ventana *Autenticar contacto*, regresará a la ventana de la conversación:

![](/sbox/screen/jitsi-es/41.png)

*Figura 12: Ventana de la conversación de texto con el cifrado OTR autenticado*

Observe que el candado ya no tiene el triángulo naranja con el signo de exclamación blanco. Esto significa que ha autenticado el contacto. **La autenticación debe realizarse una vez para cada contacto**. Si el triángulo con el signo de exclamación blanco vuelve, significa que está conversando con alguien a quien no ha autenticado todavía. Esto puede suceder cuando el contacto se cambia a un dispositivo con otra clave de cifrado (otra instalación de Jitsi u otro programa con OTR activado, etc.). En este caso deberán volver a autenticarse otra vez para asegurarse de la identidad de la persona con la que se comunican.

**Jitsi** permite mantener conversaciones de texto con más de una persona a la vez. El cifrado OTR funciona sólo cuando conversa con una persona.


<a name="3.3."></a>
##3.3 Chat de texto y vídeo con cifrado ZRTP##

**Jitsi** ofrece chats de voz y vídeo que pueden ser cifrados independientemente con el estándar abierto llamado ZRTP. Para iniciar un chat debe: 

**Paso 1**. **Hacer clic** en el contacto en la lista de contactos **Jitsi** y **hacer clic** en el icono de voz (el segundo de la izquierda debajo del nombre del contacto) o de vídeo (el tercero). Consulte la figura 5 anterior. Una nueva ventana aparecerá indicando que **Jitsi** está estableciendo la conexión.

![](/sbox/screen/jitsi-es/42.png)

*Figura 13: Ventana de llamada indicando el estado Llamando*

El contacto verá una notificación de llamada entrante:

![](/sbox/screen/jitsi-es/43.png)

*Figura 14: Notificación de llamada entrante*

**Paso 2**. Si el contacto **acepta la llamada**, recibirá información de que se realizó la conexión:

![](/sbox/screen/jitsi-es/44.png)

*Figura 15: Ventana de llamada recibida sin cifrado ZRTP*

**Observe** el candado rojo abierto. Esto significa que la llamada aún no está cifrada con ZRTP.

**Paso 3**. **Espere...** Los programas suyos y de su contacto están estableciendo una conexión cifrada, lo cual podría tardar un momento. Si lo logran, verá las letras *zrtp* sobre un fondo naranja con un candado cerrado, como se muestra a continuación. Si no logran establecer la conexión, usted podrá de todas formas realizar la conversación, pero sin el cifrado. Puede desconectarse, reiniciar **Jitsi** y volver a intentarlo, a ver si el programa puede conectarse con cifrado esta vez. Es posible que ZRTP no funcione en llamadas entre cuentas de diferentes proveedores (como entre Google y Jit.si).

![](/sbox/screen/jitsi-es/45.png)

*Figura 16: Parte de la ventana Llamada con cifrado ZRTP activado pero no confirmado*

**Paso 4**. **Observe** la sección debajo de las letras *zrtp* y el candado con el mensaje “Comparar con la otra parte” seguido de cuatro caracteres. **Dígale** estas letras a su contacto y pregúntele si ve los mismos caracteres. Si lo hace, significa que la comunicación está cifrada y que nadie está interfiriendo. Puede **hacer clic en *Confirmar***. El campo *zrtp* naranja se volverá verde:

![](/sbox/screen/jitsi-es/46.png)

*Figura 17: Parte de la ventana Llamada con el cifrado ZRTP confirmado y activado*

**Paso 5**. Puede cerrar la sección de confirmación negra de la ventana haciendo clic en el signo x blanco en la parte superior de la sección negra:

![](/sbox/screen/jitsi-es/47.png)

*Figura 18: Parte de la ventana Llamada con el cifrado ZRTP confirmado y activado*

**Jitsi** le permite realizar chats de voz y vídeo con más de una persona. **Considere** que con este tipo de comunicación, el cifrado ZRTP se puede activar entre el iniciador de la llamada y las otras partes, pero no entre estas otras partes.

