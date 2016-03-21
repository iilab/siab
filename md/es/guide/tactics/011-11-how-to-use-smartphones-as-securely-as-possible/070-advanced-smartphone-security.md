

---

lang: es
community: guide
type: tactics
legacy: True
child: True
weight: 7
depth: 3
title: Advanced Smartphone Security

---

## Obtén acceso completo a tu teléfono inteligente ##

La mayoría de los teléfonos inteligentes son capaces de hacer más que lo que ofrece el sistema operativo instalado en ellos, del software manufacturado (firmware) o de los programas del operador móvil. Al contrario, algunas funcionalidades están "encerradas" por lo que el usuario no es capaz de controlar o alterar estas funciones, y están fuera de alcance. En la mayoría de casos, esas funcionalidades son innecesarias para los usuarios de teléfonos inteligentes. Sin embargo, existen algunas aplicaciones y funcionalidades que pueden aumentar la seguridad de datos y comunicaciones en el teléfono inteligente. También existen otras funciones existentes que se pueden remover para evitar riesgos a la seguridad. 

Por esto, y por otras razones, algunos usuarios de teléfonos inteligentes prefieren manipular los diversos programas y software ya instalados en los teléfonos inteligentes con el fin de obtener privilegios que les permite instalar funciones mejoradas, o remover y/o reducir otras.  

El proceso de superar los límites impuestos por el operador móvil, o manufactureros de los sistemas operativos en un teléfono inteligente se llaman “rooting” (en el caso de dispositivos de Android), o “jailbreaking” (en el caso de dispositivos iOS como iPhone o iPad). Normalmente, el éxito del “rooting” o “jailbreaking” tiene como resultado obtener todos los privilegios necesarios para instalar o utilizar aplicaciones adicionales, realizar modificaciones a configuraciones bloqueadas, y control total sobre los datos guardados y la memoria del teléfono inteligente.  

**ADVERTENCIA**: El “rooting” o “jailbreaking” no es un proceso reversible, y requiere de experiencia en la instalación y configuración de software. Considere lo siguiente:

- Existe el riesgo de que tu teléfono inteligente quede permanentemente inoperable, o “bricking it” (convertirlo en un ladrillo).
- La garantía del manufacturero u operador móvil puede quedar sin efecto o anulada.
- En algunos lugares este proceso puede ser considerado ilegal.

Pero si eres cuidadoso/a, un dispositivo “rooted” puede ser una forma sencilla de obtener mayor control sobre los teléfonos inteligentes hacerlo mucho más seguro.


### Firmware Alternativo ###

Firmware se refiere a programas que están estrechamente relacionados a un dispositivo en particular. Están en cooperación con el sistema operativo del dispositivo y son responsables de la operación básica del hardware de tu teléfono inteligente, tales como el micrófono, parlantes, cámara,  pantalla táctil, memoria, llaves, antenas, etc. 

Si tienes un dispositivo Android, puedes considerar instalarle un firmware alternativo para mejorar aún más tu control sobre el teléfono. Nota que para instalar firmware alternativo implementa el proceso de “rooting” a tu teléfono. 

Un ejemplo de un firmware alternativo para un teléfono Android es [**Cyanogenmod**](http://www.cyanogenmod.com), el cual te permite desinstalar aplicaciones al nivel del sistema de tu teléfono (aquellas aplicaciones instaladas por el manufacturero del teléfono o tu operador de red móvil). Al hacerlo, puedes reducir la cantidad de formas en las que tu dispositivo es monitoreado, como cuando la información es enviada a tu proveedor de servicios sin tu conocimiento. 

Adicionalmente, Cyanogenmod navega por defecto con una aplicación [*OpenVPN*](/es/glossary#VPN), que en caso contrario sería tedioso instalar. VPN (Red Privada Virtual, siglas en inglés) es una de las formas de asegurar el proxy de tu comunicación en internet (ver abajo). 

Cyanogenmod también ofrece un modo de navegación  Incógnito en el cual el historial de tus comunicaciones no es registrada en tu teléfono inteligente.  

Cyanogenmod viene con muchas otras características. Sin embargo, no es compatible con todos los dispositivos de Android, así que antes de continuar revisa la [lista de dispositivos compatibles](http://www.cyanogenmod.com/devices).
 
### Cifrar volúmenes completos ###

Si tu teléfono ha sido “rooted” quizá quieras cifrar todo el espacio de almacenamiento de datos, o bien crear un volumen en el teléfono inteligente para proteger alguna información en el teléfono. 

[**Luks Manager**](https://play.google.com/store/apps/details?id=com.nemesis2.luksmanager&hl=de ) le permite cifrar volúmenes con alta seguridad y de forma instantánea mediante una interfaz amigable. Es altamente recomendable que instale esta herramienta antes de empezar a guardar datos en tu dispositivo Android y utilizar los Volúmenes Cifrados que provee el Luks Manager para almacenar tus datos.


### Red Virtual Privada (VPN por sus siglas en inglés) ###

Una RPV ofrece un túnel cifrado a través de la internet entre tu dispositivo y un servidor VPN. Esto se llama un túnel porque a diferencia de otros tráficos cifrados, como https, esconde todos los servicios, protocolos y contenidos. Una conexión VPN se configura una sola vez, y termina solo cuando tu lo decidas. 

Ten en cuenta que como todo tu tráfico viaja a través de un servidor proxy o VPN, un intermediario sólo necesitará acceso al proxy para analizar tus actividades.  Por lo tanto, es sumamente importante que escojas cuidadosamente entre los servicios de proxy y de VPN. También es recomendable utilizar diferentes proxys y/o RPV, ya que al distribuir en diferentes canales tus datos se reduce el impacto de un servicio en peligro.

Recomendamos el uso del servidor [**RiseUp VPN**](https://help.riseup.net/en/vpn). Puedes utilizar RiseUp VPN en un dispositivo Android después de instalar Cyanogenmod (ver arriba). Además es muy fácil de configurar la conexión del RiseUp VPN a un iPhone – para más información leer [aquí](https://support.apple.com/kb/HT1424).

