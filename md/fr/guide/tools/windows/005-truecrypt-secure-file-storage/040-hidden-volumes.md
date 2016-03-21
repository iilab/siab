

---

lang: fr
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 4
depth: 3
title: Hidden Volumes

---

Sommaire des sections de cette page:

- [**5.0 À propos des volumes cachés**](#5.0)
- [**5.1 Comment créer un volume caché**](#5.1)
- [**5.2 Comment monter un volume caché**](#5.2)
- [**5.3 Conseils sur l'utilisation sécuritaire de la fonction disque caché**](#5.3)

-------

<a name="5.0"></a>
## 5.0 À propos des volumes cachés ##

Dans **TrueCrypt**, un *volume caché* est placé à l'intérieur de votre *volume standard* chiffré, mais son existence est dissimulée. Même si vous *montez* votre volume standard, il est impossible de trouver un volume caché, ou même d'en prouver l'existence. Dans l'éventualité où l'on vous forcerait à révéler votre mot de passe et l'emplacement de votre volume standard, le contenu de ce dernier serait révélé, mais l'existence du volume caché resterait occultée. 

Imaginez une valise pourvue d'un double fond. Les dossiers de peu d'importance, dont la perte ou la confiscation ne vous dérange pas, sont conservés dans le compartiment normal, mais les dossiers importants et privés sont dissimulés dans le double fond. L'intérêt d'un compartiment secret (surtout s'il est bien conçu) est justement le secret: toute personne hostile ou malveillante n'en perçoit tout simplement pas l'existence. **TrueCrypt** utilise cette technique à votre avantage.

<a name="5.1"></a>
## 5.1 Comment créer un volume caché ##

La création d'un *volume caché* est semblable à celle d'un *volume standard*. Certains panneaux et fenêtres ont exactement la même apparence. 

**Première étape**. **Ouvrez** **TrueCrypt**.

**Deuxième étape**. **Cliquez** sur ![](/sbox/screen/truecrypt-fr/13.png) pour afficher l'*Assistant de création de volume de TrueCrypt*. 

**Troisième étape**. **Cliquez** sur  ![](/sbox/screen/truecrypt-fr/05.png) pour accepter l'option par défaut *Create an encrypted file container*.

**Quatrième étape**. **Cochez** l'option *Volume TrueCrypt caché*, comme suit: 

![](/sbox/screen/truecrypt-fr/37.png)

*Figure 1: L'Assistant de création de volume TruCrypt avec l'option Volume TrueCrypt caché sélectionné*

**Cinquième étape**. **Cliquez** sur ![](/sbox/screen/truecrypt-fr/05.png) pour afficher la fenêtre suivante:

![](/sbox/screen/truecrypt-fr/38.png)

*Figure 2: La fenêtre Mode création de volume*

- *Mode direct*: Cette option vous permet de créer un volume caché dans un *volume standard* existant.

- *Mode normal*: Cette option vous permet de créer un nouveau *volume standard*, à l'intérieur duquel vous incorporerez un *volume caché*.

Pour les fins de cet exercice, **cochez** l'option *Mode direct*.

**Commentaire**: Si vous souhaitez plutôt créer un nouveau *volume standard*, répétez les étapes détaillées à la section [**2.2 Comment créer un volume standard**](/fr/truecrypt_volumestandard#2.2).

**Sixième étape**. **Cochez** l'option *Mode direct*, puis **cliquez** sur ![](/sbox/screen/truecrypt-fr/05.png) pour afficher la fenêtre *Sélectionner un volume TrueCrypt*.

**Commentaire**: Assurez-vous que le *volume standard* est démonté lorsque vous le sélectionnez. 

**Septième étape**. **Cliquez** sur ![](/sbox/screen/truecrypt-fr/17.png) pour afficher la fenêtre suivante:

![](/sbox/screen/truecrypt-fr/29.png)

*Figure 3: La fenêtre Sélectionner un volume TrueCrypt*

**Huitième étape**. **Trouvez** le fichier du volume à l'aide de la fenêtre *Sélectionner un volume TrueCrypt*, tel qu'illustré à *figure 3*. 

**Neuvième étape**. **Cliquez** sur ![](/sbox/screen/truecrypt-fr/30.png) pour revenir à l'*Assistant de création de volume*.

**Dixième étape**. **Cliquez** sur ![](/sbox/screen/truecrypt-fr/33.png) pour afficher la fenêtre *Mot de passe du volume*.

**Onzième étape**. **Saisissez** le mot de passe que vous avez utiliser lors de la création du *volume standard* dans la zone de texte *Mot de passe* pour afficher la fenêtre suivante:

![](/sbox/screen/truecrypt-fr/46.png)

*Figure 4: Le panneau volume caché*

**Douzième étape**. **Cliquez** sur ![](/sbox/screen/truecrypt-fr/05.png) après avoir lu le message pour afficher la fenêtre *Options de chiffrement du volume caché*.

**Commentaire**: Laissez les options de l'*Algorithme de chiffrement* et l'*Algorithme de hachage* du *volume caché * telles quelles.

**Treizième étape**. **Cliquez** sur ![](/sbox/screen/truecrypt-fr/05.png) pour afficher la fenêtre suivante:

![](/sbox/screen/truecrypt-fr/41.png)

*Figure 5: La fenêtre Taille du volume caché*

Il faut maintenant choisir la taille du *volume caché*. 

**Commentaire**: Tenez compte du type de documents, de leur taille ainsi que de la quantité de fichiers à stocker. N'oubliez pas de laisser de l'espace pour le *volume TrueCrypt standard*. Si vous choisissez la taille maximale disponible pour votre *volume caché*, vous ne pourrez plus stocker de fichiers dans le *volume standard* original. 

Si votre *volume standard* est de 10 Mo et que vous indiquez que votre volume caché doit avoir 5 Mo (tel qu'illustré à la *figure 5*, ci-dessus), vous aurez deux volumes (un standard et l'autre caché) d'approximativement 5 Mo chacun.

Dans ce cas, vous devez vous assurer que les données que vous stockerez dans le *volume standard* ne dépassent pas 5 Mo. Le programme **TrueCrypt** ne détecte pas automatiquement l'existence d'un *volume caché* (par mesure de sécurité) et il est donc possible que les données qui s'y trouvent soient écrasées par mégarde. Vous risquez de perdre les données contenues dans le volume caché si vous dépassez la taille que vous aviez fixée. 

**Quatorzième étape**. **Saisissez** la taille que vous souhaitez pour votre *volume caché* dans la zone appropriée de la fenêtre illustrée à la *figure 5*.

**Quinzième étape**. **Cliquez** sur ![](/sbox/screen/truecrypt-fr/05.png) pour afficher la fenêtre *Mot de passe du volume caché*.

Vous devez maintenant choisir pour votre *volume caché* un mot de passe *différent* de celui que vous avez attribué au *volume standard*. N'oubliez pas de choisir un mot de passe fort. Pour plus d'information sur la création de mot de passes forts, voir le Guide pratique [**KeePass**](/fr/keepass_principale). Vous devez absolument choisir un mot de passe différent de celui utilisé pour le volume standard.

**Astuce**: Si vous craignez qu'advienne une situation où vous êtes forcé de révéler le contenu de vos *volumes TrueCrypt*, archivez le mot de passe du *volume standard* dans **KeePass**, puis créez un mot de passe fort que vous mémoriserez pour le *volume caché*. Cela contribuera à protéger davantage le *volume caché*, puisque vous ne laisserez aucune trace de son existence.

**Seizième étape**. **Créez** un mot de passe, **saisissez-le** deux fois, puis **cliquez** sur ![](/sbox/screen/truecrypt-fr/05.png) pour afficher la fenêtre suivante:

![](/sbox/screen/truecrypt-fr/42.png)

*Figure 6: La fenêtre Formatage du volume caché*

Laissez les options *Système* et *Cluster* telles qu'elles. 

**Dix-septième étape**. **Bougez** la souris au dessus de la fenêtre pour accroître la force de chiffrement, puis **cliquez** sur ![](/sbox/screen/truecrypt-fr/25.png) pour formater le *volume caché*.

*Lorsque le formatage du volume caché est complété, vous verrez apparaître une fenêtre semblable à celle-ci:* 

![](/sbox/screen/truecrypt-fr/43.png)

*Figure 7: Fenêtre d'avertissement de l'Assistant de création de volume*

**Commentaire**: La *Figure 7* ci-dessus confirme que vous avez bien créé un *volume caché* et vous rappelle le risque d'écraser des fichiers dans le *volume caché* lorsque vous stockez des fichiers dans le *volume standard* original.

**Dix-huitième étape**. **Cliquez** sur ![](/sbox/screen/truecrypt-fr/27.png) pour afficher la fenêtre *Volume caché créé*, puis **cliquez** sur ![](/sbox/screen/truecrypt-fr/28.png) pour revenir à la console **TrueCrypt**. 

Le *volume caché* a été créé à l'intérieur de votre *volume standard*. Cela vous permet de cacher des documents à l'intérieur de votre *volume standard*. Ceux-ci resteront invisibles, même pour une personne qui a réussi à obtenir le mot de passe de ce *volume standard*. 

<a name="5.2"></a>
## 5.2 Comment monter un volume caché ##

La méthode pour accéder à un *volume caché* est exactement de la même que pour un *volume standard*. La seule différence est que vous devez utiliser le mot de passe du *volume caché* plutôt que celui du *volume standard*. C'est par le mot de passe que **TrueCrypt** détermine s'il doit ouvrir le *volume standard* ou le *volume caché*. 

Pour *monter*, ou ouvrir, le volume caché, suivez les étapes énumérées ci-dessous:

**Première étape**. **Sélectionnez** un lecteur dans la liste (dans cet exemple, le lecteur *K*):

![](/sbox/screen/truecrypt-fr/44.png)

*Figure 8: Un lecteur sélectionné dans la fenêtre des volumes de TrueCrypt*

**Deuxième étape**. **Cliquez** sur ![](/sbox/screen/truecrypt-fr/17.png) pour afficher la fenêtre *Sélectionnez un volume TrueCrypt*. 

**Troisième étape**. **Naviguez** jusqu'à votre fichier de volume **TrueCrypt** (le même fichier que pour votre *volume standard*), puis **sélectionnez-le**. 

**Quatrième étape**. **Cliquez** sur ![](/sbox/screen/truecrypt-fr/30.png) pour revenir à la console **TrueCrypt**.

**Cinquième étape**. **Cliquez** sur ![](/sbox/screen/truecrypt-fr/31.png) pour afficher la fenêtre *Entrez le mot de passe pour...*, tel qu'illustré ci-dessous:

![](/sbox/screen/truecrypt-fr/32.png)

*Figure 9: La fenêtre Entrez le mot de passe pour...*

**Sixième étape**. **Saisissez** e mot de passe que vous avez choisi lors de la création du *volume caché*, puis **cliquez** sur ![](/sbox/screen/truecrypt-fr/33.png). 

Le *volume caché* est maintenant monté (ouvert), tel qu'illustré ci-dessous:

![](/sbox/screen/truecrypt-fr/45.png)

*Figure 10: La fenêtre principale de TrueCrypt affichant le volume caché récemment monté*

**Septième étape**. **Double-cliquez** sur cette entrée ou passer par la fenêtre *Poste de travail*.

<a name="5.3"></a>
## 5.3 Conseils sur l'utilisation sécuritaire de la fonction disque caché ##

Le but de la fonction lecteur caché est de vous soustraire à toute situation potentiellement dangereuse en *laissant l'impression* à un adversaire que vous lui donnez ce qu'il veut - l'accès à vos fichiers - sans pour autant compromettre la sécurité de vos données. En plus de protéger vos données, cela vous permet d'éviter de vous mettre davantage en danger ou d'exposer vos collègues et partenaires. Pour que cette technique soit efficace, vous devez créer une situation où votre adversaire sera satisfait des résultats de sa recherche et cessera de vous importuner. 

Pour que cela soit efficace, vous devriez suivre ces quelques indications: 

- Placez vos documents semi-sensibles, ceux dont la perte vous dérange moins, dans le *volume standard*. Ces documents doivent tout de même être assez "intéressants" pour capter l'attention de votre adversaire lorsque vous serez forcé de les lui montrer. 

- Gardez à l'esprit que votre adversaire est peut être conscient de la possibilité de créer des *volumes cachés* avec **TrueCrypt**. Cela dit, si vous utilisez **TrueCrypt** correctement, cette personne ne sera pas en mesure de prouver l'existence d'un volume caché, ce qui rendra votre démenti plus crédible.

- Actualisez régulièrement (une fois par semaine) les fichiers placés dans le *volume standard*. Cela donnera l'impression que vous utilisez réellement ces fichiers. 

Lorsque vous montez un volume **TrueCrypt**, il vous est toujours possible d'activer la fonction *Empêcher les dommages causés en écrivant dans le volume externe*. C'est une option extrêmement importante qui vous permet d'ajouter des fichiers de "diversion" à votre *volume standard* sans devoir vous inquiéter de supprimer ou d'écraser le contenu chiffré de votre *volume caché*. 

Comme nous l'avons déjà vu, il existe un risque que vous écrasiez vos fichiers cachés lorsque vous dépassez la limite d'espace que vous avez déterminée pour votre *volume standard*. Vous ne devriez jamais activer l'option *Protection du volume caché* lorsque vous êtes forcé par quelqu'un de monter un volume **TrueCrypt**, parce que vous seriez alors obligé de saisir le mot de passe secret de votre *volume caché* et cela révélerait automatiquement l'existence dudit volume. Lorsque vous actualisez vos fichiers de "diversion" en privé, par contre, vous devriez *toujours* activer cette option.

Pour utiliser l'option *Protection du volume caché*, suivez les étapes énumérées ci-dessous.

**Première étape**. **Cliquez** sur ![](/sbox/screen/truecrypt-fr/47.png) de la fenêtre *Entrez le mot de passe pour...* illustrée à la *figure 9*, ci-dessus, pour afficher la fenêtre *Options de montage*, illustrée ci-dessous:

![](/sbox/screen/truecrypt-fr/48.png)

*Figure 11: La fenêtre Options de montage*

**Deuxième étape**. **Cochez** l'option *Empêcher les dommages causés en écrivant dans le volume externe*.

**Troisième étape**. **Saisissez** le mot de passe de votre *volume caché*, puis **cliquez** sur ![](/sbox/screen/truecrypt-fr/33.png).

**Quatrième étape**. **Cliquez** sur ![](/sbox/screen/truecrypt-fr/31.png) pour monter votre *volume standard*. Lorsque celui-ci sera monté, vous serez en mesure d'ajouter des fichiers de "diversion" sans endommager les fichiers stockés dans votre *volume caché*.

**Cinquième étape**. **Cliquez** sur ![](/sbox/screen/truecrypt-fr/51.png) pour démonter votre *volume standard* quand vous avez fini d'en actualiser le contenu.

**N'oubliez pas**: Vous ne devez effectuer cette opération que lorsque vous actualisez les fichiers qui se trouvent dans votre *volume standard*. Lorsque vous révélez l'existence de votre volume standard à quelqu'un, vous ne devriez pas utiliser la fonction *Protection du volume caché*.

