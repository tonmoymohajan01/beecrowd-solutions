N = int(input())
print(N)
for note in [100,50,20,10,5,2,1]:
    count = N // note
    N %= note
    print(f"{count} nota(s) de R$ {note},00")
    

