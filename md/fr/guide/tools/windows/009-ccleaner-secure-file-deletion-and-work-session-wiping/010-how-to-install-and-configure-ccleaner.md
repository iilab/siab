

---

lang: fr
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: How to Install and Configure CCleaner

---

Sommaire des sections de cette page:  

- [**2.0 Comment installer CCleaner**](#2.0)
- [**2.1 Avant de commencer à configurer CCleaner**](#2.1)
- [**2.2 Comment configurer CCleaner**](#2.2)

----

<a name="2.0"></a>
### 2.0 Comment installer CCleaner ###

L'installation de **CCleaner** est relativement simple et rapide. Pour lancer l'installation de **CCleaner**, suivez les étapes énumérées ci-dessous:

**Première étape**. **Double-cliquez** sur ![](/sbox/screen/ccleaner-fr/01.png) pour lancer le processus d'installation. Il est possible que s'ouvre une boîte de dialogue *Fichier ouvert - Avertissement de sécurité*. Si c'est le cas, **cliquez** sur ![](/sbox/screen/ccleaner-fr/02.png) pour afficher la fenêtre suivante:

![](/sbox/screen/ccleaner-fr/03.png)

*Figure 1: Bienvenue dans le programme d'installation de CCleaner v4.03*

**Deuxième étape**. **Cliquez** sur ![](/sbox/screen/ccleaner-fr/06.png) pour afficher la fenêtre *Options d’installation*, puis **cliquez** à nouveau sur ![](/sbox/screen/ccleaner-fr/06.png) pour afficher la fenêtre suivante :

![](/sbox/screen/ccleaner-fr/10.png)

*Figure 2: La fenêtre sans titre d’installation de Google Chrome défini comme navigateur par défaut*

**Troisième étape**. **Cliquez** sur *Installer Google Chrome en le définissant comme navigateur par défaut* comme présenté ci-dessus pour l’empêcher de s’installer automatiquement sur votre ordinateur. Notez que cette fenêtre peut ne pas apparaître au cours de votre installation.

**Quatrième étape**. **Cliquez** sur ![](/sbox/screen/ccleaner-fr/11.png) pour activer la fenêtre *Installation en cours* affichant la barre d'état de progression de l'installation.

**Cinquième étape**. **Cliquez** sur ![](/sbox/screen/ccleaner-fr/13.png) pour finaliser l'installation de **CCleaner** et activer le message pop-up suivant :

*Figure 3: Le message pop-up proposant le scanner intelligent de cookies*

**Sixième étape**. **Cliquez** sur **NON** pour éviter de stocker des cookies en permanence sur votre ordinateur et activer l'interface utilisateur de *Piriform CCleaner*.

![](/sbox/screen/ccleaner-fr/15.png)

*Figure 4: L'interface utilisateur de Piriform CCleaner*

<a name="2.1"></a>
### 2.1 Avant de commencer à configurer CCleaner ###

Tel que décrit en détail dans le chapitre [6. Détruire définitivement des données sensibles](/fr/chapter-6) du Livret pratique, les méthodes standard de suppressions de fichiers de **Microsoft Windows** ne suppriment pas réellement les données du disque (et ce, même lorsque vous videz votre "Corbeille*). Même chose pour les fichiers temporaires. Pour supprimer ces fichiers de façon permanente du disque dur (ce qu'on appelle *nettoyer* ou *effacer* le disque), il faut écraser les données en question avec des données aléatoires. **CCleaner** doit être configuré pour écraser les fichiers qu'il supprime et ainsi les nettoyer de façon sécuritaire, le programme n'est pas réglé de cette façon par défaut. **CCleaner** peut également supprimer de vieilles données inutiles en nettoyant l'espace libre de votre disque dur (veuillez consulter la section **5.3 Comment nettoyer l'espace disque libre avec CCleaner**).

<a name="2.2"></a>
### 2.2 Comment configurer CCleaner ###

Avant de commencer à utiliser **CCleaner**, vous devriez le régler pour être en mesure de supprimer les fichiers temporaires de façon permanente et sécuritaire.

Pour configurer CCleaner, suivez les étapes suivantes:

**Première étape**. **Cliquez** sur ![](/sbox/screen/ccleaner-fr/20.png) ou **sélectionnez Démarrer > Programmes > CCleaner** pour afficher l'interface principale de *Piriform CCleaner*.

**Deuxième étape**. **Cliquez** sur ![](/sbox/screen/ccleaner-fr/22.png) pour afficher la fenêtre suivante:

![](/sbox/screen/ccleaner-fr/21.png)

*Figure 5: L'onglet Options affichant le panneau À propos par défaut*

**Troisième étape**. **Cliquez** sur ![](/sbox/screen/ccleaner-fr/23.png) pour afficher le panneau *Paramètres*. Le panneau *Paramètres* vous permet de choisir votre langue de travail et de déterminer comment **CCleaner** supprimera les fichiers temporaires et nettoiera vos disques.

**Commentaire:** La section *Effacement sécurisé* s'affiche avec l'option *Effacement normal de fichiers* sélectionnée par défaut.

**Quatrième étape**. **Cliquez** sur l'option *Effacement sécurisé (Lent)* pour activer le menu déroulant.

**Cinquième étape. Développez** le menu déroulant d'*Effacement sécurisé de fichiers* et **sélectionnez** l'item *Écrasement avancé* (3 passages) comme dans la fenêtre suivante: 

![](/sbox/screen/ccleaner-fr/24.png)

*Figure 6: Le panneau Paramètres affichant les options d'Effacement sécurisé*

Après avoir configuré cette option, **CCleaner** écrasera les fichiers et dossiers que vous voulez supprimer avec des données aléatoires, ce qui les effacera de façon permanente. Les *Passages* du menu déroulant *Effacement sécurisé* réfère au nombre de fois que les données à effacer seront écrasées par des données aléatoires. Plus le nombre de passages est élevé, plus vos documents, fichiers ou dossiers seront écrasés avec des données aléatoires. Cela réduit considérablement la possibilité de restaurer ces documents, fichiers ou dossiers, mais cela augmente le temps de traitement requis par le processus d'effacement.


