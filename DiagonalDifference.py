"""
Problem:
https://www.hackerrank.com/challenges/diagonal-difference/problem
"""

import os

def diagonalDifference(arr, n):
    
    primary = 0
    secondary = 0
    
    l = n - 1
    
    for i in range(n):
        primary += arr[i][i]
        secondary += arr[l][i]
        l -= 1
    
    return abs(primary - secondary)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr, n)
    fptr.write(str(result) + '\n')

    fptr.close()
