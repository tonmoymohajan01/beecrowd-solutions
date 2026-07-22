c = 0 
t = 0 
for i in range(6):
    n = float(input())
    

    if n > 0:
        c+= 1 
        t+= n 

print(f'{c} valores positivos\n{t / c:.1f}')