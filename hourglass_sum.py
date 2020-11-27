# Hackerrank problem url
# https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

#!/bin/python3

import math
import os
import random
import re
import sys

arr = [[-9, -9, -9, 1, 1, 1],
       [0, -9, 0, 4, 3, 2],
       [-9, -9, -9, 1, 2, 3],
       [0, 0, 8, 6, 6, 0],
       [0, 0, 0, -2, 0, 0],
       [0, 0, 1, 2, 4, 0]]

# Complete the hourglassSum function below.


def hourglassSum(arr):
    final_sum = -10*9
    n = len(arr)
    for i in range(n-2):
        for j in range(n-2):
            # sum of 1 hour glass
            h_sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i +
                                                                1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            if h_sum > final_sum:
                final_sum = h_sum
    return final_sum


print(hourglassSum(arr))
