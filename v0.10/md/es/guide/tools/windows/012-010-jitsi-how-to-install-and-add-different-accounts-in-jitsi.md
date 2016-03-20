

---

lang: es
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: Jitsi - How to Install and Add Different Accounts in Jitsi

---

Listado de las secciones en esta página:

- [**2.1. Cómo instalar Jitsi**](#2.1)
- [**2.2. Cómo añadir cuentas en Jitsi**](#2.2)
- [**2.2.1. Cómo añadir una cuenta de Gmail/Google**](#2.2.1)
- [**2.2.2. Registrar una cuenta nueva de Jabber/XMPP o SIP y añadirla a Jitsi**](#2.2.2)
- [**2.2.3. Cómo añadir una cuenta de Facebook**](#2.2.3)
- [**2.3. Cómo cambiar una contraseña para una cuenta en Jitsi**](#2.3)
- [**2.4. Cómo configurar Jitsi para mejorar su seguridad**](#2.4)
- [**2.4.1 Desactivar y eliminar el historial de llamadas y chats**](#2.4.1)
- [**2.4.2. Solicitar mensajería privada al realizar un chat de texto**](#2.4.2)
- [**2.4.3. Proteger las contraseñas de sus cuentas con una contraseña maestra**](#2.4.3)

<a name="2.1."></a>
##2.1. Cómo instalar Jitsi##

Para instalar **Jitsi**, realice uno de los siguientes pasos:

**Paso 1**. **Haga doble clic** en ![](/sbox/screen/jitsi-es/02.png). Es posible que aparezca el cuadro de diálogo *Abrir archivo - Advertencia de seguridad*. Si aparece, **haga clic** en **Sí** para activar la pantalla del *Instalador de Windows*, seguida por la ventana *Bienvenido al asistente de configuración de Jitsi*.  

**Paso 2**. **Haga clic** en ![](/sbox/screen/jitsi-es/04.png) para activar la ventana *Acuerdo de licencia del usuario final*, **seleccione** la opción *Acepto los términos de este Acuerdo de licencia* para activar el botón *Siguiente*, y luego **haga clic** en ![](/sbox/screen/jitsi-es/04.png) para activar la ventana *Carpeta de destino*.

**Paso 3**. **Haga clic** en ![](/sbox/screen/jitsi-es/04.png) para activar la ventana **Tareas adicionales** y acepte la configuración por omisión.

**Nota**: activar la opción *Auto-iniciar al arrancar o reiniciar el sistema* puede hacer que la funcionalidad del equipo se ralentice, especialmente si ya tiene múltiples aplicaciones configuradas para ejecutarse al iniciar el sistema.

**Paso 4**.  **Haga clic** en ![](/sbox/screen/jitsi-es/04.png) para activar la ventana *Listo para instalar Jitsi* y **haga clic** en ![](/sbox/screen/jitsi-es/05.png) para activar la ventana **Instalando Jitsi** que muestra la barra de progreso de la instalación.

**Paso 5**. **Haga clic** en ![](/sbox/screen/jitsi-es/06.png) para completar el proceso de instalación y ejecutar automáticamente la ventana **Iniciar sesión** de **Jitsi** como se muestra a continuación:

![](/sbox/screen/jitsi-es/07.png)

*Figura 1: Ventana de inicio de sesión de Jitsi*

**Nota**: en algunos casos, instalar y ejecutar **Jitsi** por primera vez activa una pantalla emergente de *Alerta de seguridad de Windows* (*Figura 2* a continuación). Esta alerta es un comportamiento normal del sistema operativo **MS Windows** y se puede seguir usando **Jitsi**. Incluso si no hace clic en ninguno de los botones y simplemente cierra la ventana emergente, **Jitsi** podrá comunicarse a través de los servidores públicos comunes, tales como **Jabber/XMPP o SIP**, **Google Chat** y **Facebook Chat** o **Yahoo! Messenger**. Sin embargo, si hace clic en el botón **Permitir acceso** se activa una función avanzada de **Jitsi** llamada *Cuentas SIP sin registro*. Para obtener más información sobre estas cuentas especiales, consulte la página [**Cuentas SIP sin registro**](https://jitsi.org/Documentation/RegistrarlessSIPAccount).  

![](/sbox/screen/jitsi-es/08.png)

*Figura 2: Pantalla emergente “Alerta de seguridad de Windows”*

**Paso 6**. **Seleccione** las dos casillas de red **Privada** y **Pública**, y **haga clic** en **Permitir acceso** para ver la ventana de inicio de sesión de **Jitsi** (como se muestra en la *Figura 1* anterior) o la ventana principal de interfaz del usuario (como se muestra en la *Figura 4* a continuación).


<a name="2.2."></a>
##2.2. Cómo añadir cuentas en Jitsi##

Esta sección describe cómo añadir o configurar diferentes tipos de cuentas en **Jitsi**. **Jitsi** es compatible con muchos tipos de cuentas distintas. Las cuentas descritas a continuación están basadas principalmente en los protocolos de comunicación **Jabber/XMPP** y **SIP**. Entre muchos otros servicios, **Jitsi** le permite usar cuentas de **Gmail** o **Facebook** para comunicarse. Debido a que estos son unos de los servicios más populares usados en Internet, a continuación se muestra cómo añadirlos a Jitsi, junto con información sobre cómo mejorar la seguridad al comunicarse mediante dichas cuentas haciendo uso del cifrado independiente de **Jitsi** junto con la protección ofrecida por sus proveedores de cuentas. Sin embargo, considere que incluso con el cifrado de **Jitsi** los proveedores de cuentas como **Google** o **Facebook** supervisan el hecho de que se comunique (e incluso con quién lo hace), y es posible que compartan esta información con terceros, tales como corporaciones o gobiernos. Por lo tanto, quizá sea mejor que evite usar estas cuentas para información delicada, incluso con el cifrado de **Jitsi**. También se describe en esta sección cómo crear cuentas más seguras (Jabber/XMPP o SIP) y añadirlas a Jitsi, y se recomienda usarlas en su lugar.

<a name="2.2.1."></a>
###2.2.1. Cómo añadir una cuenta de Gmail/Google###

**Nota**: El ejemplo siguiente está basado en una cuenta de **Google Talk**, y el proceso de configuración para otros protocolos de comunicación enumerados en la *Figura 1* anterior es similar. Es posible que la comunicación o algunas funciones (como el cifrado independiente de Jitsi para chats de texto o voz - **OTR** y **ZRTP**) no funcionen entre dos o más usuarios con proveedores de cuentas diferentes (como Facebook, Gmail, Yahoo, etc.). Sin embargo, deberían funcionar al comunicarse entre dos cuentas del mismo proveedor del servicio.

**Paso 1**. **Seleccione Inicio > Jitsi** o **haga doble clic** en el icono de escritorio de **Jitsi** para abrir el programa.

**Paso 2**. En la ventana de *inicio de sesión*, **introduzca** el usuario y la contraseña de la cuenta de **Gmail** que desea usar para chatear, de forma que se parezca a:

![](/sbox/screen/jitsi-es/09.png)

*Figura 3: Ventana de inicio de sesión de Jitsi (redimensionada)*

**Nota**: Puede añadir múltiples cuentas usando distintos protocolos al mismo tiempo. 

**Paso 3**. **Haga clic** en ![Sign in](/sbox/screen/jitsi-es/09s.png) para activar la ventana de chat de la cuenta:

![](/sbox/screen/jitsi-es/10.png)

*Figura 4: Un ejemplo de la ventana principal de Jitsi después de añadir una cuenta Gmail*

**Nota**: si cerró la ventana de *inicio de sesión*, o si desea añadir otra cuenta, puede hacerlo al **seleccionar *Archivo* > *Añadir nueva cuenta...***. En la nueva ventana **seleccione una Red**, como *Google Talk* e **introduzca** el usuario y la contraseña para la cuenta de **Gmail** como se muestra en la imagen siguiente:

![](/sbox/screen/jitsi-es/11.png)

*Figura 5: Ventana “Añadir nueva cuenta”*

Para verificar que haya registrado la cuenta de **Gmail** con **Jitsi**, realice lo siguiente:

**Paso 1**. **Seleccione *Herramientas* > *Opciones*** en el menú para activar la siguiente ventana:

![](/sbox/screen/jitsi-es/12.png)

*Figura 6: La ventana Opciones mostrando la nueva cuenta de Gmail registrada (redimensionada)*

**Nota**: Si está usando la [verificación de 2 pasos](https://support.google.com/accounts/answer/180744?hl=es) para proteger el acceso a su cuenta de **Gmail**, es posible que vea el siguiente mensaje al intentar iniciar sesión en **Jitsi** con su contraseña normal: Para iniciar sesión usando **Jitsi** necesitará generar una “contraseña específica para la aplicación”. Vea las instrucciones de Google sobre [cómo hacerlo](https://support.google.com/accounts/answer/185833?hl=es).

![](/sbox/screen/jitsi-es/13.png)

*Figura 7: Ejemplo de error de autenticación en el inicio de sesión de Google Talk*

<a name="2.2.2."></a>
###2.2.2. Registrar una cuenta nueva de Jabber/XMPP o SIP y añadirla a Jitsi###

**Jabber/XMPP** y **SIP** son estándares abiertos de comunicación de voz y texto. Hay [muchos servidores](https://xmpp.net/directory.php) que ofrecen cuentas gratuitas que puede utilizar con Jitsi. A continuación se recomiendan algunos de los servidores que puede usar para comunicación delicada. Considere que también es posible descargar un [software de servidor de Jabber/XMPP](http://xmpp.org/xmpp-software/servers/) (como [ejabberd](http://www.process-one.net/en/ejabberd/) o [Prosody IM](http://prosody.im/)), instalarlo en su propio equipo de servidor y configurarlo para comunicación privada y segura entre miembros de su grupo, comunidad u organización.

* Cuenta Jabber/XMPP de **Riseup.net**

Si cuenta con una cuenta en el [servicio de correo electrónico seguro Riseup.net](/es/riseup_principal) (ubicado en EE. UU.), puede también [usar esta cuenta para comunicarse a través de una red Jabber/XMPP](https://www.riseup.net/en/chat) al añadir esta cuenta a Jitsi (consulte más adelante cómo añadir una cuenta Jabber/XMPP) existente).

* Cuentas **Jabber.ccc.de** y otras cuentas Jabber/XMPP

Puede registrar una cuenta en el servidor Jabber.ccc.de (ubicado en Alemania) realizando los siguientes pasos:

**Paso 1**.  En **Jitsi, seleccione *Archivo* > *Añadir nueva cuenta...*** en el menú. En la nueva ventana, **seleccione *Red*: XMPP** y **seleccione la opción *Crear una cuenta nueva XMPP***. En *Servidor*, **escriba** jabber.ccc.de, **introduzca** el usuario XMPP que desea crear y **rellene** los campos *Contraseña* y *Confirmar contraseña* de tal forma que se vea así:

![](/sbox/screen/jitsi-es/14.png)

*Figura 8: Ejemplo de la ventana “Añadir nueva cuenta” con la opción “Crear una cuenta nueva XMPP” seleccionada*

**Paso 2**. **Haga clic en *Añadir***. Después de registrar correctamente se le mostrará una ventana similar a la *Figura 4* anterior.

Si alguien más ya está usando el nombre de usuario y la contraseña que solicitó, el proceso de registro marcará un error con el mensaje *No se pudo crear la cuenta debido al siguiente error: No se pudieron confirmar los datos.*  Puede volver a intentar repetir el proceso y seleccionar un nombre de usuario distinto.

**Considere** que si no inicia sesión en jabber.ccc.de durante más de 12 meses su cuenta se eliminará automáticamente del servidor y el nombre de usuario volverá a estar disponible para que otra persona lo registre.

Otro servidor Jabber/XMPP que vale la pena mencionar es **jit.si**. Este servidor lo mantienen los desarrolladores del programa Jitsi. Puede registrar una cuenta en [**jit.si**](https://jit.si) y muchos otros servidores Jabber/XMPP públicos de la misma forma descrita en la sección anterior. IM Observatory mantiene una [lista y clasificación de los servidores Jabber/XMPP públicos](https://xmpp.net/directory.php), y también le permite [probar la seguridad de cualquier servidor Jabber/XMPP](https://xmpp.net/index.php).

* Cuenta SIP **ostel.com**

Las cuentas **SIP** no se pueden registrar desde dentro del programa **Jitsi**. El servidor **ostel.co** (ubicado en EE. UU.) ofrece [registro en su página web](https://ostel.co/users/sign_up). **Seleccione** un nombre de usuario, contraseña y proporcione su dirección de correo electrónico existente y **haga clic** en el botón *Registrar* en la página web. Una vez que se haya registrado correctamente, regrese al programa Jitsi. **Seleccione *Archivo* > *Añadir nueva cuenta...*** en el menú, **seleccione Red: SIP**, **introduzca** el nombre de usuario (por ejemplo, terence@ostel.co) y la contraseña que creó durante el registro en la página web, y **haga clic en *Añadir***. Consulte la siguiente imagen como referencia:

![](/sbox/screen/jitsi-es/15.png)

*Figura 9: Ejemplo de la ventana “Añadir nueva cuenta” para una cuenta SIP*

* **Añadir cuentas Jabber/XMPP o SIP existentes a Jitsi**

Si ya tiene una cuenta Jabber/XMPP o SIP, puede añadirla a **Jitsi** **seleccionando *Archivo* > *Añadir nueva cuenta...*** en el menú y seleccionando la **Red** adecuada (ya sea XMPP o SIP, dependiendo del tipo de cuenta).

<a name="2.2.3."></a>
###2.2.3. Cómo añadir una cuenta de Facebook###

**Facebook** tiene dos configuraciones que es posible que deba cambiar antes de que **Jitsi** se  pueda conectar al chat de Facebook.

* **Nombre de usuario de Facebook**

**Facebook** solicita un nombre de usuario para que **Jitsi** se conecte al chat de Facebook. Muchos usuarios de **Facebook** ya tienen un nombre de usuario. Para verificar/chequear su nombre de usuario, **inicie sesión** en su cuenta de **Facebook**; su nombre de usuario es lo que aparece en la barra de dirección después de *https://www.facebook.com/* al mirar en su Biografía. Su nombre de usuario está también en la dirección de correo electrónico de **Facebook** de su cuenta personal (por ejemplo: nombredeusuario@facebook.com). Puede ver o cambiar el nombre de usuario u obtener uno en *Configuración de la cuenta* > *General* o visitando [https://www.facebook.com/username](https://www.facebook.com/username). Para establecer el nombre de usuario, es posible que **Facebook** le solicite que verifique la cuenta, lo que podría incluir enviar un mensaje SMS a un teléfono móvil, cuyo número deberá proporcionar a **Facebook** durante el proceso de verificación. Para ver más información consulte la [explicación de Facebook de los nombres de usuarios](https://es-la.facebook.com/help/329992603752372/).

* **Configuración de apps**

La “plataforma de aplicaciones” de **Facebook** debe estar activada antes de que **Jitsi** se pueda conectar al chat de Facebook. En **Facebook**, vaya a la sección **Configuración > Aplicaciones** y asegúrese de que la opción **Aplicaciones que utiliza** esté activada. Esto activará la “plataforma de aplicaciones” de su cuenta.

**Considere** que activar la “plataforma de actividades” de **Facebook** da acceso a desarrolladores de aplicaciones de terceros a mucha de su información de **Facebook**. Estos datos estarán disponibles no sólo en las aplicaciones de **Facebook** que use, sino en las aplicaciones de **Facebook** que utilicen sus amigos. Después de activar la “plataforma de aplicaciones” de **Facebook**, asegúrese de comprobar la configuración de la sección “Aplicaciones que utiliza“. Esta configuración le permitirá ocultar cierta información personal de las aplicaciones que usan sus amigos. Desafortunadamente, **Facebook** no ofrece configuración para ocultar toda la información personal. Ciertas categorías de información (como la lista de amigos, el género, o la información que ha hecho pública) será visible mientras la “plataforma de aplicaciones” de **Facebook** esté activa. Depende de usted determinar si este es un sacrificio aceptable para su privacidad. 

Ahora está listo para añadir su cuenta de **Facebook** a **Jitsi**. Para hacerlo siga los siguientes pasos:

**Paso 1**.  Desde el menú principal **seleccione *Archivo > Añadir nueva cuenta...***

**Paso 2**.  En el menú **Red** del cuadro de diálogo “Añadir nueva cuenta”, seleccione *Facebook*, **introduzca su nombre de usuario y contraseña** y **haga clic en Añadir**.
 
![](/sbox/screen/jitsi-es/16.png)

*Figura 10: Ejemplo de la ventana “Añadir nueva cuenta” para una cuenta de Facebook*


<a name="2.3."></a>
##2.3. Cómo cambiar una contraseña para una cuenta en Jitsi##

Una cuestión importante de seguridad es la de saber cómo cambiar la contraseña de cada cuenta que se tenga. Muchas de las cuentas que puede usar con Jitsi ofrecen el cambio de contraseña como parte de la configuración, a la cual se puede acceder mediante la interfaz web. Sin embargo algunas cuentas Jabber/XMPP y SIP no tienen ninguna interfaz web que las administre. Puede cambiar la contraseña de dichas cuentas usando Jitsi y siguiendo los siguientes pasos:

**Paso 1**. **Seleccione *Herramientas* > *Opciones*** en el menú y **seleccione** la pestaña **Cuentas**.

![](/sbox/screen/jitsi-es/17.png)

*Figura 11: Ventana de opciones con una cuenta seleccionada*

**Paso 2**. **Haga clic en el botón *Editar*** en la parte inferior para activar la ventana siguiente:

![](/sbox/screen/jitsi-es/18.png)

*Figura 12: Ventana “Asistente de registro de cuenta” con el botón “Cambiar contraseña de cuenta” en la parte inferior*

**Paso 3**. **Haga clic en *Cambiar contraseña de cuenta*** para activar la ventana *Cambiar contraseña de cuenta*:

![](/sbox/screen/jitsi-es/19.png)

*Figura 13: Ventana “Cambiar contraseña de cuenta”*

**Paso 4**. ***Introduzca la nueva contraseña*, *vuelva a introducir la contraseña*** y **haga clic en el botón *OK*** para cerrar la ventana.

**Paso 5**. Cierre el asistente de registro de cuenta.

<a name="2.4."></a>
##2.4. Cómo configurar Jitsi para mejorar su seguridad##

<a name="2.4.1."></a>
###2.4.1 Desactivar y eliminar el historial de llamadas y chats###

**Jitsi** guarda por omisión la información sobre las llamadas de voz y vídeo entrantes y salientes, así como el historial de los chats de texto (todos los mensajes que envía y recibe). Puede acceder a las llamadas de voz/vídeo **haciendo clic** en el icono del reloj en la ventana principal de Jitsi:

![](/sbox/screen/jitsi-es/20.png)

*Figura 14: Parte superior de la ventana principal de Jitsi con el botón del historial de llamadas marcado*

Puede ver el historial de chats de texto **haciendo clic** en el icono de temporizador con forma de huevo en la ventana de chats de texto mientras conversa con un contacto:

![](/sbox/screen/jitsi-es/21.png)

*Figura 15: Ventana del chat con el botón del historial del chat marcado*

Esta información se recopila y se almacena en el disco del ordenador. **Incluso si cifra el chat de texto con OTR, todos los mensajes de texto que envía y recibe se almacenan en el ordenador en un formato de texto abierto.** La misma información se recopila y almacena en el disco de los contactos con lo que se comunica. 

Para evitar que Jitsi recopile esta información (y eliminar los datos que ya se recopilaron), **usted y su contacto deben realizar lo siguiente**.

####Para evitar que Jitsi recopile la información: ####

**Paso 1**.  **Seleccione *Herramientas* > *Opciones*** en el menú, **seleccione** la pestaña ***General*** y **anule la selección** de la opción ***Historial de conversaciones*** como se muestra a continuación:

![](/sbox/screen/jitsi-es/22.png)

*Figura 16: Pestaña “General” de la ventana “Opciones” con la opción “Historial de conversaciones” sin marcar*

**Paso 2**. En la ventana *Opciones*, primero **seleccione la pestaña *Avanzado***, luego **seleccione la sección *Registro*** y **anule la selección de la opción *Activar registro de paquetes*** como se muestra a continuación: 

![](/sbox/screen/jitsi-es/23.png)

*Figura 17: Sección “Registro” de la pestaña “Avanzado” de la ventana “Opciones” con la opción “Activar registro de paquetes” sin marcar*

Los cambios surtirán efecto después de que **reinicie Jitsi**.

####Para eliminar la información de sus llamadas y mensajes de texto que ya se había recopilado: ####

**Paso 1**. **Salga** de Jitsi.

**Paso 2**. Elimine la carpeta del historial de registro *history_ver1.0* de la carpeta del *perfil de usuario* de **Jitsi**. Puede eliminar la sub-carpeta de history_ver1.0 si desea eliminar sólo una parte del historial. La ubicación de las carpetas del *perfil del usuario* y el *historial de registro* depende del sistema operativo:

* En versiones XP y anteriores de Windows, está ubicada en *C:\Documents and Settings\&lt;nombre_usuario&gt;\Application Data\Jitsi\history_ver1.0*
* En Windows Vista, 7 y 8 está en *C:\Users\&lt;nombre_usuario&gt;\AppData\Roaming\Jitsi\history_ver1.0* (**nota**: es posible que la carpeta “AppData” esté oculta. Consulte [cómo ver archivos ocultos](http://windows.microsoft.com/es-es/windows/show-hidden-files#show-hidden-files=windows-7)).
* En Mac OS X, en la carpeta de inicio *~/Library/Application Support/Jitsi/history_ver1.0*
* En Linux, en la carpeta de inicio *~/.jitsi/history_ver1.0* (**nota**: es posible que la carpeta “jitsi” esté oculta. Consulte [cómo ver archivos ocultos en Ubuntu](http://www.guia-ubuntu.com/index.php?title=Archivos_ocultos))

Consulte el capítulo [cómo destruir información delicada](/en/chapter-6) para obtener más información sobre cómo eliminar información de forma segura.

<a name="2.4.2."></a>
###2.4.2. Solicitar mensajería privada al realizar un chat de texto###

Se recomienda que configure **Jitsi** para que solicite mensajería de texto privada y cifrada usando el [*cifrado*](/es/glossary#encryption) [*OTR*](/es/glossary#OTR) cuando sea posible. Para hacerlo, **seleccione *Herramientas* > *Opciones*** en el menú, **seleccione la pestaña *Seguridad***, **seleccione la pestaña *Charla*** y **marque *Requiere mensajes privados*** en la parte inferior de la pantalla, como se muestra a continuación:

![](/sbox/screen/jitsi-es/24.png)

*Figura 18: Pestaña “Charla” de la pestaña “Seguridad” de la ventana “Opciones” con la opción “Requiere mensajes privados” marcada*

<a name="2.4.3."></a>
###2.4.3 Proteger las contraseñas de sus cuentas con una contraseña maestra###

Es mejor no permitirle a Jitsi que recuerde las contraseñas de las cuentas. Si decide hacerlo, cualquiera que tenga acceso a su ordenador podrá iniciar sesión en sus cuentas al ejecutar Jitsi. También será posible ver las contraseñas en la ventana *Opciones*. Por lo tanto se **recomienda ampliamente** proteger las contraseñas de sus cuentas con una **contraseña maestra** segura. Una vez que configure la contraseña maestra, Jitsi se la solicitará al iniciar el programa.

**Paso 1**. **Abra** la ventana *Opciones* (**seleccionando *Herramientas* > *Opciones*** en el menú), **seleccione la pestaña *Seguridad*** y luego la pestaña ***Contraseñas***, y **marque la opción *Usar una contraseña maestra*** para activar la ventana ***Contraseña maestra***.

**Paso 2**. En la nueva ventana, **introduzca su contraseña** como se muestra en la imagen siguiente. Para más información sobre cómo crear una contraseña segura, consulte [***cómo crear y mantener contraseñas seguras***](/es/chapter-3).

![](/sbox/screen/jitsi-es/25.png)

*Figura 19: Ventana “Contraseña maestra”*

**Paso 3**. **Haga clic en *OK*** para confirmar la contraseña y activar una nueva ventana que debería decir ***La contraseña maestra se cambió con éxito***. **Haga clic en “OK”** para cerrarla y regresar a la ventana *Opciones*, que debería parecerse a:

![](/sbox/screen/jitsi-es/26.png)

*Figura 20: Pestaña “Contraseñas” de la pestaña “Seguridad” de la ventana “Opciones” con la opción “Usar una contraseña maestra” marcada*	

**Nota**: El botón ***Cambiar contraseña maestra*** le permite cambiar la contraseña maestra y el botón ***Contraseñas almacenadas*** le permite acceder a la lista de contraseñas guardadas de Jitsi y eliminarlas si lo necesita.

