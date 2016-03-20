

---

lang: fr
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: How to Install Thunderbird

---

Sommaire des sections de cette page:

- [**2.0 Comment installer Thunderbird**](#2.0)
- [**2.1 Comment désactiver l'option Recherche et indexation globales dans Thunderbird**](#2.1)
- [**2.2 Comment enregistrer un compte de courrier électronique dans Thunderbird**](#2.2)
- [**2.3 Comment enregistrer des comptes de Blogs, de nouvelles et de Groupes de discussion dans Thunderbird**](#2.3)

-------

<a name="2.0"></a>
## 2.0 Comment installer Thunderbird ##

L'installation de **Thunderbird** est un processus relativement simple et rapide. Pour lancer l'installation de **Thunderbird**, suivez les étapes énumérées ci-dessous:

**Première étape**. **Double-cliquez** sur ![](/sbox/screen/thunderbird-fr/01.png); il est possible que la boîte de dialogue de confirmation *Fichier ouvert - Avertissement de sécurité* s'affiche à ce moment. Si c'est le cas, **cliquez** sur ![](/sbox/screen/thunderbird-fr/02.png) pour afficher la fenêtre suivante:

![](/sbox/screen/thunderbird-fr/03.png)

*Figure 1: La barre de progression de l'extraction*

Lorsque l'extraction des fichiers de **Thunderbird** est complétée, la fenêtre *Bienvenue dans l'assistant d'installation de Mozilla Thunderbird* apparaît.

**Deuxième étape**. **Cliquez** sur ![](/sbox/screen/thunderbird-fr/04.png) pour activer la fenêtre *Mozilla Thunderbird - Type d'installation*.

**Troisième étape**. **Cliquez** sur ![](/sbox/screen/thunderbird-fr/04.png) pour accepter les réglages par défaut et afficher la fenêtre suivante:

![](/sbox/screen/thunderbird-fr/05.png)

*Figure 2: La fenêtre Mozilla Thunderbird - Résumé*

**Quatrième étape**. **Cliquez** sur ![](/sbox/screen/thunderbird-fr/06.png) pour lancer le processus d'installation. La barre de progression **Mozilla Thunderbird - Installation** s'affiche alors. Lorsque le processus d'installation est terminé, la fenêtre suivante s'affiche:

![](/sbox/screen/thunderbird-fr/07.png)

*Figure 3: La fenêtre Fin de l'assistant d'installation de Mozilla Thunderbird*

**Cinquième étape**. **Cliquez** sur ![](/sbox/screen/thunderbird-fr/08.png) pour compléter le processus d'installation.

**Astuce**: **Thunderbird** se lancera automatiquement si l'option *Lancer Mozilla Thunderbird* est cochée, tel qu'illustré à la *figure 3* ci-dessus. Pour lancer le programme à l'avenir, vous pouvez, soit **double-cliquer** sur l'icone de bureau de **Thunderbird**, soit **sélectionner > Programmes > Mozilla Thunderbird > Mozilla Thunderbird**.

<a name="2.1"></a>
## 2.1 Comment désactiver l'option Recherche et indexation globales dans Thunderbird ##

**Attention**: La fonction *Recherche et indexation globales* de **Thunderbird** *doit* être désactivée pour optimiser la performance du programme. Selon la quantité et la taille de vos messages, cette fonction peut ralentir votre système et réécrivant continuellement et inutilement les mêmes données sur votre disque dur. Au fur et à mesure que votre disque dur se remplit, plusieurs opérations de votre système tourneront de plus en plus au ralentit.

Pour désactiver l'option *Recherche et indexation globales*, suivez les étapes énumérées ci-dessous: 

**Première étape**. **Sélectionnez Outils > Options** dans la console **Thunderbird** pour afficher la fenêtre *Options*.

**Deuxième étape**. **Cliquez** sur ![](/sbox/screen/thunderbird-fr/09.png) pour afficher le contenu de cet onglet:

![](/sbox/screen/thunderbird-fr/10.png)

*Figure 4: La fenêtre Options affichant le contenu de l'onglet Avancé*

**Troisième étape**. **Cliquez** sur la case *Activer la recherche et l'indexation globales*, dans la section *Configuration avancée*, pour *désactiver* cette option, tel qu'illustré ci-dessous: 

![](/sbox/screen/thunderbird-fr/11.png)

*Figure 5: La section Configuration avancée*

Maintenant que vous avez désactivé cette option, vous êtes prêt à enregistrer un compte de courrier électronique dans **Thunderbird**.

<a name="2.2"></a>
## 2.2 Comment enregistrer un compte de courrier électronique dans Thunderbird ## 

La fenêtre *Assistant d'importation - Importer les paramètres et les dossiers de messages* n'apparaît qu'à la première installation de **Thunderbird**. 

**Première étape**. **Cochez** l'option *Ne rien importer*, tel qu'illustré ci-dessous:
 
![](/sbox/screen/thunderbird-fr/12.png)

*Figure 6: L'Assistant d'importation - Importer les paramètres et les dossiers de messages*

**Deuxième étape**. **Cliquez** sur ![](/sbox/screen/thunderbird-fr/04.png) pour afficher la fenêtre suivante: 

![](/sbox/screen/thunderbird-fr/13.png)

*Figure 7: La fenêtre Création d'un compte courrier*

**Troisième étape**. **Saisissez** votre nom, adresse de courrier électronique et mot de passe dans les champs appropriés; puis **décochez** l'option *Retenir le mot de passe*, tel qu'illustré à la *figure 7* ci-dessous.

**Quatrième étape**. **Cliquez** sur ![](/sbox/screen/thunderbird-fr/14.png) pour afficher la fenêtre suivante:

![](/sbox/screen/thunderbird-fr/15.png)

*Figure 8: La fenêtre Création d'un compte courrier avec l'option **IMAP - Accès aux dossiers et messages à partir de plusieurs ordinateurs** sélectionnée*

## IMAP et POP: Descriptions et utilisation ###

**Internet Message Access Protocol** (**IMAP**) et **Post Office Protocol** (**POP**) sont deux méthodes distinctes d'archiver et de recevoir des messages de courrier électronique.

- **Internet Message Access Protocol** (**IMAP**): Lorsque vous utilisez la méthode **IMAP**, tous vos dossiers (y compris les dossiers *Courrier entrant*, *Brouillons*, *Envoyés*, *Corbeille* et tous les autres dossiers) demeure sur le serveur de courrier. De cette façon, vous pouvez accéder à ces dossiers depuis un autre ordinateur. Tous les messages seront donc conservés sur le serveur et, initialement, seulement le titre des messages (comportant des renseignements comme la date et l'heure, le sujet du message, le nom de l'expéditeur, etc.) sont téléchargés pour être affichés par votre client mail sur votre ordinateur. Les messages complets ne sont affichés que lorsque vous cliquez dessus pour les ouvrir. **Thunderbird** peut aussi être configuré pour archiver dans votre ordinateur des copies de vos messages qui se trouvent dans certains ou dans tous vos dossiers, afin que vous puissiez travailler dessus en mode autonome (non connecté à Internet). En mode **IMAP**, lorsque vous supprimé des messages ou des dossiers, vous le faites *à la fois* sur votre ordinateur local et sur le serveur.

-  **Post Office Protocol** (**POP**): Lorsque vous utilisez la méthode **POP**, seul le dossier *Courrier entrant* (le dossier où sont livrés et affichés les nouveaux messages entrants) demeure sur le serveur distant; tous les autres dossiers sont situés sur votre ordinateur local seulement. Vous pouvez choisir de laisser vos messages dans le dossier *Courrier entrant* sur le serveur après les avoir téléchargés sur votre ordinateur, ou vous pouvez les supprimer du serveur. Dans le dernier cas, si vous accédez à votre compte depuis un autre ordinateur, vous ne verrez uniquement que les messages du dossier *Courrier entrant* (les nouveaux messages et ceux que vous avez choisi de ne pas supprimé du serveur). 

**Cinquième étape**. **Cliquez** sur ![](/sbox/screen/thunderbird-fr/16.png) pour créer votre compte et afficher la console **Thunderbird** avec votre compte de courrier compris dans la barre *Tous les dossiers*, à gauche, tel qu'illustré ci-dessous: 

![](/sbox/screen/thunderbird-fr/17.png)

*Figure 9: L'interface principale de Thunderbird affichant votre compte Gmail nouvellement enregistré*

**Commentaire**: Pour ajouter un autre compte de courriel, **sélectionnez Fichier > Nouveau > Comptes courrier...** pour afficher la  *figure 7* de cette section, et reprenez les **étapes 3 à 5**.

Après avoir enregistré vos comptes de courrier électronique dans **Thunderbird**, la prochaine fois que vous ouvrirez l'interface principale, on vous demandera de saisir votre mot de passe pour chaque compte, comme suit: 

![](/sbox/screen/thunderbird-fr/20.png)

*Figure 10: La fenêtre Saisissez votre mot de passe*

**Commentaire**: Bien que la fonction d'enregistrement du mot de passe ne soit généralement pas recommandée, **Thunderbird** comporte une fonction de *Mot de passe maître*. Cette fonction permet de n'utiliser qu'un seul mot de passe pour protéger tous les mots de passes associés à vos différents comptes, que vous ne saisissez qu'une seule fois lors du processus d'enregistrement. Pour plus de renseignements sur cette fonction, veuillez consulter la section [**3.3 Comment configurer les onglets de sécurité dans Thunderbird**](/fr/thunderbird_securite#3.3) - **L'onglet Mot de passe**.

<a name="2.3"></a>
## 2.3 Comment enregistrer des comptes de blogs, de nouvelles et de groupes de discussion ##

Pour créer et enregistrer un compte pour des blogs, des nouvelles ou des groupes de discussion, suivez les étapes énumérées ci-dessous: 

**Première étape**. **Sélectionnez > Fichier > Nouveau > Autres comptes** pour afficher la fenêtre  *Assistant de création de compte > Paramétrage du nouveau compte*.

**Deuxième étape**. **Cochez** soit l'option *Blogs et nouvelles*, soit l'option *Groupes de discussion*, puis **cliquez** sur ![](/sbox/screen/thunderbird-fr/04.png) pour afficher la fenêtre suivante:

![](/sbox/screen/thunderbird-fr/21.png)

*Figure 11: La fenêtre Assistant de création de compte - Nom du compte*

**Troisième étape**. **Cliquez** sur ![](/sbox/screen/thunderbird-fr/04.png) pour afficher la fenêtre suivante: 

![](/sbox/screen/thunderbird-fr/22.png)

*Figure 12: La fenêtre Assistant de création de compte - Félicitations!*

**Cinquième étape**. **Cliquez** sur ![](/sbox/screen/thunderbird-fr/08.png) pour compléter le processus d'enregistrement du compte et retourner à la console **Thunderbird**.

Maintenant que vous avez configuré **Thunderbird** pour une utilisation optimale, veuillez lire la prochaine section, [**Comment régler les options de sécurité dans Thunderbird**](/fr/thunderbird_securite).



