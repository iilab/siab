

---

lang: fr
community: guide
type: tactics
legacy: True
child: True
weight: 1
depth: 3
title: Securing your email

---

<p>Tout d’abord, vous devriez appliquer quelques mesures importantes pour améliorer la sécurité de vos communications par courrier électronique. La première chose à faire est de vous assurer que personne d’autre que votre destinataire ne soit en mesure de lire le message que vous envoyez. Cette question est abordée dans les sections <a href="#Preserver_la_confidentialite_de_votre_courrier_electronique" title="Préserver la confidentialité de votre courrier
électronique"><i><b>Préserver la confidentialité de votre courrier électronique</b></i></a> et <a href="#Adopter_un_service_de_courriel_securise" title="Adopter un service de courriel sécurisé"><i><b>Adopter un service de courriel sécurisé</b></i></a>, ci-dessous. Au delà des questions élémentaires, il est essentiel que vos correspondants soient en mesure de vérifier, hors de tout doute, qu’un message donné provient bel et bien de vous et non pas d’une tierce personne qui aurait réussi à usurper votre identité. Nous verrons cela à la sous-section <a href="chapter_7_4#Chiffrer_et_authentifier_des_messages_individuellement" title="Chiffrer et authentifier des messages individuellement"><i><b>Chiffrer et authentifier des messages individuellement</b></i></a> de la section <a href="chapter_7_4" title="Principes de sécurité avancée"><i><b>Principes de sécurité avancée</b></i></a>.</p>

<p>Vous devriez toujours savoir quoi faire lorsque vous avez l’impression que la confidentialité de vos communications par courriel a été transgressée. La section <a href="chapter_7_2" title="Chapitre 7.2"><i><b>Que faire si vous soupçonnez que vos communications par courriel sont surveillées</b></i></a> aborde cette question délicate.</p>

<p>Gardez également à l’esprit qu’un service de courriel sécurisé ne vous servira pas à grand-chose si chaque mot que vous tapez est enregistré par un logiciel espion et retransmis périodiquement à un tiers. Le chapitre <a href="chapter-1" title="Chapitre 1"><i><b>1. Protéger votre ordinateur contre les logiciels malveillants et les pirates</b></i></a> offre de bons conseils sur les moyens de se prémunir contre ce type de menaces et le chapitre <a href="chapter-3" title="Chapitre 3"><i><b>3. Créer et sauvegarder des mots de passe sûrs</b></i></a> vous aidera à protéger efficacement l’accès à vos comptes de courriel et de messagerie instantanée.</p>

<p>&nbsp;</p>

<h3><a name="Preserver_la_confidentialite_de_votre_courrier_electronique" title="Préserver la confidentialité de votre courrier électronique"></a>Préserver la confidentialité de votre courrier électronique</h3>

<p>&nbsp;</p>

<p>L’Internet est un réseau de communication ouvert où les données circulent habituellement dans des formats lisibles. Si un message de courriel est intercepté entre un expéditeur et un destinataire, son contenu peut facilement être lu. Comme l’Internet est justement un vaste réseau global qui repose sur une multitude d’ordinateurs intermédiaires pour faire circuler les données, plusieurs personnes ont l’occasion d’intercepter un message. Votre fournisseur de services Internet (<a href="glossaire#FSI" title="FSI"><i>FSI ou FAI</i></a> ou <i>ISP</i>, en anglais) est le premier intermédiaire du message que vous envoyez à un destinataire donné. De même, le FSI de votre destinataire est le dernier intermédiaire par lequel le message transite avant d’aboutir dans la corbeille d’arrivée de celui-ci. À moins que vous ne mettiez en place certaines mesures de précaution, votre message pourrait très bien être intercepté et falsifié à l’une ou l’autre de ces étapes, ou à n’importe quelle étape entre les deux.</p>

<p>&nbsp;</p>

