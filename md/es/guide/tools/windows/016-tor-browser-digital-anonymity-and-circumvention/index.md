

---

lang: es
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 016
title: Tor Browser - Digital Anonymity and Circumvention

---

**Página principal**
			
[**https://www.torproject.org**](https://www.torproject.org/)
			
**Requisitos del sistema**:

- Cualquier versión de **Windows** (XP o más nueva)
- Conexión a Internet		

**Versión usada en esta guía**:

- Navegador Tor 4.0.2

**Última revisión de este capítulo**

- Agosto de 2015

**Licencia** 

- Libre, software de código abierto ([licencia BSD](https://es.wikipedia.org/wiki/Licencia_BSD))

**Lectura requerida**: 

- Instrucciones capítulo [**8. Mantenerse en el anonimato y evadir la censura en Internet**](/es/chapter-8) 

**¿Qué obtendrá?**: 

- Habilidad para ocultar su identidad digital de los sitios que visite.
- Habilidad para ocultar sus destinos en línea desde los **Proveedores de Internet (ISPs)** y de otros mecanismos de vigilancia.
- Habilidad para evitar la censura en Internet y reglas de filtros.

**GNU Linux, Mac OS y otros programas compatible de Microsoft Windows**:

El **Navegador Tor** está disponible para **GNU Linux**, **Mac OS**, **Microsoft Windows** y sistemas operativos **Android**. **Tor** es la herramienta más recomendable y rigurosamente testada para mantener su actividad en línea de forma anónima. A continuación, presentamos una serie de soluciones posibles:


* [**Riseup VPN**](https://help.riseup.net/es/vpn) es una red virtual privada (**VPN**) para **Linux**, **MAC**, **Android** y **Microsoft Windows**.
* [**Psiphon3**](http://www.psiphon3.com/) es una red virtual privada gratuita **Virtual Private Network** (**VPN**) para **Microsoft Windows** y **Android OS**.
* [**Dynaweb FreeGate**](http://dit-inc.us/dynaweb.html) es una herramienta gratuita de proxy para **Microsoft Windows**.
* [**Your Freedom**](http://www.your-freedom.net/) es una herramienta de proxy comercial que también ofrece servicio gratuito, aunque lento. Se encuentra disponible para **Linux**, **Mac OS** y **Microsoft Windows**.

##1.1 Lo que debe saber sobre esta herramienta antes de comenzar:##

El **Navegador Tor** es una herramienta de software diseñada para hacer que sus actividades en Internet sean cada vez más anónimas. Oculta su identidad y protege sus actividades en línea de varias formas de vigilancia desde Internet. **Tor** también es útil como un medio seguro para evadir restricciones electrónicas por lo que podrá acceder o publicar blogs y reportes de noticias.

**Tor** protege su *anonimato* mediante el envío de las comunicaciones a través de una red distribuida de servidores, la cual es mantenida por voluntarios de todo el mundo. Mediante el uso de **Tor**, tanto la ubicación e identidad de los sitios que visite quedarán ocultos para los potenciales curiosos. El software está diseñado para asegurar de que los servidores de la red de **Tor desconozcan** tanto la **ubicación** como **los sitios que usted visita**.

**Tor** también está preparada para encriptar la comunicación hacia y a través de la red, **pero** esta medida no se puede extender todo el camino por un sitio que está enviando y recibiendo contenido sobre canales no encriptados (es decir, que no proveen acceso https).   Sin embargo, la ventaja de usar Tor cuando se accede a estos sitios, es que **Tor** puede asegurar su comunicación hasta el paso entre la última comunicación de los servidores de **Tor** y de sitios no seguros. Esto restringe la posibilidad de interceptar el contenido del paso anterior.

El **paquete Navegador Tor** consiste en el software **Tor** y una versión modificada de **Firefox**, el cual está diseñado para brindar protección extra mientras se usa. El paquete del navegador también incluye [**NoScript**](/es/firefox_noscript) y [**HTTPS-Everywhere**](/es/firefox_otros#5.5) add-ons. 

**Nota**: Existe una compensación entre el anonimato y la velocidad. Debido a que Tor facilita la navegación anónima mediante el rechazo del tráfico de navegación que usted genere a través del trabajo voluntario, tanto los ordenadores y los servidores de varias partes del mundo podrán estar más lentos que si usara otros navegadores.

**Definiciones**: 

- **Bridge Relay**: Bridge Relay es un servidor de **Tor** que no se ha anunciado públicamente. Si usted prefiriera usar un puente, el servidor puede proveerle acceso a la red de **Tor** aunque **Tor** esté bloqueado en su país.

- **Puerto:** El puerto es un punto de acceso a través del cual el programa se comunica con los servicios que estén funcionando en las redes de otros ordenadores. Si una URL como **www.google.com** le brindara la dirección de un servicio, el puerto le dirá qué puerta usar para que alcance el destino correcto. Cuando navega en la web, usted comúnmente usa el puerto 80 para sitios inseguros.(**http://mail.google.com**) y el puerto 443 para los seguros (**https://mail.google.com**).

- **Proxy:** Es un programa intermedio que funciona en su ordenador, en su red local o en cualquier otro sitio de Internet que ayuda a la transmisión de su comunicación hasta su destino final.

- **Ruta:** Una ruta es el camino de comunicación en Internet entre su ordenador y el servidor de destino.


