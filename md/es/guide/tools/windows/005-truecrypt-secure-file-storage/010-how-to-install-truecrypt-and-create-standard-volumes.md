

---

lang: es
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: How to Install TrueCrypt and Create Standard Volumes

---

Lista de las secciones en esta página: 

- [**2.0 Cómo instalar TrueCrypt**](#2.0)
- [**2.1 Acerca de TrueCrypt**](#2.1)
- [**2.2 Cómo crear un Volumen común**](#2.2)
- [**2.3 Cómo crear un Volumen común en un dispositivo de memoria USB**](#2.3)
- [**2.4 Cómo crear un Volumen común (Continuación)**](#2.4)

<a name="2.0"></a>
## 2.0 Cómo instalar TrueCrypt ##

**Paso 1**. **Pulsa dos veces** ![](/sbox/screen/truecrypt-es-1/001.png); la ventana *Abrir archivo - Advertencia de seguridad* puede aparecer. Si aparece, **pulsa** ![](/sbox/screen/truecrypt-es-1/002.png) para activar la pantalla de la *Licencia* de **TrueCrypt**.

**Paso 2**. **Marca** la opción *Acepto y me comprometo a cumplir con los términos de la licencia* para habilitar el botón de *Aceptar*, **pulsa** ![](/sbox/screen/truecrypt-es-1/03.png) para activar la siguiente pantalla:

![](/sbox/screen/truecrypt-es-1/04.png)

*Figura 1: Modo asistente en el modo de instalación por defecto*

- Modo *Instalación*: Esta es una opción para usuarios que no desean ocultar el hecho de que utilizan **TrueCrypt** en su computadora.

- Modo de *extracción*: Esta es una opción para usuarios que desean llevar una versión portátil de **TrueCrypt** en un dispositivo de memoria USB y no desean instalar **TrueCrypt** en su computadora.

**Nota**: Algunas opciones (como el cifrado de la partición y del disco completo) no funcionan con solo extraer **TrueCrypt**.

**Nota**: A pesar de recomendar el modo *Instalación* por defecto, aun podrás utilizar **TrueCrypt** en modo portátil más tarde. Para averiguar cómo utilizar el modo **TrueCrypt viajero**, puedes consultar la [**página TrueCrypt portátil**](/es/truecrypt_portatil). 

**Paso 3**. **Pulsa** ![](/sbox/screen/truecrypt-es-1/05.png) para activar la siguiente pantalla:

![](/sbox/screen/truecrypt-es-1/06.png)

*Figura 2: Ventana de opciones de configuración*

**Paso 4**. **Pulsa** ![](/sbox/screen/truecrypt-es-1/07.png) para activar la pantalla de *Instalación* y comenzar a instalar **TrueCrypt** en tu sistema.

**Paso 5**. **Pulsa** ![](/sbox/screen/truecrypt-es-1/08.png) y luego ![](/sbox/screen/truecrypt-es-1/11.png) para finalilzar.

**Nota**: Instamos a todos los usuarios a consultar [la documentación de ayuda de **TrueCrypt**](http://andryou.com/truecrypt/docs/index.php) después de terminar este tutorial. 

<a name="2.2"></a>
## 2.2 Cómo crear un Volumen común ##

**TrueCrypt** te permite crear dos tipos de volúmenes: *Oculto* y *Común*. En esta sección aprenderás cómo crear un *Volumen común* para almacenar tus archivos. 

Para crear un *Volumen común* con **TrueCrypt**, sigue los siguientes pasos:  

**Paso 1**. **Pulsa dos veces** ![](/sbox/screen/truecrypt-es-1/52.png) o **selecciona Inicio > Programas > TrueCrypt > TrueCrypt** para abrir **TrueCrypt**.

**Paso 2**. **Selecciona** una unidad de la lista en el panel de **TrueCrypt** como se indica a continuación:

![](/sbox/screen/truecrypt-es-1/12.png)

*Figura 3: Panel de control de TrueCrypt*

**Paso 3**. **Pulsa** ![](/sbox/screen/truecrypt-es-1/13.png) para activar el *asistente para la creación de volúmenes TrueCrypt* como sigue:

![](/sbox/screen/truecrypt-es-1/14.png)

*Figura 4: Ventana del asistente para la creación de volúmenes TrueCrypt* 

La *Figura 4* presenta tres opciones para cifrar un *Volumen común*. En este capítulo, utilizamos la opción *Crear un contenedor para archivos cifrados*. Favor de consultar la documentación de [**TrueCrypt**](http://www.truecrypt.org/docs/) para la descripción de las otras dos opciones.

**Paso 4**. **Pulsa** ![](/sbox/screen/truecrypt-es-1/05.png) para activar la siguiente pantalla:

![](/sbox/screen/truecrypt-es-1/15.png)

*Figura 5: Ventana del tipo de volumen*

La ventana del *Asistente para la creación de tipos de volumen* te permite especificar si deseas crear un Volumen **TrueCrypt** *Común* u *Oculto*. 

**Importante**: Para mayor información sobre *Cómo crear un Volumen oculto*, considera  consultar la página [**Volúmenes ocultos**](/es/truecrypt_volumenesocultos). 

**Paso 5**. **Elige** la opción *Volumen TrueCrypt estándar*. 

**Paso 6**. **Pulsa** ![](/sbox/screen/truecrypt-es-1/05.png) para activar la siguiente pantalla:

![](/sbox/screen/truecrypt-es-1/16.png)

*Figura 6: Asistente para la creación de volúmenes - Panel de ubicación del volumen*

Puedes especificar dónde quieres almacenar tu *Volumen común* mediante el *asistente para la creación de volúmenes - Pantalla de ubicación del volumen*. Este archivo se puede almacenar como cualquier otro archivo. 

**Paso 7**. **Ingresa** el nombre del archivo en el campo de texto o **pulsa** ![](/sbox/screen/truecrypt-es-1/17.png) para activar la siguiente pantalla:

![](/sbox/screen/truecrypt-es-1/18.png)

*Figura 7: Ventana de navegación para la especificación de la ruta de acceso y el nombre del archivo*

**Nota**: Un volumen de **TrueCrypt** puede contenerse dentro de un archivo normal. Esto significa que se puede mover, copiar o ¡hasta borrar! Debes recordar tanto la ubicación como el nombre del archivo. No obstante, debes elegir un nuevo nombre de archivo para el volumen que creas (consultar la sección [**2.3 Cómo crear un Volumen común en un dispositivo de memoria USB**](#2.3)). En este tutorial crearemos nuestro Volumen común en la carpeta **Mis documentos** y lo llamaremos *My volume* como se muestra en la *Figura 7* de arriba. 

**Consejo**: Puedes utilizar cualquier nombre y extensión de archivo. Por ejemplo, puedes llamar *Recetas.doc* a tu Volumen común, de modo que parezca un documento de *Word* o *Vacaciones.mpg*, para que parezca un archivo de vídeo. Esta es una forma de disfrazar la existencia de tu Volumen común. 

**Paso 8**. **Pulsa** ![](/sbox/screen/truecrypt-es-1/19.png) para cerrar la ventana de *Especificación de la ruta y el nombre del archivo* y regresar a la ventana del *Asistente para la creación de volúmenes* como sigue:

![](/sbox/screen/truecrypt-es-1/20.png)

*Figura 8: Asistente para la creación de volúmenes TrueCrypt que muestra el panel de ubicación del volumen*

**Paso 9**. **Pulsa** ![](/sbox/screen/truecrypt-es-1/05.png) para activar *Figura 9*. 

<a name="2.3"></a>
## 2.3 Cómo crear un Volumen común en un dispositivo de memoria USB ##

Para crear un *Volumen común* **TrueCrypt** en un dispositivo de memoria USB, sigue los pasos 1 a 7 de la sección [**2.2 Cómo crear un Volumen común**](#2.2), donde activas la pantalla *Selecciona un volumen TrueCrypt*. En lugar de elegir *Mis documentos* para la ubicación de tu archivo **desplázate** hasta tu dispositivo de memoria USB y **escógelo**. Luego, **ingresa** un nombre de archivo y crea allí el *Volumen común*. 

<a name="2.4"></a>
## 2.4 Cómo crear un Volumen común (continuación)##

En esta etapa, estás listo para escoger un método de cifrado específico (o *algoritmo* como se lo llama en la pantalla) para codificar la información que almacenarás en tu *Volumen común*. 

![](/sbox/screen/truecrypt-es-1/21.png)

*Figura 9: Panel de opciones del asistente para la creación de volúmenes*

**Nota**: Puedes dejar las opciones por defecto como aparecen aquí. Todos los algoritmos que se presentan en estas dos opciones se consideran seguros. 

**Paso 10**. **Pulsa** ![](/sbox/screen/truecrypt-es-1/05.png) para activar el *Asistente para la creación de volúmenes TrueCrypt* como sigue:

![](/sbox/screen/truecrypt-es-1/22.png)

*Figura 10: Asistente para la creación de volúmenes TrueCrypt que muestra el panel de tamaño del volumen*

El panel de *Tamaño del volumen* te permite especificar el tamaño del *Volumen común*. En este ejemplo, se fija en 10 Megabytes. No obstante, puedes especificar un tamaño diferente. Considera el tamaño de los documentos y tipos de archivos que deseas almacenar para fijar un tamaño de volumen adecuado para estos. 

**Consejo**: Si más tarde deseas guardar una copia de respaldo de tu Volumen común en un CD, deberás fijar el tamaño en 700 MB o menos.

**Paso 11**. **Ingresa** el tamaño específico del volumen en el campo de texto y luego **pulsa** ![](/sbox/screen/truecrypt-es-1/05.png) para activar la siguiente pantalla:

![](/sbox/screen/truecrypt-es-1/23.png)

*Figura 11: Asistente para la creación de volúmenes TrueCrypt que muestra el panel de contraseña del volumen*

**Importante**: La elección de una contraseña segura y sólida es una de las tareas más importantes que llevarás a cabo al crear un *Volumen común*. Una buena contraseña protegerá tu volumen cifrado y cuanto más sólida sea, mejor. No tienes que crear tus propias contraseñas ni recordarlas si utilizas un programa generador de contraseñas como **KeePass**. Por favor, consulta [**KeePass**](/es/keepass_principal), para obtener más información acerca de la creación y el almacenado de las contraseñas.

**Paso 12**. **Ingresa tu contraseña y luego vuelve a ingresarla** en el campo de texto marcado *Confirmar*.

**Importante**: El botón *Next* permanecerá desactivado hasta que las contraseñas de ambos campos coincidan. Si tu contraseña no es particularmente segura, verás una advertencia que te lo indica. ¡Piensa en cambiarla! Aunque **TrueCrypt** funcione con cualquier contraseña que escojas, tu información puede no estar tan segura. 

**Paso 13**. **Pulsa** ![](/sbox/screen/truecrypt-es-1/05.png) para activar la siguiente pantalla:

![](/sbox/screen/truecrypt-es-1/24.png)

*Figura 12: Asistente para la creación de volúmenes TrueCrypt que muestra el panel de formateo del volumen*

**TrueCrypt** está listo para crear un *Volumen común*. Mueve tu ratón de manera aleatoria dentro del *Asistente para la creación de volúmenes* por unos segundos. Cuanto más tiempo lo muevas, mejor será la calidad de la clave de cifrado.

**Paso 14**. **Pulsa** ![](/sbox/screen/truecrypt-es-1/25.png) para comenzar a crear tu Volumen común.

**TrueCrypt** creará un archivo llamado *My volume* en la carpeta *Mis documentos* previamente especificada. Este archivo ha de contener un *Volumen común* de 10 Megabytes de tamaño, que puedes utilizar para almacenar tus archivos de manera segura. 

Luego de crear satisfactoriamente un *Volumen común*, aparecerá el siguiente cuadro de diálogo: 

![](/sbox/screen/truecrypt-es-1/26.png)

*Figura 13: Pantalla del mensaje que muestra que el volumen TrueCrypt se ha creado satisfactoriamente*

**Paso 15**. **Pulsa** ![](/sbox/screen/truecrypt-es-1/27.png) para finalizar la creación de tu *Volumen común* y regresar al panel de control de **TrueCrypt**.

**Paso 16**. **Pulsa** ![](/sbox/screen/truecrypt-es-1/28.png) para cerrar el *asistente para la creación de volúmenes TrueCrypt*.

