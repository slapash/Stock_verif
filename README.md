# Stock_verif
vérification des livres en stock dans la base de données à partir d'un fichier excel

état actuel: Rudimentaire

Pour configurer le script il faut changer le nom du serveur de base de donnée ainsi que le nom de la base de donnée
Pour ça il faut aller dans Microsoft SQL Management Studio pour récuperer les informations nécessaires
Le nom de la base est de mémoire CARREFOURDULIVRE 
Pour le nom du serveur il faut créer une requete sur la base CARREFOURDULIVRE et mettre le code suivant: SELECT @@SERVERNAME   puis executer la requete, le résultat sera le nom du serveur 

Les informations recceuillies doivent etre changées dans le fichier DB_query.py

Pour cette version, il n'y a que ça à modifier
Pour lancer le site web il faut avoir python sur l'ordi 

enfin il faut ouvrir une invite de commande (cmd) ou un terminal et éxecuter la commande ci dessous:
python main.py (si ça ne marche pas alors : python3 main.py)

il faut qu'il y ait un colonne nomée ISBN (majuscule importante pour l'instant) dans le fichier excel

apres avoir exécuté le fichier main.py on peut acceder au site via http://localhost:5000 ou http://127.0.0.1:5000/

une fois fais il faut charger le fichier excel sur le site et clicker sur le boutton submit

le résultat est une liste des isbn qui figurent dans la base de données
