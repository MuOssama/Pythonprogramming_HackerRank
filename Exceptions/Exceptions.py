# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

for i in range(n):
    inputs = input().split()
    try:
        print(int(int(inputs[0])/int(inputs[1])))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:",e)
        
