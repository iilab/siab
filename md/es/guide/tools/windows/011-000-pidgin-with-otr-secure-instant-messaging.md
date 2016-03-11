

---

lang: es
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 011
title: Pidgin with OTR - Secure Instant Messaging

---

**Sitios web**

- **Pidgin**: [**www.pidgin.im**](http://www.pidgin.im)
- **OTR**: [**https://otr.cypherpunks.ca/**](https://otr.cypherpunks.ca/)

**Requisitos del sistema**

- Conexión a internet
- Todas las versiones de Windows 

**Versión utilizada en esta guía**

- Pidgin 2.10.11
- OTR 4.0.1 

**Última actualización de este capítulo**

- Agosto 2015

**Licencia**: 

- Software gratuito y de código abierto

**Lectura necesaria**

Guía Paso a Paso, capítulo [**7. Mantener privada tu comunicación en Internet**](/es/chapter-7)

**¿Qué recibes a cambio?**: 

- La capacidad de organizar y administrar algunos de los servicios de mensajería instantánea más populares por medio de un único programa 
- La capacidad de mantener sesiones de chat privadas y autenticadas

**GNU Linux, Mac OS y otros programas compatibles con Microsoft Windows:**

**Nota:** Recomendamos utilizar [**Jitsi**](/es/jitsi) para sustituir a **Pidgin**. Además de poder utilizar **Jitsi** para sesiones seguras de chat (también con usuarios de Pidgin), también puedes utilizarlo para comunicaciones seguras vocales o por vídeo con otro usuarios de **Jitsi**. **Jitsi** está disponible para **Microsoft Windows**, **GNU/Linux**, **Mac OS** y más.

Tanto **Pidgin** como **OTR** están disponibles para **Microsoft Windows** y para **GNU/Linux**. Otro programa multiprotocolo de **MI** para **Microsoft Windows** que admite **OTR** es [**Miranda IM**](http://www.miranda-im.org/). Para **Mac OS** se puede utilizar [**Adium**](http://adium.im/), un programa multiprotocolo de **MI** que es compatible con el plugin **OTR**.

## 1.1 Cosas que debes saber sobre esta herramienta antes de empezar ##

Antes de poder empezar a utilizar **Pidgin** debes tener una cuenta de **MI**, que registrarás con **Pidgin**. Por ejemplo, si dispones de una **cuenta Google** puedes utilizar **GoogleTalk**, su servicio de  **MI**, con **Pidgin**. Los datos de acceso a tu cuenta de  **MI** se utilizan para registrarte y acceder a tu cuenta por medio de **Pidgin**. 

**Nota**: animamos a todos los usuarios a que se informen todo lo posible sobre la política de privacidad y seguridad de su **proveedor de cuenta de Mensajería Instantánea**. 

**Pidgin** es compatible con los siguientes servicios de **MI**: [**AIM**](https://www.aim.com/), [**Bonjour**](http://www.apple.com/es/support/bonjour/), [**Gadu-Gadu**](http://komunikator.gadu-gadu.pl/), [**Google Hangouts**](http://www.google.com/intl/es/hangouts/), **Groupwise**, [**ICQ**](http://www.icq.com), **IRC**, [**MSN**](http://www.msn.com/), [**MXit**](http://www.mxit.com/), [**MySpaceIM**](http://www.myspace.com/guide/im), [**SILC**](http://silcnet.org/), **SIMPLE**, [**Sametime**](http://www.ibm.com/developerworks/downloads/ls/lst/), [**Yahoo!**](http://es.messenger.yahoo.com), **Zephyr** y cualquier cliente de **MI** que funcione con el protocolo de mensajería **XMPP**.

**Pidgin** no permite la comunicación entre diferentes servicios de **MI**. Por ejemplo, si utilizas **Pidgin** para acceder a tu cuenta de **Google Talk**, no podrás chatear con un amigo que utilice una cuenta **ICQ**. 

Sin embargo, **Pidgin** puede configurarse para administrar múltiples cuentas que se basen en cualquiera de los protocolos de mensajería admitidos. Es decir, que puedes utilizar simultáneamente cuentas **Gmail** y **ICQ** y chatear con usuarios de *uno u otro* de esos servicios específicos (que son compatibles con **Pidgin**). 

El plugin **Off-the-Record (Fuera de Registro)** (**OTR**) está desarrollado específicamente para **Pidgin** y ofrece las siguientes funciones de seguridad y privacidad: 

- **Autenticación**: Garantiza que la persona con la que te comunicas es quien tú crees que es.
- **Rechazo**: Una vez finalizada la sesión de chat, los mensajes no pueden ser identificados como procedentes de ti o de tu interlocutor.
- **Cifrado**: Nadie puede tener acceso a tus mensajes y leerlos.
- **Perfecta seguridad adicional**: En caso de que terceros obtengan tus claves privadas, ninguna de tus conversaciones anteriores estará en peligro.

**Nota**: **Pidgin** debe necesariamente instalarse antes del plugin **OTR**.

