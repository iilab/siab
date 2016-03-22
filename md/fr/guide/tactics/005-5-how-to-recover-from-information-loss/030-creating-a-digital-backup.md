

---

lang: fr
community: guide
type: tactics
legacy: True
child: True
weight: 3
depth: 3
title: Creating a digital backup

---

<p>De tous les types de fichiers mentionnés ci-dessus, ce sont des «&nbsp;documents informatisés&nbsp;», c.-à-d. les documents numériques, que la plupart des gens ont tendance à se préoccuper lorsqu’ils mettent en place une politique de sauvegarde de leurs données. Ce terme est plutôt ambigu, mais il désigne généralement les fichiers dont vous assurez vous-même la gestion, et qui s’ouvrent manuellement en double-cliquant sur le nom ou en passant par le menu Fichier d’une application appropriée. Plus précisément, il est question de fichiers texte, de documents de traitement de texte, de présentations, de PDF et de feuilles de calcul, pour ne citer que quelques exemples. Contrairement aux messages de courrier électronique, par exemple, les documents informatisés ne sont habituellement pas synchronisés avec des copies distantes sur Internet.</p>

<p>Lorsque vous sauvegardez vos documents informatisés, vous devriez toujours vous rappeler de sauvegarder également les bases de données de vos programmes. Si vous utilisez un calendrier électronique ou un carnet d’adresse électronique, par exemple, vous devrez trouver le répertoire où ces programmes stockent leurs données. Avec un peu de chance, ces bases de données se trouveront au même emplacement que vos documents informatisés, puisque ceux-ci sont habituellement stockés dans le répertoire <kbd>Mes documents</kbd> d’un système Windows. Si ce n’est pas le cas, vous devriez ajouter le répertoire approprié à votre copie de sauvegarde.</p>

<p>Les messages de courriel stockés à l’aide d’un client de messagerie comme <a href="glossaire#Thunderbird" title="Thunderbird"><i>Mozilla Thunderbird</i></a> présentent un exemple particulier de base de données. Si vous utilisez un programme de messagerie (et tout particulièrement si vous ne souhaitez pas ou êtes incapable de stocker une copie de vos messages sur le serveur de courriels), vous devriez vous assurer d’inclure la base de données de courriel dans votre sauvegarde régulière. Il est possible que vous considériez vos fichiers graphiques et audio comme des documents informatisés ou des items associés à une base de données de programme, selon l’utilisation que vous en faites. Certaines applications, comme Windows Media Player et iTunes, par exemple, fonctionnent comme des bases de données. Si vous utilisez des programmes comme ceux-là, vous devrez peut-être effectuer une recherche sur votre disque dur pour découvrir où sont stockés les fichiers média dont ils assurent la gestion.</p>

<p>&nbsp;</p>

<h3>Les dispositifs de stockage</h3>

<p>&nbsp;</p>

<p>Avant de faire une copie de sauvegarde de vos documents informatisés, vous devez d’abord choisir un ou des dispositifs de stockage appropriés.</p>

<p><b>Les disques ou clés de mémoire USB</b> - Les disques ou clés de mémoire USB peuvent ne coûter presque rien et offrent une grande capacité de mémoire. Il est facile d'en supprimer le contenu ou de réécrire plusieurs fois dessus. Les disques ou clés USB ont une durée de vie limitée qui dépend en grande partie de la manière et de la fréquence d'utilisation. Elle est estimée à environ dix ans.</p>

<p><b>Les disques compacts (CD)</b> Les CD peuvent stocker jusqu’à 700 Mo de données. Vous aurez besoin d’un <a href="glossaire#Graveur_CD" title="Graveur_CD"><i>graveur de CD</i></a> et de disques vierges pour créer une copie de sauvegarde sur CD. Si vous souhaitez effacer le contenu d’un CD et actualiser les fichiers qui y sont stockés, vous aurez besoin d’un graveur CD-RW et de disques réinscriptibles. Tous les systèmes d’exploitations courants, dont Windows XP, comportent maintenant des logiciels intégrés qui permettent de graver des CD et CD-RW. Gardez à l’esprit que les données gravées sur ces disques risquent de se détériorer après une période de dix à quinze ans. Si vous devez conserver une copie de sauvegarde pour une longue période, vous devriez graver un nouveau CD périodiquement, acheter des disques spéciaux de «&nbsp;longue durée&nbsp;» ou utiliser une autre méthode de sauvegarde.</p>

<p><b>Les disques numériques polyvalents (DVD)</b> - Les DVD peuvent stocker jusqu’à 4,7 Go de données. Ils fonctionnent essentiellement de la même façon que les CD, mais requièrent du matériel un peu plus cher. Vous aurez besoin d’un <a href="glossaire#Graveur_CD" title="Graveur_CD"><i>graveur DVD ou DVD-RW</i></a>, et de disques appropriés. Comme pour les CD, les DVD normaux se dégradent avec le temps.</p>

