# Projet compteur de mot

## Demande client: 

- l'application demande a l'utiisateur d'ecirer un text
- on doit lui renvoyer le nbr de mot de son text 
- le nombre de phrase 
- la recurence de certains mot  ( la repetition d'un certains mot donnée par le client)

<br>

## Language utiliser:

Nous utiliserons python pour créé ce projet.

<br>

### Inteface graphique: 

1. Utilisation de PyQt

    1. Bouton demande l'utilisateur un texte

        1. Renvoie la forme d'un string, puis utilsation de ce string pour les fonctions

    1. Bouton pour rentrer les mots qui doivent etre pris par la recurence
    
    1. Afichage 

        1. zone pour afficher le nbr de mot 

        1. zone pour afficher le nbr de phrase 

        1. zone pour afficher le nbr de recurence


### Comment obtenir le nombre de mot ? 
1. On doit recuperais la phrase de l'utilisateur et la decouper puis compter chaque mot. Comment la decouper ? 

    1. En utilisant une fonction decouperMot créé.

    2. Besoin d'un compteur pour les mot 
