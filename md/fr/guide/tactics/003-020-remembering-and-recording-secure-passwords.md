

---

lang: fr
community: guide
type: tactics
legacy: True
child: True
weight: 2
depth: 3
title: Remembering and recording secure passwords

---

<p>À la lecture des recommandations énumérées ci-dessus, vous vous dites peut-être que seule une personne ayant une mémoire photographique pourrait se rappeler de plusieurs mots de passe aussi longs, complexes et inintelligibles sans les consigner par écrit. L’importance d’utiliser un mot de passe différent pour chaque compte complique encore les choses. Il existe toutefois quelques astuces qui pourront vous aider à créer des mots de passe faciles à mémoriser mais extrêmement difficiles à deviner, même pour une personne qui se sert d’un logiciel de «&nbsp;craquage de mots de passe&nbsp;». Vous pouvez aussi enregistrer vos mots de passe en utilisant une <a href="glossaire#BD_de_mots_de_passe_securises" title="BD_de_mots_de_passe_securises"><i>base de données de mots de passe sécurisée</i></a>, comme <a href="glossaire#Keepass" title="Keepass"><i>KeePass</i></a>.</p>

<p>&nbsp;</p>

<h3>Mémoriser des mots de passe sûrs</h3>

<p>&nbsp;</p>

<p>Il est important d’utiliser plusieurs types de caractères pour composer un nouveau mot de passe. Par exemple&nbsp;:</p>

<ul>
	<li>Combinez des minuscules et des majuscules&nbsp;: 'My naME is Not MR. MarSter'</li>
	<li>Faites alterner des lettres et des chiffes&nbsp;: 'a11 w0Rk 4nD N0 p14Y'</li>
	<li>Incluez des symboles ou des signes de ponctuation&nbsp;: 'c@t(heR1nthery3'</li>
	<li>Combinez des mots empruntés à plusieurs langues&nbsp;: 'Let Them Eat 1e gateaU du ch()colaT'</li>
</ul>

<p>Toutes ces méthodes contribuent à augmenter le niveau de complexité d’un mot de passe. Elles vous permettent de choisir des mots de passe sûrs sans pour autant abandonner l’idée de les mémoriser. Même si certaines des substitutions les plus courantes (comme l’utilisation du zéro au lieu du 'o', ou celle du '@' au lieu du 'a') sont depuis longtemps incorporées aux outils qu’emploient les pirates pour craquer les mots de passe, il est toujours utile d’y recourir. Ces substitutions simples augmentent considérablement le temps requis par un programme pour deviner un mot de passe et, dans la plupart des situations où il n’est tout simplement pas possible d’utiliser de tels outils, elles font en sorte qu’il est très difficile pour un humain de deviner la bonne combinaison.</p>

<p>Vous pouvez aussi employer des <a href="glossaire#Procede_mnemonique" title="Procede_mnemonique"><i>procédés mnémoniques</i></a> plus traditionnels, comme des acronymes. Cela vous permet de transformer de longues phrases en séquences de caractères complexes et, à première vue, aléatoires&nbsp;:</p>

<ul>
	<li>'To be or not to be? That is the question' devient '2Bon2B?TitQ'</li>
	<li>'We hold these truths to be self-evident: that all men are created equal' devient 'WhtT2bs-e:taMac='</li>
	<li>'Are you happy today?' devient 'rU:-)2d@y?'</li>
</ul>

<p>Nous vous présentons ces quelques exemples pour vous aider à trouver votre propre méthode de combinaison de mots et de phrases à la fois complexes et facile à mémoriser.</p>

<p>Le petit effort à fournir pour rendre le mot de passe plus complexe revêt une très grande utilité. Le fait d'augmenter la longueur du mot de seulement quelques caractères ou d'y ajouter des chiffres ou des caractères spéciaux peut rendre celui-ci beaucoup plus difficile à cracker. En guise de démonstration, le tableau ci-dessous expose le temps nécessité par un hacker pour cracker un mot de passe selon sa complexité - en allant du mot le plus simple au plus complexe.</p>

