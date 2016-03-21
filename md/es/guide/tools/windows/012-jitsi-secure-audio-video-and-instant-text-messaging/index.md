

---

lang: es
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 012
title: Jitsi - Secure Audio, Video and Instant Text Messaging 

---

**Página de inicio**

- [**https://jitsi.org/**](https://jitsi.org/)

**Requisitos del sistema**

- Todas las versiones de Windows

**Versión utilizada en esta guía**

- 2.8

**Última revisión de este capítulo**

- Mayo de 2015

**Licencia**

- Software gratuito y de código abierto

**Lo que usted obtiene**: 

- La capacidad de tener un sistema de comunicación integrado, privado y seguro que incluye sesiones de conversaciones de vídeo.
- La capacidad de cifrar su comunicación independientemente del proveedor de su cuenta.
- La capacidad de registrar y usar diferentes cuentas (por ejemplo, **Facebook**, **Google Talk**, **Yahoo! Messenger**) simultáneamente.

**GNU Linux, Mac OS, Microsoft Windows y otros programas compatibles.**:

**Jitsi** está disponible para **GNU Linux** y **Mac OS**, así como para **MS Windows** (y próximamente para **Android OS**). A continuación se recomiendan otros programas con los que **Jitsi** se puede comunicar usando el cifrado independiente **OTR** o **ZRTP**:

- Para **mensajes de texto**: [**Pidgin**](/es/pidgin_principal) (**MS Windows** y **GNU Linux**), [**Miranda**](http://www.miranda-im.org/) (**MS Windows**), [**Adium**](https://adium.im/) (**Mac OS X**), [**ChatSecure**](https://guardianproject.info/apps/chatsecure/) (**Android OS** y **iOS**, conocido anteriormente como [**Gibberbot**](/es/gibberbot_principal)). 

- Para **llamadas de voz**: **CSipSimple** (**Android OS**), [**Linphone**](http://www.linphone.org/) (**GNU Linux**, **MS Windows**, **Mac OS X**, **Android OS**, **iOS** y otros).

**1.1 Cosas que debería saber acerca de esta herramienta antes de comenzar**

**Jitsi** es compatible con diferentes tipos de cuentas y protocolos de comunicación y, por lo tanto, puede comunicarse con contactos que utilicen otros programas. Algunos de esos programas ofrecen funciones similares para mejorar la seguridad de su comunicación (como los programas mencionados en la sección anterior), y soportan el cifrado independiente de texto y voz (**OTR** y **ZRTP**). Otros programas podrían no tener implementadas estas funciones, especialmente los propios (por ejemplo, el chat de **Facebook** o **Google Talk**). Sin embargo, con **Jitsi** podrá comunicarse de todas formas con contactos que utilicen dichos programas propios, sólo que sin los beneficios adicionales de las funciones de seguridad de **Jitsi**.

Sin importar si se comunica mediante texto, voz o vídeo, los proveedores de servicios como **Facebook Chat**, **Google Talk**, **Yahoo! Messenger**, **Skype** o **Viber** tienen acceso a sus sesiones de comunicación y pueden ofrecer el acceso a terceros, tales como corporaciones o gobiernos. **Jitsi** le permite comunicarse de manera segura y privada usando sus cuentas existentes con la ayuda de un cifrado adicional. Esto hace que el contenido de sus comunicaciones sea inaccesible para los proveedores de cuentas y posibles terceros. Para poder proteger sus sesiones de chat y conversaciones privadas, **Jitsi** utiliza métodos criptográficos, inclusive **Off-the-Record** ([**OTR**](/es/glossary#OTR)) para conversaciones de texto, y **ZRTP/SRTP** para llamadas de voz.

Otra diferencia a notar entre **Jitsi** y programas como **Skype** es que Jitsi permite que los usuarios sigan usando sus cuentas existentes con un proveedor de servicio distinto, independiente de los desarrolladores del programa. Esto también significa que necesita configurar una cuenta antes de poder utilizar **Jitsi**.

**Nota**: **Jitsi** utiliza el lenguaje de programación **Java**, de forma que el programa Java debe estar instalado en el equipo para que funcione. Se sabe que **Oracle Java** tiene varias vulnerabilidades de seguridad que pueden permitir que usuarios remotos tomen control del equipo e instalen spyware para acceder o controlar todos sus datos y comunicaciones. Se recomienda **ampliamente** que minimice el número de programas que tienen permitido utilizar Java en su equipo. Mire cómo [**desactivar complementos asociados con Java en Firefox**](/es/firefox_complementos#3.2) y consulte los [**pasos para deshabilitar Java en todos los navegadores del equipo**](https://www.java.com/en/download/help/disable_browser.xml). Sin embargo, como verá más adelante en este capítulo, a pesar del uso de **Java**, hay una serie de beneficios de seguridad al utilizar **Jitsi**.

