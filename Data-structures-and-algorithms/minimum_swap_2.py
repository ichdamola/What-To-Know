#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    print('arr: ', arr)
    temp = [0] * (len(arr) + 1)
    for pos, val in enumerate(arr):
        print('t1:', temp)
        temp[val] = pos
        print('t2:', temp)
        pos += 1
    swaps = 0
    for i in range(len(arr)):
        if arr[i] != i+1:
            swaps += 1
            t = arr[i]
            arr[i] = i+1
            arr[temp[i+1]] = t
            temp[t] = temp[i+1]
    return swaps



arr = [4,3,1,2]
print (minimumSwaps(arr))