Alcool = 0
Gasolina = 0
Diesel = 0
while True:
    n = int(input())

    Alcool += n == 1
    Gasolina += n == 2
    Diesel += n == 3

    if n == 4:
        break
print(f"MUITO OBRIGADO\nAlcool: {Alcool}\nGasolina: {Gasolina}\nDiesel: {Diesel}")
