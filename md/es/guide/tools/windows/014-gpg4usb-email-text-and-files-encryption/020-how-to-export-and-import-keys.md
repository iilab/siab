

---

lang: es
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Export and Import Keys

---

Secciones en esta página:

- [**3.1 Cómo exportar tu clave pública con gpg4usb**](#3.1)
- [**3.2 Cómo importar una clave pública de un correspondiente con gpg4usb**](#3.2)
- [**3.3 Cómo verificar una clave pública usando gpg4usb**](#3.3)

<a name="3.1"></a>
## 3.1 Como exportar tu clave pública con gpg4usb##

Debes enviar tu clave pública a tu correspondiente antes de que ellos te puedan enviar mensajes cifrados. 

Para exportar tu clave pública con **gpg4usb**, realiza los pasos siguientes:

**Paso1** **Pulsa dos veces** ![](/sbox/screen/gpg4usb-es-1/02.png) para abrir la carpeta **gpg4usb**. 

**Paso 2**. **Pulsa dos veces**  ![](/sbox/screen/gpg4usb-es-1/03.png) para abrir el programa **gpg4usb**.

**Paso 3**. **Pulsa** ![](/sbox/screen/gpg4usb-es-1/10a.png) para activar la pantalla siguiente:

![](/sbox/screen/gpg4usb-es-1/10.png)

*Figura 1: La ventana del Administrador de claves mostrando todos los pares de claves.*

**Paso 3**. **Habilita** tu propia clave, como se muestra arriba en la *Figura 1*. 

**Paso 4**. **Selecciona** el ícono de *Exportar a archivo* desde el menú **Clave** mostrado a continuación:

![](/sbox/screen/gpg4usb-es-1/11.png)

*Figura 2: La ventana del Administrador de claves con el ícono de Exportar a archivo seleccionado*

Esto activará la siguiente pantalla: 

![](/sbox/screen/gpg4usb-es-1/12.png)

*Figura 3: Ventana de navegación de Exportar a carpeta*

**Paso 5**. **Pulsa**  ![](/sbox/screen/gpg4usb-es-1/13.png) para guardar tu par de claves en la carpeta del programa **gpg4usb**.

**Paso 6**. **Envía** el archivo exportado con tu clave pública como un adjunto a tu correspondiente.

<a name="3.2"></a>
## 3.2 Cómo importar la clave pública de un correspondiente con gpg4usb ##

Antes de poder cifrar información y enviarla a tu correspondiente, necesitas recibir e importar la clave pública de esa persona. Para importar la clave pública de un correspondiente usando **gpg4usb**, realiza los siguientes pasos:

**Paso 1**. **Pulsa dos veces**  ![](/sbox/screen/gpg4usb-es-1/03.png) para abrir el programa **gpg4usb**.

**Paso 2**. **Pulsa**   ![](/sbox/screen/gpg4usb-es-1/14.png) Importar para  activar la siguiente pantalla:

![](/sbox/screen/gpg4usb-es-1/15.png)

*Figura 4: Cuadro de diálogo de Importar Clave*

**Paso 3**. **Navega** y selecciona la clave que deseas importar.

![](/sbox/screen/gpg4usb-es-1/16a.png)

*Figura 5: Abrir clave*

**Paso 4**. **Pulsa** Abrir para activar la siguiente pantalla.

![](/sbox/screen/gpg4usb-es-1/16b.png)

*Figura 6: Detalles de Importación de Clave*
 
**Paso 5**. **Pulsa  OK** para cerrar la ventana anterior y regresar a la pantalla principal de **gpg4usb**.  Esta mostrará la clave pública recién importada como a continuación:

![](/sbox/screen/gpg4usb-es-1/16a.png)

*Figura 7: La consola de gpg4usb mostrando la clave pública recién importada asociada a la cuenta de tu correspondiente*

Ahora que has importado exitosamente la clave pública de tu correspondiente, deberás verificar y firmar la clave importada.

<a name="3.3"></a>
## 3.3 Cómo verificar un par de claves usando gpg4usb ##

Debes verificar que la clave importada pertenece realmente a la persona que supuestamente te la envío y entonces verificarla como auténtica. Este es un paso importante que tanto tú como tus contactos de correo electrónico deben seguir para cada clave pública que reciben. 

Para verificar un par de claves, realiza los pasos siguientes:

**Paso 1**. **Contacta** a tu correspondiente a través de algún medio de comunicación que no sea correo electrónico. 

**Nota**: Puedes utilizar un teléfono, mensajes de texto, **Voz sobre Protocolo de Internet**  (**VoIP**) o cualquier otro método, pero solo si estás seguro que estás comunicándote con la persona correcta. Como resultado, las conversaciones telefónicas o los encuentros cara a cara proporcionan la mayor garantía de autenticidad sobre la identidad de esa persona, siempre y cuando puedan acordarse de manera segura. 

**Paso 2**. Tú y tu correspondiente deben verificar que las “huellas digitales” de las claves públicas que han intercambiado sean las mismas. 

**Nota**. Una huella digital es una serie de números y letras únicos que identifica a cada clave. La huella digital en sí no es secreta, y puede ser guardada y usada para verificación más adelante cuando sea o si es requerida. 

Para ver la huella digital de los pares de claves que has creado o claves públicas que has importado, realiza los pasos siguientes:

**Paso1**. **Selecciona** una clave, después **pulsa el lado derecho** para activar su menú emergente asociado. 

**Paso 2**. **Selecciona** el ícono de *Mostrar detalles de la clave* como se muestra en la *figura 8*.

![](/sbox/screen/gpg4usb-es-1/17.png)

*Figura 8: El menú emergente asociado con la clave de tu correspondiente*

Esto activará la siguiente pantalla:

![](/sbox/screen/gpg4usb-es-1/18.png)

*Figura 9: La ventana de los Detalles de la clave con la huella digital de la clave en la parte de abajo.*

**Paso 3**. **Compara** esta huella digital con la que tu correspondiente ve en su programa **gpg4usb**. 

Tu correspondiente debe repetir estos pasos. Confirmen entre ustedes que la huella digital de las claves que han intercambiado coincide con la original de la persona que la envía. Si no es así, intercambien sus claves públicas otra vez (quizás mediante otro correo electrónico o medio de comunicación) y repitan el proceso de verificación. 

Si las huellas digitales coinciden *exactamente*, entonces ya están listos para enviar mensajes y archivos cifrados el uno al otro de manera segura. 

