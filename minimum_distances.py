# Minimum Distances Problem Hackerrank Url
# https://www.hackerrank.com/challenges/minimum-distances/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.

arr = [3, 2, 1, 2, 3]


def minimumDistances(arr):
    min_dist = 10**5
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            # we only need the distance between 2 equal numbers
            if arr[i] == arr[j]:
                diff = abs(j-i)
                if diff < min_dist:
                    min_dist = diff
    if min_dist != 10**5:
        return min_dist
    else:
        return -1


print(minimumDistances(arr))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input())

#     a = list(map(int, input().rstrip().split()))

#     result = minimumDistances(a)

#     fptr.write(str(result) + '\n')

#     fptr.close()
