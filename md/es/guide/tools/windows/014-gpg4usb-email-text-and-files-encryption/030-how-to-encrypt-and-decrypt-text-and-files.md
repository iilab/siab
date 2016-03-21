

---

lang: es
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: How to Encrypt and Decrypt Text and Files

---

Secciones en esta página:

- [**4.0 Cómo cifrar mensajes de texto con gpg4usb**](#4.0)
- [**4.1 Cómo descifrar mensajes de texto con gpg4usb**](#4.1)
- [**4.2 Cómo cifrar archivos con gpg4usb**](#4.2)
- [**4.3 Cómo descifrar archivos con gpg4usb**](#4.3)

<a name="4.0"></a>
## 4.0 Cómo cifrar mensajes de texto con gpg4usb ##

En el ejemplo siguiente, Terence cifrará un correo electrónico para su amiga Salima, mediante los siguientes pasos:

**Paso 1**. **Pulsa dos veces** ![](/sbox/screen/gpg4usb-es-1/03.png) para abrir la consola de **gpg4usb**. 

**Paso 2**. **Redacta** tu mensaje como se muestra en el siguiente ejemplo:

![](/sbox/screen/gpg4usb-es-1/19.png)

*Figura 1: La consola gpg4usb mostrando un ejemplo de un mensaje*

**Paso 3**. **Habilita**  la casilla asociada con el destinatario previsto de tus correos electrónicos como a continuación:

![](/sbox/screen/gpg4usb-es-1/20.png)


*Figura 2*: La consola de gpg4usb mostrando el destinatario previsto

**Nota**. Puedes cifrar un mensaje a más de un destinatario simplemente habilitando sus casillas correspondientes en el panel *Cifrar para*. También puede resultar útil para tu registro propio cifrar el mensaje para ti mismo, para así leer después lo que mandaste. 

**Paso 4**. Elige ya sea **Pulsando** ![](/sbox/screen/gpg4usb-es-1/21.png) o **Selecciona cifrar** desde el menú **Cifrar** para cifrar tus mensaje de la siguiente manera:

![](/sbox/screen/gpg4usb-es-1/22.png)

*Figura 3: La consola gpg4usb  mostrando un ejemplo de un texto cifrado*

**Paso 5**. **Pulsa**  ![](/sbox/screen/gpg4usb-es-1/23.png) para seleccionar el mensaje cifrado completo y luego **pulsa** ![](/sbox/screen/gpg4usb-es-1/24.png) para copiar el mensaje al  portapapeles.

**Nota**. Alternativamente, puedes  usar las teclas de atajo asociadas con cada artículo del menú, en este caso **Ctrl + E** cifrará el mensaje, **Ctrl + A** seleccionará todo el mensaje cifrado, y **Ctrl + C** copiará el mensaje al portapapeles. 

**Paso 6**. **Abre** tu cuenta de correo electrónico y luego **abre** una página nueva de mensaje, y entonces **pega** este mensaje para que se parezca a lo siguiente:

![](/sbox/screen/gpg4usb-es-1/25.png)

*Figura 4: Un ejemplo de un mensaje cifrado en gpg4usb pegado a un correo electrónico de una cuenta Gmail.*

**Nota**. Los **Formatos de texto enriquecido** (**RTF**) pueden corromper el formato del mensaje cifrado; por lo tanto, es mejor redactar tu mensaje en texto simple. Para convertir **RTF** en texto simple en **Gmail** solamente **pulsa** en *Más Opciones* y **seleccionar** *Modo de texto sin formato* que se muestra al pie del panel de mensaje como a continuación:

![](/sbox/screen/gpg4usb-es-1/26.png)

*Figura 5: Opciones de formato en Gmail*

<a name="4.1"></a>
## 4.1 Cómo descifrar mensajes de texto con gpg4usb ##

Para descifrar un correo electrónico cifrado, realiza los siguientes pasos:

**Paso 1**. **Pulsa dos veces**  ![](/sbox/screen/gpg4usb-es-1/03.png) para abrir el programa **gpg4usb**. 

**Paso 2**. **Abre** tu cuenta de correo electrónico y luego **abre** el mensaje. 

**Paso 3**. **Selecciona**, **copia** y luego **pega** el mensaje cifrado en la pestaña *untitled1.txt* de la consola **gpg4usb** como se muestra a continuación:

![](/sbox/screen/gpg4usb-es-1/27.png)

*Figura 6: La consola de gpg4usb mostrando un mensaje a descifrar*

 **Nota**: Si el texto cifrado aparece con saltos de línea doble como se muestra debajo en la *figura 7*, **gpg4usb** quizás no pueda descifrarlo automáticamente. Para eliminar estos saltos de línea doble **pulsa**![](/sbox/screen/gpg4usb-es-1/27b.png) (o **selecciona** *Eliminar saltos de línea dobles* desde el menú **Editar**) para eliminarlas y luego continuar el proceso de descifrado en el **Paso 4**.

![](/sbox/screen/gpg4usb-es-1/28.png)

*Figura 7: La consola de gpg4usb mostrando un mensaje para descifrar con saltos de línea doble.*

**Paso 4**. **Pulsa** ![](/sbox/screen/gpg4usb-es-1/29.png) e ingresa la contraseña que asignaste cuando creaste un par de claves, como se muestra en la siguiente pantalla:

![](/sbox/screen/gpg4usb-es-1/30.png)

*Figura 8: La ventana de aviso de Ingresar Contraseña*

**Paso 5**. **Pulsa** *OK*  para activar una consola  de **gpg4usb** similar a la *figura 2* de arriba.

<a name="4.2"></a>
## 4.2 Cómo cifrar archivos con gpg4usb ##

El proceso para cifrar un archivo es parecido al de cifrar mensajes de texto; en el ejemplo que sigue Salima cifrará un archivo para Terence, usando los siguientes pasos:

**Paso 1**. **Pulsa doble**  ![](/sbox/screen/gpg4usb-es-1/03.png) para abrir el programa **gpg4usb**.

**Paso 2**. **Pulsa**  ![](/sbox/screen/gpg4usb-es-1/31.png) y  *Cifrar archivo* para activar la siguiente pantalla:

![](/sbox/screen/gpg4usb-es-1/32.png)

*Figura 9: La ventana de Cifrar Archivo*

La lista desplazable de la ventana *Cifrar Archivo* (con el contorno en negro) te permite seleccionar la cuenta de correo electrónico y su clave correspondiente que usarás para cifrarle un mensaje. 

**Paso 3**. **Pulsa** ![](/sbox/screen/gpg4usb-es-1/33.png) junto al ícono de *Entrada* para activar la siguiente pantalla:

![](/sbox/screen/gpg4usb-es-1/34.png)

*Figura 10: La ventana del navegador de Abrir Archivo*

**Paso 4**. **Pulsa**  ![](/sbox/screen/gpg4usb-es-1/35.png) para adjuntar el archivo a cifrar y regresa a la ventana *Cifrar* como a continuación:

![](/sbox/screen/gpg4usb-es-1/36.png)

*Figura 11: La ventana de Cifrar Archivo mostrando el archivo designado para cifrar*

**Paso 5**. **Pulsa**  *OK* para activar la siguiente pantalla:

![](/sbox/screen/gpg4usb-es-1/38.png)

*Figura 12: El cuadro de diálogo de confirmación Finalizar*

El cuadro de diálogo de confirmación *Finalizar* le muestra donde reside el archivo recién cifrado. Un archivo cifrado también puede ser identificado por la extensión *asc*, por ejemplo, *Meeting Minutes.doc.asc*

**Paso 6**. **Pulsa** *OK* para completar el proceso de cifrado del archivo. 

**Nota**. Puedes cifrar un mensaje de texto que puedes enviar junto con el archivo cifrado separadamente. 

**Paso 7**. Usando tu cuenta de correo electrónico, **dirígete** a la ubicación especificada en el cuadro de confirmación *Finalizar* (*Figura 12*), y luego adjunta el archivo cifrado a tu correo electrónico como lo harías con cualquier otro archivo. 

**IMPORTANTE**: Asegúrate de que el nombre del archivo **no está cifrado**. ¡Asegúrate de que el nombre no revele ninguna información importante! No olvides que una versión no cifrada del archivo aún reside en el disco. 

<a name="4.3"></a>
## 4.3 Cómo descifrar archivos con gpg4usb ##

En el ejemplo a continuación, Terence descifrará el archivo que Salima le envió, siguiendo estos pasos:

**Paso 1**. **Pulsa dos veces** ![](/sbox/screen/gpg4usb-es-1/03.png) para abrir el programa **gpg4usb**. 

**Paso 2**. **Abre** tu cuenta de correo electrónico, **abre** el mensaje y **descarga** el archivo adjunto.

**Nota**: Si tu correspondiente te ha enviado un mensaje junto con el archivo cifrado, puedes descifrar este mensaje usando el método expresado en la sección [**4.1 Como descifrar mensajes de texto con gpg4usb**](/en/gpg4usb-encryptdecrypt#4.1).

**Paso 3**. En la consola de **gpg4usb** (como se muestra en la *figura 1* anteriormente), **Pulsa** ![](/sbox/screen/gpg4usb-es-1/31.png) y en la ventana **Descifrar Archivo**  (como se muestra debajo en la *figura 13*).

**Paso 4**. **Pulsa** ![](/sbox/screen/gpg4usb-es-1/33.png) junto al ícono *Entrada* para navegar hasta la ubicación del archivo cifrado descargado como se muestra a continuación:
![](/sbox/screen/gpg4usb-es-1/37.png) 

*Figura 13: La ventana de descifrado, mostrando el camino al archivo cifrado*

**Paso 5**. **Pulsa** *OK* para finalizar el proceso y que se muestre la ruta del fichero.

**Importante**. Si estás trabajando en un café internet o en estaciones de trabajo donde otras personas tienen acceso a la versión del archivo descifrado, es mejor copiar el archivo *.asc* a tu disco portátil o USB y llevártelo para que puedas descifrarlo en privado en tu propia casa.

