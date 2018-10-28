"""
Problem:
https://www.hackerrank.com/challenges/30-binary-numbers/problem
"""

if __name__ == '__main__':
    str_number = str(bin(int(input())))
    
    print(max(list(map(lambda x: x.count('1'), str_number.split('0') ))))
