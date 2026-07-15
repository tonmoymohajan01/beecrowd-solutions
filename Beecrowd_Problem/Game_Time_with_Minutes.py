h1, m1, h2, m2 = map(int,input().split())

if h1 > h2 and m1 > m2:
    print(f'O JOGO DUROU {((24-h1)+h2)-1} HORA(S) E {(60-m1)+m2} MINUTO(S)')
elif h1 > h2 and m1 < m2:
    print(f'O JOGO DUROU {(24-h1)+h2} HORA(S) E {m2-m1} MINUTO(S)')
elif h1 > h2 and m1 == m2:
    print(f'O JOGO DUROU {(24-h1)+h2} HORA(S) E 0 MINUTO(S)')

elif h2 > h1  and m1 > m2:
    print(f'O JOGO DUROU {(h2-h1) -} HORA(S) E {(60-m1)+m2} MINUTO(S)')
elif h2 > h1 and m1 < m2:
    print(f'O JOGO DUROU {h2-h1} HORA(S) E {m2-m1} MINUTO(S)')
elif h2 > h1 and m1 == m2:
    print(f'O JOGO DUROU {h2-h1} HORA(S) E 0 MINUTO(S)')

elif h2 == h1 and m1 > m2:
    print(f'O JOGO DUROU 24 HORA(S) E {(60-m1)+m2} MINUTO(S)')
elif h2 == h1 and m1 < m2:
    print(f'O JOGO DUROU 24 HORA(S) E {m2-m1} MINUTO(S)')
elif h2 == h1 and m1 == m2:
    print(f'O JOGO DUROU  HORA(S) E 0 MINUTO(S)')