

---

lang: es
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: How to Install and Configure CCleaner

---

Lista de secciones en esta página:

- [**2.0 Cómo instalar CCleaner**](#2.0)
- [**2.1 Qué hacer antes de empezar a configurar CCleaner**](#2.1)
- [**2.2 Cómo configurar CCleaner**](#2.3)


<a name="2.0"></a>
## 2.0 Cómo instalar CCleaner ##

Instalar **CCleaner** es fácil y rápido. Para empezar, sigue estas instrucciones:

**Paso 1**. **Haz clic** en ![](/sbox/screen/ccleaner-es-1/01.png) para empezar el proceso de instalación. Si aparece el cuadro *Abrir archivo – Advertencia de seguridad* , **haz clic** en
![](/sbox/screen/ccleaner-es-1/25.png) para activar la siguiente pantalla:

![](/sbox/screen/ccleaner-es-1/03.png)

*Figura 1: Bienvenido al Asistente de Instalación de CCleaner v4.03*

**Paso 2**.  **Haz clic** en ![](/sbox/screen/ccleaner-es-1/05.png) para activar la pantalla *Opciones de instalación – Seleccionar algunas opciones adicionales*, , luego **haz clic** en ![](/sbox/screen/ccleaner-es-1/05.png) para activar la siguiente pantalla.

**Paso 3**. **Haz clic** en ![](/sbox/screen/ccleaner-es-1/08.png) para activar la pantalla que muestra el progreso de *Instalación*.

**Paso 4**. **Haz clic** en ![](/sbox/screen/ccleaner-es-1/09.png) para finalizar la instalación de **CCleaner** y asegúrate de que la opción "Habilitar el escaneo inteligente de cookie" está desabilitada en la ventana que surgirá a continuación.

![](/sbox/screen/ccleaner-es-1/12.png)

*Figura 2: Panel de control de Piriform CCleaner*

<a name="2.1"></a>
## 2.1 Qué hacer antes de empezar a configurar CCleaner ##

Como se detalla en el [**Capítulo 6. Destruir información sensible**](/es/chapter-6) de la **Guía paso a paso**, los métodos estándares de eliminación de archivos de **Microsoft Windows** no borran realmente los datos del disco (ni siquiera vaciando la *Papelera de reciclaje*). Lo mismo se aplica a los archivos temporales. Para borrarlos (eliminarlos de manera definitiva), los archivos deben ser sobrescritos con datos aleatorios. **CCleaner** debe ser configurado para que sobrescriba cualquier archivo y lo elimine de manera segura, pues no lo hará con la configuración predeterminada. **CCleaner** puede incluso eliminar información obsoleta de manera segura a través de la limpieza de espacio libre  (lee la sección **5.3 Limpieza de Espacio Libre del Disco Utilizando CCleaner**).

<a name="2.2"></a>
## 2.2 Cómo configurar CCleaner ##

Antes de empezar a utilizar **CCleaner**, tendrás que configurarlo para que elimine de manera segura todos los archivos temporales. 

Para configurar **CCleaner**, sigue estas instrucciones:

**Paso 1**. **Haz clic** en ![](/sbox/screen/ccleaner-es-1/13.png) o **selecciona Inicio > Programas > CCleaner** para activar el panel de control de *Piriform CCleaner* .

**Paso 2**. **Haz clic** en ![](/sbox/screen/ccleaner-es-1/16.png) para activar la siguiente pantalla:

![](/sbox/screen/ccleaner-es-1/15.png)

*Figura 3: La ventana Opciones con el panel Acerca de*

**Paso 3**. **Haz clic** en ![](/sbox/screen/ccleaner-es-1/14.png) para activar el panel *Configuración*. El panel *Configuración* te permite elegir el idioma y determina cómo **CCleaner** eliminará los archivos temporales y limpiará las unidades de disco.

**Ojo**: En la sección *Borrado seguro*, la opción *Borrado normal de archivo (Rápido)* está activada de manera automática. 

**Paso 4**. **Haz clic** en la opción *Borrado seguro de archivo (Lento)* para activar el menú desplegable. 

**Paso 5**. **Abre** el menú desplegable de la opción *Borrado seguro de archivo (Lento)* y **selecciona** *Sobrescritura avanzada (3 pasadas)*, como muestra la siguiente pantalla: 

![](/sbox/screen/ccleaner-es-1/17.png)

*Figura 4: Las opciones de borrado seguro en el panel de control*

Después de que hayas fijado esta opción,  **CCleaner** sobrescribirá los archivos y las carpetas que has seleccionado con datos aleatorios, eliminándolos de manera efectiva de tu disco duro. Las *pasadas* de la opción *Borrado seguro* se refieren a cuántas veces tus datos serán sobrescritos con datos aleatorios. Cuanto mayor sea el número de pasadas seleccionadas, más veces tu documento, archivo o carpeta será sobrescrito con datos aleatorios. Esto reduce la capacidad del documento de ser recuperado, pero hace aumentar la duración del proceso de eliminación.

