# Problem 53

# How many, not necessarily distinct, values of nCr, for 1 <= n <= 100, are
# greater than one-million?


import math


def over(n):
    """ Determines if and how many combinations of n are over one-million. """
    count = 0
    for r in range(0, n):
        ncr = math.factorial(n) / (math.factorial(r) * math.factorial(n - r))
        if ncr > 1000000:
            count += 1
    return count


# main
answer = 0
for i in range(1, 101):
    answer += over(i)
print(answer)