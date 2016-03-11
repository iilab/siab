

---

lang: fr
community: guide
type: tactics
legacy: True
child: True
weight: 4
depth: 3
title: Advanced Email Security

---

<p>Les outils et concepts présentés ci-dessous sont recommandés aux utilisateurs expérimentés.</p>

<p>&nbsp;</p>

<h3>Utiliser le chiffrement asymétrique pour vos courriels</h3>

<p>&nbsp;</p>

<p>Il est possible d’améliorer davantage le niveau de confidentialité de vos communications par courriel, et ce, même en employant un compte de courriel non sécurisé. Pour ce faire, vous devrez apprendre à utiliser le <a href="glossaire#Chiffrement" title="Chiffrement"><i>chiffrement</i></a> asymétrique. Cette technique permet de chiffrer un message individuellement de telle sorte que seul le destinataire visé puisse le lire. L’aspect ingénieux du chiffrement asymétrique est que vous n’êtes pas obligé d’échanger des renseignements secrets avec vos correspondants pour leur indiquer comment vous coderez vos messages à l’avenir.</p>

<p>&nbsp;</p>

<table cellpadding="5" cellspacing="0" style="border: 2pt dashed #008000; background-color: #e9e8a4">
	<tbody>
		<tr>
			<td><i>Pablo&nbsp;: Mais comment ça fonctionne&nbsp;? </i><br />
			<br />
			<i>Claudia&nbsp;: Avec des mathématiques sophistiquées&nbsp;! Tu dois encoder les messages que tu envoies à un correspondant en particulier à l’aide de sa «&nbsp;clé publique&nbsp;», qu’il t’a préalablement fait parvenir et qu’il est libre de partager avec n’importe qui. Ensuite, cette personne utilise sa «&nbsp;clé privée&nbsp;», dont elle garde rigoureusement le secret, pour décoder les messages. En retour, ton correspondant utilise ta clé publique pour chiffrer les messages qu’il t’envoie. Au bout du compte, vous devez échanger vos clés publiques, mais vous n’avez pas à vous inquiéter qu’elles soient interceptées, puisqu’une clé publique, sans la clé privée correspondante, est parfaitement inutile.</i></td>
		</tr>
	</tbody>
</table>

<p>Cette technique peut être employée avec n’importe quel service de courriel, même ceux qui n’offrent pas de connexion sécurisée, parce que les messages sont chiffrés avant même de quitter votre ordinateur. N’oubliez pas, toutefois, que l’utilisation de procédés de chiffrement pourrait attirer sur vous une attention non désirée. Le type de chiffrement employé pour accéder à un site Internet sécurisé ou à un compte webmail attire habituellement moins de suspicion que le chiffrement asymétrique abordé dans cette section. Dans certaines circonstances, si un message contenant des données chiffrées de cette manière est intercepté ou publié sur un forum public, il pourrait incriminer la personne qui l’a envoyé, et ce, même si le message lui-même ne contient rien d’incriminant. Il faut parfois choisir entre la confidentialité de vos messages et l’importance de passer inaperçu.</p>

<p>&nbsp;</p>

<h3><a name="Chiffrer_et_authentifier_des_messages_individuellement" title="Chiffrer et authentifier des messages individuellement"></a>Chiffrer et authentifier des messages individuellement</h3>

<p>&nbsp;</p>

<p>Le chiffrement asymétrique peut sembler complexe de prime abord, mais le procédé est relativement simple, pourvu que vous en saisissiez les principes élémentaires. Par ailleurs, les outils sont très faciles à utiliser. Le client de messagerie <a href="glossaire#Thunderbird" title="Thunderbird"><i>Mozilla Thunderbird</i></a> peut être utilisé avec un module complémentaire appelé <a href="glossaire#Enigmail" title="Enigmail"><i>Enigmail</i></a> pour chiffrer et déchiffrer des messages en un tournemain.</p>

<p>&nbsp;</p>

<table cellpadding="5" cellspacing="0" style="border: 2pt dashed #008000; background-color: #e9e8a4">
	<tbody>
		<tr>
			<td><img align="middle" height="63" src="/sites/securitybkp.ngoinabox.org/files/u9/hand_web_trans.png" width="60" /> <b>Expérience pratique&nbsp;: se lancer avec le </b><i><a href="thunderbird_principale"><b>Guide pratique Thunderbird</b></a></i></td>
		</tr>
	</tbody>
</table>


<p>L'authenticité de vos courriels est un autre aspect important de la sécurité des communications. Quiconque dispose d’un accès Internet et des bons programmes peut usurper votre identité en envoyant des messages à partir d’une fausse adresse identique à la vôtre. On comprend mieux ce danger lorsqu’on le considère depuis la perspective de vos destinataires. Imaginez, par exemple, la menace posée par un message qui semble provenir d’une source fiable mais qui en réalité est émis par un tiers dont l’intention est de perturber vos activité ou d’obtenir des renseignements sensibles à propos de votre organisme.</p>

<p>Puisqu’il est impossible de voir ou d’entendre nos correspondants par courriel, nous nous fions habituellement à l’adresse de l’expéditeur pour vérifier son identité. C’est pourquoi l’on peut facilement se laisser berner par de fausses adresses. Les <a href="glossaire#Signature_numerique" title="Signature_numerique"><i>signatures numériques</i></a>, qui reposent elles aussi sur un procédé de chiffrement asymétrique, offrent un moyen plus sûr de vérifier l’identité d’un correspondant lorsque vous recevez ou envoyez des messages. La section <a href="thunderbird_utiliserenigmail" title="Comment utiliser Enigmail avec Thunderbird"><i><b>Comment utiliser Enigmail avec Thunderbird</b></i></a> du</p>

<table cellpadding="5" cellspacing="0" style="border: 2pt dashed #008000; background-color: #e9e8a4">
	<tbody>
		<tr>
			<td><i>Pablo&nbsp;: J’ai un collègue qui a déjà reçu un courriel de moi que je ne lui avais jamais envoyé. Nous avons déterminé que c’était probablement un pourriel, mais je me rends bien compte maintenant des problèmes qui pourraient survenir si un faux courriel aboutissait dans la corbeille d’arrivée de la mauvaise personne, au mauvais moment. J’ai lu quelque part qu’il est possible d’éviter ce genre de situation en recourant aux signatures numériques. Mais de quoi s’agit-il&nbsp;? </i><br />
			<br />
			<i>Claudia&nbsp;: Une signature numérique est un peu comme un cachet de cire que l’on utilise pour sceller une enveloppe contenant une lettre importante. Il est impossible de contrefaire une telle signature. Elle prouve que tu es bel et bien l’expéditeur du message et que celui-ci n’a pas été intercepté ni falsifié en chemin.</i></td>
		</tr>
	</tbody>
</table>


