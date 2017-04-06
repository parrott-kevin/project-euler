# Problem 3

# What is the largest prime factor of the number 600851475143?


def prime_factor(n):
    """ Finds the prime factors of n. """
    factors = []
    i = 2
    j = 0
    if n == 1:
        factors.append(n)
    else:
        while n != 1:
            if n % i == 0:
                factors.append(i)
                n = n / i
            else:
                i += 1
    return factors

# main
i = 600851475143

prime_fact = prime_factor(i)

i = 0
for j in prime_fact:
    if i < j:
        i = j

print(i)
        
    
