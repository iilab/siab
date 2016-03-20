

---

lang: es
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to access the Internet using the Tor Browser

---

- [**3.0 Cómo conectarse con la red de Tor**](#3.0)      
- [**3.1.1 - Acceso directo**](#3.1.1)
- [**3.1.2 - Acceso restringido**](#3.1.2)
- [**3.2 Vuelva a configurar el acceso a la red de Tor**](#3.2)
- [**3.3 Obtener direcciones de puente de acceso**](#3.3)

<a name="3.0"></a>
## 3.0 Cómo conectarse con la red de Tor ##      

La primera vez que comience a usar **Navegador Tor** se le solicitará elegir cómo acceder a Internet: 

- [Acceso directo](#3.1.1):  Deberá elegir esta opción si su acceso a Internet no está restringido y si el uso de **Tor** **no está siendo** bloqueado, prohibido o monitoreado desde donde usted se encuentre.

- [Acceso restringido](#3.1.2): Deberá elegir esta opción si su acceso a Internet está restringido y si el uso de **Tor** **está siendo** bloqueado, prohibido o monitoreado desde donde usted se encuentre.

Esta configuración se puede cambiar en cualquier fase desde dentro de **Navegador Tor** sin necesidad de volver a instalar el programa. Esto deberá hacerse si usted llegara a cambiar de ubicación o se encontrara visitando otro país.

En el momento en el que usted comience a usar **Navegador Tor** el mismo programa lo conectará con la red de **Tor** sin necesidad de configuración adicional. 


<a name="3.1.1"></a>
## 3.1.1 Cómo conectarse con la red de Tor ##      

Para configurar **Navegador Tor** para acceder a la red de **Tor** directamente, realice los siguientes pasos:

**Paso 1**: **Navegue** por la carpeta **Navegador Tor** y haga **doble clic** ![] (/sbox/screen/tor-es-1/010.png) para activar la siguiente pantalla:

![](/sbox/screen/tor-es-1/012.png)

*Figura 1: Panel de configuración de la red de Tor*


**Paso 2**: Haga **clic** en el botón ![] (/sbox/screen/tor-es-1/013.png), el cual abrirá la ventana de **Estado de Tor** que mostrará el progreso de conexión del programa con la **Red Tor**.

![](/sbox/screen/tor-es-1/014.png)

*Figura 2: La ventana de Estado de Tor muestra el proceso de conexión*

Después de unos segundos, el **Navegador Tor** activará una nueva ventana de buscador mostrando la siguiente pantalla:

![](/sbox/screen/tor-es-1/015.png)

*Figura 3: Navegador Tor; conectado con éxito a la red de Tor*

Ahora puede explorar la web con la protección de la *Red de Tor*.

**Nota**: Cada vez que quiera ejecutar el **Navegador Tor**, se abrirá automáticamente la ventana de **Estado de Tor** (*Figura 2*) antes de iniciar el **Navegador Tor** (*Figura 3*). 


<a name="3.1.2"></a>
## 3.1.2 Cómo conectarse con la red de Tor ##      

Si usted vive en un área donde el acceso directo a la red Tor, como se describe más arriba, no es posible o conlleva riesgos, podrá configurar Tor a modo de evitar los obstáculos que se presenten.  

**Paso 1**: **Navegue** por la carpeta **Navegador Tor** y haga **doble clic** ![] (/sbox/screen/tor-es-1/010.png) para activar la siguiente pantalla:

![](/sbox/screen/tor-es-1/012.png)

*Figura 4: Panel de configuración de la red de Tor*

**Paso 2**: Haga **clic** en el botón ![] (/sbox/screen/tor-es-1/016.png) el cual abrirá una nueva ventana. Se le presentarán tres preguntas cortas de configuración para así facilitar el acceso a la **Red de Tor**.

**Pregunta 1:** *Administración de acceso;* Si necesita acceder a Internet por medio de un proxy pulse **sí** y luego presione ![] (/sbox/screen/tor-es-1/017.png). Si no usa un proxy **diga no** y luego presione ![](/sbox/screen/tor-es-1/017.png).

Si selecciona **sí** arriba, complete en su configuración de administración de la siguiente pantalla.  Si no conoce su configuración de administración, revise la configuración de su navegador habitual. En **Firefox** podrá encontrarla en *Opciones* > *Avanzadas* > *Red* en la sección *Conexión* > *Configuración*. En otros navegadores deberá buscar en *Opciones de Internet*. Use la opción *Ayuda* de su navegador si necesita más información.

![](/sbox/screen/tor-es-1/018.png)

*Figura 5: Pantalla de configuración de administración*

**Pregunta 2:** *Puertos Restringidos.* Si accede a Internet a través de una barrera de control de accesos que sólo permite el acceso sobre determinados puertos, por ejemplo *puerto 80 ó 443* para navegar por la web, seleccione **si** y presione ![](/sbox/screen/tor-es-1/017.png) para configurar el puerto, de lo contrario seleccione **no** y presione ![](/sbox/screen/tor-es-1/017.png). 

![](/sbox/screen/tor-es-1/019.png)

*Figura 6: Pantalla de configuración del puerto de restricción*

**Pregunta 3:** *Conexión a Internet censurada*; Si vive en un país en el que el tráfico de **Tor** está bloqueado de forma activa o es monitoreado, usted puede configurar **Navegador Tor** para usar un *Puente* que podrá ocultar su actividad en **Tor**. 

Una vez que haya hecho clic después de *la pregunta 2* en ![](/sbox/screen/tor-es-1/017.png) se le presentará una pantalla permitiéndole pegar las **Direcciones puente**.  Vea la sección [Conseguir Direcciones Puente](#3.3) para conseguirlas.

![](/sbox/screen/tor-es-1/020.png)

*Figura 7: Pantalla de configuración de las direcciones puente de Tor*

Una vez haya añadido las **direcciones puente** haga clic en ![](/sbox/screen/tor-es-1/021.png) para terminar con su configuración y poder conectarse a la **Red de Tor**.

![](/sbox/screen/tor-es-1/014.png)

*Figure 8: La ventana de Estado de Tor muestra el proceso de conexión*

Después de unos minutos, el **Navegador Tor** activará una nueva ventana de buscador mostrando la siguiente pantalla:

![](/sbox/screen/tor-es-1/015.png)

*Figure 9: Navegador Tor*; conectado con éxito a la red de Tor

Ahora puede explorar la web con la protección de la *Red de Tor*.

**Nota**: Cada vez que quiera ejecutar **Navegador Tor**, se abrirá automáticamente la ventana de **Estado de Tor** (*Figura 8*) antes de iniciar **Navegador Tor** (*Figura 9*). 

<a name="3.2"></a>
## 3.2 Reconfigure el acceso a la red de Tor##

En cualquier paso, si usted necesitara acceder al la red de **Tor** de una forma distinta, por ejemplo, si usted viajara hacia otro país que bloqueara a Tor, puede actualizar la configuración desde el propio navegador. Haga clic en el ícono ![](/sbox/screen/tor-es-1/022.png) y seleccione *Abrir configuración de red*.

![](/sbox/screen/tor-es-1/023.png)

*Figura 10: Opciones del navegador Tor*

Se presentará a continuación una nueva ventana (*Figura 11*) que le permitirá cambiar la forma en la que el navegador *Tor* accede a Internet. Marque las opciones que desee y cambie la configuración.  Si está de acuerdo con los cambios, presione *Aceptar* y reinicie el navegador **Tor**.


![](/sbox/screen/tor-es-1/025.png)

*Figura 11: Opciones del navegador Tor*


<a name="3.3"></a>
## 3.3 Obtener direcciones de puente de acceso ###

Con el fin de configurar el navegador **Tor** para usar **puentes** de acceso, tendrá que obtener las direcciones de acceso.  Existen dos maneras principales de lograrlo:

**Email**:

Para obtener los puentes vía e-mail, necesitará una cuenta en Gmail o Yahoo.  Envie un e-mail a bridges@bridges.torproject.org y en asunto escriba:*get bridges - obtener puentes*.  Después de unos minutos, recibirá un e-mail con tres puentes enumerados y algunos detalles adicionales.

![](/sbox/screen/tor-es-1/026.png)

*Figura 12: E-mail con puentes enumerados*

**Sitio web**

Si su acceso no está completamente restringido, usted podrá obtener las direcciones de **Puente** desde el sitio web de Tor: [https://bridges.torproject.org/](https://bridges.torproject.org/)

Una vez abierto el sitio web, necesitará realizar los siguientes tres pasos:

-Haga clic en ![](/sbox/screen/tor-es-1/027.png)

-Haga clic en ![](/sbox/screen/tor-es-1/028.png)

-Complete el *captcha* y presione  ![](/sbox/screen/tor-es-1/029.png)

Una vez que haya ingresado el *captcha* correctamente, se le presentarán tres direcciones *Puente*

![](/sbox/screen/tor-es-1/030.png)

*Figura 13: Direcciones puente recibidas a través del sitio web del Proyecto Tor*


**Nota**: La *Base de Datos de direcciones puente* ha sido diseñada para evitar que alguien pueda saber fácilmente todas las direcciones de los puentes. En un primer momento, parece que le dará los mismos puentes cada vez. Sin embargo, luego le dará nuevas direcciones. 

Una vez recibidas las direcciones puente, cópielas en el campo de la ventana como se muestra en la *Figura 7: Pantalla de configuración del Puente Tor* o *Figura 11 Opciones del navegador Tor*.

