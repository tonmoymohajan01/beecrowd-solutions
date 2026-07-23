for i in range(11):
    d = round(i * 0.2, 1)
    for j in range(1, 4):
        n = j + d
        print(f"I={int(d) if d == int(d) else d} J={int(n) if n == int(n) else n}")
