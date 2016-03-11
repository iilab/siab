

---

lang: fr
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 1
depth: 3
title: How to Install Cobian Backup and Archive Your Files

---

<p>Cette section aborde les configurations minimales nécessaires à la création de copies de sauvegarde de groupes de fichiers. D’autres sections aborderont la compression et/ou le chiffrage des copies de sauvegarde des fichiers. <strong>Cobian Backup</strong> vous permet de créer des tâches de sauvegarde qui peuvent être configurées pour inclure un groupe particulier de fichiers et/ou de répertoires. Vous pouvez régler le programme pour que ces tâches de sauvegarde soient exécutées à des heures et des jours déterminés.</p>

<p>Pour créer une tâche de sauvegarde, suivez les étapes énumérées ci-dessous :</p>

<p><strong>Première étape</strong>. <strong>Cliquez</strong> sur : <img alt="Cobian_Backup/screenshots-fr/01.png" src="/sites/securitybkp.ngoinabox.org/files/u5/cobian-fr/01.png" title="Cobian_Backup/screenshots-fr/01.png" /> pour créer une nouvelle tâche de sauvegarde.</p>

<p>Ceci active la fenêtre <i>Propriétés de:</i></p>

<p>Le menu de gauche vous offre d’activer les différentes fenêtres et d’établir les paramètres nécessaires à la procédure de sauvegarde.</p>

<p><img alt="Cobian_Backup/screenshots-fr/02.png" src="/sites/securitybkp.ngoinabox.org/files/u5/cobian-fr/02.png" title="Cobian_Backup/screenshots-fr/02.png" /></p>

<p><i>Figure 2 : La fenêtre Propriétés de: affichant le nom du fichier MaSauvegarde nouvellement créé</i></p>

<h3 id="a2.1Descriptiondesoptions">2.1 Description des options</h3>

<p><i>Nom de la tâche</i> : Sélectionnez un nom pour la tâche. Utilisez un nom qui désigne la nature de la copie de sauvegarde. Par exemple, si la copie de sauvegarde contiendra les fichiers vidéo, vous pouvez la nommer <i>Copie de sauvegarde vidéo</i>.</p>

<p><i>Désactiver</i> : Laissez la case <i>désactiver</i> non cochée. <b>Avertissement</b> : Si vous cochez cette option, la tâche ne s’exécutera pas.</p>

<p><i>Inclure les sous-répertoires</i> : Si cette option est cochée, tout dossier qui se trouve dans le dossier que vous avez sélectionné sera inclus. Cette méthode est efficace pour créer des copies de sauvegarde d’un grand nombre de fichiers. Par exemple : si vous sélectionnez le dossier <i>Mes documents</i> et cochez cette option, tous les fichiers et dossiers dans Mes documents seront inclus dans la copie de sauvegarde.</p>

<p><i>Créer des copies de sauvegarde séparées avec date-heure</i> : Cette option signifie qu’une fois la copie de sauvegarde terminée, l’heure et la date à laquelle elle a été créée apparaîtra dans le nom du dossier qui contient la copie de sauvegarde. Cette option est intéressante parce qu’elle vous permettra de reconnaître facilement le moment où la copie de sauvegarde a été créée.</p>

<p><i>Utiliser les attributs de fichiers</i> : Cette option n’est utile que si vous choisissez de créer une copie de sauvegarde incrémentielle ou différentielle (voir détails ci-dessous). Les attributs de fichiers contiennent de l’information au sujet du fichier.</p>

<p>Cobian Backup vérifie cette information afin de déterminer si un changement a été apporté au fichier source depuis la dernière fois qu’une copie de sauvegarde a été créée. Si vous exécutez une copie de sauvegarde incrémentielle ou différentielle, le fichier sera mis à jour. <strong>Commentaire</strong> : Vous ne serez en mesure d’exécuter une copie de sauvegarde complète ou "factice" que si vous décochez cette option (la copie de sauvegarde "factice" est expliquée ci-dessous).</p>

<h3 id="a2.2Descriptiondestypesdecopiesdesauvegarde">2.2 Description des types de copies de sauvegarde</h3>

<p><i>Complète</i> : Tous les fichiers se trouvant à l’emplacement source seront copiés dans votre répertoire de copies de sauvegarde. Si vous cochez l’option <i>Créer des copies de sauvegarde séparées avec date-heure</i>, vous aurez plusieurs copies provenant de la même source (identifiées au moyen de l’heure et de la date, incluses dans le nom du fichier, où la copie a été créée). Autrement dit, le programme écrasera la version antérieure (s’il en existe une).</p>

