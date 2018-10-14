"""
Problem:
https://www.hackerrank.com/challenges/swap-case/problem
"""

def swap_case(s):
    return ''.join([i.upper() if i.islower() else i.lower() for i in s])
