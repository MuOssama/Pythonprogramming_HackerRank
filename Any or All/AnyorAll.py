# Enter your code here. Read input from STDIN. Print output to STDOUT
nums = int(input())
numlist = input().split()
if (all(int(i)>0 for i in numlist)) and (any(i == i[::-1] for i in numlist)):
        print(True)
else:
    print(False)