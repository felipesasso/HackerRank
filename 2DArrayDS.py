"""
Problem:
https://www.hackerrank.com/challenges/2d-array/problem
"""

def hourglassSum(arr):

    result = -9999
    for n in range(1, 5, 1):
        for m in range(1, 5, 1):
            result = max(
                result, 
                sum([arr[n-1][m-1],
                 arr[n-1][m],
                 arr[n-1][m+1],
                 arr[n][m],
                 arr[n+1][m-1],
                 arr[n+1][m],
                arr[n+1][m+1]
                ]))
    return result
            
arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

print(hourglassSum(arr))
