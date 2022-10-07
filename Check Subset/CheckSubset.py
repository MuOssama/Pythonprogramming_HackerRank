testNum = int(input())
""
for i in range(testNum):
    lenA = int(input())
    setA = set(map(int, input().split()))
    lenB = int(input())
    setB = set(map(int, input().split()))
    if(len(setA-setB) == 0):
        print(True)
    else:
        print(False)