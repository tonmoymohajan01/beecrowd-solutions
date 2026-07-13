n = int(round(float(input())* 100))

print("NOTAS:")
for note in [10000, 5000, 2000, 1000, 500, 200]:
    count,n = divmod(n,note)
    print(f"{int(count)} nota(s) de R$ {note/100:.2f}")

print("MOEDAS:")
for coin in [100, 50, 25, 10, 5, 1]:
    count, n = divmod(n,coin) 
    print(f"{int(count)} moeda(s) de R$ {coin/100:.2f}")