"""
Problem:
https://www.hackerrank.com/challenges/sparse-arrays/problem
"""

def matchingStrings(strings, queries):

    for q in range(len(queries)):
        count = 0
        for s in strings:
              if s == queries[q]: count += 1
        queries[q] = count
    
    return queries


strings_count = int(input())
strings = []

for _ in range(strings_count):
    strings.append(input())

    
queries_count = int(input())
queries = []

for _ in range(queries_count):
    queries.append(input())

res = matchingStrings(strings, queries)

for i in res:
    print(i)
