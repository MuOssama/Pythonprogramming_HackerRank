# Enter your code here. Read input from STDIN. Print output to STDOUT
dimentions = list(map(int,input().split()))
p1 = ".|."
p2 = "WELCOME"
string = p1
#Upper part
for i in range (1,int((dimentions[0]+1)/2)):
    print(string.center(dimentions[1],'-'))
    string += (2*p1)
    

#Center part
print(p2.center(dimentions[1],'-'))

#Lower part
for i in range(1,int(dimentions[0]+1)//2):
    string = p1 * (dimentions[0]-(i*2))
    print(string.center(dimentions[1],'-'))
