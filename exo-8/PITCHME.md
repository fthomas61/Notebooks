# Jupyter notebooks for learning Python

A repository of notebooks

#HSLIDE

### Découverte de la programmation orientée objets (POO)

- on fabrique des objets
- qu'on équipe de capacités (méthodes)
- qui vont interagir entre eux
- 4 principes
    - encapsulation
    - abstraction
    - héritage
    - polymorphisme

#HSLIDE

### Le pitch

- on se fabrique un objet de type : "des", une "class" en Python
- chaque objet embarque son état interne (n,faces,valeurs,score)
- les utilisateurs de la classe "des" ont accès à un ensemble de méthodes (lance(), somme(), affiche(), etc)

#HSLIDE

### Le code

```python
class des:
    def __init__(self,n=2,faces=6):
        self.n = n
        self.faces = faces
        self.valeurs = []
        for _ in range(self.n):
            self.valeurs.append(0)
        self.score = 0
```
@[1](On définit une classe d'objets avec le mot clé class, un objet de classe "des" contient le nombre de dés, le nombre de faces des dés, la valeur de chaque dé et la somme)
@[2](La fonction __init__ est appelée constructeur. C'est cette fonction qui est appelée quand on crée (construit) un objet)

#HSLIDE

### Le code - suite

```python
    def affiche(self):
        sortie=()
        for i in range(self.n):
            sortie=tuple(self.valeurs)
        return sortie

    def lance(self):
        self.score = 0
        for i in range(self.n):
            self.valeurs[i] = random.randint(self.n,self.faces)
            self.score += self.valeurs[i]

    def somme(self):
        return self.score

    # permet de "comparer" des dés
    def __eq__(self,other):
        if self.score == other.score:
            return 1
        else:
            return 0
```
@[1-5](Fonction d'affichage des valeurs des dés)
@[7-11](Fonction de lancer du jeu de dés)
@[13-14](Fonction qui retourne la somme)
@[17-21](Opérateur de comparaison entre des lancers de dés)

#HSLIDE

### Le code - suite

```python
# Et maintenant, créons des objets et faisons les travailler
d = des(n=3,faces=6)
d.lance()
print("résultat du lancer",d.affiche())
print("soit une score de",d.somme())
d.lance()
print("le score est de",d.somme())
d.lance()
print("quel lancer !",d.affiche())
```
@[2](Création d'un objet "des" contenant 3 dés à 6 faces. La fonction __init__ va être appelée)
@[3-9](On peut faire "travailler" ce jeu de dés)

#HSLIDE

### Le code - suite

```python
# Une petite opposition entre deux joueurs
d1 = des(n=2,faces=8)
d2 = des(n=2,faces=8)
for _ in range(10):
    d1.lance()
    d2.lance()
    if d2 == d1:
        print("Match nul !",d1.somme(),"to",d2.somme())
    else:
        if d2 > d1:
            print("player2 wins !",d2.somme(),"to",d1.somme())
        else:
            print("player1 wins !",d1.somme(),"to",d2.somme())
```
@[2-3](Chaque joueur se crée son ensemble de dés)
@[4](On va faire 10 parties)
@[5-6](Chaque joueur lance ses dés)
@[7,10,12](Les opérateurs de comparaisons de dés sont utilisés ici)