<table border="1">
	<tbody>
		<tr>
			<th>Exemples de mot de passe</th>
			<th>Temps de crackage avec un ordinateur basique</th>
			<th>Temps de crackage avec un ordinateur très performant</th>
		</tr>
		<tr>
			<td>bananas</td>
			<td>Moins d’une journée</td>
			<td>Moins d’une journée</td>
		</tr>
		<tr>
			<td>bananalemonade</td>
			<td>2 jours</td>
			<td>Moins d’une journée</td>
		</tr>
		<tr>
			<td>BananaLemonade</td>
			<td>3 mois, 14 jours</td>
			<td>Moins d’une journée</td>
		</tr>
		<tr>
			<td>B4n4n4L3m0n4d3</td>
			<td>3 siècles, 4 décennies</td>
			<td>1 mois, 26 jours</td>
		</tr>
		<tr>
			<td>We Have No Bananas</td>
			<td>19151466 siècles</td>
			<td>3990 siècles</td>
		</tr>
		<tr>
			<td>W3 H4v3 N0 B4n4n45</td>
			<td>20210213722742 siècles</td>
			<td>4210461192 siècles</td>
		</tr>
	</tbody>
</table>

<p>Bien sûr, le temps nécessité pour cracker l'un des mots de passe présentés ci-dessus variera considérablement selon la nature de l'attaque et les ressources dont l'attaquant dispose. En outre, de nouvelles méthodes de crackage de mots de passe sont constamment en cours d'élaboration. Toutefois, le tableau démontre bien qu'il suffit de varier les caractères et d'utiliser deux mots, ou mieux encore une phrase courte, pour rendre la tâche du hacker d'autant plus difficile.</p>

<p>Le tableau ci-dessus est basé sur des calculations <a href="https://passfault.appspot.com/password_strength.html" title="Passfault">Passfault</a>. Passfault fait partie d'un certain nombre de sites vous permettant de tester la force de vos mots de passe. De tels sites offrent certes de précieuses informations quant à l'efficacité relative des différents types de mots de passe, il est toutefois conseillé de ne pas y entrer votre mot de passe actuel.</p>

<p>&nbsp;</p>

<h3>Enregistrer des mots de passe de façon sécurisée</h3>

<p>&nbsp;</p>

<p>Même si un minimum d’inventivité peu vous aider à mémoriser tous vos mots de passe, la nécessité de modifier vos mots de passe régulièrement peut vite venir à bout de votre créativité. Comme solution de rechange, vous pouvez utiliser un programme pour générer automatiquement des mots de passe complexes et abandonner complètement l’idée de les mémoriser. Vous pouvez sauvegarder ces mots de passe aléatoires dans une base de données de mots de passe sécurisée, chiffrée et portable. C’est ce que propose le programme KeePass.</p>

<p>&nbsp;</p>

<table cellpadding="5" cellspacing="0" style="border: 2pt dashed #008000; background-color: #e9e8a4">
	<tbody>
		<tr>
			<td><img align="middle" height="63" src="/sites/securitybkp.ngoinabox.org/files/u9/hand_web_trans.png" width="60" /> <b>Expérience pratique&nbsp;: se lancer avec le </b><i><a href="keepass_principale"><b>Guide pratique KeePass</b></a></i></td>
		</tr>
	</tbody>
</table>

<p>Évidemment, si vous privilégiez cette méthode, il est particulièrement important que vous créiez une phrase secrète sûre pour KeePass ou tout autre programme employé à cet effet. Chaque fois que vous devez saisir un mot de passe pour un compte ou un service donné, vous pouvez le récupérer à l’aide de votre phrase secrète principale, ce qui facilite le recours à toutes les suggestions mentionnées ci-dessus. KeePass est portable, ce qui signifie que vous pouvez déposer la base de données sur une clé USB au cas où vous auriez besoin de rechercher un ou plusieurs mots de passe lorsque vous êtes loin de votre ordinateur principal.</p>

