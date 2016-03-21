

---

lang: fr
community: guide
type: tactics
legacy: True
child: True
weight: 3
depth: 3
title: Anonymity networks and basic proxy servers

---

<h3><a name="Reseaux_de_connexion_anonyme" title="Réseaux de connexion anonyme"></a>Les réseaux de connexion anonyme</h3>

<p>Les réseaux de connexion anonyme font généralement «&nbsp;rebondir&nbsp;» votre connexion entre plusieurs <a href="glossaire#Proxy" title="Proxy"><i>proxys</i></a> sécurisés pour occulter l’origine de vos requêtes et la nature des sites que vous tentez de joindre. Cela peut réduire considérablement la vitesse à laquelle vous pourrez charger des sites ou accéder à des services Internet. Par contre, le programme <a href="glossaire#Tor" title="Tor"><i>Tor</i></a> offre un moyen de <a href="glossaire#Contournement" title="Contournement"><i>contournement</i></a> sûr, fiable et public, dont l’utilisation toute simple vous épargne beaucoup d’inquiétude. Comme toujours, vous devez vous assurer que votre connexion à un site Internet donné soit sécurisée (avec le <kbd>HTTPS</kbd>) avant de commencer à échanger des renseignements sensibles comme des mots de passe et des courriels par l’intermédiaire d’un navigateur.</p>

<p>Pour utiliser Tor, il vous faudra installer le logiciel, mais vous serez ensuite en mesure de préserver votre anonymat, en plus de contourner efficacement les mesures de censure. Chaque fois que vous vous connectez au réseau Tor, vous passez par un chemin complètement aléatoire, par le truchement de trois proxys Tor sécurisés. Cela vous assure que ni votre <a href="glossaire#FSI" title="FSI"><i>FSI</i></a>, ni les proxys eux-mêmes, ne soient en mesure de connaître à la fois l’<a href="glossaire#Adresse_IP" title="Adresse_IP"><i>adresse IP</i></a> de votre ordinateur et la position des services Internet que vous recherchez. Pour plus d’information au sujet de ce programme, veuillez consulter le <a guide="" href="tor" pratique=""><i><b>Guide pratique Tor</b></i></a>.</p>

<p>&nbsp;</p>

<table cellpadding="5" cellspacing="0" style="border: 2pt dashed #008000; background-color: #e9e8a4">
	<tbody>
		<tr>
			<td><img align="middle" height="63" src="/sites/securitybkp.ngoinabox.org/files/u9/hand_web_trans.png" width="60" /> <b>Expérience pratique&nbsp;: se lancer avec le </b><i><a href="tor"><b>Guide pratique Tor </b></a></i></td>
		</tr>
	</tbody>
</table>

<p>Une des plus grandes forces du programme Tor est qu’en plus de pouvoir être utilisé avec un navigateur, il est compatible avec d’autres logiciels. Des clients de messagerie comme <a href="glossaire#Thunderbird" title="Thunderbird"><i>Mozilla Thunderbird</i></a> et des programmes de messagerie instantanée comme <a href="glossaire#Pidgin" title="Pidgin"><i>Pidgin</i></a> fonctionnent très bien avec Tor, que ce soit pour accéder à des services filtrés ou pour occulter votre utilisation de ces services.</p>

<p>&nbsp;</p>

<h3>Proxys de contournement uniques</h3>

<p>&nbsp;</p>

<p>Il y a trois éléments essentiels dont vous devez tenir compte au moment de choisir un proxy de contournement unique. Premièrement, s’agit-il d’un outil basé sur le Web, ou devez-vous plutôt modifier des paramètres ou installer un logiciel sur votre ordinateur&nbsp;? Deuxièmement, est-ce un service sécurisé&nbsp;? Troisièmement, est-ce un service privé ou public&nbsp;?</p>

<p><b>Proxys Web et autres types de proxys&nbsp;:</b></p>

<p>Les proxys Web sont probablement les plus faciles à utiliser. Vous n’avez pour ce faire qu’à pointer votre navigateur vers la page du proxy, saisir l’adresse filtrée que vous souhaitez visiter et cliquer sur un bouton. Le proxy affichera alors le contenu de la page filtrée à l’intérieur de sa propre page. Vous pouvez aussi suivre les hyperliens ou saisir une nouvelle adresse dans le proxy si vous souhaitez visualiser une autre page. Vous n’avez aucun logiciel à installer ni aucun paramètre à modifier dans votre navigateur, ce qui signifie que les proxys Web sont&nbsp;:</p>

<ul>
	<li>Faciles à utiliser&nbsp;;</li>
	<li>Joignables à partir d’ordinateurs publics (par exemple les ordinateurs d’un café Internet) qui ne vous permettent pas, en temps normal, d’installer des logiciels ou de modifier des paramètres&nbsp;;</li>
	<li>Possiblement plus sûrs que d’autres méthodes si vous craignez d’être «&nbsp;pris&nbsp;» avec des programmes de contournement sur votre ordinateur.</li>
</ul>

