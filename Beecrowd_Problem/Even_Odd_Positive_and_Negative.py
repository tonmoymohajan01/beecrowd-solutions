e = 0
o = 0 
p = 0
n = 0


for i in range(5):
    a = int(input())

    if a % 2 == 0:
        e += 1 
    else:
        o+= 1 
    if a > 0:
        p+= 1
    elif a < 0:
        n+= 1 

print(f"{e} valor(es) par(es)\n{o} valor(es) impar(es)\n{p} valor(es) positivo(s)\n{n} valor(es) negativo(s)")
        