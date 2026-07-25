grenais = 0
inte = 0
gre = 0
emp = 0

while True:
    inter, gremio = map(int, input().split())
    grenais += 1
    goal = int(input())

    if inter > gremio:
        inte += 1
    elif inter < gremio:
        gre += 1
    elif inter == gremio:
        emp += 1

    if goal != 1:
        break

print(("Novo grenal (1-sim 2-nao)\n") * grenais, end="")
print(grenais, "grenais")
print(f"Inter:{inte}\nGremio:{gre}\nEmpates:{emp}")

if inte == gre:
    print("Não houve vencedor")
elif inte > gre:
    print("Inter venceu mais")
else:
    print("Gremio venceu mais")
