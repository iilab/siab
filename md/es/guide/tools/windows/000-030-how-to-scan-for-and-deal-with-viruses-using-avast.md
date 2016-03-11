

---

lang: es
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: How to Scan for and Deal with Viruses Using avast!

---

Lista de secciones de esta página:  

- [**4.0 Antes de empezar**](#4.0)
- [**4.1 Guía rápida para enfrentarse a brotes de virus**](#4.1)
- [**4.2 Vista general de la interfaz principal de usuario de avast!**](#4.2)
- [**4.3 Cómo analizar su sistema para localizar malware y virus**](#4.3)
- [**4.4 Cómo realizar un análisis completo del sistema**](#4.4)
- [**4.5 Cómo analizar una carpeta seleccionada**](#4.5)
- [**4.6 Cómo realizar un análisis durante el arranque**](#4.6)
- [**4.7 Cómo enfrentarse a los virus**](#4.7)
- [**4.8 Cómo utilizar el Baúl de virus**](#4.8)
- [**4.9 Métodos avanzados para la eliminación de virus**](#4.9)



<a name="4.0"></a>
### 4.0 Antes de empezar ###

Hay dos aspectos fundamentales que debemos tener en cuenta cuando nos enfrentamos a malware y a otros virus con **avast!**. El primero es analizar su ordenador para identificar las amenazas. El segundo consiste en eliminar o mover dichas amenazas al *Baúl de virus* de **avast!**. Eliminar o mover el malware o los virus al *Baúl de los virus* es un método eficaz para impedir que interactúen con otros programas o archivos del ordenador.

Puede resultar raro almacenar malware o virus en el *Baúl de los virus*. Sin embargo, si ya han infectado información importante o delicada, puede que quiera recuperar o guardar ese documento, archivo o programa infectado en la medida de lo posible. En raras ocasiones, puede que **avast!** identifique por error programas o archivos legítimos como virus, lo que se conoce como 'falsos positivos'. Puede que esos archivos o programas sean importantes para usted o para el funcionamiento de su sistema, y puede que quiera examinarlos, curarlos y recuperarlos.

El *Baúl de virus* de **avast!**  es una 'zona muerta' o de 'cuarentena' electrónica, donde usted tiene la oportunidad de examinar el virus y determinar su amenaza potencial investigando en Internet, o enviándolo a un laboratorio de virus – una opción disponible en **avast!** cuando se hace clic con el botón derecho sobre un virus situado en el *Baúl de virus*. Hacer doble clic sobre un virus en el *Baúl de virus* *no* activará ni ejecutará el malware o virus porque el *Baúl de virus* lo mantiene aislado del resto de su sistema. 

**Consejo**: También puede transferir información importante o delicada al *Baúl de virus* de **avast!** para mantenerla a salvo durante el ataque de un virus.

<a name="4.1"></a>
### 4.1 Guía rápida para enfrentarse a brotes de virus ###

Existen algunas precauciones que puede tomar para reducir las amenazas a su sistema; por ejemplo, usar programas antivirus o anti-spyware actualizados, como **avast!** y **Spybot**, evitar documentos o páginas web problemáticos que le hayan enviado, o actuar con extrema precaución cuando inserte un dispositivo extraíble en su ordenador. Puede obtener más información sobre los pasos necesarios en la sección [Evitar una infección viral](/es/chapter_1_1) del capítulo [1. Proteger tu computadora de software malicioso (malware) y piratas informáticos (hackers)
](/es/chapter-1). No obstante, a pesar de las precauciones, en ocasiones nuestro ordenador será infectado por un virus. Los siguientes puntos han de tenerse en cuenta cuando nos enfrentamos a un ataque de un virus:
 
- Desconecte su ordenador físicamente de Internet o de la red local. Si tiene una conexión inalámbrica, desconecte su ordenador de la red inalámbrica. Si es posible, apague o extraiga su tarjeta inalámbrica. Es recomendable desconectar de Internet todos los ordenadores que compartan una red local con su ordenador.

- Prepare un análisis durante el arranque para todos los ordenadores de su red local. Escriba los nombres de todos los virus que encuentre para poder investigarlos – y bórrelos o transfiéralos al *Baúl de virus* de **avast!**. Para aprender cómo realizar un análisis durante el arranque, consulte la sección [**4.6 Cómo realizar un análisis durante el arranque**](#4.6).

- Incluso si un virus ha sido eliminado o reparado, repita el paso anterior y ejecute análisis durante el arranque en *todos* los ordenadores, hasta que **avast!** deje de mostrar mensajes de advertencia. Dependiendo de la gravedad del ataque del virus o del malware, puede que no sea necesario repetir el análisis durante el arranque.

Si desea más información sobre malware o brotes de virus, consulte la sección [**4.9 Métodos avanzados para la eliminación de virus**](#4.9).

<a name="4.2"></a>
### 4.2 Vista general de la interfaz principal de usuario de avast!###

La interfaz principal de usuario de **avast!** muestra varias pestañas en el lado izquierdo de la ventana, que incluyen: *Visión general*, *Análisis*, *Herramientas*, y *Opciones*. Las pestañas  *Análisis*, *Herramientas* y *Opciones* contienen menús con elementos que se detallan a continuación.

Para ver la interfaz principal de usuario, **haga clic** ![](/sbox/screen/avast-es-1/22.png) en la bandeja del sistema (normalmente, se encuentra en la esquina inferior derecha de su pantalla)

![](/sbox/screen/avast-es-1/56.png)

*Figura 1: Interfaz principal de usuario* 

La siguiente lista le ofrece una breve descripción de las funciones de las pestañas principales y los submenús:

**Visión general**: la interfaz principal de usuario muestra el estado de **avast!**.

**Análisis**: desde esta pestaña se pueden iniciar diferentes opciones de análisis:

- *Smart scan* puede realizar los análisis que se muestran a continuación uno por uno;
- *Buscar virus* con: *Análisis rápido*, *Análisis completo del sistema*, *Análisis de unidades extraíbles*, *Análisis de carpeta seleccionada* y *Análisis durante el arranque* - que se explican con detalle más adelante;
- *Análisis de software desactualizado*;
- El *Análisis de amenazas en la red* analiza la configuración de su router doméstico y recomienda opciones que puedan necesitar actualizarse;
- *Análisis de rendimiento* - solo disponible en la versión de pago de avast!;

**Herramientas**: esta pestaña contiene un submenú de herramientas que incluye *Actualizador de software*, *Limpieza del navegador* y *Disco de recuperación*, descritos en la sección [**3.2 Herramientas adicionales de avast!**](/es/avast_manejo#3.2)

**Opciones**: esta pestaña contiene un menú que incluye *General*, *Protección activa*, *Antivirus* y *Actualización*, que se describen en las siguientes líneas:

- **General** incluye una sección de 'Mantenimiento' desde la que puede configurar el tamaño e historial de los *Informes* y del *Baúl de virus*.

- El menú **Protección activa** le permite configurar las opciones de análisis de *Sistema de archivos*, *Correo electrónico* y *Web*. **Nota** Se recomienda que no cambie las opciones habilitadas por defecto a no ser que comprenda el impacto de habilitar o deshabilitar cada una.

- El menú **Antivirus** le permite configurar opciones globales de análisis que incluyen *Exclusiones* y *Alertas*

- El menú **Actualización** muestra el *Programa* y las *Definiciones de virus* que están instalados actualmente, y le permite actualizar ambos tal y como se describe en la sección [**3.1 Cómo actualizar avast! manualmente**](/es/avast_manejo#3.1)

<a name="4.3"></a>
### 4.3 Cómo analizar su sistema para localizar malware y virus ###

En esta sección aprenderá cuáles son las opciones de análisis disponibles y cómo usarlas. También aprenderá a realizar un análisis completo del sistema y un análisis de carpeta seleccionada, así como un análisis durante el arranque.
El panel de *Análisis* muestra las cinco opciones de análisis disponibles en **avast!**; para verlas:

**Paso 1**. **Haga clic** en ![](/sbox/screen/avast-es-1/57.png) 

**Paso 3**. **Haga clic** en ![](/sbox/screen/avast-es-1/95.png) para activar la siguiente pantalla:

![](/sbox/screen/avast-es-1/96.png)

*Figura 2: la pestaña de Análisis muestra por defecto la opción de Análisis rápido*

Las descripciones que se ofrecen a continuación le ayudarán a elegir la opción de análisis más adecuada:

**Análisis rápido**: se recomienda esta opción a aquellos usuarios que dispongan de tiempo limitado para realizar un análisis en busca de amenazas potenciales.

**Análisis completo del sistema**: se recomienda usar esta opción cuando los usuarios disponen de tiempo suficiente para realizar un análisis exhaustivo del sistema. También se recomienda si es la primera vez que utiliza un antivirus en su ordenador. La duración de este análisis depende del número de documentos, archivos y discos duros que haya en el ordenador, así como de la velocidad del mismo. Consulte la sección [**4.4 Cómo realizar un análisis completo del sistema**](#4.4).

**Análisis de unidad extraíble**: se recomienda esta opción para analizar discos duros externos, memorias USB y otros medios, especialmente si no son suyos. Esta opción analizará cualquier dispositivo extraíble en busca de programas maliciosos que se ejecutan de forma automática cuando se conecta el dispositivo.

**Análisis de carpeta seleccionada**: se recomienda esta opción para analizar una carpeta específica o varias, en especial si sospecha o sabe que una carpeta en concreto está infectada. Consulte la sección [**4.5 Cómo analizar una carpeta seleccionada**](#4.5).

**Análisis durante el arranque**: el análisis durante el arranque le permite realizar un análisis completo del disco duro antes de que el sistema operativo **Microsoft Windows** se inicie por completo. Se recomienda esta opción si desea un análisis completo y exhaustivo de su sistema y puede requerir más tiempo. Consulte la sección [**4.6 Cómo realizar un análisis durante el arranque**](#4.6).

**Consejo**: **Haciendo clic** en ![](/sbox/screen/avast-es-1/59.png) podrá ver y ajustar los detalles de un análisis determinado, por ejemplo, las zonas que se están analizando.

<a name="4.4"></a>
### 4.4 Cómo realizar un análisis completo del sistema ###

**Paso 1**. **Seleccione** la opción *Análisis completo del sistema* del menú (ver figura 2, arriba).

** Paso 2**. **Haga clic** en ![](/sbox/screen/avast-es-1/60.png) para activar la siguiente pantalla:

![](/sbox/screen/avast-es-1/61.png)

*Figura 3: el panel de Análisis muestra la ejecución del análisis completo del sistema* 

Una vez se haya completado el análisis completo del sistema, y si se ha encontrado una amenaza para el sistema, el panel *Análisis completo del sistema* mostrará una pantalla similar a esta:

![](/sbox/screen/avast-es-1/62.png)

*Figura 4: el elemento de Análisis completo muestra los archivos infectados encontrados*

Si el análisis completo del sistema ha encontrado amenazas, **haga clic** en el botón ![](/sbox/screen/avast-es-1/69.png) para abrir la página de resultados. Consulte la sección [**4.7 Cómo enfrentarse a los virus**](#4.7) para obtener más información.

<a name="4.5"></a>
### 4.5 Cómo analizar una carpeta ###

**Paso 1**. **Seleccione *Análisis de carpeta seleccionada*** del menú (ver figura 2, arriba).

**Paso 2**. **Haga clic** en ![](/sbox/screen/avast-es-1/60.png) para activar la siguiente pantalla:

![](/sbox/screen/avast-es-1/63.png)

*Figura 5: Ventana de diálogo de selección de áreas a analizar*

La ventana de diálogo de *Selección de áreas a analizar* le permite especificar la carpeta que quiere analizar. Puede seleccionar más de una carpeta. Cuando seleccione las casillas junto a las carpetas, la ruta se mostrará en el campo de texto *Rutas seleccionadas:*. 

**Paso 3**. **Haga clic** en ![](/sbox/screen/avast-es-1/64.png) para empezar a analizar sus carpetas y activar la siguiente pantalla:

![](/sbox/screen/avast-es-1/65.png)

*Figura 6: ejecución del análisis de carpeta seleccionada.* 

**Consejo**: **avast!** le permite analizar carpetas individuales mediante un menú emergente que aparece cada vez que hace clic con el botón derecho en una carpeta. Solo tiene que **seleccionar** *![](/sbox/screen/avast-es-1/66.png) Analizar...*, que aparecerá antes del nombre del archivo que desea analizar.

Si el análisis de carpetas ha encontrado amenazas, **haga clic** en el botón ![](/sbox/screen/avast-es-1/69.png) para abrir la página de resultados. Consulte la sección [**4.7 Cómo enfrentarse a los virus**](#4.7) para obtener más información.

<a name="4.6"></a>
### 4.6 Cómo realizar un análisis durante el arranque ###

El análisis durante el arranque de **avast!** le permite realizar un análisis completo del disco duro antes de que el sistema operativo **Microsoft Windows** se inicie por completo. Mientras se realiza el análisis durante el arranque, todos (o casi todos) los programas de malware y virus siguen inactivos, es decir, aún no han podido iniciarse ni interactuar con otros sistemas. Así son más fáciles de reconocer y eliminar. El análisis durante el arranque también accede directamente al disco, evitando los drivers del sistema de archivos de **Windows**, que pueden estar infectados. Esto contribuye a encontrar más virus y 'rootkits' – el nombre de una forma de malware particularmente maligna. 

Se **recomienda encarecidamente** que ejecute un análisis durante el arranque si tiene una sospecha, aunque sea remota, de que su sistema informático puede estar amenazado o infectado. El **Análisis durante el arranque** y el **Disco de recuperación** (descrito en la sección [3.2.3 Disco de recuperación](/en/howtouseavast#3.3.3)) son los análisis más completos y exhaustivos que le ofrece avast!. El análisis durante el arranque puede llevar más tiempo, dependiendo de la velocidad del ordenador, de la cantidad de datos y del número de discos duros. 

Para ejecutar un análisis durante el arranque, siga los pasos descritos a continuación:

**Paso 1**. **Haga clic** en ![](/sbox/screen/avast-es-1/57.png) para activar el panel de *Análisis*.

**Paso 2**. **Seleccione** la opción ![](/sbox/screen/avast-es-1/67.png) del menú desplegable.   

**Paso 3**. **Haga clic** en ![](/sbox/screen/avast-es-1/60.png) para programar un análisis durante el arranque la próxima vez que inicie el sistema.

**Paso 3**. **Reinicie su ordenador** para comenzar el análisis.

**Nota**: un análisis durante el arranque se realiza antes de que el sistema operativo y la interfaz hayan cargado completamente; de manera que el progreso del análisis se mostrará así en su pantalla: 

![](/sbox/screen/avast-es-1/68.png)

*Figura 7: El análisis durante el arranque de avast!*

**avast!** le preguntará qué quiere hacer si se detectan virus. Puede seleccionar las acciones posibles mediante los números adecuados del teclado. Recomendamos que **seleccione el número 2** *Arreglar automáticamente* para que avast! se encargue de los virus de forma automática.

Tenga en cuenta que eliminar un archivo infectado o transferirlo al Baúl de virus puede dar como resultado que alguna información o funcionalidad de su sistema sea inaccesible. En casos extremos en los que un virus haya infectado archivos vitales para el funcionamiento del sistema operativo, transferir estos archivos al Baúl de virus o eliminarlos puede ocasionar que su sistema operativo no se inicie correctamente.

<a name="4.7"></a>
### 4.7 Cómo enfrentarse a los virus ###

Las secciones 4.5 y 4.6 muestran cómo analizar el sistema con avast! de forma manual. Cuando se encuentra un virus durante cualquiera de esos análisis, avast! le informa mostrando el mensaje *amenaza detectada*. Para saber cómo tratar cualquier malware o virus detectados durante un análisis, siga los pasos descritos a continuación:

**Paso 1**. **Haga clic** en ![](/sbox/screen/avast-es-1/69.png) para activar la siguiente pantalla:

![](/sbox/screen/avast-es-1/70.png)

*Figura 9: La ventana de RESULTADOS DEL ANÁLISIS muestra la advertencia ¡AMENAZA DETECTADA!*

**Paso 2**. Para mostrar la lista desplegable de acciones posibles, **haga clic** en la flecha que se encuentra debajo de *Acciones*, como se muestra en la imagen anterior

**Nota**: en este ejercicio se explica cómo mover archivos infectados a la *Cuarentena (Baúl de  virus)*. Sin embargo, la lista desplegable muestra tres opciones adicionales que se describen a continuación:

**Reparar**: esta acción intentará reparar el archivo dañado.

**Eliminar**: esta acción eliminará permanentemente el archivo dañado.

**No hacer nada**: esta acción hace exactamente lo que dice, y *no se recomienda en absoluto* cuando se trata de malware o virus potencialmente peligrosos.

**Paso 3**. **Seleccione** el elemento *Mover al Baúl*, y **haga clic** *Aplicar*.


![](/sbox/screen/avast-es-1/73.png)

*Figura 11: La amenaza detectada ha sido transferida a la Cuarentena (Baúl de virus)*

**avast!** monitoriza constantemente su ordenador en busca de virus y malware, ejecutándose de fondo mientras usted trabaja. 
Cuando *avast!* detecta malware o un archivo sospechoso, le alertará con un mensaje emergente.

La acción por defecto transferirá el archivo a la *Cuarentena (Baúl de virus)*. La siguiente sección describe cómo enfrentarse a cualquier malware o virus detectados durante un análisis que hayan sido transferidos a la *Cuarentena Baúl de virus*

<a name="4.8"></a>
### 4.8 Cómo utilizar el Baúl de virus ###

Durante el proceso de instalación de **avast!**, el *Baúl de virus* de **avast!** fue creado en su disco duro. El *Baúl de virus* es una carpeta especial aislada del resto de su sistema informático, y se utiliza para almacenar el malware y los virus detectados durante el análisis, así como documentos, archivos o carpetas infectados o amenazados. 

Puede acceder al contenido del *Baúl de virus* y decidir cómo tratar los archivos que se almacenan allí:

**Paso 1**. **Haga clic** en ![](/sbox/screen/avast-es-1/57.png) y **haga clic** en ![](/sbox/screen/avast-es-1/74.png) para activar la siguiente pantalla:

![](/sbox/screen/avast-es-1/75.png)

*Figura 13: el Baúl de virus muestra un virus*

**Paso 2**: **Haga clic con el botón derecho** en cada elemento para mostrar el menú de acciones posibles para un archivo seleccionado como se muestra a continuación:

![](/sbox/screen/avast-es-1/76.png)

*Figura 14: Menú emergente de acciones contra virus disponibles en el Baúl de virus*

**Nota**: Hacer doble clic en un elemento del *Baúl de virus* no hará que dicho elemento se abra, se active o se ejecute. Solo mostrará las propiedades del archivo, la misma información que obtendría si seleccionase *Propiedades* en el menú emergente.

La lista siguiente describe las acciones posibles contra los virus que muestra el menú emergente:

**Eliminar**: El archivo se eliminará del *Baúl de virus* de forma irreversible.

**Restaurar**: El archivo será restaurado a su ubicación original.

**Extraer**: El archivo será copiado en la carpeta que usted especifique.

**Analizar**: El archivo será analizado.

**Enviar al laboratorio de virus...**: Al seleccionar esta opción se activará un formulario de envío que usted tendrá que cumplimentar y enviar junto al archivo para que el laboratorio interno de avast! pueda analizarlo. ¡No envíe archivos que contengan información confidencial!

**Propiedades**: Esta opción le proporcionará más información sobre el archivo. 

**Agregar...**: Esta opción le permite examinar el sistema para buscar otros archivos que desee agregar al *Baúl de virus*. Esta función resulta muy útil si desea proteger archivos determinados durante un brote.

**Actualizar todos los archivos**: Esta opción le permite actualizar la lista de los archivos presentes en el *Baúl de virus*, para poder visualizar los últimos archivos.

<a name="4.9"></a>
### 4.9 Métodos avanzados para la eliminación de virus ###

En ocasiones, la protección que ofrecen **avast!**, **Comodo Firewall** y **Spybot** no es suficiente; a pesar de nuestros esfuerzos, el malware y los virus pueden infectar nuestro sistema informático. En la sección [**4.1 Guía rápida para enfrentarse a brotes de virus**](#4.1), ofrecimos una serie de métodos para lidiar con malware y virus persistentes. Sin embargo, *existen* opciones alternativas que puede emplear para eliminar dichas amenazas de su ordenador.

**Método A:
 Cómo utilizar CD/DVD o USB de rescate anti-malware**

Algunas empresas informáticas de anti-malware ofrecen un CD/DVD antivirus de 'rescate'. Se pueden descargar en formato de imagen ISO (un formato que se graba fácilmente en un CD, DVD o se copia en una memoria USB). 

Para empezar a usar estos CD/DVD/USB anti-malware de rescate, siga estos pasos:

1. Descargue la imagen ISO de rescate específica (ver lista inferior) y grabe el programa anti-malware de rescate en un CD/DVD, o cópielo a un USB.  <br>
*Puede usar programas gratuitos como [**ImgBurn**](http://www.imgburn.com/) para grabar la imagen en el disco, u otros como [**Universal USB Installer**](http://www.pendrivelinux.com/universal-usb-installer-easy-as-1-2-3/) para guardar la imagen en una memoria USB*<br>
**Nota:** Es mejor realizar este paso en otro ordenador que no esté infectado, si tiene esa posibilidad.

2. Inserte el disco en el reproductor de CD/DVD o conecte la memoria USB a un ordenador infectado. Después reinicie el ordenador desde la memoria USB o el CD/DVD.  <br>
*En general se puede hacer haciendo clic en F10, F12 o Esc desde el propio teclado al encender el ordenador. Preste atención a las instrucciones que aparecen en su pantalla mientras se inicia el ordenador para aprender a hacerlo en su sistema. Busque en Internet las instrucciones para iniciar (arrancar) su ordenador desde una memoria USB o un CD/DVD. Las instrucciones pueden ser diferentes para cada ordenador.*

3. Una vez el ordenador infectado se haya iniciado desde el USB/CD/DVD, vuelva a conectarlo a Internet para que el programa de rescate anti-malware pueda actualizar sus definiciones de virus si es necesario. <br>
*Es mejor conectarse a Internet mediante conexión por cable, si es posible*.

4. Empiece a analizar los discos duros de su ordenador para eliminar amenazas de malware y virus. 

A continuación presentamos una lista de imágenes de antivirus de rescate gratuitas (en inglés):

- [**Avira AntiVir Rescue CD**](https://www.avira.com/en/download/product/avira-rescue-system)
- [**AVG Rescue CD**](http://www.avg.com/us-en/avg-rescue-cd)
- [**BitDefender Rescue CD**](http://www.bitdefender.com/support/How-to-create-a-BitDefender-Rescue-CD-627.html)
- [**F-Secure Rescue CD**](http://www.f-secure.com/en/web/labs_global/rescue-cd)
- [**Kaspersky Rescue CD**](http://support.kaspersky.com/viruses/rescuedisk/)
- [**Dr.Web Live Rescue CD**](http://www.freedrweb.com/livecd/)

Aquí hay más recursos con herramientas y métodos adicionales que pueden resultarle útiles e interesantes (en inglés):

- [**How to easily clean an infected computer (Malware Removal Guide)**](http://malwaretips.com/blogs/malware-removal-guide-for-windows/)
- [**Malware Removal Guide for Windows**](http://www.selectrealsecurity.com/malware-removal-guide)

**Nota:** Puede utilizar cada una de las herramientas mencionadas por separado para maximizar las posibilidades de limpiar su ordenador de forma eficaz.

**Método B: Reinstalar el sistema operativo Microsoft Windows**

En raras ocasiones, una infección causada por un virus puede ser *tan* destructiva que las herramientas de software que recomendamos antes pueden resultar inútiles. En situaciones como esa le recomendamos que siga el proceso descrito a continuación: 

***Nota**: Antes de empezar, asegúrese de que tiene todos los números de serie y de licencia apropiados y copias de instalación del sistema operativo **MS Windows**, así como de otros programas que necesite. Puede que este proceso le lleve mucho tiempo, pero vale la pena si no consigue eliminar el malware y los virus de otra manera.*

1. Cree una copia de seguridad de todos los archivos personales que tenga en su ordenador.

2. Reinstale el sistema operativo **Microsoft Windows** formateando completamente el disco.

3. Actualice el sistema operativo **Microsoft Windows** una vez la instalación se haya completado.

4. Instale **avast!** (o su antivirus favorito) y actualícelo.

5. Instale todos los programas que necesite. Recuerde descargar las últimas versiones y todas las actualizaciones de cada programa. <br><br>**Nota**: en ningún caso debe conectar su disco de seguridad al ordenador *antes* de haber completado estas tareas. Corre el riesgo de volver a infectar su ordenador.

6. Conecte su disco de seguridad al ordenador y realice un análisis exhaustivo para detectar y eliminar cualquier amenaza. 

7. Una vez haya detectado y eliminado esas amenazas, podrá copiar sus archivos de su disco de seguridad al disco duro del ordenador.


