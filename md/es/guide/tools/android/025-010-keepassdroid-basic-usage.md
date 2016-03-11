

---

lang: es
community: guide
type: tools
legacy: True
child: True
os: android
weight: 1
depth: 3
title: KeePassDroid - Basic Usage

---

-----

## 2. ¿Cómo instalar y usar KeePassDroid?

Lista de secciones:
- [**2.0 ¿Cómo instalar KeePassDroid**](#2.0)
- [**2.1 ¿Cómo Crear una Nueva Base de Datos de Contraseñas?**](#2.1)
- [**2.2 ¿Cómo Agregar un Grupo o Entrada?**](#2.2)
- [**2.3 ¿Cómo Editar una Entrada?**](#2.3)
- [**2.4 ¿Cómo Generar Contraseñas al Azar?**](#2.4)
- [**2.5 ¿Cómo Bloquear la Base de Datos KeePassDroid?**](#2.5)
- [**2.6 ¿Cómo crear un respaldo del Archivo de la Base de Datos de Contraseñas?**](#2.6)
- [**2.7 ¿Cómo cambiar Tu Contraseña Maestra?**](#2.7)

-------

<a name="2.0"></a>
## 2.0 ¿Cómo instalar KeePassDroid? ##

**Paso 1**. **Descarga** la aplicación desde [**F-Droid**](http://f-droid.org/).

![](/sbox/screen/keepassdroid-en/01.png)

*Figura 1: Versiones de KeyPassDroid*

**Paso 2**. Una vez que finaliza la descarga haz clic en **Instalador de Paquetes** y luego haz **clic** en *Instalar*.

![](/sbox/screen/keepassdroid-en/02.png)

*Figura 2: Permisos necesarios para KeyPassDroid*

**Paso 3**. Haz **clic** en *Abrir*, como puedes ver en la captura de pantalla abajo, para activar **KeePassDroid**.

![](/sbox/screen/keepassdroid-en/03.png)

*Figura 3: Pantalla de instalación de la aplicación.*

<a name="2.1"></a>
## 2.1 ¿Cómo Crear una Nueva Base de Datos de Contraseñas? ##

En las secciones siguientes, se te enseñará cómo crear una contraseña maestra, guardar tu nueva base de datos, generar una contraseña al azar para un programa particular y crear una copia de respaldo de tu base de datos.

Para abrir **KeePassDroid** deberás hacer clic en el ícono de la aplicación. 

![](/sites/securityinabox.org/files/u12/keepass.gif)

El crear una nueva base de datos de contraseñas requiere de dos pasos: debes inventar una única contraseña maestra que sea original y fuerte la cual te permitirá bloquear y desbloquear tu base de datos de contraseñas. Luego debes guardar la base de datos de contraseñas. 

Para crear una nueva base de datos de contraseñas, debes completar los siguientes pasos:

**Paso 1**. Para crear una nueva base de datos de contraseñas haz **clic** en *crear*. 

![](/sbox/screen/keepassdroid-en/04.png)

*Figura 4: Pantalla de Abrir/crear base de datos.*

Esto activará la pantalla *Ingrese contraseña de base de datos*, como se muestra abajo:

![](/sbox/screen/keepassdroid-en/05.png)

*Figura 5: Pantalla del ingreso de contraseña maestra de la base de datos*

**Paso 2**. **Escriba** la contraseña maestra que has inventado en el campo *contraseña* y luego confirma la *contraseña* como se muestra abajo:

![](/sbox/screen/keepassdroid-en/06.png)

*Figura 6: Ingresar contraseña*

**Consejo**: Asegúrate de crear una contraseña maestra muy fuerte, para más información revisa [**3. ¿Cómo crear y mantener buenas contraseñas**](/es/capitulo_3_1). 

**Paso 3**. Haz clic en **Aceptar** para activar la siguiente pantalla

![](/sbox/screen/keepassdroid-en/07.png)

*Figura 7: Pantalla principal de KeePassDroid*

¡Felicidades! Has creado de forma exitosa tu base de datos de contraseñas seguras. Ahora podrás empezar a llenarla con todas tus contraseñas actuales y futuras. 

**Nota**: También puedes copiar archivos de base de datos **KeePass** ya creadas desde tu computadora a tu dispositivo Android y abrirla con **KeePassDroid**. 

<a name="2.2"></a>
## 2.2. ¿Cómo Agregar un Grupo o Entrada? ##

**KeePassDroid** almacena las entradas de contraseñas en grupos para organizar tu información, los grupos por defecto son **eMail** e **Internet**, pero puedes crear tus propios grupos haciendo **clic** en **Grupo** y **Añadir un nuevo grupo**, luego escribes el nombre que le desea asignar al grupo y haz clic en *Aceptar* para activar la siguiente pantalla: 

![](/sbox/screen/keepassdroid-en/09.png) ![](/sbox/screen/keepassdroid-en/10.png)

*Figuras 8 y 9: Añadiendo un nuevo grupo*

La pantalla de **Añadir entrada** te permite agregar información sobre cuentas, contraseñas y otros detalles importantes en tu nueva y recién creada base de datos. Como se muestra en el ejemplo abajo, tendrás la posibilidad de añadir entradas para guardar contraseñas y usuarios para diferentes sitios web y cuentas elecrtrónicas. 

**Paso 1**. Haz **clic** en *Añadir Entrada* para activar la pantalla de *Añadir entrada* como se muestra a continuación:

![](/sbox/screen/keepassdroid-en/11.png) ![](/sbox/screen/keepassdroid-en/12.png)

*Figuras 10 y 11: Agregando una nueva entrada de contraseña.*

**Nota**: La pantalla de *Añadir Entrada* te presenta una serie de campos para ser completados. Ninguno de los campos son obligatorios, la información que suministras aquí es básicamente para tu conveniencia. Podrá ser útil para situaciones cuando estás buscando una entrada particular. 

Una breve explicación sobre estos campos de texto se presenta a continuación: 

**Nombre**: Un nombre que describa tu entrada de contraseña particular. Por ejemplo tu contraseña de Gmail.

**Usuario**: El ususario asociado con la entrada de contraseña. Por ejemplo, securitybox@gmail.com

**URL**: El sitio web asociado con tu entrada de contraseña. Por ejemplo, https://mail.google.com

**Contraseña**: Esta función genera una contraseña al azar cuando se activa la pantalla de *Anadir entrada**. Puedes usar esta función si quieres cambiar una contraseña ya existente por una generada por  KeePassDroid. Como KeePassDroid siempre recordará la contraseña por tí, no hay necesidad de verla. Una contraseña al azar es generada y considerada fuerte (es decir, difícil para un  intruso de adivinar o descifrar).  

Más adelante en esta sección se describirá cómo generar una contraseña al azar. Siempre puedes reemplazar una contraseña autogenerada por una propia. Por ejemplo, si estás creando una entrada para una cuenta ya existente querrás ingresar la contraseña correcta aquí.

**Confirme contraseñas**: Es la confirmación de la contraseña.

**Comentarios**: Aquí es donde escribes información descriptiva o general sobre la cuenta o sitio web de la cual estás guardando información. Por ejemplo: Configuración del servidor de correos electrónicos *POP3 SSL, pop.gmail.com, Port 995; SMTP TLS, smtp.gmail.com, Port: 465*

**Nota**: Crear o modificar entradas en **KeePassDroid** no cambia tus contraseñas actuales! Piensa en **KeePassDroid** como un directorio electrónico seguro para tus contraseñas. Sólo guardará lo que escribas en ella, nada más. 

**Paso 2**. Haz clic en **guardar** para salvar los cambios realizados en la pantalla de Añadir entrada. 

Tu nueva entrada ahora aparecerá en el grupo.

![](/sbox/screen/keepassdroid-en/13.png)

*Figura 12: Nueva entrada aparecer en el grupo recién creado.*

<a name="2.3"></a>
## 2.3 ¿Cómo Editar una Entrada? ##

Puedes editar una entrada existente de **KeePassDroid** en cualquier momento. Puedes cambiar tu contraseña (es considerada una práctica segura cambiar contraseñas cada 3 o 6 meses), o modificar cualquier detalle que hayas guardado en tu entrada de contraseña. 

Para editar una entrada, realiza los siguientes pasos:

**Paso 1**. **Selecciona** el *Grupo* correcto para activar las entradas asociadas a él.  

![](/sbox/screen/keepassdroid-en/14.png)

*Figura 13: Lista de grupos.*

**Paso 2**. **Selecciona** la entrada relevante, luego haz **clic** en la entrada seleccionada para activar la siguiente ventana: 

![](/sbox/screen/keepassdroid-en/15.png)

*Figura 14: Ver entrada.*

**Paso 3**. Haz **clic** en **Editar**, ahora puedes editar la información que tienes allí. Cuando terminas haz **clic** en **guardar** para mantener todos los cambios realizados a la información, incluyendo la contraseña. 

![](/sbox/screen/keepassdroid-en/16.png)

*Figura 15: Editar información.*

Para cambiar una contraseña existente (que hayas creado previamente tú mismo/a) por una generada y recomendada por **KeePassDroid**, por favor lea la siguiente sección. 

<a name="2.4"></a>
## 2.4 ¿Cómo Generar Contraseñas al Azar? ##

Las contraseñas largas y al azar son consideradas fuertes en el mundo de la seguridad. El nivel de aleatoriedad está basada en principios matemáticos y no puede ser simplemente 'adivinado' por alguien que quiera ingresar a una de tus cuentas.  KeePass ofrece un Generador de Contraseñas que te ayuda con este proceso. Como se mostró anteriormente, una contraseña al azar se genera automáticamente cuando realizas una nueva entrada. Esta sección describirá cómo generar una tú mismo/a.  

**Nota**: El *Generador de Contraseñas* puede ser activado desde las pantallas de *Añadir entrada* y *Editar entrada*.

![](/sbox/screen/keepassdroid-en/17.png)

*Figura 16: Información sobre entrada de contraseña.*

**Paso 1**. Haz **clic** en el botón ![](/sbox/screen/keepassdroid-en/18.png) desde la pantalla de *Añadir entrada* o *Editar entrada*, para activar la pantalla *Generador de Contraseñas* como se muestra a continuación:

![](/sbox/screen/keepassdroid-en/19.png)

*Figura 17: Opciones de generación de contraseñas.*

La pantalla del Generador de Contraseñas presenta una variedad de opciones a escoger para generar una contraseña segura. Puedes especificar la longitud deseada de la contraseña, el conjunto de caracteres que contendrá la contraseña entre muchas otras opciones. Para nuestros propósitos seleccionaremos las siguientes opciones a modo de ejemplo:

- **Longitud** 16 caracteres
- **Marca** Mayúsculas
- **Marca** Minúsculas
- **Marca** Números
- **Marca** Menos
- **Marca** Caracteres especiales
- **Marca** Subrayado

![](/sbox/screen/keepassdroid-en/19.png)

*Figura 18: Opciones para la generación de contraseñas*

**Paso 2**. Haz **clic** ![](/sbox/screen/keepassdroid-en/20.png) para iniciar el proceso. Cuando se haya completado, **KeePassDroid** te presentará la contraseña creada para tí. 

![](/sbox/screen/keepassdroid-en/21.png)

*Figura 19: Una contraseña generada aleatoriamente.*

**Paso 3**. Haz **clic** en *Aceptar* para activar las siguientes pantallas:

![](/sbox/screen/keepassdroid-en/22.png)

*Figura 20: Información de la entrada*

**Nota**: Puedes ver la contraseña generada escogiendo la opción en el menú. Sin embargo esto crea un riesgo a la seguridad como conversamos anteriormente. En escencia no necesitas ver nunca la contraseña generada.  Explicaremos más sobre esto en la sección [**3.0 Usando contraseñas de KeePass**](/en/keepass_passwords).

**Paso 4**. Haz **clic** en *Guardar* para aceptar la contraseña y volver a la pantalla *Entrada* como se muestra aquí: 

![](/sbox/screen/keepassdroid-en/23.png)

*Figura 21: Pantalla de entrada*

<a name="2.5"></a>
## 2.5  ¿Cómo Bloquear la Base de Datos KeePassDroid? ##

**Paso 1**. Haz **clic** en el botón **Menú** para activar la siguiente pantalla:

![](/sbox/screen/keepassdroid-en/24.png)

*Figura 22: Opciones del menú*

**Paso 2**. Haz **clic** en *Bloquear Base de Datos* para deshabilitar la consola de **KeePassDroid** como se muestra aquí:

![](/sbox/screen/keepassdroid-en/25.png)

*Figura 23: Base de Datos Bloqueada*

Deberás ingresar tu contraseña maestra para poder acceder de nuevo a tu base de datos **KeePassDroid**.

<a name="2.6"></a>
## 2.6 ¿Cómoo crear un respaldo del Archivo de la Base de Datos de Contraseñas? ##

El archivo de la base de datos **KeePassDroid** en tu teléfono Android aparecerá con la extensión   .kdb. Puedes copiar este archivo a tu computadora o a tu llave USB. Nadie podrá abrir la base de datos sin la contraseña maestra.

**Nota**: Para abrir tu base de datos **KeePassDroid** que copiaste de tu dispositivo Android a tu computadora, necesitas asegurarte de haber instalado el programa KeePass en tu computadora o bien en tu llave USB como versión portable.

Por favor lea [**Versión portable de KeePass**](https://securityinabox.org/en/keepass_portable) para mayor información.

<a name="2.7"></a>
## 2.7 ¿Cómo cambiar Tu Contraseña Maestra? ##

Puedes cambiar tu contraseña maestra en cualquier momento. Esto puede hacerse una vez que hayas abierto la base de datos de contraseñas.

**Paso 1**. **Selecciona** la base de datos y haz **clic** en *Menú* para activar lo siguiente: 

![](/sbox/screen/keepassdroid-en/26.png)

*Figura 24: Opciones del Menú*

**Paso 2**. Haz **clic** en **Cambiar Contraseña Maestra** para activar la siguiente pantalla:

![](/sbox/screen/keepassdroid-en/27.png)

*Figura 25: Ingresar nueva contraseña.*

**Paso 3**. Escriba tu contraseña en los espacios de  **Contraseña** y **Confirmar contraseña**, luego haz **clic** en Aceptar.

![](/sbox/screen/keepassdroid-en/28.png)

*Figura 26: Ingresa la nueva contraseña*

## 3.0 Usando Contraseñas de KeePassDroid ##

Dado que una contraseña segura no es fácil de memorizar, **KeePassDroid** te permite copiar la contraseña desde la base de datos y pegarla en la cuenta o sitio web que la requiera. 

Para mayor seguridad tienes la opción de mantener la contraseña copiada en el portapapeles por **30 segundos**, **1 minuto** o **5 minutos**, para que puedas pegar la contraseña en el lugar requerido sin la necesidad de correr antes de que el portapapeles la borre automáticamente. 

Puedes ver estas opciones en la siguiente pantalla visitando: **Menú** > **Configuraciones** > **Aplicación** > **Tiempo de expiración del portapapeles**

![](/sbox/screen/keepassdroid-en/29.png)

*Figura 27: Opciones de expiración de tiempo del Portapapeles.*

### Copiando una contraseña de KeePassDroid 

**Paso 1**. Haz clic en **Menú** de la entrada de contraseña requerida para activar lo siguiente: 

![](/sbox/screen/keepassdroid-en/30.png)

*Figura 28: Opciones de contraseña*

**Paso 2**. **Selecciona** ![](/sbox/screen/keepassdroid-en/31.png)

**Paso 3**. **Abra** la cuenta o sitio relacionado y **pega** la contraseña pulsando y sosteniendo en el espacio apropiado y seleccionando *Pegar*:

![](/sbox/screen/keepassdroid-en/32.png)

*Figura 29: Opciones para editar texto*

**Nota**: Al usar todo el tiempo **KeePassDroid** nunca necesitarás ver o conocer cuáles son tus contraseñas.  Las funciones de copiar/pegar se encargarán de mover tus contraseñas desde la base de datos a la ventana requerida. Si utilizas la función de *Generador de Contraseñas* y luego transfieres esta contraseña a un proceso nuevo de registro de cuenta de correo electrónico por ejemplo, estarás usando una contraseña que nunca has visto. ¡Y aún así funciona! 

### Bloquear la base de datos 

Tienes la opción de bloquear tu base de datos cada vez que la aplicación se encuentre inactiva por un periodo de tiempo. Puedes hacer esto visitando:

**Menú** > **Configuración** > **Aplicación** haz **clic** en **Tiempo de la aplicación** para activar lo siguiente:


![](/sbox/screen/keepassdroid-en/33.png)

*Figura 30:* Opciones de tiempo de la aplicación.

**Selecciona** el tiempo de bloqueo para tu base de datos.

