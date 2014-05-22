Epicard
=======

Ceci est un générateur de carte de membre pour les associations.  
Il a été créé originalement pour [L'Association des Teks/Ta Experts en Bière](http://lateb.org).  
Il a été fait en python3, avec amour et bière.

Ce script va récupérer des informations d’une base de données `mysql` afin de les mettre sur la carte.

Les dimensions trouvées dans le script sont en pixel.

Prérequis
---------

Pour utiliser ce script, les modules suivants sont indispensables :

 * [pyBarcode](https://pypi.python.org/pypi/pyBarcode)  
 * [Pillow](https://pypi.python.org/pypi/Pillow/)  
 * [SQLAlchemy](https://pypi.python.org/pypi/SQLAlchemy) avec [oursql](https://pythonhosted.org/oursql/install.html), qui requiert [Cython](https://pypi.python.org/pypi/Cython)

Les fichiers suivants sont obligatoires :

 * `typo.ttf`, contenant la police de votre choix  
 * `logo.jpg`, contenant le logo de votre association  
 * `photos`, un dossier contenant les photos des membres (au format indiqué en dessous)  
 * `result`, un dossier qui contiendra les jpg des cartes finales

Les photos doivent être fournies au format `[adresse@mail].jpg`.  
Si la photo n’existe pas, le membre n’est pas traité.  
Les photos doivent faire la taille 210px par 270px.  
Le logo est attendu au format 450px par 207px.

Comment utiliser ce script
--------------------------

Au premier lancement, le script va créer un fichier de configuration pour la base de données mysql.  
Le script va, si tout est bien configuré, générer les cartes de membre de tous les noms de la base de données qui ont une photo correspondante, et les stocker dans le dossier `result`.

Autres détails
--------------

J'ai personnellement une table `CUSTOMERS` (requis par le logiciel qui traite les membres à Lateb), et j'y séléctionne les informations dont j'ai besoin.
La commande est une commande SQL classique, et ne devrait pas être difficile à adapter.

La police utilisée pour les cartes Lateb est [Streetwise Buddy](http://www.dafont.com/streetwise-buddy.font), au format `ttf`.

Si le code barres est inutile pour vous, il devrait être simple de l’enlever et de mettre autre chose à la place.

Un exemple est fourni sur la branche `lateb_example`, ça peut être utile.

License
-------

MIT, voir le fichier `LICENSE` pour les détails.

Contact
-------

Une question ? Une super idée ? Contactez moi à lucas *at* calus *point* fr.
