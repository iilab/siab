

---

lang: fr
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: How to Use Enigmail with GnuPG in Thunderbird

---

Sommaire de sections de cette page:

- [**4.0 Un aperçu d'Enigmail, de GnuPG et du chiffrement asymétrique (à clé privée)**](#4.0)
- [**4.1 Comment installer Enigmail et GnuPG**](#4.1)
- [**4.2 Comment générer des paires de clés et configurer Enigmail pour qu'il fonctionne avec vos comptes de courriel**](#4.2)
- [**4.3 Comment échanger des clés publiques**](#4.3)
- [**4.4 Comment valider et signer un paire de clés**](#4.4)
- [**4.5 Comment chiffrer et déchiffrer des messages**](#4.5)

-------

<a name="4.0"></a>
## 4.0 Un aperçu d'Enigmail, de GnuPG et du chiffrement asymétrique (à clé privée) ##

**Enigmail** est un module complémentaire de **Mozilla Thunderbird** qui vous permet de protéger la confidentialité de vos communications par courrier électronique. **Enigmail** n'est rien d'autre qu'une interface graphique conçue pour faciliter l'utilisation du programme de chiffrement **GnuPG** avec **Thunderbird**. L'interface d'**Enigmail** est représentée par un lien *OpenPGP* dans la barre d'outils de la console **Thunderbird**. 

**Enigmail** emploie la méthode de [**cryptographie asymétrique, ou cryptographie à clé publique**](http://fr.wikipedia.org/wiki/Cryptographie_asym%C3%A9trique). En vertu de cette méthode, chaque individu doit générer sa propre paire de clés. La première clé est dite *privée*. Celle-ci est protégée par un mot de passe complexe, gardée secrète et *jamais* partagée avec *qui que ce soit*.

La deuxième clé est dite *publique*. Cette clé peut être partagée avec vos correspondants. Lorsque vous avez la *clé publique* d'un correspondant, vous pouvez commencer à envoyer des messages chiffrés à cette personne. Elle, et elle seule, sera en mesure de déchiffrer et de lire vos messages, car elle est la seule personne qui dispose de la *clé privée* correspondante.

De la même façon, si vous envoyez une copie de votre propre *clé publique* à tous vos contacts et gardez la *clé privée* secrète, vous et vous seul serez en mesure de lire les messages chiffrés que vous enverront vos contacts.

**Enigmail** vous permet également d'attacher des *signatures numériques* à vos messages. Le destinataire de votre message qui dispose d'une copie légitime de votre clé publique pourra vérifier que le message provient bel et bien de vous, et que son contenu n'a pas été altéré en chemin. En échange, si vous avez la clé publique d'un correspondant, vous pouvez vérifier la signature numérique de ses messages.

<a name="4.1"></a>
## 4.1 Comment installer Enigmail et GnuPG ##

Veuillez consulter la section [**Téléchargement**](http://securityinabox.org/fr/thunderbird_principale) pour obtenir les consignes de téléchargement d'**Enigmail** et de **GnuPG**.

### 4.1.1 Comment installer GnuPG ###

L'installation de **GnuPG** est très simple et ressemble au processus d'installation de programmes que vous avez déjà probablement déjà effectué.

Pour installer **GnuPG**, suivez les étapes énumérées ci-dessous:

**Première étape**. **Double-cliquez** sur ![](/sbox/screen/thunderbird-fr/40.png) pour lancer le processus d'installation. Il est possible que la boîte di dialogue *Fichier ouvert - Avertissement de sécurité* s'affiche. Si c'est le cas, **cliquez** sur ![](/sbox/screen/thunderbird-fr/02.png) pour afficher la fenêtre suivante:

![](/sbox/screen/thunderbird-fr/41.png)

*Figure 1: L'assistant d'installation de GNU Privacy Guard*

**Deuxième étape**. **Cliquez** sur ![](/sbox/screen/thunderbird-en/04.png) pour afficher la fenêtre *GNU Privacy Guard Setup - License Agreement*; après l'avoir lu, **cliquez** sur ![](/sbox/screen/thunderbird-en/04.png) pour afficher la fenêtre *GNU Privacy Guard Setup - Choose Components*.

**Troisième étape**. **Cliquez** sur ![](/sbox/screen/thunderbird-en/04.png) pour accepter les paramètres par défaut et afficher la fenêtre *GNU Privacy Guard Setup - Install Options - GnuPG Language Selection*. 

**Quatrième étape**. **Sélectionnez** *fr-Français* dans la liste défilante, puis **Cliquez** sur ![](/sbox/screen/thunderbird-en/04.png) pour afficher la fenêtre *Choose Install Location*.

**Cinquième étape**. **Cliquez** sur ![](/sbox/screen/thunderbird-en/04.png) pour accepter l'emplacement par défaut et afficher la fenêtre *Choose Start Menu Folder*.

**Sixième étape**. **Cliquez** sur ![](/sbox/screen/thunderbird-en/06.png) pour installer **GnuPG**. Lorsque ce processus est complété, la fenêtre *Installation Complete* s'affiche.

**Septième étape**. **Cliquez** sur ![](/sbox/screen/thunderbird-en/04.png), puis sur ![](/sbox/screen/thunderbird-en/08.png) pour finaliser l'installation du programme **GnuPG**.

### 4.1.2 Comment installer le module complémentaire Enigmail ###

Après avoir complété l'installation du programme **GnuPG**, il vous faut installer le module complémentaire **Enigmail**. 

Pour lancer l'installation d'**Enigmail**, suivez les étapes énumérées ci-dessous:

**Première étape**. **Ouvrez Thunderbird**, puis **sélectionnez Outils > Modules complémentaires** pour afficher la fenêtre *Modules complémentaires*; le panneau *Catalogue* sera affiché par défaut.

**Deuxième étape**. **Cliquez** sur ![](/sbox/screen/thunderbird-fr/44.png) pour afficher la fenêtre suivante: 

![](/sbox/screen/thunderbird-fr/45.png)

*Figure 3: La fenêtre Modules complémentaires affichant le panneau Extensions*

**Troisième étape**. **Cliquez** sur ![](/sbox/screen/thunderbird-fr/46.png) pour afficher la fenêtre suivante:

![](/sbox/screen/thunderbird-fr/47.png)

*Figure 4: La fenêtre Choisissez une extension à installer*

**Quatrième étape**. Naviguez jusqu'à l'emplacement du dossier où vous avez sauvegardé **Enigmail**, puis **cliquez** sur ![](/sbox/screen/thunderbird-fr/48.png) pour afficher la fenêtre suivante:

![](/sbox/screen/thunderbird-fr/49.png)

*Figure 5: La fenêtre Installation d'un logiciel*

**Important**: Avant de franchir cette étape, assurez-vous que vos tâches et travaux en ligne aient été sauvegardés!

**Cinquième étape**. **Cliquez** sur ![](/sbox/screen/thunderbird-fr/50.png) pour revenir à la *figure 5*, puis **cliquez** sur ![](/sbox/screen/thunderbird-fr/51.png) pour finaliser l'installation du module complémentaire **Enigmail**. 

Pour vérifier que l'installation d'**Enigmail** a bien été complétée, retournez à la console **Thunderbird**, et vérifiez si le bouton *OpenPGP* apparaît désormais dans la barre d'outils de **Thunderbird**. 

![](/sbox/screen/thunderbird-fr/52.png)

*Figure 6: La barre d'outils de Thunderbird avec l'onglet OpenPGP en surbrillance*

### 4.1.3 Comment confirmer qu'Enigmail et GnuPG fonctionnent normalement ###

Avant de commencer à utiliser **Enigmail** et **GnuPG** pour authentifier et chiffrer vos messages, vous devez d'abord vous assurer que les deux programmes communiquent normalement entre eux.

**Première étape**. **Sélectionnez OpenPGP > Préférences** pour afficher la fenêtre *Préférences OpenPGP*: 

![](/sbox/screen/thunderbird-fr/53.png)

*Figure 7: La fenêtre Préférences OpenPGP*

Si **GnuPG** a été correctement installé, la ligne ![](/sbox/screen/thunderbird-fr/54.png) sera visible dans la section *Fichiers et répertoires*; sinon il est possible que vous receviez un alerte semblable à celle-ci:

![](/sbox/screen/thunderbird-fr/55.png)

*Figure 8: Exemple d'alerte OpenPGP*

**Astuce**: Si vous avez reçu un tel message, il est possible que vous ayez installé le fichier au mauvais emplacement. Si tel est le cas, **cochez** l'option *Outrepasser avec* pour activer le bouton *Parcourir*, **cliquez** sur ![](/sbox/screen/thunderbird-fr/69.png) pour activer la fenêtre *Localiser l'agent GnuPG* et naviguer jusqu'à l'emplacement du fichier *gpg.exe* sur votre ordinateur.

**Deuxième étape**. **Cliquez** sur ![](/sbox/screen/thunderbird-fr/56.png) pour retourner à la console **Thunderbird**.

<a name="4.2"></a>
## 4.2 Comment générer des paires de clés et configurer Enigmail pour qu'il fonctionne avec vos comptes de courriel ##

Lorsque vous avez confirmé qu'**Enigmail** et **GnuPG** fonctionnent correctement, vous être prêt à configurer un ou plusieurs de vos comptes de courrier électronique afin d'utiliser **Enigmail** pour générer une ou plusieurs paires de clés.

### 4.2.1 Comment utiliser l'assistant de configuration OpenPGP pour générer une paire de clés ###

**Enigmail** offre deux méthodes distinctes pour générer un paire de clés privée/publique; la première consiste à utiliser l'*Assistant de configuration OpenPGP*, et la seconde à employer la fenêtre *Gestion de clefs*.

Pour générer une première paire de clés à l'aide de l'*Assistant de configuration OpenPGP*, veuillez suivre les étapes énumérées ci-dessous: 

**Première étape**. **Sélectionnez OpenPGP > Assistant de configuration** pour ouvrir la fenêtre *Assistant de configuration OpenPGP*: 

![](/sbox/screen/thunderbird-fr/58.png)

*Figure 9: La fenêtre Assistant de configuration OpenPGP - Bienvenue*

**Deuxième étape**. **Cliquez** sur ![](/sbox/screen/thunderbird-fr/04.png) pour afficher la fenêtre suivante:

![](/sbox/screen/thunderbird-fr/59.png)

*Figure 10: La fenêtre Sélectionnez une identité*

**Troisième étape**. **Cliquez** sur ![](/sbox/screen/thunderbird-fr/04.png) pour afficher la fenêtre suivante:

![](/sbox/screen/thunderbird-fr/60.png)

*Figure 11: La fenêtre Signature - Signer numériquement vos messages sortants*

**Quatrième étape**. **Cliquez** sur ![](/sbox/screen/thunderbird-fr/04.png) pour afficher la fenêtre suivante:

![](/sbox/screen/thunderbird-fr/61.png)

*Figure 12: La fenêtre Chiffrement - Chiffrer vos messages sortants*

**Cinquième étape**. **Cliquez** sur ![](/sbox/screen/thunderbird-fr/04.png) pour afficher la fenêtre suivante:

![](/sbox/screen/thunderbird-fr/62.png)

*Figure 13: La fenêtre Désirez-vous modifier quelques paramètres par défaut afin qu'OpenPGP fonctionne mieux sur votre machine?*

**Sixième étape**. **Cliquez** sur ![](/sbox/screen/thunderbird-fr/63.png) pour afficher la fenêtre suivante:

![](/sbox/screen/thunderbird-fr/64.png)

*Figure 14: La fenêtre Préférences*

**Commentaire**: À la section *3.2 Comment désactiver la fonction HTML dans Thunderbird*, nous avons vu brièvement comment les messages mis en pages en HTML peuvent vous exposer à différentes menaces. Ici, les options *Afficher les corps des messages en texte brut* et *Ne pas composer les messages en HTML* servent précisément à prendre des précautions contre ces menaces.

**Septième étape**. **Cliquez** sur ![](/sbox/screen/thunderbird-fr/56.png) pour revenir à l'*Assistant de configuration OpenPGP*, puis **cliquez** sur ![](/sbox/screen/thunderbird-fr/04.png) pour afficher la fenêtre *Créer une clef - Créer une clef pour signer et chiffrer les messages*. 

**Commentaire**: La première fois que créerez une paire de clés, aucun de vos comptes de courriel n'apparaîtra dans la liste défilante.

**Huitième étape**. **Saisissez** un mot de passe complexe (ou phrase secrète) d'au moins 8 caractères alphanumériques dans les deux champs *Phrase secrète*:

![](/sbox/screen/thunderbird-fr/65.png)

*Figure 15: La fenêtre Créer une clef - Créer une clef pour signer et chiffrer les messages*

**Neuvième étape**. **Cliquez** sur ![](/sbox/screen/thunderbird-fr/04.png) pour confirmer ces réglages, puis **cliquez** sur ![](/sbox/screen/thunderbird-fr/66.png) pour retourner à la fenêtre *Créer un clef*; le nom de votre premier compte de courriel devrait  maintenant être affiché, comme suit: 

![](/sbox/screen/thunderbird-fr/67.png)

*Figure 16: Le Compte /ID utilisateur nouvellement créé*

**Dixième étape**. **Cliquez** sur ![](/sbox/screen/thunderbird-fr/04.png) pour afficher la fenêtre *Résumé*, qui devrait être fidèle aux réglages utilisés lors de la création de la paire de clés.

**Commentaire**: Chaque paire de clés générée avec l'*Assistant de configuration OpenPGP* est automatiquement basée sur une structure 2048-bit et a une durée de vie de 5 ans. Ces deux caractéristiques ne peuvent pas être modifiées après la création d'une paire de clés à l'aide de cette méthode.

### 4.2.2 Comment générer une paire de clés et un certificat de révocation supplémentaires pour un autre compte de courriel ###

Il est de pratique courante de conserver une paire de clés distincte pour chaque compte de courriel. Suivez les étapes énumérées ci-dessous pour générer des paires de clés supplémentaires pour vos autres comptes. La création d'une paire de clés implique également la création d'un *certificat de révocation* qui lui est associé. Envoyez ce certificat à vos contacts pour leur permettre de désactiver votre clé publique dans l'éventualité où votre clé privée serait compromise ou perdue.

**Première étape**. **Sélectionnez OpenPGP > Gestion de clefs** pour afficher la fenêtre suivante:

![](/sbox/screen/thunderbird-fr/70.png)

*Figure 17: Le menu Générer du gestionnaire de clefs OpenPGP Key avec l'option Nouvelle paire de clefs sélectionnée*

**Commentaire**: **Cochez** l'option *Afficher toutes les clefs par défaut* pour afficher la paire de clés générée à l'aide de l'*Assistant de configuration OpenPGP* pour votre premier compte de courriel, tel qu'illustré à la *figure 17* ci-dessus.

**Deuxième étape**. **Sélectionnez Générer > Nouvelle paire de clefs** dans la fenêtre de *gestion de clefs*, tel qu'illustré à la *figure 20* ci-dessus, pour afficher la fenêtre suivante:

![](/sbox/screen/thunderbird-fr/71.png)

*Figure 18: La fenêtre Génération de clefs OpenPGP*

**Troisième étape**. **Sélectionnez** un compte de courrier électronique dans la liste défilante *Compte / ID utilisateur*, puis **cochez** l'option *Utiliser la clef générée pour l'identité sélectionnée*. Créez ensuite une phrase secrète pour protéger votre clé privée.

**Commentaire**: Comme son nom l'indique, une phrase secrète est en quelque sorte un mot de passe long et complexe. **Enigmail** vous demande de choisir un mot de passe qui est plus long et plus complexe que d'habitude.

**Important**: Il faut *toujours* générer une paire de clés avec une phrase secrète, et ne *jamais* activer l'option 'Pas de phrase secrète'.

![](/sbox/screen/thunderbird-en/72.png)

*Figure 19: La fenêtre Génération de clef OpenPGP affichant l'onglet Expiration de la clef*

**Commentaire**: La durée de vie d'une paire de clés dépend uniquement de vos besoins en matière de confidentialité et de sécurité. Plus vous changez fréquemment de paires de clés, plus il est difficile pour une tierce partie de compromettre votre nouvelle paire de clés. Par contre, chaque fois que vous changez de paire de clés, vous devez l'envoyer à vos correspondants et recommencer la vérification.

**Cinquième étape**. **Saisissez** le nombre approprié, puis **sélectionnez** l'unité de temps désiré (*jours*, *mois* ou *années*) pour déterminer la durée de vie de la paire de clés. 

**Sixième étape**. **Cliquez** sur ![](/sbox/screen/thunderbird-fr/73.png) pour afficher la fenêtre suivante:

![](/sbox/screen/thunderbird-fr/74.png)

*Figure 20: La boîte de dialogue de Confirmation OpenPGP*

**Septième étape**. **Cliquez** sur ![](/sbox/screen/thunderbird-fr/73.png) pour afficher la fenêtre suivante:

![](/sbox/screen/thunderbird-fr/75.png)

*Figure 21: La boîte de dialogue de Confirmation OpenPGP*

**Huitième étape**. **Cliquez** sur ![](/sbox/screen/thunderbird-fr/76.png) pour afficher la fenêtre de navigation *Créer et enregistrer le certificat de révocation*.

**Commentaire**: Si avez connaissance qu'une tierce partie hostile ou malveillante est parvenu à accéder sans autorisation à votre clé privée, ou que vous avez vous-même perdu l'accès, vous pouvez envoyer un certificat de révocation à vos contacts pour les informer qu'ils ne doivent plus utiliser votre clé publique. Soyez aussi conscient que vous devrez mener cette opération si votre ordinateur est perdu, volé ou confisqué. Il est fortement recommandé de faire une copie de sauvegarde sécurisée de votre certificat de révocation.

![](/sbox/screen/thunderbird-fr/77.png)

*Figure 22: La fenêtre Créer et enregistrer le certificat de révocation*

**Neuvième étape**. **Cliquez** sur ![](/sbox/screen/thunderbird-fr/78.png) pour afficher la fenêtre suivante; puis **saisissez** la phrase secrète associée à ce compte:

![](/sbox/screen/thunderbird-fr/79.png) 

*Figure 23: La fenêtre Veuillez saisir votre phrase secrète OpenPGP*

**Dixième étape**. **Cliquez** sur ![](/sbox/screen/thunderbird-fr/56.png) pour finaliser la génération de la paire de clés et du certificat de révocation, et revenir à la fenêtre suivante:

![](/sbox/screen/thunderbird-fr/80.png) 

*Figure 24: La fenêtre Gestion de clefs OpenPGP affichant la nouvelle paire de clés*

**Commentaire**: **Cochez** l'option *Afficher toutes les clefs par défaut* pour afficher toutes les clés avec leur compte respectif, si vous êtes seul et dans un milieu sûr.

Maintenant que vous avez générer une paire de clés et un certificat de révocation, vous êtes prêt à échanger vos clés publiques avec un correspondant de confiance.

### 4.2.3 Comment configurer Enigmail pour une utilisation avec votre compte de courrier électronique ###

Pour activer l'utilisation d'**Enigmail** avec un compte en particulier, suivez les étapes énumérées ci-dessous: 

**Première étape**. **Sélectionnez Outils > Paramètres des comptes**.

**Deuxième étape**. **Sélectionnez** l'item de menu *OpenPGP* dans l'encadré de gauche, tel qu'illustré ci-dessous:

![](/sbox/screen/thunderbird-fr/57.png)

*Figure 25: La fenêtre Paramètres des comptes - OpenPGP*

**Troisième étape**. **Cochez** l'option *Activer le support OpenPGP (Enigmail) pour cette identité* et **sélectionnez** l'option *Utiliser l'adresse électronique de cette identité pour identifier la clef OpenPGP*, tel qu'illustré ci-dessus à la *figure 25*.

**Quatrième étape**. **Cliquez** sur ![](/sbox/screen/thunderbird-fr/56.png) pour revenir à la console **Thunderbird**.

<a name="4.3"></a>
## 4.3 Comment échanger vos clés publiques ##

Avant de commencer à envoyer et recevoir des messages chiffré, vous et vos correspondants devez échanger vos clés publiques. Vous devez également confirmer la validité des clés que vous acceptez en vous assurant qu'elles appartiennent bel et bien aux expéditeurs qui sont censées vous les avoir envoyées.

### 4.3.1 Comment envoyer une clé publique avec Enigmail ###

Pour envoyer une clé publique en utilisant **Enigmail**/**OpenPGP**, vous et votre correspondant devez suivre les étapes énumérées ci-dessous:

**Première étape**. **Ouvrez Thunderbird**, puis **cliquez** sur ![](/sbox/screen/thunderbird-fr/81.png) pour rédiger un nouveau message.

**Deuxième étape**. **Sélectionnez** l'option de menu **OpenPGP > Attacher ma clef publique**.

**Commentaire**: Avec cette méthode, la clé ne s'affiche pas immédiatement dans le panneau **Pièces jointes**; il apparaîtra aussitôt que vous enverrez le message.

Si vous souhaitez envoyer une autre clé publique, sélectionnez l'option de menu **OpenPGP > Attacher une clef publique...** et sélectionnez la clé que vous désirez envoyer.

![](/sbox/screen/thunderbird-fr/82.png) 

*Figure 26: La fenêtre de rédaction d'un message affichant la clé publique dans le panneau des pièces jointes*

**Troisième étape**. **Cliquez** sur ![](/sbox/screen/thunderbird-fr/101.png) pour envoyer votre message avec votre clé publique jointe. Il est possible que la fenêtre suivante s'affiche alors:

![](/sbox/screen/thunderbird-fr/104.png)

*Figure 28: La fenêtre d'invite de OpenPGP servant à définir le mode de chiffrement et de signature par défaut* 

**Quatrième étape**. **Cochez** l'option *Chiffrer/signer le message en entier*, puis **cliquez** sur ![](/sbox/screen/thunderbird-fr/56.png) pour afficher la fenêtre d'invite illustrée à la *figure 23*.

**Cinquième étape**. **Saisissez** votre phrase secrète, puis **cliquez** sur ![](/sbox/screen/thunderbird-fr/56.png) pour afficher la fenêtre suivante:

![](/sbox/screen/thunderbird-en/105.png)

*Figure 29: La fenêtre d'invite d'OpenPGP - Do you want to encrypt the message before saving screen* 

**Sixième étape**. **Cliquez** sur ![](/sbox/screen/thunderbird-en/106.png) pour chiffrer, signer et envoyer votre message.

### 4.3.2 Comment importer une clé publique avec Enigmail ###

Vous et votre correspondant devrez suivre les étapes énumérées ci-dessous pour importer la clé publique de l'autre: 

**Première étape**. **Sélectionnez** et **ouvrez** le message qui contient la clé publique de votre correspondant.

Si la clé publique de votre correspondant est incorporée au message, le bouton *Déchiffrer* sera activé et l'en-tête suivante s'affichera dans le panneau du message: 

![](/sbox/screen/thunderbird-fr/84.png) 

*Figure 30: Le message Cliquez sur le bouton 'Déchiffrer' pour importer la clef publique jointe au message*

**Deuxième étape**. **Cliquez** sur ![](/sbox/screen/thunderbird-en/85.png) pour lancer automatiquement le balayage du message reçu pour détecter des données chiffrées. Lorsqu'*Enigmail/OpenPGP* détecte un message contenant une clé publique, il vous demande d'importer la clé comme suit: 

![](/sbox/screen/thunderbird-fr/86.png)

*Figure 31: L'invite de confirmation OpenPGP Importer la/les clef(s) publique(s) incorporée(s) au message?* 

**Troisième étape**. **Cliquez** sur ![](/sbox/screen/thunderbird-fr/87.png) pour importer la clé publique de votre correspondant.

Si vous avez réussi à importer la clé publique, un message semblable à celui-ci s'affichera: 

![](/sbox/screen/thunderbird-fr/108.png)

*Figure 32: Une fenêtre d'alerte OpenPGP affichant la clé publique de votre correspondant*

Pour confirmer que vous avez reçu la clé publique de votre correspondant, suivez les étapes énumérées ci-dessous: 

**Première étape**. **Sélectionnez OpenPGP > Gestion de clefs** pour afficher la fenêtre *Gestion de clefs OpenPGP*:

![](/sbox/screen/thunderbird-fr/107.png)

*Figure 33: La fenêtre OpenPGP - Gestion de clefs affichant la clé publique récemment importée* 

<a name="4.4"></a>
## 4.4 Comment valider et signer un paire de clés ##

Finalement, vous devez vérifier que la clé importée appartient bel et bien à la personne censée vous l'avoir envoyée, et confimrer sa 'validité'. C'est une étape importante que vous et vos contacts devrez suivre pour chaque clé publique que vous recevez.

### 4.4.1 Comment valider une paire de clés ###

**Première étape**. **Contactez** votre correspondant par un autre moyen de communication que le courrier électronique. Vous pouvez utiliser le téléphone, le message texte,  You can use a telephone, text messages, la **Voix sur réseau IP** (**VoIP**) ou toute autre méthode, mais vous **devez** être absolument certain que vous communiquez avec la bonne personne. À cet égard, les conversations téléphonique ou les rencontres en face à face sont les meilleures solutions possibles, si vous êtes en mesure de le faire.

**Deuxième étape**. Vous et votre correspondant devez vérifier l'empreinte des clés publiques que vous avez échangées. Une empreinte est une série unique de chiffres et de lettres qui sert à identifier chaque clé. Vous pouvez utiliser la fenêtre de *Gestion de clefs* d'**OpenPGP** pour visualiser l'empreinte des paires de clés que vous avez créées et des clés publiques que vous avez importées.

Pour visualiser l'empreinte d'une paire de clés en particulier, suivez les étapes énumérées ci-dessous:

**Première étape**. **Sélectionnez > OpenPGP > Gestion de clefs**, puis **cliquez à droite** sur la clé dont vous voulez vérifier l'empreinte pour afficher le menu contextuel suivant:

![](/sbox/screen/thunderbird-fr/90.png) 

*Figure 34: Le menu contextuel de Gestion de clefs d'OpenPGP avec l'item Propriétés de la clef sélectionné*

**Deuxième étape**. **Sélectionnez** l'item *Propriété de la clef* pour afficher la fenêtre suivante:

![](/sbox/screen/thunderbird-fr/91.png)

*Figure 35: La fenêtre Propriétés de la clef*

Votre correspondant devrait suivre les mêmes étapes. Confirmez l'un auprès de l'autre que l'empreinte des clés que vous avez correspond bel et bien à l'original. Si les empreintes ne correspondent pas, échangez vos clés publiques à nouveau et répétez le processus de validation.

**Commentaire**: L'empreinte elle-même n'est pas secrète et peut être enregistrée quelque part en vue d'une vérification ultérieure.

### 4.4.2 Comment signer une clé publique validée ###

Lorsque vous avez déterminé que la clé publique d'un correspondant donné est valide, vous devez la *signer* pour confirmer que vous considérez cette clé comme valide.

Pour signer une clé publique validée, suivez les étapes énumérées ci-dessous:

**Première étape**. **Cliquez** sur ![](/sbox/screen/thunderbird-fr/56.png) pour revenir à la fenêtre *Gestion de clefs*

**Deuxième étape**. **Cliquez à droite** sur la clé publique de votre correspondant, puis **sélectionnez** l'item *Signer la clef* dans le menu contextuel pour afficher la fenêtre suivante:

![](/sbox/screen/thunderbird-fr/92.png)

*Figure 36: La fenêtre OpenPGP - Signature de la clef*

**Troisième étape**. **Cochez** l'option *J'ai fait une vérification très poussée*, puis **cliquez** sur ![](/sbox/screen/thunderbird-fr/56.png) pour compléter la signature de la clé publique de votre correspondant, finaliser le processus de validation et revenir à la fenêtre *Gestion de clefs OpenPGP*: 

![](/sbox/screen/thunderbird-en/93.png)

*Figure 37: La fenêtre Gestion de clefs OpenPGP affichant la paire de clés validée*

#### 4.4.3 COmment gérer vos paires de clés ####

La fenêtre *Gestion de clefs OpenPGP* est utilisée pour générer, valider et signer différentes paires de clés. Il vous est aussi possible de mener d'autres tâches de gestion, y compris: 

- **Modifier la phrase secrète**: Cette fonction vous permet de changer la phrase secrète qui protège votre paire de clés.
- **Gérer les identifiants utilisateurs**: Cette fonction vous permet d'associer plus d'un compte de courriel à une paire de clés donnée.
- **Créer et enregistrer un certificat de révocation**: Cette fonction vous permet de générer un nouveau certificat de révocation si vous avez perdu celui que vous aviez créé à l'origine.

<a name="4.5"></a>
## 4.5 Comment chiffrer et déchiffrer des messages ##

**Important**: L'en-tête d'un message de courrier électronique, c'est-à-dire le *Sujet* et les destinataires (y compris tous les renseignements inclus dans les champs *Pour*, *CC* et *BCC*), *ne peut pas* être chiffrée et sera envoyée en clair. Pour préserver la confidentialité et la sécurité de vos communications par courriel, le sujet ou le titre de vos messages devraient être vague et non descriptifs pour éviter de révéler des renseignements sensibles. De plus, il est fortement recommandé de mettre toutes les adresses de vos destinataires dans le champs *BCC* lorsque vous envoyez des messages à un groupe de personnes.

Lorsque vous chiffrez des messages avec des pièces jointes, il est fortement recommandé d'utiliser l'option **PGP/MIME**, puisque ceci étendra le chiffrement aux fichiers joints au message.

### 4.5.1 Comment chiffrer un message ###

Une fois que vous et votre correspondant avez tous deux importé, validé et signé vos clés publiques respectives, vous êtes désormais prêts à envoyer des messages chiffrés et à déchiffrer ceux que l'on vous envoie.

Pour chiffrer le contenu d'un message, suivez les étapes énumérées ci-dessous:

**Première étape**. **Ouvrez** votre compte de courriel et  **cliquez** sur ![](/sbox/screen/thunderbird-fr/81.png) pour rédiger un nouveau message.

**Deuxième étape**. **Cliquez** sur ![](/sbox/screen/thunderbird-fr/94.png) pour afficher la fenêtre suivante:

![](/sbox/screen/thunderbird-fr/95.png)

*Figure 38: La fenêtre Chiffrement OpenPGP*

**Commentaire**: Si vous avez coché l'option *Chiffrer/signer le message en entier et l'envoyer en utilisant **PGP**/**MIME*** à la *figure 28* tel qu'indiqué, la *figure 38* ne s'affichera pas.

**Troisième étape**. **Cochez** les options *Signer le  message* et *Chiffrer le message* tel qu'illustré à la *figure 38*, puis **cliquez** sur ![](/sbox/screen/thunderbird-fr/56.png) pour finaliser la signature et le chiffrement de votre message.

**Commentaire**: Pour vérifier que votre message sera bel et bien chiffré et signé, assurez-vous que les deux icones ci-dessous figurent dan sle coin inférieur droit du panneau de message: 

![](/sbox/screen/thunderbird-fr/97.png)

*Figure 39: Les icones de confirmation de la signature et du chiffrement*

**Quatrième étape**. **Cliquez** sur ![](/sbox/screen/thunderbird-fr/101.png) pour envoyer le message. Une fenêtre d'invite vous demande de saisir votre phrase secrète pour utiliser votre clé privée et signer le message.

### 4.5.2 Comment déchiffrer un message ###

Lorsque vous recevez un message chiffré, **Enigmail/OpenPGP** tentera automatiquement de le déchiffrer sur réception ou lorsque vous souuhaitez l'ouvrir. La fenêtre suivante s'affiche: 

![](/sbox/screen/thunderbird-fr/79.png)

*Figure 40: La fenêtre d'invite d'OpenPGP - Veuillez saisir votre phrase secrète OpnePGP ou le code PIN de votre carte à puce*

**Première étape**. **Saisissez** votre phrase secrète tel qu'illustré à la *figure 40*.

Lorsque vous avez saisi la phrase secrète de votre clé privée, le message est déchiffré et affiché en clair: 

![](/sbox/screen/thunderbird-en/109.png)

*Figure 41: Le message déchiffré dans le panneau de message*

Vous avez réussi à déchiffrer le message. En répétant les étapes énumérées à la section **4.5 Comment chiffrer et déchiffrer des messages** chaque fois que votre correspondant et vous échangez des messages, vous maintiendrez une voie de communication privée et sécurisée, même si des tierces parties essaient de surveiller vos communications.

