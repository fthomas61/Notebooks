# Jupyter notebooks for learning Python

A repository of notebooks

#HSLIDE

### Algorithme de résolution numérique d'équations - Newton-Raphson

- si on peut calculer la fonction et sa dérivée première
- alors l'algorithme est le suivant
    - calculer en un point donné la fonction et sa dérivée
    - suivre la "flèche", c'est à dire suivre la direction de la tangente
      pour aboutir à une nouvelle estimation de la solution.
    - recommencer

#HSLIDE

### Le pitch

- on souhaite résoudre l'équation $f(x) = x^2 - 3 = 0$
- en partant de $x = 1$

#HSLIDE

### Le code

```python
import math
# La fonction qu'on cherche à annuler
def f(x):
    return x*x - 3
# La dérivée d'icelle
def fp(x):
    return 2*x

a = 1

xa = a
for _ in range(10):
    xa = xa - f(xa)/fp(xa)
    
print("La solution est proche de",xa)
print("La vraie solution est",math.sqrt(3.0))
```
@[1](On importe les fonctions mathématiques - pour la racine carrée plus bas)
@[3-4](Définition de la fonction f)
@[6-7](Définition de la dérivée fp)
@[11](Estimation initiale de la solution)
@[12](On va faire 10 itérations)
@[13](On met à jour l'estimation de la solution)
@[15](Affichage de la solution obtenue par la méthode de Newton-Raphson)
@[16](Affichage la la solution "exacte" $sqrt(3)$)