<table cellpadding="5" cellspacing="0" style="border: 2pt dashed #008000; background-color: #e9e8a4">
	<tbody>
		<tr>
			<td><i>Pablo&nbsp;: Je parlais justement de ça avec une de nos partenaires et elle me disait que ses collègues et elles sauvegardent parfois des messages importants dans le répertoire «&nbsp;Brouillons&nbsp;» d’un compte de courriel dont ils partagent le mot de passe. Ça me paraît un peu étrange, mais est-ce que ça peut fonctionner&nbsp;? Est-ce que ça n’empêche pas justement les tiers malveillants de lire ces messages, puisqu’ils ne sont jamais vraiment envoyés&nbsp;? </i><br />
			<br />
			<i>Claudia&nbsp;: Chaque fois que tu lis un message sur ton ordinateur, même si ce n’est qu’un brouillon, son contenu t’a été envoyé par Internet. Sinon, tu ne pourrais pas l’afficher sur ton écran, pas vrai&nbsp;? Le problème, c’est que si quelqu’un t’a placé sous surveillance, il ne se contente pas d’inspecter tes messages, il peut aussi espionner toutes les données qui circulent depuis et vers ton ordinateur. En d’autres termes, ce truc ne peut fonctionner que si tous les collègues en question se connectent au compte partagé de façon sécurisée. Et si c’est le cas, il n’est pas moins pratique de créer des comptes séparés pour chaque personne.</i></td>
		</tr>
	</tbody>
</table>

<p>Il existe depuis fort longtemps un moyen de sécuriser la connexion entre votre ordinateur et les sites que vous visitez. C’est ce niveau de sécurité que l’on retrouve, par exemple, lorsqu’on saisi un mot de passe ou les détails d’une carte de crédit sur un site Internet. La technologie qui rend possible ce genre de connexion s’appelle <a href="glossaire#Chiffrement" title="Chiffrement"><i>chiffrement</i></a> par <a href="glossaire#SSL" title="SSL"><i>Secure Sockets Layer (SSL)</i></a>. Il est possible de distinguer une connexion SSL d’une connexion normale en jetant un coup d’œil attentif à la <b>barre de navigation</b> de votre navigateur Web.</p>

<p>Toutes les adresses commencent normalement par la formule <b>HTTP</b>, tel qu’illustré ci-dessous&nbsp;:</p>

<p><img alt="source:Booklet/en/Scenario1/01.png" height="25" src="/sites/securitybkp.ngoinabox.org/files/u5/01.png" width="235" /></p>

<p>Lorsque vous visitez un site Internet sécurisé, l’adresse commence par la formule <kbd>HTTPS</kbd>&nbsp;:</p>

<p><img alt="source:Booklet/en/Scenario1/02.png" height="27" src="/sites/securitybkp.ngoinabox.org/files/u5/02.png" width="236" /></p>

<p>Le <b>S</b> supplémentaire signifie que votre ordinateur a ouvert une connexion sécurisée à ce site. Vous pouvez aussi remarquer une icône de cadenas, soit dans la <kbd>barre de navigation</kbd>, soit dans la <kbd>barre d’état</kbd> tout au bas de la fenêtre du navigateur. Ces éléments vous indiquent qu’aucun intrus ne sera en mesure d’espionner vos communications avec ce site en particulier.</p>

<p>En plus de protéger vos mots de passe et transactions financières, ce type de chiffrement est idéal pour sécuriser les communications par courriel. Par contre, plusieurs fournisseurs de services de courriel n’offrent pas l’accès sécurisé, alors que d’autres exigent que vous activiez vous-même la fonction, soit en réglant une préférence à cet effet, soit en saisissant la formule <b>HTTPS</b> manuellement. Vous devriez toujours vous assurer que votre connexion est sécurisée avant de vous enregistrer sur un site, de lire vos courriels ou d’envoyer des messages.</p>

<p>Vous devriez aussi être sur vos gardes lorsque le navigateur signale un <a href="glossaire#Certificat_de_securite" title="Certificat_de_securite"><i>certificat de sécurité</i></a> invalide au moment de se connecter à un compte de courriel. Cela pourrait signifier qu’un tiers tente de s’interposer dans la communication entre votre ordinateur et le serveur afin d’intercepter vos messages. Finalement, si vous utilisez un service webmail pour échanger des renseignements sensibles, il est essentiel que votre navigateur soit aussi fiable que possible. Nous suggérons fortement d’installer <a href="glossaire#Firefox" title="Firefox"><i>Mozilla Firefox</i></a> et ses modules de sécurité complémentaires.</p>

