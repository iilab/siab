

---

lang: fr
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Use Spybot in Advanced Mode

---

- [**3.0 À propos du mode avancé**](#3.0)
- [**3.1 Comment activer le mode avancé**](#3.1)
- [**3.2 Comment utiliser les outils du mode avancé**](#3.2)

-------

<a name="3.0"></a>
## 3.0 À propos du mode avancé* ##

**Spybot** fonctionne en mode *par défaut* et en mode *avancé*. Le mode *avancé* vous permet d’accéder aux paramètres du programme, ainsi qu’à des outils supplémentaires. 

<a name="3.1"></a>
## 3.1 Comment activer le mode avancé ## 

Pour activer le mode *avancé* de **Spybot**, suivez les étapes énumérées ci-dessous:
 
**Première étape**. **Sélectionnez Mode > Mode avancé** dans la barre menu: 

![](/sbox/screen/spybot-fr/51.png)

*Figure 1: Les options du sous-menu Mode*

*Cette action activera la fenêtre suivante*:

![](/sbox/screen/spybot-fr/52.png)

*Figure 2: La fenêtre d'invite Avertissement*

**Deuxième étape**. **Cliquez** sur ![](/sbox/screen/spybot-fr/49.png) pour confirmer le choix du mode *avancé*. 

Dans le mode *avancé* , le menu latéral de **Spybot** comporte plus d’options que sous le mode par défaut: 

![](/sbox/screen/spybot-fr/53.png)

*Figure 3: Le menu latéral du mode avancé de Spybot - Search & Destroy*

**Troisième étape**. **Double-cliquez** sur *Réglages* pour afficher les descriptions de divers éléments et options dans le panneau principal: 

![](/sbox/screen/spybot-fr/54.png)

*Figure 4: La fenêtre réglages*

**Quatrième étape**. **Double-cliquez** sur *outils* pour afficher les outils qui vous permettront d’identifier des mouchards que le processus de vérification normal ne suffit pas à détecter, et à refaire la vérification du système.

![](/sbox/screen/spybot-fr/55.png)

*Figure 5: La fenêtre  outils*

**Cinquième étape**. **Double-cliquez** sur *Info & Licence* pour afficher les renseignements généraux et l’information portant sur la licence d’utilisation de **Spybot 1.6.2**. 

<a name="3.2"></a>
## 3.2 Comment utiliser les outils du mode avancé ##

Les utilisateurs **avancés** apprécieront les options avancées offertes par **Spybot**: *Ajustements IE* , *Effaceur de sécurité*, *Intérieur du système* et *Démarrage système*. 

### 3.2.1 Ajustements IE ###

L’option *Ajustements IE* sert à la configuration d’**Internet Explorer**. Cela vous permet de configurer certains paramètres de sécurité importants d’IE, en particulier lorsque plusieurs utilisateurs se servent d'un même système. 

![](/sbox/screen/spybot-fr/56.png)

*Figure 6: La fenêtre Ajustements IE* 

Vous devriez toujours laisser la première option cochée, tel qu’illustré dans l’exemple ci-dessus.

### 3.2.2 Effaceur de sécurité  ###

Voici une option très pratique pour supprimer définitivement (effacer) des fichiers temporaires de **Windows** et du navigateur Internet. Pour plus d’information sur la suppression définitive de fichiers temporaires, consultez le chapitre [**6. Détruire définitivement des données sensibles**](/fr/chapter-6) du livret pratique Security in-a-Box. 

**Première étape**. **Cliquez** sur ![](/sbox/screen/spybot-fr/57.png) pour afficher la fenêtre suivante:

![](/sbox/screen/spybot-fr/58.png)

*Figure 7: La fenêtre de l'Effaceur de sécurité de Spybot-S&D*

**Deuxième étape**. **Cliquez** sur *Templates* pour activer un menu défilant des emplacements où se trouvent des fichiers temporaires, tel qu'illustré à la *figure 7*, puis **sélectionnez** un item dans la liste pour remplir la fenêtre de l'*Effaceur de sécurité de Spybot-S&D*:

![](/sbox/screen/spybot-fr/59.png)

*Figure 8: La liste des fichiers temporaires dans la fenêtre de l'Effaceur de sécurité*

**Troisième étape**. **Sélectionnez** un ou des fichier(s) à supprimer.

**Quatrième étape*. **Déterminer** le nombre de passages utilisés pour effacer le(s) fichier(s) sélectionné(s):

![](/sbox/screen/spybot-fr/60.png)

*Figure 9: Choisissez le nombre de passages désiré*

**Cin quième étape**. **Cliquez** sur ![](/sbox/screen/spybot-fr/61.png) après avoir déterminé le nombre de passages que comptera la processus de suppression

***Spybot** supprimera définitivement de votre ordinateur tous les fichiers temporaires non nécessaires.*

Vous pouvez également utiliser l'*Effaceur de sécurité* pour supprimer et effacer d'autres fichiers. Pour ce faire, suivez les étapes énumérées ci-dessous: 

**Première étape**. **Sélectionnez > Add file(s) to the list...** pour afficher la fenêtre suivante:

![](/sbox/screen/spybot-fr/65.png)

*Figure 10: La fenêtre de navigateur Select File(s) to shred*

**Deuxième étape**. **Sélectionnez** le fichier que vous souhaitez effacer.

**Troisième étape**. **Cliquez** sur ![](/sbox/screen/spybot-fr/66.png) pour afficher le fichier dans la *figure 8*, puis **cliquez** ![] sur (/sbox/screen/spybot-fr/61.png) pour supprimer et effacer le fichier.

### 3.2.3 Intérieur du système (Pour utilisateurs avancés seulement!)  ###

L’outil *Intérieur du système* cherchera des fichiers incorrectement nommés ou dotés de noms incohérents dans le **Registre Windows**. L’explication détaillée du registre de Windows est donnée dans le Guide pratique  [**CCleaner**](//securityinabox.org/fr/ccleaner_registredewindows#4.0). 

![](/sbox/screen/spybot-fr/62.png)

*Figure 11: La fenêtre Intérieur du système*

**Première étape**. **Cliquez** sur ![](/sbox/screen/spybot-fr/63.png) pour entamer la recherche de problèmes dans le **Registre Windows**.

**Deuxième étape**. Lorsque la vérification est terminée, **cliquez** sur ![](/sbox/screen/spybot-fr/41.png) pour corriger tous les problèmes trouvés.

### 3.2.4 Démarrage système (Pour utilisateurs avancés seulement!) ###

L’outil *Démarrage système* affiche, en ordre séquentiel, tous les programmes chargés par **Windows** au démarrage de l’ordinateur. Il vous laisse départager ceux qui sont nécessaires de ceux qui ne sont pas essentiels au démarrage. 

**Astuce**: Le retrait de certains éléments de cette liste augmente la vitesse à laquelle **Windows** démarre.

![](/sbox/screen/spybot-fr/64.png)

*Figure 12: La fenêtre de l’outil Démarrage système*

**Première étape**. **Cliquez** sur ![](/sbox/screen/spybot-fr/39.png) pour afficher le panneau d'information.

Dans ce panneau d’information, chaque élément surligné comporte une description de son comportement et de sa fonction. Lisez attentivement ces descriptions avant de décider si oui ou non un élément doit être chargé au démarrage de **Windows**.

