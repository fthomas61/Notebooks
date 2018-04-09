# Jupyter notebooks for learning Python

A repository of notebooks

#HSLIDE

### Un petit exercice sur les statistiques

- Pratique des listes
- algorithmes de calcul de la moyenne et de l'écart type
- vérification possible avec Excel ou LibreOffice

#HSLIDE

### Le pitch

- on relève la liste de l'âge de nos parents à notre naissance
- et on calcule moyenne et écart type

#HSLIDE

### Le code

```python
import math
# Deux listes initialement vides pour stocker les âges de notre mère et notre père à notre naissance
agem = []
agep = []
# La fonction append() permet d'ajouter un élément à la suite d'une liste
agep.append(31)
agem.append(29)

# Calcul de la moyenne
sage=0.0
for i in agep:
    sage=sage+i
magep = sage / len(agep)

# Calcul de l'écart type
variance=0.0
for i in agem:
    variance=variance+(i-magem)*(i-magem)
variance=variance/(len(agem)-1)
ecartm=math.sqrt(variance)
```
@[1](Pour la fonction sqrt() nécessaire au calcul de l'écart type
@[3-4](Deux listes initialement vides pour les âges de nos père et mère)
@[4-5](Si le montant dépasse 90€ on fait la remise)
@[6-7](Ajout des éléments)
@[10-13](Calcul de la moyenne, on fait la somme des âges et on divise par le nombre de personnes)
@[16-20](Calcul de la variance puis de l'écart type - attention : échantillon vs population)