<p>&nbsp;</p>

<table cellpadding="5" cellspacing="0" style="border: 2pt dashed #008000; background-color: #e9e8a4">
	<tbody>
		<tr>
			<td><img align="middle" height="63" src="/sites/securitybkp.ngoinabox.org/files/u9/hand_web_trans.png" width="60" /> <b>Expérience pratique&nbsp;: se lancer avec le </b><i><a href="firefox_principale"><b>Guide pratique Firefox </b></a></i></td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>

<table cellpadding="5" cellspacing="0" style="border: 2pt dashed #008000; background-color: #e9e8a4">
	<tbody>
		<tr>
			<td><i>Pablo&nbsp;: Une de nos partenaires qui doit collaborer à la rédaction du rapport utilise habituellement son compte de courriel Yahoo lorsqu’elle est à l’extérieur du bureau. Je crois aussi me rappeler qu’une autre personne utilise Hotmail. Si j’envoie un message à ces personnes, est-ce que d’autres personnes peuvent les lire&nbsp;? </i><br />
			<br />
			<i>Claudia&nbsp;: Probablement. Les sites Internet de Yahoo, Hotmail et plusieurs autres fournisseurs de services webmail ne sont pas sécurisés et ne protègent donc pas la confidentialité de leurs usagers. Il va falloir changer les habitudes de quelques personnes si nous voulons discuter de ces témoignages en privé.</i></td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>

<h3><a name="Adopter_un_service_de_courriel_securise" title="Adopter un service de courriel sécurisé"></a>Adopter un service de courriel sécurisé</h3>

<p>&nbsp;</p>

<p>Très peu de fournisseurs de service webmail offrent l’accès SSL aux comptes de courriel. Yahoo et Hotmail, par exemple, offrent une connexion sécurisée <i>seulement</i> lorsque vous vous connectez (pour protéger votre mot de passe) mais vos messages, eux, sont envoyés et reçus de façon non sécurisée. De plus, Yahoo, Hotmail et d’autres fournisseurs de services gratuits intègrent <a href="glossaire#Adresse_IP" title="Adresse_IP"><i>l’adresse IP</i></a> de l’ordinateur que vous utilisez dans tous les messages que vous envoyez.</p>

<p>Les comptes Gmail, par contre, utilisent une connexion sécurisée à partir du moment où vous vous connectez jusqu'à ce que vous déconnectiez. Vous pouvez vérifier ceci dans la barre d'adresse, présentant une URL commençant par 'https', le 's' indiquant une connexion sécurisée. Contrairement à Yahoo et Hotmail, Gmail ne révèle pas votre adresse IP aux destinataires du message. Cela dit, il n’est pas recommandé de dépendre uniquement de Google si la confidentialité de vos communications est un enjeu important. Google balaye et enregistre le contenu des messages de ses usagers pour une variété de raisons et a déjà acquiescé aux requêtes de gouvernements reconnus pour imposer des limites aux droits numériques. Voir la section <a href="chapter_7_5" title="Chapitre 7.5"><i><b>Lecture complémentaire</b></i></a>, à la fin de ce chapitre, pour plus de renseignements à propos de la Charte de confidentialité de Google.</p>

