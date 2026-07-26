values = list(map(int, input().split()))

a = values[0]

for x in values[1:]:
    if x > 0:
        n = x
        break
print(sum(range(a, a + n)))
