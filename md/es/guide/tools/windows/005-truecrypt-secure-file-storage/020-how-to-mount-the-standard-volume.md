

---

lang: es
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Mount the Standard Volume

---

Lista de las secciones en esta página:

- [**3.0 Cómo montar un Volumen común**](#3.0)
- [**3.1 Cómo desmontar un Volumen común**](#3.1)

<a name="3.0"></a>
## 3.0 Cómo montar un Volumen común ##

En **TrueCrypt**, *montar* un *Volumen común* se refiere a habilitarlo para su uso. En esta sección, aprenderás cómo montar tu nuevo Volumen común.  

Para empezar a montar tu Volumen común, sigue los siguientes pasos: 

**Paso 1**. **Pulsa dos veces** ![](/sbox/screen/truecrypt-es-1/52.png) o **selecciona Inicio > Programas > TrueCrypt > TrueCrypt** para abrir **TrueCrypt**.

**Paso 2**. **Selecciona** cualquier unidad de la lista según se muestra a continuación: 

![](/sbox/screen/truecrypt-es-1/12.png)

*Figura 1: Panel de control de TrueCrypt*

*En este ejemplo, se montará el Volumen común como la unidad M:.*

**Nota**: En la *Figura 1*, se ha seleccionado la unidad *M:* para montar el *Volumen común*; no obstante, puedes elegir cualquier otra unidad de la lista.

**Paso 3**. **Pulsa** ![](/sbox/screen/truecrypt-es-1/17.png)

*La pantalla “Selecciona un volumen TrueCrypt” aparecerá como se muestra a continuación.*

![](/sbox/screen/truecrypt-es-1/29.png)

*Figura 2: Pantalla para Seleccionar un volumen TrueCrypt*

**Paso 4**. **Selecciona** el archivo del Volumen común que creaste, luego **pulsa** ![](/sbox/screen/truecrypt-es-1/30.png) para cerrar *Figura 2* y regresar al panel de control de **TrueCrypt**.

**Paso 5**. **Pulsa** ![](/sbox/screen/truecrypt-es-1/31.png) para activar la pantalla de solicitud de *Ingrese la contraseña* como sigue:

![](/sbox/screen/truecrypt-es-1/32.png)

*Figura 3: Pantalla de solicitud de Ingrese la contraseña*

**Paso 6**. **Ingrese** la contraseña en el campo de texto *Contraseña*. 

**Paso 7**. **Pulsa** ![](/sbox/screen/truecrypt-es-1/33.png) para comenzar a montar el *Volumen común*.

**Nota**: Si la contraseña que ingresaste era incorrecta, **TrueCrypt** solicitará que la vuelvas a ingresar y **pulses** ![](/sbox/screen/truecrypt-es-1/33.png). Si la contraseña es correcta, el *Volumen común* se montará como sigue:

![](/sbox/screen/truecrypt-es-1/34.png)

*Figura 4: Panel de control de TrueCrypt que muestra el Volumen común recientemente montado*

**Paso 8**. **Pulsa dos veces** la entrada resaltada en **TrueCrypt** o la letra de la unidad correspondiente en la pantalla de *Mi computadora* para acceder al Volumen común (ahora montado en la unidad *M*: de tu computadora). 

![](/sbox/screen/truecrypt-es-1/35.png)

*Figura 5: Acceso al Volumen común por medio de la pantalla Mi computadora*

**Nota**: Hemos montado satisfactoriamente el Volumen común *Mi volumen* en el disco virtual *M*:. Este disco virtual se comporta como un disco real, salvo que está completamente cifrado. Cualquier archivo que copies, muevas o guardes en este disco virtual, se cifrará automáticamente (en un proceso conocido como cifrado sobre la marcha). 

Puedes guardar y hacer copias de archivos del *Volumen común* del mismo modo en que harías con cualquier disco normal (por ejemplo, arrastrándolas y soltándolas). Cuando mueves un archivo fuera del *Volumen común*, este se descifra automáticamente. Inversamente, si mueves un archivo al *Volumen común*, **TrueCrypt** lo cifra automáticamente. Si tu computadora falla o se apaga de pronto, **TrueCrypt** cierra el *Volumen común* de inmediato. 

**Importante**: Luego de transferir los archivos al volumen **TrueCrypt**, asegúrate de que no queden rastros de los archivos en la computadora o dispositivo de memoria USB de donde vinieron. Por favor, consulta el capítulo [**6. Cómo destruir información sensible**](/es/chapter-6).

<a name="3.1"></a>
## 3.1 Cómo desmontar un Volumen común ##

En **TrueCrypt**, *desmontar* un *Volumen común* simplemente significa inhabilitar su uso. 

Para cerrar o desmontar un *Volumen común* y hacer que sus archivos sean accesibles solo a personas con una contraseña, sigue los siguientes pasos: 

**Paso 1**. **Selecciona** el volumen de la lista de volúmenes montados de la ventana principal de **TrueCrypt** como se indica a continuación:

![](/sbox/screen/truecrypt-es-1/34.png)

*Figure 17: Selección del Volumen común a ser desmontado*

**Paso 2**. **Pulsa** ![](/sbox/screen/truecrypt-es-1/49.png) para desmontar o cerrar tu Volumen común **TrueCrypt**. 

**Importante**: Asegúrate de desmontar tu volumen **TrueCrypt** antes de dejar tu computadora en modo de *espera* o de *hibernación*. Mejor aún, siempre apaga tu computadora de escritorio o portátil si planeas dejarla desatendida. Esto impedirá que alguien obtenga la contraseña de tu volumen.

Para recuperar un archivo almacenado en un Volumen común cerrado o desmontado, tendrás que volver a montarlo.


