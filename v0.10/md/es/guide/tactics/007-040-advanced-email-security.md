

---

lang: es
community: guide
type: tactics
legacy: True
child: True
weight: 4
depth: 3
title: Advanced Email Security

---

Las herramientas y conceptos tratados a continuación se recomiendan para usuarios de computadoras experimentados.

### Utilizar cifrado de clave (llave) pública en correo electrónico ###

Es posible alcanzar un gran nivel de privacidad con el correo electrónico, incluso con una cuenta de correo electrónico insegura. Para hacer esto, necesitas aprender sobre [**cifrado**](/es/glossary#Cifrado) de clave pública. Esta técnica te permite cifrar mensajes individuales, haciéndolos ilegibles a cualquiera que no sea uno de los destinatarios previstos. El aspecto ingenioso del cifrado de clave pública es que no tiene que intercambiar ninguna información secreta con tus contactos sobre cómo vas a cifrar tus mensajes en el futuro.

<div class="background" markdown="1">
**Pablo**: Pero, ¿cómo funciona todo esto? 

**Claudia**: ¡Puras matemáticas! Cifras tus mensajes hacia un contacto de correo electrónico dado, utilizando su 'clave pública' especial la cual puede distribuir libremente. Luego, ella utiliza su 'clave privada,' la cual debe guardar cuidadosamente, con el fin de leer dichos mensajes. A su turno, tu contacto utiliza tu clave pública para cifrar mensajes que te escribe. De modo que al final, debes intercambiar claves públicas, pero puedes compartirlas abiertamente, sin tener que preocuparte sobre el hecho de que cualquiera que desee tu clave pública pueda obtenerla.

</div>
			
Esta técnica puede utilizarse con cualquier servicio de correo electrónico, incluso con uno que no cuente con un canal de comunicación seguro, debido a que los mensajes individuales son [**cifrados**](/es/glossary#Cifrado) antes de que dejen tu computadora. 

Recuerda que al utilizar el [**cifrado**](/es/glossary#Cifrado) puedes atraer la atención hacia ti. El tipo de [**cifrado**](/es/glossary#Cifrado) utilizado cuando accedes a un sito web seguro, incluyendo una cuenta de correo con interfaz web, se ve a menudo con menor sospecha que la del tipo de [**cifrado**](/es/glossary#Cifrado) de clave pública del que nos ocupamos aquí. En algunas circunstancias, si un correo electrónico que contenga esta suerte de datos [**cifrados**](/es/glossary#Cifrado) es interceptado o publicado en un foro público, podría incriminar a la persona que lo envió, sin considerar el contenido del mensaje. Tú a veces tendrías que escoger entre la privacidad de tu mensaje y la necesidad de mantenerte sin llamar la atención. 

### Cifrar y autenticar mensajes individuales ###

El [**cifrado**](/es/glossary#Cifrado) de clave pública puede parecer complicado al inicio, pero es muy directo una vez que has entendido los fundamentos, y las herramientas no son difíciles de utilizar. Simple, de fácil uso para el usuario y portátil; así es el programa **gpg4usb** el cual puede cifrar textos y archivos para mensajes de correo electrónico incluso cuando no estás conectado a la Internet.

<div class="getstarted" markdown="1">
Parte Práctica: Empieza con [*gpg4usb Portátil - guía del programa de cifrado de texto y archivos para mensajes de correo electrónico*](/es/gpg4usb_portatil)
</div>

El programa de correo electrónico de **Mozilla** [**Thunderbird**](/es/thunderbird_principal) puede ser utilizado con un complemento llamado [**Enigmail**](/es/glossary#Enigmail) para cifrar y descifrar muy fácilmente mensajes de correo electrónico.

<div class="getstarted" markdown="1">
Parte Práctica: Empieza con [*Thunderbird cliente de correo seguro*](/es/thunderbird_principal)
</div>

La autenticidad de tu correo electrónico es otro aspecto importante de la seguridad en las comunicaciones. Cualquiera con acceso a la Internet y las herramientas correctas puede suplantarte enviando mensajes desde un correo electrónico falso que sea idéntico al tuyo. El peligro aquí es más aparente cuando se considera desde la perspectiva del destinatario. Imagina, por ejemplo, la amenaza planteada por un correo electrónico que aparenta ser de un contacto confiable pero que es en realidad de alguien cuyo objetivo es el de perturbar tus actividades o conocer información sensible sobre tu organización.

Debido a que no podemos ver o escuchar a nuestros corresponsales a través del correo electrónico, normalmente confiamos en la dirección del remitente para verificar su identidad, que es la razón por la cual somos fácilmente engañados por correos electrónicos falsos. Las [**Firmas digitales**](/es/glossary#Firma_digital) - las cuales también se sostienen en el [**cifrado**](/es/glossary#Cifrado) de clave pública - proporcionan un medio más seguro de probar la identidad de uno cuando se envía un mensaje. La guía del [***gpg4usb Portátil***](/es/gpg4usb_portatil) o la sección [***Utilizar Enigmail con GnuPG en Thunderbird***](/es/thunderbird_usarenigmail) de la [***Guía del Thunderbird***](/es/thunderbird_principal) explica en detalle cómo se hace esto.

<div class="background" markdown="1">
**Pablo**: Tengo un colega que una vez recibió un correo electrónico de parte mía que nunca envié. Decidimos, al final, que simplemente era correo comercial no deseado (spam), pero ahora me imagino cuanto daño podría haberse hecho si un correo electrónico falso apareciera en el buzón de la persona equivocada en el momento inapropiado. Escuche que se puede impedir esta clase de evento con firmas digitales ¿pero qué son?
			
**Claudia**: Una firma digital es como un sello lacrado sobre la solapa de un sobre con tu carta incluida. Excepto que no puede falsificarse. Esto prueba que eres el verdadero remitente del mensaje y que este no ha sido falsificado en el camino.
</div>



