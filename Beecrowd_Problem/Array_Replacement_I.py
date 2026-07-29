for i in range(10):
    x = int(input())
    arr = [None] * 10
    if x <= 0:
        arr[i] = 1
    else:
        arr[i] = x
    print(f"X{[i]} = {arr[i]}")