<p><i>Incrémentielle</i> : Le programme vérifiera si les fichiers source ont été modifiés depuis la création de la plus récente copie de sauvegarde. Le programme ignorera les fichiers qui n’ont pas besoin d’être copiés, ce qui économisera du temps. L’option <i>Utiliser les attributs de fichiers</i> doit être cochée pour que ce type de sauvegarde puisse être exécutée.</p>

<p><i>Bit d’archive</i> : Il s’agit d’information sur la taille du fichier et sur la date de création et de modification. Cette information permet à Cobian Backup de déterminer si le fichier a été modifié par vous depuis la dernière création d’une copie de sauvegarde.</p>

<p><i>Différentielle</i> : Le programme vérifiera si la source a été modifiée depuis la dernière création d’une copie de sauvegarde <b>complète</b>. Le programme ignorera les fichiers qui n’ont pas besoin d’être copiés, ce qui économisera du temps. Si vous avez auparavant exécuté une copie de sauvegarde complète du même groupe de fichiers, vous pouvez alors continuer à créer des copies de sauvegarde en utilisant la méthode différentielle.</p>

<p><i>Sauvegarde factice</i> : Cette option correspond à une fonction de copie de sauvegarde dont nous n’avons pas vraiment besoin. Tu peux l’utiliser pour que ton ordinateur exécute ou ferme certains programmes à des moments précis. Cette option, de niveau avancé, est peu utile à nos procédures de copie de sauvegarde.</p>

<h3 id="a2.3Commentcréerunfichierdesauvegarde">2.3 Comment créer un fichier de sauvegarde</h3>

<p>Pour démarrer la création d’un fichier de sauvegarde, suivez les étapes énumérées ci-dessous :</p>

<p><strong>Première étape</strong>. <strong>Cliquez</strong> sur l’icône <i>Fichiers</i> dans le coin gauche de la fenêtre <i>Propriétés de:</i> pour sélectionner les fichiers qui seront copiés.</p>

<p><img alt="Cobian_Backup/screenshots-fr/03.png" src="/sites/securitybkp.ngoinabox.org/files/u5/cobian-fr/03.png" title="Cobian_Backup/screenshots-fr/03.png" /></p>

<p><i>Figure 3 : La fenêtre Propriétés de : affichant les fenêtres Source et Destination</i></p>

<p><strong>Deuxième étape</strong>. <strong>Sélectionnez</strong> les fichiers que vous souhaitez copier. (Dans l’exemple précédent, le dossier <i>Mes documents</i> est sélectionné.)</p>

<p><strong>Troisième étape</strong>. <strong>Cliquez</strong> sur <img alt="Cobian_Backup/screenshots-fr/04.png" src="/sites/securitybkp.ngoinabox.org/files/u5/cobian-fr/04.png" title="Cobian_Backup/screenshots-fr/04.png" /> dans la fenêtre <strong>Source</strong> pour activer le menu suivant :</p>

<p><img alt="Cobian_Backup/screenshots-fr/05.png" src="/sites/securitybkp.ngoinabox.org/files/u5/cobian-fr/05.png" title="Cobian_Backup/screenshots-fr/05.png" /></p>

<p><i>Figure 4 : La fenêtre Source – le menu du bouton Ajouter</i></p>

<p><strong>Quatrième étape</strong>. <strong>Sélectionnez</strong> <i>Fichiers</i> pour créer des copies de sauvegarde de fichiers individuels, et <i>Répertoire</i> si vous souhaitez créer une copie de sauvegarde d’un répertoire entier ou pour indiquer quel fichier ou répertoire doit être copié.</p>

<p><strong>Commentaire</strong> : Vous pouvez ajouter autant de fichiers ou de répertoires que vous le souhaitez. Si vous souhaitez effectuez une sauvegarde de fichiers se trouvant déjà sur votre serveur FTP, <strong>sélectionnez</strong> l'option <i>Site FTP</i> (vous aurez besoins des détails de connexion appropriés pour vous connecter au serveur).</p>

<p>Après avoir sélectionné les fichiers et/ou dossiers, vous les verrez apparaître dans la zone <i>Source</i>. Comme vous le constatez avec l’exemple ci-dessous, <i>Mes documents</i> est affiché dans cette partie, ce qui veut dire que ce dossier fait maintenant partie de la copie de sauvegarde.</p>

<p>La fenêtre <i>Destination</i> désigne l’endroit où les copies de sauvegarde seront stockées.</p>

<p><strong>Cinquième étape</strong>. <strong>Cliquez</strong> sur : <img alt="Cobian_Backup/screenshots-fr/06.png" src="/sites/securitybkp.ngoinabox.org/files/u5/cobian-fr/06.png" title="Cobian_Backup/screenshots-fr/06.png" /> dans la fenêtre <i>Destination</i> pour activer le menu suivant :</p>

