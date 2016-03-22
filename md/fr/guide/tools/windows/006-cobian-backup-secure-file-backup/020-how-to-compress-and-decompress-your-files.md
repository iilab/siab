

---

lang: fr
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Compress and Decompress Your Files

---

<p><strong>Étape 1.</strong> <strong>Créez</strong> une tâche de sauvegarde pour tous les fichiers que vous souhaitez archiver en suivant les étapes énumérées à la section <a href="cobian_howtobackup" target="_blank" title="Section 2.3 Créer une copie de sauvegarde"><strong>2.3 Créer une copie de sauvegarde</strong></a>.</p>

<p><strong>Étape 2.</strong> <strong>Sélectionnez</strong> l’option <i>Archive</i> dans le menu de gauche pour activer la fenêtre <i>Propriétés de:</i></p>

<p><img alt="Cobian_Backup/screenshots-fr/10.png" src="/sites/securitybkp.ngoinabox.org/files/u5/cobian-fr/10.png" title="Cobian_Backup/screenshots-fr/10.png" /></p>

<p><i>Figure 8 : La fenêtre Propriétés de: affichant les rubriques Compression et Cryptage avancé</i></p>

<h3>3.1 Comment compresser vos archives</h3>

<p>La rubrique <i>Compression</i> sert à déterminer la méthode de compression de votre choix.</p>

<p>La compression sert à réduire l'espace employé pour stocké vos fichiers. Supposons que votre ordinateur contienne une série de vieux fichiers dont vous vous servez peu, mais que vous souhaitez tout de même conserver. Il est logique que vous les stockiez dans un format qui occupe le moins d’espace possible en ayant recours aux techniques de compression et de décompression. La compression enlève les éléments de codification peu importants d’un document, tout en conservant l’information importante. La compression n’abîme pas vos données originales. Les fichiers ne sont pas visibles lorsque compressés. Le processus inverse, la <i>décompression</i>, doit être appliqué aux fichiers pour les rendre visibles à nouveau.</p>

<p>Les trois sous-options du menu défilant de la <i>méthode de compression</i> sont :</p>

<p><i>Pas de compression</i> : Tel que son nom l’indique, cette option n’exécute pas de compression.</p>

<p><i>Compression Zip</i> : Il s’agit de la technique de compression normale pour les systèmes <strong>Windows</strong>. Les archives, une fois créées, peuvent être ouvertes à l’aide des outils Windows habituels (vous pouvez aussi télécharger le programme <a href="http://www.zipgenius.it/" target="_blank">ZipGenius</a> pour les ouvrir). Cette option est la plus pratique des trois.</p>

<p><i>Compression SQX</i> : La compression SQX est plus lente que la compression Zip. Cependant, en cas de corruption des archives, son taux de récupération des données est plus élevé.</p>

<p>Si vous avez choisi l’une des trois options de compression mentionnées ci-dessus, vous pouvez également choisir :</p>

<p><i>Options de découpage</i>, du menu défilant. Cette option est pratique pour stocker des données sur des supports portatifs comme des CD, des DVD, des disquettes ou des clés USB. Vos archives seront découpées en morceaux dont la taille correspond au dispositif de stockage de votre choix. Supposons que vous copiez un grand nombre de fichiers, que vous souhaitez les transférer sur un CD et que la taille de vos archives dépasse 700 Mo (la taille d’un CD). La fonction de découpage divisera vos archives en morceaux plus petits que 700 Mo, ou équivalents à cette taille : vous pourrez alors les graver sur un ou plusieurs CD. Si vous prévoyez créer des copies de sauvegarde du disque dur de votre ordinateur ou que la taille de votre copie de sauvegarde est inférieure à la capacité de stockage de votre dispositif, vous pouvez passer cette section.</p>

<p>Les options de taille suivantes vous sont offertes lorsque vous cliquez sur le menu défilant <i>Options de découpage</i>. Votre choix dépendra du dispositif de stockage que vous souhaitez utiliser.</p>

<p><img alt="Cobian_Backup/screenshots-fr/11.png" src="/sites/securitybkp.ngoinabox.org/files/u5/cobian-fr/11.png" title="Cobian_Backup/screenshots-fr/11.png" /></p>

<p><i>Figure 9 : Le menu défilant Options de découpage</i></p>

<ul>
	<li>3,5" – Disquette. Cette option contient assez d’espace pour y stocker un petit nombre de documents.</li>
	<li>Zip – Disque Zip (vérifiez la capacité du disque Zip que vous utilisez). Vous aurez besoin d’un lecteur de disque Zip connecté à votre ordinateur et des disques personnalisés.</li>
	<li>Disque CD-R – CD (vérifiez la capacité du disque que vous utilisez). Vous aurez besoin d’un graveur de CD connecté à votre ordinateur et d’un programme d’écriture de CD.</li>
	<li>Disque DVD – DVD (vérifiez la capacité du disque que vous utilisez). Vous aurez besoin d’un graveur DVD connecté à votre ordinateur et d’un programme d’écriture DVD.</li>
</ul>

<p>Si vous créez des copies de sauvegarde que vous stockez sur plusieurs clés USB, vous avez peut-être intérêt à fixer une taille personnalisée.</p>

<p>Pour ce faire, suivez les étapes énumérées ci-dessous :</p>

