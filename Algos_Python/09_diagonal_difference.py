import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    n = len(arr)
    if n == 0:
        return 0
    l = sum(int(arr[i][i]) for i in range(n))
    r = sum(int(arr[i][n-i-1]) for i in range(n))
    return abs(l-r)

n_matrix = int(input("Input # of rows and columns in the matrix: "))
arr = [list(map(int, input("Input matrix row: ").split())) for _ in range(n_matrix)]
# print(arr)
print(diagonalDifference(arr))