

---

lang: es
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 4
depth: 3
title: Hidden Volumes

---

Lista de las temas en esta página:

- [**5.0 Acerca de los volúmenes ocultos**](#5.0)
- [**5.1 Cómo crear un Volumen oculto**](#5.1)
- [**5.2 Cómo montar un Volumen oculto**](#5.2)
- [**5.3 Consejos acerca de cómo utilizar la característica del disco oculto de manera segura**](#5.3)

<a name="5.0"></a>
## 5.0 Acerca de los volúmenes ocultos ##

En **TrueCrypt**, un *Volumen oculto* se almacena dentro de tu *Volumen común* cifrado, pero su existencia permanece oculta. Aunque «montes» o abras tu Volumen común, no es posible encontrar ni probar la existencia del Volumen oculto. Si te fuerzan a revelar tu contraseña y la ubicación de tu Volumen común, se revelará su contenido pero **no** la existencia del Volumen oculto dentro del mismo. 

Imagina un maletín con un compartimiento secreto. En la sección normal de tu maletín, guardas archivos que no te importa que sean confiscados o que se pierdan y mantienes los archivos importantes y privados en el compartimiento secreto. El propósito del compartimiento secreto (especialmente uno bien diseñado), es el de ocultar su propia existencia y por tanto, los documentos dentro del mismo. 

<a name="5.1"></a>
## 5.1 Cómo crear un Volumen oculto ##

La creación de un *Volumen oculto* **TrueCrypt** es similar a la de un *Volumen común* de **TrueCrypt**: Incluso algunos de los paneles, pantallas y ventanas son iguales. 

**Paso 1**. **Abre** **TrueCrypt**.

**Paso 2**. **Pulsa** ![](/sbox/screen/truecrypt-es-1/13.png) para activar el *asistente para la creación de volúmenes TrueCrypt*. 

**Paso 3**. **Pulsa** ![](/sbox/screen/truecrypt-es-1/05.png) para aceptar la opción por defecto *Crear un contenedor para archivos cifrados*.

**Paso 4**. **Elige** la opción *Volumen TrueCrypt oculto* como sigue: 

![](/sbox/screen/truecrypt-es-1/37.png)

*Figura 1: Ventana del asistente para la creación de volumen con la opción de volumen TrueCrypt oculto habilitada*

**Paso 5**. **Pulsa** ![](/sbox/screen/truecrypt-es-1/05.png) para activar la siguiente pantalla:

![](/sbox/screen/truecrypt-es-1/38.png)

*Figura 2: Ventana del asistente para la creación de volúmenes de TrueCrypt - Ventana de modos*

- *Modo directo*: Esta opción te permite crear el *Volumen oculto* dentro de un *Volumen común* existente.

- *Modo normal*: Esta opción te permite crear un *Volumen común* completamente nuevo donde almacenar el *Volumen oculto*. 

En este ejemplo, utilizaremos el *Modo directo*. 

**Nota**: Si prefieres crear un nuevo *Volumen común*, ten a bien repetir el proceso de la sección [**Cómo crear un Volumen común**](/es/truecrypt_instalar_volumenescomunes#2.2).

**Paso 6**. **Elige** la opción *Modo directo* y luego **pulsa** ![](/sbox/screen/truecrypt-es-1/05.png) para activar la ventana para la *Creación de volúmenes TrueCrypt - Ubicación del volumen*.

**Nota**: Asegúrate de que el *Volumen común* se encuentre desmontado antes de seleccionarlo. 

**Paso 7**. **Pulsa** ![](/sbox/screen/truecrypt-es-1/17.png) para activar la siguiente pantalla:

![](/sbox/screen/truecrypt-es-1/29.png)

*Figura 3: Ventana del asistente para la creación de volúmenes de TrueCrypt - Selecciona un volumen TrueCrypt*

**Paso 8**. **Localiza** el archivo de volumen a través de la ventana *Selecciona un volumen TrueCrypt* como se muestra en la *Figura 3*. 

**Paso 9**. **Pulsa** ![](/sbox/screen/truecrypt-es-1/30.png) para regresar al *Asistente para la creación de volúmenes TrueCrypt*.

**Paso 10**. **Pulsa** ![](/sbox/screen/truecrypt-es-1/05.png) para activar la pantalla *Ingrese la contraseña*.

**Paso 11**. **Ingresa** la contraseña que utilizaste al crear el *Volumen común* en el campo de texto *Contraseña* para activar la siguiente pantalla:

![](/sbox/screen/truecrypt-es-1/46.png)

*Figura 4: Asistente para la creación de volúmenes TrueCrypt - Panel de mensaje del Volumen oculto*

**Paso 12**. **Pulsa** ![](/sbox/screen/truecrypt-es-1/05.png) luego de leer el mensaje para activar la pantalla *Opciones de cifrado del Volumen oculto*.

**Nota**: Deja tal como están los parámetros por defecto del *Algoritmo de cifrado* y del *Algoritmo Hash* para el *Volumen oculto*. 

**Paso 13**. **Pulsa** ![](/sbox/screen/truecrypt-es-1/05.png) para activar la siguiente pantalla:

![](/sbox/screen/truecrypt-es-1/41.png)

*Figura 5: Asistente para la creación de volúmenes TrueCrypt - Ventana de tamaño del Volumen oculto*

Se te solicitará que especifiques el tamaño del *Volumen oculto*. 

**Nota**: Considera el tipo de documentos, la cantidad y el tamaño requerido para almacenarlos. Deja algo de espacio para el *Volumen común*. Si seleccionas el tamaño máximo disponible para el *Volumen oculto*, no podrás agregar ningún otro archivo al *Volumen común* original. 

Si el tamaño de tu *Volumen común* es de 10 Megabytes (MB) y especificas un tamaño de *Volumen oculto* de 5 MB (como se muestra en la *Figura 6* anterior), tendrás dos volúmenes (uno oculto y otro común) de aproximadamente 5 MB cada uno. 

Asegúrate de que la información que almacenes en el *Volumen común* no exceda los 5 MB que has fijado. Esto es porque el programa **TrueCrypt** no detecta automáticamente, por sí mismo, la existencia de un *Volumen oculto*, y puede sobrescribirlo accidentalmente. Si excedes el tamaño previamente establecido, te arriesgas a perder archivos almacenados en el Volumen oculto. 

**Paso 14**. **Ingresa** el tamaño deseado del Volumen oculto en el campo de texto correspondiente, como se muestra en la *Figura 5*. 

**Paso 15**. **Pulsa** ![](/sbox/screen/truecrypt-es-1/05.png) para activar la ventana *Contraseña del Volumen oculto*.

Ahora debes crear una contraseña para el Volumen oculto *diferente* de la que utilizas para proteger tu Volumen común. Nuevamente, recuerda escoger una contraseña sólida. Por favor, consulta el capítulo [**KeePass**](https://info.securityinabox.org/es/keepass_principal) para aprender más acerca de la creación de contraseñas sólidas. 

**Consejo**: Si crees que te verás forzado a revelar el contenido de tus volúmenes **TryeCrypt**, almacena tu contraseña para el Volumen común en **KeePass** y crea una contraseña sólida que tengas que recordar solo para el Volumen oculto. Esto te ayudará a esconder tu Volumen oculto, ya que no dejarás ningún rastro de su existencia.

**Paso 16**. **Crea** una contraseña e **ingrésala** allí dos veces, luego **pulsa** ![](/sbox/screen/truecrypt-es-1/05.png) para activar la siguiente pantalla:

![](/sbox/screen/truecrypt-es-1/42.png)

*Figura 6: Asistente para la creación de volúmenes TrueCrypt - Panel de formateo del Volumen oculto*

Deja las opciones por defecto del *Sistema de* archivo y *Cluster* tal como están. 

**Paso 17**. **Mueve** el ratón alrededor de la pantalla para aumentar la solidez criptográfica del cifrado y luego **pulsa** ![](/sbox/screen/truecrypt-es-1/25.png) para formatear el Volumen oculto.

*Después de formatear el Volumen oculto, aparecerá la siguiente pantalla* 

![](/sbox/screen/truecrypt-es-1/43.png)

*Figura 7: Ventana de mensaje del Asistente para la creación de volúmenes TrueCrypt*

**Nota**: La *Figura 7* confirma que has creado satisfactoriamente un Volumen oculto y también te advierte del peligro de sobrescribir los archivos en el Volumen oculto cuando almacenes archivos en el Volumen común. 

**Paso 18**. **Pulsa** ![](/sbox/screen/truecrypt-es-1/27.png) para activar la ventana *Volumen oculto creado* y luego **pulsa** ![](/sbox/screen/truecrypt-es-1/28.png) y regresa a panel de control de **TrueCrypt**. 

El Volumen oculto ya se ha creado dentro del Volumen común. Ahora puedes almacenar documentos en el Volumen oculto, que permanece invisible incluso para quien obtenga la contraseña para ese Volumen común en particular. 

<a name="5.2"></a>
## 5.2 Cómo montar un Volumen oculto ##

El método para montar un *Volumen oculto* o hacer que sea accesible para su uso, es el mismo que para un *Volumen común*, la única diferencia es que utilizas la contraseña que acabas de crear para el *Volumen oculto*.

Para *montar* o abrir el *Volumen oculto*, sigue los siguientes pasos: 

**Paso 1**. **Selecciona** una unidad de la lista (en este ejemplo, es la unidad *K:*):

![](/sbox/screen/truecrypt-es-1/44.png)

*Figura 8: Unidad seleccionada para montar en la pantalla de volumen de TrueCrypt*

**Paso 2**. **Pulsa** ![](/sbox/screen/truecrypt-es-1/17.png) para activar la ventana *Selecciona un volumen TrueCrypt*. 

**Paso 3**. **Desplázate** hasta el archivo de volumen *TrueCrypt* y **selecciónalo** (el mismo archivo que para el Volumen común). 

**Paso 4**. **Pulsa** ![](/sbox/screen/truecrypt-es-1/30.png) para regresar al *panel de control de **TrueCrypt**.

**Paso 5**. **Pulsa** ![](/sbox/screen/truecrypt-es-1/31.png) para activar la pantalla de solicitud de *Ingrese la contraseña* como sigue:

![](/sbox/screen/truecrypt-es-1/32.png)

*Figura 9: Pantalla Ingrese la contraseña*

**Paso 6**. **Ingresa** la contraseña que usaste para crear el Volumen oculto y luego **pulsa** ![](/sbox/screen/truecrypt-es-1/33.png). 

Tu Volumen oculto ya está montado (o abierto) como sigue:

![](/sbox/screen/truecrypt-es-1/45.png)

*Figura 10: Pantalla principal de TrueCrypt que muestra el Volumen oculto recientemente montado*

**Paso 7**. **Pulsa dos veces** sobre la entrada o accede a ella a través de la ventana *Mi computadora*. 

<a name="5.3"></a>
##5.3 Consejos acerca de cómo utilizar la característica del disco oculto de manera segura ##

El propósito de la característica del disco oculto es escapar a la potencial situación de peligro *aparentemente* entregando tus archivos cifrados, cuando alguien en una posición de poder demande verlos, sin estar realmente forzado a revelar tu información más sensible. Además de proteger tu información, esto puede permitirte que evites poner en peligro tu seguridad, la de tus colegas o compañeros. Para que esta técnica sea efectiva, debes crear una situación en la que la persona que demande ver tus archivos se satisfaga con lo que le muestres y te deje ir.

Para esto, quizá quieras implementar algunas de las sugerencias siguientes: 

- Coloca en el Volumen común algunos documentos confidenciales que no te importe exponer. Esta información deberá ser lo suficientemente sensible como para que la mantengas en un volumen cifrado. 

- Ten en cuenta que alguien que exija ver tus archivos puede saber de
Volúmenes ocultos. No obstante, si utilizas **TrueCrypt** correctamente, esta persona no podrá probar la existencia de tu Volumen oculto, lo que hará tu negativa más fácil de creer.

- Actualiza los archivos en el Volumen común semanalmente. Esto creará la impresión de que realmente utilizas esos archivos.

Siempre que montes un volumen **TrueCrypt**, puedes elegir habilitar la característica *Proteger Volumen oculto contra daños causados por la escritura en el Volumen externo*. Una característica *muy* importante, que te permite agregar nuevos archivos «señuelo» a tu Volumen común sin riesgo de borrar o sobrescribir accidentalmente el contenido cifrado de tu Volumen oculto. 

Como se mencionó anteriormente, si excedes el límite de almacenamiento en tu Volumen común puedes destruir tus archivos ocultos. No habilites la característica *Proteger el Volumen oculto* si te fuerzan a montar un volumen **TrueCrypt**, porque para hacerlo tendrás que ingresar la contraseña secreta de tu Volumen oculto y revelarás claramente la existencia de dicho volumen. No obstante, cuando actualices los archivos señuelo en privado *siempre* debes habilitar esta opción.

Para utilizar la característica *Proteger el Volumen oculto* sigue los siguientes pasos:

**Paso 1**. **Pulsa** ![](/sbox/screen/truecrypt-es-1/47.png) en la pantalla de solicitud de *Ingrese la contraseña* que se muestra en la *Figura 9*, arriba. Esto activará la ventana de *Opciones de montaje* como sigue:

![](/sbox/screen/truecrypt-es-1/48.png)

*Figure 11: Ventana de opciones de montaje*

**Paso 2**. **Marca** la opción *Protect hidden volume against damage caused by writting to outer volume (Proteger el Volumen oculto contra daños ocasionados por la escritura en el volumen externo)*.

**Paso 3**. **Ingresa** la contraseña en tu Volumen oculto y luego **pulsa** ![](/sbox/screen/truecrypt-es-1/33.png).

**Paso 4**. **Pulsa** ![](/sbox/screen/truecrypt-es-1/31.png) para montar tu Volumen común. Luego de montarlo satisfactoriamente, podrás agregar archivos señuelo sin dañar tu Volumen oculto.

**Paso 5**. **Pulsa** ![](/sbox/screen/truecrypt-es-1/51.png) para desmontar tu Volumen común o inhabilitar su uso, cuando hayas terminado de modificar su contenido. 

**Recuerda**: Sólo debes hacer esto cuando actualices los archivos en tu Volumen común. Si te ves forzado a revelar tu Volumen común a alguien, no debes utilizar la característica *Proteger Volumen oculto*.

