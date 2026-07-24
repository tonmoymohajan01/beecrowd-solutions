for i in range(3):
    a, b = map(int, input().split())

    if a <= 0 or b <= 0:
        print("0")
    else:
        s = min(a, b)
        e = max(a, b) + 1
        total = 0
        for i in range(s, e):
            total += i
            print(i, end=" ")
        print(f"Sum={total}")
