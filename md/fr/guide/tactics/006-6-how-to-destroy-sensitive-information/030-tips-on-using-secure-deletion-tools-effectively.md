

---

lang: fr
community: guide
type: tactics
legacy: True
child: True
weight: 3
depth: 3
title: Tips on using secure deletion tools effectively

---

<p>Lorsque vous utilisez un programme de suppression sécurisée comme ceux que nous recommandons dans le présent chapitre, il est plus juste de dire que vous remplacez, ou «&nbsp;écrasez&nbsp;», les données sensibles, que de simplement parler de suppression. Revenons aux documents conservés dans le classeur mal étiqueté dont il était question ci-dessus, et admettons qu’ils sont rédigés au crayon de plomb. Le programme de suppression sécurisée ne se contentera pas d’effacer ce qui y est écrit, il gribouillera en plus par-dessus chaque mot. Et comme des phrases écrites au crayon de plomb, les données informatisées peuvent tout de mêmes êtres lues (quoique difficilement) après avoir été effacées. Il est même parfois possible de les lire après qu’on ait gribouillé par-dessus. C’est pourquoi les programmes recommandés ici écrasent plusieurs fois les fichiers avec des données aléatoires. Ce processus est appelé «&nbsp;<a _mce_href="/glossaire#Wiping" href="glossaire#Wiping" title="Wiping"><i>nettoyage</i></a>&nbsp;» (ou <i>wiping</i> en anglais). En écrasant plusieurs fois les données à éliminer (le nombre de «&nbsp;passes&nbsp;» est important), le programme réduit exponentiellement les probabilités qu’une personne mal intentionnée parvienne à récupérer ces données. Les spécialistes s’accordent généralement pour dire que trois passes ou plus sont nécessaires (certains recommandent jusqu’à sept passes), mais les programmes de «&nbsp;nettoyage&nbsp;» le font automatiquement.</p>

<p>&nbsp;</p>

<h3>Le nettoyage des fichiers</h3>

<p>Il existe deux moyens répandus pour nettoyer vos disques durs et autres dispositifs de stockage dans le but de supprimer définitivement les données sensibles que vous souhaitez éliminer. Vous pouvez nettoyer un fichier unique ou nettoyer tout l’espace «&nbsp;non alloué&nbsp;» du disque dur. Avant de choisir l’une ou l’autre de ces méthodes, il est utile de se rappeler notre exemple du long rapport dont plusieurs versions se retrouvent un peu partout sur votre disque dur, et ce, même si un seul fichier est visible. Si vous écrasez le fichier lui-même, vous vous assurez que la version actuelle est définitivement supprimée, mais vous laissez les autres copies intactes. En fait, il n’y a aucun moyen de cibler précisément ces copies parce qu’il n’est pas possible de les localiser sans l’aide de logiciels spéciaux. En nettoyant tout l’espace libre de votre disque dur, cependant, vous vous assurez que toutes les données préalablement supprimées seront définitivement détruites. Pour revenir à la métaphore du classeur, cette procédure est comparable à une recherche systématique de tous les documents stockés dans le classeur dont l’étiquette a été retirée, pour en effacer le contenu et écrire plusieurs fois par-dessus l’ancien contenu.</p>

<p><a _mce_href="/glossaire#Eraser" href="glossaire#Eraser" title="Eraser"><i>Eraser</i></a> est un programme de suppression sécurisée, gratuit et de code source libre, extrêmement facile à utiliser. Vous pouvez nettoyer des fichiers de trois façons différentes avec Eraser&nbsp;: en sélectionnant un fichier en particulier, en sélectionnant le contenu entier de votre <kbd>Corbeille</kbd>, ou en nettoyant tout l’espace libre de votre disque dur. Eraser peut aussi nettoyer le contenu du <a _mce_href="/glossaire#Swap_file" href="glossaire#Swap_file" title="Swap_file"><i>fichier d’échange</i></a> de Windows.</p>

<p>&nbsp;</p>

<table _mce_style="border: 2pt dashed #008000; background-color: #e9e8a4;" cellpadding="5" cellspacing="0" class="mceItemTable" style="border: 2pt dashed #008000; background-color: #e9e8a4">
	<tbody>
		<tr>
			<td><img _mce_src="/sites/securitybkp.ngoinabox.org/files/u9/hand_web_trans.png" align="middle" height="63" src="https://info.securityinabox.org/sites/securitybkp.ngoinabox.org/files/u9/hand_web_trans.png" width="60" /> <b>Expérience pratique&nbsp;: se lancer avec le </b><i><a _mce_href="/eraser_principale" href="https://securityinabox.org/fr/eraser_main"><b>Guide pratique Eraser</b></a></i></td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>

<p>Même si, a priori, les programmes de suppression sécurisée ne risquent pas d’endommager les fichiers visibles (à moins que vous ne les nettoyiez volontairement), la précaution est de mise. Après tout, un accident est si vite arrivé. C’est justement pourquoi les <kbd>Corbeilles</kbd> et les logiciels de récupération de données sont tellement utiles. Si vous vous habituez à nettoyer vos données chaque fois que vous supprimez quelque chose, vous pourriez vous retrouver dans une situation où il serait tout simplement impossible de réparer une erreur toute banale. Assurez-vous de toujours avoir une copie de sauvegarde avant de nettoyer de grandes quantités de données.</p>

<p>&nbsp;</p>

