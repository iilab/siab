

---

lang: fr
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: How to Install and Configure Eraser

---

<p>Tel que décrit au chapitre <a href="/chapter-6" target="_blank" title="6. Détruire définitivement des données sensibles">6. Détruire définitivement des données sensibles</a> du livret pratique, <strong>Eraser</strong> supprime les données sur le disque en les écrasant avec d'autres données aléatoires. Plus le nombre de réécritures est élevé (pour écraser les fichiers), plus il sera difficile de les récupérer.</p>

<p><strong>Commentaire :</strong> Nous recommandons d’écraser les données au moins trois fois.</p>

<p><strong>Conseil :</strong> Notez que chaque «&nbsp;passe&nbsp;» de réécriture prend un certain temps et que plus le nombre de passes est élevé, plus long sera le processus de suppression du fichier. Évidemment, cet effet sera davantage ressenti lors de la suppression de fichiers volumineux ou lors de la suppression/réécriture de l'espace libre.</p>

<p>Le nombre de passes peut être choisi en accédant au menu <i>Preferences: Erasing</i>.</p>

<p><strong>Première étape</strong>. <strong>Sélectionnez</strong>: <strong>Edit &gt; Preferences &gt; Erasing</strong>, comme suit :</p>

<p><img alt="Eraser/screenshots-en/01.png" src="/sites/securitybkp.ngoinabox.org/files/u5/eraser-fr/01.png" title="Eraser/screenshots-en/01.png" /></p>

<p><i>Figure 1 : La fenêtre Eraser [On-demand] affichant les options du menu Edit</i></p>

<p><i>La fenêtre </i>Preferences:Erasing<i> s'affiche comme suit</i> :</p>

<p><img alt="Eraser/screenshots-en/02.png" src="/sites/securitybkp.ngoinabox.org/files/u5/eraser-fr/02.png" title="Eraser/screenshots-en/02.png" /></p>

<p><i>Figure 2 : La fenêtre Preferences: Erasing</i></p>

<p>La fenêtre <i>Preferences: Erasing</i> décrit la méthode utilisée pour la suppression/réécriture des fichiers.</p>

<p><i>Description</i>: Les noms des procédures de réécriture sont affichés dans cette colonne.<br />
<i>Passes</i>: Le nombre de passes de réécritures utilisées pour chaque méthode.</p>

<p>Nous allons écraser nos données en utilisant la méthode <i>Pseudorandom Data</i>. Par défaut, cette méthode comprend une seule passe de réécriture. Par souci de sécurité, nous allons augmenter cette valeur à 3.</p>

<p><strong>Deuxième étape</strong>. <strong>Sélectionnez</strong> : <i># 4 Pseudorandom Data</i>, tel qu’illustré à la <i>figure 2</i>.</p>

<p><strong>Troisième étape</strong>. <strong>Cliquez</strong> sur <i>Edit</i> pour faire apparaître la fenêtre <i>Passes</i>, illustrée ci-dessous :</p>

<p><img alt="Eraser/screenshots-en/03.png" src="/sites/securitybkp.ngoinabox.org/files/u5/eraser-fr/03.png" title="Eraser/screenshots-en/03.png" /></p>

<p><i>Figure 3 : La fenêtre Passes d’Eraser</i></p>

<p><strong>Quatrième étape</strong>. Choisissez un nombre de passes entre 3 et 7 (tenez compte autant du temps requis pour chaque passe que du niveau de sécurité souhaité).</p>

<p><strong>Cinquième étape</strong>. <strong>Cliquez</strong> sur le bouton <i>OK</i> pour revenir à la fenêtre <i>Eraser Preferences: Erasing</i>.</p>

<p><i>L'option </i># 4 Pseudorandom Data<i> devrait maintenant ressembler à ceci :</i></p>

<p><img alt="Eraser/screenshots-en/04.png" src="/sites/securitybkp.ngoinabox.org/files/u5/eraser-fr/04.png" title="Eraser/screenshots-en/04.png" /></p>

<p><i>Figure 4 : La fenêtre </i>Preferences: Erasing<i> avec l’option 4 sélectionnée.</i></p>

<p><strong>Conseil</strong> : Assurez-vous que les options <i>Cluster Tip Area</i> et <i>Alternate Data Streams</i> sont sélectionnées (elles devraient l'être par défaut).</p>

<p><img alt="Eraser/screenshots-en/05.png" src="/sites/securitybkp.ngoinabox.org/files/u5/eraser-fr/05.png" title="Eraser/screenshots-en/05.png" /></p>

<p><i>Figure 5 : Les options Cluster Tip Area et Alternate Data Streams sélectionnées par défaut.</i></p>

<ul>
	<li><i>Cluster Tip Area</i> : Un disque dur est divisé en plusieurs segments que l'on nomme <i>clusters</i> ou «&nbsp;blocs&nbsp;». Habituellement, un fichier est contenu sur plusieurs blocs, sans toutefois remplir complètement le dernier bloc qu'il occupe. La partie vacante à la fin du dernier bloc se nomme la <i>Cluster Tip Area</i> ou «&nbsp;Zone de fin de bloc&nbsp;». Cette Zone de fin de bloc peut contenir une partie des données sensibles d'un autre fichier ayant précédemment occupé cet espace du bloc. Les données qui se trouvent dans cette zone peuvent être récupérées par un spécialiste. Assurez-vous donc de <b>cocher</b> cette case!</li>
</ul>

<ul>
	<li><i>Alternate Data Streams</i> : Un fichier stocké sur un ordinateur peut comporter plusieurs parties. Par exemple, le présent document contient du texte et des images. Ces différents éléments sont stockés à différents emplacements du disque : c’est ce que sont les <i>streams</i> ou «&nbsp;trames de données&nbsp;». <b>Cocher</b> cette option vous assure que toutes les «&nbsp;Trames de données alternatives&nbsp;» associées aux fichiers seront effacées.</li>
</ul>

<p><strong>Sixième étape</strong>. <strong>Cliquez</strong> sur le bouton <i>OK</i>.</p>

<p>Vous venez de configurer la méthode utilisée pour écraser les fichiers dans Eraser. Vous devriez choisir les mêmes options dans l'onglet suivant de la fenêtre <i>Preferences : Erasing</i>, c.-à-d. l'onglet <i>Unused Disk Space</i>. Cela dit, tenant en considération que chaque passe prendra environ deux heures, vous pouvez y spécifier un nombre de passes moins élevé.</p>


