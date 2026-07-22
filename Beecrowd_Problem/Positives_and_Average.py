res = []
for i in range(6):
    n = float(input())
    

    if n > 0:
        res.append(n)

print(f'{len(res)} valores positivos\n{sum(res)/len(res):.1f}')