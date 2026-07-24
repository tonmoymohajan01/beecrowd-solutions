
while True:
    media = []
    import sys
    while True:
        n = float(input())

        if 0 <= n <= 10:
            media.append(n)
        else:
            print("nota invalida")

        if len(media) == 2:
            print(f"media = {sum(media) / 2:.2f}")

            while True:
                print("novo calculo (1-sim 2-nao)")
                num = int(input())

                if num == 1:
                    break

                elif num == 2:
                    sys.exit()

            break