<p><b>Les serveurs distants</b> - Un serveur de sauvegarde bien entretenu peut offrir une capacité de mémoire quasiment illimitée, mais c’est la vitesse et la stabilité de votre connexion Internet qui déterminera si cette option est appropriée à votre situation. N’oubliez pas que la tenue d’un serveur de sauvegarde à l’intérieur même de votre bureau trahit la règle voulant qu’il est nécessaire de conserver une copie de sauvegarde de vos données dans au moins deux emplacements physiques séparés. Il existe par ailleurs des services de stockage gratuits sur Internet, mais vous devriez soigneusement considérer les risques liés au fait de mettre vos informations en ligne et vous devriez toujours chiffrer vos données avant de les téléverser sur des serveurs gérés par des individus ou organismes que vous ne connaissez pas ou en qui vous ne faites pas entièrement confiance. Veuillez consulter la section <a href="chapter_5_5" title="Chapitre 5.5"><i><b>Lecture complémentaire</b></i></a>, à la fin de ce chapitre, pour plus de conseils à ce sujet.</p>

<p>&nbsp;</p>

<h3>Les logiciels de sauvegarde</h3>

<p>&nbsp;</p>

<p>Cobian Backup est un logiciel facile à utiliser qui peut être programmé pour exécuter des sauvegardes automatiquement, à des intervalles prédéterminés, et actualiser uniquement les fichiers qui ont été modifiés depuis la dernière sauvegarde. Le programme peut également comprimer les copies de sauvegarde pour économiser l’espace.</p>

<p>&nbsp;</p>

<table cellpadding="5" cellspacing="0" style="border: 2pt dashed #008000; background-color: #e9e8a4">
	<tbody>
		<tr>
			<td><img align="middle" height="63" src="/sites/securitybkp.ngoinabox.org/files/u9/hand_web_trans.png" width="60" /> <b>Expérience pratique&nbsp;: se lancer avec le </b><i><a href="cobian_principale"><b>Guide pratique Cobian Backup</b></a></i></td>
		</tr>
	</tbody>
</table>

<p>Comme toujours, il est conseillé de chiffrer vos fichiers de sauvegarde à l’aide d’un programme comme <a href="glossaire#TrueCrypt" title="TrueCrypt"><i>TrueCrypt</i></a>. Vous trouverez plus de renseignements sur le chiffrement de données dans le chapitre <a href="chapter-4" title="Chapitre 4"><i><b>4. Protéger les données sensibles stockées sur votre ordinateur</b></i></a>.</p>

<p>&nbsp;</p>

<table cellpadding="5" cellspacing="0" style="border: 2pt dashed #008000; background-color: #e9e8a4">
	<tbody>
		<tr>
			<td><img align="middle" height="63" src="/sites/securitybkp.ngoinabox.org/files/u9/hand_web_trans.png" width="60" /> <b>Expérience pratique&nbsp;: se lancer avec le </b><i><a href="truecrypt_principale"><b>Guide pratique TrueCrypt</b></a></i></td>
		</tr>
	</tbody>
</table>

<p>Lorsque vous utilisez ces logiciels de sauvegarde, il y a un certain nombre de manœuvres que vous pouvez effectuer pour faire en sorte que votre système de sauvegarde fonctionne sans heurts&nbsp;:</p>

<ul>
	<li>Organisez adéquatement vos fichiers sur votre ordinateur. Autant que possible, essayez de transférer tous les document informatisés dont vous souhaitez faire une copie de sauvegarde dans un seul emplacement, comme par exemple dans le répertoire <kbd>Mes documents</kbd>.</li>
	<li>Si vous utilisez des logiciels qui utilisent une base de données, vous devriez tout d’abord déterminer l’emplacement des bases de données. Si l’emplacement initial n’est pas pratique pour vous, voyez si le programme vous permet d’en choisir un nouveau pour y déplacer la base de données. Si cela s’avère possible, vous pouvez déplacer la base de données du programme vers le répertoire où vous aviez déjà stocké vos documents informatisés.</li>
	<li>Déterminez un intervalle régulier pour la création des sauvegardes automatiques.</li>
	<li>Tâchez d’établir une procédure standard pour tous les membres du personnel de votre bureau qui n’adhèrent pas déjà à une politique de sauvegarde commune. Expliquez bien à vos collègues l’importance d’une telle politique.</li>
	<li>N’oubliez pas de tester le processus de récupération des données depuis vos copies de sauvegarde. En fin de compte, ce n’est pas tant la procédure de sauvegarde qui vous importe, sinon la procédure de récupération&nbsp;!</li>
</ul>

<p>&nbsp;</p>

<table cellpadding="5" cellspacing="0" style="border: 2pt dashed #008000; background-color: #e9e8a4">
	<tbody>
		<tr>
			<td><i>Elena&nbsp;: OK, j’ai donc créé une copie de sauvegarde chiffrée quand j’étais au bureau, que j’ai ensuite gravée sur un CD. Cobian est maintenant programmé pour actualiser ma sauvegarde dans deux jours. Mon poste de travail au bureau comporte un tiroir que je peux fermer à clé, où j’ai l’intention de garder mes CD de sauvegarde pour éviter de les perdre ou de les endommager. </i><br />
			<br />
			<i>Nikolai&nbsp;: Mais que feras-tu si les locaux de l’ONG sont détruits par un incendie&nbsp;? Les ordinateurs, les bureaux, les CD de sauvegarde et tout. Ou encore, imagine que ton forum serve de tremplin pour une méga manifestation environnementaliste et que le gouvernement décide alors d’intervenir, de tout fermer et de saisir le matériel&nbsp;? Je doute fort que la petite serrure de ton tiroir puisse résister à la police si elle décide de confisquer tes CD. Pourquoi ne pas conserver ces copies de sauvegarde à la maison&nbsp;? Ou encore demander à un ami de les garder pour toi&nbsp;?</i></td>
		</tr>
	</tbody>
</table>


