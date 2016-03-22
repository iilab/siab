

---

lang: fr
community: guide
type: tactics
legacy: True
child: False
weight: 008
title:  8. How to remain anonymous and bypass censorship on the Internet

---

<p>Plusieurs gouvernements nationaux, un peu partout sur la planète, ont choisi d’installer des programmes spéciaux pour empêcher les internautes de leurs pays respectifs d’accéder à certains sites et services Internet. Des sociétés privées, des écoles et des bibliothèques publiques emploient des logiciels similaires pour protéger leurs employés, étudiants et clients contre des contenus jugés dérangeants ou nocifs. Ces technologies de filtrage se présentent sous diverses formes. Certains filtres bloquent des sites par leur <a href="glossaire#Adresse_IP" title="Adresse_IP"><i>adresse IP</i></a>, alors que d’autres dressent des «&nbsp;<a href="glossaire#Liste_noire" title="Liste_noire"><i>listes noires</i></a>&nbsp;» de <a href="glossaire#Nom_de_domaine" title="Nom_de_domaine"><i>noms de domaine</i></a> ou effectuent des recherches à travers l’ensemble des communications non chiffrées sur Internet pour y détecter certains mots-clé particuliers.</p>

<p>D’une manière ou d’une autre, il est quasiment toujours possible de contourner ces méthodes de filtrage en utilisant des ordinateurs intermédiaires, à l’extérieur de votre pays, pour accéder aux services qui vous sont interdits. Ce procédé est souvent appelé «&nbsp;contournement de la censure&nbsp;», ou tout simplement <a href="glossaire#Contournement" title="Contournement"><i> contournement</i></a>, et les ordinateurs intermédiaires sont appelés «&nbsp;<a href="glossaire#Proxy" title="Proxy"><i>mandataires</i></a>&nbsp;» ou «&nbsp;proxys&nbsp;». (N.D.T. Dans ce chapitre nous utiliserons plutôt le terme <a href="glossaire#Proxy" title="Proxy"><i>proxy</i></a>, puisque les spécialistes et les logiciels spécialisés tendent à utiliser davantage ce mot que l’équivalent français.) Les ordinateurs ou serveurs proxys, eux aussi, peuvent prendre plusieurs formes. Ce chapitre comporte une brève présentation des réseaux de connexion anonyme par proxys multiples, suivie d’une description plus détaillée des méthodes de contournement par proxy unique et de leur fonctionnement.</p>

<p>Ces deux méthodes constituent des moyens efficaces de contournement des filtres sur Internet, bien que le premier soit davantage approprié que le second, si vous êtes toutefois disposé à sacrifier la vitesse de connexion pour assurer que vos activités sur Internet restent tout à fait confidentielles. Si vous connaissez bien l’individu ou l’organisme qui gère votre serveur proxy et que vous lui faites confiance, ou si la performance vous importe plus que l’anonymat, le contournement par serveur proxy unique vous conviendra sans doute.</p>

<p>&nbsp;</p>

<h3>Scénario de départ</h3>

<p>&nbsp;</p>

<p>&nbsp;</p>

<table cellpadding="5" cellspacing="0" style="border: 2pt dashed #008000; background-color: #e9e8a4">
	<tbody>
		<tr>
			<td><i>Mansour et Magda sont frère et soeur. Ils habitent un pays arabophone où ils gèrent ensemble un blog pour dénoncer diverses violations de droits humains et faire campagne en faveur de changements politiques. Jusqu’à présent, les autorités de leur pays n’ont pas réussi à fermer leur site parce que ce dernier est hébergé dans un autre pays. Par contre le gouvernement a à plusieurs reprises tenté d’apprendre l’identité des administrateurs du blog en interrogeant d’autres activistes. Mansour et Magda craignent que les autorités parviennent à découvrir leur identité en contrôlant les mises à jour apportées au site. De plus, ils veulent se préparer à l’éventualité où le gouvernement parviendrait à filtrer leur site, pas uniquement pour être en mesure de continuer à l’actualiser régulièrement, mais aussi pour offrir de bons conseils de contournement aux lecteurs qui se trouvent dans leur pays et qui, autrement, perdraient complètement accès au blog.</i></td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>

<h3>Qu’apprendrez-vous dans ce chapitre</h3>

<p>&nbsp;</p>

<ul>
	<li>Comment accéder à un site Internet qui est bloqué dans votre pays&nbsp;;</li>
	<li>Comment empêcher que les sites que vous visitez puissent servir à déterminer votre position&nbsp;;</li>
	<li>Comment vous assurer que ni votre <a href="glossaire#FSI" title="FSI"><i>FSI</i></a> ni aucun organisme de surveillance implanté dans votre pays ne soit en mesure de déterminer quels sites Internet vous visitez et quels services vous utilisez.</li>
</ul>

<p>&nbsp;</p>


