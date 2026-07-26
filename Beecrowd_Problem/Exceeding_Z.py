a = int(input())
z = int(input())

while a >= z:
    z = int(input())
    total = 0
    count = 0

    for i in range(a, z):
        count += 1
        total += i
        if total >= z:
            break
print(count)
