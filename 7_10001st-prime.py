# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13
# What is the 10 001st prime number?

def prime_num(x):
    count = 1
    prime = 2
    n = 1
    while count < x:
        if is_prime(n): 
            count+=1
            prime=n
        n+=2
    return prime
         
def is_prime(n):
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

result = prime_num(10001)
print(result)


