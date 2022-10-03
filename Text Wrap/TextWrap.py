import textwrap

def wrap(string, max_width):
    i = 0
    new_str = ""
    while(i<len(string)):
        if(i==0):
            new_str += string[i]
        elif((i+1) % (max_width) == 0):
            new_str += string[i]
            new_str += '\n'
        else:
            new_str += string[i]
        i += 1
    return new_str

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)