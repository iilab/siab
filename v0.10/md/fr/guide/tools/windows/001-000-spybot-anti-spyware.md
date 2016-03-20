

---

lang: fr
community: guide
type: tools
legacy: True
child: False
os: windows
weight: 001
title: Spybot - Anti-Spyware

---

		
**Site Internet**

[**www.safer-networking.org/fr**](http://www.safer-networking.org/fr)

**Configuration requise**

- Compatible avec toutes les versions de Windows 

**Version utilisée pour rédiger ce guide**

- 1.6.2

**Licence** 

- Gratuiciel (*Freeware*) 

**Lecture requise**

- Livret pratique Security in-a-box, chapitre [**1. Protéger votre ordinateur contre les logiciels malveillants et les pirates**](/fr/chapter-1)

**Niveau**: 1: Débutant, **2 : Moyen**, 3 : Intermédiaire, 4 : Expérimenté, 5 : Avancé 

**Temps d'apprentissage**: 20 minutes 

**Ce que vous apportera l’utilisation de cet outil**: 

- La capacité de **supprimer** plusieurs types de logiciels malveillants et/ou espions. 
- La capacité de **vacciner** votre système informatique **avant** qu’il ne soit infecté ou menacé de perturbations malveillantes.

**Autres programmes compatibles avec GNU Linux, Mac OS et/ou Microsoft Windows**:

Les systèmes d'exploitation **GNU Linux** et **Mac OS** sont, à l'heure actuelle, pratiquement épargnés par les logiciels malveillants (mouchards, virus, etc.). Pour vous protéger, nous vous recommandons de: **1)** mettiez régulièrement à jour votre système d'exploitation, ainsi que tous les programmes qui y sont installés; **2)** utilisez un des programmes antivirus listés au chapitre portant sur [*Avast*](/fr/avast_principale); **3)** utilisiez un des programme pare-feu listés au chapitre portant sur [*Comodo*](/fr/comodo_principale); **4)** utilisiez un navigateur sûr comme [*Firefox*](/fr/firefox_principale) avec le module complémentaire [*NoScript*] (/fr/firefox_noscript) qui empêche l'exécution des scripts téléchargés automatiquement avec les pages web. Ces mesures préventives suffiront à protéger votre système **GNU Linux** ou **Mac OS**.

La situation est très différente pour les ordinateurs équipés du système **Microsoft Windows**. Des milliers de nouveaux logiciels malveillants sont conçus chaque jour. Les méthodes d'attaque sont de plus en plus sophistiquées. Les mesures préventives décrites au précédent paragraphe sont **nécessaires** aux ordinateurs qui fonctionnent avec **Microsoft Windows**. De plus, nous recommandons fortement l'utilisation de **Spybot**, telle que décrite dans le présent chapitre.
Si malgré toutes ces précautions votre ordinateur est infecté et que vous avez besoin d'outils supplémentaires, nous recommandons les logiciels suivants: 

1. Installez [**SuperAntiSpyware**](http://superantispyware.com), actualisez les définitions et scannez votre ordinateur.
2. Installez [**Malwarebytes Anti-Malware**](http://www.malwarebytes.org/mbam.php), lancez un *Scan rapide*, puis lancez un *Scan*. Lorsque l scan est complété, supprimez les mouchards détectés affichés dans le panneau *Show Results*
3. Utilisez d'autres programmes anti-mouchards gratuits comme:  [**Microsoft Windows Defender**](http://www.microsoft.com/windows/products/winfamily/defender), [**Ad-Aware Internet Security**](http://www.lavasoft.com/) ou [**SpywareBlaster**](http://www.javacoolsoftware.com/spywareblaster.html).

### 1.1 À propos de cet outil  ###

**Spybot S&D** est un programme libre et gratuit, dont l’usage est très répandu pour détecter et éliminer des systèmes informatiques divers types de logiciels publicitaires (*adware*), malveillants (*malware*) ou espions (*spyware*). Le programme vous permet également de vacciner votre système contre les logiciels publicitaires, malveillants et/ou espions avant même qu’ils n’infectent votre ordinateur.

Le terme « logiciel publicitaire » (ou publiciel; *adware* en anglais) désigne tout logiciel qui affiche des publicités sur votre ordinateur. Certains types de publiciels fonctionnent sensiblement comme des logiciels espions et peuvent envahir votre vie privée ou menacer la sécurité de votre système. 

Le terme « logiciel malveillant » (*malware* en anglais) désigne tout programme – par ex. des Chevaux de Troie (*Trojans*) ou des vers informatiques (*worms*) – conçu pour nuire à votre ordinateur ou en détourner les opérations sans votre consentement, ou sans même que vous en soyez conscient. 

Le terme « logiciel espion » (ou mouchard; *spyware* en anglais), désigne tout programme conçu pour récolter des données, observer et enregistrer vos renseignements privés et surveiller vos habitudes de navigation sur Internet. Tout comme les logiciels malveillants, les mouchards s’exécutent souvent sur votre ordinateur à votre insu. C’est pourquoi l’installation d’un programme comme **Spybot** vous aidera à protéger votre système et à VOUS protéger! 

**Spybot** installe aussi une application supplémentaire appelée **TeaTimer**. Cela protégera votre ordinateur contre d’éventuelles infections par des logiciels malveillants.  

**Commentaire**: **Windows Vista** comporte son propre programme anti-espion, appelé **Windows Defender**. **Vista** semble cependant laisser **Spybot** fonctionner sans conflit. 


