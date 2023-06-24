#!/bin/python3


#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    container = {}
    for i, el in enumerate(ar):
        if el in container:
            container[el] += 1
        else:
            container[el] = 1
         
    total = 0
    for key in container:
        count = container[key] // 2 
        if count >= 1:
            # print(key, container[key], count) 
            total += count

    return total

n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

sockMerchant(n, ar)