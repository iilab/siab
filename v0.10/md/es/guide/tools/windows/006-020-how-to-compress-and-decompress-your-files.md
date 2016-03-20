

---

lang: es
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Compress and Decompress Your Files

---

Lista de secciones en esta página:

- [**3.0 Cómo comprimir tu copia de seguridad**](#3.0)
- [**3.1 Cómo descomprimir tu copia de seguridad**](#3.1)

-------

<a name="3.0"></a>
## 3.0 Cómo comprimir tu copia de seguridad ##

**Paso 1**. **Crea** una tarea de respaldo como se indica en la sección [**2.3 Cómo crear una copia de seguridad**](/es/cobian_propiedades#2.2) que contenga los archivos que quieras archivar.

**Paso 2**. **Selecciona** ![](/sbox/screen/cobian-es/22.png) en la barra lateral izquierda para activar la pantalla *Tarea nueva* como se ve a continuación:

![](/sbox/screen/cobian-es/23.png)

*Figura 1: La pantalla Tarea nueva mostrando los paneles Compresión y Encriptación fuerte*

El panel **Compresión** se usa para especificar el método de compresión de tu copia de seguridad.

**Nota**: La compresión se usa para reducir la cantidad de espacio para el almacenamiento de archivos. Si tienes muchos archivos viejos que solo utilizas ocasionalmente, pero todavía te interesa conservar, lo mejor sería guardarlos en un formato que ocupase el mínimo espacio posible. La compresión trabaja eliminando una gran cantidad de código innecesario de tus documentos, dejando intacta la información más importante. Asimismo, la compresión no daña los archivos originales. Sin embargo, los archivos no se pueden visualizar mientras están comprimidos, por lo que deberás ‘descomprimirlos’ si quieres visualizarlos de nuevo. 

Las tres sub-opciones en la lista desplegable del *Tipo de compresión* son:

*Sin compresión*: Como su nombre indica, esta opción no realiza ninguna compresión.

*Compresión zip*: Esta es la técnica de compresión para los sistemas **Windows**, y la más apropiada. Una vez creados los archivos, estos se pueden abrir con herramientas estándar de Windows (también puedes descargar [**ZipGenius**](http://www.zipgenius.it/) para descomprimirlos). 

Seleccionar una de las opciones de compresión listadas habilita automáticamente la sección *Opciones de división*, así como su correspondiente lista desplegable.

Las *Opciones de división* se aplican al almacenamiento en dispositivos extraíbles, como por ejemplo CD, DVD, disquetes y memorias USB. Las diversas opciones de división subdividirán el archivo en tamaños que quepan en el dispositivo que desees. 

Ejemplo: 
Digamos que estás guardando un gran número de archivos, y los quieres grabar en un CD. Como sea, el tamaño de sus archivos es mayor que 700MB (tamaño de un CD). La opción de división dividirá el archivo en piezas menores o iguales a 700MB, por lo que podrás grabarlo en tu CD. Si  vas a crear una copia de seguridad en el disco duro de tu ordenador, o el tamaño de los archivos que quieres copiar es menor que el del dispositivo en el que quieres guardarlos, puedes saltarte esta sección.

Las opciones siguientes están disponibles cuando hagas clic en la lista desplegable *Opciones de división*. Tu elección dependerá del tipo de dispositivo extraíble del que dispongas.

![](/sbox/screen/cobian-es/24.png)

*Figura 2: La lista desplegable de Opciones de división*

- 3,5" - Disquete. Esta opción es suficientemente grande como para realizar una copia de un pequeño número de documentos.
- Zip – Disco zip (comprueba la capacidad del que estás usando). Necesitarás un Lector Zip en tu ordenador, así como discos hechos a medida.
- CD-R - CD (comprueba la capacidad del que estás usando). Necesitarás un grabador de CD en tu ordenador, así como un programa de grabación de CD (ver la versión [**DeepBurner Free** ](http://www.deepburner.com/) u otras [**herramientas de grabación de disco**](http://www.thefreecountry.com/utilities/dvdcdburning.shtml)).
- DVD – Disco DVD (comprueba la capacidad del que estás usando). Necesitarás una grabadora de DVD en tu ordenador, así como un programa de grabación de DVD (ver la versión [**DeepBurner Free** ](http://www.deepburner.com/) u otras [**herramientas de grabación de disco**](http://www.thefreecountry.com/utilities/dvdcdburning.shtml)). 

Si estás realizando la copia en varias memorias USB, tal vez quieras configurar un tamaño personalizado.

Para hacer esto, sigue los siguientes pasos:

**Paso 1**. **Selecciona** la opción *Tamaño personalizado* (bytes), luego escribe el tamaño del archivo en bytes en el campo de texto de la siguiente manera:

![](/sbox/screen/cobian-es/25.png)

*Figura 10: El campo de texto Tamaño personalizado*

Para que tengas una idea de los tamaños

- 1KB (kilobyte) = 1024 bytes – un documento de texto de una página hecho en Open Office es de aproximadamente 20kb
- 1MB (megabyte) = 1024 KB – una foto tomada con una cámara digital suele ser de entre 1 - 3 MB
- 1GB (gigabyte) = 1024 MB – aproximadamente media hora de una película con calidad DVD 

**Nota**: Cuando escojas un tamaño personalizado para dividir tu copia de seguridad para un disco de CD o DVD, Cobian Backup no hará la copia en tu dispositivo extraíble automáticamente. Sin embargo, creará los archivos en tu ordenador para que después tú mismo los grabes en el CD o DVD.

*Protección de contraseña*: Esta opción te permitirá introducir una contraseña para proteger tus archivos. Simplemente escribe, y después vuelve a escribir la contraseña en las casillas correspondientes. Cuando intentes descomprimir el archivo, tendrás que introducir la contraseña antes de que empiece la descompresión.

 **Nota**: Si deseas proteger tu archivo de forma más segura, deberás considerar otro método aparte de la contraseña. **Cobian Backup** te permite encriptar tu archivo. Este método se explica en la sección [**4. Cómo encriptar tu Copia de seguridad**](/es/cobian_cifrarrespaldo). También puedes echar un vistazo a la [**Guía práctica Truecrypt**](/es/truecrypt_principal) para ver cómo crear un espacio de almacenamiento encriptado en tu ordenador o dispositivo extraíble.
 
*Comentario*: Esta opción te permite escribir una descripción para tu archivo, pero no es indispensable. 

<a name="3.1"></a>
## 3.1 Cómo descomprimir tu Copia de seguridad ##

Para descomprimir tu copia de seguridad, sigue los siguientes pasos:

**Paso 1**. **Seleccionar > Herramientas > Descompresor** como se muestra a continuación;

![](/sbox/screen/cobian-es/26.png)

*Figura 3: El menú Herramientas mostrando la opción Descompresor*.

La ventana **Descompresor** aparece como a continuación:

![](/sbox/screen/cobian-es/27.png)

*Figura 4: La ventana Cobian 10 Backup - Descompresor*

**Paso 2**. **Haz clic en** ![](/sbox/screen/cobian-es/28.png) para abrir la ventana del navegador y poder seleccionar el archivo que quieras descomprimir.

**Paso 3**. **Selecciona** el archivo (*.zip* o *.7x*) y **haz clic en** ![](/sbox/screen/cobian-es/13.png).

**Paso 4**. **Selecciona** el directorio en el que quieras descomprimir (salida) el archivo guardado. 

**Paso 5**. **Haz clic en** ![](/sbox/screen/cobian-es/29.png) para abrir una ventana nueva que te permita escoger la carpeta en la que descomprimir el archivo.

**Paso 6**. **Selecciona** una carpeta y **haz clic en** ![](/sbox/screen/cobian-es/13.png).

Usa el **Explorador de Windows** para ver los archivos incluidos en esa carpeta.

