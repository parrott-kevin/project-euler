# Problem 21

# Find and sum all amicable numbers below 10000.


import math


def amicable(m):
    """ Returns possible amicable number. """
    sqrt_m = math.floor(math.sqrt(m))
    divisors = [1]
    for i in range(2, sqrt_m + 1):
        if m % i == 0:
            divisors.append(i)
            divisors.append(m / i)
    return sum(divisors)


def pair(n, found):
    """ Check if amicable(m) is a amicable pair. """
    m = amicable(n)
    p = amicable(amicable(n))
    if n == p and n != m and m not in found:
        return True
    else:
        return False
    

# main    
pairs = []    
for i in range(1, 10000):
    if pair(i, pairs):
        pairs.extend([i, amicable(i)])

print(pairs, sum(pairs))
