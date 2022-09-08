#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s): 
    s2 = ""
    flag = True
    for i in range(0,len(s)):
        if s[i-1] == " ":
            flag = True
        if flag == True:
            s2 += s[i].upper()
            flag = False
        else:
            s2 += s[i]
    return s2


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
