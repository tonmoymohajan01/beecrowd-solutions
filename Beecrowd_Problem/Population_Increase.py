n = int(input())
for i in range(n):
    pa, pb, g1, g2 = input().split()
    pa = int(pa)
    pb = int(pb)
    g1 = float(g1)
    g2 = float(g2)

    count = 0

    while pa <= pb:
        pa += int(pa * (g1 / 100))
        pb += int(pb * (g2 / 100))
        count += 1

        if count > 100:
            break

    print("Mais de 1 seculo." if count > 100 else f"{count} anos.")
