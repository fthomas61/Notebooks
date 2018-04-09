# Jupyter notebooks for learning Python

A repository of notebooks

#HSLIDE

### Un petit exercice sur les boucles, les tests et les accumulations

- Pour en Python se dit "for"
- import random permet d'accéder aux fonctions de calcul aléatoire
- Attention à l'indentation

#HSLIDE

### Le pitch

- un jeu de dés
- deux joueurs
- chaque joueur lance 2 dés et onn fait la somme
- celui qui marque le plus prend 3 points (1 point en cas de match nul)
- on fait n parties

#HSLIDE

### Le code

```python
for i in range(n): # On fait n parties
    # Lancement de deux dés et somme des scores
    d1=random.randint(1,6)
    d2=random.randint(1,6)
    score1= d1+d2
```
@[1](On fait n parties)
@[3](Lancement du premier dé)
@[4](Lancement du second dé)
@[5](On calcule le score)

#HSLIDE

### Le code

```python
point1=0
point2=0
...
    # Qui a gagné cette partie ?
    if score1==score2:
        #print ("match nul")
        point1=point1+1
        point2=point2+1
    else :
        if score1<score2:
            #print(player2,"vainqueur")
            point2=point2+3
        else:
            #print(player1,"vainqueur")
            point1=point1+3
```
@[1-2](Initialisation du nombre de points de chaque joueur)
@[5](On évacue le cas du match nul)
@[7-8](Match nul : 1 point, ajouté au cumul de points de chaque joueur)
@[10-15](Un peu de logique pour savoir qui prend les 3 points)
