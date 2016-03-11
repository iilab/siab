

---

lang: fr
community: guide
type: tactics
legacy: True
child: True
weight: 2
depth: 3
title: Understanding censorship circumvention

---

<p>Si vous ne pouvez pas établir une connexion directe à un site parce qu’il est bloqué par l’une des méthodes présentées ci-dessus, il vous faudra trouver un moyen pour <a href="glossaire#Contournement" title="Contournement"><i>contourner</i></a> l’obstruction. Un serveur <a href="glossaire#Proxy" title="Proxy"><i>proxy</i></a> sûr, situé dans un pays qui ne filtre pas l’Internet, peut vous permettre ce type de contournement en allant chercher pour vous les pages auxquelles vous voulez accéder. Du point de vue de votre <a href="glossaire#FSI" title="FSI"><i>FSI</i></a>, vous donnerez simplement l’impression d’avoir établi une communication sécurisée avec un ordinateur inconnu (le serveur proxy) quelque part sur Internet.</p>

<p><img border="0" src="/sites/securitybkp.ngoinabox.org/security/files/img/2-fr.png" /></p>

<p>Bien sûr, l’agence gouvernementale responsable de la censure dans votre pays (ou la compagnie qui fait les mises à jour des programmes de filtrage) pourrait éventuellement découvrir que cet «&nbsp;ordinateur inconnu&nbsp;» est en réalité un proxy de contournement. Si cela se produit, l'<a href="glossaire#Adresse_IP" title="Adresse_IP"><i>adresse IP</i></a> du proxy pourrait être ajoutée à la «&nbsp;<a href="glossaire#Liste_noire" title="Liste_noire"><i>liste noire</i></a>&nbsp;» et, le cas échéant, ce dernier cessera de fonctionner pour vous. Cela dit, il faut habituellement un certain temps avant que les serveurs proxy ne soit identifiés et bloqués, et les gens qui conçoivent et améliorent ces outils sont au fait de ces risques. En général, ils se défendent en ayant recours à l’une ou l’autre des méthodes suivantes&nbsp;:</p>

<ul>
	<li>Les <b>proxys cachés</b> sont plus difficile à identifier que les proxys normaux. C’est l’une des raisons pour lesquelles il est important d’utiliser des proxys sécurisés, lesquels sont habituellement plus discrets. Cependant, le <a href="glossaire#Chiffrement" title="Chiffrement"><i>chiffrement</i></a> n’est qu’une partie de la solution. Les administrateurs d’un proxy, s’ils veulent que ce dernier reste caché, doivent être très prudents lorsqu’ils en révèlent l’emplacement à de nouveaux utilisateurs.</li>
</ul>

<ul>
	<li>Les <b>proxys jetables</b> peuvent facilement être remplacés lorsqu’ils sont bloqués. Il n’est pas particulièrement sécuritaire d’indiquer publiquement aux utilisateurs où ils peuvent trouver des proxys de rechange. C’est pourquoi les outils de contournement de ce type, la plupart du temps, essaient tout simplement de déjouer les censeurs en distribuant les nouveaux proxys plus vite que ces derniers sont capables de les bloquer.</li>
</ul>

<p>Au bout du compte, tant et aussi longtemps que vous serez en mesure de joindre un proxy pour chercher les services dont vous avez besoin, tout ce que vous aurez à faire est d’effectuer la requête et de visualiser les résultats à l’aide de l’application Internet appropriée. Habituellement, les détails de ce processus sont gérés soit automatiquement par le logiciel de contournement que vous installez sur votre ordinateur, soit en modifiant les paramètres de votre navigateur, ou encore en pointant votre navigateur vers la page d’un proxy basé sur le Web. Le réseau de connexion anonyme <a href="glossaire#Tor" title="Tor"><i>Tor</i></a>, abordé à la prochaine section, utilise la première méthode. Après cela, nous verrons quelques outils de contournement par proxy unique, dont le fonctionnement varie légèrement d’un modèle à un autre.</p>


