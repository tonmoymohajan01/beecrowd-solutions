num = int(input())
Coelho = Rato = Sapo = total = 0 

for _ in range(num):
    n, ch = input().split()
    n = int(n)

    total+= n 

    if ch == 'C':
        Coelho+= n 
    elif ch == 'R':
        Rato+= n 
    elif ch == 'S':
        Sapo+= n 

print(f'Total: {total} cobaias\nTotal de coelhos: {Coelho}\nTotal de ratos: {Rato}\nTotal de sapos: {Sapo}\nPercentual de coelhos: {(Coelho/total)*100:.2f} %\nPercentual de ratos: {(Rato/total)*100:.2f} %\nPercentual de sapos: {(Sapo/total)*100:.2f} %')




    