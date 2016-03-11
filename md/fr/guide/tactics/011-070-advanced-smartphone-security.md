

---

lang: fr
community: guide
type: tactics
legacy: True
child: True
weight: 7
depth: 3
title: Advanced Smartphone Security

---

## Obtenez l'accès complet à votre smartphone ##

La plupart des smartphones peuvent plus que ce que leur système d'exploitation, que ce que les logiciels des fabricants (firmware) et les programmes des opérateurs mobiles permettent. À l'inverse, certaines fonctionnalités sont 'bloquées' si bien que l'utilisateur ne peut ni contrôler ni modifier ces fonctions; elles restent hors de portée. Dans la plupart des cas, ces fonctionnalités sont inutiles. Certaines applications et fonctionnalités permettent cependant parfois d'améliorer la sécurité des données et des communications sur un smartphone. Il existe également d'autres fonctionnalités dont la suppression permet d'éviter des risques.

C'est pour cela, et pour d'autres raisons, que certains utilisateurs de smartphone décident de manipuler les différents logiciels et programmes tournant sous leur smartphone dans le but d'obtenir des passe-droits appropriés leur permettant d'installer des fonctionnalités améliorées, d'en supprimer, ou d'en amoindrir d'autres.

La procédure de dépassement des limites imposées par les opérateurs mobiles ou fabricants de systèmes d'exploitation est appelé rooting (dans le cas des appareils Android), ou jailbreaking, débridage (dans le cas des appareils iOS tels l'iPhone ou l'iPad). En règle générale, un rooting ou débridage réussi a pour conséquence que vous obtenez tous les passe-droits dont vous avez besoin pour installer et utiliser d'autres applications, modifier des configurations autrement verrouillées, et le contrôle complet sur le stockage de données et la mémoire du smartphone.

**ATTENTION**: Le rooting ou jailbreaking peut être irréversible et demande une certaine expérience quant à l'installation et la configuration de logiciels. Considérez ce qui suit :

- Vous risquez de rendre votre smartphone définitivement inutilisable, de le 'bricker' (cad de le réduire à l'état de 'brique').
- La garantie du fabricant ou de l'opérateur mobile peut être annulée.
- Dans certains endroits, cette procédure peut être illégale.

Mais si vous faites attention, un appareil rooté est un moyen simple de gagner plus de contrôle sur votre smartphone et de le rendre ainsi beaucoup plus sûr.

### Firmware alternatifs ###

Les firmware (appelés aussi micrologiciels) se réfèrent à des programmes étroitement liés à l'appareil en particulier. Ils coopèrent avec le système d'exploitation de l'appareil et sont responsables des fonctions de base du matériel informatique de votre smartphone, telles que le haut-parleur, le microphone, les caméras, l'écran tactile, la mémoire, les clés, les antennes, etc.

Si vous avez un téléphone Android, vous pouvez envisager l'installation d'un firmware alternatif pour renforcer vos possibilités de contrôle de votre téléphone. Notez que pour installer un firmware alternatif, vous devez rooter votre téléphone.

Un firmware alternatif pour Android est par exemple le [**Cyanogenmod**](http://www.cyanogenmod.com) qui, entre autres, vous permet de désinstaller des applications au niveau du système de votre téléphone (cad celles installées par le fabricant du téléphone ou votre opérateur de réseau mobile). En faisant cela, vous pouvez réduire les possibilités de contrôle de votre appareil, telles que l'envoi de données à votre fournisseur de services à votre insu.

En outre, Cyanogenmod est livré par défaut avec une application OpenVPN qui peut sinon être fastidieuse à installer. VPN (Virtual Private Network) est l'un des moyens de transiter vos communications en ligne à travers un autre serveur en toute sécurité. 

Cyanogenmod propose également un mode de navigation incognito dans lequel l'historique de vos communications n'est pas enregistré sur votre smartphone.

Cyanogenmod est livré avec de nombreuses autres fonctionnalités. Toutefois, il n'est pas compatible avec tous les appareils Android, donc avant de commencer, consultez la [liste des appareils compatibles](http://www.cyanogenmod.com/devices).
 
### Chiffrement de volumes entiers ###

Si votre téléphone est rooté, vous pouvez envisager de chiffrer l'intégralité des données stockées ou de créer un volume sur le smartphone pour protéger certaines informations sur le téléphone.

[**Luks Manager**](http://www.whispersys.com/) permet un chiffrement à la volée simple et solide de volumes avec une interface conviviale. Nous vous recommandons fortement d'installer cet outil avant de commencer à stocker des données importantes sur votre appareil Android et d'utiliser les volumes chiffrés que Luks Manager fournit pour stocker toutes vos données.

Le projet Whisper Systems est en train de développer l'application [**WhisperCore**](http://www.whispersys.com/whispercore.html) qui permettra le chiffrement complet de votre appareil Android.

### Réseau Privé Virtuel (virtual private network VPN) ###

Un VPN fournit un tunnel chiffré à travers Internet entre votre appareil et un serveur VPN. On parle de tunnel parce que contrairement à d'autres trafics chiffrés, comme https, il cache tous les services, protocoles et contenus. Une connexion VPN est configurée une fois et n'est résiliée que lorsque vous en décidez.

Notez que depuis que votre trafic passe par le serveur proxy ou VPN, un intermédiaire a seulement besoin d'accéder au proxy pour analyser vos activités. Par conséquent, il est important de bien choisir parmi les services proxy et VPN. Il est également conseillé d'utiliser différents proxies et/ou VPNs car le fait de répartir vos flux de données réduit les conséquences d'un service compromis.

Nous recommandons d'utiliser le serveur [**RiseUp VPN**](https://help.riseup.net/en/vpn). Vous pouvez utiliser RiseUp VPN sur un appareil Android après avoir installé Cyanogenmod (voir ci-dessus). Il est également facile d'établir la connexion à RiseUp VPN sur l'iPhone - en savoir plus [ici](https://support.apple.com/kb/HT1424).

