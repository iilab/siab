

---

lang: fr
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 011
title: Pidgin with OTR - Secure Instant Messaging

---

**Site Internet**

- **Pidgin**: [**www.pidgin.im**](http://www.pidgin.im)
- **OTR**: [**www.cypherpunks.ca/otr**](http://www.cypherpunks.ca/otr/)

**Configuration requise**:

- Une connexion Internet 
- Compatible avec toutes les versions de Windows

**Versions utilisées pour rédiger ce guide**:

- Pidgin 2.10.3
- OTR 3.2.0

**Licence**: 

- FLOSS (Free/libre Open Source Software)

**Lecture requise**:

Livret pratique Security in-a-box, chapitre [**7. Préserver la confidentialité de vos communications sur Internet**](/fr/chapter-7)

**Niveau**: 1: Débutant, **2: Moyen**, 3: Intermédiaire, 4: Expérimenté, 5: Avancé 

**Temps d’apprentissage**: 30 minutes 

**Ce que vous apportera l’utilisation de cet outil **: 

- La capacité d’organiser et de gérer certains des services de messagerie instantanée les plus connus à l’aide d’un seul programme;
- La possibilité de mener des séances de clavardage (chat) privées et sécurisées.

**Autres programmes compatibles avec GNU Linux, Mac OS ou Microsoft Windows:**

**Pidgin** et **OTR** offrent des versions compatibles avec **Microsoft Windows** et **GNU/Linux**. [**Miranda IM**](http://www.miranda-im.org/) est un autre programme de **messagerie instantanée** multi-protocoles conçu **Microsoft Windows** et compatible avec **OTR**. Pour **Mac OS**, nous recommandons [**Adium**](http://adium.im/), un programme de **messagerie instantanée** multi-protocoles qui supporte le plugin **OTR**.

## 1.1 À propos de cet outil ##

**Pidgin** est un client de **messagerie instantanée** (**MI**) gratuit et de source ouverte qui vous permet d’organiser et de gérer vos différents comptes de **messagerie instantanée** avec une seule et unique interface. Avant de commencer à utiliser **Pidgin**, vous devez disposer d’au moins un compte de **MI**. Par exemple, si vous possédez un compte de courriel **Gmail**, vous pouvez utiliser le service de **MI** **Google Talk** avec **Pidgin**. Utilisez les détails de connexion associés à votre compte de**MI** pour y accéder via **Pidgin**.

**Note**: Tous les utilisateurs sont fortement encouragés à en apprendre le plus possible sur les politiques de leurs **fournisseurs de service de MI** en matière de confidentialité et de sécurité. 

**Pidgin** est compatible avec les services de **MI** suivants: [**AIM**](http://dashboard.aim.com/aim), [**Bonjour**](http://www.apple.com/support/bonjour/), [**Gadu-Gadu**](http://komunikator.gadu-gadu.pl/), [**Google Talk**](http://www.google.com/talk/), **Groupwise**, [**ICQ**](http://www.icq.com), **IRC**, [**MIRC**](http://www.mirc.com/), [**MSN**](http://www.msn.com/), 
[**MXit**](http://www.mxit.com/), [**MySpaceIM**](http://www.myspace.com/guide/im), [**QQ**](http://www.qq.com/), [**SILC**](http://silcnet.org/), **SIMPLE**, [**Sametime**](http://www.ibm.com/developerworks/downloads/ls/lst/), [**Yahoo!**](http://messenger.yahoo.com/), **Zephyr** ainsi que tous les clients de **MI** utilisant le protocole de messagerie **XMPP**.

**Pidgin** ne permet pas la communication entre différents services de **MI**. Par exemple, si vous utilisez **Pidgin** pour accéder à votre compte **Google Talk**, il ne vous sera pas possible de clavarder avec un ami qui utilise plutôt un compte **ICQ**.

Par contre, **Pidgin** peut être réglé pour gérer plusieurs comptes compatibles avec l'un ou l'autre des protocoles supportés. Autrement dit, vous pouvez simultanément utiliser un compte **Gmail** un compte **ICQ**, et clavarder avec des correspondants qui utilisent *l'un ou l'autre* de ces services (qui sont supportés par  **Pidgin**).

Il est conseillé d’utiliser **Pidgin** pour tous vos besoins en matière de **messagerie instantanée**, puisque ce programme offre plus de sécurité que la plupart des options qui existent et ne vient pas par défaut avec des logiciels publicitaires ou espions superflus qui pourraient compromettre votre sécurité ou votre vie privée. 

La messagerie **Off-the-Record** (**OTR**) est un module complémentaire, conçu tout spécialement pour **Pidgin**, qui permet de clavarder en privé et offre les fonctions suivantes:

- **Authentification**: Vous êtes assuré que votre correspondant est bel et bien la personne que vous croyez.
- **Possibilité de démenti** (*deniability*): Après votre conversation, il est impossible de retracer les messages jusqu’à vous ou jusqu’à votre correspondant.
- **Chiffrement**: Personne d’autre que vous ne peut lire vos communications instantanées.
- **Perfect Forward Secrecy**: Si une tierce partie trouve l'accès à vos clés privées, vos conversations préalables ne sont pas compromises.

**Note**: Vous devez installer le programme **Pidgin** avant d’installer le plugin **OTR**.


