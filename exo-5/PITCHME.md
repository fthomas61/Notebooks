# Jupyter notebooks for learning Python

A repository of notebooks

#HSLIDE

### Un petit exercice sur les listes

- Une liste de valeurs []
- Dans laquelle on accumule des occurences

#HSLIDE

### Le pitch

- deux dés
- quelle est la probabilité de sortir un 2, un trois, etc
- simulation et comparaison avec les valeurs théoriques

#HSLIDE

### Le code

```python
%pylab inline
import random
n = 1000

occurences = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in range(n):
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    score = d1 + d2
    occurences[score]=occurences[score]+1
    
print(occurences)
```
@[1](Pour que le futur graphique soit affiché sur la page web)
@[2](Pour les fonctions aléatoires - random.randint()
@[3](On va faire n tirages)
@[5](Le tableau de stockage des occurences... un peu surdimensionné)
@[7](On fait les n tirages)
@[11](Ventilation du résultat dans le tableau des occurences)
@[13](Affichage du résultat)

#HSLIDE

### Le code

```python
p2 = 1./36.
p7 = 6./36.
print(int(p2*n),int(p7*n))

plt.plot(occurences)
```
@[1-2](Les probabilités théoriques d'obtenir un 2 et un 7)
@[5](Tracé des probabilités)
