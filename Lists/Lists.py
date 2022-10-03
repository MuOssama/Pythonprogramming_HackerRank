CommandNumber = int(input())
Command = []
List = []
for _ in range(0,CommandNumber):
    Command = input().split()
    if Command[0] == "insert":
        List.insert(int(Command[1]),int(Command[2]))
    elif Command[0] == "append":
        List.append(int(Command[1]))
    elif Command[0] == "print":
        print(List)
    elif Command[0] == "remove":
        List.remove(int(Command[1]))
    elif Command[0] == "sort":
        List.sort()
    elif Command[0] == "pop":
        List.pop()
    elif Command[0] == "reverse":
        List.reverse()