

---

lang: fr
community: guide
type: tactics
legacy: True
child: True
weight: 2
depth: 3
title: Hiding your sensitive information

---

<p>L’inconvénient principal de garder un coffre-fort à la maison ou au bureau (sans mentionner d’en transporter un dans sa poche&nbsp;!) est que ces objets ne sont habituellement pas très discrets. Plusieurs personnes craignent que l’utilisation de procédés de <a href="glossaire#Chiffrement" title="Chiffrement"><i>chiffrement</i></a> ne les incrimine. C’est une préoccupation raisonnable. Même si les raisons légitimes de chiffrer des données sont beaucoup plus nombreuses que les raisons illégitimes, cette menace n’en est pas moins très réelle. Essentiellement, il existe deux raisons pour lesquelles une personne n’aurait pas intérêt à utiliser des programmes comme TrueCrypt&nbsp;: l’éventuel risque d’auto incrimination; et le risque d’indiquer très précisément où se trouvent vos renseignements les plus sensibles.</p>

<p>&nbsp;</p>

<h3><a name="tenir_compte_du_risque_d_auto-incrimination" title="tenir_compte_du_risque_d_auto-incrimination"></a>Tenir compte du risque d’auto incrimination</h3>

<p>&nbsp;</p>

<p>Les procédés de chiffrement sont illégaux dans certains pays, ce qui signifie que le téléchargement, l’installation ou l’utilisation de logiciels de chiffrement, en tant que tels, constituent des infractions criminelles. Si la police, l’armée ou les services secrets font partie des groupes à qui vous souhaitez cacher des renseignements, l’infraction à ces lois pourrait être utilisée comme prétexte pour placer vos activités sous enquête ou harceler votre organisme. En fait, à dire vrai, ce type de menace n’a pas toujours de lien avec la légalité des logiciels dont il est question. Dans tous les cas où le simple fait d’être associé de près ou de loin à l’utilisation de programmes de chiffrement peut entraîner des accusations d’activités criminelles ou d’espionnage (et ce, sans égard à ce qui se trouve réellement à l’intérieur des volumes chiffrés), il est très important de réfléchir longuement avant de déterminer si l’utilisation de tels programmes est vraiment appropriée à la situation particulière de votre organisme.</p>

<p>Si vous êtes effectivement dans une situation épineuse, vous avez quelques options&nbsp;:</p>

<ul>
	<li>Vous pouvez simplement éviter d’utiliser des programmes de sécurisation de données. Cela vous oblige à ne conserver strictement que des données non confidentielles ou à inventer un système de code personnalisé pour protéger vos renseignements sensibles.</li>
	<li>Vous pouvez recourir à la <a href="glossaire#Steganographie" title="Steganographie"><i>stéganographie</i></a>, une technique qui consiste à dissimuler vos données confidentielles au lieu de les chiffrer. Il existe des outils qui permettent de faciliter le recours à ce procédé, mais leur utilisation exige beaucoup de préparation et, de toute façon, vous risquez quand même de vous incriminer devant les groupes ou personnes qui apprendraient que vous avez utilisé ces outils.</li>
	<li>Vous pouvez essayer de stocker tous vos renseignements sensibles dans un compte webmail, mais cela nécessite une bonne connexion réseau et une connaissance assez avancée de l’informatique et des services Internet. Par ailleurs, vous ne pouvez recourir à cette méthode que si le chiffrement réseau est moins incriminant que le chiffrement de fichiers. Surtout, il vous faut à tout prix éviter de copier par accident des renseignements sensibles sur votre ordinateur… et de les y oublier.</li>
	<li>Vous pouvez stocker vos données sensibles ailleurs que sur votre ordinateur. Sur une clé USB ou un disque dur portable, par exemple. Par contre, ces dispositifs sont habituellement plus susceptibles d’être perdus ou confisqués que les ordinateurs de bureau. C’est pourquoi il est généralement fortement déconseillé d’y stocker des renseignements sensibles non chiffrés.</li>
</ul>

<p>Selon les circonstances, vous pouvez employer l’une ou l’autre, ou une combinaison, des tactiques énumérées ci-dessus. Néanmoins, même dans les cas où les risques d’auto incrimination sont importants, le recours à <a href="glossaire#TrueCrypt" title="TrueCrypt"><i>TrueCrypt</i></a> peut s’avérer la solution la plus sûre. Il est alors particulièrement important de déguiser le plus efficacement possible vos volumes chiffrés.</p>

<p>Pour faire en sorte que votre volume chiffré soit moins suspect, vous pouvez le renommer pour lui donner l’aspect d’un autre type de fichier. Par exemple, vous pouvez attribuer au fichier l’extension de format <i>.iso</i> pour lui donner l’aspect d’une image CD (cela est particulièrement approprié pour des volumes d’environ 700 Mo). D’autres types d’extension seraient plus réalistes pour des volumes plus petits. C’est un peu comme si vous dissimuliez votre coffre-fort derrière un tableau accroché au mur de votre bureau. L’astuce ne résistera peut-être pas à une inspection minutieuse, mais elle offre tout de même un minimum de protection. Vous pouvez également renommer le programme TrueCrypt lui-même si vous l’avez stocké comme n’importe quel autre fichier quelque part sur votre disque dur ou sur une clé USB, au lieu de l’installer comme vous le feriez normalement pour tout autre programme. Le <a href="truecrypt_principale" title="Guide pratique TrueCrypt"><i><b>Guide pratique TrueCrypt</b></i></a> vous explique comment faire cela.</p>

<p>&nbsp;</p>

<h3>Tenir compte du risque d’indiquer l’emplacement de vos données de nature délicate</h3>

