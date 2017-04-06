# Problem 5

# What is the smallest positive number that is evenly divisible by all
# of the numbers from 1 to 20?


PRIME = [2, 3, 5, 7, 11, 13, 17, 19]

def factor_prime(n):
    """ Finds the prime factor of n. """
    factors = []
    if n not in PRIME and n != 1:
        i = 0
        while n != 1:
            if n % PRIME[i] == 0:
                factors.append(PRIME[i])
                n = n/PRIME[i]
            else:
                i += 1
    else:
        factors.append(n)
    return factors


# main
fact_prime = []
for i in range(1, 21, 1):
    fact_prime.append(factor_prime(i))

i = 0
sq_fact = [0, 0, 0, 0, 0, 0, 0, 0]
while i <= len(fact_prime)-1:
    j = 0
    current_set = fact_prime[i]
    while j <= len(current_set)-1:
        k = 0
        if current_set[j] != 1:
            while k <= len(PRIME)-1:
                power = current_set.count(PRIME[k])
                if sq_fact[k] < PRIME[k] ** power:
                    sq_fact[k] = PRIME[k] ** power
                k += 1
        j += 1
    i += 1

answer = 1
for i in sq_fact:
    answer *= i

print(fact_prime)
print(answer)
