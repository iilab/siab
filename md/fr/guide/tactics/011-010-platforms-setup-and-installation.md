

---

lang: fr
community: guide
type: tactics
legacy: True
child: True
weight: 1
depth: 3
title: Platforms, Setup and Installation

---

### Plateformes et systèmes d'exploitation ###

Au moment de la rédaction de ces lignes, les smartphones les plus couramment utilisés sont l'iPhone d'Apple et l'Android de Google, suivis par les Blackberry et les Windows Phones. La principale différence entre l'Android et d'autres systèmes d'exploitation se trouve dans le fait qu'Android est le plus souvent un système open source ([*FOSS*](/en/Glossary#FOSS)), qui permet au système d'exploitation d'être audité indépendamment afin de vérifier s'il protège correctement les informations et communications des utilisateurs. Il soutient également le développement d'applications de sécurité pour cette plateforme. De nombreux analystes programmeurs sensibles à la sécurité développent des applications Android en prenant en compte la sûreté des utilisateurs. Certains d'entre eux seront mentionnés plus tard dans ce chapitre.

Quel que soit le type de smartphone que vous utilisez, il vous faut être au courant de certains faits liés à l'utilisation d'un téléphone connecté à Internet et livré avec des fonctionnalités telles que le [*GPS*](/en/glossary#GPS) ou la possibilité de mise en réseau sans fil. Dans ce chapitre, nous nous concentrons sur les appareils équipés de la plateforme Android, car, comme mentionné ci-dessus, il y est plus facile de sécuriser les données et communications. Néanmoins, les guides de configuration de base et quelques applications pour d'autres appareils que les téléphones Android seront également exposés.

Les téléphones Blackberry ont été présentés comme des appareils de messagerie texte et email « sûrs » dans la mesure où les messages et emails transitent par des serveurs Blackberry, hors de portée d'oreilles indiscrètes potentielles. Malheureusement, de plus en plus de gouvernements réclament l'accès à ces communications, invoquant la nécessité de se prémunir contre le terrorisme et le crime organisé. Les gouvernements d'Inde, des Émirats arabes unis, d'Arabie Saoudite, d'Indonésie et du Liban ont par exemple examiné attentivement l'utilisation des appareils Blackberry et exigé l'accès aux données des utilisateurs dans leur pays.

### Mobiles classiques (ou feature phones) ###

Les 'feature phones' (par exemple le 7705 Twist de Nokia ou le Rogue de Samsung) constituent une autre catégorie de téléphones mobiles. Ceux-ci ont depuis peu augmenté leurs fonctionnalités de façon à inclure celles de certains smartphones. Mais de manière générale, les systèmes d'exploitation des feature phones restent moins accessibles, les possibilités de développement d'applications de sécurité ou de perfectionnement sont donc limitées. Nous ne traitons pas spécifiquement des feature phones, toutefois de nombreuses mesures présentées ici valent également pour ceux-ci.

### Smartphones labellisés et simlockés ###

Les smartphones sont généralement vendus labellisés ou simlockés. Un smartphone simlocké est un appareil qui ne peut fonctionner qu'avec la carte SIM fournie par l'opérateur. Généralement, les opérateurs de réseau mobile simlockent un téléphone en y installant leur propre firmware ou logiciel. Ils peuvent également désactiver certaines fonctionnalités ou en ajouter d'autres. Le simlockage permet aux entreprises d'augmenter leurs gains en orientant votre utilisation du smartphone, souvent aussi en collectant des données sur la façon dont vous utilisez votre téléphone ou en permettant l'accès à votre smartphone à distance.

Pour ces raisons, nous recommandons l'achat d'un téléphone non simlocké, si possible. Un téléphone simlocké présente un risque plus élevé dans la mesure où toutes vos données sont acheminées par un seul opérateur, qui centralise vos flux de données, empêche de changer de carte SIM et donc de diffuser des données via d'autres opérateurs. Si votre téléphone est simlocké, demandez à quelqu'un en qui vous avez confiance de le désimlocker.

### Configuration générale ###

Les smartphones ont de nombreux paramètres contrôlant la sûreté de l'appareil. Il est important de prêter attention à la configuration de votre smartphone. Dans les guides pratiques ci-dessous, nous vous signalons certains paramètres de sécurité qui sont disponibles mais non actifs par défaut, tout comme d'autres qui sont actifs par défaut et rendent votre téléphone vulnérable.

<div class=getstarted markdown=1>
Expérience pratique : se lancer avec le [*guide de configuration générale pour Android*](/en/android_basic).
</div>

### Installation et mise à jour des applications ###

La façon habituelle d'installer un nouveau logiciel sur votre smartphone consiste à utiliser l'Appstore d'iPhone ou le Play Store de Google, de s'y connecter avec vos accréditations d'utilisateur et, de télécharger et installer l'application désirée. En vous connectant, vous associez votre usage de la boutique en ligne à votre compte d'utilisateur connecté. Les propriétaires de la boutique en ligne d'applications conservent des registres indiquant l'historique de la navigation de l'utilisateur et des applications choisies.

Les applications proposées dans les boutiques en ligne officielles sont censées êtres vérifiées par les propriétaires des boutiques (Google ou Apple), mais ceci fournit en réalité une protection faible contre ce que les applications peuvent engendrer une fois installées sur votre téléphone. Par exemple, certaines applications sont en état de copier et de communiquer votre carnet d'adresses après avoir été installées sur votre téléphone. Dans le cas des téléphones Android, toute application doit demander durant le processus d'installation ce qu'elle est en droit d'accomplir à partir du moment où elle est en service. Vous devez porter une attention toute particulière aux autorisations qui vous sont demandées et si ces autorisations sont en rapport avec la fonction de l'application que vous installez. Par exemple, si vous envisagez d'installer un « lecteur de nouvelles » et vous découvrez qu'il demande le droit d'envoyer vos contacts via une connexion de données mobile à un tiers, vous feriez mieux de chercher une autre application dont l'accès et les demandes de droits sont plus appropriés.

Les applications Android sont également disponibles à partir de sources situées en dehors des canaux officiels de Google. Pour utiliser ces sites de téléchargement, il vous suffit de cocher l'option *Sources inconnues* dans les *paramètres des applications*.

Il est utile de tenir compte de ces autres sites si vous souhaitez minimiser le contact avec Google. Nous recommandons [**F-Droid**](http://f-droid.org) ('Free Droid'), qui ne propose que des applications [*FOSS*](/en/glossary#FOSS). Dans ce guide, F-Droid constitue le dépôt principal des applications que nous recommandons et nous ne faisons référence à Google Play que si F-Droid ne dispose pas du type d'app recherché.

Si vous ne voulez (ou ne pouvez) pas vous connecter à Internet pour accéder à ces apps, vous pouvez transférer les apps à partir du téléphone de quelqu'un d'autre en envoyant des fichiers [*.apk*](/en/glossary#apk) ('android application package') via bluetooth. Vous pouvez soit télécharger le fichier .apk sur la carte Micro SD de votre téléphone, soit utiliser un câble USB afin de l'y déplacer à partir d'un PC. Quand vous avez reçu le fichier, il suffit de cliquer le nom du fichier assez longtemps jusqu'à ce que vous soyez invité à l'installer. (**Note** : soyez particulièrement prudent lorsque vous utilisez bluetooth - infos à ce sujet dans le [***chapitre 10 : Autres fonctions des appareils mobiles***](/fr/chapter_10_2_4).

