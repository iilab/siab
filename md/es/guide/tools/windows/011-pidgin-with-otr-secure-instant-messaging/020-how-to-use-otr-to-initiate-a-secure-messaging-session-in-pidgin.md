

---

lang: es
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Use OTR to Initiate a Secure Messaging Session in Pidgin

---

Lista de secciones en esta página:

- [**3.0 Acerca de Pidgin y OTR**](#3.0)
- [**3.1 Configurar el plugin Pidgin-OTR**](#3.1)
- [**3.2 Primer paso – Generar una llave privada y mostrar su huella digital**](#3.2)
- [**3.3 Segundo paso – Autenticar una sesión de mensajería**](#3.3)
- [**3.4 Tercer paso – Autenticar la identidad de tu interlocutor**](#3.4)


<a name="3.0"></a>
## 3.0 Acerca de Pidgin y OTR ##

Tanto tú como tu interlocutor debéis configurar el plugin **OTR** antes de poder tener sesiones de **Mensajería instantánea** (**MI**) privadas y seguras.  El plugin **OTR** detectará automáticamente cuando ambas partes lo hayan instalado y configurado correctamente.

**Nota**: Si solicitas una conversación privada con un amigo que no tenga instalado ni configurado **OTR**, se le enviará inmediatamente un mensaje explicándole cómo puede obtener el plugin **OTR**. 

<a name="3.1"></a>
## 3.1 Configurar el plugin Pidgin-OTR ##

Para activar el plugin **OTR** tienes que llevar a cabo los siguientes pasos: 

**Paso 1**. **Haz doble clic** ![](/sbox/screen/pidgin-es-1/51.png) o **selecciona** **Inicio >  Programas > Pidgin** para iniciar **Pidgin** y activar la pantalla *Lista de Amigos* (observa la  *Figura 1*).

**Paso 2**. **Abre** el menú *Herramientas* y **selecciona** la opción *Complementos (plugins)* como se indica: 

![](/sbox/screen/pidgin-es-1/52.png)

*Figura 1: La pantalla Lista de Amigos con la opción Complementos (plugins) seleccionada en el menú Herramientas*

Esto activará la pantalla de *Complementos (plugins)* como se muestra:

**Paso 2**. **Desplázate** hasta la opción *Mensaje Fuera-de-Registro* y **selecciona** la casilla correspondiente para activarlo. 

![](/sbox/screen/pidgin-es-1/53.png)

*Figura 2: Pantalla de Complementos (plugins) de Pidgin con la opción Mensaje Fuera-de-Registro seleccionada*

**Paso 3**. **Haz clic en** ![](/sbox/screen/pidgin-es-1/54.png) para empezar a configurar *Fuera-de-Registro*.

A continuación se explican los 3 pasos necesarios para la configuración correcta de **OTR**, de manera que permita tener sesiones de **MI** privadas y seguras de manera eficaz: 

- **Primer Paso**: Consiste en generar una llave privada única asociada con tu cuenta y que muestra su huella digital.

Los dos pasos siguientes consisten en asegurar la sesión de **MI** y autenticar a tus amigos.

- **Segundo Paso**: Consiste en que uno de los interlocutores solicite una sesión de mensajería privada y segura con otro interlocutor que se encuentre en ese momento on-line. 

- El **Tercer Paso** consiste en *autenticar* o verificar la identidad de tu *amigo* en **Pidgin**. (**Nota**: En **Pidgin**, un amigo es todo aquel con quien te comuniques durante tus sesiones de **MI**.) Dicho proceso de verificación de la identidad de un amigo en **Pidgin** se conoce como *autenticación* y supone determinar que tu amigo es *exactamente* la persona que dice ser.   

<a name="3.2"></a>
## 3.2 Primer Paso – Generar una llave privada y mostrar su huella digital ##

Las sesiones de chat seguras en **Pidgin** se habilitan al generarse una *llave privada* para la cuenta en cuestión. La pantalla de configuración de *Off-the-Record (Mensaje fuera de Registro)* está dividida en dos pestañas: la de *Config* y la de *Huellas digitales conocidas*. La pestaña *Config* se utiliza para generar una *llave* para cada una de tus cuentas y para establecer opciones específicas de **OTR**. La pestaña *Huellas digitales conocidas* contiene una lista de las huellas digitales de las llaves de tus amigos. Debes tener una llave para cualquier amigo con el que quieras chatear de forma privada. 

![](/sbox/screen/pidgin-es-1/55.png)

*Figura 3: La pantalla de Mensaje fuera de Registro mostrando la pestaña Config*

**Paso 1**. Para optimizar tu privacidad, **selecciona** las opciones *Habilitar mensajes privados*, *Iniciar automáticamente mensajes privados* y *No grabar conversaciones OTR* en la pestaña *Config* , como se muestra en la *Figura 3*. 

**Paso 2**. **Haz clic en** ![](/sbox/screen/pidgin-es-1/56.png) para empezar a generar tu llave segura. A continuación aparecerá una pantalla notificándote que se está generando una llave privada:

![](/sbox/screen/pidgin-es-1/57.png)

*Figura 4: Cuadro de confirmación de generación de llave privada*

**Nota**: Tu amigo debe llevar a cabo los mismos pasos para su propia cuenta. 

**Paso 3**. **Haz clic en** ![](/sbox/screen/pidgin-es-1/58.png) una vez que la llave privada  (que se asemeja a la siguiente) se haya generado: 

![](/sbox/screen/pidgin-es-1/59.png)

*Figura 5: Ejemplo de una huella digital de la llave generada por el complemento OTR*

**Importante**: Ya has creado una llave privada para tu cuenta en tu computadora, que servirá para cifrar tus conversaciones de forma que nadie más pueda leerlas, incluso si consiguen vigilar tus sesiones de chat. La huella digital es una larga secuencia de letras y números utilizada para identificar la llave para una cuenta en particular, como se muestra en la *Figura 5*. 

**Pidgin** guarda automáticamente en la computadora que estés utilizando tu huella digital y las de tus amigos, de manera que no tengas que recordarlas. Si vuelves a instalar **Pidgin** o si cambias de computadora tendrás que volver a generar tu llave y volver a autenticar a tus amigos, o tendrás que trasladar tu llave y las huellas digitales de tus amigos a la nueva computadora. Para ello tendrás que copiar el contenido de la carpeta %APPDATA%\\.purple (~/.purple en Linux o Mac) a una carpeta similar en la nueva computadora.

<a name="3.3"></a>
## 3.3 Segundo Paso – Autenticar una conversación privada ##

**Paso 1**. **Haz doble clic en** la cuenta de un amigo que se encuentre actualmente on-line para iniciar una conversación de **MI**. Si los dos tenéis el plugin **OTR** instalado y debidamente configurado podréis observar que aparece un nuevo botón **OTR**en la esquina inferior derecha de la pantalla de chat. 

![](/sbox/screen/pidgin-es-1/60.png)

*Figura 6: Pantalla de mensajería de Pidgin mostrando el icono de OTR enmarcado en negro*

**Paso 2**. **Haz clic en** ![](/sbox/screen/pidgin-es-1/61.png) para activar el menú emergente asociado, y luego **selecciona** la opción *Iniciar una conversación privada* como se muestra: 

![](/sbox/screen/pidgin-es-1/62.png)

*Figura 7: Menú emergente con la opción Iniciar una conversación privada seleccionada*

*Tu pantalla de **MI Pidgin** se parecerá a la siguiente:*

![](/sbox/screen/pidgin-es-1/63.png)

*Figura 8: Pantalla de MI Pidgin mostrando el botón No verificado*

**Nota**: **Pidgin** comienza a comunicarse automáticamente con el programa de **MI** de tu amigo y a generar mensajes siempre que intentes habilitar una sesión de chat privada y segura. Como consecuencia el botón *No privado* **OTR** cambia a *No verificado*, indicando que ya puedes tener una conversación cifrada con tu amigo. 

**Aviso**! Aunque se trata de una conversación segura, la identidad de tu amigo no ha sido aún *verificada*. Cuidado: Tu amigo puede tratarse otra persona *haciéndose pasar* por tu amigo. 

<a name="3.4"></a>
## 3.4 Tercer Paso – Autenticar la identidad de tu amigo en Pidgin ##

Puedes utilizar uno de los tres siguientes métodos de identificación para autenticar a tu amigo en  **Pidgin**: 1). Un código o palabra secreta pre-establecidos, 2). formular una pregunta, cuya respuesta sólo vosotros conocéis o 3)verificar manualmente las huella digitales de tu llave por medio de un método diferente de comunicación.

### Método del código o palabra secreta ###

Podéis establecer un código o palabra secreta por adelantado, ya sea en persona o por medio de un medio de comunicación distinto (como el teléfono, mensajería de voz de [**Jitsi**](/en/jitsi) o un mensaje por teléfono móvil). Una vez que ambos hayáis introducido la misma frase o código se habrá autenticado la sesión. 

**Nota**: La función de reconocimiento de código o palabra secreta de **OTR** distingue entre mayúsculas (A,B,C) y minúsculas (a,b,c). ¡Es importante recordarlo al crear un código  o palabra secreta!

**Paso 1** . **Haz clic** en el botón *OTR* en la pantalla de chat y luego **selecciona** la opción *Autenticar Amigo* como se muestra: 

![](/sbox/screen/pidgin-es-1/66.png)

*Figura 9: Menú emergente de No Verificado con la opción Autenticar Amigo seleccionada*

Esto activará la pantalla *Autenticar Amigo*, solicitándote que selecciones un método de autenticación. 

**Paso 2**. **Haz clic en** ![](/sbox/screen/pidgin-es-1/67.png) y **selecciona** *Shared Secret (secreto compartido)* como se muestra: 

![](/sbox/screen/pidgin-es-1/68.png)

*Figura 10: Pantalla de Autenticar Amigo mostrando la lista desplegable* 

**Paso 3**. **Introduce** el código o palabra secreta como se muestra:

![](/sbox/screen/pidgin-es-1/69.png)

*Figura 11: Pantalla de Shared Secret (secreto compartido)* 

**Paso 4**. **Haz clic en** ![](/sbox/screen/pidgin-es-1/70.png) para activar la siguiente pantalla:

![](/sbox/screen/pidgin-es-1/71.png)

*Figura 12: La pantalla Autenticar Amigo para un interlocutor ficticio*

**Nota**: *Tu amigo, por su parte, verá en este momento la pantalla que se muestra en la figura 13 y tendrá que introducir la misma palabra o código. Si coinciden se habrá autenticado la sesión.*

![](/sbox/screen/pidgin-es-1/72.png)

*Figura 13: La pantalla Autenticar Amigo para un interlocutor ficticio*

Una vez se haya autenticado la sesión,  el botón *OTR* cambiará a ![](/sbox/screen/pidgin-es-1/75.png). La sesión será ya segura y tendrás la certeza de estar hablando con tu amigo.

### Método de pregunta y respuesta ###

Otra forma de autentificar la identidad de los interlocutores es el método de pregunta y respuesta. Formula una pregunta y elige una respuesta. Tras leer la pregunta, tu amigo debe introducir la respuesta *exacta* y si coincide con la tuya, la identidad estará de inmediato autentificada. 

**Paso 1**. **Haz clic en** el menú *OTR* en la pantalla de mensaje activa para desplegar el menú emergente asociado y **selecciona** la opción *Autenticar Amigo* (observa la *Figura 9*).

![](/sbox/screen/pidgin-es-1/76.png)

*Figura 14: Pantalla de chat de Pidgin mostrando el icono* OTR 

Aparecerá la pantalla *Autenticar Amigo* solicitándote que elijas el método de autenticación. 

**Paso 2**. **Haz clic en el ** menú desplegable y **selecciona** la opción *Pregunta y respuesta* como se muestra:  

![](/sbox/screen/pidgin-es-1/77.png)

*Figura 15: La pantalla de autenticar amigo*

**Paso 3**. **Introduce** una pregunta y su respuesta correspondiente. Se enviará esta pregunta a tu amigo. 

![](/sbox/screen/pidgin-es-1/78.png)

*Figura 16: Pantalla de pregunta y respuesta*

Si la respuesta de tu amigo coincide con la tuya, vuestra identidad se habrá verificado y ambas partes serán quienes dicen ser. 

Una vez se haya autenticado la sesión el botón de *OTR* cambiará a ![](/sbox/screen/pidgin-es-1/79.png). Tu sesión  será ahora segura y puedes tener la certeza de la identidad de tu amigo de chat.

### Verificación manual de la huella digital ###

El tercer método de autenticar la identidad es la verificación de la huella digital. Esto consiste en intercambiar o mostrar tus huellas digitales y las de tu amigo por medio de otro canal de comunicación (por ejemplo, email seguro o llamada telefónica). Si las huellas intercambiadas coinciden puedes seleccionar ***He verificado* que se trata de la huella digital correcta* y **Autenticar** así la sesión.


Observa que cuando seleccionas **Seleccionar > Lista de amigos > Herramientas > Plugins > Mensaje Fuera de Registro (OTR) > Configurar plugin**, la pestaña de *Huellas digitales conocidas* ahora muestra la cuenta de tu amigo junto con un mensaje advirtiendo que su identidad ha sido verificada. 

![](/sbox/screen/pidgin-es-1/98.png)

*Figura 18: Pantalla de Mensaje Fuera de Registro (OTR) mostrando la pestaña Huellas Digitales Conocidas*

¡Enhorabuena! Ahora ya podéis conversar en privado. La próxima vez que tengas una sesión de  chat con tu amigo (con las mismas computadoras), sólo tendrás que solicitar una conexión segura (como se muestra en la figura 7) y que tu amigo la acepte. La sesión ya deberá estar autenticada.

