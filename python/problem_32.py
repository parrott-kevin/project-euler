# Problem 32

# Find the sum of all products whose multiplicand/multiplier/product identity
# can be written as a 1 through 9 pandigital.


def divisors(n):
    """ Finds the divisors of n, then sends them to arrange then verifies. """
    for m in range(2, int(n**.5) + 1):
        if n % m == 0:
            p = int(n / m)
            if arrange(n, m, p) == "123456789":
                return True
    return False

def arrange(n, m, p):
    """ Arranges n, m, p in ascending order. """
    t = str(n) + str(m) + str(p)
    s = []
    for i in t:
        s.append(i)
    s.sort()
    r = ""
    for i in s:
        r += i
    return r


# main
ans = 0
for i in range(1000, 10000):
    if divisors(i):
        ans += i
print(ans)
