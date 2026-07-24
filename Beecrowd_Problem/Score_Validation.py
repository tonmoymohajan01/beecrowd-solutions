media = []
while True:
    n = float(input())

    if 0 <= n <= 10:
        media.append(n)
    else:
        print("nota invalida")

    if len(media) == 2:
        print(f"media = {sum(media) / 2:.2f}")
        break
