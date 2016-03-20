

---

lang: es
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 5
depth: 3
title: Torbirdy - adding digital anonymity and circumvention to Thunderbird

---

![](/sbox/screen/thunderbird-TorBirdy-es/01.png)

**TorBirdy** es un complemento para Thunderbird que se puede utilizar para enviar y recibir correos electrónicos a través de la red Tor, así como proteger tu comunicación con el servidor de correo que uses, aumentar el anonimato de tus mensajes y evitar la posible censura. **TorBirdy** es un complemento magnífico para el cifrado de **Enigmail y GnuPG**.

Puedes [descargar TorBirdy](https://addons.mozilla.org/en-us/thunderbird/addon/torbirdy/) desde el servidor de complementos de Mozilla Thunderbird. 

Se necesita iniciar y configurar los siguientes componentes en tu ordenador para usar TorBirdy:

- Thunderbird (consulta el apartado [**Thunderbird con Enigmail y GPG - Cliente de correo seguro**](/es/thunderbird_principal));
- Navegador Tor (consulta el apartado [**Navegador Tor - Anonimato y camuflaje digital**](/es/tor_principal)).

Hay que tener en cuenta que TorBirdy aún está en fase de desarrollo y prueba. Existen otras alternativas disponibles que se pueden emplear para proteger la comunicación entre Thunderbird y tu servidor de correo, como VPN o SSH proxy - consulta el apartado 8. Guía paso a paso [**8. Permanecer anónimo y evitar la censura en internet**](/es/chapter-8)

<a name="1.0"></a>
## 6.1 Instalar TorBirdy para Thunderbird ##

Después de [descargar  **TorBirdy**](https://addons.mozilla.org/en-us/thunderbird/addon/torbirdy/) en tu ordenador, comienza la instalación de **TorBirdy** realizando los pasos siguientes: 

 **Paso 1**. **Abre Thunderbird**, luego **haz clic** en ![](/sbox/screen/thunderbird-TorBirdy-es/03.png) para mostrar el *Menú de Thunderbird* y **selecciona Complementos** para activar la ventana *Administrador de complementos*.

**Paso 2**. **Haz clic** en ![](/sbox/screen/thunderbird-TorBirdy-es/04.png) en la barra lateral izquierda.

**Paso 3**. **Haz clic** en ![](/sbox/screen/thunderbird-TorBirdy-es/05.png) y  **selecciona** *Instalar complemento desde archivo* tal y como se muestra a continuación: 

![](/sbox/screen/thunderbird-TorBirdy-es/06.png)

*Imagen 1: Menú de herramientas para todos los complementos*

**Paso 4**. Navega hasta la carpeta donde has guardado el complemento TorBirdy (probablemente en la carpeta *Descargas*) tal y como se muestra en la pantalla siguiente:

![](/sbox/screen/thunderbird-TorBirdy-es/07.png)

*Imagen 2: Seleccionar extensión para su instalación*

**Paso 5**.  **Haz clic** en ![](/sbox/screen/thunderbird-TorBirdy-es/08.png) para activar la siguiente pantalla:

![](/sbox/screen/thunderbird-TorBirdy-es/09.png)

*Imagen 3: Ventana Instalación de programa*

**Importante**: ¡Antes de realizar el paso siguiente, asegúrate de que has enviado o guardado todos tus correos! 

**Paso 6**. **Haz clic** en ![](/sbox/screen/thunderbird-TorBirdy-es/10.png) y luego **haz clic** en ![](/sbox/screen/thunderbird-TorBirdy-es/11.png) para reiniciar Thunderbird y completar la instalación del complemento **TorBirdy**.


## 6.2 Usar TorBirdy en Thunderbird ##

Antes de utilizar **TorBirdy** con **Thunderbird**, debes asegurarte de que el **Navegador Tor** funciona y está bien conectado a la **Red Tor**. Pero si no has instalado el **Buscador Tor**, consulta [**Buscador Tor - Anonimato y camuflaje digital**](/es/tor_principal) antes de continuar.

## 6.2.1 Habilitar TorBirdy para Thunderbird ##

Sigue los pasos siguientes para iniciar el **Navegador Tor** y ejecuta Thunderbird a través de la red *Tor*
 
**Paso 1**. **Navega** hasta la carpeta *Navegador Tor*, y luego **haz doble clic** en ![](/sbox/screen/thunderbird-TorBirdy-es/18.png) para activar la siguiente pantalla:

![](/sbox/screen/thunderbird-TorBirdy-es/19.png)

*Imagen 8: Ventana Estado de Tor*

*Nota: se recomienda cerrar cualquier ventana abierta de Firefox antes de iniciar el Navegador Tor*

Poco después, el **Navegador Tor** abrirá una nueva ventana donde se muestra lo siguiente:

![](/sbox/screen/thunderbird-TorBirdy-es/20.png)

*Imagen 9: Navegador Tor; conectado con éxito a la red Tor*

Ahora estás conectado a la *Red Tor* a través del *Navegador Tor*.

**Paso 2**. **Inicia** Thunderbird e introduce tu contraseña cuando te la solicite. Se verá el estado de TorBirdy en la esquina inferior derecha de la ventana de Thunderbird tal y como se muestra a continuación:


 ![](/sbox/screen/thunderbird-TorBirdy-es/30.png)  

*Imagen 10: TorBirdy habilitado para Tor*

## 6.2.2 Confirmar TorBirdy se conecta usando Tor ##

Sigue los pasos siguientes para probar y confirmar los ajustes de TorBirdy.

**Paso 1**. **Haz clic** en ![](/sbox/screen/thunderbird-TorBirdy-es/21.png) para activar el siguiente menú: 

![](/sbox/screen/thunderbird-TorBirdy-es/22.png)

*Imagen 11: Menú de preferencias de TorBirdy*

**Paso 2**. **Selecciona** *Abrir Preferencias de TorBirdy* para abrir la ventana que ves a continuación. **Haz clic** en ![](/sbox/screen/thunderbird-TorBirdy-es/23.png) el mensaje de advertencias de *Opciones avanzadas de TorBirdy*.   

![](/sbox/screen/thunderbird-TorBirdy-es/25.png)

*Imagen 12: Ventana Preferencias de TorBirdy*

**Paso 3**. **Haz clic** en ![](/sbox/screen/thunderbird-TorBirdy-es/24.png). Si te has conectado con  éxito a través de la red *Tor*, verás el siguiente mensaje (*Las direcciones IP cambiarán*).

![](/sbox/screen/thunderbird-TorBirdy-es/26.png)

*Imagen 13: Ventana ¿Estás usando Tor?*

**Nota**: Si no has iniciado el Navegador de Tor o no se conectó a la Red Tor como se muestra en la sección anterior 6.2.1, no podrás conectarte a tu servidor de correo y puede aparecer el siguiente mensaje cuando inicies Thunderbird:

![](/sbox/screen/thunderbird-TorBirdy-es/27.png)

*Imagen 14: Mensaje Conexión rechazada*

Hay que tener en cuenta que algunos proveedores de correo como Google Mail podrían rechazar la conexión al servidor de correos a través de la *red Tor*.

## 6.3 Deshabilitar TorBirdy para Thunderbird ##

Puedes deshabilitar el complemento TorBirdy si deseas ejecutar Thunderbird sin él  siguiendo los pasos siguientes:

**Paso 1**. **Abre Thunderbird**, luego **haz clic** en ![](/sbox/screen/thunderbird-TorBirdy-es/03.png) para mostrar el *Menú Thunderbird* y **seleciona Complementos** para activar la ventana *Administrador de complementos*.

**Paso 2**. **Haz clic** en ![](/sbox/screen/thunderbird-TorBirdy-es/04.png) en la barra lateral izquierda.

**Paso 3**. **Haz clic** en ![](/sbox/screen/thunderbird-TorBirdy-es/29.png) de la pantalla siguiente: 

![](/sbox/screen/thunderbird-TorBirdy-es/28.png)

*Imagen 15: Deshabilitar la extensión TorBirdy*

**Paso 4**. **Haz clic** en ![](/sbox/screen/thunderbird-TorBirdy-es/11.png) para reiniciar Thunderbird y terminar de deshabilitar TorBirdy.

