# Jupyter notebooks for learning Python

A repository of notebooks

#HSLIDE

### Un petit exercice sur les instructions conditionnelles

- Si en Python se dit "if"
- Sinon se dit "else:"
- Attention à l'indentation

#HSLIDE

### Le pitch

- une caisse de magasin
- si le montant du caddy est supérieur à x euros on fait une ristourne de y%
- sinon, c'est plein pot !

#HSLIDE

### Le code

```python
montantDuCaddy = float(input('Entrez le montant du caddy : '))

montantAPayer = montantDuCaddy
if montantDuCaddy > 90. :
    montantAPayer = montantDuCaddy * 0.9
    
print('Le montant à payer est',montantAPayer)
```
@[1](Entrée du montant du caddy)
@[3](Par défaut c'est plein pot)
@[4-5](Si le montant dépasse 90€ on fait la remise)
@[7](Affichage du prix à payer)
