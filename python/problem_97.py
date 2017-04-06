# Problem 97

# Find the last ten digits of the prime number 28433 * 2**7830457 + 1.


def power(x,n):
    """ Computes the number, x**n. """
    result = 1
    while n > 0:
        if n % 2 != 0:
            result *= x
            n -= 1
        x *= x
        n = n // 2
    return result


# main
m = 7830457
n = m // 24
i = int(str(power(2, n))[-10:])
j = i
for count in range(1, 24):
    j = int(str(i * j)[-10:])
j = int(str(j * 56866 + 1)[-10:])
print(j)
