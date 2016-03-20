

---

lang: fr
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 009
title: CCleaner - Secure File Deletion and Work Session Wiping

---

**Site Internet**

[**www.ccleaner.com**](http://www.ccleaner.com)
 
**Configuration requise**

- Compatible avec toutes les versions de Windows 

**Version utilisée pour rédiger ce guide**

- 4.03

**Licence**

- Gratuiciel

**Lecture préalable**

**Livret pratique** Security-in-a-Box, chapitre [6. Détruire définitivement des données sensibles](/fr/chapter-6)

**Niveau**: 1: Débutant, **2: Moyen**, 3: Intermédiaire, 4: Expérimenté, 5: Avancé

**Temps d'apprentissage**: 15 minutes

**Ce que vous apportera l’utilisation de cet outil**:

- La capacité de supprimer définitivement toutes traces de vos activités et des fichiers temporaires stockés sur votre ordinateur.
- La capacité de **nettoyer l'espace libre des disques** connectés à votre ordinateur
- La capacité de nettoyer le **Registre de Windows**
- La capacité de **déterminer quels programmes sont activés au démarrage de votre ordinateur**

**Autres programmes compatibles avec GNU Linux, Mac OS et/ou Microsoft Windows**:

[**BleachBit**](http://bleachbit.sourceforge.net/) est un autre excellent outil de suppression et de destruction de fichiers temporaires, compatible avec **GNU Linux** et **Microsoft Windows**. **BleachBit** vous permet de supprimer les fichiers temporaires générés par 70 des applications les plus répandues et par le système d'exploitation, et de libérer de l'espace sur vos disques durs. Un programme de code source libre proposant une version portable, **BleachBit** est disponible en 32 langues. Les utilisateurs de **Ubuntu Linux** peuvent en outre se référer au guide [Nettoyer Ubuntu…](http://doc.ubuntu-fr.org/nettoyer_ubuntu) pour apprendre à nettoyer leur système.

Les utilisateurs de **Mac OS** apprécieront sûrement les outils gratuits proposés par [Titanium’s Software: **OnyX** et **Maintenance**](http://www.titanium.free.fr/) pour supprimer les traces de vos séances de travail. Pour effacer de façon sécuritaire le contenu de votre *Trash*, ouvrez l'application *Finder* et sélectionnez le menu *Finder > Secure Empty Trash*. Vous pouvez choisir de toujours supprimer le contenu de votre *Trash* de façon sécuritaire en ouvrant les préférences *Avancées* du Finder et en cochant l'option *Empty Trash securely*. Pour nettoyer l'espace libre de votre disque dur, lancez l'application système *Disk Utility*, sélectionnez la partition voulue, sélectionnez l'onglet *Erase* et cliquez sur le bouton *Erase Free Space.* 


### 1.1 À propos de cet outil ###

Les paramètres par défaut de votre système et de votre navigateur Web génèrent automatiquement une trace de vos données dont un tiers parti hostile ou malveillant pourrait tirer avantage, un peu comme un chasseur traquant sa proie. Chaque fois que vous utilisez un navigateur ou un logiciel de traitement de texte, ou tout autre programme, des fichiers et données temporaires sont générés et stockés quelque part sur votre ordinateur. Ces programme génèrent également des listes de documents ou pages Internet récemment consultés. Par exemple, chaque fois que vous saisissez une adresse Internet dans votre navigateur préféré, une liste des adresses qui commencent avec les mêmes caractères s'affichent automatiquement, comme ceci: 

![](/sbox/screen/ccleaner-fr/16.png)

*Figure 1: Une barre d'adresse de navigateur affichant différentes URLs*

Bien que les historiques des navigateurs puissent êtres utiles à l'occasion, elle peuvent aussi permettre à un tiers parti d'identifier les sites Internet que vous avez visités. De plus, vos activités récentes peuvent être exposées par les données temporaires sauvegardées à partir des images comprises dans ces sites Internet, y compris les messages de courrier électronique et les coordonnées saisies dans des formulaires.

Pour supprimer les données temporaires générées chaque fois que vous utilisez un programme, il vous faudrait ouvrir chaque répertoire de chaque programme, identifier et supprimer manuellement chaque fichier temporaire. **CCleaner affiche une liste de programmes et vous laisse choisir le ou les programme(s) dont vous souhaitez supprimer les fichiers temporaires.

**Important**: Même si **CCleaner** ne supprime que les fichiers temporaires, et non pas les documents sauvegardés sur votre ordinateur, il est **fortement recommandé** que vous conserviez une sauvegarde mise à jour de vos documents (veuillez consulter le **Livret pratique** Security-in-a-Box, chapitre [**5. Récupérer des données perdues**](/fr/chapter-5) pour plus de conseils sur la création de copies de sauvegarde). 

Après avoir lancé **CCleaner**, il est possible que vous ayez perdu les historiques de votre navigateur et de vos documents récents, ainsi que vos mots de passe sauvegardés. C'est précisément la fonction de cet outil, c'est-à-dire de minimiser les différentes façons par lesquelles des tiers partis malveillants pourraient infecter ou espionner votre système.

