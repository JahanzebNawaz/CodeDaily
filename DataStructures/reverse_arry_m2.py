#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def reverseArray(arr, ar_length):
    # Write your code here
    reverse_list = []
    for x in range(0, len(arr)):
        reverse_list.append(arr[(ar_length - 1) - x])
    return reverse_list


if __name__ == '__main__':
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr, arr_count)
    res_str = ' '.join(map(str, res))
    print(res_str)