<p>Les proxys Web comportent néanmoins certains inconvénients. Ils n’affichent pas toujours les pages correctement et plusieurs proxys Web sont tout simplement incapables de charger les sites Internet complexes et les flux de données audio et vidéo. De plus, malgré que tous les proxys tendent à ralentir proportionnellement au nombre d’utilisateurs qui s’y connectent, ce désagrément est encore plus prononcé avec les proxys Web publics. Par ailleurs, les proxys Web ne fonctionnent évidemment qu’avec les pages Web. Vous ne pouvez pas, par exemple, utiliser un programme de messagerie instantanée ou un client de messagerie pour accéder à certains services bloqués via un proxy Web. Finalement, les proxys Web sécurisés ne peuvent offrir qu’une confidentialité limitée parce qu’ils doivent eux-mêmes intercepter et modifier les données qui vous sont envoyées par les sites que vous visitez. S’ils ne le faisaient pas, vous ne pourriez pas cliquer sur un lien sans automatiquement quitter le proxy pour tenter d’établir une connexion directe à la page Web visée. Nous reviendrons sur ce détail à la prochaine section.</p>

<p>Les autres types de proxys exigent habituellement que vous installiez un programme ou que vous configuriez une adresse de proxy externe dans les paramètres de votre navigateur ou de votre système d’exploitation. Dans le premier cas, le programme de contournement vous offre habituellement la possibilité d’activer et de désactiver l’outil pour indiquer à votre navigateur d’utiliser ou non le proxy. Souvent, ces logiciels vous permettent également, lorsqu’un proxy est bloqué, d’en trouver automatiquement un nouveau (comme nous avons vu ci-dessus). Dans le second cas, vous devrez apprendre à utiliser la bonne adresse de proxy, laquelle doit être modifiée si ledit proxy est bloqué ou s’il ralentit tellement qu’il en devient inutilisable.</p>

<p>Bien qu’elle soit légèrement plus difficile à utiliser qu’un proxy Web, cette méthode est plus susceptible d’afficher des pages complexes correctement. Elle devrait également rester efficace plus longtemps avant de commencer à ralentir en raison du nombre élevé d’utilisateurs qui s’y connectent. De plus, différents proxyspeuvent être utilisés pour divers types d’applications Internet. Il existe par exemple des proxys HTTP pour les navigateurs, des proxys SOCKS pour les programmes de courriel et de messagerie instantanée et des proxys VPN, qui peuvent être utilisés pour rediriger la totalité de vos activités sur Internet afin d’éviter le filtrage.</p>

<p><b>Proxys sécurisés et proxys non sécurisés&nbsp;:</b></p>

<p>Un proxy sécurisé, dans ce chapitre, désigne tout proxy qui donne la possibilité aux utilisateurs d’établir des connexions <a href="glossaire#Chiffrement" title="Chiffrement"><i>chiffrées</i></a>. Un proxy non sécurisé vous permettra tout de même de contourner plusieurs types de filtrage, mais vous sera moins utile si votre connexion Internet est l’objet d’une recherche de mots-clé ou d’adresses Web ciblées. C’est une idée particulièrement mauvaise d’utiliser un proxy non sécurisé pour accéder à des sites Internet habituellement chiffrés, comme des comptes de webmail ou des sites de services bancaires. En faisant cela, il est possible que vous exposiez des renseignements sensibles qui seraient normalement restés cachés. De plus, comme nous l’avons vu ci-dessus, les proxys non sécurisés sont plus faciles à identifier et à bloquer que les proxys sécurisés pour ceux dont c’est le travail d’actualiser les logiciels de filtrage. En fin de compte, le fait qu’il existe d’excellents proxys gratuits, rapides et sécurisés signifie qu’il y a très peu de raisons valides d’employer un proxy non sécurisé.</p>

<p>Vous pouvez déterminer si un proxy Web est sécurisé ou non en tentant de vous connecter au site du proxy avec une adresse <kbd>HTTPS</kbd>. Tout comme avec les services webmail, il est possible que les connexions sécurisées et non sécurisées soient toutes deux possibles. C’est pourquoi vous devriez toujours vous assurer d’utiliser l’adresse sécurisée. La plupart du temps, dans de tels cas, vous devez accepter un «&nbsp;<a href="glossaire#Certificat_de_securite" title="Certificat_de_securite"><i>certificat de sécurité</i></a>&nbsp;» (exigé par votre navigateur) afin de continuer. Tel est le cas du proxy <a href="glossaire#Peacefire" title="Peacefire"><i>Peacefire</i></a>, abordés ci-dessous. Les avertissements de votre navigateur concernant les certificats de sécurité vous indiquent que quelqu’un, comme votre FSI ou un <a href="glossaire#Hacker" title="Hacker"><i>pirate informatique</i></a>, pourrait être en train de contrôler votre connexion au proxy. Malgré l’utilité de ces avertissements, il est toujours conseillé d’utiliser, autant que possible, des proxys sécurisés. Par contre, lorsque votre méthode de contournement dépend exclusivement d’un proxy de ce type, vous devriez éviter de visiter des sites Internet sécurisés, de saisir des mots de passe ou d’échanger des renseignements sensibles, à moins que vous ne soyez en mesure de vérifier l’authenticité de la signature <a href="glossaire#SSL" title="SSL"><i>SSL</i></a> du proxy. Pour ce faire, vous aurez besoin d’une voie de communication avec l’administrateur du proxy.</p>

