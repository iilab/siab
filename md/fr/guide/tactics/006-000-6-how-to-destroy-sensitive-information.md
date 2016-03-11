

---

lang: fr
community: guide
type: tactics
legacy: True
child: False
weight: 006
title: 6. How to destroy sensitive information

---

<p>Dans les chapitres précédents, nous avons présenté un certain nombre de programmes et de pratiques exemplaires qui vous aideront à protéger vos données de nature délicate. Mais qu’arrive-t-il lorsque vous décidez de vous débarrasser de données dont vous n’avez plus besoin&nbsp;? Si vous décidez, par exemple, que la copie de sauvegarde chiffrée d’un fichier donné constitue une garantie suffisante et que vous voulez supprimer l’original, quel est le meilleur moyen de procéder&nbsp;? Malheureusement, la réponse est plus compliquée que l’on croit. Lorsqu’on supprime un fichier, même après avoir vider la <kbd>Corbeille</kbd>, le contenu de ce fichier reste intact quelque part sur le disque dur et peut être récupéré, avec les outils appropriés et un peu de chance, par n’importe qui.</p>

<p>Pour vous assurer que vos données supprimées n’aboutissent pas dans les mains de personnes mal intentionnées, vous devrez avoir recours à un logiciel spécial pour effacer vos données de façon sécurisée et définitive. <a href="glossaire#Eraser" title="Eraser"><i>Eraser</i></a>, abordé plus en détails ci-dessous, est l’un de ces programmes. On peut comparer Eraser à une déchiqueteuse&nbsp;: on l’emploie pour détruire complètement un document au lieu de le jeter à la corbeille en espérant que personne ne le trouve. Évidemment, la suppression de fichiers n’est qu’un exemple de situations où vous devriez détruire des renseignements de nature délicate. En réfléchissant bien aux types de renseignements qu’une personne (à plus forte raison une personne puissante et mue par des intérêts politiques) pourraient apprendre à votre sujet ou à propos de votre organisme en lisant certains fichiers que vous croyiez avoir supprimés, d’autres exemples de situations vous viendront sûrement à l’esprit, comme&nbsp;: la destruction de copies de sauvegarde, le <a href="glossaire#Wiping" title="Wiping"><i>nettoyage (wiping)</i></a> de vieux disques durs, la suppression de vieux comptes d’utilisateur, la suppression de votre historique de navigation, etc. <a href="glossaire#CCleaner" title="CCleaner"><i>CCleaner</i></a>, l’autre programme abordé dans ce chapitre, vous aidera à faire face au défi que pose la suppression des innombrables fichiers temporaires accumulés sur votre ordinateur par le système d’exploitation et les programmes que vous utilisez régulièrement.</p>

<p>&nbsp;</p>

<h3>Scénario de départ</h3>

<p>&nbsp;</p>

<p>&nbsp;</p>

<table cellpadding="5" cellspacing="0" style="border: 2pt dashed #008000; background-color: #e9e8a4">
	<tbody>
		<tr>
			<td><i>Elena est une militante environnementaliste, résidente d’un pays russophone, qui gère un site Internet de plus en plus populaire où elle dénonce l’étendue du problème que pose la déforestation illégale dans sa région. Elle a créé des copies de sauvegarde des données utilisées pour monter le site, et elle en garde au moins une à son domicile, une au bureau et une troisième sur son nouvel ordinateur portable. Récemment, elle a également commencé à conserver une copie du journal de connexion au serveur et de la base de données contenant les contributions au forum de discussion de son site. Bientôt, Elena doit se rendre à l’étranger pour assister à une grande conférence réunissant des environnementalistes de plusieurs pays, dont plusieurs ont déjà rapporté s’être fait confisquer leur ordinateur portable pendant plusieurs heures à la frontière. Afin de protéger ses données sensibles et préserver la sécurité de certains participants à son forum de discussion, elle a transféré ses copies de sauvegarde dans un volume TrueCrypt chiffré et supprimé la copie qui se trouvait sur son ordinateur portable. Lorsqu’elle a demandé conseil à son neveu Nikolai, celui-ci lui a bien expliqué que si elle craint de se faire confisquer son ordinateur par les agents frontaliers, la simple suppression de ses vieilles copies de sauvegarde ne suffit pas.</i></td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>

<h3>Qu’apprendrez-vous dans ce chapitre</h3>

<p>&nbsp;</p>

<ul>
	<li>Comment supprimer définitivement les données sensibles qui se trouvent sur votre ordinateur&nbsp;;</li>
	<li>Comment supprimer définitivement les données sensibles qui se trouvent sur des dispositifs de stockage amovibles comme des CD ou des clés USB&nbsp;;</li>
	<li>Comment empêcher que des intrus soient en mesure de récupérer les documents que vous avez déjà affichés sur votre ordinateur&nbsp;;</li>
	<li>Comment entretenir votre ordinateur de telle sorte que les fichiers supprimés ne puissent jamais être récupérés.</li>
</ul>

<p>&nbsp;</p>


