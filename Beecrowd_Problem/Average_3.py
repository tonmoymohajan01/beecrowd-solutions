n1, n2, n3, n4 = map(float,input().split())

result = (n1*2 + n2*3 + n3*4 + n4*1)/10
print(f'Media: {result:.1f}')

if result > 7:
    print("Aluno aprovado.")
elif result < 5:
    print('Aluno reprovado.')
elif 5 <= result <= 6.9:
    print("Aluno em exame.")

    n5 = float(input())
    print(f'Nota do exame: {n5}')

    sum = (result + n5)/2 

    if sum >= 5.0:
        print("Aluno aprovado.")
    elif sum <= 4.9:
        print("Aluno reprovado.")
    
    print(f"Media final: {sum:.1f}")