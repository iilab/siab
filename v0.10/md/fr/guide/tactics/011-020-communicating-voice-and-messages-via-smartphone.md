

---

lang: fr
community: guide
type: tactics
legacy: True
child: True
weight: 2
depth: 3
title: Communicating (Voice and Messages) via Smartphone

---

## Parler en toute sécurité ##

### Téléphonie de base ###

Dans la section [***Fonctions de base, traçabilité et anonymat***](https://securityinabox.org/fr/chapter_10_2_2) du Chapitre 10, nous avons présenté diférentes mesures à suivre afin de réduire le risque d'interception lors de l'utilisation du réseau opérateur de téléphonie mobile pour votre communication vocale.

Le fait d'utiliser Internet par le biais de votre smartphone via des connexions de données mobiles ou WiFi peut permettre une communication plus sûre, à savoir en utilisant [*VoIP*](/en/Glossary#VoIP) et des moyens de sécurisation de ce canal de communication. Certains outils de smartphone peuvent même étendre la sécurité au-delà de VoIP, aux appels à partir d'un téléphone mobile aussi (Voir **Redphone** ci-dessous).

Voici une liste de quelques outils, leurs avantages et inconvénients :

### Skype ###

La plus populaire des applications VoIP commerciales, [*Skype*](/en/glossary#skype), est disponible sur toutes les plateformes de smartphone et fonctionne bien si votre connectivité sans fil est fiable. Elle est moins fiable via une connexion de données mobile.

Dans la section [***Sécuriser vos autres outils de communication par Internet***](/fr/chapter_7_3) du [***chapitre 7 : Préserver la confidentialité de vos communications sur Internet***](https://securityinabox.org/fr/chapter-7), nous avons discuté des risques liés à l'utilisation de Skype et pourquoi il vaut mieux, dans la mesure du possible, l'éviter. En résumé, Skype est un logiciel non open-source qui fait qu'il est très difficile d'en confirmer indépendamment le niveau de sécurité. De plus, Skype appartient à Microsoft, qui a un intérêt commercial à savoir quand et d'où vous utilisez Skype. Skype peut également permettre à des organismes chargés de l'application de la loi d'accéder rétrospectivement à l'historique de vos communications.

### D'autres VoIP ###

L'utilisation de VoIP est généralement gratuite (ou nettement moins chère que les appels téléphoniques mobiles) et laisse peu de traces de données. De fait, un appel VoIP sécurisé peut être le moyen le plus sûr de communiquer.

[**CSipSimple**](http://f-droid.org/repository/browse/?fdid=com.csipsimple&fdpage=4) est un client VoIP solide pour téléphones Android, qui est bien entretenu et livré avec de nombreux assistants simples pour saisir les paramètres de différents services VoIP.

Le projet du [**Open Secure Telephony Network (OSTN)**](https://guardianproject.info/wiki/OSTN) et le serveur entretenu par le Guardian Project [**ostel.me**](https://ostel.me) proposent actuellement l'un des moyens les plus sûrs de communication vocale. Bien connaître et faire confiance à l'entité qui exploite le serveur que vous utilisez pour vos communications vocales est extrêmement important. Les hôtes de ce service – le [**Guardian Project**](https://guardianproject.info) – sont très connus et respectés dans la communauté. 

Lors de l'utilisation de CSipSimple, vous ne communiquez jamais directement avec votre interlocuteur; toutes vos données passent par le serveur Ostel. Il est alors beaucoup plus difficile de retracer vos données et de découvrir à qui vous parlez. En outre, Ostel ne conserve aucune de ces données, mises à part les données du compte dont vous avez besoin pour vous connecter. Tout ce que vous dites est chiffré et même vos métadonnées, qui sont normalement difficiles à dissimuler, sont floues puisque le trafic se fait à travers le serveur ostel.me. Si vous téléchargez CSipSimple depuis ostel.me, vous le recevrez préconfiguré pour ostel.me; ce qui rend son installation et utilisation d'autant plus faciles.

[**RedPhone**](https://play.google.com/store/apps/details?id=org.thoughtcrime.redphone) est une application logicielle libre et open source qui permet de chiffrer les données de communication vocale envoyées entre deux appareils qui utilisent cette application. Elle est facile à installer et très facile à utiliser puisqu'elle s'intègre dans votre numérotation normale et dans votre schéma des contacts. Mais les gens auxquels vous souhaitez parler doivent également installer et utiliser RedPhone. Pour une utilisation facile de RedPhone, prenez votre numéro de téléphone mobile comme identificateur (tel un nom d'utilisateur dans d'autres services VoIP). Toutefois, sachez qu'il devient de plus en plus facile d'analyser le trafic produit et de remonter jusqu'à vous par le biais de votre numéro de mobile. RedPhone utilise un serveur central, qui est un point de centralisation et place RedPhone dans une position de force (celle d'avoir le contrôle sur certaines de ces données). 

Des guides pratiques pour CSipSimple, Ostel.me et Redphone sont en prévision. En attendant, des informations supplémentaires sont disponibles en cliquant sur les liens mentionnés ci-dessus.

## Envoyer des messages en toute sécurité ##

Certaines précautions sont à prendre lors de l'envoi de SMS et l'utilisation de la messagerie instantanée ou de discussions en ligne sur votre smartphone.

### SMS ###

Comme décrit dans le [***chapitre 9.2.3 : Communications par texte – SMS / Messages textes***](/fr/chapter_10_2_3), la communication par SMS est non sûre par défaut. Toute personne ayant accès à un réseau de télécommunication mobile peut intercepter ces messages facilement, ce qui est un fait quotidien dans de nombreuses situations. Ne comptez pas sur l'envoi SMS non sécurisés lors de situations critiques. Il est de surcroît impossible d'authentifier les messages SMS, de savoir si le contenu d'un message a été modifié en chemin ou si l'expéditeur est bien la personne qu'il prétend être.

### SMS sécurisés ###

[**TextSecure**](https://play.google.com/store/apps/details?id=org.thoughtcrime.securesms) est un outil [*FOSS*](/en/glossary#FOSS) qui permet d'envoyer et de recevoir des SMS sécurisés via un téléphone Android. Il fonctionne à la fois pour des messages chiffrés et non chiffrés si bien que vous pouvez l'utiliser comme votre application SMS par défaut. Pour échanger des messages chiffrés, cet outil doit être installé par l'expéditeur et par le destinataire. Vous devrez donc amener les gens avec lesquels vous communiquez régulièrement à l'utiliser également. TextSecure détecte automatiquement lorsqu'un message chiffré est reçu par un autre utilisateur de TextSecure. Il vous permet également d'envoyer des messages chiffrés à plusieurs personnes. Les messages sont automatiquement signés; ce qui rend presque impossible la falsification du contenu. Dans notre guide pratique consacré à TextSecure, nous expliquons en détail les caractéristiques de cet outil et comment l'utiliser.

<div class=getstarted markdown=1>
Expérience pratique : se lancer avec le [*guide pratique TextSecure*](/en/textsecure_main).
</div>

### Chat sécurisé ###

L'utilisation de la messagerie instantanée ou le fait de chatter avec votre téléphone produit un grand nombre d'informations qui peuvent être interceptées. Vous courez ainsi le risque que ces conversations soient utilisées plus tard contre vous par des adversaires. Vous devez donc être extrêmement prudent sur les informations que vous divulguez lorsque vous envoyez des messages ou chattez avec votre téléphone.

Il existe des moyens de chatter et d'envoyer des messages instantanés en toute sécurité. Le meilleur moyen est d'utiliser le chiffrement de bout en bout, qui assure que la personne à l'autre bout du fil est bien celle que vous souhaitez.

Pour les téléphones Android, nous recommandons [**Gibberbot**](https://guardianproject.info/apps/gibber/) comme application de messagerie instantanée sécurisée. Gibberbot permet un chiffrement de vos chats facile et résistant avec protocole de messagerie [*Off-the-Record*](/en/glossary#OTR). Ce chiffrement assure à la fois l'authenticité (vous pouvez vérifier que vous chattez avec la bonne personne) et la sécurisation autonome de chaque session : s'il arrive que le chiffrement d'une session de chat soit compromise, d'autres sessions passées ou futures ne seront pas concernées.

Gibberbot a été conçu pour être utilisé avec Orbot; de sorte que vos messages de chat peuvent passer par le réseau anonymisant [*Tor*](/en/glossary#Tor). Tout échange est ainsi rendu intraçable voire comme n'ayant jamais eu lieu.

<div class=getstarted markdown=1>
Expérience pratique : se lancer avec le [*guide pratique Gibberbot*](/en/gibberbot_main).
</div>

Pour les iPhones, le client [**ChatSecure**](https://chatsecure.org) offre les mêmes fonctionnalités. Il n'est toutefois pas évident à utiliser avec le réseau [*Tor*](/en/glossary#Tor).

Un guide pratique pour ChatSecure va bientôt paraître. En attendant, des informations supplémentaires sont disponibles sur la [page d'accueil](https://chatsecure.org). 

Quelle que soit l'application que vous utilisez, réfléchissez bien au type de compte duquel vous voulez chatter. Par exemple, quand vous utilisez Google Talk, vos informations d'identification et l'heure de votre session de discussion sont connus par Google. De même, mettez-vous d'accord avec vos interlocuteurs sur le fait que l'historique des discussions ne doit en aucun cas être sauvegardé - surtout si les discussions ne sont pas chiffrées.

