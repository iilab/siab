

---

lang: es
community: guide
type: tactics
legacy: True
child: True
weight: 1
depth: 3
title: Platforms, Setup and Installation

---

### Plataformas y Sistemas Operativos ###

Al momento de escribir este capítulo, los teléfonos inteligentes de uso más común son el iPhone de Apple y Android de Google, seguidos por el Blackberry y teléfonos de Windows. La mayor diferencia entre el Android y los otros sistemas operativos, es que Android es un sistema, principalmente de Código Abierto ([*FOSS*](/es/Glossary#FOSS)), permitiendo que su sistema operativo sea auditado de forma independiente para verificar si protege apropiadamente la información y comunicación de los usuarios. También facilita el desarrollo de aplicaciones de seguridad para su plataforma. Muchos programadores conscientes de la seguridad desarrollan aplicaciones para Android pensando siempre en la seguridad del usuario. Algunas de estas aplicaciones las destacaremos más adelante en este capítulo.  

Sin importar el tipo de teléfono inteligente que utilizas, es importante que seas consciente de algunos temas al usar un teléfono que se conecta a internet y que contiene características tales como [*GPS*](/es/glossary#GPS) o capacidad de red inalámbrica. En este capítulo nos enfocamos en dispositivos con la plataforma Android, ya que, como explicamos anteriormente, es más fácil asegurar datos y comunicaciones.  Sin embargo, las guías de configuración básicas y algunas aplicaciones para dispositivos que no sean teléfonos Android también se proporcionan.

Los teléfonos Blackberry han sido presentados como dispositivos “seguros” para mensajería y correo electrónico. Esto se debe a que los mensajes y correos electrónicos son tranferidos de forma segura por medio de los servidores de Blackberry, fuera del alcance de potenciales intrusos. Desafortunadamente, más y más gobiernos están demandando acceso a estas comunicaciones, citando la necesidad de protegerse contra el terrorismo y crimen organizado. La India, Emiratos Árabes Unidos, Arabia Saudita, Indonesia y el Líbano son ejemplos de gobiernos que han analizado el uso de dispositivos Blackberry y han exigido el acceso a los datos del usuario en sus países.

### Teléfonos móviles convencionales ###

Otra categoría de teléfonos móviles son llamados comúnmente 'móviles convencionales' (eje.  Nokia 7705 Twist o Samsung Rogue). Recientemente, los móviles convencionales han incrementado sus funcionalidades para incluir algunas contenidas en los teléfonos inteligentes. Pero generalmentes, los sistemas operativos de los móviles convencionales son menos accesibles, y por lo tanto existen limitadas oportunidades para aplicaciones de seguridad o mejoras a las mismas. No abordamos específicamente los móviles convencionales, sin embargo muchas de las medidas expresadas en este capítulo también tienen sentido para los móviles convencionales.  

### Teléfonos inteligentes de marca y bloqueados ###

Los teléfonos inteligentes usualmente son vendidos con una marca o bloqueados. Un teléfono inteligente bloqueado significa que el dispositivo sólo puede ser operado con un único proveedor, y el dispositivo sólo funciona con su tarjeta SIM. Los proveedores de redes móviles usualmente le ponen marca a los teléfonos mediante la instalación de su propio “firmware” o software. También puede que los proveedores deshabiliten algunas funcionalidades o agregar otras. La marca es un medio para que las empresas aumenten sus ingresos mediante la canalización del uso de tu teléfono inteligente, a menudo también recopilando datos acerca de cómo utilizas el teléfono o habilitando el acceso remoto a tu teléfono inteligente.

Por estas razones, recomendamos comprar teléfonos inteligentes desbloqueados, siempre que puedas. Un teléfono bloqueado incrementa los riesgos debido a que tus datos son canalizados a través de un sólo proveedor, centralizando así el flujo de tu información haciendo imposible cambiar las tarjetas SIM para difundir los datos a través de diferentes proveedores.  Si tu teléfono está bloqueado, pregúntale a alguien de confianza cómo desbloquearlo.

### Configuración General ###

Los teléfonos inteligentes tienen muchas opciones de configuración que controlan la seguridad del dispositivo. Es importante prestar atención sobre cómo se encuentra configurado tu teléfono inteligente. En las guías prácticas que se presentan más adelante, te alertaremos sobre algunas opciones de seguridad del teléfono inteligente que están disponibles pero no están activadas por defecto, así como aquellas opciones que se encuentran activadas por defecto y que vulneran tu teléfono. 

<div class=getstarted markdown=1>
Guía Práctica: Empezar con la [*Guía de Configuración Básica de Android*](/es/android_basica)
</div>

### Instalar y actualizar aplicaciones ###

La forma más común de instalar nuevo software en tu teléfono inteligente es usando el Appstore de iPhone o Google Play store, allí ingresas tu información de usuario, y descargas e instalas la aplicación que deseas. Al iniciar la sesión, estás asociando tu información de cuenta de usuario a la tienda virtual. Los dueños de la tienda virtual mantienen registros del historial de navegación del usuario y sus preferencias de aplicaciones.

Las aplicaciones que ofrecen las tiendas virtuales oficiales son, supuestamente, verificadas por los dueños de las tiendas (Google o Apple), pero en la realidad esto provee poca protección contra lo que puede hacer la aplicación una vez instalada en tu teléfono. Por ejemplo, algunas aplicaciones pueden copiar y enviar tu directorio de contactos luego de ser instaladas en tu teléfono. En el caso de los teléfonos Android, durante el proceso de instalación cada aplicación te solicita permiso sobre lo que puede o no hacer una vez instalada. Deberías prestar mucha atención a los tipos de permisos solicitados, y si estos permisos tienen sentido respecto a la funcionalidad de la aplicación que estás instalando. Por ejemplo, si estás considerando instalar una aplicación para “lectura de noticias” y te das cuenta que te solicita derechos para enviar tus contactos a través de una conexión móvil de datos a terceros, deberías buscar otras aplicaciones más acordes con accesos y derechos.

Las aplicaciones de Android también están disponibles fuera de los canales oficiales de Google. Sólo debes marcar la caja de *Fuentes desconocidos* que se encuentra en *Aplicaciones* para poder utilizar estos sitios web de descargas. 

Son muy útiles estos sitios web alternativos si quieres minimizar tu contacto en línea con Google. Recomendamos [**F-Droid**](http://f-droid.org) ('Free Droid'), que sólo ofrece aplicaciones de  [*FOSS*](/es/glossary#FOSS). En esta guía, F-Droid es el repositorio primordial de las aplicaciones que recomendamos, y sólo te referimos a Google Play si una aplicación no está disponible en F-Droid.

Si no deseas (o no puedes) conectarte a internet para acceder a las aplicaciones, puedes transferir aplicaciones al teléfono de otra persona enviando archivos [*.apk*](/es/glossary#apk) (siglas del inglés para 'paquetes de aplicaciones para android') vía bluetooth. Como alternativa también puedes descargar el archivo .apk a la tarjeta Micro SD de tu dispositivo móvil o utilizar un cable usb para trasladarlo desde una computadora. Cuando hayas recibido el archivo, simplemente haz un pulso largo al archivo y estará listo para instalarse.  (**Nota**: se especialmente cuidadoso/a mientras usas bluetooth – leer más en la sección [***Funciones más allá de la conversación y los mensajes***](/es/chapter_10_2) del [***Capítulo 10***](/es/chapter-10).

