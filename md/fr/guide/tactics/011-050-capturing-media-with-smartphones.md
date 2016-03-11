

---

lang: fr
community: guide
type: tactics
legacy: True
child: True
weight: 5
depth: 3
title: Capturing Media with Smartphones

---

Comme nous en avons discuté dans le [***chapitre 7 : Préserver la confidentialité de vos communications sur Internet***](https://securityinabox.org/fr/chapter-7) et le [***chapitre 8 : Préserver votre anonymat et contourner la censure sur Internet***](https://securityinabox.org/fr/chapter-8), accéder à des contenus sur Internet ou publier du matériel en ligne tel que des photos ou des vidéos, laisse de nombreuses traces indiquant qui et où vous êtes et ce que vous faites. Cela peut vous mettre en danger. Utiliser votre smartphone pour communiquer avec Internet amplifie ce risque.

### Accès par WiFi ou données mobiles ###

Les smartphones vous permettent de contrôler la façon dont vous accédez à Internet : via une connexion sans fil fournie par un point d'accès (tel qu'un cybercafé), ou via une connexion données mobile telle que GPRS, EDGE ou UMTS, fournies par votre opérateur de réseau mobile. 

L'utilisation d'une connexion WiFi réduit les traces de données que vous pourriez laisser auprès de votre opérateur de réseau mobile (en n'utilisant pas votre forfait de téléphonie mobile pour vous connecter). Toutefois, une connexion données mobile est parfois le seul moyen d'être en ligne. Malheureusement, les protocoles de connexion données mobile (telles EDGE ou UMTS) ne sont pas des standards ouverts. Les développeurs indépendants et les ingénieurs de sécurité ne peuvent pas analyser ces protocoles pour voir comment ils sont mis en oeuvre par des supports de données mobiles. 

Dans certains pays, les opérateurs de réseau mobile opèrent conformément à une législation différente de celle des fournisseurs d'accès à Internet, ce qui peut conduire à une surveillance plus directe de la part des gouvernements et des transporteurs.

Quel que soit le chemin que vous prenez pour vos communications numériques avec un smartphone, vous pouvez réduire les risques d'exposition des données en utilisant des outils d'anonymisation et de chiffrement.

### Anonymiser ###

Pour accéder à du contenu en ligne de façon anonyme, vous pouvez utiliser une app Android appelée [**Orbot**](https://www.torproject.org/docs/android.html.en). Orbot fait passer vos communications sur Internet par le réseau anonyme Tor. 

<div class=getstarted markdown=1>
Expérience pratique : se lancer avec le [*guide pratique Orbot*](/en/Orbot_main).
</div>

Une autre app, Orweb, est un navigateur web qui offre des fonctionnalités améliorant la confidentialité en passant par des serveurs mandataires et en ne conservant pas d'historique local de la navigation. Orbot et Orweb contournent ensemble les filtres et pare-feux du réseau, et procurent une navigation anonyme.

<div class=getstarted markdown=1>
Expérience pratique : se lancer avec le [*guide pratique Orweb*](/en/Orweb_main).
</div>

### Proxies ###

La version mobile  [*Firefox*](/en/glossary#Firefox) – [**Firefox mobile**](http://f-droid.org/repository/browse/?fdid=org.mozilla.firefox) peut-être équipée d'extensions proxy qui dirigent le trafic vers un serveur proxy (appelé aussi mandataire). De là, votre trafic est acheminé vers le site que vous souhaitez. Ceci est très utile en cas de censure, mais peut toujours encore révéler vos demandes, à moins que la connexion de votre client au proxy soit chiffrée. Nous recommandons l'extension [**Proxy Mobile**](https://guardianproject.info/apps/proxymob-firefox-add-on/), (également du [**Guardian Project**](https://guardianproject.info/), qui rend facile l'utilisation de serveurs mandataires avec Firefox. Il s'agit également du seul moyen de canaliser les communications mobiles via Firefox vers Orbot et d'utiliser le réseau [*Tor*](/en/glossary#Tor).

