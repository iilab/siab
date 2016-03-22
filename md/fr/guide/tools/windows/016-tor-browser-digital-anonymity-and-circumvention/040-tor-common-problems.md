

---

lang: fr
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 4
depth: 3
title: Tor Common Problems

---

- [**5.0 Acerca de Resover Problemas Comúnes de Tor**](#5.0)
- [**5.1 Visualizar el Informe de Mensajes**](#5.1)
- [**5.2 Configurar las Preferencias de la Red Tor**](#5.2)

-------

<a name="5.0"></a>
## 5.0 Acerca de Resolver Problemas Comúnes de Tor ##

Existen varias razones por las cuales **Tor** podría no funcionar adecuadamente. Unos
cuantos de los más comúnes problemas se describen aquí, junto con sugerencias de 
solución. Todas las funciones descritas en esta sección se hallan en el *Panel de Control de Vidalia*.

**Nota**: Un sorprendente número de errores comúnes puede resolverse simplemente reiniciando la computadora, o volviendo a extraer el **Paquete del Navegador Tor**.

<a name="5.1"></a>
## 5.1 Visualizar el Informe de Mensajes ##

Puedes visualizar los informes de mensajes de **Tor** incluso cuando está intentando establecer una conexión inicial a la red **Tor**. Los informes de mensajes pueden ayudarte a determinar si el software está trabajando adecuadamente, y si no, la causa del problema.

**Paso 1**. **Pulsa** ![](/sbox/screen/tor-es/58.png) para activar la
pantalla de *Informe de Mensajes*, y luego **pulsa** la pestaña *Avanzado* para mostrar una pantalla parecida a la siguiente:

![](/sbox/screen/tor-es/59.png)

*Figura 1: Informe de Mensajes de Vidalia*

Este informe muestra que **Tor** se ha iniciado. Este continuará mostrando mensajes de cómo está funcionando **Tor**. No estes demasiado preocupado sobre la advertencia de *software experimental*; a pesar de este mensaje, **Tor** es la mejor y más meticulosamente probada herramienta de anonimato disponible.

### 5.1.1 Entender Mensajes de Error Comúnes ###

Sin embargo, existen algunos importantes mensajes de error que son críticos si tienes problemas con **Tor**; algunos se describen a continuación.

- *connection_create_listener(): Could not bind to 127.0.0.1:9050: Address already in use. Is Tor already running?*

Este mensaje indica que otro programa **Tor** ya ha sido iniciado. La solución más simple en este caso sería cerrar todos los programas **Vidalia** en funcionamiento o reiniciar la computadora.

- *Vidalia was unable to start Tor. Check your settings to ensure the correct name and location of your Tor executable is specified*

Este mensaje indica que el programa **Vidalia** no puede ubicar el archivo ejecutable de **Tor**, *tor.exe* el cual aparece como se muestra: ![](/sbox/screen/tor-es/60.png). Para resolver este problema, ejecuta los siguientes pasos:

"**Paso 1**. **Reinicia** tu computadora e intenta ejecutar nuevamente el **Navegador Tor**. Si el error persiste, ejecuta el Paso 2**:

**Paso 2**. **Borra** la carpeta actual del **Navegador Tor**, luego descarga la última versión del **Paquete del Navegador Tor**. **Extrae** el **Paquete del Navegador Tor**, y luego **ejecútalo**."

- *I have learned some directory information, but not enough to build a circuit*

Este mensaje puede aparecer repetidamente mientras **Tor** se inicia por primera vez, y puede continuar apareciendo por mucho tiempo si tienes una conexión muy lenta a la Internet. Este simplemente significa que **Tor** todavía está en proceso de descargar la información necesaria sobre la red **Tor** para establecer un circuito **Tor** o conexión a tu sistema.

Cuando **Tor** esta listo, el informe de mensajes mostrará el siguiente mensaje en la *Figura 2* a continuación:

- *Tor has successfully opened a circuit. Looks like client functionality is working.*

![](/sbox/screen/tor-es/61.png)

*Figura 2: Mensaje confirmando una conexión exitosa resaltado en azul oscuro*

Este mensaje indica que **Tor** ha establecido con éxito una ruta a través de su red y parece estar funcionando correctamente.

**Nota**: Incluso cuando estas utilizando **Mozilla Firefox**, *debes obligatoriamente* habilitar el **Torbutton** antes de que puedas navegar anónimamente en Internet. Si estás utilizando un navegador diferente, debes obligatoriamente configurar sus preferencias de servidor proxy de modo que se conecte a la Internet a través de **Tor**.

Si el informe de mensajes deja de producir nueva información después de quince minutos más o menos, e incluso después de mostrar un mensaje de *Opening Control listener* o *Tor has learned some directory information, but not enough to build a circuit*, entonces podrías necesitar ajustar la configuración de la red **Tor**. Es posible que tu actual conexión a Internet necesite que utilices un servidor proxy específico o que bloquee ciertos puertos. También es posible que tu gobierno o tu ISP haya empezado a bloquear el acceso a
la red **Tor**.

<a name="5.2"></a>
## 5.2 Configurar las Preferencias de la Red Tor ##

Si encuentras que **Tor** no conecta cuando lo instalas o lo ejecutas por primera vez, o que ha dejado de funcionar adecuadamente, el cambio de la configuración de la red podría resolver el problema. La configuración de la conexión de red está
vinculada al servidor proxy, los puertos o los puentes de retransmisión, como se trata en esta sección.

**Paso 1**. **Pulsa** ![](/sbox/screen/tor-es/62.png) en el *Panel de Control de Vidalia* para detener **Tor**.

**Paso 2**. **Pulsa** ![](/sbox/screen/tor-es/63.png) para activar la pantalla de *Preferencias*.

**Paso 3**. **Pulsa** ![](/sbox/screen/tor-es/71.png) para ver la pantalla de *Preferencias* en modo *Red* como sigue:

![](/sbox/screen/tor-es/64.png)

*Figura 3: Pantalla de Preferencias en modo Red*

**Paso 4**. **Pulsa** ![](/sbox/screen/tor-es/65.png) aceptar las preferencias y cerrar la pantalla *Preferencias*, luego **pulsa** ![](/sbox/screen/tor-es/66.png) en el *Panel de Control de Vidalia* para iniciar **Tor**.

### 5.2.1 Utilizar un Servidor Proxy con Tor ###

Si se te requiere utilizar un servidor proxy para acceder a la Internet, entonces especifíca sus detalles en esta pantalla. En general, los servidores proxy son más comúnes en redes de corporaciones y universidades, pero los servidores proxy son a veces requeridos en los Café Internet, o incluso a nivel nacional en algunos países. Si la información proxy necesaria no está claramente publicada, podrías tener que consultar un adminsitrador de red o alguien que utilice la misma conexión a Internet.

**Paso 1**. **Habilita** la opción *Uso un proxy para acceder a Internet*.

**Paso 2**. **Ingresa** los detalles del proxy en los casilleros proporcionados:

![](/sbox/screen/tor-es/67.png)

*Figura 4: Sección de Configuración de Proxy*

### 5.2.2 Gestionar Restricciones de Puerto ###

Algunas redes o configuraciones de computadora pueden restringir el acceso a ciertos puertos. Si puedes navegar normalmente por sitios web, entonces puedes confiar en que por lo menos dos puertos (*80* y *443*) son accesibles. Puedes configurar **Tor** para funcionar exclusivamente a través de estos puertos.

**Paso 1**. **Habilita** la opción *Mi cortafuegos sólo me permite conectarme a ciertos puertos*.

**Paso 2**. El casillero de *Puertos Permitidos* debería mostrar ya '80,443', como se muestra en la *Figura 5* a continuación:

![](/sbox/screen/tor-es/68.png)

*Figura 5: Sección de Configuración de Cortafuegos especificando los puertos abiertos en la red*

### 5.2.3 Utilizar un Puente de Retransmisión (Bridge Relay) ###

Si *todavía* no eres capaz de conectarte a la red **Tor**, te quedan dos opciones:

**Opción 1**: Dirígete al [**Tor FAQ wiki**](https://wiki.torproject.org/noreply/TheOnionRouter/TorFAQ) para obtener sugerencias.

**Opción 2**: Si vives en uno de los pocos países que bloquea activamente **Tor** para acceder a la Internet, podrías necesitar utilizar un *puente de retransmisión (bridge relay)* - o en breve *puentes (bridges)* - para establecer una conexión a la red de anonimato **Tor**.

Un *puente* **Tor** te permite acceder a la red **Tor** - incluso si está bloqueado dentro de tu país - proporcionándote un 'primer paso' oculto dentro de la red. Para utilizar esta opción, debes obligatoriamente proporcionarle a **Tor** una ubicación de por lo menos un puente. Idealmente, debes ingresar tres o más ubicaciones de puentes. Si alguien que conoces y en quien confias está ya utilizando un puente, podrías solicitarle esta información.

Opcionalmente, podrías utilizar uno de los dos métodos respaldados por el **Proyecto Tor (Tor Project)** *base de datos de Puentes*.

**Método 1**: Envía un correo electrónico a [**bridges |at| torproject |dot| org**], desde cualquier cuenta de **Gmail**, con las palabras "obtener puentes (get bridges)" en el cuerpo de tu mensaje. La base de datos responderá con las ubicaciones de tres o más puentes. (Recuerda, ¡sólo debes ingresar a tu cuenta de **Gmail** utilizando la dirección [**https://mail.google.com**](https://mail.google.com)!)

**Método 2**: **Cierra** el programa **Tor** y dirígete al sitio web de la base de datos *Puente*  del **Proyecto Tor (Tor Project)** [**https://bridges.torproject.org/**](https://bridges.torproject.org/), y esta te mostrará información sobre tres puentes diferentes.

**Nota**: La *Base de datos de Puentes* esta diseñada para impedir a cualquiera averiguar fácilmente todas las ubicaciones de puentes; en un inicio, parece hacer público los mismos puentes cada vez que los solicitas. Sin embargo, despúes de que ha pasado suficiente tiempo, este finalmente te proporcionará nuevas ubicaciones.

**Paso 1**. **Habilita** la opción *Mi ISP bloquea conexiones a la red Tor*.

**Paso 2**. **Corta y pega**  o **ingresa** la ubicación de un puente en el casillero de *Agregar un Puente*, como se muestra en la *Figura 6*. La información del Puente incluirá una dirección IP y un número de puerto, tal como *79.47.201.97:443*, y *podría* también incluir una larga serie de letras o números al final, tal como *80E03BA048BFFEB4144A4359F5DF7593A8BBD47B*.

**Paso 3**. **Pulsa** ![](/sbox/screen/tor-es/69.png) para agregar la ubicación en el panel debajo del casillero de *Agregar un Puente*.

**Paso 4**. **Repita** los pasos 2 y 3 por cada ubicación de puente adicional; se recomienda que ingreses como mínimo tres; para ingresar más, tendrás que esperar un momento para que la base de datos de puentes se refresque a sí misma.

![](/sbox/screen/tor-es/70.png)

*Figura 6: Agregar una Ubicación de Puente de Retransmisión*

