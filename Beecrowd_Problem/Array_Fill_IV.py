even = []
odd = []
for i in range(15):
    n = int(input())

    if n % 2 == 0:
        even.append(n)
        if len(even) == 5:
            for i in range(5):
                print(f"par[{i}] = {even[i]}")
            even.clear()
    else:
        odd.append(n)
        if len(odd) == 5:
            for j in range(5):
                print(f"impar[{j}] = {odd[j]}")
            odd.clear()

for j in range(len(odd)):
    print(f"impar[{j}] = {odd[j]}")

for i in range(len(even)):
    print(f"par[{i}] = {even[i]}")
