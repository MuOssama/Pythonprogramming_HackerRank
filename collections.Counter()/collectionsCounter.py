x = int(input())
l = list(map(int,input().split()))

n = int(input())
money = 0
for _ in range(n):
    a, b = tuple(map(int,input().split()))
    if a in l:
        money += b
        l.remove(a)
print(money)