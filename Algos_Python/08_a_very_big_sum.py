#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#



def aVeryBigSum(ar):
    # Write your code here
    sum = 0
    for n in ar:
        sum += n
    return sum

print(aVeryBigSum([100001, 100002, 100003, 100004, 100005]))