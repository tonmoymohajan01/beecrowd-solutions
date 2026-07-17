_, day1 = input().split()
h1, m1, s1 = map(int,input().replace(":"," ").split())

_, day2 = input().split()
h2, m2, s2 = map(int,input().replace(":"," ").split())


st = int(day1) * 86400 + h1 * 3600 + m1 * 60 + s1
en = int(day2) * 86400 + h2 * 3600 + m2 * 60 + s2 



duration = en - st 

print(f'{duration // 86400} dia(s)\n{(duration % 86400) // 3600} hora(s)\n{(duration%3600)//60} minuto(s)\n{duration%60} segundo(s)')