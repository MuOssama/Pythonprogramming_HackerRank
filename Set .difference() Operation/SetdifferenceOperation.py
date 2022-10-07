numA = int(input())
a = set(map(int, input().split()))
numB = int(input())
b = set(map(int, input().split()))

print(len(a.difference(b)))
