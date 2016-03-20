

---

lang: fr
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 013
title: Thunderbird with Enigmail and GPG - Secure Email Client

---

**Site Internet**

- [**www.mozilla.com/thunderbird**](http://www.mozilla.com/thunderbird/)
- [**www.enigmail.mozdev.org**](http://enigmail.mozdev.org/home/index.php)
- [**www.gnupg.org**](http://www.gnupg.org/)

**Configuration requise**

- Compatible avec toutes les versions de Windows

**Versions utilisées pour rédiger ce guide**

- Thunderbird 3.1.5 
- Enigmail 1.1.2
- GNU Privacy Guard (GnuPG) 2.0.4 

**Licence**

- FLOSS (Free/Libre Open Source Software) 

**Lecture préalable**

- Livret pratique Security in-a-box, chapitre [**7. Préserver la confidentialité de vos communications sur Internet**](/fr/chapter-7)

**Niveau**: 1: Débutant, **2: Moyen** et **3: Intermédiaire**, 4: Expérimenté, 5: Avancé 

**Temps d'apprentissage**: 40 minutes 

**Ce que vous apportera l’utilisation de cet outil**: 

- La capacité de gérer plusieurs comptes de courrier électronique à l’aide d’un seul et unique programme. 
- La capacité de lire et composer des messages lorsque vous n’êtes pas connecté à Internet. 
- La capacité d’utiliser le chiffrage par clé publique (asymétrique) pour faire en sorte que vos courriels restent confidentiels. 

**Autres programmes compatibles avec GNU Linux, Mac OS et/ou Microsoft Windows**:

Le client de messagerie **Mozilla Thunderbird** est disponible pour **GNU Linux**, **Mac OS**, **Microsoft Windows** et d'autres systèmes d'exploitation. En ce qui a trait à la sécurité numérique, la gestion simultanée de plusieurs comptes de courrier électronique est une tâche complexe, c'est pourquoi il est *fortement recommandé* d'utiliser **Mozilla Thunderbird** à cette fin. Les avantages que présente  **Thunderbird**, un client de messagerie *libre* et *gratuit*, multi plateforme et de *source ouverte*, sont d'autant plus importants lorsqu'on le compare à ses rivaux commerciaux comme **Microsoft Outlook**. Cela dit, si vous préférez utiliser un autre programme que **Mozilla Thunderbird**, nous recommandons les trois options suivantes, également gratuites et de source ouverte:

* [**Claws  Mail**](http://www.claws-mail.org/) disponible pour **GNU Linux** et **Microsoft Windows**;
* [**Sylpheed**](http://sylpheed.sraoss.jp/en/) disponible pour **GNU Linux**, **Mac OS** et**Microsoft Windows**;
* [**Alpine**](http://www.washington.edu/alpine/) disponible pour **GNU Linux**, **Mac OS** et**Microsoft Windows**.

### 1.1 À propos de cet outil ###

**Mozilla Thunderbird** est un client de messagerie électronique libre, gratuit, multi plateforme et de source ouverte, qui permet de recevoir, envoyer, trier et archiver des messages de courrier électronique. Un client de messagerie est une application informatique qui vous permet de télécharger et gérer vos courriels sans utiliser un navigateur Internet. Vous pouvez gérer plusieurs comptes de courriel à l'aide sd'un seul et unique programme de messagerie. Vous devez avoir au moins un compte de courrier électronique pour utiliser **Thunderbird**. Vous pouvez également créer des comptes [**Gmail**](https://www.google.com/accounts/NewAccount?service=mail) ou [**RiseUp**](http://securityinabox.org/en/riseup_createaccount) si vous le souhaitez.

**Enigmail** est un module complémentaire conçu pour **Thunderbird**. Il donne accès aux fonctions d'authentification et de chiffrement offertes par **GNU Privacy Guard** (**GnuPG**).

**GnuPG** est un programme de chiffrement par clé publique (asymétrique) utilisé pour générer et gérer des paires de clés afin de chiffrer et déchiffrer des messages pour préserver la confidentialité et la sécurité de vos communications par courrier électronique. Comme nous le verrons plus loin dans ce chapitre, **GnuPG** doit être installé pour qu'**Enigmail** fonctionne.

