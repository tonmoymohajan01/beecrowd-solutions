x = int(input())
y = int(input())

for i in range(min(x, y) + 1, max(x, y)):
    if i % 5 in (2, 3):
        print(i)
