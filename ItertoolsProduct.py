"""
Problem:
https://www.hackerrank.com/challenges/itertools-product/problem
"""

from itertools import product

A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))

print(*list(product(A,B)))
