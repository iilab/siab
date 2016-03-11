

---

lang: es
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: How to Install gpg4usb and Generate a Key Pair

---

Secciones en esta página:

- [**2.0 Cómo instalar gpg4usb**](#2.0)
- [**2.1 Cómo generar un par de claves con gpg4usb**](#2.1)

<a name="2.0"></a>
## 2.0 Como instalar gpg4usb ##

**gpg4usb** es una herramienta portátil que no requiere ser instalada en la computadora. El programa se encuentra como archivo comprimido zip y debe ser extraído directamente a un disco USB o a una carpeta en la computadora. Para comenzar realiza los pasos siguientes:

**Paso 1**. **Localiza** el archivo comprimido **gpg4usb**, y después **extrae** todos los archivos a un disco USB removible o en una carpeta en tu computadora. 

![](/sbox/screen/gpg4usb-es-1/01.png)

*Figura 1: Ubicación de destino del programa gpg4usb*

<a name="2.1"></a>
## 2.1 Como generar un par de claves con gpg4usb ##

Antes de comenzar a cifrar y descifrar correos electrónicos, mensajes de texto, documentos y archivos, debes seguir dos pasos preliminares: primero necesitas generar o importar tu par de claves cifradas y segundo necesitas enviar tu clave pública a tus contactos y recibir sus claves públicas e importarlas a tu administrador de claves. En la próxima página describimos como compartir las claves públicas. **gpg4usb** te ayuda a generar tu par de claves la primera vez que inicias el programa. Ten en cuenta que siempre puedes regresar a la ventana de *Primeros Pasos* desde el menú de *Ayuda* -> *Abrir Asistente*.

**Paso 1**. Para ejecutar el programa **gpg4usb** por primera vez, **encuentra y pulsa dos veces** ![](/sbox/screen/gpg4usb-es-1/02.png) para abrir la carpeta **gpg4usb** y después **pulsa dos veces** ![](/sbox/screen/gpg4usb-es-1/03.png). Esto  activará la ventana de *Primeros Pasos*. Selecciona un idioma y pulsa en *Siguiente*. 

**Paso 2**. En la pantalla *Asistente para empezar*, pulsa *Crear un nuevo par de claves*.

![](/sbox/screen/gpg4usb-es-1/04.png)

*Figura 2: Asistente para empezar*

Observa las otras opciones para importar las claves existentes disponibles en la pantalla del asistente para el primer inicio. Si estás actualizando desde una versión anterior de gpg4usb, puedes seleccionar *importar configuración y/o claves desde el gpg4usb*. Si estás usando [Thunderbird con Enigmail](/es/thunderbird_principal), puedes seleccionar la opción *importar claves desde GnuPG*.  También puedes seleccionar el importar claves más adelante ejecutando el asistente otra vez desde el menú *Ayuda*-> *Abrir Asistente*.

**Paso 3**. En **Crear un par de llaves** **Pulsa**  *Crear llave nueva*

![](/sbox/screen/gpg4usb-es-1/05.png)

*Figura 3: Crear llave nueva*

**Paso 4**. **Ingresa** la información adecuada en los campos de texto correspondientes, para que tu pantalla se parezca a la siguiente:

![](/sbox/screen/gpg4usb-es-1/06.png)

*Figura 4: Un ejemplo de un formulario finalizado de Crear Llave.*

**Importante:**

* Establece una contraseña segura para proteger tu clave privada (por favor dirígete al capítulo [**3. Cómo crear y mantener contraseñas seguras**](/es/chapter-3)).
* Te aconsejamos que uses una fecha de expiración y que la fijes a menos de 5 años. 
* Te recomendamos sobre todo, que generes claves de un tamaño de por lo menos 2048 bits. Una clave de un mayor tamaño es más segura, pero también requiere más tiempo para crear, cifrar y descifrar textos.

**Nota**. No necesitas usar tu nombre y dirección de correo electrónico verdaderos cuando generas tu  clave. Sin embargo, usar la dirección de correo electrónico de la cuenta que vas a usar para comunicarte facilitará a tus contactos el asociar tu clave con dicha cuenta. 

**Paso 6**. **Pulsa**  **OK** para generar el par de claves.

![](/sbox/screen/gpg4usb-es-1/07.png)

*Figura 5: Generar clave…*

![](/sbox/screen/gpg4usb-es-1/08.png)

*Figura 6: Nueva clave creada*

**Paso 7**. **Pulsa OK** para regresar a la ventana **gpg4usb**. Después de haber generado exitosamente el par de claves, verás una pantalla parecida a la siguiente:

![](/sbox/screen/gpg4usb-es-1/09.png)

*Figura 7: La ventana gpg4usb, mostrando el par de claves recién creado.*

Ahora que has creado un nuevo par de claves exitosamente, necesitas aprender como exportar tu clave pública para compartirla con otras personas, y como importar las claves públicas de tus correspondientes.

