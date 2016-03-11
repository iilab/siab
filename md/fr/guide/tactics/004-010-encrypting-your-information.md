

---

lang: fr
community: guide
type: tactics
legacy: True
child: True
weight: 1
depth: 3
title: Encrypting your information

---

<p>&nbsp;</p>

<table cellpadding="5" cellspacing="0" style="border: 2pt dashed #008000; background-color: #e9e8a4">
	<tbody>
		<tr>
			<td><i>Pablo&nbsp;: Mais mon ordinateur est déjà protégé par le mot de passe de connexion à Windows&nbsp;! Ça ne suffit pas&nbsp;?</i><br />
			<br />
			<i>Claudia&nbsp;: En fait, les mots de passe de connexion à Windows sont réputés pour être faciles à craquer. De plus, quiconque parvient à manipuler ton ordinateur assez longtemps pour le redémarrer en glissant un LiveCD dans le lecteur de disques sera en mesure de copier l’ensemble de tes données sans se préoccuper du mot de passe. Si l’intrus a l’occasion de partir avec l’ordinateur, ne serait-ce que pour une courte période, tu cours encore plus de risques. Et ce n’est pas uniquement des mots de passe Windows dont tu devrais t’inquiéter. Les mots de passe de Microsoft Word ou d’Adobe Acrobat ne sont pas plus fiables.</i></td>
		</tr>
	</tbody>
</table>

<p><a href="glossaire#Chiffrement" title="Chiffrement"><i>Chiffrer</i></a> vos données, c’est un peu comme les déposer dans un coffre-fort verrouillé et sécurisé. Seules les personnes qui disposent de la combinaison (dans ce cas-ci, une clé de chiffrement ou une phrase secrète) peuvent accéder au contenu. Cette analogie est particulièrement appropriée au programme <a href="glossaire#TrueCrypt" title="TrueCrypt"><i>TrueCrypt</i></a> et autres logiciels semblables. Ces programmes, au lieu de protéger les fichiers individuellement, servent à créer des espaces sécurisés, nommés «&nbsp;volumes chiffrés&nbsp;», où vous pouvez stocker une quantité importante de fichiers. Ces outils, toutefois, ne protègent pas les fichiers qui se trouvent ailleurs sur votre ordinateur ou sur vos dispositifs de stockage portables.</p>

<p>&nbsp;</p>

<table cellpadding="5" cellspacing="0" style="border: 2pt dashed #008000; background-color: #e9e8a4">
	<tbody>
		<tr>
			<td><img align="middle" height="63" src="/sites/securitybkp.ngoinabox.org/files/u9/hand_web_trans.png" width="60" /> <b>Expérience pratique&nbsp;: se lancer avec le </b><i><a href="truecrypt_principale"><b>Guide pratique TrueCrypt</b></a></i></td>
		</tr>
	</tbody>
</table>

<p>Même si d’autres programmes offrent des fonctions de <a href="glossaire"> <i>chiffrement</i></a> tout aussi efficaces, le logiciel <a href="glossaire"><b>TrueCrypt</b> </a>contient plusieurs fonctions importantes vous permettant de concevoir votre stratégie de sécurité de l'information. Il offre la possibilité de <b>chiffrer de façon permanente la totalité du disque de votre ordinateur</b>, y compris tous vos fichiers, tous les fichiers temporaires créés au cours de votre travail, tous les programmes que vous avez installés et tous les fichiers du système d'exploitation Windows. TrueCrypt est compatible aux volumes <a href="glossaire"> <i>chiffrés</i></a> sur des dispositifs de stockage amovibles. Il fournit des fonctions de « déni plausible » décrites dans la section <a href="chapter_4_2" title="Chapitre 4.2"><i><b>Dissimuler vos données</b></i></a> ci-dessous. En outre, TrueCrypt repose sur une licence <a href="glossaire#FLOSS" title="FLOSS"><i>FLOSS</i></a>.</p>

<p>&nbsp;</p>

<table cellpadding="5" cellspacing="0" style="border: 2pt dashed #008000; background-color: #e9e8a4">
	<tbody>
		<tr>
			<td><i>Pablo&nbsp;: Bon, maintenant je suis inquiet. Qu’en est-il des autres utilisateurs sur un même ordinateur&nbsp;? Est-ce que cela signifie qu’ils peuvent lire les fichiers qui se trouvent dans le répertoire Mes documents&nbsp;? </i><br />
			<br />
			<i>Claudia&nbsp;: J’aime ta façon de t’inquiéter&nbsp;! Si ton mot de passe Windows ne te protège pas des intrus, comment pourrait-il te protéger des autres utilisateurs sur le même ordinateur&nbsp;? En fait, normalement, tout le monde peut voir ton dossier Mes documents. Les autres utilisateurs n’ont même pas besoin de recourir à des manœuvres sophistiquées pour accéder à tes fichiers. Même si le répertoire est défini comme «&nbsp;privé&nbsp;», il n’est toujours pas sécurisé, à moins que tu n’utilises un mécanisme de chiffrement.</i></td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>

