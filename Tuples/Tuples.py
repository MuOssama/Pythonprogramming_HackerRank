if __name__ == '__main__':
    n = int(input())
    tup = tuple(map(int,input().split()))
    print(hash(tup))
