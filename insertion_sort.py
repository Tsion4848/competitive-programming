#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    ind = n - 2
    t = arr[-1]
    
    while (t < arr[ind]) and (ind >= 0):
        arr[ind + 1] = arr[ind]
        print(*arr)
        ind -= 1
        
    arr[ind + 1] = t
    print(*arr)
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
