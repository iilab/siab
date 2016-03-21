

---

lang: fr
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Use COMODO Firewall

---

Sommaire des sections de cette page:

- [**3.0 Comment autoriser ou bloquer des accès avec COMODO Firewall**](#3.0)
- [**3.1 Comment ouvrir l'interface principale de COMODO Firewall**](#3.1)
- [**3.2 Un survol de l'interface principale de COMODO Firewall**](#3.2)

-------

<a name="3.0"></a>
## 3.0 Comment autoriser ou bloquer des accès avec COMODO Firewall ##

Un pare-feu est un programme conçu pour protéger votre ordinateur contre des pirates ou des logiciels malveillants. Ces derniers peuvent tenter d'accéder directement à votre ordinateur ou d'envoyer des donnée à partir de votre ordinateur vers une tierce partie. **Comodo Firewall** doit être configuré correctement pour lui permettre d'apprendre et d'enregistrer quelles sont les applications qui sont "sûres" afin de leur autoriser l'accès, et de bloquer les requêtes provenant de logiciels dangereux et/ou constituent des menaces.

Chaque fois que **Comodo Firewall** reçoit une requête de connexion, il affiche une fenêtre *Alerte Pare-feu* vous demandant d'*autoriser* ou de *bloquer* l'accès de votre système depuis ou vers l'Internet. L'exercice qui suit concerne un programme sûr (**Firefox**) et vous aidera à vous familiariser avec les alertes pare-feu et à les utiliser correctement. Même si des exceptions sont parfois faites pour les requêtes provenant de navigateurs et clients de courrier électronique universellement reconnus, chaque fois qu'une requête de connexion est faite, une *Alerte pare-feu* semblable à celle-ci s'affiche: 

![](/sbox/screen/comodo-fr/21.png)

*Figure 1: Un exemple d'alerte pare-feu de COMODO*

Un pare-feu n'est rien d'autre qu'un ensemble de règles servant à contrôler le trafic entrant et sortant. Chaque fois que vous cliquez sur *Autoriser* ou *Bloquer*, **COMODO Firewall** génère une règle sur mesure pour la requête au réseau de ce processus ou de ce programme. **COMODO Firewall** fait cela pour les processus et programmes nouveaux ou inconnus, ainsi que pour ceux compris dans la liste *Éditeurs de logiciels certifiés* de la fenêtre *Defense+ - Tâches > Stratégie de Sécurité*.

**Se souvenir de ma réponse**: Cette option est employée pour enregistrer si autorisez ou bloquez un programme en particulier. **COMODO Firewall* autorisera ou bloquera automatiquement les requêtes provenant de ce programme la prochaine fois qu'il tentera de se connecter, selon le choix que vous aurez fait préalablement.

**Important**: Nous recommandons fortement de désactiver la fonction *Se souvenir de ma réponse* lorsque vous commencez à utiliser **COMODO Firewall**. Décidez si vous autorisez ou bloquez différentes requêtes et observez quels effets vos décisions ont sur le fonctionnement de votre système. Activez la fonction *Se souvenir de ma réponse* si et *seulement si* vous êtes complètement sûr de votre décision.

**Astuce**: Limiter strictement l'accès à votre système est la meilleure façon d'en assurer la sécurité. N'hésitez pas à bloquer toutes les requêtes suspectes ou non identifiées. Si un blocage fait en sorte qu'un programme ne fonctionne plus normalement, vous pourrez autoriser la requête la prochaine fois que vous recevez une alerte du pare-feu.

**Première étape**. **Cliquez** sur ![](/sbox/screen/comodo-fr/26.png) pour afficher la fenêtre *Propriétés* et obtenir des renseignements sur le processus ou le programme qui lance une requête, dans ce cas-ci, **Firefox**: 

![](/sbox/screen/comodo-fr/27.png)

*Figure 2: La fenêtre Propriétés de Firefox.exe*

**Deuxième étape**: **Cliquez** sur ![](/sbox/screen/comodo-fr/02.png) pour fermer la fenêtre *Propriétés* du programme.

**Troisième étape**:  Selon les renseignements affichés dans la fenêtre *Propriétés*: 
si vous avez déterminé qu'une requête n'est pas sûre, ou si vous êtes incertain, **cliquez** sur ![](/sbox/screen/comodo-fr/29.png) pour donner à **COMODO Firewall** la consigne de bloquer l'accès à votre système.
OU: 
Si vous avez déterminé qu'un programme légitime lance une requête non malveillante, **cliquez** sur ![](/sbox/screen/comodo-fr/28.png) pour autoriser l'accès à votre système.

**Quatrième étape**. **Cliquez** sur ![](/sbox/screen/comodo-fr/28.png) pour permettre à **Firefox** d'accéder à votre système par l'intermédiaire de **COMODO Firewall**.

**Cinquième étape**. Puisque **Firefox** est un programme considéré sûr, **cochez** l'option ![](/sbox/screen/comodo-fr/30.png) pour que **COMODO Firewall** autorise automatiquement l'accès à **Firefox** la prochaine fois et subséquemment.

**Commentaire**: Le bouton *Autoriser* vous permet d'autoriser manuellement, au cas par cas, l'accès à un processus ou un programme.

**Astuce**: **Cliquez** sur ![](/sbox/screen/comodo-fr/31.png) pour accéder aux fiches d'aide en ligne de **COMODO Firewall**.

Votre capacité à prendre les bonnes décisions s'améliorera au fur et à mesure que vous prendrez de l'expérience avec **COMODO Firewall**. 

<a name="3.1"></a>
## 3.1 Comment ouvrir l'interface principale de COMODO Firewall ##

**COMODO Firewall** démarrera automatiquement lorsque vous aurez installé le programme et redémarré votre système. Le programme comporte un panneau de configuration complet, avec de nombreuses fonctions et options flexibles. Les utilisateurs **débutants** apprendront facilement à gérer les alertes de sécurité **COMODO Firewall**, alors que les utilisateurs *expérimentés* et *avancés* pourront se familiariser avec des aspects plus complexes de la gestion et de la configuration du pare-feu.

**Commentaire**: Tous les exemples illustrés ici sont basés sur le mode *Défense optimale*. Cela signifie que le système de prévention des intrusions est activé automatiquement. Si vous avez installé **COMODO Firewall** avec l'option *Pare-feu seulement*, *Defense+"* ne sera pas activé.

Pour ouvrir l'interface principale de **COMODO Firewall** suivez les étapes énumérées ci-dessous:

**Première étape**. **Sélectionnez Démarrer> Programmes > Comodo > Firewall > Comodo Firewall**. 

**Commentaire**: Vous pouvez également afficher l'interface principale du programme en **double-cliquant** sur l'icone de bureau, ou en **double-cliquant** sur l'icone **COMODO Firewall** qui se trouve dans la *Barre des tâches*. De plus, vous pouvez **cliquer à droite** sur l'icone **COMODO Firewall** pour afficher le menu contextuel, puis **sélectionner** *ouvrir*, comme suit: 

![](/sbox/screen/comodo-fr/35.png)

*Figure 3: Le menu contextuel à partir de l'icone de connectivité COMODO Firewall*

![](/sbox/screen/comodo-fr/36.png)

*Figure 4: L'interface principale de Comodo Firewall, en mode Sommaire par défaut*

<a name="3.2"></a>
## 3.2 Un survol de l'interface principale de COMODO Firewall ##

La fenêtre *Pare-feu* affiche un sommaire clair et concis des requêtes entrantes et sortantes des processus et programmes qui tentent de se connecter par l'entremise de **COMODO Firewall**. Il y a habituellement davantage de requêtes sortantes que de requêtes entrantes. Le mode de fonctionnement par défaut est le *Mode sécurisé*. Les différents modes seront abordés plus loin dans cette section. Le *Trafic* affiche les différents processus et programmes en cours et le nombre de requêtes effectuées, sous forme de pourcentage.

**Cliquez** sur ![](/sbox/screen/comodo-fr/37.png) pour afficher les sommaires détaillés des requêtes sortantes *en tout temps*, comme suit: 

![](/sbox/screen/comodo-fr/38.png)

*Figure 5: Un exemple de fenêtre de Connexions actives affichant les détails du trafic Internet*

**Cliquez** sur ![](/sbox/screen/comodo-fr/39.png) pour afficher la fenêtre des *Connexions actives* des requêtes entrantes, *en tout temps*.

**Astuce**: **Cliquez** sur ![](/sbox/screen/comodo-fr/40.png) pour arrêter toutes les requêtes entrantes et sortantes, si votre service Internet ralentit ou plante soudainement, et/ou si vous avez des raisons de croire qu'un processus ou un programme malveillant est en cours de téléchargement ou d'opération. Ce faisant, vous mettez automatiquement le *pare-feu* en mode de fonctionnement ![](/sbox/screen/comodo-fr/41.png). Révisez le sommaire détaillé dans la fenêtre *Connexions actives* pour trouver les possibles sources du problème.

Après vous être assuré d'avoir résolu les problèmes, **cliquez** sur ![](/sbox/screen/comodo-fr/42.png) pour indiquer à **COMODO Firewall** de recommencer à traiter les requêtes entrantes et sortantes et retourner au ![](/sbox/screen/comodo-fr/43.png) comme d'habitude.

### 3.2.1 Les icones d'état de COMODO Firewall ###

 **COMODO Firewall** et **Defense+** fonctionnent main dans la main; si les deux programmes sont en cours d'opération, l'icone qui se trouve à la gauche de l'interface principale s'affiche comme suit: 

![](/sbox/screen/comodo-fr/69.png)

*Figure 6: L'icone d'état vert de COMODO Firewall*

Si l'un ou l'autre des programmes est désactivé, l'icone d'état indique que le pare-feu ou une des composants de la protection proactive est désactivé: 

![](/sbox/screen/comodo-fr/70.png)

*Figure 7: L'icone d'état jaune indiquant que le pare-feu est désactivé*

Si les deux programmes sont désactivés, l'icone d'état s'affiche comme suit: 

![](/sbox/screen/comodo-fr/71.png)

*Figure 8: L'icone d'état jaune de COMODO Firewall indiquant que plusieurs protections sont désactivées*

Dans un cas comme dans l'autre, **cliquez** sur ![](/sbox/screen/comodo-fr/72.png) pour activer la protection correspondante.

