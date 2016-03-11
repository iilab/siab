

---

lang: fr
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Mount the Standard Volume

---

Sommaire des sections de cette page:

- [**3.0 Comment monter un volume standard**](#3.0)
- [**3.1 Comment démonter un volume standard**](#3.1)

-------

<a name="3.0"></a>
## 3.0 Comment monter un volume standard ##

Dans **TrueCrypt**, *monter un volume* désigne le processus par lequel le volume est rendu accessible et prêt à l’utilisation. Dans cette section, vous apprendrez à *monter* le *volume standard* que vous venez de créer.

Pour entamer le montage du volume standard, suivez les étapes énumérées ci-dessous : 

**Première étape**. **Double-cliquez** sur ![](/sbox/screen/truecrypt-fr/52.png) ou **Sélectionnez Démarrer > Programmes > TrueCrypt > TrueCrypt** pour ouvrir **TrueCrypt**.

**Deuxième étape**. **Sélectionnez** un lecteur dans la liste, comme suit : 

![](/sbox/screen/truecrypt-fr/200.png)

*Figure 1: La console TrueCrypt*

*Dans cet exemple, le volume standard sera monté sur le lecteur M.*

**Commentaire**: Dans la *figure 1*, le lecteur 'M' est sélectionné pour le montage du *volume standard*, mais vous pouvez choisir n’importe quel lecteur.

**Troisième étape**. **Cliquez** sur![](/sbox/screen/truecrypt-fr/17.png)

*La fenêtre Sélectionner un volume TrueCrypt apparaîtra:*

![](/sbox/screen/truecrypt-fr/29.png)

*Figure 2: La fenêtre Sélectionner un volume TrueCrypt*

**Quatrième étape**. **Sélectionnez** le fichier du *volume standard* que vous avez créé, puis **cliquez** sur ![](/sbox/screen/truecrypt-fr/30.png) pour fermer la *figure 2* et revenir à la console **TrueCrypt**.

**Cinquième étape**. **Cliquez** sur ![](/sbox/screen/truecrypt-fr/31.png) pour activer la fenêtre *Entrez le mot de passe pour...*, illustrée ci-dessous: 

![](/sbox/screen/truecrypt-fr/32.png)

*Figure 3: La fenêtre Entrez le mot de passe pour...*

**Sixième étape**. **Saisissez** le mot de passe dans la zone de texte *Mot de passe:*.

**Septième étape**. **Cliquez** sur ![](/sbox/screen/truecrypt-fr/33.png) pour monter le *volume standard*.

**Commentaire**: Si le mot de passe que vous avez saisi est incorrect, **TrueCrypt** vous en avisera et vous devrez saisir le mot de passe de nouveau, puis **cliquer** sur ![](/sbox/screen/truecrypt-fr/33.png). i cette fois-ci le mot de passe est correct, le volume standard sera monté:

![](/sbox/screen/truecrypt-fr/34.png)

*Figure 4: La console TrueCrypt affichant le volume standard nouvellement monté*

**Huitième étape**. **Double-cliquez** sélection surlignée dans la liste **TrueCrypt** ou **double-cliquez** la lettre du disque correspondant dans la fenêtre *Poste de travail* pour accéder directement au *volume standard* maintenant monté sur le lecteur 'M:'.

![](/sbox/screen/truecrypt-fr/35.png)

*Figure 5: Accéder au volume standard via la fenêtre Poste de travail*

**Commentaire**: Nous venons de monter le volume standard *Mon volume* en tant que lecteur virtuel *M:*. Ce lecteur virtuel a tous les attributs d’un vrai lecteur, sauf qu’il est complètement chiffré. Tous les fichiers copiés, déplacés ou sauvegardés dans ce disque virtuel seront automatiquement chiffrés (un processus appelé chiffrage à la volée).

Vous pouvez copier des fichiers dans le *volume standard*, exactement de la même façon qu’avec un lecteur normal (par exemple en le glissant depuis un autre répertoire). Lorsque vous déplacez un fichier depuis le *volume standard* vers un autre emplacement, celui-ci est automatiquement déchiffré. De la même façon, lorsque vous déplacez un fichier vers le *volume standard*, celui-ci est automatiquement chiffré. Lorsque votre ordinateur plante, ou s’il est soudainement éteint, **TrueCrypt** ferme automatiquement le *volume standard*. 

**Important**: Après avoir transférer des fichiers dans le volume **TrueCrypt**, assurez-vous de ne laisser aucune trace de ces fichiers ailleurs sur l'ordinateur ou la clé USB dont ils proviennent. Veuillez consulter le chapitre [**6. Détruire définitivement des données sensibles**](/fr/chapter-6) du livret pratique.

<a name="3.1"></a>
## 3.1 Comment démonter un volume standard ##

Dans **TrueCrypt*, le terme *démonter* désigne simplement le processus par lequel le volume est rendu inaccessible. 

Pour fermer, ou démonter, un *volume standard* et faire en sorte que les fichiers qui s’y trouvent ne soient accessibles qu’aux personnes disposant du bon mot de passe, suivez les étapes énumérées ci-dessous : 

**Première étape**. **Sélectionnez** le volume voulu dans la liste des volumes montés de la fenêtre principale de **TrueCrypt**:

![](/sbox/screen/truecrypt-fr/34.png)

*Figure 17: Sélectionner le volume standard à démonter*

**Deuxième étape**. **Cliquez** sur ![](/sbox/screen/truecrypt-fr/49.png) pour démonter, ou fermer, le *volume standard* **TrueCrypt**. 

**Important**: Assurez-vous de démonter votre volume **TrueCrypt** avant de mettre l'ordinateur en *veille* ou en *veille prolongée*. En fait, il est plutôt conseillé d'éteindre le système complètement si vous avez l'intention de vous en éloigner. Cela empêchera tout intrus éventuel d'accéder au mot de passe de votre volume.

Pour récupérer les fichiers stockés dans votre volume standard, vous devrez monter le volume de nouveau.

