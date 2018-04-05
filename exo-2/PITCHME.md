# Jupyter notebooks for learning Python

A repository of notebooks

#HSLIDE

### Les types de données complexes : les collections

- Les listes
- Les tuples
- Les dictionnaires
- Les ensembles

#HSLIDE

### Les listes

- ensemble de données
- l'accès à chaque élément se fait via la position de cet élément
- les positions commencent à 0
- les éléments de la liste sont inclus entre [ et ] et sont sépares par des virgules

```python
l = [10,20,30,40]
print(l[2])
```
@[1](Définition d'une liste de nombres)
@[2](Quel sera l'affichage ?)

#HSLIDE

### Longueur et parcours d'une liste

```python
l = [10,20,30,40]
longueur = len(l)
for e in l:
    print("element de la liste",e)
```
@[1](Définition d'une liste de nombres)
@[2](La fonction len() retourne le nombre d'éléments)
@[3-4](Une façon de parcourir la liste)

#HSLIDE

### Les tuples

- comme des listes mais non modifiables (immutable)
- les éléments du tuple sont inclus entre ( et ) et sont sépares par des virgules

```python
t = (10,20,30,40)
longueur = len(t)
for e in t:
    print("element du tuple",e)
t[2]=999
```
@[1](Définition d'un tuple)
@[2](La fonction len() retourne le nombre d'éléments d'un tuple aussi)
@[3-4](Le parcours des éléments d'un tuple)
@[5](Cette opération va échouer, les tuples sont "immutable")

#HSLIDE

### Les dictionnaires

- les éléments sont accédés via une clé
- pas d'ordre particulier
- les éléments sont inclus entre { et } et séparés par des virgules

```python
profs = {'maths':"Pogu",'info':"François"}
print("Le prof de maths et",profs['maths'])
for matiere in profs.keys():
    print("Le prof de",matiere,"est",profs[matiere])
```
@[1](Définition du dictionaire)
@[2](L'acces se fait par clé. Ici la clé vaut 'maths'
@[3-4](Le parcours des éléments d'un dictionnaire)

#HSLIDE

### Les ensembles

- pas de doublons dans les ensembles
- opérations ensemblistes

```python
impairs = {1,3,5,7,9}
pairs = {2,4,6,8}
tous = pairs | impairs
vide = pairs & impairs
```
@[1-2](Création de deux ensembles)
@[3](Union (|) de deux ensembles)
@[4](Intersection (&) (vide ici) de deux ensembles)

#HSLIDE

### Quelques références pour aller plus loin

[A whirlwind tour of Python, le livre](http://www.oreilly.com/programming/free/files/a-whirlwind-tour-of-python.pdf)
<br>
[A whirlwind tour of Python, les exos](https://github.com/jakevdp/WhirlwindTourOfPython)
