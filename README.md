# Projets-Numworks
Une collection de petits programmes contenant des jeux (surtout des jeux) ainsi que quelques algorithmes plus ou moins utiles.
La plupart des ces programmes ont été écris entre deux écercices de mathématiques au lycée.
Il est fortement probable que certains de ces programmes ne soient pas fonctionnels ou qu'ils ne puissent pas répondre à tous les besoins.
Il est peut-être possible ed les exécuter sur PC avec les librairies adaptées de [ZetaMap](https://github.com/ZetaMap)

## PAC-MAN
Ce jeu est très certainement mon plus gros projet pour le moment, il nécessite l'utilisation de plusieurs librairies:
* maps.py qui va simplement importer une carte du jeu.
* coords.py, une classe permettant de gérer les coordonnées.
* perso.py qui va gérer la plupart des mouvements et des actions des personnages, alliés comme ennemis.
* ont.py, une bibliothèque de fonctions dont certaines ont été à une époque requise par perso.py

Pour le lancer il suffit d'exécuter pacman.py
Certaines options peuvet être modifiées comme le nombre d'ennemis qui va dépendre des objets "pero" (faute de frappe ==> flemme de corriger) insérés dans la liste.
Le self.dt sert à manipuler la rapidité du jeu.
Pour avoir des personnages carrés et donc une meilleure rapidité de jeu, modifiez le programme perso.py afin de sélectionner dep_1, dep_2, ... ou bien dep_1c, dep_2c, ... pour des objets ronds.
Les personnages ronds ne sont pas encore tout à faits finis.

## Bases
Cet algorithme sert à passer de bases en bases par example 011 ==> 3 pour du binaire.

## Binaire
Binaire.py sert à faire la même chose mais exclusivement pour du binaire.

## Démineur
Ce jeu est un petit projet mettant en place un démineur sur numworks. il est possible de modifier le nombre de mines dans l'appel en bas du programme.

## Divisions
divisions.py est une bibliothèque de fonctions pratiques en mathématiques.

## Jeu de la vie
Le programme vie.py mets en oeuvre le jeu de lma vie sur numworks, il est possible de régler le nombre de cases à simuler en fonction de la taille des cases "self.taille" ainsi que de limiter le nombre de cycles à éxécuter en modifiant "self.nbloop".