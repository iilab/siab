

---

lang: fr
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: How to Use the NoScript Add On

---

Sommaire des sections de cette page:

- [**4.0 À propos de NoScript**](#4.0)
- [**4.1 Comment utiliser NoScript**](#4.1)
- [**4.2 À propos du Clickjacking et des attaques XXS (Cross-Site Scripting)**](#4.2)

-------

<a name="4.0"></a>
## 4.0 À propos de NoScript ##

![](/sites/securitybkp.ngoinabox.org/files/u9/noscript.png)

**NoScript** est un **module complémentaire Mozilla** particulièrement utile. Ce programme peut contribuer à protéger votre ordinateur contre des sites Internet malveillants. Il fonctionne en dressant une "liste blanche" des sites que vous avez désignés comme acceptables, sûrs ou fiables (tel qu’un site de "télébanque" à domicile ou un journal électronique). Tous les autres sites sont considérés comme potentiellement dangereux et leurs fonctions sont limitées jusqu’à ce que vous décidiez que le contenu du site ne comporte aucun risque et que vous l’ajoutiez à la liste blanche. 

**NoScript** commencera à bloquer automatiquement les bannières publicitaires, les publicités intempestives (*pop-up*), **JavaScript** et les codes **Java** associés, ainsi que plusieurs autres éléments Web potentiellement dommageables. **NoScript** ne fait pas lui-même la différence entre des contenus dommageables et des contenus nécessaires à l'affichage normal des sites Internet. Il vous revient de définir des exceptions pour les sites dont vous jugez les contenus sûrs.

<a name="4.1"></a>
## 4.1 Comment utiliser NoScript ##

Avant de commencer à utiliser **NoScript**, assurez-vous d'avoir installé le programme correctement en **sélectionnant Outils > Modules complémentaires** pour afficher la fenêtre des *Modules complémentaires* et confirmer l'installation.

**Astuce**: Bien que l’utilisation de **NoScript** puisse paraître laborieuse au début, (parce que, par exemple, les sites Web que vous avez l’habitude de visiter ne s’affichent pas correctement), vous tirerez immédiatement avantage de la fonction de blocage automatique des éléments suspects. 

Cela bloquera toutes les publicités et fenêtres intempestives, ainsi que les éléments de code malveillants intégrés (ou piratés) à certains sites Web. 

**NoScript** fonctionnera silencieusement en arrière-plan jusqu'à ce qu'il détecte la présence de contenu **JavaScript**, **Adobe Flash** ou autre contenu de type script. À ce moment-là, **NoScript** bloquera ledit contenu et la barre d'état du logiciel s'affichera au bas de la fenêtre **Firefox**, tel qu'illustré ci-dessous: 

![](/sbox/screen/firefox-fr/37.png)

*Figure 1: La barre d'état de NoScript*

La barre d'état de **NoScript** affiche de l’information sur les *objets* (par exemple, la publicité et les fenêtres intempestives) et les *scripts* dont l’exécution est actuellement bloquée par le programme. Les deux figures suivantes sont des exemples typiques de **NoScript** à l'oeuvre: à la *Figure 2*, **NoScript** a réussi à bloquer une publicité créée en **Adobe Flash Player** sur un site commercial.

![](/sbox/screen/firefox-fr/38.png)

*Figure 2: Un exemple de publicité intempestive bloquée par NoScript sur un site commercial*

À la *Figure 3*, le site Internet de **Twitter** affiche un avertissement vous invitant à activer **JavaScript** (au moins temporairement) pour afficher normalement le contenu du site.

![](/sbox/screen/firefox-fr/39.png)

*Figure 3: Le site Internet de Twitter suggère d'activer JavaScript*

Puisque **NoScript** ne fait pas la différence entre code malveillant et code légitime, il est possible que certaines fonctions et fonctionnalités importantes (par exemple, une barre d’outil) soient désactivées. Certaines pages Web affichent du contenu, y compris du contenu script, provenant de plusieurs sites Internet à la fois. Par exemple, un site Internet comme **www.youtube.com** comporte trois différentes sources de scripts: 

![](/sbox/screen/firefox-fr/40.png)

*Figure 4: Un exemple d'affichage du menu de la barre d'état NoScript*

Pour débloquer des scripts dans une telle situation, commencer par **sélectionner** l'option *Autoriser [cette page] temporairement* (dans ce cas-ci, youtube.com). Si cela ne vous permet pas d'afficher la page normalement, il vous faudra peut-être déterminer, par un processus d'essais et erreurs, le nombre minimal de sites nécessaire pour afficher le contenu de votre choix. Pour **YouTube**, vous n'avez qu'à **sélectionner** l'option *Autoriser youtube.com temporairement* et *Autoriser ytimg.com temporairement* pour faire en sorte que **YouTube** fonctionne.

**Attention!**: Vous ne devriez en aucune circonstance sélectionner l'option: *Autoriser les scripts globalement (dangereux)*. Autant que possible, évitez de sélectionner l'option *Autoriser toute la page*. De temps en temps, il vous faudra peut-être autoriser tous les scripts; si une telle situation se présente, assurez-vous de le faire uniquement pour les sites dont vous avez entièrement confiance, et temporairement, c-à-d. jusqu'à la fin de votre session de navigation. *Une seule* injection de code malveillant suffit à compromettre votre sécurité et votre confidentialité en ligne.

<a name="4.2"></a>
## 4.2 À propos du Clickjacking et des attaques XXS (Cross-Site Scripting) ##

**NoScript** peut être configuré pour défendre votre système contre les attaques XXS (Cross-Site Scripting) et de détournement de clic (Clickjacking). 

Un script *cross-site* est un type de faille de sécurité informatique qui permet à des pirates et autres intrus d’injecter un code malveillant dans une page Web existante. Un détournement de clic (ou *clickjacking*) se produit, par exemple, lorsque vous cliquez sur un bouton qui sert en apparence à accomplir une fonction quelconque, mais que le même bouton lance l'exécution d'un code ou d'un script à votre insu. Ces deux types d'attaques peuvent se produire sans que vous ne vous en rendiez compte, à moins que **NoScript** soit configuré pour les bloquer.

Chaque fois qu'une attaque de *clickjacking* est en cours, une fenêtre comme celle-ci apparaît:

![](/sbox/screen/firefox-en/41.png)

*Figure 5: Un exemple de tentative d'attaque de détournement* 

Suivez les consignes affichées dans la fenêtre pour neutraliser la tentative de détournement, puis **cliquez** sur ![](/sbox/screen/firefox-fr/15.png).


