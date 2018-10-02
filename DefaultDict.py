"""
Problem:
https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

Sample Input:

5 2
a
a
b
a
b
a
b

"""



from collections import defaultdict

N, M = map(int, input().split())

A = defaultdict(list)
B = defaultdict(list)

for i in range(N):
    val = input()
    A[i + 1].append(val)

for i in range(M):
    val = input()
    B[i + 1].append(val)
    
    flag = 0
    
    for j in range(len(A)):

        if(A[j + 1] == B[i + 1]):
            print(j + 1, end=" ")
            flag = 1
    
    if(flag == 0):
        print(-1, end=" ")
    
    
    print("")


