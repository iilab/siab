

---

lang: es
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Configure Important Thunderbird Settings

---

Secciones en esta página:

- [**3.0 Sobre las opciones de seguridad en Thunderbird**](#3.0)
- [**3.1 Deshabilitar el panel de vista previa en Thunderbird**](#3.1)
- [**3.2 Deshabilitar la opción HTML en Thunderbird**](#3.2)
- [**3.3 Configurar las pestañas de seguridad en Thunderbird**](#3.3)
- [**3.4 Habilitar el filtro adaptativo de correo no deseado en la cuenta**](#3.4)


<a name="3.0"></a>
## 3.0 Sobre las opciones de seguridad en Thunderbird ##

En el contexto de **Mozilla Thunderbird**, la seguridad se refiere, por norma general, a la protección de tu ordenador de correos dañinos o malicioso. Algunos pueden ser simplemente spams, otros pueden contener spyware y virus. Existen varias opciones que se pueden configurar, deshabilitar o habilitar dentro de **Mozilla Thunderbird** para reforzar la protección de tu sistema de ataques procedentes de correos. También es *muy importante* que tengas instalado un programa anti-malware y un cortafuegos. 

Para más información sobre cómo evitar programas dañinos o maliciosos, consulta el apartado **Guía paso a paso** [**1. Proteger tu ordenador de Virus, Malware y Hackers**](/es/chapter-1) donde hallarás más información sobre herramientas como [**Avast**](/es/avast_principal), [**Comodo Firewall**](/es/comodo_principal) y [**Spybot**](/es/spybot_principal).

<a name="3.1"></a>
## 3.1 Deshabilitar el panel de vista previa en Thunderbird ##

La pantalla principal de **Thunderbird** está dividida en tres zonas: la barra lateral izquierda muestra las carpetas de tu cuenta de correo, la barra lateral derecha muestra la lista de mensajes, y en el panel inferior se muestra una *vista previa* del mensaje seleccionado. La vista previa se visualiza de forma automática en cuanto seleccionas un mensaje. 

**Nota**: Si un correo electrónico contiene algún código malicioso, el panel de *vista previa* del mensaje podría activarlo; por lo tanto, es buena idea deshabilitarlo. 

![](/sbox/screen/thunderbird-es-1/23.png)

*Imagen 1: Interfaz principal de usuario de Thunderbird*

Para deshabilitar el panel de vista previa, ejecuta el siguiente paso: 

**Paso 1**. **Haz clic** en ![](/sbox/screen/thunderbird-es-1/24a.png) para mostrar el *Menú de Thunderbird* y **selecciona Opciones > Disposición > Mensaje F8** para desactivarlo tal y como se muestra a continuación: 

![](/sbox/screen/thunderbird-es-1/24.png)

*Imagen 2: El menú de Opciones mostrando el submenú Disposición y la opción Mensaje seleccionada*

El *Panel de mensaje* desaparecerá, y deberás **hacer doble clic** en un mensaje para leer el contenido. Si un correo electrónico parece sospechoso (tal vez presenta un asunto inesperado o irrelevante, o procede de un remitente desconocido), ahora puedes borrarlo sin tener que previsualizar su contenido.

<a name="3.2"></a>
## 3.2 Deshabilitar la opción HTML en Thunderbird ##

Con **Thunderbird** puedes utilizar **HyperText Markup Language** (**HTML**) para redactar y leer mensajes. Esto te permite recibir y enviar mensajes que incluyan colores, fuentes, imágenes y otras características de formato. Sin embargo, **HTML** es el mismo lenguaje que se emplea para las páginas web; ver los mensajes en formato **HTML**, te puede exponer a correos electrónicos maliciosos que representan el mismo tipo de amenazas que para las páginas web. 
 
Para deshabilitar el formato **HTML**, ejecuta el siguiente paso: 

**Paso 1**. **Haz clic** en ![](/sbox/screen/thunderbird-es-1/24a.png) para mostrar el *Menú de Thunderbird* y **selecciona Opciones > Vista > Cuerpo del mensaje como > Texto sin formato** tal y como se muestra a continuación: 

![](/sbox/screen/thunderbird-es-1/25.png)

*Imagen 3: Menú de Vista mostrando el submenú Cuerpo del mensaje con la opción Texto sin formato seleccionada*

<a name="3.3"></a>
### 3.3 Configurar las opciones de seguridad ###

**Thunderbird** dispone de dos filtros de correo no deseado que te ayudarán a determinar cuáles de los mensajes entrantes son spams. Estos filtros están deshabilitados por defecto, así que debes activarlos para utilizarlos. Incluso después de haberlo hecho, seguirás recibiendo correo no deseado, pero **Thunderbird** lo enviará automáticamente a la carpeta *Junk*. 

Los scams - también conocidos como correos de *suplantación de identidad* - normalmente tratan de que hagas clic en un enlace incluido en el correo. Con frecuencia, estos enlaces dirigirán tu navegador a una página web que tratará de infectar tu ordenador con un virus. En otros casos, el enlace te llevará a una página aparentemente legítima y te engañará para que introduzcas un nombre de usuario y una contraseña, que luego serán utilizados o vendidos por la entidad o persona con propósitos comerciales o maliciosos. 

**Thunderbird** puede ayudarte a identificar este tipo de correos y te advierte sobre ellos. Se describen algunas herramientas adicionales que pueden ayudarte a evitar la infección de páginas web maliciosas en la sección [**Otros complementos útiles de Mozilla**](/es/firefox_otros) del apartado **Firefox**.

Se accede a los tipos de correo basura y a los controles de seguridad a través de la pantalla *Opciones – Seguridad* donde se configura la mayoría de estas opciones de privacidad y seguridad. Para acceder a ellas, sigue los pasos siguientes:

**Paso 1**. **Selecciona Menú > Opciones** para activar la ventana *Opciones*.

**Paso 2**. **Haz clic** en ![](/sbox/screen/thunderbird-es-1/26.png) para activar la siguiente pantalla:

![](/sbox/screen/thunderbird-es-1/27.png)

*Imagen 4: Ventana de Seguridad mostrando las pestañas asociadas*

### Pestaña Correo no deseado ###

**Paso 1**. **Marca** las opciones pertinentes en la pestaña *Correo no deseado*, tal y como se muestra en la *imagen 4* de arriba, para permitir que **Thunderbird** elimine el correo que has definido como correo basura. Más adelante en esta misma sección, se describen los ajustes adicionales para el correo no deseado. 

### Pestaña Correo fraudulento ###

**Paso 1**. **Marca** la opción *Decirme si el mensaje que estoy leyendo parece un mensaje fraudulento* para permitir que **Thunderbird** analice los mensajes en busca de scams tal y como se muestra a continuación: 

![](/sbox/screen/thunderbird-es-1/28.png)

*Imagen 5: La pestaña Correo fraudulento*  

### La pestaña Antivirus ###

**Paso 1**. **Haz clic** en la pestaña *Antivirus* para activar la siguiente pantalla: 

![](/sbox/screen/thunderbird-es-1/29.png)

*Imagen 6: Pestaña Antivirus* 

Esta opción permite que tu antivirus escanee y aísle los mensajes individuales a medida que llegan. Si no habilitas este ajuste, es posible que *toda* tu carpeta de *bandeja de entrada* pueda ser “puesta en cuarentena” si recibes un mensaje infectado.

**Nota**: Con esto se presupone que tienes un antivirus instalado. Consulta [**Avast**](/es/avast_principal) para obtener más información sobre cómo instalar y configurar el programa antivirus.

### La pestaña Contraseñas ###

**Paso 2**. **Haz clic** en la pestaña *Contraseñas* para activar la siguiente pantalla: 

![](/sbox/screen/thunderbird-es-1/30.png)

*Imagen 7: La pestaña Contraseñas*

**Importante:** Te recomendamos encarecidamente que mantengas tus contraseñas privadas y seguras utilizando un programa diseñado específicamente con este propósito. Consulta [**KeyPass**](/es/keepass_principal) para obtener más información. 

**Nota**: Las opciones de la pestaña *Contraseñas* solo funcionarán si has marcado la casilla *Recordar contraseña* en la primera pantalla de *Configuración de cuenta de correo* en el momento de registrar tu correo con **Thunderbird**. 

**Paso 1**. **Haz clic** en ![](/sbox/screen/thunderbird-es-1/31.png) para activar la siguiente pantalla:

![](/sbox/screen/thunderbird-es-1/32.png)

*Imagen 8: Ventana Contraseñas guardadas*

La ventana *Contraseñas guardadas* te permite eliminar o ver todas las contraseñas correspondientes a cada una de tus cuentas. Sin embargo, para aumentar tu privacidad y seguridad, puedes crear una *Contraseña maestra* para proteger el acceso a tus cuentas de correo y hacer que todas tus contraseñas sean inaccesibles a cualquiera que esté familiarizado con las opciones de contraseña en **Thunderbird**.

**Paso 3**. **Marca** la opción *Usar una contraseña maestra* tal y como se muestra en la *imagen 7* para habilitar el botón *Cambiar contraseña maestra...*.

**Paso 4**. **Haz clic** en ![](/sbox/screen/thunderbird-es-1/33.png) para activar la siguiente pantalla:

![](/sbox/screen/thunderbird-es-1/34.png)

*Imagen 9: Ventana Cambiar contraseña maestra*

**Paso 5**. **Escribe** una contraseña lo suficientemente segura que solo tú recuerdes, y luego **haz clic** en ![](/sbox/screen/thunderbird-es-1/35.png) para confirmar que es tu *Contraseña maestra*. 

### Contenido Web ###

Una cookie es un pequeño texto que tu navegador utiliza para autenticar o identificar una página web determinada. La opción *Contenido Web* te permite especificar qué blog, canal de noticias o chats son fiables y seguros.  

**Paso 1**. **Haz clic** en ![](/sbox/screen/thunderbird-es-1/36.png) para mostrar las opciones del *Contenido Web* tal y como se muestra a continuación:

![](/sbox/screen/thunderbird-es-1/37.png)

*Imagen 10: La pestaña Privacidad*

**Paso 2**. **Selecciona** la opción *Cierre Thunderbird* en *Conservar hasta que:* para eliminar las cookies cada vez que cierres **Thunderbird** y añadir más seguridad.

<a name="3.4"></a>
### 3.4 Habilitar el filtro adaptativo de correo no deseado en la cuenta ###

El segundo filtro de correo basura de **Thunderbird** está disponible en la ventana *Configuración de la cuenta - Configuración de correo no deseado*. Estos filtros están deshabilitados por defecto, así que debes activarlos para utilizarlos. Cada vez que lleguen correos basura, **Thunderbird** los enviará automáticamente a las carpetas *Junk* relacionadas con cada cuenta. 

**Paso 1**. **Selecciona Herramientas > Configuración de la cuenta** para activar la ventana *Configuración de la cuenta*.

**Paso 2**. **Selecciona** *Configuración de correo no deseado* relacionada con una cuenta determinada de **Gmail** o **RiseUp** en la barra lateral. 

**Paso 3**. **Activa** las opciones de *Configuración de correo no deseado* para que tu propia pantalla *Configuración de la cuenta- Configuración de correo no deseado* sea igual que la que se muestra a continuación: 

![](/sbox/screen/thunderbird-es-1/38.png)

*Imagen 11: Ventana Configuración de la cuenta - Configuración de correo no deseado*

**Paso 4**. **Haz clic** en ![](/sbox/screen/thunderbird-es-1/35.png) para completar la configuración de la ventana *Configuración de la cuenta*.

**Nota**: Se deben configurar las casillas de *Configuración de correo no deseado* por separado para cada una de las cuentas. De esta forma, el correo basura de una cuenta de **Gmail** o **RiseUp** se enviará a la correspondiente carpeta de *Eliminados*. Como alternativa, puedes escoger una *Carpeta local* para recibir el correo basura de todas tus cuentas. 

![](/sbox/screen/thunderbird-es-1/39.png)

*Imagen 12: Ventana Configuración de la cuenta - Configuración de correo no deseado mostrando los ajustes de la carpeta principal de correo basura*

**Paso 1**. **Selecciona** la opción *Configuración de correo no deseado* justo debajo de las *Carpetas locales* en la barra lateral.

**Paso 2**. **Selecciona** la alternativa *Carpetas locales* del desplegable en la carpeta *Junk* tal y como se muestra en la *imagen 12*.

**Paso 3**. **Haz clic** en ![](/sbox/screen/thunderbird-es-1/35.png) para completar la configuración de la ventana *Configuración de la cuenta*.

Ahora que has configurado las distintas opciones de seguridad y de correo no deseado en **Thunderbird**, continúa con la sección siguiente, [**Usar Enigmail con GnuPG en Thunderbird**] (/en/thuderbird_encryption). 

