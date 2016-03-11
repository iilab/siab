

---

lang: fr
community: guide
type: tactics
legacy: True
child: False
weight: 007
title: 7. How to keep your Internet communication private

---

<p>L’aspect pratique, le rapport coût-efficacité et la flexibilité des services de courriel et de messagerie instantanée en font des instruments extrêmement précieux pour les individus et organismes qui disposent d’un accès, ne serait-ce que limité, à Internet. Pour ceux dont la connexion est plus rapide et plus stable, des outils comme <a href="https://jitsi.org/" title="Jitsi"><i>Jitsi</i></a>, <a href="glossaire#Skype" title="Skype"><i>Skype</i></a> ou d’autres programmes de <i>voix sur réseau IP</i> (<a href="glossaire#VoIP" title="VoIP"><i>VoIP</i></a>) présentent les mêmes caractéristiques avantageuses. Malheureusement, en ce qui a trait à la confidentialité, ces solutions numériques ne sont pas toujours fiables. Bien sûr, il n’y a là rien de nouveau. Le courrier postal, le téléphone et les messages texte sont des moyens de communication tout aussi vulnérables, particulièrement quand ils sont utilisés par des personnes que les autorités ont choisi de surveiller pour une raison ou une autre.</p>

<p>Une différence importante entre les moyens de communication traditionnels et les méthodes numériques propres à Internet est que ces dernières permettent à l’utilisateur de déterminer lui-même le niveau de sécurité qu’il juge approprié. Si vous envoyez des courriels et des messages instantanés ou participez à des conversations VoIP par voies non sécurisées, ces communications seront presque certainement moins confidentielles qu’une lettre écrite ou qu’un appel téléphonique traditionnel. C’est qu’il est relativement facile, à l’aide de puissants ordinateurs, d’exécuter des recherches automatiques à travers une somme colossale de données afin d’identifier des expéditeurs, des destinataires et certains mots-clé particuliers. Lorsqu’il est question de surveiller les voies de communications traditionnelles, il faut habituellement mobiliser beaucoup plus de ressources pour atteindre un degré d’efficacité similaire. Cela dit, il est possible de contourner ces mesures de contrôle en mettant en place certaines précautions élémentaires. La flexibilité des communications par Internet et la force des nouveaux procédés de <a href="glossaire#Chiffrement" title="Chiffrement"><i>chiffrement</i></a> peuvent désormais assurer un niveau de confidentialité qui était autrefois exclusivement réservé aux forces armées et services de renseignements.</p>

<p>En suivant attentivement les recommandations avancées dans ce chapitre et en explorant le potentiel des logiciels qui y sont présentés, vous serez en mesure d’améliorer considérablement la sécurité de vos communications numériques. Le service de courriel <a href="glossaire#Riseup" title="Riseup"><i>Riseup</i></a>, le module complémentaire <a href="glossaire#OTR" title="OTR"><i>OTR</i></a> du programme de messagerie instantanée <a href="glossaire#Pidgin" title="Pidgin"><i>Pidgin</i></a>, <a href="glossaire#Firefox" title="Firefox"><i>Mozilla Firefox</i></a> et le module complémentaire <a href="glossaire#Enigmail" title="Enigmail"><i>Enigmail</i></a> du client de messagerie <a href="glossaire#Thunderbird" title="Thunderbird"><i>Mozilla Thunderbird</i></a> sont tous d’excellents outils. Vous devriez toutefois garder à l’esprit que la confidentialité d’une conversation numérique n’est jamais garantie à cent pour cent. Il subsiste toujours une menace qui nous a échappée, que ce soit un <a href="glossaire#Keylogger" title="Keylogger"><i>enregistreur de frappe</i></a> installé à votre insu sur votre ordinateur, une personne qui écoute aux portes, un correspondant imprudent ou quoi que ce soit d’autre.</p>

<p>L’objectif de ce chapitre est de vous aider à vous protéger contre ces menaces, autant que possible. Nous n’avons pas l’intention de minimiser l’importance de ces dangers, mais nous ne voulons pas non plus faire valoir la position extrême, défendue par certains, selon laquelle aucune information ne devrait être communiquée par Internet à moins que l’on soit disposé à la rendre tout à fait publique.</p>

<p>&nbsp;</p>

<h3>Scénario de départ</h3>

<p>&nbsp;</p>

<p>&nbsp;</p>

<table cellpadding="5" cellspacing="0" style="border: 2pt dashed #008000; background-color: #e9e8a4">
	<tbody>
		<tr>
			<td><i>Claudia et Pablo sont employés par une ONG dans un pays sud-américain. Après avoir passé plusieurs mois à compiler les dépositions de nombreux témoins de violations de droits humains commises par l’armée dans leur région, Claudia et Pablo ont entrepris des démarches pour protéger ces données importantes. Ils ont gardé uniquement les renseignements dont ils avaient vraiment besoin, qu’ils ont stockés immédiatement dans un volume TrueCrypt. Ils ont ensuite créé des copies de sauvegarde de ce volume, qu’ils gardent à plusieurs emplacements physiques. En préparant la publication d’un rapport préliminaire, où ils exposeront certains aspects des témoignages recueillis, ils se sont rendus compte qu’ils doivent discuter d’enjeux sensibles avec un collègue qui se trouve à l’étranger. Même s’ils se sont entendus pour ne révéler aucun nom de personnes ou de lieux, ils veulent s’assurer que leurs échanges par courriel et messagerie instantanée resteront tout à fait confidentiels. Claudia a organisé une rencontre pour aborder l’importance de la sécurité des communications et veut savoir si ses collègues ont des questions à ce sujet.</i></td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>

<h3>Qu’apprendrez vous dans ce chapitre</h3>

<p>&nbsp;</p>

<ul>
	<li>Pourquoi la plupart des services de courriel et de messagerie instantanée ne sont pas sécurisés&nbsp;;</li>
	<li>Comment créer un compte de courriel plus sûr&nbsp;;</li>
	<li>Comment augmenter le niveau de sécurité de votre compte de courriel&nbsp;;</li>
	<li>Comment utiliser un service sécurisé de messagerie instantanée&nbsp;;</li>
	<li>Que faire si vous avez de bonnes raisons de croire que quelqu’un accède à votre courrier électronique&nbsp;;</li>
	<li>Comment authentifier l’identité d’un correspondant.</li>
</ul>

<p>&nbsp;</p>


