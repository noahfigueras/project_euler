#!/usr/bin/python

# By considering the terms in the Fibonacci sequence whose values do not 
# exceed four million, find the sum of the even-valued terms.

# Author: Noah Figueras

def main():
    _sum = 0 
    i = 1
    prev= 1
    while i <= 4000000: 
        if i % 2 == 0:
            _sum += i
        s = i
        i += prev
        prev=s
    return _sum
    
result = main()
print(result)

