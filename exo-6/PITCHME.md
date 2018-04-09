# Jupyter notebooks for learning Python

A repository of notebooks

#HSLIDE

### Un petit exercice sur les boucles et instructions conditionnelles

- Si en Python se dit "if"
- Pour en Python se dit "for"
- Attention à l'indentation

#HSLIDE

### Le pitch

- un jeu de pierre, feuille, ciseaux
- n parties entre deux joueurs
- victoire : 3 points, nul : 1 point, défaite : 0 point.

#HSLIDE

### Le code

```python
    #pierre=1
    #feuille=2
    #ciseau=3
    if d1==d2:
        point1=point1+1
        point2=point2+1
    else:
        if d1==1:
            if d2==2:
                point2=point2+3
            else:
                point1=point1+3
        elif d1==2:
```
@[1-3](Notre convention)
@[4-6](En cas de match nul)
@[8-13](La pierre casse les ciseaux, la feuille enveloppe la pierre, etc)
