

---

lang: fr
community: guide
type: tactics
legacy: True
child: True
weight: 3
depth: 3
title: Securing other Internet communication tools

---

<p>Tout comme le courrier électronique, les programmes de messagerie instantanée et de <a href="glossaire#VoIP" title="VoIP"><i>VoIP</i></a> peuvent être sécurisés ou non, selon les outils que vous choisissez et l’utilisation que vous en faites.</p>

<p>&nbsp;</p>

<h3>Sécuriser votre programme de messagerie instantanée</h3>

<p>&nbsp;</p>

<p>La messagerie instantanée, aussi appelée <i>chat</i> ou «&nbsp;clavardage&nbsp;», n’est habituellement pas sécurisée et, à cet égard, peut s’avérer tout aussi vulnérable que le courrier électronique. Heureusement, il existe des logiciels conçus pour garantir la confidentialité de vos séances de clavardage. Comme pour les courriels, cependant, une voie de communication sécurisée exige que vos correspondants par <i>chat</i> et vous utilisiez les mêmes logiciels et respectiez les mêmes mesures de précaution.</p>

<p><a href="glossaire#Pidgin" title="Pidgin"><i>Pidgin</i></a> est un programme de clavardage qui fonctionne avec la plupart des protocoles de messagerie instantanée existants, ce qui signifie que vous pouvez facilement commencer à l’utiliser sans pour autant devoir changer vos noms de comptes ou recréer votre liste de contacts. Pour mener des conversations confidentielles <a href="glossaire#Chiffrement" title="Chiffrement"><i>chiffrées</i></a> avec Pidgin, vous devrez installer et activer le module complémentaire Off-the-Record (<a href="glossaire#OTR" title="OTR"><i>OTR</i></a>). Heureusement, cette opération est plutôt simple.</p>

<p>&nbsp;</p>

<table cellpadding="5" cellspacing="0" style="border: 2pt dashed #008000; background-color: #e9e8a4">
	<tbody>
		<tr>
			<td><img align="middle" height="63" src="/sites/securitybkp.ngoinabox.org/files/u9/hand_web_trans.png" width="60" /> <b>Expérience pratique&nbsp;: se lancer avec le <i><a href="pidgin_principale"><b>Guide pratique Pidgin</b></a></i> </b></td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>

<table cellpadding="5" cellspacing="0" style="border: 2pt dashed #008000; background-color: #e9e8a4">
	<tbody>
		<tr>
			<td><i>Pablo&nbsp;: Si le service webmail de Yahoo n’est pas sécurisé, est-ce que cela signifie que Yahoo Chat est également non sécurisé&nbsp;? </i><br />
			<br />
			<i>Claudia&nbsp;: Tu dois surtout te rappeler que si l’on veut utiliser la messagerie instantanée pour discuter de ce rapport, on doit d’abord s’assurer que chacune des personnes impliquées a installé et configuré Pidgin et le module OTR. Si c’est le cas, nous pouvons utiliser Yahoo Chat ou n’importe quel autres service semblable.</i></td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>

<h3>Sécuriser votre programme de VOIP (voix sur IP)</h3>

<p>&nbsp;</p>

<p>Les appels entre utilisateurs de VoIP sont habituellement gratuits. Certains programmes vous permettent de placer des appels bon marché à des téléphones réguliers, y compris vers l’étranger. Inutile de dire que ces outils peuvent s’avérer extrêmement utiles. <a class="ext-link" href="http://www.skype.com" title="Site Internet de Skype"><span class="icon">Skype</span></a>, <a class="ext-link" href="http://jitsi.org/" title="Site Internet de Jitsi"><span class="icon">Jitsi</span></a>, <a class="ext-link" href="http://www.google.com/talk" title="Site Internet de Google Talk"><span class="icon">Google Talk</span></a>, <a class="ext-link" href="http://voice.yahoo.com/" title="Site Internet de Yahoo Voice"><span class="icon">Yahoo! Voice</span></a> et <a class="ext-link" href="http://get.live.com/messenger" title="Site Internet de MSN Messenger"><span class="icon">MSN Messenger</span></a> figurent parmi les programmes de VoIP les plus répandus.</p>

<p>Normalement, les communications par voix sur réseau IP ne sont pas plus sûres que les courriels ou les chats non sécurisés. Lorsque vous utilisez ce type de communication pour échanger des informations sensibles, il est important de choisir un programme en état de chiffrer l'appel depuis votre ordinateur jusqu'à celui du destinataire. De même, il vaut mieux utiliser des logiciels libres et Open Source ; de préférence ceux qui ont été examinés, testés et recommandés par un groupe ou une communauté en lesquels vous avez confiance. En considération des critères exposés ci-dessus, nous conseillons l'utilisation de <a href="http://jitsi.org/" title="Jitsi"><i>Jitsi</i></a> comme logiciel de VoIP.</p>

<p><b>Remarques sur la sécurité de Skype</b></p>

