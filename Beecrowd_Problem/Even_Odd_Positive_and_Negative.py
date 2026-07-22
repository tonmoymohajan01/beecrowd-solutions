e = o = p = m = 0 


for _ in range(5):
  n = int(input())

  e += n % 2 == 0 
  o += n % 2 != 0 
  p += n > 0 
  m += n < 0 

print(f"{e} valor(es) par(es)\n{o} valor(es) impar(es)\n{p} valor(es) positivo(s)\n{m} valor(es) negativo(s)")

        