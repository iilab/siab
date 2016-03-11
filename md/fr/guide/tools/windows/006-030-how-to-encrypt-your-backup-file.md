

---

lang: fr
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: How to Encrypt Your Backup File

---

<p>Le chiffrement peut s'avérer nécessaire si vous voulez protéger vos copies de sauvegarde des accès non autorisés. Le <i>Chiffrement</i> est le processus de codification, ou d’embrouillage, des données : une fois chiffrées, les données sont inintelligibles pour quiconque ne détient pas la clé nécessaire au décodage du message. Pour plus de renseignements sur le chiffrement, veuillez consulter le chapitre <a href="chapter-4" target="_blank" title="4. Protéger les données sensibles stockées sur votre ordinateur">4. Protéger les données sensibles stockées sur votre ordinateur</a> du livret pratique.</p>

<h4>4.1 Comment chiffrer vos archives</h4>

<p>La fenêtre <i>Cryptage avancé</i> sert à préciser la méthode de chiffrement que vous souhaitez utiliser.</p>

<p><strong>Étape 1</strong> : <strong>Cliquez</strong> sur le menu défilant <i>Type de cryptage</i> pour activer la liste des diverses méthodes de chiffrement :</p>

<p><img alt="Cobian_Backup/screenshots-fr/13.png" src="/sites/securitybkp.ngoinabox.org/files/u5/cobian-fr/13.png" title="Cobian_Backup/screenshots-fr/13.png" /></p>

<p><i>Figure 11 : Le menu défilant des types de chiffrement</i></p>

<p>Par souci de simplicité, nous vous recommandons de choisir entre les méthodes <i>Blowfish</i> et <i>Rijndael</i> (128 octets). Ces méthodes sont très sûres et vous permettent d’accéder aux données chiffrées à l’aide d’une phrase de protection que vous choisissez.</p>

<p><strong>Deuxième étape</strong>: <strong>Sélectionnez</strong> le <i>type de chiffrement</i> de votre choix.</p>

<p><strong>Commentaire</strong> : <i>Rijndael</i> et <i>Blowfish</i> s’équivalent en ce qui concerne le niveau de sécurité. <i>DES</i> est plus faible, mais le processus de chiffrement est plus rapide.</p>

<p><strong>Troisième étape</strong> : <strong>Saisissez </strong> (deux fois) la phrase de protection dans les boîtes appropriées, tel que dans l’exemple suivant :</p>

<p><img alt="Cobian_Backup/screenshots-fr/17.png" src="/sites/securitybkp.ngoinabox.org/files/u5/cobian-fr/17.png" title="Cobian_Backup/screenshots-fr/17.png" /></p>

<p><i>Figure 12 : Les zones de texte du Type de chiffrement et de la phrase de protection</i></p>

<p>La force de la phrase de protection est indiquée par la barre <i>Qualité de la phrase de protection</i>. Plus la barre bouge vers la droite, plus la phrase de protection est forte. Voir le chapitre 3. Créer et sauvegarder des mots de passe sûrs du livret pratique pour obtenir des directives sur la création et le stockage de mots de passe sûrs.</p>

<p><strong>Quatrième étape</strong> : <strong>Cliquez</strong> sur le bouton <i>OK</i>.</p>

<h4>4.2 Comment déchiffrer votre archive</h4>

<p><strong>Étape 2</strong>. <strong>Sélectionnez</strong> : <strong>Outils &gt; Décryptage et clés</strong></p>

<p><img alt="Cobian_Backup/screenshots-fr/22.png" src="/sites/securitybkp.ngoinabox.org/files/u5/cobian-fr/22.png" title="Cobian_Backup/screenshots-fr/22.png" /></p>

<p><i>Figure 13 : Le menu Outils avec l'option Décryptage et Clés sélectionnée</i></p>

<p>Ceci activera la fenêtre <i>Décryptage et clés</i> :</p>

<p><img alt="Cobian_Backup/screenshots-fr/23.png" src="/sites/securitybkp.ngoinabox.org/files/u5/cobian-fr/23.png" title="Cobian_Backup/screenshots-fr/23.png" /></p>

<p><i>Figure 14 : La fenêtre Décryptage et Clés dans Cobian Backup 8</i></p>

<p><strong>Deuxième étape</strong>. <strong>Cliquez</strong> sur le bouton <i>Source</i> pour sélectionner l’archive que vous souhaitez déchiffrer.</p>

<p><strong>Troisième étape</strong>. <strong>Cliquez</strong> sur le bouton <i>Afficher</i> pour sélectionner le répertoire où l’archive doit être stockée.</p>

<p><strong>Quatrième étape</strong>. <strong>Sélectionnez</strong> le type de chiffrement (que vous avez choisi à la section <strong>4.1 Comment chiffrer vos archives</strong>) dans le menu défilant <i>Nouvelles méthodes<strong>. </strong></i></p>

<p><img alt="Cobian_Backup/screenshots-fr/28.png" src="/sites/securitybkp.ngoinabox.org/files/u5/cobian-fr/28.png" title="Cobian_Backup/screenshots-fr/28.png" /></p>

<p><i>Figure 15 : Le menu défilant Nouvelles méthodes</i></p>

<p><strong>Cinquième étape</strong>. <strong>Sélectionnez</strong> la méthode de chiffrement appropriée (celle que vous avez utilisée pour chiffrer votre copie de sauvegarde).</p>

<p><strong>Sixième étape</strong>. <strong>Saisissez</strong> votre <i>Phrase de protection</i> dans la zone de texte du même nom.</p>

<p><strong>Septième étape</strong>. <strong>Cliquez</strong> sur le bouton <i>Décrypter</i>.</p>

<p>Les fichiers seront déchiffrés vers l’emplacement que vous avez spécifié. Si les fichiers étaient également compressés, vous devrez les décompresser en suivant les étapes énumérées à la section <a href="cobian_compress" target="_blank" title="Section 3.2 Comment décompresser vos archives"><strong>3.2 Comment décompresser vos archives</strong>. </a></p>


