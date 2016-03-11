

---

lang: es
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 005
title: TrueCrypt - Secure File Storage

---

**El 28 de mayo de 2014, los desarrolladores del sitio web de TrueCrypt comenzaron a informar a los usuarios que a partir de ese momento suspenderían el desarrollo de TrueCrypt. Aun no aclaran las circunstancias que llevaron a esta situación. Los desarrolladores del sitio ofrecen la nueva versión 7.2 de TrueCrypt, de funcionalidad reducida. Pese a este nuevo lanzamiento, recomendamos que continúes utilizando la versión 7.1a anterior (véanse las instrucciones para descargarla), hasta que sepamos más acerca de lo que ha sucedido y de los planes futuros para el desarrollo de TrueCrypt. Para alternativas a TrueCrypt por favor consulta «GNU Linux, Mac OS y otros programas compatibles con Microsoft Windows» en la siguiente sección.**

**Página de inicio**

[**www.truecrypt.org**](http://www.truecrypt.org)

**Requisitos para la computadora**

- Windows 2000/XP/2003/Vista/7
- Derechos de administrador para la instalación o creación de volúmenes, pero no para acceder a volúmenes existentes 

**Versión utilizada en esta guía**

- 7.1a

**Última revisión del presente capítulo**

- Junio de 2015

**Licencia**

- Programa informático gratuito y de código abierto 

**Versión portátil**

 - [**Guías prácticas para TrueCrypt portátil**](/es/truecrypt_portatil)

**Lectura necesaria**

- Guía capítulo [**4. Cómo proteger los archivos sensibles de tu computadora**](/es/chapter-4)

**Qué obtienes a cambio**: 

- La capacidad de proteger tus archivos eficazmente de intrusos o accesos no autorizados
- La capacidad de almacenar de manera fácil y segura copias de tus archivos importantes  


**GNU Linux, Mac OS y otros programas compatibles con Microsoft Windows:**

**Nota**: **TrueCrypt** también se encuentra disponible en **GNU Linux** y **Mac OS**. 

Muchas distribuciones de **GNU Linux**, como [**Ubuntu**](http://www.ubuntu.com/), disponen de cifrado y descifrado sobre la marcha para el disco completo, como una característica estándar; puedes decidir utilizarla al instalar el sistema. Además, también recomendamos la activación del cifrado de la capeta de inicio durante la instalación. También puedes agregar la funcionalidad de cifrado a tu sistema **Linux** mediante la integración de [**dm-crypt**](http://www.saout.de/misc/dm-crypt/) y [**cryptsetup y LUKS**](https://gitlab.com/cryptsetup/cryptsetup). Otra opción es utilizar [**ScramDisk para Linux SD4L**](http://sd4l.sourceforge.net/), un programa de cifrado y descifrado sobre la marcha gratis y de código abierto.

Para **Mac OS** puedes usar **FileVault**, que es parte del sistema operativo, para ofrecer cifrado y descifrado *sobre la marcha* para el contenido completo de tu disco o tu carpeta de inicio y todas las subcarpetas.

Un programa alternativo en **Microsoft Windows** cuyo uso recomendamos es:

* [DiskCryptor](https://diskcryptor.net/wiki/Main_Page), una solución de cifrado de código abierto que ofrece el cifrado de todas las particiones del disco, incluida la del sistema.
* [**AxCrypt**](http://www.axantum.com/AxCrypt/) es un programa gratis y de código abierto capaz de cifrar archivos individuales.

Para las versiones MS Windows 7 Ultimate o Enterprise o MS Windows 8 Pro y Enterprise puedes utilizar [**BitLocker**](http://windows.microsoft.com/en-us/windows7/products/features/bitlocker) para el cifrado del disco completo. Nota: BitLocker es un programa cerrado de Microsoft, que no se somete a una auditoría independiente para establecer el nivel de protección y privacidad que ofrece a tu información.

### 1.1 Lo que debes saber sobre esta herramienta antes de empezar ###

**TrueCrypt** protege tu información de accesos no autorizados bloqueándola con una contraseña que tú crearás. ¡Si olvidas esa contraseña pierdes acceso a tu información! **TrueCrypt** utiliza un proceso llamado cifrado para proteger tus archivos. Ten en cuenta que el uso del cifrado es ilegal en algunos países. En lugar de cifrar archivos específicos, **TrueCrypt** crea un área protegida, o *volumen*, en tu computadora. Puedes almacenar tus archivos de forma segura en este volumen cifrado. 

**TrueCrypt** ofrece la posibilidad de crear un volumen cifrado común u oculto. Ambos mantendrán tus archivos confidenciales, pero un volumen oculto te permite esconder información importante detrás de datos menos sensibles, con el objeto de protegerla, aunque te veas forzado a revelar la existencia de tu volumen **TrueCrypt**. Esta guía proporciona información detallada sobre ambos volúmenes. 

