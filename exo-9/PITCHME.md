# Jupyter notebooks for learning Python

A repository of notebooks

#HSLIDE

### Algorithme de résolution numérique d'équations - dichotomie

- si la fonction est monotone entre a et b
- et qu'elle change de signe entre a et b
- alors l'algorithme est le suivant
    - couper l'intervalle [a,b] en deux et déterminer si la solution
    - déterminer dans quel demi-intervalle la solution existe
    - recommencer

#HSLIDE

### Le pitch

- on souhaite résoudre l'équation $f(x) = x^2 - 3 = 0$
- entre x=1 et x=5

#HSLIDE

### Le code

```python
import math
# La fonction qu'on cherche à annuler
def f(x):
    return x*x - 3

# Méthode de dichotomie

a = 1
b = 5

xa = a
xb = b
for _ in range(0,40):
    #print("intervalle avant dichotomie [",xa,',',xb,']')
    xm = (xa+xb)/2.0
    if f(xa)*f(xm) < 0:
        xb = xm
    else:
        xa = xm

print("La solution est comprise entre",xa,"et",xb)
print("La vraie solution est",math.sqrt(3.0))
```
@[1](On importe les fonctions mathématiques - pour la racine carrée plus bas)
@[3-4](Définition de la fonction f)
@[8-9](Bornes de l'intervalle de recherche)

#HSLIDE

### Le code - suite

```python
xa = a
xb = b
for _ in range(0,40):
    xm = (xa+xb)/2.0
    if f(xa)*f(xm) < 0:
        xb = xm
    else:
        xa = xm

print("La solution est comprise entre",xa,"et",xb)
print("La vraie solution est",math.sqrt(3.0))
```
@[1-2](Initialisation de l'intervalle de recherche)
@[3](On fait 40 dichotomies)
@[4](Calcul du point milieu)
@[5-8](Si la fonction f change de signe entre xa et xm alors il faut chercher la solution entre xa et xm, sinon entre xm et xb)
@[10](Affichage de la solution obtenue par la méthode de dichotomie)
@[11](Affichage la la solution "exacte" $sqrt(3)$)
