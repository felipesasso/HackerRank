"""
Problem:
https://www.hackerrank.com/challenges/security-bijective-functions/problem
"""

n = int(input())

array = list(map(int, input().split()))

print("YES" if len(array) == len(set(array)) else "NO")