<p><img alt="Cobian_Backup/screenshots-fr/07.png" src="/sites/securitybkp.ngoinabox.org/files/u5/cobian-fr/07.png" title="Cobian_Backup/screenshots-fr/07.png" /></p>

<p><i>Figure 5 : La fenêtre Destination – le menu du bouton Ajouter</i></p>

<p><strong>Sixième étape</strong>. <strong>Sélectionnez</strong> <i>Répertoire</i>. Une fenêtre de navigation s’ouvre par laquelle vous devez sélectionner le répertoire de destination de votre copie de sauvegarde.</p>

<p><strong>Commentaire</strong> : Si vous souhaitez créer différentes versions de la copie de sauvegarde du fichier, vous pouvez à ce moment sélectionner plusieurs répertoires. Si vous avez coché l’option <i>Manuellement</i>, vous devez saisir le chemin complet vers le répertoire où vous souhaitez conserver la copie de sauvegarde. Pour utiliser un serveur Internet distant pour stocker votre archive, <strong>sélectionnez</strong> l'option <i>Site FTP</i> (vous aurez besoins des détails de connexion appropriés pour vous connecter au serveur).</p>

<p>La fenêtre devrait maintenant ressembler à l’exemple ci-dessus, avec des fichiers et/ou des répertoires dans la zone source et des répertoires dans la zone destination. Toutefois, ne cliquez pas tout de suite sur <i>OK</i>! Nous devons encore planifier la création de nos copies de sauvegarde!</p>

<h3 id="a2.4Commentplanifiervostâchesdesauvegarde">2.4 Comment planifier vos tâches de sauvegarde</h3>

<p>La dernière partie que nous devons aborder afin que nos copies de sauvegarde automatiques soient fonctionnelles est la partie <i>Planification</i>. Cette partie vous permet de déterminer les moments où vous souhaitez que vos copies de sauvegarde soient créées.</p>

<p>Pour régler les options de planification, suivez les étapes énumérées ci-dessous :</p>

<p><strong>Première étape</strong>. <strong>Sélectionnez</strong> <i>Planification</i>, dans le menu de gauche, pour activer la fenêtre suivante :</p>

<p><img alt="Cobian_Backup/screenshots-fr/08.png" src="/sites/securitybkp.ngoinabox.org/files/u5/cobian-fr/08.png" title="Cobian_Backup/screenshots-fr/08.png" /></p>

<p><i>Figure 6 : Les Propriétés de MaSauvegarde affichant la fenêtre Type de planification.</i></p>

<p>Les options de <i>Type de planification</i> sont énumérées dans un menu défilant. Elles sont décrites ci-dessous :</p>

<p><i>Une fois</i> : La copie de sauvegarde sera créée une seule fois à la date et à l’heure que vous inscrivez dans la zone <i>Date/Heure</i>.</p>

<p><i>Quotidienne</i> : La copie de sauvegarde sera créée chaque jour à la date et à l’heure que vous inscrivez dans la zone <i>Date/Heure</i>.</p>

<p><i>Hebdomadaire</i> : La copie de sauvegarde sera créée le jour de la semaine que vous aurez choisi. Dans l’exemple ci-dessus, la copie est créée le vendredi. Vous pouvez aussi choisir une autre journée. La copie de sauvegarde sera créée selon les journées et l’heure inscrites dans la zone <i>Date/Heure</i>.</p>

<p><i>Mensuelle</i> : La copie de sauvegarde sera créée selon les journées choisies dans la boîte <i>mois</i> à l’heure inscrite dans la zone <i>Date/Heure</i>.</p>

<p><i>Annuelle</i> : La copie de sauvegarde sera créée selon les journées choisies dans la boîte <i>mois</i>, au cours du mois que vous aurez également choisi et à l’heure inscrite dans la zone <i>Date/Heure</i>.</p>

<p><i>Minuterie</i> : La copie de sauvegarde sera créée à plusieurs reprises aux intervalles inscrits dans la boîte <i>Minuteur</i> de la zone <i>Date/Heure</i>.</p>

<p><i>Manuellement</i> : Vous devrez exécuter la copie vous-même depuis la fenêtre principale du programme.</p>

<p><strong>Deuxième étape</strong>. <strong>Cliquez</strong> sur le bouton <i>OK</i>.</p>

<p><i>La planification des sauvegardes clôt le processus. Des copies de sauvegarde des fichiers sélectionnés seront désormais créées aux moments que vous avez déterminés.</i></p>

<p><img alt="Cobian_Backup/screenshots-fr/08.png" src="/sites/securitybkp.ngoinabox.org/files/u5/cobian-fr/08.png" title="Cobian_Backup/screenshots-fr/08.png" /></p>

<p><i>Figure 7 : Les propriétés de MaSauvegarde affichant le panneau </i>Type de planification</p>


