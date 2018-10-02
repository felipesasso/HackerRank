"""
Problem:
https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

"""

from collections import namedtuple

N = int(input())

Marks = namedtuple('Marks', input())

sum_of_all_marks = 0

for i in range(N): sum_of_all_marks += int(Marks._make(input().split()).MARKS)

print(sum_of_all_marks/N)

