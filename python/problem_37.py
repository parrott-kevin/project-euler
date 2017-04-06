# Problem 37

# Find the sum of the only eleven primes that are both truncatable from left to
# right and right to left.


PRIMES = [2]


def prime(n):
    """ Checks for primality. """
    m = int(n**.5)
    for i in range(2, m + 1):
        if n % i == 0 and n != i:
            return False
    return True


def truncate(n):
    """ Truncate a number from left to right and vice versa"""
    if n < 11:
        return False
    m = str(n)
    for i in range(1, len(m)):
        j = int(m[i:len(m)])
        k = int(m[:i])
        if j not in PRIMES or k not in PRIMES:
            return False
    return True


# main
answer = []
i = 3
while len(answer) <= 10:
    if prime(i):
        PRIMES.append(i)
        if truncate(i):
            answer.append(i)
    i += 2
print(answer, sum(answer))