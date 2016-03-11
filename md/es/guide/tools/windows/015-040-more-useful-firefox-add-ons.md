

---

lang: es
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 4
depth: 3
title: More Useful Firefox Add-Ons

---

Lista de secciones de esta página:

- [**5.0 Acerca de los complementos**](#5.0)
- [**5.1 Utilización de HTTPS Everywhere**](#5.1)
- [**5.2 Utilización de Adblock Plus**](#5.2)
- [**5.3 Utilización de Beef Taco (Targeted Advertising Cookies Opt-Out)**](#5.3)
- [**5.4 Utilización de Better Privacy**](#5.4) 
- [**5.5 Otros complementos útiles**](#5.5)

-------

<a name="5.0"></a>
## 5.0 Acerca de los complementos ##
Los **complementos de Mozilla Firefox** que se presentan en esta sección están pensados para mejorar o proteger el anonimato, privacidad y seguridad de las sesiones de exploración del usuario. Para descargarlos, consulta la sección [**Descarga de Firefox**](/es/firefox_principal).

<a name="5.1"></a>
## 5.1 Utilización de HTTPS Everywhere ##

![](/sbox/screen/firefox-en-1/httpseverywherelogo.png)

**HTTPS Everywhere** es una extensión de **Mozilla Firefox** que garantiza que la comunicación con una lista concreta de sitios web se realice siempre a través de un canal cifrado (*https*). Aunque hay muchos sitios web que sí que ofrecen cifrado, de manera predeterminada suelen ofrecer una dirección http no cifrada. La extensión **HTTPS Everywhere** soluciona estos problemas al volver a formular todas las solicitudes del usuario en protocolo **HTTPS**. Esta extensión se ejecuta silenciosamente en segundo plano y te garantiza que todas las sesiones en Internet con dichos sitios seleccionados estén protegidas y sean seguras.  No obstante, *únicamente* funciona cuando dichos sitios utilizan el protocolo **HTTPS**.

Tras haber instalado correctamente la extensión **HTTPS Everywhere**, aparecerá la siguiente pantalla:

![](/sbox/screen/firefox-es-1/75.png)

*Figura 1: La pantalla ¿Debe HTTPS Everywhere utilizar el Observatorio SSL?* 

**Paso 1**. **Haz clic en** ![](/sbox/screen/firefox-es-1/76.png) para que aparezca la siguiente pantalla: 

![](/sbox/screen/firefox-es-1/77.png)

*Figura 2: La ventana Opciones del Observatorio SSL* 

**Nota**: Si se ha instalado anteriormente **HTTPS Everywhere** en el explorador **Firefox**, **selecciona Herramientas > HTTPS Everywhere > Opciones del Observatorio SSL** y comprueba que están marcadas las opciones *¿Utilizar el Observatorio?* y *Cuando vea un nuevo certificado, comuníquele al Observatorio a qué ISP está conectado*. Si no utilizas **Tor**, **activa** también la opción *Verificar certificados incluso si Tor no está disponible*.  

<a name="5.2"></a>
## 5.2 Utilización de Adblock Plus ##

![](/sbox/screen/firefox-en-1/adblockpluslogo.png)

**Adblock Plus** es una extensión de filtrado de contenido pensada para limitar o restringir la capacidad de los anuncios de mostrarse. 

Tras haber instalado correctamente **Adblock Plus**, se mostrará el siguiente mensaje: 
 
![](/sbox/screen/firefox-es-1/60.png)

*Figura 3: Mensaje de correcta instalación de Adblock Plus*

**Paso 1**. **Selecciona Herramientas > Adblock Plus > Preferencias de filtros...** para abrir la siguiente ventana:

![](/sbox/screen/firefox-es-1/63.png)

*Figura 4: Las Preferencias de filtros de AdBlock Plus con tres suscripciones de filtros*

**Paso 2**. **Haz clic en** cada casilla de suscripción de filtros para activarla (como se ve en la *Figura 4*) y, a continuación, **desactiva** la opción ![](/sbox/screen/firefox-es-1/64.png) para impedir que se muestren *todos* los anuncios descritos o enumerados en dichos filtros.

**Paso 3**.  Si trabajas con más de un idioma, **haz clic en** ![](/sbox/screen/firefox-es-1/65.png) para ver distintas suscripciones de filtros y, a continuación, **haz clic en** ![](/sbox/screen/firefox-es-1/66.png) para abrir una lista desplegable de distintas suscripciones de filtros, **selecciona** la correcta y luego **haz clic en**  ![](/sbox/screen/firefox-es-1/67.png).

**Paso 4**. Para actualizar las suscripciones de filtros, **haz clic en** ![](/sbox/screen/firefox-es-1/68.png) y, a continuación, **selecciona** el elemento *Actualizar filtros* del menú desplegable.

<a name="5.3"></a>

## 5.3 Utilización de Beef Taco (Targeted Advertising Cookies Opt-Out) ##

![](/sbox/screen/firefox-en/beeftacologo.png)

**Beef Taco** es un complemento de **Mozilla Firefox** con el que se pueden administrar las *cookies* de publicidad de una serie de empresas, como **Google**, **Microsoft** y **Yahoo**, entre otras. El complemento se puede configurar para borrar las **cookies** denominadas **Targeted Advertising Cookies Opt-Out** automáticamente. No obstante, también permite que los usuarios **Expertos** y **Avanzados** especifiquen con más detalle qué *cookies* se permiten en el sistema y cuáles se borran.

<a name="5.4"></a>
## 5.4 Utilización de Better Privacy ##

![](/sbox/screen/firefox-en-1/adblockpluslogo.png)

**Better Privacy** es un complemento de **Mozilla Firefox** que ayuda a proteger el sistema de unas **cookies** especiales que se denominan **LSO** (**objetos locales compartidos**, del inglés *local shared objects*) que es posible que se coloquen en el equipo por medio de un *script* de *Flash*. Estas *cookies* no se eliminan por medio del procedimiento habitual de **Firefox** de limpieza de *cookies*.

<a name="5.5"></a>
## 5.5 Otros complementos útiles ##
En esta sección se describen una serie de complementos y extensiones de utilidad, gratuitas y de código abierto (o en proceso de ser de código abierto), que pueden mejorar o ampliar la posibilidad de navegar por Internet de forma privada y segura. 

### 5.5.1 Cryptocat ###

[![](/sbox/screen/firefox-en-1/cryptocatlogo.png)](https://addons.mozilla.org/es/firefox/addon/cryptocat/)

**Cryptocat** es un complemento de mensajería instantánea de código abierto, cifrado y privado que funciona en el explorador. Por tanto, puede que en determinadas situaciones resulte más fácil utilizarlo que otros programas similares de chat por texto. **Cryptocat** permite crear una sala de chat virtual en la que se puede conversar con todos los miembros o bien establecer conversaciones en privado uno a uno con participantes individuales. Todas las conversaciones del chat se cifran y descifran en el explorador de los usuarios antes de enviarse y después de recibirse. La extensión para explorador de **Cryptocat** está disponible para **Mozilla Firefox**, **Google Chrome** y **Apple Safari**, y también existe una aplicación para **Mac OS X**. [**Más información...**](https://crypto.cat/)

### 5.5.2 Disconnect ###

[![](/sbox/screen/firefox-en-1/disconnectmelogo.png)](https://addons.mozilla.org/es/firefox/addon/disconnect/)

**Disconnect** está pensado para proteger tus datos de rastreadores web de terceros, al tiempo que analiza los rastreadores y los clasifica en distintos grupos, como por ejemplo de publicidad, analíticos y de redes sociales. [**Más información...**](https://www.disconnect.me/)

### 5.5.3 DuckDuckGo ###

[![](/sbox/screen/firefox-en-1/duckduckgologo.png)](https://addons.mozilla.org/es/firefox/addon/duckduckgo-ssl/)

**DuckDuckGo** te ofrece una alternativa privada y segura frente a motores de búsqueda en Internet como **Google** o **Bing**. **DuckDuckGo** no guarda ni comparte la información del usuario, y todos los usuarios tienen acceso a la misma información. Puedes ir directamente al sitio web de [**DuckDuckGo**](https://duckduckgo.com/) o bien **hacer clic** en el icono de **DuckDuckGo** para instalarlo en la barra de búsqueda como motor de búsqueda predeterminado. 

### 5.5.4 vtzilla ###

[![](/sbox/screen/firefox-en-1/vtzillalogo.png)] (https://addons.mozilla.org/es/firefox/addon/vtzilla/)

**vtzilla** es una extensión para el explorador **Mozilla Firefox** que analiza las descargas y los sitios web en busca de programas maliciosos y virus. Tras haber instalado correctamente la extensión **vtzilla**, la barra de herramientas de **vtzilla** (que puede mostrarse y ocultarse) aparece debajo de la barra de herramientas de navegación de **Firefox**. Basta con copiar y pegar o escribir una dirección web en el cuadro de búsqueda de **vtzilla** y la solicitud de búsqueda se dirigirá a **Virus Total**, un sitio web que ejecuta más de 40 análisis distintos del vínculo o sitio web especificado en busca de programas maliciosos o virus. Además, **vtzilla** reduce el riesgo de infección al añadir otro nivel de protección a un programa antivirus ya existente (como por ejemplo [**avast!**](https://securityinabox.org/es/avast_principal), ya que analiza los archivos descargables. [**Más información...**](https://www.virustotal.com/es/documentation/browser-extensions/).

### 5.5.5 ShareMeNot ###

[![](/sbox/screen/firefox-en-1/sharemenotlogo.png)](https://addons.mozilla.org/es/firefox/addon/sharemenot/)

**ShareMeNot** evita que te rastreen botones de terceros (como el botón “Me gusta” de Facebook o el botón “Twittear” de Twitter) que están incrustados en sitios de Internet, a menos que hagas clic en ellos. [**Más información...**](http://sharemenot.cs.washington.edu/.)


### 5.5.6 Click&Clean ###

[![](/sbox/screen/firefox-en-1/clickcleanlogo.png)](https://addons.mozilla.org/es/firefox/addon/clickclean/) 

**Click&Clean** borra automáticamente datos privados al cerrar **Firefox**, lo que incluye borrar el historial de descargas, el historial de exploración y eliminar las *cookies*, incluidos los **objetos locales compartidos de Flash** (**LSO**). Asimismo, borra los archivos temporales y vacía la caché local. 

**Nota**: Otra opción que los usuarios también pueden plantearse es utilizar aplicaciones externas, como [**CCleaner**](https://securityinabox.org/es/ccleaner_principal), **Wise Disk Cleaner** etc., en sistemas operativos **Windows**, o **Janitor** o **BleachBit** en **Linux**.

