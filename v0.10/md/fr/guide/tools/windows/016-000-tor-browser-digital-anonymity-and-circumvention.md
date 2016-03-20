

---

lang: fr
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 016
title: Tor Browser - Digital Anonymity and Circumvention

---

**Site Internet**
			
[**https://www.torproject.org**](https://www.torproject.org/)
			
**Configuration requise**

- Compatible avec toutes les versions de **Windows**
- Une connexion Internet
- Compatible avec tous les navigateurs populaires, en particulier **Mozilla Firefox**			

**Versions utilisées pour rédiger ce guide**

- Tor Browser: 1.3.24 

**Licence** 

- Free/Libre Open Source Software

**Lecture préalable** 

- Livret pratique Security in-a-box, chapitre [**8. Préserver son anonymat et contourner la censure sur Internet**](/fr/chapter-8) 

**Niveau**: 1: Débutant, 2: Moyen, 3: **Intermédiaire**, 4: **Expérimenté**, 5: Avancé  

**Temps d’apprentissage**: 20 - 30 minutes 

**Ce que vous apportera l’utilisation de cet outil**: 

- La capacité de cacher votre identité numérique sur Internet.
- La capacité de déjouer vos **fournisseurs de service Internet** et les mécanismes de surveillance en dissimulant vos destinations en ligne. 
- La capacité de contourner la censure et les règles de filtrage sur Internet.

**Autres programmes compatibles avec GNU Linux, Mac OS et/ou Microsoft Windows**:

Il existe des versions du client de réseau de connexion anonyme **Tor** pour les systèmes d'exploitation *GNU Linux**, **Mac OS** et **Microsoft Windows**. **Tor** est l'outil en son genre le plus recommandé et le mieux testé. Nous vous présentons néanmoins d'autres solutions: 

* [**Hotspot Shield**](http://hotspotshield.com/) est une solution commerciale gratuite de **Réseau privé virtuel** (**VPN**)  pour **Microsoft Windows**.
* [**Dynaweb FreeGate**](http://www.dit-inc.us/freegate) est un outil de proxy gratuit pour **Microsoft Windows**.
* [**UltraReach UltraSurf**](http://www.ultrareach.com/) est un outil de proxy gratuit pour **Microsoft Windows**.
* [**Your Freedom**](http://www.your-freedom.net/) est un outil de proxy commercial qui offre également un service gratuit (quoique plus lent). Il est disponible en versions **Linux**, **Mac OS** et **Microsoft Windows**.
* [**Psiphon**](http://psiphon.ca/) est un proxy web et fonctionne donc avec tous les systèmes d'exploitation.

Nous suggérons fortement de lire la documentation concue par  [**Sesawe**](http://sesawe.net/), une alliance mondiale vouée à la promotion de l'accès à l'information sans censure sur Internet.

## 1.1 À propos de cet outil ##

**Tor** est un logiciel conçu pour accroître le degré de sécurité et d’anonymat de vos activités et habitudes de navigation sur Internet. Il agit en camouflant votre identité et en brouillant la trace de vos activités sur Internet, afin que les technologies de surveillance soient incapables de vous retracer. Que l’anonymat soit important ou pas pour vous, **Tor** peut s’avérer un moyen utile et sécuritaire de promouvoir les libertés en ligne et contourner les mesures de censure sur Internet lorsque vous naviguez (ou publiez) sur certains sites ou carnets. 

**Tor** protège votre anonymat en routant vos communications à travers un réseau décentralisé de serveurs/relais géré par des bénévoles un peu partout dans le monde. Cela empêche d’éventuels agents espions ou malveillants de surveiller votre connexion Internet pour savoir quels sites vous avez visités et/ou pour déterminer votre position géographique (où vous vous trouvez, sur quel ordinateur vous travaillez, etc.). Quant aux administrateurs bénévoles du réseau **Tor**, certains d’entre eux sont en mesure de savoir que vous utilisez le logiciel, et certains autres peuvent savoir que *quelqu’un* est en train d’accéder aux sites que vous visitez, mais personne ne peut détenir ces deux renseignements en même temps. 

**Tor** peut camoufler vos tentatives de connexion à un site en particulier, mais n’a pas été conçu pour cacher le contenu de vos communications. En conséquence, **Tor** peut ajouter une couche supplémentaire de protection lorsque vous l’utilisez en combinaison avec d’autres services sécurisés comme **Riseup** ou **Gmail**, mais vous ne devriez pas utiliser ce programme pour accéder à des fournisseurs de service de courrier électronique non sécurisé, comme **Hotmail** ou **Yahoo**, ou tout autre site qui envoie ou reçoit des renseignements sensibles par une connexion *http* non sécurisée. 

**Définitions**: 

- **Port**: Dans ce guide, le terme « port » désigne un point d’entrée à travers lequel un logiciel peut communiquer avec des services se trouvant sur d’autres ordinateurs mis en réseau. Si une URL, comme **www.google.com**, vous fournit « l’adresse » d’un service, le port vous indique quelle « porte » utiliser lorsque vous arrivez à la bonne destination. Lorsque vous naviguez sur Internet, vous utilisez habituellement le port 80 pour les sites non sécurisés (**http://mail.google.com**) et le port 443 pour les sites sécurisés (**https://mail.google.com**). 

- **Proxy**: Dans ce guide, le terme « proxy » désigne un logiciel intermédiaire – sur votre ordinateur, votre réseau local ou quelque part d’autre sur Internet – qui contribue à relayer votre communication jusqu’à sa destination finale. 

- **Route**: Dans ce guide, le terme « route » désigne le chemin de communication sur Internet entre votre ordinateur et le serveur de destination. 

- **Relais passerelle**: Un relais passerelle (ou passerelle) est un serveur **Tor** qui facilite votre première entrée dans le réseau de connexion anonyme **Tor**. Les passerelles sont optionnelles et sont conçues pour être utilisées dans les pays où l’accès à **Tor** est bloqué.


