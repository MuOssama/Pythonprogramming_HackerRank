def print_formatted(number):
    # your code goes here
    x=len(str(bin(number))[2:])

    for i in range(1,number+1):
        print(str(i).rjust(x),str(oct(i))[2:].rjust(x),str(hex(i))[2:].rjust(x).upper(),str(bin(i))[2:].rjust(x))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)