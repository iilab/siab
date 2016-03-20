

---

lang: es
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Use COMODO Firewall

---

Lista de secciones en esta página:

- [**4.0 Acceder a las Ventanas de Ajustes de Comportamiento de Firewall y Configuración del Defense+**](#4.0)
- [**4.1 Ventana de Ajustes de Comportamiento del Firewall**](#4.1)
- [**4.2 Ventana de Configuración del Defense+**](#4.2)

-------

<a name="4.0"></a>
## 4.0 Acceder a las Ventanas de Ajustes de Comportamiento del Firewall y y Configuración de Defense+ ##

La interafaz principal de usuario de **COMODO Firewall** está dividida en dos paneles, el panel de *Firewall* y el de *Defense+*.

![](/sbox/screen/comodo-es/80.png)

*Figura 1: Intefaz principal de usuario de COMODO Firewall mostrando los paneles de Firewall y de Defense+*

Las ventanas de  *Ajustes de Comportamiento del Firewall* y de *Configuración de Defense+* pueden ser accesadas **pulsando** ![](/sbox/screen/comodo-es/43.png) en cualquier parte de los paneles para activar sus ventanas y pestañas asociadas.

Alternativamente, puedes acceder a cualquiera de ellas ejecutando los siguientes pasos:

**Paso 1**. **Abre** la interfaz principal de usuario de **COMODO Firewall**.

**Paso 2**. **Pulsa** 

![](/sbox/screen/comodo-es/60.png) o ![](/sbox/screen/comodo-es/81.png)

para activar los paneles de  *Tareas del Firewall* o *Tareas de Defense+* respectivamente.

**Paso 3**. **Pulsa** 

![](/sbox/screen/comodo-es/82.png) o ![](/sbox/screen/comodo-es/83.png)

para activar la pestaña de *Ajustes de Comportamiento del Firewall* o la de *Configuración de Defense+* respectivamente.

**Consejo**: El *Nivel de Seguridad del Firewalll*, *Nivel de Seguridad de Defense+* y  *Nivel de Seguridad del Sandbox* que son descritos en las siguientes secciones pueden ser fácil y eficazmente configurados utilizando el ícono de conectividad de **COMODO Firewall** localizado en la *Bandeja de Sistema*. **Pulsa** en el ícono para activar el menú emergente y el correspondiente submenú como sigue:

![](/sbox/screen/comodo-es/84.png)

*Figura 2: Menú emergente del ícono de conectividad y el submenú del Nivel de Seguridad del Firewalll*

<a name="4.1"></a>
## 4.1 Ventana de Ajustes de Comportamiento del Firewall ##

La ventana de  **Ajustes de Comportamiento del Firewall** te permite personalizar la seguridad del cortafuegos utilizando una diversidad de características y opciones, entre ellas el nivel de seguridad del cortafuegos (firewall), el número y tipo de alertas de seguridad recibidas y el analisis y vigilancia de paquetes.

![](/sbox/screen/comodo-es/44.png)

*Figura 3: Ventana de  Ajustes de Comportamiento del Firewall -Pestaña de Configuración General*

La pestaña de *Configuración General* te permite especificar el nivel de seguridad que consideres apropiado para **COMODO Firewall**. El control deslizante te permite ajustar el nivel de seguridad entre las siguientes opciones.

**Bloquear Todo**: Este modo detiene todo el tráfico relacionado a Internet y anula cualquier configuración y reglas de cortafuegos (firewall) que hayas especificado. Esta opción no generará reglas de tráfico para aplicaciones, ni registrará o 'aprenderá' sus comportamientos.

**Política personalizada**: Este modo aplica *sólo* las políticas de seguridad y de tráfico de red de **COMODO Firewall** definidas por el usuario y que han sido previamente definidas en las ventanas *Firewall Tareas> Políticas de Seguridad de Red* y  *Defense+ Tareas > Políticas de Seguridad del Sistema*.

**Modo Seguro**: Este es el modo por defecto para **COMODO Firewall**, incluyendo las instalaciones de *Defensa Proactiva Óptima* y *Defensa Proactiva Máxima*.

**Consejo**: **COMODO Firewall** mantiene una lista interna de aplicaciones utilizadas comúnmente y de archivos verificados como seguros, y no emite alertas emergentes para estos.

**Advertencia**: Tanto el *Modo de aprendizaje* y el *Modo Desactivado*  no son recomendables por que pueden comprometer la efectividad de **COMODO Firewall** y exponer tu sistema al riesgo de una infección.

<a name="4.2"></a>
### 4.2 Ventana de Configuración del Defense+ ###

**Nota**: Las caracteristicas y opciones descritas en esta seccion requieren un conocimiento profundo de cortafuegos (firewalls) y de temas de seguridad relacionados, y está diseñado en su mayor parte pensando en un usuario **Avanzado**.

**Importante**: Si has elegido las opciones *Firewall con Defensa Proactiva Óptima* como la *Firewall con la Máxima Defensa Proactiva* durante el proceso de instalación del **COMODO Firewall**, el sistema de prevención de intrusión al servidor *Defense+* fue activado automáticamente. Sin embargo, si optaste por *Solo Firewall* el sistema *Defense+* puede ser habilitado manualmente. La característica *Defense+* debe ser habilitada para que varias de las características documentadas aquí puedan funcionar.

*Defense+* de **COMODO Firewall**  es un sistema de prevención de intrusión al servidor. Cualquier computadora conectada a una red esta técnicamente en comunicación con un servidor. El sistema *Defense+* vigila constantemente las actividades de todos los archivos ejecutables que actualmente residen en tu computadora. Un archivo ejecutable es simplemente una aplicación o programa, o una parte si este, se identifica de manera típica pero no exclusiva con las siguientes extensiones de archivo: *.bat*, *.exe*, *.dll*, *.sys*, y otros.

*Defense+* emite advertencias emergentes cada vez que un archivo ejecutable desconocido intenta activarse, y te solicita permitir o bloquear su funcionamiento. Este puede ser importante en situaciones en las que cualquier tipo de software malicioso (malware) intentara instalar aplicaciones o programas para dañar o robar tu información personal, reformatear tu disco duro o tomar control de tu computadora, y utilizarla para propagar software malicioso (malware) o correo comercial no solicitado (spam) - sin tu consentimiento o conocimiento.

### 4.2.1 Configuración del Defense+ - Pestaña de Configuración General ###

Para habilitar manualmente el sistema *Defense+* y activar la ventana de *Configuración de Defense+* ejecuta los siguientes pasos:

**Paso 1**. **Pulsa** la pestaña de *Defense+* en la interfaz principal de usuario de **COMODO Firewall** y luego **pulsa** ![](/sbox/screen/comodo-es/50.png) para activar la siguiente ventana:

![](/sbox/screen/comodo-es/51.png)

*Figura 6: Ventana de Defense+ mostrando la pestaña de Configuracion General por defecto*

**Paso 2**. **Mueve** el control deslizante hacia el indicador de *Modo Seguro* y luego **pulsa** ![](/sbox/screen/comodo-es/06.png) para habilitar el sistema *Defense+* como está mostrado arriba en la *Figura 6*.

El *Nivel de Seguridad de Defense+* se asemeja al de *Ajustes de Comportamiento del Firewall* el cual ofrece opciones similares, y te permite utilizar un control deslizante para elegir el nivel óptimo de protección de intrusión al servidor para tu sistema.

**Modo Paranoico**: Este modo ofrece el mayor nivel disponible de seguridad, y vigila todos y cada uno de los archivos ejecutables aparte de aquellos que has especificado como seguros, incluyendo aquellos que están en la lista de *Proveedores de Software Confiable*. Este genera un gran número de alertas de seguridad, y la actividad del sistema se filtra a través de tus parámetros de configuración.

**Modo Seguro**: Este modo automáticamente 'aprenderá' los comportamientos de distintas aplicaciones ejecutables, al tiempo de vigilar la actividad crítica del sistema. Cada aplicación no certificada generará una *Alerta de Seguridad* cuando se ejecute. Este modo es el más recomendado para la mayoría de los usuarios.

- La opción *Bloquear todas las solícitudes desconocidas si la aplicación esta cerrada* automáticamente bloquea todas las solicitudes de aplicaciones y programas desconocidos y de aquellos que no especificaste en tu *Política de Seguridad del Sistema*.

- La opción *Desactivar el Defense+ permanentemente (Requiere reiniciar el sistema)* te permite desactivar manualmente el sistema de prevención de intrusión a servidor *Defense+*. Esta opción, en general, no se recomienda.

### 4.2.2 Configuración del Defense+ - Pestaña de Ajustes de Control de Ejecución ###

La pestaña de *Ajustes de Control de Ejecución* limita el grado en que un archivo sospechoso o desconocido puede tener acceso a los recursos de tu sistema y ejecutarse, y los remite para su análisis.

![](/sbox/screen/comodo-es/54.png)

*Figura 7: Pestaña de Ajustes de Control de Ejecución de Defense+*

**Consejo**: Los usuarios **Avanzados** pueden crear exclusiones a las tareas anteriormente mencionadas al pulsar ![](/sbox/screen/comodo-es/55.png) para activar el panel de *Exclusiones*, y explorar en busca de o seleccionar distintos procesos o programas para su exclusión.

**Nota**: Se recomienda enfáticamente a los usuarios **Experimentados** y **Avanzados** **pulsar** ![](/sbox/screen/comodo-es/47.png) para acceder a la amplia ayuda en línea de **COMODO** relativa a las pestañas de *Ajustes de Control de Ejecución*, *Configuración del Sandbox* y *Ajustes de Monitoreo*. Opcionalmente, puedes dirigirte a **http://help.comodo.com/topic-72-1-155-1074-Introduction-to-Comodo-Internet-Security.html** para escoger de una lista de tópicos de ayuda en linea.

