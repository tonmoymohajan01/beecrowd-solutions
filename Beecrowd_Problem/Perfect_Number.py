t = int(input())
for i in range(t):
    x = int(input())

    total = 0
    for i in range(1, x):
        if x % i == 0:
            total += i

    print(f"{x} eh perfeito" if total == x else f"{x} nao eh perfeito")
