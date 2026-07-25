n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    total = 0
    for i in range(min(a, b) + 1, max(a, b)):
        if i % 2 != 0:
            total += i
    print(total)
