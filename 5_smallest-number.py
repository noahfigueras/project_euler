# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Author: Noah Figueras

def smallest_multiple():
    i = 2000
    found = False
    while not found:
        counter = 0
        for x in range(1,21):
            if i % x == 0:
                counter+=1
            else:
                break 
        if counter == 20:
            found = True
            print("Found:", i)
        i+=1

smallest_multiple()
