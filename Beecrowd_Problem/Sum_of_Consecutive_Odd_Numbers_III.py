n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    total = 0
    count = 0

    while count < y:
        if x % 2 != 0:
            total += x
            count += 1
        x += 1
    print(total)
