a, b, c, d = map(int,input().split())
print("Valores aceitos" if b>c and d>a and (c+d)>(a+b) and 0<c and 0<d and a%2 == 0 else "Valores nao aceitos")