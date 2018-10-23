"""
Problem:
https://www.hackerrank.com/challenges/security-tutorial-permutations/problem
"""

n = int(input())

values = list(map(int,input().split()))

for i in values: print(values[i-1])
