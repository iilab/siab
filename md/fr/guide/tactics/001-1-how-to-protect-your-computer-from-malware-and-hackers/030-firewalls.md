

---

lang: fr
community: guide
type: tactics
legacy: True
child: True
weight: 3
depth: 3
title: Firewalls

---

<p>Un pare-feu est un programme conçu pour contrôler les données entrantes depuis l’Internet. C’est aussi le pare-feu qui contrôle en dernier lieu les données sortantes. Un peu comme un garde de sécurité posté en permanence à la porte d’un immeuble pour décider qui peut y entrer et en sortir, un pare-feu reçoit et examine toutes les données entrantes et sortantes et décide des mesures à prendre selon le résultat de ses inspections. Évidemment, il est essentiel que vous défendiez votre système contre les connexions suspectes provenant d’Internet ou des réseaux locaux, puisque ce sont deux points d’accès possibles à votre ordinateur pour les virus et les pirates. La surveillance des connexions sortantes (à partir de votre ordinateur) est elle aussi très importante.</p>

<p>Un bon pare-feu vous permet de définir des permissions d’accès pour chacun des programmes installés sur votre ordinateur. Lorsqu’un de ces programmes tente d’établir une connexion avec l’extérieur, le pare-feu bloque automatiquement la connexion et vous soumet un avertissement, à moins qu’il ne reconnaisse le programme et soit en mesure de confirmer que vous avez déjà défini une permission pour ce type de connexion. Cela sert principalement à empêcher des <a href="glossaire#Logiciel_malveillant" title="Logiciel_malveillant"><i>logiciels malveillants</i></a> existants de répandre des virus ou d’inviter des <a href="glossaire#Hacker" title="Hacker">pirates</a> à envahir votre ordinateur. À cet égard, un bon pare-feu offre à la fois une seconde ligne de défense et un système d’alarme efficace pour vous signaler toute menace à l’intégrité et la sécurité de votre ordinateur.</p>

<p>&nbsp;</p>

<h3>Les logiciels pare-feu</h3>

<p>&nbsp;</p>

<p>Les dernières versions de Microsoft Windows incluent un pare-feu intégré qui est désormais activé automatiquement. Malheureusement, le pare-feu Windows comporte plusieurs limites. Par exemple, il n’inspecte pas les connexions sortantes. Cependant, il existe un excellent <a href="glossaire#Gratuiciel" title="Gratuiciel"><i>gratuiciel</i></a> appelé <a href="glossaire#Comodo" title="Comodo"><i>Comodo Personal Firewall</i></a>, qui peut sécuriser encore plus efficacement votre ordinateur.</p>

<p>&nbsp;</p>

<table cellpadding="5" cellspacing="0" style="border: 2pt dashed #008000; background-color: #e9e8a4">
	<tbody>
		<tr>
			<td><img align="middle" height="63" src="/sites/securitybkp.ngoinabox.org/files/u9/hand_web_trans.png" width="60" /> <b>Expérience pratique&nbsp;: se lancer avec le </b><i><a href="comodo_principale"><b>Guide pratique Comodo Firewall</b></a></i></td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>

<h3>Prévenir les connexions réseau suspectes</h3>

<p>&nbsp;</p>

<ul>
	<li>Installez uniquement les programmes essentiels sur l’ordinateur que vous utilisez pour effectuer des tâches délicates. Assurez-vous d’obtenir ces programmes de sources fiables. Désinstallez tous les logiciels que vous n’utilisez pas.</li>
	<li>Déconnectez votre ordinateur d’Internet lorsque vous ne l’utilisez pas et éteignez-le complètement pendant la nuit.</li>
	<li>Ne révélez votre mot de passe Windows à personne.</li>
	<li>Si certains services Windows que vous n’utilisez plus sont toujours activés, vous devriez les désactiver. À ce propos, veuillez consulter la section <a href="chapter_1_5"><i><b>Lecture complémentaire</b></i></a>, à la fin de ce chapitre.</li>
	<li>Assurez-vous que tous les ordinateurs branchés au réseau local de votre bureau disposent d’un pare-feu actif.</li>
	<li>Si vous n’en avez pas déjà un, vous devriez envisager d’installer un pare-feu supplémentaire pour protéger l’ensemble du réseau local au bureau. Plusieurs <a href="glossaire#Routeur" title="Routeur"><i>passerelles</i></a> commerciales à large bande incluent un pare-feu facile d’utilisation. L’activation de cet outil peut grandement améliorer la sécurité de votre réseau local. Si vous ne savez pas trop par où commencer, vous pouvez toujours demander de l’aide à la personne qui a mis le réseau en place initialement.</li>
</ul>

<p>&nbsp;</p>

<table cellpadding="5" cellspacing="0" style="border: 2pt dashed #008000; background-color: #e9e8a4">
	<tbody>
		<tr>
			<td><i>Assani&nbsp;: Alors, tu voudrais que j’installe un antivirus, un programme anti-mouchards et un pare-feu&nbsp;? Est-ce que mon ordinateur peut supporter tout ça&nbsp;?</i><br />
			<br />
			<i>Muhindo&nbsp;: Absolument. En fait, de nos jours, ces trois outils constituent le strict minimum si tu souhaites sécuriser ton ordinateur. Comme ces trois programmes sont conçus pour fonctionner ensemble, il ne devrait pas y avoir de problème. N’oublie pas cependant que tu ne dois jamais faire fonctionner simultanément deux antivirus ou deux pare-feu.</i></td>
		</tr>
	</tbody>
</table>


