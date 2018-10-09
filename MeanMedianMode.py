from math import ceil
from collections import Counter, OrderedDict

import numpy as np
from scipy import stats

#Using numpy and stat
def calculateMeanMedianModeNpStat(numbers):
    print(np.mean(numbers))
    print(np.median(numbers))
    print(stats.mode(numbers))

def calculateMeanMedianMode(numbers):
    
    class OrderedCounter(Counter, OrderedDict):
        pass
    
    mean = sum(numbers) / N

    numbers = sorted(numbers)

    median = numbers[(len(numbers)//2) + 1] if len(numbers) % 2 == 1 else (numbers[len(numbers)//2] + numbers[(len(numbers))//2 - 1]) / 2

    mode = OrderedCounter(numbers).most_common(1)[0][0]

    print(mean)
    print(median)
    print(mode)

N = int(input())

numbers = list(map(int, input().split()))

calculateMeanMedianMode(numbers)

