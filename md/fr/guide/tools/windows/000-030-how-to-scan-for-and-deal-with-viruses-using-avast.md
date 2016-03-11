

---

lang: fr
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: How to Scan for and Deal with Viruses Using avast!

---

Sommaire des sections de cette page:  

- [**4.0 Avant de commencer**](#4.0)
- [**4.1 Comment faire face efficacement à une attaque de virus**](#4.1)
- [**4.2 Un survol de l'interface principale d'avast!**](#4.2)
- [**4.3 Comment balayer votre ordinateur pour détecter des programmes malveillants et des virus**](#4.3)
- [**4.4 Comment exécuter un Scan minutieux du système**](#4.4)
- [**4.5 Comment exécuter un Scan de dossiers**](#4.5)
- [**4.6 Comment exécuter un Scan au démarrage**](#4.6)
- [**4.7 Comment gérer les virus détectés**](#4.7)
- [**4.8 Comment utiliser la Zone de quarantaine**](#4.8)
- [**4.9 Méthodes avancées de suppression de virus**](#4.9)

----
<a name="4.0"></a>
### 4.0 Avant de commencer ###
Le traitement efficace des virus et logiciels malveillants à l'aide d'**avast!** comporte deux étapes importantes. Il vous faut d'abord balayer (ou scanner) votre ordinateur pour détecter les menaces. Il faut ensuite éliminer les menaces ou les délacer vers la *Zone de quarantaine* d'**avast!**. La suppression et/ou le déplacement des virus et logiciels malveillants empêche ceux-ci d'interagir avec d'autres systèmes, tel que le système de fichiers ou les programmes de gestion du courrier électronique.

Il peut paraître étrange de sauvegarder de tels virus ou logiciels malveillants. Mais si ceux-ci se sont attachés à des données importantes ou sensibles, vous voudrez peut-être ultérieurement récupérer ou sauvegarder ces documents, fichiers ou programmes infectés. Dans de rares cas, **avast!** peut se tromper en identifiant des codes et programmes légitimes comme malveillants. Généralement appelés *faux positifs*, ces codes ou programmes sont potentiellement important pour le bon fonctionnement de votre système, il vous faudra peut-être les récupérer ultérieurement.

La *Zone de quarantaine* d'**avast!** est un espace virtuel où vous pouvez examiner un virus et déterminer s'il constitue une authentique menace, soit en effectuant une recherche sur Internet, soit en le soumettant à l'attention d'un laboratoire spécialisé (une option qui s'offre à vous dans **avast!** en cliquant à droite sur un virus listé dans la *Zone de quarantaine*. Cette opération *n'activera pas* le virus ou le logiciel malveillant en question car la *Zone de quarantaine* l'isole du reste de votre système.

**Astuce**: À l'inverse, la *Zone de quarantaine* d'**avast!** peut être utilisée pour y transférer des données importantes ou sensibles et les mettre à l'abri en cas d'attaque de virus.

Dans cette section:

- Nous étudierons les pratiques exemplaires pour protéger votre réseau et/ou votre ordinateur personnel;
- Nous explorerons l'interface principale, et en particulier les onglets LANCER UN SCAN et MAINTENANCE;
- Nous verrons comment exécuter les divers types de scans; et
- Nous verrons comment utiliser la *Zone de quarantaine* d'**avast!**.

<a name="4.1"></a>
### 4.1 Comment faire face efficacement à une attaque de virus ###

Il y a un ensemble de précautions élémentaires que vous pouvez prendre pour limiter les menaces contre votre ordinateur; par exemple, en évitant les sites douteux ou problématiques ou en utilisant régulièrement des logiciels anti-mouchard et antivirus comme **avast!** et **Spybot**. Cela dit, il est possible que notre système personnel fasse partie d'un réseau local (LAN) et/ou que l'on partage une connexion Internet. Les considérations qui suivent concernent les façons de réagir efficacement à une attaque de virus lorsque plusieurs ordinateurs sont en réseau, que ce soit en contexte communautaire ou au travail.

- Déconnectez physiquement votre ordinateur d'Internet et du réseau local. Si vous utilisez une connexion sans fil, déconnectez votre ordinateur du réseau sans fil. Si possible, éteignez la machine et retirez la carte de communications sans fil.

- Si votre ordinateur fait partie d'un réseau, vous devriez immédiatement déconnecter tous les ordinateurs d'Internet et du réseau lui-même. Chaque utilisateur devrait cesser d'utiliser le réseau et lancer **avast!** ou un autre programme antivirus fiable afin de détecter et éliminer le virus. Cela peut sembler laborieux, mais cette procédure est essentielle à la protection des ordinateurs personnels et du réseau.

- Planifiez un Scan au prochain démarrage pour chaque ordinateur du réseau. Notez bien le nom de chaque virus détecté, de sorte que vous puissiez effectuer une recherche, puis supprimez-les ou déplaces-les vers la *Zone de quarantaine* d'**avast!**. Pour vous familiariser avec cette procédure, veuillez consulter la section **4.6 Comment exécuter un Scan au démarrage**.

- Même si un virus a été détecté ou réparé, répétez les étapes précédentes et lancez un scan au démarrage sur *chaque* ordinateur, jusqu'à ce qu'**avast!** n'affiche plus aucun message d'avertissement. Selon la gravité de l'attaque, il est possible qu'un seul scan au démarrage suffise.

Pour plus de renseignements sur les moyens de défense contre les virus et les logiciels malveillants, veuillez consulter la section **4.9 Méthodes avancées de suppression de virus**

<a name="4.2"></a>
### 4.2 Un survol de l'interface principale d'avast! ###

L'interface utilisateur d'**avast!** comporte quatre onglets principaux, situés à la gauche de la fenêtre: RÉSUMÉ, LANCER UN SCAN, PROTECTION RÉSIDENTE et MAINTENANCE. Chaque onglet est divisé en sous-onglets qui permettent d'afficher les panneaux correspondants.

**Première étape**. **Cliquez** sur ![](/sbox/screen/avast-fr/60.png) pour afficher la fenêtre ci-dessous:

![](/sbox/screen/avast-fr/61.png)

*Figure 1: L'onglet RÉSUMÉ affichant le panneau État actuel SÉCURISÉ*

La liste ci-dessous détaille brièvement les fonctions des quatre onglets principaux: 

**RÉSUMÉ**: Cet onglet comprend les sous-onglets *État actuel* et *Statistiques*. Le sous-onglet *État actuel* affiche l'état des composantes principales utilisées par **avast!** pour défendre votre ordinateur contre les virus et autres attaques. Le panneau *Statistiques* affiche les opérations des composantes d'**avast!**. Affichage par semaine, mois ou année.

**LANCER UN SCAN**: Cet onglet comporte les sous-onglets *Scanner maintenant*, *Scan au démarrage* et *Rapports de scans*. Le panneau *SCANNER MAINTENANT* affiche les différentes options de scan manuels. Le panneau *SCAN AU DÉMARRAGE* vous permet de planifier un scan au prochain démarrage de votre ordinateur. Le panneau *RAPPORTS DE SCANS* affiche un rapport des scans manuels effectués, sous forme de tableau.

**PROTECTION RÉSIDENTE**: Cet onglet affiche tous les agents de protection associés aux fonctions de votre ordinateur, dont l'*AGENT DES FICHIERS*. Vous avez ici un accès direct aux réglages des agents de protection, y compris les boutons pour les arrêter et les démarrer.

**MAINTENANCE**: Cet onglet comporte les sous-onglets *Mise à jour*, *Enregistrement*, *Zone de quarantaine* et *À propos d'avast!*. Le panneau *MISE À JOUR* vous permet de lancer manuellement des mises à jour du programme et des définitions de virus. Le panneau *ENREGISTREMENT* vous permet d'enregistrer votre copie d'**avast!**. Le panneau *ZONE DE QUARANTAINE* affiche les virus et logiciels malveillants détectés par **avast!** lors des scans et vous permet de les gérer de différentes façons, soit en les supprimant, en lançant de nouveaux scans ou en soumettant les virus détectés à l'analyse de laboratoires spécialisés. Le panneau *À PROPOS D'AVAST* affiche des renseignements sur la plus récente version d'**avast!** installée sur votre ordinateur.

**Commentaire**: Les panneaux *LANCER UN SCAN* et *MAINTENANCE* sont particulièrement pratiques pour traiter les menaces posées par des virus et des logiciels malveillants.

<a name="4.3"></a>
### 4.3 Comment balayer votre ordinateur pour détecter des programmes malveillants et des virus ###

Dans cette section, nous examinerons les différentes options de scan disponibles, ainsi que leur mode d'emploi. Nous verrons également comment lancer un scan du système, un scan de dossiers et un scan au démarrage.

Le panneau *LANCER UN SCAN > SCANNER MAINTENANT* présente les quatre options de scan offertes par **avast!**; pour les afficher, suivez les étapes décrites ci-dessous:

**Première étape**. **Cliquez** sur ![](/sbox/screen/avast-fr/62.png) pour afficher la fenêtre suivante:

![](/sbox/screen/avast-fr/63.png)

*Figure 2: L'onglet LANCER UN SCAN affichant le panneau SCANNER MAINTENANT*

Les descriptions suivantes vous aideront à choisir le mode de scan le plus approprié:

**Scan rapide**: Cette option est recommandée aux utilisateurs qui ont peu de temps pour détecter de potentielles menaces.

**Scan minutieux**: Cette option est recommandées aux utilisateurs qui ont assez de temps pour lancer un scan minutieux de leur système. Ce mode est également recommandé si vous utilisez le programme antivirus pour la première fois sur votre ordinateur. La durée de ce scan dépend du nombre de documents, de fichiers, de dossiers et de disques durs sur votre ordinateur, ainsi que la vitesse de la machine. Veuillez consulter la section **4.4 Comment exécuter un Scan minutieux du système**.

**Scan des médias amovibles**: Cette option est recommandée pour scanner des disques durs externes, des clés USB et d'autres dispositifs ou supports amovibles, en particulier ceux qui ne vous appartiennent pas. **avast!** tentera de détecter des programmes malveillants conçus pour s'exécuter lorsque le dispositif est connecté.

**Scan des dossiers sélectionnés**: Cette option est recommandée pour scanner un ou plusieurs dossiers en particulier. Cette option est utile si vous soupçonnez qu'un fichier ou un dossier est infecté. Veuillez consulter la section **4.5 Comment exécuter un Scan de dossiers**.

**Astuce**: Chaque option de scan vous permet de voir les détails du scan, par exemple, les secteurs qui sont actuellement balayés. **Cliquez** sur ![](/sbox/screen/avast-fr/84.png) pour les afficher. Si vous êtes un utilisateur avancé ou expert, **cliquez** sur ![](/sbox/screen/avast-fr/85.png) pour raffiner les réglages pour chaque mode de scan.

<a name="4.4"></a>
### 4.4 Comment exécuter un Scan minutieux du système ###

Pour lancer un scan minutieux du système, suivez les étapes décrites ci-dessous: 

**Première étape**. **Cliquez** sur ![](/sbox/screen/avast-fr/64.png) dans la rubrique du mode *Scan minutieux* pour afficher la fenêtre suivante: 

![](/sbox/screen/avast-fr/65.png)

*Figure 3: Le panneau SCANNER MAINTENANT affichant le scan minutieux en cours d'exécution* 

À l'issue du scan minutieux, si une menace a été détectée sur votre ordinateur le panneau *Scan minutieux* ressemblera à ceci: 

![](/sbox/screen/avast-fr/66.png)

*Figure 4: La rubrique Scan complété affichant un avertissement MENACE DÉTECTÉE!*

Le scan minutieux du système a détecté quelques menaces; pour savoir quoi faire à partir de là, veuillez consulter la section [**4.7 Comment gérer les virus détectés**](#4.7).

La *Zone de quarantaine* d'**avast!** est un dossier mis en place lors du processus d'installation d'**avast!**; c'est une zone de quarantaine virtuelle où les virus et les logiciels malveillants sont isolés de telle sorte qu'ils ne peuvent pas interagir avec, ou parasiter, les autres processus en cours sur votre ordinateur.

<a name="4.5"></a>
### 4.5 Comment exécuter un Scan de dossiers ###

Pour scanner vos dossiers, suivez les étapes décrites ci-dessous:

**Première étape**. **Cliquez** sur ![](/sbox/screen/avast-fr/64.png) dans la rubrique du mode *Scan des dossiers sélectionnés* pour afficher la fenêtre suivante:

![](/sbox/screen/avast-fr/86.png)

*Figure 5: La boîte de dialogue Sélection des zones*

La boîte de dialogue *Sélection des zones* vous permet de choisir le dossier que vous souhaitez scanner. Vous pouvez également sélectionner plus d'un dossier. Lorsque vous cochez la case correspondant à chaque dossier, le chemin d'accès du dossier s'affiche dans le champs *Chemins d'accès choisis:*.

**Deuxième étape**. **Cliquez** sur ![](/sbox/screen/avast-fr/87.png) pour lancer le scan de vos dossiers et afficher la fenêtre suivante:

![](/sbox/screen/avast-fr/88.png)

*Figure 6: Le Scan de dossiers en cours d'exécution* 

**Astuce**: **avast!** vous permet de scanner des dossiers à partir du menu local *Windows* standard qui s'affiche lorsque vous cliquez à droite sur un dossier donné. Vous n'avez qu'à **sélectionner** l'icone ![](/sbox/screen/avast-fr/13.png) qui apparaît à côté du nom du dossier que vous souhaitez scanner.

<a name="4.6"></a>
### 4.6 Comment exécuter un Scan au démarrage ###

Le scan au démarrage d'**avast!** vous permet de planifier un scan complet de votre disque dur avant que le *Système d'exploitation Windows de Microsoft* ne soit mis en exécution. Au moment où le scan au démarrage s'exécute, la majorité des programmes malveillants sont toujours en dormance, c'est-à-dire, qu'ils n'ont pas encore eu l'occasion de s'activer ou d'interagir avec d'autres processus du système. C'est pourquoi ils sont plus facilement détectables à cette étape.

Le scan au démarrage accède directement au disque sans passer par les pilotes du système de fichier **Windows**, une cible de premier choix pour la plupart des programmes malveillants. Un scan au démarrage devrait être en mesure de détecter même les plus agressifs des "rootkits" (c'est le nom employé pour désigner un type de logiciel malveillant particulièrement pernicieux). Il est **fortement recommandé** de planifier un scan au démarrage si vous avez le moindre soupçon que votre système a été compromis ou infecté. 

L'option *Scan au démarrage* est recommandée pour un scan complet et minutieux de votre système. Le scan peut prendre un certain temps, selon la vitesse de votre ordinateur, la quantité de données à examiner et le nombre de disques dur branchés à votre ordinateur. Le *Scan au démarrage* est toujours planifié pour le prochain redémarrage de votre ordinateur. 

Pour scanner votre système au prochain démarrage, suivez les étapes décrites ci-dessous: 

**Première étape**. **Cliquez** sur ![](/sbox/screen/avast-fr/67.png) pour afficher le panneau *SCAN AU DÉMARRAGE*.

**Deuxième étape**. **Cliquez** sur ![](/sbox/screen/avast-fr/68.png) pour planifier un scan au prochain démarrage de votre ordinateur.

**Troisième étape**. **Cliquez** sur ![](/sbox/screen/avast-fr/69.png) pour lancer le scan au démarrage immédiatement si vous préférez. 

**Commentaire**: Un scan au démarrage s'exécute avant que le système d'exploitation et l'interface utilisateur ne soient chargés. C'est pourquoi vous ne verrez qu'un écran bleu affichant le progrès du scan, tel qu'illustré ci-dessous:

![](/sites/securitybkp.ngoinabox.org/files/u5/Avast_3_2_6.png)

*Figure 7: Le scan au démarrage planifié d'avast!*

Chaque fois qu'**avast!** détecte une menace, le programme vous demande si vous voulez *Supprimer*, *Ignorer*, *Mettre en quarantaine* ou *Réparer* les virus détectés. Il est recommandé de ne *jamais* les ignorer. La liste de ces commandes n'apparaît uniquement que si un virus est détecté sur votre système.

<a name="4.7"></a>
### 4.7 Comment gérer les virus détectés ###

Lors du processus d'installation d'**avast!**, la *Zone de quarantaine* d'**avast!** a été créée sur votre disque dur. La *Zone de quarantaine* n'est ni plus ni moins qu'un dossier qui est isolé du reste de votre système et utilisé pour stocker les logiciels malveillants ou les virus détectés au cours du scan, ainsi que les documents, fichiers et dossiers infectés ou compromis.

Si vous avez déjà mis à jour le programme et la base de données virale, vous êtes déjà familier avec l'onglet *MAINTENANCE*, par lequel vous pouvez également accéder à la *Zone de quarantaine* d'**avast!**.
 
Pour gérer adéquatement les virus et logiciels malveillants détectés lors du scan, suivez les étapes décrites ci-dessous: 

**Première étape**. **Cliquez** sur ![](/sbox/screen/avast-fr/70.png) pour afficher la fenêtre suivante:

![](/sbox/screen/avast-fr/71.png)

*Figure 8: La fenêtre RÉSULTATS DU SCAN affichant le message d'avertissement MENACE DÉTECTÉE!*

**Deuxième étape**. **Cliquez** sur ![](/sbox/screen/avast-fr/72.png) pour afficher le menu déroulant présentant la liste des actions qui peuvent être appliquées aux menaces détectées, tel qu'illustré à la *Figure 8*, ci-dessus.

**Commentaire**: Dans cet exercice, nous voulons déplacer les fichiers infectés vers la *Zone de quarantaine*. Cependant, le menu déroulant présente trois autres options que nous décrivons sommairement ci-dessous:

**Réparer**: Cette action tentera de réparer le fichier infecté.

**Supprimer**: Cette action supprimera de façon permanente le fichier infecté.

**Ne rien faire**: Cette action *n'est définitivement pas recommandée* lorsqu'il est question de gérer adéquatement des virus ou des programmes malveillants.

**Troisième étape**. **Sélectionnez** l'action *Déplacer vers la zone de quarantaine*, puis  **cliquez** sur ![](/sbox/screen/avast-fr/74.png)  pour afficher la fenêtre ci-dessous:

![](/sbox/screen/avast-fr/75.png)

*Figure 9: Les virus ont été déplacés vers la Zone de quarantaine*

<a name="4.8"></a>
### 4.8 Comment utiliser la Zone de quarantaine ###

Maintenant que le virus a été délacé vers la *Zone de quarantaine* d'**avast!**, vous pouvez déterminer quelle est la meilleure chose à faire.

**Première étape**. **Cliquez** sur ![](/sbox/screen/avast-fr/80.png) puis **cliquez** sur ![](/sbox/screen/avast-fr/81.png) pour afficher la fenêtre ci-dessous:

![](/sbox/screen/avast-fr/82.png)

*Figure 10: La Zone de quarantaine affichant deux virus*

**Deuxième étape**: **Cliquez à droite** sur un des virus pour afficher le menu des actions possibles, tel qu'illustré ci-dessous:

![](/sbox/screen/avast-fr/83.png)

*Figure 11: Le menu déroulant des actions à appliquer aux virus dans la Zone de quarantaine*

**Commentaire**: Vous n'activerez pas un virus en double-cliquant dessus dans la *Zone de quarantaine*. Cette action affichera plutôt les propriétés du virus, de la même façon que si vous cliquiez sur l'option *Propriétés* dans le menu local.

La liste ci-dessous décrit les différentes actions du menu déroulant: 

**Supprimer**: Cette action supprimera le virus de façon irréversible.

**Restaurer**: Cette action restaurera les virus à leur emplacement initial.

**Extraire...**: Cette action copiera le fichier ou le virus dans un dossier de votre choix.

**Scan**: Cette action soumettra le virus à un nouveau scan.

**Envoyer à AVAST Software...**: Cette action vous permet de soumettre le virus à une analyse plus poussée. En sélectionnant cette action, vous activerez un formulaire à remplir et à envoyer.

**Propriétés**: Cette action vous permet d'afficher plus de détails concernant le virus en question.

**Ajouter...**: Cette action vous permet de naviguer dans votre système pour chercher d'autres fichiers que vous aimeriez déplacer vers la *Zone de quarantaine*. Cette fonction pourrait s'avérer très utile pour protéger certains fichiers lors d'une attaque de virus.

**Actualiser tous fichiers**: Cette action permet d'opérer une mise à jour des fichiers pour être certain d'afficher les fichiers les plus récents.

<a name="4.9"></a>
### 4.9 Méthodes avancées de suppression de virus ###

Dans certains cas, la protection fournie par **avast!**, **Comodo Firewall** et **Spybot** n'est tout simplement pas suffisante. Malgré nos efforts les plus rigoureux, nos ordinateurs personnels et de travail sont parfois infectés par des programmes malveillants et des virus. Dans la section **4.1 Comment faire face efficacement à une attaque de virus**, nous avons vu quelques méthodes pour faire face aux virus les plus coriaces. Mais il existe d'autres mesures qui peuvent être mises en place pour éliminer complètement ces menaces.

**Méthode A: Utiliser des CD/DVD de secours anti-logiciel malveillant (Rescue CD)**

Certaines des compagnies qui développent des outils contre les programmes malveillants offrent également des CD/DVD de secours, ou Rescue CD/DVD. On peut les télécharger sous forme d'images ISO (un format qui peut être facilement gravé sur un disque CD ou DVD).

Pour utiliser un CD ou un DVD anti-programme malveillant, veuillez suivre les étapes décrites ci-dessous:

1. Téléchargez et gravez le programme anti-logiciel malveillant sur un CD.
*Vous pouvez utiliser un logiciel gratuit comme [**ImgBurn**](http://www.imgburn.com/) pour graver l'image sur un disque.*

2. Insérez le disque dans le lecteur de CD/DVD de l'ordinateur infecté, puis redémarrez l'ordinateur à partir du CD/DVD.
*Habituellement, vous pouvez démarrer à partir d'un disque en appuyant sur la touche F10 ou F12 du clavier immédiatement après avoir allumé l'ordinateur. Soyez très attentif aux consignes qui s'affichent sur l'écran lors du démarrage pour connaître la méthode appropriée sur votre ordinateur.*

3. Connectez votre ordinateur à Internet pour permettre au programme anti-logiciel malveillant de mettre à jour ses définitions de virus, si nécessaire. Le programme se mettra automatiquement à la recherche des menaces sur votre ordinateur, puis il les supprimera au fur et à mesure.

Voici une liste d'images de CD de secours:

- [**AVG Rescue CD**](http://www.avg.com/us-en/avg-rescue-cd)
- [**Kaspersky Rescue CD**](http://support.kaspersky.com/viruses/rescuedisk/)
- [**F-Secure Rescue CD**](http://www.f-secure.com/linux-weblog/files/f-secure-rescue-cd-release-3.00.zip)
- [**BitDefender Rescue CD**](http://download.bitdefender.com/rescue_cd/)

Il peut aussi être utile de scanner votre ordinateur à l'aide des outils suivants, qui se mettent en marche au démarrage de **Windows OS**. Par contre, ces outils ne s'exécuteront que si les virus qui infectent votre ordinateur ne les empêchent pas de fonctionner normalement.

- [**HijackThis**](http://free.antivirus.com/hijackthis/) et d'autres outils gratuits [Clean-up Tools](http://free.antivirus.com/clean-up-tools/) de la compagnie **Trend Micro**.
- [**RootkitRevealer**](http://technet.microsoft.com/en-us/sysinternals/bb897445.aspx) de [Sysinternals](http://technet.microsoft.com/en-us/sysinternals) de **Microsoft**.

**Commentaire:** Il est possible d'utiliser les outils listés ci-dessus séparément pour maximiser vos chances de nettoyer votre ordinateur complètement.

**Méthode B: Réinstaller le système d'exploitation Windows de Microsoft**

***Commentaire**: Avant d'entamer le processus de réinstallation, assurez vous de disposer de tous les numéros de série et licences nécessaires, ainsi que des copies d'installation de **Windows OS** et de tous les programmes dont vous avez besoin. Ce processus peut prendre un certain temps mais en vaut l'effort si vous n'avez pas réussi à éliminer toutes les menaces avec les autres méthodes.*

Dans de rares cas, une infection peut s'avérer tellement destructrice que les logiciels recommandés ci-dessus s'avèrent impuissants. Dans de telles situations, il est recommandé de suivre les étapes énumérées ci-dessous: 

1. Créer une copie de sauvegarde de tous vos fichiers personnels. 

2. Réinstaller le système d'exploitation **Microsoft Windows** en formatant le disque au complet.

3. Mettre à jour le système d'exploitation **Microsoft Windows** immédiatement après l'installation. 

4. Installer **avast!** (ou un autre programme antivirus recommandé) et le mettre à jour.

5. Installer tous les programmes dont vous avez besoin et télécharger les plus récentes versions, ainsi que toutes les mises à jour pour chaque programme.

   **IMPORTANT**: Vous ne devriez *jamais* insérer votre disque de sauvegarde dans le lecteur de votre ordinateur *avant* d'avoir compléter toutes ces tâches. Vous risqueriez ainsi de ré-infecter votre ordinateur.

6. Insérez votre copie de sauvegarde dans le lecteur de l'ordinateur et exécutez un scan minutieux pour détecter et éliminer tous les problèmes potentiels.

7. Lorsque vous aurez détecté et supprimé tous les problèmes, vous pourrez copier vos fichiers du disque de sauvegarde vers votre disque dur.

