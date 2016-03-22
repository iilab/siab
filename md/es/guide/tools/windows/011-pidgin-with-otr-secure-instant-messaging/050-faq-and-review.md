

---

lang: es
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 5
depth: 3
title: FAQ and Review

---

<a name="5.0"></a>
## 5.0 FAQs and Review ##

<div class="background" markdown="1"> 

***P: ¿Puedo utilizar OTR para chatear con amigos en MSN y Yahoo***? 

***R**: Aunque **Pidgin-OTR** admite varios servicios de chat y mensajería, la mayor parte del tiempo tienes que utilizar el mismo proveedor para iniciar una sesión de **MI** con tu amigo. Ambos tenéis que utilizar una cuenta de **IRC** o **ICQ**, por ejemplo. Sin embargo, los servicios que utilizan el protocolo **XMPP** (como **RiseUp**, **Google Talk**, **Facebook**, u otros servidores **XMPP**) pueden permitir hacer chat entre sus respectivas cuentas. De este modo puedes hacer chat entre una cuenta en **RiseUp** y otra en **Google Talk**. Ten en cuenta también que en **Pidgin** puedes registrar y estar on-line con varias cuentas de **MI** simultáneamente. Esa es la ventaja de utilizar un cliente de **MI** multiprotocolo*

***P: ¿Cómo puedo acceder a mi cuenta Pidgin-OTR en otra computadora?***

***R**: Una opción es generar una nueva llave privada para utilizar con tu cuenta de **MI** en esa computadora. Podrás iniciar una conversación con tu amigo utilizando esta nueva llave, pero tendrás que volver a autenticar tu sesión. Otra opción es copiar las claves de cifrado a la nueva computadora (puedes localizarlas en %APPDATA%\\.purple en Windows y en ~/.purple en Linux o Mac).*

***P: ¿Qué ocurre si olvido la contraseña de mi cuenta de MI? ¿o si alguien la roba? ¿Tendrán acceso a mis conversaciones pasadas y futuras?***

***R**: Esta es una pregunta importante. En primer lugar, si olvidas tu contraseña y no puedes renovarla con las opciones que te ofrece tu proveedor, tendrás que generar una nueva cuenta de **MI**. Tras ello, debes informar a tu amigo de la nueva cuenta por medio de email o chat de voz autenticados donde os podáis reconocer.*

*Por último os debéis autenticar el uno al otro como amigos. Si de algún modo alguien ha conseguido tu contraseña de **MI**, esa persona podría intentar hacerse pasar por ti al utilizar **Pidgin**. Afortunadamente, no podrá autenticar la sesión sin tus llaves de cifrado o sin conocer tu palabra o código compartido. Tu amigo podría, de esta forma, sospechar. De ahí la importancia de la autenticación.*

*Además, si seguiste las instrucciones y estableciste las preferencias recomendadas en la pestaña Configuración de **OTR**, entonces incluso alguien que robe tu contraseña o tenga acceso a tu computadora no podrá acceder a tus conversaciones anteriores, puesto que elegiste no registrarlas.*

</div>

<a name="5.1"></a>
## 5.1 Preguntas de revisión ##

- ¿Cuántas veces es necesario autenticar tu sesión de chat con un amigo en particular?
- ¿Es posible registrar y utilizar simultáneamente múltiples cuentas de **MI** en **Pidgin**? 
- ¿Qué es una huella digital en **Pidgin**? 
- ¿Qué ocurrirá a tus preferencias **OTR** (incluidas las huellas digitales de las llaves recibidas) cuando instalas  **Pidgin- OTR** en otra computadora?
- ¿Qué se requiere para iniciar una sesión de chat privada y autenticada en  **Pidgin**?
- ¿Cuáles son los requisitos para crear una cuenta en **Pidgin**?

