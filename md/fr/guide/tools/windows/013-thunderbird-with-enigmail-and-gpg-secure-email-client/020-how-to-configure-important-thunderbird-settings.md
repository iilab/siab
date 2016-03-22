

---

lang: fr
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Configure Important Thunderbird Settings

---

Sommaire des sections de cette page:

- [**3.0 À propos des options de sécurité de Thunderbird**](#3.0)
- [**3.1 Comment désactiver le panneau d'affichage des messages de Thunderbird**](#3.1)
- [**3.2 Comment désactiver la fonction HTML dans Thunderbird**](#3.2)
- [**3.3 Comment régler les options de sécurité dans Thunderbird**](#3.3)
- [**3.4 Comment activer le filtre des indésirables dans les paramètres du compte**](#3.4)

-------

<a name="3.0"></a>
## 3.0 À propos des options de sécurité de Thunderbird ##

Dans le contexte de **Mozilla Thunderbird**, le terme 'sécurité' fait référence à la protection de votre ordinateur contre des messages de courrier électronique nuisibles ou malveillants. Il peut s'agir de pourriel, par exemple, ou encore de messages servant de véhicules à des virus ou des logiciels espions. Il existe plusieurs paramètres qui doivent être activés, désactivés ou réglés adéquatement dans **Mozilla Thunderbird** pour permettre au programme de défendre efficacement votre système contre des attaques provenant du courrier électronique. Il est également *absolument impératif* que vous installiez des logiciels pare-feu, antivirus et anti-mouchards.

Pour plus de renseignements sur les moyens de prévenir les intrusions nuisibles ou malveillantes, veuillez consulter le chapitre [**1. Protéger votre ordinateur contre les logiciels malveillants et les pirates**](chapter-1) du **Livret pratique**, ainsi que les chapitres portant sur [**Avast**](/fr/avast_principale), [**Comodo Firewall**](comodo_principale) et [**Spybot**](spybot_principale).

<a name="3.1"></a>
## 3.1 Comment désactiver le panneau d'affichage des messages de Thunderbird ##

La console **Thunderbird** est séparée en trois sections distinctes: l'encadré à gauche affiche les différents dossiers de vos comptes de courriel; le panneau à droite affiche une liste de messages; et le panneau du bas à droite affiche un *aperçu* d'un message sélectionné.

**Commentaire**: Si un message contient du code malicieux, ce panneau affichant l'aperçu du message pourrait l'activer; il est donc recommandé de le désactiver.

![](/sbox/screen/thunderbird-fr/23.png)

*Figure 1: L'interface principale de Thunderbird*

Pour désactiver le panneau d'affichage des messages, suivez les étapes énumérées ci-dessous: 

**Première étape**. **Sélectionnez  Affichage > Disposition**, puis **dessélectionnez** l'option *Panneau d'affichage des messages* pour la désactiver, comme suit: 

![](/sbox/screen/thunderbird-fr/24.png)

*Figure 2: Le menu Affichage affichant le sous-menu Disposition avec le Panneau d'affichage des messages sélectionné*

Le *Panneau d'affichage des messages* n'apparaitra plus et vous devrez désormais **double-cliquer** sur un message pour en afficher le contenu. Si un message vous semble suspect (parce que son titre, par exemple, est impertinent ou inattendu, ou parce qu'il provient d'un expéditeur inconnu), vous pouvez maintenant le supprimer avant d'en afficher le contenu.

<a name="3.2"></a>
## 3.2 Comment désactiver la fonction HTML dans Thunderbird ##

**Thunderbird** vous permet d'utiliser le **HyperText Markup Language** (**HTML**) pour composer vos messages. Cela signifie que vous pouvez recevoir ou envoyer des messages qui comprennent des couleurs, des polices spéciales, des images et d'autres options de mise en page. Par contre, le **HTML** est le même langage utilisé pour coder des pages Web; l'affichage de messages codés en **HTML** peut vous exposer à des codes malveillants, ce qui comporte certains des mêmes risques que ceux posés par les sites Internet.

Pour désactiver la fonction de mise en page **HTML**, suivez les étapes énumérées ci-dessous:

**Première étape**. **Sélectionnez Affichage > Corps du message en > Texte seul**, comme suit: 

![](/sbox/screen/thunderbird-fr/25.png)

*Figure 3: Le menu Affichage affichant le sous-menu Corps du message en avec l'option Texte seul sélectionné*

<a name="3.3"></a>
### 3.3 Comment régler les options de sécurité ###

**Thunderbird** comporte deux filtres de courrier indésirable qui peuvent vous aider à déterminer quels messages sont des pourriels. Par défaut, ces filtres sont désactivés et vous devez donc les activer avant de les utiliser. Même après les avoir désactivés, vous continuerez à recevoir du courrier indésirable, mais **Thunderbird** les classera automatiquement dans le dossier *Indésirables*.

Le courrier frauduleux, aussi appelés messages d'*hammeçonnage*, ou *phishing*, essaie habituellement de vous faire cliquer sur des liens qui sont codés dans le message. Souvent, ces liens redirigent votre navigateur vers des sites Internet qui tenteront d'infecter votre ordinateur avec un virus. Dans d'autres cas, le lien vous mènera vers un site Internet qui semble légitime, mais qui est en fait conçu pour vous induire à révéler vos noms d'utilisateurs et vos mots de passe, qui pourront ensuite être utilisés ou vendus à une tierce partie à des fins commerciales ou malveillantes.

**Thunderbird** peut identifier ce type de courrier et vous en avertir. Des outils supplémentaires peuvent prévenir les infections provenant de sites Internet malveillants: voir la section [**Autres modules utiles de Mozilla**](/fr/firefox_autres) du chapitre portant sur **Firefox**.

Le premier ensemble de paramètres de sécurité concernant le courrier indésirable se trouve dans la fenêtre *Options - Sécurité*, où la majorité des options de sécurité et de confidentialité peuvent être réglées. Pour y accéder, suivez les étapes énumérées ci-dessous:

**Première étape**. **Sélectionnez Outils > Options** pour afficher la fenêtre *Options*.

**Deuxième étape**. **Cliquez** sur ![](/sbox/screen/thunderbird-fr/26.png) pour afficher la fenêtre suivante:

![](/sbox/screen/thunderbird-fr/27.png)

*Figure 4: La fenêtre Sécurité affichant le contenu de l'onglet Indésirables*

### L'onglet Indésirables ###

**Première étape**. **Cochez** les options pertinentes dans l'onglet *Indésirables*, tel qu'illustré à la *figure 4*, ci-dessus, pour permettre à **Thunderbird** de supprimer les messages que vous définis comme courrier indésirable. D'autres options de filtrage du courrier indésirable seront abordés plus loin dans cette section.

### L'onglet Courrier frauduleux ###

**Première étape**. **Cochez** l'option *Signaler si le message en cours de lecture est susceptible d'être frauduleux* pour permettre à **Thunderbird** d'analyser les messages pour y détecter des fraudes potentielles: 

![](/sbox/screen/thunderbird-fr/28.png)

*Figure 5: L'onglet Courrier frauduleux* 

### L'onglet Antivirus ###

**Première étape**. **Cliquez** sur l'onglet *Antivirus* pour afficher la fenêtre suivante: 

![](/sbox/screen/thunderbird-fr/29.png)

*Figure 6: L'onglet Antivirus* 

Cette option permet à votre logiciel antivirus de scanner et d'isoler des messages individuellement au fur et à mesure qu'ils arrivent. Si cette option n'est pas activée, il est possible que votre dossier *Courrier entrant* *au complet* soit placé 'en quarantaine' si vous recevez ne serait-ce qu'un seul message infecté.

**Commentaire**: Il est tenu pour acquis qu'il y a un programme antivirus fonctionnel installé sur votre ordinateur. Veuillez consulter le chapitre portant sur [**Avast**](/fr/avast_principale) pour plus de renseignements sur l'installation et la configuration d'un logiciel antivirus.

### L'onglet Mots de passe ###

**Première étape**. **Cliquez** sur l'onglet *Mots de passe* pour afficher la fenêtre suivante: 

![](/sbox/screen/thunderbird-fr/30.png)

*Figure 7: L'onglet Mots de passe*

**Important:** Nous recommandons fortement que vous gardiez vos mots de passe privés en utilisant un programme conçu spécialement à cette fin; veuillez consulter le chapitre portant sur [**KeyPass**](/fr/keepass_principale) pour plus de renseignements à ce sujet. 

**Commentaire**: Les options de l'onglet *Mots de passe* ne fonctionneront que si vous sélectionnez d'abord l'option *Retenir le mot de passe* dans la toute première fenêtre d'enregistrement d'un compte courrier dans **Thunderbird**. 

**Deuxième étape**. **Cliquez** sur ![](/sbox/screen/thunderbird-fr/31.png) pour afficher la fenêtre suivante:

![](/sbox/screen/thunderbird-fr/32.png)

*Figure 8: La fenêtre Enregistrement des mots de passe*

La fenêtre *Enregistrement des mots de passe* vous permet de supprimer ou d'afficher les mots de passe correspondant à chacun de vos comptes. Cela dit, pour maximiser votre sécurité et la confidentialité de vos renseignements, vous pouvez également définir un *Mot de passe principal* pour faire en sorte que vos mots de passe ne soit pas accessibles aux personnes qui sont le moindrement familière avec les options de mots de passe de **Thunderbird**.

**Troisième étape**. **Cochez** l'option *Utiliser un mot de passe principal*, tel qu'illustré à la *figure 7* pour activer le bouton *Modifier le mot de passe principal*.

**Quatrième étape**. **Cliquez** sur ![](/sbox/screen/thunderbird-fr/33.png) pour afficher la fenêtre suivante:

![](/sbox/screen/thunderbird-fr/34.png)

*Figure 9: La fenêtre Modifier le mot de passe principal*

**Cinquième étape**. **Saisissez** un mot de passe suffisamment difficile, que vous seul connaîtrez, puis **cliquez** sur ![](/sbox/screen/thunderbird-fr/35.png) pour confirmer votre *Mot de passe principal*. La prochaine fois que vous **cliquerez** sur ![](/sbox/screen/thunderbird-fr/31.png), la fenêtre suivante apparaîtra pour vous demander de saisir votre mot de passe principal:

![](/sbox/screen/thunderbird-fr/36.png)

*Figure 10: La fenêtre Mot de passe requis*

### L'onglet Contenu Web ###

Un cookie est un minuscule texte codé que votre navigateur web utilise pour authentifier ou identifier un site Internet donné. L'onglet *Contenu Web* vous permet de spécifier quels cookies de blogs, de nouvelles ou de groupes de discussions sont sûrs et fiables.

**Première étape**. **Cliquez** sur l'onglet *Contenu Web* pour afficher la fenêtre suivante:

![](/sbox/screen/thunderbird-fr/37.png)

*Figure 11: L'onglet Contenu Web*

**Deuxième étape**. **Sélectionnez** l'option *la fermeture de Thunderbird* dans la liste *Les conserver jusqu'à:* pour supprimer les cookies lorsque vous fermez **Thunderbird**, pour une plus grande sécurité.

<a name="3.4"></a>
### 3.4 Comment activer le filtre des indésirables dans les paramètres du compte ###

Le deuxième type de filtrage du courrier indésirable offert par **Thunderbird** se trouve dans la fenêtre *Paramètres des comptes - Paramètres pour les indésirables*. Par défaut, ces filtres sont désactivés et vous devrez donc les activer pour les utiliser. Lorsque des messages indésirables arrivent, **Thunderbird** les classera automatiquement dans les dossiers *Indésirables* associés à chaque compte.

**Première étape**. **Sélectionnez Outils > Paramètres des comptes** pour afficher la fenêtre *Paramètres des comptes*.

**Deuxième étape**. **Sélectionnez** l'option *Paramètres des indésirables* associé à un compte **Gmail** ou **RiseUp** dans l'encadré de gauche. 

**Troisième étape**. **Réglez** les options des *Paramètres des indésirables* de sorte que vos *Paramètres de comptes - Paramètres des indésirables* ressemblent à ceci:

![](/sbox/screen/thunderbird-fr/38.png)

*Figure 12: La fenêtre Paramètres des comptes - Paramètres des indésirables*

**Quatrième étape**. **Cliquez** sur ![](/sbox/screen/thunderbird-fr/35.png) pour compléter la configuration de la fenêtre *Paramètres des comptes*.

**Commentaire**: Les options des *Paramètres des indésirables* doivent être réglés séparément pour chaque compte. Ainsi, les indésirables des compte *Gmail* ou *Riseup* seront placés dans leur dossier *Supprimés* respectif. Sinon, vous pouvez également désigner un *Dossier local* pour recevoir les indésirables de tous vos comptes.

![](/sbox/screen/thunderbird-fr/39.png)

*Figure 13: La fenêtre Paramètres des comptes - Paramètres des indésirables affichant les réglages pour un dossier Indésirables central*

**Première étape**. **Sélectionnez** l'option *Paramètres des indésirables* sous la rubrique *Dossiers locaux* dans l'encadré de gauche.

**Deuxième étape**. **Sélectionnez** l'option *Dossiers locaux* dans la liste défilante *Dossier Indésirables sur:*, tel qu'illustré à la *figure 13*.

**Troisième étape**. **Cliquez** sur ![](/sbox/screen/thunderbird-fr/35.png) pour compléter la configuration de la fenêtre *Paramètres des comptes*.

Maintenant que vous avez configuré les diverses options de sécurité et de gestion des indésirables de **Thunderbird**, veuillez lire la prochaine section, [**Comment utiliser Enigmail avec GnuPG dans Thunderbird**](/fr/thunderbird_utiliserenigmail). 



