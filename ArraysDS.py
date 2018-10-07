"""
Problem:
https://www.hackerrank.com/challenges/arrays-ds/problem
"""


def reverseArray(a):
    print(*a[::-1])

def reverseArrayForLoop(a):
    print(*[a[i] for i in range(len(a) - 1, -1, -1)])

arr_count = int(input())

arr = list(map(int, input().rstrip().split()))

reverseArrayForLoop(arr)
