

---

lang: fr
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: Advanced Configurations and Settings

---

Sommaire des sections de cette page:

- [**4.0 Comment accéder aux fenêtres Pare-feu et Defense+**](#4.0)
- [**4.1 La fenêtre Paramètres du comportement du Pare-feu**](#4.1)
- [**4.2 La fenêtre Paramètres Defense+**](#4.2)

-------

<a name="4.0"></a>
## 4.0 Comment accéder aux fenêtres Pare-feu et Defense+ ##

L'interface principale de **COMODO Firewall** est séparée en deux panneaux, le panneau *Pare-feu* et le panneau *Defense+*.

![](/sbox/screen/comodo-fr/80.png)

*Figure 1: L'interface principale de COMODO Firewall affichant les panneaux Pare-feu et Defense+*

On accède aux fenêtres *Paramètres du comportement du Pare-feu* et *Paramètres Defense+* en **cliquant** sur ![](/sbox/screen/comodo-fr/43.png) dans l'un ou l'autre des panneaux pour afficher la fenêtre correspondante et les onglets associés.

On peut également accéder à l'une ou l'autre de ces fenêtres en suivant les étapes énumérées ci-dessous: 

**Première étape**. **Ouvrez** l'interface principale de **COMODO Firewall**. 

**Deuxième étape**. **Cliquez** sur

![](/sbox/screen/comodo-fr/60.png) OU ![](/sbox/screen/comodo-fr/81.png)

pour afficher la fenêtre *Tâches du Pare-feu* ou *Tâches Defense+*, respectivement.

**Troisième étape**. **Cliquez** sur

![](/sbox/screen/comodo-fr/82.png) OU ![](/sbox/screen/comodo-fr/83.png) 

Pour afficher le contenu de l'onglet *Paramètres du comportement du pare-feu* OU celui de l'onglet *Paramètres Defense+*, respectivement.

**Astuce**: Les *Niveau de Sécurité Pare-feu*, *Niveau de Sécurité Defense+* et *Niveau de Sécurité de la Sandbox*, qui sont abordés dans la prochaine section, peuvent être réglés facilement et efficacement en passant par l'icone de connectivité de **COMODO Firewall** qui se trouve dans la *Barre des tâches* Windows. **Cliquez à droite** sur l'icone de connectivité pour afficher le menu contextuel et les sous-menus, tel qu'illustré ci-dessous: 

![](/sbox/screen/comodo-fr/84.png)

*Figure 2: Le menu contextuel de l'icone de connectivité affichant le niveau de sécurité du Pare-feu* 

<a name="4.1"></a>
## 4.1 La fenêtre des paramètres du comportement du Pare-feu ##

La fenêtre **Paramètres du comportement du Pare-feu vous permet de personnaliser le pare-feu avec une panoplie d'options et de fonctionnalités, dont le niveau de sécurité du pare-feu, la fréquence et le type d'alertes à recevoir, ainsi que l'analyse et la surveillance des paquets.

![](/sbox/screen/comodo-fr/44.png)

*Figure 3: La fenêtre Paramètres du comportement du pare-feu - Paramètres généraux*

L'onglet *Paramètres généraux* vous permet de spécifier le niveau de sécurité que vous jugez approprié pour **COMODO Firewall**. Le glisseur vous permet de choisir parmi les niveaux de sécurité suivants:
toutes 
**Bloquez tout**: Ce mode bloque tout le trafic Internet et outrepasse tous les réglages et toutes les règles que vous avez déterminées. Ce mode ne génère aucune règle de trafic pour les applications et n'enregistre pas leur comportement.

**Mode avancé**: Ce mode applique *uniquement* les stratégies de sécurité et de réseautage déterminées par l'utilisateur dans les fenêtres *Tâches Pare-feu > Stratégie de Sécurité Réseau* et *Tâches Dedense+ > Stratégie de Sécurité*.

**Mode sécurisé**: Ce mode est le réglage par défaut de **COMODO Firewall**, y compris les installations *Défense proactive optimale* et *Défense proactive maximale*.

**Astuce**: **COMODO Firewall** maintient une liste interne des applications et fichiers régulièrement utilisés qui ont été définis comme sûrs, et n'émet pas d'alertes pour ceux-ci.

**Avertissement**: Les modes *Apprentissage* et *Désactivé* ne sont pas recommandés car ils peuvent nuire à l'efficacité de **COMODO Firewall** et exposer votre ordinateur à des risques d'infection.

<a name="4.2"></a>
### 4.2 La fenêtre Paramètres Defense+ ###

**Commentaire**: Les fonctionnalités et options décrites dans cette section exigent une compréhension approfondie des pare-feu et des questions de sécurité, et est par conséquent principalement conçu pour les utilisateurs de niveau *avancé*.

**Important**: si vous avez coché l'une ou l'autre des options **Pare-feu avec défense proactive optimale* et *Pare-feu avec défense proactive maximale* lors du processus d'installation de **COMODO Firewall**, le système de prévention des intrusions *Defense+* a été automatiquement activé. Cela dit, si vous avez coché l'option *Pare-feu seulement*, le système *Defense+* peut tout de même être activé manuellement. L'option *Defense+* doit être activée pour que plusieurs des fonctionnalités décrites ci-dessous soient en mesure de fonctionner.

La fonction *Defense+* de **COMODO Firewall**  est un système de prévention des intrusions. Tout ordinateur connecté à un réseau est techniquement un ordinateur hôte. Le système *Defense+* surveille continuellement les activités de tous les fichiers exécutables qui se trouvent actuellement sur votre ordinateur. Un fichier exécutable est une application ou un programme, ou une partie d'un programme, est est habituellement (mais pas nécessairement) identifiable par l'un ou l'autre des extensions de fichiers suivants: *.bat*, *.exe*, *.dll*, *.sys*, ou d'autres. 

*Defense+* émet des alertes chaque fois qu'un fichier exécutable inconnu tente de s'exécuter, et vous demande d'autoriser ou de bloquer son exécution. Ce système peut s'avérer important dans les situations où des logiciels malveillants essaieraient d'installer des applications ou des programmes pour endommager ou voler vos données personnelles, reformater votre disque dur ou  détourner votre système pour propager des programmes malveillants ou du pourriel sans votre consentement ou votre connaissance.

### 4.2.1 La fenêtre Paramètres Defense+ - Onglet Paramètres généraux ###

Pour activer manuellement le système *Defense+* et afficher la fenêtre *Paramètres Defense+*, suivez les étapes énumérées ci-dessous: 

**Première étape**. **Cliquez** sur l'onglet *Defense+* dans l'interface principale de **COMODO Firewall**, puis **cliquez** sur ![](/sbox/screen/comodo-fr/50.png) pour afficher la fenêtre suivante:

![](/sbox/screen/comodo-fr/51.png)

*Figure 6: La fenêtre Defense+ affichant l'onglet Paramètres général par défaut*

**Deuxième étape**. **Faites passer** le glisseur au *Mode sécurisé*, puis **cliquez** sur ![](/sbox/screen/comodo-fr/06.png) pour activer le système *Defense+* tel qu'illustré à la *Figure 6*.

Le *Niveau de Sécurité Defense+* ressemble au *Niveau de sécurité du comportement du Pare-feu*, offre des options similaires, et vous permet d'utiliser le glisseur pour choisir le niveau de protection optimal contre les intrusions.

**Mode Paranoïa**: Ce mode offre le niveau de sécurité le plus élevé; il comprend une surveillance automatique de tous les fichiers exécutables, à part ceux que vous avez définis comme sûrs, y compris ceux inclus dans la liste des *Éditeurs de logiciels certifiés*. Ce mode comporte la plus haute fréquence d'alertes de sécurité, et l'activité du système est filtrée à travers les paramètres de votre configuration.

**Mode sécurisé**: Ce mode 'apprend' automatiquement les comportements des différentes applications exécutables, tout en surveillant les activités critiques du système. Toutes les applications non certifiées génèrent une *Alerte de sécurité* chaque fois qu'elles sont mises en exécution. Ce mode est le plus recommandé pour la majorité des utilisateurs.

- L'option *Bloquer toutes les requêtes inconnues si l'application est fermée* bloque automatiquement toutes les requêtes émises par des applications et des programmes inconnus, ou que vous n'avez pas spécifié dans votre *Stratégie de sécurité*. 

- L'option *Désactiver Defense+ de façon permanent (nécessite un redémarrage)* vous permet de désactiver manuellement le système de prévention des intrusions * Defense+*. Cette option n'est généralement pas recommandée.

### 4.2.2 Les paramètres Defense+ - Onglet Réglages du contrôle des exécutables  ###

L'onglet *Réglages du contrôle des exécutables* limite l'auto-exécution des fichiers suspects ou inconnus (ainsi que leur accès aux ressources de votre ordinateur), et soumet ceux-ci à une analyse. 

![](/sbox/screen/comodo-fr/54.png)

*Figure 7: L'onglet Réglages du contrôle des exécutables*

**Astuce**: Les utilisateurs de niveau **avancé** peuvent créer des exclusions aux tâches susmentionnées en cliquant sur ![](/sbox/screen/comodo-fr/55.png) pour afficher le panneau *Exclusions* et sélectionner différents processus et programmes à exclure.

**Commentaire**: Les utilisateurs de niveau **expérimenté** et **avancé** sont fortement encouragés à **cliquer** sur ![](/sbox/screen/comodo-fr/47.png) pour accéder aux fiches d'aide en ligne de **COMODO** qui concernent les onglets *Réglages du contrôle des exécutables*, les *Paramètres de la Sandbox* et les *Paramètres de surveillance*. Vous pouvez également vous référer à **http://help.comodo.com/topic-72-1-155-1074-Introduction-to-Comodo-Internet-Security.html** pour choisir une fiche à partir d'une liste de rubriques d'aides en ligne.





