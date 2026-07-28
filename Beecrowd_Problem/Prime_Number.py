t = int(input())
for i in range(t):
    x = int(input())

    count = 0
    for i in range(1, x + 1):
        if x % i == 0:
            count += 1
    print(f"{x} eh primo" if count == 2 else f"{x} nao eh primo")
