_,quantity1,price1 = input().split()
_,quantity2,price2 = input().split()

result = int(quantity1) * float(price1) + int(quantity2) * float(price2)

print(f'VALOR A PAGAR: R$ {result:.2f}')