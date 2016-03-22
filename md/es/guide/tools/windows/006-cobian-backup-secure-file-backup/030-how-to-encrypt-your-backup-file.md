

---

lang: es
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: How to Encrypt Your Backup File

---

Lista de secciones de esta página:

- [**4.0 Sobre la Encriptación**](#4.0)
- [**4.1 Cómo encriptar tu copia de seguridad**](#4.1)
- [**4.2 Cómo desencriptar tu copia de seguridad**](#4.2)

-------

<a name="4.0"></a>
## 4.0 Sobre la Encriptación ##

La encriptación puede ser una necesidad para aquellos que deseen proteger su copia de seguridad de accesos no autorizados.

La encriptación es el proceso de codificar, o mezclar datos, de modo que parezcan ininteligibles para cualquiera que no cuente con la clave específica necesaria para decodificar el mensaje. Para más información sobre el proceso de encriptación, consulta la guía **Paso a paso** capítulo [**4. Proteger los archivos sensibles en tu computadora**](/es/chapter-4)

<a name="4.1"></a>
## 4.1 Cómo encriptar tu copia de seguridad ##

El panel *Encriptación fuerte* se usa para especificar el método de encriptación que deseas utilizar.

**Paso 1**. **Haz clic** en la casilla desplegable *Tipo de encriptación* para activar la lista de los diferentes métodos de encriptación, explicados a continuación:

![](/sbox/screen/cobian-es/31.png)

*Figura 1: La lista desplegable Tipos de encriptación*

Para simplificar las cosas, te recomendamos que escojas entre los métodos *Blowfish* o *Rijndael* (128 bits). Estos te proveerán una seguridad excelente para tus archivos, y te permitirán acceder a los datos encriptados con la contraseña elegida.

**Paso 2**. **Selecciona** el tipo de *Encriptación* que quieras utilizar.

**Nota**: *Rijndael* y *Blowfish* ofrecen aproximadamente el mismo nivel de seguridad. *DES* es más débil pero el proceso de encriptación es más rápido.

**Paso 3**. **Escribe** y **vuelve a escribir** la contraseña en las dos casillas como se muestra a continuación.

![](/sbox/screen/cobian-es/32.png)

*Figura 2: Los campos Tipo de cifrado y Frase clave*

La fuerza de la contraseña se indica en la barra marcada como ‘Calidad de la frase de seguridad’. Cuanto más a la derecha se mueva la barra, más fuerte es la frase de seguridad. Consulta el capítulo [**3.Cómo crear y mantener contraseñas seguras**](/es/chapter-3) de la **Guía paso a paso**, así como la Guía Práctica de [**KeePass**](/es/keepass_principal) para saber cómo crear y guardar frases de seguridad fiables (o contraseñas).

**Paso 4**. **Haz clic en** ![](/sbox/screen/cobian-es/13.png).

<a name="4.2"></a>
## 4.2 Cómo desencriptar tu copia de seguridad ##

Desencriptar tu copia de seguridad es rápido y sencillo. Para desencriptar tu copia de seguridad, sigue los siguientes pasos:

**Paso 1**. **Seleccionar > Herramientas > Descifrado y llaves**.

*Esto activará la ventana Descifrado y llaves como se ve a continuación:*

![](/sbox/screen/cobian-es/34.png)

*Figura 3: La ventana Descifrado y llaves de Cobian Backup 10*

**Paso 2**. **Haz clic en** ![](/sbox/screen/cobian-es/35.png) para seleccionar el archivo que quieres desencriptar.

**Paso 3**. **Haz clic en** ![](/sbox/screen/cobian-es/36.png) para seleccionar la carpeta en la que quieres guardar el archivo.

**Paso 4**. **Selecciona** el mismo tipo de encriptación que seleccionaste en la sección [**4.1 Cómo encriptar tu copia de seguridad**](/es/chapter_4_1#4.1), en la lista desplegable *Métodos*.

![](/sbox/screen/cobian-es/37.png)

*Figura 4: La lista desplegable Nuevos Métodos*

**Paso 5**. **Selecciona** el método apropiado de encriptación (la misma que utilizaste para encriptar tu copia de seguridad).

**Paso 6**. **Escribe** tu frase de seguridad en el campo de texto *Frase de seguridad*.

**Paso 7**. **Haz clic en** ![](/sbox/screen/cobian-es/38.png).

Los archivos se desencriptarán en el lugar especificado. Si los archivos estuviesen también comprimidos, necesitarás descomprimirlos como se indica en la sección [**3.1 Cómo descomprimir tu copia de seguridad**](/es/chapter_3_1#3.1).

