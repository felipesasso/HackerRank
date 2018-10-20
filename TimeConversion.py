"""
Problem:
https://www.hackerrank.com/challenges/time-conversion/problem
"""

from datetime import datetime

import os

def timeConversion(s):
    a = datetime.strptime(s, '%I:%M:%S%p')
    
    return "%02d:%02d:%02d" % (a.hour, a.minute, a.second)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
