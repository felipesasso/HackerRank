"""
Problem:
https://www.hackerrank.com/challenges/input/problem
"""

x, k = list(map(int, input().split()))
print(True if eval(input().replace('x', str(x))) == k else False)
