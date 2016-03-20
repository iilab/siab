

---

lang: es
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: How to Install and Launch COMODO Firewall 

---

Lista de secciones en esta pagina:

- [**2.0 Vista General de la Instalación de COMODO Firewall**](#2.0)
- [**2.1 Deshabilitar el Cortafuegos de Windows**](#2.1)
- [**2.2 Instalar COMODO Firewall**](#2.2)

-------

<a name="2.0"></a>
## 2.0 Vista general de la instalación de COMODO Firewall ##

La instalación de **COMODO Firewall** es un procedimiento relativamente sencillo y rápido, dividido en dos etapas: La primera implica deshabilitar manualmente el **Cortafuegos de Windows**, y la segunda es la instalación propiamente dicha del **COMODO Firewall**.

Idealmente solo deberías utilizar un programa cortafuegos en el sistema de tu computador en cualquier momento. Si estás usando algún otro cortafuegos en tu computador debería ser desinstalado antes de instalar **COMODO Firewall**, de esta manera evitarás potenciales conflictos entre programas de similar naturaleza.

<a name="2.1"></a>
## 2.1 Deshabilitar el Firewall de Windows ##

Para deshabilitar el Programa **Firewall de Windows**, ejecuta los siguientes pasos:

**Paso 1**: **Selecciona  Inicio > Panel de Control > Firewall de Windows** para activar la pantalla de **Firewall de Windows**.

**Paso 2**. **Habilita** la opción *Desactivado (no se recomienda)* para deshabilitar el **Firewall de Windows** como se muestra en la  *Figura 1*:

![](/sbox/screen/comodo-es/01.png)

*Figura 1. Firewall de Windows con la opción Desactivado habilitada*

**Paso 3**. **Pulsa** ![](/sbox/screen/comodo-es/02.png) para terminar de deshabilitar el *Firewall de Windows*.

<a name="2.2"></a>
## 2.2 Instalar COMODO Firewall ##

**Nota**: **COMODO Firewall** no desinstala automáticamente versiones antiguas o previamente existentes de su software. Estas deben ser desinstaladas manualmente antes de empezar a instalar la versión más reciente.

Para comenzar a instalar **COMODO Firewall**, ejecuta los siguientes pasos:

**Paso 1**. **Pulsa dos veces** ![](/sbox/screen/comodo-es/03.png) para empezar el proceso de instalación. La ventana de dialogo *Advertencia de seguridad - Abrir archivo* puede aparecer. Si así ocurre, **pulsa** en ![](/sbox/screen/comodo-es/04.png) para activar la siguiente ventana de confirmación:

![](/sbox/screen/comodo-es/05.png)

*Figura 2: La ventana de selección de idioma*

**Paso 2**. **Pulsa** ![](/sbox/screen/comodo-es/06.png) para activar el *Acuerdo de licencia para usuario final*. Por favor lee el *Acuerdo de licencia para usuario final* antes de proceder con el resto del proceso de instalación, y luego **pulsa** ![](/sbox/screen/comodo-es/07.png) para activar la pantalla de *Registro Gratuito*.

**Paso 3**: **No** introduzcas tu dirección de correo electrónico en el campo de texto *Ingresa tu dirección de correo electrónico(opcional)*; simplemente **pulsa** ![](/sbox/screen/comodo-es/09.png) para activar la pantalla de *Extrayendo paquetes*.

Después de terminado el proceso de extracción, aparecerá el *Asistente de folder de destino del cortafuegos*.

**Paso 4**. **Pulsa** ![](/sbox/screen/comodo-es/09.png) para aceptar la ruta por defecto y activar la pantalla de *Selección de nivel de seguidad del Firewall (cortafuegos)*, y entonces elige la opción *Solo el Firewall* como sigue:

![](/sbox/screen/comodo-es/11.png)

*Figura 3: Pantalla de Selección del nivel de seguridad del Firewall (cortafuegos)*

**Definición de las Opciones del Nivel de Seguridad del Firewall (cortafuegos)**

Cada opción de nivel de seguridad del cortafuegos satisface a usuarios de diferentes niveles. Cada opción equilibra diferentes tipos de protección con la complejidad de su uso, asi como el número de alertas de seguridad que podrías recibir. Una breve descripción de cada nivel de seguridad se presenta a continuación:

Modo **Solo el Firewall**: Esta opción te permite ejecutar **COMODO Firewall** sin que se habilite el atributo o la característica *Defense+*. Este modo identifica fácilmente aplicaciones populares las cuales son relativamente seguras (como navegadores web y clientes de correo electrónico), reduciendo el número de alertas de seguridad que podrías recibir. Este ofrece explicaciones generales de porque una pantalla de alerta particular ha aparecido. Además, las acciones a ser emprendidas son relativamente simples.

Modo **Firewall con Defensa Proactiva Óptima**: Esta opción combina la sólida protección del modo *Solo el Firewall* con la de la característica *Defense+* habílitada. *Defense+* ofrece una protección activa contra el software malicioso (malware) diseñado para evadir distintos cortafuegos. Las *Alertas de COMODO Firewall* ofrecen explicaciones más profundas sobre por qué cierta aplicación o solicitud esta siendo bloqueada, y tienes la opción de aislar parcialmente o 'aislar el proceso (sandboxing)' de un archivo o programa sospechoso.

Modo **Firewall con la Máxima Defensa Proactiva**: Esta opción combina la seguridad de la opción *Firewall con Defensa Proactiva Óptima* con una protección 'a prueba de filtraciones (anti-leak)' contra amenazas de seguiridad más 'pasivas', por ejemplo, detalles sobre puertos abiertos en tu computadora que sean enviados a través de la Internet. La característica u opción de asilamiento de proceso (sandbox) esta completamente automátizada.

**Paso 6**. **Pulsa** ![](/sbox/screen/comodo-es/09.png) para activar la pantalla de *Configuraciones del COMODO SecureDNS*, con la opción *Deseo utilizar los servidores de COMODO SecureDNS* habilitada como sigue:

![](/sbox/screen/comodo-es/12.png)

*Figura 4: Pantalla de Configuraciones del COMODO SecureDNS*

**Importante**: A pesar que ningún servidor del **Sistema de Nombres de Dominio** (**DNS**) es completamente seguro, las ventajas de usar los  **Servidores COMODO Secure DNS** superan las desventajas. Estos ofrecen una mayor protección ante el *redireccionamiento malicioso (pharming)* y la *suplantación de identidad (phishing)*, que son dos métodos populares para 'tomar control' o redireccionar tu computadora a un sitio peligroso u hostil. Los **Servidores COMODO Secure DNS** pueden también protegerte de la injerencia gubernamental, por ser fácil de configurar durante el proceso de instalación, y al facilitar un acceso seguro a los sitios web que están registrados con **COMODO**. Por ejemplo, la escritura errónea de una URL activará un mensaje de los **Servidores COMODO Secure DNS** parecido al siguiente:

![](/sbox/screen/comodo-es/126.png)

*Figura 5:  Ejemplo típico de una notificación del Servidor COMODO Secure DNS*

**Paso 7**. **Pulsa** ![](/sbox/screen/comodo-es/09.png) para activar la pantalla de *Listo para instalar COMODO Firewall*, luego **pulsa** ![](/sbox/screen/comodo-es/13.png) para empezar el proceso de instalación,y activar la pantalla *COMODO Instalación de Firewall*. Una vez compleatado el proceso de instalación, este activará la pantalla *Completado el Asistente de Configuración de COMODO Firewall*.

**Paso 8**. **Pulsa** ![](/sbox/screen/comodo-es/14.png) para activar la pantalla de confirmación *Finalizar*, y luego **pulsa** ![](/sbox/screen/comodo-es/14.png) para activar el siguiente dialogo de confirmación:

![](/sbox/screen/comodo-es/15.png)

*Figura 6: Diálogo de confirmación de Instalación de Firewall*

**Paso 9**. **Pulsa** ![](/sbox/screen/comodo-es/16.png) para reiniciar tu computadora, y completar el proceso de instalación de **COMODO Firewall**.

Después del reincio de tu computadora, la pantalla *¡Nueva red privada detectada!* aparecerá como sigue:

![](/sbox/screen/comodo-es/17.png)

*Figura 7: Pantalla del COMODO Firewall de ¡Se ha detectado una Nueva Red Privada!*

**Consejo**: Si estás trabajando en un entorno LAN, simplemente marca la opción *Deseo estar accesible a las otras PCs en esta red* para habilitar el uso compartido de archivos/carpetas/impresoras y/o la conexión a Internet.

**Paso 10**. **Ingresa** un nombre en el campo de texto de *Dar un nombre a esta red* o simplemente acepta el nombre por defecto propuesto como se muestra en la *Figura 7*. Mantén deshabilitadas las opciones listadas bajo el *Paso 2 - Decidir si confia en las otras PCs en esta red*, y luego **pulsa** ![](/sbox/screen/comodo-es/06.png) para completar la instalación.

El ícono de escritorio de  **COMODO Firewall** y el ícono de conectividad de **COMODO Firewall** aparecerán simultaneamente con la *Figura 7*. Antes que te conectes a la internet, el ícono de conectividad aparecerá en la *Bandeja del Sistema* como sigue:

![](/sbox/screen/comodo-es/18.png)

*Figura 8: El ícono de conectividad de COMODO Firewall enmarcado en negro en la Bandeja de Sistema*

Ponerse en linea o activar programas dependientes de la red (por ejemplo, navegadores web) desencadenarán una serie de puntas de flecha anaranjadas dirigidas hacia abajo y/o otras de color verde claro dirigidas hacia arriba, estas indican solicitudes de conexión a Internet de ingreso y de salida, estas se representan como sigue:

![](/sbox/screen/comodo-es/19.png)

*Figura 9: Ícono de conectividad en acción de COMODO Firewall*

Después de unos momentos de funcionamiento del **COMODO Firewall**, el mensaje emergente de *COMODO Centro de mensajes* aparece como se muestra:

![](/sbox/screen/comodo-es/20.png)

*Figura 10: Mensaje emergente del *COMODO Centro de Mensajes*

**Nota**: **Pulsa** en el hipervínculo *Aprende más* para ser direccionado a los foros de ayuda dirigidos a la comunidad de **COMODO**.

**Consejo**: **Pulsa con el botón derecho del ratón** en el ícono de conectividad de **COMODO Firewall** en la *Bandeja de Sistema* (como se muestra en la *Figura 10*) para activar el siguiente menú emergente y sus submenúes asociados como sigue:

![](/sbox/screen/comodo-es/127.png)

*Figura 11: Menú y submenúes de Configuración del ícono de conectividad*

El menú del ícono de conectividad te permite cambiar los productos de **COMODO Firewall** que estás utilizando. La **sSelección** del elemento *Configuración* activa el submenú *Administrar Mi Configuración* donde puedes **selecionar** tanto  *COMODO - Proactive Security (Seguridad Proactiva)* o *COMODO - Internet Security (Seguridad en Internet)* para habilitar la opción o caracteristica de aislamiento de procesos (sandboxing).

Adicionalmente,  cada producto puede tener su nivel de seguridad ajustado en el menú del ícono de conectividad como se muestra; estos niveles de seguridad se discuten en mayor detalle en las secciones **4.1 Ventana de Ajustes del Comportamiento del Firewall** y **4.2 Ventana de Configuración del Defense+**

![](/sbox/screen/comodo-es/128.png)

*Figura 12: Submenú del Nivel de Seguridad del Firewall del ícono de conectividad*

Lista de secciones en esta página:

- [**3.0 Permitir y Bloquear el Acceso Utilizando el COMODO Firewall**](#3.0)
- [**3.1 Abrir la Interfaz Principal de Usuario de COMODO Firewall**](#3.1)
- [**3.2 Visión General de la Interfaz Principal de Usuario de COMODO Firewall**](#3.2)

-------

<a name="3.0"></a>
## 3.0 Permitir y Bloquear el Acceso Utilizando el COMODO Firewall ##

Un cortafuegos es un programa diseñado para proteger tu computadora de piratas informáticos (hackers) maliciosos y software malicioso (malware). Ambos pueden intentar acceder directamente a tu computadora, o enviar información desde tu computadora a terceros.**Comodo Firewall** debe ser configurado para 'aprender' o registrar que aplicaciones son 'seguras' y permitirles el acceso, al tiempo  de bloquear solicitudes de software inseguro y procesos no autorizados dirigidas a tu sistema. Puede ser necesaria un poco de experiencia para determinar que solicitudes son legítimas y cuales son amenazas.

Cada vez que  **Comodo Firewall** recibe una solicitud de conexión, se activa una ventana emergente *Alerta de Firewall* solicitándote *Permitir* o *Bloquear* el acceso a tu sistema tanto hacia como desde Internet. El ejercicio que sigue, que involucra un programa seguro como **Firefox** te ayudará a familiarizarte con las alertas del cortafuegos como utilizarlas. Aunque a veces se hacen excepciones para solicitudes de navegadores y progrmas de correo electrónico universalmente aceptados, cada vez que se realiza una solicitud de conexiión *Alerta de Firewall* parecida a la siguiente aparece:

![](/sbox/screen/comodo-es/21.png)

*Figura 1: Ejemplo de una Alerta de Firewall de COMODO*

Un cortafuegos es un simple conjunto de reglas para vigilar el tráfico de entrada y salida. Cada vez que pulsas *Permitir* o *Bloquear* el **COMODO Firewall** genera una regla para las solicitudes de conexión acceso a la red de tal proceso o programa. **COMODO Firewall** hace esto para procesos y programas nuevos o no reconocidos, así como para aquellos considerados en la lista de *Proveedores de Software Confiables*, en la pantalla de *Defense+ - Tareas > Política de Seguridad del Sistema*.

**Recuerda mi respuesta**: Esta opción es usada para registrar si has permitido o denegado a un determinado programa el acceso a través de **COMODO Firewall**. Este permitirá o bloqueará automáticamente las solicitudes de conexión de este programa la próxima vez que intente conectarse a tu computadora, de acuerdo a cuál haya sido la opción que especificaste aquí.

**Importante**: Recomendamos enfáticamente deshabilitar la opción  *Recuerda mi Respuesta* cuando estés usando **COMODO Firewall** por primera vez. Decide ya sea permitir o bloquear diostintas solicitudes de conexión, y luego observa cómo o situ decisión afecta el funcionamiento de tu sistema. Habilita la opción *Recuerda mi respuesta* si y *solamente si* estás completamente seguro de tu decisión.

**Consejo**: Ser estricto acerca de limitar el acceso a tu sistema es el mejor enfoque para la seguridad informática. No dudes en bloquear cualquier solicitud sospechosa o no identificable. Si ello causa que un programa normal deje de funcionar correctamente, puedes permitir al proceso que se ejecute la próxima vez que recibas una alerta de cortafuegos (firewall).

**Paso 1**. **Pulsa** ![](/sbox/screen/comodo-es/26.png) para activar la ventana de *Propiedades* para saber más acerca del proceso o programa que solicita acceso, en este caso, **Firefox**:

![](/sbox/screen/comodo-es/27.png)

*Figura 2: Pantalla de propiedades de firefox.exe*

**Paso 2**: **Pulsa** ![](/sbox/screen/comodo-es/02.png) para cerrar la pantalla de *Propiedades* del programa.

**Paso 3**: Si has determinado que una solicitud es insegura, o simplemente tienes dudas sobre esta, a partir de la información mostrada en la pantalla de *Propiedades* del programa, **pulsa** ![](/sbox/screen/comodo-es/29.png) para ordenarle a **COMODO Firewall** que niegue el acceso a tu sistema. O: Si has determinado que un programa legitimo está haciendo una solicitud no maliciosa, basado en la información mostrada en la pantalla de *Propiedades* del programa, entonces **pulsa** ![](/sbox/screen/comodo-es/28.png) para permitirle el acceso a tu sistema.

**Paso 4**. **Pulsa** ![](/sbox/screen/comodo-es/28.png) para permitirle a **Firefox** el acceso a tu sistema a través de **COMODO Firewall**.

**Paso 5**. Dado que **Firefox** es un programa seguro, **habilita** la opción ![](/sbox/screen/comodo-es/30.png) de modo que **COMODO Firewall** permita automáticamente el acceso a tu sistema de **Firefox** la próxima vez.

**Nota**: El botón *Permitir* te permite otorgar manualmente acceso a un proceso o programa caso por caso.

**Consejo**: **Pulsa** ![](/sbox/screen/comodo-es/31.png) para acceder a los amplios archivos de ayuda en línea de **COMODO Firewall**.

Tu capacidad para tomar la decisión correcta de permitir o bloquear mejorará a medida que tengas más confianza y experiencia utilizando el **COMODO Firewall**.

<a name="3.1"></a>
## 3.1 Abrir la Interfaz Principal de Usuario de COMODO Firewall ##

**COMODO Firewall** empezará automáticamente a funcionar después de que lo hayas instalado y hayas reiniciado tu sistema. Este presenta un amplio panel de control con numerosas características y opciones personalizables. Usuarios de nivel **Principiante** aprenderán rapidamente como lidiar con las alertas de seguridad de **COMODO Firewall**, mientras usuarios **Experimentados** y **Avanzados** aprenderán acerca de configuración y gestión más compleja de cortafuegos (firewall).

**Nota**: Todos los ejemplos mostrados aquí son basados en **COMODO Firewall** en el modo **Defensa Proactiva Óptima**. Esto significa que el sistema de prevención de intrusión de servidor *Defense+* está habilitado automáticamente. Si has instalado **COMODO Firewall** usando la opción *Solo el Firewall*, entonces el *Defense+* no estará habilitado.

Para abrir la interfaz principal de usuario de **COMODO Firewall**, ejecuta el siguiente paso:

**Paso 1**. **Selecciona Inicio > Programas > Comodo > Firewall > Comodo Firewall**.

**Nota**: Alternativamente, puedes **pulsar dos veces** en el ícono de escritorio, o **pulsar dos veces** en el ícono de **COMODO Firewall** en la *Bandeja de Sistema* para abrir la interfaz principal de usuario. Aparte de ello, puedes **pulsar con el botón derecho del ratón** en el ícono de **COMODO Firewall** para activar su menú emergente, y luego **seleccionar** *Abrir...* como se muestra a continuación:

![](/sbox/screen/comodo-es/35.png)

*Figura 3: Menú emergente del ícono de conectividad de COMODO Firewall*

![](/sbox/screen/comodo-es/36.png)

*Figura 4: Interfaz de usuario de COMODO Firewall en el modo por defecto Resumen*

<a name="3.2"></a>
## 3.2 Visión General de la Interfaz Principal de usuario de COMODO Firewall ##

El panel *Firewall* muestra un resumen claro y conciso de solicitudes de ingreso y salida de procesos y programas que intentan hacerlo a través de **COMODO Firewall**. Por lo general, existen más solicitudes de salida que de ingreso. El modo de operación por defecto es el *Modo Seguro*, los diferentes modos de operación serán esbozados más adelante en esta sección. *Tráfico* muestra los diferentes procesos y programas en operación, y el número de solicitudes hechas expresadas en porcentajes.

**Pulsa**![](/sbox/screen/comodo-es/37.png) para activar el resumen detallado correspondiente de las solicitudes de salida *en un momento dado* como sigue:

![](/sbox/screen/comodo-es/38.png)

*Figura 5: Ejemplo de la ventana de Conexiones Activas mostrando detalles del tráfico de internet*

**Pulsa** ![](/sbox/screen/comodo-es/39.png) para activar una ventana de *Conexiones Activas* para las solicitudes de tráfico entrante *en un momento determinado*.

**Consejo**: **Pulsa** ![](/sbox/screen/comodo-es/40.png) para detener todas las solicitudes entrantes y salientes si tu servicio de Internet subitamente se hace lento o se detiene y tienes razones para sospechar que un proceso o programa malicioso está descargandose a si mismo o está en operación. Hacer esto, inmediatamente cambia el modo de operación del Firewall a ![](/sbox/screen/comodo-es/41.png).
Revisa el resumen detallado en la ventana de *Conexiones Activas* para identificar la posible fuente del problema.

Una vez que estés seguro que has resuelto el problema exitosamente, **pulsa** ![](/sbox/screen/comodo-es/42.png) para comenzar a procesar solicitudes entrantes y salientes al **COMODO Firewall** y regresar a ![](/sbox/screen/comodo-es/43.png) como es usual.

### 3.2.1 Íconos de Estado de COMODO Firewall ###

Tanto **COMODO Firewall** como **Defense+** trabajan juntos; si ambos programas están ejecutandose, el indicador de la izquierda de la interfaz principal de usuario aparece como sigue:

![](/sbox/screen/comodo-es/69.png)

*Figura 6: Ícono de estado de COMODO Firewall en verde*

Si uno de los programas está deshabilitado, el ícono de estado indicará que esta deshabilitado ya sea el *cortafuegos (firewall)* o el componente de protección proactiva como se muestra:

![](/sbox/screen/comodo-es/70.png)

*Figura 7: Ícono de estado deshabilitado de COMODO Firewall en amarillo*

Sin embargo, si ambos programas han sido deshabilitados, el ícono de estado aparecerá como sigue:

![](/sbox/screen/comodo-es/71.png)

*Figura 8: Ícono de estado de protección múltiple deshabilitada de COMODO Firewall*

En ese caso, **pulsa** ![](/sbox/screen/comodo-es/72.png) para habilitar la protección correspondiente.



