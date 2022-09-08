HasNum = False
HasChar = False
HasDigit = False
HasLower = False
HasUpper = False
s = input()


for i in range(0,len(s)):
    if (s[i].isalnum()):
        HasNum = True
    if (s[i].isalpha()):
        HasChar = True
    if (s[i].islower()):
        HasLower = True
    if (s[i].isupper()):
        HasUpper = True     
    if (s[i].isdigit()):
        HasDigit = True       

    
print(HasNum)
print(HasChar)
print(HasDigit)
print(HasLower)
print(HasUpper)

    