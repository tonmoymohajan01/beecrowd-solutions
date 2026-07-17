n = float(input())

if n <= 400:
    p = 15
elif n <= 800:
    p = 12
elif n <= 1200:
    p = 10
elif n <= 2000:
    p = 7
else:
    p = 4

increase = n * p / 100
new_salary = n + increase


print(f'Novo salario: {new_salary:.2f}')
print(f'Reajuste ganho: {increase:.2f}')
print(f"Em percentual: {p} %")