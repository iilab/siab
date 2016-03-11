

---

lang: es
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 014
title: gpg4usb - email text and files encryption

---

**Página de incio**

- [**http://www.gpg4usb.org/**](http://www.gpg4usb.org/)

**Requisitos del sistema**

- Para todas las versiones de Windows

**Versión utilizada en esta guía**

- 0.3.3

**Última revisión de este capítulo**

- Junio, 2015

**Licencia**

- Software libre. Programa gratuito y de código abierto

**Lectura obligada**

- Guía práctica de instrucciones capítulo [**7. Mantener privada tu comunicación por internet**](/es/chapter-7)

- [**Seguridad digital y privacidad para los Defensores de los Derechos Humanos**](https://www.frontlinedefenders.org/esecman), capítulo **2.4 Criptología – Cifrado de Clave Pública (página 38)**

**¿Qué recibirás a cambio?**:

- La capacidad de cifrar archivos y mensajes de texto desde donde estés (por ejemplo, un café internet o desde tu trabajo) 
- La capacidad de cifrar los mensajes, *sin conexión* o cuando el acceso al internet no esté disponible, y más tarde enviarlos desde una computadora con acceso a la red de internet.

## 1.1 Cosas que deberías saber sobre esta herramienta antes de comenzar##

**gpg4usb** es un programa simple, ligero y portátil que te permite cifrar y descifrar mensajes de texto y archivos. **gpg4usb** está basado en la criptografía de las claves públicas. Bajo este método cada individuo debe crear su propio **par de claves** personal. La primera clave se conoce como la **clave privada**. Esta clave está protegida por una contraseña o frase de acceso, que se guarda y *nunca* se comparte con nadie. 

La segunda clave se conoce como la **clave pública**. Esta clave la puedes compartir con cualquiera de tus correspondientes  - y ellos pueden compartir las suyas contigo. Una vez que tengas la clave pública de un correspondiente, puedes empezar a enviarle mensajes de correo electrónico cifrados. Solamente esa persona podrá descifrar y leer tus correos, ya que es la única persona que tiene acceso a la clave privada correspondiente. 

Del mismo modo, si envías una copia de tu clave pública a tus contactos de correo electrónico y mantienes la clave privada correspondiente en secreto, solo tú podrás leer los mensajes cifrados de esos contactos. 

También puedes adjuntar firmas digitales a tus mensajes. El destinatario de tu mensaje quién posee una copia legítima de tu clave pública podrá verificar que el correo electrónico fue enviado por tí, y que su contenido no fue alterado en el camino. De igual forma, si tienes la clave pública de algún correspondiente, puedes verificar las firmas digitales en sus mensajes. 

**gpg4usb** te permite generar un par de claves cifradas, exportar las claves públicas para compartirlas con otras personas, escribir un mensaje de texto y cifrarlo. Puedes simplemente copiar y pegar la clave pública y/o el mensaje cifrado desde **gpg4usb** al cuerpo del correo electrónico, o guardarlos como un archivo de texto para ser enviado más tarde.  Los documentos y los archivos tambien puede ser cifrados.

**Nota**: Ten presente que las versiones originales y no cifradas de tus documentos y archivos pueden permanecer todavía en tu computadora, de modo que tanto tú como tu correspondiente deben recordar eliminarlos de las computadores cuando sea necesario.
 
**gpg4usb** te permite intercambiar claves y mensajes cifrados con otros programas **GPG** o  **PGP** similares. 

