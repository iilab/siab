

---

lang: fr
community: guide
type: tools
legacy: True
child: True
os: android
weight: 1
depth: 3
title: KeePassDroid - Basic Usage

---

-----

## 2. Comment installer et utiliser KeePassDroid

Liste des sections :

- [**2.0 Comment installer KeePassDroid**](#2.0)
- [**2.1 Comment créer une nouvelle base de données de mots de passe**](#2.1)
- [**2.2 Comment ajouter un groupe et une entrée**](#2.2)
- [**2.3 Comment modifier une entrée**](#2.3)
- [**2.4 Comment générer des mots de passe aléatoires**](#2.4)
- [**2.5 Comment verrouiller la base de données KeePassDroid**](#2.5)
- [**2.6 Comment créer une sauvegarde du fichier de la base de mots de passe**](#2.6)
- [**2.7 Comment réinitialiser votre mot de passe maître**](#2.7)

-------

<a name="2.0"></a>
## 2.0 Comment installer KeePassDroid ##

**Étape 1**. **Téléchargez** l'application à partir de [**Google Play**](https://play.google.com/store/apps/details?id=com.android.keepass).

![](/sbox/screen/keepassdroid-en/01.png)

*Graphique 1 : Versions de KeyPassDroid*

**Étape 2**. Une fois le téléchargement effectué, cliquez sur **Package installer** (installeur du paquetage, puis **cliquez** sur *Install* (installer).

![](/sbox/screen/keepassdroid-en/02.png)

*Graphique 2 : Autorisations nécessaires pour KeyPassDroid*

**Étape 3**. **Cliquez** sur *Open* (ouvrir) comme montré dans la capture d'écran ci-dessous pour activer **KeePassDroid**.

![](/sbox/screen/keepassdroid-en/03.png)

*Graphique 3 : Écran de l'application installée.*

<a name="2.1"></a>
## 2.1 Comment créer une nouvelle base de données de mots de passe ##

Dans les sections qui suivent, vous allez apprendre à créer un mot de passe maître, sauvegarder votre base de données nouvellement créée, générer un mot de passe aléatoire pour un programme particulier et créer une copie de sauvegarde de la base de données.

Pour ouvrir **KeePassDroid**, il vous faut cliquer sur l'icône de l'application.

![](/sites/securityinabox.org/files/u12/keepass.gif)

Créer une nouvelle base de données de mots de passe implique deux étapes : vous devez déterminer un mot de passe maître unique et complexe, que vous allez utiliser pour verrouiller et déverrouiller votre base de données de mots de passe. Vous devez ensuite sauvegarder cette base de données de mots de passe.

Pour créer une nouvelle base de données de mots de passe, suivez les étapes suivantes :

**Étape 1**. Pour créer une nouvelle base de données de mots de passe, **cliquez** sur *create* (créer). 

![](/sbox/screen/keepassdroid-en/04.png)

*Graphique 4: Écran d'ouverture/création de la base de données.*

L'écran *Enter database password* (Entrer le mot de passe de la base de données) sera activé comme ci-dessous:

![](/sbox/screen/keepassdroid-en/05.png)

*Graphique 5 : Écran Entrer le mot de passe de la base de données.*

**Étape 2**. **Tapez** le mot de passe maître que vous avez inventé dans les champs *password* (mot de passe) et *confirm password* (confirmer le mot de passe), comme indiqué ci-dessous:

![](/sbox/screen/keepassdroid-en/06.png)

*Graphique 6 : Entrer un mot de passe*

**Conseil**: Assurez-vous d'avoir bien créé un mot de passe maître fort. Consultez [**3. Créer et sauvegarder des mots de passe sûrs**](https://securityinabox.org/fr/chapter-3) pour plus d'informations à ce sujet.

**Étape 3**. Cliquez sur **OK** pour activer l'écran suivant

![](/sbox/screen/keepassdroid-en/07.png)

*Graphique 7 : Écran d'accueil de KeePassDroid*

Félicitations ! Vous venez de créer une base de données de mots de passe sécurisée. Vous pouvez maintenant commencer à y déposer tous vos mots de passe actuels et futurs.

**Note**: Vous pouvez également copier les fichiers de base de données **KeePass** existants de votre ordinateur vers votre appareil Android, puis les ouvrir avec **KeePassDroid**.

<a name="2.2"></a>
## 2.2. Comment ajouter un groupe et une entrée ##

**KeePassDroid** conserve les entrées de mots de passe en groupes pour garder votre information organisée, les groupes par défaut sont **Email** et **Internet**, mais vous pouvez créer votre propre groupe en **cliquant** sur *Add Group* (ajouter un groupe) et en tapant le nom du groupe, puis sur *OK* pour activer l'écran suivant : 

![](/sbox/screen/keepassdroid-en/09.png) ![](/sbox/screen/keepassdroid-en/10.png)

*Graphiques 8 et 9 : Ajouter un nouveau groupe*

L'écran **Add entry** (ajouter une entrée) vous permet d'ajouter des informations de compte, des mots de passe et autres détails importants dans votre base de données nouvellement créée. Dans l'exemple qui suit, vous allez ajouter des entrées pour stocker les mots de passe et noms d'utilisateur pour d'autres sites web et comptes de messagerie.

**Étape 1**. **Cliquez** sur *Add Entry* (ajouter une entrée) pour activer l'écran *Add Entry* comme suit :

![](/sbox/screen/keepassdroid-en/11.png) ![](/sbox/screen/keepassdroid-en/12.png)

*Graphiques 10 et 11 : Ajouter une entrée de mot de passe.*

**Note**: L'écran *Ajouter une entrée* présente plusieurs champs à compléter. Aucun de ces champs n'est obligatoire ; l'information fournie ici est à utiliser à votre guise. Elle peut s'avérer utile si vous recherchez une entrée particulière.

Ces différentes zones de textes vous sont brièvement expliquées ci-dessous :

**Name** (nom) : Un nom pour spéficier l'entrée du mot de passe. Par exemple, votre mot de passe gmail.

**Username** (nom d'utilisateur) : Le nom d'utilisateur associé à l'entrée du mot de passe. Par exemple, securitybox@gmail.com

**URL** : Le site Internet associé à l'entrée du mot de passe. Par exemple, https://mail.google.com

**Password** (mot de passe) : Cette fonction génère un mot de passe aléatoire lorsque l'écran *Add an entry* (ajouter une entrée) est activé. Vous pouvez utiliser cette fonction si vous souhaitez modifier un mot de passe existant par un mot de passe généré par KeePassDroid. Comme KeePassDroid s'en souviendra toujours pour vous, il ne vous est pas même nécessaire de voir le mot de passe. Un mot de passe généré de façon aléatoire est considéré comme fort (c'est à dire qu'il sera difficile à un intrus de le deviner ou de le cracker).

La section suivante décrit comment générer un mot de passe aléatoire. Vous pouvez bien sûr remplacer le mot de passe par défaut par un mot que vous avez créé vous-même. Par exemple, si vous créez une entrée pour un compte déjà existant, vous entrerez le mot de passe correct ici.

**Confirm passwords** (confirmer les mots de passe) : La confirmation du mot de passe.

**Comments** (commentaires) : C'est ici que vous inscrivez l'information descriptive ou générale du compte ou du site pour lequel vous stockez des informations. Par exemple : Paramètres du serveur de messagerie : *POP3 SSL, pop.gmail.com, Port 995; SMTP TLS, smtp.gmail.com, Port: 465*

**Note** : Le fait de créer ou de modifier les entrées de mot de passe dans **KeePassDroid** ne change en rien vos mots de passe courants ! Considérez **KeePassDroid** comme un carnet d'adresses électroniques sûr pour vos mots de passe. Il ne stocke que ce que vous y écrivez, rien d'autre.

**Étape 2**. Cliquez sur **save** pour sauvegarder vos modifications de l'écran d'ajout d'entrées.

Votre nouvelle entrée apparaît alors dans le groupe.

![](/sbox/screen/keepassdroid-en/13.png)

*Graphique 12 : Nouvelle entrée apparaissant dans le groupe nouvellement créé.*

<a name="2.3"></a>
## 2.3 Comment modifier une entrée ##

Vous pouvez modifier une entrée existante dans **KeePassDroid** à tout moment. Vous pouvez changer votre mot de passe (il est généralement conseillé de changer de mot de passe tous les trois ou six mois pour plus de sécurité) ou modifier d'autres détails stockés dans l'entrée du mot de passe. 

Pour modifier une entrée, effectuez les étapes suivantes :

**Étape 1**. **Sélectionnez** le *groupe* correct pour activer les entrées auxquelles il est associé.

![](/sbox/screen/keepassdroid-en/14.png)

*Graphique 13 : Liste de groupes.*

**Étape 2**. **Sélectionnez** l'entrée correspondante, puis **cliquez** sur l'entrée sélectionnée pour activer la fenêtre suivante : 

![](/sbox/screen/keepassdroid-en/15.png)

*Graphique 14 : Aperçu de l'entrée.*

**Étape 3**. **Cliquez** sur **Edit** (modifier), vous pouvez maintenant modifier l'information donnée. Ceci effectué, **cliquez** sur **save** (enregistrer) pour conserver les modifications nécessaires à l'information, y compris le mot de passe.

![](/sbox/screen/keepassdroid-en/16.png)

*Graphique 15 : Modifier l'info.*

Pour échanger un mot de passe existant (que vous avez créé vous-même au préalable) contre un mot de passe généré et recommandé par **KeePassDroid**, veuillez lire la section suivante.

<a name="2.4"></a>
## 2.4 Comment générer des mots de passe aléatoires ##

Les mots de passe aléatoires longs sont considérés comme forts dans le domaine de la sécurité. Leur caractère aléatoire est basé sur des principes mathématiques et ne peut pas être simplement 'deviné' par quelqu'un cherchant à cracker l'un de vos comptes. KeePass fournit un générateur de mots de passe facilitant cette procédure. Comme il vous a été montré ci-dessus, un mot de passe aléatoire est automatiquement généré lorsque vous ajoutez une entrée. Cette section décrit comment en générer un vous-même.

**Note** : Le *générateur de mots de passe* peut être activé à partir des écrans *Add Entry* (ajouter une entrée) et *Edit Entry* (modifier une entrée).

![](/sbox/screen/keepassdroid-en/17.png)

*Graphique 16 : Info sur l'entrée de mots de passe.*

**Étape 1**. **Cliquez** la touche ![](/sbox/screen/keepassdroid-en/18.png) soit à partir de l'écran *Add Entry* soit de l'écran *Edit Entry* pour activer l'écran du *générateur de mots de passe* comme suit :

![](/sbox/screen/keepassdroid-en/19.png)

*Graphique 17 : Options pour la génération de mots de passe.*

L'écran du générateur de mots de passe offre plusieurs critères quant à la création d'un mot de passe. Vous pouvez entre autres spécifier la longueur du mot de passe souhaité, le type de caractères que vous souhaitez utiliser. À titre exemplaire, nous allons sélectionner les options suivantes :

- **Longueur** d'au moins 16 caractères
- **Cochez** Upper-case Letter (lettre majuscule)
- **Cochez** Lower-case Letter (lettre minuscule)
- **Cochez** Digits (chiffres)
- **Cochez** Minus (tirets)
- **Cochez** Brackets (parenthèses)
- **Cochez** Underline (soulignages)

![](/sbox/screen/keepassdroid-en/19.png)

*Graphique 18 : Options pour la création de mots de passe*

**Étape 2**. **Cliquez** sur ![](/sbox/screen/keepassdroid-en/20.png) pour démarrer la procédure. Une fois terminée, **KeePassDroid** affichera le mot de passe généré.

![](/sbox/screen/keepassdroid-en/21.png)

*Graphique 19 : Exemple de mot de passe aléatoire.*

**Étape 3**. **Cliquez** sur *Accept* (accepter) pour activer l'écran suivant :

![](/sbox/screen/keepassdroid-en/22.png)

*Graphique 20 : Informations de l'entrée*

**Note**: Vous pouvez afficher le mot de passe généré en sélectionnant l'option correspondante dans le menu. Toutefois, comme nous l'avons évoqué ci-dessus, ceci constitue un risque quant à la sécurité. Par essence, il n'est pas nécessaire de voir le mot de passe généré. Nous revenons sur ce sujet dans la section [**3.0 Comment utiliser les mots de passe**](https://securityinabox.org/fr/keepass_motsdepasse).

**Étape 4**. **Cliquez** sur *Save* (enregistrer) pour accepter le mot de passe et retourner à l'écran *Entry* (entrée), comme suit :

![](/sbox/screen/keepassdroid-en/23.png)

*Graphique 21 : Écran d'entrée*

<a name="2.5"></a>
## 2.5 Comment verrouiller la base de données KeePassDroid ##

**Étape 1**. **Cliquez** sur la touche **Menu** pour activer l'écran suivant :

![](/sbox/screen/keepassdroid-en/24.png)

*Graphique 22 : Options du menu*

**Étape 2**. **Cliquez** sur *Lock Database* (verrouiller la base de données) pour désactiver la console **KeePassDroid** comme ci-dessous :

![](/sbox/screen/keepassdroid-en/25.png)

*Graphique 23 : Base de données verrouillée*

Il vous faut entrer votre mot de passe à nouveau pour accéder à votre base de données **KeePassDroid**.

<a name="2.6"></a>
## 2.6 Comment créer une sauvegarde du fichier de la base de mots de passe ##

Le fichier de la base de données **KeePassDroid** de votre téléphone Android est indiqué par son extension de fichier .kdb. Vous pouvez copier ce fichier sur votre ordinateur ou votre clé USB. Personne d'autre que vous ne sera en état d'ouvrir cette base de données sans le mot de passe maître.

**Note** : Pour ouvrir la base de données **KeePassDroid** que vous avez copiée depuis votre appareil Android sur votre ordinateur, vous devez vous assurer que le programme KeePass a bien été installé sur votre ordinateur ou que vous en avez la version portable sur votre clé USB.

Consultez s'il vous plaît [**Portable KeePass**](https://securityinabox.org/en/keepass_portable) pour plus d'informations.

<a name="2.7"></a>
## 2.7 Comment réinitialiser votre mot de passe maître ##

Vous pouvez modifier le mot de passe principal à tout moment. Ceci peut être effectué une fois que vous avez ouvert la base de données de mots de passe.

**Étape 1**. **Sélectionnez** la base de données et **cliquez** sur *Menu* pour activer l'écran suivant :

![](/sbox/screen/keepassdroid-en/26.png)

*Graphique 24 : Options du menu*

**Étape 2**. **Cliquez** sur **Change Master key** (modifier la clé principale) pour activer l'écran suivant :

![](/sbox/screen/keepassdroid-en/27.png)

*Graphique 25 : Entrer un nouveau mot de passe.*

**Étape 3**. Entrez votre mot de passe dans les champs **Password** (mot de passe) et **Confirm Password** (confirmer le mot de passe), puis **cliquez** sur OK.

![](/sbox/screen/keepassdroid-en/28.png)

*Graphique 26 : Entrer un nouveau mot de passe*

## 3.0 Comment utiliser les mots de passe KeePassDroid ##

Puisqu'un mot de passe sécurisé est difficile à mémoriser, **KeePassDroid** vous permet de le copier depuis la base de données et de le coller directement dans le compte ou le site Internet qui le requiert. 

Pour plus de sécurité, vous pouvez faire en sorte que le mot de passe copié dans le presse-papier n'y reste que **30 secondes**, **1 minute**, ou **5 minutes** de sorte que vous puissiez y coller le mot de passe correspondant sans devoir vous dépêcher avant qu'il ne soit automatiquement effacé du presse-papier. 

Vous pouvez voir ces options dans l'écran suivant en allant à : **Menu** > **Settings** (paramètres) > **Application** > **Clipboard timeout** (délai presse-papier)

![](/sbox/screen/keepassdroid-en/29.png)

*Graphique 27 : Options délai du presse-papier.*

### Copier un mot de passe KeePassDroid

**Étape 1**. Cliquez dans **Menu** sur le mot de passe requis pour activer l'écran suivant :

![](/sbox/screen/keepassdroid-en/30.png)

*Graphique 28 : Options mots de passe*

**Étape 2**. **Sélectionnez** ![](/sbox/screen/keepassdroid-en/31.png)

**Étape 3**. **Ouvrez** le compte ou le site afférent et **collez** le mot de passe dans le champ correspondant en cliquant et maintenant le champ correspondant, puis sélectionnez *Paste* (coller) :

![](/sbox/screen/keepassdroid-en/32.png)

*Graphique 29 : Options édition de texte*

**Note**: Si vous utilisez **KeePassDroid** tout le temps, vous n'avez jamais réellement besoin de voir ou de connaître votre mot de passe. Les fonctions copier/coller suffisent à le déplacer depuis la base de données vers la fenêtre requise. Si vous utilisez la fonction *Générateur aléatoire* puis transférez le mot de passe vers le processus d'inscription d'un nouveau compte de messagerie, vous utiliserez un mot de passe que vous n'avez jamais vu. Et il continue de remplir sa tâche !

### Verrouiller la base de données selon un délai

Il vous est également possible de verrouiller votre base de données lorsque l'application est restée inactive durant un temps déterminé. Ceci peut être affectué en allant à :

**Menu** > **Settings** (paramètres) > **Application** **Cliquez** sur **Application timeout** (délai application) pour activer ce qui suit :


![](/sbox/screen/keepassdroid-en/33.png)

*Graphique 30 :* Options Délai de l'application.

**Sélectionnez** le délai de verrouillage de votre base de données.

