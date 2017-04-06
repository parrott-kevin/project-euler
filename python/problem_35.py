# Problem 35

# How many circular primes are there below one million?

import itertools
import time


CONTENTS = [1, 3, 7, 9]


def prime(n):
    """ Checks for primality. """
    m = int(n**.5)
    for i in range(2, m + 1):
        if n % i == 0 and n != i:
            return False
    return True


def circular_prime(n):
    """ Determines if all circular rotations of n are prime. """
    m = str(n)
    for i in range(0, len(m)):
        if int(m[i]) not in CONTENTS:
            return False
    if prime(n):
        i = 0
        while i < len(m) - 1:
            j = m[0]
            m = m[1:]
            m = m + j
            if not prime(int(m)):
                return False
            i += 1
        return True


# main
start = time.time()
circle = [2, 3, 5, 7]
for i in range(11, 1000000, 2):
    if circular_prime(i):
        circle.append(i)
print(len(circle), time.time() - start)        