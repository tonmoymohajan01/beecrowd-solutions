x = int(input())
y = int(input())

print(sum(i for i in range(min(x,y)+1, max(x,y)) if i % 2 != 0 ))