# Roua Almulhem
# Pizza calculator

Smallpizza = int(input('Hoeveel Small pizzas wil u?'))
SmallPrijs = int(7)
Mediumpizza = int(input('Hoeveel Medium pizzas wil u?'))
MediumPrijs = int(10)
Largepizza = int(input('Hoeveel Large pizzas wil u?'))
LargePrijs = int(15)

TotalPrijs = int((Smallpizza*SmallPrijs)+(Mediumpizza*MediumPrijs)+(Largepizza+LargePrijs))

print('U heeft',Smallpizza,'Small,',Mediumpizza,'Medium en',Largepizza,'Large pizzas besteld. Dit kost in totaal',TotalPrijs,'euro')