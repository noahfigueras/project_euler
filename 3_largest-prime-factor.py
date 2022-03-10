#!/usr/bin/python

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# Author: Noah Figueras
import math 

def get_largest_prime_factor(n): 
    for x in range(3,int(math.sqrt(n))+1,2):
        while n % x == 0:
            n = n / x
            print(x)

get_largest_prime_factor(600851475143)
