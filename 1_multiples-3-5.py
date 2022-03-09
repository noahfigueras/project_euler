#!/usr/bin/python

# Find the sum of all the multiples of 3 or 5 below 1000.
# Author: Noah Figueras

def main(num):
    _sum = 0
    for i in range(num):
        if i % 3 == 0 or i % 5 == 0:
            _sum+= i
    return _sum

result = main(1000)

print(result)
    
