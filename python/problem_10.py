# Problem 10

# Find the sum of all the primes below two million.


import math

def check_prime(n):
    """ Check if n is a prime number. """
    j = math.floor(math.sqrt(n))

    prime = True
    for k in range(3, j+1, 1):
        if n % k == 0:
            prime = False
            break
    return prime


primes = [2]
for i in range(3, 2000000, 2):
    if check_prime(i):
        primes.append(i)

print(sum(primes))
