l = int(input())
t = input().upper()
total = 0
arr = [[None] * 12 for _ in range(12)]

for i in range(12):
    for j in range(12):
        arr[i][j] = float(input())

for j in range(12):
    total += arr[l][j]

if t == "S":
    print(f"{total:.1f}")
elif t == "M":
    print(f"{total / 12:.1f}")
