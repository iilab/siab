

---

lang: fr
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 005
title: TrueCrypt - Secure File Storage

---

**Site Internet**

[**www.truecrypt.org**](http://www.truecrypt.org/)

**Configuration requise**

- Windows 2000/XP/2003/Vista/7
- Les droits d’administration sont nécessaires pour installer le logiciel et créer des volumes chiffrés, mais pas pour accéder aux volumes existants. 

**Version utilisée pour rédiger ce guide**

- 7.0a

**Licence**

- FLOSS (Free/Libre & Open Source Software)

**Lecture préalable**

- Livret pratique Security in-a-box, chapitre [**4. Protéger les données sensibles stockées sur votre ordinateur**](/fr/chapter-4)
	
**Niveau** 

- (Volumes Standards): 1 : Débutant, 2 : Moyen, **3 : Intermédiaire**, 4 : Expérimenté, 5 : Avancé 
- (Volumes cachés): 1 : Débutant, 2 : Moyen, 3 : Intermédiaire, **4 : Expérimenté**, 5 : Avancé 

**Temps d’apprentissage**: 

- (Volumes Standards): 30 minutes 
- (Volumes cachés): 30 minutes 

**Ce que vous apportera l'utilisation de cet outil **: 

- La capacité de protéger efficacement vos fichiers de toute intrusion et de tout accès non autorisé.
- La capacité de stocker facilement des copies de sauvegarde de vos fichiers importants, et ce, de façon sécurisée.

**Autres programmes compatibles avec GNU Linux, Mac OS et/ou Microsoft Windows:**

**Commentaire**: Nous recommandons fortement **TrueCrypt** pour **GNU Linux** et **Mac OS**. 

Plusieurs distributions de **GNU Linux**, par exemple [**Ubuntu**](http://www.ubuntu.com/), supportent le chiffrement/déchiffrement à la volée du disque au complet. Vous pouvez choisir d'utiliser cette fonction standard à l'installation du système. Vous pouvez également ajouter la fonction de chiffrement à votre système **Linux** en utilisant l'intégration de [**dm-crypt**](http://www.saout.de/misc/dm-crypt/) et [**cryptsetup et LUKS**](http://code.google.com/p/cryptsetup/). Une autre approche consiste à utiliser  [**ScramDisk pour Linux SD4L**](http://sd4l.sourceforge.net/), un programme gratuit et de source libre de chiffrement/déchiffrement à la volée.

Pour **Mac OS**, vous pouvez utiliser **FileVault**, qui est intégré au système d'exploitation, pour chiffrer et déchiffrer à la volée le contenu de votre répertoire *Home* et tous ses dossiers. On trouve également un programme gratuit et de source libre [**Encrypt This**](http://www.nathansheldon.com/files/). Ce programme permet de chiffrer des fichiers choisis dans une image de disque .DMG.

Il existe plusieurs programmes de chiffrement pour **Microsoft Windows**. Nous recommandons ceux-ci:

* [**FREE CompuSec**](http://www.ce-infosys.com/english/free_compusec/free_compusec.aspx) est un programme gratuit, propriétaire, de chiffrement/déchiffrement à la volée. Il peut, chiffrer un disque dur, une clé USB ou un CD en partie ou au complet. Le module **DataCrypt** de **CompuSec** peut être utilisé pour chiffrer des fichiers individuels.
* [**CryptoExpert 2009 Lite**](http://www.cryptoexpert.com/lite/) est un programme gratuit, propriétaire, de chiffrement/déchiffrement à la volée qui crée des volumes chiffrés, à la manière de **TrueCrypt**.
* [**AxCrypt**](http://www.axantum.com/AxCrypt/) est un programme gratuit et de source libre qui permet de chiffrer des fichiers individuels.
* [**Steganos LockNote**](https://www.steganos.com/us/products/for-free/locknote/overview/) est un programme gratuit et de source libre. Il peut être utilisé pour chiffrer et déchiffrer n'importe quel texte. Le texte sera stocké dans l'application **LockNote**: Le mécanisme qui permet de chiffrer ou de déchiffrer une note est incorporé au fichier. **LockNote** est portable et aucune installation n'est requise.

### 1.1 À propos de cet outil ###

**TrueCrypt** protégera vos données en les verrouillant derrière un mot de passe que vous créerez vous-même. Attention : Si vous oubliez le mot de passe, vous perdrez l’accès à vos données! **TrueCrypt** utilise un processus de chiffrement pour protéger vos fichiers (veuillez vous assurer que le chiffrement est légal dans votre pays!). Au lieu de chiffrer les fichiers existants, **TrueCrypt** crée une section protégée sur votre ordinateur, un *volume* chiffré, où vous pouvez ensuite stocker des fichiers de façon sécurisée.  

**TrueCrypt** offre la possibilité de créer un volume standard ou un volume caché. D'une manière ou d'une autre, vos fichiers resteront confidentiels, mais un volume caché vous permet de dissimuler vos données les plus importantes derrière des données moins délicates, ce qui les protège même lorsque vous êtes forcé à ouvrir votre volume **TrueCrypt** standard. Le présent guide explique comment fonctionnent les deux types de volume.


