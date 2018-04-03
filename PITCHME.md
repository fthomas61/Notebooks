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

#HSLIDE

### Les variables

#HSLIDE

### Calcul de périmètre

- Application à un problème simple
- $p = 2*(L+l)$

#HSLIDE

### Calcul de périmètre avec une conversion

- Plus de variables

#HSLIDE

### Premier algorithme... premiers calculs itératifs, premiers tests

- for i in range(2,n-1):
- de l'importance de l'indentation
- if n%i == 0:

### Algorithme

``̀`
n = int(input("Entrez le nombre dont on veut tester la primalité : "))

isPrime = True      # isPrime est une variable de type booléen (True/False)
for i in range(2,n): # range(2,n) parcourt l'espace 2 à n exclu (donc de 2 à n-1)
    if n%i == 0:
        isPrime = False
        break
    else:
        pass

if isPrime:
    print("Congratulations :",n,"is prime !")
else:
    print("Nope.",n,"is not prime. Try again.")

``̀`

#HSLIDE

!-- ![Flux Explained](https://facebook.github.io/flux/img/flux-simple-f8-diagram-explained-1300w.png)