<p>Si possible, vous devriez créer un nouveau compte de courriel <a href="glossaire#Riseup" title="Riseup"><i>Riseup</i></a> en visitant <a class="ext-link" href="https://mail.riseup.net"><span class="icon">https://mail.riseup.net</span></a>. Les administrateurs de Riseup offrent des services de courrier électronique à des centaines d’activistes de partout dans le monde et se font un point d’honneur de protéger rigoureusement les données qui sont stockées sur leurs serveurs. Depuis plusieurs années, les services offerts par le collectif Riseup constituent une solution fiable pour tous ceux qui souhaitent utiliser un courriel sécurisé. Contrairement à Google, ils ont des politiques très strictes concernant la confidentialité de leurs utilisateurs et n’ont aucun intérêt commercial qui pourrait éventuellement entrer en conflit avec ces politiques. Pour créer un compte Riseup, cependant, vous aurez besoin de deux «&nbsp;codes d’invitation&nbsp;». Ces codes peuvent vous être fournis par quiconque dispose déjà d’un compte Riseup. Si vous avez une copie reliée de ce livret, vous devriez également avoir reçu vos «&nbsp;codes d’invitation&nbsp;». Sinon, vous devrez trouver deux usagers Riseup et leur demander de vous faire parvenir des codes d’invitation.</p>

<p>&nbsp;</p>

<table cellpadding="5" cellspacing="0" style="border: 2pt dashed #008000; background-color: #e9e8a4">
	<tbody>
		<tr>
			<td><img align="middle" height="63" src="/sites/securitybkp.ngoinabox.org/files/u9/hand_web_trans.png" width="60" /> <b>Expérience pratique&nbsp;: se lancer avec le </b><a href="riseup_principale"><b>Guide pratique RiseUp</b></a></td>
		</tr>
	</tbody>
</table>

<p>Gmail et Riseup n’offrent pas seulement le service webmail. Les deux fournisseurs peuvent être utilisés avec un client de messagerie comme <a href="glossaire#Thunderbird" title="Thunderbird"><i>Mozilla Thunderbird</i></a>, qui permet le recours aux techniques présentées à la section <a href="chapter_7_4" title="Chapitre 7.4"><i><b>Principes de sécurité avancée</b></i></a>, ci-dessous. Il est tout aussi important de s’assurer que votre client de messagerie établisse une connexion chiffrée à votre fournisseur de service que de se connecter au webmail via <kbd>HTTPS</kbd>. Pour plus de renseignements sur les clients de messagerie, nous vous invitons à consulter le <a href="thunderbird_principale" title="Guide pratique Thunderbird"><i><b>Guide pratique Thunderbird</b></i></a>. À tout le moins, vous devriez activer la fonction de chiffrement SSL ou TLS pour vos serveurs entrant et sortant.</p>

<p>&nbsp;</p>

<table cellpadding="5" cellspacing="0" style="border: 2pt dashed #008000; background-color: #e9e8a4">
	<tbody>
		<tr>
			<td><i>Pablo&nbsp;: Alors, devrais-je créer un nouveau compte Riseup, ou bien continuer à utiliser Gmail, mais avec une adresse sécurisée 'https'&nbsp;? </i><br />
			<br />
			<i>Claudia&nbsp;: C’est ta décision, mais il y a un certain nombre d’éléments dont tu devrais tenir compte lorsque tu choisis un service de courriel régulier. Premièrement, est-ce que le fournisseur permet une connexion sécurisée à son serveur&nbsp;? Gmail le fait, donc ça va. Deuxièmement, fais-tu confiance aux administrateurs quant à la confidentialité de tes communications&nbsp;? Vont-ils lire tes messages ou en partager le contenu avec un tiers&nbsp;? C’est à toi d’évaluer les risques. Finalement, tu dois déterminer s’il est acceptable que tu sois associé à ce fournisseur. En d’autres termes, est-il possible que tu t’attires éventuellement des ennuis parce que tu as une adresse «&nbsp;riseup.net&nbsp;» (qui est reconnue pour être populaire auprès des activistes)&nbsp;? Devrais-tu plutôt, par souci de discrétion, te contenter d’une adresse «&nbsp;gmail.com&nbsp;»&nbsp;?</i></td>
		</tr>
	</tbody>
</table>

<p>D’une manière ou d’une autre, vous devez garder à l’esprit que chaque message a un expéditeur et au moins un destinataire. Vous, personnellement, n’êtes qu’un élément de l’équation. Même si vous accédez à votre compte de façon sécurisée, vous devez considérer les précautions que vos contacts prennent (ou ne prennent pas) lorsqu’ils envoient, lisent ou répondent à vos messages. Si possible, demandez à vos correspondants de vous indiquer où sont situés leurs fournisseurs de service de courriel. Certains pays sont plus agressifs que d’autres en ce qui concerne la surveillance des communications par courrier électronique. <b>Pour assurer la confidentialité de vos communications, vos correspondants et vous devriez tous utiliser des services sécurisés hébergés dans des pays relativement sûrs.</b> Si vous voulez être absolument certain que vos messages ne soient pas interceptés entre votre serveur de courriel et celui de votre correspondant, il serait pertinent que vous adoptiez tous deux des comptes courriels du même fournisseur. À cet égard, Riseup est un excellent choix.</p>

<p>&nbsp;</p>

<h3>Conseils supplémentaires pour améliorer la sécurité de vos correspondances par courriel</h3>

<p>&nbsp;</p>

<ul>
	<li>Soyez toujours prudent lorsque vous ouvrez des pièces jointes que vous n’attendiez pas, qui proviennent de personnes que vous ne connaissez pas ou dont la ligne d’objet est douteuse. Lorsque vous ouvrez des messages de ce type, vous devriez toujours, 1) vous assurer que votre programme antivirus soit actualisé et 2) rester particulièrement attentif aux avertissements lancés par votre navigateur ou votre programme de courriel.</li>
	<li>Vous devriez utiliser un programme de connexion anonyme, comme <a href="glossaire#Tor" title="Tor"><i>Tor</i></a>. Ce programme, abordé au chapitre <a href="chapter-8" title="Chapitre 8"><i><b>8. Préserver votre anonymat et contourner la censure sur Internet</b></i></a>, peut vous aider à cacher votre service de courriel à ceux qui pourraient être en train de surveiller votre connexion Internet. Selon le degré de filtrage des courriels qui prévaut dans votre pays, il vous sera peut-être nécessaire d’utiliser Tor, ou un autre des outils de <a href="glossaire#Contournement" title="Contournement"><i>contournement</i></a> décrits au <a href="chapter-8" title="Chapitre 8"><i><b>chapitre 8</b></i></a>, ne serait-ce que pour accéder à un fournisseur de services de courriel sécurisés comme Riseup ou Gmail.</li>
	<li>Au moment de créer un compte que vous avez l’intention d’utiliser anonymement (pour communiquer avec vos destinataires ou participer à des forums par courriel), faites attention à ne pas enregistrer un nom d’utilisateur ou un «&nbsp;Nom complet&nbsp;» qui se rapporte à votre vie personnelle ou professionnelle. Dans ces cas-là, il est également indiqué d’éviter les comptes Hotmail, Yahoo, ou tout autre fournisseur de webmail qui inclut automatiquement votre adresse IP dans les messages que vous envoyez.</li>
	<li>Compte tenu des personnes qui ont physiquement accès à votre ordinateur, le nettoyage régulier des fichiers temporaires liés à l’utilisation des services de courriel est tout aussi important que la protection des messages envoyés sur Internet. À ce sujet, voir le chapitre <a href="chapter-6" title="Chapitre 6"><i><b>6. Détruire définitivement des données sensibles</b></i></a> et le <a href="ccleaner_principale" title="Guide pratique CCleaner"><i><b>Guide pratique CCleaner</b></i></a>.</li>
	<li>Vous pouvez envisager d'utiliser plusieurs comptes de messagerie anonymes pour communiquer avec différents groupes de personnes et assurer ainsi la protection de votre réseau de contacts. Vous pouvez également utiliser d'autres comptes de messagerie pour vous inscrire à des services Internet exigeant une adresse électronique.</li>
	<li>Au-delà de toutes ces précautions, prenez garde à ce que vous écrivez dans vos emails et aux conséquences qu'ils pourraient avoir s'ils tombaient entre de mauvaises mains. Un moyen d'accroître la sécurité de tout échange de données consiste à créer un système de code réservé à l'échange de données sensibles et vous permettant de ne pas nommer les gens par leur propre nom, ni de citer des adresses réelles, etc.</li>
</ul>


