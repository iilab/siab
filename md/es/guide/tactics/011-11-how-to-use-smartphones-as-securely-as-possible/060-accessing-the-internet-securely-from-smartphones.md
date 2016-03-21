

---

lang: es
community: guide
type: tactics
legacy: True
child: True
weight: 6
depth: 3
title: Accessing the Internet Securely from Smartphones

---

Según se abordó en el [***Capítulo 7: Mantener privada tu comunicación en Internet***](/es/chapter-7) y en el [***Capítulo 8: Mantenerse en el anonimato y evadir la censura en Internet***](/es/chapter-8), acceder a contenidos en Internet, o publicar fotos y videos, dejan huellas y rastros de quién eres y dónde estás y qué estás haciendo.  Esto puede ponerte en riesgo. Utilizar tu teléfono inteligente para comunicarte con la internet aumenta considerablemente estos riesgos. 

### Acceso mediante WiFi o Data Móvil ###

Los teléfonos móviles te permiten controlar cómo accedes a Internet: vía conexión inalámbrica desde un punto de acceso (como un internet café o cyber), o vía conexión de data móvil, tales como [*GPRS*, *EDGE*](/es/glossary#EDGE), o [*UMTS*](/es/glossary#EDGE) que ofrece tu proveedor de red móvil. 

Utilizar una conexión WiFi reduce los rastros o huellas de los datos que estás dejando en tu proveedor de servicios de telefonía móvil (ya que no estás conectado/a con tu suscripción de teléfono móvil). A pesar de ello, algunas veces la conexión de data móvil es la única forma de estar en línea. Desafortunadamente, los protocolos de la conexión de data móvil (como EDGE o UMTS) no tienen protocolos abiertos. Desarrolladores independientes e ingenieros de seguridad no pueden examinar estos protocolos para ver cómo están siendo implementados por operadores de data móvil.

En algunos países los proveedores de servicios móviles operan bajo diferentes legislaciones que los proveedores de servicios de internet, lo que puede resultar en una mayor vigilancia por parte de gobiernos y responsables del soporte. 

Independientemente del camino que tomes para tus comunicaciones digitales con teléfonos inteligentes, puedes reducir los riesgos de exponer datos mediante el uso de herramientas para el cifrado y anonimato. 

### Anonimizar ###

Para acceder a contenido en línea de forma anónima, puedes usar la aplicación para Android llamada  [**Orbot**](https://securityinabox.org/es/orbot_principal). Orbot canaliza tu comunicación en internet mediante la red anónima de Tor. 

<div class=getstarted markdown=1>
Guía Práctica: Empezar con la [*Guía de Orbot*](/es/orbot_principal)
</div>

Otra aplicación llamada Orweb, tiene la característica de ser un navegador web con potentes características de privacidad utilizando proxies que no guardan el historial de la navegación local. Juntos Orbot y Orweb eluden los filtros y cortafuegos en la web, y ofrecen navegación anónima. 

<div class=getstarted markdown=1>
Guía Práctica: Empezar con la [*Guía de Orweb*](/es/orweb_principal)
</div>

### Proxies ###

La versión móvil del navegador [*Firefox*](/es/glossary#Firefox) – [**Firefox mobile**](http://f-droid.org/repository/browse/?fdid=org.mozilla.firefox) puede equiparse con complementos proxy que dirijan tu tráfico a un servidor proxy. Por lo tanto, tu tráfico irá al sitio que estás solicitando. Esto es poderoso en casos de censura, pero puede que revele tus solicitudes si tu conexión desde tu cliente al proxy no está cifrada.  Recomendamos el complemento llamado [**Proxy Mobile**](https://guardianproject.info/apps/proxymob-firefox-add-on/) (también de el [**Guardian Project**](https://guardianproject.info/), el cual hace que el proxy con Firefox sea sencillo. Así mismo, es la única forma de canalizar la comunicación móvil de Firefox a Orbot y utilizar la red  [*Tor*](/es/glossary#Tor).

