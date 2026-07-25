while True:
    x = int(input())

    if x == 0:
        break

    print(*range(1, x + 1))
