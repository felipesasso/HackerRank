"""
Problem:
https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
"""

from collections import OrderedDict

ordered_dictionary = OrderedDict()

N = int(input())

for i in range(N):
    item_name, space, net_price = input().rpartition(' ')
    ordered_dictionary[item_name] = ordered_dictionary.get(item_name, 0) + int(net_price) 
    
for item, price in ordered_dictionary.items():
    print(item , price)
