

---

lang: es
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: How to Use the NoScript Add On

---

Lista de secciones de esta página:

- [**4.0 Acerca de NoScript**](#4.0)
- [**4.1 Utilización de NoScript**](#4.1)

-------

<a name="4.0"></a>
## 4.0 Acerca de NoScript ##

![](/sites/securitybkp.ngoinabox.org/files/u9/noscript.png)

**NoScript** es un **complemento de Mozilla** que resulta especialmente de utilidad a la hora de proteger el equipo de sitios web maliciosos en Internet. Este complemento implementa una "lista blanca" de sitios que el usuario ha determinado que son aceptables, seguros o de confianza (como el sitio web de un banco o de una publicación electrónica). El resto de sitios se consideran potencialmente dañinos y se restringe su funcionamiento hasta que el usuario determina que el contenido de un sitio en concreto no resulta perjudicial; en ese momento se puede añadir a la lista blanca. 

**NoScript** empezará a bloquear automáticamente todos los anuncios, publicidad emergente, código de **JavaScript** y de **Java**, así como otros atributos de un sitio web que pueden ser potencialmente dañinos. **NoScript** no puede distinguir el contenido dañino del que es necesario para que un sitio web se muestre correctamente. Corresponde al usuario crear excepciones para aquellos sitios que tengan contenido que este considere seguro. 

<a name="4.1"></a>
## 4.1 Utilización de NoScript ##

Antes de empezar a utilizar **NoScript**, cerciórate de que se instaló correctamente al **seleccionar Herramientas > Complementos** para abrir la ventana de *Complementos* y confirmar que se ha instalado.

**Un consejo**: Aunque es posible que **NoScript** resulte un poco frustrante al principio (ya que puede que los sitios web que siempre hayas visitado no se muestren correctamente), de inmediato sacarás partido a la función de bloqueo automático de objetos. Con esta función, se restringirá publicidad molesta, mensajes emergentes y código malicioso que se haya incrustado en páginas web (o que lo hayan incrustado piratas informáticos).  

**NoScript** se ejecutará silenciosamente en segundo plano hasta que detecte la presencia de **JavaScript**, **Adobe Flash** u otro contenido con *scripts*. En ese momento, **NoScript** bloqueará dicho contenido y aparecerá una barra de estado en la parte inferior de la ventana de **Firefox** como esta: 

![](/sbox/screen/firefox-es-1/50.png)

*Figura 1: La barra de estado de NoScript*

La barra de estado de **NoScript** muestra qué *objetos* (por ejemplo, publicidad y mensajes emergentes) y *scripts* se está evitando que se ejecuten en el sistema. Las dos figuras siguientes son ejemplos idóneos de **NoScript** en acción: en la *Figura 2*, **NoScript** ha bloqueado satisfactoriamente un anuncio creado en **Adobe Flash Player** en un sitio web comercial. 

![](/sbox/screen/firefox-es-1/51.png)

*Figura 2: Un ejemplo de NoScript bloqueando publicidad emergente en un sitio comercial*

En la *Figura 3*, el sitio web de **Twitter** informa que **JavaScript** debe activarse (al menos temporalmente) para ver este sitio web. 

![](/sbox/screen/firefox-es-1/52.png)

*Figura 3: El sitio web de Twitter solicitando la activación de JavaScript*

Como **NoScript** no distingue el código malicioso del verdadero, es posible que no aparezcan determinadas características y funciones importantes (como por ejemplo una barra de herramientas). Hay páginas web que presentan contenido, incluido contenido de *scripts*, proveniente de más de un sitio web.  Por ejemplo, un sitio web como **www.twitter.com** tiene dos fuentes de *scripts* (*twitter.com* y *twimg.com*): 

![](/sbox/screen/firefox-es-1/53.png)

*Figura 4: Un ejemplo del menú Opciones de la barra de estado de NoScript*

Para desbloquear los *scripts* en estos casos, **selecciona** la opción *Permitir temporalmente [nombre del sitio web]* (en este ejemplo, *Permitir temporalmente twitter.com*).  No obstante, si con esto no puedes ver la página, es posible que tengas que determinar, mediante un proceso de ensayo y error, el número mínimo de sitios web que hacen falta para ver el contenido seleccionado. Por ejemplo, en **Twitter**, debes **seleccionar** las opciones *Permitir temporalmente twitter.com* y *Permitir temporalmente twimg.com* para que **Twitter** funcione.

**¡Advertencia!** En **ningún** caso debes seleccionar la opción *Permitir JavaScript globalmente (peligroso)*. Siempre que sea posible, no selecciones la opción *Permitir toda esta página*. Habrá veces en las que pueda que tengas que permitir todos los *scripts*; en estos casos, cerciórate de hacerlo solo temporalmente para sitios de confianza, es decir, hasta que termines tu sesión en línea. Con una *sola* inyección de código malicioso se pone en peligro toda tu privacidad y seguridad en línea. 

Para sitios web en los que confíes y que visites a menudo, **selecciona** la opción *Permitir [nombre del sitio web]*. (En el ejemplo anterior, se han seleccionado *Permitir twitter.com* y *Permitir twimg.com*). Al marcar esa opción, **NoScript** guarda permanentemente dicho sitio web en la lista como un sitio de confianza.

