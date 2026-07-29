x = int(input())
arr = [None] * 10
for i in range(10):
    arr[i] = x
    x += x
    print(f"N{[i]} = {arr[i]}")
