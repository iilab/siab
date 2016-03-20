

---

lang: es
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: How to Install and Configure Eraser

---

Lista de sectiones en esta página:

- [**2.0 Instalar Eraser**](#2.0)
- [**2.1 Configurar Eraser**](#2.1)

-------

<a name="2.0"></a>
## 2.0 Instalar Eraser ##

**Nota de Instalación**: Antes de iniciar el proceso de instalación, verifica que tienes tanto la última versión del **Microsoft Windows Installer** y del **Microsoft.NET Framework**. 

El instalar **Eraser** es un proceso fácil y rápido. Para empezar a instalar **Eraser**, ejecuta los siguientes pasos:

Como se describe en la Guía Paso a Paso capitulo [**6. Destruir información sensible**](/es/chapter-6), **Eraser** limpia los datos en tu disco duro al sobreescribirlo con información aleatoria. Cuanto mñás veces sobreescribas los datos, menos probable es que este pueda ser recuperado.

**Paso 1**. **Pulsa dos veces** ![](/sbox/screen/eraser-en/01.png); puede aparecer el cuadro de diálogo *Abrir Archivo - Advertencia de Seguridad*. Si así ocurre, **pulsa** ![](/sbox/screen/eraser-en/02.png) para activar el *InstallAware Wizard (Asistente de InstallAware)*; después de unos momentos, aparecerá la pantalla de *Welcome to the InstallAware Wizard for Eraser (Bienvenido al Asistente de InstallAware para Eraser)*.

**Paso 2**. **Pulsa** ![](/sbox/screen/eraser-en/03.png) para activar la pantalla del *License Agreement (Acuerdo de Licencia)*, y luego **pulsa** sobre el casillero para habilitar la opción de *I accept the terms of the license agreement (Acepto los terminos del Acuerdo de Licencia)*, y luego **pulsa** ![](/sbox/screen/eraser-en/03.png) nuevamente para activar la pantalla de *Important Information (Información Importante)*.

**Paso 3**. **Pulsa** ![](/sbox/screen/eraser-en/03.png) después de leer los contenidos mostrados en la ventana desplazable para activar la pantalla de *Destination Folder (Carpeta de Destino)* y luego **pulsa** ![](/sbox/screen/eraser-en/03.png) nuevamente.

**Paso 4**. **Pulsa** ![](/sbox/screen/eraser-en/03.png) para activar la siguiente pantalla:

![](/sbox/screen/eraser-en/04.png)

*Figura 1: Pantalla de Select Program Folder (Selección de la Carpeta del Programa)*

**Paso 5**. **Habilita** la opción *Only for me (current user) (Sólo para mi (usuario actual))* para garantizar que sólo tú estas permitido de utilizar **Eraser**, y luego **pulsa** ![](/sbox/screen/eraser-en/03.png) para activar la pantalla de *Completar el Asistente de InstallAware para Eraser (Completing the InstallAware Wizard for Eraser)*.

**Paso 6**. **Pulsa** ![](/sbox/screen/eraser-en/03.png) y luego **pulsa** ![](/sbox/screen/eraser-en/05.png) para completar el proceso de instalación, y luego ejecuta **Eraser** como se muestra:

![](/sbox/screen/eraser-en/06.png)

*Figura 2: Interfaz de usuario principal de (Eraser main user interface)*

<a name="2.1"></a>
## 2.1 Configurar Eraser ##

**Nota**: Se recomienda que sobreescribas los datos al menos unas tres veces.

**Consejo**: Cada sobreescritura o *pass (pasada)* toma tiempo y por tanto, cuanto más pasadas realices, mayor será el tiempo que dure el proceso de eliminación. Esto se notará especialmente cuando se este eliminando grandes archivos, o cuando se este limpiando espacio libre.

El número de pasadas puede ser fijado al acceder al menú de *Preferences: Erasing(Preferencias: Eliminar)*.

**Paso 1**. **Selecciona > Edit (Editar) > Preferences (Preferencias) > Erasing... (Eliminar)** como se muestra: 

![](/sbox/screen/eraser-en/07.png)

*Figura 3: Pantalla de Eraser [On-Demand (A-Pedido)] mostrando las opciones del menú de Editar*

*La pantalla de Preferences: Erasing (Preferencias: Eliminar)  aparece como se muestra a continuación:*

![](/sbox/screen/eraser-en/08.png)

*Figura 4: Pantalla de (Eraser Preferences: Erasing)*

Pantalla de *Preferencias: Borrando* describe cómo deben ser sobrescritos los archivos.

*Description (Descripción)*: Esta columna lista el nombre del procedimiento de sobrescritura.

*Passes (Pasadas)*: Esta columna lista cuantas veces serán sobrescritos los datos.

En este ejemplo, sobrescribiremos nuestros datos utilizando el método *Pseudorandom Data*. Por defecto, sólo se realiza una pasada cuando se utiliza esta opción. Sin embargo, para una mayor seguridad incrementaremos el número de pasadas.

**Paso 2**. **Selecciona** la opción *# 4 Pseudorandom Data* como se muestra en la *Figura 2*.

**Paso 3**. **Pulsa** ![](/sbox/screen/eraser-en/09.png) para activar la pantalla de *Passes (Pasadas)* como se muestra a continuación:

![](/sbox/screen/eraser-en/10.png)

*Figura 3: Pantalla de Eraser Passes (Pasadas de Eraser)*

**Paso 4**. **Fija** el número de pasadas entre tres y siete (recuerda el intercambio entre tiempo/seguridad).

**Paso 5**. **Pulsa** ![](/sbox/screen/eraser-en/11.png) para regresar a la pantalla de *Passes (Pasadas)*.

\# 4 Pseudorandom Data debe parecerse a la siguiente:

![](/sbox/screen/eraser-en/12.png)

*Figura 4: Pantalla de Borrado de Eraser con el panel mostrando seleccionada a la opción 4*

**Consejo**: Asegúrate que las casillas de *Cluster Tip Area (Área Extrema de Sectores Consecutivos de Disco)* y la de *Alternate Data Streams (Flujo de Datos Alternos)* esten habilitadas como se muestra (estas se hallan habilitadas por defecto):

![](/sbox/screen/eraser-en/13.png)

*Figure 5: Las casillas de Eraser Cluster Tip Area y Alternate Data Streams en modo por defecto*


- *Cluster Tip Area (Área Extrema de Sectores Consecutivos de Disco)*: El disco	duro de la computadora está dividido en pequeños segmentos llamados	sectores consecutivos (clústers). Normalmente un archivo abarca varios	sectores consecutivos, y a menudo el archivo no utiliza completamente	el último sector consecutivo. El espacio no utilizado de este último	sector consecutivo se llama el Área Extrema de Sectores Consecutivos de Disco.	Esta sección  de área de sectores consecutivos puede contener información	sensible del otro archivo que fue escrito sobre este sector consecutivo	de disco antes y que ocupaba la mayor parte del sector consecutivo	del disco. La información del área extrema de un sector consecutivo de	disco puede ser legible para un especialista en recuperación de datos.	De modo que debes asegurarte de **habilitar** la casilla correspondiente a *Cluster Tip Area (Área Extrema de Sectores Consecutivos de Disco)* de modo que todos los datos asociados con el archivo sean eliminados con este.

- *Alternate Data Streams (Flujo de Datos Alternos)*: Cuando se almacena un	archivo en tu computadora, este puede ubicarse en diferentes partes.	Por ejemplo, este texto contiene tanto texto como imágenes. Este se	almacenaría en diferentes ubicaciones o 'streams (flujos)' en tu computadora. **Habilita** la casilla marcada como *Alternate Data Streams (Flujo de Datos Alternos)* para garantizar que todos los datos asociados con el archivo sean borrados.

**Paso 6**. **Pulsa** ![](/sbox/screen/eraser-en/11.png).

Ahora has fijado el método de sobrescritura para que **Eraser** para limpiar o eliminar permanentemente archivos. También debes fijar las mismas opciones para la característica de *Unused Disk Space (Espacio de Disco No Utilizado)* que aparece en la siguiente pestaña en la pantalla de *Preferencias: Erasing*. sin embargo, puedes fijar el número de pasadas a un número *razonable* -- considerando que la limpieza de espacio libre de disco tomará aproximadamente unas dos horas por pasada.




