a, b, c = map(float,input().split())
print(f"Perimetro = {a+b+c:.1f}" if(a+b)>c and (b+c)>a and (c+a)>b else f'Area = {0.5 * ((a+b) * c):.1f}' )
