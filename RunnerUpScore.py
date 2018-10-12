"""
Problem:
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
"""


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    highest = -100
    runnerup = -100
    
    for item in arr:
        if item > highest:

            runnerup = highest
            highest = item
        
        elif item > runnerup and item != highest:
            runnerup = item

        
    print(runnerup)
