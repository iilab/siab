

---

lang: es
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: How to Install Thunderbird

---

Secciones en esta página:

- [**2.0 Instalar Thunderbird**](#2.0)
- [**2.1 Deshabilitar la opción de Búsqueda Global e Indexado en Thunderbird**](#2.1)
- [**2.2 Registrar una cuenta de correo en Thunderbird**](#2.2)
- [**2.3 Registrar Blogs, Grupos de noticias y Chats en Thunderbird**](#2.3)

<a name="2.0"></a>
## 2.0 Instalar Thunderbird ##

Para empezar con la instalación de **Thunderbird**, sigue los siguientes pasos:

**Paso 1**.  **Haz doble clic** en ![](/sbox/screen/thunderbird-es-1/01.png); puede que aparezca el cuadro de diálogo *Abrir Archivo – Advertencia de Seguridad*.  Si eso ocurriera, **haz clic** en ![](/sbox/screen/thunderbird-es-1/02.png) para activar la siguiente pantalla:

![](/sbox/screen/thunderbird-es-1/03.png)

*Imagen 1: Barra de progreso de extracción*

Una vez completada la extracción de archivos de **Thunderbird**, aparecerá la ventana de *Bienvenido al asistente de configuración de Mozilla Thunderbird*.

**Paso 2**. **Haz clic** en ![](/sbox/screen/thunderbird-es-1/04.png) para activar la ventana *Mozilla Thunderbird – Tipo de configuración*. 

**Paso 3**. **Haz clic** en ![](/sbox/screen/thunderbird-es-1/04.png) de la ventana *Elegir opciones de configuración*. La configuración por defecto es *Estándar* 

**Paso 4**. **Haz clic** en ![](/sbox/screen/thunderbird-es-1/04.png) para aceptar los ajustes por defecto y pasar a la siguiente pantalla:

![](/sbox/screen/thunderbird-es-1/05.png)

*Imagen 2: Pantalla de resumen Mozilla Thunderbird*

**Paso 5**. **Haz clic** en ![](/sbox/screen/thunderbird-es-1/06.png) para comenzar el proceso de instalación. Aparecerá la ventana de progreso de **Mozilla Thunderbird - Instalación**. Una vez completada, aparece la siguiente pantalla:

![](/sbox/screen/thunderbird-es-1/07.png)

*Imagen 3: Pantalla de Completando el asistente de instalación de Mozilla Thunderbird*

**Paso 6**. **Haz clic** en ![](/sbox/screen/thunderbird-es-1/08.png) para completar el proceso de instalación.

**Consejo**: **Thunderbird** se abrirá de forma automática si la casilla de *Iniciar Mozilla Thunderbird ahora* está habilitada, tal y como se muestra en la *imagen 3* de arriba.  Para abrir el programa más adelante, puedes hacer **doble clic** en el ícono del escritorio de **Thunderbird**, o **seleccionar > Programas > Mozilla Thunderbird > Mozilla Thunderbird**.

<a name="2.1"></a>
## 2.1 Deshabilitar la opción de Búsqueda Global e Indexado en Thunderbird ##

**Advertencia**: La aplicación de *Búsqueda Global e Indexado* en **Thunderbird** *debe* estar desactivada para mejorar su rendimiento. Según la cantidad y el tamaño de correos electrónicos, la velocidad de tu sistema puede disminuir al sobrescribir tus correos de forma continua e innecesaria en el disco duro. A medida que el disco duro se llene, las operaciones del sistema se ralentizarán.

Para desactivar la opción *Búsqueda Global e Indexado*, sigue los siguientes pasos: 

**Paso 1**. **Selecciona Herramientas > Opciones** en el panel de control de **Thunderbird** para activar la ventana *Opciones*.

**Paso 2**. **Haz clic** en ![](/sbox/screen/thunderbird-es-1/09.png) para activar la pestaña tal y como se muestra a continuación:

![](/sbox/screen/thunderbird-es-1/10.png)

*Imagen 4: La ventana Opciones mostrando la pestaña Avanzadas*

**Paso 3**. **Haz clic** en la casilla *Habilitar indexado y búsqueda global* en *Configuración avanzada* para *desactivar* esta opción, tal y como se muestra a continuación: 

![](/sbox/screen/thunderbird-es-1/11.png)

*Imagen 5: Sección de Configuración avanzada*

Si ya has conseguido deshabilitar esta opción, estás listo para registrar una cuenta de correo en **Thunderbird**.

<a name="2.2"></a>
## 2.2 Registrar una cuenta de correo en Thunderbird ## 

La ventana *Integración de sistemas* aparece la primera vez que instalas Thunderbird. Esta ventana se puede configurar para *Usar Thunderbird como cliente por defecto para: Correo electrónico*.  Si no, puedes elegir *Saltar integración*  

**Paso 1**. En la ventana de *Bienvenido a Thunderbird* **haz clic** en la opción *Saltarse esto y usar mi cuenta de correo existente*, tal y como se muestra en la siguiente pantalla:
 
![](/sbox/screen/thunderbird-es-1/12.png)

*Imagen 6: Pantalla de Bienvenido a Thunderbird*

**Paso 2**. **Introduce** tu nombre, correo electrónico y contraseña en los campos correspondientes; **haz clic** en la casilla para desactivar la opción *Recordar contraseña* tal y como muestra la *imagen 7* a continuación.

![](/sbox/screen/thunderbird-es-1/13.png)

*Imagen 7: Ventana de Configuración de la cuenta*


**Paso 3**. **Haz clic** en ![](/sbox/screen/thunderbird-es-1/14.png) para activar la siguiente pantalla:

![](/sbox/screen/thunderbird-es-1/15.png)

*Imagen 8: Ventana de Configuración de la cuenta con la opción **IMAP (carpetas remotas)** habilitada*

## IMAP y POP: Descripción y Uso ###

**Protocolo de acceso a mensajes de internet** (**IMAP**) y **Protocolo de oficina de correo** (**POP**) son dos métodos diferentes que se utilizan para almacenar y recibir correos electrónicos.

- **Protocolo de acceso a mensajes de internet** (**IMAP**): Si usas **IMAP**, todas tus carpetas (incluidas *Bandeja de entrada*, *Borradores*, *Plantillas*, *Enviados*, *Eliminados* y todas las demás carpetas) se encuentran en el servidor del correo electrónico. De esta manera, puedes acceder a ellas desde un ordenador diferente. Todos los mensajes están en el servidor y, al principio, se descargan solo los encabezados de los mensajes o las barras de título (que contienen información como fecha y hora, asunto, remitente, etc.) que se mostrarán en tu ordenador. Los mensajes completos se descargan cuando los abres. También se puede configurar **Thunderbird** para guardar copias de los mensajes de todas o solo algunas de las carpetas en tu ordenador, así puedes trabajar con ellos offline (es decir, sin conexión a internet). Si borras correos electrónicos o carpetas en **IMAP**, también se borran en *ambos*, tu ordenador y el servidor.

-  **Protocolo de oficina de correo versión 3** (**POP3**): Si usas **POP3**, solo la *Bandeja de entrada* (la carpeta a la que llegan los nuevos mensajes entrantes) se encuentra en el servidor; todas las demás carpetas están solo en tu ordenador. Puedes elegir entre dejar los mensajes en la carpeta de *Bandeja de entrada* o en el servidor tras haberlos descargado en tu ordenador, o borrarlos del servidor. Si tienes acceso a tu cuenta de correo desde un ordenador diferente, solo podrás ver los mensajes de la *Bandeja de entrada* (los mensajes nuevos y los antiguos que no hayas borrado). Ten en cuenta que según la configuración del servidor, las copias de tus correos enviados se pueden almacenar en el servidor en la carpeta *Enviados*. Merece la pena que lo compruebes tú  mismo.

**Paso 4**. **Haz clic** en ![](/sbox/screen/thunderbird-es-1/16.png) para crear tu cuenta, activar el panel de control de **Thunderbird** con la cuenta de correo en la barra lateral izquierda tal y como se muestra a continuación:

![](/sbox/screen/thunderbird-es-1/17.png)

*Imagen 9: Interfaz principal de usuario de Mozilla Thunderbird mostrando la nueva cuenta de riseup*

**Nota**: Para añadir otra cuenta de correo, **haz clic en Carpetas locales > Cuentas > Crear una cuenta nueva: Correo electrónico** para activar la *imagen 7* de esta sección, y repite desde el **paso 2** al **paso 4**.

Una vez registrada con éxito tu cuenta de correo en **Thunderbird**, la próxima vez que abras la interfaz de usuario principal, te pedirá la contraseña para cada cuenta tal y como se muestra a continuación: 

![](/sbox/screen/thunderbird-es-1/20.png)

*Imagen 10: Ventana de Es necesaria la contraseña del servidor de correo*

**Nota**: Aunque la opción de registrar o recordar la contraseña no es recomendable desde el punto de vista de la privacidad y la seguridad en internet, **Thunderbird** ofrece la opción de la *Contraseña maestra*. Esta te da la posibilidad de utilizar una contraseña para proteger cualquier otra asociada a tus diferentes cuentas de correo y que ya has introducido durante el proceso de instalación. . Para más información sobre esta  característica, consulta la sección [**3.3 Configurar las pestañas de seguridad en  Thunderbird**](/es/thunderbird_seguridad#3.3) - **Pestaña de contraseñas**.

<a name="2.3"></a>
## 2.3 Registrar Blogs, Grupos de noticias y Chats ##

Para crear y registrar una cuenta de blogs, grupos de noticias y chats, sigue los pasos siguientes:

**Paso 1**. Selecciona tu cuenta en la barra lateral izquierda **haz clic en Cuentas> Canales** para activar la ventana *Asistente de cuenta de canales web* que se muestra a continuación:

![](/sbox/screen/thunderbird-es-1/21.png)

*Imagen 11: Asistente de cuentas de canales web – Nombre de la cuenta*

**Paso 2**. **Haz clic** en ![](/sbox/screen/thunderbird-es-1/04.png) para activar la siguiente pantalla: 

![](/sbox/screen/thunderbird-es-1/22.png)

*Imagen 12: Ventana de Asistente de la cuenta – Felicidades*

**Paso 5**. **Haz clic** en ![](/sbox/screen/thunderbird-es-1/08.png) para completar el proceso de instalación de la cuenta y vuelve al panel de control de **Thunderbird**.

Ahora que ya has configurado adecuadamente **Thunderbird** para un uso óptimo, continua con la sección siguiente [**Configurar los ajustes de seguridad en Thunderbird**](/en/thunderbird_security).

