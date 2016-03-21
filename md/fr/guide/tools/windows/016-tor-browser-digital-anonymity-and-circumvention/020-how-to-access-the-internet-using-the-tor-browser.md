

---

lang: fr
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to access the Internet using the Tor Browser

---

Sommaire des sections de cette page:

- [**3.0 À propos de l'accès au réseau Tor**](#3.0)
- [**3.1 Comment se connecter au réseau Tor**](#3.1)
- [**3.2 Comment vérifier manuellement votre connexion au réseau Tor**](#3.2)
- [**3.3 Comment naviguer sur Internet en utilisant Tor**](#3.3)
- [**3.3.1 Comment configurer Mozilla Firefox pour fonctionner avec Tor**](#3.3.1)
- [**3.3.2 Comment configurer Internet Explorer pour fonctionner avec Tor**](#3.3.2)

-------

<a name="3.0"></a>
## 3.0 À propos de l'accès au réseau Tor ##

Pour commencer à naviguer anonymement sur Internet, vous devez lancer le programme **Navigateur Tor**. Dans un premier temps, le programme connectera votre système au réseau **Tor**. Une fois que la connexion au réseau **Tor** sera établie, le **Navigateur Tor** lancera automatiquement une instance distincte du **Firefox portable** qui est inclus dans le **Paquetage du navigateur Tor**.

**Note**: Il y a un compromis nécessaire entre l'anonymat et la vitesse d'exécution. Puisque **Tor** facilite la navigation anonyme, son utilisation ralentira considérablement la navigation. **Tor** fait transiter votre navigation par les ordinateurs de nombreux bénévoles situés un peu partout dans le monde afin de protéger votre sécurité et votre identité.

<a name="3.1"></a>
## 3.1 Comment se connecter au réseau Tor ##

Pour se connecter au réseau **Tor**, suivez les étapes énumérées ci-dessous:

**Première étape**. **Naviguez** jusqu'au dossier du *Navigateur Tor*, puis **double-cliquez** sur ![](/sbox/screen/tor-fr/30.png) pour afficher la fenêtre suivante:

![](/sbox/screen/tor-fr/24.png)

*Figure 1: Le panneau de contrôle de Vidalia en cours de connexion au réseau Tor*

Lorsque le *Panneau de contrôle de Vidalia* établit une connexion au réseau **Tor**, un icone ressemblant à un oignon jaune apparaît dans la *barre des tâches*, comme suit:  ![](/sbox/screen/tor-fr/31.png). Une fois que la connexion a été établie entre votre ordinateur et le réseau **Tor**, l'icone devient vert: ![](/sbox/screen/tor-fr/32.png)

**Note**: Pour apprendre à utiliser efficacement le *Panneau de contrôle de Vidalia*, veuillez consulter la page [**Comment utiliser le Panneau de contrôle de Vidalia**](/fr/tor_vidaliacontrole).

Quelques secondes plus tard, le **Navigateur Tor** activera le navigateur **Mozilla Firefox** affichant la fenêtre suivante:

![](/sbox/screen/tor-fr/33.png)

*Figure 2: Mozilla Firefox affichant l'onglet Are you using Tor?*

Chaque fois que vous lancez le programme **Navigateur Tor**, ce dernier active automatiquement le *Panneau de contrôle Vidalia* (*Figure 1*) et la fenêtre [**https://check.torproject.org/**](https://check.torproject.org/)  (*Figure 2*). Le module complémentaire **Torbutton** apparaît également dans le coin inférieur droit de la fenêtre, comme suit: ![](/sbox/screen/tor-fr/34.png) 

**Note**: Par contre, si une fenêtre de navigation de **Mozilla Firefox** était déjà ouverte lorsque vous avez lancé le **Navigateur Tor**, le **Torbutton** apparaîtra en mode désactivé dans cette même fenêtre, comme suit: ![](/sbox/screen/tor-fr/35.png)

Le **Torbutton** est utilisé pour configurer **Firefox** afin de se connecter adéquatement au réseau **Tor**. Vous n'avez qu'à **cliquer** sur le **Torbutton** pour alterner entre les modes actif et inactif. 

Cependant, si vous *n'êtes pas* connecté au réseau **Tor**, le **Torbutton** sera désactivé et la fenêtre suivante s'affichera: 

![](/sbox/screen/tor-fr/36.png)

*Figure 3: Mozilla Firefox affichant l'onglet Désolé, vous n'utilisez pas Tor*

<a name="3.2"></a>
## 3.2 Comment vérifier manuellement votre connexion au réseau Tor ##

Pour vérifier manuellement si vous êtes connecté ou non au réseau **Tor**, suivez les étapes énumérées ci-dessous: 

**Première étape**. **Ouvrez** le site Internet [**https://check.torproject.org/**](https://check.torproject.org/). Ce site confirmera si vous êtes connecté ou non au réseau **tor**.

Si votre navigateur Internet est connecté à l'Internet par l'entremise du réseau **Tor**, les sites qui sont bloqués ou restreints dans votre pays seront désormais accessibles, et vos activités en ligne seront privées et sécurisées. Vous remarquerez peut-être également que certaines pages Web, tel que **www.google.com**, se comporteront occasionnellement comme si vous vous trouviez dans un autre pays. Cela est normal lorsqu'on utilise **Tor**.

<a name="3.3"></a>
## 3.3 Comment naviguer sur Internet en utilisant Tor ##

Bien qu'il vous soit possible de commencer immédiatement à naviguer sur Internet avec **Firefox** par l'entremise du réseau **Tor**, nous vous recommandons de lire la section suivante pour régler **Firefox** de sorte que votre sécurité et votre anonymat en ligne soient optimisées.

<a name="3.3.1"></a>
### 3.3.1 Comment modifier les paramètres de Mozilla Firefox pour Tor ###

Le **torbutton** est un module complémentaire pour **Mozilla Firefox**. Il s'agit d'un petit programme conçu pour protéger l'anonymat et la sécurité de vos activités en ligne en bloquant certaines vulnérabilités de **Mozilla Firefox**. 

**Important**: Des sites malveillants, ou même un serveur **Tor**, pourraient *quand-même* révéler des renseignements sur votre emplacement et vos activités en ligne, et ce, *même* lorsque vous utilisez **Tor**. Heureusement, la configuration par défaut de **Torbutton** est relativement sécuritaire; cependant, nous vous recommandons de modifier certains paramètres pour optimiser votre sécurité et la protection de votre vie privée.

**Note**: Les utilisateurs **avancés** qui ont une compréhension approfondie des enjeux de sécurité associés aux navigateurs voudront peut-être raffiner encore davantage leurs paramètres.

La fenêtre des *Préférences Torbutton* comporte trois onglets qui vous permettent de régler diverses options: 

- L'onglet **Paramètres du proxy**
- L'onglet **Paramètres de sécurité**
- L'onglet **Paramètres d'affichage**

Il est facile d'accéder à la fenêtre des *Préférences Torbutton*, que **Torbutton** soit activé ou non. Pour afficher la fenêtre des *Préférences Torbutton*, suivez les étapes énumérées ci-dessous:

**Première étape**. **Cliquez à droite** sur le **Torbutton** pour afficher son menu, comme suit:

![](/sbox/screen/tor-fr/37.png)

*Figure 4: Le menu de Torbutton*

**Deuxième étape**. **Sélectionnez** l'item *Préférences...* pour afficher la fenêtre suivante:

![](/sbox/screen/tor-fr/38.png)

*Figure 5: La fenêtre des préférences de Torbutton affichant l'onglet Paramètres du proxy*

- L'onglet **Paramètres du proxy** 
 
L'onglet *Paramètres du proxy* permet de déterminer comment **Firefox** accède à l'Internet quand le **Torbutton** est activé. Vous ne devriez pas avoir à changer quoi que ce soit dans cet onglet.

- L'onglet **Paramètres de sécurité** 

L'onglet *Paramètres de sécurité* est conçu pour les utilisateurs *expérimentés* et *avancés* qui ont une compréhension approfondie des navigateurs et de la sécurité sur Internet. Ses paramètres par défaut présentent un niveau élevé de sécurité pour les utilisateurs moyens. Ces *Paramètres de sécurité* vous permettent de déterminer comment **Torbutton** gère l'historique de navigation, la mémoire cache, les cookies et d'autres fonctions de **firefox**.

![](/sbox/screen/tor-fr/39.png)

*Figure 6: L'onglet Paramètres de sécurité*

L'option *Désactiver les plugins pendant l'utilisation de Tor (indispensable)* est l'un des quelques paramètres de sécurité que vous pourriez devoir activer, quoique *temporairement*. Pour afficher des contenus vidéo en ligne avec **Tor**, y compris avec les services de [**DailyMotion**](http://www.dailymotion.com/), [**The Hub**](http://hub.witness.org/) et [**YouTube**](http://www.youtube.com), vous devez **décocher** l'option *Désactiver les plugins pendant l'utilisation de Tor*.

**Note**: Vous ne devriez activer que les plugins des sites de confiance, et vous devez retourner à l'onglet *Paramètres de sécurité* et **re-cocher** l'option *Désactiver les plugins penadnt l'utilisation de Tor* lorsque vous aurez complété votre visite de ces sites.

Pour plus d'information sur les fonctions particulières de chaque option de l'onglet **Paramètres de sécurité**, veuillez consulter la page [**Torbutton**](https://www.torproject.org/torbutton/).

- L'onglet **Paramètres d'affichage**

L'onglet *Paramètres d'affichage* vous permet de déterminer comment s'affiche le **Torbutton** dans la barre d’état de **Firefox**, soit ![](/sbox/screen/tor-fr/34.png) ou ![](/sbox/screen/tor-fr/40.png), ou ![](/sbox/screen/tor-fr/35.png) ou ![](/sbox/screen/tor-fr/41.png). La fonctionnalité opère de façon identique d’une manière ou d’une autre. 

![](/sbox/screen/tor-fr/42.png)

*Figure 7: L'onglet Paramètres d'affichage*

**Conseil**: Lorsque vous avez terminé votre consultation, assurez-vous de supprimer cotre cache de fichiers temporaires et vos cookies. Cela peut être fait dans **Firefox** en **sélectionnant *Outils > Supprimer l'historique récent...*, cochant** toutes les options disponibles dans la fenêtre qui s'affiche, puis en **cliquant** sur le bouton *Effacer maintenant*. Pour plus d'information à ce sujet, veuillez consulter le chapitre du **Guide pratique** portant sur [**Mozilla Firefox**] (/fr/firefox_privacy_and_security).

Pour plus dinformation sur le **Torbutton**, veuillez consulter la page [**Torbutton FAQ**](https://www.torproject.org/torbutton/torbutton-faq.html.en).

<a name="3.3.2"></a>
### 3.3.2 Comment configurer Internet Explorer pour fonctionner avec Tor ###

**Note**: Bien que **Tor** soit conçu pour fonctionner avec n'importe quel navigateur, **Firefox** et **Tor** constituent une combinaison idéale pour éviter d'être détecté par des parties malveillantes ou hostiles. Idéalement, **Internet Explorer** ne devrait être utilisé qu'en dernier ressort!

Cela dit, si vous êtes dans une situation où l'utilisation d'**Internet Explorer** est complètement inévitable, suivez les étapes énumérées ci-dessous: 

**Première étape**. **Ouvrez** le navigateur **Internet Explorer**. 

**Deuxième étape**. **Sélectionnez Outils > Options Internet** pour afficher la fenêtre *Options Internet*.

**Troisième étape**. **Cliquez** sur l'onglet *Connexions* pour afficher la fenêtre illustrée à la *Figure 8* ci-dessous: 

![](/sbox/screen/tor-fr/43.png)

*Figure 8: L'onglet Connexions de la fenêtre Options Internet*

**Quatrième étape**. **Cliquez** sur ![](/sbox/screen/tor-fr/44.png) pour afficher la fenêtre *Paramètres du réseau local* illustrée ci-dessous: 

![](/sbox/screen/tor-fr/45.png)

*Figure 9: La fenêtre des Paramètres du réseau local*

**Cinquième étape**. **Cochez** l'option *Utiliser un serveur proxy...*, tel qu'illustré à la *figure 9* ci-dessus, puis **cliquez** sur ![](/sbox/screen/tor-fr/46.png) pour afficher la fenêtre des *Paramètres du proxy*. 

**Sixième étape**. **Remplissez** les zones des paramètres du proxy tel qu'illustré ci-dessous:

![](/sbox/screen/tor-fr/47.png)

*Figure 10: Un exemple de fenêtre de paramètres du proxy*

**Septième étape**. **Cliquez** sur ![](/sbox/screen/tor-fr/07.png) sur chacune des fenêtres de configuration ci-dessus pour sortir de la fenêtre **Options Internet** et revenir au navigateur **Internet Explorer**.

**Note**: Vous devrez répéter les **étapes 1 à 4** pour cesser d'utiliser **Tor**. Au lieu de l'**étape 5**, vous devriez **désactiver** l'option *Utiliser un serveur proxy...*.

**Conseil**: Vous devez vider le cache des fichiers Internet temporaires et supprimer les cookies et l'historique de navigation à la fin de votre séance de navigation en suivant les étapes énumérées ci-dessous: 

**Première étape**. **Sélectionnez Outils > Options Internet** pour afficher l'onglet *Général* par défaut, tel qu'illustré ci-dessous:

![](/sbox/screen/tor-fr/48.png)

*Figure 11: L'onglet Général des Options Internet d'Internet Explorer*

**Deuxième étape**. **Cliquez** sur ![](/sbox/screen/tor-fr/49.png) dans la section *Historique de navigation* pour afficher la fenêtre *Supprimer l'historique de navigation*:

![](/sbox/screen/tor-fr/50.png)

*Figure 12: la fenêtre Supprimer l'historique de navigation*

**Troisième étape**. **Cochez** *Fichiers Internet temporaires*, *Cookies* et *Historique*.

**Quatrième étape**. **Cliquez** sur ![](/sbox/screen/tor-fr/51.png) pour supprimer les Fichiers Internet temporaires, les Cookies et l'Historique de navigation.

**Note:** Pour accéder au réseau **Tor** avec **Internet Explorer**, vous devez laisser fonctionner le **Navigateur Tor** avec **Vidalia** connecté au réseau **Tor**.

