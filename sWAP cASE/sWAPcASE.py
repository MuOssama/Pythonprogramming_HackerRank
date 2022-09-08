def swap_case(s):
    s2 = ""
    for i in range(0,len(s)):
        if(s[i].islower()):
            s2 += (s[i].upper())
        elif(s[i].isupper()):
            s2 += (s[i].lower())
        else:
            if(s[i] == " "):
                 s2 += (" ")
            else:
                 s2 += (s[i])
        
            
    return s2

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)