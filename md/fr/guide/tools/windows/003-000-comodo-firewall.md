

---

lang: fr
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 003
title: Comodo Firewall

---

**Site Internet**

[**www.personalfirewall.comodo.com**](http://www.personalfirewall.comodo.com)

**Configuration requise**

- Windows 2000/XP/2003/Vista
- Les privilèges d'administration sont nécessaires à l'installation

**Version utilisée pour rédiger ce guide**

- 5.0.16

**Licence** 

- Gratuiciel

**Lecture préalable**: 

- Livret pratique Security-in-a-Box chapitre [**1. Protéger votre ordinateur contre les logiciels malveillants et les pirates**](/fr/chapter-1)

**Niveau:** 1: Débutant, 2: Moyen, **3: Intermédiaire, 4: Expérimenté**, 5: Avancé

**Temps d’apprentissage**: 60 minutes 

**Ce que vous apportera l’utilisation de cet outil**:

- Une protection efficace de votre ordinateur et de votre réseau contre les attaques de tiers hostiles ou de pirates, et contre les programmes malveillants, les virus et autres menaces à vos logiciels et à votre système;
- La capacité, au moyen d’une interface de logiciel aisément configurable, de filtrer toutes les requêtes effectuées par les programmes installés sur votre ordinateur lorsque vous accédez à Internet.  

**Autres programmes compatibles avec GNU Linux, Mac OS et/ou Microsoft Windows:**

**GNU/Linux** comporte un pare-feu intégré ([**netfilter/iptables**](http://www.netfilter.org/)) et présente d'excellents paramètres de sécurité. Il existe plusieurs interfaces utilisateurs simplifiées, dont [**GUFW**](https://help.ubuntu.com/community/Gufw) (**Graphical Uncomplicated Firewall**) (voir [**plus d'information**](http://blog.bodhizazen.net/linux/firewall-ubuntu-gufw/)).

**Mac OS** contient également un puissant pare-feu intégré, qui peut être amélioré par un assortiment de modules complémentaires, dont: [**NoobProof**](http://www.hanynet.com/noobproof/) ou [**IPSecuritas**](http://www.lobotomo.com/products/IPSecuritas/). Pour les utilisateurs qui en ont les moyens, nous recommandons l'achat de [**Little Snitch**](http://www.obdev.at/products/littlesnitch/index.html), qui permet de pousser au niveau supérieur votre sécurité et la protection de votre identité sur Internet.

À part **COMODO Firewall**, il existe de nombreuses options pour **Microsoft Windows**. Les utilisateurs pourront apprécier [**ZoneAlarm Free Firewall**](http://www.zonealarm.com/security/en-us/zonealarm-pc-security-free-firewall.htm) ou [**Outpost Firewall Free**](http://free.agnitum.com/).

### 1.1 À propos de cet outil ###

Un pare-feu agit comme un portier ou un gardien de votre ordinateur. Le pare-feu applique une série de règles quant à l’information qui doit être autorisée à accéder à votre ordinateur et celle qui doit pouvoir en sortir. Votre pare-feu est le premier programme à recevoir et à analyser l’information provenant d’Internet, et le dernier programme à balayer l’information sortante.

Le pare-feu permet d’empêcher les pirates ou d’autres intrus d’accéder aux renseignements personnels stockés sur votre ordinateur. Le programme empêche aussi les programmes malveillants d’envoyer de l’information vers Internet sans votre autorisation. **COMODO Firewall** est un logiciel pare-feu bien connu et réputé. C’est un logiciel d’exploitation libre, ce qui signifie que vous n’avez pas besoin d’obtenir une licence d’utilisation pour vous en servir. 

L’utilisation d’un programme pare-feu personnalisé exige, dans les premiers temps, un investissement important de temps et d’effort. Vous devez vous assurer que tous les paramètres sont correctement réglés et adaptés à l’usage que vous faites de votre ordinateur. Une fois la période initiale d’apprentissage complétée, le pare-feu n’exigera que des interventions mineures de votre part.

**Avertissement**!: N’accédez jamais à Internet si aucun pare-feu n’est installé sur votre ordinateur! Même si votre modem Internet ou votre routeur possèdent leur propre pare-feu, il est fortement recommandé que vous en installiez également un sur votre ordinateur.


