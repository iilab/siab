

---

lang: fr
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: How to Install TrueCrypt and Create Standard Volumes

---

Sommaire des sections de cette page: 

- [**2.0 Comment installer TrueCrypt**](#2.0)
- [**2.1 À propos de TrueCrypt**](#2.1)
- [**2.2 Comment créer un volume standard**](#2.2)
- [**2.3 Comment créer un volume standard sur une clé USB**](#2.3)
- [**2.4 Comment créer un volume standard (suite)**](#2.4)

-------

<a name="2.0"></a>
## 2.0 Comment installer TrueCrypt ##

**Première étape**. **Double-cliquez** ![](/sbox/screen/truecrypt-fr/01.png); si la boîte de dialogue *Fichier ouvert - Avertissement de sécurité* s'affiche, **cliquez** sur ![](/sbox/screen/truecrypt-en/02.png) pour afficher la fenêtre  **TrueCrypt** *License*.

**Deuxième étape**. **Cochez** l'option *I accept and agree to be bound by the license terms* pour activer le bouton *Accept*; **cliquez** sur ![](/sbox/screen/truecrypt-fr/03.png) pour afficher la fenêtre suivante:

![](/sbox/screen/truecrypt-fr/04.png)

*Figure 1: Le Mode assistant en mode d'installation par défaut*

- Le mode *Installer*: Cette option est pour les utilisateurs qui ne souhaitent pas cacher le fait qu'ils utilisent **TrueCrypt** sur leur ordinateur.

- Le mode *Extraire*: Cette option est pour les utilisateurs qui souhaitent transporter une version portable de **TrueCrypt** sur une clé USB et qui ne souhaitent pas installer **TrueCrypt** sur leur ordinateur.

**Commentaire**: Certaines options (par exemple, le chiffrement de partitions entières et de disques entiers) ne fonctionneront pas si **TrueCrypt** est extrait mais non installé.

**Commentaire**: Même si le mode *Installer* par défaut est recommandé ici, vous voudrez peut-être utiliser la version portable de **TrueCrypt** ultérieurement. Pour en savoir plus sur le mode **TrueCrypt Traveller**, veuillez consulter le chapitre [**TrueCrypt mode Traveler**](http://securityinabox.org/fr/truecrypt_portable). 

**Troisième étape**. **Cliquez** sur ![](/sbox/screen/truecrypt-fr/05.png) pour afficher la fenêtre suivante:

![](/sbox/screen/truecrypt-fr/06.png)

*Figure 2: La fenêtre Options d'installation*

**Quatrième étape**. **Cliquez** sur ![](/sbox/screen/truecrypt-fr/07.png) pour afficher la fenêtre  *Installation en cours* et lancer l'installation de **TrueCrypt** sur votre système.

**Cinquième étape**. **Cliquez** sur ![](/sbox/screen/truecrypt-fr/08.png) pour afficher la fenêtre suivante:

![](/sbox/screen/truecrypt-fr/09.png)

*Figure 3: La boîte de dialogue de confirmation de l'installation de TrueCrypt*

**Sixième étape**. **Cliquez** sur ![](/sbox/screen/truecrypt-fr/10.png) pour ouvrir le site Internet de **TrueCrypt** et finaliser l'installation de *TrueCrypt**, puis **cliquez** sur ![](/sbox/screen/truecrypt-fr/11.png).

**Commentaire**: Il est recommandé à tous les utilisateurs de consulter la documentation d'aide fournie par **TrueCrypt**. 

<a name="2.1"></a>
## 2.1 À propos de TrueCrypt ##

**TrueCrypt** est conçu pour sécuriser vos fichiers en bloquant l’accès à quiconque ne dispose pas du mot de passe nécessaire. Le logiciel fonctionne un peu comme un "coffre-fort" électronique en vous permettant de verrouiller vos fichiers de telle sorte que seule une personne disposant du bon mot de passe puisse y accéder. **TrueCrypt** vous permet de créer des *volumes*, ou des sections de votre ordinateur où vous pouvez stocker des fichiers de façon sécurisée. Lorsque vous créez des données dans ces volumes, ou lorsque vous y transférez des données, TrueCrypt chiffre automatiquement cette information. Lorsque vous ouvrez ou déplacez ces fichiers, le programme les déchiffre automatiquement. Ce processus s’appelle chiffrage/déchiffrage *à la volée*. 

<a name="2.2"></a>
## 2.2 Comment créer un volume standard ##

**TrueCrypt** vous donne le choix de créer deux types de volumes: *caché* et *standard*. Dans cette section section, nous verrons comment créer un *volume standard* pour y stocker vos fichiers.

Pour commencer à utiliser **TrueCrypt** en créant un *volume standard*, suivez les étapes énumérées ci-dessous: 

**Première étape**. **Double-cliquez** ![](/sbox/screen/truecrypt-fr/52.png) ou **Sélectionnez Démarrer > Programmes > TrueCrypt > TrueCrypt** pour ouvrir **TrueCrypt**.

**Deuxième étape**. **Sélectionnez** un lecteur dans la liste du panneau principal **TrueCrypt** illustré ci-dessous:

![](/sbox/screen/truecrypt-fr/12.png)

*Figure 4: La console TrueCrypt*

**Troisième étape**. **Cliquez** sur ![](/sbox/screen/truecrypt-fr/13.png) pour activer l’*Assistant de création de volume TrueCrypt*, illustré ci-dessous:

![](/sbox/screen/truecrypt-fr/14.png)

*Figure 5: L’Assistant de création de volume TrueCrypt* 

La *figure 5* vous présente trois options pour créer un *volume standard*. Dans ce chapitre, nous aborderons la *Création d'un conteneur chiffré* (*Create an encrypted file container*). Veuillez consulter la documentation de [**TrueCrypt**](http://www.truecrypt.org/docs/) pour obtenir les descriptions des deux autres options.

**Quatrième étape**. **Cliquez** sur ![](/sbox/screen/truecrypt-fr/05.png) pour afficher la fenêtre suivante:

![](/sbox/screen/truecrypt-fr/15.png)

*Figure 6: La fenêtre Type de volume*

La fenêtre  *Assistant de création de volume TrueCrypt - Type de volume* offre le choix entre un *volume standard* et un *volume caché*. 

**Important**: Voir la section [**Volumes cachés**](/fr/truecrypt_volumescaches) du présent guide pour plus d'information sur la création d'un *volume caché*.

**Cinquième étape**. **Cochez** l'option *Volume TrueCrypt Standard*.

**Sixième étape**. **Cliquez** sur ![](/sbox/screen/truecrypt-fr/05.png) pour afficher la fenêtre suivante:

![](/sbox/screen/truecrypt-fr/16.png)

*Figure 7: L’Assistant de création de volume TrueCrypt affichant le panneau Emplacement du volume*

Vous pouvez déterminer où vous aimeriez stocker votre *volume standard* dans la fenêtre de l’*Assistant de création de volume - Emplacement du volume*. Ce fichier peut être stocké comme n’importe quel autre type de fichier

**Septième étape**. **Saisissez** le nom du fichier dans la zone de texte ou **cliquez** sur ![](/sbox/screen/truecrypt-fr/17.png) pour afficher la fenêtre suivante:

![](/sbox/screen/truecrypt-fr/18.png)

*Figure 8: La fenêtre Spécifier le nom et l’emplacement*

**Commentaire**: Un volume **TrueCrypt** est contenu à l’intérieur d’un fichier normal. Cela signifie qu’il peut être déplacé, copié et même supprimé! Il est donc très important de se rappeler le nom et l'emplacement du fichier. Cependant, vous devez choisir un nouveau nom de fichier pour le volume que vous créez (veuillez également consulter la section [2.3 Comment créer un volume standard sur une clé USB](#2.3)). Pour les fins de cet exercice, nous créerons notre *volume standard* dans le répertoire *Mes documents*, et nous nommerons le fichier *Mon volume* (voir Figure 8, ci-dessus).

**Astuce**: Vous pouvez utiliser n’importe quel nom de fichier et type d’extension. Par exemple, vous pouvez nommer votre volume standard *recettes.doc* pour lui donner l'apparence d'un document *Word*, ou *vacances.mpeg* pour lui donner l'apparence d'un d’un fichier vidéo. C'est un moyen par lequel vous pouvez dissimuler l’existence d’un volume standard. 

**Huitième étape**. **Cliquez** sur ![](/sbox/screen/truecrypt-en/19.png) pour fermer la fenêtre *Spécifier le nom et l’emplacement* et revenir à l’*Assistant de création de volume*:

![](/sbox/screen/truecrypt-fr/20.png)

*Figure 9: L’Assistant de création de volume de TrueCrypt affichant le panneau Emplacement du volume*

**Neuvième étape**. **Cliquez** sur ![](/sbox/screen/truecrypt-fr/05.png) pour afficher la *figure 10*. 

<a name="2.3"></a>
## 2.3 Comment créer un volume standard sur une clé USB ##

Pour créer un volume **TrueCrypt** standard sur une clé USB, suivez les étapes 1 à 3 décrites à la section [2.2 Comment créer un volume standard](#2.2) afin d'activer la fenêtre *Type de volume*. Au lieu de choisir *Mes documents* comme emplacement, **naviguez** jusqu’à votre clé USB. **Nommez** ensuite votre fichier et **créez** votre *volume standard* à cet emplacement. 

<a name="2.4"></a>
## 2.4  Comment créer un volume standard (suite) ##

À ce point, il faut déterminer une méthode de chiffrement spécifique (ou *algorithme* selon le vocabulaire du logiciel) pour encoder les données qui seront stockées dans le *volume standard*. 

![](/sbox/screen/truecrypt-fr/21.png)

*Figure 10: Le panneau Options de chiffrement*

**Commentaire**: Vous pouvez laisser les options par défaut telles quelles. Tous les algorithmes présentés dans les deux options sont considérés sûrs. 

**Dixième étape**. **Cliquez** sur ![](/sbox/screen/truecrypt-fr/05.png) pour afficher la fenêtre *Taille du volume* de l'*Assistant de création de volume TrueCrypt*:

![](/sbox/screen/truecrypt-fr/22.png)

*Figure 11: La fenêtre Taille du volume*

La fenêtre *Taille du volume* vous permet de préciser la taille du *volume standard*. Dans cet exemple, le volume est réglé à 10 Mo. Vous pouvez toutefois déterminer la taille qui vous convient. Prenez en considération les documents et les types de fichiers que vous voudrez stocker, ainsi que leur poids, et déterminez ensuite une taille de volume appropriée. 

**Astuce**: Si vous avez l’intention de créer une copie de sauvegarde de votre *volume standard* sur un CD, vous devriez régler votre volume à 700 Mo. 

**Onzième étape**. **Saisissez** la taille de volume souhaitée dans la zone de texte, puis **cliquez** sur ![](/sbox/screen/truecrypt-fr/05.png) pour afficher la fenêtre suivante:

![](/sbox/screen/truecrypt-fr/23.png)

*Figure 12: La fenêtre Mot de passe du volume *

**Important**: Le choix d’un mot de passe fort et sécuritaire est l’une des tâches les plus importantes à accomplir lors du processus de création d’un *volume standard*. Un bon mot de passe protégera efficacement un volume chiffré: plus votre mot de passe est fort, mieux votre volume sera protégé. Vous n’êtes pas obligé de créer vos propres mots de passe, ou même de vous en rappeler, si vous utilisez un programme de génération automatique de mots de passe comme **KeePass**. Veuillez consulter le Guide pratique [**KeePass**](/fr/keepass_principale) pour obtenir des renseignements sur la création et le stockage de mots de passe. 

**Douzième étape**. **Saisissez** votre mot de passe, puis **saisissez-le** à nouveau dans les zones de texte *Mot de passe* et *Confirmer*.

**Important**: Le bouton *Suivant* demeurera désactivé tant et aussi longtemps que les mots de passe saisis dans les deux zones de texte ne correspondront pas. Si le mot de passe que vous avez choisi n’est pas particulièrement sûr, un message d’avertissement apparaîtra. Il est conseillé, dans ce cas, de changer de mot de passe! Cela dit, **TrueCrypt** fonctionnera tout de même avec le mot de passe que vous avez choisi, même si vos données ne seront pas particulièrement bien sécurisée. 

**Treizième étape**. **Cliquez** sur ![](/sbox/screen/truecrypt-fr/05.png) pour afficher la fenêtre suivante:

![](/sbox/screen/truecrypt-fr/24.png)

*Figure 13: La fenêtre Formatage du volume*

**TrueCrypt** est maintenant prêt à créer un volume standard. Bougez votre souris aléatoirement au dessus de la fenêtre de l’*Assistant de création de volume TrueCrypt* pendant au moins 30 secondes. Plus vous bougez votre souris longtemps, meilleure sera la qualité de la clé de chiffrement.

**Quatorzième étape**. **Cliquez** sur ![](/sbox/screen/truecrypt-fr/25.png) pour poursuivre la création de votre *volume standard*.

**TrueCrypt** créera un fichier nommé *Mon volume* dans le répertoire *Mes documents*, tel que spécifié plus tôt. Ce fichier contiendra un *volume TrueCrypt standard*, d’une taille de 10 Mo, que vous pourrez utiliser pour stocker vos fichiers de façon sécurisée. 

Quand la création du *volume standard* sera achevée, cette boîte de dialogue apparaîtra : : 

![](/sbox/screen/truecrypt-fr/26.png)

*Figure 14: La boîte de dialogue Le volume TrueCrypt a été créé avec succès*

**Quinzième étape**. **Cliquez** sur ![](/sbox/screen/truecrypt-fr/27.png) pour finaliser la création du *volume standard* et revenir à la console **TrueCrypt**.

**Seizième étape**. **Cliquez** sur ![](/sbox/screen/truecrypt-fr/28.png) pour fermer l'*Assistant de création de volume TrueCrypt*.

