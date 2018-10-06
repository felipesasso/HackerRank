"""
Problem:
https://www.hackerrank.com/challenges/piling-up/problem
"""


T = int(input())

for _ in range(T):
    n = int(input())
    
    top_item = 0
    
    cubes = list(map(int, input().split()))
    
    for i in range(n):
        left, right = cubes[0], cubes[len(cubes) - 1]
        
        if(i == 0):
            top_item = cubes.pop(0) if left >= right else cubes.pop()

        else:
            if(left >= right):
                if(top_item < left):
                    print("No")
                    break;
                else: 
                    top_item = cubes.pop(0)
            else:
                if(top_item < right):
                    print("No")
                    break;
                else:
                    top_item = cubes.pop()
    else:
        print("Yes")
                        
