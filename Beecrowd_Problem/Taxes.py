n = float(input())

if 0 <= n <= 2000:
    print("Isento")
elif 2000 < n <= 3000:
    print(f'R$ {(n - 2000) * 8/100:.2f}')
elif 3000 < n <= 4500:
    print(f'R$ {80 + (n - 3000) * 18/100:.2f}')
else:
    print(f"R$ {350 + (n - 4500) * 28/100:.2f}")
  