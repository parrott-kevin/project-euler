# Problem 33

# If the product of these four fractions is given in its lowest common terms,
# find the value of the denominator.


import fractions


def trivial(n, d):
    """ Compare the numerator, n, to the denominator, d to find non-trivial
        examples of the fraction. """
    if n > d:
        return False
    n0 = int(str(n)[0])
    n1 = int(str(n)[1])
    d0 = int(str(d)[0]) 
    d1 = int(str(d)[1])
    if n0 == 0 or n1 == 0 or d0 == 0 or d1 == 0:
        return False
    if n0 == d1 or n1 == d0:
        if n0 / d1 == n / d:
            return True
        if n1 / d0 == n / d:
            return True
    return False

# main
pool = []
n = 1
d = 1
for i in range(11, 100):
    for j in range(i + 1, 100):
        frac = str(i) + "/" + str(j)
        if trivial(i, j) and frac not in pool:
            pool.append(frac)
            n *= i
            d *= j
print(n / d, fractions.Fraction(n, d))