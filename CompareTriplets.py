"""
Problem:
https://www.hackerrank.com/challenges/compare-the-triplets/problem
"""

def compareTriplets(a, b):
    
    c = [0, 0]

    for x, y in zip(a, b):
        if(x != y):
            c[0 if x > y else 1] += 1
            
    return c
         
a = list(map(int, input().rstrip().split()))

b = list(map(int, input().rstrip().split()))

print(' '.join(map(str, compareTriplets(a, b))))