<p>Même s’il s’agit probablement de la meilleure option pour une personne qui dispose de plusieurs comptes différents, cette méthode comporte quelques désavantages. Premièrement, si vous perdez ou supprimez malencontreusement la seule et unique copie de votre base de données de mots de passe, vous ne pourrez plus accéder aux comptes dont le mot de passe y était stocké. C’est pourquoi il est de toute première importance que vous conserviez une copie de sauvegarde de votre base de données KeePass. Consultez attentivement le chapitre <a href="chapter-5" title="Chapitre 5"><i><b>5. Récupérer des données perdues</b></i></a> pour plus de conseils sur la création de copies de sauvegarde. Heureusement, le fait que votre base de données soit chiffrée signifie que vous n’avez pas à paniquer si vous perdez une clé USB ou un disque de sauvegarde où vous l’aviez stockée.</p>

<p>Le deuxième inconvénient majeur peut s’avérer encore plus grave. Si vous oubliez votre phrase secrète principale pour KeePass, il n’existe aucun moyen pour récupérer le contenu de la base de mots de passe. Il est donc capital que vous choisissiez une phrase secrète principale aussi sûre que facile à mémoriser&nbsp;!</p>

<p>Dans certaines situations, la force de cette méthode peut en devenir la faiblesse. Si quelqu'un vous force à donner votre phrase secrète principale pour KeePass, il aura accès à tous les mots de passe stockés dans cette base de données. S'il s'agit d'une situation à laquelle vous puissiez être confronté, considérez la base de données KeePass comme un fichier sensible et veillez à sa protection comme décrit dans le chapitre <a href="https://securityinabox.org/fr/chapter-4" title="Chapitre 4"><i><b>4. Protéger les données sensibles stockées sur votre ordinateur</b></i></a>. Vous pouvez également créer une base de données KeePass séparée, destinée à contenir les mots de passe protégeant des informations plus sensibles - et prenez des précautions supplémentaires pour cette base de données.</p>

<p>&nbsp;</p>

<table cellpadding="5" cellspacing="0" style="border: 2pt dashed #008000; background-color: #e9e8a4">
	<tbody>
		<tr>
			<td><i>Mansour&nbsp;: Attends un peu. Si KeePass utilise un seul et unique mot de passe pour protéger tous les autres mots de passe, comment cela est-il plus sûr que d’utiliser le même mot de passe pour tous les comptes&nbsp;? Si un type mal intentionné parvient à dénicher ton mot de passe principal, il pourra accéder à toutes tes données, non&nbsp;? </i><br />
			<br />
			<i>Magda&nbsp;: C’est une bonne question, et c’est vrai qu’il est extrêmement important de protéger la phrase secrète, c.-à-d. le mot de passe principal. Mais il y a quand même quelques différences importantes entre les deux méthodes que tu compares. Premièrement, le «&nbsp;type mal intentionné&nbsp;» en question n’aurais pas seulement besoin du mot de passe principal, il faudrait aussi qu’il ait accès à la base de données KeePass correspondante. Par contre, si tu n’utilises qu’un seul mot de passe pour tous tes comptes, le type n’aurait besoin que de ce mot de passe unique pour accéder à toutes tes données. Par ailleurs, nous savons que KeePass est un programme extrêmement sûr, pas vrai&nbsp;? Et bien, on ne peut pas en dire autant de plusieurs programmes et sites Internet. Certains sont beaucoup moins sûrs que d’autres et tu ne voudrais surtout pas que quelqu’un parvienne à se connecter à un site faible et utilise ensuite ce qu’il y a appris pour accéder à des comptes mieux sécurisés. Et il y a un dernier point. Il est très facile, dans KeePass, de changer ton mot de passe principal si tu juges que c’est nécessaire. Je n’ai pas eu cette chance&nbsp;! J’ai dû passer la journée au complet à modifier chacun de mes mots de passe.</i></td>
		</tr>
	</tbody>
</table>


