"""
Problem:
https://www.hackerrank.com/challenges/s10-quartiles/problem
"""

def getQuartiles(x):
    
    size = len(x)
    quartile = 0

    if(size % 2 == 0):
        quartile = (x[size//2] + x[(size//2) - 1]) // 2
    else:
        quartile = x[size//2]

    return quartile    

n = int(input())

x = sorted(list(map(int, input().split())))

size = len(x)

print(getQuartiles(x[0:size//2]))
print(getQuartiles(x))
print(getQuartiles(x[size//2 + (0 if size % 2 == 0 else 1) : size + 1]))
