

---

lang: es
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: Using the Tor Browser

---

- [**4.0 Usar el navegador Tor**](#4.0)
- [**4.1 Control adicional de funcionamiento del navegador Tor**](#4.1)
- [**4.2 Cómo crear una nueva identidad**](#4.2)
- [**4.3 Habilitar el add-on NoScript**](#4.3)
- [**4.4 Actualizaciones del navegador Tor**](#4.3)


<a name="4.0"></a>
## 4.0 Usar el navegador Tor ##

El navegador **Tor** ha sido diseñado para ser usado fácilmente, de hecho si usted está familiarizado con el uso de algún navegador web, estará apto para usar el navegador **Tor** ya que es una versión modificada de **Firefox** para privacidad y seguridad adicionales.  

**Nota:** debido a que el navegador **Tor** ha sido diseñado con el objetivo de privacidad, no ha sido configurado para proteger cualquier información de su disco rígido o dispositivo USB.  Esto significa que cuando se desconecte del navegador **Tor**, todo su historial de navegación será eliminado.

<a name="4.1"></a>
## 4.1 Control adicional de funcionamiento del navegador Tor ##

Al igual que con cualquier software para ocultar información,  se recomienda realizar pruebas independientes simples para asegurar el funcionamiento del navegador **Tor**, visitando cualquier sitio web que tratara de identificar dónde está usted, basado en la dirección IP desde donde se visita el sitio.

Existen varios sitios web gratuitos para realizar esto, tales como: [check.torproject.org](https://check.torproject.org), [iplocation.net](http://www.iplocation.net/), [ip2location.com](http://www.ip2location.com/), [whatismyipaddress.com](http://whatismyipaddress.com/), etc.Si accede a estos sitios web directamente sin usar el navegador  **Tor** u otra herramienta de seguridad, debe mostrar su verdadera dirección IP y proporcionar un lugar físico más o menos exacto para usted. Sin embargo, si usted accede a estos sitios web usando el navegador **Tor** u otra herramienta de seguridad, la ubicación y dirección IP que verá serán diferentes.

![](/sbox/screen/tor-es-1/031.png)

*Figura 1: Firefox (arriba) y el navegador Tor (abajo) en el mismo equipo que muestra el estado de Tor y las diferencias de dirección IP*

<a name="4.2"></a>
## 4.2 Cómo crear una nueva identidad ##

Usted podrá crear una *nueva identidad* para su navegador.  Esto significa que se seleccionará un nuevo conjunto de administradores de servidores **Tor** al azar para que usted los utilice. Esto le hará verse como si proviniera de una nueva ubicación. Para ello haga clic en ![](/sbox/screen/tor-es-1/022.png) y seleccione *Nueva Identidad* desde el menú.  El navegador *Tor* se cerrará rápidamente, limpiará su *historial de navegación* y *cookies* y luego se reiniciará. Una vez que el navegador se reinicie, usted podrá comprobar su nueva ubicación tal como se describe en la sección 4.1.

![](/sbox/screen/tor-es-1/032.png)

*Figura 2: Seleccionar una Nueva Identidad desde el menú Tor*

<a name="4.3"></a>
## 4.3 Habilitar el add-on NoScript ##

El navegador **Tor** viene con el add-on NoScript preinstalada. El add-on NoScript puede además protegerlo de sitios web maliciosos y del escape de su identidad real a través de la ejecución de pequeños programas o scripts en su navegador **Tor**,  sin embargo NoScript está desactivado por defecto en el navegador **Tor** por lo que esta protección adicional no está disponible por defecto. 

Si desea habilitar las protecciones adicionales que ofrece NoScript, éste se puede activar mediante la apertura del menú y haciendo clic en *Bloquear JavaScript grobalmente* y luego configurar las diversas *opciones* que proporciona. 

Recomendamos que lea más sobre [**NoScript** en el capítulo **FireFox**](/es/firefox_noscript). 

![](/sbox/screen/tor-es-1/033.png)

*Figura 3: Activando NoScript mediante la selección la opción de Bloquear JavaScript grobalmente* (recomendado)

<a name="4.4"></a>
## 4.4 Actualizaciones del navegador Tor ##

En la **[Guía paso a paso capítulo 1.4](/es/chapter_1_4)** se explica la importancia de mantener su programa actualizado y el navegador **Tor** no es la excepción.  Cuando las actualizaciones estén disponibles la próxima vez que inicie el navegador **Tor**, se le presentará una nota informándole de que su navegador está desactualizado (*Figura 4*) y le será indicado hacer clic y seleccionar **Descargar actualización para el navegador Tor**. Será direccionado hacia el sitio web **Proyecto Tor** donde podrá obtener la última versión.  Una vez que haya sido descargada, podrá seguir esta guía para instalar la nueva versión del navegador **Tor**.


![](/sbox/screen/tor-es-1/034.png)

*Figura 4: El navegador Tor muestra la actualización disponible*


