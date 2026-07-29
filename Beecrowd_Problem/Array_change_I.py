arr = []
for i in range(20):
    x = int(input())
    arr.append(x)
for j in range(19, -1, -1):
    print(f"N[{19 - j}] = {arr[j]}")
