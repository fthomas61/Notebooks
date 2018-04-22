# Jupyter notebooks for learning Python

A repository of notebooks

#HSLIDE

### La monnaie en Syldavie

Petit exercice de prestidigitation utilisant les ensembles (sets) en Python

#HSLIDE

### Le pitch

Hervé passe ses vacances en Syldavie. Dans ce pays, les pièces de
monnaie n'ont plus cours, et il n'existe que trois sortes de billets de
banque, qui valent respectivement 57, 62 et 72 khôrs (couronnes).

Hier, Hervé a acheté des croissants à la boulangerie, qui lui ont coûté
4 couronnes. Il a donné un certain nombre de billets, d'un montant
inférieur à 600 khôrs, et le vendeur a pu lui rendre la monnaie
exacte de son achat.

Quelle somme Hervé a-t'il donné au vendeur?

S'il y en a plusieurs, on donnera la plus petite.

#HSLIDE

### Le code

```python
# x = nombre de billets de 57, inférieur à 10
# y = nombre de billets de 62, inférieur à 9
# z = nombre de billets de 72, inférieur à 8
e = set()
for x in range(0,11):
    for y in range(0,10):
        for z in range(0,9):
            s = x*57 + y*62 + z*72
            if s<600 :
                #print(x,y,z,s)
                e.add(s)
print(e)
for s in e:         # Pour chaque somme d'argent que je peux donner
    if s-4 in e:    # Le commercant peut il me rendre somme - 4 ?
        print("bingo",s,"et",s-4,"sont possibles !")
```
@[1-3](Bornes supérieures du nombre de billets de chaque type : 600/57, 600/62, etc. 
@[4](Création d'un ensemble vide)
@[5-11](Remplissage de l'ensemble des sommes d'argent qu'on peut détenir en Syldavie
@[12](Affichage de cet ensemble)
@[13-14] (Pour chacune des sommes d'argent qu'Hervé peut donner, on vérifie si le commerçant peut nous rendre cette $somme - 4$
