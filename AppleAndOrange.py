"""
Problem:
https://www.hackerrank.com/challenges/apple-and-orange/
"""

def countApplesAndOranges2(s, t, a, b, apples, oranges):
    
    apples_house = 0
    oranges_house = 0
    
    for i in apples:
        if(s <= (a + i) <= t):
            apples_house += 1

    for i in oranges:
        if(s <= (b + i) <= t):
            oranges_house += 1
    
    print(apples_house)
    print(oranges_house)
    
def countApplesAndOranges(s, t, a, b, apples, oranges):
    
    print(sum([1 for i in apples if s <= (a + i) <= t]))
    print(sum([1 for i in oranges if s <= (b + i) <= t]))

if __name__ == '__main__':
    s, t = list(map(int, input().split()))

    a, b = list(map(int, input().split()))

    m, n = list(map(int, input().split()))

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
