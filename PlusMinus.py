"""
Problem:
https://www.hackerrank.com/challenges/plus-minus/
"""

def plusMinus(arr):
    size = len(arr)
    print("{:.6f}".format(len(list(filter(lambda x:x > 0, arr)))/size))
    print("{:.6f}".format(len(list(filter(lambda x:x < 0, arr)))/size))
    print("{:.6f}".format(len(list(filter(lambda x:x == 0, arr)))/size))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
