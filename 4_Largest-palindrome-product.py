#!/usr/bin/python

# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

# Author: Noah Figueras

def isPalindrome(num):
    string = str(num)
    return string == string[::-1]

def main():
    result = 0
    for i in range( 100, 999, 1):
        for x in range(100, 999, 1):
            mul = i * x
            if isPalindrome(mul):
                if mul > result:
                    result = mul
    print(result)

main()
