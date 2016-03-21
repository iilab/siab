

---

lang: fr
community: guide
type: tactics
legacy: True
child: True
weight: 1
depth: 3
title: Understanding Internet censorship

---

<p>Des recherches menées par des organismes comme <a href="http://opennet.net/" title="OpenNet Initiative">OpenNet Initiative (ONI)</a>&nbsp;[1] et <a href="http://www.rsf.org/" title="Reporters sans frontières">Reporters sans frontières (RSF)</a>&nbsp;[2] indiquent que plusieurs pays ont recours au filtrage d’un vaste éventail de contenus à caractère social ou politique (et/ou de renseignements étant rattachés au concept de «&nbsp;sécurité nationale&nbsp;»), sans toutefois publier des listes précises des contenus bloqués. Bien entendu, les agences qui souhaitent limiter l’accès de leurs citoyens à Internet font aussi de leur mieux pour bloquer les serveurs <a href="glossaire#Proxy" title="Proxy"><i>proxy</i></a> et les sites Internet qui offrent des outils et des instructions pour aider les utilisateurs à <a href="glossaire#Contournement" title="Contournement"><i>contourner</i></a> les mesures de filtrage.</p>

<p>Malgré le droit à l’information garanti par l’article 19 de la Déclaration universelle des droits de la personne, le nombre des pays qui emploient des mesures de censure sur Internet n’a pas cessé d’augmenter au cours des quelques dernières années. Alors que le filtrage des contenus sur Internet est de plus en plus répandu, il en va de même des techniques et outils de contournement créés, déployés et distribués par des activistes, des programmeurs et des bénévoles un peu partout dans le monde.</p>

<p>Avant d’explorer les diverses méthodes par lesquelles il est possible de contourner la censure sur Internet, vous devriez d’abord avoir une bonne compréhension du fonctionnement de ces filtres. Pour ce faire, il est utile de se représenter un modèle simplifié de votre connexion Internet.</p>

<p>&nbsp;</p>

<h3>Votre connexion Internet</h3>

<p>&nbsp;</p>

<p><img border="0" src="/sites/securitybkp.ngoinabox.org/security/files/img/1-fr.png" /></p>

<p>La première étape de votre connexion à Internet est habituellement le lien qui est établi par votre <a href="glossaire#FSI" title="FSI"><i>fournisseur de services Internet (FSI)</i></a> à votre domicile, bureau, école, bibliothèque ou café Internet. Le FSI assigne à votre ordinateur une <a href="glossaire#Adresse_IP" title="Adresse_IP"><i>adresse IP</i></a>, que divers services Internet utilisent pour vous identifier et vous transmettre de l’information, tel que les courriels et les sites Internet que vous cherchez. Quiconque connaît votre adresse IP peut plus ou moins facilement déterminer dans quelle ville vous vous trouvez. Certaines agences influentes dans votre pays peuvent même utiliser ce renseignement pour déterminer très exactement votre position.</p>

<ul>
	<li><b>Votre FSI</b> peut déterminer à quelle adresse vous êtes situé ou quelle ligne téléphonique vous utilisez si vous accédez à Internet via un modem.</li>
	<li><b>Le café Internet, la bibliothèque ou le commerce privé d’où vous travaillez</b> peut déterminer quel ordinateur vous utilisez à tel ou tel moment, ainsi que le port ou le point d’accès sans-fil par lequel vous êtes connecté.</li>
	<li><b>Les agences gouvernementales </b> peuvent facilement obtenir ces renseignements, du fait de leur influence sur ces organismes.</li>
</ul>

<p>À ce point, votre FSI s’en remet à l’infrastructure du réseau existant dans votre pays pour connecter ses utilisateurs, vous y compris, au reste du monde. À l’autre bout de la connexion, le site ou le service Internet auquel vous accédez a dû passer par un processus similaire, ayant lui aussi reçu des adresses IP de la part d’un FSI dans le pays où il est hébergé. Même sans plus de détails techniques, un modèle simplifié comme celui-là pourra vous être utile pour tenir compte des différents outils qui permettent de contourner les filtres tout en restant anonyme sur Internet.</p>

<p>&nbsp;</p>

<h3>Comment les sites Internet sont-ils bloqués</h3>

<p>&nbsp;</p>

