

---

lang: fr
community: guide
type: tools
legacy: True
child: True
os: windows
weight: 3
depth: 3
title: How to Clean the Windows Registry in CCleaner

---

Sommaire des sections de cette page:

- [**4.0 Avant de commencer**](#4.0)
- [**4.1 Comment nettoyer le Registre de Windows avec CCleaner**](#4.1)
- [**4.2 Comment restaurer un fichier de sauvegarde du registre**](#4.2)

----

<a name="4.0"></a>
### 4.0 Avant de commencer ###

**CCleaner** vous permet également de nettoyer le **Registre de Windows**, une base de données où sont enregistrées vos configurations et les paramètres du matériel et des logiciels installés sur votre ordinateur. Chaque fois que vous modifiez la configuration du système, installez un logiciel ou exécutez une tâche de routine, ces modifications sont enregistrées dans le **Registre de Windows**.

Au fil du temps, le **Registre de Windows** accumule des données de configuration et de réglage désuètes, y compris des traces de programmes obsolètes. L'option *Registre* de **CCleaner** vous permet d'exécuter un scan du registre pour supprimer ces données inutiles, ce qui améliore le fonctionnement et la vitesse de votre système, en plus de protéger votre confidentialité et votre sécurité numérique.

**Astuce**: Un scan du **Registre de Windows** devrait être exécuté à tous les mois.

<a name="4.1"></a>
### 4.1 Comment nettoyer le Registre de Windows avec CCleaner ###

**Première étape**. **Cliquez** sur![](/sbox/screen/ccleaner-fr/50.png) pour afficher la fenêtre suivante:

![](/sbox/screen/ccleaner-fr/51.png)

*Figure 1: L'interface de CCleaner en mode Registre*

La fenêtre *Registre* de **CCleaner** est divisée en deux panneaux: la liste *Intégrité du Registre* et le panneau où s'affiche l'information concernant les problèmes trouvés.

**Deuxième étape**. **Cochez** tous les items de la liste *Intégrité du registre*, puis **cliquez** sur ![](/sbox/screen/ccleaner-fr/53.png) pour lancer le scan du registre et détecter d'éventuels problèmes à corriger; après un certain temps, le résultat du scan s'affiche comme suit:

![](/sbox/screen/ccleaner-fr/54.png)

*Figure 2: La panneau des résultats affichant une liste de problèmes à corriger* 

En guise de mesure de précaution avant de corriger le **Registre Windows**, le programme vous proposera de créer une copie de sauvegarde du registre. Si un quelconque problème survient suite au nettoyage du **Registre de Windows**, il vous sera possible de restaurer le **Registre de Windows** à son état précédent en utilisant cette copie de sauvegarde.

**Troisième étape**. **Cliquez** sur ![](/sbox/screen/ccleaner-fr/55.png) pour afficher la boîte de dialogue de confirmation illustrée ci-dessous:

![](/sbox/screen/ccleaner-fr/56.png)

*Figure 3: La boîte de dialogue de confirmation*

**Astuce**: Si vous oubliez l'emplacement de votre copie de sauvegarde, vous n'avez qu'à effectuer une recherche de l'extension de fichier *.reg*.

**Quatrième étape**. **Cliquez** sur ![](/sbox/screen/ccleaner-fr/57.png) pour créer une copie de sauvegarde des clés du registre et afficher la fenêtre suivante:

![](/sbox/screen/ccleaner-fr/58.png)

*Figure 4: La fenêtre Enregistrer sous*

**Cinquième étape**. **Cliquez** sur ![](/sbox/screen/ccleaner-fr/59.png), après avoir choisi un emplacement pour votre copie de sauvegarde, pour afficher la fenêtre suivante:

![](/sbox/screen/ccleaner-fr/60.png)

*Figure 5: La boîte de dialogue Corriger l'erreur/Corriger toutes les erreurs sélectionnées*

**Commentaire:** Les utilisateurs experts ou avancés apprécieront la possibilité de corriger certaines erreurs et d'en ignorer d'autres, selon leur préférences. Il est recommandé aux utilisateurs moyens ou intermédiaires de corriger toutes les erreurs sélectionnées.

**Sixième étape**. **Cliquez** sur ![](/sbox/screen/ccleaner-fr/61.png) ou ![](/sbox/screen/ccleaner-fr/62.png) pour afficher chaque erreur, puis **cliquez** sur ![](/sbox/screen/ccleaner-fr/64.png) pour corriger uniquement celles que vous souhaitez corriger.

**Septième étape**. **Cliquez** sur ![](/sbox/screen/ccleaner-fr/63.png) pour corriger toutes les erreurs sélectionnées et **cliquez** sur **Fermer** pour achever le processus de nettoyage.

**Astuce:** Répétez les **étapes 2 à 7** jusqu'à ce qu'il n'y ait plus aucune erreur à corriger.

Le **Registre de Windows** a été nettoyé avec succès. 

<a name="4.2"></a>
### 4.2 Comment restaurer un fichier de sauvegarde du registre ###

Si vous avez l'impression que le nettoyage du **Registre de Windows** a occasionné un problème avec le fonctionnement normal de votre système, le fichier de sauvegarde que vous avez créé aux **étapes 3** à **5** de la section **4.1** peut être utilisée pour restaurer le registre à son état précédent et ainsi réduire l'interférence avec votre système.

Pour restaurer le registre, suivez les étapes énumérées ci-dessous:

**Première étape**. **Sélectionnez Démarrer > Exécuter** pour afficher la boîte de dialogue *Exécuter*, puis **saisissez** *regedit*, comme suit:

![](/sbox/screen/ccleaner-fr/65.png)

*Figure 6: La boîte de dialogue Exécuter*

**Deuxième étape**. **Cliquez** sur ![](/sbox/screen/ccleaner-fr/04.png) pour afficher la fenêtre suivante:

![](/sbox/screen/ccleaner-fr/66.png)

*Figure 7: L'Éditeur du registre*

**Troisième étape**. **Sélectionnez Fichier > Importer** dans la barre de menu pour afficher la fenêtre *Importer un fichier du registre*, puis **sélectionnez** ![](/sbox/screen/ccleaner-fr/68.png).

**Quatrième étape**. **Cliquez** sur ![](/sbox/screen/ccleaner-fr/77.png) pour afficher la boîte de dialogue suivante:

![](/sbox/screen/ccleaner-fr/70.png)

*Figure 8: Une autre Boîte de dialogue de l'Éditeur du registre confirmant que le fichier de sauvegarde a été restauré*

**Cinquième étape**. **Cliquez** sur ![](/sbox/screen/ccleaner-fr/04.png) pour finaliser la restauration du fichier de sauvegarde du registre.


