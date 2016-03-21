

---

lang: fr
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Perform Different Scans Using Recuva

---

Sommaire des sections de cette page:  

- [**3.0 Avant de commencer**](#3.0)
- [**3.1 Comment exécuter un scan avec l'assistant de Recuva**](#3.1)
- [**3.2 Comment exécuter un scan sans utiliser l'assistant de Recuva**](#3.2)
- [**3.3 Comment exécuter une Analyse approfondie avec Recuva**](#3.3)
- [**3.4 Une introduction à la fenêtre Options**](#3.4)

----

<a name="3.0"></a>
### 3.0 Avant de commencer ###

Dans cette section, nous verrons comment lancer différent types de scans et nous examinerons les onglets *Général* et *Actions* de la fenêtre *Options*.

**Commentaire**: Un scan ne fait que retrouver et afficher les fichiers récupérables. Le processus de récupération comme tel sera examiné à la section [**4.0 Comment récupérer et effacer des fichiers de façon sécuritaire avec Recuva**](/fr/recuva_recuperer). 

<a name="3.1"></a>
### 3.1 Comment exécuter un scan avec l'assistant de Recuva###

L'*Assistant* de **Recuva** est recommandé dans les situations ou le nom du fichier à récupérer n'est pas connu. Ce mode est également recommandé si vous utilisez **Recuva** pour la première fois. L'*Assistant* de **Recuva** vous laisse régler les paramètres du scan en vous permettant de spécifier le type de fichier et/ou l'emplacement original du fichier supprimé.

Pour commencer à chercher les fichiers supprimés, suivez les étapes énumérées ci-dessous:

**Première étape**. **Cliquez** sur ![](/sbox/screen/recuva-fr/15.png) ou **sélectionnez Démarrer > Programmes > Recuva > Recuva** pour lancer le programme et afficher la fenêtre suivante:

![](/sbox/screen/recuva-fr/16.png)

*Figure 1: La fenêtre Bienvenue dans l'assistant de Recuva*

**Astuce**: Si vous connaissez le nom du fichier que vous souhaitez récupérer, au complet ou en partie, **cliquez** sur ![](/sbox/screen/recuva-fr/17.png) pour vous afficher l'interface  principale de *Piriform Recuva*. Vous n'avez ensuite qu'à suivre les consignes décrites à la section  **3.2 Comment exécuter un scan sans utiliser l'assistant de Recuva**.

**Deuxième étape**. **Cliquez** sur ![](/sbox/screen/recuva-fr/18.png) pour afficher la fenêtre suivante:

![](/sbox/screen/recuva-fr/19.png)

*Figure 2: La fenêtre Type de fichiers de l'assistant de Recuva*

La fenêtre *Type de fichiers* affiche une liste des différents types de fichiers et décrit quels fichiers peuvent être récupérés lorsque l'une ou l'autre des options est sélectionnée.

**Troisième étape**. **Cochez** l'option *autre*, tel qu'illustré à la *Figure 2*, puis **cliquez** sur ![](/sbox/screen/recuva-fr/18.png) pour afficher la fenêtre suivante:

![](/sbox/screen/recuva-fr/20.png)

*Figure 3: La fenêtre Emplacement du fichier de l'Assistant de Recuva*

**Commentaire**: Le réglage par défaut de la fenêtre *Emplacement de fichier* est *Je ne suis pas sûr*. Cette option lancera un scan sur tous les disques et sur tous les dispositifs amovibles, à l'exception des CD, DVD et médias optiques. Il est donc possible qu'un tel scan prennent un certain temps à générer des résultats.

Le plus souvent, les fichiers sont supprimés à partir de la *Corbeille* du système d'exploitation *Windows*, pour réduire les chances que vous supprimiez des données sensibles ou privées.

**Quatrième étape**. **Cochez** l'option *Dans la corbeille*, tel qu'illustré à la *Figure 3* ci-dessus, puis **cliquez** sur ![](/sbox/screen/recuva-fr/18.png) pour afficher la fenêtre suivante:

![](/sbox/screen/recuva-fr/21.png)

*Figure 4: Merci, maintenant Recuva est prêt à chercher vos fichiers*

**Commentaire**: Pour les fins de cet exercice, n'activez pas l'option *Analyse approfondie*. Cette technique de scan sera abordée à la section **3.3 Comment exécuter une analyse approfondie**. 

**Première étape**. **Cliquez** sur ![](/sbox/screen/recuva-fr/22.png) pour entamer la restauration de vos fichiers supprimés. 

Au cours du processus de récupération, de barre de progression s'affichent successivement. La barre de progression *Recherche des fichiers effacés sur les lecteurs* liste les fichiers supprimés. La barre de progression *Analyse du contenu du fichier* regroupe et trie les fichiers supprimés par types de fichiers et selon qu'ils sont récupérables ou non. Elle affiche également la durée estimée du processus de scan et d'analyse. L'interface principale de *Piriform Recuva* ressemblera alors à ceci:

![](/sbox/screen/recuva-fr/23.png)

*Figure 5: L'interface principale de Piriform Recuva affichant des fichiers supprimés retrouvés*

L'interface principale de *Piriform Recuva* liste des renseignements sur chaque fichier supprimé en six colonnes. Voici une description de chaque colonne:

**Nom du fichier**: Cette colonne affiche le nom et l'extension de fichier du fichier supprimé **Cliquez** sur le titre *Nom du fichier*pour arranger les résultats en ordre alphabétique.

**Emplacement**: Cette colonne affiche l'emplacement où le fichier a été retrouvé. Puisque l'option *Dans la corbeille* a été sélectionnés dans cet exemple, l'emplacement du fichier est *C:RECYCLER* pour tous les fichiers supprimés.  **Cliquez** sur le titre *Emplacement* pour afficher tous les fichiers rangés sous un emplacement de fichier ou de dossier particulier.

**Dernier modifié**: Cette colonne affiche la dernière date à laquelle le fichier a été modifié avant d'être supprimé. Cela peut être utile pour identifier un fichier que vous souhaiteriez récupérer. **Cliquez** le titre 
*Dernier modifié* pour lister les résultats du plus ancien au plus récent.

**Taille**: Cette colonne affiche la taille des fichiers. **Cliquez** sur *Taille* pour lister les fichiers du plus grand au plus petit, ou du plus petit au plus grand.

**État**: Cette colonne indique dans quelle mesure il est possible de récupérer un fichier et correspond à l'icone de l'état du fichier dont il est question à la *Figure 6* ci-dessous. **Cliquez** sur *Etat* pour trier les fichiers par catégorie, de *Excellent* à *Irrécupérable*.

**Commentaire**: Cette colonne affiche les raisons pour lesquelles un fichier peut ou non être récupérer, et indique si un fichier supprimé a été ou non écrasé dans la **Table de fichiers maîtres (MFT)**. **Cliquez** sur *Commentaire* pour voir dans quelle mesure un fichier ou un groupe de fichiers a été écrasé.

Chaque fichier est doté d'un icone de couleur qui indique dans quelle mesure chaque fichier peut être récupéré:

![](/sbox/screen/recuva-fr/24.png)

*Figure 6: Les icones d'état des fichiers*

La liste suivante décrit chaque icone d'état:

- **Vert**: Excellente possibilité de récupérer le fichier au complet.
- **Orange**: Possibilité acceptable de récupérer le fichier.
- **Rouge**: Très faible possibilité de récupérer le fichier.

<a name="3.2"></a>
### 3.2 Comment exécuter un scan sans utiliser l'assistant de Recuva ###

Pour accéder directement à l'interface principale de **Recuva**, c.-à-d. sans passer par l'**Assistant de Recuva**, suivez les étapes énumérées ci-dessous: 

**Première étape**. **Cliquez** sur ![](/sbox/screen/recuva-fr/15.png) ou **sélectionnez Démarrer > Programmes > Recuva > Recuva** pour afficher la *Figure 1*.

**Deuxième étape**. **Cochez** l'option  *Ne plus afficher cet assistant au démarrage*, puis **cliquez** sur ![](/sbox/screen/recuva-fr/50.png) pour afficher la fenêtre suivante:

![](/sbox/screen/recuva-fr/51.png)

*Figure 7: L'interface principale de Recuva*

L'interface principale de *Piriform Recuva* est divisée en deux panneaux: le panneau des résultats, à gauche, et les onglets *Aperçu*, *Info* et *En-tête*, à droite, qui servent à trier et afficher les renseignements concernant un fichier supprimé en particulier. Vous pouvez y régler certaines options d'analyse similaires à celles qu'on retrouve dans l'*assistant de Recuva*.

**Troisième étape**. **Cliquez** sur le menu déroulant et **sélectionnez** le disque à analyser; le *Disque local (C:)* est sélectionné par défaut, et c'est celui qui est utilisé dans l'exemple suivant: 

![](/sbox/screen/recuva-fr/52.png)

*Figure 8: Le menu déroulant des disques à analyser*

Le menu déroulant *Nom du fichier ou emplacement* vous permet de spécifier le type de fichier que vous recherchez, et correspond *grosso modo* aux catégories comprises dans la fenêtre *Type de fichiers de l'assistant de Recuva* illustrée à la *Figure 2*. 

![](/sbox/screen/recuva-fr/53.png)

*Figure 9: Le menu déroulant Nom du fichier ou emplacement*

L'option *Nom du fichier ou emplacement* est une combinaison de zone de texte et de menu déroulant. Elle a deux fonctions principales: elle vous permet de chercher directement un fichier particulier, et/ou de trier un liste de fichiers supprimés par types de fichiers.

La même option l'option *Nom du fichier ou emplacement* peut être utilisée pour chercher des fichiers d'un type particulier ou de trier un liste générale de fichiers supprimés dans le panneau des résultats.

Pour retrouver un fichier dont le nom est connu (partiellement ou au complet), suivez les étapes énumérées ci-dessous: 

**Première étape**. **Saisissez** le nom (ou la partie du nom que vous connaissez) du fichier que vous souhaitez récupérer comme suit (dans l'exemple suivant, nous cherchons le fichier *triangle.png*): 

![](/sbox/screen/recuva-en/54.png)

*Figure 10: Le menu déroulant Nom du fichier ou emplacement affichant le nom de fichier triangle.png*

**Astuce**: **Cliquez** sur ![](/sbox/screen/recuva-fr/55.png) pour rafraîchir la zone de texte *Nom du fichier ou emplacement* (qui s'affiche estompée).

**Deuxième étape**. **Cliquez** sur ![](/sbox/screen/recuva-fr/56.png) pour lancer la recherche du ou des fichier(s) supprimé(s); peu après, une fenêtre similaire à celle-ci s'affichera:

![](/sbox/screen/recuva-fr/57.png)

*Figure 11: L'interface principale de Recuva affichant le fichier triangle.png dans l'onglet Aperçu*

<a name="3.3"></a>
#### 3.3 Comment exécuter une analyse approfondie avec Recuva ####

L'option *Analyse approfondie* vous permet d'exécuter un scan plus minutieux; bien entendu, une analyse approfondie prendra plus de temps, selon la vitesse de votre ordinateur et le nombre de fichiers à analyser. Cette option peut s'avérer utile si votre scan initial n'a pas trouvé les fichiers que vous souhaitez récupérer. Bien qu'une analyse approfondie puisse prendre plusieurs heures, selon la quantité de données stockées sur votre ordinateur, elle peut augmenter considérablement vos chances de récupérer les fichiers que vous cherchez.

L'option *Analyse approfondie* de **Recuva** peut également être activée en **cochant** l'option *Activer l'analyse approfondie* dans l'*assistant de Recuva* (veuillez vous référer à la *Figure 4*). 

**Première étape**. **Cliquez** sur ![](/sbox/screen/recuva-fr/70.png) pour afficher la fenêtre *Options*, puis **cliquez** sur l'onglet *Actions*:

![](/sbox/screen/recuva-fr/73.png)

*Figure 12: La fenêtre Options affichant l'onglet Actions* 

**Deuxième étape**. **Cochez** l'option *Analyse approfondie* *(augmentation de la durée d'analyse)*, puis **cliquez** sur ![](/sbox/screen/recuva-fr/72.png). 

**Troisième étape**. **Cliquez** sur ![](/sbox/screen/recuva-fr/74.png) pour chercher des fichiers supprimés à l'aide de la fonction *Analyse approfondie*. Il est possible que le scan prennent plusieurs heures, selon la taille du disque dur et la vitesse de l'ordinateur:

![](/sbox/screen/recuva-fr/78.png)

*Figure 13: La fenêtre de progression du scan affichant le temps restant estimé pour compléter l'analyse approfondie*

<a name="3.4"></a>
### 3.4 Une introduction à la fenêtre Options ###

Dans cette section, nous verrons comment utiliser les différents paramètres de la fenêtre *Options* pour récupérer et/ou écraser efficacement vos données privées ou sensibles. Pour régler ces paramètres, suivez les étapes énumérées ci-dessous: 

**Première étape**: **Cliquez** sur ![](/sbox/screen/recuva-fr/70.png) pour afficher la fenêtre suivante:

![](/sbox/screen/recuva-fr/71.png)

*Figure 14: La fenêtre Options affichant l'onglet Général par défaut*

La fenêtre *Options* est divisée en trois onglets: *Général*, *Actions* et *À propos*. 

L'onglet *Général* vous permet de définir un ensemble de paramètres importants, dont la *Langue* (Recuva supporte 37 langues), le *Type de vue* et la possibilité d'activer ou de désactiver l'*Assistant de Recuva*. 

![](/sbox/screen/recuva-fr/76.png)

*Figure 15: Le menu déroulant de l'option Type de vue*

L'option **Type de vue** vous permet de choisir la façon dont s'afficheront les fichiers supprimés. Cette option peut aussi être activée en **cliquant à droite* sur un fichier dans l'interface *Piriform Recuva*. 

- **Liste**: Cette option vous permet d'afficher les fichiers supprimés sous forme de liste, tel qu'illustré à la *Figure 5*.
- **Arborescence**: Cette option vous permet d'afficher l'emplacement des fichiers supprimés sous forme d'arborescence extensible.
- **Vignettes**: Cette option vous permet d'afficher les fichiers supprimés sous forme de graphiques ou d'images lorsque cela est possible.

La section *Avancé* de l'onglet *Général* vous permet de déterminer le nombre de fois que vos données seront écrasées par des données aléatoires pour empêcher que des parties malveillantes soient en mesure de les récupérer.

Le menu déroulant *Effacement sécurisé* affiche quatre options distinctes pour écraser vos données privées. Le mode par défaut est *Simple (1 passage)*, tel qu'illustré à la *Figure 14*. Les *passages* sont les fois que vos documents, fichiers ou dossiers seront écrasés avec des données aléatoires pour les rendre illisibles et irrécupérables.

**Deuxième étape**: **Sélectionnez** l'option *DOD 5220.22-M (3 passages)*:

![](/sbox/screen/recuva-fr/77.png) 

*Figure 16: Le menu déroulant Effacement sécurisé avec l'option DOD 5220.22-M (3 passages) sélectionnée*

Un passage simple peut être efficace pour écraser un document, un fichier ou un dossier donné; certaines personnes disposent des ressources et des capacités nécessaires pour récupérer des données relativement peu écrasées. L'option de trois passages constitue un équilibre entre la durée exigée pour écraser des données de façon sécurisée, d'une part, et la capacité de récupérer ces documents, fichiers ou dossiers, d'autre part.

**Troisième étape**. **Cliquez**sur ![](/sbox/screen/recuva-fr/72.png) pour sauvegarder vos paramètres de l'onglet *Général*. 

![](/sbox/screen/recuva-fr/75.png)

*Figure 17: La fenêtre Options affichant l'onglet Actions* 

- **Afficher les fichiers trouvés dans les dossiers cachés du système**: Cette option vous permet d'afficher des fichiers qui se trouvent dans des répertoires cachés du système.

- **Afficher les fichiers vides (0 octets)**: Cette option vous permet d'afficher des fichiers qui ne comportent pas ou très peu de contenu, et qui sont pratiquement irrécupérables.

- **Afficher les fichiers effacés définitivement**: Cette option vous permet d'afficher dans le panneau des résultats des fichiers qui ont été effacés de façon sécurisée.

**Commentaire**: Si vous avez déjà utilisé **CCleaner** ou un programme similaire, ce dernier change le nom du fichier pour *ZZZZZZZ.ZZZ* lorsqu'il efface un fichier de façon sécurisée.

- **Analyse approfondie**: Cette option vous permet de scanner un disque dur au complet pour retrouver un document ou un fichier supprimé; si les analyses précédentes n'ont pas suffit à retrouver le fichier, l'*analyse approfondie* pourrait s'avérer utile. Par contre, il faut être conscient que cette méthode prend beaucoup plus de temps. Veuillez consulter la section **3.3 Comment exécuter une analyse approfondie avec Recuva**.

- **Analyse des fichiers non effacés (pour récupérer depuis des disques endommagés ou formatés)**: Cette option vous permet d'essayer de récupérer des fichiers sur des disques qui ont subi des dommages physiques ou une corruption due à l'action de logiciels.

L'onglet *À propos* affiche des renseignements sur la version du programme, ainsi que des liens vers le site Internet de Piriform.

Maintenant que vous avez acquis la confiance nécessaire pour exécuter différents types de scans et que vous vous êtes familiarisé avec les paramètres des onglets *Général* et *Actions* de la fenêtre *Options*, nous pouvons voir comment récupérer ou effacer vos données privées ou sensibles à la section [**4.0 Comment récupérer et/ou effacer des fichiers avec Recuva**](/fr/recuva_recuperer)




