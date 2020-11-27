# challenge hackerrank url
# https://www.hackerrank.com/challenges/repeated-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.


def repeatedString(s, n):

    # finding the total no. of a's in the string s
    a_in_s = s.count('a')

    # length of string s
    s_len = len(s)
    # if n is divisible by the length of string s
    if n % s_len == 0:
        total_as = a_in_s * (n/s_len)
        return int(total_as)
    # if n is not divisible by the length of string s
    elif n % s_len != 0:
        total_as_1 = a_in_s * (n//s_len)
        # now to calculate the no. of a's in the remaining string
        rem = n % s_len
        total_as_1 += s[:rem].count('a')
        return total_as_1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