<p>Essentiellement, lorsque vous souhaitez visiter une page Web, vous indiquez l’adresse IP du site en question à votre FSI et vous lui demandez d’établir une connexion entre vous et le FSI du serveur Web où est hébergé ce site. Si vous avez une connexion Internet non filtrée, c’est précisément ce qu’il fera. Par contre, si vous vous trouvez dans un pays qui exerce de la censure sur Internet, il consultera d’abord une «&nbsp;<a href="glossaire#Liste_noire" title="Liste_noire"><i>liste noire</i></a>&nbsp;» de sites interdits et déterminera ensuite s’il peut consentir ou non à votre requête.</p>

<p>Dans certains cas, c’est une agence centrale, et non pas les FSI, qui s’occupe du filtrage. La plupart du temps, une «&nbsp;liste noire&nbsp;» contient des <a href="glossaire#Nom_de_domaine" title="Nom_de_domaine"><i>noms de domaine</i></a>, comme <a href="http://www.blogger.com" title="www.blogger.com">www.blogger.com</a>, plutôt que des adresses IP. Dans certains pays, des logiciels de filtrage contrôlent carrément votre connexion au lieu de bloquer votre accès à certaines adresses en particulier. Ce type de programme balaie toutes les requêtes que vous effectuez (et tous les sites Internet qui tentent de vous répondre) afin de détecter certains mots-clé et, selon ses conclusions, décider si vous pouvez ou non voir les résultats de vos requêtes.</p>

<p>Pire encore, lorsqu’un site Internet est bloqué, il est fort possible que vous ne le sachiez même pas. Alors que certains filtres présentent une «&nbsp;page de blocage&nbsp;», qui vous explique pourquoi une page en particulier a été censurée, d’autres affichent des messages d’erreur pour tromper les utilisateurs. Ces messages indiquent que la page ne peut être trouvée, par exemple, ou qu’il y a une erreur dans l’adresse.</p>

<p>En général, quand il est question de censure sur Internet, il est plus simple d’adopter une attitude carrément «&nbsp;pessimiste&nbsp;» que d’étudier attentivement toutes les forces et les faiblesses des technologies de filtrage utilisées dans votre pays. En d’autres termes, vous avez avantage à tenir pour acquis que&nbsp;:</p>

<ul>
	<li>Quelqu’un contrôle vos activités sur Internet pour détecter certains mots-clé&nbsp;;</li>
	<li>Le filtrage se produit directement au niveau du FSI&nbsp;;</li>
	<li>Les sites bloqués sont mis à l’index selon leurs adresses IP et leurs noms de domaine&nbsp;;</li>
	<li>Il est fort probable que l’on vous fournisse une raison ambiguë ou trompeuse pour expliquer pourquoi la connexion à un site donné a échoué.</li>
</ul>

<p>Comme les outils de contournement les plus efficaces peuvent aussi bien être utilisés contre l’une ou l’autre de ces méthodes de filtrage, il est en fait plutôt utile d’adhérer à ces hypothèses «&nbsp;pessimistes&nbsp;».</p>

<p>&nbsp;</p>

<table cellpadding="5" cellspacing="0" style="border: 2pt dashed #008000; background-color: #e9e8a4">
	<tbody>
		<tr>
			<td><i>Mansour&nbsp;: Alors, si un jour ou l’autre je ne peux plus accéder au blog, mais qu’un camarade dans un autre pays y parvient toujours, est-ce que cela signifie que le gouvernement a finalement réussi à le bloquer&nbsp;? </i><br />
			<br />
			<i>Magda&nbsp;: Pas nécessairement. Il est possible qu’un problème d’une toute autre nature touche uniquement les utilisateurs qui tentent de joindre le site à partir d’ici. Il peut aussi s’agir d’un problème avec ton ordinateur qui ne survient qu’avec certains types de pages Web. Cela dit, tu es sur la bonne voie. Pour en avoir le cœur net, tu devrais essayer de visiter le site à l’aide d’un outil de contournement. Après tout, la plupart de ces programmes reposent sur l’utilisation de serveurs proxy externes, ce qui revient à peu près à demander à un ami à l’étranger de tester le site pour toi, sauf que tu le fais toi-même.</i></td>
		</tr>
	</tbody>
</table>


