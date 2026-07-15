h1, m1, h2, m2 = map(int, input().split())

start = h1 * 60 + m1
end = h2 * 60 + m2

if start >= end:
    end += 24 * 60

duration = end - start

hour = duration // 60
minute = duration % 60

print(f"O JOGO DUROU {hour} HORA(S) E {minute} MINUTO(S)")