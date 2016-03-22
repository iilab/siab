

---

lang: es
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: How to Use Enigmail with GnuPG in Thunderbird

---

Secciones en esta página:

- [**4.0 Un resumen de Enigmail, GnuPG y Cifrado de clave pública y privada**](#4.0)
- [**4.1 Instalar Enigmail y GnuPG**](#4.1)
- [**4.2 Generar pares de claves y configurar Enigmail para que funcione con tus cuentas correo**](#4.2)
- [**4.3 Intercambiar claves públicas**](#4.3)
- [**4.4 Validar y firmar un par de claves**](#4.4)
- [**4.5 Cifrar y descifrar un mensaje**](#4.5)


<a name="4.0"></a>
## 4.0 Un resumen de Enigmail, GnuPG y Cifrado de clave pública y privada ##

**Enigmail** es un complemento de **Mozilla Thunderbird** que te permite proteger la privacidad de tu comunicación por correo. **Enigmail** es una interfaz que te deja utilizar el programa de cifrado **GnuPG** dentro de **Thunderbird**.  La interfaz de **Enigmail** está representada como *Enigmail* en la barra de herramientas del panel de control de **Thunderbird**. 

**Engimail** se basa en la [**criptografía asimétrica**](https://es.wikipedia.org/wiki/Criptografia_asimetrica).
Con este método, cada individuo debe generar su propio par de claves personal. La primera clave se conoce como *clave privada*. Está protegida con una contraseña o frase clave que debe guardarse y *nunca* compartirse con *nadie*. 

La segunda clave se conoce como *clave pública*. Esta clave se puede compartir con cualquiera de tus corresponsales. Una vez que dispongas de la *clave pública* de un corresponsal, puedes comenzar a enviarle correos cifrados a esta persona. Solo esa persona podrá descifrar y leer tus correos porque es la única que tiene acceso a la *clave privada* correspondiente.

Del mismo modo, si envías una copia de tu *clave pública* a tus contactos de correo y mantienes en secreto la correspondiente *clave privada*, solo tú podrás leer los mensajes cifrados de esos contactos.

**Enigmail** te permite adjuntar *firmas digitales* a tus mensajes. El receptor de tu mensaje que tenga una copia auténtica de tu *clave pública* podrá verificar que el correo es tuyo, y que su contenido no fue manipulado en el trayecto. Asimismo, si tienes una *clave pública* de un corresponsal, puedes verificar las firmas digitales de sus mensajes firmados.

<a name="4.1"></a>
## 4.1 Instalar Enigmail y GnuPG ##

Consulta la [**sección descargar**](/es/thunderbird_principal) sobre las instrucciones para descargar **Enigmail** y **GnuPG**.

### 4.1.1 Instalar GnuPG ###

Instalar **GnuPG** es bastante sencillo, se parece a la instalación de otros programas que ya has realizado, y se puede hacer siguiendo los pasos siguientes:  

**Paso 1**. **Haz doble clic** en ![](/sbox/screen/thunderbird-es-1/40.png) para comenzar con el proceso de instalación. Puede que aparezca el cuadro de diálogo *Abrir Archivo – Advertencia de Seguridad*. Si eso ocurre, **haz clic** en ![](/sbox/screen/thunderbird-es-1/02.png) para activar la siguiente pantalla:

![](/sbox/screen/thunderbird-es-1/41.png)

*Imagen 1: Asistente de configuración de GnuPG*

**Paso 2**. **Haz clic** en ![](/sbox/screen/thunderbird-es-1/04.png) para activar la pantalla *Configuración de GNU Privacy Guard - Acuerdo de licencia*; una vez leído, **haz clic** en ![](/sbox/screen/thunderbird-es-1/04.png) para activar la ventana *Configuración de GNU Privacy Guard - Elegir componentes*.

**Paso 3**. **Haz clic** en ![](/sbox/screen/thunderbird-es-1/04.png) para aceptar la configuración defecto y activar la ventana *Configuración de GNU Privacy Guard - Instalar opciones - Selección de idioma GnuPG*. 

**Paso 4**. **Haz clic** en ![](/sbox/screen/thunderbird-es-1/04.png) para aceptar *en-English* como idioma por defecto y activar la ventana *Seleccionar lugar de instalación*.

**Paso 5**. **Haz clic** en ![](/sbox/screen/thunderbird-es-1/06.png) para aceptar la ruta de instalación por defecto y activar la pantalla *Elegir carpeta de menú de inicio*.

**Paso 6**. **Haz clic** en ![](/sbox/screen/thunderbird-es-1/06.png) para empezar a descomprimir e instalar los distintos paquetes de *GnuPG**. Una vez completado este proceso, aparecerá la pantalla *Instalación completa*.

**Paso 7**. **Haz clic** en ![](/sbox/screen/thunderbird-es-1/04.png) y luego en ![](/sbox/screen/thunderbird-es-1/08.png) para finalizar la instalación del programa **GnuPG**.

<a name="4.1.2"></a>
### 4.1.2 Instalar el complemento Enigmail ###

Una vez instalado con éxito el programa **GnuPG**, ahora estás preparado para instalar el complemento **Enigmail**. 

Para comenzar con la instalación de **Enigmail**, sigue los pasos siguientes: 

 **Paso 1**. **Abre Thunderbird**, luego **haz clic** en ![](/sbox/screen/thunderbird-es-1/24a.png) para mostrar el *Menú de Thunderbird* y **selecciona Complementos** para activar la ventana *Administrador de complementos*.

**Paso 2**. **Haz clic** en ![](/sbox/screen/thunderbird-es-1/44.png) en la barra lateral izquierda - Si no se ha detectado el Complemento Enigmail, verás este mensaje *No tiene instalado ningún complemento de este tipo*.   

**Paso 3**. Si el complemento Enigmail aparece en el panel principal *Extensiones*, **haz clic** en ![](/sbox/screen/thunderbird-es-1/46.png). Si no aparece, **haz clic** en ![](/sbox/screen/thunderbird-es-1/45a.png) y **selecciona** *Instalar complemento desde archivo* tal y como muestra a continuación: 

![](/sbox/screen/thunderbird-es-1/46a.png)

*Imagen 3: Menú de herramientas para todos los complementos*

**Paso 4**. Navega hasta la carpeta donde has guardado la extensión Enigmail (probablemente en la carpeta *Descargas*) tal y como se muestra en la siguiente pantalla:

![](/sbox/screen/thunderbird-es-1/47.png)

*Imagen 4: Ventana Selecciona extensión que quieres instalar

**Paso 5**.  **Haz clic** en ![](/sbox/screen/thunderbird-es-1/48.png) para activar la siguiente pantalla:

![](/sbox/screen/thunderbird-es-1/49.png)

*Imagen 5: Ventana Instalación de programa*

**Importante**: Antes de ejecutar el paso 6, ¡asegúrate de que has guardado todo tu trabajo online!

**Paso 6**. **Haz clic** en ![](/sbox/screen/thunderbird-es-1/50.png) y luego **haz clic** en ![](/sbox/screen/thunderbird-es-1/51.png) para completar la instalación del complemento **Enigmail**. 

Para comprobar que el complemento **Enigmail** se ha instalado con éxito, vuelve a la interfaz principal de usuario, **haz clic** en ![](/sbox/screen/thunderbird-es-1/24a.png) y comprueba que *Enigmail* aparece como una de las opciones, tal y como se muestra a continuación: 

![](/sbox/screen/thunderbird-es-1/52.png)

*Imagen 6: Barra de herramientas de Thunderbird con Enigmail resaltado*

### 4.1.3 Confirmar que Enigmail y GnuPG funcionan ###

Antes de empezar a utilizar **Enigmail** y **GnuPG** para autenticar y descifrar tus correos, primero debes asegurarte de que ambos se comunican.

**Paso 1**. **Selecciona Enigmail > Preferencias** para mostrar la pantalla de *Preferencias de Enigmail* tal y como se muestra a continuación:

![](/sbox/screen/thunderbird-es-1/53.png)

*Imagen 7: Ventana de Preferencias de Enigmail*

Si la instalación de **GnuPG** se ha realizado con éxito, ![](/sbox/screen/thunderbird-es-1/54.png) se verá en la sección *Archivos y directorios*; de lo contrario, recibirás una alerta parecida a la siguiente:

![](/sbox/screen/thunderbird-es-1/55.png)

*Imagen 8: Mensaje de Alerta de Enigmail*

**Consejo**: Si recibes este mensaje, puede significar que no has instalado **GnuPG** o que lo has instalado en una ubicación diferente. Si has instalado **GnuPG** en una ubicación diferente, **marca** la opción *Ignorar con* para activar el botón *Buscar...*, y luego **haz clic** en ![](/sbox/screen/thunderbird-es-1/69.png) para activar *Buscar programa GnuPG* y navega de forma manual hasta donde se encuentra el archivo *gpg.exe* en tu ordenador; si no es así vuelve a [4.1 Instalar Enigmail y GnuPG](#4.1).

**Paso 2**. **Haz clic** en ![](/sbox/screen/thunderbird-es-1/35.png) para regresar al panel de control de **Thunderbird**.

<a name="4.2"></a>
## 4.2 Generar pares de claves y configurar Enigmail para que funcione con tus cuentas correo ##

Una vez confirmado el correcto funcionamiento de **Enigmail** y **GnuPG**, puedes configurar una o más cuentas de tu correo para usar **Enigmail** como generador de uno o más pares de claves públicas y privadas.

### 4.2.1 Usar el asistente de Enigmail para generar un par de claves ###

**Enigmail** te ofrece dos formas de generar un par de claves pública y privada. La primera utiliza el *Asistente de instalación de Enigmail* y la segunda, la pantalla *Administrar claves*. 

Para generar un par de claves por primera vez utilizando el *Asistente de instalación de Enigmail*, sigue los pasos siguientes:

**Paso 1**. Si la ventana **Asistente de instalación** no se activa **selecciona Enigmail > Asistente de instalación** para abrir la pantalla de *Asistente de instalación de Enigmail* tal y como se muestra a continuación: 

![](/sbox/screen/thunderbird-es-1/56.png)

*Imagen 9: Pantalla Bienvenido al asistente de configuración de Enigmail*

**Paso 2**. **Haz clic** en ![](/sbox/screen/thunderbird-es-1/04.png) para activar la siguiente pantalla. *Nota - esta pantalla solo aparecerá si has creado par de claves para otra cuenta*.

![](/sbox/screen/thunderbird-es-1/59.png)

*Imagen 10: Pantalla Seleccionar identidades*

**Paso 3**. **Introduce** una frase clave segura en las dos casillas de *Contraseña*.

![](/sbox/screen/thunderbird-es-1/65.png)

*Imagen 15: Ventana Crear clave - Crear una clave para firmar y cifrar correo electrónico*

**Paso 4**. **Haz clic** en ![](/sbox/screen/thunderbird-es-1/04.png) para activar la pantalla *Resumen*, que te muestra los ajustes realizados durante la generación del par de claves.

**Paso 5**. **Haz clic** en ![](/sbox/screen/thunderbird-es-1/04.png) para iniciar la generación del par de claves, tal y como se muestra en la siguiente pantalla:

![](/sbox/screen/thunderbird-es-1/67.png)

*Imagen 16: Ventana Generación de clave - Tu clave se está generando ahora*

**Nota**: Cualquier clave generada utilizando el *Asistente de instalación de Enigmail* tiene un tamaño de 4096 bits y una duración de 5 años.

**Paso 6**. Una vez generada la clave, se te pedirá que crees un certificado de revocación. **Haz clic** en ![](/sbox/screen/thunderbird-es-1/76.png) tal y como se muestra en la siguiente pantalla:

![](/sbox/screen/thunderbird-es-1/68.png)

*Imagen 17: Confirmación de solicitud de Enigmail*

**Nota**: Si sabes que alguien hostil o malicioso ha tenido acceso no autorizado a tu clave privada o has perdido el acceso a la misma, debes enviar el certificado de revocación para informarle de que no debería usar la correspondiente clave pública. Ten en cuenta que tal vez debas hacer esto si tu ordenador se extravía, es robado o confiscado. Te aconsejamos que hagas copias de seguridad y protejas tu certificado de revocación.

**Paso 7**. Te solicitará que **introduzcas** la contraseña que asociaste con la clave recién creada. Y luego **navega** hasta la ubicación donde puedas guardar el certificado de forma segura y **haz clic** en ![](/sbox/screen/thunderbird-es-1/78.png) en la pantalla siguiente:

![](/sbox/screen/thunderbird-es-1/70.png)

*Imagen 18: Crear y guardar certificado de revocación*

**Paso 8**. **Haz clic** en **OK** para completar la creación tanto del par de claves como del certificado de revocación.

### 4.2.2 Generar pares de claves adicionales y certificados de revocación para otra cuenta de correo ###

Es muy común tener un par de claves diferente para cada cuenta de correo. Es posible utilizar el mismo par de claves para muchas cuentas de correo, pero quizás confunda a tus contactos. Se puede añadir más de una cuenta de correo a un solo par de claves (no hablaremos de eso en este apartado), lo cual aporta algunos beneficios en cuanto al uso, pero también asocia todas esas cuentas de correo a una persona que quizás no sea la deseada.

Sigue los pasos siguientes si quieres generar pares de claves adicionales para otras cuentas de correo.

**Paso 1**. **Selecciona Enigmail > Administrar clave** para activar la siguiente pantalla:

![](/sbox/screen/thunderbird-es-1/71.png)

*Imagen 19: El menú Generar en la ventana de Administrar clave de Enigmail con la alternativa Nuevo par de claves seleccionada* 

**Nota**: **Marca** *Mostrar por defecto todas las claves* para ver el par de claves generado utilizando el *Asistente de configuración de OpenPGP* para tu primera cuenta de correo, tal y como se muestra en la *imagen 19* de arriba y la *imagen 23* de abajo.

**Paso 2**. **Selecciona Generar > Nuevo par de claves** en *Administrar claves* tal y como se muestra en la *imagen 19* de arriba para activar la pantalla siguiente: 

![](/sbox/screen/thunderbird-es-1/72.png)

*Imagen 20: Pantalla Generar clave OpenPGP*

**Paso 3**. **Selecciona** una cuenta de correo del desplegable *Cuenta / ID de usuario*, **marca** la opción *Usar la clave generada para la identidad seleccionada*. 

**Importante**: Genera siempre pares de claves con una frase clave, y **nunca** actives la opción "sin frase clave".

![](/sbox/screen/thunderbird-es-1/73.png)

*Imagen 21: Ventana Generar clave OpenPGP mostrando la pestaña Expiración de la clave*

**Nota**: El período de validez de un par de claves depende completamente de tus necesidades de privacidad y seguridad; cuanto más a menudo cambies los pares de clave, más difícil resulta que el nuevo par de claves esté comprometida. Sin embargo, cada vez que cambies tu par de claves, necesitarás enviar la nueva clave privada a tus corresponsales, y verificarla con cada uno de ellos.

**Paso 4**. **Introduce** el número adecuado, y luego **selecciona** la unidad de tiempo deseada (*días*, *meses*, *años*) durante el cual el par de claves será válido. 

**Paso 5**. **Haz clic** en ![](/sbox/screen/thunderbird-es-1/74.png) para activar la ventana Confirmación de Enigmail.

**Paso 6**. Te solicitará que generes una certificado tal y como se muestra en la *imagen 17*.

**Paso 7**. **Haz clic** en ![](/sbox/screen/thunderbird-es-1/76b.png) para activar la ventana de navegación *Crear y guardar certificado de revocación*.

**Nota**: Si sabes que alguien hostil o malicioso ha tenido acceso no autorizado a tu clave privada o has perdido el acceso a la misma, debes enviar el certificado de revocación para informarle de que no debería usar la correspondiente clave pública. Ten en cuenta que tal vez debas hacer esto si tu ordenador se extravía, es robado o confiscado. Te aconsejamos que hagas copias de seguridad y protejas tu certificado de revocación.

**Paso 8**. Busca una ubicación segura para guardar el certificado de revocación tal y como se muestra en la pantalla siguiente y **haz clic** en ![](/sbox/screen/thunderbird-es-1/78.png). Luego te solicitará que introduzcas una frase clave que hayas asociado a tu clave recién creada.

![](/sbox/screen/thunderbird-es-1/77.png)

*Imagen 22: Ventana Crear y guardar certificado de revocación*

**Paso 9**. **Haz clic** en ![](/sbox/screen/thunderbird-es-1/35.png) para completar la generación tanto del par de claves como del certificado de revocación, y regresa a la pantalla siguiente:

![](/sbox/screen/thunderbird-es-1/79.png) 

*Imagen 23: Ventana Administrar claves de Enigmail mostrando los pares de clave*

**Nota**: **Marca** la opción *Mostrar por defecto todas las claves* para mostrar todos los pares de clave y sus cuentas asociadas. Procura encontrarte en un lugar seguro cuando realices esto.

Una vez que hayas generado con éxito tanto el par de claves como el certificado de revocación, ya estás preparado para intercambiar las claves públicas con un corresponsal de confianza.

### 4.2.3 Configurar Enigmail para usarlo con tu cuenta de correo ###

Para habilitar el uso de **Enigmail** con una cuenta de correo específica, sigue los pasos siguientes:

**Paso 1**.  **Haz clic** en ![](/sbox/screen/thunderbird-es-1/24a.png) para mostrar el *Menú de Thunderbird* y **selecciona Opciones > Configuración de la cuenta**.

**Paso 2**. **Selecciona** *Seguridad OpenPGP* en el menú de la barra lateral tal y como se muestra a continuación: 

![](/sbox/screen/thunderbird-es-1/80.png)

*Imagen 24: Pantalla Configuración de la cuenta - Seguridad OpenPGP*

**Paso 3**. **Marca** la opción *Activar el soporte OpenPGP* y **selecciona** la opción *Usar la dirección de correo de esta identidad para identificar la clave OpenPGP*.

**Paso 4**. **Haz clic** en ![](/sbox/screen/thunderbird-es-1/35.png) para volver al panel de control de **Thunderbird**. 

<a name="4.3"></a>
## 4.3 Intercambiar claves públicas ##

Antes de empezar a enviaros mensajes de correos cifrados, tú y tus corresponsales debéis intercambiaros las claves públicas. También debes confirmar la validez de cualquier clave que aceptes mediante la confirmación de que realmente pertenece al supuesto remitente. 

### 4.3.1 Enviar una clave pública utilizando Enigmail ###

Para enviar una clave pública usando **Enigmail**, tanto tú como tu corresponsal seguiréis los siguientes pasos:

**Paso 1**. **Abre Thunderbird** y luego **haz clic** en ![](/sbox/screen/thunderbird-es-1/81.png) para escribir un nuevo mensaje.

**Paso 2**. Selecciona en el menú la opción **Enigmail > Adjuntar mi clave pública**.

**Nota**: Siguiendo este método, no se muestra el panel **Adjuntar archivo:** de forma inmediata. Aparecerá en cuanto envíes el mensaje.

Si deseas enviar una clave pública diferente, **selecciona** la opción del menú **Enigmail > Adjuntar clave pública...** y luego **selecciona** la clave que te gustaría enviar.

![](/sbox/screen/thunderbird-es-1/82.png) 

*Imagen 25: El panel Redactar mensaje mostrando la clave adjunta en el panel Adjunto*.

**Paso 3**. **Haz clic** en ![](/sbox/screen/thunderbird-es-1/83.png) para enviar tu correo con tu clave pública adjunta. 

### 4.3.2 Importar una clave pública usando Enigmail ###

Tanto tú como tu corresponsal realizaréis los mismos pasos cuando importéis las claves públicas de cada uno.

**Paso 1**. **Selecciona** y **abre** el correo electrónico que contiene la clave pública de tu corresponsal. El archivo adjunto aparecerá de forma similar a como se muestra aquí: ![](/sbox/screen/thunderbird-es-1/87.png)

**Paso 2**. **Haz clic** en el archivo adjunto arriba ![](/sbox/screen/thunderbird-es-1/87a.png). **Enigmail** detecta un mensaje que contiene una clave pública y te pedirá que importes la clave tal y como se muestra a continuación:

![](/sbox/screen/thunderbird-es-1/88.png)

*Imagen 26: Pantalla Confirmación de Enigmail para importar la clave pública* 

**Paso 3**. **Haz clic** en ![](/sbox/screen/thunderbird-es-1/89.png) para importar la clave pública de tu corresponsal.

Si la clave se ha importado con éxito, aparecerá un mensaje parecido al siguiente:

![](/sbox/screen/thunderbird-es-1/90.png)

*Imagen 27: Pantalla Alerta de Enigmail mostrando la clave pública de tu corresponsal*

Para confirmar que has importado con éxito la clave pública de tu corresponsal, ejecuta el siguiente paso:

**Paso 1**. **Selecciona Enigmail > Administrar claves** para ver la pantalla *Administrar claves Enigmail* tal y como se muestra a continuación:

![](/sbox/screen/thunderbird-es-1/91.png)

*Imagen 28: Pantalla Administrar claves Enigmail mostrando una clave pública importada recientemente* 

**Ten en cuenta** que la opción *Mostrar por defecto todas las claves* tiene que estar seleccionada para poder ver las claves.
<a name="4.4"></a>
## 4.4 Validar y firmar un par de claves ##

Por último, debes verificar que la clave importada realmente pertenece a la persona que supuestamente la envió. Por tanto, confirma su 'validez'. Este es un paso importante que tanto tú como tus contactos deberíais seguir cada vez que recibáis una clave pública. 

### 4.4.1 Validar un par de claves ###

**Paso 1**. **Contacta** con tu corresponsal a través de otro medio de comunicación distinto al correo electrónico. Puedes usar el teléfono, mensajes de texto, **Voz sobre Protocolo de Internet** (**VoIP**) o cualquier otro método, pero **debes** estar totalmente seguro de que realmente estás hablando con la persona correcta. Por sus resultados, las conversaciones por voz o vídeo y los encuentros cara a cara son la mejor alternativa, si es conveniente y se pueden concertar de forma segura. 

**Paso 2**. Tanto tú como tu corresponsal deberíais verificar las 'huellas digitales' de las claves públicas que habéis intercambiado. Una huella es una serie de números y letras únicos que identifica cada clave. Puedes utilizar la pantalla *Administrar claves* de **Enigmail** para ver la huella de los pares de clave que has creado y las claves públicas que has importado. 

Para ver la huella de un par de claves en particular, sigue los pasos siguientes:

**Paso 1**. **Selecciona Enigmail > Administrar claves** y luego **haz clic con el botón derecho** en una clave determinada para activar el menú emergente: 

![](/sbox/screen/thunderbird-es-1/92.png) 

*Imagen 29: Menú Administrar claves de Enigmail con la alternativa Propiedades seleccionada*

**Paso 2**. **Selecciona** la opción *Propiedades de la clave* para activar la siguiente pantalla: 

![](/sbox/screen/thunderbird-es-1/93.png)

*Imagen 30: Pantalla Propiedades de la clave*

Tu corresponsal debería repetir estos pasos. Para confirmar las huellas, lee la de tu clave a tu contacto y pídele la verificación de que coincide con la huella que ve en la clave pública que ha recibido. A continuación, pide a tu contacto que realice lo mismo con la huella de su clave. Si las huellas no coinciden, intercambiad las claves públicas de nuevo y repetid el proceso de validación.

**Nota**: La huella en sí no es un secreto y puede guardarse para realizar una verificación posterior y cuando mejor te convenga.

### 4.4.2 Firmar una clave pública válida ###

Una vez verificada la clave del corresponsal determinado, puedes *firmarla* para confirmar la validez de esta clave.
Firmar claves puede revelar una conexión entre tu corresponsal y tú cuando enviáis la clave firmada a otra persona o la exportáis al servidor de claves. Con el fin de evitar que esto ocurra, selecciona siempre la opción *Firma local* de abajo.

Para firmar una clave pública verificada de forma correcta sigue los pasos siguientes:

**Paso 1**. **Selecciona Enigmail > Administrar claves** para abrir la pantalla *Administrar claves*.

**Paso 2**. **Haz clic con el botón derecho** en la clave pública de tu corresponsal desde la pantalla *Administrar claves* (véase la imagen 29 de arriba) y **selecciona** en el menú *Firmar clave* para activar la siguiente pantalla:

![](/sbox/screen/thunderbird-es-1/94.png)

*Imagen 31: Pantalla Firmar clave de Enigmail*

**Paso 3**. **Marca** la casilla *He realizado una comprobación muy cuidadosa*, **selecciona** *Firma local (no se puede exportar)*, y luego **haz clic** en ![](/sbox/screen/thunderbird-es-1/35.png) para firmar la clave pública de tu corresponsal. Tal vez te solicite una contraseña para tu clave privada. 

#### 4.4.3 Administrar tus pares de claves ####

La ventana *Administrar claves de Enigmail* se utiliza para generar, validar y firmar diferentes pares de claves. Sin embargo, también puedes realizar otras acciones relacionadas con la administración de claves entre las que se incluyen (véase imagen 29 de arriba): 

- **Administrar ID de usuarios** te permite asociar más de una dirección de correo a un único par de claves.
- **Cambiar fecha de expiración** te permite cambiar la fecha de expiración de tu par de claves.
- **Cambiar frase clave** te permite cambiar la contraseña que protege tu par de claves.
- **Generar y guardar certificado de revocación** te permite generar un nuevo certificado de revocación, si has perdido o extraviado el que habías creado anteriormente. 

<a name="4.5"></a>
## 4.5 Cifrar y descifrar mensajes de correo ##

**Importante**: La cabecera de cualquier mensaje de correo - es decir, el *Asunto* y los destinatarios, incluidos cualquier información en los campos *Para*, *CC* y *CCO* - *no se puede* cifrar y se enviará como texto abierto. Para asegurar la privacidad y seguridad de tus intercambios de correo, el asunto de tu mensaje no debería ser descriptivo con el fin de no revelar información personal.  Además, te aconsejamos que coloques todas las direcciones en el campo *CCO* cuando envíes correos a un grupo de personas.

Si cifras mensajes de correo con archivos adjuntos, te recomendamos encarecidamente que utilices la opción **PGP/MIME**, ya que ampliará el cifrado a cualquier archivo y nombre de archivos adjuntos en tu correo.

Ten en cuenta que cualquier mensaje cifrado que envíes con Thunderbird/Enigmail/GnuPG se encripta automáticamente con tu clave junto con los destinatarios elegidos de ese correo, así que puedes descifrar los correos en tu carpeta de enviados.

### 4.5.1 Cifrar un mensaje ###

Una vez que tanto tú como tu corresponsal hayáis importado, validado y firmado con éxito las claves públicas de ambos, ya estáis listos para empezar a cifrar mensajes y descifrar los que recibáis.

Para cifrar los contenidos del mensaje para tu corresponsal, sigue los pasos siguientes:

**Paso 1**. **Abre** **Thunderbird** y **haz clic** en ![](/sbox/screen/thunderbird-es-1/81.png) para escribir un correo.

**Paso 2**. Para cifrar el mensaje, **haz clic** en *Enigmail -> El mensaje no será cifrado* y **selecciona** *Forzar cifrado* tal y como se muestra en la pantalla siguiente:

![](/sbox/screen/thunderbird-es-1/84.png) 

*Imagen 33: Opción Forzar cifrado*

**Paso 3**. Para firmar el mensaje **haz clic** en *Enigmail -> El mensaje no será firmado* y **selecciona** *Forzar firma*. 

**Nota**: Para verificar que el mensaje se cifra y se firma, comprueba que aparecen **resaltados** los dos iconos siguientes en la esquina inferior derecha del panel de mensaje tal y como se muestra a continuación:

![](/sbox/screen/thunderbird-es-1/85.png) 

*Imagen 34: Cifrado y firma habilitado*

**Paso 4**. **Haz clic** en ![](/sbox/screen/thunderbird-es-1/83.png) para enviar el mensaje. Es posible que te solicite una contraseña para usar tu clave privada a la hora de firmar el mensaje.

**Paso 5 opcional**. Si adjuntas cualquier archivo al mensaje, necesitas **seleccionar** la opción *Cifrar/firmar todo el mensaje y enviarlo usando PGP/MIME* y **haz clic** en el botón OK de la pantalla siguiente: 

 ![](/sbox/screen/thunderbird-es-1/86.png) 

*Imagen 35: Pantalla Solicitud de Enigmail*

**Nota: Si *cifras cada archivo adjunto por separado* (segunda opción en la imagen 35 de arriba), ¡los nombres de los archivos adjuntos no se cifran y se envían con el texto íntegro! ¡Esto podría filtrar información personal! Utilizar PGP/MIME garantiza que todo el texto, los archivos adjuntos y sus nombres estén cifrados y ocultos.**

### 4.5.2 Descifrar un mensaje ###

Cuando recibes y abres un mensaje cifrado, **Enigmail/OpenPGP** automáticamente intentará descifrar el mensaje en cuanto lo recibes y lo abres. 
Si no es así, selecciona el botón *Descifrar*.
Esto activará la siguiente pantalla:

![](/sbox/screen/thunderbird-es-1/96.png)

*Imagen 36: Aviso de Enigmail - Introduzca su frase clave o el PIN de su tarjeta electrónica*

**Paso 1**. **Introduce** tu frase clave tal y como se muestra arriba.

Una vez introducida la frase clave para tu clave privada, el mensaje se descifra y se muestra de la siguiente manera:

![](/sbox/screen/thunderbird-es-1/97.png)

*Imagen 37: El nuevo mensaje descifrado en el panel de mensaje*

Ahora has descifrado con éxito este mensaje. Si cada vez que tú y tu corresponsal intercambiáis mensajes repetís los pasos descritos en la sección **4.5 Cifrar y descifrar mensajes de correo**, podréis mantener un canal de comunicación verificado y privado, aunque alguien intente controlar los intercambios de correo.

### 4.5.3 Ampliar las opciones de seguridad ###

Al utilizar *Enigmail y GnuPG* para garantizar tu privacidad, es muy importante que te asegures de que **todos** los correos enviados están cifrados. Esto incluye respuestas a correos cifrados, borradores de correos que te gustaría cifrar y extractos de correos cifrados anteriormente. 

**Activa siembre el cifrado del mensaje (como en la sección anterior *4.5.1 Cifrar un mensaje*) antes de empezar a escribirlo**. De esta manera, te aseguras de que los borradores del mensaje solo se escribirán en el servidor del correo de manera encriptada.

Te recomendamos encarecidamente que **configures Enigmail para que te alerte antes de enviar un mensaje sin cifrar**. A continuación te mostramos los pasos a seguir:

**Paso 1**. **Haz clic** en el menú *Enigmail > Preferencias* y **selecciona** la pestaña *Enviar*.

**Paso 2**. Dentro de *Confirmar antes de enviar* **selecciona** *Si no está cifrado* y haz clic en OK. 

![](/sbox/screen/thunderbird-es-1/99.png)

*Imagen 38: Preferencias de Enigmail - Confirmar antes de enviar*

Ahora, cada vez que envíes un mensaje sin cifrar, saltará una alerta avisándote de que el mensaje no está cifrado, tal y como se muestra abajo. Si quieres enviar el correo cifrado, **haz clic** en *Cancelar* y sigue los pasos de la sección 4.5.1.
 
![](/sbox/screen/thunderbird-es-1/98.png)

*Imagen 39: Confirmar Enigmail*

**Recuerda otra vez que** los campos *Asunto, Para, CC* y *CCO* **nunca** se cifran.

