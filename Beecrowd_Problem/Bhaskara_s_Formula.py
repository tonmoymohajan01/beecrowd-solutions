from math import*
a, b, c = map(float,input().split())

x = b**2 - 4*a*c

if x > 0 and a > 0:
    print(f"R1 = {(-b+sqrt(x))/(2*a):.5f}\nR2 = {(-b-sqrt(x))/(2*a):.5f}")
else:
    print("Impossivel calcular")