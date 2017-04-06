# Problem 41

# What is the largest pandigital prime that exists?


import itertools


def prime(n):
    """ Checks for primality. """
    m = int(n**.5)
    for i in range(2, m + 1):
        if n % i == 0 and n != i:
            return False
    return True


answer = 1
n = 7
ans = list(itertools.permutations(range(1,n + 1),n))
for i in ans:
    k = ""
    for j in i:
        k += str(j)
    k = int(k)
    if prime(k) and k > answer:
        answer = k
print(answer)
