

---

lang: es
community: guide
type: tactics
legacy: True
child: True
weight: 2
depth: 3
title: Communicating (Voice and Messages) via Smartphone

---

## Conversaciones Seguras ##

### Telefonía Básica ###

En la sección [***Funciones básicas, capacidad de rastreo y anonimato***](/es/chapter_10_2_2) del [***Capítulo 10***](/es/chapter-10), hablamos de las diferentes medidas que deberías considerar para aminorar los riesgos de interceptación al utilizar los operadores de redes móviles para la comunicación de voz. 

Utilizar la internet a través de tu teléfono inteligente sobre conexiones móviles de datos o WiFi puede ofrecer muchas opciones para comunicarte de forma segura con las personas, utilizando por ejemplo   [*VoIP*](/es/glossary#VoIP) e implementando medios para asegurar este canal de comunicación.  Incluso, algunos teléfonos inteligentes pueden extender la seguridad a llamadas de teléfono móvil, más allá de VoIP (Ver **Redphone** abajo).

Aquí enumeramos algunas herramientas, con sus pros y contras:

### Skype ###

La aplicación comercial VoIP más popular [*Skype*](/es/glossary#Skype)  está disponible para todas las plataformas de teléfonos inteligentes y funciona si tu conexión inalámbrica es fiable. Es menos seguro en conexiones de datos móviles.

En la [***Sección 3***](/es/chapter_7_3) del [***Capítulo 7: Mantener privada tu comunicación en Internet***](/es/chapter_7_3), hablamos de los riesgos al utilizar Skype, y por qué, si es posible, debemos evitar usuarlo. En resumen, Skype no es un software de Código Abierto, lo que dificulta verificar de forma independiente sus niveles de seguridad. Adicionalmente, Skype es propiedad de Microsoft, la cual tiene el interés comercial de saber cuándo utilizas Skype y desde dónde. Así mismo, Skype podría permitirle a las agencias de la fuerza del orden acceso retrospectivo de todo tu historial de comunicaciones.  

### Otros VoIP ###

Utilizar VoIP generalmente es gratuito (o significativamente más barato que las llamadas móviles) y deja menos rastros de tus datos. Es más, una llamada segura con VoIP puede ser la forma más segura de comunicarse. 

[**CSipSimple**](http://f-droid.org/repository/browse/?fdid=com.csipsimple&fdpage=4) es un poderoso cliente VoIP para teléfonos Android, que cuenta con excelente mantenimiento y contiene sencillas configuraciones de asistente para diferentes servicios VoIP.

[**Open Secure Telephony Network (OSTN)**](https://guardianproject.info/wiki/OSTN) y el servidor de [**Guardian Project**](https://guardianproject.info), [**ostel.co**](https://ostel.co), actualmente ofrece uno de los medios más seguros para la comunicación de voz.  Conocer y confiar en el proveedor que opera el servidor de tu comunicación VoIP es de vital importancia. Los que hospedan este servicio – Guardian Project – son bien conocidos y respetados en la comunidad.

Al utilizar CSipSimple nunca te comunicas directamente con la otra persona, sino que todos tus datos se canalizan a través del servidor Ostel. Esto hace que sea mucho más difícil rastrear tus datos y averiguar con quién estás hablando. Adicionalmente, Ostel no guarda ninguna información, excepto los datos de la cuenta que necesitas para iniciar la sesión. Todas tus conversaciones están [*cifradas*](/es/glossary#Cifrado); y tus meta datos (los cuales son usualmente muy difíciles de ocultar) son borrosas porque el tráfico pasa por el servidor ostel.co. Si descargas CSipSimple desde ostel.co, ya vendrá configurado para utilizarlo con ostel, lo que lo hace aún más fácil de instalar y usar. 

[**RedPhone**](https://play.google.com/store/apps/details?id=org.thoughtcrime.redphone) es una aplicación gratuita y Código Abierto que cifra datos de comunicación de voz enviados entre dos dispositivos que corren con esta misma aplicación. Es fácil de instalar y fácil de utilizar, ya que se integra a tu marcado normal y sistema de contactos. Sin embargo las personas con las que deseas comunicarte también necesitan instalar y utilizar RedPhone. Para facilitar el uso RedPhone utiliza tu número de teléfono móvil como tu identificador (como un nombre de usuario en otros servicios VoIP). Sin embargo, se vuelve más sencillo para analizar el tráfico que produce y rastrearto de vuelta a través de tu número de teléfono móvil. RedPhone utiliza un servidor central como punto de centralización lo que pone a RedPhone en una poderosa posición (por tener control sobre algunos esto datos).

Estamos desarrollando las Guías Prácticas para CSipSimple, Ostel y Redphone. Por el momento, puedes encontrar más información en los enlaces disponibles arriba.

## Enviando Mensajes de forma Segura ##

Debes tomar precauciones a la hora de enviar SMS o al utilizar mensajería instantánea o chat en tu teléfono inteligente. 

### SMS ###

Como se describe en la sección [***Comunicaciones textuales – SMS / Mensajes de Texto***](/es/chapter_10_2_3) del [***Capítulo 10***](/es/chapter-10), la comunicación SMS es insegura por defecto. Cualquier persona con acceso a una red de telecomunicación móvil puede interceptar fácilmente los mensajes, y esto es una acción cotidiana que se da en muchas situaciones. No se confíe enviando mensajes SMS inseguros en situaciones críticas. No existen ninguna forma de autenticar un mensaje SMS, por lo tanto es imposible saber si el contenido de dicho mensaje fue alterado durante su envío o si el emisor del mensaje realmente es la persona que dice ser. 

### Asegurando los SMS ###

[**TextSecure**](https://play.google.com/store/apps/details?id=org.thoughtcrime.securesms) es una herramienta de Código Abierto [*FOSS*](/es/glossary#FOSS) para enviar y recibir SMS de forma segura en los teléfonos Android. Funciona tanto para mensajes cifrados y no cifrados, así que puedes utilizarla por defecto como una aplicación SMS. Para intercambiar mensajes cifrados esta herramienta debe estar instalado tanto por parte del emisor como del receptor del mensaje, por lo tanto deberás promover su uso constante entre las personas con las que te comunicas. TextSecure detecta automáticamente los mensajes cifrados recibidos desde otro usuario de TextSecure. También te permite cifrar mensajes a más de una persona. Los mensajes son firmados automáticamente haciendo casi imposible que los contenidos del mensaje sean alterados. En nuestra guía sobre TextSecure explicamos en detalle las características de esta herramienta y cómo utilizarla. 

<div class=getstarted markdown=1>
Guía Práctica:  Empezar con la [*Guía de TextSecure*](/es/textsecure_main)
</div>

### Chat Seguro ###

La mensajería instantánea o chat en tu teléfono puede producir mucha información vulnerable a la interceptación. Estas conversaciones podrían ser usadas en tu contra por adversarios posteriormente. Deberías, por lo tanto, ser extremadamente cauteloso/a sobre lo que escribes en tu teléfono mientras envías mensajes instantáneos y al chatear.

Existen formas seguras para chatear y enviar mensajes instantáneos. La mejor forma es utilizar cifrado de extremo a extremo (doble vía), asegurando que la persona al otro extremo sea la persona con la que deseas comunicarte. 

Recomendamos [**Gibberbot**](https://securityinabox.org/es/gibberbot_principal)* por ser una aplicación segura para chatear en teléfonos Android. Gibberbot ofrece cifrado sencillo y fuerte para tus chats con  el protocolo de mensajería [*Off-the-Record*](/es/glossary#OTR). Este cifrado provee ambas autenticaciones, por un lado puedes verificar que chateas con la persona correcta, y por otro lado contiene seguridad independiente entre cada sesión, de esta forma si una sesión de chat cifrado se ve comprometida, otras sesiones pasadas o futuras se mantendrán seguras.

Gibberbot ha sido diseñado para funcionar en conjunto con Orbot, de esta forma tus mensajes de chat son canalizados a través de la red anónima [*Tor*](/es/glossary#Tor). Esto hace que sea muy difícil de rastrear o incluso averiguar si sucedió alguna vez. 

<div class=getstarted markdown=1>
Guía Práctica: Empezar con la [*Guía de Gibberbot*](/es/gibberbot_principal)
</div>

Para clientes de iPhones, el [**ChatSecure**](https://chatsecure.org) provee las mismas características, sin embargo no es tan sencillo utilizarlo con la red de [*Tor*](/es/glossary#Tor).

Estamos desarrollando las Guías Prácticas para ChatSecure. Por el momento, puedes encontrar más información en su [homepage](https://chatsecure.org). 

Independientemente de la aplicación que utilices, siempre considera desde qué cuenta usarás el chat. Por ejemplo, cuando utilizas Google Talk, tus credenciales y tiempo de la sesión del chat serán conocidas por Google. Ponte de acuerdo con tus contactos para no dejar guardados los historiales de chat, especialmente si no están cifrados. 

* [22/01/2014] *Gibberbot ahora se llama ChatSecure. Una guía práctica actualizada viene enseguida.*

