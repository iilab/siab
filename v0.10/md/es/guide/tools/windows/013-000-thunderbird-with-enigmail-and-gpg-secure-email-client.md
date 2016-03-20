

---

lang: es
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 013
title: Thunderbird with Enigmail and GPG - Secure Email Client

---

**Inicio**

- [**www.mozilla.com/thunderbird**](http://www.mozilla.com/thunderbird/)
- [**www.enigmail.net**](http://enigmail.net/)
- [**www.gnupg.org**](http://www.gnupg.org/)
- [**trac.torproject.org/projects/tor/wiki/torbirdy**](https://trac.torproject.org/projects/tor/wiki/torbirdy)

**Requisitos del sistema**

- Todas las versiones de Windows

**Versiones usadas en esta guía**

- Thunderbird 31.7
- Enigmail 1.8.2
- GNU Privacy Guard (GnuPG) 2.1.0
- TorBirdy 0.1.4

**Última revisión de este apartado**

- Agosto de 2015

**Licencia**

- Software libre y de código abierto

**Lectura recomendada**

- Apartado Guía paso a paso [**7. Conservar la privacidad de tu comunicación en internet**](/es/chapter-7)

**Qué aprenderás**:  

- Gestionar diferentes cuentas de correo con un solo programa
- Leer y redactar mensajes después de desconectarlo de internet
- Cifrar con clave pública para que mantenga la privacidad de tu correo  

**GNU Linux, Mac OS y otros programas compatibles con Microsoft Windows**:

El cliente de correo de **Mozilla Thunderbird** está disponible para **GNU Linux**, **Mac OS**, **Microsoft Windows** y otros sistemas operativos.  Gestionar varias cuentas de correo es una tarea compleja desde el punto de vista de la seguridad digital. Por tanto, *recomendamos encarecidamente* que utilices **Mozilla Thunderbird** con este propósito.  Las ventajas de seguridad que ofrece **Thunderbird**, un programa multiplataforma *libre* y *de código abierto*, son incluso más importantes si las comparas con sus equivalentes comerciales, como **Microsoft Outlook**.  Sin embargo, si prefieres usar un programa diferente a **Mozilla Thunderbird**, recomendamos las siguientes alternativas libres y de código abierto:

* [**Claws  Mail**](http://www.claws-mail.org/) disponible para **GNU Linux** y **Microsoft Windows**;
* [**Sylpheed**](http://sylpheed.sraoss.jp/en/) disponible para **GNU Linux**, **Mac OS** y **Microsoft Windows**;
* [**Alpine**](http://www.washington.edu/alpine/) disponible para **GNU Linux**, **Mac OS** y **Microsoft Windows**.

Nota: Aunque recomendamos el uso de **Enigmail/GnuPG** por su fácil manejo con Thunderbird, también se pueden utilizar herramientas independientes de cifrado como gpg4usb junto con Thunderbird. Lee el apartado [gpg4usb](/es/gpg4usb_portatil) para descubrir otra forma de cifrar tu correo usando el método de cifrado con clave pública.

### 1.1 Cosas que deberías saber de esta herramienta antes de empezar ###

**Mozilla Thunderbird** es un cliente de correo multiplataforma, libre y de código abierto que sirve para recibir, enviar y almacenar correos electrónicos.  Un cliente de correo es una aplicación informática que te permite descargar y administrar tus correos electrónicos sin necesidad de un navegador.  Puedes administrar varias cuentas de correo con un solo programa.  Debes disponer de una cuenta de correo existente antes de utilizar **Thunderbird**.  También puedes crear cuentas de correo [**RiseUp**](/es/riseup_crearcuenta) si así lo deseas.

**Enigmail** es un complemento desarrollado para **Thunderbird**. Permite que los usuarios tengan acceso a las aplicaciones de autenticación y cifrado ofrecidas por **GNU Privacy Guard** (**GnuPG**).

**GnuPG** es un programa de cifrado con clave pública utilizado para generar y administrar los pares de claves que se usarán en el cifrado y descifrado de los mensajes, de esta manera tu comunicación por correo será privada y segura. Se debe instalar **GnuPG** para que **Enigmail** funcione, tal y como explicamos más adelante en este apartado.

