n = int(input())

result = [1, 2, 3]

for i in range(n):
    print(*result, "PUM")
    result = [x + 4 for x in result]