<p><strong>Première étape</strong>. <strong>Sélectionnez</strong> l’option <i>Taille personnalisée</i>, et <strong>saisissez</strong> la taille de l’archive en octets dans la zone de texte :</p>

<p><img alt="Cobian_Backup/screenshots-fr/12.png" src="/sites/securitybkp.ngoinabox.org/files/u5/cobian-fr/12.png" title="Cobian_Backup/screenshots-fr/12.png" /></p>

<p><i>Figure 10 : La zone de texte Taille personnalisée</i></p>

<p>Un aperçu des tailles :</p>

<ul>
	<li>1 Ko (kilooctet) = 1 024 octets – un document texte d’une page fait à l’aide de Open Office correspond environ à 20 Ko.</li>
	<li>1 Mo (mégaoctet) = 1 024 Ko – une photo prise à l’aide d’une caméra numérique se situe généralement entre 1 et 3 Mo.</li>
	<li>1 Go (gigaoctet) = 1 024 Mo – environ une demi-heure d’un film DVD de bonne qualité.</li>
</ul>

<p><strong>Commentaire</strong> : Lorsque vous choisissez une taille personnalisée pour découper vos copies de sauvegarde afin de les stocker sur un DVD ou un CD, Cobian Backup ne copiera pas automatiquement la sauvegarde sur votre dispositif de stockage. Le programme créera plutôt vos archives sur votre ordinateur, et vous devrez les graver vous-même sur le CD ou le DVD.</p>

<p><i>Protéger par mot de passe</i> : Cette option vous permet de choisir un mot de passe pour protéger vos archives. Saisissez simplement, deux fois, un mot de passe dans les zones de texte appropriées. Au moment de décompresser l’archive, le programme vous demandera votre mot de passe avant d’exécuter la tâche.</p>

<p><strong>Commentaire</strong> : Si vous souhaitez augmenter le niveau de sécurité de l’archive, vous devriez envisager d’utiliser une autre méthode que celle du mot de passe. Cobian Backup vous permet également de chiffrer votre archive. Cette méthode sera abordée dans la section qui suit, <a href="cobian_encrypt" target="_blank" title="Section 4. Chiffrer vos archives"><strong>4. Chiffrer vos archives</strong></a>. Sinon, vous pouvez aussi consulter le <a href="truecrypt_main" target="_blank" title="Guide pratique TrueCrypt">Guide pratique TrueCrypt</a> pour apprendre comment créer un volume de stockage chiffré sur votre ordinateur ou sur un dispositif amovible.</p>

<p><i>Commentaire</i> : Cette option vous permet d’inscrire une information descriptive au sujet de l’archive (facultatif).</p>

<h4>3.2 Comment décompresser votre archive</h4>

<p>Pour décompresser votre archive, suivez les étapes énumérées ci-dessous :</p>

<p><strong>Première étape</strong>. <strong>Sélectionnez :</strong> <strong>Outils &gt; Décompacteur</strong></p>

<p><img alt="Cobian_Backup/screenshots-fr/18.png" src="/sites/securitybkp.ngoinabox.org/files/u5/cobian-fr/18.png" title="Cobian_Backup/screenshots-fr/18.png" /></p>

<p><i>Figure 16 : Le menu Outils affichant l’option Décompacteur</i></p>

<p>La fenêtre <i>Décompacteur</i> apparaît :</p>

<p><img alt="Cobian_Backup/screenshots-fr/19.png" src="/sites/securitybkp.ngoinabox.org/files/u5/cobian-fr/19.png" title="Cobian_Backup/screenshots-fr/19.png" /></p>

<p><i>Figure 17 : </i>La fenêtre Cobian Backup - Décompacteur</p>

<p><strong>Deuxième étape</strong>. <strong>Cliquez</strong> sur : <img alt="Cobian_Backup/screenshots-fr/20.png" src="/sites/securitybkp.ngoinabox.org/files/u5/cobian-fr/20.png" title="Cobian_Backup/screenshots-fr/20.png" /></p>

<p><strong>Troisième étape</strong>. <strong>Sélectionnez</strong> l’archive (fichier .zip ou .sqx)</p>

<p><strong>Quatrième étape</strong>. <strong>Cliquez</strong> sur le bouton <i>OK</i>.</p>

<p><strong>Cinquième étape</strong>. <strong>Sélectionnez</strong> un répertoire ou vous souhaitez décompresser le fichier archivé.</p>

<p><strong>Sixième étape</strong>. <strong>Cliquez sur</strong> : <img alt="Cobian_Backup/screenshots-fr/21.png" src="/sites/securitybkp.ngoinabox.org/files/u5/cobian-fr/21.png" title="Cobian_Backup/screenshots-fr/21.png" /></p>

<p>Vous verrez apparaître une nouvelle fenêtre qui vous permettra de choisir le répertoire où vous souhaitez décompresser l’archive.</p>

<p><strong>Septième étape</strong>. <strong>Sélectionnez</strong> un répertoire.</p>

<p><strong>Huitième étape</strong>. <strong>Cliquez</strong> sur le bouton <i>OK</i>.</p>

<p>Utilisez <strong>Windows Explorer</strong> pour voir les fichiers transférés dans ce répertoire.</p>


