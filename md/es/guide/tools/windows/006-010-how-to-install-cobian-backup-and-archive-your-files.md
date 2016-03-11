

---

lang: es
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: How to Install Cobian Backup and Archive Your Files

---

Lista de secciones en esta página:

- [**2.0 Cómo instalar Cobian Backup**](#2.0)
- [**2.1 Cómo hacer una copia de seguridad de tus directorios y archivos**](#2.1)
- [**2.2 Cómo crear una copia de seguridad**](#2.2)
- [**2.3 Cómo programar la hora de tu copia de seguridad**](#2.3)

-------

<a name="2.0"></a>
## 2.0 Cómo instalar Cobian Backup ##

**Nota de instalación**: Antes de iniciar la instalación, verifica que tienes las dos últimas versiones de ***Microsoft Windows Installer* y *Microsoft.NET Framework***.

Instalar **Cobian Backup** es un procedimiento relativamente rápido y sencillo. Para empezar la instalación de **Cobian Backup**, debes realizar los siguientes pasos:

**Paso 1**. **Haz doble clic en** ![](/sbox/screen/cobian-es/01.png); es posible que aparezca el siguiente cuadro de diálogo *Abrir archivo – Aviso de seguridad*. Si esto ocurre, **haz clic en** ![](/sbox/screen/cobian-es/02.png) para activar la barra de estado azul claro *Extrayendo la fuente*, seguido después por la siguiente pantalla:

![](/sbox/screen/cobian-es/03.png)

*Figura 1: Configuración de Cobian. Selecciona una ventana de Idioma*

**Paso 2**. **Haz clic en** ![](/sbox/screen/cobian-es/04.png) para activar la pantalla *Lee y acepta el acuerdo de licencia*; **selecciona** la opción *Acepto*, y entonces **haz clic en** ![](/sbox/screen/cobian-es/04.png) de nuevo para activar la siguiente pantalla:

![](/sbox/screen/cobian-es/05.png)

*Figura 2: Ventana de selección de un directorio de instalación*

**Paso 3**. **Haz clic en** ![](/sbox/screen/cobian-es/04.png) para activar la siguiente pantalla:

![](/sbox/screen/cobian-es/06.png)

*Figura 3: La ventana de Tipo de instalación y Opciones de servicio*

**Paso 4**. **Selecciona** la opción *Usar la cuenta de LocalSystem* en el panel *Opciones de servicio*, de manera que se parezca a la *Figura 3* que se muestra. 

**Importante**: Esta opción permite que **Cobian Backup** funcione silenciosamente de fondo constantemente, para que tus copias de seguridad funcionen según lo programado.

**Paso 5**. **Haz clic en** ![](/sbox/screen/cobian-es/04.png) para activar el siguiente mensaje emergente:

![](/sbox/screen/cobian-es/07.png)

*Figura 4: El mensaje emergente Cobian Backup 10* 

**Paso 6**. **Haz clic en** ![](/sbox/screen/cobian-es/08.png) para pasar a la siguiente pantalla de instalación, y vuelve a hacer **clic en** ![](/sbox/screen/cobian-es/04.png) para continuar con el proceso de instalación.

**Paso 7**. **Haz clic en** ![](/sbox/screen/cobian-es/09.png) para completar el proceso de instalación. Una vez finalizado, el icono de **Cobian Backup** aparecerá en la **Bandeja de sistema de Windows**: ![](/sbox/screen/cobian-es/10.png)

<a name="2.1"></a>
## 2.1 Cómo hacer una copia de seguridad de tus directorios y archivos ##

En esta sección aprenderás a crear una sencilla copia de seguridad o archivo de una carpeta o archivo específicos. **Cobian Backup** utiliza una *copia de seguridad* que puede ser configurada para incluir un grupo concreto de archivos o carpetas. Es posible configurar la copia de seguridad para que se realice en un día y hora determinados.

Para crear una nueva tarea de respaldo, sigue los siguientes pasos:

**Paso 1**. **Haz clic en** ![](/sbox/screen/cobian-es/11.png) para crear una nueva tarea de respaldo y activar la ventana *Tarea nueva*:

![](/sbox/screen/cobian-es/12.png)

*Figura 2: El panel Tarea nueva*

La barra lateral izquierda enumera una serie de pestañas y sus pantallas asociadas – usadas para configurar diferentes opciones de respaldo y parámetros – se muestran en el panel derecho. Todas las opciones de la pestaña *General* se describen abajo:

### 2.1.1 Descripción de opciones ###

*Nombre de la tarea*: El campo de texto *Nombre la tarea* permite introducir un nombre para la tarea de respaldo. Utiliza un nombre asociado con la tarea de respaldo. Por ejemplo, si la copia de seguridad contiene archivos de vídeo, podrías llamarle *Copia de seguridad de vídeos*.

*Inactivo*: *Debes* dejar esta opción sin marcar. 

**Aviso**: Habilitar la opción *Inactivo* anulará el resto de opciones, e impedirá que se realice la tarea de respaldo. 

*Incluir subdirectorios*: Esta opción te permitirá incluir todos los subdirectorios/carpetas dentro del directorio/carpeta seleccionados para la copia de seguridad. Este es un método eficaz para hacer una copia de seguridad de un gran número de carpetas y archivos. Por ejemplo, si seleccionas la carpeta *Mis documentos* y habilitas esta opción, todos los archivos y carpetas en *Mis documentos* se incluirán en la copia de seguridad.

*Crear copias de seguridad separadas usando fechas*: Esta opción te permitirá especificar que la fecha y la hora de la tarea de respaldo será incluida automáticamente en el nombre de la carpeta que contenga la copia de seguridad. Esta es una buena opción, ya que te permitirá identificar fácilmente cuándo se realizó la tarea de seguridad.

*Usar lógica de atributos*: Esta opción sólo es importante cuando escojas realizar una copia de seguridad incremental o diferencial (ver a continuación). Los atributos de archivo contienen información sobre el propio archivo.

**Nota**: La siguiente opción solo está disponible para versiones recientes de **Windows OS**, incluida **Windows XP**.

*Usar Copias ocultas (Volume shadow copy)*: Esta opción te permitirá hacer copias de seguridad de archivos bloqueados.

**Cobian Backup** verifica esta información para determinar si ha habido un cambio en el archivo original desde la última copia de seguridad realizada. Si después realizas una copia de seguridad *Diferencial* o *Incremental*, se actualizará el archivo.

**Nota**: Sólo podrás realizar una copia de seguridad completa o ‘simulada’ si *deshabilitas esta opción* (la copia de seguridad simulada se explica a continuación).

### 2.1.2 Descripción de los tipos de copia de seguridad ###

*Completa*: Esta opción indica que *cada* archivo de la localización de origen se copiará en el directorio de tu copia de seguridad. Si has habilitado la opción *Crear copias de seguridad separadas usando marcas de tiempo*, tendrás diversas copias del mismo archivo original (identificadas con la hora y la fecha de la copia de seguridad en el título de la carpeta). Si no, **Cobian Backup** sobrescribirá la versión anterior (si la hubiere).

*Incremental*: Esta opción permitirá al programa verificar si los archivos seleccionados para la copia de seguridad han cambiado con respecto a la última copia de seguridad realizada. Si no ha habido cambio, se omitirá durante la tarea de respaldo, guardando la hora de la copia de seguridad. Se ha de marcar la opción *Usar lógica de atributos* para poder realizar este tipo de copia de seguridad.

*Diferencial*: El programa comprobará si el archivo original ha cambiado desde la última copia de seguridad *completa*. Si no necesita copiar este archivo, se omitirá, guardando la hora de la copia de seguridad. Si has realizado previamente una copia de los mismos archivos, puedes continuar hacienda la copia de seguridad usando el método Diferencial.

*Simulada*: Puedes usar esta opción para que tu ordenador abra o cierre programas en momentos determinados. Esta es una opción avanzada que no es necesaria para realizar la copia de seguridad básica.

**Paso 2**. **Haz clic en** en ![](/sbox/screen/cobian-es/13.png) para confirmar tus opciones de búsqueda y parámetros para la tarea de respaldo.

<a name="2.2"></a>
## 2.2 Cómo crear una Copia de seguridad ##

Para empezar a crear una copia de seguridad, sigue los siguientes pasos:

**Paso 1**. **Haz clic** ![](/sbox/screen/cobian-es/14.png) en la barra lateral izquierda de la ventana *Tarea nueva* para desplegar una versión en *blanco* de la siguiente pantalla:

![](/sbox/screen/cobian-es/15.png)

*Figura 3: La ventana Tarea nueva (MiCopia) mostrando los paneles de Origen y Destino*

**Paso 2**. **Selecciona** los archivos que quieras copiar. (En la *Figura 3* más arriba, la carpeta *Mis documentos* está seleccionada.)

**Paso 3**. **Haz clic** ![](/sbox/screen/cobian-es/16.png) en el panel *Origen* para activar el siguiente menú:

![](/sbox/screen/cobian-es/17.png)

*Figura 4: El panel Origen – Menú del botón Añadir*

**Paso 4**. **Selecciona** *Directorio* si quieres realizar una copia de seguridad de un directorio entero, y *Archivos* para hacerla de archivos individuales. Para especificar archivos individuales o directorios de los que quieras hacer una copia de respaldo, selecciona *Manual*, y escribe la dirección del archivo y directorio para la copia.

**Nota**: Puedes añadir tantos archivos o directorios como quieras. Si deseas realizar una copia de archivos que se encuentran en tu servidor **FTP**, elige la opción *Página FTP* (necesitarás los datos de acceso al servidor pertinentes).

Cuando hayas seleccionado los archivos y/o carpetas, estos aparecerán en la pestaña *Origen*. Como puedes ver en la *Figura 3*, se muestra la carpeta *Mis documentos*, lo que significa que esa carpeta se incluye en la tarea de respaldo.

El panel *Destino* especifica dónde se guarda la copia de seguridad.

**Paso 5**. **Haz clic** ![](/sbox/screen/cobian-es/16.png) en el *panel de Destino* para activar el siguiente menú:

![](/sbox/screen/cobian-es/18.png)

*Figura 5: El panel Origen –  Menú del botón Añadir*

**Paso 6**. **Selecciona** *Directorio* para abrir una ventana de navegación donde seleccionar la carpeta de destino de tu copia de seguridad.

**Nota**: Si deseas crear varias versiones de tu copia, deberás seleccionar diversas carpetas. Si has seleccionado la opción *Manual*, tendrás que escribir la dirección completa de dónde quieres guardar la copia. Para guardar tus archivos en un servidor remoto de Internet, **selecciona** la opción *página FTP* (necesitarás tener los datos de acceso al servidor pertinentes).

La pantalla deberá parecerse al ejemplo anterior con archivo(s) y carpeta(s) en Origen y carpeta(s) en Destino. ¡Pero no hagas clic en Ok aún! Todavía necesitas programar el horario de tu tarea de respaldo.

<a name="2.3"></a>
## 2.3 Cómo programar el horario de tu tarea de respaldo ##

Para que tu tarea de respaldo funcione automáticamente, tendrás que rellenar la sección *Horario*. Esta sección te permitirá concretar cuándo quieres que se realice la tarea de respaldo.

Para configurar las opciones de horario, sigue los siguientes pasos:

**Paso 1**. **Selecciona** ![](/sbox/screen/cobian-es/19.png) de la barra lateral izquierda para activar el siguiente panel:

![](/sbox/screen/cobian-es/20.png)

*Figura 6: El panel Tipo de Horario dentro del panel Propiedades de MiCopia*

Las opciones de *Tipo de horario* se listan en el menú desplegable, descritas a continuación:

*Una vez*: La copia de seguridad se realizará sólo una vez en la fecha y hora programadas en el área *Fecha/Hora*.

*Diaria*: La copia de seguridad se realizará cada día a la hora programada en el área *Fecha/Hora*.

*Semanal*: La copia de seguridad se realizará en los días de la semana señalados. En el ejemplo anterior, la copia se realiza los lunes. También puedes seleccionar otros días. La copia de seguridad se realizará en todos los días seleccionados a la hora programada en el área *Fecha/Hora*. 

*Mensual*: La copia de seguridad se realizará en los días especificados en la caja Días del mes a la hora programada en el área *Fecha/Hora*.

*Anual*: La copia de seguridad se realizará en los días especificados en la caja Días del mes, en el mes señalado y la hora programados en el área *Fecha/Hora*.

*Temporizador*: La copia de seguridad se hará repetidamente en intervalos programados en la caja de diálogo Temporizador en el área *Fecha/Hora*.

*Manual*: Tendrás que realizar la copia de seguridad tú mismo desde la ventana principal del programa.

**Paso 2**. **Haz clic en** ![](/sbox/screen/cobian-es/13.png) para confirmar las opciones y la configuración del horario de la copia de seguridad como se indica a continuación:

![](/sbox/screen/cobian-es/21.png)

*Figura 7: La ventana Tarea nueva mostrando un panel Horario ya configurado*

Una vez hayas decidido el horario de la copia de seguridad, ya has completado el paso final. La copia de seguridad se activará en las carpetas programadas de acuerdo con el horario escogido. 