<table _mce_style="border: 2pt dashed #008000; background-color: #e9e8a4;" cellpadding="5" cellspacing="0" class="mceItemTable" style="border: 2pt dashed #008000; background-color: #e9e8a4">
	<tbody>
		<tr>
			<td><i>Elena&nbsp;: Je sais que les programmes de traitement de texte comme Microsoft Word ou Open Office génèrent des copies temporaires des documents que je rédige. Est-ce que d’autres programmes font la même chose, ou devrais-je surtout m’inquiéter des fichiers que je crée et supprime moi-même&nbsp;? </i><br />
			<br />
			<i>Nikolai&nbsp;: En fait, les programmes que tu utilises laissent des traces de tes renseignements personnels et de tes activités à plusieurs endroits sur ton ordinateur. Les sites que tu as visités, les brouillons de courriels que tu as rédigés récemment et autres trucs semblables en sont quelques exemples. Tous ces renseignements peuvent être plus ou moins sensibles, selon la fréquence à laquelle tu utilises cet ordinateur.</i></td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>

<p>&nbsp;</p>

<h3>Le nettoyage des données temporaires</h3>

<p>La fonction qui permet à Eraser de nettoyer tout l’espace non alloué d’un disque dur n’est pas aussi dangereuse qu’elle le semble, parce qu’elle n’écrase que les données préalablement supprimées. Les fichiers normaux, c.-à-d. toujours visibles, ne seront pas touchés. Cependant, cela soulève un autre enjeu&nbsp;: Eraser ne peut pas être utilisé pour écraser des données sensibles qui n’ont pas été supprimées, mais qui sont par contre bien cachées. Les fichiers contenant des données de ce type peuvent être dissimulés dans des répertoires peu connus, par exemple, ou sauvegardés avec des noms inintelligibles. Cette question n’est pas particulièrement importante pour vos documents informatisés, mais elle peut l’être pour les données qui sont sauvegardées automatiquement chaque fois que vous utilisez votre ordinateur. Voici quelques exemples&nbsp;:</p>

<ul>
	<li>Les données temporaires enregistrées automatiquement par votre navigateur lorsqu’il affiche des pages Web, dont le texte, les images, les <a _mce_href="/glossaire#Cookie" href="glossaire#Cookie" title="Cookie"><i>cookies</i></a>, les détails du compte et les renseignements personnels utilisés pour remplir des formulaire en ligne, sans oublier l’historique de navigation.</li>
</ul>

<ul>
	<li>Les fichiers temporaires sauvegardés par divers programme pour vous aider à récupérer vos documents lorsque l’ordinateur plante inopinément avant que vous ayez pu sauvegarder vos modifications. Ces fichiers contiennent, par exemple, du texte, des images, des données de feuilles de calcul et les noms d’autres fichiers.</li>
</ul>

<ul>
	<li>Des fichiers et des liens sauvegardés par Windows par souci de commodité, comme les raccourcis vers les programmes que vous avez utilisés récemment, les liens flagrants vers des répertoires que vous souhaiteriez garder secrets et, évidemment, le contenu de votre <kbd>Corbeille</kbd> si vous avez oublié de la vider.</li>
</ul>

<ul>
	<li>Le fichier d’échange de Windows. Quand la mémoire vive de votre ordinateur est utilisée à pleine capacité, comme lorsque vous faites fonctionner plusieurs programmes simultanément sur un vieil ordinateur, Windows copie parfois les données que vous utilisez dans un seul grand fichier, appelé fichier d’échange (ou swap file, en anglais). En fait, selon l’utilisation que vous faites de l’ordinateur, ce fichier pourrait contenir à peu près n’importe quoi, y compris des pages Web, le contenu de certains documents, des mots de passe ou même des clés de chiffrement. Le fichier d’échange n’est pas supprimé lorsque vous éteignez votre ordinateur. C’est pourquoi vous devez le nettoyer manuellement.</li>
</ul>

<p>Pour éliminer de votre ordinateur les fichiers temporaires les plus courants, vous pouvez utiliser un gratuiciel appelé <a _mce_href="/glossaire#CCleaner" href="glossaire#CCleaner" title="CCleaner"><i>CCleaner</i></a>. Ce logiciel a été conçu spécialement pour nettoyer les traces que génèrent des programmes comme Internet Explorer, <a _mce_href="/glossaire#Firefox" href="glossaire#Firefox" title="Firefox"><i>Mozilla Firefox</i></a> et Microsoft Office (tous trois connus pour leur indiscrétion), ainsi que le système Windows lui-même. CCleaner supprime les fichiers temporaires définitivement et de façon sécurisée. Vous n’êtes donc pas obligé de nettoyer systématiquement l’espace non alloué du disque dur avec Eraser après chaque utilisation du programme.</p>

<p>&nbsp;</p>

<table _mce_style="border: 2pt dashed #008000; background-color: #e9e8a4;" cellpadding="5" cellspacing="0" class="mceItemTable" style="border: 2pt dashed #008000; background-color: #e9e8a4">
	<tbody>
		<tr>
			<td><img _mce_src="/sites/securitybkp.ngoinabox.org/files/u9/hand_web_trans.png" align="middle" height="63" src="https://info.securityinabox.org/sites/securitybkp.ngoinabox.org/files/u9/hand_web_trans.png" width="60" /> <b>Expérience pratique&nbsp;: se lancer avec le </b><i><a _mce_href="/ccleaner_principale" href="https://securityinabox.org/fr/ccleaner_principale"><b>Guide pratique CCleaner </b></a></i></td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>

<p>&nbsp;</p>