<p>&nbsp;</p>

<p>Dans certaines circonstances, vous serez peut-être moins préoccupé par les conséquences éventuelles d’être «&nbsp;pris&nbsp;» avec des logiciels de chiffrement sur votre ordinateur ou votre clé USB que par le fait que votre volume chiffré risque de révéler précisément où se trouvent les renseignements que vous souhaitez protéger. Bien que, dans un tel cas, personne ne soit en mesure de lire les données, un intrus éventuel saura que lesdites données sont là et que vous avez pris des précautions extraordinaires pour les cacher. Cela vous expose aux diverses méthodes non techniques auxquelles votre intrus pourra recourir pour accéder aux données, comme l’intimidation, le chantage, les interrogatoires ou la torture. C’est dans une situation comme celle-là que la fonction de «&nbsp;possibilité de démenti&nbsp;» de TrueCrypt (abordée en détails ci-dessous) entre en jeu.</p>

<p>La fonction de «&nbsp;possibilité de démenti&nbsp;» de TrueCrypt est un des éléments qui confèrent à ce programme une certaine supériorité sur les autres programmes de chiffrement de données. Cette fonction peut être vue comme une forme singulière de stéganographie, qui vous permet de cacher vos renseignements les plus sensibles parmi des données dont la nature est moins délicate. C’est un peu comme si vous installiez un «&nbsp;double fond&nbsp;» invisible dans votre coffre-fort pas-vraiment-subtil. Si un intrus parvient à vous soutirer la clé, où vous force à lui donner la combinaison du coffre-fort, il y trouvera des «&nbsp;leurres&nbsp;» convaincants (des renseignements moins importants pour vous, mais qui satisferont tout de même sa curiosité), mais pas les renseignements que vous voulez vraiment protéger.</p>

<p>Vous et vous seul savez que votre coffre-fort contient un compartiment secret. Cela vous permet de «&nbsp;démentir&nbsp;» que vous cachez d’autres secrets que ceux que vous avez déjà révélés à l’intrus. Cela est particulièrement pratique dans les situations où vous êtes forcé, pour une raison ou une autre, de révéler votre mot de passe (par ex. parce que vous, vos associés, collègues, parents ou amis êtes la cible de menaces juridiques ou physiques). Le but de cette fonction est de vous donner la possibilité de vous soustraire à une situation potentiellement dangereuse, et ce, même lorsque vous choisissez de continuer à protéger vos données. Par contre, comme nous l’avons vu à la section <a href="#tenir_compte_du_risque_d_auto-incrimination" title="Tenir compte du risque d’auto incrimination"><i><b>Tenir compte du risque d’auto incrimination</b></i></a>, cette fonction n’est pas vraiment utile si le simple fait d’être pris avec un coffre-fort dans votre bureau entraîne pour vous ou votre organisme des conséquences graves et/ou inacceptables.</p>

<p>La fonction de «&nbsp;possibilité de démenti&nbsp;» de TrueCrypt vous permet de stocker un «&nbsp;volume caché&nbsp;» à l’intérieur d’un volume chiffré standard. Vous ne pouvez ouvrir ce volume qu’avec un mot de passe différent de celui utilisé pour ouvrir le volume standard. Même si un intrus spécialiste parvient à accéder au volume standard, il lui sera tout simplement impossible de prouver l’existence d’un volume caché. Bien sûr, cette personne pourrait très bien savoir que le programme TrueCrypt offre la possibilité de dissimuler des données de cette façon, alors il n’y a aucune garantie que la menace disparaîtra lorsque vous révélerez le mot de passe de «&nbsp;diversion&nbsp;». Par contre, plusieurs personnes utilisent TrueCrypt sans pour autant se servir de la fonction de «&nbsp;volume caché&nbsp;» et, en règle générale, il est pratiquement impossible de déterminer par analyse informatique si un volume chiffré comporte un tel «&nbsp;double fond&nbsp;». Cela dit, il vous revient entièrement de vous assurer que l’existence de votre volume caché ne soit pas révélée par des moyens non techniques&nbsp;: ne laissez jamais le volume caché inutilement ouvert et ne créez pas de raccourcis vers les fichiers qu’il contient, par exemple. Les liens indiqués à la section <a href="chapter_4_3" title="Chapitre 4.3"><i><b>Lecture complémentaire</b></i></a>, ci-dessous, offrent des conseils supplémentaires à ce sujet.</p>

<p>&nbsp;</p>

<table cellpadding="5" cellspacing="0" style="border: 2pt dashed #008000; background-color: #e9e8a4">
	<tbody>
		<tr>
			<td><i>Claudia&nbsp;: Bon, alors nous n’avons qu’à balancer des trucs sans importance dans le volume standard et placer tous les témoignages importants dans le volume caché. As-tu des vieux PDF ou quelque chose du genre qu’on pourrait utiliser comme diversion&nbsp;? </i><br />
			<br />
			<i>Pablo&nbsp;: En fait, je pensais justement à ça. Je me disais que le principe de ce stratagème est de révéler le mot de passe du volume standard uniquement si nous n’avons aucun autre choix, pas vrai&nbsp;? Mais pour que cela soit convaincant, nous devons nous assurer que les fichiers que nous livrons comme leurres aient l’air d’être importants, tu ne crois pas&nbsp;? Sinon, pourquoi prendrions-nous la peine de le chiffrer&nbsp;? Peut-être devrions-nous utiliser comme leurres des documents ayant trait à nos finances, par exemple, ou encore une liste de faux mots de passe.</i></td>
		</tr>
	</tbody>
</table>


