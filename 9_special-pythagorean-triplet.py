# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
import random

def main(): 
    res = 0
    a = 0
    b = 0
    c = 0
    while res != 1000: 
        c = random.randint(1,500)
        b = random.randint(1,c)
        a = random.randint(1,b)
        res = calc(a, b, c) 
    print(a, b, c)
    
def calc(a, b, c):
    if a**2 + b**2 == c**2:
        return a+b+c
    
main()

