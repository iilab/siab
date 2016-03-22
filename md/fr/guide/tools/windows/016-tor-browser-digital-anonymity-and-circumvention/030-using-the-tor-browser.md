

---

lang: fr
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: Using the Tor Browser

---

- [**4.0 À propos du Panneau de contrôle de Vidalia**](#4.0)
- [**4.1 Pour visualiser la connexion au réseau Tor**](#4.1)
- [**4.2 Pour visualiser et régler les paramètres du Panneau de contrôle de Vidalia**](#4.2)
- [**4.3 Pour interrompre et relancer le service Tor**](#4.3)

-------

<a name="4.0"></a>
## 4.0 À propos du Panneau de contrôle de Vidalia ##

Le *Panneau de contrôle de Vidalia*, avec lequel vous êtes désormais familier, est le principal interface graphique du programme **Tor**. Le *Panneau de contrôle de Vidalia* vous permet de régler les paramètres principaux de **Tor** et de visualiser les paramètres de connexion.

Pour ouvrir le *Panneau de contrôle de Vidalia*, suivez les étapes énumérées ci-dessous:

**Si le Navigateur Tor est déjà en fonction**, **double-cliquez** sur ![](/sbox/screen/tor-fr/32.png) pour lancer le *Panneau de contrôle de Vidalia*.

**Conseil**: Si vous cliquez à droite sur l'icone représentant un oignon vert, le *Panneau de contrôle de Vidalia* s'affichera sous forme de menu contextuel, tel qu'illustré ci-dessous:

![](/sbox/screen/tor-fr/73.png)

*Figure 1: Le menu contextuel du Panneau de contrôle de Vidalia*

**Si le Navigateur Tor n'est pas déjà en fonction**, **naviguez** jusqu'au dossier du **Navigateur Tor**, puis **double-cliquez** sur ![](/sbox/screen/tor-fr/60.png) pour activer le *Panneau de contrôle de Vidalia* et vous connecter automatiquement au réseau **Tor**, comme suit:

![](/sbox/screen/tor-fr/61.png)

*Figure 2: Le Panneau de contrôle de Vidalia affichant le message Connecté au réseau Tor*

<a name="4.1"></a>
## 4.1 Pour visualiser la connexion au réseau Tor ##

**Première étape**. **Cliquez** sur ![](/sbox/screen/tor-fr/62.png) pour afficher la fenêtre suivante:

![](/sbox/screen/tor-fr/63.png)

*Figure 3: La carte du réseau Tor*

La *Carte du réseau Tor* liste tous les relais **Tor** disponibles qui composent actuellement le réseau de connexion anonyme **Tor**. Le panneau de gauche liste ces serveurs en fonction de leur bande passante disponible et de leur situation géographique.

- **Cliquez** sur ![](/sbox/screen/tor-fr/64.png) pour lister ces serveurs en ordre ascendant ou descendant de la bande passante disponible, ou en ordre alphabétique du pays d'origine.

Sous la mappemonde se trouvent deux panneaux, le panneau *Connexion* et le panneau ou s'affichent les détails du relais. Le panneau *Connexion* affiche les noms des serveurs **Tor** choisis au hasard comme relais de votre connexion anonyme.

- **Choisissez** un serveur dans la liste *Connexion* pour visualiser le trajet emprunté par votre connexion dans le réseau **Tor**, illustré par des lignes vertes sur la carte.

Le panneau adjacent affiche les détails de connexion des serveurs relais listés dans le panneau *Relais* à gauche; à la *Figure 3*, les détails de connexion d'un serveur relais situé au Canada, *zzzzzebra*, sont affichées.

**Note**: La *Carte du réseau Tor* sert à illustrer comment **Tor** fonctionne en présentant des idées abstraites et des renseignements complexes sur un mode graphique.

<a name="4.2"></a>
## 4.2 Pour visualiser et régler les paramètres du Panneau de contrôle de Vidalia ##

**Première étape**. **Cliquez** sur ![](/sbox/screen/tor-fr/65.png) pour afficher la fenêtre suivante:

![](/sbox/screen/tor-fr/66.png)

*Figure 4: La fenêtre des paramètres du Panneau de contrôle de Vidalia*

L'onglet *Général* vous permet d'indiquer si *Vidalia** doit être lancé automatiquement à chaque démarrage de **Windows** et si **Tor** devrait être également lancé à ce moment. 

Si vous préférez lancer le programme **Vidalia** manuellement, vous n'avez qu'à **décocher** l'option *Lancer Vidalia au démarrage du système*.

**Note**: Nous recommandons aux utilisateurs **débutants** ou **moyens** d'accepter les paramètre par défaut, tel qu'illustré à la *Figure 4*.

**Deuxième étape**. **Cliquez** sur ![](/sbox/screen/tor-fr/67.png) pour enregistrer vos paramètres.

Bien que la langue par défaut du programme **Tor** soit l'anglais, l'onglet *Interface* vous permet une autre langue d'interface pour le *Panneau de contrôle de Vidalia*. Cet onglet vous permet en outre de modifier l'apparence du programme. 

![](/sbox/screen/tor-fr/68.png)

*Figure 5: L'onglet Interface des paramètres du Panneau de contrôle de Vidalia*

<a name="4.3"></a>
## 4.3 Pour interrompre et relancer le service Tor ##

**Première étape**. **Cliquez** sur ![](/sbox/screen/tor-fr/69.png) dans le panneau *Raccourcis Vidalia* pour interrompre le programme **Tor**; la section *État* du *Panneau de contrôle de Vidalia* s'affiche alors comme suit:

![](/sbox/screen/tor-fr/70.png)

*Figure 6: La section de l'état de Tor affichant le message Tor est arrêté*

**Deuxième étape**. **Cliquez** sur ![](/sbox/screen/tor-fr/71.png) pour relancer le programme **Tor**; après quelques secondes, la section *État* du *Panneau de contrôle de Vidalia* s'affiche alors comme suit:

![](/sbox/screen/tor-fr/72.png)

*Figure 7: La section de l'état de Tor affichant le message Connecté au réseau Tor!*