<h3>Astuces concernant l’utilisation du chiffrement</h3>

<p>&nbsp;</p>

<p>Le stockage de données confidentielles comporte des risques pour vous et vos collègues. Le chiffrement des données contribue à réduire ces risques, mais ne les élimine pas complètement. La première mesure à prendre pour protéger des renseignements de nature délicate est de réduire le plus possible le nombre de ces renseignements que vous stockez sur votre ordinateur. À moins d’avoir une très bonne raison de conserver un fichier en particulier (ou une catégorie de données à l’intérieur d’un fichier) vous devriez tout simplement le supprimer. (À ce sujet, veuillez consulter le chapitre <a href="chapter-6" title="Chapitre 6"><i><b>6. Détruire définitivement des données sensibles</b></i></a>.) La deuxième étape est d’utiliser un bon programme de chiffrement, comme TrueCrypt.</p>

<p>&nbsp;</p>

<table cellpadding="5" cellspacing="0" style="border: 2pt dashed #008000; background-color: #e9e8a4">
	<tbody>
		<tr>
			<td><i>Claudia&nbsp;: Nous ne sommes peut-être pas obligés de conserver des renseignements qui pourraient servir à identifier nos témoins. Qu’en penses-tu&nbsp;? </i><br />
			<br />
			<i>Pablo&nbsp;: Je suis d’accord. Nous devrions consigner le strict minimum. De plus, nous devrions trouver un code simple pour protéger les noms et les lieux que nous devons absolument enregistrer.</i></td>
		</tr>
	</tbody>
</table>

<p>Pour revenir à l’analogie du coffre-fort, vous devriez gardez à l’esprit un certain nombre de questions lorsque vous utilisez TrueCrypt ou d’autres programmes du même genre. Peu importe le degré de robustesse de votre coffre-fort, cela ne vous servira à rien si vous laissez la porte ouverte. Lorsque votre volume TrueCrypt est «&nbsp;monté&nbsp;» (c.-à-d. quand vous pouvez vous-même accéder aux données qui s’y trouvent), vos données sont vulnérables. C’est pourquoi vous devriez toujours le garder fermé (démonté), sauf quand vous lisez ou modifiez les fichiers qui y sont stockés.</p>

<p>Il y a quelques situations où il est particulièrement important que vous vous rappeliez de démonter vos volumes chiffrés&nbsp;:</p>

<ul>
	<li>Démontez vos volumes chiffrés lorsque vous vous éloignez de votre ordinateur plus de quelques minutes. Même si vous avez l’habitude de laisser votre ordinateur sous tension pendant la nuit, assurez-vous de ne jamais laisser vos données sensibles à la portée des intrusions physiques ou numériques.</li>
	<li>Démontez vos volumes chiffrés avant d’éteindre votre ordinateur ou de le mettre en veille. Cela concerne aussi bien la fonction «&nbsp;veille&nbsp;» que la fonction «&nbsp;veille prolongée&nbsp;», qui sont habituellement utilisées sur les ordinateurs portables mais qui peuvent également se retrouver sur un ordinateur de bureau.</li>
	<li>Démontez toujours vos volumes chiffrés avant de permettre à qui que ce soit de manipuler votre ordinateur. Lorsque vous transportez votre ordinateur portable avec vous pour traverser un point de contrôle ou une frontière, il est très important que vous démontiez vos volumes chiffrés et éteigniez complètement votre ordinateur.</li>
	<li>Démontez vos volumes chiffrés avant de connecter une clé USB, ou tout autre dispositif de stockage amovible inconnu, à votre ordinateur (y compris les appareils qui appartiennent à vos amis, parents et collègues).</li>
	<li>Si vous conservez un volume chiffré sur une clé USB, rappelez-vous que de retirer la clé ne suffit pas nécessairement à déconnecter immédiatement le volume. Même si vous êtes dans une situation où vous êtes forcé de sécuriser vos fichiers en toute vitesse, vous devez démonter le volume comme d’habitude, arrêter le disque externe ou la clé, et ensuite déconnecter physiquement le dispositif en question. Il peut être utile de répéter cette séquence à quelques reprises pour trouver la façon la plus rapide de procéder.</li>
</ul>

<p>Conseil&nbsp;: Si vous décidez de garder votre volume TrueCrypt sur une clé USB, il est utile d’y conserver également une copie du programme TrueCrypt. Cela vous permettra d’accéder à vos données à partir d’un autre ordinateur que le vôtre. Évidemment, les consignes de sécurité élémentaires s’appliquent&nbsp;: si vous avez un doute raisonnable que l’ordinateur est infecté par des <a href="glossaire#Logiciel_malveillant" title="Logiciel_malveillant"><i>logiciels malveillants</i></a>, vous ne devriez probablement pas y saisir votre mot de passe ni accéder à vos données sensibles.</p>


