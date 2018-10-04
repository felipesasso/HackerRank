"""
Problem:
https://www.hackerrank.com/challenges/word-order/problem
"""

from collections import OrderedDict

N = int(input())

ord_dict = OrderedDict()

for _ in range(N):
    word = input()
    ord_dict[word] = ord_dict.get(word, 0) + 1

print(len(ord_dict))

for i in ord_dict.values():
    print(i, end=" ")
