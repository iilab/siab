

---

lang: fr
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 2
depth: 3
title: How to Use OTR to Initiate a Secure Messaging Session in Pidgin

---

Sommaire des sections de cette page:

- [**3.0 À propos de Pidgin et d'OTR**](#3.0)
- [**3.1 Comment configurer le plugin Pidgin-OTR**](#3.1)
- [**3.2 La première étape - Comment produire une clé privée et afficher son empreinte**](#3.2)
- [**3.3 La deuxième étape - Comment authentifier une séance de clavardage privée**](#3.3)
- [**3.4 La troisième étape - Comment authentifier l'identité de votre contact Pidgin**](#3.4)

-------

<a name="3.0"></a>
## 3.0 À propos de Pidgin et d'OTR ##

Vous et vos correspondants devez configurer le plugin **OTR** pour être en mesure de mener des séances de **messagerie instantanée** (**MI**) privée et sécurisée. Puisque le plugin a été conçu spécialement pour **Pidgin**, le programme détecte automatiquement **OTR** lorsque les deux parties l'ont correctement installé et configuré.

**N. B.**: Si vous sollicitez une conversation privée auprès d'un contact qui n'a pas installé et configuré **OTR**, le programme envoie automatiquement un message expliquant comment obtenir le plugin **OTR*

<a name="3.1"></a>
## 3.1 Comment configurer le plugin Pidgin-OTR ##

Pour activer le plugin **OTR**, veuillez suivre les étapes énumérées ci-dessous:

**Première étape**. **Double-cliquez** sur ![](/sbox/screen/pidgin-fr/13.png) ou **sélectionnez** **Démarrer > Programmes > Pidgin** pour lancer **Pidgin** et afficher la fenêtre *Liste des contacts* (voir la *Figure 1*).

**Deuxième étape**. **Ouvrez** le menu *Outils*, puis **sélectionner** l'item *Plugins*, comme suit: 

![](/sbox/screen/pidgin-fr/40.png)

*Figure 1: La fenêtre Liste de contacts avec l'item Plugins sélectionné dans le menu Outils*

La fenêtre *plugins* s'affiche alors: 

**Deuxième étape**. **Faites défiler** jusqu'à l'option *Messagerie confidentielle Off-the-Record*, puis **cochez** la case adjacente pour l'activer. 

![](/sbox/screen/pidgin-fr/41.png)

*Figure 2: La fenêtre des Plugins de Pidgin avec l'option Messagerie confidentielle Off-the-Record sélectionnée*

**Troisième étape**. **Cliquez** sur ![](/sbox/screen/pidgin-fr/42.png) pour configurer la fenêtre *Messagerie confidentielle Off-the-Record*.

Pour résumer, il y a trois étapes de base pour configurer **OTR** correctement et être en mesure de mener des séances de *MI** privée et sécurisée: 

- **La première étape**: Générer une clé privée unique associée à votre compte et afficher son empreinte.

Les deux étapes suivantes consistent à sécuriser votre séance de **MI** et authentifier vos contacts.

- **La deuxième étape**: Une des parties sollicite une séance de messagerie auprès d'un correspondant actuellement en ligne.

- **La troisième mouvement** implique l'*authentification*, c.-à-d. la vérification de l'identité, de votre contact **Pidgin**. (**N. B.**: Dans **Pidgin**, un contact est une personne avec qui vous communiquez lors d'une séance de **MI** La procédure de vérification de l'identité d'un contact est appelé *authentification* dans **Pidgin**. Il s'agit en fait de confirmer que votre contact est *exactement* la personne qu'elle prétend être.

<a name="3.2"></a>
## 3.2 La première étape - Comment produire une clé privée et afficher son empreinte ##

Les séances de clavardage sécurisées avec **Pidgin** ne sont possibles qu'en créant une *clé privée* pour le compte que vous utilisez. La fenêtre de configuration de *Off-the-Record* comporte deux onglets: *Configuration* et *Empreintes connues*. L'onglet *Configuration* sert à créer une *clé* pour chacun de vos comptes et à régler certaines options d'**OTR**. L'onglet *Empreintes connues* contient les clés de vos contacts. Vous devez disposer d'une clé pour chaque contact avec qui vous souhaiter clavarder de façon privée et confidentielle. 

![](/sbox/screen/pidgin-fr/43.png)

*Figure 3: La fenêtre Messagerie confidentielle Off-the-Record affichant le contenu de l'onglet Configuration*

**Première étape**. Pour optimiser la confidentialité de vos communications, **cochez** les options *Permettre messagerie privée*, *Commencer messagerie privée automatiquement* et *Ne pas archiver les conversations OTR* dans l’onglet *Configuration* illustré ci-dessus. 

**Deuxième étape**. **Cliquez** sur ![](/sbox/screen/pidgin-fr/44.png) pour créer votre clé. Peu de temps après, une fenêtre apparaît pour vous aviser que la clé privée a bel et bien été crée:

![](/sbox/screen/pidgin-fr/45.png)

*Figure 4: La fenêtre Génération de la clé privée*

**N. B.**: Votre contact devra suivre les mêmes étapes dans son propre compte.

**Troisième étape**. **Cliquez** sur ![](/sbox/screen/pidgin-fr/37.png) lorsque la clé privée (qui devrait ressembler à l'illustration ci-dessous) a été créée: 

![](/sbox/screen/pidgin-fr/46.png)

*Figure 5: Une exemple d'empreinte de clé privée créée par le moteur OTR*

**Important**: Vous venez de créer une clé privée pour votre compte. Cette clé sera utilisée pour chiffrer vos séances de clavardage et faire en sorte que personne ne puisse vous espionner. L’empreinte est une longue séquence de lettres et de chiffres utilisés pour identifier la clé d’un compte, tel qu'illustré à la *Figure 5* ci-dessus.

**Pidgin** sauvegarde et vérifie automatiquement votre empreinte et celles de vos contacts pour que vous n’ayez pas à les mémoriser. 

<a name="3.3"></a>
## 3.3 La deuxième étape - Comment authentifier une séance de clavardage privée ##

**Première étape**. **Double-cliquez** sur le compte d’un de vos contact en ligne pour entamer une nouvelle séance de **MI**. Si vous avez tous les deux installé et correctement configuré le module **OTR**, vous remarquerez qu’un nouvel icone **OTR** est apparu au bas de la fenêtre de clavardage. 

![](/sbox/screen/pidgin-fr/47.png)

*Figure 6: Une fenêtre de messagerie de Pidgin affichant l’icone OTR surligné en noir*

**Deuxième étape**. **Cliquez** sur ![](/sbox/screen/pidgin-fr/48.png) pour afficher le menu associé, puis **sélectionnez** l'item *Commencer conversation privée*, tel qu'illustré ci-dessous: 

![](/sbox/screen/pidgin-fr/49.png)

*Figure 7: Le menu de l'icone OTR avec l'item Commencer conversation privée sélectionné*

*Votre fenêtre de messagerie **Pidgin** devrait maintenant ressembler à ceci:*

![](/sbox/screen/pidgin-fr/50.png)

*Figure 8: La fenêtre de messagerie de Pidgin affichant le bouton Non-vérifié*

**N. B.**: **Pidgin** communique automatiquement avec le programme de **MI** de votre contact et affiche un message chaque fois que vous entamez une séance de clavardage privée et sécurisée. En conséquence, le bouton **OTR**  ![](/sbox/screen/pidgin-fr/48.png) prend maintenant cette allure ![](/sbox/screen/pidgin-fr/51.png), ce qui vous indique que vous êtes maintenant prêt à mener une conversation chiffrée avec votre contact. 

**Attention**! Même si la conversation est maintenant sécurisée, l'identité de votre contact n'est toujours pas *vérifiée*. Attention: Votre contact pourrait être une tierce personne *usurpant l'identité* de votre contact.

<a name="3.4"></a>
## 3.4 La troisième étape - Comment authentifier l'identité de votre contact Pidgin ##

Pour authentifier votre contact dans **Pidgin**, vous devrez utiliser l'une des trois méthodes détaillées ci-dessous. Vous pouvez 1) saisir un code ou une phrase secrète déterminée à l'avance avec votre contact; 2) poser un e question dont seulement vous et votre contact connaissez la réponse; 3) vérifiez manuellement vos empreintes respectives en employant un autre mode de communication.

### La méthode par code ou phrase secrète ###

Vous pouvez vous entendre sur un code secret à l’avance, soit lors d’une rencontre en personne ou en utilisant un autre moyen de communication (comme le téléphone, le téléphone Internet **Skype**, ou un message texte par téléphone cellulaire). Lorsque vous saisissez le même code secret chacun de votre côté, votre séance sera authentifiée. 

**N. B.**: La fonction de reconnaissance du code secret dans **OTR** est sensible à la case, c'est-à-dire qu'elle peut faire la différence entre majuscules (A,B,C) et minuscules (a,b,c). Rappelez vous ce détail lorsque vous inventez un code ou une phrase secrète!

**Première étape** . **Cliquez** sur le bouton *OTR* dans la fenêtre de messagerie, puis **sélectionnez** l'item *Authentifier contact*, comme suit: 

![](/sbox/screen/pidgin-fr/52.png)

*Figure 9: Le menu Non-vérifié avec l'item Authentifier contact sélectionné*

La fenêtre *Authenticate Buddy* s'affiche alors et vous demande de choisir une méthode d'authentification.

**Deuxième étape**. **Cliquez** sur ![](/sbox/screen/pidgin-fr/53.png) et **sélectionnez** l'option *Shared Secret*: 

![](/sbox/screen/pidgin-fr/54.png)

*Figure 10: La fenêtre Authenticate buddy avec le menu défilant des options de méthodes d'authentification* 

**Troisième étape**. **Saisissez** le code ou la phrase secrète, comme suit:

![](/sbox/screen/pidgin-fr/55.png)

*Figure 11: La fenêtre Shared Secret* 

**Quatrième étape**. **Cliquez** sur ![](/sbox/screen/pidgin-fr/56.png) pour afficher la fenêtre suivante:

![](/sbox/screen/pidgin-fr/58.png)

*Figure 12: La fenêtre d'authentification d'un correspondant fictif*

Si les deux codes correspondent, votre séance sera authentifiée.

**N. B.**: *De son côté, votre contact verra la même fenêtre et devra saisir le même code secret. Si les deux codes correspondent, votre séance sera authentifiée.*

![](/sbox/screen/pidgin-fr/57.png)

*Figure 13: La fenêtre Authenticate Buddy d'un correspondant fictif*

Lorsque la séance est authentifiée, le bouton *OTR* s'affiche comme ceci: ![](/sbox/screen/pidgin-fr/51.png). Votre séance de clavardage est désormais sécurisée et vous êtes assuré que la personne avec qui vous correspondez est bel et bien votre contact.

### La méthode par question et réponse ###

Une autre façon d'authentifier vos contacts est la méthode par question et réponse. Créez une question et une réponse correspondante. Après avoir lu votre question, votre contact doit saisir *exactement* la même réponse, et si les deux réponses correspondent, votre identité sera automatiquement authentifiée. 

**Première étape**. **Cliquez** sur le bouton *OTR* dans une fenêtre de messagerie active pour afficher le menu correspondant, puis **sélectionnez** l'item *Authentifier contact* (voir la *Figure 9*).

![](/sbox/screen/pidgin-fr/59.png)

*Figure 14: Une fenêtre de messagerie Pidgin affichant l'icone OTR*

Une fenêtre *Authentifier contact* s'affiche alors et vous demande de choisir une méthode d'authentification. 

**Deuxième étape**. **Cliquez** sur le menu défilant et **sélectionnez** la méthode *Question and Answer*:  

![](/sbox/screen/pidgin-fr/60.png)

*Figure 15: La fenêtre Authenticate Buddy*

**Troisième étape**. **Saisissez** une question et la réponse correspondante. La question sera automatiquement envoyée à votre contact.

![](/sbox/screen/pidgin-fr/61.png)

*Figure 16: La fenêtre Question et réponse*

Si la réponse de votre contact correspond à la vôtre, vos identités seront mutuellement authentifiées, et les deux parties sont bel et bien qui elles prétendent être!

Lorsque la séance sera authentifiée, le bouton *OTR* ressemblera à ceci ![](/sbox/screen/pidgin-fr/51.png). Votre séance est maintenant sécurisée et vous êtes assuré de l'identité de votre contact.

Remarquez que lorsque vous **Sélectionnez > Liste de contacts > Outils > Plugins > Messagerie confidentielle Off-The-Record > Configurer le plugin**, l’onglet *Empreintes connues* affiche désormais le compte de votre contact et un message indiquant que son identité a été vérifiée. 

![](/sbox/screen/pidgin-fr/62.png)

*Figure 17: La fenêtre Messagerie confidentielle Off-the-Record Messaging affichant les empreintes connues*

Félicitations! Vous pouvez maintenant clavarder en tout confidentialité. La prochaine fois que votre contact et vous voudrez clavarder (en utilisant les mêmes ordinateurs), vous pourrez sauter les étapes 1 et 2 décrites ci-dessus. Vous n’aurez qu’à demander une connexion sécurisée et votre contact n’aura qu’à l’accepter. 