<p><a href="https://securityinabox.org/fr/glossaire" title="Skype"><i>Skype</i></a> est un logiciel de messagerie instantanée et vocale très courant, et avec lequel on peut également effectuer des appels à destination de numéros fixes comme mobiles. Malgré sa popularité, ce logiciel n'est pas un choix sûr pour plusieurs raisons. Certaines de ces raisons sont décrites ci-dessous.</p>

<p>Selon Skype, les messages et les appels vocaux sont <a href="https://securityinabox.org/fr/glossaire" title="chiffrés"><i>chiffrés</i></a>. Ceci ne peut donc être le cas que lorsque toutes les personnes impliquées dans l'échange utilisent un logiciel Skype. Skype ne chiffre donc ni les appels à destination de téléphones ni les textes envoyés sous forme de SMS.</p>

<p>Si toutes les personnes impliquées dans l'échange utilisent un logiciel Skype (authentique), son chiffrement peut être plus sûr que lors d'un appel ordinaire via téléphone. Mais comme Skype est un logiciel à code source fermé, ce qui rend impossible tout contrôle ou évaluation indépendamment de ses déclarations, il est également impossible de vérifier si Skype protège vraiment ses utilisateurs, leurs informations et communications. Le <i><a href="https://securityinabox.org/fr/chapter-1"><b>chapitre 1. Protéger votre ordinateur contre les logiciels malveillants et les pirates</b></a></i> présente clairement les avantages des logiciels Free/Libre Open-Source (<a href="glossaire#FLOSS" title="FLOSS"><i>FLOSS</i></a>), à la section <a href="chapter_1_4" title="Chapitre 1.4"><i><b>Actualiser vos logiciels</b></i></a>.</p>

<p>Nous ne recommandons donc pas l'usage de Skype. Si vous décidez toutefois de l'utiliser pour échanger des informations sensibles, prenez un certain nombre de précautions:</p>

<p>- Téléchargez Skype à partir de son site officiel <a class="ext-link" href="http://www.skype.com" title="www.skype.com"><span class="icon">www.skype.com</span></a> afin d'éviter un programme Skype infecté par un logiciel espion. Il est important de toujours vérifier l'URL afin d'être sûr que vous êtes connecté au site officiel. Dans certains pays, le site de Skype est bloqué et/ou de faux sites prétendant être Skype circulent sur le net. Dans de nombreux cas, la version de Skype disponible est probablement infectée par un logiciel malveillant, conçu pour espionner les communications. Utilisez les outils de contournement décrits dans le <i><a href="https://securityinabox.org/fr/chapter-8"><b>chapitre 8. Préserver votre anonymat et contourner la censure sur Internet</b></a></i> pour vous connecter au site Internet de Skype et télécharger une version authentique du logiciel ; que vous souhaitiez l'installer ou le mettre à jour.</p>

<p>- Il est très important de modifier votre mot de passe Skype régulièrement. Skype assure des connexions multiples à partir d'emplacements différents et ne vous informe pas sur le nombre de sessions simultanées. Si votre mot de passe est compromis, vous courez le risque que n'importe qui puisse se connecter à votre place. Toutes les sessions connectées reçoivent toutes les communications par texte et ont accès à l'historique des appels. Le seul moyen de stopper ces sessions sournoises est de modifier son mot de passe (en forçant une reconnexion).</p>

<p>- Il est également conseillé de régler les paramètres de confidentialité sur Skype de façon à ce que l'historique des conversations ne soit pas conservé.</p>

<p>- Il est recommandé de désactiver la fonction d'acceptation automatique de fichiers entrants. C'est par ce biais que des logiciels malveillants/espions ont pu parfois être introduits sur des ordinateurs.</p>

<p>- Vérifiez toujours indépendamment l'identité de la personne avec laquelle vous communiquez. Ceci est plus facile à effectuer lors de communications vocales - si vous connaissez la personne à laquelle vous souhaitez parler.</p>

<p>- Demandez-vous s'il est nécessaire que votre nom d'utilisateur Skype soit votre nom réel ou celui de votre organisation.</p>

<p>- Prévoyez d'autres moyens de communication - Skype peut devenir indisponible à tout moment.</p>

<p>- Exprimez-vous prudemment. Développez un système codé pour discuter des sujets sensibles sans avoir à utiliser la terminologie spécifique.</p>

<p>Malgré la popularité de Skype, les préoccupations mentionnées ci-dessus font douter de son efficacité en matière de sécurité. Bref, vous avez tout avantage à utiliser des logiciels tels que Jitsi pour vos communications vocales et <a href="https://securityinabox.org/fr/glossaire" title="Pidgin"><i>Pidgin</i></a> avec le module complémentaire <a href="https://securityinabox.org/fr/glossaire" title="OTR"><i>OTR</i></a> pour une messagerie instantanée sécurisée.</p>

<p>&nbsp;</p>


