#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    n = len(a)
    count = 0
    for i in range (n):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                count = count + 1
    print("Array is sorted in %d swaps."%count)
    print("First Element: %d"%a[0])
    print("Last Element: %d"%a[n-1])

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    
    countSwaps(a)