<p>L’annexe C du <a href="">Guide de l’utilisateur de Psiphon</a>&nbsp;[3] explique les étapes que vous et l’administrateur du proxy devez suivre pour vérifier l’empreinte numérique du proxy.</p>

<p>Vous devriez également éviter d’accéder à des données sensibles par le truchement d’un proxy Web, à moins que vous ne fassiez totalement confiance à son administrateur. Cette mesure de précaution s’impose, que vous receviez ou non un avertissement de certificat de sécurité lorsque vous visitez le proxy. Elle s’impose même si vous connaissez assez bien l’administrateur du proxy pour vérifier l’empreinte du serveur avant d’indiquer à votre navigateur d’accepter le certificat de sécurité. Lorsque vous dépendez d’un serveur proxy unique pour contourner les mesures de filtrage, les administrateurs dudit proxy connaîtront votre adresse IP et les sites Web que vous visitez. Qui plus est, si ce proxy est basé sur le Web, un administrateur malveillant pourrait facilement accéder à toutes les données qui circulent entre votre navigateur et les sites Internet que vous visitez, y compris le contenu de vos courriels et vos mots de passe.</p>

<p>Quant aux proxys non Web, vous devrez peut-être effectuer quelques recherches pour déterminer si les connexions sécurisées sont permises ou non. Tous les proxys et réseaux de connexion anonyme recommandés dans ce chapitre sont sécurisés.</p>

<p><b>Proxys privés et proxys publics&nbsp;:</b></p>

<p>Les proxys publics acceptent des connexions de n’importe qui, alors que les proxys privés exigent habituellement un nom d’utilisateur et un mot de passe. Bien que les proxys publics comportent l’avantage évident d’être librement accessibles, dans la mesure où on peut les trouver, ils tendent bien souvent à être rapidement très achalandés. En conséquence, même si les proxys publics sont aussi sophistiqués et bien administrés que les proxys privés, ils sont souvent plutôt lents. Finalement, les proxys privés sont habituellement gérés soit par des entreprises commerciales, soit par des administrateurs qui créent des comptes pour les utilisateurs qu’ils connaissent personnellement ou socialement. Il est donc assez facile, dans la majorité des cas, de déterminer les motivations des administrateurs de proxys privés. Vous ne devriez pas tenir pour acquis, cependant, que les proxys privés sont plus dignes de confiances que leurs pendants publics. Après tout, il est déjà arrivé que l’appât du profit mène les administrateurs de certains services numériques à dénoncer leurs utilisateurs.</p>

<p>Des proxys publics uniques non sécurisés peuvent souvent être trouvés en exécutant une recherche avec des mots-clé comme «&nbsp;public proxy&nbsp;» dans un moteur de recherche, mais vous ne devriez pas vous fier aux services trouvés de cette manière. Si vous avez le choix, il est préférable d’utiliser un proxy privé sécurisé, administré par des gens que vous connaissez (personnellement ou de réputation) et en qui vous avez confiance, et qui ont les aptitudes techniques nécessaires pour préserver la sécurité de leur serveur. Votre choix d’utiliser ou non un proxy Web dépendra de vos besoins particuliers et de vos préférences personnelles. Chaque fois que vous utilisez un proxy pour contourner des mesures de censure, il est fortement conseillé d’employer le navigateur <a href="glossaire#Firefox" title="Firefox"><i>Firefox</i></a> et d’installer le module complémentaire <a href="glossaire#NoScript" title="NoScript"><i>NoScript</i></a>, tel qu’indiqué dans le <a guide="" href="firefox_principale" pratique=""><i><b>Guide pratique Firefox</b></i></a>. Cela vous protégera contre les proxys malveillants et les sites Internet qui pourraient tenter de découvrir votre vraie adresse IP. Finalement, n’oubliez pas qu’un proxy chiffré ne transformera pas magiquement un site non sécurisé en site sécurisé. Vous devez toujours vous assurer d’avoir établi une connexion <kbd>HTTPS</kbd> avant d’envoyer ou de recevoir des renseignements sensibles.</p>

<p>Si vous n’êtes pas en mesure de trouver un individu, un organisme ou une compagnie dont le service de proxy vous semble digne de confiance, abordable et facilement accessible depuis votre pays, vous devriez sérieusement considérer l’utilisation du réseau de connexion anonyme Tor, que nous avons brièvement abordé ci-dessus, à la section <a href="#Reseaux_de_connexion_anonyme" title="Réseaux de connexion anonyme"><i><b>Réseaux de connexion anonyme</b></i></a>.</p>

<p>&nbsp;</p>


