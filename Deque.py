"""
Problem:
https://www.hackerrank.com/challenges/py-collections-deque/problem
"""



from collections import deque

N = int(input())
d = deque()

for i in range(N):
    operation, *args = input().split()
    getattr(d, operation)(*args)
    
print(' '.join(d))
