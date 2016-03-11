

---

lang: fr
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: How to Install and Launch COMODO Firewall 

---

Sommaire des sections de cette page:

- [**2.0 Survol du processus d'installation de COMODO Firewall**](#2.0)
- [**2.1 Comment désactiver le pare-feu Windows**](#2.1)
- [**2.2 COmment installer COMODO Firewall**](#2.2)

-------

<a name="2.0"></a>
## 2.0 Survol du processus d'installation de COMODO Firewall ##

L'installation de **COMODO Firewall** est relativement simple et rapide. Elle comporte deux étapes: il faut dans un premier temps désactiver manuellement le pare-feu de Windows, et ensuite installer le logiciel **COMODO Firewall**.

Idéalement, vous ne devriez utiliser qu'un seul logiciel pare-feu sur votre ordinateur, en tout temps. Si vous utilisez actuellement un autre pare-feu sur votre ordinateur, vous devez le désinstaller avant d'installer **Comodo Firewall**, afin d'éviter les conflits possibles entre logiciels d'un même type.

<a name="2.1"></a>
## 2.1 Comment désactiver le pare-feu Windows ##

Pour désactiver le programme **Pare-feu Windows**, suivez les étapes énumérées ci-dessous:

**Première étape**: **Sélectionnez Démarrer> Panneau de configuration > Pare-feu Windows** pour afficher la fenêtre **Pare-feu Windows **. 

**Deuxième étape**. **Cochez** l'option *Désactivé (non recommandé)* pour désactiver le **Pare-feu Windows** tel qu'illustré ci-dessous: 

![](/sbox/screen/comodo-fr/01.png)

*Figure 1. Le Pare-feu Windows avec l'option 'Désactivé' sélectionnée*

**Troisième étape**. **Cliquez** sur ![](/sbox/screen/comodo-fr/02.png) pour finaliser la désactivation du *Pare-feu Windows*.

<a name="2.2"></a>
## 2.2 Comment installer COMODO Firewall ##

**Commentaire**: **COMODO Firewall** ne désinstalle pas automatiquement les versions plus anciennes de son logiciel. Celles-ci doivent être désinstallée manuellement avant d'entamer le processus d'installation de la plus récente version.

Pour lancer l'installation de **COMODO Firewall**, suivez les étapes énumérées ci-dessous:

**Première étape**. **Double-cliquez** sur ![](/sbox/screen/comodo-fr/03.png) pour entamer le processus d'installation. Si une boîte de dialogue *Fichier ouvert - Avertissement de sécurité* s'affiche,  **cliquez** sur ![](/sbox/screen/comodo-fr/04.png) pour afficher la boîte de dialogue suivante:

![](/sbox/screen/comodo-fr/05.png)

*Figure 2: La boîte de dialogue de sélection de la langue*

**Deuxième étape**. **Cliquez** sur ![](/sbox/screen/comodo-fr/06.png) pour afficher le *Contrat de licence de l'utilisateur*. Veuillez lire attentivement le *Contrat de licence de l'utilisateur* avant de poursuivre le processus d'installation du logiciel, puis **cliquez** sur ![](/sbox/screen/comodo-fr/07.png) pour afficher la fenêtre *Enregistrement gratuit*. 

**Troisième étape**: **Ne saisissez pas** votre adresse email dans le champs *Entrez votre adresse email (facultatif)*; **cliquez** simplement sur ![](/sbox/screen/comodo-fr/09.png) pour afficher la fenêtre d'extraction des fichiers.

Lorsque le processus d'extraction est complété, la fenêtre *Dossier de destination* s'affiche.

**Quatrième étape**. **Cliquez** sur ![](/sbox/screen/comodo-fr/09.png) pour accepter l'emplacement par défaut et afficher la fenêtre *Sélection du niveau de sécurité du pare-feu*, puis **cochez** l'option *Pare-feu seulement*, tel qu'illustré ci-dessous: 

![](/sbox/screen/comodo-fr/11.png)

*Figure 3: La fenêtre Sélection du niveau de sécurité du pare-feu*

**Définition des différents niveau de sécurité du pare-feu**

Chaque niveau de sécurité du pare-feu répond aux besoins particuliers d'utilisateurs de différents niveaux. Chaque option équilibre différents types de protection selon la complexité de l'utilisation et détermine le nombre d'avertissements de sécurité que vous pourriez recevoir. Voici une brève description de chaque niveau de sécurité:

Le mode **Pare-feu seulement**: Ce mode vous permet d'utiliser **COMODO Firewall** sans la fonction *Defense +*. Le logiciel identifie les applications les plus couramment utilisées et qui sont relativement sûres (comme les navigateurs Web et les clients de courrier électronique), ce qui réduit le nombre d'avertissements de sécurité que vous pourriez recevoir. Dans ce mode, le programme explique en termes généraux pourquoi un avertissement en particulier s'affiche dans telle ou telle circonstance. De plus, les actions à entreprendre sont relativement simples. 


Le mode **Pare-feu avec une défense proactive optimale**: Ce mode ajoute la fonction *Defense +* à la bonne protection de base du mode **Pare-feu seulement**. *Defense +* offre une protection active contre les logiciels malveillants conçus spécifiquement pour contourner différents pare-feu. Les *Avertissements Comodo Firewall* présentent des explications approfondies des raisons pour lesquelles certaines applications ou requêtes sont bloquées, et vous donnent l'option d'isoler des fichiers ou programmes suspects ou de les placer dans une 'sandbox'.

Le mode **Pare-feu avec une défense proactive maximale**: Ce mode combine l'option **Pare-feu avec une défense proactive optimale** avec une fonction de protection 'anti-fuite' contre les menaces 'passives', par exemple lorsque des renseignements concernant les ports ouverts sur votre ordinateur sont envoyés sur Internet. La fonction 'sandbox' est complètement automatique.

**Sixième étape**. **Cliquez** sur ![](/sbox/screen/comodo-fr/09.png) pour afficher la fenêtre *Configuration de COMODO Secure DNS*, avec l'option *Je veux utiliser les serveurs COMODO SecureDNS* sélectionnée, tel qu'illustré ci-dessous:

![](/sbox/screen/comodo-fr/12.png)

*Figure 4: La fenêtre Configuration de COMODO Secure DNS*

**Important**: Même si aucun **Système de noms de domaine** (**DNS**) n'est parfaitement sécurisé les bénéfices liés à l'utilisation des ** Serveurs COMODO Secure DNS** sont plus nombreux que les inconvénients. Cette fonction vous offre une protection supplémentaire contre le *dévoiement (pharming)* et l'*hammeçonnage (phishing)*, deux techniques de piratage courantes employées par des tiers malveillants pour détourner votre ordinateur vers des sites hostiles ou dangereux. Facile à configurer à l'installation, la fonction **serveurs COMODO Secure DNS** peut également vous protéger des interférences du gouvernement et facilite l'accès sécurisé aux sites Internet qui sont inscrits auprès de  **COMODO**. Par exemple, si vous faites une faute en saisissant une URL, vous recevrez un avertissement du **Serveur COMODO Secure DNS** semblable à celui-ci:

![](/sbox/screen/comodo-fr/126.png)

*Figure 5: Un exemple typique d'avertissement du Serveur COMODO Secure DNS*

**Septième étape**. **Cliquez** sur ![](/sbox/screen/comodo-fr/09.png) pour afficher la fenêtre *Prêt à installer COMODO Firewall*, puis **cliquez** sur ![](/sbox/screen/comodo-fr/13.png) pour lancer l'installation et afficher la fenêtre 

 *Installation de COMODO Firewall en cours*. À l'issue du processus d'installation, la fenêtre *L'installation du COMODO Firewall est terminée* s'affiche.

**Huitième étape**. **Cliquez** sur ![](/sbox/screen/comodo-fr/14.png) pour afficher la fenêtre de confirmation *Fait*, puis **cliquez** à nouveau sur ![](/sbox/screen/comodo-fr/14.png) pour afficher la fenêtre de confirmation illustrée ci-dessous:

![](/sbox/screen/comodo-fr/15.png)

*Figure 6: La fenêtre de confirmation Installation de Firewall*

**Neuvième étape**. **Cliquez** sur ![](/sbox/screen/comodo-fr/16.png) pour redémarrer l'ordinateur et finaliser la procédure d'installation de **COMODO Firewall**.

Après avoir redémarré votre ordinateur, la fenêtre *Nouveau réseau privé détecté* s'affiche comme suit:  

![](/sbox/screen/comodo-fr/17.png)

*Figure 7: La fenêtre Nouveau réseau privé détecté de COMODO Firewall*

**Astuce**: Si vous travaillez dans un environnement LAN, cochez l'option *Je veux être pleinement accessible aux autres ordinateurs du réseau* pour activer les fonctions de partage de fichiers/dossiers/imprimantes et/ou de connexion à Internet.

**Dixième étape**. Dans le champs *Donnez un nom à ce réseau*, **saisissez** un nouveau nom ou acceptez le nom par défaut tel qu'illustré à la *Figure 7* ci-dessus. Laissez les options de la rubrique *Étape 2 - Déterminez si vous voulez faire confiance aux autres PC en réseau* dessélectionnez, puis **cliquez** sur ![](/sbox/screen/comodo-fr/06.png) pour finaliser l'installation.

L'icone de bureau **COMODO Firewall** et l'icone de connectivité **COMODO Firewall** apparaissent en même temps que la fenêtre illustrée à la *figure 7*. Avant de vous connecter à Internet, l'icone de connectivité s'affiche dans la barre des tâches, tel qu'illustré ci-dessous: 

![](/sbox/screen/comodo-fr/18.png)

*Figure 8: L'icone de connectivité de COMODO Firewall (ici surligné en noir) dans la barre des tâches*

Lorsque une requête est faite pour aller sur Internet ou lancer un programme qui doit accéder à Internet (par exemple, un navigateur Web), une série de flèches orange pointant vers le bas et de flèches verte pointant vers le haut s'afficheront pour indiquer toute requête de connexion entrante ou sortante à Internet, tel qu'illustré ci-dessous:

![](/sbox/screen/comodo-fr/19.png)

*Figure 9: L'icone de connectivité de COMODO Firewall en action*

Après quelques minutes de fonctionnement, le *Centre de messagerie de COMODO* affichera peut-être un message comme celui-ci:

![](/sbox/screen/comodo-fr/20.png)

*Figure 10: La fenêtre du Centre de messagerie de COMODO*

**Commentaire**: **Cliquez** sur le lien *Learn more* pour être automatiquement redirigé vers les forums d'aide de **Comodo**.

**Astuce**: **Cliquez à droite** sur l'icone de connectivité de **COMODO Firewall** dans la *Barre des tâches* (tel qu'illustré à la *figure 10*) pour afficher le menu contextuel suivant, ainsi que ses sous-menus:

![](/sbox/screen/comodo-fr/127.png)

*Figure 11: Le menu et les sous-menus contextuels de l'icone de connectivité*

Le menu de l'icone de connectivité vous permet de changer les produits de **COMODO Firewall** que vous utilisez. En **sélectionnant** l'item *Configuration*, vous activez le sous-menu *Gérer mes configurations*, où vous pouvez **sélectionner** soit *COMODO - Proactive Security*, soit *COMODO - Internet Security* afin d'activer la fonction 'Sandbox'.

De plus, il est possible d'ajuster le niveau de sécurité de chaque produit à partir du menu contextuel de l'icone de connectivité, tel qu'illustré ci-dessous; ces niveaux de sécurité sont examinés plus attentivement dans les sections   **4.1 La fenêtre de réglages du comportement du pare-feu** et **4.2 La fenêtre de réglages de Defense+**

![](/sbox/screen/comodo-fr/128.png)

*Figure 12: Le sous-menu 'Niveau de sécurité Pare-feu' de l'icone de connectivité*



