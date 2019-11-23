#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def repeatedString(s, n):
    count = 0
    while len(s) < n: s *= 2
    for x in s[:n]:
        if x == 'a':
            count += 1
    return count

print(repeatedString('a', 20))
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input())

#     ar = list(map(int, input().rstrip().split()))

#     result = sockMerchant(n, ar)

#     fptr.write(str(result) + '\n')

#     fptr.close()
