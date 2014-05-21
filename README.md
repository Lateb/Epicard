Epicard
=======

lateb\_card_gen
---------------

Ceci est un générateur de carte de membre pour les associations.  
Il a été créé originalement pour [L'Association des Teks/Ta Experts en Bière](http://lateb.org).  
Il a été fait en python3, avec amour et bière.

Ce script va récupérer des informations d’une base de données `mysql` afin de les mettre sur la carte.

Les dimensions trouvées dans le script sont en pixel.

Comment ça s’utilise ?
----------------------

Pour utiliser ce script, les modules suivants sont indispensables :

 * [pyBarcode](https://pypi.python.org/pypi/pyBarcode)

 * [Pillow](https://pypi.python.org/pypi/Pillow/)

 * [SQLAlchemy](https://pypi.python.org/pypi/SQLAlchemy) avec [oursql](https://pythonhosted.org/oursql/install.html), qui requiert [Cython](https://pypi.python.org/pypi/Cython)

Au premier lancement, le script va créer un fichier de configuration pour la base de données mysql.  

Autres détails
--------------

J'ai personnellement une table `CUSTOMERS` (requis par le logiciel qui traite les membres à Lateb), et j'y séléctionne les informations dont j'ai besoin.
La commande est une commande SQL classique, et ne devrait pas être difficile à adapter.

La police utilisée pour les cartes Lateb est [Streetwise Buddy](http://www.dafont.com/streetwise-buddy.font), au format `ttf`.

License
-------

ISC, voir le fichier `LICENSE` pour les détails.

Contact
-------

Une question ? Une super idée ? Contactez moi à lucas *at* calus *point* fr
