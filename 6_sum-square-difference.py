# Author: Noah Figueras

# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

def sum_squares(n):
    total = 0
    for x in range(n+1):
        total += x**2
    return total 

def square_sum(n):
    total = 0
    for x in range(n+1):
        total += x
    return total**2

inpt = 100
result = square_sum(inpt) - sum_squares(inpt)
print(result)
