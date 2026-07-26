n = int(input())

a, b = 0, 1

arr = []
for i in range(n):
    arr.append(a)
    a, b = b, a + b
    
print(*arr, sep=" ")
