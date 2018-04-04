# Jupyter notebooks for learning Python

A repository of notebooks

#HSLIDE

### Premiers enroulements

- Les variables
- Les fonctions
- Les itérations
- Les tests logiques

#HSLIDE

### La fonction print()

```python
print("Ceci","puis cela")
```

#HSLIDE

### Les variables

```python
v1 = 2
x = 1.6
nomPersonne = "Homer Simpson"
success = False
```
@[1](Variable de type entier - integer)
@[2](Variable de type réel - float)
@[3](Variable de type chaine de caractères - string)
@[4](Variable de type booléen - boolean)

#HSLIDE

### Calcul de périmètre

- Application à un problème simple

`$$p = 2*(L+l)$$`

#HSLIDE

### Calcul de périmètre avec une conversion

- Plus de variables

```python
metersPerYard = 0.9144 # Facteur de conversion
longueur = float(input("Entrez la longueur du rectangle (en m) : "))
largeur = float(input("Entrez la largeur du rectangle (en m) : "))
perimetre = 2 * (longueur + largeur)
print("Le périmètre est",perimetre,"m")
perimetreYards = perimetre / metersPerYard
print("which is",perimetreYards,"yards")
```

#HSLIDE

### Premier algorithme... premiers calculs itératifs, premiers tests

Test de primalité. Un algorithme possible (et très sub-optimal) : on prend un nombre n et on fait la division entière de n par tous les nombres compris entre 2 et n-1. Si le reste de la division entière est nul pour au moins un de ces nombres alors le nombre n n'est pas premier. Pourquoi éviter 1 et n ? Parce que tout nombre est divisible par 1 et par lui-même. C'est justement s'il n'est divisible que par ces deux là qu'il est premier !

#HSLIDE

### Algorithme

---?code=prime.py&lang=python
@[1](Lecture de la valeur de n)
@[3](Initialisation de la variable isPrime)
@[4](Pour i allant de 2 à n exclu)
@[5-9](Le calcul pour un i quelconque)

#HSLIDE

### Quelques références pour aller plus loin

[Les nombres premiers](https://fr.wikipedia.org/wiki/Nombre_premier)
<br>
[Les tests de primalité](https://fr.wikipedia.org/wiki/Test_de_primalit%C3%A9)
<br>
:bulb:
